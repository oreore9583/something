import subprocess
import os

# ダウンロード対象のファイルがなければ自動で作る
list_file = "wget-list-systemd"
if not os.path.exists(list_file):
    with open(list_file, "w") as f:
        # テスト用にGoogleのURLを書き込んでおく
        f.write("https://google.com\n")

try:
    print("ダウンロードを開始します...")
    subprocess.run(["wget", f"--input-file={list_file}", "--continue"], check=True)
    print("正常に完了しました！")
except subprocess.CalledProcessError as e:
    print(f"エラーが発生しました (終了コード: {e.returncode})")

