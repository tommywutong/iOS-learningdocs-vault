---
title: Resolving App ID Prefix Mismatching
apple_id: DTS40014940
resource_type: QA
platform: iOS|macOS
topic: Languages & Utilities
technology: Security
published: '2014-09-10'
source_url: https://developer.apple.com/library/archive/qa/qa1879/_index.html
archived_at: '2026-07-18T02:35:11.971698Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1879

# Resolving App ID Prefix Mismatching

## Q:  How do I diagnose and resolve an App ID Prefix mismatch?

A: The App ID Prefix on an app's signature must match the App ID Prefix in the app's embedded provisioning profile. An app whose prefix does not match across its signature and embedded profile will fail validation for submission and will also fail to install on testing or enterprise iOS devices.

This document shows how to diagnose and resolve an App ID Prefix mismatch.

There are two code signing phases involved in distributing an app and the App ID Prefix of the Provisioning Profiles used in both phases must match. If they don't, it'll cause an App ID Prefix mismatch. The easiest way to satisfy the requirement is to make sure that the same profile is used in both phases.

An example App ID Prefix is shown below. It's the 10-character prefix of the App ID associated with the Provisioning Profile. So for App ID:


```
A1B2C3D4E5.com.myCompany.myApp1
```

The App ID Prefix is:


```
A1B2C3D4E5
```

To diagnose an App ID Prefix mismatch, you'll be comparing prefixes across two locations within the built app. Those locations are numbered below.

1. Check the App ID Prefix on the app's signature using the steps in [How do I check the entitlements on my Application's Signature?](https://developer.apple.com/library/ios/technotes/tn2318/_index.html#//apple_ref/doc/uid/DTS40013777-CH1-TNTAG33).

   __Listing 1__  Example entitlements on an app's signature.

```
$ codesign -d --entitlements :- ./Payload/myApp.app

Executable=./Payload/myApp.app/myApp
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>application-identifier</key>
    <string>5E4D3C2B1A.com.myCompany.myApp1</string>
    <key>com.apple.developer.team-identifier</key>
    <string>5E4D3C2B1A</string>
    <key>get-task-allow</key>
    <false/>
    <key>keychain-access-groups</key>
    <array>
        <string>5E4D3C2B1A.com.myCompany.myApp1</string>
    </array>
</dict>
</plist>
```
2. Check the App ID Prefix in the app’s embedded profile using the steps in: [How do I check the entitlements associated to my Provisioning Profile?](https://developer.apple.com/library/ios/technotes/tn2318/_index.html#//apple_ref/doc/uid/DTS40013777-CH1-TNTAG65) Use the steps in the second half of the section that talk about the app's embedded profile.

   __Listing 2__  Example entitlements associated to an app's embedded provisioning profile.

```
$ security cms -D -i "./Payload/myApp.app/embedded.mobileprovision"

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
   ...
  <key>Entitlements</key>
  <dict>
    <key>com.apple.developer.team-identifier</key>
    <string>5E4D3C2B1A</string>
    <key>keychain-access-groups</key>
    <array>
      <string>A1B2C3D4E5.com.myCompany.*</string>
    </array>
    <key>application-identifier</key>
    <string>A1B2C3D4E5.com.myCompany.*</string>
    <key>get-task-allow</key>
    <false/>
  </dict>
  <key>ExpirationDate</key>
  <date>2015-08-13T14:59:38Z</date>
  <key>Name</key>
  <string>Distribution Provisioning Profile</string>
  <key>TeamIdentifier</key>
  <array>
    <string>5E4D3C2B1A</string>
  </array>
  <key>TeamName</key>
  <string>Appleseed Corp.</string>
  <key>TimeToLive</key>
  <integer>364</integer>
  <key>UUID</key>
  <string>7156a539-3c66-41f5-a0b5-49c3456659d7</string>
  <key>Version</key>
  <integer>1</integer>
</dict>
```

The mismatch in the above example can be seen by comparing the 10-character prefix of the `application-identifier` entitlement. This is the App ID Prefix. The prefix on the app's signature `5E4D3C2B1A` doesn't match the prefix on the app's embedded profile `A1B2C3D4E5`.

There are two code signing phases involved in distributing an app and the App ID Prefix of both profiles used in those phases must match.

The easiest way to satisfy this requirement is to use the same profile in both signing phases:

1. Open the Xcode project Target > Build Settings, and expand the Code Signing Identity and Provisioning Profile build settings. Set “Any iOS SDK” to “iOS Distribution” for Release.
2. Set the Provisioning Profile build setting to your distribution provisioning profile.
3. Re-archive the app (via Xcode > Product menu > Archive).
4. Re-submit the app through the Xcode Organizer, and be sure to pick the same distribution profile to sign the submission.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-09-10 | New document that walks through the process of diagnosing and resolving an App ID Prefix mismatch. |

