---
title: CFURLError
framework: Core Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+（7.0 起废弃）, iPadOS 2.0+（7.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/cfurlerror
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlerror.json'
content_hash: 'sha256:0b3c864e5c7beee6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLError

<sub>Enumeration</sub>

`CFURL` error codes.

> [!warning] Deprecated
> Use CFError codes instead

<sub>tvOS, visionOS, watchOS</sub>

```swift
enum CFURLError
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCFURLUnknownError](cfurlerror/unknownerror.md) — Indicates an unknown error. _(deprecated)_
- [kCFURLUnknownSchemeError](cfurlerror/unknownschemeerror.md) — Indicates that the scheme is not recognized. _(deprecated)_
- [kCFURLResourceNotFoundError](cfurlerror/resourcenotfounderror.md) — Indicates a resource was not found. _(deprecated)_
- [kCFURLResourceAccessViolationError](cfurlerror/resourceaccessviolationerror.md) — Indicates an error in accessing a resource. _(deprecated)_
- [kCFURLRemoteHostUnavailableError](cfurlerror/remotehostunavailableerror.md) — Indicates a remote host is unavailable. _(deprecated)_
- [kCFURLImproperArgumentsError](cfurlerror/improperargumentserror.md) — Indicates one or more arguments are improper. _(deprecated)_
- [kCFURLUnknownPropertyKeyError](cfurlerror/unknownpropertykeyerror.md) — Indicates a property key is unknown. _(deprecated)_
- [kCFURLPropertyKeyUnavailableError](cfurlerror/propertykeyunavailableerror.md) — Indicates a property key was unavailable. _(deprecated)_
- [kCFURLTimeoutError](cfurlerror/timeouterror.md) — Indicates a timeout. _(deprecated)_

### Initializers

- [init(rawValue:)](<cfurlerror/init(rawvalue_).md>) _(deprecated)_

## See Also

### Constants

- [File URL Properties](file-url-properties.md) — Properties for file URL resources.
- [HTTP URL Properties](http-url-properties.md) — Properties for HTTP URL resources.
