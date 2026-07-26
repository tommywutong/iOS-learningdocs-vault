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
doc_path: /documentation/foundation/nsurl/bookmarkcreationoptions/withsecurityscope
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/bookmarkcreationoptions/withsecurityscope'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/bookmarkcreationoptions/withsecurityscope.json'
content_hash: 'sha256:38e7643ce8d4ad27'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSURL](../../nsurl.md) · [BookmarkCreationOptions](../bookmarkcreationoptions.md)

# withSecurityScope

<sub>Type Property</sub>

Specifies that when creating a security-scoped bookmark, upon resolution, it provides a security-scoped URL allowing read/write access to a file-system resource.

<sub>Mac Catalyst, macOS</sub>

```swift
static var withSecurityScope: NSURL.BookmarkCreationOptions { get }
```

## Discussion

For use in an app that adopts App Sandbox. For more information, see [App Sandbox Design Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183).

> [!note] Note
> This flag can’t be used in conjunction with either [NSURLBookmarkCreationMinimalBookmark](minimalbookmark.md) or [NSURLBookmarkCreationSuitableForBookmarkFile](suitableforbookmarkfile.md).

## See Also

### Options

- [NSURLBookmarkCreationMinimalBookmark](minimalbookmark.md) — Specifies that when creating a bookmark, it includes minimal information.
- [NSURLBookmarkCreationSuitableForBookmarkFile](suitableforbookmarkfile.md) — Specifies that the bookmark data includes the required properties for creating Finder alias files.
- [NSURLBookmarkCreationSecurityScopeAllowOnlyReadAccess](securityscopeallowonlyreadaccess.md) — Specifies that when creating a security-scoped bookmark, upon resolution, it provides a security-scoped URL allowing read-only access to a file-system resource.
- [NSURLBookmarkCreationWithoutImplicitSecurityScope](withoutimplicitsecurityscope.md) — Prevents inclusion of a bookmark’s implicit ephemeral security scope, when creating one without security scope.
- [NSURLBookmarkCreationPreferFileIDResolution](preferfileidresolution.md) — Specifies that when creating a bookmark, upon resolution, its embedded file ID takes precedence over other sources of information (file system path, for example) when there’s a conflict. _(deprecated)_
