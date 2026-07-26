---
title: ImmersionChangeContext
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 26.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/immersionchangecontext
source_url: 'https://developer.apple.com/documentation/swiftui/immersionchangecontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersionchangecontext.json'
content_hash: 'sha256:ba979124993714ac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ImmersionChangeContext

<sub>Structure</sub>

A structure that represents a state of immersion of your app.

<sub>macOS, visionOS</sub>

```swift
struct ImmersionChangeContext
```

## Overview

You don’t use this structure directly. Instead, SwiftUI provides instances of this structure via the `onImmersionChange` modifier’s closure.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [amount](immersionchangecontext/amount.md) — The current amount of immersion.

## See Also

### Responding to immersion changes

- [onImmersionChange(initial:_:)](<view/onimmersionchange(initial___).md>) — Performs an action when the immersion state of your app changes.
