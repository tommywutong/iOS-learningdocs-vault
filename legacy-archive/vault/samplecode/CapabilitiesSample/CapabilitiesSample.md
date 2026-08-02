---
title: CapabilitiesSample
apple_id: DTS10000652
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: ImageCaptureCore
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CapabilitiesSample/Introduction/Intro.html
archived_at: '2026-07-18T03:02:52.249593Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# CapabilitiesSample

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Shows how to detect Image Capture device capabilities and send messages to devices with ICAObjectSendMessage. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Mac OS X Mac OS 10.1 or better |

READ ME - Camera Capabilities sample code June 27, 2002 Image Capture devices may support a number of special features, such as the ability to delete an image on the camera, or the ability to capture a new image, and these features can be accessed via the Image Capture APIs using the ICAObjectSendMessage function. Simply specify the desired feature (message) in the messageType field of the ICAObjectSendMessagePB parameter block. A list of these messages can be found in the ICACamera.h interface file as follows: kICAMessageCameraCaptureNewImage = 'ccni', kICAMessageCameraDeleteOne = 'del1', kICAMessageCameraDeleteAll = 'dela', kICAMessageCameraSyncClock = 'sclk', kICAMessageCameraUploadData = 'load' To determine whether or not your device supports any of the above special features, you must obtain the camera dictionary for your device, and examine the camera capabilities in this dictionary. The camera dictionary can be gotten using the ICACopyObjectPropertyDictionary function. The camera capabilities can be retrieved from the camera dictionary using the 'capa' key. What is returned is an array containing all the device capabilities. If any of the above message ID values are listed in the camera capabilities they are supported by the device. USING THE APPLICATION Connect an Image Capture device to your Mac and launch the application (the application currently will not re-scan for devices after it is launched). In the window you'll see a list of supported capabilities for the device. Click on any of these, then press the "Issue Command" button to issue the command to the device via the ICAObjectSendMessage function. REQUIREMENTS Mac OS 10.1 or better Requirements: Mac OS 10.1 or better Keywords: Image Capture camera capabilities

[Next](main.m.md)

