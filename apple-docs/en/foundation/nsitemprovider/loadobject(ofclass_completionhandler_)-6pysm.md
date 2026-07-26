---
title: 'loadObject(ofClass:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/loadobject(ofclass:completionhandler:)-6pysm'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/loadobject(ofclass:completionhandler:)-6pysm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/loadobject%28ofclass%3Acompletionhandler%3A%29-6pysm.json'
content_hash: 'sha256:a04c0e1e3684b33f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# loadObject(ofClass:completionHandler:)

<sub>Instance Method</sub>

Asynchronously loads an object of a specified class to an item provider, returning a progress object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func loadObject<T>(ofClass: T.Type, completionHandler: @escaping @Sendable (T?, (any Error)?) -> Void) -> Progress where T : _ObjectiveCBridgeable, T._ObjectiveCType : NSItemProviderReading
```

## See Also

### Loading the provider’s contents

- [- loadItemForTypeIdentifier:options:completionHandler:](<loaditem(fortypeidentifier_options_completionhandler_).md>) — Loads the item’s data and coerces it to the specified type. _(deprecated)_
- [- loadDataRepresentationForTypeIdentifier:completionHandler:](<loaddatarepresentation(fortypeidentifier_completionhandler_).md>) — Asynchronously copies the provided, typed data into a generic data object, returning a progress object.
- [loadDataRepresentation(for:completionHandler:)](<loaddatarepresentation(for_completionhandler_).md>) — Asynchronously copies the universal type data into a generic data object, returning a progress object.
- [- loadFileRepresentationForTypeIdentifier:completionHandler:](<loadfilerepresentation(fortypeidentifier_completionhandler_).md>) — Asynchronously writes a copy of the provided, typed data to a temporary file, returning a progress object.
- [loadFileRepresentation(for:openInPlace:completionHandler:)](<loadfilerepresentation(for_openinplace_completionhandler_).md>) — Asynchronously writes a copy of the universal type data to a temporary file, returning a progress object.
- [- loadInPlaceFileRepresentationForTypeIdentifier:completionHandler:](<loadinplacefilerepresentation(fortypeidentifier_completionhandler_).md>) — Asynchronously opens a file in place, if possible, returning a progress object.
- [- loadObjectOfClass:completionHandler:](<loadobject(ofclass_completionhandler_)-8ak5d.md>) — Asynchronously loads an object of a specified class to an item provider, returning a progress object.
- [loadTransferable(type:completionHandler:)](<loadtransferable(type_completionhandler_).md>) — Asynchronously loads an object of a specified transferable type to an item provider, returning a progress object.
