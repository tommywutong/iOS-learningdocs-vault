---
title: AVAssetWriterInputCaptionAdaptor
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+（27.0 起废弃）, iPadOS 18.0+（27.0 起废弃）, Mac Catalyst 15.0+（27.0 起废弃）, macOS 12.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetwriterinputcaptionadaptor
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputcaptionadaptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputcaptionadaptor.json'
content_hash: 'sha256:2faadf41ad924daf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetWriterInputCaptionAdaptor

<sub>Class</sub>

An object that appends captions to an asset writer input.

> [!warning] Deprecated
> Use AVAssetWriter.inputCaptionReceiver(for:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class AVAssetWriterInputCaptionAdaptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a caption adaptor

- [- initWithAssetWriterInput:](<avassetwriterinputcaptionadaptor/init(assetwriterinput_).md>) — Creates a new caption adaptor that writes to the specified asset writer input. _(deprecated)_

### Accessing the writer input

- [assetWriterInput](avassetwriterinputcaptionadaptor/assetwriterinput.md) — The associated asset writer input. _(deprecated)_

### Appending captions

- [- appendCaption:](<avassetwriterinputcaptionadaptor/append(__)-910lp.md>) — Appends a caption to the writer input. _(deprecated)_
- [- appendCaptionGroup:](<avassetwriterinputcaptionadaptor/append(__)-4ils8.md>) — Appends a caption group that the system writes to the output. _(deprecated)_

## See Also

### Reading and writing

- [AVAssetReaderOutputCaptionAdaptor](avassetreaderoutputcaptionadaptor.md) — An object that reads caption group objects from an asset track that contains timed text. _(deprecated)_
