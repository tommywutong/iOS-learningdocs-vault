---
title: Managing Colors With ColorSync in Mac OS 9
apple_id: TP40000896
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2003-02-01'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ManagingColorSync/WhatsNew/WhatsNew.html
archived_at: '2026-07-15T07:36:28.851748Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Managing Colors With ColorSync in Mac OS 9](About%20This%20Document.md)


[Next](Document%20Revision%20History.md)[Previous](Version%20and%20Compatibility%20Information.md)

# What’s New

This section lists the new features available with version 2.5 of the ColorSync Manager, provides links to new and revised material in other sections, and summarizes changes to ColorSync functions, data types, and constants. It also contains a brief summary of features that were added for ColorSync 2.1.

This section includes the following:

- [New Features in ColorSync Manager Version 2.5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzufvbecqsfirceqri) lists the features new to version 2.5 and provides links to new and revised material.
- [New and Revised Functions, Data Types, and Constants](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzufvbecqscifeuiry) provides tables that include a brief description of all new and changed functions, data types, and constants, as well as links to more detailed descriptions.
- [New and Revised Code Listings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzufvbecqskjbdeesa) describes new and revised code listings for ColorSync 2.5.
- [New Features in ColorSync Manager Version 2.1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzufvbecqsfjjbesra) lists the features new to ColorSync version 2.1.
- [Other Color Documentation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzufvbecqsei5aumsi) explains where you can find information on earlier versions of ColorSync, and on other color technologies such as the Color Picker Manager.

For related information, see [Document Revision History](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenztfvkfawcsivddcmbr) and [About This Document](About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenbzfvbeeq2ijjaugrq).

Version 2.5 of the ColorSync Manager provides many new or enhanced features. The following sections present a brief overview of these features, with links to detailed information in other sections.

Earlier versions of ColorSync placed the ColorSync Profiles folder inside the Preferences folder. Version 2.5 places the profiles folder at the first level inside the System folder. For backward compatibility, ColorSync may put an alias to the original folder location inside the new profiles folder.

You can now organize profiles by storing them in one level of subfolders within the profiles folder. You can also store aliases to other profiles and profile folders. Profile searching can find profiles in any of these locations.

For an overview of this and related topics, see:

- [Profile Search Locations](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2civbuory)
- [Where ColorSync Searches for Profiles](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2jjjbukqq)
- [Where ColorSync Does Not Look for Profiles](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2gifduury)
- The function description for `NCMGetProfileLocation`
- [Optimized Profile Searching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzufvbecqsgizeuura)

ColorSync 2.5 uses a cache file to keep track of currently-installed profiles. A flexible new routine, `CMIterateColorSyncFolder`, takes advantage of the profile cache to perform fast profile searches and provide profile information quickly.

For an overview of this topic, see:

- [The Profile Cache and Optimized Searching](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2cijceory)

For related information, including sample code that demonstrates optimized searching, see:

- [Performing Optimized Profile Searching](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2djbcucry)
- The function description for `CMIterateColorSyncFolder`

ColorSync 2.5 uses the Monitors & Sound control panel to provide a monitor calibration framework and per/monitor profiles. Among the features: you can select a separate profile for each available monitor; you can calibrate monitors and, for each monitor, create one or more color profiles (based on variations in gamma, white point, and so on); Apple provides a default calibration plug-in, but you can create your own calibration plug-in or use third-party versions; you can choose from any available calibrator to create a monitor profile.

For an overview of these features, see:

- [Monitor Calibration and Profiles](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2gjbbessq)

Starting with version 2.5, ColorSync also offers new features for working with displays: you can call ColorSync functions to get or set a monitor profile by AVID; you can use an optional profile tag, which you specify with the `cmVideoCardGammaTag` constant, to provide video card gamma data for a profile—when you call the function `CMSetProfileByAVID`, it retrieves the video card gamma data and sets the video card.

For sample code that uses the function `CMGetProfileByAVID`, see:

- [Getting the Profile for the Main Display](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2givdeosa)

For an overview of video card gamma, see:

- [Video Card Gamma](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2jjffeoqq)

For descriptions of the data types and constants you use with video card data, see _ColorSync Manager Reference_.

ColorSync 2.5 provides an extensible AppleScript framework that allows users to script many common tasks. Among the features:

- Scriptable operations include setting the system profile, matching an image, and embedding a profile in an image.
- Several sample scripts demonstrate how to automate repetitive tasks.
- The scripting framework uses a plug-in architecture that is fully accessible to third-party scripting plug-ins.

For more information, see:

- [Scripting Support](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2gijducsq)

  - [Scriptable Properties](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2ijfcueqi)
  - [Scriptable Operations](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2iinbeisi)
  - [Extending the Scripting Framework](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2iivbeusi)
  - [Sample Scripts](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2iireukra)

ColorSync’s default Color Matching Module, or CMM, now supports multiple processors for some color matching functions. Multiprocessor support is transparent to your code—it is invoked automatically when the required conditions are met. Matching algorithms take advantage of multiple processors with up to 95% efficiency. As a result, an operation can be performed nearly twice as fast when two processors are available. Performance is scalable.

For more information on this topic, see:

- [Multiprocessor Support](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2gireeksi)

  - [When ColorSync Uses Multiple Processors](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2gifcecqq)
  - [Efficiency of ColorSync’s Multiprocessor Support](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2givaumqq)

ColorSync’s default Color Matching Module now supports 16-bits-per-channel color spaces. The new formats supported are:

- RBG stored in 48 bits per pixel
- CMYK stored in 64 bits per pixel
- Lab stored in 48 bits per pixel

To make use of these new spaces, you specify one of the following constants in the color space field (`space`) of the `CMBitmap` structure:

```
cmRGB48Space
cmCMYK64Space
cmLAB48Space
```

For more information on these constants, see _ColorSync Manager Reference_.

The ColorSync control panel, which replaces the ColorSync™ System Profile control panel, now lets you choose a preferred CMM from any CMMs that are present.

Related changes include the following:

- ColorSync previously supported only one default profile—the RGB System profile. Users can now use the ColorSync control panel to set default profiles for RGB and CMYK color spaces as well.
- ColorSync provides functions your code can call to get and set default color space profiles for RGB, CMYK, Lab, and XYZ color spaces.

For more information, see:

- [Setting a Preferred CMM](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2hijdemqy)
- [Setting Default Profiles](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2jiveukri)
- _ColorSync Manager Reference_

Version 2.5 of the ColorSync Manager ships with the following additional features:

- The Kodak Color Matching Module (available as an install option). Some cross-platform applications use the Kodak Color Management System on the Windows platform. Users working with Macintosh versions of those applications can use the Kodak CMM to ensure consistent output.
- New versions of the ColorSync Photoshop plug-ins that take advantage of ColorSync 2.5. The Filter plug-in is accessible from the Photoshop Filters menu, while the Export and Import filters are accessible from the File menu.
- Commonly-requested profiles, including SWOP (standard web offset press) and sRGB (standardized RGB monitor).
- Support for an optional video card gamma tag in profiles. For more information, see [Monitor Calibration Framework and Per/Monitor Profiles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzufvbecqsiifcuqsa).
- A ColorPicker Manager extension that works with ColorSync 2.x.
- A revised version of the CSDemo application provides sample code that demonstrates how to use many of the new features of ColorSync 2.5.

The tables in this section provide a brief description of new and changed functions, data types, and constants in ColorSync version 2.5, as well as links to more detailed information.

- Table 8-1 shows new and revised functions.
- Table 8-2 shows new and revised data types.
- Table 8-3 shows new and revised constants.

__Table 8-1__  New and revised functions in ColorSync 2.5

| Function | Version 2.5 Notes |
| `NCMGetProfileLocation` | New. Obtains either a profile location structure for a specified profile or the size of the location structure for the profile. Has parameter to specify size of location structure. |
| `CMGetProfileLocation` | Not recommended. Use NCMGetProfileLocation (page 233) instead. |
| `CMFlattenProfile` | Changed. The ColorSync Manager now calls the transfer function directly, without going through the preferred, or any, CMM. |
| `CMUnflattenProfile` | Changed. The ColorSync Manager now calls the transfer function directly, without going through the preferred, or any, CMM. |
| `NCWNewColorWorld` | Changed. Use of the system profile has changed, as described in [Setting Default Profiles](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2jiveukri). This could affect use of `src` and `dst` parameters. |
| `CWConcatColorWorld` | Changed. Selection of preferred CMM has changed, as described in [Setting a Preferred CMM](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2hijdemqy) and [How the ColorSync Manager Selects a CMM](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2cijdeura). |
| `CWNewLinkProfile` | Changed. Selection of preferred CMM has changed, as described in [Setting a Preferred CMM](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2hijdemqy) and [How the ColorSync Manager Selects a CMM](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2cijdeura). |
| `CMGetCWInfo` | Changed. Selection of preferred CMM has changed, as described in [Setting a Preferred CMM](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2hijdemqy) and [How the ColorSync Manager Selects a CMM](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2cijdeura). |
| `CWMatchBitmap` | Changed. Now supports additional color space constants: `cmGray16Space`, `cmGrayA32Space`, `cmRGB48Space`, `cmCMYK64Space`, and `cmLAB48Space`. |
| `NCMBeginMatching` | Changed. Use of the system profile has changed, as described in [Setting Default Profiles](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2jiveukri). This could affect use of `src` and `dst` parameters. |
| `NCMDrawMatchedPicture` | Changed. Use of the system profile has changed, as described in [Setting Default Profiles](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2jiveukri). This could affect use of `dst` parameter. |
| `CMGetPreferredCMM` | New. Identifies the preferred CMM specified by the ColorSync control panel. |
| `CMGetSystemProfile` | Changed. Use of the system profile has changed, as described in [Setting Default Profiles](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2jiveukri). |
| `CMSetSystemProfile` | Changed. Use of the system profile has changed, as described in [Setting Default Profiles](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2jiveukri). |
| `CMGetDefaultProfileBySpace` | New. Gets the default profile for the specified color space. |
| `CMSetDefaultProfileBySpace` | New. Sets the default profile for the specified color space. |
| `CMGetProfileByAVID` | New. Gets the current profile for a monitor. |
| `CMSetProfileByAVID` | New. Sets the current profile for a monitor. |
| `CMGetColorSyncFolderSpec` | Changed. The name and location of the profile folder changed, as described in [Profile Search Locations](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2civbuory). |
| `CMIterateColorSyncFolder` | New. Provides optimized profile searching by iterating over available profiles. |
| `CMNewProfileSearch` | Not recommended. Use `CMIterateColorSyncFolder` instead. |
| `CMUpdateProfileSearch` | Not recommended. Use `CMIterateColorSyncFolder` instead. |
| `CMDisposeProfileSearch` | Not recommended. Use `CMIterateColorSyncFolder` instead. |
| `CMSearchGetIndProfile` | Not recommended. Use `CMIterateColorSyncFolder` instead. |
| `CMSearchGetIndProfileFileSpec` | Not recommended. Use `CMIterateColorSyncFolder` instead. |
| `MyProfileIterateProc` | New. Application-defined function that the `CMIterateColorSyncFolder` function calls once for each found profile file as it iterates over the available profiles. |
| `MyColorSyncDataTransfer` | Changed. The ColorSync Manager calls the function directly, without going through the preferred, or any, CMM |

Table 8-2 shows new and revised data types.

__Table 8-2__  New and revised data types in ColorSync 2.5

| Data type | Version 2.5 Notes |
| `CMProfileIterateProcPtr` | New. Universal procedure pointer definition for application-defined function you pass to the function `CMIterateColorSyncFolder`. |
| `CMProfileIterateData` | New. Provides concise description of key profile data during iteration over available profiles. |
| `CMSearchRecord` | Not recommended. Use `CMProfileIterateData` instead. |
| `CMProfileSearchRef` | Not recommended. Use `CMProfileIterateData` instead. |
| `CMVideoCardGammaType` | New. Optional profile tag for video card gamma. |
| `CMVideoCardGammaTable` | New. Specifies video card gamma data in table format, based on the specified number of channels, entries per channel, and entry size. |
| `CMVideoCardGammaFormula` | New. Specifies video card gamma data as a formula, based on specified actual, minimum, and maximum values for red, blue and green gamma. |
| `CMVideoCardGamma` | New. Specifies video gamma data to store with a video gamma profile tag, in either table or formula format. |

Table 8-3 shows new and revised constants.

__Table 8-3__  New and revised constants in ColorSync 2.5

| Constants | Version 2.5 Notes |
| Color Packing for Color Spaces | Changed. The constants `cm48_16ColorPacking` and `cm64_16ColorPacking` were added. |
| Abstract Color Space Constants | Changed. The constants `cmRGBASpace` and `cmGrayASpace` were moved from Color Space Constants With Packing Formats. |
| Color Space Constants With Packing Formats | Changed. The constants `cmRGBASpace` and `cmGrayASpace` were moved to Abstract Color Space Constants.The constants `cmGray16Space`, `cmGrayA32Space`, `cmRGB48Space`, `cmCMYK64Space`, and `cmLAB48Space` were added. |
| Device Attribute Values for Version 2.x Profiles | Changed. The illustration was revised to show the correct ICC definitions for the `deviceAttributes` field in the `CM2Header` data structure. Unused enums were removed. |
| Video Card Gamma Tag | New. Specifies the video card gamma tag in a profile. |
| Video Card Gamma Tag Type | New. Specifies the signature type for a video card gamma profile tag. |
| Video Card Gamma Storage Type | New. Specifies whether the data in a video card gamma tag is in table or formula format. |

This section provides a brief description of new and revised code listings.

__Table 8-4__  New and revised code listings for ColorSync 2.5

| Listing | Version 2.5 Notes |
| [Listing 4-1](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2gjfduuqq),[Determining if ColorSync 2.5 is available](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2gjfduuqq) | Revised. Checks for version 2.5. |
| [Listing 4-2](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2ii5fesry),[Opening a reference to a file-based profile](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2ii5fesry) | Revised. Replaced profLoc.u.file.spec with profLoc.u.fileLoc.spec. |
| [Listing 4-3](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2ijbeeqrq),[Poor man’s exception handling macro](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2ijbeeqrq) | New. Provides the `require` macro for simple error handling. |
| [Listing 4-4](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2kirbeeqq), [Identifying the current system profile](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2kirbeeqq) | Revised. Returns `CMError` instead of `void`. Uses `require` error-handling macro. |
| [Listing 4-5](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2gjjdeeri), [Getting the profile for the main display](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2gjjdeeri) | New. Uses the new `CMGetProfileByAVID` function to get the profile for the main display. |
| [Listing 4-6](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2djbauoqq), [Matching a picture to a display](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2djbauoqq) | Revised. Formerly called both `NCMBeginMatching` and `NCMDrawMatchedPicture`. Now calls only the latter. Uses `require` error-handling macro. |
| [Listing 4-6](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2djbauoqq), [Matching a picture to a display](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2djbauoqq) | Revised. Formerly called both `CWMatchPixMap` and `CWMatchBitmap`. Now calls only the latter (fixes bug 1669727). Uses `require` error-handling macro. |
| [Listing 4-8](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2gi5beuqy), [Embedding a profile by prepending it before its associated picture](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2gi5beuqy) | Revised. Uses `require` error-handling macro. Disposes of graphics world if necessary on error condition. |
| [Listing 4-9](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2iifdugqq), [Counting the number of profiles in a picture](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2iifdugqq) | Revised. Renamed bottleneck procedures for clarity. |
| [Listing 4-10](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2hiveesqq), [Calling the CMUnflattenProfile function to extract an embedded profile](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2hiveesqq) | Revised. Uses `require` error-handling macro. Performs cleanup if necessary on error condition. |
| [Listing 4-13](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2gjfceuqy), [An iteration function for profile searching with ColorSync 2.5](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2gjfceuqy) | New. Provides an iteration function for optimized profile searching with the new `MyProfileIterateProc` function. |
| [Listing 4-14](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2ejfdeoqi), [A filter function for profile searching prior to ColorSync 2.5](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2ejfdeoqi) | New. Provides a filter function to perform profile searching with the `CMNewProfileSearch` function that mimics the optimized searching supported by the `MyProfileIterateProc` function. |
| [Listing 4-15](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2cjfeumqi), [Optimized profile searching compatible with previous versions of ColorSync](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2cjfeumqi) | New. Provides sample code that performs an optimized profile search if ColorSync 2.5 is available, but provides a compatible (though not optimized) search if it is not. |
| [Listing 5-1](Developing%20ColorSync-Supportive%20Device%20Drivers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzxfvbegskci5bussi), [Modifying a profile header’s quality flag and setting the rendering intent](Developing%20ColorSync-Supportive%20Device%20Drivers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzxfvbegskci5bussi) | Revised. Additional comments. |

This section describes new features added to version 2.1 of the ColorSync Manager. These features are documented throughout this document. If you are interested in documentation that covers only version 2.1, see [Other Color Documentation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzufvbecqsei5aumsi).

- procedure-based profiles: You can specify your own profile-access procedure that ColorSync will call when the profile is created, initialized, opened, read, updated, or closed.
- support for named color spaces: The ColorSync Manager provides data structures and routines for working with named color spaces.
- profile identifiers: The ColorSync Manager defines the profile identifier, an abbreviated data structure that identifies, and possibly modifies, a profile in memory or on disk. An embedded profile identifier requires much less space than an entire profile.
- additional PostScript support: Postscript Level 2 now supports up to four-component color spaces. This allows the creation of device-independent color space definitions that can support calibrated CMYK spaces and provide more flexible support for calibrated scanner and monitor spaces.
- color conversion without components: Color conversion routines are an integral part of the ColorSync Manager and are no longer implemented as a separate component.
- support for new bitmap formats: The ColorSync Manager supports bitmap formats for many additional color spaces, including 24-bit RGB, 32-bit RGB with an alpha last channel, and 24-bit Lab.
- profile reference counts: The ColorSync Manager maintains an internal reference count for each profile reference so that it can efficiently free private memory associated with that profile reference once it is no longer in use.
- profile changed flag: The ColorSync Manager maintains a flag that indicates whether the content of a profile has changed.
- speed and accuracy enhancements: You can use a lookup only flag to skip interpolation and speed up runtime color conversion. You can also disable gamut checking to speed up initialization and reduce profile size.
- revised sample application: A revised version of the CSDemo application provides sample code that demonstrates how to use many of the new features of ColorSync 2.1.

For a guide to the new features in version 2.1 of the ColorSync Manager, see the document What’s New in Advanced Color Imaging on the Mac OS, available with the ColorSync 2.1 SDK.

For documentation that covers only features available with ColorSync Manager 2.1 and earlier versions, see Advanced Color Imaging on the Mac OS Revised for ColorSync 2.1 and Advanced Color Imaging Reference Revised for ColorSync 2.1. These documents also describe the Color Picker Manager (Version 2.0), Color Manager, and Palette Manager.

An earlier, paper version of Advanced Color Imaging on the Mac OS, covering ColorSync through version 2.0, was published by Addison-Wesley Publishing Company. It has the catalog number ISBN 0-201-48949-X.

Technote 1100, Color Picker 2.1 describes version 2.1 of the Color Picker Manager. Note that Color Picker Manager version 2.1 works with ColorSync Manager versions 2.0 and greater.

The electronic documents described here are available at <http://developer.apple.com/>.

[Next](Document%20Revision%20History.md)[Previous](Version%20and%20Compatibility%20Information.md)

