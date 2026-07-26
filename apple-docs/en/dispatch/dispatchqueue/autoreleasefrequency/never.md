---
title: DispatchQueue.AutoreleaseFrequency.never
framework: Dispatch
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqueue/autoreleasefrequency/never
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/autoreleasefrequency/never'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/autoreleasefrequency/never.json'
content_hash: 'sha256:2ea9ea772759ec14'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Dispatch](../../../dispatch.md) · [DispatchQueue](../../dispatchqueue.md) · [AutoreleaseFrequency](../autoreleasefrequency.md)

# DispatchQueue.AutoreleaseFrequency.never

<sub>Case</sub>

The queue does not set up an autorelease pool around executed blocks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case never
```

## Discussion

This option is the default behavior for the system-defined global queues.

## See Also

### Autorelease Frequencies

- [DispatchQueue.AutoreleaseFrequency.inherit](inherit.md) — The queue inherits its autorelease frequency from its target queue.
- [DispatchQueue.AutoreleaseFrequency.workItem](workitem.md) — The queue configures an autorelease pool before the execution of a block, and releases the objects in that pool after the block finishes executing.
