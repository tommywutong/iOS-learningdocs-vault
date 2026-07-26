---
title: 'startImpression(_:completionHandler:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/storekit/skadnetwork/startimpression(_:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/storekit/skadnetwork/startimpression(_:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skadnetwork/startimpression%28_%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:4e74665ca8805dbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKAdNetwork](../skadnetwork.md)

# startImpression(_:completionHandler:)

<sub>Type Method</sub>

Indicates that your app is presenting a view-through ad to the user.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class func startImpression(_ impression: SKAdImpression, completionHandler completion: (@Sendable ((any Error)?) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class func startImpression(_ impression: SKAdImpression) async throws
```

## Parameters

- `impression` — An instance of [SKAdImpression](../skadimpression.md) with the properties set for the view-through ad that you’re presenting.

- `completion` — The callback handler you provide to handle any tasks relevant to the start of the ad impression.

## Discussion

Call this method when you start presenting the view-through ad to the user. If you call [+ startImpression:completionHandler:](<startimpression(__completionhandler_).md>) more than once for the same advertised app before calling [+ endImpression:completionHandler:](<endimpression(__completionhandler_).md>), the latest impression overwrites the earlier impression.

Call [+ endImpression:completionHandler:](<endimpression(__completionhandler_).md>) when the impression ends and is no longer visible to the user.

> [!note] Note
> To ensure that SKAdNetwork records the impression, call [+ endImpression:completionHandler:](<endimpression(__completionhandler_).md>) after the impression ends, regardless of whether [+ startImpression:completionHandler:](<startimpression(__completionhandler_).md>) returns an error in the completion handler.

## See Also

### Signing view-through ads

- [Generating the signature to validate view-through ads](../generating-the-signature-to-validate-view-through-ads.md) — Initiate install validation by displaying a view-through ad with signed parameters.
- [SKAdImpression](../skadimpression.md) — A class that defines an ad impression for a view-through ad.
- [+ endImpression:completionHandler:](<endimpression(__completionhandler_).md>) — Indicates that your app is no longer presenting a view-through ad to the user.
