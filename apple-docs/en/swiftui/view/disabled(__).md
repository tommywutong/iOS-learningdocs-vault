---
title: 'disabled(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/disabled(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/disabled(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/disabled%28_%3A%29.json'
content_hash: 'sha256:d1495ec7972c4595'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# disabled(_:)

<sub>Instance Method</sub>

Adds a condition that controls whether users can interact with this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func disabled(_ disabled: Bool) -> some View

```

## Parameters

- `disabled` — A Boolean value that determines whether users can interact with this view.

## Return Value

A view that controls whether users can interact with this view.

## Discussion

The higher views in a view hierarchy can override the value you set on this view. In the following example, the button isn’t interactive because the outer `disabled(_:)` modifier overrides the inner one:

```swift
HStack {
    Button(Text("Press")) {}
    .disabled(false)
}
.disabled(true)
```

## See Also

### Managing view interaction

- [isEnabled](../environmentvalues/isenabled.md) — A Boolean value that indicates whether the view associated with this environment allows user interaction.
- [interactionActivityTrackingTag(_:)](<interactionactivitytrackingtag(__).md>) — Sets a tag that you use for tracking interactivity.
- [invalidatableContent(_:)](<invalidatablecontent(__).md>) — Mark the receiver as their content might be invalidated.
