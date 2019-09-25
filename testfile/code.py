import numpy as np
import json
import os
import h5py


######################
# global parameteres #
######################
print('loading parameters ...')
# Data input path
dataDir = '../process/'
img_dataDir = '../process_img/'
input_img_h5 = 'data_img.h5'  # image_features

# ques_train、ques_length_train、answers、question_id_train、img_pos_train
# ques_test、ques_length_test、question_id_test、img_pos_test
input_ques_h5 = 'data_prepro.h5'

# dict_keys(['ix_to_word', 'ix_to_answer', 'unique_img_train', 'unique_img_test'])
input_json = 'data_prepro.json'

###################################
# initialization train parameters #
###################################

'''Start'''
class Answer_Generator():
    def __init__(self, rnn_size, rnn_layer, batch_size, input_embedding_size):
        """
        The code is an excerpt from san_lstm_att.py

        """
        self.rnn_size = rnn_size
        self.rnn_layer = rnn_layer
        self.batch_size = batch_size
        self.input_embedding_size = input_embedding_size


'''
The following code is omitted
'''

"""End"""
