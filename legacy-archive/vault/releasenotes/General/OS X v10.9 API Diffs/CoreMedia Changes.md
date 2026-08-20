---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/CoreMedia.html
archived_at: '2026-07-18T02:54:11.508456Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# CoreMedia Changes

## CoreMedia

CMFormatDescription.hAdded [CMVideoFormatDescriptionCreateFromH264ParameterSets()](https://developer.apple.com/documentation/coremedia/1489818-cmvideoformatdescriptioncreatefr)Added [CMVideoFormatDescriptionGetH264ParameterSetAtIndex()](https://developer.apple.com/documentation/coremedia/1489529-cmvideoformatdescriptiongeth264p)Added [kCMFormatDescriptionError_ValueNotAvailable](https://developer.apple.com/documentation/coremedia/1564245-error_codes/kcmformatdescriptionerror_valuenotavailable)Added [kCMMPEG2VideoProfile_XF](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_xf)CMSampleBuffer.hAdded [CMSampleBufferCopyPCMDataIntoAudioBufferList()](https://developer.apple.com/documentation/coremedia/1489200-cmsamplebuffercopypcmdataintoaud)CMSync.hAdded [kCMTimebaseNotificationKey_EventTime](https://developer.apple.com/documentation/coremedia/kcmtimebasenotificationkey_eventtime)CMTextMarkup.hAdded [kCMTextMarkupAlignmentType_End](https://developer.apple.com/documentation/coremedia/kcmtextmarkupalignmenttype_end)Added [kCMTextMarkupAlignmentType_Left](https://developer.apple.com/documentation/coremedia/kcmtextmarkupalignmenttype_left)Added [kCMTextMarkupAlignmentType_Middle](https://developer.apple.com/documentation/coremedia/kcmtextmarkupalignmenttype_middle)Added [kCMTextMarkupAlignmentType_Right](https://developer.apple.com/documentation/coremedia/kcmtextmarkupalignmenttype_right)Added [kCMTextMarkupAlignmentType_Start](https://developer.apple.com/documentation/coremedia/kcmtextmarkupalignmenttype_start)Added [kCMTextMarkupAttribute_Alignment](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_alignment)Added [kCMTextMarkupAttribute_BackgroundColorARGB](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_backgroundcolorargb)Added [kCMTextMarkupAttribute_BaseFontSizePercentageRelativeToVideoHeight](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_basefontsizepercentagerelativetovideoheight)Added [kCMTextMarkupAttribute_BoldStyle](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_boldstyle)Added [kCMTextMarkupAttribute_CharacterBackgroundColorARGB](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_characterbackgroundcolorargb)Added [kCMTextMarkupAttribute_CharacterEdgeStyle](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_characteredgestyle)Added [kCMTextMarkupAttribute_FontFamilyName](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_fontfamilyname)Added [kCMTextMarkupAttribute_ForegroundColorARGB](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_foregroundcolorargb)Added [kCMTextMarkupAttribute_GenericFontFamilyName](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_genericfontfamilyname)Added [kCMTextMarkupAttribute_ItalicStyle](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_italicstyle)Added [kCMTextMarkupAttribute_OrthogonalLinePositionPercentageRelativeToWritingDirection](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_orthogonallinepositionpercentagerelativetowritingdirection)Added [kCMTextMarkupAttribute_RelativeFontSize](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_relativefontsize)Added [kCMTextMarkupAttribute_TextPositionPercentageRelativeToWritingDirection](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_textpositionpercentagerelativetowritingdirection)Added [kCMTextMarkupAttribute_UnderlineStyle](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_underlinestyle)Added [kCMTextMarkupAttribute_VerticalLayout](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_verticallayout)Added [kCMTextMarkupAttribute_WritingDirectionSizePercentage](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_writingdirectionsizepercentage)Added [kCMTextMarkupCharacterEdgeStyle_Depressed](https://developer.apple.com/documentation/coremedia/kcmtextmarkupcharacteredgestyle_depressed)Added [kCMTextMarkupCharacterEdgeStyle_DropShadow](https://developer.apple.com/documentation/coremedia/kcmtextmarkupcharacteredgestyle_dropshadow)Added [kCMTextMarkupCharacterEdgeStyle_None](https://developer.apple.com/documentation/coremedia/kcmtextmarkupcharacteredgestyle_none)Added [kCMTextMarkupCharacterEdgeStyle_Raised](https://developer.apple.com/documentation/coremedia/kcmtextmarkupcharacteredgestyle_raised)Added [kCMTextMarkupCharacterEdgeStyle_Uniform](https://developer.apple.com/documentation/coremedia/kcmtextmarkupcharacteredgestyle_uniform)Added [kCMTextMarkupGenericFontName_Casual](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_casual)Added [kCMTextMarkupGenericFontName_Cursive](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_cursive)Added [kCMTextMarkupGenericFontName_Default](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_default)Added [kCMTextMarkupGenericFontName_Fantasy](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_fantasy)Added [kCMTextMarkupGenericFontName_Monospace](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_monospace)Added [kCMTextMarkupGenericFontName_MonospaceSansSerif](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_monospacesansserif)Added [kCMTextMarkupGenericFontName_MonospaceSerif](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_monospaceserif)Added [kCMTextMarkupGenericFontName_ProportionalSansSerif](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_proportionalsansserif)Added [kCMTextMarkupGenericFontName_ProportionalSerif](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_proportionalserif)Added [kCMTextMarkupGenericFontName_SansSerif](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_sansserif)Added [kCMTextMarkupGenericFontName_Serif](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_serif)Added [kCMTextMarkupGenericFontName_SmallCapital](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_smallcapital)Added [kCMTextVerticalLayout_LeftToRight](https://developer.apple.com/documentation/coremedia/kcmtextverticallayout_lefttoright)Added [kCMTextVerticalLayout_RightToLeft](https://developer.apple.com/documentation/coremedia/kcmtextverticallayout_righttoleft)

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
