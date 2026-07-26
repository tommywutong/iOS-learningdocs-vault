---
title: 'printFormattersForPage(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintpagerenderer/printformattersforpage(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintpagerenderer/printformattersforpage(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintpagerenderer/printformattersforpage%28at%3A%29.json'
content_hash: 'sha256:6e52b0c0ff6102c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintPageRenderer](../uiprintpagerenderer.md)

# printFormattersForPage(at:)

<sub>Instance Method</sub>

Returns the print formatters for a specified page.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func printFormattersForPage(at pageIndex: Int) -> [UIPrintFormatter]?
```

## Parameters

- `pageIndex` — The index of a page of printable content.

## Return Value

An array of [UIPrintFormatter](../uiprintformatter.md) objects. A print formatter can be an instance of [UISimpleTextPrintFormatter](../uisimpletextprintformatter.md), [UIMarkupTextPrintFormatter](../uimarkuptextprintformatter.md), or [UIViewPrintFormatter](../uiviewprintformatter.md).

## Discussion

A print formatter is associated with a starting page of printable content through the [- addPrintFormatter:startingAtPageAtIndex:](<addprintformatter(__startingatpageat_).md>) method or the [startPage](../uiprintformatter/startpage.md) property of [UIPrintFormatter](../uiprintformatter.md). The number of pages from that page is determined by the [pageCount](../uiprintformatter/pagecount.md) property, which [UIPrintFormatter](../uiprintformatter.md) computes based on layout metrics and content.

## See Also

### Managing print formatters

- [- addPrintFormatter:startingAtPageAtIndex:](<addprintformatter(__startingatpageat_).md>) — Adds a print formatter to the page renderer starting at the specified page.
- [printFormatters](printformatters.md) — The print formatters for the page renderer.
