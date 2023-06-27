from sqlalchemy import create_engine
import pandas as pd
import streamlit as st
from sqlalchemy import inspect

connection_string = "postgresql+psycopg2://{user}:{pass}@{ip}:{port}}/postgres"
connect_args = {
    "options": "-csearch_path={}".format("{schema}")
}

engine = create_engine(connection_string, connect_args=connect_args)


def upload_csv_to_postgres(csv_file, table_name):
    df = pd.read_csv(csv_file, encoding='UTF-8')
    df.to_sql(table_name, con=engine, if_exists='replace')


def view_data(table_name):
    query = f'SELECT * FROM viz_temp."{table_name}"'
    df = pd.read_sql(query, con=engine)
    st.dataframe(df)


def get_table_names():
    insp = inspect(engine)
    return insp.get_table_names(schema='viz_temp')

def view_before_delete(table_name):
    query = f'SELECT * FROM viz_temp."{table_name}" LIMIT 10'
    df = pd.read_sql(query,con=engine)
    st.dataframe(df)
    

def view_table_data(table_name):
    query = f'SELECT * FROM viz_temp."{table_name}" LIMIT 100'
    df = pd.read_sql(query, con=engine)
    return df


def drop_table(table_name):
    query = f'DROP TABLE IF EXISTS viz_temp."{table_name}"'
    engine.execute(query)


def view_data_from_all_tables():
    table_names = get_table_names()
    for table_name in table_names:
        st.write(f"Table: {table_name}")
        df = view_table_data(table_name)
        st.write(df)
        st.write('---')  # Add a separator between tables


def main():
    st.title('Analyst & Viz Team Tools')
    st.header('Custom ingesting data in database for vizualization ')

    # File upload section
    uploaded_file = st.file_uploader('Upload CSV file')
    if uploaded_file is not None:
        table_name = st.text_input('Enter table name')
        if st.button('Upload'):
            upload_csv_to_postgres(uploaded_file, table_name)
            st.success('CSV uploaded successfully.')

    # View data section
    st.header('View Data')
    table_list = get_table_names()
    selected_table = st.selectbox('Select table', table_list)
    if selected_table:
        view_data(selected_table)

    # Drop table section
    st.header('Drop Table')
    selected_table = st.selectbox('Select Table', table_list)
    view_before_delete(selected_table)
    if st.button('Delete'):
        drop_table(selected_table)
        st.success('Table dropped successfully.')


if __name__ == '__main__':
    main()
