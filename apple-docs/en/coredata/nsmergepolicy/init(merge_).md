---
title: 'init(merge:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmergepolicy/init(merge:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmergepolicy/init(merge:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmergepolicy/init%28merge%3A%29.json'
content_hash: 'sha256:9a576b9f0a058f77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMergePolicy](../nsmergepolicy.md)

# init(merge:)

<sub>Initializer</sub>

Returns a merge policy initialized with a given policy type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(merge ty: NSMergePolicyType)
```

## Parameters

- `ty` — A merge policy type.

## Return Value

A merge policy initialized with a given policy type.

## Discussion

If you override this method in a subclass, you should invoke the superclass’s implementation with the merge policy that is closest to the behavior you want.

- This will make it easier to use the superclass’s implementation of [- resolveConflicts:error:](<resolve(mergeconflicts_).md>) and then customize the results.
- Due to the complexity of merging to-many relationships, this class is designed with the expectation that you call super as the base implementation.

## See Also

### Related Documentation

- [Core Data Model Versioning and Data Migration Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/Introduction.html#//apple_ref/doc/uid/TP40004399)

### Getting a Merge Policy

- [mergeType](mergetype.md) — The merge type.
