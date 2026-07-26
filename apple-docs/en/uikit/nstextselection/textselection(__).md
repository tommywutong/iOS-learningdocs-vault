---
title: 'textSelection(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextselection/textselection(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextselection/textselection(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselection/textselection%28_%3A%29.json'
content_hash: 'sha256:fcc9d2400e07c46b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelection](../nstextselection.md)

# textSelection(_:)

<sub>Instance Method</sub>

Creates a subselection of the current text selection with the ranges you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func textSelection(_ textRanges: [NSTextRange]) -> NSTextSelection
```

## Parameters

- `textRanges` — An array of text ranges.

## Return Value

A new [NSTextSelection](../nstextselection.md).
