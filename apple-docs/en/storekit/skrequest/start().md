---
title: start()
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skrequest/start()
source_url: 'https://developer.apple.com/documentation/storekit/skrequest/start()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skrequest/start%28%29.json'
content_hash: 'sha256:c874a009da6dcf85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKRequest](../skrequest.md)

# start()

<sub>Instance Method</sub>

Sends the request to the Apple App Store.

> [!warning] Deprecated
> No longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func start()
```

## Discussion

The results for a request are sent to the request’s delegate.

## See Also

### Related Documentation

- [In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)

### Controlling the Request

- [- cancel](<cancel().md>) — Cancels a previously started request. _(deprecated)_
