---
title: transform
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsaffinetransform/transform
source_url: 'https://developer.apple.com/documentation/foundation/nsaffinetransform/transform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsaffinetransform/transform.json'
content_hash: 'sha256:13877730e68461c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAffineTransform](../nsaffinetransform.md)

# transform

<sub>Type Method</sub>

Creates a new affine transform initialized to the identity matrix.

<sub>Mac Catalyst, macOS</sub>

```objc
+ (NSAffineTransform *) transform;
```

## Return Value

A new identity transform object. This matrix transforms any point to the same point.

## See Also

### Related Documentation

- [Cocoa Drawing Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40003290)

### Creating an Affine Transform

- [- init](<init().md>) — Initializes an affine transform matrix to the identity matrix.
- [- initWithTransform:](<init(transform_).md>) — Initializes the receiver’s matrix using another transform object.
