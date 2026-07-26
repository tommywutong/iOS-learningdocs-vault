---
title: URLRequest
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlrequest
source_url: 'https://developer.apple.com/documentation/foundation/urlrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlrequest.json'
content_hash: 'sha256:426188bc6e2c70eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLRequest

<sub>Structure</sub>

A URL load request that is independent of protocol or URL scheme.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct URLRequest
```

## Overview

[URLRequest](urlrequest.md) encapsulates two essential properties of a load request: the URL to load and the policies used to load it. In addition, for HTTP and HTTPS requests, [URLRequest](urlrequest.md) includes the HTTP method (`GET`, `POST`, and so on) and the HTTP headers.

[URLRequest](urlrequest.md) only represents information about the request. Use other classes, such as [URLSession](urlsession.md), to send the request to a server. See [Fetching website data into memory](fetching-website-data-into-memory.md) and [Uploading data to a website](uploading-data-to-a-website.md) for an introduction to these techniques.

When writing Swift code, favor this structure over the [NSURLRequest](nsurlrequest.md) and [NSMutableURLRequest](nsmutableurlrequest.md) classes.

Certain header fields are reserved; see [Reserved HTTP headers](nsurlrequest.md#Reserved-HTTP-headers).

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [ReferenceConvertible](referenceconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a request

- [init(url:cachePolicy:timeoutInterval:)](<urlrequest/init(url_cachepolicy_timeoutinterval_).md>) — Creates and initializes a URL request with the given URL, cache policy, and timeout interval.

### Working with a cache policy

- [cachePolicy](urlrequest/cachepolicy-swift.property.md) — The request’s cache policy.
- [CachePolicy](urlrequest/cachepolicy-swift.typealias.md) — An alias for the cache policy.
- [CachePolicy](nsurlrequest/cachepolicy-swift.enum.md) — The constants used to specify interaction with the cached responses.

### Accessing request components

- [httpMethod](urlrequest/httpmethod.md) — The HTTP request method.
- [url](urlrequest/url.md) — The URL of the request.
- [httpBody](urlrequest/httpbody.md) — The data sent as the message body of a request, such as for an HTTP POST request.
- [httpBodyStream](urlrequest/httpbodystream.md) — The stream used to deliver the HTTP body.
- [mainDocumentURL](urlrequest/maindocumenturl.md) — The main document URL associated with this request.

### Accessing header fields

- [allHTTPHeaderFields](urlrequest/allhttpheaderfields.md) — A dictionary containing all of the HTTP header fields for a request.
- [addValue(_:forHTTPHeaderField:)](<urlrequest/addvalue(__forhttpheaderfield_).md>) — Adds a value to the header field.
- [setValue(_:forHTTPHeaderField:)](<urlrequest/setvalue(__forhttpheaderfield_).md>) — Sets a value for the header field.
- [value(forHTTPHeaderField:)](<urlrequest/value(forhttpheaderfield_).md>) — Retrieves a header value.

### Controlling request behavior

- [timeoutInterval](urlrequest/timeoutinterval.md) — The timeout interval of the request.
- [httpShouldHandleCookies](urlrequest/httpshouldhandlecookies.md) — A Boolean value indicating whether cookies will be sent with and set for this request.
- [httpShouldUsePipelining](urlrequest/httpshouldusepipelining.md) — A Boolean value indicating whether the request should transmit before the previous response is received. _(deprecated)_
- [allowsCellularAccess](urlrequest/allowscellularaccess.md) — A Boolean value indicating whether the request is allowed to use the built-in cellular radios to satisfy the request.
- [allowsPersistentDNS](urlrequest/allowspersistentdns.md) — `true` if the request is allowed to store and use DNS answers, potentially beyond TTL expiry, in a persistent per-process cache, `false` otherwise. Defaults to `false`. This should only be set to `true` for hostnames whose resolutions are not expected to change across networks.
- [assumesHTTP3Capable](urlrequest/assumeshttp3capable.md) — `true` if server endpoint is known to support HTTP/3. Enables QUIC racing without HTTP/3 service discovery. Defaults to `false`. The default may be `true` in a future OS update.
- [cookiePartitionIdentifier](urlrequest/cookiepartitionidentifier.md)
- [requiresDNSSECValidation](urlrequest/requiresdnssecvalidation.md) — `true` if the request is required to do DNSSEC validation during DNS lookup. `false` otherwise. Defaults to `false`.

### Supporting limited modes

- [allowsConstrainedNetworkAccess](urlrequest/allowsconstrainednetworkaccess.md) — A Boolean value that indicates whether the request may use the network when the user has specified Low Data Mode.
- [allowsExpensiveNetworkAccess](urlrequest/allowsexpensivenetworkaccess.md) — A Boolean value that indicates whether connections may use a network interface that the system considers expensive.

### Accessing the service type

- [networkServiceType](urlrequest/networkservicetype-swift.property.md) — The type of network service for all tasks within network sessions to enable Cellular Network Slicing.
- [NetworkServiceType](urlrequest/networkservicetype-swift.typealias.md) — An alias for the network service type.
- [NetworkServiceType](nsurlrequest/networkservicetype-swift.enum.md) — Constants that specify how a request uses network resources.

### Indicating the source of the request

- [attribution](urlrequest/attribution-swift.property.md) — The entity that initiates the network request.
- [Attribution](urlrequest/attribution-swift.typealias.md) — A type that indicates the entities that can make a network request.

### Using reference types

- [NSURLRequest](nsurlrequest.md) — A URL load request that is independent of protocol or URL scheme.
- [NSMutableURLRequest](nsmutableurlrequest.md) — A mutable URL load request that is independent of protocol or URL scheme.
- [MutableURLRequest](mutableurlrequest.md) _(deprecated)_

### Instance Properties

- [allowsUltraConstrainedNetworkAccess](urlrequest/allowsultraconstrainednetworkaccess.md) — `true` if the receiver is allowed to use an interface marked as ultra-constrained to satify the request, `false` otherwise.

## See Also

### Requests and responses

- [NSURLRequest](nsurlrequest.md) — A URL load request that is independent of protocol or URL scheme.
- [NSMutableURLRequest](nsmutableurlrequest.md) — A mutable URL load request that is independent of protocol or URL scheme.
- [URLResponse](urlresponse.md) — The metadata associated with the response to a URL load request, independent of protocol and URL scheme.
- [HTTPURLResponse](httpurlresponse.md) — The metadata associated with the response to an HTTP protocol URL load request.
