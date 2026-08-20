---
title: Quartz Programming Guide for QuickDraw Developers
apple_id: TP40001098
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/QuickDrawToQuartz2D/tq_color/tq_color.html
archived_at: '2026-07-15T05:24:31.871991Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quartz Programming Guide for QuickDraw Developers](Introduction%20to%20Quartz%20Programming%20Guide%20for%20QuickDraw%20Developers.md)


[Next](Converting%20PICT%20Data.md)[Previous](Basic%20Drawing.md)

# Using Color

In Quartz, everything drawn on the page has color information associated with it. Color components are floating-point values ranging from 0.0 (no color) to 1.0 (full intensity). To support transparency, colors include an alpha component that ranges from 0.0 (transparent) to 1.0 (opaque). Quartz supports drawing with transparency in all types of graphics contexts. There are many uses for transparency in Mac OS X. For example, you can use translucent overlay windows to indicate selection.

Quartz colors are always associated with a color space. This ensures that colors are reproduced faithfully regardless of the drawing destination. Quartz supports separate color spaces for stroking and filling. Further, bitmap images and shadings are drawn to their own color spaces. When drawing is rendered to a destination, Quartz uses ColorSync to achieve accurate color matching.

If color fidelity is critical to your application, you’ll need to learn how to manage colors and how to use calibrated color spaces in Quartz. If you don’t need a sophisticated level of color-matching in your application, don’t panic. Using colors and color spaces in Quartz is straightforward. Starting in Mac OS X v10.4, you can use Generic color spaces, which let Quartz manage color for you in the best way possible, without your needing to know all the particulars of calibrated color spaces.

If you haven’t worked with color spaces, you might want to read _[Color Management Overview](../../Graphics%20Imaging/Color%20Management%20Overview/Introduction%20to%20Color%20Management%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnby)_ to learn the terminology and basic concepts associated with color and color spaces. This document discusses color perception, the dimensions associated with color, device-dependent and device-independent color spaces, color component values, color matching systems, rendering intents, color profiles, and ColorSync.

Regardless of your needs, before you start to work with color in Quartz, read [Color and Color Spaces](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_color/dq_color.html#//apple_ref/doc/uid/TP30001066-CH205) in _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_.

The QuickDraw RGB data type provides storage for the red, green, and blue components of an RGB color, as shown in Listing 3-1. Values for a QuickDraw color component can range from 0 to 65,535. Quartz RGB colors have an additional component for alpha. The values for each component are floating-point, and can range in value from 0.0 (component not present) to 1.0.

__Listing 3-1__  The QuickDraw RGBColor data type

```
struct RGBColor {
   unsigned short red;
   unsigned short green;
   unsigned short blue;
};
```

The `ConvertRGBColortoCGrgba` routine in Listing 3-2 shows how to convert from QuickDraw RGB to Quartz RGB. The `CGrgba` structure in the listing contains components for red, green, blue, and alpha. To convert, the `ConvertRGBColortoCGrgba` routine divides each QuickDraw color component by 65,535. The alpha value that’s passed to the routine gets assigned to the Quartz RGB color.

__Listing 3-2__  A routine that converts RGB color to Quartz RGBA

```swift
struct CGrgba {
        float r;
        float g;
        float b;
        float a;
}

void ConvertRGBColorToCGrgba (const RGBColor* inRGB,
                    float alpha,
                    CGrgba* outCGrgba)
{
    outCGrgba->r = (float)inRGB->red   / 65535.0;
    outCGrgba->g = (float)inRGB->green / 65535.0;
    outCGrgba->b = (float)inRGB->blue  / 65535.0;
    outCGrgba->a = alpha;
}
```


Generic color spaces let the system choose the best possible color representation for a given device and application. These are device-independent color spaces that are easy to use and recommended. Starting in Mac OS X v10.4, you can call the function [CGColorSpaceCreateWithName](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408921-init), passing the constant `kCGColorSpaceGenericRGB`. Use of DeviceRGB is not recommended.

If your code must run in versions of Mac OS X prior to Mac OS X v10.4, see the `GetGenericRGBColorSpace` routine shown in [Listing 3-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgywugsscjfceoqsk). This routine creates a GenericRGB color space by calling the application-defined routine `OpenGenericProfile` once. `CreateGenericRGBColorSpace` keeps the color space so that it can return the color space whenever this routine is called.

__Listing 3-3__  A routine that creates a generic RGB color space

```
CGColorSpaceRef CreateGenericRGBColorSpace(void)
{
    static CGColorSpaceRef genericRGBColorSpace = NULL;

    if (genericRGBColorSpace == NULL)
    {
        CMProfileRef genericRGBProfile = OpenGenericProfile();

        if (genericRGBProfile)
        {
            genericRGBColorSpace = CGColorSpaceCreateWithPlatformColorSpace
                                    (genericRGBProfile);
            if (genericRGBColorSpace == NULL)
                fprintf(stderr, "Couldn't create the generic
                             RGB color space\n");

            // This routine opened the profile so it must close it
            CMCloseProfile(genericRGBProfile);
        }
    }
    return genericRGBColorSpace;
}
```

The `OpenGenericProfile` routine (see Listing 3-4) locates, opens, and returns a reference to the ColorSync profile for the calibrated Generic RGB color space. It is up to the caller to call the function `CMCloseProfile` when done with the profile reference that this function returns.

__Listing 3-4__  A routine that returns a reference to a calibrated GenericRGB color space

```
#define kGenericRGBProfilePathStr
        "/System/Library/ColorSync/Profiles/Generic RGB Profile.icc"

CMProfileRef OpenGenericProfile(void)
{
    static CMProfileRef cachedRGBProfileRef = NULL;

    // Create the profile reference only once
    if (cachedRGBProfileRef == NULL)
    {
        OSStatus            err;
        CMProfileLocation   loc;

        loc.locType = cmPathBasedProfile;
        strcpy(loc.u.pathLoc.path, kGenericRGBProfilePathStr);

        err = CMOpenProfile(&cachedRGBProfileRef, &loc);

        if (err != noErr)
        {
            cachedRGBProfileRef = NULL;
            // Log a message to the console
            fprintf (stderr, "Couldn't open generic profile due to
                                error %d\n",(int)err);
        }
    }

    if (cachedRGBProfileRef)
    {
        // Clone the profile reference so that the caller has
        // their own reference, not our cached one.
        CMCloneProfileRef (cachedRGBProfileRef);
    }

    return cachedRGBProfileRef;
}
```


In _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_, see

- [Color and Color Spaces](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_color/dq_color.html#//apple_ref/doc/uid/TP30001066-CH205)

See these reference documents:

- _[CGColor Reference](https://developer.apple.com/documentation/coregraphics/cgcolor)_
- _[CGColorspace Reference](https://developer.apple.com/documentation/coregraphics/cgcolorspace)_

For those new to color spaces, see _[Color Management Overview](../../Graphics%20Imaging/Color%20Management%20Overview/Introduction%20to%20Color%20Management%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnby)_.

[Next](Converting%20PICT%20Data.md)[Previous](Basic%20Drawing.md)

