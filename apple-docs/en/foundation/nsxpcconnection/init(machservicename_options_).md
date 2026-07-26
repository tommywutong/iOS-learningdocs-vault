---
title: 'init(machServiceName:options:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsxpcconnection/init(machservicename:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection/init(machservicename:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection/init%28machservicename%3Aoptions%3A%29.json'
content_hash: 'sha256:d5a46ff3b852f0de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCConnection](../nsxpcconnection.md)

# init(machServiceName:options:)

<sub>Initializer</sub>

Initializes an [NSXPCConnection](../nsxpcconnection.md) object to connect to a LaunchAgent or LaunchDaemon with a name advertised in a `launchd.plist`.

<sub>macOS</sub>

```swift
init(machServiceName name: String, options: NSXPCConnection.Options = [])
```

## Discussion

For example, if an agent is managed with `launchd` and has a `launchd.plist` in `~/Library/LaunchAgents`, this method would create a connection to that agent. The agent should use [NSXPCListener](../nsxpclistener.md) to wait for new connections.

If the connection is being made to a process that is running in a privileged Mach bootstrap context (for example, a daemon started by a `launchd` property list in `/Library/LaunchDaemons`), then pass the [NSXPCConnection](../nsxpcconnection.md) option.

## See Also

### Creating a connection

- [- initWithListenerEndpoint:](<init(listenerendpoint_).md>) — Initializes an [NSXPCConnection](../nsxpcconnection.md) object to connect to an [NSXPCListener](../nsxpclistener.md) object in another process, identified by an [NSXPCListenerEndpoint](../nsxpclistenerendpoint.md) object.
- [Options](options.md) — Options that you can pass to a connection.
- [- initWithServiceName:](<init(servicename_).md>) — Initializes an [NSXPCConnection](../nsxpcconnection.md) object to connect to an [NSXPCListener](../nsxpclistener.md) object in an XPC service, identified by a service name.
