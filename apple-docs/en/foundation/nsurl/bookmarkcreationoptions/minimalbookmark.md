---
title: minimalBookmark
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurl/bookmarkcreationoptions/minimalbookmark
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/bookmarkcreationoptions/minimalbookmark'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/bookmarkcreationoptions/minimalbookmark.json'
content_hash: 'sha256:c23cafe4764984b1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSURL](../../nsurl.md) · [BookmarkCreationOptions](../bookmarkcreationoptions.md)

# minimalBookmark

<sub>Type Property</sub>

Specifies that when creating a bookmark, it includes minimal information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var minimalBookmark: NSURL.BookmarkCreationOptions { get }
```

## Discussion

This produces a smaller bookmark that can be resolved in fewer ways.

## See Also

### Options

- [NSURLBookmarkCreationSuitableForBookmarkFile](suitableforbookmarkfile.md) — Specifies that the bookmark data includes the required properties for creating Finder alias files.
- [NSURLBookmarkCreationWithSecurityScope](withsecurityscope.md) — Specifies that when creating a security-scoped bookmark, upon resolution, it provides a security-scoped URL allowing read/write access to a file-system resource.
- [NSURLBookmarkCreationSecurityScopeAllowOnlyReadAccess](securityscopeallowonlyreadaccess.md) — Specifies that when creating a security-scoped bookmark, upon resolution, it provides a security-scoped URL allowing read-only access to a file-system resource.
- [NSURLBookmarkCreationWithoutImplicitSecurityScope](withoutimplicitsecurityscope.md) — Prevents inclusion of a bookmark’s implicit ephemeral security scope, when creating one without security scope.
- [NSURLBookmarkCreationPreferFileIDResolution](preferfileidresolution.md) — Specifies that when creating a bookmark, upon resolution, its embedded file ID takes precedence over other sources of information (file system path, for example) when there’s a conflict. _(deprecated)_
