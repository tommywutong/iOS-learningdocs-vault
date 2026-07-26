---
title: UIViewPrintFormatter
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewprintformatter
source_url: 'https://developer.apple.com/documentation/uikit/uiviewprintformatter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewprintformatter.json'
content_hash: 'sha256:2ccc7d37a29a8873'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIViewPrintFormatter

<sub>Class</sub>

An object that lays out the drawn content of a view for printing.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class UIViewPrintFormatter
```

## Overview

Instances of three system classes offer usable view print formatters to applications: [UIWebView](uiwebview.md) and [UITextView](uitextview.md) of the UIKit framework, and [MKMapView](../mapkit/mkmapview.md) of the MapKit framework. To obtain a view print formatter for a print job, call the [UIView](uiview.md) method [- viewPrintFormatter](<uiview/viewprintformatter().md>) and initialize the print formatter’s inherited layout properties.

Add the print formatter to the print job in one of two ways:

- If a single print formatter is being used for the print job (with no additional drawing), assign it to the [printFormatter](uiprintinteractioncontroller/printformatter.md) property of the [UIPrintInteractionController](uiprintinteractioncontroller.md) shared instance. The inherited [startPage](uiprintformatter/startpage.md) property identifies the beginning page of content with which the formatter is associated.
- If you are using multiple formatters along with a page renderer, associate each print formatter with a starting page of the printed content. You often take this approach when you want to add content such as headers and footers to what the formatters provide. You have two ways of associating a print formatter with a  [UIPrintPageRenderer](uiprintpagerenderer.md) object:
- You can add print formatters to the [printFormatters](uiprintpagerenderer/printformatters.md)  property of the [UIPrintPageRenderer](uiprintpagerenderer.md) object; the [startPage](uiprintformatter/startpage.md) property of the print formatter specifies the starting page
- You can add print formatters by calling [- addPrintFormatter:startingAtPageAtIndex:](<uiprintpagerenderer/addprintformatter(__startingatpageat_).md>) for each print formatter; the second parameter of this method specifies the starting page (and overrides any [startPage](uiprintformatter/startpage.md) value).

View print formatters typically implement the [UIView](uiview.md) method [- drawRect:forViewPrintFormatter:](<uiview/draw(__for_).md>) to draw content in a way that is suitable for printing, If they don’t implement this method, their [- drawRect:](<uiview/draw(__).md>) method is called instead.

### Subclassing Notes

Subclassing `UIViewPrintFormatter` to print the contents of a view is not recommended. To print the contents of a custom view, you should instead draw the view’s contents for printing using a custom [UIPrintPageRenderer](uiprintpagerenderer.md) object.

## Relationships

- **Inherits From**: [UIPrintFormatter](uiprintformatter.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing the view

- [view](uiviewprintformatter/view.md) — The view from which the view print formatter was derived.

## See Also

### Formatters

- [UIPrintFormatter](uiprintformatter.md) — An abstract base class for print formatters, which are objects that lay out custom printable content that can cross page boundaries.
- [UISimpleTextPrintFormatter](uisimpletextprintformatter.md) — An object that lays out plain text for printing, possibly over multiple pages.
- [UIMarkupTextPrintFormatter](uimarkuptextprintformatter.md) — An object that lays out HTML text for a multipage print job.
