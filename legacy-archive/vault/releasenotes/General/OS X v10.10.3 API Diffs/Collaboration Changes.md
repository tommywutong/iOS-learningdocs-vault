---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/Collaboration.html
archived_at: '2026-07-18T02:52:09.726874Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# Collaboration Changes

## Collaboration

Added CBIdentity.image() -> NSImage!Added CBIdentityPicker.runModalForWindow(NSWindow!, modalDelegate: AnyObject!, didEndSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)Modified CBGroupIdentity.init(posixGID: gid_t, authority: CBIdentityAuthority!)

|  | Declaration |
| --- | --- |
| From | ``` init(posixGID gid: gid_t, authority authority: CBIdentityAuthority!) -> CBGroupIdentity ``` |
| To | ``` init!(posixGID gid: gid_t, authority authority: CBIdentityAuthority!) -> CBGroupIdentity ``` |

Modified CBIdentity.init(CSIdentity: CSIdentity!)

|  | Declaration |
| --- | --- |
| From | ``` init(CSIdentity csIdentity: CSIdentity!) -> CBIdentity ``` |
| To | ``` init!(CSIdentity csIdentity: CSIdentity!) -> CBIdentity ``` |

Modified CBIdentity.init(UUIDString: String!, authority: CBIdentityAuthority!)

|  | Declaration |
| --- | --- |
| From | ``` init(UUIDString uuid: String!, authority authority: CBIdentityAuthority!) -> CBIdentity ``` |
| To | ``` init!(UUIDString uuid: String!, authority authority: CBIdentityAuthority!) -> CBIdentity ``` |

Modified CBIdentity.init(name: String!, authority: CBIdentityAuthority!)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: String!, authority authority: CBIdentityAuthority!) -> CBIdentity ``` |
| To | ``` init!(name name: String!, authority authority: CBIdentityAuthority!) -> CBIdentity ``` |

Modified CBIdentity.init(persistentReference: NSData!)

|  | Declaration |
| --- | --- |
| From | ``` init(persistentReference data: NSData!) -> CBIdentity ``` |
| To | ``` init!(persistentReference data: NSData!) -> CBIdentity ``` |

Modified CBIdentityAuthority.init(CSIdentityAuthority: CSIdentityAuthority!)

|  | Declaration |
| --- | --- |
| From | ``` init(CSIdentityAuthority CSIdentityAuthority: CSIdentityAuthority!) -> CBIdentityAuthority ``` |
| To | ``` init!(CSIdentityAuthority CSIdentityAuthority: CSIdentityAuthority!) -> CBIdentityAuthority ``` |

Modified CBUserIdentity.init(posixUID: uid_t, authority: CBIdentityAuthority!)

|  | Declaration |
| --- | --- |
| From | ``` init(posixUID uid: uid_t, authority authority: CBIdentityAuthority!) -> CBUserIdentity ``` |
| To | ``` init!(posixUID uid: uid_t, authority authority: CBIdentityAuthority!) -> CBUserIdentity ``` |

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
