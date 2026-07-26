---
title: CFStringEncoding
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstringencoding
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringencoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringencoding.json'
content_hash: 'sha256:cf21351175c1fb64'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringEncoding

<sub>Type Alias</sub>

An integer type for constants used to specify supported string encodings in various CFString functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFStringEncoding = UInt32
```

## Discussion

This type is used to define the constants for the built-in encodings (see [CFStringBuiltInEncodings](cfstringbuiltinencodings.md) for a list) and for platform-dependent encodings (see [External String Encodings](external-string-encodings.md)). If CFString does not recognize or support the string encoding of a particular string, CFString functions will identify the string’s encoding as [kCFStringEncodingInvalidId](kcfstringencodinginvalidid.md).

## See Also

### Data Types

- [CFStringEncodings](cfstringencodings.md) — Index type for constants used to specify external string encodings.
- [CFStringCompareFlags](cfstringcompareflags.md) — A [CFOptionFlags](cfoptionflags.md) type for specifying options for string comparison .
- [CFStringInlineBuffer](cfstringinlinebuffer.md) — Defines the buffer and related fields used for in-line buffer access of characters in CFString objects.
