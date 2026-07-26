---
title: 'previousLocation(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitouch/previouslocation(in:)-ea29'
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/previouslocation(in:)-ea29'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/previouslocation%28in%3A%29-ea29.json'
content_hash: 'sha256:d4a79ac7683a8070'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# previousLocation(in:)

<sub>Instance Method</sub>

Returns the previous location of the touch in the coordinate system of the given node.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func previousLocation(in node: SKNode) -> CGPoint
```

## Parameters

- `node` — A node that is a descendant of a scene presented in the window that received the touch event.

## Return Value

The location of the touch in the node’s coordinate system.

## See Also

### Working with touch events in SpriteKit

- [- locationInNode:](<location(in_)-44h4k.md>) — Returns the current location of the touch in the coordinate system of the given node.
