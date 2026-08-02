---
title: Validating Your Version of Xcode
apple_id: DTS40016593
resource_type: QA
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2015-09-22'
source_url: https://developer.apple.com/library/archive/qa/qa1900/_index.html
archived_at: '2026-07-18T02:35:33.310445Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1900

# Validating Your Version of Xcode

## Q:  How do I validate my version of Xcode?

A: Applications that are built with a counterfeit version of Xcode have the potential to cause harm to customers. You should always [Download Xcode](https://developer.apple.com/xcode/download/) directly from the Mac App Store, or from the Apple Developer website, and leave Gatekeeper enabled on all your systems to protect against tampered software.

When you download Xcode from the Mac App Store, OS X automatically checks the code signature for Xcode and validates that it is code signed by Apple. When you download Xcode from the Apple Developer website, the code signature is also automatically checked and validated by default as long as you have not disabled Gatekeeper.

Whether you downloaded Xcode from Apple or received Xcode from another source, such as a USB or Thunderbolt disk, or over a local network, you can easily verify the integrity of your copy of Xcode.

To verify the identity of your copy of Xcode run the following command in Terminal on a system with Gatekeeper enabled:

`spctl --assess --verbose /Applications/Xcode.app`

where /Applications/ is the directory where Xcode is installed. This tool performs the same checks that Gatekeeper uses to validate the code signatures of applications.

The tool should return the following result for a version of Xcode downloaded from the Mac App Store:

`/Applications/Xcode.app: accepted
 source=Mac App Store`

and for a version downloaded from the Apple Developer web site, the result should read either

`/Applications/Xcode.app: accepted
source=Apple`

or

`/Applications/Xcode.app: accepted
source=Apple System`

Any result other than ‘accepted’ or any source other than ‘Mac App Store’, ‘Apple System’ or ‘Apple’ indicates that the application signature is not valid for Xcode. You should download a clean copy of Xcode and recompile your apps before submitting them for review.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-09-22 | New document that shows how to easily verify the integrity of your copy of Xcode. |

