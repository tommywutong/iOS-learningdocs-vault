---
title: 'invalidatableContent(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/invalidatablecontent(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/invalidatablecontent(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/invalidatablecontent%28_%3A%29.json'
content_hash: 'sha256:1c89c10e46cc09ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# invalidatableContent(_:)

<sub>Instance Method</sub>

Mark the receiver as their content might be invalidated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func invalidatableContent(_ invalidatable: Bool = true) -> some View

```

## Parameters

- `invalidatable` — Whether the receiver content might be invalidated.

## Discussion

Use this modifier to annotate views that display values that are derived from the current state of your data and might be invalidated in response of, for example, user interaction.

The view will change its appearance when [invalidated](../redactionreasons/invalidated.md) is present in the environment.

In an interactive widget a view is invalidated from the moment the user interacts with a control on the widget to the moment when a new timeline update has been presented.

## See Also

### Managing view interaction

- [disabled(_:)](<disabled(__).md>) — Adds a condition that controls whether users can interact with this view.
- [isEnabled](../environmentvalues/isenabled.md) — A Boolean value that indicates whether the view associated with this environment allows user interaction.
- [interactionActivityTrackingTag(_:)](<interactionactivitytrackingtag(__).md>) — Sets a tag that you use for tracking interactivity.
