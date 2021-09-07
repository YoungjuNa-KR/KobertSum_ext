import os
os.chdir('/tmp/')
!curl -LO https:://bitbucket.org/eunjeon/mecab-ko/downloads/
mecab-0.994-ko-0.9.2.tar.gz
!tar zxfv mecab-0.996-ko-0.9.2.tar.gz

os.chdir('/tmp/mecab-0.996-ko-0.9.2')
!./configure

!make
!make check
!make install
!ldconfig

#GNU M4 설치
os.chdir('/tmp/')
!wget https://ftp.gnu.org/gnu/m4/m4-1.4.9.tar.gz
!tar -zvxf m4-1.4.9.tar.gz
os.chdir('/tmp/m4-1.4.9')
!./configure
!make
!make install

#automake 설치
os.chdir('/tmp')
!curl -LO http://ftpmirror.gnu.org/automake/automake-1.11.tar.gz
!tar -zxvf automake-1.11.tar.gz
os.chdir('/tmp/automake-1.11')
!./configure
!make
!make install

#mecab dictionary 설치
os.chdir('/tmp')
!curl -LO https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-2.1.1-20180720.tar.gz
os.chdir('/tmp/mecab-ko-dic-2.1.1-20180720')
!./autogen.sh
!./configure

!sudo make
!sudo make install

#mecab python 설치
os.chdir('/content')

!git clone https://bitbucket.org/eunjeon/mecab-python-0.996.git
os.chdir('/content/mecab-python-0.996')

!sudo python3 setup.py build
!sudo python3 setup.py install
!sudo pip install kss

