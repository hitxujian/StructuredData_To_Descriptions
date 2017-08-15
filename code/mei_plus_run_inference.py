from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os.path
import time
import math
import sys
from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf
from optparse import OptionParser
from mei_plus_model import *
from dataset_iterator_hier import *
from run_inference_mei import *
import os

def main():
    parser = OptionParser()
 
    parser.add_option(
    "-w", "--work-dir", dest="wd", default="../Data/")
    parser.add_option(
        "-l", "--learning-rate", dest="lr", default=0.0001)
    parser.add_option(
        "-e", "--embedding-size", dest="emb_size",
        help="Size of word embeddings", default=50)
    parser.add_option(
        "-s", "--hidden-size", dest="hid_size",
        help="Hidden size of the cell unit", default=100)
    parser.add_option(
        "-a", "--batch-size", dest="batch_size",
        help="Number of examples in a batch", default=32)
    parser.add_option(
        "-n", "--epochs", dest="epochs",
        help="Maximum Number of Epochs", default=10)

    parser.add_option(
        "-t", "--early_stop", dest="early_stop",
        help="Stop after these many epochs if performance on validation is not improving", default=2)

    parser.add_option(
        "-o", "--output_dir", dest="outdir",
        help="Output directory where the model will be stored", default="../out/")

    parser.add_option(
        "-x", "--emb-train", dest="emb_tr")

    parser.add_option(
        "-g", "--gamma_tunable", dest="gamma_param")


    parser.add_option(
        "-p", "--vocab-frequency", dest="vocab_frequency")

    parser.add_option(
        "-m", "--num-fields", dest="num_fields")

    parser.add_option(
	"-f", "--feed-previous", dest="feed_previous")

    parser.add_option(
    "-k", "--embedding|-dir", dest="embedding_dir")

    parser.add_option(
    "-c", "print_frequency", dest="print_frequency")

    (option, args) = parser.parse_args(sys.argv)

    if (option.emb_tr == "True"):
        x = True
    else:
        x = False

    c = Config(float(option.lr), int(option.emb_size), int(option.hid_size), int(option.batch_size),
                int(option.epochs), early_stop=int(option.early_stop), outdir= option.outdir, emb_tr=x,
                feed_previous=int(option.feed_previous), gamma_param = float(option.gamma_param), vocab_frequency = int(option.vocab_frequency), num_fields=int(option.num_fields), embedding_dir=option.embedding_dir, print_frequency=int(option.print_frequency))


    run_attention = run_inference(option.wd, BasicAttention(), c)
    run_attention.run_testing()



if __name__ == '__main__':
    main()
