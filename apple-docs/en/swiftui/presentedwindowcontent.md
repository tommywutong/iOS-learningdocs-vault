---
title: PresentedWindowContent
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/presentedwindowcontent
source_url: 'https://developer.apple.com/documentation/swiftui/presentedwindowcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/presentedwindowcontent.json'
content_hash: 'sha256:ff46447d655af277'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PresentedWindowContent

<sub>Structure</sub>

A view that represents the content of a presented window.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated struct PresentedWindowContent<Data, Content> where Data : Decodable, Data : Encodable, Data : Hashable, Content : View
```

## Overview

You don’t create this type directly. [WindowGroup](windowgroup.md) creates values for you.

## Relationships

- **Conforms To**: [View](view.md)
