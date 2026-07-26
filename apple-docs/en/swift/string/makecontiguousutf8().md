---
title: makeContiguousUTF8()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/makecontiguousutf8()
source_url: 'https://developer.apple.com/documentation/swift/string/makecontiguousutf8()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/makecontiguousutf8%28%29.json'
content_hash: 'sha256:e4b0550de4c42903'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# makeContiguousUTF8()

<sub>Instance Method</sub>

If this string is not contiguous, make it so. If this mutates the string, it will invalidate any pre-existing indices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func makeContiguousUTF8()
```

## Discussion

Complexity: O(n) if non-contiguous, O(1) if already contiguous

## See Also

### Working with Encodings

- [availableStringEncodings](availablestringencodings.md) — An array of the encodings that strings support in the application’s environment.
- [defaultCStringEncoding](defaultcstringencoding.md) — The C-string encoding assumed for any method accepting a C string as an argument.
- [localizedName(of:)](<localizedname(of_).md>) — Returns a human-readable string giving the name of the specified encoding.
- [isContiguousUTF8](iscontiguousutf8.md) — Returns whether this string’s storage contains validly-encoded UTF-8 contents in contiguous memory.
- [withUTF8(_:)](<withutf8(__).md>) — Runs `body` over the content of this string in contiguous memory. If this string is not contiguous, this will first make it contiguous, which will also speed up subsequent access. If this mutates the string, it will invalidate any pre-existing indices.
