---
title: Extracting InstaCompOne Archive Files
apple_id: DTS10001539
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-03-14'
source_url: https://developer.apple.com/library/archive/qa/plat/plat29.html
archived_at: '2026-07-18T02:29:53.946420Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A PLAT29Extracting InstaCompOne Archive Files |

|  |
| --- |
| ---   Q: When I attempted to extract a file from an InstaCompOne archive I got an error #28202 -- "The compressed file or resource was not found in the catalog of the archive." When I run ScriptCheck, I got this warning: "You should probably use a ScriptCheck extension to compute the correct target size for 'infa' ID = XXXX."  A: This type of error occurs because you do not have the InstaCompOne ScriptCheck extension available. The InstaCompOne documentation says:  To enable ScriptCheck for use with InstaCompOne archives:   1. Place a copy of the file "InstaCompOneSCExt.rsrc" in the same folder    as your Installer script source file (myInstallScript.r, etc.). 2. Rename the file so that it has the same name as the install script    source but uses the filename extension of ".scx". Example: "myInstallScript.scx"   However, this assumes that the .r file is the name of the resulting script, i.e., the resulting Installer script will be called "myInstallScript". Actually, the InstaCompOneSCExt.rsrc file should take the name of your resulting script. For instance, if "myInstallScript.r" produces a script named "InstallScript," then the "InstaCompOneSCExt.rsrc" file should be called "InstallScript.scx", __NOT__ "myInstallScript.scx." |

#### [Mar 14 1997]

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
