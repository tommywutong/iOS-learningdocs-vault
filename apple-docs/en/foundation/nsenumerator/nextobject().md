---
title: nextObject()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsenumerator/nextobject()
source_url: 'https://developer.apple.com/documentation/foundation/nsenumerator/nextobject()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsenumerator/nextobject%28%29.json'
content_hash: 'sha256:60d4b9fa6da26a9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSEnumerator](../nsenumerator.md)

# nextObject()

<sub>Instance Method</sub>

Returns the next object from the collection being enumerated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nextObject() -> Any?
```

## Return Value

The next object from the collection being enumerated, or `nil` when all objects have been enumerated.

## Discussion

The following code illustrates how this method works using an array:

```objc
NSArray *anArray = // ... ;
NSEnumerator *enumerator = [anArray objectEnumerator];
id object;
 
while ((object = [enumerator nextObject])) {
    // do something with object...
}
```

## See Also

### Getting the Enumerated Objects

- [allObjects](allobjects.md) — The array of unenumerated objects.
