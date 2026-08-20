---
title: Progress Indicator Programming Topics
apple_id: 10000024i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2002-11-12'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgIndic/Tasks/IndeterProgIndic.html
archived_at: '2026-07-15T07:17:51.040193Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Progress Indicator Programming Topics](Introduction%20to%20Progress%20Indicators.md)


[Next](Document%20Revision%20History.md)[Previous](Using%20Determinate%20Progress%20Indicators.md)

# Using Indeterminate Progress Indicators

For an indeterminate progress indicator, invoke `startAnimation:` to start the animation (the spinning of the barber pole) and `stopAnimation:` when the task is complete. By default, the delay between animation steps is one twelfth of a second (5/60). You can change the animation delay by invoking `setAnimationDelay:`. Setting the delay to a double value larger than the default value will slow the animation, while setting the delay to a smaller value will speed it up.

Instead of invoking `startAnimation:` and `stopAnimation:`, you can control an indeterminate progress indicator directly by sending the `animate:` message. Each time you invoke `animate:`, the animation advances by one step. You can speed up or slow down the animation by varying how often you invoke `animate:`. Like other views, a progress indicator redisplays itself on each pass through the event loop, if needed. To ensure immediate redrawing, however, you can invoke the `displayIfNeeded` method (inherited from NSView) each time you invoke `animate:`.

If your application is threaded, you may want the progress indicator’s animation to happen in a separate thread by calling `setUsesThreadedAnimation:`. If your application doesn’t already use threads, creating a thread just for the progress indicator can actually slow down your application.

By default, a progress indicator is indeterminate.

[Next](Document%20Revision%20History.md)[Previous](Using%20Determinate%20Progress%20Indicators.md)

