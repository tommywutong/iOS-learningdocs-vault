---
title: 'CGPDFOperatorTableSetCallback(_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfoperatortablesetcallback(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfoperatortablesetcallback(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfoperatortablesetcallback%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:60741d78b19b977f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFOperatorTableSetCallback(_:_:_:)

<sub>Function</sub>

Sets a callback function for a PDF operator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFOperatorTableSetCallback(_ table: CGPDFOperatorTableRef, _ name: UnsafePointer<CChar>, _ callback: CGPDFOperatorCallback)
```

## Parameters

- `table` — A PDF operator table.

- `name` — The name of the PDF operator you want to set a callback for.

- `callback` — The callback to invoke for the PDF operator specified by the `name` parameter.

## Discussion

You call the function [CGPDFOperatorTableSetCallback](<cgpdfoperatortablesetcallback(______).md>) for each PDF operator for which you want to provide a callback. See Appendix A in the _PDF Reference, Second Edition_, version 1.3, Adobe Systems Incorporated for a summary of PDF operators.
