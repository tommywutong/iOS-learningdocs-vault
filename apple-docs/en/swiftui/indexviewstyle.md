---
title: IndexViewStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/indexviewstyle
source_url: 'https://developer.apple.com/documentation/swiftui/indexviewstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/indexviewstyle.json'
content_hash: 'sha256:ff1fd70b84ae14c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# IndexViewStyle

<sub>Protocol</sub>

Defines the implementation of all `IndexView` instances within a view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
protocol IndexViewStyle
```

## Overview

To configure the current `IndexViewStyle` for a view hierarchy, use the `.indexViewStyle()` modifier.

## Relationships

- **Conforming Types**: [PageIndexViewStyle](pageindexviewstyle.md)

## Topics

### Getting built-in index view styles

- [page](indexviewstyle/page.md) — An index view style that places a page index view over its content.
- [page(backgroundDisplayMode:)](<indexviewstyle/page(backgrounddisplaymode_).md>) — An index view style that places a page index view over its content.

### Supporting types

- [PageIndexViewStyle](pageindexviewstyle.md) — An index view style that places a page index view over its content.

## See Also

### Styling groups

- [controlGroupStyle(_:)](<view/controlgroupstyle(__).md>) — Sets the style for control groups within this view.
- [ControlGroupStyle](controlgroupstyle.md) — Defines the implementation of all control groups within a view hierarchy.
- [ControlGroupStyleConfiguration](controlgroupstyleconfiguration.md) — The properties of a control group.
- [formStyle(_:)](<view/formstyle(__).md>) — Sets the style for forms in a view hierarchy.
- [FormStyle](formstyle.md) — The appearance and behavior of a form.
- [FormStyleConfiguration](formstyleconfiguration.md) — The properties of a form instance.
- [groupBoxStyle(_:)](<view/groupboxstyle(__).md>) — Sets the style for group boxes within this view.
- [GroupBoxStyle](groupboxstyle.md) — A type that specifies the appearance and interaction of all group boxes within a view hierarchy.
- [GroupBoxStyleConfiguration](groupboxstyleconfiguration.md) — The properties of a group box instance.
- [indexViewStyle(_:)](<view/indexviewstyle(__).md>) — Sets the style for the index view within the current environment.
- [labeledContentStyle(_:)](<view/labeledcontentstyle(__).md>) — Sets a style for labeled content.
- [LabeledContentStyle](labeledcontentstyle.md) — The appearance and behavior of a labeled content instance..
- [LabeledContentStyleConfiguration](labeledcontentstyleconfiguration.md) — The properties of a labeled content instance.
