---
title: 'init(serviceName:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsxpcconnection/init(servicename:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection/init(servicename:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection/init%28servicename%3A%29.json'
content_hash: 'sha256:aa023bf53e1646eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCConnection](../nsxpcconnection.md)

# init(serviceName:)

<sub>Initializer</sub>

Initializes an [NSXPCConnection](../nsxpcconnection.md) object to connect to an [NSXPCListener](../nsxpclistener.md) object in an XPC service, identified by a service name.

<sub>macOS</sub>

```swift
init(serviceName: String)
```

## Discussion

XPC services are helper processes that are usually part of your application bundle. The service should use [NSXPCListener](../nsxpclistener.md) to wait for new connections.

## See Also

### Creating a connection

- [- initWithListenerEndpoint:](<init(listenerendpoint_).md>) — Initializes an [NSXPCConnection](../nsxpcconnection.md) object to connect to an [NSXPCListener](../nsxpclistener.md) object in another process, identified by an [NSXPCListenerEndpoint](../nsxpclistenerendpoint.md) object.
- [- initWithMachServiceName:options:](<init(machservicename_options_).md>) — Initializes an [NSXPCConnection](../nsxpcconnection.md) object to connect to a LaunchAgent or LaunchDaemon with a name advertised in a `launchd.plist`.
- [Options](options.md) — Options that you can pass to a connection.
