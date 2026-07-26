---
title: defaultCStringEncoding
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/defaultcstringencoding
source_url: 'https://developer.apple.com/documentation/swift/string/defaultcstringencoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/defaultcstringencoding.json'
content_hash: 'sha256:5a86496486a5a77b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# defaultCStringEncoding

<sub>Type Property</sub>

The C-string encoding assumed for any method accepting a C string as an argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var defaultCStringEncoding: String.Encoding { get }
```

## See Also

### Working with Encodings

- [availableStringEncodings](availablestringencodings.md) — An array of the encodings that strings support in the application’s environment.
- [localizedName(of:)](<localizedname(of_).md>) — Returns a human-readable string giving the name of the specified encoding.
- [isContiguousUTF8](iscontiguousutf8.md) — Returns whether this string’s storage contains validly-encoded UTF-8 contents in contiguous memory.
- [makeContiguousUTF8()](<makecontiguousutf8().md>) — If this string is not contiguous, make it so. If this mutates the string, it will invalidate any pre-existing indices.
- [withUTF8(_:)](<withutf8(__).md>) — Runs `body` over the content of this string in contiguous memory. If this string is not contiguous, this will first make it contiguous, which will also speed up subsequent access. If this mutates the string, it will invalidate any pre-existing indices.
