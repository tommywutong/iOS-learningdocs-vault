---
title: signature
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skadimpression/signature
source_url: 'https://developer.apple.com/documentation/storekit/skadimpression/signature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skadimpression/signature.json'
content_hash: 'sha256:97dd61d4a9519bf4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKAdImpression](../skadimpression.md)

# signature

<sub>Instance Property</sub>

The advertising network’s cryptographic signature for the ad impression.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var signature: String { get set }
```

## Discussion

The ad network creates a cryptographic signature that it uses to sign ads. For instructions on generating this value, see [Generating the signature to validate view-through ads](../generating-the-signature-to-validate-view-through-ads.md).
