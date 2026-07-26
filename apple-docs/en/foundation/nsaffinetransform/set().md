---
title: set()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsaffinetransform/set()
source_url: 'https://developer.apple.com/documentation/foundation/nsaffinetransform/set()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsaffinetransform/set%28%29.json'
content_hash: 'sha256:ca6227a864d5a0a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAffineTransform](../nsaffinetransform.md)

# set()

<sub>Instance Method</sub>

Sets the current transformation matrix to the receiver’s transformation matrix.

<sub>macOS</sub>

```swift
func set()
```

## Discussion

The current transformation is stored in the current graphics context and is applied to subsequent drawing operations. You should use this method sparingly because it removes the existing transformation matrix, which is an accumulation of transformation matrices for the screen, window, and any superviews. Instead use the [- concat](<concat().md>) method to add this transformation matrix to the current transformation matrix.

## See Also

### Setting and Building the Current Transformation Matrix

- [- concat](<concat().md>) — Appends the receiver’s matrix to the current transformation matrix stored in the current graphics context, replacing the current transformation matrix with the result.
