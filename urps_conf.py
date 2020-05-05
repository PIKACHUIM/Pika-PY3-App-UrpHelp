import os
import requests
http_main = requests.session()
http_week = ['一', '二', '三', '四', '五', '六', '日','  ']
http_urls_zyxk = "http://zhjw.scu.edu.cn/student/courseSelect/courseSelect/index"
http_urls_xkl1 = "http://zhjw.scu.edu.cn/student/courseSelect/courseSelectResult/index"
http_urls_xkl2 = "http://zhjw.scu.edu.cn/student/courseSelect/thisSemesterCurriculum/callback"
http_urls_jdjs = "http://zhjw.scu.edu.cn/student/integratedQuery/scoreQuery/coursePropertyScores/index#id_1"
http_urls_jddt = "http://zhjw.scu.edu.cn/student/integratedQuery/scoreQuery/coursePropertyScores/callback"
http_urls_kclb = "http://zhjw.scu.edu.cn/student/courseSelect/freeCourse/courseList"
http_urls_post = "http://zhjw.scu.edu.cn/student/courseSelect/selectCourse/checkInputCodeAndSubmit"
http_head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}

def urps_outs(urps_data=0):
    if urps_data==0:
        print("-----------------------------------------------------------------------------------------------------")
    elif urps_data==1:
        print("----------------------------------------------搜索结果-----------------------------------------------")
        print()
        print("#                课程名           校区 余量  位置   教室    周数    时间    教师")
        print("-----------------------------------------------------------------------------------------------------")
    elif urps_data==-1:
        print()
        print("**************************************列表为空，请检查输入内容**************************************")
        print()
        input("--------------------------------------------按回车键返回--------------------------------------------")
    elif urps_data=="zdqk":
        print("----------------------------------------------自动抢课-----------------------------------------------")
    elif urps_data=='zzqk':
        print("----------------------------------------------正在抢课-----------------------------------------------")
    elif urps_data=="back":
        input("--------------------------------------------按回车键返回---------------------------------------------")
    elif urps_data=='succ':
        os.system('color 2f')
        print()
        print()
        print("                                       ■■■■■■■■■■■")
        print("                                       ■                  ■")
        print("                                       ■      抢课成功    ■")
        print("                                       ■                  ■")
        print("                                       ■■■■■■■■■■■")
        print("[指令发送OK]：仅表示成功提交，不保证抢到")
        print("[指令发送OK]：如果失败，可能是别人先提交")
        print()
    elif urps_data=='fail':
        os.system('color 4f')
        print()
        print()
        print("                                       ■■■■■■■■■■■")
        print("                                       ■                  ■")
        print("                                       ■      抢课失败    ■")
        print("                                       ■                  ■")
        print("                                       ■■■■■■■■■■■")
        print()
        print("----------------------------------------------5s后重试-----------------------------------------------")
    elif urps_data=='next':
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>按回车下一页>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    elif urps_data=='nete':
        print("[严重的错误]：网络连接中断，请确保网络稳定")
    elif urps_data=='iner':
        print("[输入不正确]：请重新输入")
    elif urps_data=='retr':
        input("--------------------------------------------按回车键重试---------------------------------------------")