---
title: Deprecated symbols
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsession-deprecated-symbols
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession-deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession-deprecated-symbols.json'
content_hash: 'sha256:c7da3e492f320290'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media reading and writing](media-reading-and-writing.md) · [AVAssetExportSession](avassetexportsession.md)

# Deprecated symbols

<sub>API Collection</sub>

Review unsupported symbols and their replacements.

## Topics

### Accessing export presets

- [+ exportPresetsCompatibleWithAsset:](<avassetexportsession/exportpresets(compatiblewith_).md>) — Returns compatible export presets for the asset. _(deprecated)_

### Configuring output

- [outputURL](avassetexportsession/outputurl.md) — A URL where an asset export session writes its output. _(deprecated)_
- [outputFileType](avassetexportsession/outputfiletype.md) — The file type of the output an asset export session writes. _(deprecated)_

### Exporting media

- [- exportAsynchronouslyWithCompletionHandler:](<avassetexportsession/exportasynchronously(completionhandler_).md>) — Starts the asynchronous execution of an export session. _(deprecated)_
- [- cancelExport](<avassetexportsession/cancelexport().md>) — Cancels the execution of an export session. _(deprecated)_

### Monitoring export progress

- [status](avassetexportsession/status-swift.property.md) — The status of the export session. _(deprecated)_
- [progress](avassetexportsession/progress.md) — A value that indicates the progress of the export. _(deprecated)_
- [error](avassetexportsession/error.md) — An optional error object. _(deprecated)_

### Estimating file length and duration

- [estimatedOutputFileLength](avassetexportsession/estimatedoutputfilelength.md) — The estimated length of the exported file, in bytes. _(deprecated)_

### Estimating duration

- [maxDuration](avassetexportsession/maxduration.md) — Provides an estimate of the maximum duration of the exported media. _(deprecated)_
