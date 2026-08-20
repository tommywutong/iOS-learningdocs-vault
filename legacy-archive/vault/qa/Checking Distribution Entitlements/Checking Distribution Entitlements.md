---
title: Checking Distribution Entitlements
apple_id: DTS40014167
resource_type: QA
platform: iOS|Xcode Developer Tools|macOS
topic: Languages & Utilities
technology: null
published: '2015-10-08'
source_url: https://developer.apple.com/library/archive/qa/qa1798/_index.html
archived_at: '2026-07-18T02:34:49.654217Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1798

# Checking Distribution Entitlements

## Q:  How can I verify that my submission to the App Store was code signed and entitled correctly?

A: During the app distribution process through the Xcode Organizer > Archives tab, entitlements are set onto the app by way of the provisioning profile used for code signing. It is important to be aware that the re-application of entitlements at this phase creates the opportunity for unintended entitlement differences between any prior development builds you may have tested. The primary purpose of this document is to verify that your entitlements are correct for your distribution builds for beta testing and App Store submission.

Xcode shows the distribution build's entitlements in the Summary pane during the submission workflow. This is the last opportunity you have to visually ensure that your app contains the expected entitlements before submitting your app for review.

__Figure 1__  Distribution build entitlements preview in Xcode.

!!

Alternatively to Xcode's entitlements preview, you can check the entitlements of an iOS app store submission by first creating and inspecting an .ipa file. The following steps outline the process to do this.

1. In the Xcode Organizer, instead of Submit to the iOS App Store, do Save for Enterprise or Ad-Hoc Deployment. This will create a local copy of the .ipa file that would be submitted to the App Store.
2. When asked to choose the provisioning profile to sign with, select the same distribution profile you use when submitting to the App Store. Take a screenshot of your choice (command-shift-3) so you can verify this step later. During submission, this screenshot will be the only record you have identifying which profile was used to sign the app.
3. When asked to save the package, uncheck Save for Enterprise Distribution, then save the .ipa file.

1. Find the .ipa file and change its the extension to .zip.
2. Expand the `.zip` file. This will produce a `Payload` folder containing your .app bundle.
3. Use the codesign tool to check the entitlements on the .app bundle like this:


```
$ codesign -d --entitlements :- "Payload/YourApp.app"
```

   where YourApp.app is the actual name of your .app bundle.
4. Use the security tool to check the entitlements of the app's embedded provisioning profile:


```
$ security cms -D -i "Payload/YourApp.app/embedded.mobileprovision"
```

   where YourApp.app is the actual name of your .app bundle.

Alternatively to Xcode's entitlements preview, you can check the entitlements of a OS X app store submission by first creating and inspecting an .ipa file. The following steps outline the process to do this.

1. In the Xcode Organizer, instead of Submit to the Mac App Store, do Export as Mac Installer Package. That will create a local copy of the .pkg file that would be submitted to the Mac App Store.
2. When asked to choose a provisioning profile to sign with, select the same distribution profile you use when submitting to the Mac App Store. Take a screenshot of your choice (command-shift-3) so you can verify this step later. During submission, this screenshot is the only record you'll have that identifies which profile was used to sign the app.
3. Save the .pkg file when prompted.
4. Use the pkgutil tool to expand the package into its components:


```
$ pkgutil --expand "YourApp.pkg" Expanded_pkg
```

   where YourApp.pkg is the actual name of the package you created in the previous step.
5. Expand the compressed payload inside the package using the `open` tool or by double-clicking it:


```
$ open Expanded_pkg/com.yourcompany.yourapp/Payload
```

   where com.yourcompany.yourapp is the actual bundle ID of your app.

Use the `codesign` tool to check the entitlements on the .app bundle like this:


```
$ codesign -d --entitlements - "Expanded_pkg/com.yourcompany.yourapp/YourApp.app"
```

where YourApp.app is the actual name of your .app bundle.

Use the security tool to check the entitlements of the app's embedded provisioning profile:


```
$ security cms -D -i "Expanded_pkg/com.yourcompany.yourapp/YourApp.app/embedded.provisionprofile"
```

where YourApp.app is the actual name of your .app bundle.

Follow these steps if an entitlement is not set as expected.

1. Log into [Certificates, Identifiers & Profiles](https://developer.apple.com/account/overview.action) > (iOS or OS X) > Provisioning Profiles > Distribution.

- Click the distribution profile and ensure the desired entitlements are listed under "Enabled services." If the desired services are not enabled, navigate to the App ID section of the site and enable the necessary services on the App ID associated to the distribution profile.
- Ensure the status of the distribution profile is "Valid." If the status is "Invalid," it means that the profile needs to be regenerated. A profile's status becomes invalid if there were changes made to its associated certificates or to the enabled services of its App ID. To regenerate the profile, select it from the list and click "Edit." Associate the profile to any new certificates (if necessary) and then click "Generate."

2. Follow the steps in [Refreshing Provisioning Profiles in Xcode](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html#//apple_ref/doc/uid/TP40012582-CH30-SW26) to ensure that Xcode's provisioning profile library is up to date.

3. Click "Distribute..." on the Xcode > Organizer > Archives tab and choose the distribution profile within the Provisioning Profile selection menu. Take a screenshot of your choice (command-shift-3) so you can verify this step later. During submission, this screenshot will be the only record you have that identifies which profile was used to sign the app.

For troubleshooting general entitlement problems, see __TN2415__ - [Entitlements Troubleshooting](https://developer.apple.com/library/ios/technotes/tn2415/_index.html#//apple_ref/doc/uid/DTS40016427).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-10-08 | Cover Xcode's new entitlements preview. Fix error in profile entitlements command. |
| 2014-09-10 | Add requirement to check app's embedded provisioning profile. |
| 2014-05-06 | Additional troubleshooting. |
| 2014-02-24 | New document that describes how to check entitlements on development or distribution builds for accuracy before installation or submission. |

