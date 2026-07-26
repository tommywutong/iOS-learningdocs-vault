---
title: 'object(with:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectcontext/object(with:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/object(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/object%28with%3A%29.json'
content_hash: 'sha256:3574c99f175336fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# object(with:)

<sub>Instance Method</sub>

Returns either an existing object from the context or a fault that represents that object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func object(with objectID: NSManagedObjectID) -> NSManagedObject
```

## Parameters

- `objectID` — The identifier of the object to retrieve. For more information, see [NSManagedObjectID](../nsmanagedobjectid.md).

## Return Value

The identified object, if its known to the context; otherwise, a fault with its [objectID](../nsmanagedobject/objectid.md) property set to `objectID`.

## Discussion

If the context doesn’t recognize the specified object, this method returns a _fault_ — a placeholder object that doesn’t load its properties until your code accesses them. The context then fetches the corresponding values from the persistent store and uses those values to turn the fault into a fully realized object.

When this method returns a fault, Core Data makes no attempts to verify the existence of the underlying object in the persistent store. If the object doesn’t exist when the context tries to the fetch the object’s values, the framework throws an exception.

## See Also

### Registering and fetching objects

- [fetch(_:)](<fetch(__)-38ys1.md>) — Returns an array of objects that meet the criteria of the specified fetch request.
- [fetch(_:)](<fetch(__)-4xeoz.md>) — Returns an array of items of the specified type that meet the fetch request’s critieria.
- [- countForFetchRequest:error:](<count(for_)-93zbm.md>) — Returns the number of objects the specified request fetches when it executes.
- [- objectRegisteredForID:](<registeredobject(for_).md>) — Returns an object that exists in the context.
- [- existingObjectWithID:error:](<existingobject(with_).md>) — Returns an existing object from either the context or the persistent store.
- [registeredObjects](registeredobjects.md) — The set of registered managed objects in the context.
- [count(for:)](<count(for_)-3r91z.md>) — Returns a count of the objects the specified request fetches when it executes.
- [- executeRequest:error:](<execute(__).md>) — Passes a request to the persistent store without affecting the contents of the managed object context, and returns a persistent store result.
- [- refreshAllObjects](<refreshallobjects().md>) — Refreshes all of the registered managed objects in the context.
- [retainsRegisteredObjects](retainsregisteredobjects.md) — A Boolean value that indicates whether the context keeps strong references to all registered managed objects.
