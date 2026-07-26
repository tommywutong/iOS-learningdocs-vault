---
title: 'right(columns:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/oslogstringalignment/right(columns:)'
source_url: 'https://developer.apple.com/documentation/os/oslogstringalignment/right(columns:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogstringalignment/right%28columns%3A%29.json'
content_hash: 'sha256:4c83d3a23870607a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogStringAlignment](../oslogstringalignment.md)

# right(columns:)

<sub>Type Method</sub>

Aligns the value on the right side of a column with the specified width.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func right(columns: @autoclosure @escaping () -> Int) -> OSLogStringAlignment
```

## Parameters

- `columns` — The width of the item in characters.

## Return Value

A string-alignment structure with the specified value.

## See Also

### Getting a Custom String Alignment

- [left(columns:)](<left(columns_).md>) — Aligns the value on the left side of a column with the specified width.
