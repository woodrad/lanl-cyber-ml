#! /usr/bin/env python3
"""Convenience objects and methods for working with LANL's Cyber-Security Event data."""

from urllib.parse import urlparse
from urllib.request import urlretrieve
from posixpath import basename
from os.path import isfile
from gzip import open
from matplotlib.mlab import csv2rec
import matplotlib.pyplot as plt


class LanlData:
    """Provides an object to model LANL Cyber-Security Event data."""

    def __init__(self):
        self.data_set = ''
        self.source_url = None
        self.target_file = None
        self.source_file = None

    def download(self, data_set, source_url=None, target_file=None):
        """ Download the specified data set to the specified local directory.
        Args:
            data_set: str containing the name of the data set to download.
                data_set names follow the same naming conventions used by LANL:
                for example, 'proc' represents workstation process data.
            source_url: str containing the URL root to download files from.
                Defaults to the value of URL_PATH (http://csr.lanl.gov/data/cyber1/auth.txt.gz).
            target_file: str containing where to save the downloaded data.
                Defaults to a temp file.
        """

        source_url = "http://csr.lanl.gov/data/cyber1/" + data_set + ".txt.gz" \
            if source_url is None else source_url
        target_file = "data/" + basename(urlparse(source_url).path) \
            if target_file is None else target_file

        if isfile(target_file) is False:
            print("Saving " + source_url + " to " + target_file + ".")
            urlretrieve(source_url, target_file)
        else:
            print(target_file + " exists. Doing nothing.")


if __name__ == "__main__":
    DATA_SETS = ["proc"]

    for d in DATA_SETS:
        LanlData().download(d)

    # We call gzip.open manually because csv2rec does not open the file in text mode otherwise.
    hist_data = csv2rec(open("reports/procCount/part-00000.gz", 'rt'),
                           names=('process', 'count'),
                           delimiter=',')

    n, bins, patches = plt.hist(hist_data['count'], 50)
    plt.xlabel('Process')
    plt.ylabel('Frequency')
    plt.title('Process Frequency')
    plt.savefig("reports/process_frequency.png")
