---
title: CGPDFOperatorTable
framework: Core Graphics
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfoperatortable
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfoperatortable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfoperatortable.json'
content_hash: 'sha256:67334757c1ce0534'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFOperatorTable

<sub>API Collection</sub>

A set of callback functions for operators used when scanning content in a PDF document.

## Overview

You pass an operator table and a PDF content stream to a CGPDFScanner object. When the scanner parses a PDF operator, Core Graphics invokes your callback for that operator. See also [CGPDFScanner](cgpdfscanner.md) and [CGPDFContentStream](cgpdfcontentstream.md).

> [!note] Note
> This object is not derived from CFType and therefore you can’t use the Core Foundation base functions on it, such as [CFRetain](../corefoundation/cfretain.md) and [CFRelease](../corefoundation/cfrelease.md). In Objective-C, handle memory management with [CGPDFOperatorTableRetain](<cgpdfoperatortableretain(__).md>) and [CGPDFOperatorTableRelease](<cgpdfoperatortablerelease(__).md>).

For more about PDF operators, see the latest version of _PDF Reference_, Adobe Systems Incorporated.

## Topics

### Creating a PDF Operator Table

- [CGPDFOperatorTableCreate](<cgpdfoperatortablecreate().md>) — Creates an empty PDF operator table.

### Setting Callback Functions

- [CGPDFOperatorTableSetCallback](<cgpdfoperatortablesetcallback(______).md>) — Sets a callback function for a PDF operator.

### Retaining and Releasing a PDF Operator Table

- [CGPDFOperatorTableRetain](<cgpdfoperatortableretain(__).md>) — Increments the retain count of a CGPDFOperatorTable object.
- [CGPDFOperatorTableRelease](<cgpdfoperatortablerelease(__).md>) — Decrements the retain count of a CGPDFOperatorTable object.

### Callbacks

- [CGPDFOperatorCallback](cgpdfoperatorcallback.md) — Performs custom processing for PDF operators.

### Data Types

- [CGPDFOperatorTableRef](cgpdfoperatortableref.md) — A type that stores callback functions for PDF operators.
