---
title: 'LaserWriter 8.3 %%?BeginQuery: RBIAppleDevice Query'
apple_id: DTS10001767
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-01'
source_url: https://developer.apple.com/library/archive/qa/qd/qd08.html
archived_at: '2026-07-18T02:38:35.584689Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Printing](https://developer.apple.com/referencelibrary/Printing/index.html)

|  |
| --- |
| Technical Q&A QD08LaserWriter 8.3 %%?BeginQuery: RBIAppleDevice Query |

|  |
| --- |
| ---   Q: I've been checking out LaserWriter 8.3fc2 for compatibility with our network printing products (NetWare for Macintosh Print Services and NetWare Client for Macintosh), and was dissapointed to see that it uses a new, nonstandard printer query (`%%?BeginQuery: RBIAppleDevice`) at Setup and Print time.  New queries, particularly non-standard ones not documented in the PostScript Language Reference Manual, are problematical for AppleTalk printer spoolers that use the Adobe Document Structuring Conventions to recognize and respond to queries. Unlike printers, which simply execute the PostScript code to generate the correct response to the query, spoolers need to be explicitly coded to handle any new query. Thus, products in the field are obsoleted when a new driver comes out that makes a query that hasn't been used or documented before. The spooler must use the default response encoded in the query instead of returning the correct information.  In this case, the new query is particularly annoying, because it is unnecessary. The query, which is presumably used to determine if the printer is an Apple device, merely has the printer scan its product name for the string "LaserWriter". This could have been just as easily accomplished on the Macintosh using the results of the "`%%?BeginFeatureQuery: *Product`" query. Why ask the printer for information you already have, especially since this breaks existing spoolers in the process?  Is it possible to remove remove this query, and if not, what adverse affects will result from the printer/spooler always returning "Unknown"?  A: The query comments are set up so that when a spooler doesn't recognize a comment, it returns the contents of the `%%?EndFeatureQuery`: line. Thus, adding new queries does not break correctly built spoolers. In the case of the `RBIAppleDevice` query, the spooler should return Unknown.  The `RBIAppleDevice` query is different from the product query in that the> `RBIAppleDevice` returns true or false. True is returned if the printer is an> Apple product. The reply to this query is used to decide whether JPEG data should be sent to the printer. We implemented the JPEG switch this way so that you can easily change the contents of the query to cause the driver to allow JPEG data to be sent to non-Apple printers.  The new query shouldn't cause any problems for spoolers, since they should return "unknown", and we send the normal image data to the spooler. The only adverse effect is the driver won't pass JPEG image data through to an Apple printer on the other side of a spooler. When we open JPEG up for everyone, the JPEG data will be passed through to both spoolers and non-Apple printers. |

#### [Jul 01 1995]

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
