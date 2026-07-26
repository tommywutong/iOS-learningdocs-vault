---
title: 'init(context:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobject/init(context:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/init(context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/init%28context%3A%29.json'
content_hash: 'sha256:0d8ea0c466184cb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# init(context:)

<sub>Initializer</sub>

Initializes a managed object subclass and inserts it into the specified managed object context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(context moc: NSManagedObjectContext)
```

## Return Value

An initialized instance of the appropriate subclass.

## Discussion

This method is only legal to call on subclasses of `NSManagedObject` that represent a single entity in the model.

## See Also

### Creating a Managed Object

- [- initWithEntity:insertIntoManagedObjectContext:](<init(entity_insertinto_).md>) — Initializes a managed object from an entity description and inserts it into the specified managed object context.
