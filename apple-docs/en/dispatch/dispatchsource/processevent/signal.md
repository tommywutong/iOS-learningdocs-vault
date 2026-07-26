---
title: signal
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsource/processevent/signal
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsource/processevent/signal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsource/processevent/signal.json'
content_hash: 'sha256:c7c17b7db7451ac2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Dispatch](../../../dispatch.md) · [DispatchSource](../../dispatchsource.md) · [ProcessEvent](../processevent.md)

# signal

<sub>Type Property</sub>

The process received a UNIX signal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let signal: DispatchSource.ProcessEvent
```

## See Also

### Process Event Flags

- [all](all.md) — All process-related events.
- [exec](exec.md) — The process became another executable image.
- [exit](exit.md) — The process has exited (perhaps cleanly, perhaps not).
- [fork](fork.md) — The process created one or more child processes.
