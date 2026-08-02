---
title: Creating textures in the PVRTC compression format
apple_id: DTS40008044
resource_type: QA
platform: iOS
topic: null
technology: OpenGLES
published: '2009-07-14'
source_url: https://developer.apple.com/library/archive/qa/qa1611/_index.html
archived_at: '2026-07-18T02:32:42.162703Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1611

# Creating textures in the PVRTC compression format

## Q:  How do I create textures in the PVRTC compression format?

A: How do I create textures in the PVRTC compression format?

The iPhone SDK includes a tool that allows you to create textures in the PVRTC compression format, aptly named `texturetool`. If you have Xcode installed with the iPhone OS 2.2 SDK in the default location (`/Developer/Platforms/`), then `texturetool` is located at:  `/Developer/Platforms/iPhoneOS.platform/Developer/usr/bin/texturetool`.

`texturetool` allows you to create four variants of PVRTC data, the primary difference being tradeoffs between quality and size. You will have to experiment with these variants to determine which setting is the best compromise for each individual texture image.

The parameters that may be passed to `texturetool` and their function is presented in the rest of this document.

__Listing 1__  Encoding Options.

```
user$ texturetool -l  Encoders:  PVRTC  --channel-weighting-linear  --channel-weighting-perceptual  --bits-per-pixel-2  --bits-per-pixel-4  Formats:  Raw PVR
```

The `texturetool` will default to `--bits-per-pixel-4`, `--channel-weighting-linear`, and `-f` Raw if no other options are provided.

The `--bits-per-pixel-2` and `--bits-per-pixel-4` options create PVRTC data that encodes source pixels into 2 or 4 bits per pixel. These options represent a fixed 16:1 and 8:1 compression ratio over the uncompressed 32-bit RGBA image data. There is a minimum data size of 32 bytes; the compressor will never produce files smaller than this, and at least that many bytes are expected when uploading compressed texture data.

When compressing specifying `--channel-weighting-linear` will spread compression error equally across all channels. By contrast specifying `--channel-weighting-perceptual` attempts to reduce error in the green channel compared to the linear option. In general, PVRTC compression does better with photographic images than with line art.

The `-m` option allows you to automatically generate mipmap levels for the source image. This levels are provided as additional image data in the archive created. If you use the Raw image format, then each level of image data will be appended one after another to the archive. If you use the PVR archive format, then each mipmap image will be provided as a separate image in the archive.

With iPhone OS 2.2, the `texturetool` now additional supports a format (`-f`) parameter that allows you to control the format of its output file. While this parameter is not available with iPhone OS 2.1 or earlier, the data files produced are compatible with those versions if iPhone OS.

The default format is Raw, which is equivalent to the format that `texturetool` produced under iPhone SDK 2.0 and 2.1. This format is raw compressed texture data, either for a single texture level (without the `-m` option) or for each texture level concatenated together (with the `-m` option). Each texture level stored in the file will be at least 32 bytes in size, and must be uploaded to the GPU in its entirety.

The PVR format is the same format that the PVRTexTool from the Imagination Technologies PowerVR SDK produces, and requires parsing to obtain the actual texture data. See the [PVRTextureLoader](https://developer.apple.com/iphone/library/samplecode/PVRTextureLoader/index.html) sample for an example of working with texture data in this format.

- Height and Width must be a power of 2.
- Must be square (height==width).
- Source images must be in a format that Image IO accepts. This includes PNG, JPG, TIFF and others.

__Listing 2__  Encoding images into the PVRTC compression format.

```
Encode Image.png into PVRTC using linear weights and 4 bpp, and saving as ImageL4.pvrtc user$ texturetool -e PVRTC --channel-weighting-linear --bits-per-pixel-4 -o ImageL4.pvrtc Image.png  Encode Image.png into PVRTC using perceptual weights and 4 bpp, and saving as ImageP4.pvrtc user$ texturetool -e PVRTC --channel-weighting-perceptual --bits-per-pixel-4 -o ImageP4.pvrtc Image.png  Encode Image.png into PVRTC using linear weights and 2 bpp, and saving as ImageL2.pvrtc user$ texturetool -e PVRTC --channel-weighting-linear --bits-per-pixel-2 -o ImageL2.pvrtc Image.png  Encode Image.png into PVRTC using perceptual weights and 2 bpp, and saving as ImageP2.pvrtc user$ texturetool -e PVRTC --channel-weighting-perceptual --bits-per-pixel-2 -o ImageP2.pvrtc Image.png
```


__Listing 3__  Encoding images into the PVRTC compression format while creating a preview.

```
Encode Image.png into PVRTC using linear weights and 4 bpp, and saving the output as ImageL4.pvrtc and a PNG preview as ImageL4.png user$ texturetool -e PVRTC --channel-weighting-linear --bits-per-pixel-4 -o ImageL4.pvrtc -p ImageL4.png Image.png  Encode Image.png into PVRTC using perceptual weights and 4 bpp, and saving the output as ImageP4.pvrtc and a PNG preview as ImageP4.png user$ texturetool -e PVRTC --channel-weighting-perceptual --bits-per-pixel-4 -o ImageP4.pvrtc -p ImageP4.png Image.png  Encode Image.png into PVRTC using linear weights and 2 bpp, and saving the output as ImageL2.pvrtc and a PNG preview as ImageL2.png user$ texturetool -e PVRTC --channel-weighting-linear --bits-per-pixel-2 -o ImageL2.pvrtc -p ImageL2.png Image.png  Encode Image.png into PVRTC using perceptual weights and 2 bpp, and saving the output as ImageP2.pvrtc and a PNG preview as ImageP2.png user$ texturetool -e PVRTC --channel-weighting-perceptual --bits-per-pixel-2 -o ImageP2.pvrtc -p ImageP2.png Image.png
```

The sample images produced by these settings are shown below.

__Table 1__  Sample Images.

| 4bpp, Linear | Original | 4bpp, Perceptual |
|  |  |  |

__Table 2__  Sample Images.

| 2bpp, Linear | Original | 2bpp, Perceptual |
|  |  |  |

Listing 4 demonstrates how you can upload Raw PVRTC data to the GPU via the `texImage2DPVRTC` sample function. Typically on iPhone OS you would use NSBundle and NSData methods to load data from a file. For a complete example demonstrating how to upload texture data from a PVR formatted data file, see the [PVRTextureLoader](https://developer.apple.com/iphone/library/samplecode/PVRTextureLoader/index.html) sample.

__Listing 4__  Example of uploading PVRTC data to the graphics chip.

```
void texImage2DPVRTC(GLint level, GLsizei bpp, GLboolean hasAlpha, GLsizei width, GLsizei height, void *pvrtcData) {     GLenum format;     GLsizei size = width * height * bpp / 8;     if(hasAlpha) {         format = (bpp == 4) ? GL_COMPRESSED_RGBA_PVRTC_4BPPV1_IMG : GL_COMPRESSED_RGBA_PVRTC_2BPPV1_IMG;     } else {         format = (bpp == 4) ? GL_COMPRESSED_RGB_PVRTC_4BPPV1_IMG : GL_COMPRESSED_RGB_PVRTC_2BPPV1_IMG;     }     if(size < 32) {         size = 32;     }     glCompressedTexImage2D(GL_TEXTURE_2D, level, format, width, height, 0, size, data); }
```

For sample code see the [PVRTextureLoader](https://developer.apple.com/iphone/library/samplecode/PVRTextureLoader/index.html) sample.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-07-14 | Revised to point to the OpenGL ES Programming Guide. Please refer to that documentation for further updates. |
| 2009-01-27 | Clarified non-square texture support (it isn't supported). Linked to the PVRTextureLoader sample. |
| 2008-11-24 | Changes for iPhone SDK 2.2, which include the new location for the texturetool and new options for its use. |
| 2008-10-13 | New document that describes how to create textures in the PVRTC compression format. |

