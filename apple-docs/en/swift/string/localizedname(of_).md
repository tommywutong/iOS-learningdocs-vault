---
title: 'localizedName(of:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/localizedname(of:)'
source_url: 'https://developer.apple.com/documentation/swift/string/localizedname(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/localizedname%28of%3A%29.json'
content_hash: 'sha256:1fd438c8cd3ff440'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# localizedName(of:)

<sub>Type Method</sub>

Returns a human-readable string giving the name of the specified encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func localizedName(of encoding: String.Encoding) -> String
```

## Parameters

- `encoding` — A string encoding. For possible values, see `String.Encoding`.

## Return Value

A human-readable string giving the name of `encoding` in the current locale.

## See Also

### Working with Encodings

- [availableStringEncodings](availablestringencodings.md) — An array of the encodings that strings support in the application’s environment.
- [defaultCStringEncoding](defaultcstringencoding.md) — The C-string encoding assumed for any method accepting a C string as an argument.
- [isContiguousUTF8](iscontiguousutf8.md) — Returns whether this string’s storage contains validly-encoded UTF-8 contents in contiguous memory.
- [makeContiguousUTF8()](<makecontiguousutf8().md>) — If this string is not contiguous, make it so. If this mutates the string, it will invalidate any pre-existing indices.
- [withUTF8(_:)](<withutf8(__).md>) — Runs `body` over the content of this string in contiguous memory. If this string is not contiguous, this will first make it contiguous, which will also speed up subsequent access. If this mutates the string, it will invalidate any pre-existing indices.
