---
title: directoryForTemporaryFiles
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/directoryfortemporaryfiles
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/directoryfortemporaryfiles'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/directoryfortemporaryfiles.json'
content_hash: 'sha256:f1fe9f89de7efa34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# directoryForTemporaryFiles

<sub>Instance Property</sub>

A directory to contain temporary files that the export process generates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var directoryForTemporaryFiles: URL? { get set }
```

## Discussion

In some configurations, such as performing multipass encoding, an asset writer may need to write temporary files. Use this property value to set the file-system location where it writes temporary files. The system deletes all temporary files after it finishes writing successfully, fails, or you cancel the writing session.

You can set this value after writing starts.

## See Also

### Configuring output

- [metadata](metadata.md) — An array of metadata items to write to the output file.
- [shouldOptimizeForNetworkUse](shouldoptimizefornetworkuse.md) — A Boolean value that indicates whether to write the output file to make it more suitable for playback over a network.
