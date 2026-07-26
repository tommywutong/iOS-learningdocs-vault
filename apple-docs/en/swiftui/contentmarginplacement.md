---
title: ContentMarginPlacement
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/contentmarginplacement
source_url: 'https://developer.apple.com/documentation/swiftui/contentmarginplacement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contentmarginplacement.json'
content_hash: 'sha256:c7d40446794aa88b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ContentMarginPlacement

<sub>Structure</sub>

The placement of margins.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ContentMarginPlacement
```

## Overview

Different views can support customizating margins that appear in different parts of that view. Use values of this type to customize those margins of a particular placement.

For example, use a [scrollIndicators](contentmarginplacement/scrollindicators.md) placement to customize the margins of scrollable view’s scroll indicators separately from the margins of a scrollable view’s content.

Use this type with the [contentMargins(_:for:)](<view/contentmargins(__for_).md>) modifier.

## Topics

### Getting the placement

- [automatic](contentmarginplacement/automatic.md) — The automatic placement.
- [scrollContent](contentmarginplacement/scrollcontent.md) — The scroll content placement.
- [scrollIndicators](contentmarginplacement/scrollindicators.md) — The scroll indicators placement.

## See Also

### Setting margins

- [contentMargins(_:for:)](<view/contentmargins(__for_).md>) — Configures the content margin for a provided placement.
- [contentMargins(_:_:for:)](<view/contentmargins(____for_).md>) — Configures the content margin for a provided placement.
