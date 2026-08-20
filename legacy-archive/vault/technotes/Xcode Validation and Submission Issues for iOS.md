---
title: Xcode Validation and Submission Issues for iOS
apple_id: DTS40011374
resource_type: Technical Note
platform: iOS
topic: Languages & Utilities
technology: null
published: '2012-11-29'
source_url: https://developer.apple.com/library/archive/technotes/tn2294/_index.html
archived_at: '2026-07-26T19:54:10.167295Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



# Retired Document

__Important:__
This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Technical Note TN2294

# Xcode Validation and Submission Issues for iOS

__Important:__ This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Covers common errors that occur during Xcode Validation or Application Submission, and offers steps to resolve or work around those issues. For more information, see the [iTunes Connect Developer Guide](https://developer.apple.com/library/mac/#documentation/LanguagesUtilities/Conceptual/iTunesConnect_Guide/1_Introduction/Introduction.html).

[Xcode Validation Errors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzxgqwugsbrfvke4vcbi4yq)[Application failed codesign verification](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzxgqwugsbrfvke4vcbi4zq)[Bundle identifier: (x) differs from reserved bundle identifier: (y)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzxgqwugsbrfvke4vcbi42q)[iTunes Connect Store - Binary Rejection emails](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzxgqwugsbrfvke4vcbi4za)[Invalid Signature](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzxgqwugsbrfvke4vcbi42a)[Invalid Code Signing Entitlements - com.apple.developer.ubiquity-kvstore-identifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzxgqwugsbrfvke4vcbi43a)[Invalid Launch Image](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzxgqwugsbrfvke4vcbi43q)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzxgqwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Xcode Validation Errors

This section covers common issues that occur during Xcode Archive Validation, or during application submission with App Loader, and offers steps to resolve or work around those issues.

### Application failed codesign verification

Examples of this error follow:

```
Application failed codesign verification. The signature was invalid, or it was not signed with an iPhone Distribution Certificate.

Application failed codesign verification. The signature was invalid, or it was not signed with an Apple Submission Certificate.

warning: Application failed codesign verification. The signature was invalid, or it was not signed with an iPhone Distribution Certificate. (-19011)
```

To resolve this error, use the troublshooting process described here [How do I resolve the error: Application failed codesign verification?](https://developer.apple.com/library/ios/technotes/tn2250/_index.html#//apple_ref/doc/uid/DTS40009933-CH1-TNTAG32)

### Bundle identifier: (x) differs from reserved bundle identifier: (y)

Submissions for application updates will alternatively read as:

```
Bundle identifier: (x) differs from prior bundle identifier: (y)
```

This error occurs when you've chosen a Bundle Identifier for this app in iTunes Connect that resolves to (y) but you've defined the bundle Identifier in your Xcode project Target > Info tab (or application's Info.plist) as (x). One of the two needs to change depending on which you intend to use for this app.

1) refer to the [iTunes Connect Developer Guide](http://itunesconnect.apple.com/docs/iTunesConnect_DeveloperGuide.pdf) for steps to define the Bundle ID on the [iTunes Connect](http://itunesconnect.apple.com) website.

2) refer to the TN2250 section for steps on [Defining a Bundle Identifier in Xcode that is compatible with your App ID](https://developer.apple.com/library/ios/#technotes/tn2250/_index.html).

[Back to Top](#)

## iTunes Connect Store - Binary Rejection emails

When your uploaded app receives the status 'Invalid Binary' in iTunes Connect, an automated email from the iTunes Connect Store is sent to you identifying the particular rejection reason. This section covers some of the common rejection reasons and elaborates or offers additional steps to address the issue.

### Invalid Signature

This issue is caused by a bug in older versions of Xcode. To work around the problem it is recommended to update to the latest Mac OS X and latest Xcode, then rebuild, and resubmit your application. Many developers either work around this issue by upgrading, or they attain a version of Xcode which correctly identifies an actual problem with the submission at client side validation time.

### Invalid Code Signing Entitlements - com.apple.developer.ubiquity-kvstore-identifier

An example of this rejection email follows:

```
Invalid Code Signing Entitlements - The signature for your app bundle contains entitlement values that are not supported.

Specifically, value "ABC123DE45.*" for key "com.apple.developer.ubiquity-kvstore-identifier" in ... is not supported.
```

This error results from building your app with Xcode prior to version 4.2. The solution depends on whether you intend to utilize iCloud in your application or not. If you do intend to use iCloud, download and install the latest version of Xcode which supports iCloud (4.2 for 10.6, and 4.2.1 for 10.7) from the downloads section of the [iOS Dev Center](https://developer.apple.com/devcenter/ios/index.action) website.

If you do not intend to utilize iCloud in your application, follow these steps to ensure your project is configured accordingly:

1) The "Enable for iCloud" check box should be switched off for your app's "App ID" on the [iOS Portal > App IDs](https://developer.apple.com/ios/manage/bundles/index.action) section. To do that, click "Configure" next to the App ID and uncheck "Enabled for iCloud".

2) Once iCloud has been disabled, generate a new App Store Provisioning Profile for the app to refresh the entitlements associated with your profile. Install the new provisioning profile into Xcode, and assign it to your "Release" code signing identity, according to the steps provided here [Assigning Provisioning Profiles to Build Configurations](https://developer.apple.com/library/ios/technotes/tn2250/_index.html#//apple_ref/doc/uid/DTS40009933-CH1-TNTAG7).

3) Navigate to your Xcode project's Target > Build Settings tab. If you are defining a custom entitlements file in your "Code Signing Entitlements" build setting, check that file within your project and ensure that it does not contain iCloud entitlements. If any of the following iCloud entitlements exist in your custom code signing entitlements file, please remove them:

```
<key>com.apple.developer.ubiquity-container-identifiers</key>
<array>
    <string>A1B2C3D4E5.com.appleseedinc.MyGreatApp</string>
</array>
<key>com.apple.developer.ubiquity-kvstore-identifier</key>
<string>A1B2C3D4E5.com.appleseedinc.MyGreatApp</string>
```

__Important:__ If you do not intend to utilize any custom Code Signing Entitlements in your application, be sure to uncheck the "Entitlements" check box in the Xcode project Target > Summary tab.

4) Rebuild and resubmit your app by following the process described here [Steps to submit your app to the App Store](https://developer.apple.com/library/ios/technotes/tn2250/_index.html#//apple_ref/doc/uid/DTS40009933-CH1-TNTAG13)

### Invalid Launch Image

An example of this rejection email follows:

```
Your app contains a launch image with a size modifier that is only supported for apps built with the iOS 6.0 SDK or later.
```

This issue results from building your application with iOS SDK 5.1 and earlier and adding a `Default-568h@2x.png` image to it in order to support the 4-inch retina display. If you intend to support the 4-inch retina display, then you must build your application against the iOS 6.0 SDK. If you do not intend to build your application against iOS 6 SDK, then remove `Default-568h@2x.png` from your project.

__Note:__ iOS SDK 6.0 is only supported by Xcode 4.5 and later.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-11-29 | Editorial update. |
| 2012-10-10 | Added the Invalid Launch Image binary rejection email. |
| 2012-02-22 | Editorial updates to iCloud and signature verification sections. |
| 2011-12-15 | New document that covers common errors that occur during Xcode Validation or Application Submission, and offers steps to resolve or workaround those issues. |

