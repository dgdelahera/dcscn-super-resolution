"""
Paper: "Fast and Accurate Image Super Resolution by Deep CNN with Skip Connection and Network in Network"
Author: Jin Yamanaka
Github: https://github.com/jiny2001/dcscn-image-super-resolution
Ver: 2.0
Apply Super Resolution for image file.
--file [your image filename]: will generat HR images.
see output/[model_name]/ for checking result images.
Also you must put same model args as you trained.
For ex, if you trained like
python3 train.py --layers 4 --filters 24 --dataset test --training_images 400
Then you must run evaluate.py like below.
python3 evaluate.py --layers 4 --filters 24 --file your_image_file_path
"""

import tensorflow as tf

import main.DCSCN as DCSCN
from main.helper import args

args.flags.DEFINE_string("file", "image.jpg", "Target filename")
FLAGS = args.get()


def main(_):
    model = DCSCN.SuperResolution(FLAGS, model_name=FLAGS.model_name)
    model.build_graph()
    model.build_optimizer()
    model.build_summary_saver()

    model.init_all_variables()
    model.load_model()

    model.do_for_file(FLAGS.file, FLAGS.output_dir)


if __name__ == '__main__':
    tf.app.run()
