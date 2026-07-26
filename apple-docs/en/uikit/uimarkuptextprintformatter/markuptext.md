---
title: markupText
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimarkuptextprintformatter/markuptext
source_url: 'https://developer.apple.com/documentation/uikit/uimarkuptextprintformatter/markuptext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimarkuptextprintformatter/markuptext.json'
content_hash: 'sha256:c08be7f8a5f226ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMarkupTextPrintFormatter](../uimarkuptextprintformatter.md)

# markupText

<sub>Instance Property</sub>

The HTML markup text for the print formatter.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var markupText: String? { get set }
```

## Discussion

When drawing begins for the print job, you cannot change the value of this property. The delegate method [- printInteractionControllerWillStartJob:](<../uiprintinteractioncontrollerdelegate/printinteractioncontrollerwillstartjob(__).md>) is called immediately before the formatting is set for the job.

## See Also

### Related Documentation

- [- initWithMarkupText:](<init(markuptext_).md>) — Returns a markup-text print formatter initialized with an HTML string.
