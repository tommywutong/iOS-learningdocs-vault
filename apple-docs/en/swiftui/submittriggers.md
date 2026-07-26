---
title: SubmitTriggers
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/submittriggers
source_url: 'https://developer.apple.com/documentation/swiftui/submittriggers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/submittriggers.json'
content_hash: 'sha256:2a72efb94ca85eab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SubmitTriggers

<sub>Structure</sub>

A type that defines various triggers that result in the firing of a submission action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SubmitTriggers
```

## Overview

These triggers may be provided to the [onSubmit(of:_:)](<view/onsubmit(of___).md>) modifier to alter which types of user behaviors trigger a provided submission action.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Getting submit triggers

- [search](submittriggers/search.md) — Defines triggers originating from search fields constructed from searchable modifiers.
- [text](submittriggers/text.md) — Defines triggers originating from text input controls like `TextField` and `SecureField`.

### Creating a set of options

- [init(rawValue:)](<submittriggers/init(rawvalue_).md>) — Creates a set of submit triggers.

## See Also

### Responding to submission events

- [onSubmit(of:_:)](<view/onsubmit(of___).md>) — Adds an action to perform when the user submits a value to this view.
- [submitScope(_:)](<view/submitscope(__).md>) — Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.
