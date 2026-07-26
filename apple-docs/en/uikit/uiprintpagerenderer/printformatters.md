---
title: printFormatters
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintpagerenderer/printformatters
source_url: 'https://developer.apple.com/documentation/uikit/uiprintpagerenderer/printformatters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintpagerenderer/printformatters.json'
content_hash: 'sha256:b29ad4a32c47a65f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintPageRenderer](../uiprintpagerenderer.md)

# printFormatters

<sub>Instance Property</sub>

The print formatters for the page renderer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var printFormatters: [UIPrintFormatter]? { get set }
```

## Discussion

The elements of the array are [UIPrintFormatter](../uiprintformatter.md) objects. A print formatter can be an instance of [UISimpleTextPrintFormatter](../uisimpletextprintformatter.md), [UIMarkupTextPrintFormatter](../uimarkuptextprintformatter.md), or [UIViewPrintFormatter](../uiviewprintformatter.md). Print formatters added this way to a page renderer are associated with page ranges through each print formatter’s [startPage](../uiprintformatter/startpage.md) and [pageCount](../uiprintformatter/pagecount.md) properties.

## See Also

### Managing print formatters

- [- addPrintFormatter:startingAtPageAtIndex:](<addprintformatter(__startingatpageat_).md>) — Adds a print formatter to the page renderer starting at the specified page.
- [- printFormattersForPageAtIndex:](<printformattersforpage(at_).md>) — Returns the print formatters for a specified page.
