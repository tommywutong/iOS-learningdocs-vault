---
title: TCP Application Acquires Different Port Address After Relaunch
apple_id: DTS10001440
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-05-14'
source_url: https://developer.apple.com/library/archive/qa/nw/nw28.html
archived_at: '2026-07-18T02:29:45.623436Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md) · [Receiving UDP Broadcasts](Not%20Recommended%20Documentclose%20button.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/Networking/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Networking/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Networking > Carbon](https://developer.apple.com/referencelibrary/Networking/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A NW28TCP Application Acquires Different Port Address After Relaunch |

|  |  |
| --- | --- |
| ---   Q: In my Open Transport TCP based server application, I use a specific socket for receiving incoming connection requests.  If I relaunch the server immediately after quitting, the initialization calls complete without error, but the server never receives any incoming connection requests. If I wait several minutes before restarting the server, this problem doesn't occur. It appears that there is some internal timeout for disconnected connections. Is there a solution to this problem so that the server can be launched without waiting for the timeout?  A: TCP has a 2-minute timeout on a binding after a connection has closed before the same port can be bound to again. This prevents stale data from corrupting a new connection. For this reason, you see a delay before you can successfully bind to the port again.  There is a way around this, using the `IP_REUSEADDR` option and the `OTOptionManagement` call. Set this option on all of your listening endpoints before you bind, and the problem should disappear.  Important - even after using the `IP_REUSEADDR` option, at most one endpoint that is in a state less than connected (listening; unbound doesn't count) may be bound to a given port. Any number of connected or closing endpoints may be so bound to other unique ports, however.  The following sample will help to show how to set this option. The function takes 2 input parameters, the `EndpointRef` that you want to set the option for, and the state of the option that you want, typically, true. The function returns a result of `OSStatus`. If the result is less than zero, then it it the result of making the `OTOptionManagement` call. If the result is positive, then the call completed successfully, but the status field had a value other than `T_SUCCESS`.   |  | | --- | | ``` #include <OpenTransport.h>            // open transport files #include <OpenTptInternet.h>  /* input: noDelayState - true - nodelay //                         false - normal delay state // // output:    if result less that kOTNoError, then the result of //        OTOptionManagement call is returned //        otherwise, the status value is returned as defined in //        OpenTransport.h         T_SUCCESS    = 0x020,        return kOTNoError if SUCCESS         T_FAILURE    = 0x040,         T_PARTSUCCESS    = 0x100,         T_READONLY    = 0x200,         T_NOTSUPPORT    = 0x400  */ OSStatus DoNegotiateIPReuseAddrOption(EndpointRef ep, Boolean reuseState) {     UInt8        buf[kOTFourByteOptionSize];    // define buffer for fourByte                             // Option size     TOption*    opt;                // option ptr to make items                             // easier to access     TOptMgmt    req;     OSStatus    err;     Boolean        isAsync = false;      opt = (TOption*)buf;                // set option ptr to buffer     req.opt.buf    = buf;     req.opt.len    = sizeof(buf);     req.opt.maxlen = sizeof(buf);            // were using ret for the                             // return result also.     req.flags    = T_NEGOTIATE;            // negotiate for option      opt->level    = INET_IP;            // dealing with an IP Level                             // function     opt->name    = IP_REUSEADDR;     opt->len    = kOTFourByteOptionSize;     *(UInt32*)opt->value = reuseState;        // set the desired option                             // level, true or false     if (OTIsSynchronous(ep) == false)        // check whether ep sync or                             // not     {         isAsync = true;            // set flag if async         OTSetSynchronous(ep);            // set endpoint to sync     }      err = OTOptionManagement(ep, &req, &req);      if (isAsync == true)                // restore ep state if                             // necessary         OTSetAsynchronous(ep);          // if no error then check the option status value     if (err == kOTNoError)     {         if (opt->status != T_SUCCESS)     // if not T_SUCCESS, return                             // the status             err = opt->status;     }    // otherwise return kOTNOError     return err; } ``` | |

#### [May 01 1996]

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
