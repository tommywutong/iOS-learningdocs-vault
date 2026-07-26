---
title: 'accessibilityHidden(_:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/modifiedcontent/accessibilityhidden(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibilityhidden(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibilityhidden%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:521f7b8be12aabb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibilityHidden(_:isEnabled:)

<sub>Instance Method</sub>

Specifies whether to hide this view from system accessibility features.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityHidden(_ hidden: Bool, isEnabled: Bool) -> ModifiedContent<Content, Modifier>
```

## Parameters

- `hidden` — Whether to hide this view from accessibility features.

- `isEnabled` — If true the accessibility hidden state is applied; otherwise the accessibility hidden state is unchanged.
