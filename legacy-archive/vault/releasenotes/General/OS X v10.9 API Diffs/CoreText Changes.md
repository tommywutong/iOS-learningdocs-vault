---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/CoreText.html
archived_at: '2026-07-18T02:54:12.022500Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# CoreText Changes

## CoreText

CTDefines.hRemoved #def CT_AVAILABLE_BUT_DEPRECATEDRemoved #def CT_AVAILABLE_STARTINGRemoved #def CT_DEPRECATED_ENUMERATORCTFont.hAdded [kCTFontTableLtag](https://developer.apple.com/documentation/coretext/kctfonttableltag)Modified [CTFontCopyLocalizedName()](https://developer.apple.com/documentation/coretext/1510714-ctfontcopylocalizedname)

|  | Declaration |
| --- | --- |
| From | CFStringRef CTFontCopyLocalizedName ( CTFontRef font, CFStringRef nameKey, CFStringRef \*language); |
| To | CFStringRef CTFontCopyLocalizedName ( CTFontRef font, CFStringRef nameKey, CFStringRef \*actualLanguage); |

CTFontDescriptor.hAdded [CTFontDescriptorCreateCopyWithFamily()](https://developer.apple.com/documentation/coretext/1510392-ctfontdescriptorcreatecopywithfa)Added [CTFontDescriptorCreateCopyWithSymbolicTraits()](https://developer.apple.com/documentation/coretext/1509171-ctfontdescriptorcreatecopywithsy)Added [CTFontDescriptorMatchFontDescriptorsWithProgressHandler()](https://developer.apple.com/documentation/coretext/1511433-ctfontdescriptormatchfontdescrip)Added [CTFontDescriptorMatchingState](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate)Added [CTFontDescriptorProgressHandler](https://developer.apple.com/documentation/coretext/ctfontdescriptorprogresshandler)Added [kCTFontDescriptorMatchingCurrentAssetSize](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingcurrentassetsize)Added [kCTFontDescriptorMatchingDescriptors](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingdescriptors)Added [kCTFontDescriptorMatchingDidBegin](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/kctfontdescriptormatchingdidbegin)Added [kCTFontDescriptorMatchingDidFailWithError](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/kctfontdescriptormatchingdidfailwitherror)Added [kCTFontDescriptorMatchingDidFinish](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/kctfontdescriptormatchingdidfinish)Added [kCTFontDescriptorMatchingDidFinishDownloading](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/kctfontdescriptormatchingdidfinishdownloading)Added [kCTFontDescriptorMatchingDidMatch](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/didmatch)Added [kCTFontDescriptorMatchingDownloading](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/kctfontdescriptormatchingdownloading)Added [kCTFontDescriptorMatchingError](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingerror)Added [kCTFontDescriptorMatchingPercentage](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingpercentage)Added [kCTFontDescriptorMatchingResult](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingresult)Added [kCTFontDescriptorMatchingSourceDescriptor](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingsourcedescriptor)Added [kCTFontDescriptorMatchingStalled](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/kctfontdescriptormatchingstalled)Added [kCTFontDescriptorMatchingTotalAssetSize](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingtotalassetsize)Added [kCTFontDescriptorMatchingTotalDownloadedSize](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingtotaldownloadedsize)Added [kCTFontDescriptorMatchingWillBeginDownloading](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/willbegindownloading)Added [kCTFontDescriptorMatchingWillBeginQuerying](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/willbeginquerying)Added [kCTFontDownloadableAttribute](https://developer.apple.com/documentation/coretext/kctfontdownloadableattribute)CTFrame.hAdded [kCTFrameProgressionLeftToRight](https://developer.apple.com/documentation/coretext/ctframeprogression/kctframeprogressionlefttoright)CTRunDelegate.hAdded [CTRunDelegateCallbacks](https://developer.apple.com/documentation/coretext/ctrundelegatecallbacks)Added [CTRunDelegateCreate()](https://developer.apple.com/documentation/coretext/1498167-ctrundelegatecreate)Added [CTRunDelegateDeallocateCallback](https://developer.apple.com/documentation/coretext/ctrundelegatedeallocatecallback)Added [CTRunDelegateGetAscentCallback](https://developer.apple.com/documentation/coretext/ctrundelegategetascentcallback)Added [CTRunDelegateGetDescentCallback](https://developer.apple.com/documentation/coretext/ctrundelegategetdescentcallback)Added [CTRunDelegateGetRefCon()](https://developer.apple.com/documentation/coretext/1498169-ctrundelegategetrefcon)Added [CTRunDelegateGetTypeID()](https://developer.apple.com/documentation/coretext/1498175-ctrundelegategettypeid)Added [CTRunDelegateGetWidthCallback](https://developer.apple.com/documentation/coretext/ctrundelegategetwidthcallback)Added [CTRunDelegateRef](https://developer.apple.com/documentation/coretext/ctrundelegate)Added [kCTRunDelegateCurrentVersion](https://developer.apple.com/documentation/coretext/kctrundelegatecurrentversion)Added [kCTRunDelegateVersion1](https://developer.apple.com/documentation/coretext/1498177-run_delegate_versions/kctrundelegateversion1)CTStringAttributes.hAdded [kCTLanguageAttributeName](https://developer.apple.com/documentation/coretext/kctlanguageattributename)CoreText.hAdded [#def kCTVersionNumber10_9](https://developer.apple.com/documentation/coretext/kctversionnumber10_9)SFNTLayoutTypes.hAdded [LtagStringRange](https://developer.apple.com/documentation/coretext/ltagstringrange)Added [LtagTable](https://developer.apple.com/documentation/coretext/ltagtable)Added [kBSLNIdeographicHighBaseline](https://developer.apple.com/documentation/coretext/1446472-anonymous/kbslnideographichighbaseline)Added [kLTAGCurrentVersion](https://developer.apple.com/documentation/coretext/1446351-anonymous/kltagcurrentversion)Added [kLanguageTagType](https://developer.apple.com/documentation/coretext/klanguagetagtype)

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
