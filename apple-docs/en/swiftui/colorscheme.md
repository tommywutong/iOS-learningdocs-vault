---
title: ColorScheme
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/colorscheme
source_url: 'https://developer.apple.com/documentation/swiftui/colorscheme'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/colorscheme.json'
content_hash: 'sha256:46f67a8c0e4fb472'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ColorScheme

<sub>Enumeration</sub>

The possible color schemes, corresponding to the light and dark appearances.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ColorScheme
```

## Overview

You receive a color scheme value when you read the [colorScheme](environmentvalues/colorscheme.md) environment value. The value tells you if a light or dark appearance currently applies to the view. SwiftUI updates the value whenever the appearance changes, and redraws views that depend on the value. For example, the following [Text](text.md) view automatically updates when the user enables Dark Mode:

```swift
@Environment(\.colorScheme) private var colorScheme

var body: some View {
    Text(colorScheme == .dark ? "Dark" : "Light")
}
```

Set a preferred appearance for a particular view hierarchy to override the user’s Dark Mode setting using the [preferredColorScheme(_:)](<view/preferredcolorscheme(__).md>) view modifier.

## Relationships

- **Conforms To**: [CaseIterable](../swift/caseiterable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting color schemes

- [ColorScheme.light](colorscheme/light.md) — The color scheme that corresponds to a light appearance.
- [ColorScheme.dark](colorscheme/dark.md) — The color scheme that corresponds to a dark appearance.

### Creating a color scheme

- [init(_:)](<colorscheme/init(__).md>) — Creates a color scheme from its user interface style equivalent.

### Supporting types

- [PreferredColorSchemeKey](preferredcolorschemekey.md) — A key for specifying the preferred color scheme.

## See Also

### Detecting and requesting the light or dark appearance

- [preferredColorScheme(_:)](<view/preferredcolorscheme(__).md>) — Sets the preferred color scheme for this presentation.
- [colorScheme](environmentvalues/colorscheme.md) — The color scheme of this environment.
