---
title: Sending SMS Programmatically
apple_id: DTS40017631
resource_type: QA
platform: iOS
topic: null
technology: MessageUI
published: '2017-04-14'
source_url: https://developer.apple.com/library/archive/qa/qa1944/_index.html
archived_at: '2026-07-18T02:37:25.129405Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1944

# Sending SMS Programmatically

## Q:  Is it possible to send an SMS message programmatically, without user interaction?

A: No. You can use the [MessageUI framework](https://developer.apple.com/reference/messageui) to send a message, but that requires explicit confirmation from the user. There’s no way to send a message without that confirmation. This is not an accidental ommission but a deliberate design decision.

Depending on your specific requirements you may be able to achieve your goal by setting up your own web service for sending SMS messages. Your app could then use TCP/IP networking to ask the web service to send an SMS message on its behalf.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-04-14 | New document that discusses the inability to send SMS messages without user interaction. |

