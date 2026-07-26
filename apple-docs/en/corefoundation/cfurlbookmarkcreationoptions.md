---
title: CFURLBookmarkCreationOptions
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfurlbookmarkcreationoptions
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlbookmarkcreationoptions.json'
content_hash: 'sha256:8b5097f7af32f7d1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLBookmarkCreationOptions

<sub>Structure</sub>

Type for bookmark data creation options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFURLBookmarkCreationOptions
```

## Overview

See [Bookmark Data Creation Options](bookmark-data-creation-options.md) for possible values.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<cfurlbookmarkcreationoptions/init(rawvalue_).md>)

### Type Properties

- [kCFURLBookmarkCreationMinimalBookmarkMask](cfurlbookmarkcreationoptions/minimalbookmarkmask.md) — Specifies that an alias created with the bookmark data be created with minimal information, which may make it smaller but still able to resolve in certain ways.
- [kCFURLBookmarkCreationPreferFileIDResolutionMask](cfurlbookmarkcreationoptions/preferfileidresolutionmask.md) — Specifies that an alias created with the bookmark data prefers resolving with its embedded file ID. _(deprecated)_
- [kCFURLBookmarkCreationSecurityScopeAllowOnlyReadAccess](cfurlbookmarkcreationoptions/securityscopeallowonlyreadaccess.md) — When combined with the [kCFURLBookmarkCreationWithSecurityScope](cfurlbookmarkcreationoptions/withsecurityscope.md) option, specifies that you want to create a security-scoped bookmark that, when resolved, provides a security-scoped URL allowing read-only access to a file-system resource; for use in an app that adopts App Sandbox.
- [kCFURLBookmarkCreationSuitableForBookmarkFile](cfurlbookmarkcreationoptions/suitableforbookmarkfile.md) — Specifies that the bookmark data include properties required to create Finder alias files.
- [kCFURLBookmarkCreationWithSecurityScope](cfurlbookmarkcreationoptions/withsecurityscope.md) — Specifies that you want to create a security-scoped bookmark that, when resolved, provides a security-scoped URL allowing read/write access to a file-system resource; for use in an app that adopts App Sandbox.
- [kCFURLBookmarkCreationWithoutImplicitSecurityScope](cfurlbookmarkcreationoptions/withoutimplicitsecurityscope.md)

## See Also

### Bookmark Data Types

- [CFURLBookmarkFileCreationOptions](cfurlbookmarkfilecreationoptions.md) — Type for bookmark file creation options.
- [CFURLBookmarkResolutionOptions](cfurlbookmarkresolutionoptions.md) — Type for bookmark data resolution options.
