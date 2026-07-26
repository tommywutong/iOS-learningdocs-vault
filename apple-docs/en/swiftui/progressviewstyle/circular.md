---
title: circular
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/progressviewstyle/circular
source_url: 'https://developer.apple.com/documentation/swiftui/progressviewstyle/circular'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/progressviewstyle/circular.json'
content_hash: 'sha256:8f239c8bbd362017'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProgressViewStyle](../progressviewstyle.md)

# circular

<sub>Type Property</sub>

The style of a progress view that uses a circular gauge to indicate the partial completion of an activity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated static var circular: CircularProgressViewStyle { get }
```

## Discussion

On watchOS, and in widgets and complications, a circular progress view appears as a gauge with the [accessoryCircularCapacity](../gaugestyle/accessorycircularcapacity.md) style. If the progress view is indeterminate, the gauge is empty.

In cases where no determinate circular progress view style is available, circular progress views use an indeterminate style.

## See Also

### Getting built-in progress view styles

- [automatic](automatic.md) — The default progress view style in the current context of the view being styled.
- [linear](linear.md) — A progress view that visually indicates its progress using a horizontal bar.
