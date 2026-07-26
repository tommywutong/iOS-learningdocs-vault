---
title: 'CGPDFOperatorTableRetain(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfoperatortableretain(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfoperatortableretain(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfoperatortableretain%28_%3A%29.json'
content_hash: 'sha256:588bc5f36ff70205'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFOperatorTableRetain(_:)

<sub>Function</sub>

Increments the retain count of a CGPDFOperatorTable object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFOperatorTableRetain(_ table: CGPDFOperatorTableRef) -> CGPDFOperatorTableRef
```

## Parameters

- `table` — A PDF operator table.

## Return Value

The same PDF operator table you passed in as the `table` parameter.

## See Also

### Retaining and Releasing a PDF Operator Table

- [CGPDFOperatorTableRelease](<cgpdfoperatortablerelease(__).md>) — Decrements the retain count of a CGPDFOperatorTable object.
