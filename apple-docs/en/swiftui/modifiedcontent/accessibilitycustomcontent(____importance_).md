---
title: 'accessibilityCustomContent(_:_:importance:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/modifiedcontent/accessibilitycustomcontent(_:_:importance:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibilitycustomcontent(_:_:importance:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibilitycustomcontent%28_%3A_%3Aimportance%3A%29.json'
content_hash: 'sha256:f415efa6c9076014'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibilityCustomContent(_:_:importance:)

<sub>Instance Method</sub>

Add additional accessibility information to the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func accessibilityCustomContent(_ key: AccessibilityCustomContentKey, _ valueResource: LocalizedStringResource, importance: AXCustomContent.Importance = .default) -> ModifiedContent<Content, Modifier>
```

## Parameters

- `key` — Key used to specify the identifier and label of the of the additional accessibility information entry.

- `valueResource` — Text resource for the additional accessibility information. For example: “landscape.” A value of `nil` will remove any entry of additional information added earlier for any `key` with the same identifier.

- `importance` — Importance of the accessibility information. High-importance information gets read out immediately, while default-importance information must be explicitly asked for by the user.

## Discussion

Use this method to add information you want accessibility users to be able to access about this element, beyond the basics of label, value, and hint. For example, `accessibilityCustomContent` can be used to add information about the orientation of a photograph, or the number of people found in the picture.

> [!note] Note
> Repeated calls of `accessibilityCustomContent` with `key`s having different identifiers will create new entries of additional information. Calling `accessibilityCustomContent` repeatedly with `key`s having matching identifiers will replace the previous entry.
