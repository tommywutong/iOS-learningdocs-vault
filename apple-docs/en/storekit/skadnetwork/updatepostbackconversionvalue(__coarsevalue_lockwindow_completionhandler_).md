---
title: 'updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.1+, iPadOS 16.1+, Mac Catalyst 16.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/storekit/skadnetwork/updatepostbackconversionvalue(_:coarsevalue:lockwindow:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/storekit/skadnetwork/updatepostbackconversionvalue(_:coarsevalue:lockwindow:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skadnetwork/updatepostbackconversionvalue%28_%3Acoarsevalue%3Alockwindow%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:91e06bab01d7a778'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKAdNetwork](../skadnetwork.md)

# updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)

<sub>Type Method</sub>

Updates the fine and coarse conversion values and indicates whether to send the postback before the conversion window ends, and calls a completion handler if the update fails.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class func updatePostbackConversionValue(_ fineValue: Int, coarseValue: SKAdNetwork.CoarseConversionValue, lockWindow: Bool, completionHandler completion: (@Sendable ((any Error)?) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class func updatePostbackConversionValue(_ fineValue: Int, coarseValue: SKAdNetwork.CoarseConversionValue, lockWindow: Bool) async throws
```

## Parameters

- `fineValue` — An unsigned 6-bit value `≥0` and `≤63`. The app or the ad network defines the meaning of the fine conversion value.

- `coarseValue` — An [CoarseConversionValue](coarseconversionvalue.md) value of [SKAdNetworkCoarseConversionValueLow](coarseconversionvalue/low.md), [SKAdNetworkCoarseConversionValueMedium](coarseconversionvalue/medium.md), or [SKAdNetworkCoarseConversionValueHigh](coarseconversionvalue/high.md). The app or the ad network defines the meaning of the coarse conversion value.

- `lockWindow` — A Boolean value that indicates whether to send the postback before the conversion window ends. Use `true` to tell the system to send the postback without waiting for the end of the conversion window. The default value is `false`.

- `completion` — An optional completion handler you provide to catch and handle any errors this method encounters when you update a conversion value. Set this value to `nil` if you don’t provide a handler.

## Discussion

Call this method when the user first launches an app to register the app installation, and again to update conversion values as the user engages with the app. It’s up to your app to decide what the conversion values signify in your app, both the `fineValue` and the `coarseValue`.

This method supports ads signed with any verison of SKAdNetwork, and you can use it instead of calling [+ updatePostbackConversionValue:completionHandler:](<updatepostbackconversionvalue(__completionhandler_).md>) and [+ updatePostbackConversionValue:coarseValue:completionHandler:](<updatepostbackconversionvalue(__coarsevalue_completionhandler_).md>). The system automatically determines the method’s behavior based on the ad’s version, as the following sections describe — the app doesn’t need to know the ad version. To take advantage of the multiple postbacks available starting in version 4, use this method or [+ updatePostbackConversionValue:coarseValue:completionHandler:](<updatepostbackconversionvalue(__coarsevalue_completionhandler_).md>).

This method returns [SKANErrorInvalidConversionValue](../skanerror-swift.struct/code/invalidconversionvalue.md) if the `fineValue` is outside of the allowed range.

> [!important] Important
> The system ignores calls to this method if the `fineValue` is outside of the valid range. Valid conversion updates your app sends before or after an invalid conversion remain available.

### Update conversion values for ads signed with SKAdNetwork 4 or later

For ads that ad networks sign using version 4 or later, calling this method behaves as follows:

- Both the `fineValue` and `coarseValue` represent conversion values. The method ignores the `fineValue` after the first conversion window.
- Setting the `lockWindow` parameter to `true` indicates a final update for the conversion value for the current conversion window. The system ignores additional calls to update the conversion value until the end of the conversion window.
- Setting the `lockWindow` parameter to `false` continues updating the conversion value throughout the conversion window.

For information about the data you may receive in postbacks, see [Receiving postbacks in multiple conversion windows](../receiving-postbacks-in-multiple-conversion-windows.md).

### Update conversion values for ads signed with SKAdNetwork 3 or earlier

For ads that ad networks sign using version 3 or earlier, calling this method behaves as follows:

- The `fineValue` represents the conversion value.
- The method ignores the `coarseValue` and `lockWindow` parameters.
- There’s a single conversion period that ends after a rolling 24-hour timer expires. The 24-hour timer restarts each time the app calls this method with a valid conversion value greater than the previous value. When the timer expires, the conversion value is final and subsequent calls to this method have no effect.
- The device sends the postback 0–24 hours after the timer expires.
- The postback contains the final conversion value only if the postback data tier contains the value.

For more information about SKAdNetwork versions, see [SKAdNetwork release notes](../skadnetwork-release-notes.md).

## See Also

### Providing conversion information

- [+ updatePostbackConversionValue:coarseValue:completionHandler:](<updatepostbackconversionvalue(__coarsevalue_completionhandler_).md>) — Updates the fine and coarse conversion values, and calls a completion handler if the update fails.
- [CoarseConversionValue](coarseconversionvalue.md) — Coarse values to use for updating conversion values.
- [+ updatePostbackConversionValue:completionHandler:](<updatepostbackconversionvalue(__completionhandler_).md>) — Verifies the first launch of an advertised app and, on subsequent calls, updates the conversion value or calls a completion handler if the update fails.
