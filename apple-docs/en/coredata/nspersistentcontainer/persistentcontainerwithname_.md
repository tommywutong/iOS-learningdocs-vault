---
title: 'persistentContainerWithName:'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentcontainer/persistentcontainerwithname:'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcontainer/persistentcontainerwithname:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcontainer/persistentcontainerwithname%3A.json'
content_hash: 'sha256:45f1028f8c2d3a2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentContainer](../nspersistentcontainer.md)

# persistentContainerWithName:

<sub>Type Method</sub>

Initializes a new persistent container using the provided name for the container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) persistentContainerWithName:(NSString *) name;
```

## Parameters

- `name` — The name of the persistent container.

## Return Value

An initialized persistent container using the passed in name, or `nil` if the container could not be initialized.

## Discussion

This convenience method will invoke [- initWithName:](<init(name_).md>) and returns the initialized persistent container.

## See Also

### Creating a Container

- [- initWithName:](<init(name_).md>) — Creates a container with the specified name.
- [- initWithName:managedObjectModel:](<init(name_managedobjectmodel_).md>) — Create a container with the specified name and managed object model.
- [persistentContainerWithName:managedObjectModel:](persistentcontainerwithname_managedobjectmodel_.md) — Initializes a new persistent container using the provided name and managed object model.
