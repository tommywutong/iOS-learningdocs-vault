---
title: NSWhoseSpecifier.SubelementIdentifier
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nswhosespecifier/subelementidentifier
source_url: 'https://developer.apple.com/documentation/foundation/nswhosespecifier/subelementidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nswhosespecifier/subelementidentifier.json'
content_hash: 'sha256:9319871c3afcdd65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSWhoseSpecifier](../nswhosespecifier.md)

# NSWhoseSpecifier.SubelementIdentifier

<sub>Enumeration</sub>

`NSWhoseSpecifier` uses these constants to specify sub-elements within the collection of objects being tested that pass the specifier’s test.

<sub>Mac Catalyst, macOS</sub>

```swift
enum SubelementIdentifier
```

## Overview

These constants are used by [startSubelementIdentifier](startsubelementidentifier.md), [startSubelementIdentifier](startsubelementidentifier.md), [endSubelementIdentifier](endsubelementidentifier.md), and [endSubelementIdentifier](endsubelementidentifier.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSIndexSubelement](subelementidentifier/indexsubelement.md) — An element at a given index that meets the specifier test.
- [NSEverySubelement](subelementidentifier/everysubelement.md) — Every element that meets the specifier test.
- [NSMiddleSubelement](subelementidentifier/middlesubelement.md) — The middle element that meets the specifier test.
- [NSRandomSubelement](subelementidentifier/randomsubelement.md) — Any element that meets the specifier test.
- [NSNoSubelement](subelementidentifier/nosubelement.md) — No sub-element met the specifier test. Valid only for specifying the end sub-element.; that is, there is no end, so consider all elements.

### Initializers

- [init(rawValue:)](<subelementidentifier/init(rawvalue_).md>)
