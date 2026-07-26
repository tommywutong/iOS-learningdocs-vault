---
title: 'runSynchronously(on:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/executorjob/runsynchronously(on:)-9dhs1'
source_url: 'https://developer.apple.com/documentation/swift/executorjob/runsynchronously(on:)-9dhs1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/executorjob/runsynchronously%28on%3A%29-9dhs1.json'
content_hash: 'sha256:a1f9751aae960907'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ExecutorJob](../executorjob.md)

# runSynchronously(on:)

<sub>Instance Method</sub>

Run this job on the passed in executor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func runSynchronously(on executor: UnownedSerialExecutor)
```

## Parameters

- `executor` — The executor this job will be semantically running on.

## Discussion

This operation runs the job on the calling thread and _blocks_ until the job completes. The intended use of this method is for an executor to determine when and where it wants to run the job and then call this method on it.

The passed in executor reference is used to establish the executor context for the job, and should be the same executor as the one semantically calling the `runSynchronously` method.

This operation consumes the job, preventing it accidental use after it has been run.

Converting a `ExecutorJob` to an [UnownedJob](../unownedjob.md) and invoking ``UnownedJob/runSynchronously(_:)` on it multiple times is undefined behavior, as a job can only ever be run once, and must not be accessed after it has been run.
