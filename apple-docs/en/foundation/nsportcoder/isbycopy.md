---
title: isBycopy
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsportcoder/isbycopy
source_url: 'https://developer.apple.com/documentation/foundation/nsportcoder/isbycopy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsportcoder/isbycopy.json'
content_hash: 'sha256:682beb5c55b2ea75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPortCoder](../nsportcoder.md)

# isBycopy

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the receiver is encoding an object by copying it.

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) isBycopy;
```

## Return Value

[true](../../swift/true.md) if the receiver is encoding an object by copying it, [false](../../swift/false.md) if it expects a proxy.

## Discussion

See [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i) for more information.

## See Also

### Checking for Encoding

- [isByref](isbyref.md) — Returns a Boolean value that indicates whether the receiver is encoding an object by reference. _(deprecated)_
