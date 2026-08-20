---
title: Accessing the DialAssist data
apple_id: DTS10001463
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-07-11'
source_url: https://developer.apple.com/library/archive/qa/nw/nw51.html
archived_at: '2026-07-18T02:29:47.027963Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW51Accessing the DialAssist data |

|  |  |  |  |
| --- | --- | --- | --- |
| ---   Q: Is there any documentation or SDKs available for the ARA DialAssist program?  A: At this time, there is no official SDK or support for third party access to the DialAssist system. However, it is quite possible to look at the DialAssist Pref file yourself. You of course have to follow all the rules about not opening the resource when Dial Setup does (standard resource mgr problems).    |  | | --- | | __Note:__  USE THE FOLLOWING INFORMATION AT YOUR OWN RISK!! THIS IS NOT SUPPORTED BY DTS AND COULD (WILL PROBABLY) CHANGE IN THE FUTURE. |    The DialAssist prefs are kept in the DialAssist Pref file in the preference folder (no surprises there)  DialAssist Pref Information   |  | | --- | | ``` File Creator 'dlsu' File Type    'dspf' ``` |   All the relevant info is kept in the resource fork under the following resources:   |  | | --- | | ``` 'DSPF'  0           // Dial Setup prefs record resource id. 'DSPF'  1           // Country Codes list resource id. 'DSPF'  2           // Prefixes list resource id. 'DSPF'  3           // Long Distance Carriers list resource id. 'DSPF'  4           // Suffixes list (Credit Card) resource id.                     // Dial Setup prefs record   'DSPF' 0 {     short       version;     // should be  0     Str31       areaCode;    // Current Area Code     short       numCCodes;   // number of Country codes records     short       curCCode;    // current country code record     void*       reserved;     short       numPrefixes; // number of Prefix records     short       curPrefix;   // current Prefix record     short       notused;     void*       reserved;     short       numCarriers; // number of Long Distance Carrier records     short       curCarrier;  // current Long Distance Carrier record     void*       reserved;     short       numSuffixes; //  number of Suffix (credit card) record     short       curSuffix;   //  current Suffix (credit card) record     void*       reserved; }; // Country codes record  'DSPF' 1 {     Str31       countryName;     Str31       countryCode;     Str31       countryIAC; }; /*     Example Country Codes List 'DSPF' 1      "Australia",           "61",   "0011",      "Austria",             "43",   "00",      "Belgium",             "32",   "00",      "Canada",              "1",    "011",      "Denmark",             "45",   "009",      "Finland",             "358",  "990",      "France",              "33",   "19",      "Germany",             "49",   "00",      "Great Britain",       "44",   "010",      "Greece",              "30",   "00",      "Hong Kong",           "852",  "106",      "Iceland",             "354",  "90",      "Indonesia",           "62",   "00",      "Ireland",             "353",  "16",      "Italy",               "39",   "00",      "Japan",               "81",   "001",      "Malaysia",            "60",   "00",      "Netherlands",         "31",   "09",      "New Zealand",         "64",   "00",      "Norway",              "47",   "095",      "Philippines",         "63",   "00",      "Singapore",           "65",   "005",      "Spain",               "34",   "07",      "Sweden",              "46",   "009",      "Switzerland",         "41",   "00",      "United States",       "1",    "011"  */ // Other Dialing Setup lists  'DSPF' 2 - 3 {     Str31       name;     Str31       code; }; /*     Example Prefixes  List 'DSPF' 2      "Outside Line - 9",        "9,",      "Outside Line - 8",        "8," */  /*     Example Long Distance Carriers  List 'DSPF' 3      "Dial 1",              "1",      "AT&T (USA)",          "10288 0",      "MCI (USA)",           "10222 0",      "Sprint (USA)",        "10333 0" */  /*     Example Suffixes (Credit Card) List 'DSPF' 4      "My Credit Card",      "**** **** **** **** ****",      "My Calling Card",     "**** **** **** **** ****" */ ``` | |

#### [Jul 11 1997]

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
