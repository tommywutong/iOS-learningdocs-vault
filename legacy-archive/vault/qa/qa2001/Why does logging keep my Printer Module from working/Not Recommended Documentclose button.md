---
title: Why does logging keep my Printer Module from working?
apple_id: DTS10001711
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2002-11-06'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1182.html
archived_at: '2026-07-18T02:38:17.156569Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/Printing/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/Printing/idxHardwareDrivers-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Printing > Hardware & Drivers](https://developer.apple.com/referencelibrary/Printing/idxHardwareDrivers-date.html)

|  |
| --- |
| Technical Q&A QA1182Why does logging keep my Printer Module from working? |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ---   Q: Why does logging keep my Printer Module from working? This used to work fine in Mac OS X 10.0 and 10.1.  A: Unlike in previous versions of Mac OS X, in Mac OS X 10.2 (Jaguar) the printing system (CUPS) makes use of `stdout` to route information between modules. Any code in a Printer Module (PM) or I/O Module (IOM) that tries to log to `stdout` via `printf`, etc., will interfere with the printing system. If you must write to a log file, use `fprintf` to write to a specific file or send your log information to `stderr`. See Listing 1 for examples.    |  | | --- | | ``` //    Write to /private/var/log/cups/error_log fprintf( stderr, "This message will appear in the CUPS error log." );  //    Write to your own log file fprintf( file, "This message will appear in your own log file" ); ``` | | __Listing 1__. Logging examples |   Be aware that on Jaguar your PMs and IOMs run as daemon and not the currently logged in user, so if you are logging to a file via fprintf you'll need to set the appropriate permissions on the destination directory.  As an additional debugging aid, you can adjust the logging level for the CUPS "error_log" file by editing the CUPS configuration file "/etc/cups/cupsd.conf" and changing `LogLevel`. Listing 2 shows the relevant section from "cupsd.conf" that you will need to edit.   |  | | --- | | ``` # # LogLevel: controls the number of messages logged to the ErrorLog # file and can be one of the following: # #     debug2    Log everything. #     debug    Log almost everything. #     info      Log all requests and state changes. #     warn      Log errors and warnings. #     error     Log only errors. #     none      Log nothing. #  LogLevel info ``` | | __Listing 2__. Controlling the "error_log" logging level from "cups.conf" |    ---  [Nov 06 2002] |

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
