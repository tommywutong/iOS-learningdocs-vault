---
title: outputs
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreader/outputs
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreader/outputs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreader/outputs.json'
content_hash: 'sha256:879afd82ccd8e672'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReader](../avassetreader.md)

# outputs

<sub>Instance Property</sub>

The outputs from which you read media data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var outputs: [AVAssetReaderOutput] { get }
```

## Discussion

The array contains the concrete instances of [AVAssetReaderOutput](../avassetreaderoutput.md) that you associate with the reader.

## See Also

### Managing outputs

- [- canAddOutput:](<canadd(__).md>) — Determines whether you can add the output to the asset reader.
- [- addOutput:](<add(__).md>) — Adds an output to the reader. _(deprecated)_
