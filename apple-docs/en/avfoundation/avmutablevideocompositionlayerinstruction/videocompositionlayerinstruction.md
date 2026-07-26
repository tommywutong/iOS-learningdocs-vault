---
title: videoCompositionLayerInstruction
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablevideocompositionlayerinstruction/videocompositionlayerinstruction
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/videocompositionlayerinstruction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocompositionlayerinstruction/videocompositionlayerinstruction.json'
content_hash: 'sha256:c841ba18cc5c3b8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoCompositionLayerInstruction](../avmutablevideocompositionlayerinstruction.md)

# videoCompositionLayerInstruction

<sub>Type Method</sub>

Returns a new mutable video composition layer instruction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) videoCompositionLayerInstruction;
```

## Return Value

A new mutable video composition layer instruction with no transform or opacity ramps and [trackID](trackid.md) initialized to [kCMPersistentTrackID_Invalid](../../coremedia/kcmpersistenttrackid_invalid.md).

## See Also

### Creating an instruction

- [+ videoCompositionLayerInstructionWithAssetTrack:](<init(assettrack_).md>) — Creates a new mutable video composition layer instruction for the given track. _(deprecated)_
