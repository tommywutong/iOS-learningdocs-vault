---
title: DispatchQueue.AutoreleaseFrequency.inherit
framework: Dispatch
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqueue/autoreleasefrequency/inherit
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/autoreleasefrequency/inherit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/autoreleasefrequency/inherit.json'
content_hash: 'sha256:99cefd82894c3ea1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Dispatch](../../../dispatch.md) · [DispatchQueue](../../dispatchqueue.md) · [AutoreleaseFrequency](../autoreleasefrequency.md)

# DispatchQueue.AutoreleaseFrequency.inherit

<sub>Case</sub>

The queue inherits its autorelease frequency from its target queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case inherit
```

## Discussion

This option is the default behavior for queues you create.

## See Also

### Autorelease Frequencies

- [DispatchQueue.AutoreleaseFrequency.workItem](workitem.md) — The queue configures an autorelease pool before the execution of a block, and releases the objects in that pool after the block finishes executing.
- [DispatchQueue.AutoreleaseFrequency.never](never.md) — The queue does not set up an autorelease pool around executed blocks.
