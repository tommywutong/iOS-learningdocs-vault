---
title: FxPlug SDK Overview
apple_id: TP40002180
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/FXPlug_overview/APIOverview/APIOverview.html
archived_at: '2026-07-15T05:17:47.059075Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [FxPlug SDK Overview](About%20the%20FxPlug%20SDK.md)


[Next](Working%20with%20Entitlements.md)[Previous](What%E2%80%99s%20New%20in%20FxPlug%203.1.1.md)

# FxPlug Concepts and API

An FxPlug plug-in is an application bundle that interacts with a host application to extend its functionality.

When a plug-in needs to access host application functionality—such as requesting video stream information—it uses methods in a host API. A host API is an object, provided by the host application, that implements methods that can be called by a plug-in. It’s analogous to a callback suite in other plug-in architectures, but is implemented as an Objective-C protocol.

For example, the FxPlug SDK defines host protocols that include methods for requesting layer information, converting between canvas and object coordinate spaces, building a list of plug-in parameters, getting and setting parameter values, and evaluating input images at arbitrary times. Not all hosts are guaranteed to support all host-API protocols specified in FxPlug, so a plug-in must request the host API object before invoking its methods.

The principal frameworks in the FxPlug SDK are `FxPlug.framework` and `PlugInManager.framework`. These frameworks are located at `/Library/Developer/Frameworks/`.

The primary protocols defined by the FxPlug SDK are [FxFilter](https://developer.apple.com/documentation/fxplug/fxfilter), [FxGenerator](https://developer.apple.com/documentation/fxplug/fxgenerator), and [FxOnScreenControl](https://developer.apple.com/documentation/fxplug/fxonscreencontrol). All FxPlug plug-ins must conform to one of these protocols.

The FxPlug SDK is made up of a number of protocols and classes. Some of these protocols are implemented by the host application and allow your plug-in access to functionality within that application. Other protocols are expected to be implemented by the application that contains your plug-in to allow the host application to communicate with your plug-in.

The following are the host-defined protocols:

- [Fx3DAPI_v3](https://developer.apple.com/documentation/fxplug/fx3dapi_v3)
- [FxAppearanceAPI](https://developer.apple.com/documentation/fxplug/fxappearanceapi)
- [FxColorGamutAPI](https://developer.apple.com/documentation/fxplug/fxcolorgamutapi)
- [FxCustomParameterActionAPI](https://developer.apple.com/documentation/fxplug/fxcustomparameteractionapi)
- [FxCustomParameterActionAPI_v2](https://developer.apple.com/documentation/fxplug/fxcustomparameteractionapi_v2)
- [FxCustomParameterActionAPI_v3](https://developer.apple.com/documentation/fxplug/fxcustomparameteractionapi_v3)
- [FxDynamicParameterAPI](https://developer.apple.com/documentation/fxplug/fxdynamicparameterapi)
- [FxHostResourcesAPI](https://developer.apple.com/documentation/fxplug/fxhostresourcesapi)
- [FxKeyframeAPI](https://developer.apple.com/documentation/fxplug/fxkeyframeapi)
- [FxKeyframeAPI_v2](https://developer.apple.com/documentation/fxplug/fxkeyframeapi_v2)
- [FxLightingAPI](https://developer.apple.com/documentation/fxplug/fxlightingapi)
- [FxLightingAPI_v2](https://developer.apple.com/documentation/fxplug/fxlightingapi_v2)
- [FxOnScreenControlAPI](https://developer.apple.com/documentation/fxplug/fxonscreencontrolapi)
- [FxOnScreenControlAPI_v2](https://developer.apple.com/documentation/fxplug/fxonscreencontrolapi_v2)
- [FxOnScreenControlAPI_v3](https://developer.apple.com/documentation/fxplug/fxonscreencontrolapi_v3)
- [FxOptionalParameterCreationAPI](https://developer.apple.com/documentation/fxplug/fxoptionalparametercreationapi)
- [FxOptionalParameterRetrievalAPI](https://developer.apple.com/documentation/fxplug/fxoptionalparameterretrievalapi)
- [FxOptionalParameterRetrievalAPI_v2](https://developer.apple.com/documentation/fxplug/fxoptionalparameterretrievalapi_v2)
- [FxOptionalParameterSettingAPI](https://developer.apple.com/documentation/fxplug/fxoptionalparametersettingapi)
- [FxParameterCreationAPI](https://developer.apple.com/documentation/fxplug/fxparametercreationapi)
- [FxParameterCreationAPI_v2](https://developer.apple.com/documentation/fxplug/fxparametercreationapi_v2)
- [FxParameterCreationAPI_v3](https://developer.apple.com/documentation/fxplug/fxparametercreationapi_v3)
- [FxParameterCreationAPI_v4](https://developer.apple.com/documentation/fxplug/fxparametercreationapi_v4)
- [FxParameterRetrievalAPI](https://developer.apple.com/documentation/fxplug/fxparameterretrievalapi)
- [FxParameterRetrievalAPI_v2](https://developer.apple.com/documentation/fxplug/fxparameterretrievalapi_v2)
- [FxParameterRetrievalAPI_v3](https://developer.apple.com/documentation/fxplug/fxparameterretrievalapi_v3)
- [FxParameterRetrievalAPI_v4](https://developer.apple.com/documentation/fxplug/fxparameterretrievalapi_v4)
- [FxParameterRetrievalAPI_v5](https://developer.apple.com/documentation/fxplug/fxparameterretrievalapi_v5)
- [FxParameterSettingAPI](https://developer.apple.com/documentation/fxplug/fxparametersettingapi)
- [FxParameterSettingAPI_v2](https://developer.apple.com/documentation/fxplug/fxparametersettingapi_v2)
- [FxParameterSettingAPI_v3](https://developer.apple.com/documentation/fxplug/fxparametersettingapi_v3)
- [FxParameterSettingAPI_v4](https://developer.apple.com/documentation/fxplug/fxparametersettingapi_v4)
- [FxPathAPI](https://developer.apple.com/documentation/fxplug/fxpathapi)
- [FxPathAPI_v2](https://developer.apple.com/documentation/fxplug/fxpathapi_v2)
- [FxPrincipalAPI](https://developer.apple.com/documentation/fxplug/fxprincipalapi)
- [FxProgressAPI](https://developer.apple.com/documentation/fxplug/fxprogressapi)
- [FxRenderNotificationAPI](https://developer.apple.com/documentation/fxplug/fxrendernotificationapi)
- [FxTemporalImageAPI](https://developer.apple.com/documentation/fxplug/fxtemporalimageapi)
- [FxTemporalImageAPI_v2](https://developer.apple.com/documentation/fxplug/fxtemporalimageapi_v2)
- [FxTemporalTransitionImageAPI](https://developer.apple.com/documentation/fxplug/fxtemporaltransitionimageapi)
- [FxTimingAPI](https://developer.apple.com/documentation/fxplug/fxtimingapi)
- [FxTimingAPI_v2](https://developer.apple.com/documentation/fxplug/fxtimingapi_v2)
- [FxTimingAPI_v3](https://developer.apple.com/documentation/fxplug/fxtimingapi_v3)
- [FxUndoAPI](https://developer.apple.com/documentation/fxplug/fxundoapi)
- [FxVersioningAPI](https://developer.apple.com/documentation/fxplug/fxversioningapi)
- [FxWindowAPI](https://developer.apple.com/documentation/fxplug/fxwindowapi)

Of the following protocols that your FxPlug plug-in can implement, you must implement either the [FxFilter](https://developer.apple.com/documentation/fxplug/fxfilter) or [FxGenerator](https://developer.apple.com/documentation/fxplug/fxgenerator) protocol:

- [FxBaseEffect](https://developer.apple.com/documentation/fxplug/fxbaseeffect)
- [FxCustomParameterInterpolation](https://developer.apple.com/documentation/fxplug/fxcustomparameterinterpolation)
- [FxCustomParameterViewHost](https://developer.apple.com/documentation/fxplug/fxcustomparameterviewhost)
- [FxFilter](https://developer.apple.com/documentation/fxplug/fxfilter)
- [FxGenerator](https://developer.apple.com/documentation/fxplug/fxgenerator)
- [FxHostResourcesClient](https://developer.apple.com/documentation/fxplug/fxhostresourcesclient)
- [FxOnScreenControl](https://developer.apple.com/documentation/fxplug/fxonscreencontrol)
- [FxOnScreenControl_v2](https://developer.apple.com/documentation/fxplug/fxonscreencontrol_v2)
- [FxWindowHost](https://developer.apple.com/documentation/fxplug/fxwindowhost)

All colors are presented to the user in sRGB color space. The numerical values displayed in the inspector for color well parameters are the sRGB values for those colors. However, when a plug-in requests a color via one of the `-[FxParameterRetrievalAPI getRedValue:greenValue:blueValue:::]` methods, the values returned are in the processing space requested by the plug-in via the dictionary it returns from its `-properties` method.

In other words, if your plug-in sets the value of the `kFxPropertyKey_DesiredProcessingColorInfo` key to `kFxImageColorInfo_RGB_LINEAR`, the color wells return linear RGB colors. Likewise, if the value is set to `kFxImageColorInfo_RGB_GAMMA_VIDEO`, the color wells return gamma-correct (Rec. 709) RGB values.

The numerical values your plug-in receives are different from the values displayed to the user in the inspector, and this is by design.

The FxTime structure and scheduling APIs enable more accurate time representations and improve overall plug-in performance.

Previously, frames were represented using a double-precision floating point value. Now you use an `FxTime` data type:

```
typedef union {
    double  frame;
    CMTime* seconds;
} FxTime;
```

Notice that this new `FxTime` type is a union, which means time is represented as _either_ a double-precision frame number _or_ a pointer to a rational number of seconds. This maintains binary compatibility with existing plug-ins, because the size of a pointer and a double-precision frame number both happen to be 64 bits, they can fit in the same space, and it won’t change the size of any existing structures. This also allows currently shipping plug-ins to continue to use frame numbers to represent time.

The addition of the `FxTime` data type requires minor changes to any plug-ins built with the new SDK. This means you won’t be able to simply point to the new FxPlug framework and build your existing plug-ins. (However, plug-ins that are already shipping will run just fine.) If you decide to update or rebuild your plug-ins, you must change your code wherever you currently use a frame number (the `renderInfo.frame` field), and change it to use `renderInfo.time` (or in some cases `renderInfo.time.frame`). In most cases, if you have to make these changes, you should move away from using frame time and instead use rational time.

The new scheduling API methods allow host applications to schedule the media contained in image wells. The `-numberOfFramesToScheduleAtRenderTime` method asks the plug-in how many frames it needs scheduled from a given image parameter. The `-schedule` method asks the plug-in to return the frame times needed from the image parameter for the given render time.

These new scheduling APIs were added as optional methods to the [FxBaseEffect](https://developer.apple.com/documentation/fxplug/fxbaseeffect) and [FxFilter](https://developer.apple.com/documentation/fxplug/fxfilter) protocols. This means existing plug-ins will build without any changes. However, plug-ins that use the temporal image API or image well parameters should properly implement scheduling to take advantage of the performance improvements. The new [FxBaseEffect](https://developer.apple.com/documentation/fxplug/fxbaseeffect) methods have an additional parameter related to image parameter numbering.

[Next](Working%20with%20Entitlements.md)[Previous](What%E2%80%99s%20New%20in%20FxPlug%203.1.1.md)

