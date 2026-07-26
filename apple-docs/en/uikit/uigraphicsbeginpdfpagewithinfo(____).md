---
title: 'UIGraphicsBeginPDFPageWithInfo(_:_:)'
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicsbeginpdfpagewithinfo(_:_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsbeginpdfpagewithinfo(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsbeginpdfpagewithinfo%28_%3A_%3A%29.json'
content_hash: 'sha256:925ad6a0e94db320'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGraphicsBeginPDFPageWithInfo(_:_:)

<sub>Function</sub>

Marks the beginning of a new page in a PDF context and configures it using the specified custom values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func UIGraphicsBeginPDFPageWithInfo(_ bounds: CGRect, _ pageInfo: [AnyHashable : Any]?)
```

## Parameters

- `bounds` — A rectangle that specifies the size and location of the new PDF page. This rectangle corresponds to the media box rectangle for the page.

- `pageInfo` — A dictionary that specifies additional page-related information, such as the boxes that define different parts of the page. For a list of keys you can include in this dictionary, see Box Keys in [Auxiliary Dictionary Keys](../coregraphics/auxiliary-dictionary-keys.md). The dictionary is retained by the new page, so you may release it after this function returns. Specify `nil` if you do not want to associate any additional information with the page.

## Discussion

This function ends any previous page before beginning a new one. It sets the media box of the new page to the value in the [kCGPDFContextMediaBox](../coregraphics/kcgpdfcontextmediabox.md) key of the `pageInfo` dictionary, or to the value in the `bounds` parameter if the dictionary does not contain the key.

If the current graphics context is not a PDF context, this function does nothing.

You must call this function or the [UIGraphicsBeginPDFPageWithInfo](<uigraphicsbeginpdfpagewithinfo(____).md>) function before you issue any drawing commands.

## See Also

### PDF creation

- [UIGraphicsBeginPDFContextToData](<uigraphicsbeginpdfcontexttodata(______).md>) — Creates a PDF graphics context that targets the specified mutable data object.
- [UIGraphicsBeginPDFContextToFile](<uigraphicsbeginpdfcontexttofile(______).md>) — Creates a PDF graphics context that targets a file at the specified path.
- [UIGraphicsEndPDFContext](<uigraphicsendpdfcontext().md>) — Closes a PDF graphics context and pops it from the current context stack.
- [UIGraphicsBeginPDFPage](<uigraphicsbeginpdfpage().md>) — Marks the beginning of a new page in a PDF context and configures it using default values.
- [UIGraphicsGetPDFContextBounds](<uigraphicsgetpdfcontextbounds().md>) — Returns the current page bounds.
- [UIGraphicsAddPDFContextDestinationAtPoint](<uigraphicsaddpdfcontextdestinationatpoint(____).md>) — Creates a jump destination in the current page.
- [UIGraphicsSetPDFContextDestinationForRect](<uigraphicssetpdfcontextdestinationforrect(____).md>) — Links a rectangular area on the current page to the specified jump destination.
- [UIGraphicsSetPDFContextURLForRect](<uigraphicssetpdfcontexturlforrect(____).md>) — Links a rectangular area on the current page to the specified URL.
