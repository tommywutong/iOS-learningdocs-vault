---
title: 'init(_:)'
framework: Core Text
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coretext/cttextalignment/init(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/cttextalignment/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/cttextalignment/init%28_%3A%29.json'
content_hash: 'sha256:0b1154f02da8843d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTTextAlignment](../cttextalignment.md)

# init(_:)

<sub>Initializer</sub>

Converts a UIKit text alignment constant value to the matching constant value that Core Text uses.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(_ nsTextAlignment: NSTextAlignment)
```

## Parameters

- `nsTextAlignment` — The UIKit text alignment constant you want to convert.

## Return Value

The Core Text alignment that corresponds to the value specified in `nsTextAlignment`.

## Discussion

Use this function when you need to map between the UIKit and Core Text constants for text alignment.
