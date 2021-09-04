import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!'

latest_ineration = st.empty()
bar = st.progress(0)

for i in range(100):
     latest_ineration.text(f'Iteration {i+1}')
     bar.progress(i + 1)
     time.sleep(0.1)

'Done!!!!!'







# st.write('Interactive Widgets')
# expander1 = st.expander('お問合せ1')
# expander1.write('問い合わせ1の回答')
# expander2 = st.expander('お問合せ2')
# expander2.write('問い合わせ2の回答')
# expander3 = st.expander('お問合せ3')
# expander3.write('問い合わせ3の回答')

# 2カラムレイアウト
# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#      right_column.write('ここは右カラム')

# st.sidebar.write('Interactive Widgets')
# text = st.sidebar.text_input('あなたの趣味をおしえて下さい')
# condition = st.sidebar.slider('あなたの今の調子は?', 0, 100, 50)
# 'あなたの趣味:', text
# 'コンディション: ', condition

# テキスト入力
# text = st.text_input('あなたの趣味をおしえて下さい')
# 'あなたの趣味:', text
# スライダー
# condition = st.slider('あなたの今の調子は?', 0, 100, 50)
# 'コンディション: ', condition

# セレクトボックス
# option = st.selectbox(
#     'あなたの好きな数字を教えてください？',
#     list(range(1, 11))
# )
# チェックボックス
# 'あなたの好きな数字は、', option, 'です。'
# if st.checkbox('Show Image'):
#     img = Image.open('005.JPG')
#     st.image(img, caption='Hiroki Yoshida', use_column_width=True)

# df = pd.DataFrame(
#       np.random.rand(100, 2)/[50, 50] + [35.69,139.70],
#       columns=['lat', 'lon']
# )
# st.map(df)
# st.table(df.style.highlight_max(axis=0))
# st.write('Display Image')
