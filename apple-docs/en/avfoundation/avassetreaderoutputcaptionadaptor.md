---
title: AVAssetReaderOutputCaptionAdaptor
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+（27.0 起废弃）, iPadOS 18.0+（27.0 起废弃）, Mac Catalyst 15.0+（27.0 起废弃）, macOS 12.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetreaderoutputcaptionadaptor
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutputcaptionadaptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutputcaptionadaptor.json'
content_hash: 'sha256:63372cd1f730f640'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetReaderOutputCaptionAdaptor

<sub>Class</sub>

An object that reads caption group objects from an asset track that contains timed text.

> [!warning] Deprecated
> Use AVAssetReader.outputCaptionProvider(for:validationDelegate:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class AVAssetReaderOutputCaptionAdaptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a caption adaptor

- [- initWithAssetReaderTrackOutput:](<avassetreaderoutputcaptionadaptor/init(assetreadertrackoutput_).md>) — Creates a caption adaptor that reads from a track output. _(deprecated)_

### Accessing the track output

- [assetReaderTrackOutput](avassetreaderoutputcaptionadaptor/assetreadertrackoutput.md) — The associated asset reader track output. _(deprecated)_

### Managing the validation delegate

- [validationDelegate](avassetreaderoutputcaptionadaptor/validationdelegate.md) — A delegate object that handles callbacks to the caption adaptor.
- [AVAssetReaderCaptionValidationHandling](avassetreadercaptionvalidationhandling.md) — A protocol that defines the methods for caption validation events.

### Reading caption groups

- [- nextCaptionGroup](<avassetreaderoutputcaptionadaptor/nextcaptiongroup().md>) — Returns the next caption group. _(deprecated)_
- [- captionsNotPresentInPreviousGroupsInCaptionGroup:](<avassetreaderoutputcaptionadaptor/captionsnotpresentinpreviousgroups(in_).md>) — Returns the set of captions in the caption group that weren’t vended by the adaptor. _(deprecated)_

## See Also

### Reading and writing

- [AVAssetWriterInputCaptionAdaptor](avassetwriterinputcaptionadaptor.md) — An object that appends captions to an asset writer input. _(deprecated)_
