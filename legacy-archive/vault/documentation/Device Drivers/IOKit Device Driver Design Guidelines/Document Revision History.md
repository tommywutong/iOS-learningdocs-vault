---
title: IOKit Device Driver Design Guidelines
apple_id: TP30000694
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2009-08-14'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingDeviceDriver/RevisionHistory/RevisionHistory.html
archived_at: '2026-07-15T07:31:53.069170Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [IOKit Device Driver Design Guidelines](Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md)


[Next](Index.md)[Previous](Glossary.md)

# Document Revision History

This table describes the changes to _IOKit Device Driver Design Guidelines_.

| __Date__ | __Notes__ |
| 2009-08-14 | Changed links from KPI Reference to Kernel Framework Reference. |
| 2007-03-06 | Made minor corrections. |
| 2006-11-07 | Updated information on building a universal I/O Kit device driver. |
| 2006-10-04 | Added information on debugging on an Intel-based Macintosh and noted that KUNC APIs are unavailable to KEXTs that depend on KPIs. |
| 2006-06-28 | Made minor corrections. |
| 2006-05-23 | Made minor corrections. |
| 2006-04-04 | Clarified the location of the AppleGMACEthernet driver source code. |
| 2005-12-06 | Made minor corrections. |
| 2005-10-04 | Made minor bug fixes. |
| 2005-09-08 | Added a chapter on creating a universal binary version of an I/O Kit device driver. |
| 2005-08-11 | Made minor bug fix. Changed title from "Writing an I/O Kit Device Driver". |
| 2005-04-29 | Added description of new way to break into kernel debugging mode in OS X v. 10.4. |
| 2005-04-08 | Fixed typos. Reorganized Introduction chapter and added note that Objective-C does not supply I/O Kit interfaces. |
| 2004-05-27 | Changed outdated links, removed references to `OSMetaClass::failModLoad()` method. |
| 2003-10-10 | Added information about changes in memory subsystem to support 64-bit architectures. Added a link to the AppleGMACEthernet driver source code. |
| 2003-09-18 | Added definition of `kAny` constant in code listing 4-20, corrected property-key name `device_type` to `device-type`, added description of the default implementation of `newUserClient` method. |
| 2003-05-15 | Added note that a symboled kernel is required for the kernel debugging macros to work. Added link to Kernel Debug Kit. |
| 2002-11-01 | First publication. |

[Next](Index.md)[Previous](Glossary.md)

