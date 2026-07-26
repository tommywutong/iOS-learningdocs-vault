---
title: 'registerFileRepresentation(forTypeIdentifier:fileOptions:visibility:loadHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/registerfilerepresentation(fortypeidentifier:fileoptions:visibility:loadhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/registerfilerepresentation(fortypeidentifier:fileoptions:visibility:loadhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/registerfilerepresentation%28fortypeidentifier%3Afileoptions%3Avisibility%3Aloadhandler%3A%29.json'
content_hash: 'sha256:8c5f1f4a20a48a30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# registerFileRepresentation(forTypeIdentifier:fileOptions:visibility:loadHandler:)

<sub>Instance Method</sub>

Registers a file-backed representation for an item, specifying file options, item visibility, and a load handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func registerFileRepresentation(forTypeIdentifier typeIdentifier: String, fileOptions: NSItemProviderFileOptions = [], visibility: NSItemProviderRepresentationVisibility, loadHandler: @escaping @Sendable (@escaping @Sendable (URL?, Bool, (any Error)?) -> Void) -> Progress?)
```

## Discussion

If a destination app must access the represented file using a file coordinator, set the `coordinated` parameter in the load handler block to [true](../../swift/true.md).

To offer a representation backed by a file provider, return an [NSURL](../nsurl.md) object that points to your app’s file provider’s container. The file provider extension is then invoked to retrieve the file when requested.

To offer a representation backed by a file to open in place, set the fileOptions parameter to a value of [NSItemProviderFileOptionOpenInPlace](../nsitemproviderfileoptions/openinplace.md); in addition, return an [NSURL](../nsurl.md) object that points to your app’s file provider’s container. Open-in-place support requires that the file provider is visible in the Files app.

## See Also

### Registering files

- [registerFileRepresentation(for:visibility:openInPlace:loadHandler:)](<registerfilerepresentation(for_visibility_openinplace_loadhandler_).md>) — Registers a file-backed representation for an item with item visibility, an open-in-place option, and a load handler.
