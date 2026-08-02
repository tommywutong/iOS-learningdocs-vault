---
title: Bonjour TXT record rate limiting in Panther
apple_id: DTS10002337
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2003-10-23'
source_url: https://developer.apple.com/library/archive/qa/qa1293/_index.html
archived_at: '2026-07-18T02:30:21.298774Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1293

# Bonjour TXT record rate limiting in Panther

## Q:  I have an application that updates the Bonjour TXT record once a second, and now my application doesn't work in Panther. Why is that?

A: Starting in Mac OS X 10.3, mDNSResponder rate limits the number of TXT record updates in order to prevent abuses that harm the network. Although the exact allowable rate is dependent on how often you've updated the TXT record in the past, you can rely on being able to update at a steady rate of once per minute without any problems. The exact rules for rate limiting are as follows.

- The TXT record starts off with ten __Update Credits__.
- Every TXT record update consumes one Update Credit.
- Update Credits are replenished at a rate of one per minute, up to a maximum of ten.
- As the number of Update Credits declines, the number of announcements of the updated TXT record is scaled back.
- When fewer than five Update Credits remain, the first announcement is also delayed by an increasing amount.

This means that you are allowed to do a few quick updates in rapid succession, but if your sustained long-term average exceeds one update per minute, the update rate will be throttled back to protect the network.

If you have an application that needs to disseminate new information to all peers on the local network more frequently than once per minute, then Bonjour is probably not the right protocol for the job. You should contact [IANA](http://www.iana.org/) to get your own IP multicast address assigned so that your protocol traffic can run on its own multicast address.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-09-18 | Explains how mDNSResponder implements TXT record rate limiting in Panther. |
| 2003-10-23 | New document that explains how mDNSResponder implements TXT record rate limiting in Panther. |

