---
title: 'accessibility(hint:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/modifiedcontent/accessibility(hint:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibility(hint:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibility%28hint%3A%29.json'
content_hash: 'sha256:9a34ebdcf44844ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibility(hint:)

<sub>Instance Method</sub>

Communicates to the user what happens after performing the view’s action.

> [!warning] Deprecated
> Use [accessibilityHint(_:)](<accessibilityhint(__)-cuvd.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibility(hint: Text) -> ModifiedContent<Content, Modifier>
```

## Discussion

Provide a hint in the form of a brief phrase, like “Purchases the item” or “Downloads the attachment”.
