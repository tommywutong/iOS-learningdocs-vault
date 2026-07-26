---
title: 'init(memberStyle:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/listformatstyle/init(memberstyle:)'
source_url: 'https://developer.apple.com/documentation/foundation/listformatstyle/init(memberstyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/listformatstyle/init%28memberstyle%3A%29.json'
content_hash: 'sha256:bfd9d489ddce3ff0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ListFormatStyle](../listformatstyle.md)

# init(memberStyle:)

<sub>Initializer</sub>

Creates an instance using the provided format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(memberStyle: Style)
```

## Parameters

- `memberStyle` — The [FormatStyle](../formatstyle.md) applied to elements of the [Sequence](../../swift/sequence.md).

## Discussion

The input type of memberStyle must match the type of an element in the sequence. The output type is a string.

The following example uses a `FloatingPointFormatStyle.Descriptive` member style to spell out a list:

```swift
[-3.0, 9.0, 11.6].formatted(.list(memberStyle: .descriptive, type: .and))
// minus three, nine, and eleven point six
```
