---
title: RunLoop.Mode
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/runloop/mode
source_url: 'https://developer.apple.com/documentation/foundation/runloop/mode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/mode.json'
content_hash: 'sha256:41ff165bca137e4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RunLoop](../runloop.md)

# RunLoop.Mode

<sub>Structure</sub>

Modes that a run loop operates in.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Mode
```

## Discussion

[NSApplication](../../appkit/nsapplication.md) defines additional run loop modes, including the following:

- [modalPanel](mode/modalpanel.md)
- [eventTracking](mode/eventtracking.md)

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### System Run Loop Modes

- [NSRunLoopCommonModes](mode/common.md) — A pseudo-mode that includes one or more other run loop modes.
- [NSDefaultRunLoopMode](mode/default.md) — The mode set to handle input sources other than connection objects.
- [eventTracking](mode/eventtracking.md) — The mode set when tracking events modally, such as a mouse-dragging loop.
- [modalPanel](mode/modalpanel.md) — The mode set when waiting for input from a modal panel, such as a save or open panel.
- [tracking](mode/tracking.md) — The mode set while tracking in controls takes place.

### Run Loop Mode Creation

- [init(_:)](<mode/init(__).md>) — Creates a run loop mode using the specified string value.
- [init(rawValue:)](<mode/init(rawvalue_).md>) — Creates a run loop mode using the specified raw string value.

## See Also

### Accessing Run Loops and Modes

- [currentRunLoop](current.md) — Returns the run loop for the current thread.
- [currentMode](currentmode.md) — The receiver’s current input mode.
- [- limitDateForMode:](<limitdate(formode_).md>) — Performs one pass through the run loop in the specified mode and returns the date at which the next timer is scheduled to fire.
- [mainRunLoop](main.md) — Returns the run loop of the main thread.
- [- getCFRunLoop](<getcfrunloop().md>) — Returns the receiver’s underlying run loop object.
