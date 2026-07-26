---
title: NSGestureRecognizerRepresentableCoordinateSpaceConverter
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter
source_url: 'https://developer.apple.com/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter.json'
content_hash: 'sha256:e2a728eb6850b0da'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# NSGestureRecognizerRepresentableCoordinateSpaceConverter

<sub>Structure</sub>

A structure used to convert locations to and from coordinate spaces in the hierarchy of the SwiftUI view associated with an [NSGestureRecognizerRepresentable](nsgesturerecognizerrepresentable.md).

<sub>macOS</sub>

```swift
struct NSGestureRecognizerRepresentableCoordinateSpaceConverter
```

## Topics

### Instance Properties

- [localLocation](nsgesturerecognizerrepresentablecoordinatespaceconverter/locallocation.md) — The represented gesture recognizer’s current location in the coordinate space of the SwiftUI view it’s attached to.
- [localTranslation](nsgesturerecognizerrepresentablecoordinatespaceconverter/localtranslation.md) — The represented gesture recognizer’s current translation in the coordinate space of the SwiftUI view it’s attached to, or `nil` if the represented gesture recognizer doesn’t respond to `-translationInView:` selector.
- [localVelocity](nsgesturerecognizerrepresentablecoordinatespaceconverter/localvelocity.md) — The represented gesture recognizer’s current velocity in the coordinate space of the SwiftUI view it’s attached to, or `nil` if the represented gesture recognizer doesn’t respond to `-velocityInView:` selector.

### Instance Methods

- [convert(globalPoint:to:)](<nsgesturerecognizerrepresentablecoordinatespaceconverter/convert(globalpoint_to_).md>) — Converts a point in the global coordinate space to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.
- [location(in:)](<nsgesturerecognizerrepresentablecoordinatespaceconverter/location(in_).md>) — Converts the represented gesture recognizer’s current location to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.
- [translation(in:)](<nsgesturerecognizerrepresentablecoordinatespaceconverter/translation(in_).md>) — Converts the represented gesture recognizer’s current translation to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.
- [velocity(in:)](<nsgesturerecognizerrepresentablecoordinatespaceconverter/velocity(in_).md>) — Converts the represented gesture recognizer’s current velocity to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.

## See Also

### Adding AppKit gesture recognizers into SwiftUI view hierarchies

- [NSGestureRecognizerRepresentable](nsgesturerecognizerrepresentable.md) — A wrapper for an `NSGestureRecognizer` that you use to integrate that gesture recognizer into your SwiftUI hierarchy.
- [NSGestureRecognizerRepresentableContext](nsgesturerecognizerrepresentablecontext.md) — Contextual information about the state of the system that you use to create and update a represented gesture recognizer.
