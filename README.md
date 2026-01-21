File Manipulator

file_manipulator.py は、コマンドライン引数を用いてファイル内容を操作するためのシンプルな Python スクリプトです。本プロジェクトは、ファイルの読み書きおよびシェル引数の扱いを学習することを目的としています。

⸻

前提条件
	•	Python 3.x がインストールされていること
	•	テキストファイルを操作対象とすること（バイナリファイル非対応）

⸻

使い方

基本構文は以下のとおりです。

python file_manipulator.py <command> <inputpath> <outputpath | 引数>

コマンドごとに必要な引数の数と意味が異なります。以下を参照してください。

⸻

対応コマンド一覧

1. reverse

python file_manipulator.py reverse input.txt output.txt

説明
	•	input.txt の内容を読み込み、文字順を逆にした内容を output.txt に書き込みます。

⸻

2. copy

python file_manipulator.py copy input.txt output.txt

説明
	•	input.txt の内容をそのままコピーし、output.txt として保存します。

⸻

3. duplicate-contents

python file_manipulator.py duplicate-contents input.txt 3

説明
	•	input.txt の内容を読み込み、内容全体を n 回 複製します。
	•	複製後の内容は 同じ input.txt に上書き保存 されます。

注意
	•	第 3 引数には整数を指定する必要があります。

⸻

4. replace-string

python file_manipulator.py replace-string input.txt old new

説明
	•	input.txt 内の文字列 old をすべて検索し、new に置き換えます。
	•	置換後の内容は input.txt に上書き保存されます。

⸻

バリデーションについて

このスクリプトでは以下の入力チェックを行っています。
	•	引数の個数が不足している場合はエラーメッセージを表示して終了
	•	存在しない入力ファイルを指定した場合はエラー表示
	•	duplicate-contents に整数以外を指定した場合はエラー表示
	•	replace-string に必要な引数が不足している場合はエラー表示

⸻

エラー時の例

無効な入力ファイルパスです。 input.txt が存在しません。

入力に誤りがあります。duplicate-contentsコマンドは第３引数に整数が必要です。


⸻

学習ポイント
	•	sys.argv を用いたコマンドライン引数の扱い
	•	open() を使ったファイルの読み書き
	•	例外処理（try / except）による安全な実装
	•	処理ごとの関数分割による可読性向上

⸻

補足

本スクリプトは学習目的であり、大規模ファイルや並列処理は想定していません。必要に応じて機能拡張やリファクタリングを行ってください。
