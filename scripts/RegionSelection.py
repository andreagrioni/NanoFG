import argparse
from pybedtools import BedTool


def get_arguments():
    '''parse input arguments'''
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(prog='NanoFG helper', description='run pybedtools to intersect a/b arbitrary files (bed/bam)')
    parser.add_argument('-a', '--a_file', type=str, dest='a', help='bed/bam input 1', required=True)
    parser.add_argument('-b', '--b_file', type=str, dest='b',help='bed/bam input 2', required=True)
    parser.add_argument('-o', '--output_name', type=str, dest='fo',help='file output name/path', required=True)
    args = parser.parse_args()
    return args
    

def intersect(a,b):
    '''intersect a and b input files
    with pybedtools
    
    arguments:
    a=BedTool Object
    b=BedTool Object

    return:
    BedTool Object
    '''
    a=BedTool(a)
    b=BedTool(b)
    a_b=a.intersect(b)
    return a_b


if __name__ == '__main__':
    args = get_arguments()
    intersected = intersect(args.a, args.b)
    # save to fo
    intersected.saveas(args.fo)