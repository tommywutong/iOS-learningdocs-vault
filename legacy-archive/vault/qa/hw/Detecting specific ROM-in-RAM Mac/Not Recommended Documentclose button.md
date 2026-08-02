---
title: Detecting specific ROM-in-RAM Mac
apple_id: DTS10001321
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-10-05'
source_url: https://developer.apple.com/library/archive/qa/hw/hw49.html
archived_at: '2026-07-18T02:29:37.651825Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/HardwareDrivers/index.html) > [Apple Hardware](https://developer.apple.com/library/archive/technicalqas/HardwareDrivers/idxAppleHardware-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > Apple Hardware](https://developer.apple.com/referencelibrary/HardwareDrivers/idxAppleHardware-date.html)

|  |
| --- |
| Technical Q&A HW49Detecting specific ROM-in-RAM Mac |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ---   __Q:__ All ROM-in-RAM (New World) Macs return 406 (decimal) as their machine ID from `Gestalt`. How do I determine which Mac my software is running on in this case?  __A:__ You will have to query the Name Registry to get this information.    |  | | --- | | __IMPORTANT:__  Do not attempt to infer if a feature exists by checking the machine ID. Use the Name Registry or `Gestalt` to determine if a specific feature exists. If checking the machine ID is the only way to determine if a specific feature exists, [file a bug report with us](https://developer.apple.com/bugreporter/) so that we can fix that. |    You can get the Mac's non-localized name from the `compatible` property. The value is an array of C-style strings, and the name is the first entry of the property's value. The `compatible` property is found at the path "Devices:device-tree". For the 1999 Power Macintosh G3 this value is "PowerMac1,1". For the iMac this value is "iMac,1".    |  | | --- | | __Note:__  This string is not meant to be shown to the user. It is not localized. Do not show this string to the user. |    Because these strings are not localized, you can easily test them; just don't show them to the user.    |  | | --- | | __Note:__  Currently, all iMacs have the same compatible property value: "iMac,1". |    To tell the difference between the original iMac with the Rage II video chip and the second revision of the iMac with the Rage Pro video chip, you can look for a Name Registry node of "Devices:device-tree:pci:ATY,RageIIC_C" or "Devices:device-tree:pci:ATY,RagePro_C", respectively. You can also search for a node with a `name` property of "ATY,RageIIC_C" or "ATY,RagePro_C", respectively. Either method will work with equal effectiveness.  To tell the difference between the 233MHz iMac with a Rage Pro video chip and the 266MHz iMac (which also has a Rage Pro video chip), you will need to check the `clock-frequency` property in the CPU node. The best way to do this is to search for a node with a `device_type` property with the value of "cpu\0" (the null terminator of the C string needs to be passed; it is part of the property's value). Once you have found the node with the CPU value, you can get the value of the `clock-frequency` property which is in the same node. You cannot just search for "clock-frequency" because there are many "clock-frequency" entries in the Name Registry and you are not guaranteed that the "clock-frequency" value you get is the one from the CPU node.  Important: I hope that the above serves to show how strongly we suggest that you __do not__ try to identify specific Macs. Instead you should look for specific features (via `Gestalt`, or some other means) that you need, such as FireWire or USB, rather than assuming that they are present based solely on the model of the computer.  You should always check for what you want, rather than assume a specific machine always has the feature you want. If you believe that you cannot check for a specific feature and are therefore relying on the machine ID, please [file a bug with us](https://developer.apple.com/bugreporter/) so that we can have a selector added.   |  | | --- | | ``` /* GetMacName returns a Pascal-formatted string with the model property string.  * Input  macName - pointer to a buffer where the model property name  *                  will be returned, if the call succeeds  *  * Output function result - noErr indicates that the model name was  *                          read successfully  *        macName - will contain the model name property if noErr  *  * Notes:  *    Caller is responsible for disposing of macName. Use DisposePtr.  */ OSStatus GetMacName (StringPtr * macName) {     OSStatus                err             = noErr;     RegEntryID              compatibleEntry;     RegPropertyValueSize    length;     RegCStrEntryNamePtr     compatibleValue;      if (macName != nil) {         *macName = 0;          err = RegistryEntryIDInit (&compatibleEntry);          if (err == noErr) {             err = RegistryCStrEntryLookup (nil, "Devices:device-tree",                 &compatibleEntry);         }          if (err == noErr) {             err = RegistryPropertyGetSize (&compatibleEntry,                 "compatible", &length);         }          if (err == noErr) {             compatibleValue = (RegCStrEntryNamePtr)NewPtr (length);             err = MemError ();         }          if (err == noErr) {             err = RegistryPropertyGet (&compatibleEntry,                 "compatible", compatibleValue,             &length);         }          if (err == noErr) {             SetPtrSize (compatibleValue, strlen (compatibleValue) + 1);             /* SetPtrSize shouldn't fail because we are shrinking the pointer,             but make sure. */             err = MemError ();         }          if (err == noErr) {             *macName = c2pstr (compatibleValue);         }          (void)RegistryEntryIDDispose (&compatibleEntry);     }      return err; }  /* GetMacSpeed returns the clock-frequency property of the CPU  * Output function result - noErr indicates that the CPU clock-frequency  *                    property was read successfully  *        cpuFreq   - will contain the clock-frequency property if noErr  *                    set to 0 if the clock-frequency could not be read */ OSStatus GetMacSpeed (UInt32 * cpuFreq) {     OSStatus                err             = noErr;     RegEntryID              cpuEntry;     RegEntryIter            cookie          = nil;     RegEntryIterationOp     iterOp          = kRegIterDescendants;     unsigned long           cpuSpeedSize    = sizeof (unsigned long);     char *                  cpuValue        = "cpu";     Boolean                 done;      if (cpuFreq != nil) {         *cpuFreq = 0;     } else {         cpuSpeedSize = 0;     }      if (err == noErr) {         err = RegistryEntryIDInit (&cpuEntry);     }      if (err == noErr) {         err = RegistryEntryIterateCreate (&cookie);     }      if (err == noErr) {         err = RegistryEntrySearch (&cookie, iterOp,             &cpuEntry, &done, "device_type",              cpuValue, strlen (cpuValue) + 1);          if (done != true && err == noErr) {             (void)RegistryPropertyGet (&cpuEntry,                 "clock-frequency", cpuFreq, &cpuSpeedSize);         }     }      (void)RegistryEntryIDDispose (&cpuEntry);     (void)RegistryEntryIterateDispose (&cookie);      return err; } ``` |   This is some sample code that shows how to query the Name Registry for the name and clock frequency values. |

#### [Oct 05 1999]

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
