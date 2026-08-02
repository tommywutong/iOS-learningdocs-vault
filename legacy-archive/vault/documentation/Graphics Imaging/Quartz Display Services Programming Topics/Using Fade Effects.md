---
title: Quartz Display Services Programming Topics
apple_id: TP40004316
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzDisplayServicesConceptual/Articles/FadeEffects.html
archived_at: '2026-07-15T07:38:03.624706Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quartz Display Services Programming Topics](Introduction%20to%20Quartz%20Display%20Services%20Programming%20Topics.md)


[Next](Notification%20of%20Configuration%20Changes.md)[Previous](Configuring%20Displays%20Using%20a%20Transaction.md)

# Using Fade Effects

A display fade effect is a smooth transition to or from a monochromatic color blended with the contents of the display, often used when entering full screen mode or switching display modes. The transitions to and from monochromatic color are sometimes called fade-out and fade-in effects.

Quartz automatically fades all online displays for you during configuration changes. The time settings for the default fade effect are 0.3 seconds to fade out and 0.5 seconds to fade in. The fade color is French Blue for a normal desktop, and black for a captured display. During a configuration transaction, you can customize this built-in fade effect—see the example in [Configuring Displays Using a Transaction](Configuring%20Displays%20Using%20a%20Transaction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2demzqfvjvomi).

You may want to use a custom fade effect to indicate a transition other than a configuration change. For example, you could fade out to black, capture the display, draw on the screen, and fade in from black. The next sections show two ways to accomplish this task.

Quartz Display Services provides functions that allow you to perform a custom fade effect on all online displays simultaneously. The first step is to call [CGAcquireDisplayFadeReservation](https://developer.apple.com/documentation/coregraphics/1456391-cgacquiredisplayfadereservation) to reserve the fade engine for a specified interval. This function passes back a token that represents a new fade reservation. Your application uses this token as an argument in subsequent calls to [CGDisplayFade](https://developer.apple.com/documentation/coregraphics/1456189-cgdisplayfade). During the fade reservation interval, your application has exclusive rights to use the fade engine. To release the reservation, you call [CGReleaseDisplayFadeReservation](https://developer.apple.com/documentation/coregraphics/1455230-cgreleasedisplayfadereservation).

Listing 1 shows how to reserve the fade engine, perform a fade effect to and from black, and release the reservation. A detailed explanation for each numbered line of code appears following the listing.

__Listing 1__  Fading all displays

```
CGDisplayFadeReservationToken token;
CGError err;

err = CGAcquireDisplayFadeReservation (kCGMaxDisplayReservationInterval, &token); // 1
if (err == kCGErrorSuccess)
{
    err = CGDisplayFade (token, 0.3, kCGDisplayBlendNormal,
        kCGDisplayBlendSolidColor, 0, 0, 0, true); // 2
    err = CGDisplayCapture (kCGDirectMainDisplay); // 3
    /* draw something on the captured display */
    err = CGDisplayFade (token, 0.5, kCGDisplayBlendSolidColor,
        kCGDisplayBlendNormal, 0, 0, 0, true); // 4
    err = CGReleaseDisplayFadeReservation (token); // 5
}
```

Here’s what the code does:

1. Reserves the fade engine for the maximum permitted interval. Your application must perform this step before it can fade the displays. During this time, your application has exclusive rights to use the fade engine.
2. Fades displays to black with a duration of 0.3 seconds. The function call is synchronous.
3. Captures the main display. The display is already black, so the user sees no change.
4. Fades displays from black to normal with a duration of 0.5 seconds. The function call is synchronous.
5. Releases the fade reservation and invalidates the token.

To fade a single display on a system with two or more displays, you can use another approach that involves incrementally adjusting the display’s gamma formula.

When you adjust the gamma values, you can’t assume that the maximum gamma value is 1.0; the user might have specified a different maximum value in System Preferences. You need to retrieve the current settings and scale them appropriately.

Listing 2 shows how to fade a specified display to black and back. A loop with a fixed delay is used to obtain a smooth fade (another approach is to use a timer to ensure a fixed fade duration on different systems).

__Listing 2__  Fading a single display

```
const double kMyFadeTime = 1.0; /* fade time in seconds */
const int kMyFadeSteps = 100;
const double kMyFadeInterval = (kMyFadeTime / (double) kMyFadeSteps);
const useconds_t kMySleepTime = (1000000 * kMyFadeInterval); /* delay in microseconds */

int step;
double fade;
CGGammaValue redMin, redMax, redGamma,
             greenMin, greenMax, greenGamma,
             blueMin, blueMax, blueGamma;
CGError err;

err = CGGetDisplayTransferByFormula (display, // 1
    &redMin, &redMax, &redGamma,
    &greenMin, &greenMax, &greenGamma,
    &blueMin, &blueMax, &blueGamma);

for (step = 0; step < kMyFadeSteps; ++step) { // 2
    fade = 1.0 - (step / (double)kMyFadeSteps);
    err = CGSetDisplayTransferByFormula (display,
        redMin, fade*redMax, redGamma,
        greenMin, fade*greenMax, greenGamma,
        blueMin, fade*blueMax, blueGamma);
    usleep (kMySleepTime); // 3
}

err = CGDisplayCapture (display);
/* draw something on the captured display */

for (step = 0; step < kMyFadeSteps; ++step) { // 4
    fade = (step / (double)kMyFadeSteps);
    err = CGSetDisplayTransferByFormula (display,
        redMin, fade*redMax, redGamma,
        greenMin, fade*greenMax, greenGamma,
        blueMin, fade*blueMax, blueGamma);
    usleep (kMySleepTime); // 5
}

CGDisplayRestoreColorSyncSettings();  // 6
```

Here’s what the code does:

1. Gets the current coefficients of the gamma transfer formula for a display as the starting gamma values.
2. Fades from the current gamma by setting the color gamma function for the display, specified as the coefficients of the gamma transfer formula. Starts with the current gamma (multiplying by a factor of 1.0) and ends with black (multiplying by a factor of 0.0).
3. Suspends processing for a short interval. To get a smooth fade out effect, you need to either use a timer or insert a short delay because the call to change the display gamma returns within 100 microseconds or so, and the actual gamma is applied asynchronously during the next vertical blanking period. Without the delay, you’ll get what appears as an instantaneous switch to black.
4. Fades from black (multiplying by a factor of 0.0) back to original gamma (multiplying by a factor of 1.0).
5. Suspends processing for a short interval to achieve a smooth fade in effect.
6. Restores the gamma tables to the values in the user’s ColorSync display profile.

[Next](Notification%20of%20Configuration%20Changes.md)[Previous](Configuring%20Displays%20Using%20a%20Transaction.md)

