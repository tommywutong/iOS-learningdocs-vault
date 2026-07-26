---
title: all
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsource/processevent/all
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsource/processevent/all'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsource/processevent/all.json'
content_hash: 'sha256:e19e1031d1425737'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Dispatch](../../../dispatch.md) · [DispatchSource](../../dispatchsource.md) · [ProcessEvent](../processevent.md)

# all

<sub>Type Property</sub>

All process-related events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let all: DispatchSource.ProcessEvent
```

## See Also

### Process Event Flags

- [exec](exec.md) — The process became another executable image.
- [exit](exit.md) — The process has exited (perhaps cleanly, perhaps not).
- [fork](fork.md) — The process created one or more child processes.
- [signal](signal.md) — The process received a UNIX signal.
