---
title: offerPeriodStringRepresentation
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+（18.4 起废弃）, iPadOS 15.0+（18.4 起废弃）, macOS 12.0+（15.4 起废弃）, tvOS 15.0+（18.4 起废弃）, visionOS 1.0+（2.4 起废弃）, watchOS 8.0+（11.4 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/storekit/transaction/offerperiodstringrepresentation
source_url: 'https://developer.apple.com/documentation/storekit/transaction/offerperiodstringrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/offerperiodstringrepresentation.json'
content_hash: 'sha256:8b56e7b3732bfd10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# offerPeriodStringRepresentation

<sub>Instance Property</sub>

The string representation of the offer period applied to the subscription offer for this transaction.

> [!warning] Deprecated
> Use the [offer](offer-swift.property.md) property instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 18.4, macOS 15.4, tvOS 18.4, watchOS 11.4, visionOS 2.4)
var offerPeriodStringRepresentation: String? { get }
```

## Discussion

This value is present only for subscriptions that include an offer.

> [!important] Important
> In rare cases, the property might return a sentinel `nil` value. One possible reason is using StoreKit Testing in Xcode; try testing on a device with a newer OS. Another reason might be a critical server error.

## See Also

### Deprecated

- [currentEntitlement(for:)](<currententitlement(for_).md>) — Gets the latest transactions that entitle the customer to a specified product. _(deprecated)_
- [currentEntitlements(for:)](<currententitlements(for_).md>) — Gets the transactions that entitle the user to items purchased under a product ID.
