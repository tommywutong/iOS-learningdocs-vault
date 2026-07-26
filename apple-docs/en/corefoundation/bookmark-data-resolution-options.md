---
title: Bookmark Data Resolution Options
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/bookmark-data-resolution-options
source_url: 'https://developer.apple.com/documentation/corefoundation/bookmark-data-resolution-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/bookmark-data-resolution-options.json'
content_hash: 'sha256:b678b020db728dab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFURL](cfurl.md)

# Bookmark Data Resolution Options

<sub>API Collection</sub>

Options used when resolving bookmark data.

## Overview

When resolving a bookmark to obtain a URL, use bitwise `OR` operators to combine the options you want to specify, and provide them to the `options` parameter of the [CFURLCreateByResolvingBookmarkData](<cfurlcreatebyresolvingbookmarkdata(______________).md>) function.

### Version-Notes

Security-scoped bookmarks are not available in versions of macOS prior to OS X v10.7.3.

## Topics

### Constants

- [kCFBookmarkResolutionWithoutUIMask](cfurlbookmarkresolutionoptions/cfbookmarkresolutionwithoutuimask.md) — Specifies that no UI feedback accompany resolution of the bookmark data.
- [kCFBookmarkResolutionWithoutMountingMask](cfurlbookmarkresolutionoptions/cfbookmarkresolutionwithoutmountingmask.md) — Specifies that no volume should be mounted during resolution of the bookmark data.
- [kCFURLBookmarkResolutionWithSecurityScope](cfurlbookmarkresolutionoptions/cfurlbookmarkresolutionwithsecurityscope.md) — Specifies that the security scope, applied to the bookmark when it was created, should be used during resolution of the bookmark data.

## See Also

### Bookmark Data Constants

- [Bookmark Data Creation Options](bookmark-data-creation-options.md) — Options used when creating bookmark data.
