---
title: NSItemProvider.LoadHandler
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsitemprovider/loadhandler
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/loadhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/loadhandler.json'
content_hash: 'sha256:c94dbe3c854dac1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# NSItemProvider.LoadHandler

<sub>Type Alias</sub>

A block that loads the item provider’s data and coerces it to the specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias LoadHandler = @Sendable (NSItemProvider.CompletionHandler?, AnyClass?, [AnyHashable : Any]?) -> Void
```

## Discussion

Use this block when registering a type-specific coercion handler with the [- registerItemForTypeIdentifier:loadHandler:](<registeritem(fortypeidentifier_loadhandler_).md>) method. The parameters for this block are as follows:

- **completionHandler** — The completion handler to call with the resulting data. For information about this block, see [CompletionHandler](completionhandler.md).
- **expectedValueClass** — The expected class of the item being loaded. Convert the item provider’s data to this type and pass the resulting object as the first parameter of the `completionHandler` block.
- **options** — A dictionary with options for how to provide the requested item. For example, the dictionary may contain the pixel dimensions of a requested image. For information about the supported keys, see [Options Dictionary Key](../options-dictionary-key.md).

When a client calls the [- loadItemForTypeIdentifier:options:completionHandler:](<loaditem(fortypeidentifier_options_completionhandler_).md>) method and requests the appropriate type, the item provider executes your block. In your implementation, create an object of the expected type and execute the block in the `completionHandler` parameter, passing the newly created object as the first parameter of that block. If there is an error, pass `nil` for the object and provide an appropriate [NSError](../nserror.md) object explaining what happened.

This type of block is also used for generating preview images. In the case of a preview image, the `expectedValueClass` is always a [NSData](../nsdata.md), [NSURL](../nsurl.md), [UIImage](../../uikit/uiimage.md) (in iOS), or [NSImage](../../appkit/nsimage.md) (in macOS) class.

## See Also

### Constants

- [CompletionHandler](completionhandler.md) — A block that receives the item provider’s data.
- [Options Dictionary Key](../options-dictionary-key.md) — Keys indicating options to use when generating the item provider’s data.
- [Keys for Items Accessed in JavaScript Code](../keys-for-items-accessed-in-javascript-code.md) — Keys in property list items that the system recieves from or sends to JavaScript code.
- [NSItemProviderErrorDomain](errordomain.md) — The error domain associated with the item provider.
- [NSItemProviderFileOptions](../nsitemproviderfileoptions.md) — Data-access specifications that declare how to handle items.
- [NSItemProviderReading](../nsitemproviderreading.md) — The protocol for implementing a class to allow an item provider to create an instance of the class.
- [NSItemProviderWriting](../nsitemproviderwriting.md) — The protocol for implementing a class to allow an item provider to retrieve data from an instance of the class.
- [NSItemProviderRepresentationVisibility](../nsitemproviderrepresentationvisibility.md) — Specifications that control which categories of processes can see an item.
- [ErrorCode](errorcode.md) — The error codes that describe problems with consuming data from an item provider.
