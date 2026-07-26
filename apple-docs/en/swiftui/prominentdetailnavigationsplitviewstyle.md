---
title: ProminentDetailNavigationSplitViewStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/prominentdetailnavigationsplitviewstyle
source_url: 'https://developer.apple.com/documentation/swiftui/prominentdetailnavigationsplitviewstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/prominentdetailnavigationsplitviewstyle.json'
content_hash: 'sha256:8949b85541c788d2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ProminentDetailNavigationSplitViewStyle

<sub>Structure</sub>

A navigation split style that attempts to maintain the size of the detail content when hiding or showing the leading columns.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct ProminentDetailNavigationSplitViewStyle
```

## Overview

Use [prominentDetail](navigationsplitviewstyle/prominentdetail.md) to construct this style.

## Relationships

- **Conforms To**: [NavigationSplitViewStyle](navigationsplitviewstyle.md)

## Topics

### Creating the navigation split view style

- [init()](<prominentdetailnavigationsplitviewstyle/init().md>) — Creates an instance of [ProminentDetailNavigationSplitViewStyle](prominentdetailnavigationsplitviewstyle.md).

## See Also

### Supporting types

- [AutomaticNavigationSplitViewStyle](automaticnavigationsplitviewstyle.md) — A navigation split style that resolves its appearance automatically based on the current context.
- [BalancedNavigationSplitViewStyle](balancednavigationsplitviewstyle.md) — A navigation split style that reduces the size of the detail content to make room when showing the leading column or columns.
- [NavigationSplitViewStyleConfiguration](navigationsplitviewstyleconfiguration.md) — The properties of a navigation split view instance.
