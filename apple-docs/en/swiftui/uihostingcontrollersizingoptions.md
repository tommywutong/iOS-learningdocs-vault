---
title: UIHostingControllerSizingOptions
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uihostingcontrollersizingoptions
source_url: 'https://developer.apple.com/documentation/swiftui/uihostingcontrollersizingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uihostingcontrollersizingoptions.json'
content_hash: 'sha256:14a94f0b28b1d178'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# UIHostingControllerSizingOptions

<sub>Structure</sub>

Options for how a hosting controller tracks its content’s size.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UIHostingControllerSizingOptions
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Getting sizing options

- [intrinsicContentSize](uihostingcontrollersizingoptions/intrinsiccontentsize.md) — The hosting controller’s view automatically invalidate its intrinsic content size when its ideal size changes.
- [preferredContentSize](uihostingcontrollersizingoptions/preferredcontentsize.md) — The hosting controller tracks its content’s ideal size in its preferred content size.

### Creating a sizing option

- [init(rawValue:)](<uihostingcontrollersizingoptions/init(rawvalue_).md>) — Creates a new option set from a raw value.
- [rawValue](uihostingcontrollersizingoptions/rawvalue.md) — The raw value.

## See Also

### Displaying SwiftUI views in UIKit

- [Using SwiftUI with UIKit](../uikit/using-swiftui-with-uikit.md) — Learn how to incorporate SwiftUI views into a UIKit app.
- [Unifying your app’s animations](unifying-your-app-s-animations.md) — Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [UIHostingController](uihostingcontroller.md) — A UIKit view controller that manages a SwiftUI view hierarchy.
- [UIHostingConfiguration](uihostingconfiguration.md) — A content configuration suitable for hosting a hierarchy of SwiftUI views.
- [UIHostingSceneDelegate](uihostingscenedelegate.md) — Extends `UIKit/UISceneDelegate` to bridge SwiftUI scenes.
