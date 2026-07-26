---
title: requiresMainThread
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintformatter/requiresmainthread
source_url: 'https://developer.apple.com/documentation/uikit/uiprintformatter/requiresmainthread'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintformatter/requiresmainthread.json'
content_hash: 'sha256:460fd3499288aa29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintFormatter](../uiprintformatter.md)

# requiresMainThread

<sub>Instance Property</sub>

A Boolean value that determines whether the system executes the print formatter’s rendering operations on the main thread.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var requiresMainThread: Bool { get }
```

## Discussion

The default value is [true](../../swift/true.md), which requires the printing system to execute rendering operations, like drawing and page-count calculation, on the main thread. Override this property to return [false](../../swift/false.md) if you want the system to execute operations like [- drawInRect:forPageAtIndex:](<draw(in_forpageat_).md>) and [pageCount](pagecount.md) on a background thread.
