package com.woodrad.cyber

import org.apache.spark.rdd.RDD
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.hadoop.io.compress.GzipCodec
import org.apache.spark.mllib.linalg.{Vector, Vectors}
import org.apache.spark.mllib.stat.{MultivariateStatisticalSummary, Statistics}

/** Object for modeling LANL Cyber-Security event data. */
object LanlModel {
  def main(args: Array[String]) {
    val master = args.length match {
      case x: Int if x > 0 => args(0)
      case _ => "local"
    }

    val conf = new SparkConf().setAppName("LANL Cyber").setMaster(master)
    val sc = new SparkContext(conf)

    val proc = sc.textFile("data/proc.txt.gz")
    val parsedProc = proc.map(line => line.split(','))

    // Map process data onto unique 3-tuples of (user, computer, process).
    val simpleProc: RDD[(String, String, String)] = parsedProc.map {
      key => (key(1), key(2), key(3))
    }.distinct()
    // Make a count of how how frequently users run processes and sort by most frequent.
    val procCnt = simpleProc.map(tup => (tup._3, 1))
      .reduceByKey((proc, cnt) => proc + cnt)
      .sortBy {case (proc, cnt) => -cnt}
      .map { case (key, value) => Array(key, value).mkString(",") }
    procCnt.saveAsTextFile("reports/procCount", classOf[GzipCodec])
  }
}
