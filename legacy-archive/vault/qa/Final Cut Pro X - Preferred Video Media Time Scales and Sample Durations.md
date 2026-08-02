---
title: Final Cut Pro X - Preferred Video Media Time Scales and Sample Durations
apple_id: DTS10003804
resource_type: QA
platform: macOS
topic: Apple Applications
technology: null
published: '2014-08-26'
source_url: https://developer.apple.com/library/archive/qa/qa1447/_index.html
archived_at: '2026-07-18T02:30:48.928100Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1447

# Final Cut Pro X - Preferred Video Media Time Scales and Sample Durations

## Q:  When creating video for import into Final Cut Pro X, are there specific time scales and sample durations that should be used?

A: Yes, there are a number of preferred values.

As mentioned in the "QuickTime Image Rates and Video" section of [Uncompressed Y´CbCr Video in QuickTime Files](https://developer.apple.com/library/mac/technotes/tn2162/_index.html), a media has a time scale and each sample in a media has a duration. Together the duration and time scale specify the frame rate of the video.

When creating video media for Final Cut Pro X, the time scales and sample durations listed in Table 1 are the preferred values and should be used to accurately represent the frame rate of your content.

__Table 1__  Preferred Final Cut Pro X Media Time Scales and Sample Durations.

| Frames Per Second | Time Scale | Sample Duration |  | Time Scale | Sample Duration |
| 59.94 | 60000 | 1001 |  |  |  |
| 50 | 5000 | 100 | or | 50 | 1 |
| 30 | 3000 | 100 | or | 30 | 1 |
| 29.97 | 30000 | 1001 |  |  |  |
| 25 | 2500 | 100 | or | 25 | 1 |
| 24 | 2400 | 100 | or | 24 | 1 |
| 23.976 | 24000 | 1001 |  |  |  |

30000/1001 is a more accurate representation of 29.97 fps and doesn't suffer the frame time deviation as discussed in 'Uncompressed Y´CbCr Video in QuickTime Files'. However, this does make a difference in duration. A media time scale of 30000 and media sample durations of 1001, along with a movie time scale of 30000, currently provides 19.9 hours of time while 2997/100 provides 8.2 days of time.

QuickTime Image Rates and Video - [Uncompressed Y´CbCr Video in QuickTime Files](https://developer.apple.com/library/mac/technotes/tn2162/_index.html)

Table 2 contains a list of legacy Media Time Scales and Sample Durations values for reference purposes.

__Table 2__  Legacy FCP Media Time Scales and Sample Durations.

| Frames Per Second | Time Scale | Sample Duration |  | Time Scale | Sample Duration |
| 60 | 6000 | 100 | or | 60 | 1 |
| 59.94 | 5994 | 100 |  |  |  |
| 50 | 5000 | 100 | or | 50 | 1 |
| 30 | 3000 | 100 | or | 30 | 1 |
| 29.97 | 30000 | 1001 | or | 2997 | 100 |
| 25 | 2500 | 100 | or | 25 | 1 |
| 24 | 2400 | 100 | or | 24 | 1 |
| 23.98 | 23976 | 1000 |  |  |  |

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-08-26 | Updated table for FCP X |
| 2005-10-24 | New document that lists the preferred time scales/sample durations for media created for use with FCP. |

