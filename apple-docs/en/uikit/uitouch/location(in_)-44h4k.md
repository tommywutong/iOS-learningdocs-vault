---
title: 'location(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitouch/location(in:)-44h4k'
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/location(in:)-44h4k'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/location%28in%3A%29-44h4k.json'
content_hash: 'sha256:6b990025674a4df8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# location(in:)

<sub>Instance Method</sub>

Returns the current location of the touch in the coordinate system of the given node.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func location(in node: SKNode) -> CGPoint
```

## Parameters

- `node` — A node that is a descendant of a scene presented in the window that received the touch event.

## Return Value

The location of the touch in the node’s coordinate system.

## See Also

### Working with touch events in SpriteKit

- [- previousLocationInNode:](<previouslocation(in_)-ea29.md>) — Returns the previous location of the touch in the coordinate system of the given node.
