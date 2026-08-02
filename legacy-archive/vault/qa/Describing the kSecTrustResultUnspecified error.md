---
title: Describing the kSecTrustResultUnspecified error.
apple_id: DTS10004208
resource_type: QA
platform: macOS
topic: Security
technology: Security
published: '2007-02-05'
source_url: https://developer.apple.com/library/archive/qa/qa1360/_index.html
archived_at: '2026-07-18T02:30:26.168788Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1360

# Describing the kSecTrustResultUnspecified error.

## Q:  I am receiving a kSecTrustResultUnspecified (4) error while checking the validity of certificates that I know to be valid, what does this mean?

A: I am receiving a kSecTrustResultUnspecified (4) error while checking the validity of certificates that I know to be valid, what does this mean?

The semantics behind receiving a kSecTrustResultUnspecified (`4`) error from Security APIs is that the certificate is indeed valid. However, the user has not explicitly set the trust settings for the certificate via Keychain Access. If the user then sets an explicit trust setting, e.g. "always trust" or "never trust" in the UI, then you should receive kSecTrustResultProceed, kSecTrustResultConfirm or kSecTrustResultDeny instead of kSecTrustResultUnspecified when making Security API calls to validate the certificate.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-02-05 | New document that explaining the semantics behind the kSecTrustResultUnspecified error returned by the Security APIs. |

