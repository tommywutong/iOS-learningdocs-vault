---
title: OT PAPServerSample
apple_id: DTS10000243
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/OT_PAPServerSample/Introduction/Intro.html
archived_at: '2026-07-18T03:17:26.556962Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ATalkSampleUtils.c.md)

# OT PAPServerSample

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-07-22 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon SSW 7.6 with OT 1.1.2 or greater. For multiple handoff endpoint support, OT 2.0 with SSW 8.5 is required. To open the project files, Metrowerks CodeWarrior Pro 2.0, IDE v2.1 is required. |

The PAPServerSample demonstrates the use of the Open Transport to create a Printer Access Protocol Server. This sample supports multiple simultaneous connections under OT 2.0 and greater. PAPServerSample demonstrates some of the following network programming techniques 1. Implementing a PAP Server which supports multiple handoff endpoints. 2. Using the OTIoctl to enable selfsend mode. 3. Using OptionManagement to enable the EOM (End-of-message option). 4. Using OptionManagement to set the default server message. The sample provides a user option to make the OTServerLimits call and to also dump the packets that are received. Note that by default, the incoming packets are saved to a file called "SavedPAPFileXX". You can launch the server on the same system that you use the client to send data to the client. Requirements: SSW 7.6 with OT 1.1.2 or greater. For multiple handoff endpoint support, OT 2.0 with SSW 8.5 is required. To open the project files, Metrowerks CodeWarrior Pro 2.0, IDE v2.1 is required. Keywords: Open Transport, PAP, AppleTalk, Printer Access Protocol, handoff endpoints, AppleTalk Transaction Protocol, ATP, OT PAPServerSample

[Next](ATalkSampleUtils.c.md)

