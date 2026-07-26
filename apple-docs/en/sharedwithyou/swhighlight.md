---
title: SWHighlight
framework: Shared with You
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/sharedwithyou/swhighlight
source_url: 'https://developer.apple.com/documentation/sharedwithyou/swhighlight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/sharedwithyou/swhighlight.json'
content_hash: 'sha256:71be0364f4482815'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Shared with You](../sharedwithyou.md)

# SWHighlight

<sub>Class</sub>

An object that represents a universal link to share by any number of contacts in one or more conversations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class SWHighlight
```

## Overview

The system doesn’t expose the identities of the contacts to the app. It tracks shared universal links for the current user and determines which links to elevate for consumption in an app. When the system deems a link to be useful, it surfaces that link to the hosting app in the form of an `SWHighlight` object.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [SWCollaborationHighlight](swcollaborationhighlight.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Viewing highlight attributes

- [identifier](swhighlight/identifier.md) — The unique identifier for the highlight.
- [URL](swhighlight/url.md) — The surfaced content URL for the highlight.

### Initializers

- [init(coder:)](<swhighlight/init(coder_).md>)

## See Also

### Highlights

- [SWHighlightCenter](swhighlightcenter.md) — An object that contains a priority-ordered list of universal links to share with the current user.
