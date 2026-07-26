---
title: NSParagraphStyle.TextTabType
framework: AppKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 10.0+（27.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/appkit/nsparagraphstyle/texttabtype
source_url: 'https://developer.apple.com/documentation/appkit/nsparagraphstyle/texttabtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsparagraphstyle/texttabtype.json'
content_hash: 'sha256:090df1529b3248d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSParagraphStyle](../nsparagraphstyle.md)

# NSParagraphStyle.TextTabType

<sub>Enumeration</sub>

Constants that specify the type of tab stop.

> [!warning] Deprecated
> Use NSTextAlignment-based API.

<sub>macOS</sub>

```swift
enum TextTabType
```

## Overview

The following mappings define the conversions between text alignment in [NSTextTab](../nstexttab.md) and tab stop types that [NSTextTab](../nstexttab.md) defines:

| Alignment | Tab stop type |
|---|---|
| [NSTextAlignmentLeft](../nstextalignment/left.md) | [NSLeftTabStopType](texttabtype/lefttabstoptype.md) |
| [NSTextAlignmentRight](../nstextalignment/right.md) | [NSRightTabStopType](texttabtype/righttabstoptype.md) |
| [NSTextAlignmentCenter](../nstextalignment/center.md) | [NSCenterTabStopType](texttabtype/centertabstoptype.md) |
| [NSTextAlignmentJustified](../nstextalignment/justified.md) | [NSLeftTabStopType](texttabtype/lefttabstoptype.md) |
| [NSTextAlignmentNatural](../nstextalignment/natural.md) | [NSLeftTabStopType](texttabtype/lefttabstoptype.md), or [NSRightTabStopType](texttabtype/righttabstoptype.md), depending on the user setting. |
| [NSTextAlignmentRight](../nstextalignment/right.md) with a terminator | [NSDecimalTabStopType](texttabtype/decimaltabstoptype.md) |

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSLeftTabStopType](texttabtype/lefttabstoptype.md) — A left-aligned tab stop. _(deprecated)_
- [NSRightTabStopType](texttabtype/righttabstoptype.md) — A right-aligned tab stop. _(deprecated)_
- [NSCenterTabStopType](texttabtype/centertabstoptype.md) — A center-aligned tab stop. _(deprecated)_
- [NSDecimalTabStopType](texttabtype/decimaltabstoptype.md) — A tab stop that aligns columns of numbers to each number’s decimal point. _(deprecated)_

### Initializers

- [init(rawValue:)](<texttabtype/init(rawvalue_).md>) _(deprecated)_

## See Also

### Accessing tab information

- [tabStops](tabstops.md) — The text tab objects that represent the paragraph’s tab stops.
- [defaultTabInterval](defaulttabinterval.md) — The documentwide default tab interval.
