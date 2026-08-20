---
title: FairPlay Streaming Server SDK Development Credentials
apple_id: DTS40017673
resource_type: QA
platform: tvOS|Safari|iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-08-31'
source_url: https://developer.apple.com/library/archive/qa/qa1967/_index.html
archived_at: '2026-07-18T02:38:00.952473Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1967

# FairPlay Streaming Server SDK Development Credentials

## Q:  Can the development credentials in the FairPlay Streaming Server SDK be used for streaming protected content using FPS secure key delivery?

A: The development credentials that are included as part of the FairPlay Streaming Server SDK are not valid to use for playback of protected content.

The purpose of the development credentials is to verify the implementation of a Key Security Module (KSM) implementation. Developers writing a KSM must use these credentials with the hardcoded Derived Application Secret key (DASk) to test their KSM implementation using the test vectors included in the FairPlay Streaming Server SDK. Using both the development credentials and Server Playback Context (SPC) test vectors, it is possible to test most of the KSM algorithm. The only step of the KSM algorithm not covered is the final step of the KSM securely providing the content keys to the FPS client application for playback.

To test this final step, developers must use the `verify_ckc` tool included in the FairPlay Steaming Server SDK with the Content Key Context (CKC) their KSM generated and the SPC test vector used to generate that CKC. This is discussed in the FairPlay Streaming Programming Guide which is available as part of the FairPlay Streaming Server SDK.

If your FPS aware client application tries to use the development credentials a Server Playback Context (SPC) message is not generated.

After verifying your KSM implementation using the documentation and tools found in the FairPlay Streaming Server SDK, you can request a Deployment Package from Apple which will include the credentials needed to do end to end playback of FPS protected content.

The latest version of the FairPlay Streaming Server SDK and information about requesting the Production Deployment package can be found here:

- [FairPlay Streaming - Apple Developer](https://developer.apple.com/streaming/fps/)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-08-31 | New document that new document that clarifies what the development credentials in the FairPlay Streaming Server SDK are meant to be used for. |

