---
title: BackgroundProminence
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/backgroundprominence
source_url: 'https://developer.apple.com/documentation/swiftui/backgroundprominence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/backgroundprominence.json'
content_hash: 'sha256:4daa1944082df13b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# BackgroundProminence

<sub>Structure</sub>

The prominence of backgrounds underneath other views.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct BackgroundProminence
```

## Overview

Background prominence should influence foreground styling to maintain sufficient contrast against the background. For example, selected rows in a `List` and `Table` can have increased prominence backgrounds with accent color fills when focused; the foreground content above the background should be adjusted to reflect that level of prominence.

This can be read and written for views with the `EnvironmentValues.backgroundProminence` property.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting background prominence

- [standard](backgroundprominence/standard.md) — The standard prominence of a background
- [increased](backgroundprominence/increased.md) — A more prominent background that likely requires some changes to the views above it.

## See Also

### Configuring backgrounds

- [listRowBackground(_:)](<view/listrowbackground(__).md>) — Places a custom background view behind a list row item.
- [alternatingRowBackgrounds(_:)](<view/alternatingrowbackgrounds(__).md>) — Overrides whether lists and tables in this view have alternating row backgrounds.
- [AlternatingRowBackgroundBehavior](alternatingrowbackgroundbehavior.md) — The styling of views with respect to alternating row backgrounds.
- [backgroundProminence](environmentvalues/backgroundprominence.md) — The prominence of the background underneath views associated with this environment.
