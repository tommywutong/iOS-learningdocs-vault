---
title: decodeNXColor
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nscoder/decodenxcolor
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodenxcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodenxcolor.json'
content_hash: 'sha256:c24688b3e921379b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeNXColor

<sub>Instance Method</sub>

Decodes a color structure from NEXTSTEP Release 3 or earlier.

> [!warning] Deprecated
> Apple discourages the use of this symbol.

<sub>Mac Catalyst, macOS</sub>

```objc
- (NSColor *) decodeNXColor;
```

## Return Value

An autoreleased `NSColor` object. Returns `nil` if the archived color is invalid.

## Discussion

This method does not have a matching method for encoding an `NXColor` structure. Encode an `NSColor` object instead.

`NXColor`, a type that dates from pre-OpenStep versions of NEXTSTEP, was a `struct`. Its replacement, `NSColor`, is a class. The difficulties of converting from a `struct` to a class require a special method like [decodeNXColor](decodenxcolor.md).

The [decodeNXColor](decodenxcolor.md) method becomes part of the `NSCoder` class only for apps that use AppKit.
