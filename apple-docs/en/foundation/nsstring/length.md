---
title: length
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring/length
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/length'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/length.json'
content_hash: 'sha256:e5dd78e7fd78e605'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# length

<sub>Instance Property</sub>

The number of UTF-16 code units in the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var length: Int { get }
```

## Discussion

This number includes the individual characters of composed character sequences, so you cannot use this property to determine if a string will be visible when printed or how long it will appear.

## See Also

### Related Documentation

- [- sizeWithAttributes:](<size(withattributes_).md>) — Returns the bounding box size the receiver occupies when drawn with the given attributes.

### Getting a String’s Length

- [- lengthOfBytesUsingEncoding:](<lengthofbytes(using_).md>) — Returns the number of bytes required to store the receiver in a given encoding.
- [- maximumLengthOfBytesUsingEncoding:](<maximumlengthofbytes(using_).md>) — Returns the maximum number of bytes needed to store the receiver in a given encoding.
