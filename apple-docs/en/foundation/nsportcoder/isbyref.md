---
title: isByref
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsportcoder/isbyref
source_url: 'https://developer.apple.com/documentation/foundation/nsportcoder/isbyref'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsportcoder/isbyref.json'
content_hash: 'sha256:5a7bd44cc62cf612'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPortCoder](../nsportcoder.md)

# isByref

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the receiver is encoding an object by reference.

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) isByref;
```

## Return Value

[true](../../swift/true.md) if the receiver is encoding an object `byref`, [false](../../swift/false.md) if it expects a copy.

## Discussion

See [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i) for more information.

## See Also

### Checking for Encoding

- [isBycopy](isbycopy.md) — Returns a Boolean value that indicates whether the receiver is encoding an object by copying it. _(deprecated)_
