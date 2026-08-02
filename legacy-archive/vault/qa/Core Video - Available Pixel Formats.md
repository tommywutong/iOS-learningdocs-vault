---
title: Core Video - Available Pixel Formats
apple_id: DTS10004198
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QuartzCore
published: '2010-05-26'
source_url: https://developer.apple.com/library/archive/qa/qa1501/_index.html
archived_at: '2026-07-18T02:31:39.609909Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1501

# Core Video - Available Pixel Formats

## Q:  What pixel formats does Core Video currently support, and is there an API that can be used to retrieve this information programatically?

A: What pixel formats does Core Video currently support, and is there an API that can be used to retrieve this information programatically?

A Core Video Pixel Buffer (represented by the opaque type `CVPixelBufferRef`) is an image buffer that holds pixels in main memory. Applications generating frames, compressing / decompressing video or using Core Image can all make use of Core Video Pixel Buffers.

Individual pixel buffers can be created and managed using APIs such as `CVPixelBufferCreate`, `CVPixelBufferCreateWithBytes`, `CVPixelBufferGetWidth,` `CVPixelBufferGetHeight` and so on (see `CVPixelBuffer.h`). A pool of pixel buffers can also be created for managing a set of `CVPixelBuffer` objects that are going to be recycled, for example, during a compression operation (see `CVPixelBufferPool.h`) and `CIImage` objects can be created from pixel buffers using methods such as `initWithCVImageBuffer:`.

At the time of this writing (Mac OS X 10.4.8 w/QuickTime 7.1.3), Core Video supports the pixel formats shown in Table 1. Note that new pixel formats may be added over time:

__Table 1__  Core Video supported pixel formats.

| Pixel Format | Description |
| k32ARGBPixelFormat | 32 - 8 bits per component Alpha, Red, Green, and Blue |
| k24RGBPixelFormat | 24 - 8 bits per component Red, Green, and Blue |
| k16BE555PixelFormat | 16 - MSB is unused, followed by 5 bits per component Red, Green and Blue |
| k32BGRAPixelFormat | BGRA - 8 bits per component Blue, Green, Red, and Alpha |
| k16GrayPixelFormat | b16g - 16-bit big-endian Grayscale |
| k32AlphaGrayPixelFormat | b32a - 16-bit big-endian AlphaGray |
| k64ARGBPixelFormat | b64a - 16 bits per component, big-endian Alpha, Red, Green and Blue |
| k48RGBPixelFormat | b48r - 16 bits per component big-endian Red, Green and Blue |
| k422YpCbCr8PixelFormat | 2vuy - Component Y'CbCr 8-bit 4:2:2 |
| kYUVSPixelFormat | yuvs - Component Y’CbCr 8-bit 4:2:2 |
| k444YpCbCr8CodecType | v308 - Component Y'CbCr 8-bit 4:4:4 |
| k422YpCbCr16CodecType | v216 - Component Y'CbCr 10,12,14,16-bit 4:2:2 |
| k422YpCbCr10CodecType | v210 - Component Y'CbCr 10-bit 4:2:2 |
| k4444YpCbCrA8RPixelFormat | r408 - Component Y'CbCrA 8-bit 4:4:4:4, rendering format, full range alpha, zero biased yuv |
| k4444YpCbCrA8PixelFormat | v408 - Component Y'CbCrA 8-bit 4:4:4:4 |
| k444YpCbCr10CodecType | v410 - Component Y'CbCr 10-bit 4:4:4 |
| 'r4fl' | r4fl - Component Y'CbCr 32-bit floating point 4:4:4:4, superblack support |

There are two APIs that can be used to dynamically retrieve all the pixel format OSTypes and Pixel Format Descriptions known to Core Video:

Use `CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes` to retrieve an array of OSTypes.


```
CFArrayRef CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes(CFAllocatorRef allocator)  Description:     Returns a CFArrayRef containing a list of all supported pixel format types.  allocator - The allocator used to allocate memory for the array and its storage for values.             Pass kCFAllocatorDefault to specify the default allocator.
```

Use `CVPixelFormatDescriptionCreateWithPixelFormatType` to retrieve a pixel format description dictionary.


```
CFDictionaryRef CVPixelFormatDescriptionCreateWithPixelFormatType(CFAllocatorRef allocator,                                                                   OSType pixelFormat)  Description:     Returns a CFDictionaryRef containing the pixel format description for the passed in pixel format type.  allocator - The allocator to use when creating the description. Pass kCFAllocatorDefault to specify the             default allocator.  pixelFormat - A four-character code that identifies the pixel format description you want to obtain.  Notes:     The returned Core Foundation dictionary contains the pixel format description. See “Pixel Format     Description Keys” for more detailed information regarding the keys relevant to the format description.  Pixel Format Description Dictionary Keys:  kCVPixelFormatName - The name of the pixel format (type CFString).  kCVPixelFormatConstant - The pixel format constant for QuickTime.  kCVPixelFormatCodecType - The codec type (type CFString). For example, '2vuy' or k422YpCbCr8CodecType.  kCVPixelFormatFourCC - The Microsoft FourCC equivalent code for this pixel format (type CFString).  kCVPixelFormatPlanes - The number of image planes associated with this format (type CFNumber).  kCVPixelFormatBlockWidth - The width, in pixels, of the smallest byte-addressable group of pixels                            (type CFNumber). Assumed to be 1 if this key is not present.  kCVPixelFormatBlockHeight - The height, in pixels, of the smallest byte-addressable group of pixels                             (type CFNumber). Assumed to be 1 if this key is not present.  kCVPixelFormatBitsPerBlock - The number of bits per block (type CFNumber). For simple pixel formats,                              this value is the same as the traditional bits-per-pixel value. This key is                              mandatory in pixel format descriptions.  kCVPixelFormatBlockHorizontalAlignment - The horizontal alignment requirements of this format                                           (type CFNumber). Assumed to be 1 if this key is not present.  kCVPixelFormatBlockVerticalAlignment - The vertical alignment requirements of this format (type CFNumber).                                        Assumed to be 1 if this key is not present.  kCVPixelFormatHorizontalSubsampling - Horizontal subsampling information for this plane                                       (type CFNumber). Assumed to be 1 if this key is not present.  kCVPixelFormatVerticalSubsampling - Vertical subsampling information for this plane                                     (type CFNumber). Assumed to be 1 if this key is not present.  kCVPixelFormatOpenGLFormat - The OpenGL format used to describe this image plane (if applicable)                              (type CFNumber). See the OpenGL specification for possible values.  kCVPixelFormatOpenGLType - The OpenGL type to describe this image plane (if applicable)                            (type CFNumber). See the OpenGL specification for possible values.  kCVPixelFormatOpenGLInternalFormat - The OpenGL internal format for this pixel format (if applicable).                                      (type CFNumber). See the OpenGL specification for possible values.  kCVPixelFormatCGBitmapInfo - The Core Graphics bitmap information for this pixel format (if applicable).  kCVPixelFormatQDCompatibility - Indicates whether this format is compatible with QuickDraw (type CFBoolean).  kCVPixelFormatCGBitmapContextCompatibility - Indicates whether this format is compatible with Core Graphics                                              bitmap contexts(type CFBoolean).  kCVPixelFormatCGImageCompatibility - Indicates whether this format is compatible with the CGImage type                                      (type CFBoolean).  kCVPixelFormatOpenGLCompatibility - Indicates whether this format is compatible with OpenGL (type CFBoolean).  kCVPixelFormatFillExtendedPixelsCallback - Specifies a custom extended pixel fill algorithm (type CFData).
```

Listing 1 demonstrates how to retrieve a list of supported Core Video pixel format types with the output produced shown in Listing 2.

__Listing 1__  Retrieving pixel format types known to Core Video.

```
{     CFArrayRef pixelFormatDescriptionsArray = NULL;     CFIndex i;      pixelFormatDescriptionsArray =     CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes(kCFAllocatorDefault);      printf("Core Video Supported Pixel Format Types:\n\n");      for (i = 0; i < CFArrayGetCount(pixelFormatDescriptionsArray); i++) {         CFStringRef pixelFormat = NULL;          CFNumberRef pixelFormatFourCC = (CFNumberRef)CFArrayGetValueAtIndex(pixelFormatDescriptionsArray, i);          if (pixelFormatFourCC != NULL) {             UInt32 value;              CFNumberGetValue(pixelFormatFourCC, kCFNumberSInt32Type, &value);              if (value <= 0x28) {                 pixelFormat = CFStringCreateWithFormat(kCFAllocatorDefault, NULL,                               CFSTR("Core Video Pixel Format Type: %d\n"), value);             } else {                 pixelFormat = CFStringCreateWithFormat(kCFAllocatorDefault, NULL,                               CFSTR("Core Video Pixel Format Type (FourCC):                               %c%c%c%c\n"), (char)(value >> 24), (char)(value >> 16),                               (char)(value >> 8), (char)value);             }              CFShow(pixelFormat);             CFRelease(pixelFormat);         }     } }
```


__Listing 2__  Output produced by Listing 1.

```
Core Video Pixel Format Type: 32 Core Video Pixel Format Type: 24 Core Video Pixel Format Type: 16 Core Video Pixel Format Type (FourCC): 2vuy Core Video Pixel Format Type (FourCC): yuvs Core Video Pixel Format Type (FourCC): r408 Core Video Pixel Format Type (FourCC): v408 Core Video Pixel Format Type (FourCC): BGRA Core Video Pixel Format Type (FourCC): b64a Core Video Pixel Format Type (FourCC): b48r Core Video Pixel Format Type (FourCC): b32a Core Video Pixel Format Type (FourCC): b16g Core Video Pixel Format Type (FourCC): v308 Core Video Pixel Format Type (FourCC): v216 Core Video Pixel Format Type (FourCC): v210 Core Video Pixel Format Type (FourCC): v410 Core Video Pixel Format Type (FourCC): r4fl
```

Listing 3 shows an example of the Pixel Format Description dictionary values returned by calling `CVPixelFormatDescriptionCreateWithPixelFormatType` for `k32ARGBPixelFormat` and Listing 4 shows the Pixel Format Description values returned for `k422YpCbCr8PixelFormat`.

__Listing 3__  Pixel Format Description values for k32ARGBPixelFormat.

```
kCVPixelFormatConstant - 32 kCVPixelFormatBitsPerBlock - 32 kCVPixelFormatQDCompatibility - true kCVPixelFormatCGBitmapContextCompatibility - true kCVPixelFormatCGImageCompatibility - true kCVPixelFormatCGBitmapInfo - kCGImageAlphaFirst | kCGBitmapByteOrder32Big kCVPixelFormatFillExtendedPixelsCallback - Extended fill procedure for this pixel format  Mac OS X:     kCVPixelFormatOpenGLFormat - GL_BGRA     kCVPixelFormatOpenGLInternalFormat - GL_RGBA8      PPC Based Mac (Big Endian):         kCVPixelFormatOpenGLCompatibility - true         kCVPixelFormatOpenGLType - GL_UNSIGNED_INT_8_8_8_8_REV      Intel Based Mac (Little Endian):         kCVPixelFormatOpenGLType - GL_UNSIGNED_INT_8_8_8_8
```


__Listing 4__  Pixel Format Description values for k422YpCbCr8PixelFormat.

```
kCVPixelFormatConstant - k422YpCbCr8PixelFormat kCVPixelFormatBlockWidth - 2 kCVPixelFormatBitsPerBlock - 32 kCVPixelFormatFillExtendedPixelsCallback - Extended fill procedure for this pixel format  Mac OS X:     kCVPixelFormatOpenGLCompatibility - true     kCVPixelFormatOpenGLFormat - GL_YCBCR_422_APPLE     kCVPixelFormatOpenGLInternalFormat - GL_RGB      PPC Based Mac (Big Endian):         kCVPixelFormatOpenGLType - GL_UNSIGNED_SHORT_8_8_REV_APPLE      Intel Based Mac (Little Endian):         kCVPixelFormatOpenGLType - GL_UNSIGNED_SHORT_8_8_APPLE  Windows (if Direct3D supports the format):     kCVPixelFormatDirect3DCompatibility - true     kCVPixelFormatDirect3DFormat - D3DFMT_UYVY     kCVPixelFormatDirect3DType - D3DFMT_UYVY     kCVPixelFormatDirect3DInternalFormat - D3DFMT_UYVY
```


- [QuickTime Pixel Format FourCCs](https://developer.apple.com/mac/library/technotes/tn2010/tn2273.html)
- [Pixel Format Description Keys](https://developer.apple.com/mac/library/documentation/GraphicsImaging/Reference/CoreVideoRef/Reference/reference.html#//apple_ref/doc/constant_group/Pixel_Format_Description_Keys)
- [Core Video Programming Guide](https://developer.apple.com/mac/library/documentation/GraphicsImaging/Conceptual/CoreVideo/CVProg_Intro/CVProg_Intro.html)
- [Core Video Reference](https://developer.apple.com/mac/library/documentation/GraphicsImaging/Reference/CoreVideoRef/Reference/reference.html)
- [Technical Q&A QA1443, 'Using QTPixelBufferContextCreate with NewMovieFromProperties'](https://developer.apple.com/qa/qa2005/qa1443.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-05-26 | Updated reference URLs. |
| 2007-01-23 | New document that discusses how to determine all the pixel format types and format descriptions known to Core Video. |

