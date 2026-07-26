---
title: 'existingObject(with:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectcontext/existingobject(with:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/existingobject(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/existingobject%28with%3A%29.json'
content_hash: 'sha256:097424ebf1f3c84c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# existingObject(with:)

<sub>Instance Method</sub>

Returns an existing object from either the context or the persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func existingObject(with objectID: NSManagedObjectID) throws -> NSManagedObject
```

## Parameters

- `objectID` — The identifier of the object to retrieve. For more information, see [NSManagedObjectID](../nsmanagedobjectid.md).

## Return Value

The identified object from either the context or the persistent store.

## Discussion

If the context recognizes the specified object, the method returns that object. Otherwise, the context fetches and returns a fully realized object from the persistent store; unlike [- objectWithID:](<object(with_).md>), this method never returns a fault. If the object doesn’t exist in both the context and the persistent store, the method throws an error.

## See Also

### Registering and fetching objects

- [fetch(_:)](<fetch(__)-38ys1.md>) — Returns an array of objects that meet the criteria of the specified fetch request.
- [fetch(_:)](<fetch(__)-4xeoz.md>) — Returns an array of items of the specified type that meet the fetch request’s critieria.
- [- countForFetchRequest:error:](<count(for_)-93zbm.md>) — Returns the number of objects the specified request fetches when it executes.
- [- objectRegisteredForID:](<registeredobject(for_).md>) — Returns an object that exists in the context.
- [- objectWithID:](<object(with_).md>) — Returns either an existing object from the context or a fault that represents that object.
- [registeredObjects](registeredobjects.md) — The set of registered managed objects in the context.
- [count(for:)](<count(for_)-3r91z.md>) — Returns a count of the objects the specified request fetches when it executes.
- [- executeRequest:error:](<execute(__).md>) — Passes a request to the persistent store without affecting the contents of the managed object context, and returns a persistent store result.
- [- refreshAllObjects](<refreshallobjects().md>) — Refreshes all of the registered managed objects in the context.
- [retainsRegisteredObjects](retainsregisteredobjects.md) — A Boolean value that indicates whether the context keeps strong references to all registered managed objects.
