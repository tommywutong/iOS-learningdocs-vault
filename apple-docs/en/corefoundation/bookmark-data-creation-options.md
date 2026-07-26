---
title: Bookmark Data Creation Options
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/bookmark-data-creation-options
source_url: 'https://developer.apple.com/documentation/corefoundation/bookmark-data-creation-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/bookmark-data-creation-options.json'
content_hash: 'sha256:978764520ef8cfe0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFURL](cfurl.md)

# Bookmark Data Creation Options

<sub>API Collection</sub>

Options used when creating bookmark data.

## Overview

When creating a bookmark, use bitwise `OR` operators to combine the options you want to specify, and provide them to the `options` parameter of the [CFURLCreateBookmarkData](<cfurlcreatebookmarkdata(____________).md>) method.

### Version-Notes

Security-scoped bookmarks are not available in versions of macOS prior to OS X v10.7.3.

## Topics

### Constants

- [kCFURLBookmarkCreationPreferFileIDResolutionMask](cfurlbookmarkcreationoptions/preferfileidresolutionmask.md) — Specifies that an alias created with the bookmark data prefers resolving with its embedded file ID. _(deprecated)_
- [kCFURLBookmarkCreationMinimalBookmarkMask](cfurlbookmarkcreationoptions/minimalbookmarkmask.md) — Specifies that an alias created with the bookmark data be created with minimal information, which may make it smaller but still able to resolve in certain ways.
- [kCFURLBookmarkCreationSuitableForBookmarkFile](cfurlbookmarkcreationoptions/suitableforbookmarkfile.md) — Specifies that the bookmark data include properties required to create Finder alias files.
- [kCFURLBookmarkCreationWithSecurityScope](cfurlbookmarkcreationoptions/withsecurityscope.md) — Specifies that you want to create a security-scoped bookmark that, when resolved, provides a security-scoped URL allowing read/write access to a file-system resource; for use in an app that adopts App Sandbox.
- [kCFURLBookmarkCreationSecurityScopeAllowOnlyReadAccess](cfurlbookmarkcreationoptions/securityscopeallowonlyreadaccess.md) — When combined with the [kCFURLBookmarkCreationWithSecurityScope](cfurlbookmarkcreationoptions/withsecurityscope.md) option, specifies that you want to create a security-scoped bookmark that, when resolved, provides a security-scoped URL allowing read-only access to a file-system resource; for use in an app that adopts App Sandbox.

## See Also

### Bookmark Data Constants

- [Bookmark Data Resolution Options](bookmark-data-resolution-options.md) — Options used when resolving bookmark data.
