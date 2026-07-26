---
title: RedeemOption
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/storekit/redeemoption
source_url: 'https://developer.apple.com/documentation/storekit/redeemoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/redeemoption.json'
content_hash: 'sha256:6a02e0105b740322'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# RedeemOption

<sub>Structure</sub>

An option that customizes the behavior of an offer code redemption.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct RedeemOption
```

## Overview

Pass a set of these values to `AppStore/presentOfferCodeRedeemSheet(from:options:)` to configure the offer code redemption.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)
