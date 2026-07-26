---
title: migrationManagerClass()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstore/migrationmanagerclass()
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstore/migrationmanagerclass()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstore/migrationmanagerclass%28%29.json'
content_hash: 'sha256:e834cf42c1dc3071'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStore](../nspersistentstore.md)

# migrationManagerClass()

<sub>Type Method</sub>

Returns the migration manager class for this store class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func migrationManagerClass() -> AnyClass
```

## Return Value

The `NSMigrationManager` class for this store class

## Discussion

In a subclass of `NSPersistentStore`, you can override this to provide a custom migration manager subclass (for example, to take advantage of store-specific functionality to improve migration performance).
