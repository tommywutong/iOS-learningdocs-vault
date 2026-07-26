---
title: 'typeSelectEquivalent(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/typeselectequivalent(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/typeselectequivalent(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/typeselectequivalent%28_%3A%29.json'
content_hash: 'sha256:a75dcaeb1e71986f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# typeSelectEquivalent(_:)

<sub>Instance Method</sub>

Sets an explicit type select equivalent text in a collection, such as a list or table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func typeSelectEquivalent(_ stringKey: LocalizedStringKey) -> some View

```

## Parameters

- `stringKey` — The localized string key to use as a type select equivalent for a view in a collection.

## Discussion

By default, a type select equivalent is automatically derived from any `Text` or `TextField` content in a list or table. In the below example, type select can be used to select a person, even though no explicit value has been set.

```swift
List(people, selection: $selectedPersonID) { person in
    Label {
        Text(person.name)
    } icon: {
        person.avatar
    }
}
```

An explicit type select value should be set when there is no textual content or when a different value is desired compared to what’s displayed in the view. Explicit values also provide a more performant for complex view types. In the below example, type select is explicitly set to allow selection of views that otherwise only display an image.

```swift
List(people, selection: $selectedPersonID) { person in
    person.avatar
        .accessibilityLabel(person.name)
        .typeSelectEquivalent(person.name)
}
```

Setting an empty string value disables text selection for the view, and a value of `nil` results in the view using its default value.
