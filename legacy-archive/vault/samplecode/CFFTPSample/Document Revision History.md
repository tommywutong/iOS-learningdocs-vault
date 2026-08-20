---
title: CFFTPSample
apple_id: DTS10003223
resource_type: Sample Code
platform: macOS
topic: Networking, Internet, & Web
technology: CoreFoundation
published: '2006-10-13'
source_url: https://developer.apple.com/library/archive/samplecode/CFFTPSample/History/History.html
archived_at: '2026-07-18T03:02:25.426523Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CFFTPSample](CFFTPSample.md)


[Previous](Read%20Me%20About%20CFFTPSample.txt.md)

# Document Revision History

This table describes the changes to _CFFTPSample_.

| __Date__ | __Notes__ |
| 2006-10-13 | Fixed a crash when CFFTPCreateParsedResourceListing returned a positive value but a NULL dictionary (r. 4533718). Follow CFNetwork best practice by only reading only one chunk of data per callback (r. 4515194). Terminate FTP upload in recommended fashion (by closing the stream rather than writing zero bytes). General tidy up. |
| 2006-03-31 | Corrected a production problem that dropped the project file and built binary. |

[Previous](Read%20Me%20About%20CFFTPSample.txt.md)

