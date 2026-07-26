---
title: CLMonitor.Events
framework: Core Location
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitor-2r51v/events-swift.struct
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/events-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitor-2r51v/events-swift.struct.json'
content_hash: 'sha256:13b52bd286bf2f30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLMonitor](../clmonitor-2r51v.md)

# CLMonitor.Events

<sub>Structure</sub>

A type that represents an asynchronous sequence of events.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
struct Events
```

## Overview

Use this structure to access and iterate over the events the framework delivers.

## Relationships

- **Conforms To**: [AsyncSequence](../../swift/asyncsequence.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Utility methods

- [Iterator](events-swift.struct/iterator.md) — The type that allows iteration over the elements of the sequence.

## See Also

### Monitor events

- [Event](event.md) — An event object that the framework passes to the events sequence in the monitor.
- [Record](record.md) — A structure that represents a condition and its associated event information that the framework is monitoring.
