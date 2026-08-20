---
title: Weak Linking To Spotlight
apple_id: DTS10003700
resource_type: QA
platform: macOS
topic: Data Management
technology: CoreServices
published: '2005-06-03'
source_url: https://developer.apple.com/library/archive/qa/qa1422/_index.html
archived_at: '2026-07-18T02:30:39.700470Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1422

# Weak Linking To Spotlight

## Q:  I'm writing a program that uses the Spotlight APIs (from the Metadata framework) if they are available. I set `MACOSX_DEPLOYMENT_TARGET` to 10.3 and then use weak linking to check for the availability of these APIs. However, when I run my program on Mac OS X 10.3.x, it won't launch, complaining that the `MDQuerySetSearchScope` symbol is not available. What gives?

A: Many of the declarations in the Metadata framework are suffixed by the `MD_AVAIL` macro, which declares the symbol to be imported weak if you're targetting a pre-10.4 system. However, due to a bug (r. 4097766), some of the declarations are missing that macro.

You can workaround this problem by simply editing the headers in the Metadata framework to include this macro. To make this even easier, we've supplied some fixed headers at the end of this document. You can install these by copying them to `/System/Library/Frameworks/CoreServices.framework/Frameworks/Metadata.framework/Headers/` (or `/Developer/SDKs/MacOSX10.4.0.sdk/System/Library/Frameworks/CoreServices.framework/Frameworks/Metadata.framework/Headers/` if you're using Xcode's SDK support).

Apple will provide a proper solution in the next release of the Metadata framework headers.

For more information about weak linking and binary compatibility, see [Technical Note TN2064, 'Ensuring Backwards Binary Compatibility - Weak Linking and Availability Macros on Mac OS X'](https://developer.apple.com/technotes/tn2002/tn2064.html).

- Fixed Metadata framework headers ("qa1422_FixedHeaders.zip", 20.2K)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-06-03 | New document that describes a problem with weak linking to Spotlight (the Metadata framework), and its solution. |

