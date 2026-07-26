---
title: 'count(for:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 3.0+, macOS 10.5+, tvOS 3.0+, visionOS, watchOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectcontext/count(for:)-3r91z'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/count(for:)-3r91z'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/count%28for%3A%29-3r91z.json'
content_hash: 'sha256:fad180364cf36b2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# count(for:)

<sub>Instance Method</sub>

Returns a count of the objects the specified request fetches when it executes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func count<T>(for request: NSFetchRequest<T>) throws -> Int where T : NSFetchRequestResult
```

## See Also

### Registering and fetching objects

- [fetch(_:)](<fetch(__)-38ys1.md>) — Returns an array of objects that meet the criteria of the specified fetch request.
- [fetch(_:)](<fetch(__)-4xeoz.md>) — Returns an array of items of the specified type that meet the fetch request’s critieria.
- [- countForFetchRequest:error:](<count(for_)-93zbm.md>) — Returns the number of objects the specified request fetches when it executes.
- [- objectRegisteredForID:](<registeredobject(for_).md>) — Returns an object that exists in the context.
- [- objectWithID:](<object(with_).md>) — Returns either an existing object from the context or a fault that represents that object.
- [- existingObjectWithID:error:](<existingobject(with_).md>) — Returns an existing object from either the context or the persistent store.
- [registeredObjects](registeredobjects.md) — The set of registered managed objects in the context.
- [- executeRequest:error:](<execute(__).md>) — Passes a request to the persistent store without affecting the contents of the managed object context, and returns a persistent store result.
- [- refreshAllObjects](<refreshallobjects().md>) — Refreshes all of the registered managed objects in the context.
- [retainsRegisteredObjects](retainsregisteredobjects.md) — A Boolean value that indicates whether the context keeps strong references to all registered managed objects.
