---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/CoreFoundation.html
archived_at: '2026-07-18T02:54:26.620739Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# CoreFoundation Changes

## CoreFoundation

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

CFBase.hAdded #def CF_AVAILABLEAdded #def CF_AVAILABLE_IOSAdded #def CF_AVAILABLE_IPHONEAdded #def CF_AVAILABLE_MACAdded #def CF_DEPRECATEDAdded #def CF_DEPRECATED_IOSAdded #def CF_DEPRECATED_IPHONEAdded #def CF_DEPRECATED_MACAdded #def CF_RETURNS_NOT_RETAINEDAdded [#def kCFCoreFoundationVersionNumber10_5_7](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_5_7)Added [#def kCFCoreFoundationVersionNumber10_5_8](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_5_8)Added [#def kCFCoreFoundationVersionNumber10_6](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_6)Added [#def kCFCoreFoundationVersionNumber10_6_1](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_6_1)Added [#def kCFCoreFoundationVersionNumber10_6_2](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_6_2)Added [#def kCFCoreFoundationVersionNumber10_6_3](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_6_3)Added [#def kCFCoreFoundationVersionNumber10_6_4](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_6_4)Added [#def kCFCoreFoundationVersionNumber10_6_5](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_6_5)CFCalendar.hAdded [kCFCalendarUnitWeekOfMonth](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/1533518-weekofmonth)Added [kCFCalendarUnitWeekOfYear](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/kcfcalendarunitweekofyear)Added [kCFCalendarUnitYearForWeekOfYear](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/kcfcalendarunityearforweekofyear)CFError.hAdded [kCFErrorFilePathKey](https://developer.apple.com/documentation/corefoundation/kcferrorfilepathkey)Added [kCFErrorURLKey](https://developer.apple.com/documentation/corefoundation/kcferrorurlkey)CFFileSecurity.hAdded [CFFileSecurityCopyAccessControlList()](https://developer.apple.com/documentation/corefoundation/1426508-cffilesecuritycopyaccesscontroll)Added [CFFileSecurityCopyGroupUUID()](https://developer.apple.com/documentation/corefoundation/1426512-cffilesecuritycopygroupuuid)Added [CFFileSecurityCopyOwnerUUID()](https://developer.apple.com/documentation/corefoundation/1426519-cffilesecuritycopyowneruuid)Added [CFFileSecurityCreate()](https://developer.apple.com/documentation/corefoundation/1426509-cffilesecuritycreate)Added [CFFileSecurityCreateCopy()](https://developer.apple.com/documentation/corefoundation/1426498-cffilesecuritycreatecopy)Added [CFFileSecurityGetGroup()](https://developer.apple.com/documentation/corefoundation/1426526-cffilesecuritygetgroup)Added [CFFileSecurityGetMode()](https://developer.apple.com/documentation/corefoundation/1426517-cffilesecuritygetmode)Added [CFFileSecurityGetOwner()](https://developer.apple.com/documentation/corefoundation/1426516-cffilesecuritygetowner)Added [CFFileSecurityGetTypeID()](https://developer.apple.com/documentation/corefoundation/1426530-cffilesecuritygettypeid)Added [CFFileSecurityRef](https://developer.apple.com/documentation/corefoundation/cffilesecurityref)Added [CFFileSecuritySetAccessControlList()](https://developer.apple.com/documentation/corefoundation/1426506-cffilesecuritysetaccesscontrolli)Added [CFFileSecuritySetGroup()](https://developer.apple.com/documentation/corefoundation/1426524-cffilesecuritysetgroup)Added [CFFileSecuritySetGroupUUID()](https://developer.apple.com/documentation/corefoundation/1426492-cffilesecuritysetgroupuuid)Added [CFFileSecuritySetMode()](https://developer.apple.com/documentation/corefoundation/1426496-cffilesecuritysetmode)Added [CFFileSecuritySetOwner()](https://developer.apple.com/documentation/corefoundation/1426528-cffilesecuritysetowner)Added [CFFileSecuritySetOwnerUUID()](https://developer.apple.com/documentation/corefoundation/1426494-cffilesecuritysetowneruuid)Added #def kCFFileSecurityRemoveACLCFRunLoop.hAdded [CFRunLoopObserverCreateWithHandler()](https://developer.apple.com/documentation/corefoundation/1542816-cfrunloopobservercreatewithhandl)Added [CFRunLoopTimerCreateWithHandler()](https://developer.apple.com/documentation/corefoundation/1542555-cfrunlooptimercreatewithhandler)CFString.hAdded [CFStringGetHyphenationLocationBeforeIndex()](https://developer.apple.com/documentation/corefoundation/1542693-cfstringgethyphenationlocationbe)Added [CFStringIsHyphenationAvailableForLocale()](https://developer.apple.com/documentation/corefoundation/1543237-cfstringishyphenationavailablefo)CFURL.hAdded [kCFURLFileResourceIdentifierKey](https://developer.apple.com/documentation/corefoundation/kcfurlfileresourceidentifierkey)Added [kCFURLFileResourceTypeBlockSpecial](https://developer.apple.com/documentation/corefoundation/kcfurlfileresourcetypeblockspecial)Added [kCFURLFileResourceTypeCharacterSpecial](https://developer.apple.com/documentation/corefoundation/kcfurlfileresourcetypecharacterspecial)Added [kCFURLFileResourceTypeDirectory](https://developer.apple.com/documentation/corefoundation/kcfurlfileresourcetypedirectory)Added [kCFURLFileResourceTypeKey](https://developer.apple.com/documentation/corefoundation/kcfurlfileresourcetypekey)Added [kCFURLFileResourceTypeNamedPipe](https://developer.apple.com/documentation/corefoundation/kcfurlfileresourcetypenamedpipe)Added [kCFURLFileResourceTypeRegular](https://developer.apple.com/documentation/corefoundation/kcfurlfileresourcetyperegular)Added [kCFURLFileResourceTypeSocket](https://developer.apple.com/documentation/corefoundation/kcfurlfileresourcetypesocket)Added [kCFURLFileResourceTypeSymbolicLink](https://developer.apple.com/documentation/corefoundation/kcfurlfileresourcetypesymboliclink)Added [kCFURLFileResourceTypeUnknown](https://developer.apple.com/documentation/corefoundation/kcfurlfileresourcetypeunknown)Added [kCFURLFileSecurityKey](https://developer.apple.com/documentation/corefoundation/kcfurlfilesecuritykey)Added [kCFURLIsExecutableKey](https://developer.apple.com/documentation/corefoundation/kcfurlisexecutablekey)Added [kCFURLIsMountTriggerKey](https://developer.apple.com/documentation/corefoundation/kcfurlismounttriggerkey)Added [kCFURLIsReadableKey](https://developer.apple.com/documentation/corefoundation/kcfurlisreadablekey)Added [kCFURLIsUbiquitousItemKey](https://developer.apple.com/documentation/corefoundation/kcfurlisubiquitousitemkey)Added [kCFURLIsWritableKey](https://developer.apple.com/documentation/corefoundation/kcfurliswritablekey)Added [kCFURLKeysOfUnsetValuesKey](https://developer.apple.com/documentation/corefoundation/kcfurlkeysofunsetvalueskey)Added [kCFURLPreferredIOBlockSizeKey](https://developer.apple.com/documentation/corefoundation/kcfurlpreferredioblocksizekey)Added [kCFURLTotalFileAllocatedSizeKey](https://developer.apple.com/documentation/corefoundation/kcfurltotalfileallocatedsizekey)Added [kCFURLTotalFileSizeKey](https://developer.apple.com/documentation/corefoundation/kcfurltotalfilesizekey)Added [kCFURLUbiquitousItemHasUnresolvedConflictsKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemhasunresolvedconflictskey)Added [kCFURLUbiquitousItemIsDownloadedKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemisdownloadedkey)Added [kCFURLUbiquitousItemIsDownloadingKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemisdownloadingkey)Added [kCFURLUbiquitousItemIsUploadedKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemisuploadedkey)Added [kCFURLUbiquitousItemIsUploadingKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemisuploadingkey)Added [kCFURLUbiquitousItemPercentDownloadedKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitempercentdownloadedkey)Added [kCFURLUbiquitousItemPercentUploadedKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitempercentuploadedkey)Added [kCFURLVolumeCreationDateKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumecreationdatekey)Added [kCFURLVolumeIdentifierKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeidentifierkey)Added [kCFURLVolumeIsAutomountedKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeisautomountedkey)Added [kCFURLVolumeIsBrowsableKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeisbrowsablekey)Added [kCFURLVolumeIsEjectableKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeisejectablekey)Added [kCFURLVolumeIsInternalKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeisinternalkey)Added [kCFURLVolumeIsLocalKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeislocalkey)Added [kCFURLVolumeIsReadOnlyKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeisreadonlykey)Added [kCFURLVolumeIsRemovableKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeisremovablekey)Added [kCFURLVolumeLocalizedNameKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumelocalizednamekey)Added [kCFURLVolumeMaximumFileSizeKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumemaximumfilesizekey)Added [kCFURLVolumeNameKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumenamekey)Added [kCFURLVolumeSupportsAdvisoryFileLockingKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportsadvisoryfilelockingkey)Added [kCFURLVolumeSupportsExtendedSecurityKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportsextendedsecuritykey)Added [kCFURLVolumeSupportsRenamingKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportsrenamingkey)Added [kCFURLVolumeSupportsRootDirectoryDatesKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportsrootdirectorydateskey)Added [kCFURLVolumeSupportsVolumeSizesKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportsvolumesizeskey)Added [kCFURLVolumeURLForRemountingKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeurlforremountingkey)Added [kCFURLVolumeUUIDStringKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeuuidstringkey)Modified [CFURLSetResourcePropertyForKey()](https://developer.apple.com/documentation/corefoundation/1541607-cfurlsetresourcepropertyforkey)

|  | Declaration |
| --- | --- |
| From | Boolean CFURLSetResourcePropertyForKey ( CFURLRef url, CFStringRef key, CFTypeRef propertValue, CFErrorRef \*error); |
| To | Boolean CFURLSetResourcePropertyForKey ( CFURLRef url, CFStringRef key, CFTypeRef propertyValue, CFErrorRef \*error); |

CFURLEnumerator.hAdded [kCFURLEnumeratorDefaultBehavior](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/kcfurlenumeratordefaultbehavior)Added [kCFURLEnumeratorDirectoryPostOrderSuccess](https://developer.apple.com/documentation/corefoundation/cfurlenumeratorresult/kcfurlenumeratordirectorypostordersuccess)Added [kCFURLEnumeratorIncludeDirectoriesPostOrder](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/1542791-includedirectoriespostorder)Added [kCFURLEnumeratorIncludeDirectoriesPreOrder](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/1541726-includedirectoriespreorder)Modified [CFURLEnumeratorGetSourceDidChange()](https://developer.apple.com/documentation/corefoundation/1575035-cfurlenumeratorgetsourcedidchang)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

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
