---
title: 'addPrintFormatter(_:startingAtPageAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintpagerenderer/addprintformatter(_:startingatpageat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintpagerenderer/addprintformatter(_:startingatpageat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintpagerenderer/addprintformatter%28_%3Astartingatpageat%3A%29.json'
content_hash: 'sha256:661740eb5591329e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintPageRenderer](../uiprintpagerenderer.md)

# addPrintFormatter(_:startingAtPageAt:)

<sub>Instance Method</sub>

Adds a print formatter to the page renderer starting at the specified page.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func addPrintFormatter(_ formatter: UIPrintFormatter, startingAtPageAt pageIndex: Int)
```

## Parameters

- `formatter` — The [UIPrintFormatter](../uiprintformatter.md) object to add to the page renderer. A print formatter can be an instance of [UISimpleTextPrintFormatter](../uisimpletextprintformatter.md), [UIMarkupTextPrintFormatter](../uimarkuptextprintformatter.md), or [UIViewPrintFormatter](../uiviewprintformatter.md).

- `pageIndex` — The index identifying the first page with which the print formatter should be associated with. This value overrides the [startPage](../uiprintformatter/startpage.md) property of the print formatter.

## Discussion

You can dissociate a print formatter from its page renderer by calling the [- removeFromPrintPageRenderer](<../uiprintformatter/removefromprintpagerenderer().md>) method on the print formatter.

## See Also

### Managing print formatters

- [- printFormattersForPageAtIndex:](<printformattersforpage(at_).md>) — Returns the print formatters for a specified page.
- [printFormatters](printformatters.md) — The print formatters for the page renderer.
