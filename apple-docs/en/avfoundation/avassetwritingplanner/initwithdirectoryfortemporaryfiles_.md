---
title: 'initWithDirectoryForTemporaryFiles:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avassetwritingplanner/initwithdirectoryfortemporaryfiles:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/initwithdirectoryfortemporaryfiles:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwritingplanner/initwithdirectoryfortemporaryfiles%3A.json'
content_hash: 'sha256:97886d133f861000'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWritingPlanner](../avassetwritingplanner.md)

# initWithDirectoryForTemporaryFiles:

<sub>Instance Method</sub>

Creates an instance of AVAssetWritingPlanner given a unique file directory to host all incremental segment files and other intermediate files.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithDirectoryForTemporaryFiles:(NSURL *) directoryForTemporaryFiles;
```

## Parameters

- `directoryForTemporaryFiles` — The file directory to host all incremental segment files and other intermediate files for the current AVAssetWritingPlanner operation.

## Return Value

An instance of AVAssetWritingPlanner.

## Discussion

The directoryForTemporaryFiles must differ between export operations, but remain identical when resuming the same export operation. The client is responsible for ensuring that this NSURL can be re-synthesized exactly across multiple launches of the app and device reboots (if desired). For example, if there are multiple source assets that need to be exported concurrently, these should result in unique NSURLs so that the planner can correctly identify each one. Another example is if the same source asset is being output with different compression configurations, they also should be uniquely identifiable so that they do not alias to the same output file. Source assets, compression configs, and video composition settings should all be taken into account when generating the unique URL. A resuming planner instance can only find the files from a previous planner instance if presented with the identical URL. All intermediate segment files and metadata files are stored in the specified directoryForTemporaryFiles. This initializer throws NSInvalidArgumentException if directoryForTemporaryFiles does not exist, or it is not writable, or it contains a corrupted AVAssetWritingPlanner incremental state file.
