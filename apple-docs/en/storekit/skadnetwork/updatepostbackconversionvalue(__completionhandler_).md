---
title: 'updatePostbackConversionValue(_:completionHandler:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/storekit/skadnetwork/updatepostbackconversionvalue(_:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/storekit/skadnetwork/updatepostbackconversionvalue(_:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skadnetwork/updatepostbackconversionvalue%28_%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:3879d114c88012fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKAdNetwork](../skadnetwork.md)

# updatePostbackConversionValue(_:completionHandler:)

<sub>Type Method</sub>

Verifies the first launch of an advertised app and, on subsequent calls, updates the conversion value or calls a completion handler if the update fails.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class func updatePostbackConversionValue(_ conversionValue: Int, completionHandler completion: (@Sendable ((any Error)?) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class func updatePostbackConversionValue(_ conversionValue: Int) async throws
```

## Parameters

- `conversionValue` — An unsigned 6-bit value `≥0` and `≤63`. The app or the ad network defines the meaning of the conversion value. For ad impressions signed with SKAdNetwork 3 or earlier, you need to increase the `conversionValue` each time you call this method. For ad impressions signed with SKAdNetwork 4 or later, you may use any valid `conversionValue` each time you call this method.

- `completion` — An optional completion handler you provide to catch and handle any errors this method encounters when you update a conversion value. Set this value to `nil` if you don’t provide a handler.

## Discussion

Invalid conversion values cause the method to fail and return error [SKANErrorInvalidConversionValue](../skanerror-swift.struct/code/invalidconversionvalue.md).

> [!note] Note
> Consider using [+ updatePostbackConversionValue:coarseValue:lockWindow:completionHandler:](<updatepostbackconversionvalue(__coarsevalue_lockwindow_completionhandler_).md>) instead of this method for newer implementations.

Apps call this method to update conversion values as people engage with the app. It’s up to the app or ad network to define the conversion value’s meaning. Call this method immediately when the user first launches the app to confirm the app’s launch. Call this method again, as needed, to reflect the person’s engagement with the app.

The final conversion value appears in the postback if sending the data meets Apple’s privacy threshold. Only postbacks that win the ad attribution can contain a conversion value. Nonwinning postbacks don’t contain conversion values. For more information, see [Receiving ad attributions and postbacks](../receiving-ad-attributions-and-postbacks.md).

The way this method behaves depends on the ad’s version, as described in the following sections. Ad networks determine an ad’s version when they sign the ad. For more information about signing ads, see [Signing and providing ads](../signing-and-providing-ads.md).

### Update the conversion value for version 3 ads and earlier

If the ad network signs the winning ad with version 3 or earlier, calling this method behaves as follows:

- Apps may call this method repeatedly before a rolling 24-hour timer expires.
- The 24-hour timer restarts each time the app calls this method with a valid `conversionValue` that’s greater than the previous value.
- When the timer expires, the conversion value is final and subsequent calls to [+ updatePostbackConversionValue:completionHandler:](<updatepostbackconversionvalue(__completionhandler_).md>) have no effect.
- The device sends the postback to the ad network’s URL within 0 to 24 hours after the timer expires. The postback contains the final conversion value only if sending the data meets Apple’s privacy threshold.

### Update the conversion value for version 4 ads and later

> [!note] Note
> This method supports ads signed with version 4 and later, however, it doesn’t provide advanced features, such as multiple postbacks and coarse conversion values, available starting in version 4. To get those advanced features for ads signed with version 4 and later, use [+ updatePostbackConversionValue:coarseValue:lockWindow:completionHandler:](<updatepostbackconversionvalue(__coarsevalue_lockwindow_completionhandler_).md>) instead of this method.

If the ad network signs the winning ad with version 4 or later, calling this method behaves as follows:

- Apps may call this method repeatedly within the first conversion window.
- Provide any `conversionValue` within the valid range; the `conversionValue` doesn’t need to increase with each call.
- This method is available only during the first conversion window. Use [+ updatePostbackConversionValue:coarseValue:lockWindow:completionHandler:](<updatepostbackconversionvalue(__coarsevalue_lockwindow_completionhandler_).md>) to update conversion values in the subsequent conversion windows.
- When the first conversion window closes, the system sends the postback within 0 to 24 hours. The postback contains the final conversion value only if sending the data meets Apple’s privacy threshold.

## See Also

### Providing conversion information

- [+ updatePostbackConversionValue:coarseValue:lockWindow:completionHandler:](<updatepostbackconversionvalue(__coarsevalue_lockwindow_completionhandler_).md>) — Updates the fine and coarse conversion values and indicates whether to send the postback before the conversion window ends, and calls a completion handler if the update fails.
- [+ updatePostbackConversionValue:coarseValue:completionHandler:](<updatepostbackconversionvalue(__coarsevalue_completionhandler_).md>) — Updates the fine and coarse conversion values, and calls a completion handler if the update fails.
- [CoarseConversionValue](coarseconversionvalue.md) — Coarse values to use for updating conversion values.
