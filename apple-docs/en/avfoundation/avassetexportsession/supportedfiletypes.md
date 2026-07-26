---
title: supportedFileTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsession/supportedfiletypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/supportedfiletypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/supportedfiletypes.json'
content_hash: 'sha256:414007895f3ddf8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# supportedFileTypes

<sub>Instance Property</sub>

An array containing the types of files the session can write.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var supportedFileTypes: [AVFileType] { get }
```

## See Also

### Configuring output

- [allowsParallelizedExport](allowsparallelizedexport.md) — A Boolean value that indicates whether the session can parallelize its export operation.
- [shouldOptimizeForNetworkUse](shouldoptimizefornetworkuse.md) — A Boolean value that indicates whether to optimize the movie for network use.
- [canPerformMultiplePassesOverSourceMediaData](canperformmultiplepassesoversourcemediadata.md) — A Boolean value that indicates whether the export session can perform multiple passes over the source media to achieve better results.
- [timeRange](timerange.md) — The time range of the source asset to export.
- [fileLengthLimit](filelengthlimit.md) — The file length that the output of the session must not exceed.
- [directoryForTemporaryFiles](directoryfortemporaryfiles.md) — A directory suitable to store temporary files that the export process generates.
