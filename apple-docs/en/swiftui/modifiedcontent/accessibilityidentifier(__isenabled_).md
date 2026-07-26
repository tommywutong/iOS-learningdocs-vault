---
title: 'accessibilityIdentifier(_:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/modifiedcontent/accessibilityidentifier(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibilityidentifier(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibilityidentifier%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:5ec99524bde1b759'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibilityIdentifier(_:isEnabled:)

<sub>Instance Method</sub>

Uses the string you specify to identify the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityIdentifier(_ identifier: String, isEnabled: Bool) -> ModifiedContent<Content, Modifier>
```

## Parameters

- `identifier` — The accessibility identifier to apply.

- `isEnabled` — If true the accessibility identifier is applied; otherwise the accessibility identifier is unchanged.

## Discussion

Use this value for testing. It isn’t visible to the user.
