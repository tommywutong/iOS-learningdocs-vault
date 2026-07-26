---
title: 'loadDataRepresentation(for:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/loaddatarepresentation(for:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/loaddatarepresentation(for:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/loaddatarepresentation%28for%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:8db5f022ddc92ffa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# loadDataRepresentation(for:completionHandler:)

<sub>Instance Method</sub>

Asynchronously copies the universal type data into a generic data object, returning a progress object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadDataRepresentation(for contentType: UTType, completionHandler: @escaping @Sendable (Data?, (any Error)?) -> Void) -> Progress
```

## See Also

### Loading the provider’s contents

- [- loadItemForTypeIdentifier:options:completionHandler:](<loaditem(fortypeidentifier_options_completionhandler_).md>) — Loads the item’s data and coerces it to the specified type. _(deprecated)_
- [- loadDataRepresentationForTypeIdentifier:completionHandler:](<loaddatarepresentation(fortypeidentifier_completionhandler_).md>) — Asynchronously copies the provided, typed data into a generic data object, returning a progress object.
- [- loadFileRepresentationForTypeIdentifier:completionHandler:](<loadfilerepresentation(fortypeidentifier_completionhandler_).md>) — Asynchronously writes a copy of the provided, typed data to a temporary file, returning a progress object.
- [loadFileRepresentation(for:openInPlace:completionHandler:)](<loadfilerepresentation(for_openinplace_completionhandler_).md>) — Asynchronously writes a copy of the universal type data to a temporary file, returning a progress object.
- [- loadInPlaceFileRepresentationForTypeIdentifier:completionHandler:](<loadinplacefilerepresentation(fortypeidentifier_completionhandler_).md>) — Asynchronously opens a file in place, if possible, returning a progress object.
- [- loadObjectOfClass:completionHandler:](<loadobject(ofclass_completionhandler_)-8ak5d.md>) — Asynchronously loads an object of a specified class to an item provider, returning a progress object.
- [loadObject(ofClass:completionHandler:)](<loadobject(ofclass_completionhandler_)-6pysm.md>) — Asynchronously loads an object of a specified class to an item provider, returning a progress object.
- [loadTransferable(type:completionHandler:)](<loadtransferable(type_completionhandler_).md>) — Asynchronously loads an object of a specified transferable type to an item provider, returning a progress object.
