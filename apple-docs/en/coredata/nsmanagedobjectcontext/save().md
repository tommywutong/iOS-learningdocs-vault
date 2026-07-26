---
title: save()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/save()
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/save()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/save%28%29.json'
content_hash: 'sha256:7da038745f567660'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# save()

<sub>Instance Method</sub>

Attempts to commit unsaved changes to registered objects to the context’s parent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func save() throws
```

## Discussion

If there were multiple errors (for example several edited objects had validation failures) the description of `NSError` returned indicates that there were multiple errors, and its userInfo dictionary contains the key `NSDetailedErrors`. The value associated with the `NSDetailedErrors` key is an array that contains the individual `NSError` objects.

If a context’s parent store is a persistent store coordinator, then changes are committed to the external store. If a context’s parent store is another managed object context, then [- save:](<save().md>) only updates managed objects in that parent store. To commit changes to the external store, you must save changes in the chain of contexts up to and including the context whose parent is the persistent store coordinator.

> [!important] Important
> Always verify that the context has uncommitted changes (using the [hasChanges](haschanges.md) property) before invoking the `save:` method. Otherwise, Core Data may perform unnecessary work.

## See Also

### Managing unsaved and uncommitted changes

- [hasChanges](haschanges.md) — A Boolean value that indicates whether the context has uncommitted changes.
