---
title: PreferredColorSchemeKey
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 11.0+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/preferredcolorschemekey
source_url: 'https://developer.apple.com/documentation/swiftui/preferredcolorschemekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/preferredcolorschemekey.json'
content_hash: 'sha256:df3caef0f50b5580'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PreferredColorSchemeKey

<sub>Structure</sub>

A key for specifying the preferred color scheme.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PreferredColorSchemeKey
```

## Overview

Don’t use this key directly. Instead, set a preferred color scheme for a view using the [preferredColorScheme(_:)](<view/preferredcolorscheme(__).md>) view modifier. Get the current color scheme for a view by accessing the [colorScheme](environmentvalues/colorscheme.md) value.

## Relationships

- **Conforms To**: [PreferenceKey](preferencekey.md)
