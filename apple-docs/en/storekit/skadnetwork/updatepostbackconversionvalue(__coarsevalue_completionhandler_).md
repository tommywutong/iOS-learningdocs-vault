---
title: 'updatePostbackConversionValue(_:coarseValue:completionHandler:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.1+, iPadOS 16.1+, Mac Catalyst 16.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/storekit/skadnetwork/updatepostbackconversionvalue(_:coarsevalue:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/storekit/skadnetwork/updatepostbackconversionvalue(_:coarsevalue:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skadnetwork/updatepostbackconversionvalue%28_%3Acoarsevalue%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:4c5bad8203400b77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKAdNetwork](../skadnetwork.md)

# updatePostbackConversionValue(_:coarseValue:completionHandler:)

<sub>Type Method</sub>

Updates the fine and coarse conversion values, and calls a completion handler if the update fails.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class func updatePostbackConversionValue(_ fineValue: Int, coarseValue: SKAdNetwork.CoarseConversionValue, completionHandler completion: (@Sendable ((any Error)?) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class func updatePostbackConversionValue(_ fineValue: Int, coarseValue: SKAdNetwork.CoarseConversionValue) async throws
```

## Parameters

- `fineValue` — An unsigned 6-bit value `≥0` and `≤63`. The app or the ad network defines the meaning of the conversion value.

- `coarseValue` — An [CoarseConversionValue](coarseconversionvalue.md) value. The app or the ad network defines the meaning of this value.

- `completion` — An optional completion handler you provide to catch and handle any errors this method encounters when you update a conversion value. Set this value to `nil` if you don’t provide a handler.

## Discussion

Call this method when the user first launches an app to register the app installation, and optionally again, to update conversion values as the user engages with the app.

This method is identical to calling [+ updatePostbackConversionValue:coarseValue:lockWindow:completionHandler:](<updatepostbackconversionvalue(__coarsevalue_lockwindow_completionhandler_).md>) with the `lockWindow` parameter set to `false`.

This method returns [SKANErrorInvalidConversionValue](../skanerror-swift.struct/code/invalidconversionvalue.md) if the `fineValue` is outside of the allowed range.

> [!important] Important
> The system ignores calls to this method if the `fineValue` is outside of the valid range. Valid conversion updates your app sends before or after an invalid conversion remain available.

## See Also

### Providing conversion information

- [+ updatePostbackConversionValue:coarseValue:lockWindow:completionHandler:](<updatepostbackconversionvalue(__coarsevalue_lockwindow_completionhandler_).md>) — Updates the fine and coarse conversion values and indicates whether to send the postback before the conversion window ends, and calls a completion handler if the update fails.
- [CoarseConversionValue](coarseconversionvalue.md) — Coarse values to use for updating conversion values.
- [+ updatePostbackConversionValue:completionHandler:](<updatepostbackconversionvalue(__completionhandler_).md>) — Verifies the first launch of an advertised app and, on subsequent calls, updates the conversion value or calls a completion handler if the update fails.
