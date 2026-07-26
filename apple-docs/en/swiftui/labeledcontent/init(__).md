---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/labeledcontent/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/labeledcontent/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/labeledcontent/init%28_%3A%29.json'
content_hash: 'sha256:3078e38749193b6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LabeledContent](../labeledcontent.md)

# init(_:)

<sub>Initializer</sub>

Creates labeled content based on a labeled content style configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ configuration: LabeledContentStyleConfiguration)
```

## Parameters

- `configuration` — The properties of the labeled content

## Discussion

You can use this initializer within the [makeBody(configuration:)](<../labeledcontentstyle/makebody(configuration_).md>) method of a [LabeledContentStyle](../labeledcontentstyle.md) to create a labeled content instance. This is useful for custom styles that only modify the current style, as opposed to implementing a brand new style.

For example, the following style adds a red border around the labeled content, but otherwise preserves the current style:

```swift
struct RedBorderLabeledContentStyle: LabeledContentStyle {
    func makeBody(configuration: Configuration) -> some View {
        LabeledContent(configuration)
            .border(.red)
    }
}
```

## See Also

### Creating labeled content

- [init(_:content:)](<init(__content_).md>) — Creates a labeled view that generates its label from a localized string key.
- [init(content:label:)](<init(content_label_).md>) — Creates a standard labeled element, with a view that conveys the value of the element and a label.
- [init(_:value:)](<init(__value_).md>) — Creates a labeled informational view.
- [init(_:value:format:)](<init(__value_format_).md>) — Creates a labeled informational view from a formatted value.
