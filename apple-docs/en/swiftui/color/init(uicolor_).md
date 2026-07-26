---
title: 'init(uiColor:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/color/init(uicolor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/color/init(uicolor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/init%28uicolor%3A%29.json'
content_hash: 'sha256:e8a0f253fcc6987e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Color](../color.md)

# init(uiColor:)

<sub>Initializer</sub>

Creates a color from a UIKit color.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(uiColor: UIColor)
```

## Discussion

Use this method to create a SwiftUI color from a [UIColor](../../uikit/uicolor.md) instance. The new color preserves the adaptability of the original. For example, you can create a rectangle using [link](../../uikit/uicolor/link.md) to see how the shade adjusts to match the user’s system settings:

```swift
struct Box: View {
    var body: some View {
        Color(uiColor: .link)
            .frame(width: 200, height: 100)
    }
}
```

The `Box` view defined above automatically changes its appearance when the user turns on Dark Mode. With the light and dark appearances placed side by side, you can see the subtle difference in shades:

![A side by side comparison of light and dark appearance screenshots of](../../../../attachments/599bf4a06d3976ad099cbd7337fdc258/Color-init-3@2x.png)

> [!note] Note
> Use this initializer only if you need to convert an existing [UIColor](../../uikit/uicolor.md) to a SwiftUI color. Otherwise, create a SwiftUI [Color](../color.md) using an initializer like [init(_:red:green:blue:opacity:)](<init(__red_green_blue_opacity_).md>), or use a system color like [blue](../shapestyle/blue.md).

## See Also

### Creating a color from another color

- [init(nsColor:)](<init(nscolor_).md>) — Creates a color from an AppKit color.
- [init(cgColor:)](<init(cgcolor_).md>) — Creates a color from a Core Graphics color.
