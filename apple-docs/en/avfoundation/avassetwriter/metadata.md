---
title: metadata
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/metadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/metadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/metadata.json'
content_hash: 'sha256:0f931dba08c456dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# metadata

<sub>Instance Property</sub>

An array of metadata items to write to the output file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var metadata: [AVMetadataItem] { get set }
```

## Discussion

You can’t modify this property value after writing starts.

## See Also

### Configuring output

- [shouldOptimizeForNetworkUse](shouldoptimizefornetworkuse.md) — A Boolean value that indicates whether to write the output file to make it more suitable for playback over a network.
- [directoryForTemporaryFiles](directoryfortemporaryfiles.md) — A directory to contain temporary files that the export process generates.
