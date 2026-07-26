---
title: 'UIGraphicsBeginPDFContextToData(_:_:_:)'
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicsbeginpdfcontexttodata(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsbeginpdfcontexttodata(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsbeginpdfcontexttodata%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:76fbd01cdb16fa0d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGraphicsBeginPDFContextToData(_:_:_:)

<sub>Function</sub>

Creates a PDF graphics context that targets the specified mutable data object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func UIGraphicsBeginPDFContextToData(_ data: NSMutableData, _ bounds: CGRect, _ documentInfo: [AnyHashable : Any]?)
```

## Parameters

- `data` — The data object to receive the PDF output data.

- `bounds` — A rectangle that specifies the default size and location of PDF pages. (This value is used as the default media box for each new page.) The origin of the rectangle should typically be (0, 0). Specifying an empty rectangle ([CGRectZero](../coregraphics/cgrectzero.md)) sets the default page size to 8.5 by 11 inches (612 by 792 points).

- `documentInfo` — A dictionary that specifies additional information to be associated with the PDF file. You can use these keys to specify additional metadata and security information for the PDF, such as the author of the PDF or the password for accessing it. The keys in this dictionary are the same keys you pass to the [init(consumer:mediaBox:_:)](<../coregraphics/cgcontext/init(consumer_mediabox___).md>) function and are described in [Auxiliary Dictionary Keys](../coregraphics/auxiliary-dictionary-keys.md). The dictionary is retained by the new context, so on return you may safely release it. Specify `nil` if you do not want to associate any additional information with the PDF document.

## Discussion

After creating the graphics context, this function makes it the current drawing context. Any subsequent drawing commands are therefore captured and turned into PDF data. When you are done drawing, you must call the [UIGraphicsEndPDFContext](<uigraphicsendpdfcontext().md>) function to close the PDF graphics context.

You can use all of the same drawing routines that you would normally use to draw the contents of your application. The graphics context converts all drawing commands into PDF drawing commands automatically. However, before you issue any drawing commands to a PDF context, you must start a new page by calling the [UIGraphicsBeginPDFPage](<uigraphicsbeginpdfpage().md>) or [UIGraphicsBeginPDFPageWithInfo](<uigraphicsbeginpdfpagewithinfo(____).md>) function. You can also use these functions to define additional pages later.

After creating it, you can get the PDF context using the [UIGraphicsGetCurrentContext](<uigraphicsgetcurrentcontext().md>) function.

## See Also

### PDF creation

- [UIGraphicsBeginPDFContextToFile](<uigraphicsbeginpdfcontexttofile(______).md>) — Creates a PDF graphics context that targets a file at the specified path.
- [UIGraphicsEndPDFContext](<uigraphicsendpdfcontext().md>) — Closes a PDF graphics context and pops it from the current context stack.
- [UIGraphicsBeginPDFPage](<uigraphicsbeginpdfpage().md>) — Marks the beginning of a new page in a PDF context and configures it using default values.
- [UIGraphicsBeginPDFPageWithInfo](<uigraphicsbeginpdfpagewithinfo(____).md>) — Marks the beginning of a new page in a PDF context and configures it using the specified custom values.
- [UIGraphicsGetPDFContextBounds](<uigraphicsgetpdfcontextbounds().md>) — Returns the current page bounds.
- [UIGraphicsAddPDFContextDestinationAtPoint](<uigraphicsaddpdfcontextdestinationatpoint(____).md>) — Creates a jump destination in the current page.
- [UIGraphicsSetPDFContextDestinationForRect](<uigraphicssetpdfcontextdestinationforrect(____).md>) — Links a rectangular area on the current page to the specified jump destination.
- [UIGraphicsSetPDFContextURLForRect](<uigraphicssetpdfcontexturlforrect(____).md>) — Links a rectangular area on the current page to the specified URL.
