---
title: springLoadingBehavior
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/springloadingbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/springloadingbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/springloadingbehavior.json'
content_hash: 'sha256:1a42cf4a70620f40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# springLoadingBehavior

<sub>Instance Property</sub>

The behavior of spring loaded interactions for the views associated with this environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var springLoadingBehavior: SpringLoadingBehavior { get }
```

## Discussion

Spring loading refers to a view being activated during a drag and drop interaction. On iOS this can occur when pausing briefly on top of a view with dragged content. On macOS this can occur with similar brief pauses or on pressure-sensitive systems by “force clicking” during the drag. This has no effect on tvOS or watchOS.

This is commonly used with views that have a navigation or presentation effect, allowing the destination to be revealed without pausing the drag interaction. For example, a button that reveals a list of folders that a dragged item can be dropped onto.

A value of `enabled` means that a view should support spring loaded interactions if it is able, and `disabled` means it should not. A value of `automatic` means that a view should follow its default behavior, such as a `TabView` automatically allowing spring loading, but a `Picker` with `segmented` style would not.

## See Also

### Configuring spring loading

- [springLoadingBehavior(_:)](<../view/springloadingbehavior(__).md>) — Sets the spring loading behavior this view.
- [SpringLoadingBehavior](../springloadingbehavior.md) — The options for controlling the spring loading behavior of views.
