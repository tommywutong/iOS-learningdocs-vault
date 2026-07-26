---
title: Transaction.OfferType
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/offertype-swift.struct
source_url: 'https://developer.apple.com/documentation/storekit/transaction/offertype-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/offertype-swift.struct.json'
content_hash: 'sha256:0442ae5b1bd02d15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# Transaction.OfferType

<sub>Structure</sub>

The types of offers that apply to a transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct OfferType
```

## Overview

You don’t create offer types in [OfferType](offertype-swift.struct.md). The static values indicate the offer types that the system reports for a transaction.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting offer types

- [introductory](offertype-swift.struct/introductory.md) — An introductory offer for an auto-renewable subscription.
- [promotional](offertype-swift.struct/promotional.md) — A promotional offer for an auto-renewable subscription.
- [code](offertype-swift.struct/code.md) — An offer code.
- [winBack](offertype-swift.struct/winback.md) — A win-back offer for an auto-renewable subscription.

### Getting a localized description

- [localizedDescription](offertype-swift.struct/localizeddescription.md) — The localized text that describes the offer type.
