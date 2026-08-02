---
title: Security Framework Error Codes
apple_id: DTS10004158
resource_type: QA
platform: macOS
topic: Security
technology: Security
published: '2006-11-16'
source_url: https://developer.apple.com/library/archive/qa/qa1499/_index.html
archived_at: '2026-07-18T02:31:37.991600Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1499

# Security Framework Error Codes

## Q:  When calling various Security Framework routines I have noticed return values that are not explicitly documented by the Security API. What do these error values mean?

A: When calling various Security Framework routines I have noticed return values that are not explicitly documented by the Security API. What do these error values mean?

The Security framework can return an error from three distinct categories:

- An `OSStatus` error, e.g., `errSecNoSuchKeychain` (`-25294`).
- A UNIX errno-style error code + `100000`, e.g., `EINVAL` (`22`) + `100000`.
- An error from Common Security Services Manager (CSSM), one of the technologies that underlies the Security framework, e.g., `CSSM_ADDIN_AUTHENTICATE_FAILED` (`0x8001011c`).

General `OSStatus`-style error codes can be found in `MacErrors.h`. Security related `OSStatus`-style error codes are defined in various headers within the Security framework: `SecBase.h`, `AuthSession.h`, `SecureTransport.h`, and `Authorization.h`.

All errno-style error codes are listed in `/usr/include/sys/errno.h`.

CSSM errors are listed in `cssmerr.h`. In addition, you can get a human readable form of CSSM errors using `cssmPerror`, provided by the Security framework, in order to translate a received CSSM error value into its canonical name. Below is an example call within a `gdb` session:


```
(gdb) call (void)cssmPerror(0, 0x8001011c) error: CSSM_ADDIN_AUTHENTICATE_FAILED (gdb) call (void)cssmPerror(0, 2147549468) error: CSSM_ADDIN_AUTHENTICATE_FAILED
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-11-16 | New document that explains how to interpret errors returned by the Security Framework with an overview of Security error handling. |

