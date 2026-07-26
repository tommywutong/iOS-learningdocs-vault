---
title: 'init(_:isOn:intent:)'
framework: AppIntents
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/toggle/init(_:ison:intent:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toggle/init(_:ison:intent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toggle/init%28_%3Aison%3Aintent%3A%29.json'
content_hash: 'sha256:9d9bac4f38c9c6bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Toggle](../toggle.md)

# init(_:isOn:intent:)

<sub>Initializer</sub>

Creates a toggle performing an `AppIntent` and generates its label from a localized string key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ titleKey: LocalizedStringKey, isOn: Bool, intent: some AppIntent)
```

## Parameters

- `titleKey` — The key for the toggle’s localized title, that describes the purpose of the toggle.

- `isOn` — Whether the toggle is on or off.

- `intent` — The `AppIntent` to be performed.

## Discussion

This initializer creates a [Text](../text.md) view on your behalf, and treats the localized key similar to [init(_:tableName:bundle:comment:)](<../text/init(__tablename_bundle_comment_).md>). See `Text` for more information about localizing strings.

To initialize a toggle with a string variable, use [init(_:isOn:intent:)](<init(__ison_intent_).md>) instead.

## See Also

### Creating a toggle for an App Intent

- [init(isOn:intent:label:)](<init(ison_intent_label_).md>) — Creates a toggle performing an `AppIntent`.
