---
title: SMJobBless
apple_id: DTS40010071
resource_type: Sample Code
platform: macOS
topic: Security
technology: ServiceManagement
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/SMJobBless/Introduction/Intro.html
archived_at: '2026-07-18T03:22:42.406882Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# SMJobBless

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.5, 2013-09-17 Set SKIP_INSTALL on the helper tool target so that the app archives properly (r. 14843533). [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytambxgewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 4.6 or later |
| __Runtime Requirements:__ | OS X v10.6 or later |

SMJobBless demonstrates how to securely install a helper tool that performs a privileged operation and how to associate the tool with an application that invokes it.

SMJobBless uses ServiceManagement.framework that was introduced in Mac OS X v10.6 Snow Leopard.

As of Snow Leopard, this is the preferred method of managing privilege escalation on Mac OS X and should be used instead of earlier approaches such as BetterAuthorizationSample or directly calling AuthorizationExecuteWithPrivileges.

[Next](ReadMe.txt.md)

