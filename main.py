import subprocess
import sys
import time

npc_str = "npc.exe -server={} -vkey={} -type={}"


def get_ip(domain, dns):
    res = subprocess.Popen("nslookup {} {}".format(domain, dns), stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE).communicate()[0]
    response = res.decode("GBK")
    res_list = response.split("\r\n")
    ip = str.strip(res_list[len(res_list) - 3])
    if ip.startswith("名称"):
        return None
    else:
        return str.strip(ip.replace("Address:", ""))


def npc(domain, vkey, type):
    connect_str = npc_str.format(domain, vkey, type)
    print(connect_str)
    pi = subprocess.Popen(connect_str, shell=False,
                          stdout=subprocess.PIPE)

    for i in iter(pi.stdout.readline, 'b'):
        out = i.decode("GBK")
        print(out)
        if "Reconnecting" in out or "reconnected in five seconds" in out:
            break

    pi.stdout.close()
    pi.terminate()
    pi.kill()


sleep_time = 10

if __name__ == '__main__':
    # npc -server=127.0.0.1:7200 -vkey=0ucn6wx7e9zuz4yg -type=tcp
    try:
        # domain = sys.argv[1]
        # port = sys.argv[2]
        # vkey = sys.argv[3]
        # type = sys.argv[4]
        # dns = sys.argv[5]

        domain = 'www.yizems.cn'
        port = '6000'
        vkey = 'aaa'
        type = 'tcp'
        dns = 'f1g1ns1.dnspod.net'
        while True:
            ip = get_ip(domain, dns)
            if ip is None:
                print("域名无法解析:5秒后开始下次执行")
                time.sleep(sleep_time)
                continue

            print(ip)

            npc(ip + ":" + port, vkey, type)
            print("进程结束:5秒后开始下次执行")
            time.sleep(sleep_time)
    except Exception as e:
        print('发生错误,请检查命令')
        print(e)
        print('main domain port vkey type dns')
