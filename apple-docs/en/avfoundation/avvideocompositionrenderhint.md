---
title: AVVideoCompositionRenderHint
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositionrenderhint
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionrenderhint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionrenderhint.json'
content_hash: 'sha256:7aa7b9d907b38598'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoCompositionRenderHint

<sub>Class</sub>

Information about upcoming composition requests, such as composition start time and end time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVVideoCompositionRenderHint
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Managing composition timing

- [startCompositionTime](avvideocompositionrenderhint/startcompositiontime.md) — The start time of the upcoming composition requests.
- [endCompositionTime](avvideocompositionrenderhint/endcompositiontime.md) — The end time of the upcoming composition requests.

## See Also

### Preparing to render frames

- [- anticipateRenderingUsingHint:](<avvideocompositing/anticipaterendering(using_).md>) — Informs a custom video compositor about upcoming rendering requests.
- [- prerollForRenderingUsingHint:](<avvideocompositing/prerollforrendering(using_).md>) — Tells a custom video compositor to perform any work in the prerolling phase.
