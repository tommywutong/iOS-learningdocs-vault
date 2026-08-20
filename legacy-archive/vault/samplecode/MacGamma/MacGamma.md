---
title: MacGamma
apple_id: DTS10000087
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/MacGamma/Introduction/Intro.html
archived_at: '2026-07-18T03:14:08.539813Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](MacGamma.cpp.md)

# MacGamma

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-07-22 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

MacGamma is code that one can drop into their application which provides easy access to gamma control for all system displays. It provides safe saving and restoring of original system gamma so one does not upset users and/or other applications. The code is based on a simple 3 channel, 256 entry, 8 bit gamma ramp. This ramp is basically an array of 256 byte size element red, green and blue channels. All routines provided use this structure to pass information to and from the systems displays, this was chosen to simplify application usage. Some displays may represent gamma data differently, gamma ramps are internally converted internally to what ever format the monitor requires. A few usage notes for the source: SetDeviceGammaRampXX may not return until the VBL following the call, depending on the display driver, this is due to the handling of the Control call by the driver. Startup and Shutdown: GetSystemGammas (...) must be called to save the system gammas prior to using MacGamma. RestoreSystemGamms (...) must be called before exiting to restore original gamma. DisposeSystemGammas (...) can then be used to dispose of the system gammas. Suspend and Resume: RestoreSystemGamms (...); DisposeSystemGammas (...); should also be called prior to suspend. GetSystemGammas (...) should be called when resuming. This architecture prevents users from unknowingly saving display settings with your modified gammas. MacGamma requires the Color QuickDraw.

[Next](MacGamma.cpp.md)

