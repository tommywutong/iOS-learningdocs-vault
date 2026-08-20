---
title: Video Digitizers - Adding Clean Aperture and Pixel Aspect Ratio Information
apple_id: DTS10004221
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2008-11-20'
source_url: https://developer.apple.com/library/archive/qa/qa1512/_index.html
archived_at: '2026-07-18T02:31:55.154277Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1512

# Video Digitizers - Adding Clean Aperture and Pixel Aspect Ratio Information

## Q:  Does the Sequence Grabber add clean aperture and aspect ratio information on behalf of a Video Digitizer?

A: The Sequence Grabber will __always__ automatically generate Clean, Production and Encoded dimensions for a captured video track based on the Clean Aperture (`kICMImageDescriptionPropertyID_CleanAperture,` `'clap'`) and Pixel Aspect Ratio (`kICMImageDescriptionPropertyID_PixelAspectRatio,` `'pasp'`) Image Description extensions returned by the Video Digitizer selector `GetImageDescription`.

In some versions of QuickTime since 7.1, when a Video Digitizer __does not__ return Clean Aperture and Pixel Aspect Ratio information the Sequence Grabber will __automatically__ generated Clean, Production and Encoded dimensions based on the codec type (this is fine when compressing to DV or DVCPRO50 for example). However, specifically in the case of uncompressed video (where this information cannot be determined based only on codec type) the generated Clean, Production and Encoded dimensions assume the Pixel Aspect Ratio is 1:1. This assumption __may not be correct__ and can lead to unexpected capture results.

In future versions of QuickTime, the Sequence Grabber will __only__ generate the Clean, Production and Encoded dimensions when a Video Digitizer specifically returns Clean Aperture and Pixel Aspect Ratio Image Description extensions. If the `'clap'` and `'pasp'` extensions do not exist, no Clean Aperture or Pixel Aspect Ratio information will be generated for the captured track.

To ensure consistent behavior for all versions of QuickTime, Video Digitizer developers are encouraged to return Clean Aperture and Pixel Aspect Ratio information as part of the Image Description returned by the `GetImageDescription` selector.

__Listing 1__  Adding `'pasp'` and `'clap'` image description extensions.

```swift
pascal VideoDigitizerError MyVDig_GetImageDescription(MyVDigGlobals* glob,
                                                      ImageDescriptionHandle description)
{
    SInt8 savedHState;
    VideoDigitizerError err = noErr;

    if (0 == description) return qtParamErr;

    savedHState= HGetState((Handle)description);
    if (err = MemError()) return err;

    err = HUnlock((Handle)description);
    if (err = MemError()) return err;

    err = SetHandleSize((Handle)description, sizeof(ImageDescription));
    if (err = MemError()) return err;

    ...

    // Set up the parts of the ImageDescription that don't vary by input standard or input format
    (**description).idSize = sizeof(ImageDescription);
    (**description).resvd1          = 0;
    (**description).resvd2          = 0;
    (**description).dataRefIndex    = 0;
    (**description).vendor          = kMyVDIGManufacturer;
    (**description).temporalQuality = 0;
    (**description).spatialQuality  = codecMaxQuality;

    // See note below
    (**description).width           = glob->myDigitizerRect.right - glob-> myDigitizerRect.left;
    (**description).height          = glob-> myDigitizerRect.bottom - glob-> myDigitizerRect.top;

    (**description).hRes            = 72 << 16;
    (**description).vRes            = 72 << 16;
    (**description).frameCount      = 1;
    (**description).depth           = 24;
    (**description).clutID          = -1;

    // Add the ImageDescription properties that don't vary by input standard or input format

    // NOTE: In all cases except DVCPROHD, the Image Description width and height
    // are the Encoded Dimensions. Setting the height and width properties below negates
    // having to directly set them in the Image Description above.
    // Doing both may be redundant, although safe.

    // Encoded width property
    /*
     * The width of the encoded image. Usually, but not always, this is
     * the ImageDescription's width field.
     */
    SInt32 width = (**description).width;
    err = ICMImageDescriptionSetProperty(description, kQTPropertyClass_ImageDescription,
                                         kICMImageDescriptionPropertyID_EncodedWidth, sizeof(SInt32),
                                         &width);
    if (noErr != err) goto bail;

    // Encoded height property
    /*
     * The height of the encoded image. Usually, but not always, this is
     * the ImageDescription's height field.
     */
    SInt32 height = (**description).height;
    err = ICMImageDescriptionSetProperty(description, kQTPropertyClass_ImageDescription,
                                         kICMImageDescriptionPropertyID_EncodedHeight, sizeof(SInt32),
                                         &height);
    if (noErr != err) goto bail;

   // The remaining portions of the Image Description that may vary based on input standard or format

    CleanApertureImageDescriptionExtension    cleanAperture;
    PixelAspectRatioImageDescriptionExtension pixelAspectRatio;

    if (ntscReallyIn == glob->myInputStandard) {

        // Setup properties for NTSC 525-line video signals sampled at 13.5 MHz
        // NOTE: these values will vary depending on your specific format - consult Ice Floe 19

        // http://developer.apple.com/quicktime/icefloe/dispatch019.html#clap
        cleanAperture.cleanApertureWidthN   = 704; // (640 * 11/10)
        cleanAperture.cleanApertureWidthD   = 1;
        cleanAperture.cleanApertureHeightN  = 480;
        cleanAperture.cleanApertureHeightD  = 1;
        cleanAperture.horizOffN             = 0;
        cleanAperture.horizOffD             = 1;
        cleanAperture.vertOffN              = 0;
        cleanAperture.vertOffD              = 1;

        // http://developer.apple.com/quicktime/icefloe/dispatch019.html#pasp
        if (glob->myFrameIs4by3) {
            /* "Non-Square 525"
                Digital 525 (SMPTE 125M-1995, 13.5 MHz)
                525-line analog video sampled at 13.5 MHz
                (e.g., composite NTSC)
            */
            pixelAspectRatio.hSpacing       = 10;
            pixelAspectRatio.vSpacing       = 11;
        } else {
            /* Digital 525 (SMPTE 267M-1995, 13.5 MHz)
               525-line analog video sampled at 13.5 MHz
               (e.g., composite NTSC)
               720x483 progressive 16:9 (SMPTE 293M-1996, 13.5 MHz)
            */
            pixelAspectRatio.hSpacing       = 40;
            pixelAspectRatio.vSpacing       = 33;
        }

        // codec info
        (**description).cType           = kMyFormat;
        (**description).version         = glob->myVersion;
        (**description).revisionLevel   = glob->myRevisionLevel;
        (**description).dataSize        = kFormatBufferSize;
        PLstrncpy((**description).name, glob->myFormatTypeName,
                  glob->myFormatTypeName[0] < 32 ? storage->myFormatTypeName[0] : 31);

        // Add the Image Description properties

        // Clean Aperture
        /*
         * Describes the clean aperture of the buffer.
         */
        err = ICMImageDescriptionSetProperty(description, kQTPropertyClass_ImageDescription,
                                             kICMImageDescriptionPropertyID_CleanAperture,
                                             sizeof(CleanApertureImageDescriptionExtension),
                                             &cleanAperture);
        if (noErr != err) goto bail;

        // Pixel Aspect Ratio
        /*
         * Describes the pixel aspect ratio.
         */
        err = ICMImageDescriptionSetProperty(description, kQTPropertyClass_ImageDescription,
                                             kICMImageDescriptionPropertyID_PixelAspectRatio,
                                             sizeof(PixelAspectRatioImageDescriptionExtension),
                                             &pixelAspectRatio);
        if (noErr != err) goto bail;

        ...

    }

    ...

bail:

    HSetState((Handle)description, savedHState);

    return err;
}
```


- [SoftVDigX](https://developer.apple.com/samplecode/SoftVDigX/index.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-11-20 | Editorial |
| 2007-02-14 | New document that discusses the importance of adding 'pasp' and 'clap' image description extensions to the ImageDescription returned by a VDIG. |

