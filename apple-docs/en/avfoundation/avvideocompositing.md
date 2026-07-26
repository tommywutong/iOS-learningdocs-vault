---
title: AVVideoCompositing
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositing
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositing.json'
content_hash: 'sha256:69201e4a772fe144'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoCompositing

<sub>Protocol</sub>

A protocol that defines the methods custom video compositors must implement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol AVVideoCompositing : NSObjectProtocol, Sendable
```

## Overview

For each AVFoundation object of class [AVPlayerItem](avplayeritem.md), [AVAssetExportSession](avassetexportsession.md), [AVAssetImageGenerator](avassetimagegenerator.md), or [AVAssetReaderVideoCompositionOutput](avassetreadervideocompositionoutput.md) that has a non-`nil` value for its `videoComposition` property, and the value of the [customVideoCompositorClass](avvideocomposition/customvideocompositorclass.md) property of the `AVVideoComposition` isn’t `nil`, AVFoundation creates and uses an instance of that custom video compositor class to process the instructions contained in the [AVVideoComposition](avvideocomposition.md).

The system creates a custom video compositor instance when you assign `videoComposition` an instance of [AVVideoComposition](avvideocomposition.md) that’s associated with a different custom video compositor class than the object was previously using.

When creating instances of custom video compositors, AVFoundation initializes them by calling `init` and then makes them available as the value of the `customVideoCompositor` property of the object. You then can do any additional setup or configuration to the custom compositor.

The AVFoundation object retains the custom video compositor instances for as long as the value of the `videoComposition` property indicates that there’s an instance of the same custom video compositor class. This is true even when the value changes from one instance of AVVideoComposition to another associated instance with the same custom video compositor class.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting processing requirements

- [sourcePixelBufferAttributes](avvideocompositing/sourcepixelbufferattributes.md) — The pixel buffer attributes that the compositor accepts for source frames.
- [requiredPixelBufferAttributesForRenderContext](avvideocompositing/requiredpixelbufferattributesforrendercontext.md) — The pixel buffer attributes that the compositor requires for pixel buffers that it creates.
- [supportsHDRSourceFrames](avvideocompositing/supportshdrsourceframes.md) — A Boolean value that indicates whether the compositor handles source frames that contain high dynamic range (HDR) properties.
- [supportsWideColorSourceFrames](avvideocompositing/supportswidecolorsourceframes.md) — A Boolean value that indicates whether the compositor handles source frames that contains wide color properties.
- [canConformColorOfSourceFrames](avvideocompositing/canconformcolorofsourceframes.md) — A Boolean value that indicates whether the compositor conforms the color space of source frames to the composition color space.
- [supportsSourceTaggedBuffers](avvideocompositing/supportssourcetaggedbuffers.md)

### Observing render context changes

- [- renderContextChanged:](<avvideocompositing/rendercontextchanged(__).md>) — Tells the compositor that the composition changed render contexts.
- [AVVideoCompositionRenderContext](avvideocompositionrendercontext.md) — An object that defines the context in which custom compositors render pixel buffers.

### Preparing to render frames

- [- anticipateRenderingUsingHint:](<avvideocompositing/anticipaterendering(using_).md>) — Informs a custom video compositor about upcoming rendering requests.
- [- prerollForRenderingUsingHint:](<avvideocompositing/prerollforrendering(using_).md>) — Tells a custom video compositor to perform any work in the prerolling phase.
- [AVVideoCompositionRenderHint](avvideocompositionrenderhint.md) — Information about upcoming composition requests, such as composition start time and end time.

### Rendering the composition

- [- startVideoCompositionRequest:](<avvideocompositing/startrequest(__).md>) — Directs a custom video compositor object to create a new pixel buffer composed asynchronously from a collection of sources.
- [AVAsynchronousVideoCompositionRequest](avasynchronousvideocompositionrequest.md) — An object that contains information a video compositor needs to render an output pixel buffer.
- [- cancelAllPendingVideoCompositionRequests](<avvideocompositing/cancelallpendingvideocompositionrequests().md>) — Directs a custom video compositor object to cancel or finish all pending video composition requests.

## See Also

### Custom video compositing

- [Processing spatial video with a custom video compositor](processing-spatial-video-with-a-custom-video-compositor.md) — Create a custom video compositor to edit spatial video for playback and export.
