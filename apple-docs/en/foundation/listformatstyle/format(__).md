---
title: 'format(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/listformatstyle/format(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/listformatstyle/format(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/listformatstyle/format%28_%3A%29.json'
content_hash: 'sha256:d96711d207a8486a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ListFormatStyle](../listformatstyle.md)

# format(_:)

<sub>Instance Method</sub>

Creates a locale-aware string representation of the value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func format(_ value: Base) -> String
```

## Parameters

- `value` — The sequence of elements to format.

## Return Value

A string representation of the provided sequence.

## Discussion

The [format(_:)](<format(__).md>) instance method generates a string from the provided sequence. Once you create a style, you can use it to format similar sequences multiple times. For example:

```swift
let percentStyle = ListFormatStyle<IntegerFormatStyle.Percent, [Int]>(memberStyle: .percent)
percentStyle.format([92, 98]) // 92% and 98%
percentStyle.format([67, 72, 99]) // 67%, 72%, and 99%
```
