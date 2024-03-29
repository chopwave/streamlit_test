import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

input_num = st.number_input('Input a number', value=0)

result = input_num ** 2
st.write('Result: ', result)

st.title('streamlit Tutorial')
st.header('This is a header')
st.subheader('This is a subheader')
st.text('Hello World!')

# st.write()はMarkdown表記対応
st.write('# headline1')
# 以下のように明示的に書くことも可能
st.markdown('# headline2')

st.write(['apple', 'orange', 'banana'])

# ダミーデータの作成
df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [25, 30],
    'gender': ['female', 'male']
})

# DataFrameを表示
st.write(df)
# st.dataframe()でも表示可能
st.dataframe(df)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write(uploaded_file)

if st.button('Say hello'):
    st.write('Hello World!')

if st.checkbox('Show/Hide'):
    st.write('Some text')

option = st.radio(
    'Which number do you like best?', 
    ['1', '2', '3']
)

option = st.selectbox(
    'Which number do you like best?', 
    ['1', '2', '3']
)

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    default=['Yellow', 'Red'] # デフォルトの設定
)

value = st.slider('Select a value', 0, 100, 50) # min, max, default

# テキスト入力ボックス
text_input = st.text_input('Input', 'Input some text here.')
# テキストエリア
text_area = st.text_area('Text Area', 'Input some text here.')

# ボタンを押したら3秒間出力を待つ
if st.button('start'):
    with st.spinner('processiong...'):
        time.sleep(3)
        st.write('end!')

# Sidebarの選択肢を定義する
options = ["Option 1", "Option 2", "Option 3"]
choice = st.sidebar.selectbox("Select an option", options)

# Mainコンテンツの表示を変える
if choice == "Option 1":
    st.write("You selected Option 1")
elif choice == "Option 2":
    st.write("You selected Option 2")
else:
    st.write("You selected Option 3")

# ダミーデータの作成
df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [25, 30],
    'gender': ['female', 'male']
})

# 2列のカラムを作成
col1, col2 = st.columns(2)

# col1にテキストを表示
with col1:
    st.header("Column 1")
    st.write("This is column 1.")

# col2にDataFrameを表示
with col2:
    st.header("Column 2")
    # DataFrameを表示
    st.write(df)

# Warningの非表示
st.set_option('deprecation.showPyplotGlobalUse', False)

#### ---- #### ---- ####
# グラフを描画する
def plot_graph():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    st.pyplot()

# グラフを表示するボタンを表示する
if st.button('Plot graph'):
    plot_graph()

#### ---- #### ---- ####
# データ生成
x = np.linspace(0, 10, 100)
y = x + np.random.randn(100) 

# プロット
plt.plot(x, y, label="test")

# 凡例の表示
plt.legend()

# プロット表示(設定の反映)
plt.show()

#### ---- #### ---- ####
# データ生成
x = np.linspace(0, 10, 100)
y = x + np.random.randn(100) 

# Figureの初期化
fig = plt.figure(figsize=(12, 8)) #...1

# Figure内にAxesを追加()
ax = fig.add_subplot(111) #...2
ax.plot(x, y, label="test") #...3

# 凡例の表示
plt.legend()

# プロット表示(設定の反映)
plt.show()

#### ---- #### ---- ####
# データ生成
x = np.linspace(0, 10, 100)
y = x + np.random.randn(100) 

# Figureの初期化
fig = plt.figure(figsize=(12, 8))

# Figure内にAxesを追加
ax = fig.add_axes([0,0,1,1])
ax.plot(x, y, label="test")

# 凡例の表示
plt.legend()

# プロット表示(設定の反映)
plt.show()
# データ生成
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# プロット領域(Figure, Axes)の初期化
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

# 棒グラフの作成
ax1.bar([1,2,3],[3,4,5])
ax2.barh([0.5,1,2.5],[0,1,2])
ax3.scatter(y1, y2)

# 水平線、垂直線を入れる
ax3.axhline(0.45)
ax3.axvline(0.65)

plt.show()

#### ---- #### ---- ####
# プロット領域の初期化(今回は1行2列の配列)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))

# データのプロット
ax1.bar([1,2,3], [3,4,5])
ax2.barh([0.5, 1, 2.5], [0,1,2])

plt.show()

#### ---- #### ---- ####
x = np.linspace(0, 100, 101)
y = np.random.randn(101)

plt.plot(x, y, color=(0,0,1))

plt.show()

#### ---- #### ---- ####
x = np.linspace(0, 100, 101)
y = np.random.randn(101)

plt.plot(x, y, color="#0F0F0F")

plt.show()
