---
title: 'EntitlementTaskState.failure(_:)'
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/entitlementtaskstate/failure(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/entitlementtaskstate/failure(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/entitlementtaskstate/failure%28_%3A%29.json'
content_hash: 'sha256:288179e8f18f2dea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [EntitlementTaskState](../entitlementtaskstate.md)

# EntitlementTaskState.failure(_:)

<sub>Case</sub>

The task failed to load the entitlement, with an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case failure(any Error)
```

## See Also

### Getting the task state

- [EntitlementTaskState.loading](loading.md) — The task is loading the entitlement in the background.
- [EntitlementTaskState.success(_:)](<success(__).md>) — The task successfully loaded the entitlement.
