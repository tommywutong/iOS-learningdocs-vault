---
title: DispatchSource.ProcessEvent
framework: Dispatch
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsource/processevent
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsource/processevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsource/processevent.json'
content_hash: 'sha256:343b357793e61848'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSource](../dispatchsource.md)

# DispatchSource.ProcessEvent

<sub>Structure</sub>

Events related to a process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ProcessEvent
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Process Event Flags

- [all](processevent/all.md) — All process-related events.
- [exec](processevent/exec.md) — The process became another executable image.
- [exit](processevent/exit.md) — The process has exited (perhaps cleanly, perhaps not).
- [fork](processevent/fork.md) — The process created one or more child processes.
- [signal](processevent/signal.md) — The process received a UNIX signal.

## See Also

### Creating a Process Source

- [makeProcessSource(identifier:eventMask:queue:)](<makeprocesssource(identifier_eventmask_queue_).md>) — Creates a new dispatch source object for monitoring the specified process.
- [DispatchSourceProcess](../dispatchsourceprocess.md) — A dispatch source that monitors an external process for events.
