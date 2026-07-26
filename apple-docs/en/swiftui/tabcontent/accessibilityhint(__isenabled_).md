---
title: 'accessibilityHint(_:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tabcontent/accessibilityhint(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabcontent/accessibilityhint(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabcontent/accessibilityhint%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:11ea296bbc2c44f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabContent](../tabcontent.md)

# accessibilityHint(_:isEnabled:)

<sub>Instance Method</sub>

Communicates to the user what happens after selecting the tab.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func accessibilityHint(_ hint: LocalizedStringResource, isEnabled: Bool = true) -> some TabContent<Self.TabValue>

```

## Parameters

- `hint` — The accessibility hint to apply.

- `isEnabled` — If true the accessibility hint is applied; otherwise the accessibility hint is unchanged.

## Discussion

Provide a hint in the form of a brief phrase, like “Open shopping cart” or “Show downloaded attachments”.

```swift
var body: some View {
    TabView {
        Tab {
            MessagesView()
        } label: {
            Image(systemName: "play")
        }
        .accessibilityHint("Select videos to download")
    }
}
```

## See Also

### Configuring tab accessibility

- [accessibilityIdentifier(_:isEnabled:)](<accessibilityidentifier(__isenabled_).md>) — Uses the string you specify to identify the view. Use this value for testing. It isn’t visible to the user.
- [accessibilityInputLabels(_:isEnabled:)](<accessibilityinputlabels(__isenabled_).md>) — Sets alternate input labels with which users identify a tab.
- [accessibilityLabel(_:isEnabled:)](<accessibilitylabel(__isenabled_).md>) — Adds a label to the tab that describes its contents.
- [accessibilityValue(_:isEnabled:)](<accessibilityvalue(__isenabled_).md>) — Adds a textual description of the value that the tab contains.
