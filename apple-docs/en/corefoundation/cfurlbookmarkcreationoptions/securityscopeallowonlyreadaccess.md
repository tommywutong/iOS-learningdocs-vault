---
title: securityScopeAllowOnlyReadAccess
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.7+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfurlbookmarkcreationoptions/securityscopeallowonlyreadaccess
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions/securityscopeallowonlyreadaccess'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlbookmarkcreationoptions/securityscopeallowonlyreadaccess.json'
content_hash: 'sha256:3f430c6b26392e6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFURLBookmarkCreationOptions](../cfurlbookmarkcreationoptions.md)

# securityScopeAllowOnlyReadAccess

<sub>Type Property</sub>

When combined with the [kCFURLBookmarkCreationWithSecurityScope](withsecurityscope.md) option, specifies that you want to create a security-scoped bookmark that, when resolved, provides a security-scoped URL allowing read-only access to a file-system resource; for use in an app that adopts App Sandbox.

<sub>Mac Catalyst, macOS</sub>

```swift
static var securityScopeAllowOnlyReadAccess: CFURLBookmarkCreationOptions { get }
```

## See Also

### Constants

- [kCFURLBookmarkCreationPreferFileIDResolutionMask](preferfileidresolutionmask.md) — Specifies that an alias created with the bookmark data prefers resolving with its embedded file ID. _(deprecated)_
- [kCFURLBookmarkCreationMinimalBookmarkMask](minimalbookmarkmask.md) — Specifies that an alias created with the bookmark data be created with minimal information, which may make it smaller but still able to resolve in certain ways.
- [kCFURLBookmarkCreationSuitableForBookmarkFile](suitableforbookmarkfile.md) — Specifies that the bookmark data include properties required to create Finder alias files.
- [kCFURLBookmarkCreationWithSecurityScope](withsecurityscope.md) — Specifies that you want to create a security-scoped bookmark that, when resolved, provides a security-scoped URL allowing read/write access to a file-system resource; for use in an app that adopts App Sandbox.
