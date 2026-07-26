---
title: 'cachedSnapshots(for:editingState:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/datastore/cachedsnapshots(for:editingstate:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/datastore/cachedsnapshots(for:editingstate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/datastore/cachedsnapshots%28for%3Aeditingstate%3A%29.json'
content_hash: 'sha256:1c0bb15d88fdd27b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [DataStore](../datastore.md)

# cachedSnapshots(for:editingState:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cachedSnapshots(for persistentIdentifiers: [PersistentIdentifier], editingState: EditingState) throws -> [PersistentIdentifier : Self.Snapshot]
```

## Default Implementations

### DataStore Implementations

- [cachedSnapshots(for:editingState:)](<cachedsnapshots(for_editingstate_)-8e689.md>)

## See Also

### Sharing cached data between model contexts

- [initializeState(for:)](<initializestate(for_).md>)
- [EditingState](../editingstate.md)
- [invalidateState(for:)](<invalidatestate(for_).md>)
