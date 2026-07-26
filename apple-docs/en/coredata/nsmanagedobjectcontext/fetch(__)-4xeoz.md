---
title: 'fetch(_:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 3.0+, macOS 10.4+, tvOS 3.0+, visionOS, watchOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectcontext/fetch(_:)-4xeoz'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/fetch(_:)-4xeoz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/fetch%28_%3A%29-4xeoz.json'
content_hash: 'sha256:5e27cd24093aa176'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# fetch(_:)

<sub>Instance Method</sub>

Returns an array of items of the specified type that meet the fetch request’s critieria.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func fetch<T>(_ request: NSFetchRequest<T>) throws -> [T] where T : NSFetchRequestResult
```

## Parameters

- `request` — The fetch request that specifies the search criteria.

## Discussion

This method fetches objects from the context and the persistent stores that you associate with the context’s persistent store coordinator. The method registers any objects it retrieves from a store with the context.

Consider the following when fetching:

- If the fetch request doesn’t have a predicate, it returns all instances of the specified entity.
- The fetch results include any object in the context that’s an instance of the request’s entity, and that meets the request’s criteria, even if the context has yet to save the object to a persistent store.
- The fetch request evalutes the in-memory state of each object. Therefore, the fetch results include any unsaved objects with changes that cause them to meet the request’s criteria, even if their counterparts in the persistent store don’t. Conversely, the results don’t include unsaved objects with in-memory changes that mean they no longer meet the criteria, even if their store versions do.
- The fetch results don’t include deleted objects, even if the context has yet to save the deletion to the persistent store.

A fetch never changes realized objects, or those with pending changes, without developer intervention. If you fetch objects, modify them, and then execute a new fetch that includes a superset of those objects, you don’t receive new instances of those objects. Instead, you receive the existing objects with their current in-memory state.

## See Also

### Registering and fetching objects

- [fetch(_:)](<fetch(__)-38ys1.md>) — Returns an array of objects that meet the criteria of the specified fetch request.
- [- countForFetchRequest:error:](<count(for_)-93zbm.md>) — Returns the number of objects the specified request fetches when it executes.
- [- objectRegisteredForID:](<registeredobject(for_).md>) — Returns an object that exists in the context.
- [- objectWithID:](<object(with_).md>) — Returns either an existing object from the context or a fault that represents that object.
- [- existingObjectWithID:error:](<existingobject(with_).md>) — Returns an existing object from either the context or the persistent store.
- [registeredObjects](registeredobjects.md) — The set of registered managed objects in the context.
- [count(for:)](<count(for_)-3r91z.md>) — Returns a count of the objects the specified request fetches when it executes.
- [- executeRequest:error:](<execute(__).md>) — Passes a request to the persistent store without affecting the contents of the managed object context, and returns a persistent store result.
- [- refreshAllObjects](<refreshallobjects().md>) — Refreshes all of the registered managed objects in the context.
- [retainsRegisteredObjects](retainsregisteredobjects.md) — A Boolean value that indicates whether the context keeps strong references to all registered managed objects.
