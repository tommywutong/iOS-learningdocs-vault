---
title: Standard Sound Dialog Component
apple_id: TP40000950
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-09-17'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/RM/MusicAndAudio/StdSoundComp/rmStdSoundComp/rmStdSoundComp.html
archived_at: '2026-07-18T02:05:04.285514Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)



# Standard Sound Dialog Component

The standard sound dialog component presents a dialog box that lets the user make audio setting selections, such as the audio compression type, sampling rate, mono or stereo, etc. Your application uses this component to present the dialog box to the user, and to read the user selections back into your application.

The standard sound dialog component is based on the standard image compression dialog component and uses some of the same function calls. You should be familiar with the image compression dialog component before reading this chapter. You should read this chapter if your application allows audio recording, resampling, or compression, or if you plan to develop a new sound dialog component.

[Inside Macintosh: QuickTime Reference](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refStdSoundComp.4.htm) describes what the standard sound dialog component does and includes an illustration of the standard dialog box.

[Inside Macintosh: QuickTime Reference](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refStdSoundComp.5.htm) describes how to use the standard sound dialog component from within an application. Sample code is included for several functions.

- [Opening a connection to the standard sound dialog component](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refStdSoundComp.5.htm)
- [Setting initial values for the dialog box](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refStdSoundComp.5.htm)
- [Restricting the list of compression types](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refStdSoundComp.5.htm)
- [Displaying the dialog box](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refStdSoundComp.5.htm)
- [Retrieving settings from the dialog box](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refStdSoundComp.5.htm)

[Inside Macintosh: QuickTime Reference](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refStdSoundComp.8.htm) describes three functions, taken from the standard image compression dialog component, which are implemented in the standard sound dialog component: SCGetInfo , SCSetInfo , and SCRequestImageSettings . Refer to the chapter "Standard Image Compression Dialog" for the complete function definitions. Also described are two new functions, SCGetSettingsAsAtomContainer and SCSetSettingsFromAtomContainer .

- `SCGetInfo`
- `SCSetInfo`
- `SCRequestImageSettings`
- `SCGetSettingsAsAtomContainer`
- `SCSetSettingsFromAtomContainer`

[Inside Macintosh: QuickTime Reference](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refStdSoundComp.7.htm) defines the constants used by the sound dialog component. These are primarily new selectors that can be passed to SCGetInfo or SCSetInfo , and are supported only when these functions are called with the standard sound dialog component. These selectors are not supported when calling SCGetInfo or SCSetInfo for a standard image compression dialog.

- scSoundSampleRateType
- scSoundSampleSizeType
- scSoundChannelCountType
- scSoundCompressionType
- scCompressionListType
- scPreferenceFlagsType
- scExtendedProcsType
- scSettingsStateType

