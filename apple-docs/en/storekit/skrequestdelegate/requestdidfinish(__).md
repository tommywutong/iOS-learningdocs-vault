---
title: 'requestDidFinish(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skrequestdelegate/requestdidfinish(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/skrequestdelegate/requestdidfinish(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skrequestdelegate/requestdidfinish%28_%3A%29.json'
content_hash: 'sha256:358a5cd394ca4ba1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKRequestDelegate](../skrequestdelegate.md)

# requestDidFinish(_:)

<sub>Instance Method</sub>

Tells the delegate that the request has completed.

> [!warning] Deprecated
> No longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func requestDidFinish(_ request: SKRequest)
```

## Parameters

- `request` — The request that completed.

## Discussion

This method is called after all processing of the request has been completed. Typically, subclasses of [SKRequest](../skrequest.md) require the delegate to implement additional methods to receive the response. When this method is called, your delegate receives no further communication from the request and can release it.

## See Also

### Related Documentation

- [In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)
