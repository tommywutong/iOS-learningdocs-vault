---
title: Quick Look for Custom Types in the Xcode Debugger
apple_id: TP40014001
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/IDEs/Conceptual/CustomClassDisplay_in_QuickLook/CH01-quick_look_for_custom_objects/CH01-quick_look_for_custom_objects.html
archived_at: '2026-07-15T07:41:16.459013Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quick Look for Custom Types in the Xcode Debugger](About%20Variables%20Quick%20Look%20for%20Custom%20Types.md)


[Next](Operating%20System%20Types%20Supporting%20debugQuickLookObject.md)[Previous](About%20Variables%20Quick%20Look%20for%20Custom%20Types.md)

# Enabling Quick Look for Custom Types

The variables Quick Look feature in the Xcode debugger allows you to obtain a quick visual assessment of the state of an object variable through a graphical rendering, displayed in a popover window either in the debugger variables view or in place in your source code. For supported operating system types, Quick Look displays debugger Quick Look object primitives to service this visualization.

This chapter describes how you implement a Quick Look method for your custom class types so that object variables of those types can also be rendered visually in the Quick Look popover window.

For your custom class type, implement a method named `debugQuickLookObject`.

```objc
- (id)debugQuickLookObject
{
    // allocate the return object for the data you wish to represent
    //   Note: "NSImage" is used here arbitrarily for illustration purposes.
    NSImage *_quickLookImage = [...]

    // code that draws a representation of the variable state
    // ...

    // return the object
    return _quickLookImage;
}
```

A set of the most common operating system types useful for rendering visualizations are able to output debugger Quick Look object primitives which Xcode uses for the Quick Look display. Your `debugQuickLookObject` method must return an object of one of these types. See [Operating System Types Supporting debugQuickLookObject](Operating%20System%20Types%20Supporting%20debugQuickLookObject.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dambrfvbuqmznknltc) for a table of operating system types and examples of their standard Quick Look displays so that you can choose the most appropriate one to render your custom type.

When you select a variable of the custom class type in the Xcode debugger variables view and use Quick Look, the `debugQuickLookObject` method defined for the class is called. The Quick Look popover display presents the returned object.

Because your `debugQuickLookObject` method runs in the debugger, when you are inside your paused application, it is best to be economical in your method implementation. Write as little code as needed to represent your variable’s state as a useful visual graphic. Remember that running code when in a paused application can have side effects. If possible, cache the item you want to return.

The following `debugQuickLookObject` method demonstrates a trivially defined custom type named `MyCustomClass` used with Quick Look in the debugger. The object type is declared as:

```objc
#import <Foundation/Foundation.h>
@interface MyCustomClass : NSObject
@end
```

The `debugQuickLookObject` method in `MyCustomClass.m` draws a graphic for Quick Look to display and returns it in an `NSImage` object.

```objc
- (id)debugQuickLookObject
{
    // Note that for simplicity in presentation, this sample allocates and returns an NSImage object.
    // Using a cached object instead is preferred; it minimizes potential impact on the paused app context.
    NSImage *image = [NSImage imageWithSize:QUICK_LOOK_IMAGE_SIZE flipped:NO drawingHandler:^BOOL(NSRect dstRect) {

        CGFloat midX = NSMidX(dstRect);
        CGFloat midY = NSMidY(dstRect);
        NSUInteger numCircles = 5;
        CGFloat circleSpacing = -10.0;
        CGFloat circleRadius = 20.0;
        CGFloat circleDiameter = circleRadius * 2;
        CGFloat stride = circleDiameter + circleSpacing;
        CGFloat currentCircleX = midX - (stride * numCircles)/2.0;

        NSColor *strokeColor = [NSColor colorWithCalibratedRed:0.10 green:0.41 blue:1.0 alpha:1.0];
        NSColor *fillColor = [strokeColor colorWithAlphaComponent:0.15];

        for (NSUInteger i=0; i < numCircles; i++) {
            NSRect circleRect = NSMakeRect(currentCircleX, midY - circleRadius, circleDiameter, circleDiameter);
            NSBezierPath *circlePath = [NSBezierPath bezierPathWithOvalInRect:circleRect];
            [fillColor set];
            [circlePath fill];
            [strokeColor set];
            [circlePath stroke];
            currentCircleX += stride;
        }
        return YES;
    }];
    return image;
}
```

To see the `debugQuickLook` method work in the Xcode debugger, add the`MyCustomClass.h` interface and `MyCustomClass.m` implementation files to a simple app created from a template. Inser the following code into the `AppDelegate.m` file. A breakpoint set at the `NSLog()` call allows you to Quick Look the returned `myObject` custom class variable.

```objc
- (void)applicationDidFinishLaunching:(NSNotification *)aNotification
{
    MyCustomClass *myObject = [self _createMyCustomObject];
    NSLog(@"created object"); // set breakpoint here, and Quick Look myObject
}

- (MyCustomClass *) _createMyCustomObject
{
    MyCustomClass *customObject = [[MyCustomClass alloc] init];
    return customObject;
}
```

The resulting Quick Look display is shown in Figure 1-1.

__Figure 1-1__  Quick Look displaying custom type

!

[Next](Operating%20System%20Types%20Supporting%20debugQuickLookObject.md)[Previous](About%20Variables%20Quick%20Look%20for%20Custom%20Types.md)

