# video-description-cnn-rnn

Latex File Link : https://www.sharelatex.com/read/fxjfhrbfpyrq


Welcome to the video-description-cnn-rnn wiki!

There are two categories of temporal structure present in video: (1) local structure and (2) global structure.
- Local temporal structure refers to the fine-grained motion information that characterizes punctuated actions such
as “answering the telephone” or “standing up”. Actions such as these are relatively localized in time, evolving over only a few consecutive frames.
- On the other hand, when we refer to global temporal structure in video, we refer to the sequence in which objects, actions, scenes and people, etc. appear in a video.

# Setting up environment
- Use python 2.x

## Assign node
```
srun -n 32 -N 2 -p gtx780 --pty /bin/bash
OR
srun -n 16 -N 1 -p gtx1080 --pty /bin/bash
```

## Seeing which jobs are active
```
squeue -u <username> -t RUNNING
```

## Installing python dependencies
```
pip2.7 install --user tables
pip2.7 install --user sklearn
pip2.7 install --user scipy
pip2.7 install --user mako
pip2.7 install --user cython
pip2.7 install --user nose
```

## Installing git from source
```
wget https://github.com/git/git/archive/v2.1.2.tar.gz -O git.tar.gz
tar -zxf git.tar.gz
cd git-2.1.2/
make configure
make install
```

## Configure git (optional)
```
# git config --global user.name "Your name"
# git config --global user.email "Your email address"
```

## Checkout arctic-capgen-vid repo
```
cd ~
git clone https://github.com/yaoli/arctic-capgen-vid.git
```

## Install dependencies
```
mkdir ~/arctic-capgen-vid/dependencies
cd ~/arctic-capgen-vid/dependencies

# Coco-caption
git clone https://github.com/tylin/coco-caption.git

# Jobman
git clone git://git.assembla.com/jobman.git Jobman

## Theano + pygpuarray
# First install cmake version 3.x
cd
wget https://cmake.org/files/v3.6/cmake-3.6.2.tar.gz
tar -zxvf cmake-3.6.2.tar.gz
cd cmake-3.6.2
./bootstrap --prefix=~/.local/
make
make install
vim ~/.bash_profile
export PATH=~/.local/bin:$PATH

# Theano
cd ~/arctic-capgen-vid/dependencies
git clone git://github.com/Theano/Theano.git
cd Theano
pip install --user -e .

# pygpu
cd ..
git clone https://github.com/Theano/libgpuarray.git
cd libgpuarray
git checkout tags/v0.7.5 -b v0.7.5
mkdir Build
cd Build
cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=~/.local
make
make install
cd ..
python setup.py build_ext -L ~/.local/lib -I ~/.local/include
python setup.py build
python setup.py install --user
```

## Adding following paths to your bash profile as per your home directory 
```
vim ~/.bash_profile

export PATH=$PATH:$HOME/.local/bin:$HOME/bin:$HOME/arctic-capgen-vid/dependencies/Jobman/bin

export PYTHONPATH=$PYTHONPATH:$HOME/arctic-capgen-vid/dependencies/Theano/:$HOME/arctic-capgen-vid/dependencies/coco-caption:$HOME/arctic-capgen-vid/dependencies/Jobman

export CPATH=$CPATH:~/.local/include
export LIBRARY_PATH=$LIBRARY_PATH:~/.local/lib
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/.local/lib
```

## Load bash profile
```
. ~/.bash_profile
```

## Download dataset
```
mkdir ~/arctic-capgen-vid/dataset
cd ~/arctic-capgen-vid/dataset
wget 'http://lisaweb.iro.umontreal.ca/transfert/lisa/users/yaoli/youtube2text_iccv15.zip'
unzip youtube2text_iccv15.zip 
```

## ALL DONE. NOW FOLLOW STEPS MENTIONED IN REPO's README FILE ;)
