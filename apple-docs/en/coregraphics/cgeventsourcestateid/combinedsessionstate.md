---
title: CGEventSourceStateID.combinedSessionState
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgeventsourcestateid/combinedsessionstate
source_url: 'https://developer.apple.com/documentation/coregraphics/cgeventsourcestateid/combinedsessionstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgeventsourcestateid/combinedsessionstate.json'
content_hash: 'sha256:cbbc680dd190e86b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGEventSourceStateID](../cgeventsourcestateid.md)

# CGEventSourceStateID.combinedSessionState

<sub>Case</sub>

Specifies that an event source should use the event state table that reflects the combined state of all event sources posting to the current user login session.

<sub>Mac Catalyst, macOS</sub>

```swift
case combinedSessionState
```

## See Also

### Constants

- [kCGEventSourceStatePrivate](privatestate.md) — Specifies that an event source should use a private event state table.
- [kCGEventSourceStateHIDSystemState](hidsystemstate.md) — Specifies that an event source should use the event state table that reflects the combined state of all hardware event sources posting from the HID system.
