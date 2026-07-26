---
title: CGEventSourceStateID.hidSystemState
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgeventsourcestateid/hidsystemstate
source_url: 'https://developer.apple.com/documentation/coregraphics/cgeventsourcestateid/hidsystemstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgeventsourcestateid/hidsystemstate.json'
content_hash: 'sha256:19cd688ecb376070'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGEventSourceStateID](../cgeventsourcestateid.md)

# CGEventSourceStateID.hidSystemState

<sub>Case</sub>

Specifies that an event source should use the event state table that reflects the combined state of all hardware event sources posting from the HID system.

<sub>Mac Catalyst, macOS</sub>

```swift
case hidSystemState
```

## See Also

### Constants

- [kCGEventSourceStatePrivate](privatestate.md) — Specifies that an event source should use a private event state table.
- [kCGEventSourceStateCombinedSessionState](combinedsessionstate.md) — Specifies that an event source should use the event state table that reflects the combined state of all event sources posting to the current user login session.
