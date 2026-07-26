---
title: NSMutableURLRequest
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutableurlrequest
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableurlrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableurlrequest.json'
content_hash: 'sha256:f7099c44c6736edb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMutableURLRequest

<sub>Class</sub>

A mutable URL load request that is independent of protocol or URL scheme.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSMutableURLRequest
```

## Overview

In Swift, this object bridges to [NSURLRequest](nsurlrequest.md) and you use when you need reference semantics or other Foundation-specific behavior.

[NSMutableURLRequest](nsmutableurlrequest.md) is a subclass of [NSURLRequest](nsurlrequest.md) that allows you to change the request’s properties.

[NSMutableURLRequest](nsmutableurlrequest.md) only represents information about the request. Use other classes, such as [URLSession](urlsession.md), to send the request to a server. See [Fetching website data into memory](fetching-website-data-into-memory.md) and [Uploading data to a website](uploading-data-to-a-website.md) for an introduction to these techniques.

Classes that create a network operation based on a request make a deep copy of that request. Thus, changing the request after creating a network operation has no effect on the ongoing operation. For example, if you use [- dataTaskWithRequest:completionHandler:](<urlsession/datatask(with_completionhandler_)-e6xv.md>) to create a data task from a request, and then later change the request, the data task continues using the original request.

> [!important] Important
> The Swift overlay to the Foundation framework provides the [URLRequest](urlrequest.md) structure, which bridges to the [NSMutableURLRequest](nsmutableurlrequest.md) class and its immutable superclass, [NSURLRequest](nsurlrequest.md). For more information about value types, see [Working with Foundation Types](../swift/working-with-foundation-types.md).

## Relationships

- **Inherits From**: [NSURLRequest](nsurlrequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSMutableCopying](nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Working with a cache policy

- [cachePolicy](nsmutableurlrequest/cachepolicy.md) — The request’s cache policy.
- [CachePolicy](nsurlrequest/cachepolicy-swift.enum.md) — The constants used to specify interaction with the cached responses.

### Accessing request components

- [HTTPMethod](nsmutableurlrequest/httpmethod.md) — The HTTP request method.
- [URL](nsmutableurlrequest/url.md) — The URL being requested.
- [HTTPBody](nsmutableurlrequest/httpbody.md) — The request body.
- [HTTPBodyStream](nsmutableurlrequest/httpbodystream.md) — The request body as an input stream.
- [mainDocumentURL](nsmutableurlrequest/maindocumenturl.md) — The main document URL.

### Accessing header fields

- [allHTTPHeaderFields](nsmutableurlrequest/allhttpheaderfields.md) — A dictionary containing all of the HTTP header fields for a request.
- [- addValue:forHTTPHeaderField:](<nsmutableurlrequest/addvalue(__forhttpheaderfield_).md>) — Adds a value to the header field.
- [- setValue:forHTTPHeaderField:](<nsmutableurlrequest/setvalue(__forhttpheaderfield_).md>) — Sets a value for the header field.

### Controlling request behavior

- [timeoutInterval](nsmutableurlrequest/timeoutinterval.md) — The request’s timeout interval, in seconds.
- [HTTPShouldHandleCookies](nsmutableurlrequest/httpshouldhandlecookies.md) — A Boolean value that indicates whether the request should use the default cookie handling for the request.
- [HTTPShouldUsePipelining](nsmutableurlrequest/httpshouldusepipelining.md) — A Boolean value that indicates whether the request can continue transmitting data before receiving a response from an earlier transmission. _(deprecated)_
- [allowsCellularAccess](nsmutableurlrequest/allowscellularaccess.md) — A Boolean value that indicates whether a connection can use the device’s cellular network (if present).

### Supporting limited modes

- [allowsConstrainedNetworkAccess](nsmutableurlrequest/allowsconstrainednetworkaccess.md) — A Boolean value that indicates whether connections may use the network when the user has specified Low Data Mode.
- [allowsExpensiveNetworkAccess](nsmutableurlrequest/allowsexpensivenetworkaccess.md) — A Boolean value that indicates whether connections may use a network interface that the system considers expensive.

### Accessing the service type

- [networkServiceType](nsmutableurlrequest/networkservicetype.md) — The network service type of the connection.
- [NetworkServiceType](nsurlrequest/networkservicetype-swift.enum.md) — Constants that specify how a request uses network resources.

### Working with hotspots

- [- bindToHotspotHelperCommand:](<nsmutableurlrequest/bind(to_).md>) — Binds a URL request to the network interface associated with the hotspot helper command instance.

### Indicating the source of the request

- [attribution](nsmutableurlrequest/attribution.md) — The entity that initiates the network request.
- [Attribution](nsurlrequest/attribution-swift.enum.md) — The entities that can make a network request.

### Instance Properties

- [allowsPersistentDNS](nsmutableurlrequest/allowspersistentdns.md) — A Boolean value that indicates whether storing and usage of DNS answers in a persistent per-process cache is allowed.
- [allowsUltraConstrainedNetworkAccess](nsmutableurlrequest/allowsultraconstrainednetworkaccess.md) — A Boolean value that indicates whether a connection created with this request is allowed to use network interfaces which have been marked as ultra constrained.
- [assumesHTTP3Capable](nsmutableurlrequest/assumeshttp3capable.md) — A Boolean value that indicates whether the server is assumed to support HTTP/3.
- [cookiePartitionIdentifier](nsmutableurlrequest/cookiepartitionidentifier.md)
- [requiresDNSSECValidation](nsmutableurlrequest/requiresdnssecvalidation.md) — A Boolean value that indicates whether a request requires DNSSEC validation during DNS lookup.

## See Also

### Requests and responses

- [URLRequest](urlrequest.md) — A URL load request that is independent of protocol or URL scheme.
- [NSURLRequest](nsurlrequest.md) — A URL load request that is independent of protocol or URL scheme.
- [URLResponse](urlresponse.md) — The metadata associated with the response to a URL load request, independent of protocol and URL scheme.
- [HTTPURLResponse](httpurlresponse.md) — The metadata associated with the response to an HTTP protocol URL load request.
