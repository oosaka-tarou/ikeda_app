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
                    st.title("部署紹介")
                    st.balloons()
                    st.toast('ログイン成功', icon='😍')

                    st.success('【製造部】', icon="✅")
                    msg1 = "製造部は5工場制となっており、第2工場が末期状態である。第2工場は「スプレードライ」、「造粒」等"
                    msg2 = "の粉体を扱っているが、片芝前工場長、妹尾副工場長が全体の把握ができておらず人心は離れている。"
                    msg3 = "ちなみに片芝前工場長は、現在工場全体を把握する統括部長の立場にあるが・・・・"
                    msg4 = "事の発端は、妹尾副工場長に相談してもまともに取り合ってくれず、これでは、相談にも行かなくなる。"
                    msg5 = "「会社を辞職する際には会社の所為にするな!」と言う有様で会社を辞めることのみを阻止するだけに留まる。"
                    msg6 = "そして、片芝前工場長は未だに第2工場で権威(工場全体を把握せず)を振るっている有様です。"
                    msg7 = "また、次の時代を担う若者の退職が相次ぎ、製造ができなくなりつつある。"
                    msg8 = "現在、毎月のように中堅社員が辞めている。"
                    msg9 = "2023年10月から「組織改革」を行うとのことだったが蓋を開けてみれば、的外れな組織改革となっている。"
                    msg10 = "現在でも辞職を考えている工場社員がいる。"
                    st.text(msg1)
                    st.text(msg2)
                    st.text(msg3)
                    st.text(msg4)
                    st.text(msg5)
                    st.text(msg6)
                    st.text(msg7)
                    st.text(msg8)
                    st.text(msg9)
                    st.text(msg10)

                    st.success('【品質保証部】', icon="✅")
                    msg1 = "品質保証部は、主に製造業（メーカー）の企業に置かれ、製品の品質に関わる保証業務を担当する職種です。"
                    msg2 = "自社が取り扱う製品について、品質基準に達していることを確認したり、販売後のアフターフォロー"
                    msg3 = "を行ったりします。また、工場の環境についても担当しています。具体的には、防虫・防鼠、制服管理、"
                    msg4 = "入退室管理等です。"
                    msg5 = "その中心となるのが高垣部長です。"
                    msg6 = "彼は、社内では通称「制服部長」と陰で言われているそうです。その所以は、制服の管理のみしか遂行して"
                    msg7 = "いないからだそうです。"
                    msg8 = "部内には、工場長経験者、開発担当者等優秀な人材がそろっていますが、コミュニケーション不足なのか部長は"
                    msg9 = "制服のこと以外は何も知りませんし、関心がありません。"
                    msg10 = "但し、その制服も規則で業者(サニクリーン)が洗濯するようになっていますが、自宅で洗濯している人が"
                    msg11 = "何人も居ます。それすら対策出来ていません。"
                    msg12 = "噂によると、会社の備品(ポータブル電源等)を担当社員の自腹で購入させているそうです。"
                    st.text(msg1)
                    st.text(msg2)
                    st.text(msg3)
                    st.text(msg4)
                    st.text(msg5)
                    st.text(msg6)
                    st.text(msg7)
                    st.text(msg8)
                    st.text(msg9)
                    st.text(msg10)
                    st.text(msg11)
                    st.text(msg12)
                    
                    st.success('【人事部】', icon="✅")
                    msg1 = "人事部とは、企業のなかで社員の採用や研修を担い、人事評価制度の設計・運用や、社員の労務管理を担当する"
                    msg2 = "部門です。重要な経営資源である「ヒト」を引き受ける企業の中心部でもあります。"
                    msg3 = "具体的には、採用・教育・研修・人事評価・労務管理・給与計算等です。"
                    msg4 = "その中心となるのが山岡部長です。"
                    msg5 = "彼は、社内では通称「命令部長」と陰で言われているそうです。その所以は、何でもかんでも【業務命令】"
                    msg6 = "の一言で指示するからだそうです。また、月の半分以上は出張(?)等で会社には居ません。"
                    msg7 = "スタッフは、優秀な人が居ますが、逆に戦力外の人も居ます。"
                    msg8 = "また、人事部の仕事のやり方がまるで「昭和」のやり方で業務遂行しています。例えば、700枚もの"
                    msg9 = "タイムカードを手作業でおまけに他部署に依頼しているそうです。"
                    msg10 = "その為、全体的に人事部の仕事をシステム構築をし、「令和」のやり方に変えるそうですが、一番大事な事"
                    msg11 = "が理解できていないのでお金と時間をかけて今より非効率な事となることでしょう。"
                    msg12 = "噂によると、会社の備品(フォルダー等)を担当社員の自腹で購入させているそうです。"
                    st.text(msg1)
                    st.text(msg2)
                    st.text(msg3)
                    st.text(msg4)
                    st.text(msg5)
                    st.text(msg6)
                    st.text(msg7)
                    st.text(msg8)
                    st.text(msg9)
                    st.text(msg10)
                    st.text(msg11)
                    st.text(msg12)

                    st.success('【業務部】', icon="✅")
                    msg1 = "業務部とは、企業のなかで原料・包材の購買管理を行い、物流倉庫の管理そして、物流管理を担当する"
                    msg2 = "部門です。原価上重要な役割を果たすべき部署といえます"
                    msg3 = "その中心となるのが岡田副部長です。"
                    msg4 = "彼は、社内では通称「成り上がり部長」と陰で言われているそうです。その所以は、前任者が急に異動となり"
                    msg5 = "成り上がり的に副部長となったからだそうです。"
                    msg6 = "特筆すべき事は、業務部で物流の窓口を行っていますが、「2024年問題」に対してノ―プランという事です。"
                    msg7 = "現状からすると2～3割程度出荷出来なくなるのは目に見えています。"
                    msg8 = "担当者である高垣、部署長である岡田両者とも何も手を打たずにいます。"
                    msg9 = "ある部署から「2024年問題は大丈夫?」と聞かれたそうですが、自信をもって「大丈夫」という間抜けぶり。"
                    st.text(msg1)
                    st.text(msg2)
                    st.text(msg3)
                    st.text(msg4)
                    st.text(msg5)
                    st.text(msg6)
                    st.text(msg7)
                    st.text(msg8)
                    st.text(msg9)

                    st.success('【研究・開発部】', icon="✅")
                    msg1 = "開発職は、基礎研究、応用研究で得られた知識や法則、現象を元に具体的な商品やサービスの開発を行います。"
                    msg2 = "営業職などの消費者と距離が近い部門と連携して市場のニーズを把握したり新商品の企画を推進する能力が"
                    msg3 = "求められます。"
                    msg4 = "また、最も商品やサービスに関して知識を持っていることから、営業と同行して客先に説明するといった場面"
                    msg5 = "もありコミュニケーション能力が必要となります。"
                    msg6 = "非常に多くの経験ができる点、自分が関わった研究成果が形になって世の中に広げられる点に魅力を感じる人が"
                    msg7 = "多いようです。"
                    msg8 = "この研究・開発部は別会社となっているようで「池田食研㈱」という名前になっているようです。"
                    msg9 = "この会社の社長が福松です。"
                    msg10 = "会社は、「現場社員の熱意で決まる」と言っていいと思います。"
                    msg11 = "しかし、社内においては人望がなく、自分と反りが合わない人は遠ざけている人物です。"
                    msg12 = "会社の実態（＝社長の実力）がわかる一例として、最近将来を嘱望された中堅社員の退職が相次ぎ"
                    msg13 = "ヘッドハンティングされ会社を辞めています。"
                    msg14 = "中堅社員は、コア人材です。企業を支える存在のことです。"
                    msg15 = "そのコア人材の働きにより、企業の成績が大きく変わりますが、その人材が流出している現状です。"

                    st.text(msg1)
                    st.text(msg2)
                    st.text(msg3)
                    st.text(msg4)
                    st.text(msg5)
                    st.text(msg6)
                    st.text(msg7)
                    st.text(msg8)
                    st.text(msg9)
                    st.text(msg10)
                    st.text(msg11)
                    st.text(msg12)
                    st.text(msg13)
                    st.text(msg14)
                    st.text(msg15)

                    st.info('以下、随時更新予定．．．', icon="ℹ️")
                    st.success('【生産技術部】', icon="✅")
                    st.success('【総務部】', icon="✅")
                    st.success('【岡山アグリフーズ】', icon="✅")
                    st.success('【分析】', icon="✅")
                    st.success('【品質情報室】', icon="✅")
                    st.success('【バイオプロダクツ】', icon="✅")
                    st.success('【開発】', icon="✅")
                    st.success('【業務推進室】', icon="✅")
                    st.success('【S精製】', icon="✅")
                    st.success('【ITK(物流部門)】', icon="✅")
                    st.success('【ITS(システム部門)】', icon="✅")
                    st.success('【ソラサン(北海道)】', icon="✅")
                    st.success('【日本リコス(手城)】', icon="✅")
                    st.success('【日本リコス(笠岡)】', icon="✅")
                    st.success('【日本リコス(松浜)】', icon="✅")
                    st.success('【人事部付き】', icon="✅")
                    st.success('【東京】', icon="✅")
                    st.success('【大阪】', icon="✅")
                    st.success('【名古屋】', icon="✅")
                    st.success('【広島】', icon="✅")
                    st.success('【福山】', icon="✅")
                    st.success('【福岡】', icon="✅")
                    st.success('【鹿児島】', icon="✅")
                    st.success('【南関東】', icon="✅")
                    st.success('【キャラメライフ】', icon="✅")
                    st.success('【キサイフーズ】', icon="✅")
                    st.success('【上越フーズ】', icon="✅")
                    st.success('【タヌマフーズ】', icon="✅")
     
                      
                    
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
