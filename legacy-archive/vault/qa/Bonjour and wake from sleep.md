---
title: Bonjour and wake from sleep
apple_id: DTS10002327
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2003-09-18'
source_url: https://developer.apple.com/library/archive/qa/qa1290/_index.html
archived_at: '2026-07-18T02:30:21.243346Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1290

# Bonjour and wake from sleep

## Q:  Do I need to do anything special in regards to my Bonjour registrations and browsing as a result of system sleep?

A: Do I need to do anything special in regards to my Bonjour registrations and browsing as a result of system sleep?

No. mDNSResponder handles system sleep on behalf of the client so nothing special needs to happen. Simply continue to register and browse through the sleep/wake process. In fact, if you were to manually de-register on sleep and re-register on wake, it would be inefficient because more packets would end up being sent on the wire. mDNSResponder will handle the de-register and re-register on your behalf and as a result, it will do it more efficiently by combining all records into one packet.

After the computer wakes up, your application will also be notified if any previously discovered services went away while the machine was asleep, so you should continue browsing through the sleep/wake process as well.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2003-09-18 | New document that explains why applications that use Bonjour should stay registered and continue browsing on sleep. |

