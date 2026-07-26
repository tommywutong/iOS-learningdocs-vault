---
title: hidden()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view/hidden()
source_url: 'https://developer.apple.com/documentation/swiftui/view/hidden()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/hidden%28%29.json'
content_hash: 'sha256:b96e29084bada372'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# hidden()

<sub>Instance Method</sub>

Hides this view unconditionally.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func hidden() -> some View

```

## Return Value

A hidden view.

## Discussion

Hidden views are invisible and can’t receive or respond to interactions. However, they do remain in the view hierarchy and affect layout. Use this modifier if you want to include a view for layout purposes, but don’t want it to display.

```swift
HStack {
    Image(systemName: "a.circle.fill")
    Image(systemName: "b.circle.fill")
    Image(systemName: "c.circle.fill")
        .hidden()
    Image(systemName: "d.circle.fill")
}
```

The third circle takes up space, because it’s still present, but SwiftUI doesn’t draw it onscreen.

![A row of circles with the letters A, B, and D, with a gap where](../../../../attachments/d79a92c97a4a28746e19c2b6af8be481/SwiftUI-View-hidden-1@2x.png)

If you want to conditionally include a view in the view hierarchy, use an `if` statement instead:

```swift
VStack {
    HStack {
        Image(systemName: "a.circle.fill")
        Image(systemName: "b.circle.fill")
        if !isHidden {
            Image(systemName: "c.circle.fill")
        }
        Image(systemName: "d.circle.fill")
    }
    Toggle("Hide", isOn: $isHidden)
}
```

Depending on the current value of the `isHidden` state variable in the example above, controlled by the [Toggle](../toggle.md) instance, SwiftUI draws the circle or completely omits it from the layout.

![Two side by side groups of items, each composed of a toggle beneath](../../../../attachments/8866e42876ae9fb1eaf66d61c87cabb0/SwiftUI-View-hidden-2@2x.png)

## See Also

### Hiding views

- [opacity(_:)](<opacity(__).md>) — Sets the transparency of this view.
