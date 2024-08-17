[Flask公式 \| The Pallets Projects](https://palletsprojects.com/p/flask/)

# ハンズオン

[GitHub \- ml\-flaskbook/flaskbook](https://github.com/ml-flaskbook/flaskbook)

pip install flask

# 環境変数のセット FLASK_APP, FLASK_ENV

# .flaskenv をつくると、そこがアプリルートになる
#   app.py の相対パスを書き込む

pip install python-dotenv

mkdir apps/appname/
touch apps/appname/app.py
touch apps/appname/.flaskenv

flask run

# デコレータ、ルーティング
#   エンドポイント命名（URIのこと） <- flask routes の見え方に影響
#   メソッドは、デフォルト: Getのみ 
#   コンバータを記述すると型をチェックできる (path: /を含むテキストを許容)

# htmlファイルをつかう、render_template関数をつかう
#   1. 【templates】 フォルダをつくる app.py と同じ階層に
#   2. import render_template する

# jinja2 テンプレート {% %}
# https://jinja.palletsprojects.com/en/3.0.x/templates/

# urlを生成する、url_for関数をつかう
#  1. import url_for する
#   エンドポイント名、変数 を指定する

# 静的ファイル（css, javascript）を、htmlにセットする
#  1. 【static】フォルダをつくる　←　flack routes で見える

# 2つのコンテキスト
# 1. アプリケーションコンテキスト
#   current_app: 実行中のアプリのインスタンス, これにアクセスさせる
#      Flaskがリクエスト処理を開始した時にスタックにPushされ current_app という属性にアクセス可能になる
#      スタックに積まれたcurrent_appにはどこからでもアクセスできる
#   g: リクエストごとにリセットされる、グローバルな一時領域
#      スタックに積まれたら、どこからでもアクセスできる
#
# 2. リクエストコンテキスト
#   request:  
#   session: 

#　===minimalapp 完成===
#　===minimalapp に問い合わせフォームをつくる===

- 画面は2つ「入力フォーム画面」「完了画面」
- データベースなし
- メールがとぶ？

# PRGパターン、再ロード時の二重Postを避ける

1. GET 入力フォーム画面を表示
2. POST メールを送信
3. REDIRECT  完了画面へリダイレクト
4. GET 完了画面を表示

Endpoint         Methods  Rule
contact          GET      /contact
contact_complete GET,POST /contact/complete

