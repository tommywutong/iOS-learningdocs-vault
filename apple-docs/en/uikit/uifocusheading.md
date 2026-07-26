---
title: UIFocusHeading
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusheading
source_url: 'https://developer.apple.com/documentation/uikit/uifocusheading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusheading.json'
content_hash: 'sha256:efa6501d96ad2c56'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFocusHeading

<sub>Structure</sub>

The general type of an event.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UIFocusHeading
```

## Overview

You obtain the direction of the focus from the [focusHeading](uifocusupdatecontext/focusheading.md) property.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [UIFocusHeadingUp](uifocusheading/up.md) — The focus update is heading in the up direction.
- [UIFocusHeadingDown](uifocusheading/down.md) — The focus update is heading in the down direction.
- [UIFocusHeadingLeft](uifocusheading/left.md) — The focus update is heading in the left direction.
- [UIFocusHeadingRight](uifocusheading/right.md) — The focus update is heading in the right direction.
- [UIFocusHeadingNext](uifocusheading/next.md) — The focus update is heading to the next item.
- [UIFocusHeadingPrevious](uifocusheading/previous.md) — The focus update is heading to the previous item.
- [UIFocusHeadingFirst](uifocusheading/first.md) — The focus update is heading to the first item.
- [UIFocusHeadingLast](uifocusheading/last.md) — The focus update is heading to the last item.

### Initializers

- [init(rawValue:)](<uifocusheading/init(rawvalue_).md>) — Creates a focus heading structure with the specified raw value.

## See Also

### Locating focus direction

- [previouslyFocusedView](uifocusupdatecontext/previouslyfocusedview.md) — The view that was focused before the focus update.
- [nextFocusedView](uifocusupdatecontext/nextfocusedview.md) — The view that takes the focus after the focus update.
- [focusHeading](uifocusupdatecontext/focusheading.md) — The heading in which the focus update is occurring.
