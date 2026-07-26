---
title: 'UIGraphicsAddPDFContextDestinationAtPoint(_:_:)'
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicsaddpdfcontextdestinationatpoint(_:_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsaddpdfcontextdestinationatpoint(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsaddpdfcontextdestinationatpoint%28_%3A_%3A%29.json'
content_hash: 'sha256:11b516ba5897250e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGraphicsAddPDFContextDestinationAtPoint(_:_:)

<sub>Function</sub>

Creates a jump destination in the current page.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func UIGraphicsAddPDFContextDestinationAtPoint(_ name: String, _ point: CGPoint)
```

## Parameters

- `name` — The name of the destination point. The name you assign is local to the PDF document and is what you use when creating links to this destination.

- `point` — A point on the current page of the PDF context.

## Discussion

This function marks the specified point in the current page as the destination of a jump. When the user taps a link that takes them to this jump destination, the PDF document scrolls until the specified point is visible.

If the current graphics context is not a PDF context, this function does nothing.

For information on how to create links to this destination, see the [UIGraphicsSetPDFContextDestinationForRect](<uigraphicssetpdfcontextdestinationforrect(____).md>) function.

## See Also

### PDF creation

- [UIGraphicsBeginPDFContextToData](<uigraphicsbeginpdfcontexttodata(______).md>) — Creates a PDF graphics context that targets the specified mutable data object.
- [UIGraphicsBeginPDFContextToFile](<uigraphicsbeginpdfcontexttofile(______).md>) — Creates a PDF graphics context that targets a file at the specified path.
- [UIGraphicsEndPDFContext](<uigraphicsendpdfcontext().md>) — Closes a PDF graphics context and pops it from the current context stack.
- [UIGraphicsBeginPDFPage](<uigraphicsbeginpdfpage().md>) — Marks the beginning of a new page in a PDF context and configures it using default values.
- [UIGraphicsBeginPDFPageWithInfo](<uigraphicsbeginpdfpagewithinfo(____).md>) — Marks the beginning of a new page in a PDF context and configures it using the specified custom values.
- [UIGraphicsGetPDFContextBounds](<uigraphicsgetpdfcontextbounds().md>) — Returns the current page bounds.
- [UIGraphicsSetPDFContextDestinationForRect](<uigraphicssetpdfcontextdestinationforrect(____).md>) — Links a rectangular area on the current page to the specified jump destination.
- [UIGraphicsSetPDFContextURLForRect](<uigraphicssetpdfcontexturlforrect(____).md>) — Links a rectangular area on the current page to the specified URL.
