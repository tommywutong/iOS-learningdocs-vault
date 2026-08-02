---
title: Resolving the Potential Loss of Keychain Access warning
apple_id: DTS40014942
resource_type: QA
platform: iOS
topic: Languages & Utilities
technology: Security
published: '2015-06-02'
source_url: https://developer.apple.com/library/archive/qa/qa1726/_index.html
archived_at: '2026-07-18T02:34:30.009479Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1726

# Resolving the Potential Loss of Keychain Access warning

## Q:  How do I resolve the Potential Loss of Keychain Access warning?

A: 

```
Potential Loss of Keychain Access. The previous version of software has an application-identifier value of 'A1B2C3D4E5.com.company.app' and the new version of software being submitted has an application-identifier of '5E4D3C2B1A.com.company.app'. This will result in a loss of keychain access.
```

This warning indicates that the App ID prefix of the pending submission differs from the App ID prefix of the live app in the app store.

Apps that should expect this warning and proceed with the submission regardless are:

1. Those that are migrating their App ID prefix from an arbitrary Bundle Seed ID to their more-modern Team ID as documented in [Technical Note TN2311 - Managing Multiple App ID Prefixes](https://developer.apple.com/library/ios/technotes/tn2311/_index.html).
2. Those that are submitting the first update for a recently acquired app via App Transfer.

For apps that do utilize technologies that rely on the App ID prefix, this warning should not be ignored. The Potential Loss of Keychain Access warning is an indication that the app was code signed with the wrong provisioning profile.

To resolve the problem:

1. You must locate or re-create a provisioning profile that uses the correct App ID prefix on the [Certs IDs & Profiles](https://developer.apple.com/account/overview.action) website.
2. Click Edit on the profile to be certain the prefix is correct.
3. Click Download and save the profile to disk.
4. Optionally double check the App ID Prefix on the downloaded profile using the Terminal command in: [How do I check the entitlements associated with my Provisioning Profile?](https://developer.apple.com/library/ios/technotes/tn2318/_index.html#//apple_ref/doc/uid/DTS40013777-CH1-TNTAG65)
5. Drag the profile onto the Xcode icon on your Dock to install it.
6. Re-submit the app and code sign it with the newly restored profile that is associated with the right prefix.

"Keychain access" refers to all the functions in the [Keychain Services Reference](https://developer.apple.com/library/ios/documentation/Security/Reference/keychainservices/index.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-06-02 | Cover App Transfer expectations. |
| 2014-10-07 | Editorial update. |
| 2014-09-10 | New document that walks thru resolving the Potential Loss of Keychain Access warning. |

