---
title: macOS 10.12.1 API Diffs
apple_id: TP40017565
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12_1/Swift/Accelerate.html
archived_at: '2026-07-18T02:51:44.059737Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12.1 API Diffs](macOS%2010.12%20to%20macOS%2010.12.1%20API%20Differences.md)


# Accelerate Changes for Swift

### Accelerate

Modified [vImageCreateCGImageFromBuffer(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_CGImageFormat>, _: ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!, _: vImage_Flags, _: UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<CGImage>!](https://developer.apple.com/documentation/accelerate/1399036-vimagecreatecgimagefrombuffer)

|  | Declaration |
| --- | --- |
| From | ``` func vImageCreateCGImageFromBuffer(_ buf: UnsafePointer<vImage_Buffer>, _ format: UnsafePointer<vImage_CGImageFormat>, _ callback: (@escaping (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)!, _ userData: UnsafeMutableRawPointer!, _ flags: vImage_Flags, _ error: UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<CGImage>! ``` |
| To | ``` func vImageCreateCGImageFromBuffer(_ buf: UnsafePointer<vImage_Buffer>, _ format: UnsafePointer<vImage_CGImageFormat>, _ callback: ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)!, _ userData: UnsafeMutableRawPointer!, _ flags: vImage_Flags, _ error: UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<CGImage>! ``` |

Modified [vImageCVImageFormat_SetUserData(_: vImageCVImageFormat, _: UnsafeMutableRawPointer!, _: ((vImageCVImageFormat?, UnsafeMutableRawPointer?) -> Swift.Void)!) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1498220-vimagecvimageformat_setuserdata)

|  | Declaration |
| --- | --- |
| From | ``` func vImageCVImageFormat_SetUserData(_ format: vImageCVImageFormat, _ userData: UnsafeMutableRawPointer!, _ userDataReleaseCallback: (@escaping (vImageCVImageFormat?, UnsafeMutableRawPointer?) -> Swift.Void)!) -> vImage_Error ``` |
| To | ``` func vImageCVImageFormat_SetUserData(_ format: vImageCVImageFormat, _ userData: UnsafeMutableRawPointer!, _ userDataReleaseCallback: ((vImageCVImageFormat?, UnsafeMutableRawPointer?) -> Swift.Void)!) -> vImage_Error ``` |

Modified [vImageGetResamplingFilterSize(_: Float, _: ((UnsafePointer<Float>?, UnsafeMutablePointer<Float>?, UInt, UnsafeMutableRawPointer?) -> Swift.Void)!, _: Float, _: vImage_Flags) -> Int](https://developer.apple.com/documentation/accelerate/1509252-vimagegetresamplingfiltersize)

|  | Declaration |
| --- | --- |
| From | ``` func vImageGetResamplingFilterSize(_ scale: Float, _ kernelFunc: (@escaping (UnsafePointer<Float>?, UnsafeMutablePointer<Float>?, UInt, UnsafeMutableRawPointer?) -> Swift.Void)!, _ kernelWidth: Float, _ flags: vImage_Flags) -> Int ``` |
| To | ``` func vImageGetResamplingFilterSize(_ scale: Float, _ kernelFunc: ((UnsafePointer<Float>?, UnsafeMutablePointer<Float>?, UInt, UnsafeMutableRawPointer?) -> Swift.Void)!, _ kernelWidth: Float, _ flags: vImage_Flags) -> Int ``` |

Modified [vImageNewResamplingFilterForFunctionUsingBuffer(_: ResamplingFilter, _: Float, _: ((UnsafePointer<Float>?, UnsafeMutablePointer<Float>?, UInt, UnsafeMutableRawPointer?) -> Swift.Void)!, _: Float, _: UnsafeMutableRawPointer!, _: vImage_Flags) -> vImage_Error](https://developer.apple.com/documentation/accelerate/1509217-vimagenewresamplingfilterforfunc)

|  | Declaration |
| --- | --- |
| From | ``` func vImageNewResamplingFilterForFunctionUsingBuffer(_ filter: ResamplingFilter, _ scale: Float, _ kernelFunc: (@escaping (UnsafePointer<Float>?, UnsafeMutablePointer<Float>?, UInt, UnsafeMutableRawPointer?) -> Swift.Void)!, _ kernelWidth: Float, _ userData: UnsafeMutableRawPointer!, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageNewResamplingFilterForFunctionUsingBuffer(_ filter: ResamplingFilter, _ scale: Float, _ kernelFunc: ((UnsafePointer<Float>?, UnsafeMutablePointer<Float>?, UInt, UnsafeMutableRawPointer?) -> Swift.Void)!, _ kernelWidth: Float, _ userData: UnsafeMutableRawPointer!, _ flags: vImage_Flags) -> vImage_Error ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
