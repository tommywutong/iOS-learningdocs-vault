---
title: 'onApplePayShippingMethodChange(perform:)'
framework: PassKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.5+, iPadOS 15.5+, macOS 12.5+, watchOS 8.5+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onapplepayshippingmethodchange(perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onapplepayshippingmethodchange(perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onapplepayshippingmethodchange%28perform%3A%29.json'
content_hash: 'sha256:71144cc7539a8e4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onApplePayShippingMethodChange(perform:)

<sub>Instance Method</sub>

Called when a user selected a shipping method. This is required if the user is being asked to provide a shipping method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated func onApplePayShippingMethodChange(perform action: @escaping (PKShippingMethod) async -> PKPaymentRequestShippingMethodUpdate) -> some View

```

## Return Value

An update to the payment request shipping method.

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
- [payLaterViewAction(_:)](<paylaterviewaction(__).md>) — Sets the action on the PayLaterView. See `PKPayLaterAction`.
- [payLaterViewDisplayStyle(_:)](<paylaterviewdisplaystyle(__).md>) — Sets the display style on the PayLaterView. See `PKPayLaterDisplayStyle`.
- [payWithApplePayButtonDisableCardArt()](<paywithapplepaybuttondisablecardart().md>) — Sets the features that should be allowed to show on the payment buttons.
- [payWithApplePayButtonStyle(_:)](<paywithapplepaybuttonstyle(__).md>) — Sets the style to be used by the button. (see `PayWithApplePayButtonStyle`).
- [verifyIdentityWithWalletButtonStyle(_:)](<verifyidentitywithwalletbuttonstyle(__).md>) — Sets the style to be used by the button. (see `PKIdentityButtonStyle`).
- [AsyncShareablePassConfiguration](../../passkit/asyncshareablepassconfiguration.md)
- [transactionTask(_:action:)](<transactiontask(__action_).md>) — Provides a task to perform before this view appears
