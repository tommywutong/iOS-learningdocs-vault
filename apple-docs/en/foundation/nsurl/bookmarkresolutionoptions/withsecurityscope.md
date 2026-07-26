---
title: withSecurityScope
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.7+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurl/bookmarkresolutionoptions/withsecurityscope
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/bookmarkresolutionoptions/withsecurityscope'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/bookmarkresolutionoptions/withsecurityscope.json'
content_hash: 'sha256:5f76fe84653b8fd2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSURL](../../nsurl.md) · [BookmarkResolutionOptions](../bookmarkresolutionoptions.md)

# withSecurityScope

<sub>Type Property</sub>

Specifies that the security scope, applied to the bookmark when it was created, should be used during resolution of the bookmark data.

<sub>Mac Catalyst, macOS</sub>

```swift
static var withSecurityScope: NSURL.BookmarkResolutionOptions { get }
```

## See Also

### Constants

- [NSURLBookmarkResolutionWithoutUI](withoutui.md) — Specifies that no UI feedback should accompany resolution of the bookmark data.
- [NSURLBookmarkResolutionWithoutMounting](withoutmounting.md) — Specifies that no volume should be mounted during resolution of the bookmark data.
- [NSURLBookmarkResolutionWithoutImplicitStartAccessing](withoutimplicitstartaccessing.md) — A property that specifies that resolution doesn’t implicitly start accessing the ephemeral security-scoped resource.
