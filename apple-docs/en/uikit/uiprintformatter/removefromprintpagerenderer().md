---
title: removeFromPrintPageRenderer()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintformatter/removefromprintpagerenderer()
source_url: 'https://developer.apple.com/documentation/uikit/uiprintformatter/removefromprintpagerenderer()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintformatter/removefromprintpagerenderer%28%29.json'
content_hash: 'sha256:680d56ed8b0d8871'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintFormatter](../uiprintformatter.md)

# removeFromPrintPageRenderer()

<sub>Instance Method</sub>

Removes the print formatter from the page renderer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func removeFromPrintPageRenderer()
```

## Discussion

A print formatter is typically associated with a pages of a [UIPrintPageRenderer](../uiprintpagerenderer.md) object through the [- addPrintFormatter:startingAtPageAtIndex:](<../uiprintpagerenderer/addprintformatter(__startingatpageat_).md>) method.

## See Also

### Communicating with the page renderer

- [printPageRenderer](printpagerenderer.md) — Returns the page renderer for the print formatter.
