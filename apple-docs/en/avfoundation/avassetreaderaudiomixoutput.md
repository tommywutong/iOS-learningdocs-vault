---
title: AVAssetReaderAudioMixOutput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreaderaudiomixoutput
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderaudiomixoutput.json'
content_hash: 'sha256:a1b27f908519e92d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetReaderAudioMixOutput

<sub>Class</sub>

An object that reads audio samples that result from mixing audio from one or more tracks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetReaderAudioMixOutput
```

## Overview

Read audio data that you mix from one or more asset tracks by adding an audio mix output to an asset reader. You can read the samples in their stored format or you can convert them to an alternative format.

## Relationships

- **Inherits From**: [AVAssetReaderOutput](avassetreaderoutput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an audio mix output

- [- initWithAudioTracks:audioSettings:](<avassetreaderaudiomixoutput/init(audiotracks_audiosettings_).md>) — Creates an object that reads mixed audio from the specified audio tracks.

### Configuring audio settings

- [audioMix](avassetreaderaudiomixoutput/audiomix.md) — The audio mix to use with this output.
- [audioTimePitchAlgorithm](avassetreaderaudiomixoutput/audiotimepitchalgorithm.md) — The processing algorithm to use for scaled audio edits.

### Inspecting an output

- [audioTracks](avassetreaderaudiomixoutput/audiotracks.md) — The tracks from which the output reads audio.
- [audioSettings](avassetreaderaudiomixoutput/audiosettings.md) — The audio settings that the output uses.

## See Also

### Media reading

- [Reading multiview 3D video files](reading-multiview-3d-video-files.md) — Render single images for the left eye and right eye from a multiview High Efficiency Video Coding format file by reading individual video frames.
- [AVAssetReader](avassetreader.md) — An object that reads media data from an asset.
- [AVAssetReaderOutput](avassetreaderoutput.md) — An abstract class that defines the interface to read media samples from an asset reader.
- [AVAssetReaderTrackOutput](avassetreadertrackoutput.md) — An object that reads media data from a single track of an asset.
- [AVAssetReaderVideoCompositionOutput](avassetreadervideocompositionoutput.md) — An object that reads composited video frames from one or more tracks of an asset.
- [AVAssetReaderSampleReferenceOutput](avassetreadersamplereferenceoutput.md) — An object that reads sample references from an asset track.
- [AVAssetReaderOutputMetadataAdaptor](avassetreaderoutputmetadataadaptor.md) — An object that creates timed metadata group objects for an asset track. _(deprecated)_
