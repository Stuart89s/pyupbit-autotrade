import pyupbit

access = "W0ODVTu70XbtN580h7xCFP2WC3obxXGVNj50R7p0"
secret = "UuO2gv2fb8AWrlyaVUkgkIpNkPX5ooZNu8RmsKgV"
upbit = pyupbit.Upbit(access, secret)

krw = upbit.get_balance("KRW")    # KRW-BTC 조회

for i in range(10):
    if krw > 0:
        continue
    else:
        print(3)
