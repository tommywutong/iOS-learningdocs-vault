---
title: 'allowsWindowActivationEvents(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/allowswindowactivationevents(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/allowswindowactivationevents(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/allowswindowactivationevents%28_%3A%29.json'
content_hash: 'sha256:10bdf921ebd28182'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# allowsWindowActivationEvents(_:)

<sub>Instance Method</sub>

Configures whether gestures in this view hierarchy can handle events that activate the containing window.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func allowsWindowActivationEvents(_ value: Bool?) -> some View

```

## Parameters

- `value` — A Boolean value that indicates whether gestures in this view hierarchy can handle events that activate the containing window. If `nil`, or if the modifier is not present, the behavior will be inherited from the view’s ancestors.

## Discussion

Views higher in the hierarchy can override the value you set on this view. In the following example, the tap gesture on the `Rectangle` won’t handle events that activate the containing window because the outer `allowsWindowActivationEvents(_:)` view modifier overrides the inner one:

```swift
HStack {
    Rectangle()
        .onTapGesture { ... }
        .allowsWindowActivationEvents()
}
.allowsWindowActivationEvents(false)
```

> [!note] Note
> It’s only possible to disallow handling events that activate the containing window for views that allow it by default or that inherit this behavior from their ancestors. Views that explicitly already disallow this functionality can’t have it turned on.

> [!note] Note
> Prefer using [allowsWindowActivationEvents()](<allowswindowactivationevents().md>) if the parameter is always `true` and it never changes.
