---
title: value
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/entitlementtaskstate/value
source_url: 'https://developer.apple.com/documentation/storekit/entitlementtaskstate/value'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/entitlementtaskstate/value.json'
content_hash: 'sha256:d85e62d1225364cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [EntitlementTaskState](../entitlementtaskstate.md)

# value

<sub>Instance Property</sub>

The entitlement value if the task is successful.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var value: Value? { get }
```

## Discussion

This value is `nil` while the value is loading, or if it fails to load for any reason.

Use [value](value.md) as a convenience to access the entitlement value in code that doesn’t depend on the reason the value can’t be accessed if it fails to load.

## See Also

### Getting the transaction with the entitlement

- [transaction](transaction.md) — The transaction value if the task is successful.
