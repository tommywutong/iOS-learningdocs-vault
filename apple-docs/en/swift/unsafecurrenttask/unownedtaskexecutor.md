---
title: unownedTaskExecutor
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsafecurrenttask/unownedtaskexecutor
source_url: 'https://developer.apple.com/documentation/swift/unsafecurrenttask/unownedtaskexecutor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafecurrenttask/unownedtaskexecutor.json'
content_hash: 'sha256:a582f0845c93f2d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeCurrentTask](../unsafecurrenttask.md)

# unownedTaskExecutor

<sub>Instance Property</sub>

The current [TaskExecutor](../taskexecutor.md) preference, if this task has one configured.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var unownedTaskExecutor: UnownedTaskExecutor? { get }
```

## Discussion

The executor may be used to compare for equality with an expected executor preference.

The lifetime of an executor is not guaranteed by an [UnownedTaskExecutor](../unownedtaskexecutor.md), so accessing it must be handled with great case – and the program must use other means to guarantee the executor remains alive while it is in use.
