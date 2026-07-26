---
title: cancel()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipreviewinteraction/cancel()
source_url: 'https://developer.apple.com/documentation/uikit/uipreviewinteraction/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipreviewinteraction/cancel%28%29.json'
content_hash: 'sha256:af31dd9d2879269b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPreviewInteraction](../uipreviewinteraction.md)

# cancel()

<sub>Instance Method</sub>

Cancels the current preview interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func cancel()
```

## Discussion

When a preview interaction is in progress, use this method to cancel it, preventing any further callbacks to the delegate methods.

## See Also

### Handling preview interactions

- [view](view.md) — The view from which the preview interaction receives touch events.
- [- locationInCoordinateSpace:](<location(in_).md>) — Returns the location of the touch that started the interaction.
