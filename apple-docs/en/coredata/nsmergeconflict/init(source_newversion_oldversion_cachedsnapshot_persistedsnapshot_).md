---
title: 'init(source:newVersion:oldVersion:cachedSnapshot:persistedSnapshot:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmergeconflict/init(source:newversion:oldversion:cachedsnapshot:persistedsnapshot:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmergeconflict/init(source:newversion:oldversion:cachedsnapshot:persistedsnapshot:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmergeconflict/init%28source%3Anewversion%3Aoldversion%3Acachedsnapshot%3Apersistedsnapshot%3A%29.json'
content_hash: 'sha256:a993d7c2fd5b27ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMergeConflict](../nsmergeconflict.md)

# init(source:newVersion:oldVersion:cachedSnapshot:persistedSnapshot:)

<sub>Initializer</sub>

Initializes a merge conflict.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(source srcObject: NSManagedObject, newVersion newvers: Int, oldVersion oldvers: Int, cachedSnapshot cachesnap: [String : Any]?, persistedSnapshot persnap: [String : Any]?)
```

## Parameters

- `srcObject` — The source object for the conflict.

- `newvers` — The new version number for the change. A value of 0 means the object was deleted and the corresponding snapshot is `nil`.

- `oldvers` — The old version number for the change.

- `cachesnap` — A dictionary containing the values of `srcObject` held in the persistent store coordinator layer.

- `persnap` — A dictionary containing the values of `srcObject` held in the persistent store.

## Return Value

A merge conflict object initialized with the given parameters.

## See Also

### Related Documentation

- [Core Data Model Versioning and Data Migration Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/Introduction.html#//apple_ref/doc/uid/TP40004399)
