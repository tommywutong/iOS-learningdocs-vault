---
title: 'indicesOfObjectsByEvaluating(withContainer:count:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptobjectspecifier/indicesofobjectsbyevaluating(withcontainer:count:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/indicesofobjectsbyevaluating(withcontainer:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptobjectspecifier/indicesofobjectsbyevaluating%28withcontainer%3Acount%3A%29.json'
content_hash: 'sha256:9bc185dabf06d1ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptObjectSpecifier](../nsscriptobjectspecifier.md)

# indicesOfObjectsByEvaluating(withContainer:count:)

<sub>Instance Method</sub>

This primitive method must be overridden by subclasses to return a pointer to an array of indices identifying objects in the key of a given container that are identified by the receiver of the message.

<sub>Mac Catalyst, macOS</sub>

```swift
func indicesOfObjectsByEvaluating(withContainer container: Any, count: UnsafeMutablePointer<Int>) -> UnsafeMutablePointer<Int>?
```

## Discussion

This primitive method must be overridden by subclasses to return a pointer to an array of indices identifying objects in the key of the container `aContainer` that are identified by the receiver of the message. The method uses key-value coding to obtain values based on the receiver’s key. It returns the number of such matching objects by indirection in `numRefs`. It returns `nil` directly and –1 via `numRefs` if all objects in the container (or the sole object) match the value of the receiver’s key. This method is invoked by [- objectsByEvaluatingWithContainers:](<objectsbyevaluating(withcontainers_).md>). The default implementation returns `nil` directly and –1 indirectly via `numRefs`.

## See Also

### Evaluating an object specifier

- [objectsByEvaluatingSpecifier](objectsbyevaluatingspecifier.md) — Returns the actual object represented by the nested series of object specifiers.
- [- objectsByEvaluatingWithContainers:](<objectsbyevaluating(withcontainers_).md>) — Returns the actual object or objects specified by the receiver as evaluated in the context of given container object.
