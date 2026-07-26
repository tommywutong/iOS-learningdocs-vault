---
title: 'accessibilityTextContentType(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/modifiedcontent/accessibilitytextcontenttype(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibilitytextcontenttype(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibilitytextcontenttype%28_%3A%29.json'
content_hash: 'sha256:7aaeac9480628bae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibilityTextContentType(_:)

<sub>Instance Method</sub>

Sets an accessibility text content type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityTextContentType(_ textContentType: AccessibilityTextContentType) -> ModifiedContent<Content, Modifier>
```

## Parameters

- `textContentType` — The accessibility content type from the available [AccessibilityTextContentType](../accessibilitytextcontenttype.md) options.

## Discussion

Use this modifier to set the content type of this accessibility element. Assistive technologies can use this property to choose an appropriate way to output the text. For example, when encountering a source coding context, VoiceOver could choose to speak all punctuation.

The default content type [plain](../accessibilitytextcontenttype/plain.md).
