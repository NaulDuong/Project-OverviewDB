### Đẩy dữ liệu orderall
df=pd.read_excel('D:\DAF\cty\Order.all.1234.xlsx')
from sqlalchemy import create_engine
def get_connection():
    return create_engine(url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format('root','', 'localhost', 3306, 'derrick'))

engine=get_connection()

# Insert dữ liệu vào table
df.to_sql('orders',engine, if_exists='append', index=False)