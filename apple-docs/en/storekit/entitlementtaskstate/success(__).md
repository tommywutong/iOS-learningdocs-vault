---
title: 'EntitlementTaskState.success(_:)'
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/entitlementtaskstate/success(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/entitlementtaskstate/success(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/entitlementtaskstate/success%28_%3A%29.json'
content_hash: 'sha256:9262f6587ad0cf71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [EntitlementTaskState](../entitlementtaskstate.md)

# EntitlementTaskState.success(_:)

<sub>Case</sub>

The task successfully loaded the entitlement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case success(Value)
```

## See Also

### Getting the task state

- [EntitlementTaskState.loading](loading.md) — The task is loading the entitlement in the background.
- [EntitlementTaskState.failure(_:)](<failure(__).md>) — The task failed to load the entitlement, with an error.
