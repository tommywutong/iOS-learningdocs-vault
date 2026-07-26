---
title: preferFileIDResolution
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsurl/bookmarkcreationoptions/preferfileidresolution
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/bookmarkcreationoptions/preferfileidresolution'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/bookmarkcreationoptions/preferfileidresolution.json'
content_hash: 'sha256:19ba7cb00d3833b7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSURL](../../nsurl.md) · [BookmarkCreationOptions](../bookmarkcreationoptions.md)

# preferFileIDResolution

<sub>Type Property</sub>

Specifies that when creating a bookmark, upon resolution, its embedded file ID takes precedence over other sources of information (file system path, for example) when there’s a conflict.

> [!warning] Deprecated
> This option does nothing and has no effect on bookmark resolution.

<sub>tvOS, visionOS, watchOS</sub>

```swift
static var preferFileIDResolution: NSURL.BookmarkCreationOptions { get }
```

## See Also

### Options

- [NSURLBookmarkCreationMinimalBookmark](minimalbookmark.md) — Specifies that when creating a bookmark, it includes minimal information.
- [NSURLBookmarkCreationSuitableForBookmarkFile](suitableforbookmarkfile.md) — Specifies that the bookmark data includes the required properties for creating Finder alias files.
- [NSURLBookmarkCreationWithSecurityScope](withsecurityscope.md) — Specifies that when creating a security-scoped bookmark, upon resolution, it provides a security-scoped URL allowing read/write access to a file-system resource.
- [NSURLBookmarkCreationSecurityScopeAllowOnlyReadAccess](securityscopeallowonlyreadaccess.md) — Specifies that when creating a security-scoped bookmark, upon resolution, it provides a security-scoped URL allowing read-only access to a file-system resource.
- [NSURLBookmarkCreationWithoutImplicitSecurityScope](withoutimplicitsecurityscope.md) — Prevents inclusion of a bookmark’s implicit ephemeral security scope, when creating one without security scope.
