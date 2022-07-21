import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="STFU_빈센조", page_icon="STFU.png")

st.set_option('deprecation.showPyplotGlobalUse', False)


dataset = pd.read_csv('sand_final_result.csv')


st.sidebar.title("편의점 리뷰 보기")
st.sidebar.image("we.jpg")
input = st.sidebar.selectbox("상품을 입력하세요!", ["gs25 아이돌인기샌드위치", "cu 생크림딸기샌드위치", "세븐일레븐 마늘빵맛샌드위치"])


labels = 'P', 'N'
sizes = [60, 40]
explode = (0, 0.1)


from os import name
import streamlit as st

def select_goods(dataset, input):
    for name in dataset['제품명']:
        if name == input:
            new_df = dataset[dataset['제품명'] == name]
            return new_df


# streamlit을 이용해 화면을 보여준다.
def show_page():

    
    new_df = select_goods(dataset, input).reset_index(drop=True)
    new_df = new_df.transpose().astype(str)
    new_df.rename(columns = {0: "정보"}, inplace=True)

    bar_df = pd.DataFrame({'Down' : [float(new_df.iloc[2])],
                      'Up' : [1 - float(new_df.iloc[2])]})


    # row2.config
    row1_spacer1, row1_1, row2_spacer2, row1_2, row2_spacer3,row2_3 = st.columns(
        (.4, 1.6, .1, 1.6, .1, .4)
        )


    # row2.config
    row2_spacer1, row2_1, row2_spacer2, row2_2, row2_spacer3,row2_3 = st.columns(
        (.4, 1.6, .1, 1.6, .1, .4)
        )

    # 상세설정
    with row1_1:

        if input == "gs25 아이돌인기샌드위치":
            st.image("gs_pic.jpg", width=150)
        elif input == "cu 생크림딸기샌드위치":
            st.image("cu_pic.jpg", width=150)
        elif input == "세븐일레븐 마늘빵맛샌드위치":
            st.image("seven_pic.jpg", width=150)

    # set row2
    with row1_2:

        st.dataframe(new_df)

    with row2_1:

        if input == "gs25 아이돌인기샌드위치":
            st.image("gs_wordcloud.jpg", width=300)
        elif input == "cu 생크림딸기샌드위치":
            st.image("cu_wordcloud.jpg", width=300)
        elif input == "세븐일레븐 마늘빵맛샌드위치":
            st.image("seven_wordcloud.jpg", width=300)
        

    # set row2
    with row2_2:
        fig, ax2 = plt.subplots(figsize=(10, 5))
        
        fig = plt.plot()
        bar_df.plot(kind='bar', stacked=True, color=['blue', '#C6B6B6'], width=0.1)
        st.pyplot(fig)


if __name__ == "__main__":
    show_page()