---
title: 'init(resolvingAliasFileAt:options:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/init(resolvingaliasfileat:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/init(resolvingaliasfileat:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/init%28resolvingaliasfileat%3Aoptions%3A%29.json'
content_hash: 'sha256:bb65cdaf611c4ed7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# init(resolvingAliasFileAt:options:)

<sub>Initializer</sub>

Creates a URL that refers to the location specified by resolving an alias file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(resolvingAliasFileAt url: URL, options: URL.BookmarkResolutionOptions = []) throws
```

## Discussion

If the `url` argument doesn’t refer to an alias file (as defined by the [NSURLIsAliasFileKey](../urlresourcekey/isaliasfilekey.md) property), the returned URL is the same as the `url` argument.

This method throws an error in the following cases:

- The url argument is unreachable.
- The original file or directory is unknown or unreachable.
- The original file or directory is on a volume that the system can’t locate or can’t mount.

This method doesn’t support the [NSURLBookmarkResolutionWithSecurityScope](../nsurl/bookmarkresolutionoptions/withsecurityscope.md) option.

## See Also

### Creating a URL by resolving a bookmark

- [init(resolvingBookmarkData:options:relativeTo:bookmarkDataIsStale:)](<init(resolvingbookmarkdata_options_relativeto_bookmarkdataisstale_)-3ic6f.md>) — Creates a URL that refers to a location specified by resolving bookmark data.
- [BookmarkResolutionOptions](bookmarkresolutionoptions.md) — An alias for the bookmark resolution options type.
- [BookmarkResolutionOptions](../nsurl/bookmarkresolutionoptions.md) — Options used when resolving bookmark data.
