# #!/usr/bin/env python
# # coding: utf8

import os

import tkinter
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog

from spleeter import __main__

def open_file():
  fTyp = [("mp3", "*.mp3")]
  file = filedialog.askopenfilename(filetypes=fTyp)
  file_name.set(file)

def run_app():
   __main__.main(['C:\\Users\\mofum\\git\\spleeter\\spleeter\\__main__.py',
   'separate', '-i', '{}'.format(file_name.get()), '-p', 'spleeter:4stems', '-o', 'output'])

if __name__ == "__main__":
  #---main window---
  root = tkinter.Tk()
  root.title("Mish")
  root.geometry("300x120")

  #---main frame---
  main_frame = ttk.Frame(root)
  main_frame.grid(column=0, row=0, sticky=tkinter.NSEW, padx=5, pady=10)

  #---create widget---
  file_name = tkinter.StringVar()
  file_label = ttk.Label(main_frame, text="Select File")
  file_box = ttk.Entry(main_frame, textvariable=file_name)
  file_btn = ttk.Button(main_frame, text="Choose", command=open_file)

  #---create run---
  run_btn = ttk.Button(main_frame, text="run", command=run_app)

  #---locate widget---
  file_label.grid(column=0, row=0, pady=10)
  file_box.grid(column=1, row=0, sticky=tkinter.EW, padx=5)
  file_btn.grid(column=2, row=0)
  run_btn.grid(column=1, row=2)

  root.mainloop()
# class FiledialogSampleApp(ttk.Frame):
#   def __init__(self, app):
#     super().__init__(app)
#     self.pack()

#     # Widget用変数を定義
#     self.filename = StringVar()

#     label = ttk.Label(self,text="file")
#     label.pack(side="left")
#     # textvariableにWidget用の変数を定義することで変数の値が変わるとテキストも動的に変わる
#     filenameEntry = ttk.Entry(self,text="",textvariable= self.filename)
#     filenameEntry.pack(side="left")

#     button = ttk.Button(self,text="参照",command = self.openFileDialog)
#     button.pack(side="left")

#     run = ttk.Button(self, text="実行", command=self.separateMusic)
#     run.pack()

#   #ファイルダイアログを開いてfilenameEntryに反映させる
#   def openFileDialog(self):
#     fTyp = [("mp3", "*.mp3")]
#     file  = filedialog.askopenfilename(filetypes=fTyp)
#     self.filename.set(file)
#     return file

#   def separateMusic(self):
#     __main__.main(['C:\\Users\\mofum\\git\\spleeter\\spleeter\\__main__.py',
#   'separate', '-i', '{}.mp3'.format(self), '-p', 'spleeter:4stems', '-o', 'output'])


# if __name__ == '__main__':
#     #Tkインスタンスを作成し、app変数に格納する
#     app  = Tk()
#     #縦幅400横幅300に画面サイズを変更します。
#     app.geometry("400x300")
#     #タイトルを指定
#     app.title("Mish")
#     # #フレームを作成する
#     frame = FiledialogSampleApp(app)
#     # 格納したTkインスタンスのmainloopで画面を起こす
#     app.mainloop()