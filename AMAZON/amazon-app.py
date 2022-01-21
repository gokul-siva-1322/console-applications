products=[
{"merchantId":"1","productId":"1001","productName":"iPhone","price":50000,"discount":10,"stock":10,"sale":0,"profit":0},
{"merchantId":"2","productId":"1001","productName":"iPhone","price":15000,"discount":50,"stock":10,"sale":0,"profit":0},
{"merchantId":"3","productId":"1001","productName":"iPhone","price":25000,"discount":30,"stock":10,"sale":0,"profit":0},
{"merchantId":"1","productId":"1002","productName":"Mac Book Pro","price":30000,"discount":10,"stock":10,"sale":0,"profit":0},
{"merchantId":"2","productId":"1002","productName":"Mac Book Pro","price":17000,"discount":50,"stock":10,"sale":0,"profit":0},
{"merchantId":"3","productId":"1002","productName":"Mac Book Pro","price":5000,"discount":30,"stock":10,"sale":0,"profit":0},
{"merchantId":"1","productId":"1002","productName":"Apple Watch","price":10000,"discount":10,"stock":10,"sale":0,"profit":0},
{"merchantId":"2","productId":"1002","productName":"Apple Watch","price":95000,"discount":50,"stock":10,"sale":0,"profit":0},
{"merchantId":"3","productId":"1002","productName":"Apple Watch","price":55000,"discount":30,"stock":10,"sale":0,"profit":0}
]


merchants=[
{"merchantId":"1","merchantName":"aaditi","password":"1234","merchantStatus":"Approved","merchantprofit":1000},
{"merchantId":"2","merchantName":"vijay","password":"1234","merchantStatus":"Approved","merchantprofit":1000},
{"merchantId":"3","merchantName":"abarna","password":"1234","merchantStatus":"Approved","merchantprofit":1000},
]

users=[
{"userId":"5001","userName":"siva","password":"1234", "cart":[],"balance":24500}
]

orders=[
{"orderId":"7001","merchantId":"1","userId":"5001","productId":"1001","productName":"iPhone 5s","orderstatus":"Received","itemsneed":3,"paid":2400,"review":["* * * * ","Good Product"]}
] 

products=[
{"merchantId":"1","productId":"1001","productName":"iPhone 5s","price":25000,"discount":10,"stock":10,"sale":0,"profit":0}
]
merchants=[
{"merchantId":"1","merchantName":"aaditi","password":"1234","merchantStatus":"Approved","merchantprofit":1000}
]


print(*sorted(products,key = lambda x : x["price"],reverse=True),sep="\n")

products=[{"merchantId":"1","productId":"1001","productName":"iPhone 5s","price":25000,"discount":10,"stock":10}]
merchants=[{"merchantId":"1","merchantName":"aaditi","password":"1234","merchantStatus":"Approved"}]
