---
title: options
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstoredescription/options
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoredescription/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoredescription/options.json'
content_hash: 'sha256:90b67ddb47e9cb08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreDescription](../nspersistentstoredescription.md)

# options

<sub>Instance Property</sub>

A dictionary representation of the options set on the associated persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var options: [String : NSObject] { get }
```

## Discussion

A dictionary containing key-value pairs that specify numerous settings for the persistent store. For key definitions, see [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md).

## See Also

### Accessing the Configuration Options

- [sqlitePragmas](sqlitepragmas.md) — The SQLite pragmas set for the associated persistent store. (read-only)
