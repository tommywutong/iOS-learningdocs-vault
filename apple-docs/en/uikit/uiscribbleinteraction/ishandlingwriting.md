---
title: isHandlingWriting
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscribbleinteraction/ishandlingwriting
source_url: 'https://developer.apple.com/documentation/uikit/uiscribbleinteraction/ishandlingwriting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscribbleinteraction/ishandlingwriting.json'
content_hash: 'sha256:eb7353ca441ca3c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScribbleInteraction](../uiscribbleinteraction.md)

# isHandlingWriting

<sub>Instance Property</sub>

A Boolean value that indicates whether the user is actively writing in a text view.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isHandlingWriting: Bool { get }
```

## Discussion

This property is [true](../../swift/true.md) in between calls to [- scribbleInteractionWillBeginWriting:](<../uiscribbleinteractiondelegate/scribbleinteractionwillbeginwriting(__).md>) and [- scribbleInteractionDidFinishWriting:](<../uiscribbleinteractiondelegate/scribbleinteractiondidfinishwriting(__).md>) when the user is writing.
