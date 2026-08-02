---
title: Text System Storage Layer Overview
apple_id: 10000087i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextStorageLayer/Tasks/TrackingSize.html
archived_at: '2026-07-15T07:20:32.225938Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text System Storage Layer Overview](Introduction%20to%20Text%20System%20Storage%20Layer%20Overview.md)


[Next](Creating%20a%20Subclass%20of%20NSTextStorage.md)[Previous](Calculating%20Region%2C%20Bounding%20Rectangle%2C%20and%20Inset.md)

# Tracking the Size of a Text View

You can set an [NSTextContainer](https://developer.apple.com/documentation/appkit/nstextcontainer) object to track the size of its [NSTextView](https://developer.apple.com/documentation/appkit/nstextview) object and adjust its own size to match whenever the text view size changes. The [setHeightTracksTextView:](https://developer.apple.com/documentation/uikit/nstextcontainer/1444559-heighttrackstextview) and [setWidthTracksTextView:](https://developer.apple.com/documentation/appkit/nstextcontainer/1444563-widthtrackstextview) methods allow you to control this tracking for either dimension.

When a text container adjusts its size to match that of its text view, it takes into account the inset specified by the text view so the bounding rectangle is inset from every edge possible. In other words, a text container that tracks the size of its text view is always smaller than the text view in a given dimension by twice the inset. Suppose a text container is set to track width and its text view gives it an inset of (10,10). Now, if the text view’s width is changed to 138, the text container’s top-left corner is set to lie at (10,10) and its width is set to 118, so its right edge is 10 points from the text view’s right edge. Its height remains the same.

Whether it tracks the size of its text view or not, a text container doesn’t grow or shrink as text is added or deleted; instead, the [NSLayoutManager](https://developer.apple.com/documentation/appkit/nslayoutmanager) object resizes the text view based on the portion of the text container actually filled with text. To allow an text view to be resized in this manner, use [setVerticallyResizable:](https://developer.apple.com/documentation/appkit/nstext/1535082-isverticallyresizable) or [setHorizontallyResizable:](https://developer.apple.com/documentation/appkit/nstext/1527489-horizontallyresizable) methods (which are inherited from [NSText](https://developer.apple.com/documentation/appkit/nstext)) as needed, set the text container not to track the size of its text view, and set the text container’s size in the appropriate dimension large enough to accommodate a great amount of text—for example, 10,000,000 points (this incurs no cost whatever in processing or storage).

Note that a text view can be resized based on its text container, and a text container can resize itself based on its text view. If you set both objects up to resize automatically in the same dimension, your application can get trapped in an infinite loop. When text is added to the text container, the text view is resized to fit the area actually used for text; this causes the text container to resize itself and relay its text, which causes the text view to resize itself again, and so on ad infinitum. Each type of size tracking has its proper uses; be sure to use only one for either dimension.

[Next](Creating%20a%20Subclass%20of%20NSTextStorage.md)[Previous](Calculating%20Region%2C%20Bounding%20Rectangle%2C%20and%20Inset.md)

