---
title: paperSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintpaper/papersize
source_url: 'https://developer.apple.com/documentation/uikit/uiprintpaper/papersize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintpaper/papersize.json'
content_hash: 'sha256:1b8d4809636da6ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintPaper](../uiprintpaper.md)

# paperSize

<sub>Instance Property</sub>

The size of the sheet to use for printing.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var paperSize: CGSize { get }
```

## Discussion

The paper size is often associated with a standard designation, such as “Letter” and “A4”. For example, the paper size for a Letter sheet of paper is 612 points wide and 792 points high.

## See Also

### Getting the paper size and the printing area

- [printableRect](printablerect.md) — The rectangle that represents the portion of the paper that can be imaged upon.
