---
title: 'customAttribute(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/text/customattribute(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/text/customattribute(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/customattribute%28_%3A%29.json'
content_hash: 'sha256:14647084cd73ea24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# customAttribute(_:)

<sub>Instance Method</sub>

Adds a custom attribute to the text view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func customAttribute<T>(_ value: T) -> Text where T : TextAttribute
```

## Parameters

- `value` — The attribute to attach.

## Return Value

A version of the text view with `value` attached.

## Discussion

Only one attribute of each type may be attached to each text view, with inner attributes taking precedence.
