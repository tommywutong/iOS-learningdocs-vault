---
title: exec
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsource/processevent/exec
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsource/processevent/exec'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsource/processevent/exec.json'
content_hash: 'sha256:6dd87944953b1bac'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Dispatch](../../../dispatch.md) · [DispatchSource](../../dispatchsource.md) · [ProcessEvent](../processevent.md)

# exec

<sub>Type Property</sub>

The process became another executable image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let exec: DispatchSource.ProcessEvent
```

## Discussion

The process has become another executable image via an `exec` or `posix_spawn` function family call.

## See Also

### Process Event Flags

- [all](all.md) — All process-related events.
- [exit](exit.md) — The process has exited (perhaps cleanly, perhaps not).
- [fork](fork.md) — The process created one or more child processes.
- [signal](signal.md) — The process received a UNIX signal.
