---
title: DispatchDataIterator
framework: Dispatch
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchdataiterator
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchdataiterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchdataiterator.json'
content_hash: 'sha256:d32a568922c50895'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchDataIterator

<sub>Structure</sub>

A byte-by-byte iterator over the contents of a dispatch data object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DispatchDataIterator
```

## Relationships

- **Conforms To**: [IteratorProtocol](../swift/iteratorprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

## Topics

### Iterating Over a Sequence’s Elements

- [next()](<dispatchdataiterator/next().md>)

## See Also

### System Event Monitoring

- [DispatchSource](dispatchsource.md) — An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [Dispatch Source](dispatch-source.md) — An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [DispatchIO](dispatchio.md) — An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [DispatchData](dispatchdata.md) — An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [Dispatch I/O](dispatch-i-o.md) — An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [Dispatch Data](dispatch-data.md) — An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [DispatchSourceProtocol](dispatchsourceprotocol.md) — Defines a common set of properties and methods that are shared with all dispatch source types.
