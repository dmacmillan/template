import argparse, os, sys

parser = argparse.ArgumentParser(description='')

parser.add_argument('',help='')
parser.add_argument('',help='')
parser.add_argument('',help='')
parser.add_argument("-l", "--log", dest="logLevel", default='WARNING', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help='Set the logging level. Default = "WARNING"')
parser.add_argument('-n', '--name', default='result', help='Name for the file output. Default is "result"')
parser.add_argument('-o', '--outdir', default=os.getcwd(), help='Path to output to. Default is {}'.format(os.getcwd()))

args = parser.parse_args()

if not os.path.isdir(args.outdir):
    try:
        os.makedirs(args.outdir)
    except OSError:
        pass

# Logging
logging.basicConfig(filename=os.path.join(args.outdir, 'logfile'), level=logging.getattr(logging, args.logLevel))
