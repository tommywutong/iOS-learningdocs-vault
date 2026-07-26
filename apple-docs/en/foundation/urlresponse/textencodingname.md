---
title: textEncodingName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresponse/textencodingname
source_url: 'https://developer.apple.com/documentation/foundation/urlresponse/textencodingname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresponse/textencodingname.json'
content_hash: 'sha256:13e6d04735150a3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResponse](../urlresponse.md)

# textEncodingName

<sub>Instance Property</sub>

The name of the text encoding provided by the response’s originating source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var textEncodingName: String? { get }
```

## Discussion

If no text encoding was provided by the protocol, this property’s value is `nil`.

You can convert this string to a `CFStringEncoding` value by calling [CFStringConvertIANACharSetNameToEncoding(_:)](<../../corefoundation/cfstringconvertianacharsetnametoencoding(__).md>). You can subsequently convert that value to an `NSStringEncoding` value by calling [CFStringConvertEncodingToNSStringEncoding(_:)](<../../corefoundation/cfstringconvertencodingtonsstringencoding(__).md>).

## See Also

### Getting the response properties

- [expectedContentLength](expectedcontentlength.md) — The expected length of the response’s content.
- [suggestedFilename](suggestedfilename.md) — A suggested filename for the response data.
- [MIMEType](mimetype.md) — The MIME type of the response.
- [URL](url.md) — The URL for the response.
