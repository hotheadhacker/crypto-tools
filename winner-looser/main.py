from modules import worker
print("Hello Winner")
print("💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰")
print("======Welcome To Crypto Winner/Looser Coins of Last 24 Hrs========")
print("======(v1.0 Alpha) Developed by: github.com/hotheadhacker ========")

# print("🚀 The Market is Up 24% From Last 24 hrs 📈")
# print("🔻 The Market is Up 1% From Last 24 hrs 📉")
print(worker.getOverallMarketTrend())
print(worker.winners())
print(worker.losers())