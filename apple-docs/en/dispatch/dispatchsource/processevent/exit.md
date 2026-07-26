---
title: exit
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsource/processevent/exit
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsource/processevent/exit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsource/processevent/exit.json'
content_hash: 'sha256:91adc20ffe2b59f9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Dispatch](../../../dispatch.md) · [DispatchSource](../../dispatchsource.md) · [ProcessEvent](../processevent.md)

# exit

<sub>Type Property</sub>

The process has exited (perhaps cleanly, perhaps not).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let exit: DispatchSource.ProcessEvent
```

## See Also

### Process Event Flags

- [all](all.md) — All process-related events.
- [exec](exec.md) — The process became another executable image.
- [fork](fork.md) — The process created one or more child processes.
- [signal](signal.md) — The process received a UNIX signal.
