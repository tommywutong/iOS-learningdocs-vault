---
title: AutomaticNavigationSplitViewStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/automaticnavigationsplitviewstyle
source_url: 'https://developer.apple.com/documentation/swiftui/automaticnavigationsplitviewstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/automaticnavigationsplitviewstyle.json'
content_hash: 'sha256:ac2e80c705dabe9a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AutomaticNavigationSplitViewStyle

<sub>Structure</sub>

A navigation split style that resolves its appearance automatically based on the current context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct AutomaticNavigationSplitViewStyle
```

## Overview

Use [automatic](navigationsplitviewstyle/automatic.md) to construct this style.

## Relationships

- **Conforms To**: [NavigationSplitViewStyle](navigationsplitviewstyle.md)

## Topics

### Creating the navigation split view style

- [init()](<automaticnavigationsplitviewstyle/init().md>) — Creates an instance of the automatic navigation split view style.

## See Also

### Supporting types

- [BalancedNavigationSplitViewStyle](balancednavigationsplitviewstyle.md) — A navigation split style that reduces the size of the detail content to make room when showing the leading column or columns.
- [ProminentDetailNavigationSplitViewStyle](prominentdetailnavigationsplitviewstyle.md) — A navigation split style that attempts to maintain the size of the detail content when hiding or showing the leading columns.
- [NavigationSplitViewStyleConfiguration](navigationsplitviewstyleconfiguration.md) — The properties of a navigation split view instance.
