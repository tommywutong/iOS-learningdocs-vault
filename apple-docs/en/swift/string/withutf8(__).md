---
title: 'withUTF8(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/withutf8(_:)'
source_url: 'https://developer.apple.com/documentation/swift/string/withutf8(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/withutf8%28_%3A%29.json'
content_hash: 'sha256:24af2c943cd82fbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# withUTF8(_:)

<sub>Instance Method</sub>

Runs `body` over the content of this string in contiguous memory. If this string is not contiguous, this will first make it contiguous, which will also speed up subsequent access. If this mutates the string, it will invalidate any pre-existing indices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func withUTF8<R, E>(_ body: (UnsafeBufferPointer<UInt8>) throws(E) -> R) throws(E) -> R where E : Error
```

## Discussion

Note that it is unsafe to escape the pointer provided to `body`. For example, strings of up to 15 UTF-8 code units in length may be represented in a small-string representation, and thus will be spilled into temporary stack space which is invalid after `withUTF8` finishes execution.

Complexity: O(n) if non-contiguous, O(1) if already contiguous

## See Also

### Working with Encodings

- [availableStringEncodings](availablestringencodings.md) — An array of the encodings that strings support in the application’s environment.
- [defaultCStringEncoding](defaultcstringencoding.md) — The C-string encoding assumed for any method accepting a C string as an argument.
- [localizedName(of:)](<localizedname(of_).md>) — Returns a human-readable string giving the name of the specified encoding.
- [isContiguousUTF8](iscontiguousutf8.md) — Returns whether this string’s storage contains validly-encoded UTF-8 contents in contiguous memory.
- [makeContiguousUTF8()](<makecontiguousutf8().md>) — If this string is not contiguous, make it so. If this mutates the string, it will invalidate any pre-existing indices.
