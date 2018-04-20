#! /bin/bash
export CPATH=$CPATH:~/.local/include
export LIBRARY_PATH=$LIBRARY_PATH:~/.local/lib
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/.local/lib
THEANO_FLAGS=mode=FAST_RUN,gpuarray.preallocate=1,device=cuda,floatX=float32 python ~/video-description-cnn-rnn/arctic-capgen-vid/train_model.py
