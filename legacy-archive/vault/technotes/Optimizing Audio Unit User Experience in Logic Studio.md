---
title: Optimizing Audio Unit User Experience in Logic Studio
apple_id: DTS40008753
resource_type: Technical Note
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2009-09-30'
source_url: https://developer.apple.com/library/archive/technotes/tn2207/_index.html
archived_at: '2026-07-26T19:54:09.610190Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2207

# Optimizing Audio Unit User Experience in Logic Studio

Logic Studio is a powerful application suite which handles key aspects of music production ranging from composing, arranging, mixing, post production, and even on-stage performance. This document highlights a few key features of the audio unit standard that developers should pay particular attention on to ensure best user experience for their products across the entire palette of audio unit host applications in Logic Studio: Logic Pro 8, Soundtrack Pro 2, MainStage and WaveBurner.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzvgmwugsbrfvjukq2ujfhu4mi)[Using auval](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzvgmwugsbrfvjukq2ujfhu4mq)[Property Caching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzvgmwugsbrfvjukq2ujfhu4my)[Audio Unit Views](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzvgmwugsbrfvjukq2ujfhu4na)[Surround Sound](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzvgmwugsbrfvjukq2ujfhu4ni)[External Control Surfaces](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzvgmwugsbrfvjukq2ujfhu4nq)[Logic Studio's Audio Unit Property Reference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzvgmwugsbrfvjukq2ujfhu4ny)[Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzvgmwugsbrfvjukq2ujfhu4oa)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzvgmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

While code and behavior are widely shared among the applications in Logic Studio, each still specializes in certain tasks and therefore naturally provides a slightly different context in which your audio unit will live. This may make it worthwhile to thoroughly test your plug-ins across the various applications to ensure proper operation. Before turning to the Logic Studio applications though, we recommend to test your audio unit with AU Lab. Designed as the reference host for audio unit development, its Leopard version supports the majority of audio unit features described in this document.

[Back to Top](#)

## Using auval

To ensure proper operation of each audio unit on a particular user system, the Logic Studio applications rely on the `auval` command line tool provided in Mac OS X, see [Technical Note TN2204, 'Audio Unit Validation Using the auval Tool'](https://developer.apple.com/technotes/tn2007/tn2204.html) for more information about this tool.

Each audio unit that is installed or updated will be validated and failures will be reported to the user.

Since Mac OS X 10.4, `auval` supports the `kAudioUnitErr_Unauthorized` error. When you develop a copy-protected audio unit, you use this error to distinguish an authorization failure from a validation error. The caller can then display an appropriate error message and allow for a validation retry after authorizing this copy of the plug-in.

[Back to Top](#)

## Property Caching

Logic, Soundtrack Pro 2, MainStage, and WaveBurner cache certain information about the audio unit plug-ins installed in the system to speed up the launch process. This includes:

- name, version, and ID triplet of the AU
- status of validation with `auval`
- I/O configuration capability information including `kAudioUnitProperty_SupportedNumChannels`, writability of `kAudioUnitProperty_ElementCount`, and default count & configuration of the elements, `kAudioUnitProperty_SupportedChannelLayoutTags`
- The value of the `kAudioUnitMigrateProperty_FromPlugin` property
- number of Carbon and Cocoa views (as determined by the size of the `kAudioUnitProperty_GetUIComponentList` and `kAudioUnitProperty_CocoaUI` properties)

If you are modifying code without increasing the version number of your audio unit, you'll need to rescan the audio unit manually in the Audio Unit Manager to make the applications recognize the changes. Alternatively, you can set an audio unit's version number to zero to force an automatic rescan at every application launch. You can use this technique while developing an audio unit, but must set an appropriate version number in the deployment build.

[Back to Top](#)

## Audio Unit Views

All four audio unit host applications in Logic Studio use Cocoa to implement their interface. This means that custom Audio Unit Views implemented in Cocoa are directly embedded in the host window, whereas custom Audio Unit Views implemented in Carbon are displayed using frameless overlay windows similar to the technique described in [Technical Note TN2213, 'Audio Units: Embedding a Carbon View in a Cocoa Window'](https://developer.apple.com/technotes/tn2007/tn2213.html).

Directly embedded views provide better user experience through better UI integration. Therefore, Cocoa is the recommended technology.

For even better user interface integration, custom Audio Unit Views should refrain from using overlay windows and from opening sheets or auxiliary windows other than for file browsing. All user interface elements should be presented inside the root Audio Unit View by laying out its content dynamically and resizing as necessary. The host window listens to size change notifications and will adapt automatically.

[Back to Top](#)

## Surround Sound

Logic Studio provides dedicated support for surround sound. If the audio processing implemented by your audio unit lends itself towards a surround-specific implementation, you should be looking into providing it in the future to enhance overall user experience.

If your audio processing doesn't use spatialization information or if it handles all channels independently, we recommend that you:

1. Support any channel count, provided that the channel count is the same for input and output
2. Do not support the channel layout (`kAudioUnitProperty_AudioChannelLayout`) property, because the audio unit does not do any semantic processing based on channel definition

[Back to Top](#)

## External Control Surfaces

Logic and MainStage feature support for external control surfaces such as the Mackie Universal Pro and Euphonix MC Control/Mix and so on.

__Note:__ While Soundtrack Pro 2 also supports control surfaces for mixing, you cannot currently edit effect parameters with a control surface.

MainStage allows for designing user-specific views for plug-ins with a limited number of parameters for easy access on stage. Both features depend on the parameters being exposed to the host via the `kAudioUnitProperty_ParameterList` property, so you should decide carefully which parameters to export.

When describing your exported parameters via `kAudioUnitProperty_ParameterInfo`, utilize the flags field of the `AudioUnitParameterInfo` struct to provide additional information about your parameters, such as `kAudioUnitParameterFlag_NonRealTime` to prevent a parameter from being automated, or `kAudioUnitParameterFlag_ExpertMode` to distinguish between the more important parameters and those that allow fora mere fine-tuning by advanced user. Also use `kAudioUnitParameterFlag_HasClump` together with `kAudioUnitProperty_ParameterClumpName` to group your parameters into meaningful sections.

Another important issue here is to make sure that if a parameter sets `kAudioUnitParameterFlag_ValuesHaveStrings`, not only should you support `kAudioUnitProperty_ParameterStringFromValue` (formerly known as `kAudioUnitProperty_ParameterValueName`) for that parameter, but also implement the reverse transformation via `kAudioUnitProperty_ParameterValueFromString` to allow the host application to translate user-entered text into a parameter value.

Many audio units still struggle to send proper notification whenever a parameter is changed due to user interaction in its custom UI. Please refer to [Technical Note TN2104, 'Audio Unit Development - Handling Audio Unit Events'](https://developer.apple.com/technotes/tn2002/tn2104.html) to learn when and how the change notifications shall be posted according to the AU specifications.

Failure to send proper notifications will cause the automation system to not work properly (particularly when using touch mode to edit existing automation), and it can also break the settings compare button in Logic which allows to compare a modified setting against its original state.

[Back to Top](#)

## Logic Studio's Audio Unit Property Reference

For your reference, here's a list of all properties used by the Logic Studio applications. Please check that you are supporting these properties as appropriate for your product.

- I/O configuration

  ```
  kAudioUnitProperty_SupportedNumChannels kAudioUnitProperty_ElementCount kAudioUnitProperty_StreamFormat kAudioUnitProperty_SupportedChannelLayoutTags kAudioUnitProperty_AudioChannelLayout
  ```
- Rendering

  ```
  kAudioUnitProperty_MaximumFramesPerSlice kAudioUnitProperty_InPlaceProcessing kAudioUnitProperty_OfflineRender kAudioUnitProperty_SetRenderCallback kAudioUnitProperty_HostCallbacks kAudioUnitProperty_Latency kAudioUnitProperty_TailTime
  ```
- Persistence

  ```
  kAudioUnitProperty_FactoryPresets kAudioUnitProperty_PresentPreset kAudioUnitProperty_ClassInfo
  ```
- Parameters

  ```
  kAudioUnitProperty_ParameterList kAudioUnitProperty_ParameterInfo kAudioUnitProperty_ParameterValueStrings kAudioUnitProperty_ParameterClumpName kAudioUnitProperty_ParameterStringFromValue kAudioUnitProperty_ParameterValueFromString
  ```
- User Interface

  ```
  kAudioUnitProperty_GetUIComponentList kAudioUnitProperty_CocoaUI
  ```
- Plug-in Migration (song import from Windows/OS 9 VST)

  ```
  kAudioUnitMigrateProperty_FromPlugin kAudioUnitMigrateProperty_OldAutomation
  ```
- New in Mac OS X 10.5

  ```
  kAudioUnitProperty_AUHostIdentifier kAudioUnitProperty_ClassInfoFromDocument kMusicDeviceProperty_DualSchedulingMode
  ```

[Back to Top](#)

## Resources

- [Audio Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000428)
- [Audio Unit Programming Guide](../documentation/Music%20Audio/Audio%20Unit%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenzyfvbuqmi)
- `LogicAUProperties.h` located in the AudioUnit Framework <AudioUnit/LogicAUProperties.h>
- [CoreAudio Mailing List](http://lists.apple.com/mailman/listinfo/coreaudio-api) - Audio Unit development and Core Audio related issues.
- Logic AudioUnit host support (__logic-au@group.apple.com__) - for questions related to Logic as the AudioUnit host.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-09-30 | Updated Audio Unit Views discussion |
| 2009-04-23 | New document that how to provide the best user experience with your audio unit in Logic Studio |

