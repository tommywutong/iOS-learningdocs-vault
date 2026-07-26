---
title: 'size(forNumberOfPages:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipagecontrol/size(fornumberofpages:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontrol/size(fornumberofpages:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontrol/size%28fornumberofpages%3A%29.json'
content_hash: 'sha256:cf93aa649ceb6517'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageControl](../uipagecontrol.md)

# size(forNumberOfPages:)

<sub>Instance Method</sub>

Returns the size the receiver’s bounds should be to accommodate the given number of pages.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func size(forNumberOfPages pageCount: Int) -> CGSize
```

## Parameters

- `pageCount` — The number of pages to fit in the receiver’s bounds.

## Return Value

The minimum size required to display dots for the page count.

## Discussion

Subclasses that customize the appearance of the page control can use this method to resize the page control when the page count changes.
