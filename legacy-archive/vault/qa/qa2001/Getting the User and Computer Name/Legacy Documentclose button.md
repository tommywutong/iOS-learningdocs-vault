---
title: Getting the User and Computer Name
apple_id: DTS10001630
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: CoreServices
published: '2001-10-30'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1078.html
archived_at: '2026-07-18T02:38:11.108725Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Networking](https://developer.apple.com/referencelibrary/Carbon/idxNetworking-date.html)

|  |
| --- |
| Technical Q&A QA1078Getting the User and Computer Name |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ---   Q: On traditional Mac OS my application use the resources `'STR '` ID=-16096 and ID=-16413 to access the user name and the computer name. This doesn't work on Mac OS X. What should I do?  A: The simple answer is that Carbon provides two high-level routines in "OSUtils.h", `CSCopyUserName` and `CSCopyMachineName`, that do what you want. However, things are never _that_ easy. You have to be aware of the following issues.   - The routines are available in all versions of Mac OS   X. - The routines are available in CarbonLib 1.5 and   higher. At the time of publication this version of   CarbonLib is not publically available. If you're running   against an older version of CarbonLib you must continue   to access this information via the Resource Manager. - Mac OS X 10.0 and 10.0.1 had a bug (r. 2665708)   that caused a crash the second time you call these   routines. - In Mac OS X 10.0.x the `CSCopyMachineName`   routine returned the BSD hostname rather than the   computer name as set in the Sharing panel of System   Preferences (r. 2650897). - These routines are not directly accessible to CFM   programs in Mac OS X 10.0.x. - The routines are not in CarbonFrameworkLib in   Universal Interfaces 3.4 (r. 2782236).   The code in Listing 1 works around all of these problems. You can download a copy of this code, complete with test program, using the link at the bottom of this Technical Q&A.  Finally, these APIs are part of Carbon. If you're working at a lower level (for example, your program is a daemon process that remains running across login/logout), you should use the equivalent low-level APIs provided by System Configuration framework (a new framework introduced in Mac OS X 10.1). The routines you want are `SCDynamicStoreCopyConsoleUser` and `SCDynamicStoreCopyComputerName`. System Configuration framework also provides a way for you to be notified when these values change.   |  | | --- | | ``` static UInt32 gMoreCSSystemVersion = 0;  enum {     kMoreCSMacOSX10point0 = 0x01000,     kMoreCSMacOSX10point1 = 0x01010 };  static CFStringRef CreateCFStringFromStringResource(SInt16 rsrcID)     // This routine is called on Mac OS 9 to create a CFString     // from the system 'STR ' resource with ID of rsrcID. {     CFStringRef result;     SInt8       s;     Handle      stringH;      result = nil;      stringH = GetResource('STR ', rsrcID);     if (stringH != nil) {         s = HGetState(stringH);         HLock(stringH);          // CFStringGetSystemEncoding returns the CFStringEncoding of the         // system as a whole.  We want the system text encoding because         // the user/machine name is set by the File Sharing control panel         // and the File Sharing control panel is localised in the system script.         //         // This only applies because we're reading a resource from the         // System file.  If we were reading it from an application resource         // we would have used GetApplicationTextEncoding (from "Processes.h")         // instead.          result = CFStringCreateWithPascalString(kCFAllocatorSystemDefault,                                                 (StringPtr) *stringH,                                                 CFStringGetSystemEncoding() );          HSetState(stringH, s);     }     return result; }  static CFStringRef ReadMachineNameFromFile(void)     // This routine is called when the client tries to get the     // machine name on Mac OS X 10.0.x.  Because CSCopyMachineName returns     // un-useful information on those systems, w reads the name     // directly from the System Configuration preferences file. {     CFStringRef     result;     CFURLRef        url;     CFDataRef       data;     CFDictionaryRef dict;     CFDictionaryRef systemDict;     CFDictionaryRef system2Dict;      assert( gMoreCSSystemVersion >= kMoreCSMacOSX10point0 );     assert( gMoreCSSystemVersion <  kMoreCSMacOSX10point1 );      // *** IMPORTANT ***     //     // The location and format of the System Configuration framework     // preferences file in the code below is subject to change     // at any time.  Do not write any code which makes any assumptions     // on this file since your app WILL BREAK at some point in time.     // The only reason we can do this safely in this code is because     // we know we're running on Mac OS 10.0 through 10.0.4.  This is     // enforced by the asserts above.  For Mac OS X 10.1 and above you     // must use the public System Configuration framework APIs (or     // APIs, like CSCopyMachineName, which are layered on top of     // System Configuration framework).      result = nil;      url = CFURLCreateWithFileSystemPath(kCFAllocatorDefault,                      CFSTR("/var/db/SystemConfiguration/preferences.xml"),                      kCFURLPOSIXPathStyle,                      false );     if (url != nil) {         if ( CFURLCreateDataAndPropertiesFromResource(kCFAllocatorDefault,                                         url, &data, nil, nil, nil ) ) {             dict = CFPropertyListCreateFromXMLData(kCFAllocatorSystemDefault,                                         data, kCFPropertyListImmutable, nil);             if (dict != nil) {                 systemDict = CFDictionaryGetValue(dict, CFSTR("System") );                 if (systemDict != nil) {                     system2Dict = CFDictionaryGetValue(systemDict,                                                        CFSTR("System") );                     if ( system2Dict != nil ) {                         result = CFDictionaryGetValue(system2Dict,                                                        CFSTR("ComputerName") );                         if (result != nil) {                             // Increment the string's reference count so that                             // releasing "dict" doesn't release the name.                             CFRetain(result);                         }                         // Don't need to release system2Dict because it was "got".                     }                     // Don't need to release systemDict because it was "got".                 }                 CFRelease(dict);             }             CFRelease( data );         }         CFRelease( url );     }      return result; }  extern pascal CFStringRef MoreCSCopyUserName(Boolean useShortName)     // See comment in header file. {     CFStringRef result;      if ( gMoreCSSystemVersion == 0 ) {         (void) Gestalt(gestaltSystemVersion, (SInt32 *) &gMoreCSSystemVersion);     }      if ( gMoreCSSystemVersion < kMoreCSMacOSX10point0 ) {          // Running on traditional Mac OS.  If we have a recent version         // of CarbonLib (1.5 and above) that supports the routine, use         // that.  Otherwise fall back to the Resource Manager.          if ( CSCopyUserName != (void *) kUnresolvedCFragSymbolAddress) {             result = CSCopyUserName(useShortName);         } else {             result = CreateCFStringFromStringResource(-16096);         }      } else {          // Call the API.  However, if we're built CFM we can't just         // call it directly because the routine isn't exported to         // CFM on Mac OS 10.0.x.  So for CFM builds we have to call         // through CFBundle.          #if TARGET_RT_MAC_CFM             {                 typedef CFStringRef (*CSCopyUserNameProc)(Boolean useShortName);                 CSCopyUserNameProc  csCopyUserName;                 CFBundleRef         bundle;                  result = nil;                 csCopyUserName = nil;                  bundle = CFBundleGetBundleWithIdentifier(                                                  CFSTR("com.apple.Carbon" ) );                 if (bundle != nil) {                     csCopyUserName =                        (CSCopyUserNameProc) CFBundleGetFunctionPointerForName(                                               bundle, CFSTR("CSCopyUserName") );                 }                 if (csCopyUserName != nil) {                     result = csCopyUserName(useShortName);                 }                 // Both bundle and csCopyUserName got with "Get", so                 // no need to release.             }         #elif TARGET_RT_MAC_MACHO             result = CSCopyUserName(useShortName);         #else             #error MoreCSCopyUserName: What runtime are you using?         #endif          // Mac OS 10.0 and 10.0.1 (which have the same gestaltSystemVersion         // result -- this just gets better and better) have a bug [2665708]         // where they fail to retain the user name and host name strings         // each time they return it to the client.  The upshot is that         // the client crashes the second time it calls CSCopyUserName or         // CSCopyMachineName.  This extra CFRetain prevents this from happening.         //         // Note that we don't need a similar workaround in MoreCSCopyMachineName         // because we never call the CSCopyMachineName on 10.0 or 10.0.1         // because of another issue.          if (result != nil && gMoreCSSystemVersion == kMoreCSMacOSX10point0) {             CFRetain(result);         }     }      return result; }  extern pascal CFStringRef MoreCSCopyMachineName(void)     // See comment in header file. {     CFStringRef result;      if ( gMoreCSSystemVersion == 0 ) {         (void) Gestalt(gestaltSystemVersion, (SInt32 *) &gMoreCSSystemVersion);     }      if ( gMoreCSSystemVersion < kMoreCSMacOSX10point0 ) {          // Running on traditional Mac OS.  If we have a recent version         // of CarbonLib (1.5 and above) that supports the routine, use         // that.  Otherwise fall back to the Resource Manager.          if ( CSCopyMachineName != (void *) kUnresolvedCFragSymbolAddress) {             result = CSCopyMachineName();         } else {             result = CreateCFStringFromStringResource(-16413);         }      } else if ( gMoreCSSystemVersion < kMoreCSMacOSX10point1 ) {          // Running on Mac OS X 10.0.x.  Read the file directly because         // the API returns the wrong information (the BSD hostname rather         // than the computer name) [2650897].          result = ReadMachineNameFromFile();      } else {          // Running on Mac OS X 10.1 and above.  Let's just call the API.          // The following checks that the CFM weak link worked.         // It's benign for the Mach-O build.          if ( CSCopyMachineName == (void *) kUnresolvedCFragSymbolAddress ) {             result = nil;         } else {             result = CSCopyMachineName();         }     }      return result; ``` | | __Listing 1__. Code for getting user and machine name |        ---   __Downloadables__   |  |  | | --- | --- | | qa1078.hqx (108K). | [Download](https://developer.apple.com/library/archive/qa/qa2001/downloads/qa1078.hqx) |           ---  [Oct 30 2001] |

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
