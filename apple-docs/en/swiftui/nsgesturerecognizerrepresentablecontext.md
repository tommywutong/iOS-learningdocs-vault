---
title: NSGestureRecognizerRepresentableContext
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nsgesturerecognizerrepresentablecontext
source_url: 'https://developer.apple.com/documentation/swiftui/nsgesturerecognizerrepresentablecontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsgesturerecognizerrepresentablecontext.json'
content_hash: 'sha256:2bea05f56f95640a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# NSGestureRecognizerRepresentableContext

<sub>Structure</sub>

Contextual information about the state of the system that you use to create and update a represented gesture recognizer.

<sub>macOS</sub>

```swift
struct NSGestureRecognizerRepresentableContext<Representable> where Representable : NSGestureRecognizerRepresentable
```

## Topics

### Instance Properties

- [converter](nsgesturerecognizerrepresentablecontext/converter.md) — A structure used to convert locations to and from coordinate spaces in the hierarchy of the associated SwiftUI view.
- [coordinator](nsgesturerecognizerrepresentablecontext/coordinator.md) — The custom object that you use to communicate state changes from your gesture recognizer to other parts of your SwiftUI interface.

## See Also

### Adding AppKit gesture recognizers into SwiftUI view hierarchies

- [NSGestureRecognizerRepresentable](nsgesturerecognizerrepresentable.md) — A wrapper for an `NSGestureRecognizer` that you use to integrate that gesture recognizer into your SwiftUI hierarchy.
- [NSGestureRecognizerRepresentableCoordinateSpaceConverter](nsgesturerecognizerrepresentablecoordinatespaceconverter.md) — A structure used to convert locations to and from coordinate spaces in the hierarchy of the SwiftUI view associated with an [NSGestureRecognizerRepresentable](nsgesturerecognizerrepresentable.md).
