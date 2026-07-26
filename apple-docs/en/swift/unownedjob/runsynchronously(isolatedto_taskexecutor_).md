---
title: 'runSynchronously(isolatedTo:taskExecutor:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unownedjob/runsynchronously(isolatedto:taskexecutor:)'
source_url: 'https://developer.apple.com/documentation/swift/unownedjob/runsynchronously(isolatedto:taskexecutor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unownedjob/runsynchronously%28isolatedto%3Ataskexecutor%3A%29.json'
content_hash: 'sha256:9f23c216fa16586b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnownedJob](../unownedjob.md)

# runSynchronously(isolatedTo:taskExecutor:)

<sub>Instance Method</sub>

Run this job isolated to the passed in serial executor, while executing it on the specified task executor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func runSynchronously(isolatedTo serialExecutor: UnownedSerialExecutor, taskExecutor: UnownedTaskExecutor)
```

## Parameters

- `serialExecutor` — The executor this job will be semantically running on.

- `taskExecutor` — The task executor this job will be run on.

## Discussion

This operation runs the job on the calling thread and _blocks_ until the job completes. The intended use of this method is for an executor to determine when and where it wants to run the job and then call this method on it.

The passed in executor reference is used to establish the executor context for the job, and should be the same executor as the one semantically calling the `runSynchronously` method.

This operation consumes the job, preventing it accidental use after it has been run.

Converting a `ExecutorJob` to an [UnownedJob](../unownedjob.md) and invoking ``UnownedJob/runSynchronously(isolatedTo:taskExecutor:)` on it multiple times is undefined behavior, as a job can only ever be run once, and must not be accessed after it has been run.

> [!info] See Also
> `runSynchronously(on:)`
