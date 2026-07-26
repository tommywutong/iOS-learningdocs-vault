---
title: timeRange
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsession/timerange
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/timerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/timerange.json'
content_hash: 'sha256:dae187aaffba3c1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# timeRange

<sub>Instance Property</sub>

The time range of the source asset to export.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var timeRange: CMTimeRange { get set }
```

## See Also

### Configuring output

- [supportedFileTypes](supportedfiletypes.md) — An array containing the types of files the session can write.
- [allowsParallelizedExport](allowsparallelizedexport.md) — A Boolean value that indicates whether the session can parallelize its export operation.
- [shouldOptimizeForNetworkUse](shouldoptimizefornetworkuse.md) — A Boolean value that indicates whether to optimize the movie for network use.
- [canPerformMultiplePassesOverSourceMediaData](canperformmultiplepassesoversourcemediadata.md) — A Boolean value that indicates whether the export session can perform multiple passes over the source media to achieve better results.
- [fileLengthLimit](filelengthlimit.md) — The file length that the output of the session must not exceed.
- [directoryForTemporaryFiles](directoryfortemporaryfiles.md) — A directory suitable to store temporary files that the export process generates.
