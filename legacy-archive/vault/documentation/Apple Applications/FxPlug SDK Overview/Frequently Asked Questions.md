---
title: FxPlug SDK Overview
apple_id: TP40002180
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/FXPlug_overview/FAQs/FAQs.html
archived_at: '2026-07-15T05:17:57.040090Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [FxPlug SDK Overview](About%20the%20FxPlug%20SDK.md)


[Next](Document%20Revision%20History.md)[Previous](FxPlug%20SDK%20Version%20History.md)

# Frequently Asked Questions

You can download the FxPlug SDK from [https://developer.apple.com/download/more/?=FXPlug](https://developer.apple.com/download/more/?=FXPlug).

To test your plug-in code in a target application, you can choose Project > Scheme > Edit Scheme, and under the Info tab for the Run action you can choose Motion or Final Cut Pro as the Executable.

You can put the file in the Resources folder for the plug-in. Then you can access the bundle from a method of one of the classes in your plug-in, like this:

```
  NSBundle *bundle = [NSBundle bundleForClass:[self  class]];
```

(The FxPlug Xcode templates do this to get localized strings.) To get data from a file called `filename.extension` in your Resources folder, you can use this snippet:

```
NSBundle *bundle = [NSBundle bundleForClass:[  self  class]];
NSString *path = [bundle pathForResource:  @"filename"
ofType:  @"extension"  ];

 NSString *dataString = [NSString stringWithContentsOfFile:path];
```


If a frame is interlaced, you’ll know in your `-renderOutput:` method, because the [FxRenderInfo](https://developer.apple.com/documentation/fxplug/fxrenderinfo) structure that’s passed in will have the “field” member set to either [kFxField_UPPER](https://developer.apple.com/documentation/fxplug/2625151-anonymous/kfxfield_upper) or [kFxField_LOWER](https://developer.apple.com/documentation/fxplug/2625151-anonymous/kfxfield_lower). Note that it doesn’t tell you the field you have, but rather what the field order is. If a frame isn’t interlaced, the “field” member will have the value [kFxField_NONE](https://developer.apple.com/documentation/fxplug/2625151-anonymous/kfxfield_none).

First, get the [FxTemporalImageAPI](https://developer.apple.com/documentation/fxplug/fxtemporalimageapi) and call one of these two methods:

```
-getInputBitmap:withInfo:atTime:
```

or

```
-getInputTexture:withInfo:atTime:
```

For the first field of frame _t_, use time _t_, and for the second field, use time _t + 0.5_.

The following code snippet returns a string, `appIdentity`, which specifies the host application:

```
CFBundleRef appBundle = CFBundleGetMainBundle();
CFStringRef appIdentity = NULL;
if ( appBundle != NULL )
    appIdentity = CFBundleGetIdentifier( appBundle );
```

Motion bundle identifier is `com.apple.motionapp`; the Final Cut Pro identifier is `com.apple.FinalCut` or `com.apple.FinalCutTrial`.

In FxPlug parlance, a reference to another clip or external media file is called an _image reference_. So using the [FxParameterCreationAPI](https://developer.apple.com/documentation/fxplug/fxparametercreationapi) protocol, call the following method to create the parameter:

```
-addImageReferenceWithName:parmId:parmFlags:
```

To get the parameter’s value, use either:

```
-getBitmap:layerOffsetX:layerOffsetY:requestInfo:fromParm:atTime:
```

or

```
-getTexture:layerOffsetX:layerOffsetY:requestInfo:fromParm:atTime:
```


In your `-parameterChanged:` method, and in response to an event in a custom parameter view or onscreen control, you’ll need to determine the current time. You can do this by calling the `-currentTime` method in the `FxCustomParameterAPI` protocol.

Yes, but the Plug-in Manager places a restriction on how you do this. If you create multiple FxPlug effects in different bundles and assign them to the same groups, the different bundles must use different group UUIDs but have the same group name. If you use the same group UUID in two bundles, the plug-ins in only one of the two bundles are loaded.

[Next](Document%20Revision%20History.md)[Previous](FxPlug%20SDK%20Version%20History.md)

