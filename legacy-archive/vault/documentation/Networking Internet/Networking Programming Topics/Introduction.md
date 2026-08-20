---
title: Networking Programming Topics
apple_id: TP40012488
resource_type: Guide
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/NetworkingTopics/Introduction/Introduction.html
archived_at: '2026-07-15T08:18:51.184249Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Using%20Sockets%20and%20Socket%20Streams.md)

# Introduction

This document is a collection of highly specialized, task-based articles related to specific areas of networking. As with other programming topics documents in this developer library, this document assumes that you already have a deep familiarity with networking concepts.

This document includes the following articles:

- [Using Sockets and Socket Streams](Using%20Sockets%20and%20Socket%20Streams.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpinedomznknltc)—Describes how to use sockets and streams for low-level networking, from the POSIX layer up through the Foundation layer. This article explains how to write both client and server code using current best practices.
- [Resolving DNS Hostnames](Resolving%20DNS%20Hostnames.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdknbtfvjvomi)—Explains how to resolve DNS hostnames in ways that avoid some of the common pitfalls associated with doing so.
- [Overriding TLS Chain Validation Correctly](Overriding%20TLS%20Chain%20Validation%20Correctly.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdknbufvjvomi)—Tells how to safely alter the behavior of Transport Layer Security (TLS) chain validation without exposing your software to serious security risks. This article covers both TCP streams (using the CFStream or NSStream API) and URL requests (using the NSURLConnection API).

Each article is intended to be read by developers who need to write code that performs the specified task.

This document assumes you have already read or otherwise understand the subjects described in the following documents:

- _[Networking Overview](../../Networking%20Internet%20Web/Networking%20Overview/About%20Networking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrq)_—Provides a basic understanding of how networking software works, and how to avoid common mistakes.
- _[Networking Concepts](../Networking%20Concepts/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdiobx)_—Provides a basic explanation of socket-based networking at a conceptual level.

[Next](Using%20Sockets%20and%20Socket%20Streams.md)

