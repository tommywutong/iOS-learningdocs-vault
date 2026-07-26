---
title: PaymentMethodBinding.PaymentMethodBindingError.failed
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.4+, iPadOS 16.4+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/paymentmethodbinding/paymentmethodbindingerror/failed
source_url: 'https://developer.apple.com/documentation/storekit/paymentmethodbinding/paymentmethodbindingerror/failed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/paymentmethodbinding/paymentmethodbindingerror/failed.json'
content_hash: 'sha256:61d107231210248a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [PaymentMethodBinding](../../paymentmethodbinding.md) · [PaymentMethodBindingError](../paymentmethodbindingerror.md)

# PaymentMethodBinding.PaymentMethodBindingError.failed

<sub>Case</sub>

The initialization or binding operation failed.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case failed
```

## Discussion

The methods of the [PaymentMethodBinding](../../paymentmethodbinding.md) struct can fail if the app isn’t entitled to use this API, or if other errors occur.

## See Also

### Getting error codes

- [PaymentMethodBinding.PaymentMethodBindingError.invalidPinningID](invalidpinningid.md) — The in-app binding identifier is invalid or expired.
- [PaymentMethodBinding.PaymentMethodBindingError.notEligible](noteligible.md) — The user isn’t eligible.
