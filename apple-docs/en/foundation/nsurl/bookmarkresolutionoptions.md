---
title: NSURL.BookmarkResolutionOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurl/bookmarkresolutionoptions
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/bookmarkresolutionoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/bookmarkresolutionoptions.json'
content_hash: 'sha256:8024e1ae14c42376'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# NSURL.BookmarkResolutionOptions

<sub>Structure</sub>

Options used when resolving bookmark data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct BookmarkResolutionOptions
```

## Overview

When resolving a bookmark, use bitwise `OR` operators to combine the options you want to specify, and provide them to the `options` parameter of the [URLByResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:error:](urlbyresolvingbookmarkdata_options_relativetourl_bookmarkdataisstale_error_.md) method.

### Version-Notes

Security-scoped bookmarks are not available in versions of macOS prior to OS X 10.7.3.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<bookmarkresolutionoptions/init(rawvalue_).md>) — Initializes a new resolution options structure.

### Constants

- [NSURLBookmarkResolutionWithoutUI](bookmarkresolutionoptions/withoutui.md) — Specifies that no UI feedback should accompany resolution of the bookmark data.
- [NSURLBookmarkResolutionWithoutMounting](bookmarkresolutionoptions/withoutmounting.md) — Specifies that no volume should be mounted during resolution of the bookmark data.
- [NSURLBookmarkResolutionWithSecurityScope](bookmarkresolutionoptions/withsecurityscope.md) — Specifies that the security scope, applied to the bookmark when it was created, should be used during resolution of the bookmark data.
- [NSURLBookmarkResolutionWithoutImplicitStartAccessing](bookmarkresolutionoptions/withoutimplicitstartaccessing.md) — A property that specifies that resolution doesn’t implicitly start accessing the ephemeral security-scoped resource.

## See Also

### Working with Bookmark Data

- [+ bookmarkDataWithContentsOfURL:error:](<bookmarkdata(withcontentsof_).md>) — Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.
- [- bookmarkDataWithOptions:includingResourceValuesForKeys:relativeToURL:error:](<bookmarkdata(options_includingresourcevaluesforkeys_relativeto_).md>) — Returns a bookmark for the URL, created with specified options and resource values.
- [+ resourceValuesForKeys:fromBookmarkData:](<resourcevalues(forkeys_frombookmarkdata_).md>) — Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [+ writeBookmarkData:toURL:options:error:](<writebookmarkdata(__to_options_).md>) — Creates an alias file on disk at a specified location with specified bookmark data.
- [- startAccessingSecurityScopedResource](<startaccessingsecurityscopedresource().md>) — In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
- [- stopAccessingSecurityScopedResource](<stopaccessingsecurityscopedresource().md>) — In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.
- [BookmarkFileCreationOptions](bookmarkfilecreationoptions.md) — Options used when creating file bookmark data
- [BookmarkCreationOptions](bookmarkcreationoptions.md) — Options used when creating bookmark data.
