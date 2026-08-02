---
title: QuickTime - Rendering in Y'CbCr
apple_id: DTS40013083
resource_type: Technical Note
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2012-07-01'
source_url: https://developer.apple.com/library/archive/technotes/tn2307/_index.html
archived_at: '2026-07-26T19:54:10.589391Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2307

# QuickTime - Rendering in Y'CbCr

Originally published August 20th, 2000 as Ice Floe Dispatch 27, part of the "Letters from the Ice Floe" group of QuickTime engineering documents.

This note addresses improvements in performance and quality when rendering video (i.e., applying effects or processing the video) by using Y'CbCr color spaces as opposed to traditional use of RGB.

RGB is the native color space of QuickTime, so historically most video compressors and decompressors convert from their compressed format to and from RGB. However, many compression algorithms for video use an internal data format where the intensity (luma) and color (chroma) values are stored separately. Converting from these YUV color spaces to RGB on decompression and back on compression impacts performance and precision, and as well, can clip values that can be represented only in one of the two color spaces.

One of the most common formats of YUV color space used in the video domain is specified by Rec. ITU-R BT.601-4, often referred to as "Rec. 601.", which defines the Y'CbCr color space. This is the format used by standard television signals, and compressed material such as DV, MPEG or Motion-JPEG.

The range of the values in a channel for a Y'CbCr image is generally as follows:

```
Y': 16 to 235 recommended range.
        (Values 0 and 255 are reserved by Rec. 601 for synchronization
        purposes.)
Cb: -112 to +112, offset by 128, for a recommended range of 16 to 240
Cr: -112 to +112, offset by 128, for a recommended range of 16 to 240
```

However, note that the extremes of the coding range provide signal headroom (Poynton, p. 174). Also note that in some cases, cameras will generate values outside of the recommended range (DV camcorders generate out of range values particularly often). - more on this later.

Y'CbCr is most commonly referred to as having a 4:2:2 subsampling - this designation refers to the sampling rates of luma and chroma in the signal. It can also refer to the way the pixels are packed in a given pixel format. Note that a subsampled signal may be packed in a pixmap than can store more resolution. A signal subsampled at 4:1:1 (such as NTSC DV) could be stored in a 4:2:2 packed pixmap. Similarly, it might be stored in a 4:4:4 pixmap as well.

[Conversion Errors between Y'CbCr and RGB](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbygmwugsbrfvbu6tswivjfgskpjzpukussj5jfgx2civkforkfjzpvsx2dijbvex2bjzcf6ushii)[Aliasing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbygmwugsbrfvbu6tswivjfgskpjzpukussj5jfgx2civkforkfjzpvsx2dijbvex2bjzcf6ushiiwuctcjifjustsh)[Luma Clamping](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbygmwugsbrfvbu6tswivjfgskpjzpukussj5jfgx2civkforkfjzpvsx2dijbvex2bjzcf6ushiiwuyvknifpugtcbjviestsh)[Chroma Clamping](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbygmwugsbrfvbu6tswivjfgskpjzpukussj5jfgx2civkforkfjzpvsx2dijbvex2bjzcf6ushiiwugscsj5gucx2djrau2ucjjzdq)[Gamma Correction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbygmwugsbrfvbu6tswivjfgskpjzpukussj5jfgx2civkforkfjzpvsx2dijbvex2bjzcf6ushiiwuoqknjvav6q2pkjjekq2ujfhu4)[Preferred Y'CbCr pixel formats](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbygmwugsbrfvbu6tswivjfgskpjzpukussj5jfgx2civkforkfjzpvsx2dijbvex2bjzcf6ushiiwvausfizcveusfirpvsx2dijbvex2qjfmektc7izhvetkbkrjq)[Known Implementation Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbygmwugsbrfvfu4t2xjzpustkqjrcu2rkokraviskpjzpusu2tkvcvg)[References](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbygmwugsbrfvjekrsfkjcu4q2fkm)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbygmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Conversion Errors between Y'CbCr and RGB

### Aliasing

When converting between two different color spaces, even though the conversion process is designed to be symmetrical (repeated conversions cause no drift), aliasing occurs because the color spaces don't align for every pixel value. Therefore, there is an inherent loss converting from Y'CbCr to RGB and back.

### Luma Clamping

Computers define RGB black as 0 (per component) and white as 255. In order to maintain full black to white range in the RGB space, the color space conversion equations map the luma values that range from 16 to 235 to RGB values of 0 to 255 (C. Poynton, Eq. 9.11, pg. 177 or [Poynton Color FAQ](http://www.poynton.com/notes/colour_and_gamma/ColorFAQ.html)).

Normally this is appropriate, but there are times when the luma value in a source image can be higher than the 'recommended' maximum value of 235. This is especially true of many DV camcorders, which routinely generate luma values in the range 236-254. In these cases, all of the values over 235 will be mapped to 255 in RGB, which causes a change in the actual intensity value. This is commonly known as 'luma clamping'.

An example of this would be a white chair in the sunlight, where the DV camcorder's Y'CbCr values might be (Y'=250,Cb=128,Cr=128). Using [color space equations](http://www.poynton.com/PDFs/coloureq.pdf) to go to RGB, we get RGB values which are clamped to 255,255,255 (272,272,272 before clamping). When going back to Y'CbCr, the result would be (Y'=235,Cb=128,Cr=128), which would be noticeably darker than the original.

### Chroma Clamping

There are many Y'CbCr color values that map to RGB values greater than 255 or less than 0. This means that there are colors in YCbCr that cannot be represented in an RGB GWorld. These colors will be clamped to RGB values that are in the range 0-255, causing 'chroma clamping'.

An example of this would be a highly saturated color, such as (Y'=155,Cb=174,Cr=220). If this were mapped into RGB(255 [309 before clamping],69,255), and then back into Y'CbCr (Y'=141, Cb=182, Cr=196), a noticeable colorshift and darkening would be visible.

Both luma clamping and chroma clamping are due to the fact that the RGB color space is smaller than the Y'CbCr color space when using the formulas for converting between Y'CbCr and computer RGB.

### Gamma Correction

GWorlds on the Macintosh are traditionally represented as gamma 1.8 RGB buffers. Standard video systems are represented as having an effective gamma of 2.2. Codecs converting to and from RGB generally gamma correct to account for the different effective gammas. This conversion is a lossy process, however, so preserving the rendered buffers at gamma 2.2 is desired.

### Preferred Y'CbCr pixel formats

By processing the render buffers in Y'CbCr, the above aliasing and clamping problems are avoided, and additionally, since the compressed format is natively Y'CbCr, the expensive conversions to and from RGB can be avoided.

#### 2vuy

The pixel format '2vuy' (k2vuyPixelFormat) is the standard recommended format for interchange in the Y'CbCr domain. '2vuy' follows the Rec. 601 component ranges. It does have certain restrictions: '2vuy' is a 4:2:2 format, which means that a pair of luma values share the same chroma values. This has the advantage that storage is smaller, but it is difficult for video processing, since pixel pairs share the same chroma values, so the processing of each individual pixel is no longer independent. Additionally, the pixel format stores two luma for every chroma pair, so it isn't a good format if the data is not also subsampled (e.g., 4:2:2 or 4:1:1 would be good, 4:4:4 would be bad). This is recommended as a storage format.

#### 'v308' and 'v408'

These pixel formats (k444YpCbCr8CodecType and k4444YpCbCrA8CodecType) use the same color space as '2vuy', so they also have the same Y'CbCr advantages. However, they are both 4:4:4 sampling, so they are more appropriate for video processing. 'v408' is similar to 'v308' except that it has an additional Alpha channel, with the same range as the Y' component: "maximum alpha" corresponds to "white" in the Y channel, and is therefore at value 235; "minimum alpha" corresponds to "black" in the Y channel, and is therefore at value 16. These are recommended as storage formats as well.

#### 'r408'

Apple has defined a new pixel format, 'r408' (k4444YpCbCrA8RCodecType), which is friendly to applications that render in ARGB formats, but want to take advantage of the Y'CbCr color space. Its advantages over the other Y'CbCr color spaces are as follows:

- It is 4:4:4:4, which means that components are NOT shared across pixels.
- Alpha ranges from 0-255, the same range as in ARGB.
- It is packed AY'CbCr. This allows many image processing routines to be run unaltered on Y'CbCr data. This includes any image processing which does pixel sampling, and most algorithms which do not perform color specific processing.
- The luma value (Y') is biased so that black is 0, rather than 16. Recommended ranges for luma are therefore 0 to 219 rather than 16-235. The headroom above 235 is preserved, but the footroom is lost. This compromise is worth it because now operations on luma only can be done easily without having to offset the black point for each pixel. This is again for performance and for easier porting of existing ARGB rendering code.

'r408' is intended as a rendering format, not a storage format. Some additional notes: 1) When decompressing material to the 'r408' format, codecs are required to fill in the alpha channel during decompression, filling with 255 (opaque) if no specific value is available. 2) Compressors must clamp input 'r408' luma values, since the stored ranges may exceed the allowable Y'CbCr luma range (1-254). Following the mapping equations, 'r408' Y' values over 238 must be clamped. 3) The gamma of an 'r408' buffer is normally 2.2. Recommendations It is recommended that all codecs that operate on Y'CbCr data be updated to support 'r408' in order to allow applications to perform the most accurate image processing.

Some codecs may also want to support the 'v408' color space because 'v408' allows for the proper encoding of images with 'super-black' values (i.e. color bars). Codecs that support 'v408' will allow applications to generate a true pluge for their color bars.

Codec writers will want to add the new pixel formats to their 'wanted pixel format list', detect them in BeginBand and implement the proper storage in DrawBand. Codecs should also advertise the supported formats in the 'cpix' resource.

Applications will likely want to present user interfaces which allow selection of the desired 'white level' for graphics. "White" would equate to a Y' value of 235, and "Super White" would equate to a Y' value of 254. The application would use this information to determine whether to map an imported RGB graphic's RGB(255,255,255) into a Y'CbCr "white" (235 [or 219 in 'r408']) or "super white" (254 [or 238 in 'r408']).

Applications can determine the capabilities for compressing to and from Y'CbCr by querying the component for its 'cpix' resource and examining the contents for the desired fourCC.

[Back to Top](#)

## Known Implementation Issues

- The Apple software DV compressor shipped in QuickTime 4.1.2 does not clamp r408 luma values to 238.
- The Apple software DV compressor can gamma correct RGB input images to 2.2, but not Y'CbCr input images. No error is returned for Y'CbCr images which are not gamma 2.2

[Back to Top](#)

## References

- Poynton, Charles. A Technical Introduction to Digital Video, (John Wiley & Sons, New York, 1996).
- Poynton, Charles. [The Color FAQ](http://www.poynton.com/notes/colour_and_gamma/ColorFAQ.html)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-02-04 | New document that was originally published as Ice Floe Dispatch 27, "Letters from the Ice Floe" engineering documents. |

