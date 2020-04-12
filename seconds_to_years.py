total_sec=int(input("몇 초 경과했습니까?:"))
year=total_sec//31536000
total_sec=total_sec%31536000
week=total_sec//604800
total_sec=total_sec%604800
day=total_sec//86400
total_sec=total_sec%86400
hour=total_sec//3600
total_sec=total_sec%3600
minute=total_sec//60
sec=total_sec%60
print(year,"년",week,"주",day,"일",hour,"시간",minute,"분",sec,"초 경과했습니다.")