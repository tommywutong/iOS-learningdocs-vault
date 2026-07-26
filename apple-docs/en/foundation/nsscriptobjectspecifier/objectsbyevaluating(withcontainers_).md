---
title: 'objectsByEvaluating(withContainers:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptobjectspecifier/objectsbyevaluating(withcontainers:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/objectsbyevaluating(withcontainers:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptobjectspecifier/objectsbyevaluating%28withcontainers%3A%29.json'
content_hash: 'sha256:2abf4913470d5a56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptObjectSpecifier](../nsscriptobjectspecifier.md)

# objectsByEvaluating(withContainers:)

<sub>Instance Method</sub>

Returns the actual object or objects specified by the receiver as evaluated in the context of given container object.

<sub>Mac Catalyst, macOS</sub>

```swift
func objectsByEvaluating(withContainers containers: Any) -> Any?
```

## Return Value

The actual object or objects specified by the receiver as evaluated in the context of its container object or objects (`containers`).

## Discussion

Invokes [- indicesOfObjectsByEvaluatingWithContainer:count:](<indicesofobjectsbyevaluating(withcontainer_count_).md>) on `self` to get an array of pointers to indices of elements in `containers` that have values paired with the message receiver’s key. This method then uses key-value coding to obtain the object or objects associated with the key; it returns these objects or `nil` if there are no matching values in containers. If there are multiple matching values, they are returned in an `NSArray`; if matching values are `nil`, `NSNull` objects are substituted. If `containers` is an `NSArray`, the method recursively evaluates each element in the array and returns an `NSArray` with evaluated objects (including `NSNulls`) in their corresponding slots.

## See Also

### Evaluating an object specifier

- [- indicesOfObjectsByEvaluatingWithContainer:count:](<indicesofobjectsbyevaluating(withcontainer_count_).md>) — This primitive method must be overridden by subclasses to return a pointer to an array of indices identifying objects in the key of a given container that are identified by the receiver of the message.
- [objectsByEvaluatingSpecifier](objectsbyevaluatingspecifier.md) — Returns the actual object represented by the nested series of object specifiers.
