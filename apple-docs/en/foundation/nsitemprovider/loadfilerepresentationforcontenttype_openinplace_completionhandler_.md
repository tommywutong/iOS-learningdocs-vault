---
title: 'loadFileRepresentationForContentType:openInPlace:completionHandler:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/loadfilerepresentationforcontenttype:openinplace:completionhandler:'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/loadfilerepresentationforcontenttype:openinplace:completionhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/loadfilerepresentationforcontenttype%3Aopeninplace%3Acompletionhandler%3A.json'
content_hash: 'sha256:b5d10fd262d009e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# loadFileRepresentationForContentType:openInPlace:completionHandler:

<sub>Instance Method</sub>

Asynchronously copies the content type data into a generic data object with the specified parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSProgress *) loadFileRepresentationForContentType:(UTType *) contentType openInPlace:(BOOL) openInPlace completionHandler:(void (^)(NSURL *URL, BOOL openInPlace, NSError *error)) completionHandler;
```

## See Also

### Loading the provider’s contents

- [- loadItemForTypeIdentifier:options:completionHandler:](<loaditem(fortypeidentifier_options_completionhandler_).md>) — Loads the item’s data and coerces it to the specified type. _(deprecated)_
- [- loadDataRepresentationForTypeIdentifier:completionHandler:](<loaddatarepresentation(fortypeidentifier_completionhandler_).md>) — Asynchronously copies the provided, typed data into a generic data object, returning a progress object.
- [loadDataRepresentationForContentType:completionHandler:](loaddatarepresentationforcontenttype_completionhandler_.md) — Asynchronously copies the provided, typed data into a generic data object, returning a progress object.
- [- loadFileRepresentationForTypeIdentifier:completionHandler:](<loadfilerepresentation(fortypeidentifier_completionhandler_).md>) — Asynchronously writes a copy of the provided, typed data to a temporary file, returning a progress object.
- [- loadInPlaceFileRepresentationForTypeIdentifier:completionHandler:](<loadinplacefilerepresentation(fortypeidentifier_completionhandler_).md>) — Asynchronously opens a file in place, if possible, returning a progress object.
- [- loadObjectOfClass:completionHandler:](<loadobject(ofclass_completionhandler_)-8ak5d.md>) — Asynchronously loads an object of a specified class to an item provider, returning a progress object.
