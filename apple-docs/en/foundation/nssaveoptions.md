---
title: NSSaveOptions
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nssaveoptions
source_url: 'https://developer.apple.com/documentation/foundation/nssaveoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssaveoptions.json'
content_hash: 'sha256:9fa83a94958e8fda'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSSaveOptions

<sub>Enumeration</sub>

The [saveOptions](nsclosecommand/saveoptions.md) method returns one of the following constants to indicate how to deal with saving any modified documents:

<sub>Mac Catalyst, macOS</sub>

```swift
enum NSSaveOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [NSSaveOptionsYes](nssaveoptions/yes.md) — Indicates a modified document should be saved on closing without asking the user.
- [NSSaveOptionsNo](nssaveoptions/no.md) — Indicates a modified document should not be saved on closing.
- [NSSaveOptionsAsk](nssaveoptions/ask.md) — Indicates the user should be asked before saving any modified documents on closing. When no option is specified, this is the default.

### Initializers

- [init(rawValue:)](<nssaveoptions/init(rawvalue_).md>)
