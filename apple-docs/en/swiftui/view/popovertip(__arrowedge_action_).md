---
title: 'popoverTip(_:arrowEdge:action:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 13.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/popovertip(_:arrowedge:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/popovertip(_:arrowedge:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/popovertip%28_%3Aarrowedge%3Aaction%3A%29.json'
content_hash: 'sha256:3f50f34a625687d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# popoverTip(_:arrowEdge:action:)

<sub>Instance Method</sub>

Presents a popover tip on the modified view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@preconcurrency nonisolated func popoverTip(_ tip: (any Tip)?, arrowEdge: Edge? = nil, action: @escaping @MainActor @Sendable (Tips.Action) -> Void = { _ in }) -> some View

```

## Parameters

- `tip` — The tip to display.

- `arrowEdge` — The edge of the attachmentAnchor that defines the location of the popover’s arrow. By default, the system will choose the best orientation of the popover’s arrow.

- `action` — The action to perform when the user triggers a tip’s button.

### Discussion

Use this modifier to present a tip as a popover on an existing view when the tip becomes eligible for display.

```swift
import SwiftUI
import TipKit

// Define your tip's content.
struct SampleTip: Tip {
    var title: Text {
        Text("Save as a Favorite")
    }

    var message: Text? {
        Text("Your favorite backyards always appear at the top of the list.")
    }

    var image: Image? {
        Image(systemName: "star")
    }
}

struct SampleView: View {
    // Create an instance of your tip.
    var tip = SampleTip()

    var body: some View {
        VStack {
            // Add `.popoverTip` to the view you want to modify.
            // Tips.configure(options:) must be called before your tip will be eligible for display.
            Image(systemName: "star")
                .popoverTip(tip)
        }
    }
}
```

## See Also

### Providing tips

- [popoverTip(_:isPresented:attachmentAnchor:arrowEdge:action:)](<popovertip(__ispresented_attachmentanchor_arrowedge_action_).md>) — Presents a popover tip on the modified view.
- [popoverTip(_:isPresented:attachmentAnchor:arrowEdges:action:)](<popovertip(__ispresented_attachmentanchor_arrowedges_action_).md>) — Presents a popover tip on the modified view.
- [tipAnchor(_:)](<tipanchor(__).md>) — Sets a value for the specified tip anchor to be used to anchor a tip view to the `.bounds` of the view.
- [tipBackground(_:)](<tipbackground(__).md>) — Sets the tip’s view background to a style.
- [tipBackgroundInteraction(_:)](<tipbackgroundinteraction(__).md>) — Controls whether people can interact with the view behind a presented tip.
- [tipCornerRadius(_:antialiased:)](<tipcornerradius(__antialiased_).md>) — Sets the corner radius for an inline tip view.
- [tipImageSize(_:)](<tipimagesize(__).md>) — Sets the size for a tip’s image.
- [tipViewStyle(_:)](<tipviewstyle(__).md>) — Sets the given style for TipView within the view hierarchy.
- [tipImageStyle(_:)](<tipimagestyle(__).md>) — Sets the style for a tip’s image.
- [tipImageStyle(_:_:)](<tipimagestyle(____).md>) — Sets the style for a tip’s image.
- [tipImageStyle(_:_:_:)](<tipimagestyle(______).md>) — Sets the style for a tip’s image.
