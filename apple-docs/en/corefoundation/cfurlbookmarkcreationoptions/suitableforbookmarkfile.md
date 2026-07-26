---
title: suitableForBookmarkFile
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfurlbookmarkcreationoptions/suitableforbookmarkfile
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions/suitableforbookmarkfile'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlbookmarkcreationoptions/suitableforbookmarkfile.json'
content_hash: 'sha256:075678a4b2c402e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFURLBookmarkCreationOptions](../cfurlbookmarkcreationoptions.md)

# suitableForBookmarkFile

<sub>Type Property</sub>

Specifies that the bookmark data include properties required to create Finder alias files.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var suitableForBookmarkFile: CFURLBookmarkCreationOptions { get }
```

## See Also

### Constants

- [kCFURLBookmarkCreationPreferFileIDResolutionMask](preferfileidresolutionmask.md) — Specifies that an alias created with the bookmark data prefers resolving with its embedded file ID. _(deprecated)_
- [kCFURLBookmarkCreationMinimalBookmarkMask](minimalbookmarkmask.md) — Specifies that an alias created with the bookmark data be created with minimal information, which may make it smaller but still able to resolve in certain ways.
- [kCFURLBookmarkCreationWithSecurityScope](withsecurityscope.md) — Specifies that you want to create a security-scoped bookmark that, when resolved, provides a security-scoped URL allowing read/write access to a file-system resource; for use in an app that adopts App Sandbox.
- [kCFURLBookmarkCreationSecurityScopeAllowOnlyReadAccess](securityscopeallowonlyreadaccess.md) — When combined with the [kCFURLBookmarkCreationWithSecurityScope](withsecurityscope.md) option, specifies that you want to create a security-scoped bookmark that, when resolved, provides a security-scoped URL allowing read-only access to a file-system resource; for use in an app that adopts App Sandbox.
