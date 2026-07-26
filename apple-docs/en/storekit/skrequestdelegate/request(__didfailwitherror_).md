---
title: 'request(_:didFailWithError:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skrequestdelegate/request(_:didfailwitherror:)'
source_url: 'https://developer.apple.com/documentation/storekit/skrequestdelegate/request(_:didfailwitherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skrequestdelegate/request%28_%3Adidfailwitherror%3A%29.json'
content_hash: 'sha256:21f5eb806684fc81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKRequestDelegate](../skrequestdelegate.md)

# request(_:didFailWithError:)

<sub>Instance Method</sub>

Tells the delegate that the request failed to execute.

> [!warning] Deprecated
> No longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func request(_ request: SKRequest, didFailWithError error: any Error)
```

## Parameters

- `request` — The request that failed.

- `error` — The error that caused the request to fail.

## Discussion

When the request fails, your application should release the request. The [- requestDidFinish:](<requestdidfinish(__).md>) method is not called after this method is called.
