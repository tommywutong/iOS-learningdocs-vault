---
title: 'init(_:value:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/labeledcontent/init(_:value:)'
source_url: 'https://developer.apple.com/documentation/swiftui/labeledcontent/init(_:value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/labeledcontent/init%28_%3Avalue%3A%29.json'
content_hash: 'sha256:bb91b805da04a119'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LabeledContent](../labeledcontent.md)

# init(_:value:)

<sub>Initializer</sub>

Creates a labeled informational view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S1, S2>(_ title: S1, value: S2) where S1 : StringProtocol, S2 : StringProtocol
```

## Parameters

- `title` — A string that describes the purpose of the view.

- `value` — The value being labeled.

## Discussion

This initializer creates a [Text](../text.md) label on your behalf, and treats the title similar to [init(_:)](<../text/init(__).md>). See `Text` for more information about localizing strings.

```swift
Form {
    ForEach(person.pet) { pet in
        LabeledContent(pet.species, value: pet.name)
    }
}
```

## See Also

### Creating labeled content

- [init(_:content:)](<init(__content_).md>) — Creates a labeled view that generates its label from a localized string key.
- [init(content:label:)](<init(content_label_).md>) — Creates a standard labeled element, with a view that conveys the value of the element and a label.
- [init(_:value:format:)](<init(__value_format_).md>) — Creates a labeled informational view from a formatted value.
- [init(_:)](<init(__).md>) — Creates labeled content based on a labeled content style configuration.
