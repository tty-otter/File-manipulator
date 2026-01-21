import sys
import os

# コマンドライン引数に基づき各コマンドを実行。
def main():
    if len(sys.argv) < 4:
        print("引数は４または５個必要です。使用例を参照してください。")
        print_usage()
        sys.exit(1)

    script_name = sys.argv[0]
    command = sys.argv[1]
    input_filepath = sys.argv[2]
    output_filepath = sys.argv[3]

    #入力ファイルが開けない場合はエラーを返す。
    try:
        with open(input_filepath, 'r') as f:
            input_data = f.read()
            if command == "reverse":
                output_filepath = check_output_file(sys.argv[3])
                reverse(input_data, output_filepath)
            elif command == "copy":
                output_filepath = check_output_file(sys.argv[3])
                copy(input_data, output_filepath)
            elif command == "duplicate-contents":
                repeat_count = sys.argv[3]
                duplicate_contents(input_data, repeat_count, input_filepath)
            elif command == "replace-string":
                if len(sys.argv) < 5:
                    print("入力に誤りがあります。replace-stringコマンドは５個の引数が必要です。使用例を参照してください。")
                    print("file_manipulator.py replace-string input_filepath find_word replace_word")
                    sys.exit(1)
                find_word = sys.argv[3]
                replace_word = sys.argv[4]
                replace_string(input_data, find_word, replace_word, input_filepath)
            else:
                print("入力に誤りがあります。受付可能なコマンドは次の４つです。")
                print("reverse, copy, duplicate-contents, replace-string")
    except FileNotFoundError:
        print(f"無効な入力ファイルパスです。 {input_filepath}が存在しません。")

def print_usage():
    print("使用例:")
    print("[reverse] file_manipulator.py reverse input_filepath output_filepath")
    print("[copy] file_manipulator.py copy input_filepath output_filepath")
    print("[duplicate-contents] file_manipulator.py duplicate-contents input_filepath repeat_intger")
    print("[replace-string command] file_manipulator.py replace-string input_filepath find_string replace_string")

def check_output_file(output_filepath):
    # 指定されたパスにファイルが作成できるかの確認
    try:
        with open(output_filepath, 'w') as f:
            f.write("Check create file.")
        os.remove(output_filepath)
        return output_filepath
    except:
        # エラーの場合に同じフォルダにoutput.txtで出力。
        return "output.txt"
    
def write_to_file(data, filepath, success_message):
    # 指定されたデータをファイルに書き込み
    with open(filepath, 'w') as f:
        f.write(data)
    print(success_message)

# Reverse
def reverse(input_data, output_filepath):
    # inputpathにあるファイルを受け取り、outputpathにinputpathの内容を逆にした新しいファイルを作成。
    reversed_data = input_data[::-1]
    write_to_file(reversed_data, output_filepath, "reverse処理が完了。")

# Copy
def copy(input_data, output_filepath):
    # inputpathにあるファイルのコピーを作成し、outputpathとして保存。
    write_to_file(input_data, output_filepath, "copy処理が完了。")

# Duplicate
def duplicate_contents(input_data, str_repeat_count, input_filepath):
    # inputpathにあるファイルの内容を読み込み、その内容を複製し、複製された内容をinputpathにn回複製する。
    try:
        int_repeat_count = int(str_repeat_count)
        duplicated_contents = input_data * int_repeat_count
        write_to_file(duplicated_contents, input_filepath, "duplicate-contents コマンドの処理が完了。")
    except ValueError:
        print("入力に誤りがあります。duplicate-contentsコマンドは第３引数に整数（複製する回数）が必要です。使用例を参照してください。")
        print("file_manipulator.py duplicate-contents input_filepath 2")
    
# Replace_string
def replace_string(input_data, target_str, replace_str, input_filepath):
    # inputpathにあるファイルの内容から文字列"needle"を検索し、"needle"のすべてを"newstring"に置き換える。
    replaced_data = input_data.replace(target_str, replace_str)
    write_to_file(replaced_data, input_filepath, "replace-stringコマンドの処理が完了。")

if __name__ == "__main__":
    main()


    
