---
title: protocolClasses
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/protocolclasses
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/protocolclasses'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/protocolclasses.json'
content_hash: 'sha256:ff850679bb18001d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# protocolClasses

<sub>Instance Property</sub>

An array of extra protocol subclasses that handle requests in a session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var protocolClasses: [AnyClass]? { get set }
```

## Discussion

The objects in this array are `Class` objects corresponding to custom [URLProtocol](../urlprotocol.md) subclasses that you define. URL session objects support a number of common networking protocols by default. Use this array to extend the default set of common networking protocols available for use by a session with one or more custom protocols that you define.

Prior to handling a request, the [URLSession](../urlsession.md) object searches the default protocols first and then checks your custom protocols until it finds one capable of handling the specified request. It uses the protocol whose [+ canInitWithRequest:](<../urlprotocol/caninit(with_)-76brg.md>) class method returns [true](../../swift/true.md), indicating that the class is capable of handling the specified request.

> [!note] Note
> You cannot use custom [URLProtocol](../urlprotocol.md) subclasses in conjunction with background sessions.

The default value is an empty array.

## See Also

### Supporting custom protocols

- [URLProtocol](../urlprotocol.md) — An abstract class that handles the loading of protocol-specific URL data.
