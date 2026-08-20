---
title: Managing Colors With ColorSync in Mac OS 9
apple_id: TP40000896
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2003-02-01'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ManagingColorSync/PrefaceCS/PrefaceCS.html
archived_at: '2026-07-15T07:36:28.822646Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Overview%20of%20Color%20and%20Color%20Management%20Systems.md)

# About This Document

This document describes ColorSync, the color management system from Apple Computer, Inc. that provides essential services for fast, consistent, and accurate color management. It also describes the ColorSync Manager, the application programming interface (API) to these services.

This Preface covers:

- [What’s in This Document](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenbzfvbeeq2jjfaukry)
- [Conventions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenbzfvbeeq2hizduiqi)
- [Important Note on Code Listings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenbzfvbeeq2diveeuri)

For additional information about this document, see What’s New.

This document introduces ColorSync and the concepts of color management, shows how to use ColorSync in applications and device drivers, and provides an overview of developing color management modules (CMMs). It describes features available through ColorSync version 2.5. Most existing code written to use version 2.0 or 2.1 of the ColorSync Manager should continue to work with version 2.5 without modification.

This document includes the following sections, as well as a glossary and index.

- [Overview of Color and Color Management Systems](Overview%20of%20Color%20and%20Color%20Management%20Systems.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydeobqfvbeeq2cirduira) provides a general introduction to color-management, defines terms such as profile, color space, and CMM, and serves as a primer for those unfamiliar with color management systems.
- [Overview of ColorSync](Overview%20of%20ColorSync.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzzfvbeeq2gi5euesi) provides an overview of ColorSync and the ColorSync Manager, including both user interface and API elements. It describes ColorSync’s support for scripting, monitor calibration, the use of multiple processors, and other features.
- [Developing ColorSync-Supportive Applications](Developing%20ColorSync-Supportive%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzyfvbeeq2kinbeqra) describes how your application can use the ColorSync Manager to provide many color management services. It includes detailed code samples.
- [Developing ColorSync-Supportive Device Drivers](Developing%20ColorSync-Supportive%20Device%20Drivers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzxfvbegskii5duosi) describes how you can use the ColorSync Manager to create ColorSync-supportive drivers for peripherals such as input, output, and display devices.
- [Developing Color Management Modules](Developing%20Color%20Management%20Modules.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzwfvbegskei5cueqy) describes how to create a color management module (CMM) component that ColorSync can use to match and check colors.
- [Version and Compatibility Information](Version%20and%20Compatibility%20Information.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzvfvbegskjinbusqq) describes the `Gestalt` information, shared library version numbers, CMM version numbers, and ColorSync header files you use with different versions of the ColorSync Manager. It also describes CPU and system requirements. In addition, it describes backward compatibility between versions of the ColorSync Manager and the profile formats they use.
- [What’s New](What%E2%80%99s%20New.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzufvbecqskjfcesrq) lists the new features available with ColorSync 2.5 and provides links to new and revised material. It includes a summary of new and changed code listings, functions, data types, and constants. It also includes a list of features new to ColorSync version 2.1, as well as information on where to obtain documentation for other color-related technologies.

This document uses the following conventions to help you locate information.

Functions and data types that are changed or not recommended in ColorSync version 2.5 generally contain a VERSION NOTES section that summarizes the changes or points to related information.

All code listings, reserved words, and the names of actual data structures, constants, fields, parameters, and routines are shown in a monospaced font such as Letter Gothic (`this is Letter Gothic`).

Words that appear in boldface are key terms or concepts and are defined in the glossary.

There are several types of notes used in this document.

All code listings in this document are shown in C, except for listings that describe resources, which are shown in Rez-input format. Many listings are from the CSDemo application, which is available with the ColorSync 2.5 SDK. See Figures, Tables, and Listings for the locations of all code listings in this document.

[Next](Overview%20of%20Color%20and%20Color%20Management%20Systems.md)

