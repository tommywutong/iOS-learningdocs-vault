---
title: EntitlementTaskState.loading
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/entitlementtaskstate/loading
source_url: 'https://developer.apple.com/documentation/storekit/entitlementtaskstate/loading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/entitlementtaskstate/loading.json'
content_hash: 'sha256:8696cec47ae56695'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [EntitlementTaskState](../entitlementtaskstate.md)

# EntitlementTaskState.loading

<sub>Case</sub>

The task is loading the entitlement in the background.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case loading
```

## See Also

### Getting the task state

- [EntitlementTaskState.success(_:)](<success(__).md>) — The task successfully loaded the entitlement.
- [EntitlementTaskState.failure(_:)](<failure(__).md>) — The task failed to load the entitlement, with an error.
