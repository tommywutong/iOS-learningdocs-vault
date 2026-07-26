---
title: 'loadInPlaceFileRepresentation(forTypeIdentifier:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/loadinplacefilerepresentation(fortypeidentifier:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/loadinplacefilerepresentation(fortypeidentifier:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/loadinplacefilerepresentation%28fortypeidentifier%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:82319f890af03c6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# loadInPlaceFileRepresentation(forTypeIdentifier:completionHandler:)

<sub>Instance Method</sub>

Asynchronously opens a file in place, if possible, returning a progress object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadInPlaceFileRepresentation(forTypeIdentifier typeIdentifier: String, completionHandler: @escaping @Sendable (URL?, Bool, (any Error)?) -> Void) -> Progress
```

## Discussion

The system sets the `isInPlace` parameter to [true](../../swift/true.md) if the system successfully opened the file in place, or [false](../../swift/false.md) if it made a local copy. In either case, you must access the returned [URL](../url.md) using an [NSFileCoordinator](../nsfilecoordinator.md) object.

If the system created a local copy of a file, it will be automatically deleted after your file coordinator relinquishes its read access to the file.

## See Also

### Loading the provider’s contents

- [- loadItemForTypeIdentifier:options:completionHandler:](<loaditem(fortypeidentifier_options_completionhandler_).md>) — Loads the item’s data and coerces it to the specified type. _(deprecated)_
- [- loadDataRepresentationForTypeIdentifier:completionHandler:](<loaddatarepresentation(fortypeidentifier_completionhandler_).md>) — Asynchronously copies the provided, typed data into a generic data object, returning a progress object.
- [loadDataRepresentation(for:completionHandler:)](<loaddatarepresentation(for_completionhandler_).md>) — Asynchronously copies the universal type data into a generic data object, returning a progress object.
- [- loadFileRepresentationForTypeIdentifier:completionHandler:](<loadfilerepresentation(fortypeidentifier_completionhandler_).md>) — Asynchronously writes a copy of the provided, typed data to a temporary file, returning a progress object.
- [loadFileRepresentation(for:openInPlace:completionHandler:)](<loadfilerepresentation(for_openinplace_completionhandler_).md>) — Asynchronously writes a copy of the universal type data to a temporary file, returning a progress object.
- [- loadObjectOfClass:completionHandler:](<loadobject(ofclass_completionhandler_)-8ak5d.md>) — Asynchronously loads an object of a specified class to an item provider, returning a progress object.
- [loadObject(ofClass:completionHandler:)](<loadobject(ofclass_completionhandler_)-6pysm.md>) — Asynchronously loads an object of a specified class to an item provider, returning a progress object.
- [loadTransferable(type:completionHandler:)](<loadtransferable(type_completionhandler_).md>) — Asynchronously loads an object of a specified transferable type to an item provider, returning a progress object.
