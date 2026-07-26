---
title: 'updateConversionValue(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+（15.4 起废弃）, iPadOS 14.0+（15.4 起废弃）, Mac Catalyst 14.0+（15.4 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skadnetwork/updateconversionvalue(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/skadnetwork/updateconversionvalue(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skadnetwork/updateconversionvalue%28_%3A%29.json'
content_hash: 'sha256:d20c5fc9a21b8ddd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKAdNetwork](../skadnetwork.md)

# updateConversionValue(_:)

<sub>Type Method</sub>

Updates the conversion value and verifies the first launch of an app installed as a result of an ad.

> [!warning] Deprecated
> Use [+ updatePostbackConversionValue:coarseValue:lockWindow:completionHandler:](<updatepostbackconversionvalue(__coarsevalue_lockwindow_completionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class func updateConversionValue(_ conversionValue: Int)
```

## Parameters

- `conversionValue` — An unsigned 6-bit value (`>=0` and `<=63`). The app or the ad network determines the meaning of the value. The default value is `0`.

## Discussion

Apps that ad networks advertise call [+ updateConversionValue:](<updateconversionvalue(__).md>) or [+ registerAppForAdNetworkAttribution](<registerappforadnetworkattribution().md>) when the app first launches, to register the attribution.

> [!important] Important
> Provide a valid conversion value within the range of `>=0` and `<=63` when calling [+ updateConversionValue:](<updateconversionvalue(__).md>) to register the attribution. Invalid conversion values cause the method to fail, and the conversion to fail to register.

Apps may call [+ updateConversionValue:](<updateconversionvalue(__).md>) again within a rolling 24-hour period to update the conversion value. Calling this method serves two purposes:

- It registers the attribution by generating an install notification — the cryptographically signed data that confirms that a user installed and launched this app as a result of an ad.
- It enables the app to provide and update a conversion value.

Conversion values are a 6-bit value that the ad network or the app defines. The app decides when to update the value, which it can do any number of times before a rolling 24-hour timer expires. The 24-hour timer restarts each time the app calls this method with a valid conversion value greater than the previous value. When the timer expires, the conversion value is final and subsequent calls to [+ updateConversionValue:](<updateconversionvalue(__).md>) have no effect.

The device sends the install notification postback to the ad network’s URL within 0-24 hours after the timer expires. The postback only contains the final conversion value if sending the data meets Apple’s privacy threshold. Only postbacks with an ad attribution can contain a conversion value; non-winning postbacks don’t include a conversion value. For more information, see [Receiving ad attributions and postbacks](../receiving-ad-attributions-and-postbacks.md).

Ad networks must verify the postback after receiving it. See [Verifying an install-validation postback](../verifying-an-install-validation-postback.md) for more information.

## See Also

### Deprecated

- [+ registerAppForAdNetworkAttribution](<registerappforadnetworkattribution().md>) — Verifies the first launch of an app installed as a result of an ad. _(deprecated)_
