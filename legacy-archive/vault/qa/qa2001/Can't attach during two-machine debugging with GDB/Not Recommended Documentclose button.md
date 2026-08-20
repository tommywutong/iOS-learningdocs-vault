---
title: Can't attach during two-machine debugging with GDB
apple_id: DTS10001573
resource_type: QA
platform: Xcode Developer Tools
topic: null
technology: null
published: '2003-06-02'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1019.html
archived_at: '2026-07-18T02:38:01.964162Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Tools](https://developer.apple.com/library/archive/technicalqas/DeveloperTools/index.html) > [Compiling & Debugging](https://developer.apple.com/library/archive/technicalqas/DeveloperTools/idxCompilersDebuggers-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Tools > Compiling & Debugging](https://developer.apple.com/referencelibrary/DeveloperTools/idxCompilersDebuggers-date.html)

|  |
| --- |
| Technical Q&A QA1019Can't attach during two-machine debugging with GDB |

|  |  |  |
| --- | --- | --- |
| ---   Q: I have a simple two machine network for doing two-machine debugging with GDB on Mac OS X. I try to attach to the target machine using its IP address such as:     |  | | --- | | ```     attach 111.22.33.44 ``` |    But I always get these errors back:     |  | | --- | | ```     kdp_bind_remote: unable to resolve host "111.22.33.44"     unable to create connection for host "111.22.33.44":RR_LOOKUP ``` |    Why can't I attach to the target machine?  A: You are probably running a version of Mac OS X older than 10.1. Prior to 10.1, GDB's `attach` command expects a hostname; an IP address won't work (r. 2499453). The remainder of this Q&A assumes you can't upgrade your system to Mac OS X 10.1 or later.  If your network has a domain name server, make sure that the target machine's hostname and IP address are defined in the DNS.  If you don't have a DNS on the network, such as the case where you've just hooked two machines together with a crossover cable or a standalone hub, you'll need to define hostnames on both systems in their local NetInfo databases. (This is equivalent to setting up a hosts file on Mac OS 9 or UNIX.)  Here are the steps to do this:     1. Launch `/Applications/Utilities/NetInfo Manager.` 2. To allow editing the NetInfo database, click the lock    button in the lower left corner of the window. 3. Enter your admin password and click OK. 4. In the second column of the browser view, select the node    named "machines". You'll see entries for -DHCP-,    broadcasthost, and localhost in the third column. 5. The quickest way to create a new entry is to duplicate    an existing one. So select the "localhost" item    in the third column. 6. Select Duplicate from the Edit menu. 7. A confirmation alert will appear. Click "Duplicate". 8. A new entry called "localhost copy" will appear,    and its properties will be shown below the browser view.    Double click the value of the "ip_address" property and enter    the IP address of the other machine. 9. Double click the value of the "name" property and enter    the hostname you want for the other machine. (This is the    name you'll use in the GDB `attach` command.) 10. Single click the "serves" property and select Delete from     the Edit menu. 11. Choose Save from the File menu. 12. A confirmation alert will appear. Click "Update     this copy". 13. Repeat steps 6-12 for each additional host entry you     wish to add, otherwise choose Quit from the NetInfo Manager     menu. You do not need to reboot.  ---  [Jun 02, 2003] |

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
