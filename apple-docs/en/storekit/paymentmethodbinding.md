---
title: PaymentMethodBinding
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.4+, iPadOS 16.4+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/paymentmethodbinding
source_url: 'https://developer.apple.com/documentation/storekit/paymentmethodbinding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/paymentmethodbinding.json'
content_hash: 'sha256:1ac5f0c2126ebbea'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# PaymentMethodBinding

<sub>Structure</sub>

A binding that makes payment methods available in apps for an Apple Account.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct PaymentMethodBinding
```

## Overview

This functionality is available only to eligible apps with server entitlements. The initializer [init(id:)](<paymentmethodbinding/init(id_).md>) throws an error if your app doesn’t have the appropriate entitlement to use this API, or if the user isn’t eligible.

> [!important] Important
> The [init(id:)](<paymentmethodbinding/init(id_).md>) and [bind()](<paymentmethodbinding/bind().md>) methods may display a system prompt that asks users to authenticate with their Apple Account. Call these methods only after an explicit user action, like tapping or clicking a button.

Initialize this structure using the in-app binding identifier that your server receives from the Apple server when your server initiates payment method binding. Call the [bind()](<paymentmethodbinding/bind().md>) method to prompt users to confirm adding the payment method and making it their primary payment method.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Identifiable](../swift/identifiable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Determining eligiblity

- [init(id:)](<paymentmethodbinding/init(id_).md>) — Creates the payment method binding for eligible apps and users.

### Creating and identifying bindings

- [id](paymentmethodbinding/id.md) — The in-app binding identifier.

### Binding payment methods

- [bind()](<paymentmethodbinding/bind().md>) — Asks the user to confirm whether to add the payment method to their Apple payment methods.

### Reading errors

- [PaymentMethodBindingError](paymentmethodbinding/paymentmethodbindingerror.md) — Error information for payment method binding.
