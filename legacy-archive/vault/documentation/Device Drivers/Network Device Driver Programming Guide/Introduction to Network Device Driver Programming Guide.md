---
title: Network Device Driver Programming Guide
apple_id: TP40000913
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2008-03-11'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/NetworkDriver/1_Intro/Intro.html
archived_at: '2026-07-15T07:31:32.941614Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](I-O%20Networking%20Family%20API.md)

# Introduction to Network Device Driver Programming Guide

_Network Device Driver Programming Guide_ is an introduction to developing network device drivers, and a companion to the source code available in the Darwin Projects Directory, [http://www.opensource.apple.com/darwinsource/Current](http://www.opensource.apple.com/darwinsource/Current/). You will find this document most useful if you examine a sample network driver as you read it. This document will refer to the AppleUSBCDCDriver. Code for this driver can be found at [http://www.opensource.apple.com/darwinsource/tarballs/apsl/AppleUSBCDCDriver-314.4.1.tar.gz](http://www.opensource.apple.com/darwinsource/tarballs/apsl/AppleUSBCDCDriver-314.4.1.tar.gz).

This book assumes some familiarity with programming the OS X kernel and the I/O Kit. For a broad overview of the OS X kernel see _Kernel Programming_. If you need more information about the I/O kit, please read _Writing an I/O Kit Device Driver_ and _I/O Kit Fundamentals_.

_Network Device Driver Programming Guide_ is intended for anyone who wants to develop network drivers for OS X.

Apple maintains several websites where developers can go for general and technical information on OS X.

- Darwin Projects Directory—Open source drivers for use with Darwin ([http://www.opensource.apple.com/darwinsource/Current/](http://www.opensource.apple.com/darwinsource/Current/))
- Apple Developer Connection—Developer Documentation ([http://developer.apple.com/documentation](https://developer.apple.com/documentation)). Features the same documentation that is installed on OS X, except that often the documentation is more up-to-date. Also includes legacy documentation.
- AppleCare Knowledge Base ([http://www.apple.com/support](http://www.apple.com/support/)). Contains technical articles, tutorials, FAQs, technical notes, and other information.
- Apple Developer Connection—OS X ([http://developer.apple.com/devcenter/macosx](https://developer.apple.com/devcenter/macosx)). Offers SDKs, release notes, product notes and reviews, and other resources and information related to OS X.

[Next](I-O%20Networking%20Family%20API.md)

