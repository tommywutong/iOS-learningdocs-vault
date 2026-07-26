---
title: URLResponse
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresponse
source_url: 'https://developer.apple.com/documentation/foundation/urlresponse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresponse.json'
content_hash: 'sha256:eeec8ae31a31c23f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLResponse

<sub>Class</sub>

The metadata associated with the response to a URL load request, independent of protocol and URL scheme.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class URLResponse
```

## Overview

The related [HTTPURLResponse](httpurlresponse.md) class is a commonly used subclass of [URLResponse](urlresponse.md) whose objects represent a response to an HTTP URL load request and store additional protocol-specific information such as the response headers. Whenever you make an HTTP request, the [URLResponse](urlresponse.md) object you get back is actually an instance of the [HTTPURLResponse](httpurlresponse.md) class.

> [!note] Note
> [URLResponse](urlresponse.md) objects don’t contain the actual bytes representing the content of a URL. Instead, the data is returned either a piece at a time through delegate calls or in its entirety when the request completes, depending on the method and class used to initiate the request.
>
> Read [Fetching website data into memory](fetching-website-data-into-memory.md) to learn various ways to receive the content data from a URL load.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [HTTPURLResponse](httpurlresponse.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a response

- [- initWithURL:MIMEType:expectedContentLength:textEncodingName:](<urlresponse/init(url_mimetype_expectedcontentlength_textencodingname_)-4s2s1.md>) — Creates an initialized [URLResponse](urlresponse.md) object with the URL, MIME type, length, and text encoding set to given values.

### Getting the response properties

- [expectedContentLength](urlresponse/expectedcontentlength.md) — The expected length of the response’s content.
- [suggestedFilename](urlresponse/suggestedfilename.md) — A suggested filename for the response data.
- [MIMEType](urlresponse/mimetype.md) — The MIME type of the response.
- [textEncodingName](urlresponse/textencodingname.md) — The name of the text encoding provided by the response’s originating source.
- [URL](urlresponse/url.md) — The URL for the response.

### Initializers

- [init(URL:MIMEType:expectedContentLength:textEncodingName:)](<urlresponse/init(url_mimetype_expectedcontentlength_textencodingname_)-3n1n4.md>)
- [init(coder:)](<urlresponse/init(coder_).md>)

## See Also

### Requests and responses

- [URLRequest](urlrequest.md) — A URL load request that is independent of protocol or URL scheme.
- [NSURLRequest](nsurlrequest.md) — A URL load request that is independent of protocol or URL scheme.
- [NSMutableURLRequest](nsmutableurlrequest.md) — A mutable URL load request that is independent of protocol or URL scheme.
- [HTTPURLResponse](httpurlresponse.md) — The metadata associated with the response to an HTTP protocol URL load request.
