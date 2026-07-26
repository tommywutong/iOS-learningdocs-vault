---
title: UIGraphicsGetPDFContextBounds()
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicsgetpdfcontextbounds()
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsgetpdfcontextbounds()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsgetpdfcontextbounds%28%29.json'
content_hash: 'sha256:fe5bfb6269f388b6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGraphicsGetPDFContextBounds()

<sub>Function</sub>

Returns the current page bounds.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func UIGraphicsGetPDFContextBounds() -> CGRect
```

## Return Value

The current page bounds associated with the PDF context or [CGRectZero](../coregraphics/cgrectzero.md) if the current context is not a PDF context.

## Discussion

If a page has not yet been started, this function returns the default media box you specified when you created the PDF context; otherwise, it returns the page bounds for the current page.

## See Also

### PDF creation

- [UIGraphicsBeginPDFContextToData](<uigraphicsbeginpdfcontexttodata(______).md>) — Creates a PDF graphics context that targets the specified mutable data object.
- [UIGraphicsBeginPDFContextToFile](<uigraphicsbeginpdfcontexttofile(______).md>) — Creates a PDF graphics context that targets a file at the specified path.
- [UIGraphicsEndPDFContext](<uigraphicsendpdfcontext().md>) — Closes a PDF graphics context and pops it from the current context stack.
- [UIGraphicsBeginPDFPage](<uigraphicsbeginpdfpage().md>) — Marks the beginning of a new page in a PDF context and configures it using default values.
- [UIGraphicsBeginPDFPageWithInfo](<uigraphicsbeginpdfpagewithinfo(____).md>) — Marks the beginning of a new page in a PDF context and configures it using the specified custom values.
- [UIGraphicsAddPDFContextDestinationAtPoint](<uigraphicsaddpdfcontextdestinationatpoint(____).md>) — Creates a jump destination in the current page.
- [UIGraphicsSetPDFContextDestinationForRect](<uigraphicssetpdfcontextdestinationforrect(____).md>) — Links a rectangular area on the current page to the specified jump destination.
- [UIGraphicsSetPDFContextURLForRect](<uigraphicssetpdfcontexturlforrect(____).md>) — Links a rectangular area on the current page to the specified URL.
