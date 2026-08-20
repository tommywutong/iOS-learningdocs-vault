---
title: SetSoundMediaBalance balance parameter clarification
apple_id: DTS10002019
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-12'
source_url: https://developer.apple.com/library/archive/qa/qtmtb49/_index.html
archived_at: '2026-07-18T02:38:49.920639Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QTMTB49

# SetSoundMediaBalance balance parameter clarification

## Q:  Q: I'm having problems with the QuickTime SetSoundMediaBalance (MediaSetSoundBalance) function. The ranges I'm using for the balance parameter are from -1.0 to 1.0, but no matter what value I pass I'm not hearing much of a difference in either the left or right channel output. What's going on?

A: The balance parameter value may range from -128 to 127. Negative values emphasize the left sound channel, while positive values emphasize the right sound channel. A value of -128 forces all output through the left channel. Similarly, a value of 127 forces all output through the right channel.

Passing a positive balance value causes the left channel to get quieter.

Passing a negative balance value causes the right channel to get quieter.

The amount it gets quieter can be seen in the following examples:

A balance value of 32 would lower the left volume by one quarter of its current value (since 32 is a quarter of 127, the full volume setting). A balance value of -96 would lower the right volume by 3/4 of its current value (since 96 is 3/4 of 128).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-12-01 | Editorial |
| 1998-10-19 | New document that describes correct parameter values for the SetSoundMediaBalance routine. |

