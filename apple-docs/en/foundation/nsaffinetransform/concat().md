---
title: concat()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsaffinetransform/concat()
source_url: 'https://developer.apple.com/documentation/foundation/nsaffinetransform/concat()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsaffinetransform/concat%28%29.json'
content_hash: 'sha256:474bb0fd5d57840e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAffineTransform](../nsaffinetransform.md)

# concat()

<sub>Instance Method</sub>

Appends the receiver’s matrix to the current transformation matrix stored in the current graphics context, replacing the current transformation matrix with the result.

<sub>macOS</sub>

```swift
func concat()
```

## Discussion

Concatenation is performed by matrix multiplication—see Manipulating Transform Values.

If this method is invoked from within an `NSView`[draw(_:)](<../../appkit/nsview/draw(__).md>) method, then the current transformation matrix is an accumulation of the screen, window, and any superview’s transformation matrices. Invoking this method defines a new user coordinate system whose coordinates are mapped into the former coordinate system according to the receiver’s transformation matrix. To undo the concatenation, you must invert the receiver’s matrix and invoke this method again.

## See Also

### Related Documentation

- [- invert](<invert().md>) — Replaces the receiver’s matrix with its inverse matrix.

### Setting and Building the Current Transformation Matrix

- [- set](<set().md>) — Sets the current transformation matrix to the receiver’s transformation matrix.
