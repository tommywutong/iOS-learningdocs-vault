---
title: removingPercentEncoding
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring/removingpercentencoding
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/removingpercentencoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/removingpercentencoding.json'
content_hash: 'sha256:9a6af0a17b7b10db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# removingPercentEncoding

<sub>Instance Property</sub>

Returns a new string made from the receiver by replacing all percent encoded sequences with the matching UTF-8 characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var removingPercentEncoding: String? { get }
```

## Return Value

A new string with the percent-encoded sequences removed, or `nil` if the receiver contains an invalid percent-encoding sequence.

## Discussion

> [!important] Important
> You must call this method only on strings that you know to be percent-encoded. Calling this method on strings that are not percent-encoded can lead to misinterpreting a percent character as the beginning of a percent-encoded sequence.

## See Also

### Related Documentation

- [- stringByReplacingPercentEscapesUsingEncoding:](<replacingpercentescapes(using_).md>) — Returns a new string made by replacing in the receiver all percent escapes with the matching characters as determined by a given encoding. _(deprecated)_
- [- stringByAddingPercentEscapesUsingEncoding:](<addingpercentescapes(using_).md>) — Returns a representation of the receiver using a given encoding to determine the percent escapes necessary to convert the receiver into a legal URL string. _(deprecated)_

### Working with URL Strings

- [- stringByAddingPercentEncodingWithAllowedCharacters:](<addingpercentencoding(withallowedcharacters_).md>) — Returns a new string made from the receiver by replacing all characters not in the specified set with percent-encoded characters.
