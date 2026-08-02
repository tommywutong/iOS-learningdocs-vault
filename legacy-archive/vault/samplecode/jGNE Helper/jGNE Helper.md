---
title: jGNE Helper
apple_id: DTS10000188
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/jGNE_Helper/Introduction/Intro.html
archived_at: '2026-07-18T03:29:47.676174Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](jGNE%20Helper.c.md)

# jGNE Helper

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

This is "jGNE Helper", formerly a monthly posting to the Usenet newsgroup alt.sources.mac. It provides an example for INIT programmers interested in filtering events before they are handed to applications calling GetNextEvent (which is called by WaitNextEvent). The jGNE filter is the Apple-sanctioned method for filtering events. It is possible to patch event traps. It is sometimes even advisable. But since the jGNE filter is the sanctioned method, one ought to attempt to use it before patching traps. This code sample has a specific conflict with older versions of PopChar. Newer versions of PopChar have a fix which makes them compatible with this code. Users of older versions of PopChar should probably upgrade to the current version anyway -- this is a very old conflict. The conflict manifests itself by rendering a good portion of the screen "impervious" to clicks unless the option key is held down. This version of jGNE Helper was built with both Symantec THINK C 7 and Metrowerks CodeWarrior CW7 for 68K machines. It's entirely possible to write a native jGNEFilter. I've even done it before. However, it hasn't occurred to me how to fit a native filter into the context of this sample. For further info on the jGNE filter, consult your Technotes.

[Next](jGNE%20Helper.c.md)

