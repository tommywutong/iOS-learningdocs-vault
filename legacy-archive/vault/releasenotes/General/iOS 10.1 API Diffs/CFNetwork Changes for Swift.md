---
title: iOS 10.1 API Diffs
apple_id: TP40017545
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS101APIDiffs/Swift/CFNetwork.html
archived_at: '2026-07-18T02:54:45.776516Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.1 API Diffs](iOS%2010.0%20to%20iOS%2010.1%20API%20Differences.md)


# CFNetwork Changes for Swift

### CFNetwork

Modified [CFNetServiceBrowserCreate(_: CFAllocator?, _: CFNetwork.CFNetServiceBrowserClientCallBack, _: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceBrowser>](https://developer.apple.com/documentation/cfnetwork/1426560-cfnetservicebrowsercreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceBrowserCreate(_ alloc: CFAllocator?, _ clientCB: CFNetwork.CFNetServiceBrowserClientCallBack, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceBrowser> ``` |
| To | ``` func CFNetServiceBrowserCreate(_ alloc: CFAllocator?, _ clientCB: @escaping CFNetwork.CFNetServiceBrowserClientCallBack, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceBrowser> ``` |

Modified [CFNetServiceMonitorCreate(_: CFAllocator?, _: CFNetService, _: CFNetwork.CFNetServiceMonitorClientCallBack, _: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceMonitor>](https://developer.apple.com/documentation/cfnetwork/1426665-cfnetservicemonitorcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceMonitorCreate(_ alloc: CFAllocator?, _ theService: CFNetService, _ clientCB: CFNetwork.CFNetServiceMonitorClientCallBack, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceMonitor> ``` |
| To | ``` func CFNetServiceMonitorCreate(_ alloc: CFAllocator?, _ theService: CFNetService, _ clientCB: @escaping CFNetwork.CFNetServiceMonitorClientCallBack, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceMonitor> ``` |

Modified [CFNetworkExecuteProxyAutoConfigurationScript(_: CFString, _: CFURL, _: CFNetwork.CFProxyAutoConfigurationResultCallback, _: UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource>](https://developer.apple.com/documentation/cfnetwork/1426362-cfnetworkexecuteproxyautoconfigu)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetworkExecuteProxyAutoConfigurationScript(_ proxyAutoConfigurationScript: CFString, _ targetURL: CFURL, _ cb: CFNetwork.CFProxyAutoConfigurationResultCallback, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource> ``` |
| To | ``` func CFNetworkExecuteProxyAutoConfigurationScript(_ proxyAutoConfigurationScript: CFString, _ targetURL: CFURL, _ cb: @escaping CFNetwork.CFProxyAutoConfigurationResultCallback, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource> ``` |

Modified [CFNetworkExecuteProxyAutoConfigurationURL(_: CFURL, _: CFURL, _: CFNetwork.CFProxyAutoConfigurationResultCallback, _: UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource>](https://developer.apple.com/documentation/cfnetwork/1426392-cfnetworkexecuteproxyautoconfigu)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetworkExecuteProxyAutoConfigurationURL(_ proxyAutoConfigURL: CFURL, _ targetURL: CFURL, _ cb: CFNetwork.CFProxyAutoConfigurationResultCallback, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource> ``` |
| To | ``` func CFNetworkExecuteProxyAutoConfigurationURL(_ proxyAutoConfigURL: CFURL, _ targetURL: CFURL, _ cb: @escaping CFNetwork.CFProxyAutoConfigurationResultCallback, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource> ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
