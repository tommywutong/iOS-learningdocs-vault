---
title: decodePortObject
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsportcoder/decodeportobject
source_url: 'https://developer.apple.com/documentation/foundation/nsportcoder/decodeportobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsportcoder/decodeportobject.json'
content_hash: 'sha256:63ddce555dd14145'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPortCoder](../nsportcoder.md)

# decodePortObject

<sub>Instance Method</sub>

Decodes and returns an `NSPort` object that was previously encoded with any of the general `encode...Object:` messages.

<sub>Mac Catalyst, macOS</sub>

```objc
- (NSPort *) decodePortObject;
```

## Return Value

An `NSPort` object that was previously encoded with any of the general `encode...Object:` messages.

## Discussion

This method is primarily for use by `NSPort` objects themselves—you can always use [- decodeObject](<../nscoder/decodeobject().md>) to decode any object.

`NSPort` invokes this method in its [- initWithCoder:](<../nscoding/init(coder_).md>) method so the appropriate kernel information for the port can be decoded. A subclass of `NSPortCoder` shouldn’t decode an `NSPort` by sending it an [- initWithCoder:](<../nscoding/init(coder_).md>) message. See [Subclassing NSCoder](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Articles/subclassing.html#//apple_ref/doc/uid/20000951) for more information.

## See Also

### Encoding NSPort Objects

- [encodePortObject:](encodeportobject_.md) — Encodes a given port so it can be properly reconstituted in the receiving process or thread. _(deprecated)_
