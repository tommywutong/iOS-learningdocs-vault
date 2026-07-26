---
title: shouldOptimizeForNetworkUse
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/shouldoptimizefornetworkuse
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/shouldoptimizefornetworkuse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/shouldoptimizefornetworkuse.json'
content_hash: 'sha256:2073fe459a1fc9b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# shouldOptimizeForNetworkUse

<sub>Instance Property</sub>

A Boolean value that indicates whether to write the output file to make it more suitable for playback over a network.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var shouldOptimizeForNetworkUse: Bool { get set }
```

## Discussion

Setting this value to [true](../../swift/true.md) writes the output file in a form that enables a player to begin playing the media after downloading only a small portion of it.

## See Also

### Configuring output

- [metadata](metadata.md) — An array of metadata items to write to the output file.
- [directoryForTemporaryFiles](directoryfortemporaryfiles.md) — A directory to contain temporary files that the export process generates.
