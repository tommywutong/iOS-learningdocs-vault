---
title: Animation Programming Guide for Cocoa
apple_id: TP40003592
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2006-05-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AnimationGuide/Articles/TimingAnimations.html
archived_at: '2026-07-15T05:25:26.386554Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Animation Programming Guide for Cocoa](Introduction%20to%20Animation%20Programming%20Guide%20for%20Cocoa.md)


[Next](Animating%20Views%20and%20Windows.md)[Previous](Introduction%20to%20Animation%20Programming%20Guide%20for%20Cocoa.md)

# Using an NSAnimation Object

The `NSAnimation` class provides sophisticated behavior for animations that occur over a finite length of time. OS X uses animation objects to implement transition animations for user interface elements. You can define custom animation objects to implement animations for your own code. Unlike `NSTimer`, animation notifications can occur at irregular intervals, allowing you to create animations that appear to speed up or slow down.

The sections that follow cover the basic steps for creating a custom `NSAnimation` object and using it to manage your animated content. If you want to animate your views and windows, you should see if the `NSViewAnimation` class (which is a subclass of `NSAnimation`) offer the behavior you need. View animation objects provide sophisticated behavior for resizing and moving views over time and are described in [Animating Views and Windows](Animating%20Views%20and%20Windows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztkojtfvjvomi).

An `NSAnimation` object has several important attributes:

- Current progress—A value between 0.0 and 1.0 that indicates the percentage of the animation completed.
- Frame rate—The number of updates per second.
- Duration—The period (in seconds) over which the animation occurs.
- Animation curve—The relative speed of the animation over its course; for example, the animation could slowly speed up at the beginning, gradually slow down near its end, or remain the same speed throughout.
- Blocking mode—The mode in which the animation runs in terms of the application’s responsiveness to user actions.

When you configure a new `NSAnimation` object, you must, at a minimum, set its duration, animation curve, frame rate, and blocking mode attributes. You should also assign a delegate to monitor the progress of the animation. When the animation begins, ends, is explicitly stopped, or reaches a progress mark, the animation object sends a message to the current delegate. (See [Setting and Handling Progress Marks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztkobrfvbuuqsiijdemsa) for information about progress marks). If you do not want to use a delegate, you must subclass `NSAnimation` to receive progress information; see [Subclassing NSAnimation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztkobrfvbuuqshi5cecra).

Listing 1 shows a sample method that creates and configures a standard `NSAnimation` object. The object that created the animation acts as the delegate and handles any progress messages.

__Listing 1__  Initializing an NSAnimation object

```objc
- (id)init
{
    self = [super init];
    if (self)
    {
        // theAnim is an NSAnimation instance variable.
        theAnim = [[NSAnimation alloc] initWithDuration:10.0
                                     animationCurve:NSAnimationEaseIn];
        [theAnim setFrameRate:20.0];
        [theAnim setAnimationBlockingMode:NSAnimationNonblocking];
        [theAnim setDelegate:self];
    }
    return self;
}
```

The `initWithDuration:animationCurve:` method is the designated initializer for the `NSAnimation` class. This method lets you set two of the animation attributes. For the other attributes, you can use the default values or set the attribute value explicitly using the appropriate accessor methods. The default attributes are as follows:

- The default animation curve is `NSAnimationEaseInOut`.
- The default blocking mode is `NSAnimationBlocking`.
- The default frame rate is a reasonable value. This frame rate is usually 60 Hz, but the exact value should not be relied upon.

Once you have prepared an `NSAnimation` object for use, you can run it by sending it a `startAnimation` message. If you need to stop it before the animation completes its scheduled duration, send the object a `stopAnimation` message. The delegate of the `NSAnimation` object (if one exists) receives messages informing it of both of these events, as well as a message that tells it if the animation completed as scheduled.

`NSAnimation` has the notion of _progress marks_—floating-point values (of type `NSAnimationProgress`) that indicate the percentage amount of the animation that is complete. When you start an animation and it reaches a progress mark (specifically, its current progress is equal to the progress mark), the animation object sends a message to its delegate. The delegate can then update a custom progress indicator, play a sound, or accomplish some other effect appropriate to that point of the animation.

Usually you set the progress marks for an animation object when you first create and initialize the object. Listing 2 shows one approach that sets 20 equally spaced progress marks.

__Listing 2__  Setting the progress marks of an NSAnimation object

```objc
- (void)awakeFromNib
{
     NSAnimationProgress progMarks[] = {
            0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5,
            0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0  };

    int i, count = 20;
    // theAnim is an NSAnimation instance variable
    theAnim = [[NSAnimation alloc] initWithDuration:10.0
                                animationCurve:NSAnimationEaseInOut];
    [theAnim setFrameRate:20.0];
    [theAnim setDelegate:self];

    for (i=0; i<count; i++)
        [theAnim addProgressMark:progMarks[i]];
}
```

Instead of adding progress-mark values in a loop, as in this example, you can set them in one invocation by using the `setProgressMarks:` method, which takes an array of `NSNumber` objects encapsulating `float` values.

When a running animation object reaches a progress mark, it sends an `animation:didReachProgressMark:` message to its delegate. The delegate should handle this message in a way appropriate to the progress mark passed in. Listing 3 illustrates how the delegate implements this method to play a train sound at regular intervals.

__Listing 3__  Delegate implementation of animation:didReachProgressMark:

```objc
- (void)animation:(NSAnimation *)animation
            didReachProgressMark:(NSAnimationProgress)progress
{
    if (animation == theAnim)
        [[NSSound soundNamed:@"chug"] play];
}
```


Although you can use an `NSAnimation` object as-is for many purposes, subclassing it is a more common scenario. There are three major reasons to subclass `NSAnimation`:

- To achieve smooth animations by redrawing at per-frame intervals
- To specify valid run-loop modes when running an animation on the main thread in nonblocking mode
- To return custom curve values without the overhead of a delegate that responds to `animation:valueForProgress:`

The procedures for accomplishing the first two of these objectives are described in the following sections. To return custom curve values without implementing the delegate method, you must override the `currentValue` method. See the `NSAnimation` class documentation for further information.

As mentioned in [Setting and Handling Progress Marks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztkobrfvbuuqsiijdemsa), you can attach a series of progress marks to an `NSAnimation` object and have the delegate implement the `animation:didReachProgressMark:` method to redraw an object at each progress mark. However, this is not the best way to animate an object. Unless you set a large number of progress marks (30 per second or more), the animation is probably going to appear jerky.

A better approach is to subclass `NSAnimation` and override the `setCurrentProgress:` method, as illustrated in Listing 4. The `NSAnimation` object invokes this method after each frame to change the progress value. By intercepting this message, you can perform any redrawing or updating you need for that frame. If you do override this method, be sure to invoke the implementation of `super` so that it can update the current progress.

__Listing 4__  Overriding the setCurrentProgress: method

```objc
- (void)setCurrentProgress:(NSAnimationProgress)progress
{
    // Call super to update the progress value.
    [super setCurrentProgress:progress];

    // Update the window position.
    NSRect theWinFrame = [[NSApp mainWindow] frame];
    NSRect theScreenFrame = [[NSScreen mainScreen] visibleFrame];
    theWinFrame.origin.x = progress *
            (theScreenFrame.size.width - theWinFrame.size.width);
    [[NSApp mainWindow] setFrame:theWinFrame display:YES animate:YES];
}
```


An `NSAnimation` object with a blocking mode of `NSAnimationNonblocking` runs in the main thread of the process in a run-loop mode that accepts user input. Before it runs the animation, the animation object sends itself a `runLoopModesForAnimation` message to get the currently valid run-loop modes. By default, this method returns `nil`, which tells `NSAnimation` to use the default mode (`NSDefaultRunLoopMode`), modal panel mode (`NSModalPanelRunLoopMode`), and event tracking run-loop mode (`NSEventTrackingRunLoopMode`).

You can override this method to return a different set of run loop modes, which can include custom modes. Listing 5 shows an implementation that returns the default array of modes minus the event-tracking mode (`NSEventTrackingRunLoopMode`).

__Listing 5__  Returning run-loop modes from runLoopModesForAnimating

```objc
- (NSArray *)runLoopModesForAnimating
{
    return [NSArray arrayWithObjects: NSDefaultRunLoopMode,
                         NSModalPanelRunLoopMode, nil];
}
```


You can link two animation objects so that one of them starts running (or stops running) when the other reaches a specified animation mark. This feature of `NSAnimation` is useful for coordinating different effects. Listing 6 illustrates how the `startWhenAnimation:reachesProgress:` method is used to start an animation when another animation reaches the midway point.

__Listing 6__  Linking two animations

```objc
- (IBAction)startAnim:(id)sender
{
    // theAnim and theOtherAnim are variables of type NSAnimation.
    [theOtherAnim startWhenAnimation:theAnim reachesProgress:0.5];
    [theAnim startAnimation];
}
```

If you want instead to stop an animation when another animation reaches a progress mark, use the `stopWhenAnimation:reachesProgess:` method. You can link animations indefinitely, one after another. However, there can be only one “start” and one “stop” animation at any given time.

If you have a delegate that is responding to `animation:didReachProgressMark:` messages, it has to distinguish among the multiple animations, as in Listing 7.

__Listing 7__  Handling progress marks of simultaneously running animations

```objc
- (void)animation:(NSAnimation *)animation
            didReachProgressMark:(NSAnimationProgress)progress
{
    if (animation == theOtherAnim)
    {
        // Do an effect appropriate to progress mark.
    }
    else if (animation == theAnim)
    {
        // Do an effect appropriate to progress mark.
    }
}
```

[Next](Animating%20Views%20and%20Windows.md)[Previous](Introduction%20to%20Animation%20Programming%20Guide%20for%20Cocoa.md)

