---
title: 'breakthroughEffect(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/breakthrougheffect(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/breakthrougheffect(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/breakthrougheffect%28_%3A%29.json'
content_hash: 'sha256:a777cd4ff201e055'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# breakthroughEffect(_:)

<sub>Instance Method</sub>

Ensures that the view is always visible to the user, even when other content is occluding it, like 3D models.

<sub>visionOS</sub>

```swift
nonisolated func breakthroughEffect(_ effect: BreakthroughEffect) -> some View

```

## Parameters

- `effect` — The type of effect to apply when the view is occluded by other content.

## Discussion

Breakthrough is an effect allowing elements to be visible to the user even when other app content (3D models, UI elements) is positioned in front. The way the element breaks through content in front depends on the chosen [BreakthroughEffect](../breakthrougheffect.md).

This modifier can be used in a number of scenarios, including ornaments and `RealityView` attachments to have them break through in their entirety.

### Regular Elements

To have SwiftUI element break through content in front, apply the `breakthroughEffect` modifier directly to the View:

```swift
ResizeHandle()
    .breakthroughEffect(.subtle)
```

### Ornaments

When applied to the whole content of an ornament, the ornament (including its background) will break through content in front:

```swift
Text("A view with an ornament")
    .ornament(attachmentAnchor: .scene(.bottom)) {
        OrnamentContent()
            .glassBackgroundEffect()
            .breakthroughEffect(.prominent)
    }
```

### RealityView Attachments

Similarly, a `RealityView` `Attachment` can break through other entities in the RealityView, including the entity it is attached to:

```swift
Attachment(id: "example") {
    AttachmentContent()
        .breakthroughEffect(.subtle)
}
```

### Presentations

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

This also applies to RealityKit presentations using `RealityKit/PresentationComponent`

## See Also

### Configuring passthrough

- [preferredSurroundingsEffect(_:)](<preferredsurroundingseffect(__).md>) — Applies an effect to passthrough video.
- [SurroundingsEffect](../surroundingseffect.md) — Effects that the system can apply to passthrough video.
- [BreakthroughEffect](../breakthrougheffect.md)
