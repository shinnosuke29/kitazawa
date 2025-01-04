# KITAZAWAプロジェクト

これは、KITAZAWAプロジェクトのROS 2パッケージです。このプロジェクトは、ロボットアプリケーションのための温度シミュレーションとデータ公開を行います。

## 機能

- **温度シミュレータノード**  
  温度データをシミュレートし、ロボットシステムで使用できる形式で出力します。

- **データ公開**  
  シミュレーションされた温度データをROS 2ネットワーク上で公開し、モニタリングや分析ができるようにします。

## 実行方法

1. ワークスペースをビルドします：

   ```bash
   colcon build
2. セットアップファイルをソースします：

   ```bash
   source install/setup.bash

3. ノードを実行します：

   ```bash
   ros2 run kitazawa temperature_simulator

## 開発環境
・ROS 2 (Foxy以降)
・Ubuntu 20.04またはそれ以降
・Python 3.x
・colcon（ビルドツール）

## その他
このプロジェクトは、ロボットの温度モニタリングやシミュレーションシステムの一部として使用することができます。温度シミュレータノードは、システムのセンサーデータを模倣し、リアルタイムで監視するためのデータを提供します。