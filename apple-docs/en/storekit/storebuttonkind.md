---
title: StoreButtonKind
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/storebuttonkind
source_url: 'https://developer.apple.com/documentation/storekit/storebuttonkind'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/storebuttonkind.json'
content_hash: 'sha256:8b9d4e54f7badae9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# StoreButtonKind

<sub>Structure</sub>

A button to display in a store view or subscription store view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct StoreButtonKind
```

## Overview

Use the [storeButton(_:for:)](<../swiftui/view/storebutton(__for_).md>) modifier on a view to set the visibility of the buttons.

## Topics

### Getting button types for store views

- [cancellation](storebuttonkind/cancellation.md) — A type of button that people use to dismiss the current store presentation.
- [restorePurchases](storebuttonkind/restorepurchases.md) — A type of button that people use to restore purchases.

### Getting additional button types for subscription store views

- [signIn](storebuttonkind/signin.md) — A type of button that people use to sign in.
- [redeemCode](storebuttonkind/redeemcode.md) — A type of button that people use to redeem an offer code.
- [policies](storebuttonkind/policies.md) — A type of button that people use to display store policies.

## See Also

### Configuring accessory buttons

- [storeButton(_:for:)](<../swiftui/view/storebutton(__for_).md>) — Specifies the visibility of auxiliary buttons that store view and subscription store view instances may use.
- [subscriptionStoreSignInAction(_:)](<../swiftui/view/subscriptionstoresigninaction(__).md>) — Adds an action to perform when a person uses the sign-in button on a subscription store view within a view.
- [SubscriptionOfferViewButtonKind](subscriptionofferviewbuttonkind.md)
