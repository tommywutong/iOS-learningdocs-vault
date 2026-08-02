---
title: Why am I getting a 'Failed to start remote debugserver for <name>.app on <device>'
  error?
apple_id: DTS40008095
resource_type: QA
platform: iOS
topic: Xcode
technology: null
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/qa/qa1616/_index.html
archived_at: '2026-07-18T02:32:46.987980Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1616

# Why am I getting a 'Failed to start remote debugserver for <name>.app on <device>' error?

## Q:  Why am I getting a 'Failed to start remote debugserver for <name>.app on <device>' error? How do I fix it?

A: Why am I getting a 'Failed to start remote debugserver for <name>.app on <device>' error? How do I fix it?

You probably have a mismatch between the iPhone OS on your device and your SDK. Check that the software version of your device (Settings > General > About) matches the version of your SDK. For instance, you may have upgraded your device to iPhone OS 2.1, but you are still using iPhone SDK for iPhone OS 2.0 for development. So, updating the SDK to the latest version will resolve this issue.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-03-09 | Moved to Retired Documents Library. |
| 2008-11-20 | First Version |

