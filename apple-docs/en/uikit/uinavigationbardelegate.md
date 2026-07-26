---
title: UINavigationBarDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationbardelegate
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbardelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbardelegate.json'
content_hash: 'sha256:69b126d9bd0af555'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UINavigationBarDelegate

<sub>Protocol</sub>

Methods that a navigation bar calls before and after it modifies its stack of navigation items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UINavigationBarDelegate : UIBarPositioningDelegate
```

## Overview

The [UINavigationBarDelegate](uinavigationbardelegate.md) protocol defines optional methods that a [UINavigationBar](uinavigationbar.md) [delegate](uinavigationbar/delegate.md) implements to update its views when items push or pop from the stack. The navigation bar represents only the bar at the top of the screen, not the view below. It’s the application’s responsibility to implement the behavior when the top item changes.

You can control whether a navigation bar pushes an item on or pops an item from the stack by implementing the [- navigationBar:shouldPushItem:](<uinavigationbardelegate/navigationbar(__shouldpush_).md>) and [- navigationBar:shouldPopItem:](<uinavigationbardelegate/navigationbar(__shouldpop_).md>) methods. These methods return [true](../swift/true.md) if the action is allowed; otherwise, [false](../swift/false.md).

The screen always reflects the top item on the navigation bar. You implement the [- navigationBar:didPushItem:](<uinavigationbardelegate/navigationbar(__didpush_).md>) method to update the view below the navigation bar to reflect the new item. Similarly, you implement the [- navigationBar:didPopItem:](<uinavigationbardelegate/navigationbar(__didpop_).md>) method to replace the view below the navigation bar.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIBarPositioningDelegate](uibarpositioningdelegate.md)

## Topics

### Pushing items

- [- navigationBar:shouldPushItem:](<uinavigationbardelegate/navigationbar(__shouldpush_).md>) — Returns a Boolean value indicating whether the navigation bar should push an item.
- [- navigationBar:didPushItem:](<uinavigationbardelegate/navigationbar(__didpush_).md>) — Tells the delegate that an item was pushed onto the navigation bar.

### Popping items

- [- navigationBar:shouldPopItem:](<uinavigationbardelegate/navigationbar(__shouldpop_).md>) — Returns a Boolean value indicating whether the navigation bar should pop an item.
- [- navigationBar:didPopItem:](<uinavigationbardelegate/navigationbar(__didpop_).md>) — Tells the delegate that an item was popped from the navigation bar.

### Building with Mac Catalyst

- [- navigationBarNSToolbarSection:](<uinavigationbardelegate/navigationbarnstoolbarsection(__).md>) — Asks the delegate which section of the toolbar to host the navigation bar in.

## See Also

### Responding to navigation bar changes

- [delegate](uinavigationbar/delegate.md) — The navigation bar’s delegate object.
