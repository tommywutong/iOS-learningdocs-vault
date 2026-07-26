---
title: 'makeObjectsPerformSelector:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/makeobjectsperformselector:'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/makeobjectsperformselector:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/makeobjectsperformselector%3A.json'
content_hash: 'sha256:eb96fdfcbee3843a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# makeObjectsPerformSelector:

<sub>Instance Method</sub>

Sends to each object in the array the message identified by a given selector, starting with the first object and continuing through the array to the last object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) makeObjectsPerformSelector:(SEL) aSelector;
```

## Parameters

- `aSelector` — A selector that identifies the message to send to the objects in the array. The method must not take any arguments, and must not have the side effect of modifying the receiving array.

## Discussion

This method raises an `NSInvalidArgumentException` if `aSelector` is `NULL`.

## See Also

### Sending Messages to Elements

- [makeObjectsPerformSelector:withObject:](makeobjectsperformselector_withobject_.md) — Sends the `aSelector` message to each object in the array, starting with the first object and continuing through the array to the last object.
- [- enumerateObjectsUsingBlock:](<enumerateobjects(__).md>) — Executes a given closure or block using each object in the array, starting with the first object and continuing through the array to the last object.
- [- enumerateObjectsWithOptions:usingBlock:](<enumerateobjects(options_using_).md>) — Executes a given closure or block using each object in the array with the specified options.
- [- enumerateObjectsAtIndexes:options:usingBlock:](<enumerateobjects(at_options_using_).md>) — Executes a given block using the objects in the array at the specified indexes.
