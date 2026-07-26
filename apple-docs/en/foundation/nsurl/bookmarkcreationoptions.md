---
title: NSURL.BookmarkCreationOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurl/bookmarkcreationoptions
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/bookmarkcreationoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/bookmarkcreationoptions.json'
content_hash: 'sha256:2ba113e6d0cfdf1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# NSURL.BookmarkCreationOptions

<sub>Structure</sub>

Options used when creating bookmark data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct BookmarkCreationOptions
```

## Overview

When creating a bookmark, use bitwise `OR` operators to combine the options you want to specify, and provide them to the `options` parameter of the [- bookmarkDataWithOptions:includingResourceValuesForKeys:relativeToURL:error:](<bookmarkdata(options_includingresourcevaluesforkeys_relativeto_).md>) method.

> [!note] Note
> Security-scoped bookmarks aren’t available in versions of macOS prior to 10.7.3.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Creating a bookmark creation option

- [init(rawValue:)](<bookmarkcreationoptions/init(rawvalue_).md>) — Initializes a new bookmark creation options structure.

### Options

- [NSURLBookmarkCreationMinimalBookmark](bookmarkcreationoptions/minimalbookmark.md) — Specifies that when creating a bookmark, it includes minimal information.
- [NSURLBookmarkCreationSuitableForBookmarkFile](bookmarkcreationoptions/suitableforbookmarkfile.md) — Specifies that the bookmark data includes the required properties for creating Finder alias files.
- [NSURLBookmarkCreationWithSecurityScope](bookmarkcreationoptions/withsecurityscope.md) — Specifies that when creating a security-scoped bookmark, upon resolution, it provides a security-scoped URL allowing read/write access to a file-system resource.
- [NSURLBookmarkCreationSecurityScopeAllowOnlyReadAccess](bookmarkcreationoptions/securityscopeallowonlyreadaccess.md) — Specifies that when creating a security-scoped bookmark, upon resolution, it provides a security-scoped URL allowing read-only access to a file-system resource.
- [NSURLBookmarkCreationWithoutImplicitSecurityScope](bookmarkcreationoptions/withoutimplicitsecurityscope.md) — Prevents inclusion of a bookmark’s implicit ephemeral security scope, when creating one without security scope.
- [NSURLBookmarkCreationPreferFileIDResolution](bookmarkcreationoptions/preferfileidresolution.md) — Specifies that when creating a bookmark, upon resolution, its embedded file ID takes precedence over other sources of information (file system path, for example) when there’s a conflict. _(deprecated)_

## See Also

### Working with Bookmark Data

- [+ bookmarkDataWithContentsOfURL:error:](<bookmarkdata(withcontentsof_).md>) — Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.
- [- bookmarkDataWithOptions:includingResourceValuesForKeys:relativeToURL:error:](<bookmarkdata(options_includingresourcevaluesforkeys_relativeto_).md>) — Returns a bookmark for the URL, created with specified options and resource values.
- [+ resourceValuesForKeys:fromBookmarkData:](<resourcevalues(forkeys_frombookmarkdata_).md>) — Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [+ writeBookmarkData:toURL:options:error:](<writebookmarkdata(__to_options_).md>) — Creates an alias file on disk at a specified location with specified bookmark data.
- [- startAccessingSecurityScopedResource](<startaccessingsecurityscopedresource().md>) — In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
- [- stopAccessingSecurityScopedResource](<stopaccessingsecurityscopedresource().md>) — In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.
- [BookmarkFileCreationOptions](bookmarkfilecreationoptions.md) — Options used when creating file bookmark data
- [BookmarkResolutionOptions](bookmarkresolutionoptions.md) — Options used when resolving bookmark data.
