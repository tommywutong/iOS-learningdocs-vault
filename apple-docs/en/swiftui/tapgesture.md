---
title: TapGesture
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 16.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tapgesture
source_url: 'https://developer.apple.com/documentation/swiftui/tapgesture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tapgesture.json'
content_hash: 'sha256:b4c706eb5fe26315'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TapGesture

<sub>Structure</sub>

A gesture that recognizes one or more taps.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct TapGesture
```

## Overview

To recognize a tap gesture on a view, create and configure the gesture, and then add it to the view using the [gesture(_:including:)](<view/gesture(__including_).md>) modifier. The following code adds a tap gesture to a [Circle](circle.md) that toggles the color of the circle:

```swift
struct TapGestureView: View {
    @State private var tapped = false

    var tap: some Gesture {
        TapGesture(count: 1)
            .onEnded { _ in self.tapped = !self.tapped }
    }

    var body: some View {
        Circle()
            .fill(self.tapped ? Color.blue : Color.red)
            .frame(width: 100, height: 100, alignment: .center)
            .gesture(tap)
    }
}
```

## Relationships

- **Conforms To**: [Gesture](gesture.md)

## Topics

### Creating a tap gesture

- [init(count:)](<tapgesture/init(count_).md>) — Creates a tap gesture with the number of required taps.
- [init(count:inputKinds:)](<tapgesture/init(count_inputkinds_).md>) — Creates a tap gesture with the number of required taps and the input kinds the gesture recognizes. _(beta)_
- [count](tapgesture/count.md) — The required number of tap events.

## See Also

### Recognizing tap gestures

- [onTapGesture(count:perform:)](<view/ontapgesture(count_perform_).md>) — Adds an action to perform when this view recognizes a tap gesture.
- [onTapGesture(count:coordinateSpace:perform:)](<view/ontapgesture(count_coordinatespace_perform_).md>) — Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [onTapGesture(count:coordinateSpace:inputKinds:perform:)](<view/ontapgesture(count_coordinatespace_inputkinds_perform_).md>) — Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction. _(beta)_
- [SpatialTapGesture](spatialtapgesture.md) — A gesture that recognizes one or more taps and reports their location.
