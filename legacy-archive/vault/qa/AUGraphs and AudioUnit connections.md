---
title: AUGraphs and AudioUnit connections
apple_id: DTS10002384
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2003-12-09'
source_url: https://developer.apple.com/library/archive/qa/qa1174/_index.html
archived_at: '2026-07-18T02:30:12.087836Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1174

# AUGraphs and AudioUnit connections

## Q:  Can I connect a single output bus of an AudioUnit to more than one destination AudioUnit at a time? A: You cannot connect a single output bus of an AudioUnit to more than one destination AudioUnit at a time.

A: Can I connect a single output bus of an AudioUnit to more than one destination AudioUnit at a time? A: You cannot connect a single output bus of an AudioUnit to more than one destination AudioUnit at a time.

Supporting this would require every AudioUnit would to: buffer the data it renders, and do the same work more than once. Neither case is desirable because of the extra memory required and slower performance. Therefore, these type of connections are not allowed in an AUGraph.

If this type of operation is needed a Matrix Mixer AudioUnit can be used. This AudioUnit can distribute results from multiple input sources to multiple output destinations. See sample code MatrixMixerTest in the SDK for more information.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2003-12-09 | New document that discusses AudioUnit connection issues when using more than one AudioUnit or an AUGraph. |

