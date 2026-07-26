---
title: 'loadItem(forTypeIdentifier:options:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsitemprovider/loaditem(fortypeidentifier:options:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/loaditem(fortypeidentifier:options:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/loaditem%28fortypeidentifier%3Aoptions%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:42ffc1724d0d1e34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# loadItem(forTypeIdentifier:options:completionHandler:)

<sub>Instance Method</sub>

Loads the item’s data and coerces it to the specified type.

> [!warning] Deprecated
> Use loadObjectOfClass:completionHandler: instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadItem(forTypeIdentifier typeIdentifier: String, options: [AnyHashable : Any]? = nil, completionHandler: NSItemProvider.CompletionHandler? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadItem(forTypeIdentifier typeIdentifier: String, options: [AnyHashable : Any]? = nil) async throws -> any NSSecureCoding
```

## Parameters

- `typeIdentifier` — A string that represents the desired UTI.

- `options` — A dictionary of keys and values that provide information about the item, such as the size of an image. (See [NSItemProviderPreferredImageSizeKey](../nsitemproviderpreferredimagesizekey.md) for a key you can use.)

- `completionHandler` — A completion handler block to execute with the results. For information about the format of this block, see [CompletionHandler](completionhandler.md).

## Discussion

Call this method when you want to retrieve the item provider’s data. If the item provider object is able to provide data in the requested type, it does so and asynchronously executes your `completionHandler` block with the results. The block may be executed on a background thread.

The type information for the first parameter of your `completionHandler` block should be set to the class of the expected type. For example, when requesting text data, you might set the type of the first parameter to [NSString](../nsstring.md) or [NSAttributedString](../nsattributedstring.md). An item provider can perform simple type conversions of the data to the class you specify, such as from [NSURL](../nsurl.md) to [NSData](../nsdata.md) or [FileWrapper](../filewrapper.md), or from [NSData](../nsdata.md) to [UIImage](../../uikit/uiimage.md) (in iOS) or [NSImage](../../appkit/nsimage.md) (in macOS). If the data could not be retrieved or coerced to the specified class, an error is passed to the completion block’s.

## See Also

### Loading the provider’s contents

- [- loadDataRepresentationForTypeIdentifier:completionHandler:](<loaddatarepresentation(fortypeidentifier_completionhandler_).md>) — Asynchronously copies the provided, typed data into a generic data object, returning a progress object.
- [loadDataRepresentation(for:completionHandler:)](<loaddatarepresentation(for_completionhandler_).md>) — Asynchronously copies the universal type data into a generic data object, returning a progress object.
- [- loadFileRepresentationForTypeIdentifier:completionHandler:](<loadfilerepresentation(fortypeidentifier_completionhandler_).md>) — Asynchronously writes a copy of the provided, typed data to a temporary file, returning a progress object.
- [loadFileRepresentation(for:openInPlace:completionHandler:)](<loadfilerepresentation(for_openinplace_completionhandler_).md>) — Asynchronously writes a copy of the universal type data to a temporary file, returning a progress object.
- [- loadInPlaceFileRepresentationForTypeIdentifier:completionHandler:](<loadinplacefilerepresentation(fortypeidentifier_completionhandler_).md>) — Asynchronously opens a file in place, if possible, returning a progress object.
- [- loadObjectOfClass:completionHandler:](<loadobject(ofclass_completionhandler_)-8ak5d.md>) — Asynchronously loads an object of a specified class to an item provider, returning a progress object.
- [loadObject(ofClass:completionHandler:)](<loadobject(ofclass_completionhandler_)-6pysm.md>) — Asynchronously loads an object of a specified class to an item provider, returning a progress object.
- [loadTransferable(type:completionHandler:)](<loadtransferable(type_completionhandler_).md>) — Asynchronously loads an object of a specified transferable type to an item provider, returning a progress object.
