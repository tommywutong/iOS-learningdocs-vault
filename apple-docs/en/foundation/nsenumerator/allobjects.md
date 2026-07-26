---
title: allObjects
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsenumerator/allobjects
source_url: 'https://developer.apple.com/documentation/foundation/nsenumerator/allobjects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsenumerator/allobjects.json'
content_hash: 'sha256:7236201efef52b8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSEnumerator](../nsenumerator.md)

# allObjects

<sub>Instance Property</sub>

The array of unenumerated objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allObjects: [Any] { get }
```

## Discussion

This array contains all the remaining objects of the enumerator in enumerated order. It does not contain objects that have already been enumerated with previous [- nextObject](<nextobject().md>) messages.

Accessing this property exhausts the enumerator’s collection so that subsequent invocations of [- nextObject](<nextobject().md>) return `nil`.

## See Also

### Related Documentation

- [Collections Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)

### Getting the Enumerated Objects

- [- nextObject](<nextobject().md>) — Returns the next object from the collection being enumerated.
