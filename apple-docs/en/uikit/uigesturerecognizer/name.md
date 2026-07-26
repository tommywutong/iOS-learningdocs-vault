---
title: name
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigesturerecognizer/name
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/name.json'
content_hash: 'sha256:7caa290d6c0cefcd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# name

<sub>Instance Property</sub>

The unique name of the gesture recognizer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var name: String? { get set }
```

## Discussion

Assign a string to this property that uniquely identifies the gesture recognizer. Use this name to distinguish one gesture recognizer from another during debugging, or to specify a relationship between gestures in SwiftUI and UIKit.

For example, you can assign a SwiftUI gesture a name when you create it using [gesture(_:name:isEnabled:)](<../../swiftui/view/gesture(__name_isenabled_).md>), as the following code shows:

```swift
// SwiftUI code
struct TapGestureView: View {
    @State private var tapLocation: CGPoint = .zero

    var tap: some Gesture {
        DragGesture(minimumDistance: 0, coordinateSpace: .local)
            .onEnded { event in
                tapLocation = event.location
            }
    }

    var body: some View {
        Text("Tap location: \(tapLocation.debugDescription)")
            .frame(width: 120, height: 120)
            .background(Color.gray)
            .gesture(tap, name: "MyTap")
    }
}
```

Then, you can use this [name](name.md) property to refer to the gesture from UIKit. For example, you might do this in your implementation of [- gestureRecognizer:shouldRequireFailureOfGestureRecognizer:](<../uigesturerecognizerdelegate/gesturerecognizer(__shouldrequirefailureof_).md>), as the following code shows:

```swift
// UIKit code
class ViewController: UIViewController, UIGestureRecognizerDelegate {  
 
    func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, 
        shouldRequireFailureOf other: UIGestureRecognizer) -> Bool {
        return other.name == "MyTap"
    }

    // ...
}
```
