---
title: allowsParallelizedExport
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 14.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsession/allowsparallelizedexport
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/allowsparallelizedexport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/allowsparallelizedexport.json'
content_hash: 'sha256:7b22151724898743'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# allowsParallelizedExport

<sub>Instance Property</sub>

A Boolean value that indicates whether the session can parallelize its export operation.

<sub>macOS</sub>

```swift
var allowsParallelizedExport: Bool { get set }
```

## Discussion

This value is [true](../../swift/true.md) by default, which indicates that the export session is allowed to expedite its processing by using additional resources in parallel on select Mac systems. If parallelization isn’t achievable, export proceeds as normal.

> [!note] Note
> Parallelized exports reduce the amount of time it takes to export media, but require additional power consumption. If your app requires opting out of the default behavior, set this value to [false](../../swift/false.md).

## See Also

### Configuring output

- [supportedFileTypes](supportedfiletypes.md) — An array containing the types of files the session can write.
- [shouldOptimizeForNetworkUse](shouldoptimizefornetworkuse.md) — A Boolean value that indicates whether to optimize the movie for network use.
- [canPerformMultiplePassesOverSourceMediaData](canperformmultiplepassesoversourcemediadata.md) — A Boolean value that indicates whether the export session can perform multiple passes over the source media to achieve better results.
- [timeRange](timerange.md) — The time range of the source asset to export.
- [fileLengthLimit](filelengthlimit.md) — The file length that the output of the session must not exceed.
- [directoryForTemporaryFiles](directoryfortemporaryfiles.md) — A directory suitable to store temporary files that the export process generates.
