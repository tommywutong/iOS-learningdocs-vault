---
title: CLMonitor.Record
framework: Core Location
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitor-2r51v/record
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/record'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitor-2r51v/record.json'
content_hash: 'sha256:04cfe645f740f2a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLMonitor](../clmonitor-2r51v.md)

# CLMonitor.Record

<sub>Structure</sub>

A structure that represents a condition and its associated event information that the framework is monitoring.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
struct Record
```

## Overview

The `CLMonitor.Record` contains a condition and most recent event that affects it.

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Record characteristics

- [condition](record/condition.md) — The condition that the framework is monitoring for.
- [lastEvent](record/lastevent.md) — The most recent event the monitor records.

## See Also

### Monitor events

- [Event](event.md) — An event object that the framework passes to the events sequence in the monitor.
- [Events](events-swift.struct.md) — A type that represents an asynchronous sequence of events.
