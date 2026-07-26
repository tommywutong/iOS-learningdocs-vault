---
title: ColorSchemeContrast
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/colorschemecontrast
source_url: 'https://developer.apple.com/documentation/swiftui/colorschemecontrast'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/colorschemecontrast.json'
content_hash: 'sha256:cf0facf1a2eed8dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ColorSchemeContrast

<sub>Enumeration</sub>

The contrast between the app’s foreground and background colors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ColorSchemeContrast
```

## Overview

You receive a contrast value when you read the [colorSchemeContrast](environmentvalues/colorschemecontrast.md) environment value. The value tells you if a standard or increased contrast currently applies to the view. SwiftUI updates the value whenever the contrast changes, and redraws views that depend on the value. For example, the following [Text](text.md) view automatically updates when the user enables increased contrast:

```swift
@Environment(\.colorSchemeContrast) private var colorSchemeContrast

var body: some View {
    Text(colorSchemeContrast == .standard ? "Standard" : "Increased")
}
```

The user sets the contrast by selecting the Increase Contrast option in Accessibility \> Display in System Preferences on macOS, or Accessibility \> Display & Text Size in the Settings app on iOS. Your app can’t override the user’s choice. For information about using color and contrast in your app, see [Accessibility](../design/human-interface-guidelines/accessibility.md#Color-and-effects) in the Human Interface Guidelines.

## Relationships

- **Conforms To**: [CaseIterable](../swift/caseiterable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting contrast options

- [ColorSchemeContrast.standard](colorschemecontrast/standard.md) — SwiftUI displays views with standard contrast between the app’s foreground and background colors.
- [ColorSchemeContrast.increased](colorschemecontrast/increased.md) — SwiftUI displays views with increased contrast between the app’s foreground and background colors.

### Creating a color scheme contrast

- [init(_:)](<colorschemecontrast/init(__).md>) — Creates a contrast from its accessibility contrast equivalent.

## See Also

### Getting the color scheme contrast

- [colorSchemeContrast](environmentvalues/colorschemecontrast.md) — The contrast associated with the color scheme of this environment.
