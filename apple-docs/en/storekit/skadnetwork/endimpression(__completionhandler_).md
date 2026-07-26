---
title: 'endImpression(_:completionHandler:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/storekit/skadnetwork/endimpression(_:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/storekit/skadnetwork/endimpression(_:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skadnetwork/endimpression%28_%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:4def704a90af14b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKAdNetwork](../skadnetwork.md)

# endImpression(_:completionHandler:)

<sub>Type Method</sub>

Indicates that your app is no longer presenting a view-through ad to the user.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class func endImpression(_ impression: SKAdImpression, completionHandler completion: (@Sendable ((any Error)?) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class func endImpression(_ impression: SKAdImpression) async throws
```

## Parameters

- `impression` — An instance of [SKAdImpression](../skadimpression.md) with the properties set for the view-through ad that you presented. This must be the same instance you provide in [+ startImpression:completionHandler:](<startimpression(__completionhandler_).md>).

- `completion` — The callback handler you provide to handle any tasks relevant to concluding the ad impression.

## Discussion

Call this method when you end the presentation of a view-through ad and it’s no longer visible to the user. To help ensure it’s a valid impression, StoreKit only records the impression if the ad displays for a minimum amount of time. That minimum is 2 seconds on devices running iOS 15.4 and iPadOS 15.4 and later, and 3 seconds on devices running earlier versions of iOS and iPadOS. If the app displays the ad for fewer than the minimum number of seconds, StoreKit doesn’t record the ad impression for attribution.

> [!note] Note
> To ensure that SKAdNetwork records the impression, call [+ endImpression:completionHandler:](<endimpression(__completionhandler_).md>) after the impression ends, regardless of whether [+ startImpression:completionHandler:](<startimpression(__completionhandler_).md>) returns an error in the completion handler.

StoreKit records a maximum of 15 view-through ad impressions per source app for various products before discarding the oldest-recorded impression.

For more information about ad impressions and attributions, see [Receiving ad attributions and postbacks](../receiving-ad-attributions-and-postbacks.md).

## See Also

### Signing view-through ads

- [Generating the signature to validate view-through ads](../generating-the-signature-to-validate-view-through-ads.md) — Initiate install validation by displaying a view-through ad with signed parameters.
- [SKAdImpression](../skadimpression.md) — A class that defines an ad impression for a view-through ad.
- [+ startImpression:completionHandler:](<startimpression(__completionhandler_).md>) — Indicates that your app is presenting a view-through ad to the user.
