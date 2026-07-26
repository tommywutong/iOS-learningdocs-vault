---
title: 'insertNewObject(forEntityName:into:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsentitydescription/insertnewobject(forentityname:into:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsentitydescription/insertnewobject(forentityname:into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitydescription/insertnewobject%28forentityname%3Ainto%3A%29.json'
content_hash: 'sha256:075e9fe5f0c33e79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityDescription](../nsentitydescription.md)

# insertNewObject(forEntityName:into:)

<sub>Type Method</sub>

Creates, configures, and returns an instance of the class for the entity with a given name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func insertNewObject(forEntityName entityName: String, into context: NSManagedObjectContext) -> NSManagedObject
```

## Parameters

- `entityName` — The name of an entity.

- `context` — The managed object context to use.

## Return Value

A new, autoreleased, fully configured instance of the class for the entity named `entityName`. The instance has its entity description set and is inserted it into `context`.

## Discussion

This method makes it easy for you to create instances of a given entity without worrying about the details of managed object creation. The method is conceptually similar to the following code example.

```objc
NSManagedObjectModel *managedObjectModel =
        [[context persistentStoreCoordinator] managedObjectModel];
NSEntityDescription *entity =
        [[managedObjectModel entitiesByName] objectForKey:entityName];
NSManagedObject *newObject = [[NSManagedObject alloc]
            initWithEntity:entity insertIntoManagedObjectContext:context];
return newObject;
```

## See Also

### Related Documentation

- [- initWithEntity:insertIntoManagedObjectContext:](<../nsmanagedobject/init(entity_insertinto_).md>) — Initializes a managed object from an entity description and inserts it into the specified managed object context.
