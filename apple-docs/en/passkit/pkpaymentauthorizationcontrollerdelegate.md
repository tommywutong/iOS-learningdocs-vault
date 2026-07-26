---
title: PKPaymentAuthorizationControllerDelegate
framework: PassKit (Apple Pay and Wallet)
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/passkit/pkpaymentauthorizationcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/passkit/pkpaymentauthorizationcontrollerdelegate.json'
content_hash: 'sha256:08a50339009de9e5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PassKit (Apple Pay and Wallet)](../passkit.md)

# PKPaymentAuthorizationControllerDelegate

<sub>Protocol</sub>

Methods that let you respond to user interactions with your payment authorization controller.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
protocol PKPaymentAuthorizationControllerDelegate : NSObjectProtocol
```

## Overview

The [PKPaymentAuthorizationControllerDelegate](pkpaymentauthorizationcontrollerdelegate.md) protocol is implemented by the payment authorization controller’s delegate. You implement this protocol to respond to user interaction with that controller.

In most cases, the payment authorization controller automatically waits for its delegate to finish responding to one method before it calls other delegate methods. You indicate that the delegate is finished with the current method by calling that method’s completion block. This action tells the pay authorization controller to proceed with the next step in the authorization process.

There is one exception to this step-by-step procedure: The pay authorization controller calls the [- paymentAuthorizationControllerDidFinish:](<pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontrollerdidfinish(__).md>) method as soon as the user cancels a payment without authorizing. The controller can call this method at any time.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Handling user interactions

- [- presentationWindowForPaymentAuthorizationController:](<pkpaymentauthorizationcontrollerdelegate/presentationwindow(for_).md>) — Returns the window in which to present a payment authorization sheet.

### Handling user’s payment method selection

- [- paymentAuthorizationController:didSelectPaymentMethod:handler:](<pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(__didselectpaymentmethod_handler_).md>) — Tells the delegate that the user changed the payment method, and asks for an updated payment request.
- [- paymentAuthorizationController:didSelectPaymentMethod:completion:](<pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(__didselectpaymentmethod_completion_).md>) — Tells the delegate that the user changed the payment method, and asks for an updated payment request. _(deprecated)_

### Handling coupons

- [- paymentAuthorizationController:didChangeCouponCode:handler:](<pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(__didchangecouponcode_handler_).md>) — Tells the delegate that the user entered or updated a coupon code.

### Handling shipping information

- [- paymentAuthorizationController:didSelectShippingContact:handler:](<pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(__didselectshippingcontact_handler_).md>) — Tells the delegate that the user selected a shipping address.
- [- paymentAuthorizationController:didSelectShippingContact:completion:](<pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(__didselectshippingcontact_completion_).md>) — Tells the delegate that the user selected a shipping address. _(deprecated)_
- [- paymentAuthorizationController:didSelectShippingMethod:handler:](<pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(__didselectshippingmethod_handler_).md>) — Tells the delegate that the user selected a shipping method.
- [- paymentAuthorizationController:didSelectShippingMethod:completion:](<pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(__didselectshippingmethod_completion_).md>) — Tells the delegate that the user selected a shipping method. _(deprecated)_

### Handling user’s payment authorization

- [- paymentAuthorizationController:didRequestMerchantSessionUpdate:](<pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(__didrequestmerchantsessionupdate_).md>) — Requests an object that validates the identity of a merchant for a payment request.
- [- paymentAuthorizationControllerWillAuthorizePayment:](<pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontrollerwillauthorizepayment(__).md>) — Tells the delegate that the user is authorizing the payment request.
- [- paymentAuthorizationController:didAuthorizePayment:handler:](<pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(__didauthorizepayment_handler_).md>) — Tells the delegate that the user authorized the payment request, and asks for a result.
- [- paymentAuthorizationController:didAuthorizePayment:completion:](<pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(__didauthorizepayment_completion_).md>) — Tells the delegate that the user authorized the payment request, and asks for a result. _(deprecated)_
- [- paymentAuthorizationControllerDidFinish:](<pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontrollerdidfinish(__).md>) — Tells the delegate that payment authorization has completed.

## See Also

### Handling user interactions

- [delegate](pkpaymentauthorizationcontroller/delegate.md) — The controller’s delegate.
- [- presentWithCompletion:](<pkpaymentauthorizationcontroller/present(completion_).md>) — Presents the payment sheet modally over your app.
- [- dismissWithCompletion:](<pkpaymentauthorizationcontroller/dismiss(completion_).md>) — Dismisses the payment sheet.
