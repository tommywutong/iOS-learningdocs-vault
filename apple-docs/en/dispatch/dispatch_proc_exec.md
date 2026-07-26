---
title: DISPATCH_PROC_EXEC
framework: Dispatch
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_proc_exec
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_proc_exec'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_proc_exec.json'
content_hash: 'sha256:a69aa7ef8ebc1a76'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DISPATCH_PROC_EXEC

<sub>Global Variable</sub>

The process became another executable image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var DISPATCH_PROC_EXEC: Int32 { get }
```

## Discussion

The process has become another executable image via an `exec` or `posix_spawn` function family call.

## See Also

### Process Event Flags

- [DISPATCH_PROC_EXIT](dispatch_proc_exit.md) — The process has exited (perhaps cleanly, perhaps not).
- [DISPATCH_PROC_FORK](dispatch_proc_fork.md) — The process created one or more child processes.
- [DISPATCH_PROC_SIGNAL](dispatch_proc_signal.md) — The process received a UNIX signal.
