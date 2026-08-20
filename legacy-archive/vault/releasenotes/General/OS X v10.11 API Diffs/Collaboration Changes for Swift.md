---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/Collaboration.html
archived_at: '2026-07-18T02:53:23.372120Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# Collaboration Changes for Swift

### Collaboration

Removed CBGroupIdentity.members() -> [AnyObject]!Removed CBGroupIdentity.posixGID() -> gid_tRemoved CBIdentity.aliases() -> [AnyObject]!Removed CBIdentity.authority() -> CBIdentityAuthority!Removed CBIdentity.CSIdentity() -> Unmanaged<CSIdentity>!Removed CBIdentity.emailAddress() -> String!Removed CBIdentity.fullName() -> String!Removed CBIdentity.image() -> NSImage!Removed CBIdentity.init(CSIdentity: CSIdentity!) -> CBIdentityRemoved [CBIdentity.isHidden() -> Bool](https://developer.apple.com/documentation/collaboration/cbidentity/1805296-ishidden)Removed CBIdentity.persistentReference() -> NSData!Removed CBIdentity.posixName() -> String!Removed CBIdentity.UUIDString() -> String!Removed CBIdentityAuthority.CSIdentityAuthority() -> Unmanaged<CSIdentityAuthority>!Removed CBIdentityAuthority.init(CSIdentityAuthority: CSIdentityAuthority!) -> CBIdentityAuthorityRemoved CBIdentityAuthority.localizedName() -> String!Removed CBIdentityPicker.allowsMultipleSelection() -> BoolRemoved CBIdentityPicker.identities() -> [AnyObject]!Removed CBIdentityPicker.setAllowsMultipleSelection(_: Bool)Removed CBIdentityPicker.setTitle(_: String!)Removed CBIdentityPicker.title() -> String!Removed CBUserIdentity.certificate() -> Unmanaged<SecCertificate>!Removed [CBUserIdentity.isEnabled() -> Bool](https://developer.apple.com/documentation/collaboration/cbuseridentity/1805246-isenabled)Removed CBUserIdentity.posixUID() -> uid_tAdded [CBGroupIdentity.memberIdentities](https://developer.apple.com/documentation/collaboration/cbgroupidentity/1423890-memberidentities)Added [CBGroupIdentity.posixGID](https://developer.apple.com/documentation/collaboration/cbgroupidentity/1423857-posixgid)Added [CBIdentity.aliases](https://developer.apple.com/documentation/collaboration/cbidentity/1423871-aliases)Added [CBIdentity.authority](https://developer.apple.com/documentation/collaboration/cbidentity/1423859-authority)Added [CBIdentity.emailAddress](https://developer.apple.com/documentation/collaboration/cbidentity/1423923-emailaddress)Added [CBIdentity.fullName](https://developer.apple.com/documentation/collaboration/cbidentity/1423863-fullname)Added [CBIdentity.hidden](https://developer.apple.com/documentation/collaboration/cbidentity/1423883-ishidden)Added [CBIdentity.image](https://developer.apple.com/documentation/collaboration/cbidentity/1423873-image)Added [CBIdentity.init(uniqueIdentifier: NSUUID, authority: CBIdentityAuthority)](https://developer.apple.com/documentation/collaboration/cbidentity/1423900-init)Added [CBIdentity.persistentReference](https://developer.apple.com/documentation/collaboration/cbidentity/1423911-persistentreference)Added [CBIdentity.posixName](https://developer.apple.com/documentation/collaboration/cbidentity/1423913-posixname)Added [CBIdentity.uniqueIdentifier](https://developer.apple.com/documentation/collaboration/cbidentity/1423929-uniqueidentifier)Added [CBIdentity.UUIDString](https://developer.apple.com/documentation/collaboration/cbidentity/1423879-uuidstring)Added [CBIdentityAuthority.localizedName](https://developer.apple.com/documentation/collaboration/cbidentityauthority/1423875-localizedname)Added [CBIdentityPicker.allowsMultipleSelection](https://developer.apple.com/documentation/collaboration/cbidentitypicker/1423921-allowsmultipleselection)Added [CBIdentityPicker.identities](https://developer.apple.com/documentation/collaboration/cbidentitypicker/1423877-identities)Added [CBIdentityPicker.runModalForWindow(_: NSWindow, completionHandler: ((NSModalResponse) -> Void)?)](https://developer.apple.com/documentation/collaboration/cbidentitypicker/1423915-runmodalforwindow)Added [CBIdentityPicker.title](https://developer.apple.com/documentation/collaboration/cbidentitypicker/1423919-title)Added [CBUserIdentity.certificate](https://developer.apple.com/documentation/collaboration/cbuseridentity/1423917-certificate)Added [CBUserIdentity.enabled](https://developer.apple.com/documentation/collaboration/cbuseridentity/1423888-isenabled)Added [CBUserIdentity.posixUID](https://developer.apple.com/documentation/collaboration/cbuseridentity/1423927-posixuid)Modified [CBGroupIdentity](https://developer.apple.com/documentation/collaboration/cbgroupidentity)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class CBGroupIdentity : CBIdentity {     init!(posixGID gid: gid_t, authority authority: CBIdentityAuthority!) -> CBGroupIdentity     class func groupIdentityWithPosixGID(_ gid: gid_t, authority authority: CBIdentityAuthority!) -> CBGroupIdentity!     func posixGID() -> gid_t     func members() -> [AnyObject]! } ``` | OS X 10.10 |
| To | ``` class CBGroupIdentity : CBIdentity {      init?(posixGID gid: gid_t, authority authority: CBIdentityAuthority)     class func groupIdentityWithPosixGID(_ gid: gid_t, authority authority: CBIdentityAuthority) -> CBGroupIdentity?     var posixGID: gid_t { get }     var members: [AnyObject]? { get }     var memberIdentities: [CBIdentity] { get } } ``` | OS X 10.5 |

Modified [CBGroupIdentity.init(posixGID: gid_t, authority: CBIdentityAuthority)](https://developer.apple.com/documentation/collaboration/cbgroupidentity/1423869-groupidentitywithposixgid)

|  | Declaration |
| --- | --- |
| From | ``` init!(posixGID gid: gid_t, authority authority: CBIdentityAuthority!) -> CBGroupIdentity ``` |
| To | ``` init?(posixGID gid: gid_t, authority authority: CBIdentityAuthority) ``` |

Modified [CBIdentity](https://developer.apple.com/documentation/collaboration/cbidentity)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class CBIdentity : NSObject, NSCoding, NSCopying {     init!(name name: String!, authority authority: CBIdentityAuthority!) -> CBIdentity     class func identityWithName(_ name: String!, authority authority: CBIdentityAuthority!) -> CBIdentity!     init!(UUIDString uuid: String!, authority authority: CBIdentityAuthority!) -> CBIdentity     class func identityWithUUIDString(_ uuid: String!, authority authority: CBIdentityAuthority!) -> CBIdentity!     init!(persistentReference data: NSData!) -> CBIdentity     class func identityWithPersistentReference(_ data: NSData!) -> CBIdentity!     init!(CSIdentity csIdentity: CSIdentity!) -> CBIdentity     class func identityWithCSIdentity(_ csIdentity: CSIdentity!) -> CBIdentity!     func authority() -> CBIdentityAuthority!     func UUIDString() -> String!     func fullName() -> String!     func posixName() -> String!     func aliases() -> [AnyObject]!     func emailAddress() -> String!     func image() -> NSImage!     func persistentReference() -> NSData!     func isHidden() -> Bool     func isMemberOfGroup(_ group: CBGroupIdentity!) -> Bool     func CSIdentity() -> Unmanaged<CSIdentity>! } ``` | OS X 10.10 |
| To | ``` class CBIdentity : NSObject, NSCoding, NSCopying {      init?(name name: String, authority authority: CBIdentityAuthority)     class func identityWithName(_ name: String, authority authority: CBIdentityAuthority) -> CBIdentity?      init?(uniqueIdentifier uuid: NSUUID, authority authority: CBIdentityAuthority)     class func identityWithUniqueIdentifier(_ uuid: NSUUID, authority authority: CBIdentityAuthority) -> CBIdentity?      init?(UUIDString uuid: String, authority authority: CBIdentityAuthority)     class func identityWithUUIDString(_ uuid: String, authority authority: CBIdentityAuthority) -> CBIdentity?      init?(persistentReference data: NSData)     class func identityWithPersistentReference(_ data: NSData) -> CBIdentity?      init(CSIdentity csIdentity: CSIdentity)     class func identityWithCSIdentity(_ csIdentity: CSIdentity) -> CBIdentity     var authority: CBIdentityAuthority { get }     var uniqueIdentifier: NSUUID { get }     var UUIDString: String { get }     var fullName: String { get }     var posixName: String { get }     var aliases: [String] { get }     var emailAddress: String? { get }     var image: NSImage? { get }     var persistentReference: NSData? { get }     var hidden: Bool { get }     func isMemberOfGroup(_ group: CBGroupIdentity) -> Bool     var CSIdentity: CSIdentity { get } } ``` | OS X 10.5 |

Modified [CBIdentity.init(name: String, authority: CBIdentityAuthority)](https://developer.apple.com/documentation/collaboration/cbidentity/1423881-identitywithname)

|  | Declaration |
| --- | --- |
| From | ``` init!(name name: String!, authority authority: CBIdentityAuthority!) -> CBIdentity ``` |
| To | ``` init?(name name: String, authority authority: CBIdentityAuthority) ``` |

Modified [CBIdentity.init(persistentReference: NSData)](https://developer.apple.com/documentation/collaboration/cbidentity/1423945-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(persistentReference data: NSData!) -> CBIdentity ``` |
| To | ``` init?(persistentReference data: NSData) ``` |

Modified [CBIdentity.init(UUIDString: String, authority: CBIdentityAuthority)](https://developer.apple.com/documentation/collaboration/cbidentity/1423855-identitywithuuidstring)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` init!(UUIDString uuid: String!, authority authority: CBIdentityAuthority!) -> CBIdentity ``` | OS X 10.10 | -- |
| To | ``` init?(UUIDString uuid: String, authority authority: CBIdentityAuthority) ``` | OS X 10.5 | OS X 10.11 |

Modified [CBIdentity.isMemberOfGroup(_: CBGroupIdentity) -> Bool](https://developer.apple.com/documentation/collaboration/cbidentity/1423867-ismember)

|  | Declaration |
| --- | --- |
| From | ``` func isMemberOfGroup(_ group: CBGroupIdentity!) -> Bool ``` |
| To | ``` func isMemberOfGroup(_ group: CBGroupIdentity) -> Bool ``` |

Modified [CBIdentityAuthority](https://developer.apple.com/documentation/collaboration/cbidentityauthority)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class CBIdentityAuthority : NSObject {     class func localIdentityAuthority() -> CBIdentityAuthority!     class func managedIdentityAuthority() -> CBIdentityAuthority!     class func defaultIdentityAuthority() -> CBIdentityAuthority!     init!(CSIdentityAuthority CSIdentityAuthority: CSIdentityAuthority!) -> CBIdentityAuthority     class func identityAuthorityWithCSIdentityAuthority(_ CSIdentityAuthority: CSIdentityAuthority!) -> CBIdentityAuthority!     func CSIdentityAuthority() -> Unmanaged<CSIdentityAuthority>!     func localizedName() -> String! } ``` | OS X 10.10 |
| To | ``` class CBIdentityAuthority : NSObject {     class func localIdentityAuthority() -> CBIdentityAuthority     class func managedIdentityAuthority() -> CBIdentityAuthority     class func defaultIdentityAuthority() -> CBIdentityAuthority      init(CSIdentityAuthority CSIdentityAuthority: CSIdentityAuthority)     class func identityAuthorityWithCSIdentityAuthority(_ CSIdentityAuthority: CSIdentityAuthority) -> CBIdentityAuthority     var CSIdentityAuthority: CSIdentityAuthority { get }     var localizedName: String { get } } ``` | OS X 10.5 |

Modified [CBIdentityAuthority.defaultIdentityAuthority() -> CBIdentityAuthority [class]](https://developer.apple.com/documentation/collaboration/cbidentityauthority/1423853-default)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultIdentityAuthority() -> CBIdentityAuthority! ``` |
| To | ``` class func defaultIdentityAuthority() -> CBIdentityAuthority ``` |

Modified [CBIdentityAuthority.localIdentityAuthority() -> CBIdentityAuthority [class]](https://developer.apple.com/documentation/collaboration/cbidentityauthority/1423861-local)

|  | Declaration |
| --- | --- |
| From | ``` class func localIdentityAuthority() -> CBIdentityAuthority! ``` |
| To | ``` class func localIdentityAuthority() -> CBIdentityAuthority ``` |

Modified [CBIdentityAuthority.managedIdentityAuthority() -> CBIdentityAuthority [class]](https://developer.apple.com/documentation/collaboration/cbidentityauthority/1423865-managedidentityauthority)

|  | Declaration |
| --- | --- |
| From | ``` class func managedIdentityAuthority() -> CBIdentityAuthority! ``` |
| To | ``` class func managedIdentityAuthority() -> CBIdentityAuthority ``` |

Modified [CBIdentityPicker](https://developer.apple.com/documentation/collaboration/cbidentitypicker)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class CBIdentityPicker : NSObject {     func setTitle(_ title: String!)     func title() -> String!     func setAllowsMultipleSelection(_ flag: Bool)     func allowsMultipleSelection() -> Bool     func runModal() -> Int     func runModalForWindow(_ window: NSWindow!, modalDelegate delegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func identities() -> [AnyObject]! } ``` | OS X 10.10 |
| To | ``` class CBIdentityPicker : NSObject {     var title: String?     var allowsMultipleSelection: Bool     func runModal() -> Int     func runModalForWindow(_ window: NSWindow, modalDelegate delegate: AnyObject?, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func runModalForWindow(_ window: NSWindow, completionHandler completionHandler: ((NSModalResponse) -> Void)?)     var identities: [CBIdentity] { get } } ``` | OS X 10.5 |

Modified [CBIdentityPicker.runModalForWindow(_: NSWindow, modalDelegate: AnyObject?, didEndSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/collaboration/cbidentitypicker/1423893-runmodal)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func runModalForWindow(_ window: NSWindow!, modalDelegate delegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` | OS X 10.10 | -- |
| To | ``` func runModalForWindow(_ window: NSWindow, modalDelegate delegate: AnyObject?, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` | OS X 10.5 | OS X 10.11 |

Modified [CBUserIdentity](https://developer.apple.com/documentation/collaboration/cbuseridentity)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class CBUserIdentity : CBIdentity, NSCoding, NSCopying {     init!(posixUID uid: uid_t, authority authority: CBIdentityAuthority!) -> CBUserIdentity     class func userIdentityWithPosixUID(_ uid: uid_t, authority authority: CBIdentityAuthority!) -> CBUserIdentity!     func posixUID() -> uid_t     func certificate() -> Unmanaged<SecCertificate>!     func isEnabled() -> Bool     func authenticateWithPassword(_ password: String!) -> Bool } ``` | OS X 10.10 |
| To | ``` class CBUserIdentity : CBIdentity {      init?(posixUID uid: uid_t, authority authority: CBIdentityAuthority)     class func userIdentityWithPosixUID(_ uid: uid_t, authority authority: CBIdentityAuthority) -> CBUserIdentity?     var posixUID: uid_t { get }     var certificate: SecCertificate? { get }     var enabled: Bool { get }     func authenticateWithPassword(_ password: String) -> Bool } ``` | OS X 10.5 |

Modified [CBUserIdentity.authenticateWithPassword(_: String) -> Bool](https://developer.apple.com/documentation/collaboration/cbuseridentity/1423892-authenticatewithpassword)

|  | Declaration |
| --- | --- |
| From | ``` func authenticateWithPassword(_ password: String!) -> Bool ``` |
| To | ``` func authenticateWithPassword(_ password: String) -> Bool ``` |

Modified [CBUserIdentity.init(posixUID: uid_t, authority: CBIdentityAuthority)](https://developer.apple.com/documentation/collaboration/cbuseridentity/1423925-useridentitywithposixuid)

|  | Declaration |
| --- | --- |
| From | ``` init!(posixUID uid: uid_t, authority authority: CBIdentityAuthority!) -> CBUserIdentity ``` |
| To | ``` init?(posixUID uid: uid_t, authority authority: CBIdentityAuthority) ``` |

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
