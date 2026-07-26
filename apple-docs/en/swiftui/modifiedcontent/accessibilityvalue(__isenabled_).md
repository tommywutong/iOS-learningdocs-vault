---
title: 'accessibilityValue(_:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/modifiedcontent/accessibilityvalue(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibilityvalue(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibilityvalue%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:b98dc0600349fb4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibilityValue(_:isEnabled:)

<sub>Instance Method</sub>

Adds a textual description of the value that the view contains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func accessibilityValue(_ valueResource: LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Content, Modifier>
```

## Parameters

- `valueResource` — The accessibility value to apply.

- `isEnabled` — If true the accessibility value is applied; otherwise the accessibility value is unchanged.

## Discussion

Use this method to describe the value represented by a view, but only if that’s different than the view’s label. For example, for a slider that you label as “Volume” using accessibilityLabel(), you can provide the current volume setting, like “60%”, using accessibilityValue().
