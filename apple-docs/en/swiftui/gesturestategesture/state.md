---
title: state
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/gesturestategesture/state
source_url: 'https://developer.apple.com/documentation/swiftui/gesturestategesture/state'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gesturestategesture/state.json'
content_hash: 'sha256:828a81f44c4c8d16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GestureStateGesture](../gesturestategesture.md)

# state

<sub>Instance Property</sub>

A value that changes as the user performs the gesture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var state: GestureState<State>
```

## See Also

### Creating an in-progress gesture

- [init(base:state:body:)](<init(base_state_body_).md>) — Creates a new gesture that’s the result of an ongoing gesture.
- [base](base.md) — The originating gesture.
