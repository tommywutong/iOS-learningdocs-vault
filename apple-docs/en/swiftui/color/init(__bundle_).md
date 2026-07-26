---
title: 'init(_:bundle:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/color/init(_:bundle:)'
source_url: 'https://developer.apple.com/documentation/swiftui/color/init(_:bundle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/init%28_%3Abundle%3A%29.json'
content_hash: 'sha256:505f840150b5e91f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Color](../color.md)

# init(_:bundle:)

<sub>Initializer</sub>

Creates a color from a color set that you indicate by name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ name: String, bundle: Bundle? = nil)
```

## Parameters

- `name` — The name of the color resource to look up.

- `bundle` — The bundle in which to search for the color resource. If you don’t indicate a bundle, the initializer looks in your app’s main bundle by default.

## Discussion

Use this initializer to load a color from a color set stored in an Asset Catalog. The system determines which color within the set to use based on the environment at render time. For example, you can provide light and dark versions for background and foreground colors:

![A screenshot of color sets for foreground and background colors,](../../../../attachments/8be673759199dc3fa229fc09e8bb0455/Color-init-1@2x.png)

You can then instantiate colors by referencing the names of the assets:

```swift
struct Hello: View {
    var body: some View {
        ZStack {
            Color("background")
            Text("Hello, world!")
                .foregroundStyle(Color("foreground"))
        }
        .frame(width: 200, height: 100)
    }
}
```

SwiftUI renders the appropriate colors for each appearance:

![A side by side comparison of light and dark appearance screenshots](../../../../attachments/708f550b6b27799d86f6238ac6d65d5e/Color-init-2@2x.png)

## See Also

### Creating a color

- [init(_:)](<init(__).md>) — Creates a constant color with the values specified by the resolved color.
- [resolve(in:)](<resolve(in_).md>) — Evaluates this color to a resolved color given the current `context`.
