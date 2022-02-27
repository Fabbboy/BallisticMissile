# BallisticMissile 🎯
<img src="https://media.discordapp.net/attachments/945398687906013194/947523570161041458/BML.png?width=2160&height=772">

EDUCATION PURPOSES ONLY\
![GitHub All Releases](https://img.shields.io/github/downloads/Fabbboy/BallisticMissile/total?color=black) ![GitHub stars](https://img.shields.io/github/stars/Fabbboy/BallisticMissile?style=social)
***
# What is BallisticMissile❓
BallisticMissile is a DDOS tool for stress testing on server that supports http and https. BallisticMissile has the option to go into hardcore mode by activating the cpuKiller mode. In this mode, not only the units are started individually, but also the "weapons" of the units, which gives faster and more intense attacks, but this is also very CPU-heavy. With BallisticMissile you also have the option of using a proxy to hide your data on the internet. 
# Why was BallisticMissile created❓
BallisticMissile was made to test a web3.0 project working with NFT


# Setup 🛠️
1. Download all files 
```shell
git clone https://github.com/Fabbboy/BallisticMissile 
```
2. Give the "BallisticMissile.py" permissions
```shell
chmod +x BallisticMissile.py
```
3. If needed edit the configuration file\
<tt>The following is the config file that we would use</tt>
```json
{
  "_comment" : "Please do not change anything if you don't know what you are doing",
  "ThreadPool" : 5,
  "delay" : "0.1",
  "retry": 5,

  "_comment" : "If your using a old, slow or bad cpu please do not use this below",
  "cpuKiller" : true,   
  "cpuKillerThreadPool" : 5,

  "_comment": "http and https proxy",
  "useProxy" : false,
  "httpProxy" : "http://35.170.183.99",
  "httpPort" : 80,
  "httpsProxy": "https://20.47.108.204",
  "httpsPort" :	8888
}
```
4. import dependencies
```shell
pip install -r requirements.txt
```
*🚀 You're good to go 🚀*

# Usage ⚙️
**Flags:**
```shell
-t Target url (https://google.com)
-a the number of attacks performed by a unit (10)
-m Number of Units
-d The number of megabytes each attack sends to the server
```

*all values in "{}" are example values*
```shell
./BallisticMissile.py -t {https://google.com} -a {10} -m {10} -d {1024}
```
# Tests 🧪
We tested this stress tool with 2 different http server.

Our system:
```
CPU: Intel I5 Dualcore 
Ram: 16 GB
OS: MacOs
```
Server system:
```
CPU: Intel Core I7-10700F
Ram: 2 GB
OS: Ubuntu
```
command that we started
```
./BallisticMissile.py -t https://ip -a 100 -d 2048 -m 1000
```
both servers crash after about 30 seconds\
**BOTH SERVER WE'RE HOSTET ON OUR OWN NETWORK**

# Fabbboy
This tool is owned and published by Fabbboy\
This tool is under the GNU license\
Changes are allowed\
Official link: https://github.com/Fabbboy/BallisticMissile \
**DO NOT REMOVE THE LICENSE OR README FILE**
