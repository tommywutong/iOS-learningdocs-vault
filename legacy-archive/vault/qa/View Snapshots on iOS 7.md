---
title: View Snapshots on iOS 7
apple_id: DTS40014134
resource_type: QA
platform: iOS
topic: Graphics & Animation
technology: null
published: '2014-05-01'
source_url: https://developer.apple.com/library/archive/qa/qa1817/_index.html
archived_at: '2026-07-18T02:34:55.928222Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1817

# View Snapshots on iOS 7

## Q:  On iOS 7 and later, how do I take a snapshot of my view and save the result in a UIImage?

A: Starting from iOS 7, the `UIView` class provides a method [-drawViewHierarchyInRect:afterScreenUpdates:](https://developer.apple.com/library/IOs/documentation/UIKit/Reference/UIView_Class/UIView/UIView.html#//apple_ref/occ/instm/UIView/drawViewHierarchyInRect:afterScreenUpdates:), which lets you render a snapshot of the complete view hierarchy as visible onscreen into a bitmap context. On iOS 6 and earlier, how to capture a view's drawing contents depends on the underlying drawing technique. This new method `-drawViewHierarchyInRect:afterScreenUpdates:` enables you to capture the contents of the receiver view and its subviews to an image regardless of the drawing techniques (for example `UIKit`, `Quartz`, `OpenGL` `ES`, `SpriteKit`, etc) in which the views are rendered.

See Listing 1 for an example of how to use `-drawViewHierarchyInRect:afterScreenUpdates:` to take a view snapshot on iOS 7 and later.

__Listing 1__  Creating a snapshot image

```objc
- (UIImage *)snapshot:(UIView *)view
{
    UIGraphicsBeginImageContextWithOptions(view.bounds.size, YES, 0);
    [view drawViewHierarchyInRect:view.bounds afterScreenUpdates:YES];
    UIImage *image = UIGraphicsGetImageFromCurrentImageContext();
    UIGraphicsEndImageContext();

    return image;
}
```

In addition to [-drawViewHierarchyInRect:afterScreenUpdates:](https://developer.apple.com/library/IOs/documentation/UIKit/Reference/UIView_Class/UIView/UIView.html#//apple_ref/occ/instm/UIView/drawViewHierarchyInRect:afterScreenUpdates:), `UIView` now provides another two snapshot related methods, [-snapshotViewAfterScreenUpdates:](https://developer.apple.com/library/IOs/documentation/UIKit/Reference/UIView_Class/UIView/UIView.html#//apple_ref/occ/instm/UIView/snapshotViewAfterScreenUpdates:) and [-resizableSnapshotViewFromRect:afterScreenUpdates:withCapInsets:](https://developer.apple.com/library/IOs/documentation/UIKit/Reference/UIView_Class/UIView/UIView.html#//apple_ref/occ/instm/UIView/resizableSnapshotViewFromRect:afterScreenUpdates:withCapInsets:). `UIScreen` also has [-snapshotViewAfterScreenUpdates:](https://developer.apple.com/library/ios/documentation/uikit/reference/UIScreen_Class/Reference/UIScreen.html#//apple_ref/occ/instm/UIScreen/snapshotViewAfterScreenUpdates:). Unlike `UIView`'s `-drawViewHierarchyInRect:afterScreenUpdates:`, these methods return a `UIView` object. If you are looking for a new snapshot view, use one of these methods. It will be more efficient than calling `-drawViewHierarchyInRect:afterScreenUpdates:` to render the view contents into a bitmap image yourself. You can use the returned view as a visual stand-in for the current view/screen in your app. For example, you might use a snapshot view for animations where updating a large view hierarchy might be expensive.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-05-01 | Editorial changes. |
| 2014-02-12 | New document that describes how to take a view snapshot on iOS 7 and later. |

