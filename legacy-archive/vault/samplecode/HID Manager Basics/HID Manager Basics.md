---
title: HID Manager Basics
apple_id: DTS10000444
resource_type: Sample Code
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2003-07-10'
source_url: https://developer.apple.com/library/archive/samplecode/HID_Manager_Basics/Introduction/Intro.html
archived_at: '2026-07-18T03:11:20.095709Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](CarbonInclude.h.md)

# HID Manager Basics

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-07-10 Shows basic use of HID Manager for Mac OS X: including device discovery, queues and polling elements. |
| __Build Requirements:__ | Xcode 2.1 |
| __Runtime Requirements:__ | Mac OS X |

HID Manager Basics
Sample code to accompany HID Documantation
Version 1.2
10-23-2002
Version 1.2: Verified functionality on Mac OS X 10.2 & new HID Utilities
Version 1.1: Verified functionality on Mac OS X 10.1.
Version 1.0: Initial version shows all the functionality in HID documantation and corrects a few errors in documentation code.
Also functions are slightly renamed and organization cleaned up for readability and straightforwardness. Documentation
can be found on the web in the Mac OS X kernel documentation section under Accessing Hardware.
----
HID Manager Basics shows the very basic use of the HID Manager for Mac OS X. This includes device discovery, using queues and polling elements.
This code is NOT designed to be production quality and serves to just support the HID documentation, with minor changes to improve interaction.
Other sample code, such as the HID Utilities Source, HID Config Save and HID Explorer, are MUCH better examples of using the HID Manager in a production
application environment. It is strong recommended developers look at those samples when starting to use the HID manager.
The code should be built and run from Project builder and the output will be in the Run pane. The application will make little sense if the stdout window is
not visible when the application is run so it is suggested it be run from Project Builder.
----
HID Manager Basics is provided as sample code and will be updated if possible for bug fixes but will not have it's functionality changed unless the HID Manager
documentation changes.
Any suggestions and/or bugs can be directed to the Apple bug reporter at:
<http://developer.apple.com/bugreporter/index.html>

[Next](CarbonInclude.h.md)

