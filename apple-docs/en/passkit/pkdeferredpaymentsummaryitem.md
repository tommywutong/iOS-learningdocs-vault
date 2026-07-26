---
title: PKDeferredPaymentSummaryItem
framework: PassKit (Apple Pay and Wallet)
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/passkit/pkdeferredpaymentsummaryitem
source_url: 'https://developer.apple.com/documentation/passkit/pkdeferredpaymentsummaryitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/passkit/pkdeferredpaymentsummaryitem.json'
content_hash: 'sha256:1fc757f08f5ec636'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PassKit (Apple Pay and Wallet)](../passkit.md)

# PKDeferredPaymentSummaryItem

<sub>Class</sub>

An object that defines a summary item for a payment that occurs at a later date, such as a pre-order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class PKDeferredPaymentSummaryItem
```

## Relationships

- **Inherits From**: [PKPaymentSummaryItem](pkpaymentsummaryitem.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Setting the payment date

- [deferredDate](pkdeferredpaymentsummaryitem/deferreddate.md) — The date, in the future, of the payment.

## See Also

### Setting payment summary items

- [deferredBilling](pkdeferredpaymentrequest/deferredbilling.md) — An object that contains details about the deferred payment.
