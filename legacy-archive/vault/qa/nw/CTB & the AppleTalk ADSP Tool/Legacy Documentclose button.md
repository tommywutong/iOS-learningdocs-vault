---
title: CTB & the AppleTalk ADSP Tool
apple_id: DTS10001415
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/nw/nw03.html
archived_at: '2026-07-18T02:29:44.063336Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Carbon](https://developer.apple.com/referencelibrary/Carbon/index.html)

|  |
| --- |
| Technical Q&A NW03CTB & the AppleTalk ADSP Tool |

|  |  |  |
| --- | --- | --- |
| ---   Q: I have a question about the CTB & the AppleTalk ADSP Tool.  I have a connection between two machines using the ADSP Tool. The local machine writes a bunch of data to the remote machine, then wants to shut down the connection. I use a `CMStatus` call to verify that there isn't a write pending, and also check the buffer sizes returned by the `CMStatus` call and verify that there is nothing in the `cmDataOut` part of the sizes array. I then call `CMClose`, and the connection closes. The problem is the remote machine has not received all of the data before the connection is closed! How do I detect if the ADSP Tool has "really" written all the data? Or how do I invoke the `CMClose` so that it properly concludes the write (i.e., setting the abort parameter to 0 when doing the `dspRemove` to the ADSP Driver)?  I've tried two `CMClose` variations:  In one case, I make a synchronous call to `CMClose` as follows (in Pascal):   |  | | --- | | ```      theErr := CMClose(theConnection, FALSE, NIL, 0, FALSE); ``` |   This call exhibits the behavior I've described above.  I've also tried an asynchronous call, in the hope that the ADSP Tool would handle finishing off the connection properly:   |  | | --- | | ```   theErr := CMClose(theConnection, TRUE, nil, 60, FALSE);   while (theErr = noErr) and     (BAND(status, cmStatusOPEN + cmStatusClosing) <> 0) do   begin     CPI_Idle(theConnection);     theErr := CPI_Status(theConnection, sizes, status);    end; ``` |   What I've found in this case is that the ADSP Tool never completes the write. I've varied the timeout from 60 above to -1 and also 6000. In all of these cases, the `cmStatusClosing` bit is ALWAYS set, and never goes low. Any suggestions?  A: You're using the correct options on your call to `CMClose`, i.e., finishing all pending writes and then closing the connection.  Making the assumption that you're also using the ADSP Tool on the receiving end of the connection, it's possible that the data has been received and then the connection closed down. The receiver should be called with `CMStatus` to see if there is data to read, regardless of whether the `cmStatusOpen` bit is set; if `cmStatusDataAvail` is set, the connection can still be read for additional data, even if it is closed. The Tool may have buffered the incoming data and then completed the close connection request from the sender.  Check to see that you are testing the flags parameter of `CMStatus` on the receiver side against `cmStatusDataAvail` and basing your final read on that. |

#### [May 01 1995]

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
