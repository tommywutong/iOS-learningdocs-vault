---
title: 'UIGraphicsSetPDFContextDestinationForRect(_:_:)'
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicssetpdfcontextdestinationforrect(_:_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicssetpdfcontextdestinationforrect(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicssetpdfcontextdestinationforrect%28_%3A_%3A%29.json'
content_hash: 'sha256:6477fd1df73b1c82'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGraphicsSetPDFContextDestinationForRect(_:_:)

<sub>Function</sub>

Links a rectangular area on the current page to the specified jump destination.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func UIGraphicsSetPDFContextDestinationForRect(_ name: String, _ rect: CGRect)
```

## Parameters

- `name` — A named destination in the PDF document. This is the same name you used when creating the jump destination using the [UIGraphicsAddPDFContextDestinationAtPoint](<uigraphicsaddpdfcontextdestinationatpoint(____).md>) function.

- `rect` — A rectangle on the current page of the PDF context.

## Discussion

You use this function to create live links within a PDF document. Tapping the specified rectangle in the PDF document causes the document to display the contents at the associated jump destination.

If the current graphics context is not a PDF context, this function does nothing.

## See Also

### PDF creation

- [UIGraphicsBeginPDFContextToData](<uigraphicsbeginpdfcontexttodata(______).md>) — Creates a PDF graphics context that targets the specified mutable data object.
- [UIGraphicsBeginPDFContextToFile](<uigraphicsbeginpdfcontexttofile(______).md>) — Creates a PDF graphics context that targets a file at the specified path.
- [UIGraphicsEndPDFContext](<uigraphicsendpdfcontext().md>) — Closes a PDF graphics context and pops it from the current context stack.
- [UIGraphicsBeginPDFPage](<uigraphicsbeginpdfpage().md>) — Marks the beginning of a new page in a PDF context and configures it using default values.
- [UIGraphicsBeginPDFPageWithInfo](<uigraphicsbeginpdfpagewithinfo(____).md>) — Marks the beginning of a new page in a PDF context and configures it using the specified custom values.
- [UIGraphicsGetPDFContextBounds](<uigraphicsgetpdfcontextbounds().md>) — Returns the current page bounds.
- [UIGraphicsAddPDFContextDestinationAtPoint](<uigraphicsaddpdfcontextdestinationatpoint(____).md>) — Creates a jump destination in the current page.
- [UIGraphicsSetPDFContextURLForRect](<uigraphicssetpdfcontexturlforrect(____).md>) — Links a rectangular area on the current page to the specified URL.
