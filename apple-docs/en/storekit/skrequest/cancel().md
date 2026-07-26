---
title: cancel()
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skrequest/cancel()
source_url: 'https://developer.apple.com/documentation/storekit/skrequest/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skrequest/cancel%28%29.json'
content_hash: 'sha256:19063c47eeb8b79d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKRequest](../skrequest.md)

# cancel()

<sub>Instance Method</sub>

Cancels a previously started request.

> [!warning] Deprecated
> No longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancel()
```

## Discussion

When you cancel a request, the delegate is not called with an error.

## See Also

### Controlling the Request

- [- start](<start().md>) — Sends the request to the Apple App Store. _(deprecated)_
