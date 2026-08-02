---
title: OT Driver returns EINVAL error for TCP/IP program, but AppleTalk works fine
apple_id: DTS10001461
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-03-14'
source_url: https://developer.apple.com/library/archive/qa/nw/nw49.html
archived_at: '2026-07-18T02:29:46.928755Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A NW49OT Driver returns EINVAL error for TCP/IP program, but AppleTalk works fine |

|  |  |  |
| --- | --- | --- |
| ---   Q: I've developed a DLPI driver to support my network hardware product under Open Transport. In testing the driver, I have no problem with supporting AppleTalk, but when I try to access TCP services, error -3221 is always returned no matter what TCP/IP application is used. What's happening?  A: The most common reason for this error is that in setting up the TCP/IP stack, the TCP/IP configurator makes a check which is not made while setting up the AppleTalk stack. The configurator verifies that the `fModuleName` registered in the `OTPortRecord` for the port, matches the module name that is set in the `module_info` global from the DLPI driver. If the two names do not match exactly, the configuration fails and error -3221 is returned to the `OpenEndpoint` call.  This problem is most easily corrected by examining the `module_info` global, and verifying that the `fModuleName` field matches the module name entered for the corresponding port record. To access the port record, [here is a sample application you can download](https://developer.apple.com/library/archive/qa/nw/downloads/ot_dpr.hqx) (along with source code) which displays all of the registered port records for a system, along with the associated port name and module name.  When Open Transport makes the `OTRegisterPort` call to a PCI card, the module name used is the "name" Name Register property for the card. If, however, you have developed a custom port scanner for your card, then the module name will be whatever is passed in the `fModuleName` field of the Port Record structure passed to the `OTRegisterPort` call.  Under PC Card Manager 3.0, the network driver expert first looks into the Name Registry to check whether a custom enabler for the network card has registered a "port-module" property (C-String). If so, then this property will be used in the `fModuleName` field of the `OTPortRecord` card that is passed to the `OTRegisterPort` call to have OT recognize the new device. If there is no "port-module" Name Registry property created for the card by a custom enabler, then the PC Card Manager expert will build the name to register with `OTRegisterPort`, from the "name" property (with some minor modifications).  For example, suppose the "name" property initially looks something like:   |  | | --- | | ``` ethernet,pc1,MY ETHERNET CARD ``` |   The PC Card Manager 3.0 expert will truncate this name to:   |  | | --- | | ``` pc1,MY ETHERNET CARD ``` |   This happens because the module name must be a string no longer than 31 characters. The `ethernet,` portion of the string will be truncated in order to reduce the length of the module name. If you are unaware that this is happening, you may enter the wrong name into the `module_info` record, instead of the right name, `pc1,MY ETHERNET CARD`.  The result is that the registered `fModuleName` will not match that of the name in the `module_info` record, the TCP/IP configuration module name check fails, and the `EINVAL` error is returned. |

#### [Mar 14 1997]

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
