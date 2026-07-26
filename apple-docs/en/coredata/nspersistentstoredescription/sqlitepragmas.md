---
title: sqlitePragmas
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstoredescription/sqlitepragmas
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoredescription/sqlitepragmas'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoredescription/sqlitepragmas.json'
content_hash: 'sha256:941f7f1964a621e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreDescription](../nspersistentstoredescription.md)

# sqlitePragmas

<sub>Instance Property</sub>

The SQLite pragmas set for the associated persistent store. (read-only)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sqlitePragmas: [String : NSObject] { get }
```

## Discussion

This property contains all of the pragmas set on the associated persistent store. This property is only relevant when the [type](type.md) is set to [NSSQLiteStoreType](../nssqlitestoretype.md).

## See Also

### Accessing the Configuration Options

- [options](options.md) — A dictionary representation of the options set on the associated persistent store.
