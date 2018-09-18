from common.base import base

class matcher(base):

    def addOrder(self,amount,marketId,price,side):
        query="""mutation ($marketId: String!, $side: OrderSide!, $price: String!, $amount: String!) {
  addOrder(input: {marketUuid: $marketId, side: $side, price: $price, amount: $amount}) {
    order {
      ...Order
      __typename
    }
    __typename
  }
}

fragment Order on Order {
  id
  marketUuid
  price
  avgDealPrice
  amount
  filledAmount
  side
  state
  insertedAt
  updatedAt
  __typename
}
"""
        operationName = None
        variables = {
            "amount":amount,
            "marketId":marketId,
            "price":price,
            "side":side}
        return self.request(query, operationName, variables)

    def cancelAllOrders(self,marketId):
        query="""mutation ($marketId: String) {
  cancelAllOrders(input: {marketUuid: $marketId}) {
    orders {
      id
      __typename
    }
    __typename
  }
}
"""
        operationName = None
        variables = {
            "marketId":marketId
            }
        return self.request(query, operationName, variables)
    
    def cancelOrder(self,id):
        query="""mutation ($id: String!) {
  cancelOrder(input: {id: $id}) {
    clientMutationId
    __typename
  }
}
"""
        operationName = None
        variables = {
            "id":id
            }
        return self.request(query, operationName, variables)
    
    def bars(self,marketId,period,startTime=None,endTime=None):
        query="""query ($marketId: String!, $period: BarPeriod!, $startTime: DateTime, $endTime: DateTime) {
  bars(marketUuid: $marketId, period: $period, startTime: $startTime, endTime: $endTime, order: DESC, limit: 1000) {
    time
    open
    high
    low
    close
    volume
    __typename
  }
}"""
        operationName = None
        variables = {
            "marketId":marketId,
            "period":period,
            }
        if startTime:
            variables["startTime"]=startTime
        if endTime:
            variables["endTime"]=endTime
        return self.request(query, operationName, variables)
    
    def depth(self,limit,marketId):
        query="""query ($marketId: String!, $limit: Int) {
    depth(marketUuid: $marketId, limit: $limit) {
    ...OrderBook
    __typename
  }
}

fragment OrderBook on Depth {
  bids {
    amount
    price
    __typename
  }
  asks {
    amount
    price
    __typename
  }
  __typename
}
"""
        operationName = None
        variables = {
            "limit":int(limit),
            "marketId":marketId
            }
        import json
        print(json.dumps(variables))
        return self.request(query, operationName, variables)
    
    def myAccounts(self,assetIds=None):
        query="""query ($assetIds: [String!]) {
  myAccounts(assetUuids: $assetIds) {
    ...Account
    __typename
  }
}

fragment Account on Account {
  assetUuid
  balance
  lockedBalance
  __typename
}
"""
        operationName = None
        variables = {}
        if assetIds:
            variables["assetIds"]=[x for x in assetIds.split(",")]
        return self.request(query, operationName, variables)
    
    def myOrders(self,limit,marketId=None,state=None):
        query="""query ($marketId: String, $limit: Int!, $state: OrderState) {
  myOrders(marketUuid: $marketId, last: $limit, state: $state) {
    nodes {
      ...Order
      __typename
    }
    __typename
  }
}

fragment Order on Order {
  id
  marketUuid
  price
  avgDealPrice
  amount
  filledAmount
  side
  state
  insertedAt
  updatedAt
  __typename
}
"""
        operationName = None
        variables = {
            "limit":int(limit),
            }
        if marketId:
            variables["marketId"]=marketId
        if state:
            variables["state"]=state
        return self.request(query, operationName, variables)
    
    def myTrades(self,marketId=None,afterTime=None,beforeTime=None,limit=None):
        query="""query ($marketId: String, $limit: Int, $beforeTime: DateTime, $afterTime: DateTime) {
  myTrades(marketUuid: $marketId, last: $limit, beforeTime: $beforeTime, afterTime: $afterTime) {
    nodes {
      ...Trade
      __typename
    }
    __typename
  }
}

fragment Trade on Trade {
  id
  marketUuid
  takerSide
  viewerSide
  price
  amount
  insertedAt
  __typename
}
"""
        operationName = None
        variables = {}
        if marketId:
            variables["marketId"]=marketId
        if afterTime:
            variables["afterTime"]=afterTime
        if beforeTime:
            variables["beforeTime"]=beforeTime
        if limit:
            variables["limit"]=int(limit)
        return self.request(query, operationName, variables)
    
    def ticker(self):
        pass
    def tickers(self):
        query="""{
  tickers {
    ...Ticker
    __typename
  }
}

fragment Ticker on Ticker {
  marketUuid
  close
  low
  high
  dailyChangePerc
  volume
  __typename
}"""
        operationName = None
        variables = {}
        return self.request(query, operationName, variables)
    
    def trades(self,marketId=None,limit=None):
        query="""query ($marketId: String, $limit: Int) {
  trades(marketUuid: $marketId, last: $limit) {
    nodes {
      ...Trade
      __typename
    }
    __typename
  }
}

fragment Trade on Trade {
  id
  marketUuid
  takerSide
  viewerSide
  price
  amount
  insertedAt
  __typename
}"""
        operationName = None
        variables = {}
        if  limit:
            variables["limit"]=int(limit)
        if marketId:
            variables["marketId"]=marketId
        return self.request(query, operationName, variables)
    
    def assetPrices(self,baseAssets,quoteAsset):
        query="""query ($baseAssets: [String]!, $quoteAsset: String!) {
  assetPrices(baseAssets: $baseAssets, quoteAsset: $quoteAsset) {
    baseAsset
    price
    __typename
  }
}"""
        operationName = None
        variables = {
            "baseAssets":[x for x in baseAssets.split(",")],
            "quoteAsset":quoteAsset,
            }
        return self.request(query, operationName, variables)