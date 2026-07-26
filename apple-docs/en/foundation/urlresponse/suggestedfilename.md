---
title: suggestedFilename
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresponse/suggestedfilename
source_url: 'https://developer.apple.com/documentation/foundation/urlresponse/suggestedfilename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresponse/suggestedfilename.json'
content_hash: 'sha256:721b69913b0b4b9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResponse](../urlresponse.md)

# suggestedFilename

<sub>Instance Property</sub>

A suggested filename for the response data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var suggestedFilename: String? { get }
```

## Discussion

Accessing this property attempts to generate a filename using the following information, in order:

1. A filename specified using the content disposition header.
2. The last path component of the URL.
3. The host of the URL.

If the host of URL can’t be converted to a valid filename, the filename “unknown” is used.

In most cases, this property appends the proper file extension based on the MIME type. Accessing this property always returns a valid filename regardless of whether the resource is saved to disk.

## See Also

### Getting the response properties

- [expectedContentLength](expectedcontentlength.md) — The expected length of the response’s content.
- [MIMEType](mimetype.md) — The MIME type of the response.
- [textEncodingName](textencodingname.md) — The name of the text encoding provided by the response’s originating source.
- [URL](url.md) — The URL for the response.
