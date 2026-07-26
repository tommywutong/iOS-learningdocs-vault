---
title: 'accessibility(inputLabels:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/modifiedcontent/accessibility(inputlabels:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibility(inputlabels:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibility%28inputlabels%3A%29.json'
content_hash: 'sha256:7e9a385b4f4ccc84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibility(inputLabels:)

<sub>Instance Method</sub>

Sets alternate input labels with which users identify a view.

> [!warning] Deprecated
> Use [accessibilityInputLabels(_:)](<accessibilityinputlabels(__)-21dwf.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibility(inputLabels: [Text]) -> ModifiedContent<Content, Modifier>
```

## Parameters

- `inputLabels` — An array of [Text](../text.md) elements to use as input labels.

## Discussion

Provide labels in descending order of importance. Voice Control and Full Keyboard Access use the input labels.

> [!note] Note
> If you don’t specify any input labels, the user can still refer to the view using the accessibility label that you add with the `accessibility(label:)` modifier.
