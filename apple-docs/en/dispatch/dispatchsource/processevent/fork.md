---
title: fork
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsource/processevent/fork
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsource/processevent/fork'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsource/processevent/fork.json'
content_hash: 'sha256:d2a7e63e537e7836'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Dispatch](../../../dispatch.md) · [DispatchSource](../../dispatchsource.md) · [ProcessEvent](../processevent.md)

# fork

<sub>Type Property</sub>

The process created one or more child processes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let fork: DispatchSource.ProcessEvent
```

## See Also

### Process Event Flags

- [all](all.md) — All process-related events.
- [exec](exec.md) — The process became another executable image.
- [exit](exit.md) — The process has exited (perhaps cleanly, perhaps not).
- [signal](signal.md) — The process received a UNIX signal.
