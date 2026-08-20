---
title: Concurrent NSOperations Failing On iOS 4
apple_id: DTS40010262
resource_type: QA
platform: iOS
topic: null
technology: Foundation
published: '2010-08-23'
source_url: https://developer.apple.com/library/archive/qa/qa1712/_index.html
archived_at: '2026-07-18T02:34:22.287198Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1712

# Concurrent NSOperations Failing On iOS 4

## Q:  I have a concurrent NSOperation that uses NSURLConnection asynchronously. Why doesn't it work on iOS 4?

A: I have a concurrent NSOperation that uses NSURLConnection asynchronously. Why doesn't it work on iOS 4?

In iOS 4 NSOperationQueue was updated to use Grand Central Dispatch (GCD). One consequence of this change is that the `-start` method of your NSOperation is now always called on a secondary thread. If your `-start` method schedules run loop callbacks on the current run loop (for example, it creates an NSURLConnection using `+[NSURLConnection connectionWithRequest:delegate:]`), it's likely that those callbacks will never be called.

This does not represent a change in the semantics of NSOperation. It has always been the case that an NSOperation's `-start` method must be prepared to run on any thread. However, on iOS 3 the `-start` method was commonly called on the thread that added the operation to the queue, which meant that bugs like this went unnoticed.

Creating a concurrent, run loop based NSOperation is quite tricky. For a concrete example of how to do this, you should look at the [Sample Code 'LinkedImageFetcher'](https://developer.apple.com/samplecode/LinkedImageFetcher/index.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-08-23 | New document that describes a common problem with concurrent, run loop based, NSOperations (such as those using NSURLConnection) on iOS 4. |

