---
title: Creating dynamic colors in SwiftUI
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2023/07/11/creating-dynamic-colors-in-swiftui/'
original_language: en
published: 2023-07-11
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1efceedc6ecccc27'
translated: false
---

> 原文：[Creating dynamic colors in SwiftUI](https://www.jessesquires.com/blog/2023/07/11/creating-dynamic-colors-in-swiftui/)　·　Jesse Squires

Beginning with the introduction of [dark mode](https://www.jessesquires.com/blog/tags/dark-mode/) in iOS 13, colors in iOS are now (optionally) dynamic. You can provide light and dark variants for all colors in your app. However, I was surprised to find that SwiftUI — which also made its first appearance on the platform in iOS 13 — _still_ does not provide any API for creating dynamic colors.

In UIKit, `UIColor` provides a dynamic initializer, [`init(dynamicProvider:)`](https://developer.apple.com/documentation/uikit/uicolor/3238041-init), which I [wrote about here](https://www.jessesquires.com/blog/2020/03/23/implementing-dark-mode-with-cgcolor/). AppKit provides the equivalent API for `NSColor`. Unfortunately, an equivalent API for SwiftUI’s `Color` [is missing](https://developer.apple.com/documentation/swiftui/color).

UIKit also allows you to extract a specific variant from a `UIColor` using [`resolvedColor(with:)`](https://developer.apple.com/documentation/uikit/uicolor/3238042-resolvedcolor), which will return either the dark or light variant based on the provided trait collection. Again, AppKit provides the equivalent API for `NSColor`. Surprisingly, in iOS 17 SwiftUI’s `Color` gained a new API for color resolution, [`resolve(in:)`](https://developer.apple.com/documentation/swiftui/color/resolve(in:)), which returns the resolved color value based on the provided `EnvironmentValues`.

The result is that SwiftUI’s `Color` API is oddly incomplete. `Color` has no equivalent API to `UIColor.init(dynamicProvider:)`, but _it does_ provide its own version of `UIColor.resolvedColor(with:)`. This is not only inconvenient, but very confusing.

Of course, you can use Asset Catalogs to define dynamic colors and reference them in SwiftUI, and Xcode 15 [makes that easier](https://nilcoalescing.com/blog/Xcode15Assets/)! But if you need to programmatically initialize dynamic colors in SwiftUI, you are out of luck due to this glaring omission. Instead, you must resort to UIKit and AppKit. So, here’s a helpful extension that accommodates the missing API for all platforms.

```
import SwiftUI

#if canImport(AppKit)
import AppKit
#endif

#if canImport(UIKit)
import UIKit
#endif

extension Color {
    init(light: Color, dark: Color) {
        #if canImport(UIKit)
        self.init(light: UIColor(light), dark: UIColor(dark))
        #else
        self.init(light: NSColor(light), dark: NSColor(dark))
        #endif
    }

    #if canImport(UIKit)
    init(light: UIColor, dark: UIColor) {
        #if os(watchOS)
        // watchOS does not support light mode / dark mode
        // Per Apple HIG, prefer dark-style interfaces
        self.init(uiColor: dark)
        #else
        self.init(uiColor: UIColor(dynamicProvider: { traits in
            switch traits.userInterfaceStyle {
            case .light, .unspecified:
                return light

            case .dark:
                return dark

            @unknown default:
                assertionFailure("Unknown userInterfaceStyle: \(traits.userInterfaceStyle)")
                return light
            }
        }))
        #endif
    }
    #endif

    #if canImport(AppKit)
    init(light: NSColor, dark: NSColor) {
        self.init(nsColor: NSColor(name: nil, dynamicProvider: { appearance in
            switch appearance.name {
            case .aqua,
                 .vibrantLight,
                 .accessibilityHighContrastAqua,
                 .accessibilityHighContrastVibrantLight:
                return light

            case .darkAqua,
                 .vibrantDark,
                 .accessibilityHighContrastDarkAqua,
                 .accessibilityHighContrastVibrantDark:
                return dark

            default:
                assertionFailure("Unknown appearance: \(appearance.name)")
                return light
            }
        }))
    }
    #endif
}
```

And now you can initialize a SwiftUI `Color` programmatically with a light and dark variant.

```
let textColor = Color(light: someColor, dark: anotherColor)
```
