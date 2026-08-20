---
title: iOS Code Signing Troubleshooting Index
apple_id: DTS40014991
resource_type: Technical Note
platform: iOS|macOS
topic: Languages & Utilities
technology: Security
published: '2015-08-18'
source_url: https://developer.apple.com/library/archive/technotes/tn2407/_index.html
archived_at: '2026-07-26T19:54:14.870368Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2407

# iOS Code Signing Troubleshooting Index

This document is an index of all of the iOS code signing troubleshooting information. The most important first step is to confirm that your project opts into automatic provisioning; this alone solves many code signing problems. The processes documented by Apple to Run on device, Beta Test, or Submit your app all involve code signing and their related code signing errors are covered in the subsequent sections.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojzgewugsbrfveu4vcsj5cfkq2ujfhu4)[Ensure your project opts into Automatic Provisioning](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojzgewugsbrfvcu4u2vkjcv6wkpkvjf6ucsj5fekq2ul5hvavctl5eu4vcpl5avkvcpjvaviskdl5ifet2wjfjust2ojfheo)[Follow workflows documented by Apple to Run on device, Beta Test, or Submit your app](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojzgewugsbrfvde6tcmj5lv6v2pkjfumtcpk5jv6rcpinku2rkokrcuix2clfpucucqjrcv6vcpl5jfkts7j5hf6rcfkzeugrk7l5bekvcbl5keku2ul5pu6us7knkuetkjkrpvst2vkjpucucq)[Run your app on device through Xcode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojzgewugsbrfvde6tcmj5lv6v2pkjfumtcpk5jv6rcpinku2rkokrcuix2clfpucucqjrcv6vcpl5jfkts7j5hf6rcfkzeugrk7l5bekvcbl5keku2ul5pu6us7knkuetkjkrpvst2vkjpucucqfvjfkts7lfhvkus7ififax2pjzpuirkwjfbukx2ujbje6vkhjbpvqq2pircq)[Beta Testing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojzgewugsbrfvde6tcmj5lv6v2pkjfumtcpk5jv6rcpinku2rkokrcuix2clfpucucqjrcv6vcpl5jfkts7j5hf6rcfkzeugrk7l5bekvcbl5keku2ul5pu6us7knkuetkjkrpvst2vkjpucucqfvbekvcbl5keku2ujfheo)[Submitting to the App Store](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojzgewugsbrfvde6tcmj5lv6v2pkjfumtcpk5jv6rcpinku2rkokrcuix2clfpucucqjrcv6vcpl5jfkts7j5hf6rcfkzeugrk7l5bekvcbl5keku2ul5pu6us7knkuetkjkrpvst2vkjpucucqfvjvkqsnjfkfiskoi5pvit27kreekx2bkbif6u2uj5jek)[Enterprise Distribution](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojzgewugsbrfvde6tcmj5lv6v2pkjfumtcpk5jv6rcpinku2rkokrcuix2clfpucucqjrcv6vcpl5jfkts7j5hf6rcfkzeugrk7l5bekvcbl5keku2ul5pu6us7knkuetkjkrpvst2vkjpucucqfvcu4vcfkjifesktivpuisktkrjesqsvkreu6tq)[Client and Contractor Distribution workflow](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojzgewugsbrfvde6tcmj5lv6v2pkjfumtcpk5jv6rcpinku2rkokrcuix2clfpucucqjrcv6vcpl5jfkts7j5hf6rcfkzeugrk7l5bekvcbl5keku2ul5pu6us7knkuetkjkrpvst2vkjpucucqfvbuyskfjzkf6qkoirpugt2okrjecq2uj5jf6rcjknkfeskckvkest2ol5lu6uslizge6vy)[Enabling code signing on your other Macs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojzgewugsbrfvmemrks)[List of Code Signing Errors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojzgewugsbrfvgesu2ul5humx2dj5cekx2tjfdu4skoi5pukussj5jfg)[Missing Certificate or Private Key errors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojzgewugsbrfvgesu2ul5humx2dj5cekx2tjfdu4skoi5pukussj5jfglknjfjvgskoi5pugrkskreumskdifkekx2pkjpvausjkzavirk7jncvsx2fkjje6ust)[Provisioning Profile related errors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojzgewugsbrfvgesu2ul5humx2dj5cekx2tjfdu4skoi5pukussj5jfglkqkjhvmsktjfhu4skoi5pvauspizeuyrk7kjcuyqkuivcf6rkskjhveuy)[Installation Failure](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojzgewugsbrfvgesu2ul5humx2dj5cekx2tjfdu4skoi5pukussj5jfglkjjzjviqkmjraviskpjzpumqkjjrkveri)[Signature Verification Errors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojzgewugsbrfvgesu2ul5humx2dj5cekx2tjfdu4skoi5pukussj5jfglktjfdu4qkukvjekx2wivjesrsjinaviskpjzpukussj5jfg)[Entitlements Errors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojzgewugsbrfvgesu2ul5humx2dj5cekx2tjfdu4skoi5pukussj5jfglkfjzkesvcmivguktsuknpukussj5jfg)[Other Errors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojzgewugsbrfvgesu2ul5humx2dj5cekx2tjfdu4skoi5pukussj5jfglkpkreekus7ivjfet2skm)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojzgewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

The first step in troubleshooting iOS code signing errors is to configure your project for automatic provisioning. This is the currently recommended and supported workflow, whereas, the manual provisioning process of assigning specific code signing build settings yourself takes longer to do and it is often more problematic.

[Back to Top](#)

## Ensure your project opts into Automatic Provisioning

The first step to troubleshoot iOS code signing failures is to opt your project into the modern code signing workflow. This is done by enabling automatic provisioning as covered the following guide:

__• QA1814__ - [Setting up Xcode to automatically manage your provisioning profiles](https://developer.apple.com/library/ios/qa/qa1814/_index.html).

[Back to Top](#)

## Follow workflows documented by Apple to Run on device, Beta Test, or Submit your app

The second step in troubleshooting iOS code signing problems is to ensure you're following the proper workflow. The following is a complete list of workflows that involve code signing that are supported by Apple.

### Run your app on device through Xcode

__• App Distribution Guide__ > Launching Your App on Devices

### Beta Testing

The following are two options to beta test your iOS app:

1. __TestFlight Beta Testing__

   Using TestFlight to beta test iOS apps involves submitting an app to iTunes Connect that is signed with your App Store distribution provisioning profile. Once the app passes your beta tests you simply queue it for release to the App Store through iTunes Connect. This is the preferred method of beta testing because it does not require you to re-build or re-sign the submission for App Store publication.

   __• App Distribution Guide__ > Beta Testing iOS Apps > Distributing Your Prerelease Build Using TestFlight

   __Important:__ Because apps submitted to TestFlight must be code signed with an App Store distribution provisioning profile, TestFlight cannot be used for the beta testing of Enterprise apps.
2. __Ad Hoc Beta Testing__

   __Important:__ TestFlight is the preferred method of the distribution of beta test builds because it does not require you to re-code sign the app in order to submit it for App Store publication. Therefore, only use Ad Hoc beta testing if there is a compelling reason that you cannot use TestFlight.

   To beta test iOS apps using Ad Hoc distribution, follow the steps in:

   __• App Distribution Guide__ > Beta Testing iOS Apps > Distributing Your Beta App Using Ad Hoc Provisioning

### Submitting to the App Store

Use the following process to submit your app for review:

__• App Distribution Guide__ > Submitting Your App to the Store > Submitting Your App to the Store

### Enterprise Distribution

The documented process to distribute Enterprise apps is covered in the __iOS Deployment Reference__ > [Introduction](https://help.apple.com/deployment/ios/#/apd5b9e6434f)

### Client and Contractor Distribution workflow

When a development contractor must distribute an app on behalf of the app client/owner, you must follow the workflow for build engineer distribution covered here:

__• QA1763__ - _[How can a build engineer distribute an app on behalf of the team?](../qa/How%20can%20a%20build%20engineer%20distribute%20an%20app%20on%20behalf%20of%20the%20team.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytemjwgu)_

### Enabling code signing on your other Macs

To enable code signing on your other Macs, OS X user accounts or partitions, use Xcode to export and import your code signing assets using the steps in:

__• App Distribution Guide__ > Maintaining Your Signing Identities and Certificates > Exporting and Importing Certificates and Profiles

[Back to Top](#)

## List of Code Signing Errors

The previous sections ensure that you opt into automatic provisioning and follow the workflow that involves code signing documented by Apple. For persistent code signing issues, consult the following list of code signing topics and their corresponding troubleshooting material.

### Missing Certificate or Private Key errors

These errors indicate that you are missing a required certificate or private key that is needed for code signing:

```
Missing Signing Identities
```

```
No Matching Signing Identity or Provisioning Profiles Found
```

```
The Private Key for Your Signing Identity Is Missing
```

```
The Private Key for a Developer ID Certificate Is Missing
```

Use the directions in the following guide to correct these kinds of problems:

__• App Distribution Guide__ > Troubleshooting > Certificate Issues

__Note:__ For App Store teams, a majority of missing signing identity related issues can easily be resolved by recreating your certificates. See the following section for steps to do this: __• App Distribution Guide__ > Maintaining Your Signing Identities and Certificates > Re-Creating Certificates and Updating Related Provisioning Profiles.

__Important:__ For Enterprise teams which are missing their distribution certificate or its private key, you must instead consult the following document created specifically for this case: __• QA1868__ - [Missing Enterprise Distribution Certificate Private Keys](https://developer.apple.com/library/ios/qa/qa1868/_index.html).

### Provisioning Profile related errors

For general provisioning profile related issues such as:

```
Invalid Provisioning Profile
```

```
Provisioning Profiles Installed on Your Device Are Invalid
```

```
No Such Provisioning Profile Was Found
```

See the following guide's recommendations to resolve them:

__• App Distribution Guide__ > Troubleshooting > Provisioning Issues

```
Provisioning Profiles Appear Invalid in Member Center
```

For answers to why your provisioning profile's status changes to Invalid, see the document:

__• QA1878__ - [Resolving the Provisioning Profile Invalid Status](https://developer.apple.com/library/ios/qa/qa1878/_index.html)

### Installation Failure

If your app is experiencing an installation failure, consult the resolutions that are covered in:

__• TN2319__ - _[Installation Failure Troubleshooting for iOS](Installation%20Failure%20Troubleshooting%20for%20iOS/Installation%20Failure%20Troubleshooting%20for%20iOS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgnzxha)_

### Signature Verification Errors

The following errors are related to app validation:

```
The bundle is not signed using an Apple submission certificate
```

```
Missing or Invalid Signature. (rejection email)
```

```
The bundle ... at bundle path ... is not signed using an Apple submission certificate
```

For help with signature verification errors such as those listed above, use the recommendations and troubleshooting steps covered in:

__• TN2318__ - _[Troubleshooting Failed Signature Verification](Troubleshooting%20Failed%20Signature%20Verification/Troubleshooting%20Failed%20Signature%20Verification.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgnzxg4)_.

### Entitlements Errors

```
Invalid Code Signing Entitlements
```

Use the following guides to troubleshooting entitlement related errors:

1. __• TN2415__ - [Entitlements Troubleshooting](https://developer.apple.com/library/ios/technotes/tn2415/_index.html)
2. __• QA1798__ - _[Checking Distribution Entitlements](../qa/Checking%20Distribution%20Entitlements/Checking%20Distribution%20Entitlements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimjwg4)_

```
None of valid provisioning profile allowed the specified entitlements
```

This error indicates that Xcode expects a specific entitlement for your app but it cannot find a provisioning profile that contains that entitlement. There are different resolutions to this error depending on the entitlement that Xcode is looking for:

- `beta-reports-active`

  See the following document that covers this topic in detail:

  __• QA1830__ - [The beta-reports-active Entitlement](https://developer.apple.com/library/ios/qa/qa1830/_index.html).
- __All other entitlements__

  1. Sync Xcode's local provisioning profile library with the current state of the Certs, ID's and Profiles website using:

     __• Xcode__ > Preferences > Accounts > (your account) > View Details > "⟳" button.
  2. Thoroughly analyze the Capabilities, Services, Entitlements your app uses with the guidance of:

     __• TN2415__ - [Entitlements Troubleshooting](https://developer.apple.com/library/ios/technotes/tn2415/_index.html)

### Other Errors

It's not always possible to infer the subject of all error messages. Check the following list of these types of general errors:

```
Your account already has a valid iOS distribution certificate
```

This error primarily indicates that your development Mac is missing the distribution certificate and/or its private key. As a result, Xcode is attempting to generate a new distribution certificate / private key pair on your behalf, however, failed to do so because your team already has the maximum number of concurrently allowable distribution certificates.

Use one of the following options to resolve this error:

- Transfer the missing certificate or private key to your Mac using the steps in section [Enabling code signing on your other Macs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojzgewugsbrfvmemrks).
- Revoke and re-create your distribution certificate using the steps in:

  __• App Distribution Guide__ > Maintaining Your Signing Identities and Certificates > Re-Creating Certificates and Updating Related Provisioning Profiles

  __Important:__ Enterprise developers must take extra caution when resolving missing distribution certificate private keys, and should instead follow the process covered in a document created specifically for this situation. See __QA1868__ - [Missing Enterprise Distribution Certificate Private Keys](https://developer.apple.com/library/ios/qa/qa1868/_index.html).
[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-08-18 | Link new entitlements troubleshooting document. |
| 2015-07-21 | Editorial update. |
| 2015-03-16 | Moved Application-Identifier issues to the installation failure technical note. |
| 2015-02-03 | added information about application-identifier and previous-application-identifiers entitlements |
| 2014-11-13 | reorganization of contents |
| 2014-10-14 | Including workflow for testing via iTunes Connect. |
| 2014-10-02 | New document that provides a starting point to troubleshoot problems in workflows that involve code signing. |

