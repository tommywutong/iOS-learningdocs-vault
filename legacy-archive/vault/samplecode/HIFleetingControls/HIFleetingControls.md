---
title: HIFleetingControls
apple_id: DTS10004280
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2007-05-08'
source_url: https://developer.apple.com/library/archive/samplecode/HIFleetingControls/Introduction/Intro.html
archived_at: '2026-07-18T03:11:26.614810Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# HIFleetingControls

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2007-05-08 Implements fleeting controls such as seen in QuickTime Player full screen mode or iPhoto slideshow |
| __Build Requirements:__ | Xcode 2.3 |
| __Runtime Requirements:__ | Mac OS X 10.2 |

This sample demonstrates how to implement fleeting controls such as seen in QuickTime Player in full screen mode or in iPhoto in slide show mode when you move the mouse.
How it Works
------------
First, a hot zone is associated with the fleeting controls view. This zone is where the mouse cursor has to be in for the fleeting controls to appear. This is done with the function HIFleetingControlsViewSetHotZone.
Second, when the mouse cursor enters the hot zone (kEventControlTrackingAreaEntered), an idle timer is installed to detect the user's inactivity.
Third, when the idle timer fires, checks are done to determine if the mouse cursor is on top of the fleeting controls themselves, and if those controls are already fading or not, see the function ShouldFadeTimer. If it is determined that the controls should fade then another timer is installed to make the fleeting controls fade into nothingness.
This fading is achieved by decrementing an alpha counter belonging to the fleeting controls view. All embedded views (the actual controls, in the sample code a HIVeryBasicView) have to obtain this alpha value before drawing through the function HIFleetingControlViewGetAlphaIfEmbedded and use this value as a multiplicator for all their colored parts.
The code was built and tested on Mac OS X 10.4.9 (PowerPC and Intel). The code code should work back to Mac OS X 10.2.

[Next](main.c.md)

