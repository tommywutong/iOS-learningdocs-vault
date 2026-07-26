---
title: 'init(directoryForTemporaryFiles:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avassetwritingplanner/init(directoryfortemporaryfiles:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/init(directoryfortemporaryfiles:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwritingplanner/init%28directoryfortemporaryfiles%3A%29.json'
content_hash: 'sha256:60c297f6b0cdab4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWritingPlanner](../avassetwritingplanner.md)

# init(directoryForTemporaryFiles:)

<sub>Initializer</sub>

Creates an instance of AVAssetWritingPlanner given a unique file directory to host all incremental segment files and other intermediate files.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(directoryForTemporaryFiles: URL) throws
```

## Parameters

- `directoryForTemporaryFiles` — The file directory to host all incremental segment files and other intermediate files for the current AVAssetWritingPlanner operation.

## Discussion

The `directoryForTemporaryFiles` must differ between export operations, but remain identical when resuming the same export operation. The client is responsible for ensuring that this URL can be re-synthesized exactly across multiple launches of the app and device reboots (if desired). For example, if there are multiple source assets that need to be exported concurrently, these should result in unique URLs so that the planner can correctly identify each one. Another example is if the same source asset is being output with different compression configurations, they also should be uniquely identifiable so that they do not alias to the same output file.

A resuming planner instance can only find the files from a previous planner instance if presented with the identical URL. All intermediate segment files and metadata files are stored in the specified `directoryForTemporaryFiles`.

Source assets, compression configs, and video composition settings should all be taken into account when generating the unique URL.

> [!danger] Throws
> An error if `directoryForTemporaryFiles` does not exist, or it is not writable, or it contains a corrupted AVAssetWritingPlanner incremental state file.
