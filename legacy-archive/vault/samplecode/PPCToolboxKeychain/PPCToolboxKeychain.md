---
title: PPCToolboxKeychain
apple_id: DTS10000210
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-14'
source_url: https://developer.apple.com/library/archive/samplecode/PPCToolboxKeychain/Introduction/Intro.html
archived_at: '2026-07-18T03:18:36.182553Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](MIB%20Bits-MoreAEObjects.c.md)

# PPCToolboxKeychain

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-03-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Mac OS 9 Mac OS 9 or higher |

This sample demonstrates the subtleties needed to create a PPC Toolbox keychain item. PPC Toolbox uses generic password keychain items, however it stores the address of the remote machine in an non-obvious fashion. This sample shows how to 'bless' a generic password keychain item so that it can be used by the PPC Toolbox. The ultimate goal of this sample is to allow you to programmatically send Apple events to a remote machine without any user interaction. Requirements: Mac OS 9 or higher Keywords: Apple events, AppleEvents, PPC Toolbox, AutoGuest INIT

[Next](MIB%20Bits-MoreAEObjects.c.md)

