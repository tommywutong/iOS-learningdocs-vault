---
title: endpoint
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpclistener/endpoint
source_url: 'https://developer.apple.com/documentation/foundation/nsxpclistener/endpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpclistener/endpoint.json'
content_hash: 'sha256:61c6b5ae234b0eee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCListener](../nsxpclistener.md)

# endpoint

<sub>Instance Property</sub>

Returns an endpoint object that may be sent over an existing connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var endpoint: NSXPCListenerEndpoint { get }
```

## Discussion

The receiver of the endpoint can use this object to create a new connection to this [NSXPCListener](../nsxpclistener.md) object. The resulting `NSXPCListenerEndpoint` object uniquely names this listener object across connections.

## See Also

### Related Documentation

- [Daemons and Services Programming Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html#//apple_ref/doc/uid/10000172i)
