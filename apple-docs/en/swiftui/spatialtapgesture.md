---
title: SpatialTapGesture
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/spatialtapgesture
source_url: 'https://developer.apple.com/documentation/swiftui/spatialtapgesture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spatialtapgesture.json'
content_hash: 'sha256:dd2c6cf286c69957'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SpatialTapGesture

<sub>Structure</sub>

A gesture that recognizes one or more taps and reports their location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated struct SpatialTapGesture
```

## Overview

To recognize a tap gesture on a view, create and configure the gesture, and then add it to the view using the [gesture(_:including:)](<view/gesture(__including_).md>) modifier. The following code adds a tap gesture to a [Circle](circle.md) that toggles the color of the circle based on the tap location:

```swift
struct TapGestureView: View {
    @State private var location: CGPoint = .zero

    var tap: some Gesture {
        SpatialTapGesture()
            .onEnded { event in
                self.location = event.location
             }
    }

    var body: some View {
        Circle()
            .fill(self.location.y > 50 ? Color.blue : Color.red)
            .frame(width: 100, height: 100, alignment: .center)
            .gesture(tap)
    }
}
```

## Relationships

- **Conforms To**: [Gesture](gesture.md)

## Topics

### Creating a spatial tap gesture

- [init(count:coordinateSpace:)](<spatialtapgesture/init(count_coordinatespace_)-75s7q.md>) — Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [init(count:coordinateSpace:)](<spatialtapgesture/init(count_coordinatespace_).md>) — Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [init(count:coordinateSpace3D:)](<spatialtapgesture/init(count_coordinatespace3d_).md>) — Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [init(count:coordinateSpace:inputKinds:)](<spatialtapgesture/init(count_coordinatespace_inputkinds_).md>) — Creates a tap gesture with the number of required taps, the coordinate space of the gesture’s location, and the input kinds the gesture recognizes. _(beta)_
- [coordinateSpace](spatialtapgesture/coordinatespace.md) — The coordinate space in which to receive location values.
- [count](spatialtapgesture/count.md) — The required number of tap events.

### Getting the gesture’s value

- [Value](spatialtapgesture/value.md) — The attributes of a tap gesture.

### Deprecated initializers

- [init(count:coordinateSpace:)](<spatialtapgesture/init(count_coordinatespace_)-1b85g.md>) — Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location. _(deprecated)_

## See Also

### Recognizing tap gestures

- [onTapGesture(count:perform:)](<view/ontapgesture(count_perform_).md>) — Adds an action to perform when this view recognizes a tap gesture.
- [onTapGesture(count:coordinateSpace:perform:)](<view/ontapgesture(count_coordinatespace_perform_).md>) — Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [onTapGesture(count:coordinateSpace:inputKinds:perform:)](<view/ontapgesture(count_coordinatespace_inputkinds_perform_).md>) — Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction. _(beta)_
- [TapGesture](tapgesture.md) — A gesture that recognizes one or more taps.
