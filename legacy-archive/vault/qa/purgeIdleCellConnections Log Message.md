---
title: purgeIdleCellConnections Log Message
apple_id: DTS40012992
resource_type: QA
platform: iOS
topic: Networking, Internet, & Web
technology: Foundation
published: '2013-01-02'
source_url: https://developer.apple.com/library/archive/qa/qa1774/_index.html
archived_at: '2026-07-18T02:34:41.368235Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1774

# purgeIdleCellConnections Log Message

## Q:  While testing my app on iOS 6.0 I noticed the log message `purgeIdleCellConnections: found one to purge`. What does that mean?

A: This is a debug message that's been erroneously left enabled
(r. 12431060)
. It happens during the normal operation of any app that uses NSURLConnection and does not, in itself, indicate a failure. The rest of this document explains what it actually means.

Internally NSURLConnection maintains an HTTP 1.1 persistent connection cache. Each cache entry represents a set of persistent connections to a host. When a new request comes in, it is queued on an entry in the cache. This may be an existing entry or it may be a new entry, and it may also generate a new HTTP connection within that entry, depending on various complex factors (the protection space, the authentication status when dealing with authenticated connections like NTLM, pipelining, various cache limits, and so on). When a connection associated with a cache entry finishes running all of its requests, it looks for more work on the cache entry's queue; if it doesn't find any, it goes idle. If a connection is idle for too long, it is purged, which closes the underlying TCP connection.

This cache implementation has changed in iOS 6. Prior to iOS 6 there was a single mechanism for purging idle cache entries, with radically different timeouts for OS X and iOS (30 seconds versus 6 seconds, and the iOS value could be as low as 3 seconds on older versions of iOS). In iOS 6 there are now two mechanisms for purging idle cache entries, one that applies to connections running over the WWAN and one that applies to all other connections. The WWAN timeout has dropped back to its old value (3 seconds) while the all-other-connections timeout has been bumped up to the OS X default (30 seconds).

The log message you're seeing is generated when a WWAN connection is purged. This log message didn't exist in iOS 5.x, which explains why you've just started seeing it. However the basic mechanism has been present, in one form or another, on all versions of iOS.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-01-02 | New document that describes the meaning of the purgeIdleCellConnections log message. |

