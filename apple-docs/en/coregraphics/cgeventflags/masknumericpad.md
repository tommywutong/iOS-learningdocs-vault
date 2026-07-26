---
title: maskNumericPad
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgeventflags/masknumericpad
source_url: 'https://developer.apple.com/documentation/coregraphics/cgeventflags/masknumericpad'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgeventflags/masknumericpad.json'
content_hash: 'sha256:a1ea0ce2e046ea6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGEventFlags](../cgeventflags.md)

# maskNumericPad

<sub>Type Property</sub>

Identifies key events from the numeric keypad area on extended keyboards.

<sub>Mac Catalyst, macOS</sub>

```swift
static var maskNumericPad: CGEventFlags { get }
```

## See Also

### Constants

- [kCGEventFlagMaskAlphaShift](maskalphashift.md) — Indicates that the Caps Lock key is down for a keyboard, mouse, or flag-changed event.
- [kCGEventFlagMaskShift](maskshift.md) — Indicates that the Shift key is down for a keyboard, mouse, or flag-changed event.
- [kCGEventFlagMaskControl](maskcontrol.md) — Indicates that the Control key is down for a keyboard, mouse, or flag-changed event.
- [kCGEventFlagMaskAlternate](maskalternate.md) — Indicates that the Alt or Option key is down for a keyboard, mouse, or flag-changed event.
- [kCGEventFlagMaskCommand](maskcommand.md) — Indicates that the Command key is down for a keyboard, mouse, or flag-changed event.
- [kCGEventFlagMaskHelp](maskhelp.md) — Indicates that the Help modifier key is down for a keyboard, mouse, or flag-changed event. This key is not present on most keyboards, and is different than the Help key found in the same row as Home and Page Up.
- [kCGEventFlagMaskSecondaryFn](masksecondaryfn.md) — Indicates that the Fn (Function) key is down for a keyboard, mouse, or flag-changed event. This key is found primarily on laptop keyboards.
- [kCGEventFlagMaskNonCoalesced](masknoncoalesced.md) — Indicates that mouse and pen movement events are not being coalesced.
