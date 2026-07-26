---
title: DispatchQueue.AutoreleaseFrequency.workItem
framework: Dispatch
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqueue/autoreleasefrequency/workitem
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/autoreleasefrequency/workitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/autoreleasefrequency/workitem.json'
content_hash: 'sha256:959ec88846a82086'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Dispatch](../../../dispatch.md) · [DispatchQueue](../../dispatchqueue.md) · [AutoreleaseFrequency](../autoreleasefrequency.md)

# DispatchQueue.AutoreleaseFrequency.workItem

<sub>Case</sub>

The queue configures an autorelease pool before the execution of a block, and releases the objects in that pool after the block finishes executing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case workItem
```

## See Also

### Autorelease Frequencies

- [DispatchQueue.AutoreleaseFrequency.inherit](inherit.md) — The queue inherits its autorelease frequency from its target queue.
- [DispatchQueue.AutoreleaseFrequency.never](never.md) — The queue does not set up an autorelease pool around executed blocks.
