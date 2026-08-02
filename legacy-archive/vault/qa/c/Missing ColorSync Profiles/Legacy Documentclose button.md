---
title: Missing ColorSync Profiles
apple_id: DTS10001141
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '1999-05-03'
source_url: https://developer.apple.com/library/archive/qa/c/cs13.html
archived_at: '2026-07-18T02:29:25.299090Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Graphics & Imaging > ColorSync](https://developer.apple.com/referencelibrary/GraphicsImaging/idxColorSync-date.html)

|  |
| --- |
| Technical Q&A CS13Missing ColorSync Profiles |

|  |
| --- |
| ---   Q: I've just installed ColorSync 2.6 and noticed some of my profiles no longer show up in the ColorSync control panel or the ColorSync plug-ins pop-up menus, even though they are properly installed in the "ColorSync Profiles" folder? What's going on?  A: One important change in the recent release of ColorSync (version 2.6) is how it handles the description (`'desc'`) tag of ICC profiles.  The `'desc'` tag of a profile, as defined by the ICC, contains up to three strings. The first is a required 7-bit roman ASCII string. The second is an optional localized Unicode string. The third, also optional, is a localized string in Mac script-code format. Applications typically use one of the available strings to show the name of profiles in a list or pop-up menu. There are a few other important devilish details in the ICC definition of the `'desc'` tag. One is that all three strings must be null terminated. Another is that all three strings are preceded by a character count that includes the null terminator. It also worth noting that for the Unicode string, the character count must not be confused with a byte count because each Unicode character requires two bytes.  Previous releases of ColorSync only make partial use of this tag and as a result performed only limited error checking on its contents. For example, the ColorSync function `CMGetScriptProfileDescription` would return the Mac script-code from a profile if it was present and, if not, it would return the 7-bit roman ASCII string. The Unicode string was simply ignored and in some cases, if the Unicode and/or Mac script-code string were non-compliant, ColorSync would return garbage (or the ACSII string if you were lucky) without returning `cmProfileErr` code.  ColorSync 2.6 is the first release of the technology that was designed to run both on Mac OS and Windows. Since Mac script-code format strings are not usable on Windows, ColorSync clients need to have access to the localized Unicode string. (Unicode strings are also becoming more usable on Macs.) For this reason a new call, `CMGetProfileDescriptions`, was added to access all three possible strings. In doing so much stricter attention had to be paid to the compliance of the `'desc'` tag. For example, if either the ASCII string or the Mac script-code strings is not null terminated or if any of the string's character counts are invalid or beyond the range of the `'desc'` tag, the and `cmProfileErr` code is returned.  In order to achieve optimal performance when applications add profiles to a list or pop-up menu, ColorSync maintains a cache of all the profiles installed in the "ColorSync Profiles" folder and its sub-directories. Among other things, this cache file contains the three possible names of each profile obtained by calling `CMGetProfileDescriptions`. If `CMGetProfileDescriptions` returns an error because the `'desc'` tag is non-compliant, then the profile is not added to the cache. This is why non-compliant profiles--even though they are properly installed in the "ColorSync Profiles" folder--no longer show up in the ColorSync control panel or the ColorSync plug-ins pop-up menus with ColorSync 2.6 installed.  The remedy for this problem is to repair the affected profiles. Unfortunately the "Rename Profile" AppleScript that is installed as part of ColorSync 2.6 cannot be used to repair profiles with bad `'desc'` tags because it can only operate on profiles in the ColorSync profile cache. Instead, a simple stand-alone tool called "Profile First Aid" to verify and repair any profile will be made available on the [ColorSync web site](http://www.apple.com/colorsync/). |

#### [May 03 1999]

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
