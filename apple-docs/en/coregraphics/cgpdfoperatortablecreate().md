---
title: CGPDFOperatorTableCreate()
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfoperatortablecreate()
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfoperatortablecreate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfoperatortablecreate%28%29.json'
content_hash: 'sha256:68f1792c6bb74982'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFOperatorTableCreate()

<sub>Function</sub>

Creates an empty PDF operator table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFOperatorTableCreate() -> CGPDFOperatorTableRef?
```

## Return Value

An empty PDF operator table. In Objective-C, you’re responsible for releasing this object by calling [CGPDFOperatorTableRelease](<cgpdfoperatortablerelease(__).md>).

## Discussion

Call the function [CGPDFOperatorTableSetCallback](<cgpdfoperatortablesetcallback(______).md>) to fill the operator table with callbacks.
