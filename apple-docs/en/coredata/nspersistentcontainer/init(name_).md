---
title: 'init(name:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentcontainer/init(name:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcontainer/init(name:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcontainer/init%28name%3A%29.json'
content_hash: 'sha256:1a38150a30134c9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentContainer](../nspersistentcontainer.md)

# init(name:)

<sub>Initializer</sub>

Creates a container with the specified name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(name: String)
```

## Parameters

- `name` — The name of the [NSPersistentContainer](../nspersistentcontainer.md) object.

## Return Value

A persistent container initialized with the given name.

## Discussion

By default, the provided name value is used to name the persistent store and is used to look up the name of the [NSManagedObjectModel](../nsmanagedobjectmodel.md) object to be used with the [NSPersistentContainer](../nspersistentcontainer.md) object.

## See Also

### Creating a Container

- [- initWithName:managedObjectModel:](<init(name_managedobjectmodel_).md>) — Create a container with the specified name and managed object model.
