# pyspark-word-count
# your input must be in /drive/MyDrive/pyspark
# Run below commands in google colab
# install Java8
apt-get install openjdk-8-jdk-headless -qq > /dev/null
# download spark3.0.0
wget -q http://apache.osuosl.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
# unzip it
tar xf spark-3.1.2-bin-hadoop3.2.tgz
# install findspark 
pip install -q findspark
