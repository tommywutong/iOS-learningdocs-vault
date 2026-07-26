---
title: CIDynamicRangeOption
framework: Core Image
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cidynamicrangeoption
source_url: 'https://developer.apple.com/documentation/coreimage/cidynamicrangeoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidynamicrangeoption.json'
content_hash: 'sha256:bea7d1142b96af31'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIDynamicRangeOption

<sub>Structure</sub>

An enum string type that your code can use to select different System Tone Mapping modes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct CIDynamicRangeOption
```

## Overview

These options are consistent with the analogous options available in Core Graphics, Core Animation, AppKit, UIKit, and SwiftUI, In Core Image, this option can be set on the `CISystemToneMap` filter.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [kCIDynamicRangeStandard](cidynamicrangeoption/standard.md) — Use Standard dynamic range.
- [kCIDynamicRangeConstrainedHigh](cidynamicrangeoption/constrainedhigh.md) — Use extended dynamic range, but brightness is modulated to optimize for co-existence with other composited content.
- [kCIDynamicRangeHigh](cidynamicrangeoption/high.md) — Use High dynamic range.

### Initializers

- [init(rawValue:)](<cidynamicrangeoption/init(rawvalue_).md>)
