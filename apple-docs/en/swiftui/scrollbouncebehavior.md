---
title: ScrollBounceBehavior
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollbouncebehavior
source_url: 'https://developer.apple.com/documentation/swiftui/scrollbouncebehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollbouncebehavior.json'
content_hash: 'sha256:43f02df17e2419e5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ScrollBounceBehavior

<sub>Structure</sub>

The ways that a scrollable view can bounce when it reaches the end of its content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ScrollBounceBehavior
```

## Overview

Use the [scrollBounceBehavior(_:axes:)](<view/scrollbouncebehavior(__axes_).md>) view modifier to set a value of this type for a scrollable view, like a [ScrollView](scrollview.md) or a [List](list.md). The value configures the bounce behavior when people scroll to the end of the view’s content.

You can configure each scrollable axis to use a different bounce mode.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Bounce behaviors

- [automatic](scrollbouncebehavior/automatic.md) — The automatic behavior.
- [always](scrollbouncebehavior/always.md) — The scrollable view always bounces.
- [basedOnSize](scrollbouncebehavior/basedonsize.md) — The scrollable view bounces when its content is large enough to require scrolling.

## See Also

### Configuring scroll bounce behavior

- [scrollBounceBehavior(_:axes:)](<view/scrollbouncebehavior(__axes_).md>) — Configures the bounce behavior of scrollable views along the specified axis.
- [horizontalScrollBounceBehavior](environmentvalues/horizontalscrollbouncebehavior.md) — The scroll bounce mode for the horizontal axis of scrollable views.
- [verticalScrollBounceBehavior](environmentvalues/verticalscrollbouncebehavior.md) — The scroll bounce mode for the vertical axis of scrollable views.
