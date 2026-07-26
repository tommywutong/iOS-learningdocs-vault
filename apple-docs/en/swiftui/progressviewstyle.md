---
title: ProgressViewStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/progressviewstyle
source_url: 'https://developer.apple.com/documentation/swiftui/progressviewstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/progressviewstyle.json'
content_hash: 'sha256:5e47d6aec33e7099'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ProgressViewStyle

<sub>Protocol</sub>

A type that applies standard interaction behavior to all progress views within a view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol ProgressViewStyle
```

## Overview

To configure the current progress view style for a view hierarchy, use the [progressViewStyle(_:)](<view/progressviewstyle(__).md>) modifier.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Relationships

- **Conforming Types**: [CircularProgressViewStyle](circularprogressviewstyle.md), [DefaultProgressViewStyle](defaultprogressviewstyle.md), [LinearProgressViewStyle](linearprogressviewstyle.md)

## Topics

### Getting built-in progress view styles

- [automatic](progressviewstyle/automatic.md) — The default progress view style in the current context of the view being styled.
- [circular](progressviewstyle/circular.md) — The style of a progress view that uses a circular gauge to indicate the partial completion of an activity.
- [linear](progressviewstyle/linear.md) — A progress view that visually indicates its progress using a horizontal bar.

### Creating custom progress view styles

- [makeBody(configuration:)](<progressviewstyle/makebody(configuration_).md>) — Creates a view representing the body of a progress view.
- [Configuration](progressviewstyle/configuration.md) — A type alias for the properties of a progress view instance.
- [Body](progressviewstyle/body.md) — A view representing the body of a progress view.

### Supporting types

- [DefaultProgressViewStyle](defaultprogressviewstyle.md) — The default progress view style in the current context of the view being styled.
- [CircularProgressViewStyle](circularprogressviewstyle.md) — A progress view that uses a circular gauge to indicate the partial completion of an activity.
- [LinearProgressViewStyle](linearprogressviewstyle.md) — A progress view that visually indicates its progress using a horizontal bar.

## See Also

### Styling indicators

- [gaugeStyle(_:)](<view/gaugestyle(__).md>) — Sets the style for gauges within this view.
- [GaugeStyle](gaugestyle.md) — Defines the implementation of all gauge instances within a view hierarchy.
- [GaugeStyleConfiguration](gaugestyleconfiguration.md) — The properties of a gauge instance.
- [progressViewStyle(_:)](<view/progressviewstyle(__).md>) — Sets the style for progress views in this view.
- [ProgressViewStyleConfiguration](progressviewstyleconfiguration.md) — The properties of a progress view instance.
