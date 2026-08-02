---
title: QuickTime Pixel Format Four Character Codes (FourCCs)
apple_id: DTS40009994
resource_type: Technical Note
platform: macOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2010-05-22'
source_url: https://developer.apple.com/library/archive/technotes/tn2273/_index.html
archived_at: '2026-07-26T19:54:09.914660Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2273

# QuickTime Pixel Format Four Character Codes (FourCCs)

The intent of this document is to catalog and define the existing pixel format Four Character Codes (FourCCs). This document will be updated as new pixel formats are implemented.

Originally published as Ice Floe Dispatch 20, part of the "Letters from the Ice Floe" group of QuickTime engineering documents.

QuickTime identifies pixel format data using Four Character Codes, also referred to as "FourCCs".

To see the full list of registrations, or to register a new `FourCC`, please visit the [QuickTime Registration Authority.](http://qtra.apple.com/)

Accurate description of pixel data is necessary to ensure correct interchange and conversion of image data. A pixel format defines the memory/file layout of pixel data. The pixel format __does not__ define register layout of pixel data, as this differs from the memory/file layout depending on processor endian-ness.

[Macintosh Native FourCCs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsojzgqwugsbrfvjukq2ujfhu4mi)[Win32 Native FourCCs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsojzgqwugsbrfvjukq2ujfhu4mq)[YUV FourCCs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsojzgqwugsbrfvjukq2ujfhu4my)[Microsoft FourCCs recognized by QuickTime](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsojzgqwugsbrfvjukq2ujfhu4na)[Developer Specific FourCCs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsojzgqwugsbrfvjukq2ujfhu4ni)[Reference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsojzgqwugsbrfvjukq2ujfhu4nq)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsojzgqwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Macintosh Native FourCCs

__Table 1__

| Pixel Format | Description |
| k1MonochromePixelFormat 0x00000001 | The seminal one bit bitmap format is common to all platforms. Each bit represents a pixel, a value of one indicates black, a value of zero, white. The most significant bit (MSB) corresponds to the leftmost pixel. The least significant bit (LSB) corresponds to the rightmost pixel. |
| k2IndexedPixelFormat 0x00000002 | Each pixel is represented by two bits, which are used as an index into the associated Color Table. The two bit indexed format is native to the Mac platform. Although QTML does support 2 bit pixmaps on Win32, the format is not native to the Win32 platform. A byte of pixel data holds four pixels in the order 11223344 where 11 is the first pixel. |
| k4IndexedPixelFormat 0x00000004 | Each pixel is represented by four bits, which are used as an index into the associated Color Table. The four bit indexed format is native to both Mac and Win32 platforms. The pixel defined by the most significant four bits of a byte of pixel data come before the pixel defined by the least significant four bits. |
| k8IndexedPixelFormat 0x00000008 | Each pixel is represented by eight bits, which are used as an index into the associated Color Table. The eight bit indexed format is native to both Mac and Win32 platforms. |
| k16BE555PixelFormat 0x00000010 | Each pixel is represented by 16 bits. The MSB is unused, followed by five bits per each Red, Green and Blue component. This is the native 16 bit format for the Mac platform. |
| k24RGBPixelFormat 0x00000018 | Each pixel is represented by 24 bits. Eight bits per each Red, Green, and Blue component. This is the native 24 bit format for the Mac platform. |
| k32ARGBPixelFormat 0x00000020 | Each pixel is represented by 32 bits. Eight bits per each Alpha, Red, Green, and Blue component. This is the native 32 bit format for the Mac platform. |
| k1IndexedGrayPixelFormat 0x00000021 | Each bit represents a pixel, which is used as an index into the associated gray Color Table. This is a legacy gray indexed format from the Mac platform. |
| k2IndexedGrayPixelFormat 0x00000022 | Each pixel is represented by two bits, which is used as an index into the associated 2-bit gray Color Table. This is a legacy gray indexed format from the Mac platform. |
| k4IndexedGrayPixelFormat 0x00000024 | Each pixel is represented by four bits, which is used as an index into the associated 4-bit gray Color Table. This is a legacy gray indexed format from the Mac platform. |
| k8IndexedGrayPixelFormat 0x00000028 | Each pixel is represented by eight bits, which is used as an index into the associated 8-bit gray Color Table. This is a legacy gray indexed format from the Mac platform. |

[Back to Top](#)

## Win32 Native FourCCs

__Table 2__

| Pixel Format | Description |
| k16LE555PixelFormat 'L555' | Identical to k16BE555PixelFormat except the 16 bit word is byte swapped. This is a native 16 bit format for the Win32 platform. |
| k16BE565PixelFormat 'B565' | Each pixel is represented by 16 bits. Five bits per Red, 6 bits per Green, and 5 bits per Blue component. This format is not commonly used, being defined primarily for completeness. |
| k16LE565PixelFormat 'L565' | Identical to k16BE565PixelFormat except the 16 bit word is byte swapped. This is a native 16 bit format for the Win32 platform. |
| k16LE5551PixelFormat '5551' | Each pixel is represented by 16 bits. Five bits per each Red, Green and Blue component, followed by an Alpha bit. The 16 bit word is byte swapped. This is the native 16 bit format for SGI’s Win32 platforms. |
| k24BGRPixelFormat '24BG' | Each pixel is represented by 24 bits. Eight bits per each Blue, Red, and Green component. This is the native 24 bit format for the Win32 platform. |
| k32BGRAPixelFormat 'BGRA' | Each pixel is represented by 32 bits. Eight bits per each Blue, Green, Red, and Alpha component. This is the native 32 bit format for the Win32 platform. |
| k32ABGRPixelFormat 'ABGR' | Each pixel is represented by 32 bits. Eight bits per each Alpha, Blue, Green, and Red component. |
| k32RGBAPixelFormat 'RGBA' | Each pixel is represented by 32 bits. Eight bits per each Red, Green, Blue, and Alpha component. |

[Back to Top](#)

## YUV FourCCs

__Table 3__

| Pixel Format | Description |
| k2vuyPixelFormat '2vuy' | 8-bit 4:2:2 Component Y’CbCr format. Each 16 bit pixel is represented by an unsigned eight bit luminance component and two unsigned eight bit chroma components. Each pair of pixels shares a common set of chroma values. The components are ordered in memory; Cb, Y0, Cr, Y1. The luminance components have a range of [16, 235], while the chroma value has a range of [16, 240]. This is consistent with the CCIR601 spec. This format is fairly prevalent on both Mac and Win32 platforms. The equivalent Microsoft fourCC is ‘UYVY’. |
| kYUVSPixelFormat 'yuvs' | 8-bit 4:2:2 Component Y’CbCr format. Identical to the k2vuyPixelFormat except each 16 bit word has been byte swapped. This results in a component ordering of; Y0, Cb, Y1, Cr. This is most prevalent yuv 4:2:2 format on both Mac and Win32 platforms. The equivalent Microsoft fourCC is ‘YUY2’. |
| kYVYU422PixelFormat 'YVYU' | 8-bit 4:2:2 Component Y’CbCr format. Identical to the k2vuyPixelFormat except the 32 bit word has been byte swapped. This results in a component ordering of; Y1, Cr, Y0, Cb. This is not a common format. The equivalent Microsoft fourCC is 'YVYU'. Currently, there is no codec support but the fourCC is reserved for future compability. |
| kYUVUPixelFormat 'yuvu' | 8-bit 4:2:2 Component Y’CbCr format. Each 16 bit pixel is represented by an unsigned eight bit luminance component and two two’s complement signed eight bit chroma components. Each pair of pixels shares a common set of chroma values. The components are ordered in memory; Y0, Cb, Y1, Cr. The luminance components have a range of [0, 255], the chroma values have a range of [-127, +127]. This format is equivalent to the ‘yuv2’ file format. |
| kYVU9PixelFormat 'YVU9' | A yuv planar format consisting of an 8-bit per pixel Y plane followed by 8-bit per pixel 4x4 subsampled V and U planes. |
| 'IF09' | An Intel define yuv planar format similar to 'YVU9' (above) followed by a plane of frame relative data. |
| 'v308' | 8-bit 4:4:4 Component Y’CbCr format. See the "Uncompressed Y´CbCr Video in QuickTime Files" document for more information. |
| 'v408' | 8-bit 4:4:4:4 Component Y’CrCbA format. See the "Uncompressed Y´CbCr Video in QuickTime Files" document for more information. |
| 'v216' | 10, 12, 14, 16-bit 4:2:2 Component Y’CbCr format. See the "Uncompressed Y´CbCr Video in QuickTime Files" document for more information. |
| 'v410' | 10-bit 4:4:4 Component Y’CbCr format. See the "Uncompressed Y´CbCr Video in QuickTime Files" document for more information. |
| kYUVXPixelFormat 'yuvx' | This is a private yuv pixel format used internally by QuickTime. Do not use this format. It is documented here solely for the purposes of completeness. |
| 'myuv' | This is a private yuv pixel format used internally by QuickTime. Do not use this format. It is documented here solely for the purposes of completeness. |
| 'syv9' | This is a private yuv pixel format used internally by QuickTime. Do not use this format. It is documented here solely for the purposes of completeness. |

[Back to Top](#)

## Microsoft FourCCs recognized by QuickTime

__Table 4__

| Pixel Format | Description |
| 'Y411' | Currently, there is no codec support but the fourCC is reserved for future compatibility. |
| 'Y211' | Currently, there is no codec support but the fourCC is reserved for future compatibility. |
| 'YV12' | Currently, there is no codec support but the fourCC is reserved for future compatibility. |

[Back to Top](#)

## Developer Specific FourCCs

__Table 5__

| Pixel Format | Description |
| 'soft' | Intermediary pixel format used by the SoftVout and SoftCodec sample code project. |
| 'vwgr' | Intermediary pixel format used by View Graphics. |
| 'SGVC' | Intermediary pixel format used by SGI. |

[Back to Top](#)

## Reference

[Uncompressed Y´CbCr Video in QuickTime Files](https://developer.apple.com/quicktime/icefloe/dispatch019.html)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-05-22 | New document that catalogs and defines the existing pixel format FourCCs. |

