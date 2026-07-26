---
title: preferFileIDResolutionMask
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, tvOS 9.0+, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/cfurlbookmarkcreationoptions/preferfileidresolutionmask
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions/preferfileidresolutionmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlbookmarkcreationoptions/preferfileidresolutionmask.json'
content_hash: 'sha256:c0db7ef6a024fec3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFURLBookmarkCreationOptions](../cfurlbookmarkcreationoptions.md)

# preferFileIDResolutionMask

<sub>Type Property</sub>

Specifies that an alias created with the bookmark data prefers resolving with its embedded file ID.

> [!warning] Deprecated
> kCFURLBookmarkCreationPreferFileIDResolutionMask does nothing and has no effect on bookmark resolution

<sub>tvOS, visionOS, watchOS</sub>

```swift
static var preferFileIDResolutionMask: CFURLBookmarkCreationOptions { get }
```

## See Also

### Constants

- [kCFURLBookmarkCreationMinimalBookmarkMask](minimalbookmarkmask.md) — Specifies that an alias created with the bookmark data be created with minimal information, which may make it smaller but still able to resolve in certain ways.
- [kCFURLBookmarkCreationSuitableForBookmarkFile](suitableforbookmarkfile.md) — Specifies that the bookmark data include properties required to create Finder alias files.
- [kCFURLBookmarkCreationWithSecurityScope](withsecurityscope.md) — Specifies that you want to create a security-scoped bookmark that, when resolved, provides a security-scoped URL allowing read/write access to a file-system resource; for use in an app that adopts App Sandbox.
- [kCFURLBookmarkCreationSecurityScopeAllowOnlyReadAccess](securityscopeallowonlyreadaccess.md) — When combined with the [kCFURLBookmarkCreationWithSecurityScope](withsecurityscope.md) option, specifies that you want to create a security-scoped bookmark that, when resolved, provides a security-scoped URL allowing read-only access to a file-system resource; for use in an app that adopts App Sandbox.
