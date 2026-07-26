---
title: 'A ZoomingViewController to animate a UIView to fullscreen | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/09/zoomingviewcontroller-to-animate-uiview.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:e07ff7d3ee050a2d'
translated: false
---

> 原文：[A ZoomingViewController to animate a UIView to fullscreen | Cocoa with Love](https://www.cocoawithlove.com/2010/09/zoomingviewcontroller-to-animate-uiview.html)　·　Cocoa with Love (Matt Gallagher)

`ZoomingViewController` is a class you can attach to any existing view that will let you zoom the view to fullscreen with a single tap, rotate the view while in fullscreen by rotating the device and tap to return to the original inline state.

## Introduction

The `ZoomingViewController` class in this week's sample project handles the zooming in the following sample app:

![](https://www.cocoawithlove.com/assets/objc-era/zoomingviewcontroller.png)

The animation between the inline and fullscreen states is smooth and you can rotate the device in fullscreen to rotate the view.

You can attach the `ZoomingViewController` to any view to add this behavior.

> and the complete sample project used in this post here
> 
> TapZoomRotate.zip
> 
> (160kb)

## Requirements

The `ZoomingViewController` has three primary requirements:

- Respond to tap actions
- Smoothly zoom between different superviews
- Allow the view to rotate in fullscreen

## Responding to tap actions

Most of the time, you don't need to handle tap actions yourself — controls like buttons or table view cells all have built-in tap detection.

Prior to iOS 3.2, detecting a tap meant implementing `touchesBegan:withEvent:` and `touchesEnded:withEvent:` in the view or responder chain. This was fiddly since you had to perform time and location based calculations yourself to determine if the tap completed validly. Further, it would not have worked for this `ZoomingViewController` class, which only attaches to the view rather than being part of the the view or responder chain implementation.

Fortunately, the gesture recognizers introduced in iOS 3.2 make this trivially easy:

```objc
singleTapGestureRecognizer =
    [[UITapGestureRecognizer alloc]
        initWithTarget:self action:@selector(toggleZoom:)];
singleTapGestureRecognizer.numberOfTapsRequired = 1;

[self.view addGestureRecognizer:singleTapGestureRecognizer];
```

## Smoothly zooming between different superviews

First, we need to remember the old superview and location within it. We do this by inserting a proxy view into the hierarchy at the view's location — this way, it will also track the autoresized location of the view if the window rotates.

```objc
proxyView = [[UIView alloc] initWithFrame:self.view.frame];
proxyView.hidden = YES;
proxyView.autoresizingMask = self.view.autoresizingMask;
[self.view.superview addSubview:proxyView];
```

Then, we need to calculate our current position in the coordinate space of the target view (the target view is the window itself for animating to fullscreen). With this location calculated, we switch superview to the target view and set the frame to this calculated position.

```objc
CGRect frame =
    [self.view.window
        convertRect:self.view.frame
        fromView:proxyView.superview];
[self.view.window addSubview:self.view];
self.view.frame = frame;
```

Then, we animate from this calculated position to actually fill the screen:

```objc
[UIView
    animateWithDuration:0.2
    animations:^{
        self.view.frame = self.view.window.bounds;
    }];
[[UIApplication sharedApplication]
    setStatusBarHidden:YES
    withAnimation:UIStatusBarAnimationFade];
```

## Allowing the view to rotate in fullscreen

`ZoomingViewController` is not actually a subclass of `UIViewController`. Even though it "controls" a view for the purpose of zooming in and out, it doesn't require any of the behavior from `UIViewController` to do this.

Even if you did make the class a `UIViewController` subclass, it still wouldn't let you use the auto rotate behavior built into `UIViewController`. The reason is that `shouldAutorotateToInterfaceOrientation:` is only invoked on the first `UIViewController` found in the window. Since the fullscreen view will always be the second view in the window (after the inline view from which it zoomed), the `UIViewController` auto rotate behavior won't be able to satisfy our rotation needs.

So we need to implement rotation ourselves. This requires 3 steps:

- Determine the correct fullscreen bounds for a given orientation
- to transform from the current bounds to the new bounds after a rotation
- and actually apply these new values when things change

Getting the bounds for the fullscreen view based on the orientation is pretty simple too. We do need to account for the strangeness of face up and face down orientations — I do this by taking the status bar orientation in these cases instead (I don't use the status bar all the time in case it is out of sync with the actual device for some reason).

```objc
- (CGRect)rotatedWindowBounds
{
    UIDeviceOrientation orientation = [[UIDevice currentDevice] orientation];
    if (orientation == UIDeviceOrientationFaceUp ||
        orientation == UIDeviceOrientationFaceDown)
    {
        orientation = [UIApplication sharedApplication].statusBarOrientation;
    }
    
    if (orientation == UIDeviceOrientationLandscapeLeft ||
        orientation == UIDeviceOrientationLandscapeRight)
    {
        CGRect windowBounds = self.view.window.bounds;
        return CGRectMake(0, 0, windowBounds.size.height, windowBounds.size.width);
    }

    return self.view.window.bounds;
}
```

After a `UIDeviceOrientationDidChangeNotification`, we apply these new bounds.

Unfortunately, applying different bounds has the effect of changing the coordinates of view's midpoint. Since the final step of rotating the view requires applying a rotation transformation and rotations are always performed around the midpoint of the view, we must also translate the view in situations where the bounds have changed so that the midpoint is the same as it was previously.

```objc
- (CGAffineTransform)orientationTransformFromSourceBounds:(CGRect)sourceBounds
{
    UIDeviceOrientation orientation = [[UIDevice currentDevice] orientation];
    if (orientation == UIDeviceOrientationFaceUp ||
        orientation == UIDeviceOrientationFaceDown)
    {
        orientation = [UIApplication sharedApplication].statusBarOrientation;
    }
    
    if (orientation == UIDeviceOrientationPortraitUpsideDown)
    {
        return CGAffineTransformMakeRotation(M_PI);
    }
    else if (orientation == UIDeviceOrientationLandscapeLeft)
    {
        CGRect windowBounds = self.view.window.bounds;
        CGAffineTransform result = CGAffineTransformMakeRotation(0.5 * M_PI);
        result = CGAffineTransformTranslate(result,
            0.5 * (windowBounds.size.height - sourceBounds.size.width),
            0.5 * (windowBounds.size.height - sourceBounds.size.width));
        return result;
    }
    else if (orientation == UIDeviceOrientationLandscapeRight)
    {
        CGRect windowBounds = self.view.window.bounds;
        CGAffineTransform result = CGAffineTransformMakeRotation(-0.5 * M_PI);
        result = CGAffineTransformTranslate(result,
            0.5 * (windowBounds.size.width - sourceBounds.size.height),
            0.5 * (windowBounds.size.width - sourceBounds.size.height));
        return result;
    }

    return CGAffineTransformIdentity;
}
```

Finally, we apply alls these values in response to the `UIDeviceOrientationDidChangeNotification`. Listening to the notification is easy, we just add ourselves as an observer when switching into fullscreen display:

```objc
[[NSNotificationCenter defaultCenter]
    addObserver:self
    selector:@selector(deviceRotated:)
    name:UIDeviceOrientationDidChangeNotification
    object:[UIDevice currentDevice]];
```

The only additional point to note is that when a view rotates, it exposes the view behind its corners briefly. To avoid this potentially unappealing situation, the `ZoomingViewController` uses a blanking view (a basic black view) that it inserts behind the view being rotated and removes when the rotation is complete.

The implementation of `deviceRotated:` contains the following code that creates and inserts the blanking view and applies the rotation in response to the `UIDeviceOrientationDidChangeNotification`:

```objc
CGRect windowBounds = self.view.window.bounds;
UIView *blankingView =
    [[[UIView alloc] initWithFrame:
        CGRectMake(-0.5 * (windowBounds.size.height - windowBounds.size.width),
            0, windowBounds.size.height, windowBounds.size.height)] autorelease];
blankingView.backgroundColor = [UIColor blackColor];
[self.view.superview insertSubview:blankingView belowSubview:self.view];

[UIView animateWithDuration:0.25 animations:^{
    self.view.bounds = [self rotatedWindowBounds];
    self.view.transform = [self orientationTransformFromSourceBounds:self.view.bounds];
} completion:^(BOOL complete){
    [blankingView removeFromSuperview];
}];
```

## Conclusion

> and the complete sample project used in this post here
> 
> TapZoomRotate.zip
> 
> (160kb)

`ZoomingViewController` is as simple to use as possible: create it, set its view and the view will immediately start responding to taps, zooming to fullscreen and rotating in fullscreen mode. You can apply it to any view in your hierarchy at any time where you need fullscreen display behavior.
