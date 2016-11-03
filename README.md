# Agoda Test Downloader

Program that can be used to download data from multiple sources and protocols to local disk. 
The list of sources will be given as input in the form of urls (e.g. http://my.file.com/file, ftp://other.file.com/other, sftp://and.also.this/ending etc). 
The program download all the sources, to a configurable location (file name should be uniquely determined from the url) and then exit. 
considerations:
 - The program should extensible to support different protocols
 - Some sources might very big (more than memory)
 - Some sources might be very slow, while others might be fast
 - Some sources might fail in the middle of download, we never want to have partial data in the final location.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
 - python 2.7

### Installing

```
git clone https://github.com/fartashh/Agoda_Test_Downloader
```


## Running the tests

```
python test_downloader.py  
```

## Running the Downloader

Download one file
```
python download_manager.py -u http://mirror.aarnet.edu.au/pub/squid/squid/squid-4.0.15.tar.gz 
```
Download more than one file
```
python download_manager.py -u http://mirror.aarnet.edu.au/pub/squid/squid/squid-4.0.15.tar.gz ftp://ftp.is.co.za/pub/squid/squid-3.1.23.tar.gz 
```



