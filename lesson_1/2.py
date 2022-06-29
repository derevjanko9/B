import requests

url = 'https://api.vk.com/method/groups.get?v=5.81&access_token=vk1.a.LgM65oqM535b6zqCOoNOXfL-9vkXsbq7SEGM56WegDU3-Hx2hkvNN6SATk1dKpo2SReAusOBdfv-sjr1A1_Up-QQMwyfR51p6nvvzS_EK3eEMRhGkCCTBprmU0ZkdE45PVLdWr-KvgDef1DzJOWBrldZCoIJKI7AWwetcti3fG4w3_uceZb5XWK2Xr4f9KVl'
response = requests.get(url)
print(response.json())
