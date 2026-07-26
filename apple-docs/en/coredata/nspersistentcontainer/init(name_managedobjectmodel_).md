---
title: 'init(name:managedObjectModel:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentcontainer/init(name:managedobjectmodel:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcontainer/init(name:managedobjectmodel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcontainer/init%28name%3Amanagedobjectmodel%3A%29.json'
content_hash: 'sha256:036c607040aa7826'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentContainer](../nspersistentcontainer.md)

# init(name:managedObjectModel:)

<sub>Initializer</sub>

Create a container with the specified name and managed object model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(name: String, managedObjectModel model: NSManagedObjectModel)
```

## Parameters

- `name` — The name used by the persistent container.

- `model` — The managed object model to be used by the persistent container.

## Return Value

A persistent container initialized with the given name and model.

## Discussion

By default, the provided name value of the container is used as the name of the persisent store associated with the container. Passing in the [NSManagedObjectModel](../nsmanagedobjectmodel.md) object overrides the lookup of the model by the provided name value.

## See Also

### Creating a Container

- [- initWithName:](<init(name_).md>) — Creates a container with the specified name.
