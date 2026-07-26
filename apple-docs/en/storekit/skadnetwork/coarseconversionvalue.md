---
title: SKAdNetwork.CoarseConversionValue
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.1+, iPadOS 16.1+, Mac Catalyst 16.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skadnetwork/coarseconversionvalue
source_url: 'https://developer.apple.com/documentation/storekit/skadnetwork/coarseconversionvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skadnetwork/coarseconversionvalue.json'
content_hash: 'sha256:225d0320e93b5246'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKAdNetwork](../skadnetwork.md)

# SKAdNetwork.CoarseConversionValue

<sub>Structure</sub>

Coarse values to use for updating conversion values.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct CoarseConversionValue
```

## Discussion

When you provide the coarse conversion value to the [+ updatePostbackConversionValue:coarseValue:completionHandler:](<updatepostbackconversionvalue(__coarsevalue_completionhandler_).md>) or [+ updatePostbackConversionValue:coarseValue:lockWindow:completionHandler:](<updatepostbackconversionvalue(__coarsevalue_lockwindow_completionhandler_).md>) methods, use the static constants [SKAdNetworkCoarseConversionValueLow](coarseconversionvalue/low.md), [SKAdNetworkCoarseConversionValueMedium](coarseconversionvalue/medium.md), or [SKAdNetworkCoarseConversionValueHigh](coarseconversionvalue/high.md).

These constants have no special meaning. The app or ad network can define their meaning, as is useful for their ad campaigns. The app is responsible for assigning a coarse conversion value, as well as the fine conversion value, when it calls one of the conversion value methods. You can determine how the coarse and fine conversion values relate to the types of conversion events you want to measure.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Providing coarse conversion values

- [SKAdNetworkCoarseConversionValueHigh](coarseconversionvalue/high.md) — A string constant value for indicating a high coarse conversion value.
- [SKAdNetworkCoarseConversionValueLow](coarseconversionvalue/low.md) — A string constant value for indicating a low coarse conversion value.
- [SKAdNetworkCoarseConversionValueMedium](coarseconversionvalue/medium.md) — A string constant value for indicating a medium coarse conversion value.
- [init(rawValue:)](<coarseconversionvalue/init(rawvalue_).md>) — Creates a coarse conversion value from the raw value.

## See Also

### Providing conversion information

- [+ updatePostbackConversionValue:coarseValue:lockWindow:completionHandler:](<updatepostbackconversionvalue(__coarsevalue_lockwindow_completionhandler_).md>) — Updates the fine and coarse conversion values and indicates whether to send the postback before the conversion window ends, and calls a completion handler if the update fails.
- [+ updatePostbackConversionValue:coarseValue:completionHandler:](<updatepostbackconversionvalue(__coarsevalue_completionhandler_).md>) — Updates the fine and coarse conversion values, and calls a completion handler if the update fails.
- [+ updatePostbackConversionValue:completionHandler:](<updatepostbackconversionvalue(__completionhandler_).md>) — Verifies the first launch of an advertised app and, on subsequent calls, updates the conversion value or calls a completion handler if the update fails.
