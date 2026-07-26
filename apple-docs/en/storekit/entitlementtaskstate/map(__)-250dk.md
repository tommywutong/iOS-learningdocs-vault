---
title: 'map(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/entitlementtaskstate/map(_:)-250dk'
source_url: 'https://developer.apple.com/documentation/storekit/entitlementtaskstate/map(_:)-250dk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/entitlementtaskstate/map%28_%3A%29-250dk.json'
content_hash: 'sha256:0dbdc6da77366919'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [EntitlementTaskState](../entitlementtaskstate.md)

# map(_:)

<sub>Instance Method</sub>

Returns a new state, mapping the entitlement value if successful.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func map<NewValue>(_ transform: (Value) async throws -> NewValue) async rethrows -> EntitlementTaskState<NewValue>
```

## See Also

### Helper methods

- [flatMap(_:)](<flatmap(__)-7gsnv.md>) — Returns a new state, mapping the entitlement value if successful.
- [flatMap(_:)](<flatmap(__)-66eb8.md>) — Returns a new state, mapping the entitlement value if successful.
- [map(_:)](<map(__)-8ly3v.md>) — Returns a new state, mapping the entitlement value if successful.
