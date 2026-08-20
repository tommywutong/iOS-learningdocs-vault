---
title: QISA
apple_id: DTS10000714
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-05-15'
source_url: https://developer.apple.com/library/archive/samplecode/QISA/Introduction/Intro.html
archived_at: '2026-07-18T03:19:42.029428Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](MoreIsBetter%20Bits-MoreIsBetter-MIB-Libraries-MoreAppearance-MoreAppearance.cp.md)

# QISA

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-05-15 Demonstrates the basics of writing an Internet setup assistant for traditional Mac OS and Mac OS X. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon (both 9 and X) Mac OS 9 or higher (excluding Mac OS X 10.0.x) |

QISA, or the Q Internet Setup Assistant, is a sample that demonstrates the basics of writing an Internet Setup Assistant for Mac OS. The sample is a Carbon application that runs on both Mac OS 9 and Mac OS X. It uses platform-specific technologies to configure the network for the appropriate platform. On Mac OS 9, it uses the Network Setup library for this, and on Mac OS X it uses the System Configuration framework. Platform-specific code is compiled into distinct bundles, which are then loaded and called at runtime via CFBundle. QISA makes extensive use of the MoreIsBetter DTS sample code library. The Mac OS 9 platform support bundle uses the MoreNetworkSetup module as a high-level interface to the Network Setup library. The Mac OS X platform support bundle uses MoreSCF as a high-level interface to System Configuration framework, and MoreSecurity to execute that code in a privileged helper tool. Requirements: Mac OS 9 or higher (excluding Mac OS X 10.0.x) Keywords: Internet setup assistant, Network Setup, System Configuration framework, setuid root helper tool, bundles, Authorization Services

[Next](MoreIsBetter%20Bits-MoreIsBetter-MIB-Libraries-MoreAppearance-MoreAppearance.cp.md)

