---
title: 'init(base:state:body:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/gesturestategesture/init(base:state:body:)'
source_url: 'https://developer.apple.com/documentation/swiftui/gesturestategesture/init(base:state:body:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gesturestategesture/init%28base%3Astate%3Abody%3A%29.json'
content_hash: 'sha256:67603d855b4cbe6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GestureStateGesture](../gesturestategesture.md)

# init(base:state:body:)

<sub>Initializer</sub>

Creates a new gesture that’s the result of an ongoing gesture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(base: Base, state: GestureState<State>, body: @escaping (GestureStateGesture<Base, State>.Value, inout State, inout Transaction) -> Void)
```

## Parameters

- `base` — The originating gesture.

- `state` — The wrapped value of a [GestureState](../gesturestate.md) property.

- `body` — The callback that SwiftUI invokes as the gesture’s value changes.

## See Also

### Creating an in-progress gesture

- [base](base.md) — The originating gesture.
- [state](state.md) — A value that changes as the user performs the gesture.
