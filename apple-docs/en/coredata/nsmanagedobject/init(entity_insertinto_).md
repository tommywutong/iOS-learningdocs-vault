---
title: 'init(entity:insertInto:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobject/init(entity:insertinto:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/init(entity:insertinto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/init%28entity%3Ainsertinto%3A%29.json'
content_hash: 'sha256:d6ac4a6fa44667cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# init(entity:insertInto:)

<sub>Initializer</sub>

Initializes a managed object from an entity description and inserts it into the specified managed object context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(entity: NSEntityDescription, insertInto context: NSManagedObjectContext?)
```

## Parameters

- `entity` — The entity of which to create an instance. The model associated with `context`’s persistent store coordinator must contain `entity`.

- `context` — The context into which the new instance is inserted.

## Return Value

An initialized instance of the appropriate class for `entity`.

## Discussion

`NSManagedObject` uses dynamic class generation to support the Objective-C 2 properties feature (see Declared Properties) by automatically creating a subclass of the class appropriate for `entity`. `initWithEntity:insertIntoManagedObjectContext:` therefore returns an instance of the appropriate class for `entity`. The dynamically-generated subclass will be based on the class specified by the entity, so specifying a custom class in your model will supersede the class passed to `alloc`.

If `context` is not `nil`, this method invokes `[context insertObject:self]` (which causes [- awakeFromInsert](<awakefrominsert().md>) to be invoked).

You are discouraged from overriding this method—you should instead override [- awakeFromInsert](<awakefrominsert().md>) and/or [- awakeFromFetch](<awakefromfetch().md>) (if there is logic common to these methods, it should be factored into a third method which is invoked from both). If you do perform custom initialization in this method, you may cause problems with undo and redo operations.

In many applications, there is no need to subsequently assign a newly-created managed object to a particular store—see [- assignObject:toPersistentStore:](<../nsmanagedobjectcontext/assign(__to_).md>). If your application has multiple stores and you do need to assign an object to a specific store, you should not do so in a managed object’s initializer method. Such an assignment is controller- not model-level logic.

> [!important] Important
> This method is the designated initializer for `NSManagedObject`. You must not initialize a managed object simply by sending it `init`.

### Special Considerations

If you override [- initWithEntity:insertIntoManagedObjectContext:](<init(entity_insertinto_).md>), you _must_ ensure that you set `self` to the return value from invocation of `super`’s implementation, as shown in the following example:

```objc
- (id)initWithEntity:(NSEntityDescription*)entity insertIntoManagedObjectContext:(NSManagedObjectContext*)context
{
    self = [super initWithEntity:entity insertIntoManagedObjectContext:context];
    if (self != nil) {
        // Perform additional initialization.
    }
    return self;
}
```

## See Also

### Related Documentation

- [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)
- [+ insertNewObjectForEntityForName:inManagedObjectContext:](<../nsentitydescription/insertnewobject(forentityname_into_).md>) — Creates, configures, and returns an instance of the class for the entity with a given name.

### Creating a Managed Object

- [- initWithContext:](<init(context_).md>) — Initializes a managed object subclass and inserts it into the specified managed object context.
