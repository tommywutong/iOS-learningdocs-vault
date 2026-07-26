---
title: 'addingPercentEncoding(withAllowedCharacters:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/addingpercentencoding(withallowedcharacters:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/addingpercentencoding(withallowedcharacters:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/addingpercentencoding%28withallowedcharacters%3A%29.json'
content_hash: 'sha256:54f02f505e8d4ebd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# addingPercentEncoding(withAllowedCharacters:)

<sub>Instance Method</sub>

Returns a new string made from the receiver by replacing all characters not in the specified set with percent-encoded characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addingPercentEncoding(withAllowedCharacters allowedCharacters: CharacterSet) -> String?
```

## Parameters

- `allowedCharacters` — The characters not replaced in the string. Typically, you specify one of the predefined character sets for a particular URL component, such as [URLPathAllowedCharacterSet](../nscharacterset/urlpathallowed.md) or [URLQueryAllowedCharacterSet](../nscharacterset/urlqueryallowed.md).

## Return Value

Returns the encoded string, or `nil` if the transformation is not possible.

## Discussion

Entire URL strings cannot be percent-encoded, because each URL component specifies a different set of allowed characters. For example, the query component of a URL allows the “`@`” character, but that character must be percent-encoded in the password component.

UTF-8 encoding is used to determine the correct percent-encoded characters. Any characters in `allowedCharacters` outside of the 7-bit ASCII range are ignored.

> [!important] Important
> You must not call this method on strings that are already percent-encoded. Calling this method on strings that are already percent-encoded will cause percent characters in a percent-encoded sequence to be percent-encoded twice.

## See Also

### Related Documentation

- [- stringByReplacingPercentEscapesUsingEncoding:](<replacingpercentescapes(using_).md>) — Returns a new string made by replacing in the receiver all percent escapes with the matching characters as determined by a given encoding. _(deprecated)_
- [- stringByAddingPercentEscapesUsingEncoding:](<addingpercentescapes(using_).md>) — Returns a representation of the receiver using a given encoding to determine the percent escapes necessary to convert the receiver into a legal URL string. _(deprecated)_

### Working with URL Strings

- [stringByRemovingPercentEncoding](removingpercentencoding.md) — Returns a new string made from the receiver by replacing all percent encoded sequences with the matching UTF-8 characters.
