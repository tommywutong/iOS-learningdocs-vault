---
title: 'filtered(using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/filtered(using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/filtered(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/filtered%28using%3A%29.json'
content_hash: 'sha256:dac1f993136ad3c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# filtered(using:)

<sub>Instance Method</sub>

Evaluates a given predicate against each object in the receiving ordered set and returns a new ordered set containing the objects for which the predicate returns true.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func filtered(using p: NSPredicate) -> NSOrderedSet
```

## Parameters

- `p` — The predicate against which to evaluate the receiving ordered set’s elements.

## Return Value

A new ordered set containing the objects in the receiving ordered set for which `p` returns true.

## Discussion

For more details, see [Predicate Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789).
