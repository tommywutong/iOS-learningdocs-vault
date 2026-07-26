---
title: withoutImplicitStartAccessing
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.2+, iPadOS 14.2+, Mac Catalyst 14.2+, macOS 11.2+, tvOS 14.2+, visionOS 1.0+, watchOS 7.2+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurl/bookmarkresolutionoptions/withoutimplicitstartaccessing
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/bookmarkresolutionoptions/withoutimplicitstartaccessing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/bookmarkresolutionoptions/withoutimplicitstartaccessing.json'
content_hash: 'sha256:8db0cfdedc372122'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSURL](../../nsurl.md) · [BookmarkResolutionOptions](../bookmarkresolutionoptions.md)

# withoutImplicitStartAccessing

<sub>Type Property</sub>

A property that specifies that resolution doesn’t implicitly start accessing the ephemeral security-scoped resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var withoutImplicitStartAccessing: NSURL.BookmarkResolutionOptions { get }
```

## Discussion

This option causes an implicit call to [- startAccessingSecurityScopedResource](<../startaccessingsecurityscopedresource().md>) on the returned URL when it’s ready to use the resource.

This option isn’t applicable to security-scoped bookmarks.

## See Also

### Constants

- [NSURLBookmarkResolutionWithoutUI](withoutui.md) — Specifies that no UI feedback should accompany resolution of the bookmark data.
- [NSURLBookmarkResolutionWithoutMounting](withoutmounting.md) — Specifies that no volume should be mounted during resolution of the bookmark data.
- [NSURLBookmarkResolutionWithSecurityScope](withsecurityscope.md) — Specifies that the security scope, applied to the bookmark when it was created, should be used during resolution of the bookmark data.
