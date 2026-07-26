---
title: 'snapshotView(afterScreenUpdates:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscreen/snapshotview(afterscreenupdates:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/snapshotview(afterscreenupdates:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/snapshotview%28afterscreenupdates%3A%29.json'
content_hash: 'sha256:1d672d0a6bf23b7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# snapshotView(afterScreenUpdates:)

<sub>Instance Method</sub>

Returns a snapshot view based on the current screen contents.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func snapshotView(afterScreenUpdates afterUpdates: Bool) -> UIView
```

## Parameters

- `afterUpdates` — A Boolean value that indicates whether the snapshot should be taken after recent changes have been incorporated. Specify the value [false](../../swift/false.md) if you want to capture the screen in its current state, which might not include recent changes.

## Return Value

A new view object containing a snapshot of the screen’s rendered contents.

## Discussion

This method captures the current visual contents of the screen from the render server and uses them to build a new snapshot view. You can use the returned snapshot view as a visual stand-in for the screen’s contents in your app. For example, you might use a snapshot view to facilitate a full screen animation. Because the content is captured from the already rendered content, this method reflects the current visual appearance of the screen and is not updated to reflect animations that are scheduled or in progress. However, this method is faster than trying to render the contents of the screen into a bitmap image yourself.

Because the returned snapshot view is still a view object, you may modify it and its layer object as needed. However, you cannot change the [contents](../../quartzcore/calayer/contents.md) property of the snapshot view’s layer and attempts to do so will fail silently. If any onscreen views have not yet been committed to the render server, that portion of the snapshot will have no content.
