# pdfファイルを改行をなくしてgoogle翻訳にいれやすくする
## pdfをtxtにする
1. pdfminerをダウンロードする
    - pip install pdfminer3kでダウンロード(3系)
2. pdf2txt.pyがScriptフォルダに置かれる
3. スクリプトのあるフォルダから python pdf2txt.py -o output.txt before.pdf　で実行可能

## txtの改行を通常の改行にする
1. sample.pyを実行（改良予定）
2. 完成！

## 文字コードがうまくいかない！
1. 調査中
