---
title: GetDriverDiskFragment and 'ndrv' Drivers
apple_id: DTS10001287
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-15'
source_url: https://developer.apple.com/library/archive/qa/hw/hw15.html
archived_at: '2026-07-18T02:29:35.866507Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > PCI and PC Card](https://developer.apple.com/referencelibrary/HardwareDrivers/idxPCIandPCCard-date.html)

|  |
| --- |
| Technical Q&A HW15GetDriverDiskFragment and 'ndrv' Drivers |

|  |
| --- |
| ---   Q: I have been successfully using `RenameDriver()` in my `'INIT'` using the PCI Power Macintosh DDK, Version B4. However, when I load my driver from an `'INIT'` file type using `GetDriverDiskFragment()` and `InstallDriverFromFragment()`, the only property added or updated in the device tree is the driver-ref property. `GetDriverDiskFragment()` and `InstallDriverFrom Fragment()` could be changed to add the same properties that the `'ndrv'` adds. Why aren't the same properties added when I use `GetDriverDiskFragment()` and `InstallDriverFrom Fragment()` as the `'ndrv'`?  In my other `'INIT'`, I used `DetachResource()` for handles. If I use the combination of `GetDriverMemoryFragment()` and `InstallDriverFromFragment()`, do I need to use a routine call to disassociate the first `Ptr` argument in `GetDriverMemoryFragment()` from the `'INIT'`, and if so, what routine should I call?  A: Although `GetDriverDiskFragment` was created for family experts, use this call for `'ndrv'` drivers, if you want to. `GetDriverDiskFragment` does not put the same properties in the device tree as `'ndrv'` drivers do, because it was not designed to be used with `'ndrv'` drivers. After you have your properties in the `NameRegistry` by using `GetDriverDiskFragment`, you can add additional ones. See _Designing PCI Cards & Drivers for Power Macintosh Computers_, in the chapter on NameRegistry, for more information.  When you make a call to `GetDriverMemoryFragment` in your INIT, and you have a pointer that you created in your code, you are responsible for disposing of that pointer, just like any other pointer you create. To free up the storage you created, make a call to `DisposePtr`. |

#### [Jul 15 1995]

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
