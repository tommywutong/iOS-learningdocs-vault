---
title: registerAppForAdNetworkAttribution()
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.3+（15.4 起废弃）, iPadOS 11.3+（15.4 起废弃）, Mac Catalyst 13.1+（15.4 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skadnetwork/registerappforadnetworkattribution()
source_url: 'https://developer.apple.com/documentation/storekit/skadnetwork/registerappforadnetworkattribution()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skadnetwork/registerappforadnetworkattribution%28%29.json'
content_hash: 'sha256:e514cfda57709a4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKAdNetwork](../skadnetwork.md)

# registerAppForAdNetworkAttribution()

<sub>Type Method</sub>

Verifies the first launch of an app installed as a result of an ad.

> [!warning] Deprecated
> Use [+ updatePostbackConversionValue:coarseValue:lockWindow:completionHandler:](<updatepostbackconversionvalue(__coarsevalue_lockwindow_completionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class func registerAppForAdNetworkAttribution()
```

## Discussion

Apps that an ad network campaign advertise call this method or [+ updateConversionValue:](<updateconversionvalue(__).md>) when the app first launches. Both methods generate an install notification, which is the cryptographically signed data that validates that a user installed and launched this app as a result of an ad.

In iOS 15.4 and earlier, the first call to [+ registerAppForAdNetworkAttribution](<registerappforadnetworkattribution().md>) generates the notification if the device has attribution data for that app, and starts a 24-hour timer. Subsequent calls to this method have no effect, unless the ad already has a conversion value set, in which case calling [+ registerAppForAdNetworkAttribution](<registerappforadnetworkattribution().md>) resets the conversion value to `0`. You may, however, call [+ updateConversionValue:](<updateconversionvalue(__).md>) to provide an updated conversion value and restart the timer.

The device sends one or more install notifications to ad network postback URLs within 0-24 hours after the timer expires. For more information about attribution-winning and non-winning postbacks, see [Receiving ad attributions and postbacks](../receiving-ad-attributions-and-postbacks.md).

Ad networks must verify the postback after receiving it. For more information, see [Verifying an install-validation postback](../verifying-an-install-validation-postback.md).

## See Also

### Deprecated

- [+ updateConversionValue:](<updateconversionvalue(__).md>) — Updates the conversion value and verifies the first launch of an app installed as a result of an ad. _(deprecated)_
