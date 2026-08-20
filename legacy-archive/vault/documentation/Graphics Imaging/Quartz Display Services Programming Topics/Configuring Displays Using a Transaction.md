---
title: Quartz Display Services Programming Topics
apple_id: TP40004316
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzDisplayServicesConceptual/Articles/DisplayTransactions.html
archived_at: '2026-07-15T07:38:03.610922Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quartz Display Services Programming Topics](Introduction%20to%20Quartz%20Display%20Services%20Programming%20Topics.md)


[Next](Using%20Fade%20Effects.md)[Previous](Changing%20Display%20Modes%20%28OS%20X%20v10.5%29.md)

# Configuring Displays Using a Transaction

Quartz Display Services makes it possible to configure a set of displays in a single transaction. During the execution of configuration changes, Quartz performs a standard fade effect on all online displays. The displays fade to a monochromatic color, the configuration takes place, and the displays return to normal. For more information about fade effects, see [Using Fade Effects](Using%20Fade%20Effects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2demzsfvjvomi).

You begin a new transaction by calling [CGBeginDisplayConfiguration](https://developer.apple.com/documentation/coregraphics/1455235-cgbegindisplayconfiguration). The next step is to declare what changes you want to make. For example, you can use these functions:

- [CGConfigureDisplayWithDisplayMode](https://developer.apple.com/documentation/coregraphics/1454273-cgconfiguredisplaywithdisplaymod) sets the display mode of a display. (In OS X v10.5 use [CGConfigureDisplayMode](https://developer.apple.com/documentation/coregraphics/1543535-cgconfiguredisplaymode) instead.)
- [CGConfigureDisplayMirrorOfDisplay](https://developer.apple.com/documentation/coregraphics/1454531-cgconfiguredisplaymirrorofdispla) adds a display to a mirroring set.
- [CGConfigureDisplayOrigin](https://developer.apple.com/documentation/coregraphics/1454090-cgconfiguredisplayorigin) sets a display’s origin in global display space.
- [CGConfigureDisplayFadeEffect](https://developer.apple.com/documentation/coregraphics/1454103-cgconfiguredisplayfadeeffect) customizes the fade effect. (Calling this function modifies the fade behavior for a single display configuration and has no permanent effect.)

After you’re finished preparing the transaction, you call [CGCompleteDisplayConfiguration](https://developer.apple.com/documentation/coregraphics/1454488-cgcompletedisplayconfiguration) to execute it. In this call you also specify the scope of the configuration change. Typically, you specify [kCGConfigureForAppOnly](https://developer.apple.com/documentation/coregraphics/cgconfigureoption/1454446-forapponly) to apply the changes for the lifetime of your application.

Listing 1 shows how to use a configuration transaction with a custom fade effect to change the display mode of a single display for OS X v10.6 and later. For OS X v10.5 or earlier, see Listing 2 instead. A detailed explanation for each numbered line of code appears following the listings.

__Listing 1__  A simple configuration transaction (OS X v10.6 or later)

```
void MyDisplaySwitchToMode (CGDirectDisplayID display, CGDisplayModeRef mode)
{
    CGDisplayConfigRef config; // 1
    CGBeginDisplayConfiguration (&config); // 2
    CGConfigureDisplayWithDisplayMode (config, display, mode, NULL); // 3

    CGConfigureDisplayFadeEffect ( // 4
        config,
        0.6,    // fade out interval in seconds
        1.0,    // fade in interval
        0.5,    // red
        0.5,    // green
        0.5     // blue
    );

    CGCompleteDisplayConfiguration (config, kCGConfigureForAppOnly); // 5
}
```


__Listing 2__  A simple configuration transaction (OS X v 10.5)

```
void MyDisplaySwitchToMode (CGDirectDisplayID display, CFDictionaryRef mode)
{
    CGDisplayConfigRef config; // 1
    CGBeginDisplayConfiguration (&config); // 2
    CGConfigureDisplayMode (config, display, mode); // 3

    CGConfigureDisplayFadeEffect ( // 4
        config,
        0.6,    // fade out interval in seconds
        1.0,    // fade in interval
        0.5,    // red
        0.5,    // green
        0.5     // blue
    );

    CGCompleteDisplayConfiguration (config, kCGConfigureForAppOnly); // 5
}
```

Here’s what the code does:

1. Declares a display configuration object, a variable that provides a context for a set of display configuration changes.
2. Begins a new configuration transaction and passes back a display configuration object.
3. Declares the display mode change for this configuration.
4. Customizes the default fade effect for this configuration. The new fade color is gray.
5. Applies the new configuration with application scope. On return, the configuration object is no longer valid.

[Next](Using%20Fade%20Effects.md)[Previous](Changing%20Display%20Modes%20%28OS%20X%20v10.5%29.md)

