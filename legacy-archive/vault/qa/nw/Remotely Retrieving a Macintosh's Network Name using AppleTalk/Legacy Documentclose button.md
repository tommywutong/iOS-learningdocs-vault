---
title: Remotely Retrieving a Macintosh's Network Name using AppleTalk
apple_id: DTS10001443
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-05-14'
source_url: https://developer.apple.com/library/archive/qa/nw/nw31.html
archived_at: '2026-07-18T02:29:45.853748Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW31Remotely Retrieving a Macintosh's Network Name using AppleTalk |

|  |  |  |
| --- | --- | --- |
| ---   Q: Given an AppleTalk network and the node address of a Macintosh, how can I remotely retrieve the Network Name specified in the Sharing setup control panel?  A: The only universal way to determine a Macintosh's "flagship" name is to target a NPB lookup of type "workstation" to that particular node. This is Illustrated in the following Etherpeek packet trace.Packet #1  |  | | --- | | ``` Long DDP Header - Datagram Delivery Protocol   Unused:           %00   Hop Count:        %0000   Datagram Length:  59   DDP Checksum:     0x0000   Dest. Network:    43203   Source Network:   43204   Dest Node:        229   Source Node:      213   Dest. Socket:     2  NBP Socket   Source Socket:    253   DDP Type:         2  NBP NBP - Name Binding Protocol   Function:     2  LkUp - Lookup   Tuple Count:  1   NBP ID:       25 NBP Tuple #1   Node Address: 43204.213   Socket Number:253   Enumerator:   0   Object:       =   Type:         workstation   Zone:         Dev Support Center (DTS) ``` |   and the target node replies with this packet: Packet #2  |  | | --- | | ``` Long DDP Header - Datagram Delivery Protocol   Unused:           %00   Hop Count:        %0000   Datagram Length:  46   DDP Checksum:     0x0000   Dest. Network:    43204   Source Network:   43203   Dest Node:        213   Source Node:      229   Dest. Socket:     253   Source Socket:    2  NBP Socket   DDP Type:         2  NBP NBP - Name Binding Protocol   Function:     3  LkUp-Reply   Tuple Count:  1   NBP ID:       25 NBP Tuple #1   Node Address: 43203.229   Socket Number:4   Enumerator:   1   Object:       Jill's IIfx   Type:         Workstation   Zone:         * ``` |   At first glance, it would seem that we could get the desired result by using the `PConfirmName` call (since `PConfirmName` allows us to direct the NBP `LkUp` to the specific node by using the `confirmAddr` field, whereas the `PLookupName` would broadcast it to an entire zone). The `PConfirmName` call does not return the NBP Tuple information to the application, however: under classic AppleTalk, `PConfirmName`'s sole purpose is to confirm or deny the existence of a registered NBP name.  This leaves you with the following alternatives: Under classic AppleTalk:  1. Use the `PLookupName` call. This is a bit complicated because `PLookupName`    requires that you specify the "zone name" of the target node. You have to make    a call to `GetZoneList` and parse through the replies (illustrated in _Inside    Mac: Networking_, pg 4-7) to extract a list of zone name(s) that correspond    to your target's network number. (Note that if you are on an extended network    it is possible for a AppleTalk zone to have a range of network numbers.)   Once you have a list of suspected network zones that the target is on, you can then direct a `PLookupName` to that zone. You will then have to parse through the responses to find the one that matches your target's node address.   2. Form the NBP `LkUp` packet yourself and send it via DDP.   Under classic AppleTalk you can open and register your own DDP listener by using the `POpenSkt` call, forming your own NBP-`LkUp` packet, and transmitting that packet to the target node's NBP listener socket (socket #2) with the `PWriteDDP` call.  The target will respond to you with a NBP LkUp-Reply, which will call back your DDP socket listener. You can parse the reply there.  Writing a DDP socket listener is tricky, but it's illustrated in the Network Watch (DMZ) sample available from DTS sample code library. Examine the `doEcho` function in the files dMZAT.c and SktListener.a.  Writing a socket listener can be challenging under PowerPC because of classic AppleTalk's 68Ks roots. If you are stuck with a classic AppleTalk system, however, this is the recommended approach. Under Open Transport: You're in luck! If your code can run under Open Transport native, you can specify the target address in the `TLookupRequest` data structure used by the `OTLookupName` function. Check out the `DoSendLkUpReq` function in DDPSample.cp, found on any Open Transport SDK CD.  Since the programming model is much simpler, you may want to investigate the Open Transport approach. |

#### [May 14 1996]

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
