import os
from pyicloud import PyiCloudService
print("🟢 正在连接中国区iCloud...")
api = PyiCloudService(
    os.environ['ICLOUD_CN_USERNAME'],
    os.environ['ICLOUD_CN_PASSWORD'],
    china_mainland=True,  # 关键参数
    client_id='com.apple.icloudweb',
    verify=True
)
print(f"✅ 登录成功: {api.account_info()['accountName']}")
# 测试下载第一张照片
first_photo = api.photos.all[0]
first_photo.download('/app/photo.jpg')
print(f"📸 已下载: {first_photo.filename}")
