---
title: 'resizableSnapshotView(from:afterScreenUpdates:withCapInsets:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/resizablesnapshotview(from:afterscreenupdates:withcapinsets:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/resizablesnapshotview(from:afterscreenupdates:withcapinsets:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/resizablesnapshotview%28from%3Aafterscreenupdates%3Awithcapinsets%3A%29.json'
content_hash: 'sha256:90caf6456b6a0885'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# resizableSnapshotView(from:afterScreenUpdates:withCapInsets:)

<sub>Instance Method</sub>

Returns a snapshot view based on the specified contents of the current view, with stretchable insets.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func resizableSnapshotView(from rect: CGRect, afterScreenUpdates afterUpdates: Bool, withCapInsets capInsets: UIEdgeInsets) -> UIView?
```

## Parameters

- `rect` — The portion of the view that you want to capture. The rectangle must be in the bounds coordinate space of the current view.

- `afterUpdates` — A Boolean value that specifies whether the snapshot should be taken after recent changes have been incorporated. Pass the value [false](../../swift/false.md) if you want to capture the screen in its current state, which might not include recent changes.

- `capInsets` — The edge insets that define the stretchable portion of the returned view’s content. You can specify [UIEdgeInsetsZero](../uiedgeinsets/zero.md) if you do not want the contents of the returned view to have a stretchable area.

## Return Value

A new view object containing a snapshot of the current view’s rendered contents.

## Discussion

This method very efficiently captures the current rendered appearance of a view and uses it to build a new snapshot view with stretchable insets. You can use the returned view as a visual stand-in for the current view in your app. For example, you might use a snapshot view for animations where updating a large view hierarchy might be expensive. Because the content is captured from the already rendered content, this method reflects the current visual appearance of the view and is not updated to reflect animations that are scheduled or in progress. However, calling this method is faster than trying to render the contents of the current view into a bitmap image yourself.

Because the returned snapshot is a view object, you can modify it and its layer object as needed. However, you cannot change the [contents](../../quartzcore/calayer/contents.md) property of the snapshot view’s layer; attempts to do so fail silently. If the current view is not yet rendered, perhaps because it is not yet onscreen, the snapshot view has no visible content.

You can call this method on a previously generated snapshot to obtain a new snapshot. For example, you could do so after you change properties of a previous snapshot (such as its alpha value) and want a new snapshot that includes those changes.

If you want to apply a graphical effect, such as blur, to a snapshot, use the [- drawViewHierarchyInRect:afterScreenUpdates:](<drawhierarchy(in_afterscreenupdates_).md>) method instead.

If you specify nonzero edge insets in the `capInsets` parameter, those values determine the returned snapshot’s stretchable content area.

## See Also

### Capturing a view snapshot

- [- snapshotViewAfterScreenUpdates:](<snapshotview(afterscreenupdates_).md>) — Returns a snapshot view based on the contents of the current view.
- [- drawViewHierarchyInRect:afterScreenUpdates:](<drawhierarchy(in_afterscreenupdates_).md>) — Renders a snapshot of the complete view hierarchy as visible onscreen into the current context.
