---
title: 'UIGraphicsBeginPDFContextToFile(_:_:_:)'
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicsbeginpdfcontexttofile(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsbeginpdfcontexttofile(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsbeginpdfcontexttofile%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:45210b7c55b4e58b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGraphicsBeginPDFContextToFile(_:_:_:)

<sub>Function</sub>

Creates a PDF graphics context that targets a file at the specified path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func UIGraphicsBeginPDFContextToFile(_ path: String, _ bounds: CGRect, _ documentInfo: [AnyHashable : Any]?) -> Bool
```

## Parameters

- `path` — A POSIX-style path string identifying the location of the resulting PDF file. The specified path may be relative or a full path name. If a file does not exist at the specified path, one is created; otherwise, the contents of any existing file are deleted. The directories in the path must exist.

- `bounds` — A rectangle that specifies the default size and location of PDF pages. (This value is used as the default media box for each new page.) The origin of the rectangle should typically be (0, 0). Specifying an empty rectangle ([CGRectZero](../coregraphics/cgrectzero.md)) sets the default page size to 8.5 by 11 inches (612 by 792 points).

- `documentInfo` — A dictionary that specifies additional information to be associated with the PDF file. You can use these keys to specify additional metadata and security information for the PDF, such as the author of the PDF or the password for accessing it. The keys in this dictionary are the same keys you pass to the [init(consumer:mediaBox:_:)](<../coregraphics/cgcontext/init(consumer_mediabox___).md>) function and are described in [Auxiliary Dictionary Keys](../coregraphics/auxiliary-dictionary-keys.md). The dictionary is retained by the new context, so on return you may safely release it. Specify `nil` if you do not want to associate any additional information with the PDF document.

## Return Value

[true](../swift/true.md) if the PDF context was created successfully or [false](../swift/false.md) if it was not.

## Discussion

After creating the graphics context, this function makes it the current drawing context. Any subsequent drawing commands are therefore captured and turned into PDF data. When you are done drawing, you must call the [UIGraphicsEndPDFContext](<uigraphicsendpdfcontext().md>) function to close the PDF graphics context.

You can use all of the same drawing routines that you would normally use to draw the contents of your application. However, before you issue any drawing commands to a PDF context, you must start a new page by calling the [UIGraphicsBeginPDFPage](<uigraphicsbeginpdfpage().md>) or [UIGraphicsBeginPDFPageWithInfo](<uigraphicsbeginpdfpagewithinfo(____).md>) function. You can also use these functions to define additional pages later.

After creating it, you can get the PDF context using the [UIGraphicsGetCurrentContext](<uigraphicsgetcurrentcontext().md>) function.

## See Also

### PDF creation

- [UIGraphicsBeginPDFContextToData](<uigraphicsbeginpdfcontexttodata(______).md>) — Creates a PDF graphics context that targets the specified mutable data object.
- [UIGraphicsEndPDFContext](<uigraphicsendpdfcontext().md>) — Closes a PDF graphics context and pops it from the current context stack.
- [UIGraphicsBeginPDFPage](<uigraphicsbeginpdfpage().md>) — Marks the beginning of a new page in a PDF context and configures it using default values.
- [UIGraphicsBeginPDFPageWithInfo](<uigraphicsbeginpdfpagewithinfo(____).md>) — Marks the beginning of a new page in a PDF context and configures it using the specified custom values.
- [UIGraphicsGetPDFContextBounds](<uigraphicsgetpdfcontextbounds().md>) — Returns the current page bounds.
- [UIGraphicsAddPDFContextDestinationAtPoint](<uigraphicsaddpdfcontextdestinationatpoint(____).md>) — Creates a jump destination in the current page.
- [UIGraphicsSetPDFContextDestinationForRect](<uigraphicssetpdfcontextdestinationforrect(____).md>) — Links a rectangular area on the current page to the specified jump destination.
- [UIGraphicsSetPDFContextURLForRect](<uigraphicssetpdfcontexturlforrect(____).md>) — Links a rectangular area on the current page to the specified URL.
