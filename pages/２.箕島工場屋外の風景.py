import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import sqlite3 
import hashlib
import subprocess
import sys

conn = sqlite3.connect('database.db')
c = conn.cursor()

conn2 = sqlite3.connect('NGdatabase.db')
c2 = conn2.cursor()

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

def create_user():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_user(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data

def check_login_user(username,password):
    c2.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c2.fetchall()
    return data

def main():
    #st.title("ログイン画面")
    st.sidebar.title('ログイン・サインアップ')
    menu = ["ログイン","サインアップ"]
    choice = st.sidebar.selectbox("メニュー",menu)
    if choice == "ログイン":
        #st.subheader("ログイン画面です")
        username = st.sidebar.text_input("ユーザー名を入力してください")
        password = st.sidebar.text_input("パスワードを入力してください",type='password')
        if st.sidebar.button('ログイン'):
            create_user()
            hashed_pswd = make_hashes(password)
            result = login_user(username,check_hashes(password,hashed_pswd))
            if result:
                password = username
                result2 = check_login_user(username,password)
                if result2:
                    st.sidebar.title("{}は利用権がありません".format(username))
                    st.snow()
                    st.toast('ログイン失敗', icon='😂')
                else:
                    st.sidebar.title("{}でログインしました".format(username)) 
                    st.title("箕島工場屋外の風景")
                    st.balloons()
                    st.toast('ログイン成功', icon='😍')
                    # 画像
                    st.text('')
                    st.text('')
                    st.text('①何の羽?')
                    image1 = Image.open('./data/2-1.jpg')
                    #image1_route = image1.rotate(-90,expand=True)
                    image2 = Image.open('./data/2-2.jpg')
                    image2_route = image2.rotate(-90,expand=True)
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2_route)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('②何の死骸があるでしょうか?')
                    image1 = Image.open('./data/3-1.jpg')
                    image1_route = image1.rotate(270,expand=True)
                    image2 = Image.open('./data/3-3.jpg')
                    #image2_route = image2.rotate(180,expand=True)
                    image3 = Image.open('./data/3-2.jpg')
                    image4 = Image.open('./data/3-4.jpg')
                    img_list = []
                    img_list.append(image1_route)
                    img_list.append(image2)
                    img_list.append(image3)
                    img_list.append(image4)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('③ゴキブリの死骸!')
                    image1 = Image.open('./data/4-1.jpg')
                    image2 = Image.open('./data/4-2.jpg')
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('④ゴキブリの死骸!')
                    image1 = Image.open('./data/5-1.jpg')
                    #image1_route = image1.rotate(270,expand=True)
                    image2 = Image.open('./data/5-2.jpg')
                    image3 = Image.open('./data/5-3.jpg')
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    img_list.append(image3)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('⑤何の羽(ゴキブリ)?')
                    image1 = Image.open('./data/6-1.jpg')
                    #image1_route = image1.rotate(270,expand=True)
                    image2 = Image.open('./data/6-2.jpg')
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('⑥セミの死骸?')
                    image1 = Image.open('./data/7-1.jpg')
                    #image1_route = image1.rotate(270,expand=True)
                    image3 = Image.open('./data/7-3.jpg')
                    image3_route = image3.rotate(270,expand=True)
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image3_route)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('⑦ゴキブリ?')
                    image1 = Image.open('./data/8-1.jpg')
                    #image1_route = image1.rotate(270,expand=True)
                    image2 = Image.open('./data/8-2.jpg')
                    #image2_route = image2.rotate(270,expand=True)
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('⑧何の死骸?')
                    image1 = Image.open('./data/9-1.jpg')
                    image1_route = image1.rotate(270,expand=True)
                    image2 = Image.open('./data/9-2.jpg')
                    image3 = Image.open('./data/9-3.jpg')
                    #image3_route = image3.rotate(270,expand=True)
                    img_list = []
                    img_list.append(image1_route)
                    img_list.append(image2)
                    img_list.append(image3)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('⑨ゴキブリの死骸')
                    image1 = Image.open('./data/10-1.jpg')
                    #image1_route = image1.rotate(270,expand=True)
                    image2 = Image.open('./data/10-2.jpg')
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('⑩またまたゴキブリの死骸')
                    image1 = Image.open('./data/11-1.jpg')
                    #image1_route = image1.rotate(270,expand=True)
                    image2 = Image.open('./data/11-2.jpg')
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('⑪工場のシヤッター開放中(いくらでも虫は入ります)')
                    image1 = Image.open('./data/13-1.jpg')
                    image1_route = image1.rotate(270,expand=True)
                    img_list = []
                    img_list.append(image1_route)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('⑫セミの死骸')
                    image1 = Image.open('./data/14-2.jpg')
                    #image1_route = image1.rotate(270)
                    image2 = Image.open('./data/14-1.jpg')
                    #image2_route = image2.rotate(270)
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('⑬セミと蟹の死骸')
                    image1 = Image.open('./data/15-1.jpg')
                    image1_route = image1.rotate(270,expand=True)
                    image2 = Image.open('./data/15-2.jpg')
                    image3 = Image.open('./data/15-3.jpg')
                    image3_route = image3.rotate(270,expand=True)
                    img_list = []
                    img_list.append(image1_route)
                    img_list.append(image2)
                    img_list.append(image3_route)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('⑭黒パレットの裏にゴキブリ発見!')
                    image1 = Image.open('./data/17-1.jpg')
                    #image1_route = image1.rotate(270,expand=True)
                    #image2 = Image.open('./data/17-2.jpg')
                    image3 = Image.open('./data/17-3.jpg')
                    img_list = []
                    img_list.append(image1)
                    #img_list.append(image2)
                    img_list.append(image3)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('⑮ゴキブリまたまた発見!')
                    image1 = Image.open('./data/18-1.jpg')
                    image2 = Image.open('./data/18-2.jpg')
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('⑯鳥の糞発見!')
                    image1 = Image.open('./data/19-1.jpg')
                    image2 = Image.open('./data/19-2.jpg')
                    img_list = []
                    img_list.append(image1)
                    img_list.append(image2)
                    st.image(img_list,width=1000)

                    st.text('')
                    st.text('')
                    st.text('⑰原料を屋外で保管　大丈夫?')
                    image1 = Image.open('./data/20-1.jpg')
                    img_list = []
                    img_list.append(image1)
                    st.image(img_list,width=1000)

                    #　動画
                    st.text('')
                    st.text('')
                    st.text('⑱工場屋外での生きたゴキブリ発見')
                    video_file = open('./data/生きたゴキブリ.mp4','rb')
                    video_bytes = video_file.read()
                    st.video(video_bytes)
            else:
                st.warning("ユーザー名かパスワードが間違っています")
                st.snow()
                st.toast('ログイン失敗', icon='😂')

    elif choice == "サインアップ":
        st.subheader("新しいアカウントを作成します")
        new_user = st.text_input("ユーザー名を入力してください")
        new_password = st.text_input("パスワードを入力してください",type='password')
        if st.button("サインアップ"):
            create_user()
            add_user(new_user,make_hashes(new_password))
            st.success("アカウントの作成に成功しました")
            st.info("ログイン画面からログインしてください")
            st.balloons()
            st.toast('サインアップ成功', icon='😍')
            
if __name__ == '__main__':
    main()


