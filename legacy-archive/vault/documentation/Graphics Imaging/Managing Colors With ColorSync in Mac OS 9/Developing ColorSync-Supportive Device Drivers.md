---
title: Managing Colors With ColorSync in Mac OS 9
apple_id: TP40000896
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2003-02-01'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ManagingColorSync/DevCSSDevDrvrs/DevCSSDevDrvrs.html
archived_at: '2026-07-15T07:36:24.448557Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Managing Colors With ColorSync in Mac OS 9](About%20This%20Document.md)


[Next](Developing%20Color%20Management%20Modules.md)[Previous](Developing%20ColorSync-Supportive%20Applications.md)

# Developing ColorSync-Supportive Device Drivers

This section describes how you can use the ColorSync Manager to provide ColorSync-supportive device drivers for peripherals. It first describes how input, display, and output devices work with color profiles. It then discusses how devices interact with color management modules (CMMs). Next it describes what you must do to provide minimum ColorSync support, as well as how you can provide more extensive support. Finally, it uses a QuickDraw-based printer device driver to demonstrate some of the color-matching features a device driver can provide.

Read this section if your device driver for an input, display, or output device will support the ColorSync Manager and allow users to produce color-matched images.

Before you read this section, you should read [Overview of ColorSync](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2gi5euesi) and [Overview of Color and Color Management Systems](Overview%20of%20Color%20and%20Color%20Management%20Systems.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydeobqfvbeeq2cirduira). These sections provide an overview of ColorSync, explain color theory and color management systems, and define key terms.

Although the features described here are commonly provided by printer device drivers, the code samples in [Developing ColorSync-Supportive Applications](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2kinbeqra) may also be of use in developing your device driver.

_ColorSync Manager Reference_ describes constants, data structures, functions, and result codes for ColorSync-supportive applications and device drivers.

[ColorSync Version Information](Version%20and%20Compatibility%20Information.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzvfvbegskgjbeusra) describes the `Gestalt` information, shared library version numbers, CMM version numbers, and ColorSync header files you use with different versions of the ColorSync Manager. It also includes CPU and Mac OS system requirements.

A device driver that supports ColorSync should provide at least one profile for the device. In addition, it can provide its own CMM, designed to perform the best possible color matching for the device. If you are creating your own CMM, you should read [Developing Color Management Modules](Developing%20Color%20Management%20Modules.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzwfvbegskei5cueqy) and _ColorSync Manager Reference_.

To assess the way each device interprets color, color scientists and profile developers perform device characterizations. This process, which entails measuring the gamut of a device, yields a color profile for that device. For an overview of profiles, see [Profiles](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2hirduqqi).

Device profiles are of paramount importance to any color management system because they characterize the unique color behavior of each device and provide the data needed for color matching and color conversion. Device profiles are used by CMMs that perform the low-level calculations required to match colors from a source device to a destination device.

The ICC defines a device profile class for each of three types of devices:

- An input device, such as a scanner or a digital camera.
- A display device, such as a monitor or a liquid crystal display.
- An output device, such as a printer.

These classes are described in detail in [Profile Classes](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2jifeuisa).

Each device profile class has its own signature. The ColorSync constants for these signatures are described in _ColorSync Manager Reference_. You can create a device driver for any of the device classes. When you create a profile for your device, you specify the signature in the profile header’s `profileClass` field. For more information on profile headers, see _ColorSync Manager Reference_

Whether you create a profile for your device or obtain one from a profile vendor, your device driver must provide at least one profile for its device. However, you can provide more than one profile for the same device to characterize different states. Although a printer that your device driver supports may have a number of profiles for different conditions, such as the use of foils or different grades of paper, all of its profiles will use the same profile signature, `cmOutputClass`.

Device profiles follow the ICC profile format, an industry standard described in [Profiles](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2hirduqqi). You can provide a single profile or a set of profiles that can be used across different operating systems for the device your driver supports. The common profile format specified by the ICC allows end users to transparently move profiles and images with embedded profiles between different operating systems.

The profile structure is defined as a header followed by a tag table which, in turn, is followed by a series of tagged elements that your device driver can access randomly and individually. Using ColorSync Manager functions, you can read the profile header and modify its contents and you can get and set individual tags and their element data.

This document uses 2.x to refer to ColorSync profiles for ColorSync Manager version 2.0 and greater, as described in [ColorSync and ICC Profile Format Version Numbers](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2ijbeeory). Version 2.x profiles require more information and are larger than ColorSync 1.0 profiles, which were originally memory based. Because version 2.x profiles are larger, they are disk-based. The ICC profile format specification defines how profiles can be stored as disk files and how profiles can be embedded in common graphics file formats such as PICT and TIFF. The ColorSync Manager provides the `CMProfileLocation` data structure to identify the location of a profile. It also provides functions you can use to embed a profile in or extract if from a PICT file, as described in _ColorSync Manager Reference_.

Device profiles reside in the ColorSync Profiles folder, in pictures, or with device drivers. Files that contain profiles store profile data in the data fork and have a file type of `'prof'`.

By convention, profiles not embedded in image documents are stored in the ColorSync Profiles folder, as described in [Profile Search Locations](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2civbuory). You can store your profile files wherever you want, but if you want other drivers or applications to have access to them, you should store them in the ColorSync Profiles folder. Applications that perform soft proofing or gamut checking can use ColorSync Manager routines to search the folder for specific types of profiles to provide a pop-up menu or list to the user. If your profiles are not available, these applications will not be able to include these profiles in menus or lists, and will not be able to color match to your device (unless they provide a profile for your device themselves).

Some applications may place special-purpose profiles for your device in the ColorSync Profiles folder. For this reason, when your device driver itself displays a pop-up menu or list to the user, you should search not only your private profile location storage, if you use one, but also the ColorSync Profiles folder, to make sure that you offer a complete list of available profiles for your device.

The ColorSync Profiles folder can contain both ColorSync 1.0 profiles and version 2.x profiles. However, your device driver will be able to search for only version 2.x profiles. This is because ColorSync Manager 2.x search functions do not acknowledge ColorSync 1.0 profiles. Support for 1.0 profiles may be even more limited in the future. For more information on this and other limitations of the 1.0 profile format, see [ColorSync 1.0 Profiles and Version 2.x Profiles](Version%20and%20Compatibility%20Information.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzvfvbegskiireeiqq).

For most ColorSync Manager functions that your device driver calls, you will need to supply references to profiles for both the source device on which the image was created and the destination device for which it is to be color matched and where it will be rendered.

The driver for an input device such as a scanner typically embeds the scanner profile used to create the image in the document containing the image. The driver for a device that displays an existing image on the system’s display or a printer device that prints a color-matched image typically extracts the embedded profile that accompanies the image from the document containing the image, and uses that profile as the source profile when matching.

Images created using input devices are commonly color matched using the profile for the input device as the source profile and the system profile for the display as the destination profile. [Setting Default Profiles](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2jiveukri) describes how to set the default system profile and other default profiles. Images that are created, depicted, or modified on a display device and that are destined for an output device such as a printer are color matched using the profile for the display as the source profile and the printer’s profile as the destination profile.

To use a profile, you must first obtain a reference to the profile. For a description of how to do this, see [Obtaining Profile References](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2kireeesi).

Your device driver can use the color conversion functions, described in _ColorSync Manager Reference_, to convert colors between color spaces belonging to the same base family without relying on a CMM. However, color matching, gamut checking, providing color rendering dictionaries to PostScript printers, and other tasks you perform using ColorSync Manager functions all require use of a CMM. It is the CMM that actually carries out the work of the ColorSync Manager functions, such as performing the low-level calculations required to match colors from a source device to a destination device.

If your ColorSync-supportive device driver can use the Apple-supplied default CMM, you need only provide one or more profiles for your device. However, you may want to provide a custom CMM that is optimized for your device and its profiles. For example, a profile can provide private tags containing information a custom CMM might use to achieve better results for the device.

To provide your own CMM, you can create one or obtain one from a vendor. For information describing how to create a CMM, see [Developing Color Management Modules](Developing%20Color%20Management%20Modules.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzwfvbegskei5cueqy) and _ColorSync Manager Reference_

For additional information on CMMs, see [Setting a Preferred CMM](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2hijdemqy) and [How the ColorSync Manager Selects a CMM](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2cijdeura).

Your ColorSync-supportive device driver can provide users with various color-matching features based on the type of device you support. This section describes:

- [Providing Minimum ColorSync Support](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzxfvbegskiineusqy)
- [Providing More Extensive ColorSync Support](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzxfvbegskfjfeeqry)

The minimum level of ColorSync support you should provide differs depending on the type of device your driver supports.

For a scanner, you should embed the scanner profile used to create the image in the document containing the image; this is also referred to as tagging an image. If you do not tag the image with the profile, you should at least make the profile for the image available so that it can be used for color matching. If you do not provide the scanner profile, an application or driver that attempts to color match the scanned image will use the system profile as the source profile and may produce results inconsistent with the colors of the original image.

For a display device driver or a printer device driver, you must preserve images tagged with a profile by not stripping out picture comments used to embed profiles or by leaving profiles in documents that use other methods to include them. For example, if your driver displays or prints PICT files but does not perform color matching, your driver should not strip out the ColorSync-related picture comments that are used to embed profiles in PICT files, begin and end use of a specific profile, and enable and disable color matching. Even though your driver may not make use of the comments, another display or printer driver or an application may use them.

If you don’t perform color matching but you want to allow other applications to produce images that are color matched for your device, you should provide a device profile to be used as the destination profile. If you provide a profile for your display or printer and place it in the ColorSync Profiles folder, applications that perform color matching can use it to create a color-matched image expressed in the colors of your device’s gamut. A user can then print a color-matched image using the printer your driver supports.

Instead of relying on an application to color match an image for your printer, your printer driver can color match the image itself before sending it to the printer. To perform color matching, your printer driver must obtain a reference to the source profile. Documents containing images to be printed often contain an embedded profile along with the image. To use the source profile, your printer driver must be able to extract it. If an image is not accompanied by a source profile, the default system profile is used, as described in [Setting Default Profiles](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2jiveukri). In this case, your driver should provide an interface that allows the user to select the rendering intent to be used. Rendering intents are described in [Rendering Intents](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2ijjdumrq).

You can provide an interface that offers additional features. Your interface can

- allow a user to turn ColorSync color matching on or off before printing
- offer pop-up menus, allowing the user to choose

  - the rendering method to be used in color matching the image (perceptual, colorimetric, or saturation)
  - the color-image quality (normal, draft, or best)

Some of these features are discussed below and in [Developing ColorSync-Supportive Applications](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2kinbeqra).

This section describes how your device driver can implement certain color matching and related features with ColorSync. It includes the following:

- [Determining If the ColorSync Manager Is Available](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzxfvbegskdjjaumry)
- [Interacting With the User](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzxfvbegskkijcugsa)
- [Color Matching an Image to Be Printed](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzxfvbegskkjfbusrq)

Many of the tasks that your device driver performs to support ColorSync can also be performed by other kinds of color-matching applications. Some of these tasks are mentioned here, but not explained in detail. For a list of code samples shown elsewhere, see [Developing Your ColorSync-Supportive Application](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2ijfduury).

To determine if the ColorSync Manager (version 2.x) is available, call the `Gestalt` function with the `gestaltColorMatchingVersion` selector. For sample code that demonstrates how to perform this operation, see [Determining If the ColorSync Manager Is Available](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2cirdeiry). ColorSync constants for use with the `Gestalt` function are described in _ColorSync Manager Reference_. For related information on ColorSync versions, see [Table 7-1](Version%20and%20Compatibility%20Information.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzvfvkfawcsivddcmjv), which lists version numbers for releases of the ColorSync Manager, along with corresponding shared library version numbers, `Gestalt` selector codes, and hardware and system requirements.

Using lists and dialog boxes, you can provide choices that influence the color-matching process. For example, you can offer any of the following:

- A list of profiles to select from. You can allow the user to choose the appropriate profile for your printer in its current state. To provide a list of profiles for the user to select from, you must first search for the relevant profiles:

  - Starting with version 2.5 of the ColorSync Manager, you should use the algorithm shown in [Performing Optimized Profile Searching](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2djbcucry) to search for profiles. That algorithm uses `CMIterateColorSyncFolder`.
  - For versions of the ColorSync Manager prior to 2.5, you can use the functions described in _ColorSync Manager Reference_.
- A dialog box for specifying how the image will be color matched. If the source profile is embedded with the image, the source profile specifies the rendering intent to be used. However, if the source profile is not provided and the system profile is used as the source profile, you should allow the user to select the rendering intent to be used. After the user chooses a rendering intent, you can use the selection to set the source profile’s header. [Setting a User-Selected Rendering Intent](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzxfvbegskdjjduqsi) explains this process.
- A dialog box for choosing which color-matching quality of image to produce. A user may want to produce a draft of the image quickly for review before producing the best possible quality of the image. After the user chooses a color-matching quality, you can use the selection to set the source profile’s header. [Setting a User-Selected Color-Matching Quality Flag](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzxfvbegskeindesra) explains how to do this.
- A dialog box for turning ColorSync color matching on or off before printing. If an application that creates or modifies an image has already performed color matching using your printer profile as the destination profile, the user might want to turn off color matching. To provide this capability, your driver should support the `PrGeneral` function with the `enableColorMatchingOp` operation code. For information on the `PrGeneral` function, see Inside Macintosh: Imaging With QuickDraw. The `enableColorMatchingOp` operation code constant defined by the ColorSync Manager is described in _ColorSync Manager Reference_.

The ColorSync Manager supports the four standard rendering intents defined by the ICC—perceptual, relative colorimetric, saturated, and absolute colorimetric. Every profile supports these four intents, which are commonly used to match the colors of a source image to the color gamut of the destination device in the most optimum way for the type of image. These intents are described in detail in [Rendering Intents](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2ijjdumrq).

If the source profile is embedded with the image, the source profile specifies the rendering intent to be used. However, if the source profile is not available and the system profile must be used as the source profile, you should allow the user to select the rendering intent to be used.

To allow users to choose the rendering intent most appropriate for color matching a graphical image, you can provide a pop-up menu or a dialog box identifying the rendering intent options available. By providing a description of the available rendering intents, you can help a user select the rendering intent that best maintains important aspects of the image.

Color professionals and technically-sophisticated users are likely to be familiar with the ICC terms for rendering intent and the gamut-matching strategies they represent. If your application is aimed at novice users, however, you may prefer to use a simplified terminology based on the typical image content associated with a rendering intent, as described in [Table 3-1](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2ci5ceiqq). For example, you might note the following:

- For perceptual matching, all the colors of a given gamut may be scaled to fit within another gamut. This intent is the best choice for realistic images, such as scanned photographs.
- For saturation matching, the relative saturation of colors is maintained from gamut to gamut. Rendering the image using this intent gives the strongest colors and is the best choice for bar graphs and pie charts, in which the actual color displayed is less important than its vividness.
- For relative colorimetric matching, the colors that fall within the gamuts of both devices are left unchanged. Some colors in both images will be exactly the same, a useful outcome when colors must match quantitatively. This intent is best suited for logos or spot colors.
- For absolute colorimetric matching, a close appearance match may be achieved over most of the tonal range, but if the minimum density of the idealized image is different from that of the output image, the areas of the image that are left blank will be different. Colors that fall within the gamuts of both devices are left unchanged.

After the user selects the intent to be used, you must modify the `renderingIntent` field of the system profile’s header to reflect the choice. To put the rendering intent chosen by the user in the profile header, follow these steps:

1. Obtain a profile reference to the system profile.

   [Identifying the Current System Profile](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2kjjbekrq) describes how to do this.
2. Get the profile header of the system profile.

   You call the function `CMGetProfileHeader`, passing the profile reference, to obtain the profile’s header. The function returns the profile header using a union of type `CMAppleProfileHeader`. You can use this function for both ColorSync 1.0 profiles and version 2.x profiles.

   For a version 2.x profile, you use the data structure `CM2Header`. For a version 1.0 profile, you use the `CMHeader` data structure. For more information on profile headers, see _ColorSync Manager Reference_.
3. Assign the new rendering intent to the header field.

   To assign a rendering intent to the system profile header’s `renderingIntent`

   `enum { cmPerceptual= 0, cmRelativeColorimetric= 1, cmSaturation= 2, cmAbsoluteColorimetric= 3 };` field, use the constants defined by the following enumeration:

   These constants are described in _ColorSync Manager Reference_.
4. Set the modified profile header of the system profile.

   After you assign the rendering intent, you must replace the header by calling the function `CMSetProfileHeader`. You can use this function to set a header for a version 1.0 or a version 2.x ColorSync profile. You pass the header using the union `CMAppleProfileHeader`.

You can now use the system profile to create a color world for the color-matching process. For information on how to create a color world, see [Creating a Color World to Use With the General Purpose Functions](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2jifdecri).

[Listing 5-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzxfvbegskci5bussi) includes code that uses the `cmSaturation` constant to set the rendering intent for a profile. 

The ColorSync Manager provides a feature, called the quality flags settings, that controls the quality of the color-matching process in relation to the time required to perform the match. This feature, which is not a standard feature defined by the ICC profile format specification, works by letting you manipulate certain bits of the profile header’s `flags` field. There are three quality flag settings: normal, draft, and best. For a description of the profile header’s `flags` field, see _ColorSync Manager Reference_.

Normal mode is the default setting. Color matching using draft mode takes the least time and produces the least exact results. Color matching using best mode takes the longest time but produces the finest results.

Users sometimes want to produce review drafts of images quickly before expending the time to produce the best-quality final copy. Your interface can allow them this flexibility by offering a dialog box that provides the three options.

After the user selects the color-matching quality, you can use the selection to set the appropriate bits of the source profile’s `flags` field. To set the color-matching quality chosen by the user, follow these steps:

1. Obtain a profile reference to the source profile.

   [Obtaining Profile References](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2kireeesi) describes how to do this.
2. Get the profile header of the source profile.

   You call the function `CMGetProfileHeader`, passing the profile reference, to obtain the profile’s header. The function returns the profile header using a union of type `CMAppleProfileHeader`.
3. Optionally, test the current setting of the source profile header’s flags.

   The `flags` field of the source profile header is a long word coded in big-endian notation. Big-endian notation is a means of encoding data in which the first byte within 16-bit and 32-bit quantities is the most significant. The ICC profile consortium reserves the first 2 bits of the low word for its own use. The least significant 2 bits of the high word constitute the quality flag settings used to specify the quality for the color matching. The bit definitions for the `flags` field are shown in _ColorSync Manager Reference_.

   To evaluate and interpret the current setting of the quality flags bits, you can take these steps, in order:

   - Right-shift by 16 bits.
   - Mask off the high 14 bits.
   - Compare the result with values defined by the following enumeration:

```
        enum
        {
         cmNormalMode = 0,
         cmDraftMode = 1,
         cmBestMode = 2
        };
```

   These constants are described in _ColorSync Manager Reference_.
4. Set the quality flags bits to the user-selected value.

   To set the quality flag, you can use the constants defined by the enumeration provided by the ColorSync Manager and shown in step 3.
5. Set the source profile with the modified profile header.

   After you set the `flags` field based on the user’s selection, you must replace the header by calling the function `CMSetProfileHeader`. You pass the header using the union `CMAppleProfileHeader`.

You can now use the source profile to create a color world for the color-matching process. For information on how to create a color world, see [Creating a Color World to Use With the General Purpose Functions](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2jifdecri).

[Listing 5-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzxfvbegskci5bussi) shows how to set the system profile’s quality flag to best mode for producing the highest-quality color-matched image. It also sets the rendering intent to saturation before setting up a color world based on the modified system profile and the printer profile.

The `MySetHeader` function shown in [Listing 5-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzxfvbegskci5bussi) initializes the `CMProfileRef` data structures it will use for the system profile and the printer profile before it calls the following two functions—the ColorSync Manager function `CMGetSystemProfile` to obtain a reference to the system profile and its own function `MyGetPrinterProfile` to obtain a reference to the profile for its printer.

The source profile (in this case, the system profile), not the printer profile, determines the quality mode and the rendering intent to be used in color matching the image to the destination printer. Now that it has a reference to the system profile, the code can obtain the profile’s header. It does this by calling the function `CMGetProfileHeader`, specifying the reference it obtained to the system profile.

Using the `kSpeedAndQualityFlagMask` constant it defined earlier, the code clears the quality mode bits of the system profile’s `flags` field. Then it sets the quality mode bits to `cmBestMode` to specify best mode quality for color matching. The least significant 2 bits of the `flags` field’s high word constitute the quality flag. After setting the quality flag, the code sets the system profile header’s `renderingIntent` field to `cmSaturation`.

Now that the code has modified the system profile’s header to indicate the user’s selections, it calls the `CMSetProfileHeader` function to write the profile header to the profile. Because the driver code intends to use the values the user selected only to color match the image to be printed, it does not permanently preserve the header field changes by calling `CMUpdateProfile` to write the changes to the profile. When the code closes its reference to the system profile after having built the color world, the system profile’s header modifications are discarded.

The code calls the `NCWNewColorWorld` function, passing the temporarily modified system profile, to create the color world. It then closes its references to both the system and printer profiles and color matches the image before sending it to the printer. When it no longer needs the color world, the code calls the `CWDisposeColorWorld` function to close the color world and release the memory it uses. Finally, the code tests to ensure that the profile references are closed.

__Listing 5-1__  Modifying a profile header’s quality flag and setting the rendering intent


```
void MySetHeader(void);
CMError MyGetPrinterProfile(CMProfileRef *printerProf);
/* for CM2Header.profileVersion */
#define kMajorVersionMask 0XFF000000
/* two bits used to specify speed & quality */
/* must be shifted left 16 bits in flag’s long word */
#define kSpeedAndQualityFlagMask 0X00000003
void MySetHeader(void)
{
    CMError                     cmErr;
    CMProfileRef                sysProf;
    CMAppleProfileHeader        sysHeader;
    CMProfileRef                printerProf;
    CMWorldRef                  cw;

    sysProf = NULL;
    printerProf= NULL;
    cw  = NULL;

    cmErr = CMGetSystemProfile(&sysProf);
    if (cmErr == noErr)
    {
        cmErr = MyGetPrinterProfile(&printerProf);
    }

    if (cmErr == noErr)
    {
        cmErr = CMGetProfileHeader(sysProf, &sysHeader);
    }

    if (cmErr == noErr)
    {
        /* clear the current quality and then set it to best */
        sysHeader.cm2.flags &= ~(kSpeedAndQualityFlagMask << 16);
        sysHeader.cm2.flags |= (cmBestMode << 16);

        /* set rendering intent to saturation */
        sysHeader.cm2.renderingIntent = cmSaturation;
        cmErr = CMSetProfileHeader(sysProf, &sysHeader);
    }

    if (cmErr == noErr)
    {
        cmErr = NCWNewColorWorld(&cw, sysProf, printerProf);
    }

    /* close any open profiles */
    if (sysProf != NULL)
    {
        (void) CMCloseProfile(sysProf);
    }

    if (printerProf != NULL)
    {
        (void) CMCloseProfile(printerProf);
    }
                    .
                    .
                    .
        /* device-driver functions that use the color world to color match
            the image and send it to the printer belong here */
                    .
                    .
                    .
    if (cw != NULL)
    {
        CWDisposeColorWorld(cw);
    }
}
```


The ColorSync Manager provides QuickDraw-specific and general purpose color-matching functions, as described in [When Color Matching Occurs](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2hjjeuuqi). Printer device drivers usually perform color matching using the general purpose ColorSync Manager functions to match all QuickDraw operations as they pass through the bottleneck routines of the printing grafport.

When the stream of QuickDraw data sent to your printer device driver contains a profile embedded using picture comments, your driver should extract the embedded profile using the ColorSync Manager’s `CMUnflattenProfile` function. After you extract the profile and open a reference to it, you should create a new color world based on the extracted profile and a profile for your printer. For information on how to extract an embedded profile, see [Extracting Profiles Embedded in Pictures](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2fifaumqq). [Creating a Color World to Use With the General Purpose Functions](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2jifdecri) describes how to create a color world.

If the QuickDraw data stream does not contain embedded profiles, your driver should use the system profile as the source profile in creating the color world.

You should then match subsequent QuickDraw operations using the color world before sending them to your printer. See [Setting Default Profiles](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2jiveukri) for information on how the user and how your code can set default profiles.

[Next](Developing%20Color%20Management%20Modules.md)[Previous](Developing%20ColorSync-Supportive%20Applications.md)

