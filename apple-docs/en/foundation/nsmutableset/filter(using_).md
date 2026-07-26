---
title: 'filter(using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableset/filter(using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableset/filter(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableset/filter%28using%3A%29.json'
content_hash: 'sha256:e92fbf830581db04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableSet](../nsmutableset.md)

# filter(using:)

<sub>Instance Method</sub>

Evaluates a given predicate against the set’s content and removes from the set those objects for which the predicate returns false.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func filter(using predicate: NSPredicate)
```

## Parameters

- `predicate` — A predicate.

## Discussion

The following example illustrates the use of this method.

```objc
NSMutableSet *mutableSet =
    [NSMutableSet setWithObjects:@"One", @"Two", @"Three", @"Four", nil];
NSPredicate *predicate =
    [NSPredicate predicateWithFormat:@"SELF beginswith 'T'"];
[mutableSet filterUsingPredicate:predicate];
// mutableSet contains (Two, Three)
```

## See Also

### Adding and removing entries

- [- addObject:](<add(__).md>) — Adds a given object to the set, if it is not already a member.
- [- removeObject:](<remove(__).md>) — Removes a given object from the set.
- [- removeAllObjects](<removeallobjects().md>) — Empties the set of all of its members.
- [- addObjectsFromArray:](<addobjects(from_).md>) — Adds to the set each object contained in a given array that is not already a member.
