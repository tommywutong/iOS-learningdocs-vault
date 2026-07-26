---
title: PayWithApplePayButton
framework: PassKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/passkit/paywithapplepaybutton
source_url: 'https://developer.apple.com/documentation/passkit/paywithapplepaybutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/passkit/paywithapplepaybutton.json'
content_hash: 'sha256:723bd242241751a6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PassKit (Apple Pay and Wallet)](../passkit.md)

# PayWithApplePayButton

<sub>Structure</sub>

A type that provides a button to pay with Apple pay.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct PayWithApplePayButton<Fallback> where Fallback : View
```

## Overview

Use this structure as the SwiftUI equivalent to [PKPaymentButton](pkpaymentbutton.md). For design guidance, see Human Interface Guidelines \> Apple Pay \> [Using Apple Pay buttons](https://developer.apple.com/design/human-interface-guidelines/apple-pay#Using-Apple-Pay-buttons).

This example shows an implementation of the Pay with Apple Pay button.

```swift
// Create a payment request.
@State private var paymentRequest = PKPaymentRequest()

// Create a payment authorization change method.
func paymentAuthorizationDidChange(phase: PayWithApplePayButtonPaymentAuthorizationPhase) { ... }

@ViewBuilder var payButton: some View {
    PayWithApplePayButton(
        .plain,
        request: paymentRequest,
        onPaymentAuthorizationChange: paymentAuthorizationDidChange
    ) {
        // Display a fallback view if the payment request fails.
    }
    .frame(width: 250, height: 50)
    .payWithApplePayButtonStyle(.automatic)
}
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating the button

- [init(_:action:)](<paywithapplepaybutton/init(__action_).md>)
- [init(_:action:fallback:)](<paywithapplepaybutton/init(__action_fallback_).md>)
- [init(_:request:onPaymentAuthorizationChange:)](<paywithapplepaybutton/init(__request_onpaymentauthorizationchange_).md>)
- [init(_:request:onPaymentAuthorizationChange:fallback:)](<paywithapplepaybutton/init(__request_onpaymentauthorizationchange_fallback_).md>)
- [init(_:request:onPaymentAuthorizationChange:onMerchantSessionRequested:)](<paywithapplepaybutton/init(__request_onpaymentauthorizationchange_onmerchantsessionrequested_).md>)
- [init(_:request:onPaymentAuthorizationChange:onMerchantSessionRequested:fallback:)](<paywithapplepaybutton/init(__request_onpaymentauthorizationchange_onmerchantsessionrequested_fallback_).md>)

## See Also

### Apple Pay buttons

- [PKPaymentButton](pkpaymentbutton.md) — An object that displays a button either to trigger payments through Apple Pay or to prompt the user to set up a card.
- [PayWithApplePayButtonLabel](paywithapplepaybuttonlabel.md)
- [PayWithApplePayButtonStyle](paywithapplepaybuttonstyle.md)
- [PayWithApplePayButtonLabel](paywithapplepaybuttonlabel.md)
