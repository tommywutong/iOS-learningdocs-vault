---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/ServiceManagement.html
archived_at: '2026-07-18T02:53:44.121086Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# ServiceManagement Changes for Swift

### ServiceManagement

Modified [SMJobBless(_: CFString!, _: CFString, _: AuthorizationRef, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> UInt8](https://developer.apple.com/documentation/servicemanagement/1431078-smjobbless)

|  | Declaration |
| --- | --- |
| From | ``` func SMJobBless(_ domain: CFString!, _ executableLabel: CFString, _ auth: AuthorizationRef, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` |
| To | ``` func SMJobBless(_ domain: CFString!, _ executableLabel: CFString, _ auth: AuthorizationRef, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>) -> UInt8 ``` |

Modified [SMJobRemove(_: CFString!, _: CFString, _: AuthorizationRef, _: UInt8, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> UInt8](https://developer.apple.com/documentation/servicemanagement/1431094-smjobremove)

|  | Declaration |
| --- | --- |
| From | ``` func SMJobRemove(_ domain: CFString!, _ jobLabel: CFString, _ auth: AuthorizationRef, _ wait: Boolean, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` |
| To | ``` func SMJobRemove(_ domain: CFString!, _ jobLabel: CFString, _ auth: AuthorizationRef, _ wait: UInt8, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>) -> UInt8 ``` |

Modified [SMJobSubmit(_: CFString!, _: CFDictionary, _: AuthorizationRef, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> UInt8](https://developer.apple.com/documentation/servicemanagement/1431084-smjobsubmit)

|  | Declaration |
| --- | --- |
| From | ``` func SMJobSubmit(_ domain: CFString!, _ job: CFDictionary, _ auth: AuthorizationRef, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` |
| To | ``` func SMJobSubmit(_ domain: CFString!, _ job: CFDictionary, _ auth: AuthorizationRef, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>) -> UInt8 ``` |

Modified [SMLoginItemSetEnabled(_: CFString, _: UInt8) -> UInt8](https://developer.apple.com/documentation/servicemanagement/1501557-smloginitemsetenabled)

|  | Declaration |
| --- | --- |
| From | ``` func SMLoginItemSetEnabled(_ identifier: CFString, _ enabled: Boolean) -> Boolean ``` |
| To | ``` func SMLoginItemSetEnabled(_ identifier: CFString, _ enabled: UInt8) -> UInt8 ``` |

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
