---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/Collaboration.html
archived_at: '2026-07-15T07:34:51.159426Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# Collaboration Changes

## Collaboration (Added)

Added CBGroupIdentityAdded CBGroupIdentity.members() -> [AnyObject]!Added CBGroupIdentity.posixGID() -> gid_tAdded CBGroupIdentity.init(posixGID: gid_t, authority: CBIdentityAuthority!)Added CBIdentityAdded CBIdentity.CSIdentity() -> Unmanaged<CSIdentity>!Added CBIdentity.init(CSIdentity: CSIdentity!)Added CBIdentity.UUIDString() -> String!Added CBIdentity.init(UUIDString: String!, authority: CBIdentityAuthority!)Added CBIdentity.aliases() -> [AnyObject]!Added CBIdentity.authority() -> CBIdentityAuthority!Added CBIdentity.emailAddress() -> String!Added CBIdentity.fullName() -> String!Added CBIdentity.image() -> NSImage!Added CBIdentity.isHidden() -> BoolAdded CBIdentity.isMemberOfGroup(CBGroupIdentity!) -> BoolAdded CBIdentity.init(name: String!, authority: CBIdentityAuthority!)Added CBIdentity.persistentReference() -> NSData!Added CBIdentity.init(persistentReference: NSData!)Added CBIdentity.posixName() -> String!Added CBIdentityAuthorityAdded CBIdentityAuthority.CSIdentityAuthority() -> Unmanaged<CSIdentityAuthority>!Added CBIdentityAuthority.init(CSIdentityAuthority: CSIdentityAuthority!)Added CBIdentityAuthority.defaultIdentityAuthority() -> CBIdentityAuthority! [class]Added CBIdentityAuthority.localIdentityAuthority() -> CBIdentityAuthority! [class]Added CBIdentityAuthority.localizedName() -> String!Added CBIdentityAuthority.managedIdentityAuthority() -> CBIdentityAuthority! [class]Added CBIdentityPickerAdded CBIdentityPicker.allowsMultipleSelection() -> BoolAdded CBIdentityPicker.identities() -> [AnyObject]!Added CBIdentityPicker.runModal() -> IntAdded CBIdentityPicker.runModalForWindow(NSWindow!, modalDelegate: AnyObject!, didEndSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)Added CBIdentityPicker.setAllowsMultipleSelection(Bool)Added CBIdentityPicker.setTitle(String!)Added CBIdentityPicker.title() -> String!Added CBUserIdentityAdded CBUserIdentity.authenticateWithPassword(String!) -> BoolAdded CBUserIdentity.certificate() -> Unmanaged<SecCertificate>!Added CBUserIdentity.isEnabled() -> BoolAdded CBUserIdentity.posixUID() -> uid_tAdded CBUserIdentity.init(posixUID: uid_t, authority: CBIdentityAuthority!)

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
