---
title: subscribe()
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolstyleconfiguration/option/subscribe()
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/option/subscribe()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyleconfiguration/option/subscribe%28%29.json'
content_hash: 'sha256:1385e6c9db913724'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SubscriptionStoreControlStyleConfiguration](../../subscriptionstorecontrolstyleconfiguration.md) · [Option](../option.md)

# subscribe()

<sub>Instance Method</sub>

Initiates a purchase when a customer activates a control to subscribe to the option.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func subscribe()
```

## Discussion

Call the [subscribe()](<subscribe().md>) method within your custom style when the customer chooses to make a purchase.

> [!important] Important
> Don’t call purchase methods, such as [purchase(confirmIn:options:)](<../../product/purchase(confirmin_options_)-8eai6.md>), on the [subscription](subscription.md) property from your custom style.
