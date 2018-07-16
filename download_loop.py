'''
runs urlretrieve over a list of ftp links (one link per row in a text file)

unhash the line 'unzip(filename)' in the download func for unzipping
'''

import sys, os, urllib.request, logging, argparse, time
# from multiprocessing import Pool
# from progress.bar import Bar


def main(args):
    # prechecks on arguments
    if args.topup and args.download:
        print('Only one run flag should be passed. -d or -r')
        sys.exit()
    elif not args.topup and not args.download:
        print('You should provide at least one flag')
        sys.exit()
    elif not args.ftp_links:
        print('You must pass a list of links. Use flag -l.')
        sys.exit()

    #initialise
    content = get_ftp_links(args.ftp_links)
    downloaded_files = os.listdir('.')


    # work

    for url in content:
        if args.topup and not already_downloaded(downloaded_files, url):
            ftp_fetch(url)
        elif args.download:
            ftp_fetch(url)


    # pool = Pool()
    # inputs = range(100)
    # bar = Bar('Processing', max=len(inputs))
    # for i in pool.imap(ftp_fetch, inputs):
    #     bar.next()
    # bar.finish()

def get_ftp_links(input_file):
    with open(input_file) as f:
        content = f.readlines()
        return [x.strip() for x in content]


def already_downloaded(downloaded_files, url):
    filename = str(url.split("/")[-1])
    if filename in downloaded_files:
        return(True)
    else:
        return(False)

def ftp_fetch(url):
    filename = str(url.split("/")[-1])
    # urllib.request.urlretrieve(url, filename=filename) # 5 files took 79.69 sec
    # os.system('wget {}'.format(url)) # 5 files took 74.75 sec




    # try:
    #     urllib.request.urlretrieve(url, filename=filename)
    #     logger.info('Downloaded %s', filename)
    #     print('Downloaded %s', filename)
    # except Exception as ex:
    #     logger.exception('An exception of type %s occurred on file %s.', type(ex).__name__, filename)

if __name__ == "__main__":


    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description='FTP loops for EC2 and basic file checks. Provide a list of FTP links and a drop destination to begin.')
    parser.add_argument('--ftp-links', '-l', help='links filename')
    parser.add_argument('--download', '-d', action='store_true', help='downloads all files in ftp-links file and overwrites existing')
    parser.add_argument('--topup', '-t', action='store_true', help='attempts to download any files in the ftp-links file that doesnt already exist in the directory')
    args = parser.parse_args()
    print('Start time: {}'.format(time.time()))
    main(args)
    print('End time: {}'.format(time.time()))

