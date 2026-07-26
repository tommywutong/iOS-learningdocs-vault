---
title: supportsCouponCode
framework: PassKit (Apple Pay and Wallet)
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/passkit/pkpaymentrequest/supportscouponcode
source_url: 'https://developer.apple.com/documentation/passkit/pkpaymentrequest/supportscouponcode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/passkit/pkpaymentrequest/supportscouponcode.json'
content_hash: 'sha256:14cf007eaa35bb2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PassKit (Apple Pay and Wallet)](../../passkit.md) · [PKPaymentRequest](../pkpaymentrequest.md)

# supportsCouponCode

<sub>Instance Property</sub>

A Boolean value that determines whether the payment sheet displays the coupon code field.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var supportsCouponCode: Bool { get set }
```

## Discussion

Set the value to `true` to display the coupon code field.

## See Also

### Working with coupon codes

- [couponCode](couponcode.md) — The initial coupon code for the payment request.
