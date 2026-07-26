---
title: 'init(_:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/labeledcontent/init(_:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/labeledcontent/init(_:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/labeledcontent/init%28_%3Acontent%3A%29.json'
content_hash: 'sha256:f28417d133404c43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LabeledContent](../labeledcontent.md)

# init(_:content:)

<sub>Initializer</sub>

Creates a labeled view that generates its label from a localized string key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ titleKey: LocalizedStringKey, @ContentBuilder content: () -> Content)
```

## Parameters

- `titleKey` — The key for the view’s localized title, that describes the purpose of the view.

- `content` — The value content being labeled.

## Discussion

This initializer creates a [Text](../text.md) label on your behalf, and treats the localized key similar to [init(_:tableName:bundle:comment:)](<../text/init(__tablename_bundle_comment_).md>). See `Text` for more information about localizing strings.

## See Also

### Creating labeled content

- [init(content:label:)](<init(content_label_).md>) — Creates a standard labeled element, with a view that conveys the value of the element and a label.
- [init(_:value:)](<init(__value_).md>) — Creates a labeled informational view.
- [init(_:value:format:)](<init(__value_format_).md>) — Creates a labeled informational view from a formatted value.
- [init(_:)](<init(__).md>) — Creates labeled content based on a labeled content style configuration.
