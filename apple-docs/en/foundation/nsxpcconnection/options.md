---
title: NSXPCConnection.Options
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcconnection/options
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection/options.json'
content_hash: 'sha256:45a1139320aab064'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCConnection](../nsxpcconnection.md)

# NSXPCConnection.Options

<sub>Structure</sub>

Options that you can pass to a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Options
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSXPCConnectionPrivileged](options/privileged.md)

### Initializers

- [init(rawValue:)](<options/init(rawvalue_).md>)

## See Also

### Creating a connection

- [- initWithListenerEndpoint:](<init(listenerendpoint_).md>) — Initializes an [NSXPCConnection](../nsxpcconnection.md) object to connect to an [NSXPCListener](../nsxpclistener.md) object in another process, identified by an [NSXPCListenerEndpoint](../nsxpclistenerendpoint.md) object.
- [- initWithMachServiceName:options:](<init(machservicename_options_).md>) — Initializes an [NSXPCConnection](../nsxpcconnection.md) object to connect to a LaunchAgent or LaunchDaemon with a name advertised in a `launchd.plist`.
- [- initWithServiceName:](<init(servicename_).md>) — Initializes an [NSXPCConnection](../nsxpcconnection.md) object to connect to an [NSXPCListener](../nsxpclistener.md) object in an XPC service, identified by a service name.
