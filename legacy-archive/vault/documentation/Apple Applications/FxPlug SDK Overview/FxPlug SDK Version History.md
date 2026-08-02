---
title: FxPlug SDK Overview
apple_id: TP40002180
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/FXPlug_overview/FxPlugVersionHistory/FxPlugVersionHistory.html
archived_at: '2026-07-15T05:17:57.065054Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [FxPlug SDK Overview](About%20the%20FxPlug%20SDK.md)


[Next](Frequently%20Asked%20Questions.md)[Previous](Testing%20Your%20Plug-in.md)

# FxPlug SDK Version History

This chapter lists the changes for each version of the FxPlug SDK from version 1.0 through 3.1. For the best possible backward compatibility, and to make your plug-in work with any version of a host application, have the plug-in first check for the availability of a host API for an SDK feature, and then only use that feature if the API is available. If a particular host API is not available, your plug-in needs to fall back to an alternative behavior.

The FxPlug 3.1 SDK includes the following new features:

- New FxTime data type can use frame numbers or rational time.
- Media inputs can be scheduled ahead of time for increased speed.

The release makes various bug fixes and improvements, including:

- Default values for all FxPlug parameters are now saved in the document.
- When an FxPlug plug-in is archived, it no longer creates a symlink in the archive.

What’s New in Motion 5.2.2 and Final Cut Pro 10.2.2:

- Automatically restarts XPC process in FxPlug 3 effects.
- [FxTimingAPI](https://developer.apple.com/documentation/fxplug/fxtimingapi) methods return correct float values for effects inside Final Cut Pro X storylines.
- [FxTimingAPI](https://developer.apple.com/documentation/fxplug/fxtimingapi) properly calculates position of Motion effects in Final Cut Pro X.
- Fixes the calculation of durations in the [FxTimingAPI](https://developer.apple.com/documentation/fxplug/fxtimingapi).
- Fixes the timing of FxPlug effects within published Motion projects.

The FxPlug 3.0.1 SDK includes these changes:

- The FxPlug SDK is now ARC compatible.
- It resolves issues that could lead to broken symlinks when archiving FxPlug plug-ins in Xcode 5.
- It fixes a missing protocol issues in SDK sample code.
- It improves the accuracy of included Xcode templates.

The biggest change in FxPlug 3.0 SDK is the support for application sandboxing. This new support required changes to the FxPlug structure, including how it’s packaged, loaded, and used.

- Entitlements—With the introduction of application sandboxing, applications must list all the ways it can access system resources. These are called _entitlements_. For security reasons each of our host applications provides only a minimal amount of entitlements, which in most cases may not be sufficient for the needs of third-party developers.
- New application structure—FxPlug plug-ins are transitioning from a filter bundle to an application bundle which contains two internal bundles, called the _Embedded Principal_ and _Service Principal_ components. This requires changes to your Xcode project structure._Embedded Principal_ and _Service Principal_ components. This requires changes to your Xcode project structure.
- New controls—Three new controls are available:

  - Push Buttons—Allow a plug-in to display a push button in the inspector or HUD and perform an action, such as opening a settings window, when it’s displayed.
  - Help Buttons—Allow a plug-in to take some action to display help content to the user.
  - Font Menu—Allows a plug-in to display the list of installed fonts from which the user can choose one.
- Custom UI support for Final Cut Pro Effects containing FxPlug 3–based plug-ins.
- Multi-GPU support—A new `kFxPropertyKey_IsThreadSafe` key has been added to allow plug-ins to build and render multiple frames simultaneously.

  This new key can be added to the dictionary returned by a plug-in’s `-properties` method with a `BOOL` value of `YES` to indicate to the host application that it’s safe to call the plug-in to render on multiple threads at the same time. This key is extremely useful when running on machines with multiple GPUs, because they can render one frame per GPU at the same time, decreasing rendering times significantly. When this flag is set, a plug-in’s `-getOutputWidth:height:::`, `-frameSetup:::`, `-frameCleanup`, and `-renderOutput:::` methods are assumed to all be thread-safe. Plug-ins must take care to ensure that they follow the rules of thread safety when they set this flag, because data corruption or crashes can occur if two threads access the same data at the same time.

  For more information on concurrent OpenGL, refer to _[OpenGL Programming Guide for Mac](../../Graphics%20Imaging/OpenGL%20Programming%20Guide%20for%20Mac/About%20OpenGL%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobx)_.

FxPlug 2.4 SDK provides several important bug fixes that developers should be aware of.

- Parameter state can now be set correctly and will be saved and restored correctly for Motion Templates created with Motion 5.0.5 or later. Older templates will load the same as before to ensure backward compatibility with older Final Cut Pro X projects.
- The [FxTemporalImageAPI](https://developer.apple.com/documentation/fxplug/fxtemporalimageapi) and [FxParameterRetrievalAPI](https://developer.apple.com/documentation/fxplug/fxparameterretrievalapi) now allow access to all frames and fields of footage.
- Accessing images at non-render time through the [FxTemporalImageAPI](https://developer.apple.com/documentation/fxplug/fxtemporalimageapi) or [FxParameterRetrievalAPI](https://developer.apple.com/documentation/fxplug/fxparameterretrievalapi) should now be more robust.
- Pixel transforms should now be correct and invertible for images returned by the [FxTemporalImageAPI](https://developer.apple.com/documentation/fxplug/fxtemporalimageapi) and [FxParameterRetrievalAPI](https://developer.apple.com/documentation/fxplug/fxparameterretrievalapi).
- The [FxKeyframeAPI](https://developer.apple.com/documentation/fxplug/fxkeyframeapi) should now work as expected in a Motion Template running inside Final Cut Pro.

- Sample code has been updated to remove any remaining warnings and to build properly with the latest Xcode.
- The [FxParameterCreationAPI_v3](https://developer.apple.com/documentation/fxplug/fxparametercreationapi_v3) protocol was updated to properly inherit from the [FxParameterCreationAPI_v2](https://developer.apple.com/documentation/fxplug/fxparametercreationapi_v2).

FxPlug 2.2 SDK provides several important bug fixes that developers should be aware of.

- Fixed a case of significant blurriness when adding a Final Cut Pro Effect to an interlaced clip.
- Fixed a rare stability issue when a filter didn't set the output width and height in `-getOutputWidth:height:withImage:withInfo:`.
- Fixed an issue with incorrect Pixel transforms when rendering in screen space.
- Fixed a stability issue with calls to set parameters when running in Final Cut Pro causing a hang in `-parameterChanged:`.

- Updated the DirectionalBlur example to use OpenGL Frame buffers for multipass rendering instead of PBuffers which are now deprecated.
- Updated the SimplePaint example to work properly on all video cards, with non-square pixels and at proxy resolution.
- Updated BoxTest to work properly with non-square pixels and at proxy resolution.
- Fixed calls to `getBitmap:::atTime` and `getTexture:::atTime:` so they now return images from the proper time, dimensions and scaling information.
- Fixed an issue where images returned from Final Cut Pro are marked with the correct origin.

FxPlug 2.1 SDK provides several important bug fixes that developers should be aware of.

The `FxTemporalAPI` should work more consistently outside of render time.

- Image sizes should now be correct when getting images from the parameter or temporal APIs regardless of rendering resolution.
- FxPlug plug-ins in Motion Effect templates now receive correct frame rate information.
- FxPlug Timing API now returns correct information if an Image well doesn’t contain footage.
- The Scrolling Rich Text and Options Dialog examples now build and load correctly.

The most obvious change in release 2.0 of FxPlug SDK is the addition of several new APIs. There are also a number of changes required for updating to 64-bit and working with the latest Final Cut Pro and Motion applications.

The FxPlug 2.0 SDK includes these components:

- The FxPlugSDK installer, which installs the FxPlug header files in the FxPlug framework. It also installs several FxPlug examples in `/Developer/Examples`. Included is an About FxPlug Examples file that provides details about the examples.

The biggest change is that all FxPlug plug-ins now run either directly in Motion or as part of a Motion Effect running inside of Final Cut Pro.

This makes most of the differences between hosts from previous versions disappear, making it easier for developers to write and maintain plug-ins.

For your plug-ins to run in Final Cut Pro, you must create a Motion Effect for each one.

All FxPlug plug-ins must now be compiled 64-bit to run in Motion 5 or later. This will require a recompile of all existing plug-ins, because you must link against the 64-bit versions of the FxPlug and PluginManager frameworks.

Along with this change, several of the pieces required to build plug-ins have moved.

Because Motion and Final Cut Pro are now available as self-contained applications on the Mac App Store, the `FxPlug.framework` and `PluginManager.framework`, which are loaded at runtime, are stored inside each application's bundle.

The developer versions of these frameworks, which contain the headers used to build your plug-ins, are now stored in `/Developer/Examples/FxPlug/`, along with several new developer examples showcasing the new APIs.

FxPlug 2.0 includes new classes and protocols. The following lists those additions and their features.

**Dynamic Parameter API**
: The dynamic parameter API allows you to add and remove parameters at runtime rather than simply showing and hiding them. See _[FxDynamicParameterAPI Protocol Reference](https://developer.apple.com/documentation/fxplug/fxdynamicparameterapi)_ for more information.

**Keyframe API**
: The keyframe API allows you to retrieve keyframe times and values as well as create new keyframes. See _[FxKeyframeAPI Protocol Reference](https://developer.apple.com/documentation/fxplug/fxkeyframeapi)_ for more information.

**Custom Window API**
: The custom window API gives you a window to draw into which looks like other windows in the application, and tells you when the application is finished with the window. See _[FxWindowAPI Protocol Reference](https://developer.apple.com/documentation/fxplug/fxwindowapi)_ and _[FxWindowHost Protocol Reference](https://developer.apple.com/documentation/fxplug/fxwindowhost)_ for more information.

**Re-Render API**
: The re-rendering API allows your plug-in to inform the host that needs to re-render your plug-in content. See _[FxRenderNotificationAPI Protocol Reference](https://developer.apple.com/documentation/fxplug/fxrendernotificationapi)_ for more information.

**Path API**
: The path API gives you access to polygonal, bezier, and x-spline curve data created by users. See _[FxPathAPI Protocol Reference](https://developer.apple.com/documentation/fxplug/fxpathapi)_ for more information.

**Host Resource Management API**
: The host application can now create and track resources that your plug-in requests such as memory, OpenGL textures and buffers. It also gives plug-ins the ability to tell the host to execute a method on several threads at once so plug-ins can use multiple processors. See _[FxHostResourcesAPI Protocol Reference](https://developer.apple.com/documentation/fxplug/fxhostresourcesapi)_ and _[FxHostResourcesClient Protocol Reference](https://developer.apple.com/documentation/fxplug/fxhostresourcesclient)_ for more information.

**Undo API**
: The undo API helps plug-ins to coalesce events in custom user interface and onscreen controls so they can be undone and redone as a single event. See _[FxUndoAPI Protocol Reference](https://developer.apple.com/documentation/fxplug/fxundoapi)_ for more information.

**Lighting API**
: The lighting API allows the retrieval of information about lights the user has placed in a 3D scene. See _[FxLightingAPI Protocol Reference](https://developer.apple.com/documentation/fxplug/fxlightingapi)_ for more information.

**Interpolatable Custom Parameters**
: The parameter APIs have been updated to support interpolation in custom parameters. See _[FxCustomParameterInterpolation Protocol Reference](https://developer.apple.com/documentation/fxplug/fxcustomparameterinterpolation)_ for more information.

Several aspects of the FxPlug SDK have been cleaned up. Several methods have been deprecated that were either confusingly named or that worked poorly. New methods have been added, where appropriate, to achieve the same results more cleanly and clearly.

Version 1.2.5 of the FxPlug SDK is functionally unchanged from version 1.2.4 and features no bug fixes.

Version 1.2.4 of the FxPlug SDK is released with Final Cut Pro 7.0 and Motion 4.0. The FxPlug 1.2.4 SDK Framework is functionally unchanged from the FxPlug 1.2.3 SDK Framework, however the applications now take advantage of more of the features.

- The [FxVersioningAPI](https://developer.apple.com/documentation/fxplug/fxversioningapi) now works correctly during `-addParameters`.
- FxPlug generators produce gamma 1.8 or gamma 2.2 images, depending on the display
settings.
- `FxParameterRetrievalAPI:getBitmap` is now reliable during UI time.
- If one parameter group is nested inside another, and the nested group is the last item in the enclosing group, parameters following the outer group are now displayed correctly. Previously they would appear inside the outer group.
- Setting point parameter values with the [FxParameterSettingAPI_v2](https://developer.apple.com/documentation/fxplug/fxparametersettingapi_v2) now works correctly. Previously, it wouldn't work if the new value contained a changed X value but the same Y value.
- Final Cut Pro no longer crashes if a plug-in doesn't specify a group name.
- Fixed a problem that could occur if a plug-in added new parameters above custom UI parameters and a project created with the previous version of the plug-in was loaded.
- Images from the `FxTemporalAPI` are now correctly premultiplied. Previously, they were labelled as premultiplied, but the pixels were not actually premultiplied.

- [Fx3DAPI](https://developer.apple.com/documentation/fxplug/fx3dapi) is now available to generators.
- Custom controls in generators are now displayed in the HUD.
- The UI should now properly update when plug-ins hide parameters.
- The `-pixelForma`t method of both input and output images now returns the correct value.
- Plug-ins can now check for the existence of the [Fx3DAPI](https://developer.apple.com/documentation/fxplug/fx3dapi) at `-addParameters` time (but should not use the API at that time).
- Text parameters now enable and disable appropriately.
- Generators can now access `FxLayerInfoAPI`.
- Motion now prints a message to the console if the data sent to the various methods in [FxParameterCreationAPI](https://developer.apple.com/documentation/fxplug/fxparametercreationapi) are invalid. (For example, if the minimum parameter value is greater than the maximum, or the slider min/max values are outside the parameter min/max values.)
- `FxImages` are labeled correctly, depending on the display settings.
- When duplicating an instance of an old plug-in, the new copy now also reports the old version number.
- A plug-in rendering inside a Motion project within the Final Cut Pro timeline now correctly gets Motion as the host when it asks to identify the host it’s rendering under.
- Output images from generators now have the correct field information.
- Previews now render right-side up.
- `-getSourceTexture:` and `-getSourceBitmap:` now work correctly for filters applied to groups.

Version 1.2.3 of the FxPlug SDK provides minor bug fixes and documentation corrections.

Version 1.2.1 of the FxPlug SDK was released with Final Cut Pro 6.0.1 and Motion 3.0.1.

The new `FxImageColorInfo` enumerated type identifies some basic color properties of an [FxImage](https://developer.apple.com/documentation/fxplug/fximage). For YUV images, this enumeration tells you whether you should use the Rec. 601 or Rec. 709 color matrix to convert an image to RGB. For RGB images, it describes the gamma level of the image.

FxPlug 1.2.2 SDK installs its Xcode templates in the location expected by Xcode 2.5 and later. Symbolic links are installed into the legacy location, so you can still open the templates using an earlier version of Xcode.

Plug-ins can now evaluate their parameter values at any time during `-parameterChanged`, or from within custom UI code. Previously, parameters could be evaluated at any time during `-renderOutput`, but otherwise only at the current time.

Parameter groups now contain disclosure triangles that allow a group to be collapsed and expanded. The [kFxParameterFlag_COLLAPSED](https://developer.apple.com/documentation/fxplug/2625055-anonymous/kfxparameterflag_collapsed) flag is also respected; plug-ins can use this flag to create groups that are initially collapsed, or to programmatically collapse or expand groups in response to other parameter changes.

The start point, end point, and reverse controls in the Transition Viewer are now respected when rendering FxPlug transitions. These three controls affect the _time fraction_ passed to the transition's render method; the _reverse_ control also swaps the A and B images. You should not have to change your plug-in to take advantage of these controls.

Fixed a bug that could result in crashes when undoing the addition of a filter, or when copying and pasting filters.

Hiding and disabling groups now work correctly with nested groups. However, there is still no visual indication that the groups are nested.

Plug-ins can use the new `FxImageColorInfo` API to determine if a YUV image is Rec. 601 or Rec. 709. This allows for improved YUV support, or accurate conversion to high-precision RGB within the plug-in.

Previously, the [FxTemporalTransitionImageAPI](https://developer.apple.com/documentation/fxplug/fxtemporaltransitionimageapi) interpreted the times passed as relative to the requested source clip. Now the times are interpreted as relative to the transition item. This is consistent with all other uses of time in Final Cut Pro.

Fixed a bug where custom UI could appear in the wrong location if the filter viewer was dragged to a second monitor.

Fixed a bug where input images in the legacy non-real-time display path were not tagged with the correct aspect ratio.

Fixed a bug where input images for transitions were not labeled with the correct field order.

Final Cut Pro no longer ignores the [kFxParameterFlag_HIDDEN](https://developer.apple.com/documentation/fxplug/2625055-anonymous/kfxparameterflag_hidden) flag when creating groups. However, groups must be disabled after the parameters they contain have been added.

Previously, when a user changed a document with a custom control, Motion did not flag the document as changed and could close it without saving the changes. Motion now properly flags the document as changed. It also fixes a crash that could occur during an undo.

When you retrieve a bitmap from an image well parameter, the image now has the proper gamma setting that matches the gamma setting it would have if you had dropped it directly into the timeline.

The various API Objects have been refactored to make them accessible at more times and to reduce the number of thread related problems. Plug-in developers should test to be sure that the APIs all still work as expected.

Motion now uses interpolation rather than line doubling to up-sample fields to frame size.

Version 1.2.1 of the FxPlug SDK was released with Final Cut Pro 6.0.1 and Motion 3.0.1. The FxPlug 1.2.1 SDK includes two new protocols, one for managing 3D camera and layer information in Motion, and another that allows plug-ins to manage backward compatibility issues. The host applications Final Cut Pro 6.0.1 and Motion 3.0.1 also contain fixes related to the FxPlug APIs.

__Motion only:__ Plug-ins can use the new [Fx3DAPI](https://developer.apple.com/documentation/fxplug/fx3dapi) protocol to get the 3D transforms for the camera and for the plug-in's layer.

Plug-ins that include a `version` key in their `Info.plist` files can use the new [FxVersioningAPI](https://developer.apple.com/documentation/fxplug/fxversioningapi) protocol to determine what version of their plug-in was used when a project was created.

For angle parameters, `-getFloatValue` and `-setFloatValue` now use degrees in all host applications.

In addition to SimpleMatte and SimplePaint, the FxPlug 1.2 SDK provided new example plug-in projects installed in `/Developer/Examples/FxPlug`:

- DirectionalBlurExample
- Options Dialog
- ScrollingRichText
- Slow SolidColor

The method `[FxTimingAPI durationForEffect]` returns the correct duration of FxPlug transition effects.

The methods `[FxTimingAPI startTimeOfImageParm]` and `[FxTimingAPI durationOfImageParm]`return the correct start time and duration for image parameters, even if the media in the image wells do not have in and out points set.

The [kFxParameterFlag_HIDDEN](https://developer.apple.com/documentation/fxplug/2625055-anonymous/kfxparameterflag_hidden) flag works correctly with group start and end markers.

Hiding or showing a parameter no longer causes the parameter list to scroll to the top.

Hiding a parameter no longer causes a spurious horizontal line to be drawn in the parameter list.

Previously, the output images for RGB-only generators would be labeled as RGBA, but the results would be interpreted as ARGB in 8-bit. The images are now correctly labeled as ARGB in 8-bit and RGBA in float.

Retrieving bitmap images using the temporal image API no longer causes a gamma shift in the retrieved image.

Retrieving bitmap images from a group no longer causes the group to render upside down.

Motion now properly releases custom NSViews when a filter is deleted.

Retrieving bitmap images from 16-bit per channel footage now returns proper 32-bit per channel footage.

Repeated renders are no longer queued up when a custom control calls `-startAction` and `-endAction` during its -`drawRect:` method. This keeps the control and the current frame from constantly re-rendering.

Motion no longer crashes under certain circumstances when calling `-currentTime:` in the [FxCustomParameterActionAPI](https://developer.apple.com/documentation/fxplug/fxcustomparameteractionapi) protocol.

Parameters are now properly updated in the inspector when their enabled-disabled or hidden-shown state is changed.

Version 1.2 of the FxPlug SDK was released with Final Cut Pro 6.0 and Motion 3.0. The focus of FxPlug 1.2 SDK is improved consistency between Motion and Final Cut Pro, and better support for timing information. In addition to the changes in the FxPlug framework itself, there are other FxPlug-related changes in Plug-in Manager 1.7, Final Cut Pro 6, and Motion 3.

A [FxTimingAPI](https://developer.apple.com/documentation/fxplug/fxtimingapi) protocol defines the methods provided by the host that allow a plug-in to query the timing properties of its input image(s), image parameters, effect, timeline, and in/out points. This protocol is the most significant change in FxPlug 1.2 SDK.

FxImage objects now respond to `-field` and `-fieldOrder` accessors. These accessors provide information about fields in interlaced images: the field identifier for an image, and the field order of an image. The incorrectly named field `FxRenderInfo.field` has been renamed `FxRenderInfo.fieldOrder`. But you should use the [FxImage](https://developer.apple.com/documentation/fxplug/fximage) accessors instead.

A [FxProgressAPI](https://developer.apple.com/documentation/fxplug/fxprogressapi) protocol defines methods for plug-ins that render slowly to update a progress bar and support user cancellation.

__Final Cut Pro only:__ The [FxTemporalTransitionImageAPI](https://developer.apple.com/documentation/fxplug/fxtemporaltransitionimageapi) protocol allows a plug-in to retrieve its A or B input images at different times. In FxPlug 1.1, retiming was only enabled for images from filter inputs and image wells, not for transition input images.

An `[FxHostCapabilities timeBase]` method allows a plug-in to determine whether the host application measures times as frame offsets from the start of the timeline, or from the start of a clip, generator, filter, or transition.

The `-getAngle:fromParm:atTime:` method is deprecated. Plug-ins should use `-getFloatValue:` instead.

The Plug-in Manager no longer requires a plug-in Info.plist file to declare which host APIs the plug-in might use. However, for a plug-in to load on a system with an older version of the Plug-in Manager, the plug-in should still list these APIs in the ProPlugProtocolList—as illustrated by the example projects and Xcode templates.

Final Cut Pro 6 respects `kFxParameterFlag_HIDDEN` and [kFxParameterFlag_DISABLED](https://developer.apple.com/documentation/fxplug/2625055-anonymous/kfxparameterflag_disabled). A plug-in can specify these flags when it creates parameters, and change them dynamically with the `-setParameterFlags:` selector of `FxParameterSettingAPI` .

Final Cut 6 respects the [kFxParameterFlag_NOT_ANIMATABLE](https://developer.apple.com/documentation/fxplug/2625055-anonymous/kfxparameterflag_not_animatable) flag if it’s set when a parameter is created. A plug-in cannot change this flag dynamically once a parameter is created.

Final Cut Pro 6 provides some support for parameter groups. Parameter groups are implemented as labels separating the parameters, similar to After Effects plug-ins in Final Cut Pro. The groups cannot be collapsed or nested.

Final Cut Pro 5.1.2 did not implement the [FxParameterSettingAPI](https://developer.apple.com/documentation/fxplug/fxparametersettingapi) and a plug-in could not set the values of its parameters after creation. Final Cut Pro 6 supports this API. Plug-ins can now change the values of their parameters dynamically. For example, an effect might want to implement a _presets_ functionality by changing some parameter values when the user makes a choice from a popup menu.

A plug-in running under Final Cut Pro 5.1.2 could only sample parameters at the current render time. The only exception to this was image parameters. In Final Cut Pro 6, a plug-in can sample any type of parameter at any time. This allows an effect to examine the values of key-framed parameters at multiple times.

At startup, Final Cut Pro 5.1.2 instantiated each installed plug-in multiple times, sometimes sending the plug-in an `-initWithAPIManager:` message, sometimes sending the plug-in an `-init` message. At startup, Final Cut Pro 6 instantiates a plug-in once via `-initWithAPIManager:`, sends the instance the following messages:

- `-addParameters`
- `-variesOverTime`
- `-properties`

and releases the plug-in instance.

Final Cut Pro 5.1.2 created two instances of a plug-in when the plug-in was added to a timeline, using one instance for rendering and the other instance for parameter management. Final Cut Pro 6 creates one instance when a plug-in is added to a timeline and uses this single instance for both rendering and parameter management.

Final Cut Pro 5.1.2 always set the initial value of point controls at the center of the image. Final Cut Pro 6 uses the value specified by the plug-in.

Final Cut Pro 5.1.2 asked a plug-in to render on the GPU unless the plug-in returned `canDoHardware = NO` from `-frameSetup`. Final Cut Pro 6 asks a plug-in to render in software if:

- The plug-in returns `canDoSoftware=YES` from `-frameSetup`
- AND
- The plug-in specifies `kFxPropertyKey_SupportsRowBytes = YES`

Otherwise, Final Cut Pro 6 asks the plug-in to render in hardware.

Final Cut Pro 5.1.2 sent plug-ins the `-parameterChanged:` message only if the parameter change caused a render. If the playhead was not on the item with the effect, Final Cut Pro 5.1.2 did not send the message. Final Cut Pro 6 sends a plug-in this message immediately when a parameter changes, whether the change causes a render or not.

In Final Cut Pro 5.1.2, a plug-in request for the value of a parameter that had not been added created an Objective-C exception and left Final Cut Pro in an inconsistent state. In Final Cut Pro 6, a request for a parameter that does not exist simply returns NO.

In Final Cut Pro 5.1.2, if an FxPlug effect was rendering in software and did not change the size of the output image, the output image would always have a pixel aspect ratio of 1.0. In Final Cut Pro 6, the pixel aspect ratio is reported correctly.

Final Cut Pro 6 does not support onscreen controls.

Final Cut Pro 6 does not allow a filter to resize its output image. In addition, it no longer calls the `-getOutputWidth:height:` method.

In Final Cut Pro 6, [FxTimingAPI](https://developer.apple.com/documentation/fxplug/fxtimingapi) and [FxTemporalImageAPI](https://developer.apple.com/documentation/fxplug/fxtemporalimageapi) only work correctly if called during one of the following selectors:

- `-getOutputWidth: height:`
- `-frameSetup`
- `-renderOutput`
- `-frameCleanup`

As well, sampling key-framed parameters at arbitrary times only works during these selectors.

Motion 2.1 did not call `-parameterChanged:` when the value of a compound parameter (for example, point, color, histogram, gradient) changed. Motion 3 does.

Motion 2.1 did not provide the correct `pixelAspect` value for [FxTexture](https://developer.apple.com/documentation/fxplug/fxtexture) images retrieved from image well parameters. Motion 3 corrects this problem.

Motion 2.1 ordered pixel components RGBA in floating-point images, but the `-pixelFormat` method returned ARGB. Motion 3 corrects this problem. You can determine whether floating-point images are mislabeled by querying `[FxHostCapabilities formatsFloatRGBABitmapsAsARGB]`.

Motion 2.1 had problems retrieving images from image well parameters at arbitrary times. The resulting images were at incorrect times and upside-down. Motion 3 retrieves these images correctly.

Motion 3 adds support for the [kFxParameterFlag_NOT_ANIMATABLE](https://developer.apple.com/documentation/fxplug/2625055-anonymous/kfxparameterflag_not_animatable) flag.

Motion 3 corrects an issue in Motion 2.1 that produced incorrect results when resizing either via `-getOutputWidth:height:` or down-sampling for low quality render.

FxPlug 1.0 SDK was introduced together with Motion 2.0 in April 2005. A few months later, version 1.0.2 was released with support for Universal Binary plug-ins but no API changes.

Version 1.1 of the FxPlug SDK was the first version that worked with Final Cut Pro 5.1.2. Version 1.1 added a number of new features, including:

- Transitions.
- New [FxBaseEffect](https://developer.apple.com/documentation/fxplug/fxbaseeffect) parent protocol for filters, generators, and transitions.
- String parameters.
- A new `-properties` method that returns a dictionary describing plug-in attributes.
- 8-bit and floating-point YUV ('r408' and 'r4fl') bitmaps.
- Row bytes support in bitmaps.
- SMPTE wipe equivalents for transitions.
- A new [FxHostCapabilities](https://developer.apple.com/documentation/fxplug/fxhostcapabilities) class for determining the capabilities of the host application.

[Next](Frequently%20Asked%20Questions.md)[Previous](Testing%20Your%20Plug-in.md)

