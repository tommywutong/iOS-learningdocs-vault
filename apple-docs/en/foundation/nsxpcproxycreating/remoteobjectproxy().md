---
title: remoteObjectProxy()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcproxycreating/remoteobjectproxy()
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcproxycreating/remoteobjectproxy()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcproxycreating/remoteobjectproxy%28%29.json'
content_hash: 'sha256:bcfb03f912b8f08d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCProxyCreating](../nsxpcproxycreating.md)

# remoteObjectProxy()

<sub>Instance Method</sub>

Returns a proxy object with no error handling block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func remoteObjectProxy() -> Any
```

## Discussion

Messages sent to the proxy object are sent over the wire to the other side of the connection. All messages must be ‘void’ return type. Control may be returned to the caller before the message is sent. The resulting proxy object conforms to the `NSXPCProxyCreating` protocol.

## See Also

### Related Documentation

- [Daemons and Services Programming Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html#//apple_ref/doc/uid/10000172i)
