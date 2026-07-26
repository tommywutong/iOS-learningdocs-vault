---
title: UIGestureRecognizerRepresentableContext
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uigesturerecognizerrepresentablecontext
source_url: 'https://developer.apple.com/documentation/swiftui/uigesturerecognizerrepresentablecontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uigesturerecognizerrepresentablecontext.json'
content_hash: 'sha256:12659d2917d6efbe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# UIGestureRecognizerRepresentableContext

<sub>Structure</sub>

Contextual information about the state of the system that you use to create and update a represented gesture recognizer.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct UIGestureRecognizerRepresentableContext<Representable> where Representable : UIGestureRecognizerRepresentable
```

## Topics

### Instance Properties

- [converter](uigesturerecognizerrepresentablecontext/converter.md) — A structure used to convert locations to/from coordinate spaces in the hierarchy of the associated SwiftUI view.
- [coordinator](uigesturerecognizerrepresentablecontext/coordinator.md) — The custom object that you use to communicate state changes from your gesture recognizer to other parts of your SwiftUI interface.

## See Also

### Adding UIKit gesture recognizers into SwiftUI view hierarchies

- [UIGestureRecognizerRepresentable](uigesturerecognizerrepresentable.md) — A wrapper for a `UIGestureRecognizer` that you use to integrate that gesture recognizer into your SwiftUI hierarchy.
- [UIGestureRecognizerRepresentableCoordinateSpaceConverter](uigesturerecognizerrepresentablecoordinatespaceconverter.md) — A proxy structure used to convert locations to/from coordinate spaces in the hierarchy of the SwiftUI view associated with a [UIGestureRecognizerRepresentable](uigesturerecognizerrepresentable.md).
