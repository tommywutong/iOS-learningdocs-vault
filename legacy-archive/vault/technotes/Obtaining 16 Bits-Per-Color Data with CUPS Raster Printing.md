---
title: Obtaining 16 Bits-Per-Color Data with CUPS Raster Printing
apple_id: DTS10003771
resource_type: Technical Note
platform: macOS
topic: Graphics & Animation
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/technotes/tn2149/_index.html
archived_at: '2026-07-26T19:54:08.549171Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



# Retired Document

__Important:__
Retired Document: This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Technical Note TN2149

# Obtaining 16 Bits-Per-Color Data with CUPS Raster Printing

In Mac OS X version 10.2 (Jaguar), Apple deployed the CUPS printing system as the backbone of its printing support on Mac OS X. CUPS offers a straightforward programming model for writing printer drivers to support raster output devices. The implementation of CUPS in Jaguar offered support for a number of CUPS color spaces, including RGB, Gray, Black , and CMYK. In Jaguar and in Mac OS X version 10.3 (Panther), the supported pixel depths available were either 1 bit- or 8 bits-per-color component (`cupsBitsPerColor` values), depending on the color space requested. [Technical Q&A 1368](https://developer.apple.com/qa/qa2004/qa1368.html) contains a table of the color spaces and bit depths supported by the CUPS implementation in each version of Mac OS X.

Starting with Mac OS X version 10.4 (Tiger), developers writing raster printer drivers for the CUPS printing system can receive bitmap raster data with 16 bits-per-color component. Working with deeper pixel data offers the opportunity for greater color fidelity and precision. The support for 16 bits-per-color is limited to the CUPS color spaces `CUPS_CSPACE_K`, `CUPS_CSPACE_W`, `CUPS_CSPACE_RGB`, and `CUPS_CSPACE_CMYK`, with the `cupsColorOrder` value `CUPS_ORDER_CHUNKED`.

[Byte Ordering (Endian-ness)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzxgewugsbrfvjukq2ujfhu4mi)[Requesting 16 Bits-Per-Color Data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzxgewugsbrfvjukq2ujfhu4mq)[Mac OS X 10.4 and Later Systems Only](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzxgewugsbrfvjvkqstivbviskpjyza)[Compatibility with Other Systems](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzxgewugsbrfvjvkqstivbviskpjyzq)[Summary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzxgewugsbrfvjukq2ujfhu4ni)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzxgewvezlwnfzws33ojbuxg5dpoj4s2u2xge)

## Byte Ordering (Endian-ness)

For raster data that is 1 bit and 8 bits-per-color component, the byte ordering of the data for a given color component is unambiguous because the color component data for each pixel is one byte or less in size. For 16 bits-per-color data, the color value for a given color component is 2 bytes and the byte ordering is defined to be the native byte ordering. That is, for 16 bits-per-color data when executing on big-endian machines, the byte order of each color component value is big-endian. For 16 bits-per-color data when executing on little-endian machines, the byte order of each color component value is little-endian. This approach offers the best performance and most straightforward treatment of the data passed to a CUPS filter expecting to receive 16 bits-per-color CUPS raster data. However, this means that your CUPS filter that processes 16 bits-per-color data must determine whether the architecture of the producer of the raster data matches your filter's architecture.

CUPS provides a straightforward way to determine whether the architecture of the producer of the raster data is the same as your filter which will process the raster. The `cupsRasterOpen` function returns a `cups_raster_t` structure containing a `sync` field that you use for this determination. The code for this test looks like that in Listing 1.

__Listing 1__  Determining if endian data swapping is needed

```
bool isRasterEndianSwapNeeded(int in_fd) {     bool swap16BitData = false;     cups_raster_t *raster;     // in_fd is the input file descriptor for the file     // you are reading the raster from, e.g. stdin.     raster = cupsRasterOpen(in_fd, CUPS_RASTER_READ);     if(raster->sync == CUPS_RASTER_REVSYNC)         swap16BitData = true;     return swap16BitData; }
```

When the `sync` field in the `cups_raster_t` returned from `cupsRasterOpen` is equal to `CUPS_RASTER_REVSYNC`, the architecture of the filter that produced the raster data and the architecture of your filter differ and you need to swap the 16-bit integer data your filter is obtaining.

[Back to Top](#)

## Requesting 16 Bits-Per-Color Data

There are two methods that developers can use to specify that they want 16 bits-per-color data. Which method is best depends on whether the driver receiving the data is intended to run on versions prior to Tiger.

### Mac OS X 10.4 and Later Systems Only

If you want to receive 16 bits-per-color raster data and only care about having your driver run on systems that support that format, you can simply specify a `cupsBitsPerColor` value of 16. The typical way of doing this is in the invocation code for the `*ColorModel` keyword in the PPD file. For example, if you were already requesting 8 bits-per-color component, your PPD file might have a line such as the one shown in Listing 2.

__Listing 2__  Specifying in a PPD file a cupsBitsPerColor value of 8

```
*ColorModel RGB/RGB Color: "<</cupsColorSpace 1/cupsColorOrder 0/cupsBitsPerColor 8>>setpagedevice"
```

This specifies the `CUPS_CSPACE_RGB` color space, with chunky pixels, with 8 bits-per-color component, that is color data in the format:

`RGBRGBRGB...`

with each color value in a single byte.

To specify the same parameters but with 16 bits-per-color, you would change the equivalent line in the PPD file to instead read as shown in Listing 3.

__Listing 3__  Specifying in a PPD file a cupsBitsPerColor value of 16

```
*ColorModel RGB/RGB Color: "<</cupsColorSpace 1/cupsColorOrder 0/cupsBitsPerColor 16>>setpagedevice"
```

This specifies the `CUPS_CSPACE_RGB` color space, with chunky pixels, with 16 bits-per-color component, that is color data in the format:

`RGBRGBRGB...`

with each color value specified as a 2-byte integer value in host-endian format.

This approach is straightforward but will fail when executing on any version of Mac OS X prior to Tiger or any other CUPS print server that does not support a `cupsBitsPerColor` value of 16.

### Compatibility with Other Systems

CUPS raster printer drivers that use `cupsBitsPerColor` with a value of 16 will fail on Mac OS X versions prior to Tiger because those versions do not support that color depth. Similarly, CUPS print servers on most other systems do not support a `cupsBitsPerColor` value of 16. For this reason, developers that want to be compatible with these other systems will want to use another approach.

The `cupsPreferredBitsPerColor` key was introduced to allow a driver to specify that it prefers 16 bits-per-color component data. This key is ignored by CUPS systems that do not support it. A typical use of this key is in the invocation code for the \*ColorModel keyword in the PPD file as shown in Listing 4.

__Listing 4__  Specifying that 16 bits per color is preferred, while maintaining 8 bits per color compatibility for systems prior to Mac OS X 10.4

```
*ColorModel RGB/RGB Color: "     <</cupsColorSpace 1/cupsColorOrder 0/cupsBitsPerColor 8     /cupsPreferredBitsPerColor 16>>setpagedevice" *End
```

On systems that recognize the `cupsPreferredBitsPerColor` key, this specifies the `CUPS_CSPACE_RGB` color space, with chunky pixels, with 16 bits-per-color component, that is color data in the format:

`RGBRGBRGB...`

with each color value specified as a 2-byte integer value in host-endian format. On systems that do not support the `cupsPreferredBitsPerColor` key, this specifies 8 bits-per-color component data.

Versions of CUPS that don't know anything about the `cupsPreferredBitsPerColor` key will simply ignore it and supply 8 bits-per-color raster data. Versions that recognize this key and that support 16 bits-per-color component data will supply 16 bits-per-color raster data.

CUPS printer drivers that specify their data request this way MUST use the CUPS raster header structure that precedes each page raster to determine the format of the raster data that is provided to them. If the header has the `header.cupsBitsPerColor` value set to 8, the raster data is 8 bits-per-color, that is, the system can't supply 16 bits-per-color data. If the header has a `header.cupsBitsPerColor` value of 16, then the raster data is 16 bits-per-color component.

[Back to Top](#)

## Summary

Mac OS X version 10.4 and later have support for providing 16 bits-per-color component data to CUPS raster printer drivers. Taking advantage of deep color data offers the potential for superior results from a given output device. You can request deep color data in a manner that is compatible with CUPS installations that don't support it, allowing deployment of a single driver across a wide range of platforms and OS versions.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2018-06-04 | Moved to Retired Documents Library. |
| 2005-08-24 | Obtaining 16 Bits-Per-Color Data with CUPS Raster Printing |
|  | Obtaining 16 Bits-Per-Color Data with CUPS Raster Printing |

