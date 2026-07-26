---
title: 'accessibilityLabel(_:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tabcontent/accessibilitylabel(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabcontent/accessibilitylabel(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabcontent/accessibilitylabel%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:415f69a324eb259e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabContent](../tabcontent.md)

# accessibilityLabel(_:isEnabled:)

<sub>Instance Method</sub>

Adds a label to the tab that describes its contents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func accessibilityLabel(_ label: LocalizedStringResource, isEnabled: Bool = true) -> some TabContent<Self.TabValue>

```

## Parameters

- `label` — The accessibility label to apply.

- `isEnabled` — If true the accessibility label is applied; otherwise the accessibility label is unchanged.

## Discussion

Use this method to provide an accessibility label for a tab that contains content like an icon. Don’t include text in the label that repeats information that users already have. For example, don’t use the label “Library tab” because a tab already has a trait that identifies it as a tab.

```swift
var body: some View {
    TabView {
        Tab {
            FavoritesView()
        } label: {
            Image(systemName: "star.fill")
        }
        .accessibilityLabel("Favorites")
    }
}
```

## See Also

### Configuring tab accessibility

- [accessibilityHint(_:isEnabled:)](<accessibilityhint(__isenabled_).md>) — Communicates to the user what happens after selecting the tab.
- [accessibilityIdentifier(_:isEnabled:)](<accessibilityidentifier(__isenabled_).md>) — Uses the string you specify to identify the view. Use this value for testing. It isn’t visible to the user.
- [accessibilityInputLabels(_:isEnabled:)](<accessibilityinputlabels(__isenabled_).md>) — Sets alternate input labels with which users identify a tab.
- [accessibilityValue(_:isEnabled:)](<accessibilityvalue(__isenabled_).md>) — Adds a textual description of the value that the tab contains.
