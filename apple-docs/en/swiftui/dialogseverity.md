---
title: DialogSeverity
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 13.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dialogseverity
source_url: 'https://developer.apple.com/documentation/swiftui/dialogseverity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dialogseverity.json'
content_hash: 'sha256:3bc55e344560aad7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DialogSeverity

<sub>Structure</sub>

The severity of an alert or confirmation dialog.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DialogSeverity
```

## Overview

You can use dialog severity to indicate that people need to take extra care when interacting with the dialog, like when an action taken from the dialog permanently deletes data.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting severities

- [automatic](dialogseverity/automatic.md) — The default dialog severity. Alerts that present an error will use `.critical` and all others will use `.standard`.
- [standard](dialogseverity/standard.md) — A severity that indicates the dialog is being displayed for the purpose of presenting information to the user.
- [critical](dialogseverity/critical.md) — A severity that indicates extra attention should be given to the dialog, for example when unexpected data loss may occur as a result of the action taken.
