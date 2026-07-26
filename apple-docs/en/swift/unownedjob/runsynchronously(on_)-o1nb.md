---
title: 'runSynchronously(on:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unownedjob/runsynchronously(on:)-o1nb'
source_url: 'https://developer.apple.com/documentation/swift/unownedjob/runsynchronously(on:)-o1nb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unownedjob/runsynchronously%28on%3A%29-o1nb.json'
content_hash: 'sha256:d611c6b24f8e0548'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnownedJob](../unownedjob.md)

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
