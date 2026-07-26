---
title: 'classes(for:argumentIndex:ofReply:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsxpcinterface/classes(for:argumentindex:ofreply:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcinterface/classes(for:argumentindex:ofreply:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcinterface/classes%28for%3Aargumentindex%3Aofreply%3A%29.json'
content_hash: 'sha256:9308aabbad548ae7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCInterface](../nsxpcinterface.md)

# classes(for:argumentIndex:ofReply:)

<sub>Instance Method</sub>

Returns the current list of allowed classes that can appear within the specified collection object argument to the specified method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func classes(for sel: Selector, argumentIndex arg: Int, ofReply: Bool) -> Set<AnyHashable>
```

## Parameters

- `sel` — Specifies which method in the protocol you want information about.

- `arg` — Specifies the position (starting at index 0) of the parameter for which you want to obtain the current set of allowed classes. This may be either the position of a parameter in the method itself or the position in its reply block.

- `ofReply` — Pass [true](../../swift/true.md) if `arg` is an index into the parameters of the reply block, or [false](../../swift/false.md) if it is an index into the parameters of the method itself.

## Discussion

See [- setClasses:forSelector:argumentIndex:ofReply:](<setclasses(__for_argumentindex_ofreply_).md>) for more explanation.

## See Also

### Related Documentation

- [Daemons and Services Programming Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html#//apple_ref/doc/uid/10000172i)
