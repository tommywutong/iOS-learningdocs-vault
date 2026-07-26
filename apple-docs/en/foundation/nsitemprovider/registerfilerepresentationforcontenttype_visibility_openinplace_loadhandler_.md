---
title: 'registerFileRepresentationForContentType:visibility:openInPlace:loadHandler:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/registerfilerepresentationforcontenttype:visibility:openinplace:loadhandler:'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/registerfilerepresentationforcontenttype:visibility:openinplace:loadhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/registerfilerepresentationforcontenttype%3Avisibility%3Aopeninplace%3Aloadhandler%3A.json'
content_hash: 'sha256:7f7d4e894f051649'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# registerFileRepresentationForContentType:visibility:openInPlace:loadHandler:

<sub>Instance Method</sub>

Registers a file-backed representation for an item with item visibility, an open-in-place option, and a load handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) registerFileRepresentationForContentType:(UTType *) contentType visibility:(NSItemProviderRepresentationVisibility) visibility openInPlace:(BOOL) openInPlace loadHandler:(NSProgress * (^)(void (^completionHandler)(NSURL *fileURL, BOOL coordinated, NSError *error))) loadHandler;
```

## See Also

### Registering files

- [- registerFileRepresentationForTypeIdentifier:fileOptions:visibility:loadHandler:](<registerfilerepresentation(fortypeidentifier_fileoptions_visibility_loadhandler_).md>) — Registers a file-backed representation for an item, specifying file options, item visibility, and a load handler.
