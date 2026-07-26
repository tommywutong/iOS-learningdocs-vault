---
title: type
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uievent/type
source_url: 'https://developer.apple.com/documentation/uikit/uievent/type'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uievent/type.json'
content_hash: 'sha256:d4131ac0254caf5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEvent](../uievent.md)

# type

<sub>Instance Property</sub>

Returns the type of the event.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var type: UIEvent.EventType { get }
```

## Discussion

The [EventType](eventtype.md) constant returned by this property indicates the general type of this event — for example, whether it’s a touch or motion event.

## See Also

### Getting the event type

- [EventType](eventtype.md) — Constants that specify the general type of an event.
- [subtype](subtype.md) — Returns the subtype of the event.
- [EventSubtype](eventsubtype.md) — Constants that specify the subtype of the event in relation to its general type.
