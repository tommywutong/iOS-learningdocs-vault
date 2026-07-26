---
title: 'setInterface(_:for:argumentIndex:ofReply:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsxpcinterface/setinterface(_:for:argumentindex:ofreply:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcinterface/setinterface(_:for:argumentindex:ofreply:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcinterface/setinterface%28_%3Afor%3Aargumentindex%3Aofreply%3A%29.json'
content_hash: 'sha256:4ff1304e6a39d014'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCInterface](../nsxpcinterface.md)

# setInterface(_:for:argumentIndex:ofReply:)

<sub>Instance Method</sub>

Configures a specific parameter of a method to be sent as a proxy object instead of copied.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setInterface(_ ifc: NSXPCInterface, for sel: Selector, argumentIndex arg: Int, ofReply: Bool)
```

## Parameters

- `ifc` — The [NSXPCInterface](../nsxpcinterface.md) object that describes the protocol for the proxy object. The interface is configured the same way as the interface for an exported object or remote object proxy.

- `sel` — Specifies which method in the protocol is being configured.

- `arg` — Specifies the position (starting at index 0) of the parameter for which you are configuring a proxy object. This may be either the position of a parameter in the method itself or the position in its reply block. This argument must be an object.

- `ofReply` — Pass [true](../../swift/true.md) if `arg` is an index into the parameters of the reply block, or [false](../../swift/false.md) if it is an index into the parameters of the method itself.

## Discussion

If an argument to a method in your protocol should be sent as a proxy object instead of by copy, then configure the interface for that protocol with a new interface for a specific argument. An example of an object that should be a proxy instead of being copied is a view object.
