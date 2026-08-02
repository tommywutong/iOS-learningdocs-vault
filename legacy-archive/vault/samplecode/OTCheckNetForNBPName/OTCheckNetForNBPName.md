---
title: OTCheckNetForNBPName
apple_id: DTS10000707
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/OTCheckNetForNBPName/Introduction/Intro.html
archived_at: '2026-07-18T03:17:10.232626Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Carbon.r.md)

# OTCheckNetForNBPName

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ |  |

The OTCheckNetForNBPName sample demonstrates the use of the Open Transport under Carbon, to search an AppleTalk network for an NBP entity using multiple simultaneous searches to reduce the lookup time. This sample demonstrates how to 1. find the number of AppleTalk zones present by dynamically increasing the buffer size until a kOTBufferOverflowErr is no longer returned. 2. Use multiple lookup request and reply structures in order to reduce the amount of time required to search the network. 3. Use asynchronous lookup requests so that other actions can be taken while performing the lookup. 4. Turn on self send globally 5. Register/deregister an entity with OT.

[Next](Carbon.r.md)

