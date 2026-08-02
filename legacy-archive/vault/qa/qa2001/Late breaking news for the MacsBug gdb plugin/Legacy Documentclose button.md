---
title: Late breaking news for the MacsBug gdb plugin
apple_id: DTS10001584
resource_type: QA
platform: Xcode Developer Tools
topic: null
technology: null
published: '2001-05-03'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1032.html
archived_at: '2026-07-18T02:38:03.701549Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Tools](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxTools-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Tools > Compiling & Debugging](https://developer.apple.com/referencelibrary/DeveloperTools/idxCompilersDebuggers-date.html)

|  |
| --- |
| Technical Q&A QA1032Late breaking news for the MacsBug gdb plugin |

|  |
| --- |
| ---   Q: How can I get the gdb MacsBug plugin to work properly in Mac OS X 10.0?  A: A special MacsBug plugin ships for gdb on the Mac OS X Developer CD, enabling you to use many of the traditional MacsBug commands from gdb. Instructions, etc. can be found in /usr/libexec/gdb/plugins/MacsBug/README.txt (Enter this path minus 'README.txt' in Finder's Go To Folder sheet to go there). There are a couple of issues, however, with the plugin:  1) Due to a build error, the file /usr/libexec/gdb/plugins/MacsBug/gdbinit-MacsBug needs one line to be manually edited. The load-plugin line in the last line of the file needs to look like,  load-plugin /usr/libexec/gdb/plugins/MacsBug/MacsBug  In other words delete the portion of the pathname preceding /usr.  Note that since this file is within /usr you need to run your editor with 'sudo' (to gain a higher level of permissions; for example, 'sudo /Applications/TextEdit.app/Contents/MacOS/TextEdit /usr/libexec/gdb/plugins/MacsBug/gdbinit-MacsBug' from the command line) to allow the update.  2) The README file mentions an install-MacsBug script. That file was not installed so that portion of the README should be ignored.     ---  [May 03 2001] |

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
