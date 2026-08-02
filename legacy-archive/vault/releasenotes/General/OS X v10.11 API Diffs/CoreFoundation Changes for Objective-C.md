---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/CoreFoundation.html
archived_at: '2026-07-18T02:52:58.214047Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreFoundation Changes for Objective-C

### CoreFoundation

#### CFAvailability.h

Added #def CF_SWIFT_UNAVAILABLE

#### CFBase.h

Removed [kCFNotFound](https://developer.apple.com/documentation/corefoundation/base_utilities/value_not_found/kcfnotfound)Added #def CF_ASSUME_NONNULL_BEGINAdded #def CF_ASSUME_NONNULL_ENDAdded #def CF_REFINED_FOR_SWIFTAdded #def CF_SWIFT_NAMEAdded [#def kCFCoreFoundationVersionNumber10_10](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_10)Added [#def kCFCoreFoundationVersionNumber10_10_1](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_10_1)Added [#def kCFCoreFoundationVersionNumber10_10_2](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_10_2)Added [#def kCFCoreFoundationVersionNumber10_10_3](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_10_3)Added [kCFNotFound](https://developer.apple.com/documentation/corefoundation/kcfnotfound)

#### CFNumberFormatter.h

Added [kCFNumberFormatterCurrencyAccountingStyle](https://developer.apple.com/documentation/corefoundation/cfnumberformatterstyle/currencyaccountingstyle)Added [kCFNumberFormatterCurrencyISOCodeStyle](https://developer.apple.com/documentation/corefoundation/cfnumberformatterstyle/kcfnumberformattercurrencyisocodestyle)Added [kCFNumberFormatterCurrencyPluralStyle](https://developer.apple.com/documentation/corefoundation/cfnumberformatterstyle/currencypluralstyle)Added [kCFNumberFormatterOrdinalStyle](https://developer.apple.com/documentation/corefoundation/cfnumberformatterstyle/kcfnumberformatterordinalstyle)

#### CFRunLoop.h

Added [CFRunLoopRunResult](https://developer.apple.com/documentation/corefoundation/cfrunlooprunresult)Modified [CFRunLoopRunInMode()](https://developer.apple.com/documentation/corefoundation/1541988-cfrunloopruninmode)

|  | Declaration |
| --- | --- |
| From | ``` SInt32 CFRunLoopRunInMode (     CFStringRef mode,     CFTimeInterval seconds,     Boolean returnAfterSourceHandled ); ``` |
| To | ``` CFRunLoopRunResult CFRunLoopRunInMode (     CFStringRef mode,     CFTimeInterval seconds,     Boolean returnAfterSourceHandled ); ``` |

#### CFURL.h

Added [kCFURLApplicationIsScriptableKey](https://developer.apple.com/documentation/corefoundation/kcfurlapplicationisscriptablekey)Added [kCFURLIsApplicationKey](https://developer.apple.com/documentation/corefoundation/kcfurlisapplicationkey)Modified [CFURLCreateStringByAddingPercentEscapes()](https://developer.apple.com/documentation/corefoundation/1542665-cfurlcreatestringbyaddingpercent)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [CFURLCreateStringByReplacingPercentEscapesUsingEncoding()](https://developer.apple.com/documentation/corefoundation/1541974-cfurlcreatestringbyreplacingperc)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.0 | OS X 10.11 |

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
