---
title: SKProductDiscount.Type
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.2+（18.0 起废弃）, iPadOS 12.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.14.4+（15.0 起废弃）, tvOS 12.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproductdiscount/type-swift.enum
source_url: 'https://developer.apple.com/documentation/storekit/skproductdiscount/type-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductdiscount/type-swift.enum.json'
content_hash: 'sha256:61ce7e67dd6e4558'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProductDiscount](../skproductdiscount.md)

# SKProductDiscount.Type

<sub>Enumeration</sub>

Values representing the types of discount offers an app can present.

> [!warning] Deprecated
> Use Product.SubscriptionOffer.OfferType.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum `Type`
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Types of Offers

- [SKProductDiscountTypeIntroductory](type-swift.enum/introductory.md) — A constant indicating the discount type is an introductory offer. _(deprecated)_
- [SKProductDiscountTypeSubscription](type-swift.enum/subscription.md) — A constant indicating the discount type is a promotional offer. _(deprecated)_

### Initializers

- [init(rawValue:)](<type-swift.enum/init(rawvalue_).md>) _(deprecated)_

## See Also

### Identifying the Discount

- [identifier](identifier.md) — A string used to uniquely identify a discount offer for a product. _(deprecated)_
- [type](type-swift.property.md) — The type of discount offer. _(deprecated)_
