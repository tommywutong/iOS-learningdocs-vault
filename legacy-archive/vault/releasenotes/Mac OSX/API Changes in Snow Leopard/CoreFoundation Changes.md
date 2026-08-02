---
title: API Changes in Snow Leopard
apple_id: TP40007673
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/SnowLeopard_API_ReleaseNote/CoreFoundation.html
archived_at: '2026-07-18T02:58:42.598152Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [API Changes in Snow Leopard](API%20Changes%20in%20Snow%20Leopard.md)


[ADC Home](https://developer.apple.com/) >
[Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) >
Release Notes >
OS X >
[API Changes in Snow Leopard Developer Preview](API%20Changes%20in%20Snow%20Leopard.md) >

# CoreFoundation Changes

## CoreFoundation

CFBase.hAdded [FourCharCode](https://developer.apple.com/documentation/kernel/fourcharcode) (no architecture available)Added [OSType](https://developer.apple.com/documentation/kernel/ostype) (no architecture available)Added ScriptCode (no architecture available)Added UniCharCount (no architecture available)Added [#def kCFCoreFoundationVersionNumber10_5](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_5)Added [#def kCFCoreFoundationVersionNumber10_5_1](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_5_1)CFCalendar.hAdded [kCFCalendarUnitQuarter](https://developer.apple.com/documentation/corefoundation/cfcalendarunit/1533474-quarter)CFLocale.hAdded [kCFISO8601Calendar](https://developer.apple.com/documentation/corefoundation/kcfiso8601calendar)Added [kCFIndianCalendar](https://developer.apple.com/documentation/corefoundation/kcfindiancalendar)Added [kCFPersianCalendar](https://developer.apple.com/documentation/corefoundation/kcfpersiancalendar)Added kCFTaiwaneseCalendarCFPropertyList.hAdded [CFPropertyListCreateData()](https://developer.apple.com/documentation/corefoundation/1429998-cfpropertylistcreatedata)Added [CFPropertyListCreateWithData()](https://developer.apple.com/documentation/corefoundation/1430002-cfpropertylistcreatewithdata)Added [CFPropertyListCreateWithStream()](https://developer.apple.com/documentation/corefoundation/1430023-cfpropertylistcreatewithstream)Added [CFPropertyListWrite()](https://developer.apple.com/documentation/corefoundation/1430001-cfpropertylistwrite)Added [kCFPropertyListReadCorruptError](https://developer.apple.com/documentation/corefoundation/1429999-reading_and_writing_error_codes/kcfpropertylistreadcorrupterror)Added [kCFPropertyListReadStreamError](https://developer.apple.com/documentation/corefoundation/kcfpropertylistreadstreamerror)Added [kCFPropertyListReadUnknownVersionError](https://developer.apple.com/documentation/corefoundation/1429999-reading_and_writing_error_codes/kcfpropertylistreadunknownversionerror)Added [kCFPropertyListWriteStreamError](https://developer.apple.com/documentation/corefoundation/1429999-reading_and_writing_error_codes/kcfpropertylistwritestreamerror)CFString.hAdded [CFStringGetLongCharacterForSurrogatePair()](https://developer.apple.com/documentation/corefoundation/1541965-cfstringgetlongcharacterforsurro)Added [CFStringGetSurrogatePairForLongCharacter()](https://developer.apple.com/documentation/corefoundation/1541601-cfstringgetsurrogatepairforlongc)Added [CFStringIsSurrogateHighCharacter()](https://developer.apple.com/documentation/corefoundation/1543284-cfstringissurrogatehighcharacter)Added [CFStringIsSurrogateLowCharacter()](https://developer.apple.com/documentation/corefoundation/1541963-cfstringissurrogatelowcharacter)CFStringEncodingExt.hAdded [kCFStringEncodingUTF7](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingutf7)Added [kCFStringEncodingUTF7_IMAP](https://developer.apple.com/documentation/corefoundation/cfstringencodings/kcfstringencodingutf7_imap)CFURL.hAdded [CFURLBookmarkCreationOptions](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions)Added [CFURLBookmarkResolutionOptions](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkresolutionoptions)Added [CFURLCreateBookmarkData()](https://developer.apple.com/documentation/corefoundation/1542923-cfurlcreatebookmarkdata)Added [CFURLCreateByResolvingBookmarkData()](https://developer.apple.com/documentation/corefoundation/1543252-cfurlcreatebyresolvingbookmarkda)Added [CFURLCreateFilePathURL()](https://developer.apple.com/documentation/corefoundation/1542076-cfurlcreatefilepathurl)Added [CFURLCreateFileReferenceURL()](https://developer.apple.com/documentation/corefoundation/1543282-cfurlcreatefilereferenceurl)Added [CFURLCreateResourcePropertiesForKeysFromBookmarkData()](https://developer.apple.com/documentation/corefoundation/1543621-cfurlcreateresourcepropertiesfor)Added [CFURLCreateResourcePropertyForKeyFromBookmarkData()](https://developer.apple.com/documentation/corefoundation/1543031-cfurlcreateresourcepropertyforke)Added [kCFBookmarkResolutionWithoutMountingMask](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkresolutionoptions/1541888-cfbookmarkresolutionwithoutmount)Added [kCFBookmarkResolutionWithoutUIMask](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkresolutionoptions/kcfbookmarkresolutionwithoutuimask)Added [kCFURLBookmarkCreationMinimalBookmarkMask](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions/1541966-minimalbookmarkmask)Added [kCFURLBookmarkCreationPreferFileIDResolutionMask](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions/kcfurlbookmarkcreationpreferfileidresolutionmask)CFURLAccess.hAdded [CFURLClearResourcePropertyCache()](https://developer.apple.com/documentation/corefoundation/1541959-cfurlclearresourcepropertycache)Added [CFURLClearResourcePropertyCacheForKey()](https://developer.apple.com/documentation/corefoundation/1542054-cfurlclearresourcepropertycachef)Added [CFURLCopyResourcePropertiesForKeys()](https://developer.apple.com/documentation/corefoundation/1542370-cfurlcopyresourcepropertiesforke)Added [CFURLCopyResourcePropertyForKey()](https://developer.apple.com/documentation/corefoundation/1542764-cfurlcopyresourcepropertyforkey)Added [CFURLResourceIsReachable()](https://developer.apple.com/documentation/corefoundation/1543666-cfurlresourceisreachable)Added [CFURLSetResourcePropertiesForKeys()](https://developer.apple.com/documentation/corefoundation/1542947-cfurlsetresourcepropertiesforkey)Added [CFURLSetResourcePropertyForKey()](https://developer.apple.com/documentation/corefoundation/1541607-cfurlsetresourcepropertyforkey)Added [CFURLSetTemporaryResourcePropertyForKey()](https://developer.apple.com/documentation/corefoundation/1542384-cfurlsettemporaryresourcepropert)Added [kCFURLAttributeModificationDateKey](https://developer.apple.com/documentation/corefoundation/kcfurlattributemodificationdatekey)Added [kCFURLContentAccessDateKey](https://developer.apple.com/documentation/corefoundation/kcfurlcontentaccessdatekey)Added [kCFURLContentModificationDateKey](https://developer.apple.com/documentation/corefoundation/kcfurlcontentmodificationdatekey)Added [kCFURLCreationDateKey](https://developer.apple.com/documentation/corefoundation/kcfurlcreationdatekey)Added [kCFURLCustomIconKey](https://developer.apple.com/documentation/corefoundation/kcfurlcustomiconkey)Added [kCFURLEffectiveIconKey](https://developer.apple.com/documentation/corefoundation/kcfurleffectiveiconkey)Added [kCFURLFileAllocatedSizeKey](https://developer.apple.com/documentation/corefoundation/kcfurlfileallocatedsizekey)Added [kCFURLFileSizeKey](https://developer.apple.com/documentation/corefoundation/kcfurlfilesizekey)Added [kCFURLHasHiddenExtensionKey](https://developer.apple.com/documentation/corefoundation/kcfurlhashiddenextensionkey)Added [kCFURLIsDirectoryKey](https://developer.apple.com/documentation/corefoundation/kcfurlisdirectorykey)Added [kCFURLIsHiddenKey](https://developer.apple.com/documentation/corefoundation/kcfurlishiddenkey)Added [kCFURLIsPackageKey](https://developer.apple.com/documentation/corefoundation/kcfurlispackagekey)Added [kCFURLIsRegularFileKey](https://developer.apple.com/documentation/corefoundation/kcfurlisregularfilekey)Added [kCFURLIsSymbolicLinkKey](https://developer.apple.com/documentation/corefoundation/kcfurlissymboliclinkkey)Added [kCFURLIsSystemImmutableKey](https://developer.apple.com/documentation/corefoundation/kcfurlissystemimmutablekey)Added [kCFURLIsUserImmutableKey](https://developer.apple.com/documentation/corefoundation/kcfurlisuserimmutablekey)Added [kCFURLIsVolumeKey](https://developer.apple.com/documentation/corefoundation/kcfurlisvolumekey)Added [kCFURLLabelColorKey](https://developer.apple.com/documentation/corefoundation/kcfurllabelcolorkey)Added [kCFURLLabelNumberKey](https://developer.apple.com/documentation/corefoundation/kcfurllabelnumberkey)Added [kCFURLLinkCountKey](https://developer.apple.com/documentation/corefoundation/kcfurllinkcountkey)Added [kCFURLLocalizedLabelKey](https://developer.apple.com/documentation/corefoundation/kcfurllocalizedlabelkey)Added [kCFURLLocalizedNameKey](https://developer.apple.com/documentation/corefoundation/kcfurllocalizednamekey)Added [kCFURLLocalizedTypeDescriptionKey](https://developer.apple.com/documentation/corefoundation/kcfurllocalizedtypedescriptionkey)Added [kCFURLNameKey](https://developer.apple.com/documentation/corefoundation/kcfurlnamekey)Added [kCFURLParentDirectoryURLKey](https://developer.apple.com/documentation/corefoundation/kcfurlparentdirectoryurlkey)Added [kCFURLTypeIdentifierKey](https://developer.apple.com/documentation/corefoundation/kcfurltypeidentifierkey)Added [kCFURLVolumeAvailableCapacityKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeavailablecapacitykey)Added [kCFURLVolumeIsJournalingKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeisjournalingkey)Added [kCFURLVolumeLocalizedFormatDescriptionKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumelocalizedformatdescriptionkey)Added [kCFURLVolumeResourceCountKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeresourcecountkey)Added [kCFURLVolumeSupportsCasePreservedNamesKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportscasepreservednameskey)Added [kCFURLVolumeSupportsCaseSensitiveNamesKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportscasesensitivenameskey)Added [kCFURLVolumeSupportsHardLinksKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportshardlinkskey)Added [kCFURLVolumeSupportsJournalingKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportsjournalingkey)Added [kCFURLVolumeSupportsPersistentIDsKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportspersistentidskey)Added [kCFURLVolumeSupportsSparseFilesKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportssparsefileskey)Added [kCFURLVolumeSupportsSymbolicLinksKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportssymboliclinkskey)Added [kCFURLVolumeSupportsZeroRunsKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportszerorunskey)Added [kCFURLVolumeTotalCapacityKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumetotalcapacitykey)Added [kCFURLVolumeURLKey](https://developer.apple.com/documentation/corefoundation/kcfurlvolumeurlkey)CFUserNotification.hAdded kCFUserNotificationAlertTopMostKey (no architecture available)Added kCFUserNotificationKeyboardTypesKey (no architecture available)

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
