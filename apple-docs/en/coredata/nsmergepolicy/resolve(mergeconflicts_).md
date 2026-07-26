---
title: 'resolve(mergeConflicts:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmergepolicy/resolve(mergeconflicts:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmergepolicy/resolve(mergeconflicts:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmergepolicy/resolve%28mergeconflicts%3A%29.json'
content_hash: 'sha256:da9a96cb7035f1fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMergePolicy](../nsmergepolicy.md)

# resolve(mergeConflicts:)

<sub>Instance Method</sub>

Resolves the conflicts in a given list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resolve(mergeConflicts list: [Any]) throws
```

## Parameters

- `list` — An array of merge conflicts (instances of [NSMergeConflict](../nsmergeconflict.md)).

## Discussion

If you override this method in a subclass, you should typically invoke the superclass’s implementation in addition to performing your own operations.

## See Also

### Resolving a Conflict

- [- resolveConstraintConflicts:error:](<resolve(constraintconflicts_).md>) — Resolves the conflicts in a given list.
- [- resolveOptimisticLockingVersionConflicts:error:](<resolve(optimisticlockingconflicts_).md>) — Resolves the conflicts in a given list.
