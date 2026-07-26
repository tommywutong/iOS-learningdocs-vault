---
title: 'accessibilityAction(_:intent:)'
framework: AppIntents
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/modifiedcontent/accessibilityaction(_:intent:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibilityaction(_:intent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibilityaction%28_%3Aintent%3A%29.json'
content_hash: 'sha256:ae72cebf415958b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibilityAction(_:intent:)

<sub>Instance Method</sub>

Adds an accessibility action representing `actionKind` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityAction<I>(_ actionKind: AccessibilityActionKind = .default, intent: I) -> ModifiedContent<Content, Modifier> where I : AppIntent
```
