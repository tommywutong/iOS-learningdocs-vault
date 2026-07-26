---
title: 'execute(_:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectcontext/execute(_:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/execute(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/execute%28_%3A%29.json'
content_hash: 'sha256:21ad3c0021724622'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# execute(_:)

<sub>Instance Method</sub>

Passes a request to the persistent store without affecting the contents of the managed object context, and returns a persistent store result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func execute(_ request: NSPersistentStoreRequest) throws -> NSPersistentStoreResult
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
- [count(for:)](<count(for_)-3r91z.md>) — Returns a count of the objects the specified request fetches when it executes.
- [- refreshAllObjects](<refreshallobjects().md>) — Refreshes all of the registered managed objects in the context.
- [retainsRegisteredObjects](retainsregisteredobjects.md) — A Boolean value that indicates whether the context keeps strong references to all registered managed objects.
