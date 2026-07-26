---
title: 'accessibilityInputLabels(_:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tabcontent/accessibilityinputlabels(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabcontent/accessibilityinputlabels(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabcontent/accessibilityinputlabels%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:3375a63bf860df0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabContent](../tabcontent.md)

# accessibilityInputLabels(_:isEnabled:)

<sub>Instance Method</sub>

Sets alternate input labels with which users identify a tab.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityInputLabels(_ inputLabelKeys: [LocalizedStringKey], isEnabled: Bool = true) -> some TabContent<Self.TabValue>

```

## Parameters

- `inputLabelKeys` — The accessibility input labels to apply.

- `isEnabled` — If true the accessibility input labels are applied; otherwise the accessibility input labels are unchanged.

## Discussion

Provide labels in descending order of importance. Voice Control and Full Keyboard Access use the input labels.

> [!note] Note
> If you don’t specify any input labels, the user can still refer to the tab using the accessibility label that you add with the `accessibilityLabel()` modifier.

```swift
var body: some View {
    TabView {
        Tab {
            MessagesView()
        } label: {
            Image(systemName: "mail")
        }
        .accessibilityInputLabels(["Messages", "Mail", "Conversations"])
    }
}
```

## See Also

### Configuring tab accessibility

- [accessibilityHint(_:isEnabled:)](<accessibilityhint(__isenabled_).md>) — Communicates to the user what happens after selecting the tab.
- [accessibilityIdentifier(_:isEnabled:)](<accessibilityidentifier(__isenabled_).md>) — Uses the string you specify to identify the view. Use this value for testing. It isn’t visible to the user.
- [accessibilityLabel(_:isEnabled:)](<accessibilitylabel(__isenabled_).md>) — Adds a label to the tab that describes its contents.
- [accessibilityValue(_:isEnabled:)](<accessibilityvalue(__isenabled_).md>) — Adds a textual description of the value that the tab contains.
