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
doc_path: '/documentation/swiftui/tabcontent/accessibilityvalue(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabcontent/accessibilityvalue(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabcontent/accessibilityvalue%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:58d20184776f196c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabContent](../tabcontent.md)

# accessibilityValue(_:isEnabled:)

<sub>Instance Method</sub>

Adds a textual description of the value that the tab contains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func accessibilityValue(_ valueResource: LocalizedStringResource, isEnabled: Bool = true) -> some TabContent<Self.TabValue>

```

## Parameters

- `valueResource` — The accessibility value to apply.

- `isEnabled` — If true the accessibility value is applied; otherwise the accessibility value is unchanged.

## Discussion

Use this method to describe the value represented by a tab, but only if that’s different than the tab’s label such as when an icon represent information about a tab.

```swift
var body: some View {
    TabView {
        Tab {
            MessagesView()
        } label: {
            Text("Messages")
        }
        .badge(30)
        .accessibilityValue("30 Unread")
    }
}
```

## See Also

### Configuring tab accessibility

- [accessibilityHint(_:isEnabled:)](<accessibilityhint(__isenabled_).md>) — Communicates to the user what happens after selecting the tab.
- [accessibilityIdentifier(_:isEnabled:)](<accessibilityidentifier(__isenabled_).md>) — Uses the string you specify to identify the view. Use this value for testing. It isn’t visible to the user.
- [accessibilityInputLabels(_:isEnabled:)](<accessibilityinputlabels(__isenabled_).md>) — Sets alternate input labels with which users identify a tab.
- [accessibilityLabel(_:isEnabled:)](<accessibilitylabel(__isenabled_).md>) — Adds a label to the tab that describes its contents.
