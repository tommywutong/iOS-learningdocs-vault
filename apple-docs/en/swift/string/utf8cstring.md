---
title: utf8CString
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/utf8cstring
source_url: 'https://developer.apple.com/documentation/swift/string/utf8cstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/utf8cstring.json'
content_hash: 'sha256:6dd1da24b0cc5342'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# utf8CString

<sub>Instance Property</sub>

A contiguously stored null-terminated UTF-8 representation of the string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var utf8CString: ContiguousArray<CChar> { get }
```

## Discussion

To access the underlying memory, invoke `withUnsafeBufferPointer` on the array.

```swift
let s = "Hello!"
let bytes = s.utf8CString
print(bytes)
// Prints "[72, 101, 108, 108, 111, 33, 0]"

bytes.withUnsafeBufferPointer { ptr in
    print(strlen(ptr.baseAddress!))
}
// Prints "6"
```

## See Also

### Getting C Strings

- [withCString(_:)](<withcstring(__).md>) — Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of UTF-8 code units.
- [withCString(encodedAs:_:)](<withcstring(encodedas___).md>) — Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of code units.
