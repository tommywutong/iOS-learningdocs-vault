---
title: EntitlementTaskState
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/entitlementtaskstate
source_url: 'https://developer.apple.com/documentation/storekit/entitlementtaskstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/entitlementtaskstate.json'
content_hash: 'sha256:74830b58990e5d0e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# EntitlementTaskState

<sub>Enumeration</sub>

The state of an entitlement task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum EntitlementTaskState<Value>
```

## Overview

To get an entitlement task state, use [currentEntitlementTask(for:priority:action:)](<../swiftui/view/currententitlementtask(for_priority_action_).md>) or [subscriptionStatusTask(for:priority:action:)](<../swiftui/view/subscriptionstatustask(for_priority_action_).md>) on a [View](../swiftui/view.md).

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the task state

- [EntitlementTaskState.loading](entitlementtaskstate/loading.md) — The task is loading the entitlement in the background.
- [EntitlementTaskState.success(_:)](<entitlementtaskstate/success(__).md>) — The task successfully loaded the entitlement.
- [EntitlementTaskState.failure(_:)](<entitlementtaskstate/failure(__).md>) — The task failed to load the entitlement, with an error.

### Getting the transaction with the entitlement

- [transaction](entitlementtaskstate/transaction.md) — The transaction value if the task is successful.
- [value](entitlementtaskstate/value.md) — The entitlement value if the task is successful.

### Helper methods

- [flatMap(_:)](<entitlementtaskstate/flatmap(__)-7gsnv.md>) — Returns a new state, mapping the entitlement value if successful.
- [flatMap(_:)](<entitlementtaskstate/flatmap(__)-66eb8.md>) — Returns a new state, mapping the entitlement value if successful.
- [map(_:)](<entitlementtaskstate/map(__)-8ly3v.md>) — Returns a new state, mapping the entitlement value if successful.
- [map(_:)](<entitlementtaskstate/map(__)-250dk.md>) — Returns a new state, mapping the entitlement value if successful.

## See Also

### Loading StoreKit data

- [storeProductTask(for:priority:action:)](<../swiftui/view/storeproducttask(for_priority_action_).md>) — Declares the view as dependent on an In-App Purchase product and returns a modified view.
- [storeProductsTask(for:priority:action:)](<../swiftui/view/storeproductstask(for_priority_action_).md>) — Declares the view as dependent on a collection of In-App Purchase products and returns a modified view.
- [currentEntitlementTask(for:priority:action:)](<../swiftui/view/currententitlementtask(for_priority_action_).md>) — Declares the view as dependent on the entitlement of an In-App Purchase product, and returns a modified view.
- [subscriptionStatusTask(for:priority:action:)](<../swiftui/view/subscriptionstatustask(for_priority_action_).md>) — Declares the view as dependent on the status of an auto-renewable subscription group, and returns a modified view.
- [CollectionTaskState](product/collectiontaskstate.md) — The state of a task that loads a collection of products in the background.
- [TaskState](product/taskstate.md) — The state of a task that loads a product in the background.
