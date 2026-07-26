---
title: LongPressGesture
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/longpressgesture
source_url: 'https://developer.apple.com/documentation/swiftui/longpressgesture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/longpressgesture.json'
content_hash: 'sha256:9482c06c7a9e9316'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# LongPressGesture

<sub>Structure</sub>

A gesture that succeeds when the user performs a long press.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct LongPressGesture
```

## Overview

To recognize a long-press gesture on a view, create and configure the gesture, then add it to the view using the [gesture(_:including:)](<view/gesture(__including_).md>) modifier.

Add a long-press gesture to a [Circle](circle.md) to animate its color from blue to red, and then change it to green when the gesture ends:

```swift
struct LongPressGestureView: View {
    @GestureState private var isDetectingLongPress = false
    @State private var completedLongPress = false

    var longPress: some Gesture {
        LongPressGesture(minimumDuration: 3)
            .updating($isDetectingLongPress) { currentState, gestureState,
                    transaction in
                gestureState = currentState
                transaction.animation = Animation.easeIn(duration: 2.0)
            }
            .onEnded { finished in
                self.completedLongPress = finished
            }
    }

    var body: some View {
        Circle()
            .fill(self.isDetectingLongPress ?
                Color.red :
                (self.completedLongPress ? Color.green : Color.blue))
            .frame(width: 100, height: 100, alignment: .center)
            .gesture(longPress)
    }
}
```

## Relationships

- **Conforms To**: [Gesture](gesture.md)

## Topics

### Creating a long press gesture

- [init(minimumDuration:)](<longpressgesture/init(minimumduration_).md>) — Creates a long-press gesture with a minimum duration
- [init(minimumDuration:maximumDistance:)](<longpressgesture/init(minimumduration_maximumdistance_).md>) — Creates a long-press gesture with a minimum duration and a maximum distance that the interaction can move before the gesture fails.
- [init(minimumDuration:maximumDistance:inputKinds:)](<longpressgesture/init(minimumduration_maximumdistance_inputkinds_).md>) — Creates a long-press gesture with a minimum duration, a maximum distance, and the input kinds the gesture recognizes. _(beta)_
- [minimumDuration](longpressgesture/minimumduration.md) — The minimum duration of the long press that must elapse before the gesture succeeds.
- [maximumDistance](longpressgesture/maximumdistance.md) — The maximum distance that the long press can move before the gesture fails.

## See Also

### Recognizing long-press gestures

- [onLongPressGesture(minimumDuration:maximumDistance:perform:onPressingChanged:)](<view/onlongpressgesture(minimumduration_maximumdistance_perform_onpressingchanged_).md>) — Adds an action to perform when this view recognizes a long press gesture.
- [onLongPressGesture(minimumDuration:maximumDistance:inputKinds:perform:onPressingChanged:)](<view/onlongpressgesture(minimumduration_maximumdistance_inputkinds_perform_onpressingchanged_).md>) — Adds an action to perform when this view recognizes a long press gesture. _(beta)_
- [onLongPressGesture(minimumDuration:perform:onPressingChanged:)](<view/onlongpressgesture(minimumduration_perform_onpressingchanged_).md>) — Adds an action to perform when this view recognizes a long press gesture.
- [onLongTouchGesture(minimumDuration:perform:onTouchingChanged:)](<view/onlongtouchgesture(minimumduration_perform_ontouchingchanged_).md>) — Adds an action to perform when this view recognizes a remote long touch gesture. A long touch gesture is when the finger is on the remote touch surface without actually pressing.
