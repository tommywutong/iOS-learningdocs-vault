---
title: anonymous()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpclistener/anonymous()
source_url: 'https://developer.apple.com/documentation/foundation/nsxpclistener/anonymous()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpclistener/anonymous%28%29.json'
content_hash: 'sha256:f68773c9f07e8691'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCListener](../nsxpclistener.md)

# anonymous()

<sub>Type Method</sub>

Returns a new anonymous listener connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func anonymous() -> NSXPCListener
```

## Discussion

Other processes can connect to this listener by passing this listener object’s `NSXPCListenerEndpoint` to the [- initWithListenerEndpoint:](<../nsxpcconnection/init(listenerendpoint_).md>) method of an [NSXPCConnection](../nsxpcconnection.md) object.

## See Also

### Using standard listeners

- [+ serviceListener](<service().md>) — Returns the singleton listener used to listen for incoming connections in an XPC service.
