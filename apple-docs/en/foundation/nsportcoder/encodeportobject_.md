---
title: 'encodePortObject:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsportcoder/encodeportobject:'
source_url: 'https://developer.apple.com/documentation/foundation/nsportcoder/encodeportobject:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsportcoder/encodeportobject%3A.json'
content_hash: 'sha256:0db73915d56291cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPortCoder](../nsportcoder.md)

# encodePortObject:

<sub>Instance Method</sub>

Encodes a given port so it can be properly reconstituted in the receiving process or thread.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) encodePortObject:(NSPort *) aport;
```

## Parameters

- `aport` — The port to encode.

## Discussion

This method is primarily for use by `NSPort` objects themselves—you can always use the general `encode...Object:` methods to encode any object.

`NSPort` invokes this method in its [- encodeWithCoder:](<../nscoding/encode(with_).md>) method so that the appropriate kernel information for the port can be encoded. A subclass of `NSPortCoder` should not encode an `NSPort` by sending it an [- encodeWithCoder:](<../nscoding/encode(with_).md>) message. See [Subclassing NSCoder](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Articles/subclassing.html#//apple_ref/doc/uid/20000951) for more information.

## See Also

### Encoding NSPort Objects

- [decodePortObject](decodeportobject.md) — Decodes and returns an `NSPort` object that was previously encoded with any of the general `encode...Object:` messages. _(deprecated)_
