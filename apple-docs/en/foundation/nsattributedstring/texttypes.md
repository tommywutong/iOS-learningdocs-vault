---
title: textTypes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/texttypes
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/texttypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/texttypes.json'
content_hash: 'sha256:c01f599c551465e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# textTypes

<sub>Type Property</sub>

An array of UTI strings that identify the file types that attributed strings support, either directly or through a user-installed filter service.

<sub>macOS</sub>

```swift
class var textTypes: [String] { get }
```

## Return Value

An array of `NSString` objects, each of which contains a UTI identifying a supported file type.

## Discussion

The returned list includes UTIs all file types supported by the receiver plus those that can be opened by the receiver after being converted by a user-installed filter service. You can use the returned UTI strings with any method that supports UTIs.

## See Also

### Getting the supported text-file formats

- [- prefersRTFDInRange:](<prefersrtfd(in_).md>) — Returns a Boolean value that indicates whether the specified range of text prefers RTFD formatting.
- [textUnfilteredTypes](textunfilteredtypes.md) — An array of UTI strings that identify the file types that attributed strings support directly.
