---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/SecurityFoundation.html
archived_at: '2026-07-18T02:52:40.631238Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# SecurityFoundation Changes

## SecurityFoundation

Modified SFAuthorization.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified SFAuthorization.authorizationRef() -> AuthorizationRef

|  | Declaration |
| --- | --- |
| From | ``` func authorizationRef() -> Unmanaged<Authorization>! ``` |
| To | ``` func authorizationRef() -> AuthorizationRef ``` |

Modified SFAuthorization.authorizationWithFlags(AuthorizationFlags, rights: UnsafePointer<AuthorizationRights>, environment: UnsafePointer<AuthorizationEnvironment>) -> AnyObject! [class]

|  | Declaration |
| --- | --- |
| From | ``` class func authorizationWithFlags(_ flags: AuthorizationFlags, rights rights: ConstUnsafePointer<AuthorizationRights>, environment environment: ConstUnsafePointer<AuthorizationEnvironment>) -> AnyObject! ``` |
| To | ``` class func authorizationWithFlags(_ flags: AuthorizationFlags, rights rights: UnsafePointer<AuthorizationRights>, environment environment: UnsafePointer<AuthorizationEnvironment>) -> AnyObject! ``` |

Modified SFAuthorization.init(flags: AuthorizationFlags, rights: UnsafePointer<AuthorizationRights>, environment: UnsafePointer<AuthorizationEnvironment>)

|  | Declaration |
| --- | --- |
| From | ``` init(flags flags: AuthorizationFlags, rights rights: ConstUnsafePointer<AuthorizationRights>, environment environment: ConstUnsafePointer<AuthorizationEnvironment>) ``` |
| To | ``` init!(flags flags: AuthorizationFlags, rights rights: UnsafePointer<AuthorizationRights>, environment environment: UnsafePointer<AuthorizationEnvironment>) ``` |

Modified SFAuthorization.obtainWithRights(UnsafePointer<AuthorizationRights>, flags: AuthorizationFlags, environment: UnsafePointer<AuthorizationEnvironment>, authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>>, error: NSErrorPointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func obtainWithRights(_ rights: ConstUnsafePointer<AuthorizationRights>, flags flags: AuthorizationFlags, environment environment: ConstUnsafePointer<AuthorizationEnvironment>, authorizedRights authorizedRights: UnsafePointer<UnsafePointer<AuthorizationRights>>, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func obtainWithRights(_ rights: UnsafePointer<AuthorizationRights>, flags flags: AuthorizationFlags, environment environment: UnsafePointer<AuthorizationEnvironment>, authorizedRights authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>>, error error: NSErrorPointer) -> Bool ``` |

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
