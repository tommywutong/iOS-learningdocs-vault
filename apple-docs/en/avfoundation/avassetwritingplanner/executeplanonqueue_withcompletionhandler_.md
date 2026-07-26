---
title: 'executePlanOnQueue:withCompletionHandler:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avassetwritingplanner/executeplanonqueue:withcompletionhandler:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/executeplanonqueue:withcompletionhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwritingplanner/executeplanonqueue%3Awithcompletionhandler%3A.json'
content_hash: 'sha256:8268d0d31c5a7c85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWritingPlanner](../avassetwritingplanner.md)

# executePlanOnQueue:withCompletionHandler:

<sub>Instance Method</sub>

Starts the incremental segment writing on a given dispatch queue

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) executePlanOnQueue:(dispatch_queue_t) executionQueue withCompletionHandler:(void (^)(AVComposition *assemblyComposition, NSError *error)) completionHandler;
```

## Parameters

- `executionQueue` — The dispatch queue on which the planner executes the plans. The segment writing callback blocks and the completion handler are called from this queue.

- `completionHandler` — Called when all the incremental segments on all tracks added to the planner have completed, or some error occurs.

## Discussion

The planner calls the writingSegmentCallbackBlock sequentially, starting with the first segment work, or at the next unfinished segment if resuming a previously suspended export. The completionHandler is called upon failure or success. When called with success (error is nil), this means that all segments for all tracks have been completed. The assemblyComposition will be non-nil and can be used to put the incremental tracks back together. One way to accomplish this is by feeding the assemblyComposition through AVAssetExportSession with the pass-through preset. The client is responsible for combining any other tracks (those that were not eligible for incremental writing), as well as establishing any track references between the incrementally written tracks and the other tracks in the final asset.

## See Also

### Executing the plan

- [executePlanWithCompletionHandler:](executeplanwithcompletionhandler_.md) — Starts the incremental segment writing. _(beta)_
