---
title: 'locale(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/formatstyle/locale(_:)-7c6hb'
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/locale(_:)-7c6hb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/locale%28_%3A%29-7c6hb.json'
content_hash: 'sha256:8b7cbe992444c9f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# locale(_:)

<sub>Instance Method</sub>

Modifies the format style to use the specified locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func locale(_ locale: Locale) -> Self
```

## Parameters

- `locale` — The locale to apply to the format style.

## Return Value

A format style modified to use the provided locale.

## Discussion

Use this format style to change the locale used by an existing format style.
