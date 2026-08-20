---
title: AVFoundation Programming Guide
apple_id: TP40010188
resource_type: Guide
platform: tvOS|iOS|macOS
topic: null
technology: AVFoundation
published: '2015-06-30'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/AVFoundationPG/Articles/04_MediaCapture.html
archived_at: '2026-07-15T05:20:58.705609Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AVFoundation Programming Guide](About%20AVFoundation.md)


[Next](Export.md)[Previous](Editing.md)

# Still and Video Media Capture

To manage the capture from a device such as a camera or microphone, you assemble objects to represent inputs and outputs, and use an instance of [AVCaptureSession](https://developer.apple.com/documentation/avfoundation/avcapturesession) to coordinate the data flow between them. Minimally you need:

- An instance of [AVCaptureDevice](https://developer.apple.com/documentation/avfoundation/avcapturedevice) to represent the input device, such as a camera or microphone
- An instance of a concrete subclass of [AVCaptureInput](https://developer.apple.com/documentation/avfoundation/avcaptureinput) to configure the ports from the input device
- An instance of a concrete subclass of [AVCaptureOutput](https://developer.apple.com/documentation/avfoundation/avcaptureoutput) to manage the output to a movie file or still image
- An instance of [AVCaptureSession](https://developer.apple.com/documentation/avfoundation/avcapturesession) to coordinate the data flow from the input to the output

To show the user a preview of what the camera is recording, you can use an instance of [AVCaptureVideoPreviewLayer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer) (a subclass of [CALayer](https://developer.apple.com/documentation/quartzcore/calayer)).

You can configure multiple inputs and outputs, coordinated by a single session, as shown in Figure 4-1

__Figure 4-1__  A single session can configure multiple inputs and outputs

!

For many applications, this is as much detail as you need. For some operations, however, (if you want to monitor the power levels in an audio channel, for example) you need to consider how the various ports of an input device are represented and how those ports are connected to the output.

A connection between a capture input and a capture output in a capture session is represented by an [AVCaptureConnection](https://developer.apple.com/documentation/avfoundation/avcaptureconnection) object. Capture inputs (instances of [AVCaptureInput](https://developer.apple.com/documentation/avfoundation/avcaptureinput)) have one or more input ports (instances of [AVCaptureInputPort](https://developer.apple.com/documentation/avfoundation/avcaptureinputport)). Capture outputs (instances of [AVCaptureOutput](https://developer.apple.com/documentation/avfoundation/avcaptureoutput)) can accept data from one or more sources (for example, an [AVCaptureMovieFileOutput](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput) object accepts both video and audio data).

When you add an input or an output to a session, the session forms connections between all the compatible capture inputs’ ports and capture outputs, as shown in Figure 4-2. A connection between a capture input and a capture output is represented by an [AVCaptureConnection](https://developer.apple.com/documentation/avfoundation/avcaptureconnection) object.

__Figure 4-2__  AVCaptureConnection represents a connection between an input and output

!

You can use a capture connection to enable or disable the flow of data from a given input or to a given output. You can also use a connection to monitor the average and peak power levels in an audio channel.

An [AVCaptureSession](https://developer.apple.com/documentation/avfoundation/avcapturesession) object is the central coordinating object you use to manage data capture. You use an instance to coordinate the flow of data from AV input devices to outputs. You add the capture devices and outputs you want to the session, then start data flow by sending the session a [startRunning](https://developer.apple.com/documentation/avfoundation/avcapturesession/1388185-startrunning) message, and stop the data flow by sending a [stopRunning](https://developer.apple.com/documentation/avfoundation/avcapturesession/1385661-stoprunning) message.

```
AVCaptureSession *session = [[AVCaptureSession alloc] init];
// Add inputs and outputs.
[session startRunning];
```


You use a _preset_ on the session to specify the image quality and resolution you want. A preset is a constant that identifies one of a number of possible configurations; in some cases the actual configuration is device-specific:

| Symbol | Resolution | Comments |
| --- | --- | --- |
| [AVCaptureSessionPresetHigh](https://developer.apple.com/documentation/avfoundation/avcapturesession/preset/1388084-high) | High | Highest recording quality.  This varies per device. |
| [AVCaptureSessionPresetMedium](https://developer.apple.com/documentation/avfoundation/avcapturesessionpresetmedium) | Medium | Suitable for Wi-Fi sharing.  The actual values may change. |
| [AVCaptureSessionPresetLow](https://developer.apple.com/documentation/avfoundation/avcapturesession/preset/1386357-low) | Low | Suitable for 3G sharing.  The actual values may change. |
| [AVCaptureSessionPreset640x480](https://developer.apple.com/documentation/avfoundation/avcapturesessionpreset640x480) | 640x480 | VGA. |
| [AVCaptureSessionPreset1280x720](https://developer.apple.com/documentation/avfoundation/avcapturesessionpreset1280x720) | 1280x720 | 720p HD. |
| [AVCaptureSessionPresetPhoto](https://developer.apple.com/documentation/avfoundation/avcapturesessionpresetphoto) | Photo | Full photo resolution.  This is not supported for video output. |

If you want to set a media frame size-specific configuration, you should check whether it is supported before setting it, as follows:

```
if ([session canSetSessionPreset:AVCaptureSessionPreset1280x720]) {
    session.sessionPreset = AVCaptureSessionPreset1280x720;
}
else {
    // Handle the failure.
}
```

If you need to adjust session parameters at a more granular level than is possible with a preset, or you’d like to make changes to a running session, you surround your changes with the [beginConfiguration](https://developer.apple.com/documentation/avfoundation/avcapturesession/1389174-beginconfiguration) and [commitConfiguration](https://developer.apple.com/documentation/avfoundation/avcapturesession/1388173-commitconfiguration) methods. The [beginConfiguration](https://developer.apple.com/documentation/avfoundation/avcapturesession/1389174-beginconfiguration) and [commitConfiguration](https://developer.apple.com/documentation/avfoundation/avcapturesession/1388173-commitconfiguration) methods ensure that devices changes occur as a group, minimizing visibility or inconsistency of state. After calling [beginConfiguration](https://developer.apple.com/documentation/avfoundation/avcapturesession/1389174-beginconfiguration), you can add or remove outputs, alter the `sessionPreset` property, or configure individual capture input or output properties. No changes are actually made until you invoke [commitConfiguration](https://developer.apple.com/documentation/avfoundation/avcapturesession/1388173-commitconfiguration), at which time they are applied together.

```
[session beginConfiguration];
// Remove an existing capture device.
// Add a new capture device.
// Reset the preset.
[session commitConfiguration];
```


A capture session posts [notifications](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Notification.html#//apple_ref/doc/uid/TP40008195-CH35) that you can observe to be notified, for example, when it starts or stops running, or when it is interrupted. You can register to receive an [AVCaptureSessionRuntimeErrorNotification](https://developer.apple.com/documentation/avfoundation/avcapturesessionruntimeerrornotification) if a runtime error occurs. You can also interrogate the session’s [running](https://developer.apple.com/documentation/avfoundation/avcapturesession/1388133-isrunning) property to find out if it is running, and its [interrupted](https://developer.apple.com/documentation/avfoundation/avcapturesession/1620475-isinterrupted) property to find out if it is interrupted. Additionally, both the [running](https://developer.apple.com/documentation/avfoundation/avcapturesession/1388133-isrunning) and [interrupted](https://developer.apple.com/documentation/avfoundation/avcapturesession/1620475-isinterrupted) properties are key-value observing compliant and the notifications are posted on the main thread.

An [AVCaptureDevice](https://developer.apple.com/documentation/avfoundation/avcapturedevice) object abstracts a physical capture device that provides input data (such as audio or video) to an `AVCaptureSession` object. There is one object for each input device, for example, two video inputs—one for the front-facing the camera, one for the back-facing camera—and one audio input for the microphone.

You can find out which capture devices are currently available using the `AVCaptureDevice` class methods [devices](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1386237-devices) and [devicesWithMediaType:](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1390520-devices). And, if necessary, you can find out what features an iPhone, iPad, or iPod offers (see [Device Capture Settings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcobyfvbuqnjnknltcoa)). The list of available devices may change, though. Current input devices may become unavailable (if they’re used by another application), and new input devices may become available, (if they’re relinquished by another application). You should register to receive [AVCaptureDeviceWasConnectedNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1389018-avcapturedevicewasconnected) and [AVCaptureDeviceWasDisconnectedNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1387782-avcapturedevicewasdisconnected) [notifications](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Notification.html#//apple_ref/doc/uid/TP40008195-CH35) to be alerted when the list of available devices changes.

You add an input device to a capture session using a capture input (see [Use Capture Inputs to Add a Capture Device to a Session](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcobyfvbuqnjnknltm)).

You can ask a device about its different characteristics. You can also test whether it provides a particular media type or supports a given capture session preset using [hasMediaType:](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1389487-hasmediatype) and [supportsAVCaptureSessionPreset:](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1386263-supportsavcapturesessionpreset) respectively. To provide information to the user, you can find out the position of the capture device (whether it is on the front or the back of the unit being tested), and its localized name. This may be useful if you want to present a list of capture devices to allow the user to choose one.

Figure 4-3 shows the positions of the back-facing ([AVCaptureDevicePositionBack](https://developer.apple.com/documentation/avfoundation/avcapturedevice/position/back)) and front-facing ([AVCaptureDevicePositionFront](https://developer.apple.com/documentation/avfoundation/avcapturedeviceposition/avcapturedevicepositionfront)) cameras.

__Figure 4-3__  iOS device front and back facing camera positions

!

The following code example iterates over all the available devices and logs their name—and for video devices, their position—on the unit.

```
NSArray *devices = [AVCaptureDevice devices];

for (AVCaptureDevice *device in devices) {

    NSLog(@"Device name: %@", [device localizedName]);

    if ([device hasMediaType:AVMediaTypeVideo]) {

        if ([device position] == AVCaptureDevicePositionBack) {
            NSLog(@"Device position : back");
        }
        else {
            NSLog(@"Device position : front");
        }
    }
}
```

In addition, you can find out the device’s model ID and its unique ID.

Different devices have different capabilities; for example, some may support different focus or flash modes; some may support focus on a point of interest.

The following code fragment shows how you can find video input devices that have a torch mode and support a given capture session preset:

```
NSArray *devices = [AVCaptureDevice devicesWithMediaType:AVMediaTypeVideo];
NSMutableArray *torchDevices = [[NSMutableArray alloc] init];

for (AVCaptureDevice *device in devices) {
    [if ([device hasTorch] &&
         [device supportsAVCaptureSessionPreset:AVCaptureSessionPreset640x480]) {
        [torchDevices addObject:device];
    }
}
```

If you find multiple devices that meet your criteria, you might let the user choose which one they want to use. To display a description of a device to the user, you can use its [localizedName](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1388222-localizedname) property.

You use the various different features in similar ways. There are constants to specify a particular mode, and you can ask a device whether it supports a particular mode. In several cases, you can observe a property to be notified when a feature is changing. In all cases, you should lock the device before changing the mode of a particular feature, as described in [Configuring a Device](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcobyfvbuqnjnknltcoi).

There are three focus modes:

- [AVCaptureFocusModeLocked](https://developer.apple.com/documentation/avfoundation/avcapturedevice/focusmode/locked): The focal position is fixed.

  This is useful when you want to allow the user to compose a scene then lock the focus.
- [AVCaptureFocusModeAutoFocus](https://developer.apple.com/documentation/avfoundation/avcapturefocusmode/avcapturefocusmodeautofocus): The camera does a single scan focus then reverts to locked.

  This is suitable for a situation where you want to select a particular item on which to focus and then maintain focus on that item even if it is not the center of the scene.
- [AVCaptureFocusModeContinuousAutoFocus](https://developer.apple.com/documentation/avfoundation/avcapturefocusmode/avcapturefocusmodecontinuousautofocus): The camera continuously autofocuses as needed.

You use the [isFocusModeSupported:](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1390215-isfocusmodesupported) method to determine whether a device supports a given focus mode, then set the mode using the [focusMode](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1389191-focusmode) property.

In addition, a device may support a focus point of interest. You test for support using [focusPointOfInterestSupported](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1390436-isfocuspointofinterestsupported). If it’s supported, you set the focal point using [focusPointOfInterest](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1385853-focuspointofinterest). You pass a `CGPoint` where `{0,0}` represents the top left of the picture area, and `{1,1}` represents the bottom right _in landscape mode with the home button on the right_—this applies even if the device is in portrait mode.

You can use the [adjustingFocus](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1390577-isadjustingfocus) property to determine whether a device is currently focusing. You can observe the property using [key-value observing](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16) to be notified when a device starts and stops focusing.

If you change the focus mode settings, you can return them to the default configuration as follows:

```
if ([currentDevice isFocusModeSupported:AVCaptureFocusModeContinuousAutoFocus]) {
    CGPoint autofocusPoint = CGPointMake(0.5f, 0.5f);
    [currentDevice setFocusPointOfInterest:autofocusPoint];
    [currentDevice setFocusMode:AVCaptureFocusModeContinuousAutoFocus];
}
```


There are two exposure modes:

- [AVCaptureExposureModeContinuousAutoExposure](https://developer.apple.com/library/ios/documentation/AVFoundation/Reference/AVCaptureDevice_Class/Reference/Reference.html#//apple_ref/doc/c_ref/AVCaptureExposureModeContinuousAutoExposure): The device automatically adjusts the exposure level as needed.
- [AVCaptureExposureModeLocked](https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposuremode/locked): The exposure level is fixed at its current level.

You use the [isExposureModeSupported:](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1389048-isexposuremodesupported) method to determine whether a device supports a given exposure mode, then set the mode using the [exposureMode](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1388858-exposuremode) property.

In addition, a device may support an exposure point of interest. You test for support using [exposurePointOfInterestSupported](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1387263-isexposurepointofinterestsupport). If it’s supported, you set the exposure point using [exposurePointOfInterest](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1388777-exposurepointofinterest). You pass a `CGPoint` where `{0,0}` represents the top left of the picture area, and `{1,1}` represents the bottom right _in landscape mode with the home button on the right_—this applies even if the device is in portrait mode.

You can use the [adjustingExposure](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1386253-adjustingexposure) property to determine whether a device is currently changing its exposure setting. You can observe the property using [key-value observing](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16) to be notified when a device starts and stops changing its exposure setting.

If you change the exposure settings, you can return them to the default configuration as follows:

```
if ([currentDevice isExposureModeSupported:AVCaptureExposureModeContinuousAutoExposure]) {
    CGPoint exposurePoint = CGPointMake(0.5f, 0.5f);
    [currentDevice setExposurePointOfInterest:exposurePoint];
    [currentDevice setExposureMode:AVCaptureExposureModeContinuousAutoExposure];
}
```


There are three flash modes:

- [AVCaptureFlashModeOff](https://developer.apple.com/documentation/avfoundation/avcaptureflashmode/avcaptureflashmodeoff): The flash will never fire.
- [AVCaptureFlashModeOn](https://developer.apple.com/documentation/avfoundation/avcapturedevice/flashmode/on): The flash will always fire.
- [AVCaptureFlashModeAuto](https://developer.apple.com/documentation/avfoundation/avcaptureflashmode/avcaptureflashmodeauto): The flash will fire dependent on the ambient light conditions.

You use [hasFlash](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1388988-hasflash) to determine whether a device has a flash. If that method returns `YES`, you then use the [isFlashModeSupported:](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1386434-isflashmodesupported) method, passing the desired mode to determine whether a device supports a given flash mode, then set the mode using the [flashMode](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1388116-flashmode) property.

In torch mode, the flash is continuously enabled at a low power to illuminate a video capture. There are three torch modes:

- [AVCaptureTorchModeOff](https://developer.apple.com/documentation/avfoundation/avcapturedevice/torchmode/off): The torch is always off.
- [AVCaptureTorchModeOn](https://developer.apple.com/documentation/avfoundation/avcapturetorchmode/avcapturetorchmodeon): The torch is always on.
- [AVCaptureTorchModeAuto](https://developer.apple.com/documentation/avfoundation/avcapturetorchmode/avcapturetorchmodeauto): The torch is automatically switched on and off as needed.

You use [hasTorch](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1387674-hastorch) to determine whether a device has a flash. You use the [isTorchModeSupported:](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1388822-istorchmodesupported) method to determine whether a device supports a given flash mode, then set the mode using the [torchMode](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1386035-torchmode) property.

For devices with a torch, the torch only turns on if the device is associated with a running capture session.

Cinematic video stabilization is available for connections that operate on video, depending on the specific device hardware. Even so, not all source formats and video resolutions are supported.

Enabling cinematic video stabilization may also introduce additional latency into the video capture pipeline. To detect when video stabilization is in use, use the [videoStabilizationEnabled](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1620485-videostabilizationenabled) property. The [enablesVideoStabilizationWhenAvailable](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1620482-enablesvideostabilizationwhenava) property allows an application to automatically enable video stabilization if it is supported by the camera. By default automatic stabilization is disabled due to the above limitations.

There are two white balance modes:

- [AVCaptureWhiteBalanceModeLocked](https://developer.apple.com/documentation/avfoundation/avcapturewhitebalancemode/avcapturewhitebalancemodelocked): The white balance mode is fixed.
- [AVCaptureWhiteBalanceModeContinuousAutoWhiteBalance](https://developer.apple.com/documentation/avfoundation/avcapturewhitebalancemode/avcapturewhitebalancemodecontinuousautowhitebalance): The camera continuously adjusts the white balance as needed.

You use the [isWhiteBalanceModeSupported:](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1388587-iswhitebalancemodesupported) method to determine whether a device supports a given white balance mode, then set the mode using the [whiteBalanceMode](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1386369-whitebalancemode) property.

You can use the [adjustingWhiteBalance](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1386544-adjustingwhitebalance) property to determine whether a device is currently changing its white balance setting. You can observe the property using [key-value observing](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16) to be notified when a device starts and stops changing its white balance setting.

You set the desired orientation on a `AVCaptureConnection` to specify how you want the images oriented in the `AVCaptureOutput` (`AVCaptureMovieFileOutput`, `AVCaptureStillImageOutput` and `AVCaptureVideoDataOutput`) for the connection.

Use the `AVCaptureConnection``supportsVideoOrientation` property to determine whether the device supports changing the orientation of the video, and the `videoOrientation` property to specify how you want the images oriented in the output port. Listing 4-1 shows how to set the orientation for a [AVCaptureConnection](https://developer.apple.com/documentation/avfoundation/avcaptureconnection) to [AVCaptureVideoOrientationLandscapeLeft](https://developer.apple.com/documentation/avfoundation/avcapturevideoorientation/landscapeleft):

__Listing 4-1__  Setting the orientation of a capture connection

```
AVCaptureConnection *captureConnection = <#A capture connection#>;
if ([captureConnection isVideoOrientationSupported])
{
    AVCaptureVideoOrientation orientation = AVCaptureVideoOrientationLandscapeLeft;
    [captureConnection setVideoOrientation:orientation];
}
```


To set capture properties on a device, you must first acquire a lock on the device using [lockForConfiguration:](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1387810-lockforconfiguration). This avoids making changes that may be incompatible with settings in other applications. The following code fragment illustrates how to approach changing the focus mode on a device by first determining whether the mode is supported, then attempting to lock the device for reconfiguration. The focus mode is changed only if the lock is obtained, and the lock is released immediately afterward.

```
if ([device isFocusModeSupported:AVCaptureFocusModeLocked]) {
    NSError *error = nil;
    if ([device lockForConfiguration:&error]) {
        device.focusMode = AVCaptureFocusModeLocked;
        [device unlockForConfiguration];
    }
    else {
        // Respond to the failure as appropriate.
```

You should hold the device lock only if you need the settable device properties to remain unchanged. Holding the device lock unnecessarily may degrade capture quality in other applications sharing the device.

Sometimes you may want to allow users to switch between input devices—for example, switching from using the front-facing to to the back-facing camera. To avoid pauses or stuttering, you can reconfigure a session while it is running, however you should use [beginConfiguration](https://developer.apple.com/documentation/avfoundation/avcapturesession/1389174-beginconfiguration) and [commitConfiguration](https://developer.apple.com/documentation/avfoundation/avcapturesession/1388173-commitconfiguration) to bracket your configuration changes:

```
AVCaptureSession *session = <#A capture session#>;
[session beginConfiguration];

[session removeInput:frontFacingCameraDeviceInput];
[session addInput:backFacingCameraDeviceInput];

[session commitConfiguration];
```

When the outermost `commitConfiguration` is invoked, all the changes are made together. This ensures a smooth transition.

To add a capture device to a capture session, you use an instance of [AVCaptureDeviceInput](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput) (a concrete subclass of the abstract [AVCaptureInput](https://developer.apple.com/documentation/avfoundation/avcaptureinput) class). The capture device input manages the device’s ports.

```
NSError *error;
AVCaptureDeviceInput *input =
        [AVCaptureDeviceInput deviceInputWithDevice:device error:&error];
if (!input) {
    // Handle the error appropriately.
}
```

You add inputs to a session using [addInput:](https://developer.apple.com/documentation/avfoundation/avcapturesession/1387239-addinput). If appropriate, you can check whether a capture input is compatible with an existing session using [canAddInput:](https://developer.apple.com/documentation/avfoundation/avcapturesession/1387180-canaddinput).

```
AVCaptureSession *captureSession = <#Get a capture session#>;
AVCaptureDeviceInput *captureDeviceInput = <#Get a capture device input#>;
if ([captureSession canAddInput:captureDeviceInput]) {
    [captureSession addInput:captureDeviceInput];
}
else {
    // Handle the failure.
}
```

See [Configuring a Session](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcobyfvbuqnjnknltcnq) for more details on how you might reconfigure a running session.

An `AVCaptureInput` vends one or more streams of media data. For example, input devices can provide both audio and video data. Each media stream provided by an input is represented by an [AVCaptureInputPort](https://developer.apple.com/documentation/avfoundation/avcaptureinputport) object. A capture session uses an `AVCaptureConnection` object to define the mapping between a set of `AVCaptureInputPort` objects and a single `AVCaptureOutput`.

To get output from a capture session, you add one or more outputs. An output is an instance of a concrete subclass of [AVCaptureOutput](https://developer.apple.com/documentation/avfoundation/avcaptureoutput). You use:

- [AVCaptureMovieFileOutput](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput) to output to a movie file
- [AVCaptureVideoDataOutput](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput) if you want to process frames from the video being captured, for example, to create your own custom view layer
- [AVCaptureAudioDataOutput](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput) if you want to process the audio data being captured
- [AVCaptureStillImageOutput](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput) if you want to capture still images with accompanying metadata

You add outputs to a capture session using [addOutput:](https://developer.apple.com/documentation/avfoundation/avcapturesession/1387325-addoutput). You check whether a capture output is compatible with an existing session using [canAddOutput:](https://developer.apple.com/documentation/avfoundation/avcapturesession/1388944-canaddoutput). You can add and remove outputs as required while the session is running.

```
AVCaptureSession *captureSession = <#Get a capture session#>;
AVCaptureMovieFileOutput *movieOutput = <#Create and configure a movie output#>;
if ([captureSession canAddOutput:movieOutput]) {
    [captureSession addOutput:movieOutput];
}
else {
    // Handle the failure.
}
```


You save movie data to a file using an [AVCaptureMovieFileOutput](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput) object. (`AVCaptureMovieFileOutput` is a concrete subclass of [AVCaptureFileOutput](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput), which defines much of the basic behavior.) You can configure various aspects of the movie file output, such as the maximum duration of a recording, or its maximum file size. You can also prohibit recording if there is less than a given amount of disk space left.

```
AVCaptureMovieFileOutput *aMovieFileOutput = [[AVCaptureMovieFileOutput alloc] init];
CMTime maxDuration = <#Create a CMTime to represent the maximum duration#>;
aMovieFileOutput.maxRecordedDuration = maxDuration;
aMovieFileOutput.minFreeDiskSpaceLimit = <#An appropriate minimum given the quality of the movie format and the duration#>;
```

The resolution and bit rate for the output depend on the capture session’s [sessionPreset](https://developer.apple.com/documentation/avfoundation/avcapturesession/1389696-sessionpreset). The video encoding is typically H.264 and audio encoding is typically AAC. The actual values vary by device.

You start recording a QuickTime movie using [startRecordingToOutputFileURL:recordingDelegate:](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/1387224-startrecording). You need to supply a file-based URL and a delegate. The URL must not identify an existing file, because the movie file output does not overwrite existing resources. You must also have permission to write to the specified location. The delegate must conform to the [AVCaptureFileOutputRecordingDelegate](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate) protocol, and must implement the [captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate/1390612-fileoutput) method.

```
AVCaptureMovieFileOutput *aMovieFileOutput = <#Get a movie file output#>;
NSURL *fileURL = <#A file URL that identifies the output location#>;
[aMovieFileOutput startRecordingToOutputFileURL:fileURL recordingDelegate:<#The delegate#>];
```

In the implementation of [captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate/1390612-fileoutput), the delegate might write the resulting movie to the Camera Roll album. It should also check for any errors that might have occurred.

To determine whether the file was saved successfully, in the implementation of [captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate/1390612-fileoutput) you check not only the error but also the value of the [AVErrorRecordingSuccessfullyFinishedKey](https://developer.apple.com/documentation/avfoundation/averrorrecordingsuccessfullyfinishedkey) in the error’s user info dictionary:

```objc
- (void)captureOutput:(AVCaptureFileOutput *)captureOutput
        didFinishRecordingToOutputFileAtURL:(NSURL *)outputFileURL
        fromConnections:(NSArray *)connections
        error:(NSError *)error {

    BOOL recordedSuccessfully = YES;
    if ([error code] != noErr) {
        // A problem occurred: Find out if the recording was successful.
        id value = [[error userInfo] objectForKey:AVErrorRecordingSuccessfullyFinishedKey];
        if (value) {
            recordedSuccessfully = [value boolValue];
        }
    }
    // Continue as appropriate...
```

You should check the value of the [AVErrorRecordingSuccessfullyFinishedKey](https://developer.apple.com/documentation/avfoundation/averrorrecordingsuccessfullyfinishedkey)key in the user info dictionary of the error, because the file might have been saved successfully, even though you got an error. The error might indicate that one of your recording constraints was reached—for example, [AVErrorMaximumDurationReached](https://developer.apple.com/documentation/avfoundation/averror/averrormaximumdurationreached) or [AVErrorMaximumFileSizeReached](https://developer.apple.com/documentation/avfoundation/averror/averrormaximumfilesizereached). Other reasons the recording might stop are:

- The disk is full—[AVErrorDiskFull](https://developer.apple.com/documentation/avfoundation/averror/averrordiskfull)
- The recording device was disconnected—[AVErrorDeviceWasDisconnected](https://developer.apple.com/documentation/avfoundation/averror/averrordevicewasdisconnected)
- The session was interrupted (for example, a phone call was received)—[AVErrorSessionWasInterrupted](https://developer.apple.com/documentation/avfoundation/averror/averrorsessionwasinterrupted)

You can set metadata for the movie file at any time, even while recording. This is useful for situations where the information is not available when the recording starts, as may be the case with location information. Metadata for a file output is represented by an array of [AVMetadataItem](https://developer.apple.com/documentation/avfoundation/avmetadataitem) objects; you use an instance of its mutable subclass, [AVMutableMetadataItem](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem), to create metadata of your own.

```
AVCaptureMovieFileOutput *aMovieFileOutput = <#Get a movie file output#>;
NSArray *existingMetadataArray = aMovieFileOutput.metadata;
NSMutableArray *newMetadataArray = nil;
if (existingMetadataArray) {
    newMetadataArray = [existingMetadataArray mutableCopy];
}
else {
    newMetadataArray = [[NSMutableArray alloc] init];
}

AVMutableMetadataItem *item = [[AVMutableMetadataItem alloc] init];
item.keySpace = AVMetadataKeySpaceCommon;
item.key = AVMetadataCommonKeyLocation;

CLLocation *location - <#The location to set#>;
item.value = [NSString stringWithFormat:@"%+08.4lf%+09.4lf/"
    location.coordinate.latitude, location.coordinate.longitude];

[newMetadataArray addObject:item];

aMovieFileOutput.metadata = newMetadataArray;
```


An [AVCaptureVideoDataOutput](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput) object uses [delegation](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) to vend video frames. You set the delegate using [setSampleBufferDelegate:queue:](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1389008-setsamplebufferdelegate). In addition to setting the delegate, you specify a serial queue on which they delegate methods are invoked. You must use a serial queue to ensure that frames are delivered to the delegate in the proper order. You can use the queue to modify the priority given to delivering and processing the video frames. See _[SquareCam](../../../samplecode/SquareCam/SquareCam.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmjzga)_ for a sample implementation.

The frames are presented in the delegate method, [captureOutput:didOutputSampleBuffer:fromConnection:](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate/1385775-captureoutput), as instances of the [CMSampleBufferRef](https://developer.apple.com/documentation/coremedia/cmsamplebuffer) opaque type (see [Representations of Media](Time%20and%20Media%20Representations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcobyfvbuqmrnknltcnq)). By default, the buffers are emitted in the camera’s most efficient format. You can use the [videoSettings](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1389945-videosettings) property to specify a custom output format. The video settings property is a dictionary; currently, the only supported key is [kCVPixelBufferPixelFormatTypeKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferpixelformattypekey). The recommended pixel formats are returned by the [availableVideoCVPixelFormatTypes](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1387050-availablevideocvpixelformattypes) property , and the [availableVideoCodecTypes](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1389227-availablevideocodectypes) property returns the supported values. Both Core Graphics and OpenGL work well with the `BGRA` format:

```
AVCaptureVideoDataOutput *videoDataOutput = [AVCaptureVideoDataOutput new];
NSDictionary *newSettings =
                @{ (NSString *)kCVPixelBufferPixelFormatTypeKey : @(kCVPixelFormatType_32BGRA) };
videoDataOutput.videoSettings = newSettings;

 // discard if the data output queue is blocked (as we process the still image
[videoDataOutput setAlwaysDiscardsLateVideoFrames:YES];)

// create a serial dispatch queue used for the sample buffer delegate as well as when a still image is captured
// a serial dispatch queue must be used to guarantee that video frames will be delivered in order
// see the header doc for setSampleBufferDelegate:queue: for more information
videoDataOutputQueue = dispatch_queue_create("VideoDataOutputQueue", DISPATCH_QUEUE_SERIAL);
[videoDataOutput setSampleBufferDelegate:self queue:videoDataOutputQueue];

AVCaptureSession *captureSession = <#The Capture Session#>;

if ( [captureSession canAddOutput:videoDataOutput] )
     [captureSession addOutput:videoDataOutput];
```


You should set the session output to the lowest practical resolution for your application. Setting the output to a higher resolution than necessary wastes processing cycles and needlessly consumes power.

You must ensure that your implementation of [captureOutput:didOutputSampleBuffer:fromConnection:](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate/1385775-captureoutput) is able to process a sample buffer within the amount of time allotted to a frame. If it takes too long and you hold onto the video frames, AV Foundation stops delivering frames, not only to your delegate but also to other outputs such as a preview layer.

You can use the capture video data output’s [minFrameDuration](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1616296-minframeduration) property to be sure you have enough time to process a frame—at the cost of having a lower frame rate than would otherwise be the case. You might also make sure that the [alwaysDiscardsLateVideoFrames](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1385780-alwaysdiscardslatevideoframes) property is set to `YES` (the default). This ensures that any late video frames are dropped rather than handed to you for processing. Alternatively, if you are recording and it doesn’t matter if the output fames are a little late and you would _prefer_ to get all of them, you can set the property value to `NO`. This does not mean that frames will not be dropped (that is, frames may still be dropped), but that they may not be dropped as early, or as efficiently.

You use an [AVCaptureStillImageOutput](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput) output if you want to capture still images with accompanying metadata. The resolution of the image depends on the preset for the session, as well as the device.

Different devices support different image formats. You can find out what pixel and codec types are supported by a device using [availableImageDataCVPixelFormatTypes](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1388622-availableimagedatacvpixelformatt) and [availableImageDataCodecTypes](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1388312-availableimagedatacodectypes) respectively. Each method returns an array of the supported values for the specific device. You set the [outputSettings](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1389306-outputsettings) dictionary to specify the image format you want, for example:

```
AVCaptureStillImageOutput *stillImageOutput = [[AVCaptureStillImageOutput alloc] init];
NSDictionary *outputSettings = @{ AVVideoCodecKey : AVVideoCodecJPEG};
[stillImageOutput setOutputSettings:outputSettings];
```

If you want to capture a JPEG image, you should typically not specify your own compression format. Instead, you should let the still image output do the compression for you, since its compression is hardware-accelerated. If you need a data representation of the image, you can use [jpegStillImageNSDataRepresentation:](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1388131-jpegstillimagensdatarepresentati) to get an `NSData` object without recompressing the data, even if you modify the image’s metadata.

When you want to capture an image, you send the output a [captureStillImageAsynchronouslyFromConnection:completionHandler:](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1387374-capturestillimageasynchronouslyf) message. The first argument is the connection you want to use for the capture. You need to look for the connection whose input port is collecting video:

```
AVCaptureConnection *videoConnection = nil;
for (AVCaptureConnection *connection in stillImageOutput.connections) {
    for (AVCaptureInputPort *port in [connection inputPorts]) {
        if ([[port mediaType] isEqual:AVMediaTypeVideo] ) {
            videoConnection = connection;
            break;
        }
    }
    if (videoConnection) { break; }
}
```

The second argument to `captureStillImageAsynchronouslyFromConnection:completionHandler:` is a [block](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3) that takes two arguments: a `CMSampleBuffer` opaque type containing the image data, and an error. The sample buffer itself may contain metadata, such as an EXIF dictionary, as an attachment. You can modify the attachments if you want, but note the optimization for JPEG images discussed in [Pixel and Encoding Formats](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcobyfvbuqnjnknltgmi).

```
[stillImageOutput captureStillImageAsynchronouslyFromConnection:videoConnection completionHandler:
    ^(CMSampleBufferRef imageSampleBuffer, NSError *error) {
        CFDictionaryRef exifAttachments =
            CMGetAttachment(imageSampleBuffer, kCGImagePropertyExifDictionary, NULL);
        if (exifAttachments) {
            // Do something with the attachments.
        }
        // Continue as appropriate.
    }];
```


You can provide the user with a preview of what’s being recorded by the camera (using a preview layer) or by the microphone (by monitoring the audio channel).

You can provide the user with a preview of what’s being recorded using an [AVCaptureVideoPreviewLayer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer) object. `AVCaptureVideoPreviewLayer` is a subclass of[CALayer](https://developer.apple.com/documentation/quartzcore/calayer) (see _[Core Animation Programming Guide](../../Cocoa/Core%20Animation%20Programming%20Guide/About%20Core%20Animation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmju)_. You don’t need any outputs to show the preview.

Using the [AVCaptureVideoDataOutput](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput) class provides the client application with the ability to access the video pixels before they are presented to the user.

Unlike a capture output, a video preview layer maintains a strong reference to the session with which it is associated. This is to ensure that the session is not deallocated while the layer is attempting to display video. This is reflected in the way you initialize a preview layer:

```
AVCaptureSession *captureSession = <#Get a capture session#>;
CALayer *viewLayer = <#Get a layer from the view in which you want to present the preview#>;

AVCaptureVideoPreviewLayer *captureVideoPreviewLayer = [[AVCaptureVideoPreviewLayer alloc] initWithSession:captureSession];
[viewLayer addSublayer:captureVideoPreviewLayer];
```

In general, the preview layer behaves like any other `CALayer` object in the render tree (see _[Core Animation Programming Guide](../../Cocoa/Core%20Animation%20Programming%20Guide/About%20Core%20Animation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmju)_). You can scale the image and perform transformations, rotations, and so on just as you would any layer. One difference is that you may need to set the layer’s [orientation](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/1623494-orientation) property to specify how it should rotate images coming from the camera. In addition, you can test for device support for video mirroring by querying the [supportsVideoMirroring](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1387424-isvideomirroringsupported) property. You can set the [videoMirrored](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1389172-isvideomirrored) property as required, although when the [automaticallyAdjustsVideoMirroring](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1387082-automaticallyadjustsvideomirrori) property is set to `YES` (the default), the mirroring value is automatically set based on the configuration of the session.

The preview layer supports three gravity modes that you set using [videoGravity](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/1386708-videogravity):

- [AVLayerVideoGravityResizeAspect](https://developer.apple.com/documentation/avfoundation/avlayervideogravity/1387116-resizeaspect): This preserves the aspect ratio, leaving black bars where the video does not fill the available screen area.
- [AVLayerVideoGravityResizeAspectFill](https://developer.apple.com/documentation/avfoundation/avlayervideogravity/1385607-resizeaspectfill): This preserves the aspect ratio, but fills the available screen area, cropping the video when necessary.
- [AVLayerVideoGravityResize](https://developer.apple.com/documentation/avfoundation/avlayervideogravity/1387460-resize): This simply stretches the video to fill the available screen area, even if doing so distorts the image.

You need to take care when implementing tap-to-focus in conjunction with a preview layer. You must account for the preview orientation and gravity of the layer, and for the possibility that the preview may be mirrored. See the sample code project _[AVCam-iOS: Using AVFoundation to Capture Images and Movies](https://developer.apple.com/library/archive/samplecode/AVCam/Introduction/Intro.html#//apple_ref/doc/uid/DTS40010112)_ for an implementation of this functionality.

To monitor the average and peak power levels in an audio channel in a capture connection, you use an [AVCaptureAudioChannel](https://developer.apple.com/documentation/avfoundation/avcaptureaudiochannel) object. Audio levels are not key-value observable, so you must poll for updated levels as often as you want to update your user interface (for example, 10 times a second).

```
AVCaptureAudioDataOutput *audioDataOutput = <#Get the audio data output#>;
NSArray *connections = audioDataOutput.connections;
if ([connections count] > 0) {
    // There should be only one connection to an AVCaptureAudioDataOutput.
    AVCaptureConnection *connection = [connections objectAtIndex:0];

    NSArray *audioChannels = connection.audioChannels;

    for (AVCaptureAudioChannel *channel in audioChannels) {
        float avg = channel.averagePowerLevel;
        float peak = channel.peakHoldLevel;
        // Update the level meter user interface.
    }
}
```


This brief code example to illustrates how you can capture video and convert the frames you get to `UIImage` objects. It shows you how to:

- Create an [AVCaptureSession](https://developer.apple.com/documentation/avfoundation/avcapturesession) object to coordinate the flow of data from an AV input device to an output
- Find the [AVCaptureDevice](https://developer.apple.com/documentation/avfoundation/avcapturedevice) object for the input type you want
- Create an [AVCaptureDeviceInput](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput) object for the device
- Create an [AVCaptureVideoDataOutput](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput) object to produce video frames
- Implement a [delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) for the [AVCaptureVideoDataOutput](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput) object to process video frames
- Implement a function to convert the CMSampleBuffer received by the delegate into a `UIImage` object

You use an [AVCaptureSession](https://developer.apple.com/documentation/avfoundation/avcapturesession) object to coordinate the flow of data from an AV input device to an output. Create a session, and configure it to produce medium-resolution video frames.

```
AVCaptureSession *session = [[AVCaptureSession alloc] init];
session.sessionPreset = AVCaptureSessionPresetMedium;
```


Capture devices are represented by [AVCaptureDevice](https://developer.apple.com/documentation/avfoundation/avcapturedevice) objects; the class provides methods to retrieve an object for the input type you want. A device has one or more ports, configured using an [AVCaptureInput](https://developer.apple.com/documentation/avfoundation/avcaptureinput) object. Typically, you use the capture input in its default configuration.

Find a video capture device, then create a device input with the device and add it to the session. If an appropriate device can not be located, then the [deviceInputWithDevice:error:](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/1450880-deviceinputwithdevice) method will return an error by reference.

```
AVCaptureDevice *device =
        [AVCaptureDevice defaultDeviceWithMediaType:AVMediaTypeVideo];

NSError *error = nil;
AVCaptureDeviceInput *input =
        [AVCaptureDeviceInput deviceInputWithDevice:device error:&error];
if (!input) {
    // Handle the error appropriately.
}
[session addInput:input];
```


You use an [AVCaptureVideoDataOutput](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput) object to process uncompressed frames from the video being captured. You typically configure several aspects of an output. For video, for example, you can specify the pixel format using the [videoSettings](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1389945-videosettings) property and cap the frame rate by setting the [minFrameDuration](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1616296-minframeduration) property.

Create and configure an output for video data and add it to the session; cap the frame rate to 15 fps by setting the `minFrameDuration` property to 1/15 second:

```
AVCaptureVideoDataOutput *output = [[AVCaptureVideoDataOutput alloc] init];
[session addOutput:output];
output.videoSettings =
                @{ (NSString *)kCVPixelBufferPixelFormatTypeKey : @(kCVPixelFormatType_32BGRA) };
output.minFrameDuration = CMTimeMake(1, 15);
```

The data output object uses [delegation](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) to vend the video frames. The delegate must adopt the [AVCaptureVideoDataOutputSampleBufferDelegate](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate) protocol. When you set the data output’s delegate, you must also provide a queue on which callbacks should be invoked.

```
dispatch_queue_t queue = dispatch_queue_create("MyQueue", NULL);
[output setSampleBufferDelegate:self queue:queue];
dispatch_release(queue);
```

You use the queue to modify the priority given to delivering and processing the video frames.

In the delegate class, implement the method ([captureOutput:didOutputSampleBuffer:fromConnection:](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutputsamplebufferdelegate/1386039-captureoutput)) that is called when a sample buffer is written. The video data output object delivers frames as `CMSampleBuffer` opaque types, so you need to convert from the `CMSampleBuffer` opaque type to a `UIImage` object. The function for this operation is shown in [Converting CMSampleBuffer to a UIImage Object](Time%20and%20Media%20Representations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcobyfvbuqmrnknlti).

```objc
- (void)captureOutput:(AVCaptureOutput *)captureOutput
         didOutputSampleBuffer:(CMSampleBufferRef)sampleBuffer
         fromConnection:(AVCaptureConnection *)connection {

    UIImage *image = imageFromSampleBuffer(sampleBuffer);
    // Add your code here that uses the image.
}
```

Remember that the delegate method is invoked on the queue you specified in [setSampleBufferDelegate:queue:](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1389008-setsamplebufferdelegate); if you want to update the user interface, you must invoke any relevant code on the main thread.

After configuring the capture session, you should ensure that the camera has permission to record according to the user’s preferences.

```
NSString *mediaType = AVMediaTypeVideo;

[AVCaptureDevice requestAccessForMediaType:mediaType completionHandler:^(BOOL granted) {
    if (granted)
    {
        //Granted access to mediaType
        [self setDeviceAuthorized:YES];
    }
    else
    {
        //Not granted access to mediaType
        dispatch_async(dispatch_get_main_queue(), ^{
        [[[UIAlertView alloc] initWithTitle:@"AVCam!"
                                    message:@"AVCam doesn't have permission to use Camera, please change privacy settings"
                                   delegate:self
                          cancelButtonTitle:@"OK"
                          otherButtonTitles:nil] show];
                [self setDeviceAuthorized:NO];
        });
    }
}];
```

If the camera session is configured and the user has approved access to the camera (and if required, the microphone), send a [startRunning](https://developer.apple.com/documentation/avfoundation/avcapturesession/1388185-startrunning) message to start the recording.

```
[session startRunning];
```

To stop recording, you send the session a [stopRunning](https://developer.apple.com/documentation/avfoundation/avcapturesession/1385661-stoprunning) message.

iOS 7.0 introduces high frame rate video capture support (also referred to as “SloMo” video) on selected hardware. The full AVFoundation framework supports high frame rate content.

You determine the capture capabilities of a device using the [AVCaptureDeviceFormat](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format) class. This class has methods that return the supported media types, frame rates, field of view, maximum zoom factor, whether video stabilization is supported, and more.

- Capture supports full 720p (1280 x 720 pixels) resolution at 60 frames per second (fps) including video stabilization and droppable P-frames (a feature of H264 encoded movies, which allow the movies to play back smoothly even on slower and older hardware.)
- Playback has enhanced audio support for slow and fast playback, allowing the time pitch of the audio can be preserved at slower or faster speeds.
- Editing has full support for scaled edits in mutable compositions.
- Export provides two options when supporting 60 fps movies. The variable frame rate, slow or fast motion, can be preserved, or the movie and be converted to an arbitrary slower frame rate such as 30 frames per second.

The _SloPoke_ sample code demonstrates the AVFoundation support for fast video capture, determining whether hardware supports high frame rate video capture, playback using various rates and time pitch algorithms, and editing (including setting time scales for portions of a composition).

An instance of `AVPlayer` manages most of the playback speed automatically by setting the `setRate:` method value. The value is used as a multiplier for the playback speed. A value of 1.0 causes normal playback, 0.5 plays back at half speed, 5.0 plays back five times faster than normal, and so on.

The `AVPlayerItem` object supports the [audioTimePitchAlgorithm](https://developer.apple.com/documentation/avfoundation/avplayeritem/1385855-audiotimepitchalgorithm) property. This property allows you to specify how audio is played when the movie is played at various frame rates using the `Time Pitch Algorithm Settings` constants.

The following table shows the supported time pitch algorithms, the quality, whether the algorithm causes the audio to snap to specific frame rates, and the frame rate range that each algorithm supports.

| Time pitch algorithm | Quality | Snaps to specific frame rate | Rate range |
| --- | --- | --- | --- |
| [AVAudioTimePitchAlgorithmLowQualityZeroLatency](https://developer.apple.com/documentation/avfoundation/avaudiotimepitchalgorithmlowqualityzerolatency) | Low quality, suitable for fast-forward, rewind, or low quality voice. | `YES` | 0.5, 0.666667, 0.8, 1.0, 1.25, 1.5, 2.0 rates. |
| [AVAudioTimePitchAlgorithmTimeDomain](https://developer.apple.com/documentation/avfoundation/avaudiotimepitchalgorithm/1387220-timedomain) | Modest quality, less expensive computationally, suitable for voice. | `NO` | 0.5–2x rates. |
| [AVAudioTimePitchAlgorithmSpectral](https://developer.apple.com/documentation/avfoundation/avaudiotimepitchalgorithm/1388153-spectral) | Highest quality, most expensive computationally, preserves the pitch of the original item. | `NO` | 1/32–32 rates. |
| [AVAudioTimePitchAlgorithmVarispeed](https://developer.apple.com/documentation/avfoundation/avaudiotimepitchalgorithmvarispeed) | High-quality playback with no pitch correction. | `NO` | 1/32–32 rates. |

When editing, you use the `AVMutableComposition` class to build temporal edits.

- Create a new [AVMutableComposition](https://developer.apple.com/documentation/avfoundation/avmutablecomposition) instance using the [composition](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1495098-composition) class method.
- Insert your video asset using the [insertTimeRange:ofAsset:atTime:error:](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1385943-inserttimerange) method.
- Set the time scale of a portion of the composition using [scaleTimeRange:toDuration:](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1390549-scaletimerange)

Exporting 60 fps video uses the `AVAssetExportSession` class to export an asset. The content can be exported using two techniques:

- Use the [AVAssetExportPresetPassthrough](https://developer.apple.com/documentation/avfoundation/avassetexportpresetpassthrough) preset to avoid reencoding the movie. It retimes the media with the sections of the media tagged as section 60 fps, section slowed down, or section sped up.
- Use a constant frame rate export for maximum playback compatibility. Set the [frameDuration](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1388013-frameduration) property of the video composition to 30 fps. You can also specify the time pitch by using setting the export session’s [audioTimePitchAlgorithm](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1385835-audiotimepitchalgorithm) property.

You capture high frame rate video using the [AVCaptureMovieFileOutput](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput) class, which automatically supports high frame rate recording. It will automatically select the correct H264 pitch level and bit rate.

To do custom recording, you must use the [AVAssetWriter](https://developer.apple.com/documentation/avfoundation/avassetwriter) class, which requires some additional setup.

```
assetWriterInput.expectsMediaDataInRealTime=YES;
```

This setting ensures that the capture can keep up with the incoming data.

[Next](Export.md)[Previous](Editing.md)

