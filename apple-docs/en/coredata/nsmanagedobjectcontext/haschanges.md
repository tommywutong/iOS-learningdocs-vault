---
title: hasChanges
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/haschanges
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/haschanges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/haschanges.json'
content_hash: 'sha256:0de41f891fd18e7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# hasChanges

<sub>Instance Property</sub>

A Boolean value that indicates whether the context has uncommitted changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hasChanges: Bool { get }
```

## Discussion

If you are observing this property using key-value observing (KVO) you should not touch the context or its objects within your implementation of [observeValue(forKeyPath:of:change:context:)](<../../objectivec/nsobject-swift.class/observevalue(forkeypath_of_change_context_).md>) for this notification. (This is because of the intricacy of the locations of the KVO notifications—for example, the context may be in the middle of an undo operation, or repairing a merge conflict.) If you need to send messages to the context or change any of its managed objects as a result of a change to the value of `hasChanges`, you must do so after the call stack unwinds (typically using [perform(_:with:afterDelay:)](<../../objectivec/nsobject-swift.class/perform(__with_afterdelay_).md>) or a similar method).

### Special Considerations

In macOS 10.6 and later, this property is [Key-value observing](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16) compliant.

## See Also

### Managing unsaved and uncommitted changes

- [- save:](<save().md>) — Attempts to commit unsaved changes to registered objects to the context’s parent store.
