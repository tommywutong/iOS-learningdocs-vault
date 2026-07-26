---
title: 'currentPersistentHistoryToken(fromStores:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstorecoordinator/currentpersistenthistorytoken(fromstores:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/currentpersistenthistorytoken(fromstores:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/currentpersistenthistorytoken%28fromstores%3A%29.json'
content_hash: 'sha256:354bdbfa7d57d1b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# currentPersistentHistoryToken(fromStores:)

<sub>Instance Method</sub>

Returns a single persistent history token representing all of the specified stores.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func currentPersistentHistoryToken(fromStores stores: [Any]?) -> NSPersistentHistoryToken?
```

## Parameters

- `stores` — The persistent stores of interest.

## Return Value

A persistent history token, or `nil` if the coordinator can’t create one.

## Discussion

If you specify `nil` or provide an empty array, the coordinator attempts to create a token for all of its registered stores.

## See Also

### Maintaining a record of changes

- [NSPersistentHistoryTrackingKey](../nspersistenthistorytrackingkey.md) — The key you use to enable persistent history tracking.
