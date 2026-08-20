---
title: Resolving the "No identities are available for signing" Error
apple_id: DTS40014678
resource_type: QA
platform: iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: Security
published: '2014-06-17'
source_url: https://developer.apple.com/library/archive/qa/qa1862/_index.html
archived_at: '2026-07-18T02:35:09.366624Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1862

# Resolving the "No identities are available for signing" Error

## Q:  How do I resolve the "No identities are available for signing" error?

A: This document iterates the common reasons Xcode presents the error message "No identities are available for signing" during the Distribute phase on the Xcode Organizer. To resolve this error, make sure your Xcode and account configuration satisfy all the items in the following list.

1. Verify that your team distribution certificate is installed within your OS X user's default keychain. The steps to verify this are covered in [App Distribution Guide](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingCertificates/MaintainingCertificates.html#//apple_ref/doc/uid/TP40012582-CH31-SW8) __> Maintaining Your Signing Identities and Certificates > Requesting Signing Identities > Verifying Your Steps > Verifying Using Keychain Access__.

2. Verify that the expiration date on the distribution certificate has not lapsed, and, that it corresponds with the expiration date of the team distribution certificate listed in [Member Center](https://developer.apple.com/membercenter/index.action) __> Certificates, Identifiers & Profiles > (your program) > Certificates > Production__.

- If the expiration date has lapsed you must create a new team distribution certificate. The complete process is covered in [App Distribution Guide](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingCertificates/MaintainingCertificates.html#//apple_ref/doc/uid/TP40012582-CH31-SW34%20%20) __> Maintaining Your Signing Identities and Certificates > Re-Creating Certificates and Updating Related Provisioning Profiles__.
- If the expiration date differs then you must acquire the certificate that exists on Member Center since it is the only active certificate. The process of acquiring the missing certificate can be done by following the process in [App Distribution Guide](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingCertificates/MaintainingCertificates.html#//apple_ref/doc/uid/TP40012582-CH31-SW15) __> Maintaining Your Signing Identities and Certificates > Exporting and Importing Certificates and Profiles__. The export must be done on the Mac where the distribution certificate was originally created, or was transferred to. If you cannot acquire the certificate, then you must re-create it by following the steps in the former link.

1. Sign into [Member Center](https://developer.apple.com/membercenter/index.action) __> Certificates, Identifiers & Profiles > (your platform) > Provisioning Profiles > Distribution__ and verify your distribution provisioning profile is listed. If it's not, you must create it using the steps in [App Distribution Guide](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/SubmittingYourApp/SubmittingYourApp.html#//apple_ref/doc/uid/TP40012582-CH9-SW8) __> Submitting Your App > Creating Store Provisioning Profiles__.

2. Verify the distribution profile is installed in Xcode's provisioning profile library, which can be viewed in __Xcode > Preferences > Accounts > (your account) > View Details > Provisioning Profiles__. If the distribution profile is not listed, press the "↺" button to have Xcode download it.

Verify that the App ID associated to the distribution profile is compatible with the app's Bundle Identifier defined in Xcode. To do that:

- Click on the distribution profile within [Member Center](https://developer.apple.com/membercenter/index.action) __> Certificates, Identifiers & Profiles > (your platform) > Provisioning Profiles > Distribution__.
- Check that the value for the App ID (within the parenthesis) matches the Bundle Identifier entered in the Xcode project's Target > Info tab.
- If the App ID contains an asterisk ("\*"), then confirm this wildcard App ID is compatible with the Bundle Identifier according to the discussion about multiple app wildcard matching within the __App ID__ section of [Cocoa Core Competencies Guide](https://developer.apple.com/library/ios/documentation/general/conceptual/DevPedia-CocoaCore/AppID.html).

If there are multiple team distribution certificates listed in [Member Center](https://developer.apple.com/membercenter/index.action) __> Certificates, Identifiers & Profiles > (your program) > Certificates > Production__ then there are a couple points to consider.

If you don't have all of the team distribution certificates installed in your OS X user's default keychain, and, not all of the team distribution certificates are associated to the distribution provisioning profile, then it's possible the distribution certificate in your keychain isn't the same distribution certificate that is associated with your distribution provisioning profile. Xcode will present the error is this case because it is unable to code signing apps for distribution with this configuration.

To diagnose and resolve this situation:

1. Sign into [Member Center](https://developer.apple.com/membercenter/index.action) __> Certificates, Identifiers & Profiles > (your program) > Certificates > Production__ and compare the number of certificates listed here with those seen in your OS X user's default keychain. Compare the certificate's expiration date to match them up.

If there are more certificates listed in Member Center than those installed in your keychain, you can resolve the issue by acquiring each of the missing team distribution certificates using the process in [App Distribution Guide](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingCertificates/MaintainingCertificates.html#//apple_ref/doc/uid/TP40012582-CH31-SW15) __> Maintaining Your Signing Identities and Certificates > Exporting and Importing Certificates and Profiles__. The export must be done on the Mac where the distribution certificate was originally created, or was transferred to.

2. If you're not able to acquire and install all of the team's distribution certificates, then at least, you must ensure that one team distribution certificate you have in your keychain is associated to the distribution provisioning profile. To do that:

- Log into [Member Center](https://developer.apple.com/membercenter/index.action) __> Certificates, Identifiers & Profiles > (your platform) > Provisioning Profiles > Distribution__ and click to edit the distribution provisioning profile.
- Within the list of associated certificates, compare the expiration dates with the distribution certificates installed in your keychain.
- Check the box next to the certificate whose expiration date matches the one installed in your keychain.
- If you made a change to the profile, regenerate it like so:

  - Click Generate at the bottom of the page.
  - Sync profiles in Xcode using the steps in [App Distribution Guide](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html#//apple_ref/doc/uid/TP40012582-CH30-SW26) __> Maintaining Your Signing Identities and Certificates > Refreshing Provisioning Profiles in Xcode__.
  - Or, manually download the regenerated profile and install it by dragging it onto the Xcode icon on your Dock.

Account access in Member Center and iTunes Connect must be in good standing, and associated with the proper role that allows app submission. Follow the upcoming steps to ensure Xcode does not present this error due to account configuration issues.

1. Sign into [Member Center](https://developer.apple.com/membercenter/index.action) __> Certificates, Identifiers & Profiles__ to verify your access.

2. If there are any agreement updates, the team Agent must agree to the new terms & conditions on the [Member Center](https://developer.apple.com/membercenter/index.action#agreements) __> Agreements__. Xcode will present this error when agreements must be re-signed before app submission can be resumed.

1. Sign into [iTunes Connect](https://itunesconnect.apple.com/) to verify your access.

2. If there are any agreement updates, a user with the Legal role must agree to the new contract in the Contracts, Tax, and Banking page. Xcode will present this error when agreements must be re-signed before app submission can be resumed.

3. Click your username in the upper-right corner __> Personal Details > Roles__. The Technical role is required for the Manage Your Apps page in order for you to submit apps.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-06-17 | New document that resolves the "No identities are available for signing" error during Xcode 5's distribute workflow. |

