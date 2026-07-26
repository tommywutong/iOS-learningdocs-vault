---
title: DISPATCH_MEMORYPRESSURE_WARN
framework: Dispatch
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_memorypressure_warn
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_memorypressure_warn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_memorypressure_warn.json'
content_hash: 'sha256:3b107ec810cf6067'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DISPATCH_MEMORYPRESSURE_WARN

<sub>Global Variable</sub>

The system memory pressure condition is at the warning stage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var DISPATCH_MEMORYPRESSURE_WARN: Int32 { get }
```

## Discussion

Apps should release memory that they do not need right now.

## See Also

### Memory Pressure Event Flags

- [DISPATCH_MEMORYPRESSURE_NORMAL](dispatch_memorypressure_normal.md) — The system memory pressure condition has returned to normal.
- [DISPATCH_MEMORYPRESSURE_CRITICAL](dispatch_memorypressure_critical.md) — The system memory pressure condition is at the critical stage.
