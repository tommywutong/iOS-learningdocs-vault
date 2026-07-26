---
title: isEmpty
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/throwingdiscardingtaskgroup/isempty
source_url: 'https://developer.apple.com/documentation/swift/throwingdiscardingtaskgroup/isempty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingdiscardingtaskgroup/isempty.json'
content_hash: 'sha256:b700ae0ddf24e5fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ThrowingDiscardingTaskGroup](../throwingdiscardingtaskgroup.md)

# isEmpty

<sub>Instance Property</sub>

A Boolean value that indicates whether the group has any remaining tasks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEmpty: Bool { get }
```

## Return Value

`true` if the group has no pending tasks; otherwise `false`.

## Discussion

At the start of the body of a `withThrowingDiscardingTaskGroup(returning:body:)` call, the task group is always empty.

It’s guaranteed to be empty when returning from that body because a task group waits for all child tasks to complete before returning.
