---
title: AddPassToWalletButton
framework: PassKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/passkit/addpasstowalletbutton
source_url: 'https://developer.apple.com/documentation/passkit/addpasstowalletbutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/passkit/addpasstowalletbutton.json'
content_hash: 'sha256:da8f68f56d86ccc6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PassKit (Apple Pay and Wallet)](../passkit.md)

# AddPassToWalletButton

<sub>Structure</sub>

A type that provides a button that enables people to add a new or existing pass to Apple Wallet.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency struct AddPassToWalletButton<Fallback> where Fallback : View
```

## Overview

Use this structure as the SwiftUI equivalent to [PKAddPassButton](pkaddpassbutton.md). For design guidance, see Human Interface Guidelines \> Technologies \> [Wallet](https://developer.apple.com/design/human-interface-guidelines/wallet#Passes).

This example checks for a created pass and displays the Add to Apple Wallet button.

```swift
@State private var addedToWallet = false

@ViewBuilder var addPassButton: some View {
    if let pass = createMyPass() {
        AddPassToWalletButton([pass]) { added in
            addedToWallet = added
        }
        .frame(width: 250, height: 50)
        .addPassToWalletButtonStyle(.blackOutline)
    } else {
        // Display a fallback view if no pass exists.
    }
}
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating the button

- [init(_:cardholderName:passStyle:primaryAccountSuffix:cardDetails:description:filters:onRequest:onCompletion:)](<addpasstowalletbutton/init(__cardholdername_passstyle_primaryaccountsuffix_carddetails_description_filters_onrequest_oncompletion_).md>)
- [init(_:cardholderName:passStyle:primaryAccountSuffix:cardDetails:description:filters:onRequest:onCompletion:fallback:)](<addpasstowalletbutton/init(__cardholdername_passstyle_primaryaccountsuffix_carddetails_description_filters_onrequest_oncompletion_fallback_).md>)
- [init(_:onCompletion:)](<addpasstowalletbutton/init(__oncompletion_)-1inhj.md>)
- [init(_:onCompletion:)](<addpasstowalletbutton/init(__oncompletion_)-5wkyi.md>)
- [init(_:onCompletion:fallback:)](<addpasstowalletbutton/init(__oncompletion_fallback_)-77t5g.md>)
- [init(_:onCompletion:fallback:)](<addpasstowalletbutton/init(__oncompletion_fallback_)-7adn5.md>)
- [init(_:onRequest:onCompletion:)](<addpasstowalletbutton/init(__onrequest_oncompletion_).md>)
- [init(_:onRequest:onCompletion:fallback:)](<addpasstowalletbutton/init(__onrequest_oncompletion_fallback_).md>)
- [init(_:primaryAccountSuffix:passStyle:cardDetails:description:filters:onRequest:onCompletion:)](<addpasstowalletbutton/init(__primaryaccountsuffix_passstyle_carddetails_description_filters_onrequest_oncompletion_).md>)
- [init(_:primaryAccountSuffix:passStyle:cardDetails:description:filters:onRequest:onCompletion:fallback:)](<addpasstowalletbutton/init(__primaryaccountsuffix_passstyle_carddetails_description_filters_onrequest_oncompletion_fallback_).md>)
- [init(action:)](<addpasstowalletbutton/init(action_).md>)
- [init(carKeyPassword:supportedRadioTechnologies:issuerIdentifier:onCompletion:)](<addpasstowalletbutton/init(carkeypassword_supportedradiotechnologies_issueridentifier_oncompletion_).md>)
- [init(carKeyPassword:supportedRadioTechnologies:issuerIdentifier:onCompletion:fallback:)](<addpasstowalletbutton/init(carkeypassword_supportedradiotechnologies_issueridentifier_oncompletion_fallback_).md>)

## See Also

### Common data types

- [PKObject](pkobject.md) — An opaque type that acts as the superclass for the pass object.
- [PKAddPassButton](pkaddpassbutton.md) — Provides a button that enables users to add passes to Wallet.
- [PKLabeledValue](pklabeledvalue.md) — An object that can represent a detail about a payment card or other item.
- [AddPassToWalletButtonFilter](addpasstowalletbuttonfilter.md)
- [AddPassToWalletButtonResponse](addpasstowalletbuttonresponse.md)
- [AddPassToWalletButtonStyle](addpasstowalletbuttonstyle.md)
