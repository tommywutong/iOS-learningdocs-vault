---
title: Creating auxiliary depth data manually
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/creating-auxiliary-depth-data-manually
source_url: 'https://developer.apple.com/documentation/avfoundation/creating-auxiliary-depth-data-manually'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/creating-auxiliary-depth-data-manually.json'
content_hash: 'sha256:2bb2a815bdafa700'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Additional data capture](additional-data-capture.md)

# Creating auxiliary depth data manually

<sub>Article</sub>

Generate a depth image and attach it to your own image.

## Overview

iOS Portrait Mode generates a depth map and attaches it to the image as auxiliary metadata, but for custom effects, you can generate your own auxiliary depth image, one not taken with iOS Portrait Mode or another depth-enabled capture device. This article shows you how to generate this map and attach it to your image.

### Convert pixel values into a compatible floating-point format

The depth image is a single-component image that must be converted per-pixel from grayscale pixel values (`0` = black to `1` = white, zNear to zFar) to either depth (in meters) or disparity (in 1/meters). Then adjust these values to fit your desired floating-point format.

The supported pixel formats for disparity or depth images are:

- `kCVPixelFormatType_DisparityFloat16 = 'hdis'`: An IEEE754-2008 binary16 (half float), describing the normalized shift when comparing two images. Units are 1/meters: (pixelShift / (pixelFocalLength * baselineInMeters))
- `kCVPixelFormatType_DisparityFloat32 = 'fdis'`: An IEEE754-2008 binary32 float, describing the normalized shift when comparing two images. Units are 1/meters: (pixelShift / (pixelFocalLength * baselineInMeters))
- `kCVPixelFormatType_DepthFloat16 = 'hdep'`: An IEEE754-2008 binary16 (half float), describing the depth (distance to an object) in meters
- `kCVPixelFormatType_DepthFloat32 = 'fdep'`: An IEEE754-2008 binary32 float, describing the depth (distance to an object) in meters

Load the grayscale image into a [CVPixelBuffer](../corevideo/cvpixelbuffer-q2e.md). Load its base address, attained via [CVPixelBufferLockBaseAddress(_:_:)](<../corevideo/cvpixelbufferlockbaseaddress(____).md>), as data ([CFData](../corefoundation/cfdata.md)) and pass it as the [kCGImageAuxiliaryDataInfoData](../imageio/kcgimageauxiliarydatainfodata.md) value into a dictionary ([CFDictionary](../corefoundation/cfdictionary.md)).

### Parse metadata dictionaries

The format of the dictionary is documented in `CGImageSource.h`. Access this dictionary with [CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)](<../imageio/cgimagesourcecopyauxiliarydatainfoatindex(______).md>). The dictionary supports JPEG, HEIF, and DNG images. The [CFDictionary](../corefoundation/cfdictionary.md) contains auxiliary data in the following format:

- [kCGImageAuxiliaryDataInfoData](../imageio/kcgimageauxiliarydatainfodata.md) → Depth data ([CFData](../corefoundation/cfdata.md))
- [kCGImageAuxiliaryDataInfoDataDescription](../imageio/kcgimageauxiliarydatainfodatadescription.md) → Depth data description ([CFDictionary](../corefoundation/cfdictionary.md): See below for more details.)
- [kCGImageAuxiliaryDataInfoMetadata](../imageio/kcgimageauxiliarydatainfometadata.md) → Optional metadata ([CGImageMetadata](../imageio/cgimagemetadata.md))

[CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)](<../imageio/cgimagesourcecopyauxiliarydatainfoatindex(______).md>) returns `nil` if the image doesn’t contain `auxiliaryImageDataType` data.

The value for key [kCGImageAuxiliaryDataInfoDataDescription](../imageio/kcgimageauxiliarydatainfodatadescription.md) is a [CFDictionary](../corefoundation/cfdictionary.md) that you populate to tell the image system how to interpret the depth map. It can contain the following depth data parameters:

- [kCGImagePropertyPixelFormat](../imageio/kcgimagepropertypixelformat.md) → One of the Core Video `CVPixelBuffer.h` depth or disparity formats
- [kCGImagePropertyWidth](../imageio/kcgimagepropertywidth.md) and [kCGImagePropertyHeight](../imageio/kcgimagepropertyheight.md) → Pixel dimensions
- [kCGImagePropertyBytesPerRow](../imageio/kcgimagepropertybytesperrow.md) → The number of bytes per row in the depth map

### Attach your custom depth map to an image

Attach the depth or disparity dictionary to an image as follows:

1. Create [AVDepthData](avdepthdata.md) with [+ depthDataFromDictionaryRepresentation:error:](<avdepthdata/init(fromdictionaryrepresentation_).md>), passing in the depth or disparity dictionary.
2. Create the image destination.
3. Create the image, using helper methods from [Image I/O](../imageio.md).

```swift
// Add an image to the destination.
CGImageDestinationAddImage(cgImageDestination, renderedCGImage, attachments)  

// Use AVDepthData to get the auxiliary data dictionary.         
var auxDataType :NSString? 
let auxData = depthData.dictionaryRepresentation(forAuxiliaryDataType: &auxDataType)  

// Add auxiliary data to the image destination. 
CGImageDestinationAddAuxiliaryDataInfo(cgImageDestination, auxDataType!, auxData! as CFDictionary)  

if CGImageDestinationFinalize(cgImageDestination) {  
	return data as Data
}  
```

## See Also

### Depth data capture

- [Capturing photos with depth](capturing-photos-with-depth.md) — Get a depth map with a photo to create effects like the system camera’s Portrait mode (on compatible devices).
- [Capturing depth using the LiDAR camera](capturing-depth-using-the-lidar-camera.md) — Access the LiDAR camera on supporting devices to capture precise depth data.
- [AVCamFilter: Applying filters to a capture stream](avcamfilter-applying-filters-to-a-capture-stream.md) — Render a capture stream with rose-colored filtering and depth effects.
- [Streaming depth data from the TrueDepth camera](streaming-depth-data-from-the-truedepth-camera.md) — Visualize depth data in 2D and 3D from the TrueDepth camera.
- [Enhancing live video by leveraging TrueDepth camera data](enhancing-live-video-by-leveraging-truedepth-camera-data.md) — Apply your own background to a live capture feed streamed from the front-facing TrueDepth camera.
- [AVCaptureDepthDataOutput](avcapturedepthdataoutput.md) — A capture output that records scene depth information on compatible camera devices.
- [AVDepthData](avdepthdata.md) — A container for per-pixel distance or disparity information captured by compatible camera devices.
- [AVCameraCalibrationData](avcameracalibrationdata.md) — Information about the camera characteristics used to capture images and depth data.
