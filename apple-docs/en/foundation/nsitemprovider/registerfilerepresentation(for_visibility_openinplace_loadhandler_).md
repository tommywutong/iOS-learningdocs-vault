---
title: 'registerFileRepresentation(for:visibility:openInPlace:loadHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/registerfilerepresentation(for:visibility:openinplace:loadhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/registerfilerepresentation(for:visibility:openinplace:loadhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/registerfilerepresentation%28for%3Avisibility%3Aopeninplace%3Aloadhandler%3A%29.json'
content_hash: 'sha256:bd8863de33cf353c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# registerFileRepresentation(for:visibility:openInPlace:loadHandler:)

<sub>Instance Method</sub>

Registers a file-backed representation for an item with item visibility, an open-in-place option, and a load handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func registerFileRepresentation(for contentType: UTType, visibility: NSItemProviderRepresentationVisibility = .all, openInPlace: Bool = false, loadHandler: @escaping @Sendable (@escaping (URL?, Bool, (any Error)?) -> Void) -> Progress?)
```

## Discussion

If a destination app must access the represented file using a file coordinator, set the `coordinated` parameter in the load handler block to [true](../../swift/true.md).

To offer a representation backed by a file provider, return an [NSURL](../nsurl.md) object that points to your app’s file provider’s container. The file provider extension is then invoked to retrieve the file when requested.

To offer a representation backed by a file to open in place, set the fileOptions parameter to a value of [NSItemProviderFileOptionOpenInPlace](../nsitemproviderfileoptions/openinplace.md); in addition, return an [NSURL](../nsurl.md) object that points to your app’s file provider’s container. Open-in-place support requires that the file provider is visible in the Files app.

## See Also

### Registering files

- [- registerFileRepresentationForTypeIdentifier:fileOptions:visibility:loadHandler:](<registerfilerepresentation(fortypeidentifier_fileoptions_visibility_loadhandler_).md>) — Registers a file-backed representation for an item, specifying file options, item visibility, and a load handler.
