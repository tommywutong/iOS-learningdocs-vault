---
title: withoutImplicitSecurityScope
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurl/bookmarkcreationoptions/withoutimplicitsecurityscope
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/bookmarkcreationoptions/withoutimplicitsecurityscope'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/bookmarkcreationoptions/withoutimplicitsecurityscope.json'
content_hash: 'sha256:3f187101ee598139'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSURL](../../nsurl.md) · [BookmarkCreationOptions](../bookmarkcreationoptions.md)

# withoutImplicitSecurityScope

<sub>Type Property</sub>

Prevents inclusion of a bookmark’s implicit ephemeral security scope, when creating one without security scope.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var withoutImplicitSecurityScope: NSURL.BookmarkCreationOptions { get }
```

## Discussion

Bookmarks that you create without security scope automatically carry implicit ephemeral security scope. This security scope is valid until reboot at the latest, and confers access to the resource to any other process that resolves the bookmark. Using this option prevents inclusion of this ephemeral security scope.

When using this option, other processes can’t call [- startAccessingSecurityScopedResource](<../startaccessingsecurityscopedresource().md>) on the resolved URL. The option prevents providing unintended access to resources to other processes, and is also a performance optimization that reduces the size of the bookmark.

## See Also

### Options

- [NSURLBookmarkCreationMinimalBookmark](minimalbookmark.md) — Specifies that when creating a bookmark, it includes minimal information.
- [NSURLBookmarkCreationSuitableForBookmarkFile](suitableforbookmarkfile.md) — Specifies that the bookmark data includes the required properties for creating Finder alias files.
- [NSURLBookmarkCreationWithSecurityScope](withsecurityscope.md) — Specifies that when creating a security-scoped bookmark, upon resolution, it provides a security-scoped URL allowing read/write access to a file-system resource.
- [NSURLBookmarkCreationSecurityScopeAllowOnlyReadAccess](securityscopeallowonlyreadaccess.md) — Specifies that when creating a security-scoped bookmark, upon resolution, it provides a security-scoped URL allowing read-only access to a file-system resource.
- [NSURLBookmarkCreationPreferFileIDResolution](preferfileidresolution.md) — Specifies that when creating a bookmark, upon resolution, its embedded file ID takes precedence over other sources of information (file system path, for example) when there’s a conflict. _(deprecated)_
