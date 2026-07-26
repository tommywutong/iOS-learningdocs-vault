---
title: predictedEndLocation
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/draggesture/value/predictedendlocation
source_url: 'https://developer.apple.com/documentation/swiftui/draggesture/value/predictedendlocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/draggesture/value/predictedendlocation.json'
content_hash: 'sha256:570a1ae3cb04994f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [DragGesture](../../draggesture.md) · [Value](../value.md)

# predictedEndLocation

<sub>Instance Property</sub>

A prediction, based on the current drag velocity, of where the final location will be if dragging stopped now.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var predictedEndLocation: CGPoint { get }
```

## See Also

### Getting 2D position

- [startLocation](startlocation.md) — The location of the drag gesture’s first event.
- [location](location.md) — The location of the drag gesture’s current event.
- [translation](translation.md) — The total translation from the start of the drag gesture to the current event of the drag gesture.
- [predictedEndTranslation](predictedendtranslation.md) — A prediction, based on the current drag velocity, of what the final translation will be if dragging stopped now.
