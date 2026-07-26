---
title: isCancelled
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchworkitem/iscancelled
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchworkitem/iscancelled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchworkitem/iscancelled.json'
content_hash: 'sha256:815e00cf2e6b5399'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchWorkItem](../dispatchworkitem.md)

# isCancelled

<sub>Instance Property</sub>

A Boolean value indicating whether the work item has been canceled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isCancelled: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) if the work item has been canceled.

## See Also

### Canceling a Work Item

- [cancel()](<cancel().md>) — Cancels the current work item asynchronously.
