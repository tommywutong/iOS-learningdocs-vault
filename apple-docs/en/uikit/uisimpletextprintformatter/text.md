---
title: text
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisimpletextprintformatter/text
source_url: 'https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/text'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisimpletextprintformatter/text.json'
content_hash: 'sha256:e8e9b054dcd1a73a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISimpleTextPrintFormatter](../uisimpletextprintformatter.md)

# text

<sub>Instance Property</sub>

A string of plain text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var text: String? { get set }
```

## Discussion

You cannot change the value of this property once drawing begins for a print job. The delegate method [- printInteractionControllerWillStartJob:](<../uiprintinteractioncontrollerdelegate/printinteractioncontrollerwillstartjob(__).md>) is called immediately before the formatting is set for the job.

Assigning a value to this property replaces the value in the [attributedText](attributedtext.md) property with the same string data, albeit without any inherent style attributes. Instead, the print formatter styles the new string using the text attribute properties of this class.

## See Also

### Related Documentation

- [- initWithText:](<init(text_).md>) — Returns a simple-text print formatter initialized with plain text.

### Getting and setting the text

- [attributedText](attributedtext.md) — A string of attributed text.
