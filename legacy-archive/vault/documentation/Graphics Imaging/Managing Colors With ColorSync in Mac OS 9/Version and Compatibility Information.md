---
title: Managing Colors With ColorSync in Mac OS 9
apple_id: TP40000896
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2003-02-01'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ManagingColorSync/VersAndCompat/VersAndCompat.html
archived_at: '2026-07-15T07:36:28.833048Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Managing Colors With ColorSync in Mac OS 9](About%20This%20Document.md)


[Next](What%E2%80%99s%20New.md)[Previous](Developing%20Color%20Management%20Modules.md)

# Version and Compatibility Information

This section describes the `Gestalt` information, shared library version numbers, CMM version numbers, and ColorSync header files you use with different versions of the ColorSync Manager. It also describes CPU and system requirements.

This section also describes backward compatibility support for ColorSync 1.0 functions, profiles, and CMMs provided by the ColorSync Manager in versions 2.0 and later.

In addition, this section explains how to use the ColorSync Manager for color matching between a ColorSync 1.0 profile and a version 2.x profile.

Version 2.5 of the ColorSync Manager replaces all earlier versions of the product, including ColorSync 2.1, 2.0, and 1.0.

Although ColorSync 1.0 used a proprietary profile format, the ColorSync Manager provides backward compatibility for applications and device drivers written for ColorSync 1.0. Your application that uses the ColorSync Manager can match, convert, and color check colors using version 2.x profiles or, when necessary, using a combination of version 2.x profiles and ColorSync 1.0 profiles.

This section describes the `Gestalt` information, shared library version numbers, CMM version numbers, CPUs, system versions, and ColorSync header files you use with different versions of the ColorSync Manager. Information is provided in the following sections:

- [Gestalt, Shared Library, and CMM Version Information](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzvfvbegskhjjeusri)
- [CPU and System Requirements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzvfvkfawcsivddcmbr)
- [ColorSync Header Files](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzvfvkfawcsivddcmbs)

For additional version information, see the section [ColorSync Versions](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvkfawcsivddcmbv) and [ColorSync and ICC Profile Format Version Numbers](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2ijbeeory).

[Table 7-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzvfvkfawcsivddcmjv) lists the version number for each release of the ColorSync Manager, along with the `Gestalt` version number, shared library version number, and `Gestalt` selector code for that version. Note that only the ColorSync version numbers and `Gestalt` version numbers are unique for each version. For more information on `Gestalt` selectors, see _ColorSync Manager Reference_.

__Table 7-1__  ColorSync Manager version numbers, with corresponding shared library version numbers and `Gestalt` selectors

| ColorSync Version | Gestalt Version | Gestalt Selector | Shared Library Version | Color Management Module (CMM) Version |
| 1.0 | $00000100 | gestaltColorSync10 | $00000000 | $00000001 |
| 1.0.3 | $00000110 | gestaltColorSync11 | $00000000 | $00000001 |
| 1.0.4 | $00000104 | gestaltColorSync104 | $00000000 | $00000001 |
| 1.0.5 | $00000105 | gestaltColorSync105 | $00000000 | $00000001 |
| 2.0 | $00000200 | gestaltColorSync20 | $02000000 | $00010001 |
| 2.0.1 | $00000200 | gestaltColorSync20 | $02000000 | $00010001 |
| 2.1.0 | $00000210 | gestaltColorSync21 | $02100000 | $00010001 |
| 2.1.1 | $00000211 | gestaltColorSync21 | $02100000 | $00010001 |
| 2.1.2 | $00000212 | gestaltColorSync21 | $02100000 | $00010001 |
| 2.5 | $00000250 | gestaltColorSync25 | $02500000 | $00010002 |
| 2.5.1 | $00000251 | gestaltColorSync251 | $02500000 | $00010002 |

Table 7-2 lists the CPU and system requirements for each release of the ColorSync Manager.

__Table 7-2__  ColorSync Manager CPU and system requirements

| ColorSync Version | CPU | System Version |
| 1.0, 1.0.3, 1.0.4, 1.0.5 | 68K or PowerPC | On 68K, requires either System 7.0 or System 6.0.7 with 32-bit QuickDraw, version 1.2.For PowerPC, requires System 7.0. |
| 2.0, 2.0.1, 2.1.0, 2.1.1, 2.1.2 | 68020 or greater or PowerPC | Requires System 7.0 or greater with Color QuickDraw. |
| 2.5, 2.5.1 | 68020 or greater or PowerPC | Requires System 7.6.1 or greater. |

Table 7-3 describes the ColorSync Manager header files. Note that some header files are no longer used or are not recommended.

__Table 7-3__  ColorSync header files

| Header File | Description | First Used | Status |
| CMAcceleration.h | CMM acceleration component interface. | 2.0 | Not used starting with 2.1. |
| CMApplication.h | ColorSync Manager functions, constants, and data types for applications, device drivers, and CMMs. | 1.0 | Supported. |
| CMCalibrator.h | Interface for developing monitor calibrator plug-ins. | 2.5 | Supported, but not documented here. |
| CMComponent.h | Old component interface for CMMs. Replaced by CMMComponent.h. | 1.0 | Not used starting with 2.0. |
| CMConversions.h | Component interface for old-style conversion routines. | 2.0 | Supported, but not recommended starting with 2.1. |
| CMICCProfile.h | Constants and data types for working with ICC profiles. | 1.0 | Supported. |
| CMMComponent.h | Component interface for ColorSync CMMs. | 1.0 | Supported. |
| CMPRComponent.h | Component interface for ColorSync 1.0 profile responders. | 1.0 | Supported, but not recommended starting with 2.0. |
| CMScriptingPlugin.h | Interface for developing scripting plug-ins. | 2.5 | Supported, but not documented here. |

The following sections describe backward compatibility for ColorSync Manager versions greater than 2.0.

Existing code written to use version 2.1 of the ColorSync Manager should continue to work with ColorSync 2.5 without modification. Existing code may operate more efficiently in some cases due to optimizations provided with version 2.5, especially for multiple processors, as described in [When ColorSync Uses Multiple Processors](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2gifcecqq). However, existing code can not take full advantage of some new features; for example, see [The Profile Cache and Optimized Searching](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2cijceory).

For a guide to the new features in version 2.5 of the ColorSync Manager, see [New Features in ColorSync Manager Version 2.5](What%E2%80%99s%20New.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzufvbecqsfirceqri).

Existing code written to use version 2.0 of the ColorSync Manager should continue to work with ColorSync 2.1 without modification, although it will not necessarily take advantage of the new features described in [New Features in ColorSync Manager Version 2.1](What%E2%80%99s%20New.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzufvbecqsfjjbesra). For example, code written for ColorSync version 2.0 cannot use the profile identifier, an abbreviated data structure that identifies, and possibly modifies, a profile in memory or on disk. An embedded profile identifier requires much less space than an entire profile.

The ColorSync Manager continues to fully support the ColorSync 1.0 interface, including the ColorSync 1.0 profile responder. Note, that this support is provided primarily for backward compatibility. If you are writing new code, you should take advantage of the many new features added between version 2.0 and version 2.5. However, existing applications and drivers that use ColorSync 1.0 functions will continue to work properly, as will ColorSync 1.0 profiles, ColorSync 1.0 CMMs, and QuickDraw GX 1.0.

Although newer versions of the ColorSync Manager continue to support use of the profile responder from ColorSync 1.0, this feature is not supported by the ColorSync Manager interface.

The ColorSync Manager continues to support the use of ColorSync 1.0 profiles. For example, you should always use ColorSync 1.0 functions with ColorSync 1.0 profiles, if possible. For example, always use ColorSync 1.0 functions to match colors between the color gamuts of two devices if both devices have ColorSync 1.0 profiles. The four ColorSync 1.0 functions and their new counterparts are listed in Table 7-4.

However, there are times when you may need to use a ColorSync 1.0 profile with a ColorSync 2.x function. The ColorSync Manager�s backward compatibility allows you to do this. For example, a document containing an image to be color matched may include an embedded ColorSync 1.0 source profile for the image. To match the colors of the source image to a device that has a version 2.x profile, you must use 2.x functions because ColorSync 1.0 functions cannot gain access to a version 2.x profile.

One of the main differences between ColorSync 1.0 and 2.x functions is the profile format used. The 2.x functions accommodate ColorSync 1.0 profiles so that you can use those profiles if you must. Before describing how to use a ColorSync 1.0 profile with the 2.x functions, this section explains the differences between the ColorSync 1.0 profile format and the version 2.x profile format defined by the International Color Consortium (ICC) and used by the ColorSync Manager.

The ColorSync 1.0 profile format was designed by Apple Computer. This profile is memory resident and follows an internal structure based on tables. Although it is an open format, it is not an industry standard.

The ICC profile format implemented in the ColorSync Manager is significantly different from the profile format implemented for ColorSync 1.0. The version 2.x profile format is specified by the ICC and provides an industry standard that allows for interoperability across platforms and devices. A version 2.x profile created for a particular device can be used on systems running different operating systems.

Because the ColorSync 1.0 and version 2.x profile formats differ, the ColorSync Manager must resolve any compatibility issues involving accessing profiles and color matching between profiles. The next section describes how these profile formats differ.

A ColorSync 1.0 profile is smaller than a version 2.x profile and can therefore reside in memory. It is handle-based. A version 2.x profile as implemented by the ColorSync Manager is commonly file-based, but it can also be memory-based. You use an abstract internal data structure, called a profile reference, to access a version 2.x profile.

A ColorSync 1.0 profile contains a header, a copy of the Apple `CMProfileChromaticities` record, profile response data for the associated device, and a profile name string for use in dialog boxes. Custom profiles may also have additional, private data. ColorSync 1.0 defines the following profile data structure:

```

struct CMProfile {
    CMHeader                    header;
    CMProfileChromaticities     profile;
    CMProfileResponse           response;
    CMIString                   profileName;    /* variable length */
    char                        customData[anyNumber];
                                        /* optional custom CMM data */
};
```

The `response` data fields contain nine tables. The first table is for grayscale values. The next three are red, green, and blue values, followed by three for cyan, magenta, and yellow values. The eighth and ninth tables are for CMYK printers requiring undercolor removal and black generation data.

The ColorSync 1.0 profile header, defined by the data structure CMHeader, and the version 2.x profile header, defined by the structure CM2Header, contain many fields in common. However, some fields in the ColorSync 1.0 profile header reflect its table-based nature, while a version 2.x profile has a tagged-element structure. A version 2.x profile also supports use of lookup table transforms that allow for faster processing.

Although version 2.x of the ColorSync Manager supports using a mix of ColorSync 1.0 and version 2.x profiles, the success of a matching session involving a ColorSync 1.0 profile depends on the CMM component performing the process. Third-party CMMs may choose not to support ColorSync 1.0 profiles. The default CMM is able to establish a matching session involving one or more ColorSync 1.0 profiles.

For device link profiles, you must include only version 2.x profiles. You cannot mix ColorSync 1.0 and version 2.x profiles in a device link profile.

The ColorSync Manager provides the CMConvertProfile2to1 function to convert 2.x format profiles to the 1.0 profile format. Because 1.0 and 2.x scanner and monitor profiles generally carry the same required color information, no accuracy is lost in converting from one to the other. With printer profiles, however, some accuracy will be lost by conversion, leading to significantly different results. Because of the possible loss of accuracy in some cases, 2.x to 1.0 profile conversion is not encouraged.

Despite differences between the version 2.x and ColorSync 1.0 profile formats, you can use most of the ColorSync Manager 2.x functions to gain access to ColorSync 1.0 profiles and their contents and to color match to and from the two disparate profile formats, if necessary. The ColorSync Manager makes this possible.

You can open a reference to a ColorSync 1.0 profile using 2.x functions and special data structures that accommodate both profile styles. You can also match the colors of an image expressed in the color gamut of one device whose characteristics are described by a ColorSync 1.0 profile to the colors within the gamut of another device whose characteristics are described by a version 2.x profile.

- which version 2.x functions you cannot use for ColorSync 1.0 profiles
- how you can use the ColorSync Manager with ColorSync 1.0 profiles

You cannot use the ColorSync Manager�s `CMUpdateProfile` function to update a ColorSync 1.0 profile. The ColorSync Manager does not provide functions for profile version conversions. This is the domain of profile-building tools and calibration applications.

The ColorSync Manager 2.x versions provide a set of functions to search the ColorSync Profiles folder for specific profiles that meet search criteria. These functions act on version 2.x profiles only. If the ColorSync Profiles folder contains ColorSync 1.0 profiles, these functions do not acknowledge them or return results that include them. The 2.x search functions, which are not supported for ColorSync 1.0 functions, are the CMIterateColorSyncFolder, CMNewProfileSearch, CMUpdateProfileSearch, CMDisposeProfileSearch, CMSearchGetIndProfile, CMSearchGetIndProfileFileSpec, CMProfileIdnetifierFolderSearch, and CMProfileIdentifierListSearch functions.

You cannot use the ColorSync Manager�s `NCMUseProfileComment` function to generate automatically the picture comments required to embed a ColorSync 1.0 profile. This function is designed to work with version 2.x profiles only.

You can use versions 2.0 and higher of the ColorSync Manager to match a document image with an embedded 1.0 source profile to the color gamut of a printer defined by a version 2.x profile. Newer versions of the ColorSync Manager are able to contend with both profile formats.

The sections that follow explain how to obtain a reference to the ColorSync 1.0 profile, get the profile�s header, and get its synthesized tags.

To use a ColorSync 1.0 profile, you must obtain a reference to the profile. Obtaining a reference to the profile is synonymous with opening the profile for your program�s use. If the profile is embedded in a document, you must extract the profile before you can open it.

You can use the `CMOpenProfileFile` function to obtain a reference to a ColorSync 1.0 profile. Other ColorSync Manager functions that you use to gain access to the profile�s contents or perform color matching based on the profile require the profile reference as a parameter.

After you obtain a reference to a profile, you can gain access to the profile�s contents. To gain access to the contents of any of the fields of a profile header, you must get the entire header. The ColorSync Manager allows you to do this using the `CMGetProfileHeader` function. You pass this function the profile reference and a data structure to hold the returned header. The ColorSync Manager defines the following union of type `CMAppleProfileHeader,` containing variants for ColorSync 1.0 and version 2.x ColorSync profile headers for this purpose:

```
union CMAppleProfileHeader {
    CMHeader        cm1;
    CM2Header       cm2;
};
```

You use the `cm1` variant for a ColorSync 1.0 profile header. You can easily test for the version of a profile header to determine which variant to use because the offset of the header version is at the same place for both ColorSync 1.0 profiles and version 2.x profiles.

The ColorSync Manager provides four tags to allow you to obtain four ColorSync 1.0 profile elements pointed to from the profile header or contained outside the header. To obtain the profile element, you specify its associated tag signature as a parameter to the `CMGetProfileElement` function along with the profile reference. The ColorSync Manager provides the following enumeration that defines these tags:

```
enum {
        cmCS1ChromTag   = 'chrm',
        cmCS1TRCTag     = 'trc ',
        cmCS1NameTag    = 'name',
        cmCS1CustTag    = 'cust'
};
```

**`cmCS1ChromTag`**
: Profile chromaticities tag signature. Element data for this tag specifies the XYZ chromaticities for the six primary and secondary colors (red, green, blue, cyan, magenta, and yellow).

**`cmCS1TRCTag`**
: Profile response data tag signature. Element data for this tag specifies the profile response data for the associated device.

**`cmCS1NameTag`**
: Profile name string tag signature. Element data for this tag specifies the profile name string. This is an international string consisting of a Macintosh script code followed by a length byte and up to 63 additional bytes composing a text string that identifies the profile.

**`cmCS1CustTag`**
: Custom tag signature. Element data for this tag specifies the private data for a custom CMM.

In ColorSync 1.0, picture comment types `cmBeginProfile` and `cmEndProfile` are used to begin and end a picture comment.

The `cmEnableMatching` and `cmDisableMatching` picture comments are used to begin and end color matching in ColorSync 1.0 and in newer versions of the ColorSync Manager.

Starting with version 2.0, the ColorSync Manager implements new versions of four of the functions supported by ColorSync 1.0. In the new version of these functions, for example, a parameter used to specify a profile takes a profile reference.

It is easy to spot a ColorSync 2.x function that is a new version of a ColorSync 1.0 function, because the function name begins with an uppercase letter N, signifying that it is new. The four ColorSync 1.0 functions and their new counterparts are listed in Table 7-4.

__Table 7-4__  ColorSync 1.0 functions and their ColorSync Manager counterparts

| ColorSync 1.0 function | ColorSync 2.x function |
| pascal CWNewColorWorld (CMWorldRef \*cw, CMProfileHandle src, CMProfileHandle dst); | pascal CMError NCWNewColorWorld (CMWorldRef \*cw, CMProfileRef src, CMProfileRef dst); |
| pascal CMError CMBeginMatching (CMProfileHandle src, CMProfileHandle dst, CMMatchRef \*myRef); | pascal CMError NCMBeginMatching (CMProfileRef src, CMProfileRef dst, CMMatchRef \*myRef); |
| pascal void CMDrawMatchedPicture (PicHandle myPicture, CMProfileHandle dst, Rect \*myRect); | pascal void NCMDrawMatchedPicture (PicHandle myPicture, CMProfileRef dst, Rect \*myRect); |
| pascal CMError CMUseProfileComment (CMProfileHandle profile); | pascal CMError NCMUseProfileComment (CMProfileRef prof, unsigned long flags); |

If you are writing a new ColorSync-supportive program, you should always use the new ColorSync Manager functions. The ColorSync 1.0 version of these functions will not be supported indefinitely in new releases of the ColorSync Manager.

[Next](What%E2%80%99s%20New.md)[Previous](Developing%20Color%20Management%20Modules.md)

