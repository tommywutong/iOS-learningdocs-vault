---
title: 'listener(_:shouldAcceptNewConnection:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsxpclistenerdelegate/listener(_:shouldacceptnewconnection:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsxpclistenerdelegate/listener(_:shouldacceptnewconnection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpclistenerdelegate/listener%28_%3Ashouldacceptnewconnection%3A%29.json'
content_hash: 'sha256:5d570e3efe07b30e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCListenerDelegate](../nsxpclistenerdelegate.md)

# listener(_:shouldAcceptNewConnection:)

<sub>Instance Method</sub>

Accepts or rejects a new connection to the listener.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func listener(_ listener: NSXPCListener, shouldAcceptNewConnection newConnection: NSXPCConnection) -> Bool
```

## Discussion

To accept the connection, first configure the connection if desired, then call [- resume](<../nsxpcconnection/resume().md>) on the new connection, then return [true](../../swift/true.md).

To reject the connect, return a value of [false](../../swift/false.md). This causes the connection object to be invalidated.

In this method, you can also set up properties on the connection object, such as its exported object and interfaces. Be sure to call [- resume](<../nsxpcconnection/resume().md>) when you are finished configuring the connection object and are ready for it to receive messages.

## See Also

### Related Documentation

- [Daemons and Services Programming Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html#//apple_ref/doc/uid/10000172i)
