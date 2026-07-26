---
title: 'accessibility(value:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/modifiedcontent/accessibility(value:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibility(value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibility%28value%3A%29.json'
content_hash: 'sha256:95369903966808ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibility(value:)

<sub>Instance Method</sub>

Adds a textual description of the value that the view contains.

> [!warning] Deprecated
> Use [accessibilityValue(_:)](<accessibilityvalue(__)-1esu1.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibility(value: Text) -> ModifiedContent<Content, Modifier>
```

## Discussion

Use this method to describe the value represented by a view, but only if that’s different than the view’s label. For example, for a slider that you label as “Volume” using [accessibility(label:)](<accessibility(label_).md>), you can provide the current volume setting, like “60%”, using [accessibility(value:)](<accessibility(value_).md>).
