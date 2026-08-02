---
title: Interrupt Management
apple_id: DTS10001280
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-15'
source_url: https://developer.apple.com/library/archive/qa/hw/hw10.html
archived_at: '2026-07-18T02:29:35.581593Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > PCI and PC Card](https://developer.apple.com/referencelibrary/HardwareDrivers/idxPCIandPCCard-date.html)

|  |
| --- |
| Technical Q&A HW10Interrupt Management |

|  |  |
| --- | --- |
| ---   Q: I am having trouble with Interrupt Management in my native ndrv. I can get it to work once using the `GetInterruptFunctions()` and `InstallInterruptFunctions()` calls, but I can't undo this Interrupt install/enable sequence so that I can turn them on again later. In fact, it crashes the second time I use the install/enable sequence. Do I need to handle the default enabler and/or disabler differently in order to make the process repeatable?  A: The code sample below shows how to handle interrupt installation:   |  | | --- | | ``` /* =================================================================== GraphicsOSSInstallVBLInterrupts()   This routine is specific for VBL interrupts and assumes that   a driver's 'driver-ist' only pertains to VBL's. The Video   Services Library (VSL) kHBLService and kFrameService are ignored.   Interrogate the HAL to get the interrupt handler, the interrupt   enabler, the interrupt disabler, and the VBL 'refCon' (private HAL   data that the HAL might need to carry out the functions).   This version of GDX interrupt handling isolates the HAL from knowing   stuff about how the handlers are installed. Conventions interrupt   routines must follow:       interrupt handler:  clear the hw interrupt source       interrupt enabler:  enable the hw interrupt source       interrupt disabler: disable the hw interrupt source and:          return true if interrupts were enabled  before the call          return false if interrupts were disabled before the call             ->   regEntryID      Name Registry RegEntryID that                                   should  have the propertyName  ========================================================================== */ GDXErr GraphicsOSSInstallVBLInterrupts(RegEntryID *regEntryID) {      Boolean installVBLInterrupts;     InterruptEnabler enabler;     InterruptDisabler disabler;      OSSData *ossData;      GDXErr err;          /* Ask HAL if OSS should install VBL routines */     installVBLInterrupts = false;          /* Use default enabler if HAL's enabler is NULL */     enabler = NULL;      ossData = GraphicsOSSGetOSSData();          /* Use default disabler if HAL's disabler is NULL */     disabler = NULL;      err = GraphicsHALGetVBLInterruptRoutines(         &installVBLInterrupts,         &ossData->chainDefault,         &ossData->halVBLHandler,         &ossData->halVBLEnabler,         &ossData->halVBLDisabler,         &ossData->vblRefCon);      if (err != noErr)         goto ErrorExit;      if (installVBLInterrupts) {              /* The OSS should handle the HAL's vbl interrupts             It is possible that OSS should install the routines             but doesn't have the InterruptSetMember */          if (ossData->hasInterruptSetMember) {             InterruptServiceIDType vslServiceID;             OSStatus osStatusErr;             OSErr osErr;              osStatusErr = GetInterruptFunctions(                 ossData->interruptSetMember.setID,                 ossData->interruptSetMember.member,                 &ossData->defaultRefCon,                 &ossData->defaultVBLHandler,                 &ossData->defaultVBLEnabler,                 &ossData->defaultVBLDisabler );              if (osStatusErr != noErr) {                 err = kGDXErrOSSNoDefaultVBLRoutines;                 goto ErrorExit;             }                 /* If the HAL's enabler/disabler functions are                 NULL, that indicates that the HAL can use the                 default enabler/disabler function. Otherwise,                 the OSS enabler/disabler functions will be                 installed. NOTE: Making a call to                 InstallInterruptFunctions() with NULL as the                 enabler/disabler,  than the enablers currently                 installed (the 'default enablers') are used. */              if (NULL != ossData->halVBLEnabler)                 enabler = GraphicsOSSVBLInterruptEnabler;              if (NULL != ossData->halVBLDisabler)                 disabler = GraphicsOSSVBLInterruptDisabler;              osStatusErr = InstallInterruptFunctions(                 ossData->interruptSetMember.setID,                 ossData->interruptSetMember.member,                 ossData->vblRefCon,                 GraphicsOSSVBLInterruptHandler,                 enabler, disabler);              if (osStatusErr != noErr) {                 err = kGDXErrOSSUnableToInstallVBLRoutines;                 goto ErrorExit;             }             // Successfully installed the routines.             ossData->installedHALVBLRoutines = true;          } else {             err = kGDXErrOSSNoISTProperty;             goto ErrorExit;         }      } ErrorExit:      return err; } ``` | |

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
