---
title: StringProtocol Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/stringprotocol-implementations
source_url: 'https://developer.apple.com/documentation/swift/string/stringprotocol-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/stringprotocol-implementations.json'
content_hash: 'sha256:82fa509bea6f6ccb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# StringProtocol Implementations

<sub>API Collection</sub>

## Topics

### Structures

- [UTF16View](utf16view.md) — A view of a string’s contents as a collection of UTF-16 code units.
- [UTF8View](utf8view.md) — A view of a string’s contents as a collection of UTF-8 code units.
- [UnicodeScalarView](unicodescalarview.md) — A view of a string’s contents as a collection of Unicode scalar values.

### Operators

- [!=(_:_:)](<!=(____)-frzf.md>)
- [==(_:_:)](<==(____)-8kzxf.md>)
- [\>(_:_:)](<_(____)-6o7qv.md>)
- [\<(_:_:)](<_(____)-8d1wy.md>)
- [\<=(_:_:)](<_=(____)-5y22v.md>)
- [\>=(_:_:)](<_=(____)-nd86.md>)

### Initializers

- [init(cString:)](<init(cstring_)-2p84k.md>) — Creates a new string by copying the null-terminated UTF-8 data referenced by the given pointer.
- [init(decoding:as:)](<init(decoding_as_).md>) — Creates a string from the given Unicode code units in the specified encoding.
- [init(decodingCString:as:)](<init(decodingcstring_as_)-8yowf.md>) — Creates a new string by copying the null-terminated sequence of code units referenced by the given pointer.

### Instance Properties

- [unicodeScalars](unicodescalars.md) — The string’s value represented as a collection of Unicode scalar values.
- [utf16](utf16.md) — A UTF-16 encoding of `self`.
- [utf8](utf8.md) — A UTF-8 encoding of `self`.

### Instance Methods

- [hasPrefix(_:)](<hasprefix(__).md>)
- [hasSuffix(_:)](<hassuffix(__).md>)
- [lowercased()](<lowercased().md>) — Returns a lowercase version of the string.
- [uppercased()](<uppercased().md>) — Returns an uppercase version of the string.
- [withCString(_:)](<withcstring(__).md>) — Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of UTF-8 code units.
- [withCString(encodedAs:_:)](<withcstring(encodedas___).md>) — Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of code units.
