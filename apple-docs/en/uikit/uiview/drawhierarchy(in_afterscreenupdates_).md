---
title: 'drawHierarchy(in:afterScreenUpdates:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/drawhierarchy(in:afterscreenupdates:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/drawhierarchy(in:afterscreenupdates:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/drawhierarchy%28in%3Aafterscreenupdates%3A%29.json'
content_hash: 'sha256:c332e494994fafa3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# drawHierarchy(in:afterScreenUpdates:)

<sub>Instance Method</sub>

Renders a snapshot of the complete view hierarchy as visible onscreen into the current context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func drawHierarchy(in rect: CGRect, afterScreenUpdates afterUpdates: Bool) -> Bool
```

## Parameters

- `rect` — A rectangle specified in the local coordinate system (bounds) of the view.

- `afterUpdates` — A Boolean value that indicates whether the snapshot should be rendered after recent changes have been incorporated. Specify the value [false](../../swift/false.md) if you want to render a snapshot in the view hierarchy’s current state, which might not include recent changes.

## Return Value

Returns [true](../../swift/true.md) if the snapshot is complete, or [false](../../swift/false.md) if the snapshot is missing image data for any view in the hierarchy.

## Discussion

Use this method when you want to apply a graphical effect, such as a blur, to a view snapshot. This method is not as fast as the [- snapshotViewAfterScreenUpdates:](<snapshotview(afterscreenupdates_).md>) method.

## See Also

### Capturing a view snapshot

- [- snapshotViewAfterScreenUpdates:](<snapshotview(afterscreenupdates_).md>) — Returns a snapshot view based on the contents of the current view.
- [- resizableSnapshotViewFromRect:afterScreenUpdates:withCapInsets:](<resizablesnapshotview(from_afterscreenupdates_withcapinsets_).md>) — Returns a snapshot view based on the specified contents of the current view, with stretchable insets.
