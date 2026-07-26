---
title: 'accessibilityLabel(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/text/accessibilitylabel(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/text/accessibilitylabel(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/accessibilitylabel%28_%3A%29.json'
content_hash: 'sha256:2f0ee444895b5d00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# accessibilityLabel(_:)

<sub>Instance Method</sub>

Adds a label to the view that describes its contents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func accessibilityLabel(_ label: LocalizedStringResource) -> Text
```

## Parameters

- `label` — The string resource for the alternative accessibility label.

## Discussion

Use this method to provide an alternative accessibility label to the text that is displayed. For example, you can give an alternate label to a navigation title:

```swift
var body: some View {
    NavigationView {
        ContentView()
            .navigationTitle(Text("􀈤").accessibilityLabel("Inbox"))
    }
}
```

## See Also

### Providing accessibility information

- [accessibilityHeading(_:)](<accessibilityheading(__).md>) — Sets the accessibility level of this heading.
- [accessibilityTextContentType(_:)](<accessibilitytextcontenttype(__).md>) — Sets an accessibility text content type.
