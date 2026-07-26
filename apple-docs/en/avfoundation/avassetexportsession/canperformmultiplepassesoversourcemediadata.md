---
title: canPerformMultiplePassesOverSourceMediaData
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsession/canperformmultiplepassesoversourcemediadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/canperformmultiplepassesoversourcemediadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/canperformmultiplepassesoversourcemediadata.json'
content_hash: 'sha256:bc64bb8e6de40ef8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# canPerformMultiplePassesOverSourceMediaData

<sub>Instance Property</sub>

A Boolean value that indicates whether the export session can perform multiple passes over the source media to achieve better results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var canPerformMultiplePassesOverSourceMediaData: Bool { get set }
```

## Discussion

When the value for this property is [true](../../swift/true.md), the export session can produce higher quality results at the expense of longer export times. Setting this property to [true](../../swift/true.md) may also require the export session to write temporary data to disk during the export. To control the location of temporary data, use the property [directoryForTemporaryFiles](directoryfortemporaryfiles.md).

The default value is [false](../../swift/false.md). Not all export session configurations can benefit from performing multiple passes over the source media. In these cases, setting this property to [true](../../swift/true.md) has no effect.

You can’t set this property after the export starts.

## See Also

### Configuring output

- [supportedFileTypes](supportedfiletypes.md) — An array containing the types of files the session can write.
- [allowsParallelizedExport](allowsparallelizedexport.md) — A Boolean value that indicates whether the session can parallelize its export operation.
- [shouldOptimizeForNetworkUse](shouldoptimizefornetworkuse.md) — A Boolean value that indicates whether to optimize the movie for network use.
- [timeRange](timerange.md) — The time range of the source asset to export.
- [fileLengthLimit](filelengthlimit.md) — The file length that the output of the session must not exceed.
- [directoryForTemporaryFiles](directoryfortemporaryfiles.md) — A directory suitable to store temporary files that the export process generates.
