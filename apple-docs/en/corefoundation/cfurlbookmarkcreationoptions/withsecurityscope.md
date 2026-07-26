---
title: withSecurityScope
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.7+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfurlbookmarkcreationoptions/withsecurityscope
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions/withsecurityscope'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlbookmarkcreationoptions/withsecurityscope.json'
content_hash: 'sha256:70249c0bc56001ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFURLBookmarkCreationOptions](../cfurlbookmarkcreationoptions.md)

# withSecurityScope

<sub>Type Property</sub>

Specifies that you want to create a security-scoped bookmark that, when resolved, provides a security-scoped URL allowing read/write access to a file-system resource; for use in an app that adopts App Sandbox.

<sub>Mac Catalyst, macOS</sub>

```swift
static var withSecurityScope: CFURLBookmarkCreationOptions { get }
```

## See Also

### Constants

- [kCFURLBookmarkCreationPreferFileIDResolutionMask](preferfileidresolutionmask.md) — Specifies that an alias created with the bookmark data prefers resolving with its embedded file ID. _(deprecated)_
- [kCFURLBookmarkCreationMinimalBookmarkMask](minimalbookmarkmask.md) — Specifies that an alias created with the bookmark data be created with minimal information, which may make it smaller but still able to resolve in certain ways.
- [kCFURLBookmarkCreationSuitableForBookmarkFile](suitableforbookmarkfile.md) — Specifies that the bookmark data include properties required to create Finder alias files.
- [kCFURLBookmarkCreationSecurityScopeAllowOnlyReadAccess](securityscopeallowonlyreadaccess.md) — When combined with the [kCFURLBookmarkCreationWithSecurityScope](withsecurityscope.md) option, specifies that you want to create a security-scoped bookmark that, when resolved, provides a security-scoped URL allowing read-only access to a file-system resource; for use in an app that adopts App Sandbox.
