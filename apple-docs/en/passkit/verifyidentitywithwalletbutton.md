---
title: VerifyIdentityWithWalletButton
framework: PassKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/passkit/verifyidentitywithwalletbutton
source_url: 'https://developer.apple.com/documentation/passkit/verifyidentitywithwalletbutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/passkit/verifyidentitywithwalletbutton.json'
content_hash: 'sha256:4eb849ec6cafa846'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PassKit (Apple Pay and Wallet)](../passkit.md)

# VerifyIdentityWithWalletButton

<sub>Structure</sub>

A type that displays a button to present the identity verification flow.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency struct VerifyIdentityWithWalletButton<Fallback> where Fallback : View
```

## Overview

Use this structure as the SwiftUI equivalent to [PKIdentityButton](pkidentitybutton.md). The system allows one in-progress identity request at a time. Otherwise, it returns a [PKIdentityErrorRequestAlreadyInProgress](pkidentityerror-swift.struct/code/requestalreadyinprogress.md) error.

This example shows an implementation of the Verify Identity with Wallet button. For more information, see [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md).

```swift
// Create an identity request.
func createRequest() -> PKIdentityRequest {
    let descriptor = PKIdentityDriversLicenseDescriptor()
    descriptor.addElements([.age(atLeast: 18)],
                            intentToStore: .willNotStore)
    descriptor.addElements([.givenName, .familyName, .portrait],
                            intentToStore: .mayStore(days: 30))

    let request = PKIdentityRequest()
    request.descriptor = descriptor
    // The merchant ID you configured in your Apple Developer account.
    request.merchantIdentifier = <YOUR_MERCHANT_ID> 
    // The nonce your server generates.
    request.nonce = <YOUR_NONCE_VALUE> 
}
```

```swift
// Show the Verify Identity with Wallet button and handle the identity request result.
@ViewBuilder var verifiyIdentityButton: some View {
    VerifyIdentityWithWalletButton(
        .verifyIdentity,
        request: createRequest(),
    ) { result in
        switch result {
        case .success(let document):
            // Securely transfer the document to the server for decryption and verification.
        case .failure(let error):
            switch error {
            case PKIdentityError.cancelled:
                // Handle the cancellation error.
            default:
                // Handle other errors.
            }
        }
    } fallback: {
        // Verify the person's identity another way.
    }
}
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating the button

- [init(_:action:)](<verifyidentitywithwalletbutton/init(__action_).md>) — Creates a verify identity button that starts the identity authorization flow.
- [init(_:request:onCompletion:)](<verifyidentitywithwalletbutton/init(__request_oncompletion_).md>) — Creates a verify identity button that starts the identity authorization flow, with a completion handler.
- [init(_:request:onCompletion:fallback:)](<verifyidentitywithwalletbutton/init(__request_oncompletion_fallback_).md>) — Creates a verify identity button that starts the identity authorization flow, with a fallback view to use if the app can’t start the flow.

## See Also

### Identity sheet interactions and authorization

- [PKIdentityAuthorizationController](pkidentityauthorizationcontroller.md) — An object that presents a sheet that prompts the user to allow a request for identity information.
- [PKIdentityRequest](pkidentityrequest.md) — An object that represents a request for identity information from a Wallet pass.
- [PKIdentityDocument](pkidentitydocument.md) — An object that represents the response to a request.
- [PKIdentityElement](pkidentityelement.md) — An object that represents the elements an app requests from identity documents.
- [PKIdentityButton](pkidentitybutton.md) — An object that displays a button to trigger the identity verification flow.
- [VerifyIdentityWithWalletButtonLabel](verifyidentitywithwalletbuttonlabel.md) — A type that represents the label you use with a verify identity button.
- [VerifyIdentityWithWalletButtonStyle](verifyidentitywithwalletbuttonstyle.md) — A type that represents the style you use with a verify identity button.
