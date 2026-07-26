---
title: PaymentMethodBinding.PaymentMethodBindingError
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.4+, iPadOS 16.4+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/paymentmethodbinding/paymentmethodbindingerror
source_url: 'https://developer.apple.com/documentation/storekit/paymentmethodbinding/paymentmethodbindingerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/paymentmethodbinding/paymentmethodbindingerror.json'
content_hash: 'sha256:8b9c31473a690c0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [PaymentMethodBinding](../paymentmethodbinding.md)

# PaymentMethodBinding.PaymentMethodBindingError

<sub>Enumeration</sub>

Error information for payment method binding.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum PaymentMethodBindingError
```

## Overview

The methods of [PaymentMethodBinding](../paymentmethodbinding.md) may return these errors, as well as the [StoreKitError.userCancelled](../storekiterror/usercancelled.md) error.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Error](../../swift/error.md), [Hashable](../../swift/hashable.md), [LocalizedError](../../foundation/localizederror.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting error codes

- [PaymentMethodBinding.PaymentMethodBindingError.failed](paymentmethodbindingerror/failed.md) — The initialization or binding operation failed.
- [PaymentMethodBinding.PaymentMethodBindingError.invalidPinningID](paymentmethodbindingerror/invalidpinningid.md) — The in-app binding identifier is invalid or expired.
- [PaymentMethodBinding.PaymentMethodBindingError.notEligible](paymentmethodbindingerror/noteligible.md) — The user isn’t eligible.
