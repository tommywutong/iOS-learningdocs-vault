---
title: Scroll Views Inside Scroll Views
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/05/scrollviews-inside-scrollviews/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:ef5b8063910cde8e'
translated: false
---

> 原文：[Scroll Views Inside Scroll Views](https://oleb.net/blog/2014/05/scrollviews-inside-scrollviews/)　·　Ole Begemann

# Scroll Views Inside Scroll Views

**Update June 30, 2014:** Updated to reflect changes I made to `OLEContainerScrollView`’s public interface. The container scroll view now exposes a read-only `contentView` property. You should add any subviews you want managed by the container scroll view directly to its content view.

In this article, I am introducing [`OLEContainerScrollView`](https://github.com/ole/OLEContainerScrollView), a `UIScrollView` subclass that allows you to add multiple scroll views, table views, or collection views to the same container.

# Use Cases

You can use `OLEContainerScrollView` to achieve the following things:

- Place multiple scroll views (or table views, or collection views) below each other so that their scrolling behavior still feels perfectly normal. In the case of table and collection views, the built-in cell reuse functionality is not affected.
- or

  into multiple simple data sources by splitting a table or collection view with multiple sections into one view per section and placing them below each other.
- Add header or footer views above or below a collection view without the need to have them managed by the collection view layout. These views can themselves be simple UIViews or UIScrollViews.

# Cell Reuse in Table and Collection Views

Before we take a look at the implementation, let’s review how table views and collection views work. Both [`UITableView`](https://developer.apple.com/library/ios/documentation/uikit/reference/UITableView_Class/Reference/Reference.html) and [`UICollectionView`](https://developer.apple.com/library/ios/documentation/uikit/reference/UICollectionView_class/Reference/Reference.html) are subclasses of [`UIScrollView`](https://developer.apple.com/Library/ios/documentation/UIKit/Reference/UIScrollView_Class/Reference/UIScrollView.html), and they mostly behave like standard scroll views. However, a key difference is that table views and collection views [reuse their cells](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UITableView_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40006943-CH3-SW92). As the view is scrolled, cells that scroll off the screen get removed from the view hierarchy and put into a reuse queue. Whenever a new cell is scrolled into view, the table view dequeues a cell from the reuse queue and re-adds it to the view hierarchy. This design conserves significant amounts of memory in views with lots of cells and minimizes expensive view allocations, which is especially important during fast scrolling.

<sub>An illustration of cell reuse in a `
    UITableView
    ` . Cells that are not in view are removed from the view hierarchy (indicated here by the dashed blue outline) and get added to the view as the scroll into view. Note that the table view’s frame (the light blue rectangle) is smaller than its content size (the dashed red outline), as is customary for scroll views. [Download the video (H.264)](https://oleb.net/media/table-view-cell-reuse-simulation.mp4).</sub>

# The Naïve Container View Approach

Placing multiple scroll views into a common container scroll view is actually pretty straightforward:

- that acts as the container view for the inner scroll views.
- Add the inner scroll views to the container view. These can be plain scroll views or table/collection views.
- . Position the inner scroll views below each other.
- to the combined size of the frames of its children.

By making the frames of the inner scroll views large enough to fit their entire content size, we ensure that they will never need to scroll. The only view that reacts to scrolling gestures is the container view. This avoids any interference between the inner scroll views and the container view in responding to gestures.

This setup works, but it has a significant drawback: it wastes memory. If the inner scroll views are table or collection views, they will create a cell for every single row because all rows are “visible” as far as they are concerned. If the collection view has hundreds or even thousands of cells, this can have a dramatic effect on your app’s memory usage (and performance, especially as the view is created).

<sub>An example of a naïve container scroll view implementation. Two table views are added as subviews of one container scroll view (black outline). The frames of the table views (the light blue and light orange rectangles) have been sized to fit their respective content size (dashed red outline). Note how this causes the table views’ cell reuse functionality to stop working: there is a cell object for every row, whether the row is currently visible (i.e., inside the black outline) or not. [Download the video (H.264)](https://oleb.net/media/naive-container-scrollview.mp4).</sub>

# OLEContainerScrollView

That’s where my custom container scroll view comes in. `OLEContainerScrollView` is a `UIScrollView` subclass that automatically arranges its child views in a stacked manner (sort of like [`NSStackView`](https://developer.apple.com/library/mac/documentation/AppKit/Reference/NSStackView_Class/Chapters/Reference.html) on OS X). It accepts all kinds of views as child views, not just scroll views — it handles scroll views in a special way, though.

## Adding Subviews

The container scroll view exposes a read-only `contentView` property. You should add any views you want managed by the container scroll view directly to the content view. I had to introduce the content view to keep the user-added subviews separate from the private subviews `UIScrollView` creates for its scroll indicators. When the container scroll view iterates over the subviews to adjust their layout, it should not touch the scroll indicators at all.

As a subview gets added, the container view performs these steps:

- If the new subview is an instance of `UIScrollView` (or one of its subclasses), disable the subview’s own scrolling with `subview.scrollEnabled = NO;`. This ensures that the container view itself handles all scroll gestures.
- Register for KVO notifications when the subview’s size changes. For regular UIViews, observe changes to the `frame` and `bounds` properties. For scroll views, observe changes to their `contentSize`. We need to do this to trigger a relayout whenever a subview’s size is changed by an outside caller.

## Adjusting Layout During Scrolling

During scrolling, the container view continuously adjusts the frames of its child views in the following manner:

- For regular

  s, reserve space according to the height of their

  rectangle. For scroll views, reserve enough vertical space to fit their

  . This means that the view coming after a scroll view will be positioned so far down that there is enough space above it to fit the scroll view’s entire content size.

- to the combined content size of all child views.

So far, this follows the naïve approach discussed above. What we want to do now is adjust the frames of any scroll views in the container view to the absolute minimum size required to fill the current viewport of the container view ([represented by its `bounds` rectangle](https://oleb.net/blog/2014/04/understanding-uiscrollview/)):

- whether its content rectangle intersects with the current viewport, and set its frame accordingly. This means that any scroll view’s frame will never be larger than the container view’s size, and views that are not in the visible region will have their frame heights set to

  .

Have a look at the video below to see how the algorithm works. At the beginning, the first table view fills the viewport of the container view (depicted by the black outline) entirely — its frame (light blue background) is equal to the container view’s bounds. The second table view is fully outside the viewport — its frame has a height of `0`, it is not visible. Consequently, it did not have to create any cells yet (the dashed orange outlines).

As the user scrolls, the second table view moves into view, and its frame (light orange background) grows from the bottom edge of the viewport until it eventually fully fills the viewport. At the same time, the blue table view’s frame shrinks to zero as it gets scrolled off the screen. Both table views can take full advantage of cell reuse at all times. Contrast this with the naïve approach above.

<sub>A demo of`OLEContainerScrollView` in action. [Download the video (H.264)](https://oleb.net/media/olecontainerscrollview-demo.mp4).</sub>

# The Code

This is the implementation of the `layoutSubviews` method that continually adjusts the layout during scrolling and when subviews are added, removed or resized:

```
@implementation OLEContainerScrollView

...

- (void)layoutSubviews
{
    [super layoutSubviews];

    // Translate the container view's content offset to contentView bounds.
    // This keeps the contentview always centered on the visible portion of the container view's
    // full content size, and avoids the need to make the contentView large enough to fit the
    // container view's full content size.
    self.contentView.frame = self.bounds;
    self.contentView.bounds = (CGRect){ self.contentOffset, self.contentView.bounds.size };

    // The logical vertical offset where the current subview (while iterating over all subviews)
    // must be positioned. Subviews are positioned below each other, in the order they were added
    // to the container. For scroll views, we reserve their entire contentSize.height as vertical
    // space. For non-scroll views, we reserve their current frame.size.height as vertical space.
    CGFloat yOffsetOfCurrentSubview = 0.0;

    for (UIView *subview in self.contentView.subviews)
    {
        if ([subview isKindOfClass:[UIScrollView class]]) {
            UIScrollView *scrollView = (UIScrollView *)subview;
            CGRect frame = scrollView.frame;
            CGPoint contentOffset = scrollView.contentOffset;

            // Translate the logical offset into the sub-scrollview's real content offset and frame size.
            // Methodology:

            // (1) As long as the sub-scrollview has not yet reached the top of the screen, set its scroll position
            // to 0.0 and position it just like a normal view. Its content scrolls naturally as the container
            // scroll view scrolls.
            if (self.contentOffset.y < yOffsetOfCurrentSubview) {
                contentOffset.y = 0.0;
                frame.origin.y = yOffsetOfCurrentSubview;
            }
            // (2) If the user has scrolled far enough down so that the sub-scrollview reaches the top of the
            // screen, position its frame at 0.0 and start adjusting the sub-scrollview's content offset to
            // scroll its content.
            else {
                contentOffset.y = self.contentOffset.y - yOffsetOfCurrentSubview;
                frame.origin.y = self.contentOffset.y;
            }

            // (3) The sub-scrollview's frame should never extend beyond the bottom of the screen, even if its
            // content height is potentially much greater. When the user has scrolled so far that the remaining
            // content height is smaller than the height of the screen, adjust the frame height accordingly.
            CGFloat remainingBoundsHeight = fmax(CGRectGetMaxY(self.bounds) - CGRectGetMinY(frame), 0.0);
            CGFloat remainingContentHeight = fmax(scrollView.contentSize.height - contentOffset.y, 0.0);
            frame.size.height = fmin(remainingBoundsHeight, remainingContentHeight);
            frame.size.width = self.contentView.bounds.size.width;

            scrollView.frame = frame;
            scrollView.contentOffset = contentOffset;

            yOffsetOfCurrentSubview += scrollView.contentSize.height;
        }
        else {
            // Normal views are simply positioned at the current offset
            CGRect frame = subview.frame;
            frame.origin.y = yOffsetOfCurrentSubview;
            frame.size.width = self.contentView.bounds.size.width;
            subview.frame = frame;

            yOffsetOfCurrentSubview += frame.size.height;
        }
    }

    self.contentSize = CGSizeMake(self.bounds.size.width, fmax(yOffsetOfCurrentSubview, self.bounds.size.height));
}

@end
```

The rest of the code is boilerplate. You can check it out [on GitHub](https://github.com/ole/OLEContainerScrollView).

# Auto Layout

A word about auto layout: `OLEContainerScrollView` does not use auto layout internally, and it would be impossible to declare the intended behavior with layout constraints. ([`UIScrollView` and auto layout are not exactly best friends](https://developer.apple.com/LIBRARY/ios/technotes/tn2154/_index.html), anyway.) Yet, it should be no problem to _use_ this class in conjunction with other views that do use auto layout internally. As I said before, you can [mix auto layout and manual layout code freely](https://oleb.net/blog/2014/03/how-i-learned-to-stop-worrying-and-love-auto-layout/).

# Where is the Podspec?

I have deliberately not (yet) made `OLEContainerScrollView` into a [CocoaPod](http://cocoapods.org/). I wrote this class to solve a very specific problem I had and while I believe it does have potential to grow into a generic component, it is definitely not there yet. Limitations include:

- It only supports vertically stacked layouts (and vertical scrolling) at the moment.
- The stack layout is very inflexible. It resizes all subviews to the width of the container. It does not support spacing between or free positioning of the subviews.
- Content size changes of the subviews are observed, but not animated nicely in the case of table or collection views. This is a big limitation for many use cases and does not seem easy to solve in a generic way, unfortunately.

If you are interested in using the class, I encourage you to take a look at the code and adopt it to your needs.

# Conclusion

Placing multiple (scroll) views into a common container scroll view is not an everyday requirement, but it can help simplify your table/collection view data sources and layout code by giving you the option to split sections into separate views.

`OLEContainerScrollView` is certainly not a full-featured component at the moment, but I hope it is still helpful to you. At any rate, writing it helped me deepen my understanding of `UIScrollView` and UIKit coordinate systems.

1. This is something that I’d like to make more flexible in a future version. At the moment, the class only supports vertically stacked layouts. [↩︎](#fnref:1)
2. I only do this for views that are subclasses of UIScrollView at the moment. The frame heights of regular UIViews remain unchanged even when they are not in the viewport. I do this to avoid any layout changes (or auto layout failures) that could be caused by resizing a view to zero that does not expect it. Changing this behavior would be a trivial change. [↩︎](#fnref:2)
