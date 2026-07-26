---
title: UIEvent.EventType
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uievent/eventtype
source_url: 'https://developer.apple.com/documentation/uikit/uievent/eventtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uievent/eventtype.json'
content_hash: 'sha256:9099f5a8e6617944'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEvent](../uievent.md)

# UIEvent.EventType

<sub>Enumeration</sub>

Constants that specify the general type of an event.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum EventType
```

## Overview

You can obtain the type of an event from the [type](type.md) property. To further identify the event, you might also need to determine its subtype, which you obtain from the [subtype](subtype.md) property.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIEventTypeTouches](eventtype/touches.md) — The event relates to touches on the screen.
- [UIEventTypeMotion](eventtype/motion.md) — The event relates to motion of the device, such as when a person shakes it.
- [UIEventTypeRemoteControl](eventtype/remotecontrol.md) — The event is a remote-control event.
- [UIEventTypePresses](eventtype/presses.md) — The event relates to the press of a physical button.
- [UIEventTypeScroll](eventtype/scroll.md) — The event relates to scrolling from an indirect input device.
- [UIEventTypeHover](eventtype/hover.md) — The event relates to a pointer from an indirect input device moving over a user interface element.
- [UIEventTypeTransform](eventtype/transform.md) — The event relates to a pointer from an indirect input device performing a transformation on a user interface element, such as scaling, rotation, or translation.

### Initializers

- [init(rawValue:)](<eventtype/init(rawvalue_).md>)

## See Also

### Getting the event type

- [type](type.md) — Returns the type of the event.
- [subtype](subtype.md) — Returns the subtype of the event.
- [EventSubtype](eventsubtype.md) — Constants that specify the subtype of the event in relation to its general type.
