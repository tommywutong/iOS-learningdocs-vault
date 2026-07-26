---
title: couponCode
framework: PassKit (Apple Pay and Wallet)
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/passkit/pkpaymentrequest/couponcode
source_url: 'https://developer.apple.com/documentation/passkit/pkpaymentrequest/couponcode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/passkit/pkpaymentrequest/couponcode.json'
content_hash: 'sha256:d94289eebcd305fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PassKit (Apple Pay and Wallet)](../../passkit.md) · [PKPaymentRequest](../pkpaymentrequest.md)

# couponCode

<sub>Instance Property</sub>

The initial coupon code for the payment request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var couponCode: String? { get set }
```

## Discussion

Set the value to `nil` or the empty string to indicate that there’s no initial coupon.

> [!important] Important
> The system doesn’t send a change event for an initial coupon code. You must apply the code to the initial payment summary items.

## See Also

### Working with coupon codes

- [supportsCouponCode](supportscouponcode.md) — A Boolean value that determines whether the payment sheet displays the coupon code field.
