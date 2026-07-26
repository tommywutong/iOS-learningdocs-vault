---
title: NavigationSplitViewColumn
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/navigationsplitviewcolumn
source_url: 'https://developer.apple.com/documentation/swiftui/navigationsplitviewcolumn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationsplitviewcolumn.json'
content_hash: 'sha256:21ae0795a665a59c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# NavigationSplitViewColumn

<sub>Structure</sub>

A view that represents a column in a navigation split view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NavigationSplitViewColumn
```

## Overview

A [NavigationSplitView](navigationsplitview.md) collapses into a single stack in some contexts, like on iPhone or Apple Watch. Use this type with the `preferredCompactColumn` parameter to control which column of the navigation split view appears on top of the collapsed stack.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting a column

- [sidebar](navigationsplitviewcolumn/sidebar.md)
- [content](navigationsplitviewcolumn/content.md)
- [detail](navigationsplitviewcolumn/detail.md)
