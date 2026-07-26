---
title: 'accessibility(selectionIdentifier:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+（1.0 起废弃）, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/modifiedcontent/accessibility(selectionidentifier:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibility(selectionidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibility%28selectionidentifier%3A%29.json'
content_hash: 'sha256:50d02a4a2c94237d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibility(selectionIdentifier:)

<sub>Instance Method</sub>

Sets a selection identifier for this view’s accessibility element.

> [!warning] Deprecated
> This functionality is no longer available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibility(selectionIdentifier: AnyHashable) -> ModifiedContent<Content, Modifier>
```

## Discussion

Picker uses the value to determine what node to use for the accessibility value.
