---
title: 'accessibility(identifier:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/modifiedcontent/accessibility(identifier:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibility(identifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibility%28identifier%3A%29.json'
content_hash: 'sha256:be7a021910e9f662'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibility(identifier:)

<sub>Instance Method</sub>

Uses the specified string to identify the view.

> [!warning] Deprecated
> Use [accessibilityIdentifier(_:)](<accessibilityidentifier(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibility(identifier: String) -> ModifiedContent<Content, Modifier>
```

## Discussion

Use this value for testing. It isn’t visible to the user.
