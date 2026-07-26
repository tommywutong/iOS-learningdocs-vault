---
title: Understanding UIScrollView
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/04/understanding-uiscrollview/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:1bac4365c5dfba47'
translated: false
---

> 原文：[Understanding UIScrollView](https://oleb.net/blog/2014/04/understanding-uiscrollview/)　·　Ole Begemann

# Understanding UIScrollView

I am a big fan of Mike Ash’s [Let’s Build …](https://mikeash.com/pyblog/?tag=letsbuild) series of articles, in which he explains how certain Cocoa features work by rebuilding them from scratch. In this post, I am gonna try to do something similar by writing my own little scroll view with just a few lines of code.

But first, let’s take a closer look how coordinate systems work in UIKit. Feel free to skip the next section if you are only interested in the scroll view implementation.

# Coordinate Systems

Every [view](https://developer.apple.com/library/ios/documentation/uikit/reference/UIView_Class/UIView/UIView.html) defines its own coordinate system. It looks like this, with the x-axis pointing to the right and the y-axis pointing down:

![A standard x/y coordinate system with the x-axis pointing right and the y-axis pointing down](https://oleb.net/media/uikit-coordinate-system-1400px.png)

<sub>A UIView coordinate system.</sub>

Note that this logical coordinate system does not concern itself with the width and height of the view. It has no boundaries and extends infinitely in all four directions.[1](#fn:1) Now let’s lay out a few items (a.k.a. subviews) in this coordinate system. Each colored rectangle stands for a subview:

![Four rectangles with different colors and sizes placed at different coordinates in the coordinate system](https://oleb.net/media/uikit-coordinate-system-with-subviews.png)

<sub>Adding subviews to the coordinate system.</sub>

In code, the setup would look like this:

```
UIView *redView = [[UIView alloc] initWithFrame:CGRectMake(20, 20, 100, 100)];
redView.backgroundColor = [UIColor colorWithRed:0.815 green:0.007
    blue:0.105 alpha:1];

UIView *greenView = [[UIView alloc] initWithFrame:CGRectMake(150, 160, 150, 200)];
greenView.backgroundColor = [UIColor colorWithRed:0.494 green:0.827
    blue:0.129 alpha:1];

UIView *blueView = [[UIView alloc] initWithFrame:CGRectMake(40, 400, 200, 150)];
blueView.backgroundColor = [UIColor colorWithRed:0.29 green:0.564
    blue:0.886 alpha:1];

UIView *yellowView = [[UIView alloc] initWithFrame:CGRectMake(100, 600, 180, 150)];
yellowView.backgroundColor = [UIColor colorWithRed:0.972 green:0.905
    blue:0.109 alpha:1];

[mainView addSubview:redView];
[mainView addSubview:greenView];
[mainView addSubview:blueView];
[mainView addSubview:yellowView];
```

## Bounds

The `UIView` documentation says this about the [`bounds`](https://developer.apple.com/library/ios/documentation/uikit/reference/UIView_Class/UIView/UIView.html#//apple_ref/doc/uid/TP40006816-CH3-SW1) property:

> The bounds rectangle … describes the view’s location and size in its own coordinate system.

**A view can be considered a window or viewport into a rectangular area of the plane defined by its coordinate system.** And the view’s `bounds` express the location and size of this rectangle.

Say our view’s `bounds` rectangle has a width and height of 320 by 480 points and its origin is the default `(0, 0)`. The view becomes a viewport into the coordinate system plane, displaying a small part of the entire plane. Everything outside the bounds is still there, only hidden:[2](#fn:2)

![A viewport of 320 by 480 points provides a viewport into the coordinate system. Some of the rectangles are inside the viewport and some outside.](https://oleb.net/media/uikit-coordinate-system-viewport.png)

<sub>A view provides a viewport into the plane defined by its coordinate system. The view’s bounds rectangle describe the position and size of the visible area.</sub>

## Frame

Next, we will modify the origin of the bounds rectangle:

```
CGRect bounds = mainView.bounds;
bounds.origin = CGPointMake(0, 100);
mainView.bounds = bounds;
```

The origin of the bounds rectangle is now at `(0, 100)` so our scene looks like this:

![The viewport has moved down by 100 points, making a different area of the coordinate system visible.](https://oleb.net/media/uikit-coordinate-system-viewport-scrolled.png)

<sub>Modifying the origin of the bounds rectangle is equivalent to moving the viewport.</sub>

It looks as though the view has moved down by 100 points, and this is in fact true in relation to its own coordinate system. The view’s _actual_ position on the screen (or in its superview, to put it more accurately) remains fixed, however, as that is determined by its [`frame`](https://developer.apple.com/library/ios/documentation/uikit/reference/UIView_Class/UIView/UIView.html#//apple_ref/doc/uid/TP40006816-CH3-SW5), which has not changed:

> The frame rectangle … describes the view’s location and size in its superview’s coordinate system.

Since the view’s position is fixed (from its own perspective), think of the coordinate system plane as a piece of transparent film we can drag around, and of the view as a fixed window we are looking through. Adjusting the `bounds`’s origin is equivalent to moving the transparent film such that another part of it becomes visible through the view:

![Animation illustrating the movement of the coordinate system caused by a change of the bounds origin](https://oleb.net/media/uikit-coordinate-system-bounds-animation.gif)

<sub>Modifying the origin of the bounds rectangle is equivalent to moving the coordinate system in the opposite direction while the view’s position remains fixed because its frame does not change.</sub>

And this is exactly what [`UIScrollView`](https://developer.apple.com/library/ios/documentation/uikit/reference/uiscrollview_class/Reference/UIScrollView.html) does when it scrolls. Note that from the perspective of the user it appears as though the view’s subviews are moving, although their positions in terms of the view’s coordinate system (in other words, their frames) remain unchanged.

# Let’s Build UIScrollView

A scroll view does not need to constantly update the coordinates of its subviews to make them scroll. All it has to do is adjust the origin of its bounds. With that knowledge, implementing a very simple scroll view is trivial. We set up a gesture recognizer to detect the user’s pan gestures, and in response to a gesture we translate the view’s `bounds` by the dragged amount:

```
// CustomScrollView.h
@import UIKit;

@interface CustomScrollView : UIView

@property (nonatomic) CGSize contentSize;

@end

// CustomScrollView.m
#import "CustomScrollView.h"

@implementation CustomScrollView

- (id)initWithFrame:(CGRect)frame
{
    self = [super initWithFrame:frame];
    if (self == nil) {
        return nil;
    }
    UIPanGestureRecognizer *gestureRecognizer = [[UIPanGestureRecognizer alloc]
        initWithTarget:self action:@selector(handlePanGesture:)];
    [self addGestureRecognizer:gestureRecognizer];
    return self;
}

- (void)handlePanGesture:(UIPanGestureRecognizer *)gestureRecognizer
{
    CGPoint translation = [gestureRecognizer translationInView:self];
    CGRect bounds = self.bounds;

    // Translate the view's bounds, but do not permit values that would violate contentSize
    CGFloat newBoundsOriginX = bounds.origin.x - translation.x;
    CGFloat minBoundsOriginX = 0.0;
    CGFloat maxBoundsOriginX = self.contentSize.width - bounds.size.width;
    bounds.origin.x = fmax(minBoundsOriginX, fmin(newBoundsOriginX, maxBoundsOriginX));

    CGFloat newBoundsOriginY = bounds.origin.y - translation.y;
    CGFloat minBoundsOriginY = 0.0;
    CGFloat maxBoundsOriginY = self.contentSize.height - bounds.size.height;
    bounds.origin.y = fmax(minBoundsOriginY, fmin(newBoundsOriginY, maxBoundsOriginY));

    self.bounds = bounds;
    [gestureRecognizer setTranslation:CGPointZero inView:self];
}

@end
```

Just like the real `UIScrollView`, our class has a `contentSize` property that must be set from the outside to define the extent of the scrollable area. When we adjust the bounds, we make sure to only allow valid values.

The result:

![Animated GIF showing our custom scroll view implementation](https://oleb.net/media/custom-scrollview-animation.gif)

<sub>Our custom scroll view in action. Note that it lacks momentum scrolling, bouncing, and scroll indicators.</sub>

# Conclusion

Thanks to the nested nature of coordinate systems in UIKit, it takes less than 30 lines of code to reimplement the essence of `UIScrollView`. Of course, there is a lot more to the real `UIScrollView` than just this. Momentum scrolling, bouncing, scroll indicators, zooming, and delegate methods are just some of the features we have not implemented here.

**Update May 2, 2014:** The code is now [available on GitHub](https://github.com/ole/CustomScrollView).

**Update May 8, 2014:** Check out the [follow-up post](https://oleb.net/blog/2014/05/scrollview-inertia-bouncing-rubberbanding/) for added features like inertial scrolling, bouncing, and rubber-banding.

1. Not really _infinitely_. The extent of the coordinate system is limited by the size of the `CGFloat` data type (32 bits on 32-bit systems and 64 bits on 64-bit), which is plenty big enough in practice. [↩︎](#fnref:1)
2. Actually, unless `clipsToBounds == YES` (the default is `NO`), subviews outside the bounds rectangle will remain visible. The view does not detect touches outside its bounds, though. [↩︎](#fnref:2)
