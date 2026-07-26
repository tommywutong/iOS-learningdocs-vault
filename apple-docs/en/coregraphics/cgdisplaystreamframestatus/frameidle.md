---
title: CGDisplayStreamFrameStatus.frameIdle
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdisplaystreamframestatus/frameidle
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaystreamframestatus/frameidle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaystreamframestatus/frameidle.json'
content_hash: 'sha256:168c931a6627d105'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDisplayStreamFrameStatus](../cgdisplaystreamframestatus.md)

# CGDisplayStreamFrameStatus.frameIdle

<sub>Case</sub>

A new frame was not generated because the display did not change.

<sub>Mac Catalyst, macOS</sub>

```swift
case frameIdle
```

## See Also

### Constants

- [kCGDisplayStreamFrameStatusFrameComplete](framecomplete.md) — A new frame was generated.
- [kCGDisplayStreamFrameStatusFrameBlank](frameblank.md) — A new frame was not generated because the display has gone blank.
- [kCGDisplayStreamFrameStatusStopped](stopped.md) — The display stream was stopped.
