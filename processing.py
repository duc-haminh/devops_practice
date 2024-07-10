import pandas as pd

def process_data(data):
    df = pd.DataFrame(data)
    df['Content_question'] = df['Content_question'].astype(str)
    df['Answer'] = df['Answer'].astype(str)
    df['Content_question'] = df['Content_question'].str.replace(r'<.*?>', '', regex=True)
    df['Content_question'] = df['Content_question'].str.replace(r'[\r\n]', '', regex=True)
    df['Content_question'] = df['Content_question'].str.replace(r'|Dạ|', '', regex=True)
    df['Answer'] = df['Answer'].str.replace(r'<.*?>', '', regex=True)
    df['Answer'] = df['Answer'].str.replace(r'[\r\n]', '', regex=True)
    df['Answer'] = df['Answer'].str.replace(r'|dạ chào bạn, |, |dạ chào bạn |, |dạ |, |Chào bạn.|, |chào bạn.|, |Chào bạn .|, |chào bạn .|' , '', regex=True)

    return df
