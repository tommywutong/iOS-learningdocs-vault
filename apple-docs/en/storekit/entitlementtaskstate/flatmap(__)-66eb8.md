---
title: 'flatMap(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/entitlementtaskstate/flatmap(_:)-66eb8'
source_url: 'https://developer.apple.com/documentation/storekit/entitlementtaskstate/flatmap(_:)-66eb8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/entitlementtaskstate/flatmap%28_%3A%29-66eb8.json'
content_hash: 'sha256:c61628f2d6192b15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [EntitlementTaskState](../entitlementtaskstate.md)

# flatMap(_:)

<sub>Instance Method</sub>

Returns a new state, mapping the entitlement value if successful.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flatMap<NewValue>(_ transform: (Value) async throws -> EntitlementTaskState<NewValue>) async rethrows -> EntitlementTaskState<NewValue>
```

## See Also

### Helper methods

- [flatMap(_:)](<flatmap(__)-7gsnv.md>) — Returns a new state, mapping the entitlement value if successful.
- [map(_:)](<map(__)-8ly3v.md>) — Returns a new state, mapping the entitlement value if successful.
- [map(_:)](<map(__)-250dk.md>) — Returns a new state, mapping the entitlement value if successful.
