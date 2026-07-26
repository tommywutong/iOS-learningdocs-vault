---
title: UIGraphicsPDFRendererFormat
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicspdfrendererformat
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicspdfrendererformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicspdfrendererformat.json'
content_hash: 'sha256:9be04e67567b7201'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGraphicsPDFRendererFormat

<sub>Class</sub>

A set of drawing attributes that represents the configuration of a PDF renderer context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class UIGraphicsPDFRendererFormat
```

## Overview

Use this subclass of [UIGraphicsRendererFormat](uigraphicsrendererformat.md) to provide context configuration parameters to a [UIGraphicsPDFRenderer](uigraphicspdfrenderer.md).

Create an instance and then add PDF configuration parameters to the [documentInfo](uigraphicspdfrendererformat/documentinfo.md) dictionary.

The following code demonstrates how you can use a PDF renderer format object to specify the author of the PDFs created by a PDF renderer.

**Swift**

```swift
let format = UIGraphicsPDFRendererFormat()
format.documentInfo = [ kCGPDFContextAuthor as String : "Kate Bell" ]
let renderer =
  UIGraphicsPDFRenderer(bounds: CGRect(x: 0, y: 0, width: 500, height: 300),
                        format: format)
```

**Objective-C**

```objc
UIGraphicsPDFRendererFormat *format = [[UIGraphicsPDFRendererFormat alloc] init];
format.documentInfo = @{ (NSString *)kCGPDFContextAuthor : @"Kate Bell" };
UIGraphicsPDFRenderer *renderer =
    [[UIGraphicsPDFRenderer alloc] initWithBounds:CGRectMake(0, 0, 500, 300)
                                           format:format];
```

## Relationships

- **Inherits From**: [UIGraphicsRendererFormat](uigraphicsrendererformat.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the PDF document info

- [documentInfo](uigraphicspdfrendererformat/documentinfo.md) — A dictionary that specifies additional information to be associated with the PDFs created by the PDF renderer.

## See Also

### Graphics contexts

- [UIGraphicsRenderer](uigraphicsrenderer.md) — An abstract base class for creating graphics renderers.
- [UIGraphicsRendererContext](uigraphicsrenderercontext.md) — The base class for the drawing environments for graphics renderers.
- [UIGraphicsRendererFormat](uigraphicsrendererformat.md) — A set of drawing attributes that represents the configuration of a graphics renderer context.
- [UIGraphicsImageRenderer](uigraphicsimagerenderer.md) — A graphics renderer for creating Core Graphics-backed images.
- [UIGraphicsImageRendererContext](uigraphicsimagerenderercontext.md) — The drawing environment for an image renderer.
- [UIGraphicsImageRendererFormat](uigraphicsimagerendererformat.md) — A set of drawing attributes that represents the configuration of an image renderer context.
- [UIGraphicsPDFRenderer](uigraphicspdfrenderer.md) — A graphics renderer for creating PDFs.
- [UIGraphicsPDFRendererContext](uigraphicspdfrenderercontext.md) — The drawing environment for a PDF renderer.
