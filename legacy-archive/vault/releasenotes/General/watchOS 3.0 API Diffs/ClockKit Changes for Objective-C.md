---
title: watchOS 3.0 API Diffs
apple_id: TP40017328
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS30APIDiffs/Objective-C/ClockKit.html
archived_at: '2026-07-18T02:58:12.803571Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.0 API Diffs](watchOS%202.2%20to%20watchOS%203.0%20API%20Differences.md)


# ClockKit Changes for Objective-C

### ClockKit

#### CLKComplicationDataSource.h

Added [-[CLKComplicationDataSource getLocalizableSampleTemplateForComplication:withHandler:]](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/1650686-getlocalizablesampletemplate)Modified [-[CLKComplicationDataSource getPlaceholderTemplateForComplication:withHandler:]](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/1628026-getplaceholdertemplateforcomplic)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

#### CLKComplicationTemplate.h

Added [CLKComplicationTemplateExtraLargeColumnsText](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargecolumnstext)Added [CLKComplicationTemplateExtraLargeColumnsText.column2Alignment](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargecolumnstext/1650719-column2alignment)Added [CLKComplicationTemplateExtraLargeColumnsText.highlightColumn2](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargecolumnstext/1650698-highlightcolumn2)Added [CLKComplicationTemplateExtraLargeColumnsText.row1Column1TextProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargecolumnstext/1650716-row1column1textprovider)Added [CLKComplicationTemplateExtraLargeColumnsText.row1Column2TextProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargecolumnstext/1650700-row1column2textprovider)Added [CLKComplicationTemplateExtraLargeColumnsText.row2Column1TextProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargecolumnstext/1650708-row2column1textprovider)Added [CLKComplicationTemplateExtraLargeColumnsText.row2Column2TextProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargecolumnstext/1650706-row2column2textprovider)Added [CLKComplicationTemplateExtraLargeRingImage](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringimage)Added [CLKComplicationTemplateExtraLargeRingImage.fillFraction](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringimage/1650713-fillfraction)Added [CLKComplicationTemplateExtraLargeRingImage.imageProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringimage/1650704-imageprovider)Added [CLKComplicationTemplateExtraLargeRingImage.ringStyle](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringimage/1650723-ringstyle)Added [CLKComplicationTemplateExtraLargeRingText](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringtext)Added [CLKComplicationTemplateExtraLargeRingText.fillFraction](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringtext/1650711-fillfraction)Added [CLKComplicationTemplateExtraLargeRingText.ringStyle](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringtext/1650722-ringstyle)Added [CLKComplicationTemplateExtraLargeRingText.textProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringtext/1650703-textprovider)Added [CLKComplicationTemplateExtraLargeSimpleImage](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargesimpleimage)Added [CLKComplicationTemplateExtraLargeSimpleImage.imageProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargesimpleimage/1650709-imageprovider)Added [CLKComplicationTemplateExtraLargeSimpleText](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargesimpletext)Added [CLKComplicationTemplateExtraLargeSimpleText.textProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargesimpletext/1650724-textprovider)Added [CLKComplicationTemplateExtraLargeStackImage](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargestackimage)Added [CLKComplicationTemplateExtraLargeStackImage.highlightLine2](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargestackimage/1650715-highlightline2)Added [CLKComplicationTemplateExtraLargeStackImage.line1ImageProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargestackimage/1650718-line1imageprovider)Added [CLKComplicationTemplateExtraLargeStackImage.line2TextProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargestackimage/1650714-line2textprovider)Added [CLKComplicationTemplateExtraLargeStackText](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargestacktext)Added [CLKComplicationTemplateExtraLargeStackText.highlightLine2](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargestacktext/1650701-highlightline2)Added [CLKComplicationTemplateExtraLargeStackText.line1TextProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargestacktext/1650707-line1textprovider)Added [CLKComplicationTemplateExtraLargeStackText.line2TextProvider](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargestacktext/1650695-line2textprovider)

#### CLKDefines.h

Added [CLKComplicationFamilyExtraLarge](https://developer.apple.com/documentation/clockkit/clkcomplicationfamily/clkcomplicationfamilyextralarge)Added [CLKComplicationFamilyUtilitarianSmallFlat](https://developer.apple.com/documentation/clockkit/clkcomplicationfamily/clkcomplicationfamilyutilitariansmallflat)

#### CLKTextProvider.h

Added [+[CLKTextProvider localizableTextProviderWithStringsFileFormatKey:textProviders:]](https://developer.apple.com/documentation/clockkit/clktextprovider/1650721-localizabletextproviderwithstrin)Added [+[CLKTextProvider localizableTextProviderWithStringsFileTextKey:]](https://developer.apple.com/documentation/clockkit/clktextprovider/1650705-localizabletextprovider)Added [+[CLKTextProvider localizableTextProviderWithStringsFileTextKey:shortTextKey:]](https://developer.apple.com/documentation/clockkit/clktextprovider/1650696-localizabletextproviderwithstrin)Added CLKTextProvider(Localizable)

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
