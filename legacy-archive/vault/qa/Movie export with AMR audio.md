---
title: Movie export with AMR audio
apple_id: DTS10003219
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2010-02-24'
source_url: https://developer.apple.com/library/archive/qa/qa1347/_index.html
archived_at: '2026-07-18T02:30:25.677237Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1347

# Movie export with AMR audio

## Q:  I'm trying to create movies containing AMR audio on my Windows PC using the QuickTime `ConvertMovieToFile` function. The resulting files always contain valid video, but no audio. No errors are being returned from this function. What am I doing wrong?

A: I'm trying to create movies containing AMR audio on my Windows PC using the QuickTime `ConvertMovieToFile` function. The resulting files always contain valid video, but no audio. No errors are being returned from this function. What am I doing wrong?

The AMR compressor that ships with QuickTime is only available to licensed applications via a special Software Development Kit (SDK) on Windows.

Therefore, you can't use any of the QuickTime movie exporter functions such as `ConvertMovieToFile` from your own application to encode audio to the AMR format without first obtaining a license.

Contact [VoiceAge](http://www.voiceage.com/amr.php) for AMR licensing information.

Once the AMR patent license is obtained, contact [Apple Software Licensing](https://developer.apple.com/softwarelicensing/index.html) for the AMR SDK license. When contacting Apple Software Licensing please indicate that you are interested in the AMR SDK license and include a full company name, address and contact email address.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-02-24 | Removed references to the AAC format since it no longer requires a license. |
| 2009-03-16 | Updated licensing requirements |
| 2007-04-13 | Updated contact URL for Via Licensing Corporation |
| 2006-01-25 | misc. changes |
| 2006-01-06 | fixed broken link |
| 2004-05-20 | minor wording changes |
| 2004-04-05 | New document that this Q&A discusses use of the QuickTime AMR audio compressor on Macintosh and Windows |

