---
title: 'init(rawValue:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.1+, iPadOS 16.1+, Mac Catalyst 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/skadnetwork/coarseconversionvalue/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/storekit/skadnetwork/coarseconversionvalue/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skadnetwork/coarseconversionvalue/init%28rawvalue%3A%29.json'
content_hash: 'sha256:9fc3d8da35b3e29c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SKAdNetwork](../../skadnetwork.md) · [CoarseConversionValue](../coarseconversionvalue.md)

# init(rawValue:)

<sub>Initializer</sub>

Creates a coarse conversion value from the raw value.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
init(rawValue: String)
```

## Parameters

- `rawValue` — A string that is one of  [SKAdNetworkCoarseConversionValueLow](low.md), [SKAdNetworkCoarseConversionValueMedium](medium.md), or [SKAdNetworkCoarseConversionValueHigh](high.md).

## Discussion

You don’t need to call the initializer to use coarse conversion values. When you provide the coarse conversion value to the [+ updatePostbackConversionValue:coarseValue:completionHandler:](<../updatepostbackconversionvalue(__coarsevalue_completionhandler_).md>) or [+ updatePostbackConversionValue:coarseValue:lockWindow:completionHandler:](<../updatepostbackconversionvalue(__coarsevalue_lockwindow_completionhandler_).md>) methods, use the static constants, [SKAdNetworkCoarseConversionValueLow](low.md), [SKAdNetworkCoarseConversionValueMedium](medium.md), or [SKAdNetworkCoarseConversionValueHigh](high.md).

## See Also

### Providing coarse conversion values

- [SKAdNetworkCoarseConversionValueHigh](high.md) — A string constant value for indicating a high coarse conversion value.
- [SKAdNetworkCoarseConversionValueLow](low.md) — A string constant value for indicating a low coarse conversion value.
- [SKAdNetworkCoarseConversionValueMedium](medium.md) — A string constant value for indicating a medium coarse conversion value.
