---
title: executePlan()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassetwritingplanner/executeplan()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/executeplan()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwritingplanner/executeplan%28%29.json'
content_hash: 'sha256:515e20be96debd6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWritingPlanner](../avassetwritingplanner.md)

# executePlan()

<sub>Instance Method</sub>

Starts the incremental segment writing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func executePlan() async throws -> AVComposition
```

## Return Value

The assembly composition containing all completed segments from all tracks.

## Discussion

The planner calls every segment handler sequentially, starting with the first one available, or at the next unfinished segment if resuming a previously canceled session. Upon success (no error thrown), this means that all segments for all tracks have been completed. The returned assemblyComposition can be used to put the incremental tracks back together. One way to accomplish this is by feeding the assemblyComposition through AVAssetExportSession with the pass-through preset. The client is responsible for combining any other tracks (those that were not eligible for incremental writing), as well as establishing any track references between the incrementally written tracks and the other tracks in the final asset.

> [!danger] Throws
> An error if the export fails or if a segment handler reports an error.
