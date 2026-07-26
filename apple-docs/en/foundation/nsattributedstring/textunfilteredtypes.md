---
title: textUnfilteredTypes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/textunfilteredtypes
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/textunfilteredtypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/textunfilteredtypes.json'
content_hash: 'sha256:5cef1b4d8441f8cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# textUnfilteredTypes

<sub>Type Property</sub>

An array of UTI strings that identify the file types that attributed strings support directly.

<sub>macOS</sub>

```swift
class var textUnfilteredTypes: [String] { get }
```

## Return Value

An array of `NSString` objects, each of which contains a UTI identifying a supported file type.

## Discussion

The returned list includes UTI strings only for those file types that are supported directly by the receiver. It does not include types that are supported through user-installed filter services. You can use the returned UTI strings with any method that supports UTIs.

## See Also

### Getting the supported text-file formats

- [- prefersRTFDInRange:](<prefersrtfd(in_).md>) — Returns a Boolean value that indicates whether the specified range of text prefers RTFD formatting.
- [textTypes](texttypes.md) — An array of UTI strings that identify the file types that attributed strings support, either directly or through a user-installed filter service.
