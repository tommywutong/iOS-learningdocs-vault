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
doc_path: '/documentation/swiftui/tabcontent/accessibilityidentifier(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabcontent/accessibilityidentifier(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabcontent/accessibilityidentifier%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:e4d14302da98afec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabContent](../tabcontent.md)

# accessibilityIdentifier(_:isEnabled:)

<sub>Instance Method</sub>

Uses the string you specify to identify the view. Use this value for testing. It isn’t visible to the user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityIdentifier(_ identifier: String, isEnabled: Bool = true) -> some TabContent<Self.TabValue>

```

## Parameters

- `identifier` — The accessibility identifier to apply.

- `isEnabled` — If true the accessibility identifier is applied; otherwise the accessibility identifier is unchanged.

## See Also

### Configuring tab accessibility

- [accessibilityHint(_:isEnabled:)](<accessibilityhint(__isenabled_).md>) — Communicates to the user what happens after selecting the tab.
- [accessibilityInputLabels(_:isEnabled:)](<accessibilityinputlabels(__isenabled_).md>) — Sets alternate input labels with which users identify a tab.
- [accessibilityLabel(_:isEnabled:)](<accessibilitylabel(__isenabled_).md>) — Adds a label to the tab that describes its contents.
- [accessibilityValue(_:isEnabled:)](<accessibilityvalue(__isenabled_).md>) — Adds a textual description of the value that the tab contains.
