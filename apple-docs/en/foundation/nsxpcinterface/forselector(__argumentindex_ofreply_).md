---
title: 'forSelector(_:argumentIndex:ofReply:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsxpcinterface/forselector(_:argumentindex:ofreply:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcinterface/forselector(_:argumentindex:ofreply:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcinterface/forselector%28_%3Aargumentindex%3Aofreply%3A%29.json'
content_hash: 'sha256:54c64d3a94e636b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCInterface](../nsxpcinterface.md)

# forSelector(_:argumentIndex:ofReply:)

<sub>Instance Method</sub>

Returns the interface previously set for the specified selector and parameter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func forSelector(_ sel: Selector, argumentIndex arg: Int, ofReply: Bool) -> NSXPCInterface?
```

## Parameters

- `sel` — Specifies which method in the protocol you want information about.

- `arg` — Specifies the position (starting at index 0) of the parameter for which you want to obtain the current interface. This may be either the position of a parameter in the method itself or the position in its reply block.

- `ofReply` — Pass [true](../../swift/true.md) if `arg` is an index into the parameters of the reply block, or [false](../../swift/false.md) if it is an index into the parameters of the method itself.

## Discussion

See [- setInterface:forSelector:argumentIndex:ofReply:](<setinterface(__for_argumentindex_ofreply_).md>) for more explanation.
