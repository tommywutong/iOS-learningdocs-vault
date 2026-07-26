---
title: 'Synthesizing a touch event on the iPhone | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/10/synthesizing-touch-event-on-iphone.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:12536a9ecfd59e0a'
translated: false
---

> 原文：[Synthesizing a touch event on the iPhone | Cocoa with Love](https://www.cocoawithlove.com/2008/10/synthesizing-touch-event-on-iphone.html)　·　Cocoa with Love (Matt Gallagher)

The iPhone lacks specific methods to create UIEvent and UITouch objects. I'll show you how to add this functionality so you can write programmatically driven user-interfaces.

> **Update #1**: Added a "Device SDK" version that will link correctly outside of the "Simulator SDK".  
> **Update #2**: Two bugs have been fixed since the code was originally posted... the objects in the `UIEvent` member `_keyedTouches` are now `NSSet`s and the `_view` and `_window` in `UITouch` are now retained.  
> **Update #3**: changes to the `UITouch` and `UIEvent` categories as well as `performTouchInView:` to support SDK 2.2 changes.  
> **Update #4**: Support for SDK 3.0.

## A warning before we begin...

The content of this post is for **_debugging and testing only_**. Do not submit this code in an application to the App Store. Doing so will likely result in:

- A bad UI experience for your users.
- An app that breaks on every OS update.
- Rejection of your application.

Synthesized touches are never the right way to trigger actions in a real application. The only useful use for this post is in automated user testing (see my later post [Automated User Interface Testing on the iPhone](https://www.cocoawithlove.com/2008/11/automated-user-interface-testing-on.html)).

## User-interface testing

When running application tests, it is helpful to be able to generate user events to test your user-interface. That way, you can run user-interface tests automatically instead of manually.

On Cocoa Senior (also known as "the Mac") we have methods like the gargantuan:

to generate events.

Cocoa Junior on the iPhone doesn't have any methods like this, so we must work out how to achieve it ourselves.

## UITouch category

A basic touch event normally consists of three objects:

- The UITouch object — which will be used for the touch down and touch up
- A first UIEvent to wrap the touch down
- A second UIEvent to wrap the touch up

Lets look first at creating the UITouch object. Since most of the fields in this object are private, we can't sublcass it or set them directly — everything must be done on a category. My category goes something like this:

```objc
@implementation UITouch (Synthesize)

- (id)initInView:(UIView *)view
{
    self = [super init];
    if (self != nil)
    {
        CGRect frameInWindow;
        if ([view isKindOfClass:[UIWindow class]])
        {
            frameInWindow = view.frame;
        }
        else
        {
            frameInWindow =
                [view.window convertRect:view.frame fromView:view.superview];
        }
         
        _tapCount = 1;
        _locationInWindow =
            CGPointMake(
                frameInWindow.origin.x + 0.5 * frameInWindow.size.width,
                frameInWindow.origin.y + 0.5 * frameInWindow.size.height);
        _previousLocationInWindow = _locationInWindow;

        UIView *target = [view.window hitTest:_locationInWindow withEvent:nil];
        _view = [target retain];
        _window = [view.window retain];
        _phase = UITouchPhaseBegan;
        _touchFlags._firstTouchForView = 1;
        _touchFlags._isTap = 1;
        _timestamp = [NSDate timeIntervalSinceReferenceDate];
    }
    return self;
}

- (void)changeToPhase:(UITouchPhase)phase
{
    _phase = phase;
    _timestamp = [NSDate timeIntervalSinceReferenceDate];
}

@end
```

This method builds a touch in the center of the specified UIView (window coordinates must be used).

You should note that this category includes the changeToPhase: method. This phase (set to UITouchPhaseBegan in the initInView: method) refers to the begin/drag/ended state of the touch operation. We need a method to change the state because the same UITouch object must be used for touch began and touch ended events (otherwise the whole windowing system crashes).

## UIEvent category

The UIEvent object is mostly handled through an existing private method (`_initWithEvent:touches:)`. There are two difficulties with this method though:

- We must provide it a `GSEvent` object (or something very close to it)
- We must allocate the object as a UITouchesEvent on SDK 3.0 and later but as a UIEvent on earlier versions.

Here's how all that will look:

```objc
@interface UIEvent (Creation)
- (id)_initWithEvent:(GSEventProxy *)fp8 touches:(id)fp12;
@end

@implementation UIEvent (Synthesize)

- (id)initWithTouch:(UITouch *)touch
{
    CGPoint location = [touch locationInView:touch.window];
    GSEventProxy *gsEventProxy = [[GSEventProxy alloc] init];
    gsEventProxy->x1 = location.x;
    gsEventProxy->y1 = location.y;
    gsEventProxy->x2 = location.x;
    gsEventProxy->y2 = location.y;
    gsEventProxy->x3 = location.x;
    gsEventProxy->y3 = location.y;
    gsEventProxy->sizeX = 1.0;
    gsEventProxy->sizeY = 1.0;
    gsEventProxy->flags = ([touch phase] == UITouchPhaseEnded) ? 0x1010180 : 0x3010180;
    gsEventProxy->type = 3001;    
    
    //
    // On SDK versions 3.0 and greater, we need to reallocate as a
    // UITouchesEvent.
    //
    Class touchesEventClass = objc_getClass("UITouchesEvent");
    if (touchesEventClass && ![[self class] isEqual:touchesEventClass])
    {
        [self release];
        self = [touchesEventClass alloc];
    }
    
    self = [self _initWithEvent:gsEventProxy touches:[NSSet setWithObject:touch]];
    if (self != nil)
    {
    }
    return self;
}

@end
```

You can see that most of the setup is simply concerned with filling in the fields of the `GSEventProxy` object which is the pretend object that we substitute in place of the actual `GSEvent` object (which can't be easily allocated).

The fields and values used are determined simply by staring at real `GSEvent` structures in the debugger until the values for fields could be determined.

The definition of this object follows. You'll need to place it before the previous `UIEvent` category implemention.

```objc
@interface GSEventProxy : NSObject
{
@public
    unsigned int flags;
    unsigned int type;
    unsigned int ignored1;
    float x1;
    float y1;
    float x2;
    float y2;
    unsigned int ignored2[10];
    unsigned int ignored3[7];
    float sizeX;
    float sizeY;
    float x3;
    float y3;
    unsigned int ignored4[3];
}
@end
@implementation GSEventProxy
@end
```

## Sending the event

There is no API to route the events to the appropriate view — so we will just invoke the methods directly on the view ourselves.

Using the above categories to create the UITouch and UIEvent objects, dispatching a touch event to a UIView looks like this:

```objc
- (void)performTouchInView:(UIView *)view
{
    UITouch *touch = [[UITouch alloc] initInView:view];
    UIEvent *eventDown = [[UIEvent alloc] initWithTouch:touch];
    
    [touch.view touchesBegan:[eventDown allTouches] withEvent:eventDown];
    
    [touch setPhase:UITouchPhaseEnded];
    UIEvent *eventUp = [[UIEvent alloc] initWithTouch:touch];
    
    [touch.view touchesEnded:[eventUp allTouches] withEvent:eventUp];
    
    [eventDown release];
    [eventUp release];
    [touch release];
}
```

## Legality of use and risks

The approach used in this post constitutes _using an undisclosed API_ — it is therefore illegal to submit applications to the App Store that use this approach, according to the iPhone SDK Agreement.

In terms of risks, this type of undisclosed API use has a high probability of breaking on every update to the iPhone OS — yet another reason why this code is for in-house developer use only.

If you use this code, **only use it in a separate target for testing purposes only**. Do not submit this code to the App Store.

## Conclusion

> You can download a copy of TouchSynthesis.m as part of the [SelfTesting project](https://www.cocoawithlove.com/assets/objc-era/SelfTesting.zip) (from my later post [Automated User Interface Testing on the iPhone](https://www.cocoawithlove.com/2008/11/automated-user-interface-testing-on.html)).

I have only tested this for performing touch events in UITableViewCells in a UINavigationController — navigating a hierarchy to verify that the hierarchy works. Of course, once you've programmatically navigated, you must also read back from the hierarchy to ensure that required features are present — but that's a post for a different time.

Working directly with the fields of a class is always a little risky. I'm sure there are UIViews that won't work well with this type of synthetic touch. Apple is also free to change the meaning of any fields at any time so this code is prone to break frequently.

Finally, remember to keep this type of testing code in a separate target so it isn't included in the application you submit to the App Store. I don't want to see your projects break or be rejected because you're trying to invoke use undisclosed APIs in your final application.
