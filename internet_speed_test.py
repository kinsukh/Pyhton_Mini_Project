## pip install speedtest-cli
import speedtest


def internet_speed_test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    download_speed = s.download() / 1e6
    upload_speed = s.upload() / 1e6
    ping = s.results.ping
    return download_speed, upload_speed, ping

## print(result of speed test)
download_speed, upload_speed, ping = internet_speed_test()
print(f"Download Speed: {download_speed} Mbps")
print(f"Upload Speed: {upload_speed} Mbps")
print(f"Ping: {ping} ms")



