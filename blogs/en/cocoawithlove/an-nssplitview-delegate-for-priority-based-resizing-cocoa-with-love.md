---
title: 'An NSSplitView delegate for priority based resizing | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/09/nssplitview-delegate-for-priority-based.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:ff15814f10b38225'
translated: false
---

> 原文：[An NSSplitView delegate for priority based resizing | Cocoa with Love](https://www.cocoawithlove.com/2009/09/nssplitview-delegate-for-priority-based.html)　·　Cocoa with Love (Matt Gallagher)

The default resizing mechanism in `NSSplitView` is proportional resizing — if the `NSSplitView` changes size, each column resizes by an equal percent. This works badly in the common case where the columns in a split view are used to separate a side panels from a main view area (for example the "source list" in iTunes or the file tree in Xcode). In this post, I'll show you a delegate class that configures a split view for this side panel and main view behavior — resizing the views in a split view based on a priority list.

## Snow Leopard?

Every Mac programming blog that I read is overflowing this week with Snow Leopard information. To celebrate this exciting event, I proudly ignore the trend and present code that (aside from a little Objective-C 2.0 syntax) would run on Mac OS 10.0.

## Proportional versus priority-based resizing

For a three section `NSSplitView`, the default proportional resizing behaves like this:

![](https://www.cocoawithlove.com/assets/objc-era/prioritylarge.png)

Priority-based resizing nominates 1 view as the most important. This is normally the window's "main" view. This highest priority view is the only view that grows in size as the window grows.

> ColumnSplitView.zip
> 
> (60kb) to see the priority resizing at work.

## Proportional resizing in reverse

The flip side to priority resizing is that the highest priority view is also the first to compress to zero. For this reason, the priority-based resizing should also implement minimum sizes so that the main view never actually reaches zero size.

Once the highest priority view reaches minimum, remaining views are collapsed by priority until all views are at their minimum size. The window or enclosing scroll view's minimum size should be constrained so that the split view is never forced past the point where columns are all at minimum size.

## Controlling an NSSplitView

`NSSplitView` takes a delegate. The delegate methods are where we control the minimum sizes of sections and which views expand or collapse by what amount.

The class I'll present will be a dedicated delegate class named `PrioritySplitViewDelegate` that allows you to configure priorities and minimum sizes for the `NSSplitView`'s subviews. This generic delegate can then be constructed, configured and attached to the `NSSplitView` in your controller code.

```objc
@interface PrioritySplitViewDelegate : NSObject
{
    NSMutableDictionary *lengthsByViewIndex;
    NSMutableDictionary *viewIndicesByPriority;
}

- (void)setMinimumLength:(CGFloat)minLength
    forViewAtIndex:(NSInteger)viewIndex;
- (void)setPriority:(NSInteger)priorityIndex
    forViewAtIndex:(NSInteger)viewIndex;

@end
```

Some usage cautions about this design: the delegate does not know in advance how many sections the split view will have, so it will let you specify priorities or minimum sizes for views that don't exist.

Specifying a priority for every view is mandatory so if you forget to specify a priority for a view, an exception will be thrown when the `NSSplitView` is resized. Minimum sizes are optional but will be zero if not specified. Keep these points in mind when using this class.

## Implementation

Constraining the coordinates in the `splitView:constrainMinCoordinate:ofSubviewAt:` and `splitView:constrainMaxCoordinate:ofSubviewAt:` happens when the user drags the boundary between two split view sections. In these methods, we need to ensure that the view which is getting smaller does not exceed its minimum size.

When dragging the boundary between two columns to the left, this means that the minimum coordinate is that which would collapse the left view to its minimum size.

```objc
- (CGFloat)splitView:(NSSplitView *)sender
    constrainMinCoordinate:(CGFloat)proposedMin ofSubviewAt:(NSInteger)offset
{
    NSView *subview = [[sender subviews] objectAtIndex:offset];
    NSRect subviewFrame = subview.frame;
    CGFloat frameOrigin;
    if ([sender isVertical])
    {
        frameOrigin = subviewFrame.origin.x;
    }
    else
    {
        frameOrigin = subviewFrame.origin.y;
    }
    
    CGFloat minimumSize =
        [[lengthsByViewIndex objectForKey:[NSNumber numberWithInteger:offset]]
            doubleValue];
    
    return frameOrigin + minimumSize;
}
```

The `splitView:constrainMaxCoordinate:ofSubviewAt:` is similar. You can download the sample project to see the implementation of this method.

Finally, we need to handle the priority resizing itself. This happens in the implementation of the delegate method `splitView:resizeSubviewsWithOldSize:`. This method is invoked when the split view is resized (normally because the enclosing window has resized).

A brief description of the work involved is:

1. Iterate over the list of views, sorted by priority.
2. As each view is reached, attempt to apply the entire size change to this view.
3. If applying the size to the view would cause it to become smaller than its minimum size, apply as much as possible and proceed to the next view by priority.

The size change for the split view is named `delta` in the following code taken from the `splitView:resizeSubviewsWithOldSize:` method.

```objc
for (NSNumber *priorityIndex in
    [[viewIndicesByPriority allKeys] sortedArrayUsingSelector:@selector(compare:)])
{
    NSNumber *viewIndex = [viewIndicesByPriority objectForKey:priorityIndex];
    NSInteger viewIndexValue = [viewIndex integerValue];
    if (viewIndexValue >= subviewsCount)
    {
        continue;
    }
    
    NSView *view = [subviews objectAtIndex:viewIndexValue];
    
    NSSize frameSize = [view frame].size;
    NSNumber *minLength = [lengthsByViewIndex objectForKey:viewIndex];
    CGFloat minLengthValue = [minLength doubleValue];
    
    if (isVertical)
    {
        frameSize.height = sender.bounds.size.height;
        if (delta > 0 ||
            frameSize.width + delta >= minLengthValue)
        {
            frameSize.width += delta;
            delta = 0;
        }
        else if (delta &lt; 0)
        {
            delta += frameSize.width - minLengthValue;
            frameSize.width = minLengthValue;
        }
    }
    else
    {
        frameSize.width = sender.bounds.size.width;
        if (delta > 0 ||
            frameSize.height + delta >= minLengthValue)
        {
            frameSize.height += delta;
            delta = 0;
        }
        else if (delta &lt; 0)
        {
            delta += frameSize.height - minLengthValue;
            frameSize.height = minLengthValue;
        }
    }
    
    [view setFrameSize:frameSize];
    viewCountCheck++;
}
```

The "`continue`" skips invalid priorities. You might replace this in your own code with an `NSAssert` instead, depending on how you like to handle minor errors.

The other point to notice is that we don't break out of the loop once the `delta` is fully applied — we still need to run `setFrameSize:` on each view to apply any size change in the perpendicular direction (vertically for columns or horizontally for rows).

This fragment doesn't show it but the code includes a second iteration over all the views, in order, which sets the origins of each view following the resize so they are all positioned correctly for their new sizes.

## Hitting the minimum size

If all views are at their minimum and the split view cannot contract any further, the current implementation throws an exception giving the minimum size. This is so that you can configure the containing view (often a window) to respect this minimum and never try to make the `NSSplitView` smaller than this. If you don't like this behavior, you can remove the `NSAssert3` statement in the `setMinimumLength:forViewAtIndex:` method.

## Conclusion

> ColumnSplitView.zip
> 
> (60kb) to see the full
> 
> class.

The advantage to the `PrioritySplitViewDelegate` class is that it is generic: you don't need to write this code each time and it handles the common case of using an `NSSplitView` to contain columns and a main view. It offers an easy plug in solution for managing a split view in this arrangement.

It could probably be improved by changing the `setMinimumLength:forViewAtIndex:` and `setPriority:forViewAtIndex:` methods to something that prevents you from providing the wrong values for indices or number of lengths or priorities but the `NSAssert`s in the `splitView:resizeSubviewsWithOldSize:` method will pick up the most critical errors you might make.
