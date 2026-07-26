---
title: DISPATCH_MEMORYPRESSURE_CRITICAL
framework: Dispatch
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_memorypressure_critical
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_memorypressure_critical'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_memorypressure_critical.json'
content_hash: 'sha256:ad49f0309595ebf4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DISPATCH_MEMORYPRESSURE_CRITICAL

<sub>Global Variable</sub>

The system memory pressure condition is at the critical stage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var DISPATCH_MEMORYPRESSURE_CRITICAL: Int32 { get }
```

## Discussion

Apps should release as much memory as possible.

## See Also

### Memory Pressure Event Flags

- [DISPATCH_MEMORYPRESSURE_WARN](dispatch_memorypressure_warn.md) — The system memory pressure condition is at the warning stage.
- [DISPATCH_MEMORYPRESSURE_NORMAL](dispatch_memorypressure_normal.md) — The system memory pressure condition has returned to normal.
