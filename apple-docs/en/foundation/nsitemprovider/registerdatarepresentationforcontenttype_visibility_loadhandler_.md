---
title: 'registerDataRepresentationForContentType:visibility:loadHandler:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/registerdatarepresentationforcontenttype:visibility:loadhandler:'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/registerdatarepresentationforcontenttype:visibility:loadhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/registerdatarepresentationforcontenttype%3Avisibility%3Aloadhandler%3A.json'
content_hash: 'sha256:b0944adbf09a523a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# registerDataRepresentationForContentType:visibility:loadHandler:

<sub>Instance Method</sub>

Lazily registers an item, according to the item provider type coercion policy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) registerDataRepresentationForContentType:(UTType *) contentType visibility:(NSItemProviderRepresentationVisibility) visibility loadHandler:(NSProgress * (^)(void (^completionHandler)(NSData *data, NSError *error))) loadHandler;
```

## Parameters

- `contentType` — A string that represents the desired UTI.

- `visibility` — The [NSItemProviderRepresentationVisibility](../nsitemproviderrepresentationvisibility.md) setting.

- `loadHandler` — A block capable of returning the data item as the specified type. For information about implementing this block, see [LoadHandler](loadhandler.md).

## See Also

### Registering data

- [- registerDataRepresentationForTypeIdentifier:visibility:loadHandler:](<registerdatarepresentation(fortypeidentifier_visibility_loadhandler_).md>) — Registers a data-backed representation for an item, specifiying item visibility and a load handler.
- [- registerItemForTypeIdentifier:loadHandler:](<registeritem(fortypeidentifier_loadhandler_).md>) — Lazily registers an item, according to the item provider type coercion policy. _(deprecated)_
