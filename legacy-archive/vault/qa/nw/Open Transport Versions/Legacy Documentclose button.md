---
title: Open Transport Versions
apple_id: DTS10001476
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-05-08'
source_url: https://developer.apple.com/library/archive/qa/nw/nw64.html
archived_at: '2026-07-18T02:29:47.808415Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Networking > Carbon](https://developer.apple.com/referencelibrary/Networking/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A NW64Open Transport Versions |

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ---   Q: Where can I get a definitive list of all the versions of Open Transport and their features?  A: Right here.   | Vers. | Systems | Distribution | Features | | --- | --- | --- | --- | | 1.0 | 7.5.2 on 9500 | pre-installed on CPU | initial release | | 1.0.1 | as per 1.0 | electronic update | data corruption bug fixes | | 1.0.6 | 7.5.2 version 2 on 7200/7500/8500/9500 | pre-installed on CPU | many bug fixes | | 1.0.7 | as per 1.0.6 | electronic update only | mostly `'mdev'` compatibility fixes | | 1.0.8 | as per 1.0.6 | electronic full install | MacTCP backward compatibility fixes, BOOTP/DHCP fixes | | 1.1 | 7.1.x, 7.5.3 (all flavors), 7.5.5 | system update ([7.5.3](https://developer.apple.com/technotes/tn/tn1017.html#RTFToC28), all flavors),  standalone retail product,  system software ([7.5.3](https://developer.apple.com/technotes/tn/tn1017.html#RTFToC28)) | support for all hardware (except [NuBus PowerPC Performas](#apple-jz2ue5ltkbxxozlskbbvazlsmzxxe3lbom)), performance tuning, many bug fixes | | 1.1.1 | 7.1.x, 7.5.3 (all flavors), 7.6, 7.6.1 | electronic full install for NuBus PowerPC Performas,  electronic update from OT 1.1 for other hardware,  system software ([7.6](https://developer.apple.com/technotes/tn/tn1090.html#OpenTransport), [7.6.1](https://developer.apple.com/technotes/tn/tn1096.html)),  system update ([7.6.1](https://developer.apple.com/technotes/tn/tn1096.html)) | tilisten, sync idle events, third party port scanners and configurators, performance tuning, serial fixes, other bug fixes | | 1.1.2 | as per 1.1.1 | electronic full install for NuBus PowerPC Performas,  electronic update from OT 1.1 for other hardware | PAP server fixes, serial fixes | | 1.2 | 8.0 | system software ([8.0](https://developer.apple.com/technotes/tn/tn1102.html#opentransport)) | CFM-68K support, SYN flood and ping of death fixes, PAP fixes | | 1.2.1 | as per 1.2 | AppleShare IP 5.0.2 update CD | AppleShare-specific bug fixes | | 1.3 | 8.1 | system update,  system software ([8.1](https://developer.apple.com/technotes/tn/tn1121.html#Open%20Transport%201.3)) | single link multihoming, tilisten fixes, PAP fixes, CFM port scanners and configurators | | 1.3.1 | as per 1.3 | electronic update,  system software ([8.1](https://developer.apple.com/technotes/tn/tn1121.html#Open%20Transport%201.3)) | fixes cosmetic problem with library resource forks | | 2.0.1 | 8.5 | system software ([8.5](https://developer.apple.com/technotes/tn/tn1142/part73.html)) | DHCP client ID, SNMP support, RFC 1877 support, DHCP autonet | | 2.0.3 | 8.6 | system update,  system software ([8.6](https://developer.apple.com/technotes/tn/tn1163.html#opentransport)) | DHCP fixes, PAP fixes | | 2.5.1 | 8.6 on [early AirPort-capable computers](#apple-ifuxeudpoj2egylqmfrgyzi) | pre-installed on CPU | update MPS (3.3) and Mentat TCP/IP (3.5), fewer libraries, wake on LAN support | | 2.5.2 | 9.0, 8.6 on [early AirPort-capable computers](#apple-ifuxeudpoj2egylqmfrgyzi) | system software ([9.0](https://developer.apple.com/technotes/tn/tn1176.html#opentransport)),  AirPort 1.0 software | 2.5.1 features plus minor bug fixes | | 2.6 | 9.0.2 on early 2000 CPUs, 9.0, 8.6 on [early AirPort-capable computers](#apple-ifuxeudpoj2egylqmfrgyzi) | automatic update,  electronic update,  pre-installed on CPU,  AirPort 1.1 software | see Technote 1194 [Mac OS Update 9.0.4](https://developer.apple.com/technotes/tn/tn1194.html#opentpt) (path MTU, ARP storm, async DHCP, DHCP fixes, `strlog`, etc) | | 2.6.1 | 9.0.4 | pre-installed on CPU,  automatic update,  electronic update | minor AirPort fixes |   __Notes:__   - NuBus PowerPC   Performas include the Power Mac 52xx, 53xx, 62xx, and   63xx and all derivatives (except the Power Mac 6360). - Early units of the   iBook, the slot-loading iMacs, and the Power Mac G4 (AGP   Graphics) shipped with a special version of Mac OS 8.6   that supports OT 2.5.x. OT 2.5.x is not supported under   8.6 on any other hardware. - Apple strongly recommends that your software require   Open Transport 1.1.1 or greater. Older versions of Open   Transport are either very buggy (OT 1.0.x) or not   supported on all hardware (OT 1.1). In addition, Open   Transport 1.1.1 contains critical developer features   (tilisten, sync idle events, third-party port scanners   and configurators) that your software may depend on. - For more detailed information about the history of   OT's DHCP implementation, see Tech Info Library article   [58372](http://til.info.apple.com/techinfo.nsf/artnum/n58372). |

#### [May 08 2000]

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
