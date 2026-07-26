---
title: subtype
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uievent/subtype
source_url: 'https://developer.apple.com/documentation/uikit/uievent/subtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uievent/subtype.json'
content_hash: 'sha256:0784dd9ed2adabf7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEvent](../uievent.md)

# subtype

<sub>Instance Property</sub>

Returns the subtype of the event.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var subtype: UIEvent.EventSubtype { get }
```

## Discussion

The [EventSubtype](eventsubtype.md) constant returned by this property indicates the subtype of the event in relation to the general type, which you can retrieve from the [type](type.md) property.

## See Also

### Getting the event type

- [type](type.md) — Returns the type of the event.
- [EventType](eventtype.md) — Constants that specify the general type of an event.
- [EventSubtype](eventsubtype.md) — Constants that specify the subtype of the event in relation to its general type.
