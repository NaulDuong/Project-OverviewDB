import pandas as pd

def convert_chuoi(a):
    return a.replace('-', '')


def convert_per(a):
    return a.str.replace(',', '').str.replace('%', '').astype('float') / 100


def convert_int(a):
    return a.str.replace('.', '').astype('int')/100

def convert_weight(a):
    return a.replace('.','').astype('float')

def convert_money(a):
    return a.replace('.', '').astype('int')

## Xử lý file orderall
df=pd.read_excel('D:\DAF\cty\Order.all.123.xlsx')
df['Cân nặng sản phẩm']=convert_weight(df['Cân nặng sản phẩm'])
df['Tổng cân nặng']=convert_weight(df['Tổng cân nặng'])
df['Cân nặng sản phẩm']=convert_weight(df['Cân nặng sản phẩm'])
df['Giá gốc']=convert_money(df['Giá gốc'])
df['Người bán trợ giá']=convert_money(df['Người bán trợ giá'])
df['Được Shopee trợ giá']=convert_money(df['Được Shopee trợ giá'])
df['Tổng số tiền được người bán trợ giá']=convert_money(df['Tổng số tiền được người bán trợ giá'])
df['Giá ưu đãi']=convert_money(df['Giá ưu đãi'])
df['Tổng giá bán (sản phẩm)']=convert_money(df['Tổng giá bán (sản phẩm)'])
df['Tổng giá trị đơn hàng (VND)']=convert_money(df['Tổng giá trị đơn hàng (VND)'])
df['Mã giảm giá của Shop']=convert_money(df['Mã giảm giá của Shop'])
df['Hoàn Xu']=convert_money(df['Hoàn Xu'])
df['Mã giảm giá của Shopee']=convert_money(df['Mã giảm giá của Shopee'])
df['Giảm giá từ combo Shopee']=convert_money(df['Giảm giá từ combo Shopee'])
df['Giảm giá từ Combo của Shop']=convert_money(df['Giảm giá từ Combo của Shop'])
df['Số tiền được giảm khi thanh toán bằng thẻ Ghi nợ']=convert_money(df['Số tiền được giảm khi thanh toán bằng thẻ Ghi nợ'])
df['Phí vận chuyển (dự kiến)']=convert_money(df['Phí vận chuyển (dự kiến)'])
df['Phí vận chuyển mà người mua trả']=convert_money(df['Phí vận chuyển mà người mua trả'])
df['Phí vận chuyển tài trợ bởi Shopee (dự kiến)']=convert_money(df['Phí vận chuyển tài trợ bởi Shopee (dự kiến)'])
df['Phí trả hàng']=convert_money(df['Phí trả hàng'])
df['Tổng số tiền người mua thanh toán']=convert_money(df['Tổng số tiền người mua thanh toán'])
df['Phí cố định']=convert_money(df['Phí cố định'])
df['Phí Dịch Vụ']=convert_money(df['Phí Dịch Vụ'])
df['Phí thanh toán']=convert_money(df['Phí thanh toán'])
df['Tiền ký quỹ']=convert_money(df['Tiền ký quỹ'])

df.to_excel('D:\DAF\cty\Order.all.1234.xlsx',sheet_name='Order', index=False)