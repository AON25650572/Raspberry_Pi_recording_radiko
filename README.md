# Raspberry_Pi_recording_radiko

## 1. radiko録音

https://qiita.com/yuppejp/items/04a904ee183dc69dcb73 より

```sh
./rec_radiko.sh channel_name duration(minuites) [outputdir] [prefix]
```

## ~~2. dropboxにアップロード~~

https://iot-plus.net/make/raspi/upload-data-to-dropbox-from-raspi/#toc_id_1 より

普通にgitコマンドでとってこい（怒）

（ドロップボックスのAPI仕様が変わってる？アクセスできない）

## ~~2. Google Driveにアップロード~~

https://qiita.com/yuppejp/items/04a904ee183dc69dcb73 後半より

（死ぬほどめんどくさい、却下）

## ~~2. OneDriveにアップロード~~

https://qiita.com/Soleiyu/items/2fd1dcc4f707597547b5

makeにえぐいほど時間かかるみたい

（makeでエラーが起こりまくる。ムリ...）


## 3. crontabで自動化

https://www.server-memo.net/tips/crontab.html#crontab

