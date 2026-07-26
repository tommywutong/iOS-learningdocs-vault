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
doc_path: /documentation/swift/substring/stringprotocol-implementations
source_url: 'https://developer.apple.com/documentation/swift/substring/stringprotocol-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/stringprotocol-implementations.json'
content_hash: 'sha256:0e01f850b265875b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md) · [Substring](../substring.md)

# StringProtocol Implementations

<sub>API Collection</sub>

## Topics

### Structures

- [UTF16View](utf16view.md)
- [UTF8View](utf8view.md)
- [UnicodeScalarView](unicodescalarview.md)

### Operators

- [!=(_:_:)](<!=(____)-fryj.md>)
- [==(_:_:)](<==(____).md>)
- [\>(_:_:)](<_(____)-6o7pz.md>)
- [\<(_:_:)](<_(____)-8d1w2.md>)
- [\<=(_:_:)](<_=(____)-5y23r.md>)
- [\>=(_:_:)](<_=(____)-nd7a.md>)

### Initializers

- [init(cString:)](<init(cstring_).md>) — Creates a string from the null-terminated, UTF-8 encoded sequence of bytes at the given pointer.
- [init(decoding:as:)](<init(decoding_as_).md>) — Creates a string from the given Unicode code units in the specified encoding.
- [init(decodingCString:as:)](<init(decodingcstring_as_).md>) — Creates a string from the null-terminated sequence of bytes at the given pointer.

### Instance Properties

- [unicodeScalars](unicodescalars.md)
- [utf16](utf16.md)
- [utf8](utf8.md)

### Instance Methods

- [hasPrefix(_:)](<hasprefix(__).md>) — Returns a Boolean value indicating whether the string begins with the specified prefix.
- [hasSuffix(_:)](<hassuffix(__).md>) — Returns a Boolean value indicating whether the string ends with the specified suffix.
- [hash(into:)](<hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.
- [lowercased()](<lowercased().md>)
- [uppercased()](<uppercased().md>)
- [withCString(_:)](<withcstring(__).md>) — Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of UTF-8 code units.
- [withCString(encodedAs:_:)](<withcstring(encodedas___).md>) — Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of code units.
