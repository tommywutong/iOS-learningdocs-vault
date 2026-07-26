---
title: CTRunStatus
framework: Core Text
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctrunstatus
source_url: 'https://developer.apple.com/documentation/coretext/ctrunstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrunstatus.json'
content_hash: 'sha256:8f62ad62f3134b9a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRunStatus

<sub>Structure</sub>

A bitfield that represents the disposition of the run.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CTRunStatus
```

## Overview

The [CTRunGetStatus](<ctrungetstatus(__).md>) function passes back this bitfield to indicate the disposition of the run.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [kCTRunStatusRightToLeft](ctrunstatus/righttoleft.md) — The run proceeds from right to left.
- [kCTRunStatusNonMonotonic](ctrunstatus/nonmonotonic.md) — The run isn’t in strictly increasing or decreasing order.
- [kCTRunStatusHasNonIdentityMatrix](ctrunstatus/hasnonidentitymatrix.md) — The run requires a specific text matrix to be set in the current Core Graphics context for proper drawing.

### Initializers

- [init(rawValue:)](<ctrunstatus/init(rawvalue_).md>) — Creates a run status structure with the specified raw value.
