---
title: CircularProgressViewStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/circularprogressviewstyle
source_url: 'https://developer.apple.com/documentation/swiftui/circularprogressviewstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/circularprogressviewstyle.json'
content_hash: 'sha256:bcb862b51c8982d6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# CircularProgressViewStyle

<sub>Structure</sub>

A progress view that uses a circular gauge to indicate the partial completion of an activity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct CircularProgressViewStyle
```

## Overview

On watchOS, and in widgets and complications, a circular progress view appears as a gauge with the [accessoryCircularCapacity](gaugestyle/accessorycircularcapacity.md) style. If the progress view is indeterminate, the gauge is empty.

In cases where no determinate circular progress view style is available, circular progress views use an indeterminate style.

Use [circular](progressviewstyle/circular.md) to construct the circular progress view style.

## Relationships

- **Conforms To**: [ProgressViewStyle](progressviewstyle.md)

## Topics

### Creating the progress view style

- [init()](<circularprogressviewstyle/init().md>) — Creates a circular progress view style.

### Deprecated initializers

- [init(tint:)](<circularprogressviewstyle/init(tint_).md>) — Creates a circular progress view style with a tint color. _(deprecated)_

## See Also

### Supporting types

- [DefaultProgressViewStyle](defaultprogressviewstyle.md) — The default progress view style in the current context of the view being styled.
- [LinearProgressViewStyle](linearprogressviewstyle.md) — A progress view that visually indicates its progress using a horizontal bar.
