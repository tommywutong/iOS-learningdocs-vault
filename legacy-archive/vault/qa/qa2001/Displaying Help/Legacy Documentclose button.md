---
title: Displaying Help
apple_id: DTS10001562
resource_type: QA
platform: macOS
topic: User Experience
technology: Carbon
published: '2001-02-21'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1006.html
archived_at: '2026-07-18T02:38:01.248978Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [User Experience](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxUserExperience-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [User Experience > Help Technologies](https://developer.apple.com/referencelibrary/UserExperience/idxHelpTechnologies-date.html)

|  |
| --- |
| Technical Q&A QA1006Displaying Help |

|  |  |  |
| --- | --- | --- |
| ---   Q: My application's help is provided in a collection of HTML files viewable in the Help Viewer. What is the quickest way to display information about a particular topic?  A: Your application can call the `AHLookupAnchor` routine to display help about particular topics in your help files. `AHLookupAnchor` asks the Help Viewer to search your application's help book and present the page containing a particular HTML anchor scrolled so the anchor's location is visible.     |  | | --- | | ```      /* GoToMyHelpAnchor can be used to tell Apple Help to find     the page containing the named anchor and display the text     immediately below that anchor in the main view.      anchorName - the name of the anchor you would like to display.     This routine illustrates a convenient way to use the AHLookupAnchor     routine to look up anchors in your application's help book.  */  OSStatus GoToMyHelpAnchor(CFStringRef anchorName) {     CFBundleRef myAppsBundle;     CFTypeRef myBookName;     OSStatus err;          /* set up a known state */     myAppsBundle = NULL;     myBookName = NULL;          /* Get our application's main bundle         from Core Foundation */     myAppsBundle = CFBundleGetMainBundle();     if (myAppsBundle == NULL) { err = fnfErr; goto bail; }          /* get the help book's name */     myBookName = CFBundleGetValueForInfoDictionaryKey(                    myAppsBundle, CFSTR("CFBundleHelpBookName"));     if (myAppsBundle == NULL) { err = fnfErr; goto bail; }          /* go to the page */     err = AHLookupAnchor( myBookName, anchorName);     if (err != noErr) goto bail;          /* done */     return noErr; bail:     return err; }  Examples:  err = GoToMyHelpAnchor(CFSTR("surfing")); err = GoToMyHelpAnchor(CFSTR("seaboards")); ``` | | __Listing 1__. Displaying help using the AHLookupAnchor routine. |     Using `AHLookupAnchor` in your application means your application does not need to keep track of the names of the files where particular help content appears - your application only needs to track the anchor name used to locate particular help content.  This allows your help content creators greater freedom when designing and maintaining your help content as they can move information from file to file or redesign the look of your help pages without worrying about the help book getting out of sync with how your application asks the Help Viewer to present information about particular topics.   ---  [Feb 21 2001] |

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
