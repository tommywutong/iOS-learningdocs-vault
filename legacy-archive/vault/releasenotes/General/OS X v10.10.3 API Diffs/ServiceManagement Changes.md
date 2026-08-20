---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/ServiceManagement.html
archived_at: '2026-07-18T02:52:40.664191Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# ServiceManagement Changes

## ServiceManagement

Modified SMCopyAllJobDictionaries(CFString!) -> Unmanaged<CFArray>!

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.6 | OS X 10.10 |

Modified SMJobBless(CFString!, CFString, AuthorizationRef, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SMJobBless(_ domain: CFString!, _ executableLabel: CFString!, _ auth: Authorization!, _ outError: UnsafePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.10 |
| To | ``` func SMJobBless(_ domain: CFString!, _ executableLabel: CFString, _ auth: AuthorizationRef, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.6 |

Modified SMJobCopyDictionary(CFString!, CFString) -> Unmanaged<CFDictionary>!

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func SMJobCopyDictionary(_ domain: CFString!, _ jobLabel: CFString!) -> Unmanaged<CFDictionary>! ``` | OS X 10.10 | -- |
| To | ``` func SMJobCopyDictionary(_ domain: CFString!, _ jobLabel: CFString) -> Unmanaged<CFDictionary>! ``` | OS X 10.6 | OS X 10.10 |

Modified SMJobRemove(CFString!, CFString, AuthorizationRef, Boolean, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func SMJobRemove(_ domain: CFString!, _ jobLabel: CFString!, _ auth: Authorization!, _ wait: Boolean, _ outError: UnsafePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.10 | -- |
| To | ``` func SMJobRemove(_ domain: CFString!, _ jobLabel: CFString, _ auth: AuthorizationRef, _ wait: Boolean, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.6 | OS X 10.10 |

Modified SMJobSubmit(CFString!, CFDictionary, AuthorizationRef, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func SMJobSubmit(_ domain: CFString!, _ job: CFDictionary!, _ auth: Authorization!, _ outError: UnsafePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.10 | -- |
| To | ``` func SMJobSubmit(_ domain: CFString!, _ job: CFDictionary, _ auth: AuthorizationRef, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.6 | OS X 10.10 |

Modified SMLoginItemSetEnabled(CFString, Boolean) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SMLoginItemSetEnabled(_ identifier: CFString!, _ enabled: Boolean) -> Boolean ``` | OS X 10.10 |
| To | ``` func SMLoginItemSetEnabled(_ identifier: CFString, _ enabled: Boolean) -> Boolean ``` | OS X 10.6 |

Modified kSMDomainSystemLaunchd

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kSMDomainUserLaunchd

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kSMErrorDomainFramework

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.6 | OS X 10.10 |

Modified kSMErrorDomainIPC

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.6 | OS X 10.10 |

Modified kSMErrorDomainLaunchd

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.6 | OS X 10.10 |

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
