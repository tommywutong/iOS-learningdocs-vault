---
title: 'init(listenerEndpoint:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsxpcconnection/init(listenerendpoint:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection/init(listenerendpoint:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection/init%28listenerendpoint%3A%29.json'
content_hash: 'sha256:78056b4e2d1a0be7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCConnection](../nsxpcconnection.md)

# init(listenerEndpoint:)

<sub>Initializer</sub>

Initializes an [NSXPCConnection](../nsxpcconnection.md) object to connect to an [NSXPCListener](../nsxpclistener.md) object in another process, identified by an [NSXPCListenerEndpoint](../nsxpclistenerendpoint.md) object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(listenerEndpoint endpoint: NSXPCListenerEndpoint)
```

## Parameters

- `endpoint` — The desired listener endpoint for the service.

## See Also

### Related Documentation

- [Daemons and Services Programming Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html#//apple_ref/doc/uid/10000172i)

### Creating a connection

- [- initWithMachServiceName:options:](<init(machservicename_options_).md>) — Initializes an [NSXPCConnection](../nsxpcconnection.md) object to connect to a LaunchAgent or LaunchDaemon with a name advertised in a `launchd.plist`.
- [Options](options.md) — Options that you can pass to a connection.
- [- initWithServiceName:](<init(servicename_).md>) — Initializes an [NSXPCConnection](../nsxpcconnection.md) object to connect to an [NSXPCListener](../nsxpclistener.md) object in an XPC service, identified by a service name.
