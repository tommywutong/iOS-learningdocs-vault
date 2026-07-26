---
title: attributedText
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisimpletextprintformatter/attributedtext
source_url: 'https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/attributedtext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisimpletextprintformatter/attributedtext.json'
content_hash: 'sha256:9b7f273f2a3af247'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISimpleTextPrintFormatter](../uisimpletextprintformatter.md)

# attributedText

<sub>Instance Property</sub>

A string of attributed text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@NSCopying var attributedText: NSAttributedString? { get set }
```

## Discussion

You cannot change the value of this property once drawing begins for a print job. The delegate method [- printInteractionControllerWillStartJob:](<../uiprintinteractioncontrollerdelegate/printinteractioncontrollerwillstartjob(__).md>) is called immediately before the formatting is set for the job.

Assigning a value to this property also replaces the value in the [text](text.md) property with the same string data, albeit without any formatting information.

## See Also

### Related Documentation

- [- initWithAttributedText:](<init(attributedtext_).md>) — Returns a simple-text print formatter initialized with attributed text.

### Getting and setting the text

- [text](text.md) — A string of plain text.
