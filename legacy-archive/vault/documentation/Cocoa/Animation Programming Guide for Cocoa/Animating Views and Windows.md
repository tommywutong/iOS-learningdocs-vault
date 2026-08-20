---
title: Animation Programming Guide for Cocoa
apple_id: TP40003592
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2006-05-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AnimationGuide/Articles/ViewAnimations.html
archived_at: '2026-07-15T05:25:26.397501Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Animation Programming Guide for Cocoa](Introduction%20to%20Animation%20Programming%20Guide%20for%20Cocoa.md)


[Next](Document%20Revision%20History.md)[Previous](Using%20an%20NSAnimation%20Object.md)

# Animating Views and Windows

The `NSViewAnimation` class is a subclass of `NSAnimation` that provides a convenient way to animate aspects of your view and window objects, including the following:

- Change the position of the frame.
- Change the size of the frame
- Change the opacity of the object and fade it in or out.

You use view animation objects in a slightly different way than you do regular `NSAnimation` objects. A single view animation object can manage the animation process for multiple views and windows simultaneously. Rather than setting the attributes using methods of the animation object, you instead create a dictionary of animation attributes for each view or window you want to modify. Each dictionary specifies the target of the action (the view or window), and the effects you want to apply to that target. To set other factors, such as the duration and timing curve of the animation, you continue to use the methods of `NSAnimation`.

An animation attributes dictionary has only one required value: the target object. You add this object to the dictionary using the `NSViewAnimationTargetKey` key. The presence of this key alone, though, does not change the view or window. To make changes, you must include one or more additional keys to specify the desired behavior.

You can perform multiple actions on a single target object simultaneously, if you choose. For example, you can resize a view, change its position on the screen, and fade it in or out all at once. The following sections show you how to perform each of these actions separately, for simplicity. To perform them both, simply add all of the relevant keys to the attributes dictionary.

Changing the frame rectangle of a view or window lets you resize and reposition that object relative to its parent. In the case of views, this means changing the position and size of the view in its superview. In the case of windows, it means changing the position and size of the window on the desktop. Table 1 lists the keys and values you would put into the attributes dictionary to change the frame rectangle.

__Table 1__  Keys for resizing or repositioning a view or window.

| Key | Value | Description |
| `NSViewAnimationTargetKey` | `id` | Identifies the `NSView` or `NSWindow` object to resize or reposition. This key is required. |
| `NSViewAnimationStartFrameKey` | `NSValue` | Contains the starting frame rectangle of the target object. The `NSValue` object should contain an encoded `NSRect` data type. This value is typically equal to the current frame of the view or window. This key is optional and defaults to the current frame rectangle of the target object. |
| `NSViewAnimationEndFrameKey` | `NSValue` | Contains the ending frame rectangle of the target object. The `NSValue` object should contain an encoded `NSRect` data type. This key is recommended; if not present, it defaults to the current frame rectangle of the target object. |

If you want to hide a view or window, rather than have the object suddenly disappear, you can use a view animation to make that object gradually fade away. Similarly, you can use a similar type of view animation to make the object visible again. When fading a view back in, the size of the ending frame rectangle must be non-zero; if it is not, the view remains hidden. Table 2 lists the keys and values you would put into the attributes dictionary to fade an object in or out.

__Table 2__  Keys for fading a view or window.

| Key | Value | Description |
| `NSViewAnimationTargetKey` | `id` | Identifies the `NSView` or `NSWindow` object to modify. This key is required. |
| `NSViewAnimationEffectKey` | `NSString` | Contains one of the following string constants: `NSViewAnimationFadeInEffect` makes the object visible and `NSViewAnimationFadeOutEffect` hides it. These effects change the opacity of the object over the course of the animation. |

Listing 1 illustrates the basic use of a view animation object. The action method sets up attribute dictionaries for two different view objects and then runs the animation whenever the action occurs. For the first view object, the animation object shifts the origin of the view by 50 units along each axis. For the second view, the animation object shrinks the frame size to zero while simultaneously fading the view out until it is completely hidden. The animation uses a custom timing curve and duration but uses the default blocking mode, which blocks user input on the main thread until the animation is complete.

__Listing 1__  Animating two NSView objects

```objc
- (IBAction)startAnimations:(id)sender
{
    // firstView, secondView are outlets
    NSViewAnimation *theAnim;
    NSRect firstViewFrame;
    NSRect newViewFrame;
    NSMutableDictionary* firstViewDict;
    NSMutableDictionary* secondViewDict;

    {
        // Create the attributes dictionary for the first view.
        firstViewDict = [NSMutableDictionary dictionaryWithCapacity:3];
        firstViewFrame = [firstView frame];

        // Specify which view to modify.
        [firstViewDict setObject:firstView forKey:NSViewAnimationTargetKey];

        // Specify the starting position of the view.
        [firstViewDict setObject:[NSValue valueWithRect:firstViewFrame]
                 forKey:NSViewAnimationStartFrameKey];

        // Change the ending position of the view.
        newViewFrame = firstViewFrame;
        newViewFrame.origin.x += 50;
        newViewFrame.origin.y += 50;
        [firstViewDict setObject:[NSValue valueWithRect:newViewFrame]
                 forKey:NSViewAnimationEndFrameKey];
    }

    {
        // Create the attributes dictionary for the second view.
        secondViewDict = [NSMutableDictionary dictionaryWithCapacity:3];

        // Set the target object to the second view.
        [secondViewDict setObject:secondView forKey:NSViewAnimationTargetKey];

        // Shrink the view from its current size to nothing.
        NSRect viewZeroSize = [secondView frame];
        viewZeroSize.size.width = 0;
        viewZeroSize.size.height = 0;
        [secondViewDict setObject:[NSValue valueWithRect:viewZeroSize]
                 forKey:NSViewAnimationEndFrameKey];

        // Set this view to fade out
        [secondViewDict setObject:NSViewAnimationFadeOutEffect
                forKey:NSViewAnimationEffectKey];
    }

    // Create the view animation object.
    theAnim = [[NSViewAnimation alloc] initWithViewAnimations:[NSArray
                arrayWithObjects:firstViewDict, secondViewDict, nil]];

    // Set some additional attributes for the animation.
    [theAnim setDuration:1.5];    // One and a half seconds.
    [theAnim setAnimationCurve:NSAnimationEaseIn];

    // Run the animation.
    [theAnim startAnimation];

    // The animation has finished, so go ahead and release it.
    [theAnim release];
}
```

[Next](Document%20Revision%20History.md)[Previous](Using%20an%20NSAnimation%20Object.md)

