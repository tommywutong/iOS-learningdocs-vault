---
title: 'transactionTask(_:action:)'
framework: SecureElementCredential
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.1+, iPadOS 18.1+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/transactiontask(_:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/transactiontask(_:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/transactiontask%28_%3Aaction%3A%29.json'
content_hash: 'sha256:e1ab770660203c06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# transactionTask(_:action:)

<sub>Instance Method</sub>

Provides a task to perform before this view appears

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
nonisolated func transactionTask(_ configuration: CredentialTransaction.Configuration?, action: @escaping (CredentialTransaction) async -> Void) -> some View

```

## Parameters

- `configuration` — A configuration containing information about the transaction task. When the task is completed or an error is encountered while performing the task, the system invalidates this configuration, and the `CredentialTransaction` is invalidated.

- `action` — A closure that will be called when `isPerformingTransaction` is `true`. It provides a `CredentialTransaction` instance that can be used to perform transactions.

## Discussion

This task provides an instance of a `CredentialTransaction` to be used to perform transactions.

A typical client should use the APIs in the following sequence:

1. `acquirePresentmentIntentAssertion()` prior to showing any proprietary payment UI
2. `relinquish()` the assertion before invoking the transaction API
3. `configuration.invalidate()` after presenting the credential
4. Optionally, `acquirePresentmentIntentAssertion()` to finish up any proprietary payment UI
5. `relinquish()` the assertion

For example:

```swift
 struct TransactionView: View {
     @State private var configuration: CredentialTransaction.Configuration?
     private var assertion: PresentmentIntentAssertion // acquirePresentmentIntentAssertion() before transitioning into this view (step 1)
     private var activeSession: CredentialSession
     private var selectedCredential: Credential

     var body: some View {
         VStack {
             Button("Perform Transaction") {
                 guard let configuration else {
                    configuration = activeSession.configuration()
                    return
                 }

                 configuration.invalidate() // step 3
                 // Optional
                 assertion = try await session.acquirePresentmentIntentAssertion() // step 4
                 // handle any proprietary UI
                 try await assertion.relinquish() // step 5
                 // Optional end
             }
             .transactionTask(configuration) { transaction in
                 do {
                     try await assertion.relinquish() // step 2
                     try await transaction.performTransaction(using: selectedCredential)
                 } catch {
                     // code to handle error
                 }
             }
         }
     }
 }
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
- [verifyIdentityWithWalletButtonStyle(_:)](<verifyidentitywithwalletbuttonstyle(__).md>) — Sets the style to be used by the button. (see `PKIdentityButtonStyle`).
- [AsyncShareablePassConfiguration](../../passkit/asyncshareablepassconfiguration.md)
