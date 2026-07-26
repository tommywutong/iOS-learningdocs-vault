---
title: 'persistentContainerWithName:managedObjectModel:'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentcontainer/persistentcontainerwithname:managedobjectmodel:'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcontainer/persistentcontainerwithname:managedobjectmodel:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcontainer/persistentcontainerwithname%3Amanagedobjectmodel%3A.json'
content_hash: 'sha256:4af54655bdd18404'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentContainer](../nspersistentcontainer.md)

# persistentContainerWithName:managedObjectModel:

<sub>Type Method</sub>

Initializes a new persistent container using the provided name and managed object model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) persistentContainerWithName:(NSString *) name managedObjectModel:(NSManagedObjectModel *) model;
```

## Parameters

- `name` — Name of the persistent container.

- `model` — The [NSManagedObjectModel](../nsmanagedobjectmodel.md) object to be used by the persistent container.

## Return Value

An initialized persistent container using the passed in name and model; or `nil` if the container could not be initialized.

## Discussion

This method invokes [- initWithName:managedObjectModel:](<init(name_managedobjectmodel_).md>) and returns the initialized persistent container. This method uses the provided [NSManagedObjectModel](../nsmanagedobjectmodel.md) object, whereas [persistentContainerWithName:](persistentcontainerwithname_.md) searches the application bundle for a model with the passed in name.

## See Also

### Creating a Container

- [- initWithName:](<init(name_).md>) — Creates a container with the specified name.
- [- initWithName:managedObjectModel:](<init(name_managedobjectmodel_).md>) — Create a container with the specified name and managed object model.
- [persistentContainerWithName:](persistentcontainerwithname_.md) — Initializes a new persistent container using the provided name for the container.
