---
title: UserInterfaceSizeClass
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/userinterfacesizeclass
source_url: 'https://developer.apple.com/documentation/swiftui/userinterfacesizeclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/userinterfacesizeclass.json'
content_hash: 'sha256:c339915bec345f34'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# UserInterfaceSizeClass

<sub>Enumeration</sub>

A set of values that indicate the visual size available to the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum UserInterfaceSizeClass
```

## Overview

You receive a size class value when you read either the [horizontalSizeClass](environmentvalues/horizontalsizeclass.md) or [verticalSizeClass](environmentvalues/verticalsizeclass.md) environment value. The value tells you about the amount of space available to your views in a given direction. You can read the size class like any other of the [EnvironmentValues](environmentvalues.md), by creating a property with the [Environment](environment.md) property wrapper:

```swift
@Environment(\.horizontalSizeClass) private var horizontalSizeClass
@Environment(\.verticalSizeClass) private var verticalSizeClass
```

SwiftUI sets the size class based on several factors, including:

- The current device type.
- The orientation of the device.
- The appearance of Slide Over and Split View on iPad.

Several built-in views change their behavior based on the size class. For example, a [NavigationView](navigationview.md) presents a multicolumn view when the horizontal size class is [UserInterfaceSizeClass.regular](userinterfacesizeclass/regular.md), but a single column otherwise. You can also adjust the appearance of custom views by reading the size class and conditioning your views. If you do, be prepared to handle size class changes while your app runs, because factors like device orientation can change at runtime.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting size classes

- [UserInterfaceSizeClass.compact](userinterfacesizeclass/compact.md) — The compact size class.
- [UserInterfaceSizeClass.regular](userinterfacesizeclass/regular.md) — The regular size class.

### Creating a size class

- [init(_:)](<userinterfacesizeclass/init(__).md>) — Creates a SwiftUI size class from the specified UIKit size class.

## See Also

### Reacting to interface characteristics

- [isLuminanceReduced](environmentvalues/isluminancereduced.md) — A Boolean value that indicates whether the display or environment currently requires reduced luminance.
- [displayScale](environmentvalues/displayscale.md) — The display scale of this environment.
- [pixelLength](environmentvalues/pixellength.md) — The size of a pixel on the screen.
- [horizontalSizeClass](environmentvalues/horizontalsizeclass.md) — The horizontal size class of this environment.
- [verticalSizeClass](environmentvalues/verticalsizeclass.md) — The vertical size class of this environment.
