---
title: presentationIntent
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolsresultoptions/presentationintent
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolsresultoptions/presentationintent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolsresultoptions/presentationintent.json'
content_hash: 'sha256:72ce6a01f95cb44c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsResultOptions](../uiwritingtoolsresultoptions.md)

# presentationIntent

<sub>Type Property</sub>

implies `RichText`, `List`, and `Table`, and Writing Tools may provide text with presentation intent attributes. Writing Tools will use `NSPresentationIntent` instead of `NSTextList` and `NSTextTable` to represent lists and tables.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static var presentationIntent: UIWritingToolsResultOptions { get }
```
