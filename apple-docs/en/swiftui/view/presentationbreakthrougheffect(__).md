---
title: 'presentationBreakthroughEffect(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/presentationbreakthrougheffect(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/presentationbreakthrougheffect(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/presentationbreakthrougheffect%28_%3A%29.json'
content_hash: 'sha256:6f412b66b4ff9b33'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# presentationBreakthroughEffect(_:)

<sub>Instance Method</sub>

Changes the way the enclosing presentation breaks through content occluding it.

<sub>visionOS</sub>

```swift
nonisolated func presentationBreakthroughEffect(_ effect: BreakthroughEffect) -> some View

```

## Parameters

- `effect` — The type of effect to apply when a presentation element is occluded by other content.

## Discussion

Use this modifier to disable or customize a breakthrough effect for the enclosing presentation.

Breakthrough is an effect allowing elements to be visible to the user even when other app content (3D models, UI elements) is occluding it. The way the element appears depends on the chosen [BreakthroughEffect](../breakthrougheffect.md).

Most system presentations appear with a breakthrough effect by default. For these cases, you can customize the type of effect by applying the [presentationBreakthroughEffect(_:)](<presentationbreakthrougheffect(__).md>) modifier to the content of the presentation, like in the following example:

```swift
Button("Show Details") {
    isShowingDetails = true
}
.popover(isPresented: $isShowingDetails) {
    DetailsView()
        .presentationBreakthroughEffect(.prominent)
}
```

Only popovers allow breakthrough to be disabled altogether. Passing a `.none` value for a sheet has no effect.

## See Also

### Sheet and popover configuration

- [interactiveDismissDisabled(_:)](<interactivedismissdisabled(__).md>) — Conditionally prevents interactive dismissal of presentations like popovers, sheets, and inspectors.
- [presentationDetents(_:)](<presentationdetents(__).md>) — Sets the available detents for the enclosing sheet.
- [presentationDetents(_:selection:)](<presentationdetents(__selection_).md>) — Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [presentationDragIndicator(_:)](<presentationdragindicator(__).md>) — Sets the visibility of the drag indicator on top of a sheet.
- [presentationBackground(_:)](<presentationbackground(__).md>) — Sets the presentation background of the enclosing sheet using a shape style.
- [presentationBackground(alignment:content:)](<presentationbackground(alignment_content_).md>) — Sets the presentation background of the enclosing sheet to a custom view.
- [presentationBackgroundInteraction(_:)](<presentationbackgroundinteraction(__).md>) — Controls whether people can interact with the view behind a presentation.
- [presentationCompactAdaptation(horizontal:vertical:)](<presentationcompactadaptation(horizontal_vertical_).md>) — Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [presentationCompactAdaptation(_:)](<presentationcompactadaptation(__).md>) — Specifies how to adapt a presentation to compact size classes.
- [presentationContentInteraction(_:)](<presentationcontentinteraction(__).md>) — Configures the behavior of swipe gestures on a presentation.
- [presentationCornerRadius(_:)](<presentationcornerradius(__).md>) — Requests that the presentation have a specific corner radius.
- [presentationSizing(_:)](<presentationsizing(__).md>) — Sets the sizing of the containing presentation.
- [presentationPreventsAppTermination(_:)](<presentationpreventsapptermination(__).md>) — Whether a presentation prevents the app from being terminated/quit by the system or app termination menu item.
