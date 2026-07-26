---
title: 'verifyIdentityWithWalletButtonStyle(_:)'
framework: PassKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/verifyidentitywithwalletbuttonstyle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/verifyidentitywithwalletbuttonstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/verifyidentitywithwalletbuttonstyle%28_%3A%29.json'
content_hash: 'sha256:b871a74a88fb3f05'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# verifyIdentityWithWalletButtonStyle(_:)

<sub>Instance Method</sub>

Sets the style to be used by the button. (see `PKIdentityButtonStyle`).

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated func verifyIdentityWithWalletButtonStyle(_ style: VerifyIdentityWithWalletButtonStyle) -> some View

```

## See Also

### Accessing Apple Pay and Wallet

- [PayWithApplePayButton](../../passkit/paywithapplepaybutton.md) — A type that provides a button to pay with Apple pay.
- [AddPassToWalletButton](../../passkit/addpasstowalletbutton.md) — A type that provides a button that enables people to add a new or existing pass to Apple Wallet.
- [VerifyIdentityWithWalletButton](../../passkit/verifyidentitywithwalletbutton.md) — A type that displays a button to present the identity verification flow.
- [addOrderToWalletButtonStyle(_:)](<addordertowalletbuttonstyle(__).md>) — Sets the button’s style.
- [addPassToWalletButtonStyle(_:)](<addpasstowalletbuttonstyle(__).md>) — Sets the style to be used by the button. (see `PKAddPassButtonStyle`).
- [onApplePayCouponCodeChange(perform:)](<onapplepaycouponcodechange(perform_).md>) — Called when a user has entered or updated a coupon code. This is required if the user is being asked to provide a coupon code.
- [onApplePayPaymentMethodChange(perform:)](<onapplepaypaymentmethodchange(perform_).md>) — Called when a payment method has changed and asks for an update payment request. If this modifier isn’t provided Wallet will assume the payment method is valid.
- [onApplePayShippingContactChange(perform:)](<onapplepayshippingcontactchange(perform_).md>) — Called when a user selected a shipping address. This is required if the user is being asked to provide a shipping contact.
- [onApplePayShippingMethodChange(perform:)](<onapplepayshippingmethodchange(perform_).md>) — Called when a user selected a shipping method. This is required if the user is being asked to provide a shipping method.
- [payLaterViewAction(_:)](<paylaterviewaction(__).md>) — Sets the action on the PayLaterView. See `PKPayLaterAction`.
- [payLaterViewDisplayStyle(_:)](<paylaterviewdisplaystyle(__).md>) — Sets the display style on the PayLaterView. See `PKPayLaterDisplayStyle`.
- [payWithApplePayButtonDisableCardArt()](<paywithapplepaybuttondisablecardart().md>) — Sets the features that should be allowed to show on the payment buttons.
- [payWithApplePayButtonStyle(_:)](<paywithapplepaybuttonstyle(__).md>) — Sets the style to be used by the button. (see `PayWithApplePayButtonStyle`).
- [AsyncShareablePassConfiguration](../../passkit/asyncshareablepassconfiguration.md)
- [transactionTask(_:action:)](<transactiontask(__action_).md>) — Provides a task to perform before this view appears
