---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/SecurityFoundation.html
archived_at: '2026-07-18T02:53:44.090864Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# SecurityFoundation Changes for Swift

### SecurityFoundation

Modified [SFAuthorization](https://developer.apple.com/documentation/securityfoundation/sfauthorization)

|  | Declaration |
| --- | --- |
| From | ``` class SFAuthorization : NSObject, NSCoding {     class func authorization() -> AnyObject!     func authorizationRef() -> AuthorizationRef     class func authorizationWithFlags(_ flags: AuthorizationFlags, rights rights: UnsafePointer<AuthorizationRights>, environment environment: UnsafePointer<AuthorizationEnvironment>) -> AnyObject!     init!(flags flags: AuthorizationFlags, rights rights: UnsafePointer<AuthorizationRights>, environment environment: UnsafePointer<AuthorizationEnvironment>)     init!()     func invalidateCredentials()     func obtainWithRight(_ rightName: AuthorizationString, flags flags: AuthorizationFlags, error error: NSErrorPointer) -> Bool     func obtainWithRights(_ rights: UnsafePointer<AuthorizationRights>, flags flags: AuthorizationFlags, environment environment: UnsafePointer<AuthorizationEnvironment>, authorizedRights authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>>, error error: NSErrorPointer) -> Bool } extension SFAuthorization {     func permitWithRights(_ rights: UnsafePointer<AuthorizationRights>, flags flags: AuthorizationFlags, environment environment: UnsafePointer<AuthorizationEnvironment>, authorizedRights authorizedRights: UnsafeMutablePointer<AuthorizationRights>) -> OSStatus     func permitWithRight(_ rightName: AuthorizationString, flags flags: AuthorizationFlags) -> OSStatus } ``` |
| To | ``` class SFAuthorization : NSObject, NSCoding {     class func authorization() -> AnyObject!     func authorizationRef() -> AuthorizationRef     class func authorizationWithFlags(_ flags: AuthorizationFlags, rights rights: UnsafePointer<AuthorizationRights>, environment environment: UnsafePointer<AuthorizationEnvironment>) -> AnyObject!     init!(flags flags: AuthorizationFlags, rights rights: UnsafePointer<AuthorizationRights>, environment environment: UnsafePointer<AuthorizationEnvironment>)     init!()     func invalidateCredentials()     func obtainWithRight(_ rightName: AuthorizationString, flags flags: AuthorizationFlags) throws     func obtainWithRights(_ rights: UnsafePointer<AuthorizationRights>, flags flags: AuthorizationFlags, environment environment: UnsafePointer<AuthorizationEnvironment>, authorizedRights authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>>) throws } extension SFAuthorization {     func permitWithRights(_ rights: UnsafePointer<AuthorizationRights>, flags flags: AuthorizationFlags, environment environment: UnsafePointer<AuthorizationEnvironment>, authorizedRights authorizedRights: UnsafeMutablePointer<AuthorizationRights>) -> OSStatus     func permitWithRight(_ rightName: AuthorizationString, flags flags: AuthorizationFlags) -> OSStatus } ``` |

Modified [SFAuthorization.obtainWithRight(_: AuthorizationString, flags: AuthorizationFlags) throws](https://developer.apple.com/documentation/securityfoundation/sfauthorization/1417652-obtainwithright)

|  | Declaration |
| --- | --- |
| From | ``` func obtainWithRight(_ rightName: AuthorizationString, flags flags: AuthorizationFlags, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func obtainWithRight(_ rightName: AuthorizationString, flags flags: AuthorizationFlags) throws ``` |

Modified [SFAuthorization.obtainWithRights(_: UnsafePointer<AuthorizationRights>, flags: AuthorizationFlags, environment: UnsafePointer<AuthorizationEnvironment>, authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>>) throws](https://developer.apple.com/documentation/securityfoundation/sfauthorization/1417648-obtainwithrights)

|  | Declaration |
| --- | --- |
| From | ``` func obtainWithRights(_ rights: UnsafePointer<AuthorizationRights>, flags flags: AuthorizationFlags, environment environment: UnsafePointer<AuthorizationEnvironment>, authorizedRights authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>>, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func obtainWithRights(_ rights: UnsafePointer<AuthorizationRights>, flags flags: AuthorizationFlags, environment environment: UnsafePointer<AuthorizationEnvironment>, authorizedRights authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>>) throws ``` |

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
