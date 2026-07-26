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
doc_path: /documentation/avfoundation/avassetexportsession/directoryfortemporaryfiles
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/directoryfortemporaryfiles'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/directoryfortemporaryfiles.json'
content_hash: 'sha256:5acf0d0e788d26be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# directoryForTemporaryFiles

<sub>Instance Property</sub>

A directory suitable to store temporary files that the export process generates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var directoryForTemporaryFiles: URL? { get set }
```

## See Also

### Configuring output

- [supportedFileTypes](supportedfiletypes.md) — An array containing the types of files the session can write.
- [allowsParallelizedExport](allowsparallelizedexport.md) — A Boolean value that indicates whether the session can parallelize its export operation.
- [shouldOptimizeForNetworkUse](shouldoptimizefornetworkuse.md) — A Boolean value that indicates whether to optimize the movie for network use.
- [canPerformMultiplePassesOverSourceMediaData](canperformmultiplepassesoversourcemediadata.md) — A Boolean value that indicates whether the export session can perform multiple passes over the source media to achieve better results.
- [timeRange](timerange.md) — The time range of the source asset to export.
- [fileLengthLimit](filelengthlimit.md) — The file length that the output of the session must not exceed.
