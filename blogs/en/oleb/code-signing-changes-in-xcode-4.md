---
title: Code Signing Changes in Xcode 4
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/06/code-signing-changes-in-xcode-4/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b953bf0ad46292cb'
translated: false
---

> 原文：[Code Signing Changes in Xcode 4](https://oleb.net/blog/2011/06/code-signing-changes-in-xcode-4/)　·　Ole Begemann

# Code Signing Changes in Xcode 4

**Update June 21, 2011:** Apparently, the process is not as straightforward as I presented it, especially if you use unique App IDs for your app. Please note the updated section below.

With Xcode 4, Apple improved the way Code Signing works for distribution builds of your iOS apps. Unfortunately, though, Apple has not yet updated [the documentation in the iOS Provisioning Portal](https://developer.apple.com/ios/manage/distribution/index.action), which still focuses on Xcode 3. I recently found out about the changes by accident when I stumbled on a Technical Note titled [Understanding and Resolving Code Signing Issues](https://developer.apple.com/library/content/technotes/tn2250/).

# Use the same build process for Ad Hoc and App Store builds

In the past, the process of preparing a build for Ad Hoc distribution varied slightly from the steps required to make a build for the App Store. In addition to requiring different provisioning profiles, an Ad Hoc build required you to create an `Entitlements.plist` file, uncheck the `get-task-allow` option and include this file in your build settings. This difference usually meant you would create separate build configurations for Ad Hoc and one for App Store distribution in Xcode. It also meant you had to create a fresh build of your app when it was ready for the App Store rather than using the last Ad Hoc build that had been successfully tested by our beta testers^[1](#fn:1).

With Xcode 4, this is no longer necessary. While you still need to sign your app with different provisioning profiles for Ad Hoc and App Store distribution, the code signing can be deferred until after building and archiving^[2](#fn:2). Ad Hoc builds no longer require special Code Signing Entitlements so you can use a single build configuration for all your release builds.

# Step by Step Guide to Code Signing with Xcode 4

1. Use the [iOS Provisioning Portal](http://developer.apple.com/ios/manage/provisioningprofiles/viewDistributionProfiles.action) to generate and download your Distribution Provisioning Profiles. Double-click the downloaded profiles to install them into Xcode. Nothing has changed here.
2. If you have previously created an `Entitlements.plist` file for Ad Hoc distribution, you can delete it. Also remove the filename from your build settings if you have listed it under “Code Signing Entitlements”. Skip this step if you require an entitlements file for other purposes than code signing. In this case, just remove the `get-task-allow` option from the property list.
3. If you have created separate build configurations for Ad Hoc and App Store builds, you can also delete them (unless you are using any custom build settings to customize these builds in another way than code signing). The default “Release” build configuration is enough.
4. The “Code Signing Identity” setting in your target’s Build Settings can be set to your default development provisioning profile (“iPhone Developer”) for both the Debug and the Release configuration. The actual code signing for distribution will be done separately after the build.

  [![Code Signing Build Settings in Xcode 4](https://oleb.net/media/xcode4-code-signing-build-settings.png)](https://oleb.net/media/xcode4-code-signing-build-settings.png)

  <sub>You can use your default development provisioning profile to sign all builds initially. The correct signing for distribution builds is deferred until later.</sub>

  **Update:** Colin Humber, developer at [TestFlight](http://testflightapp.com/), made me aware of a potential problem with this approach. Apparently, the App ID of the provisioning profile that is used for building the app is hardcoded into the binary during the build process. If you later resign the app with a provisioning profile that belongs to different App ID, the one in the binary will no longer match the provisioning profile’s App ID since the binary will not be recompiled. This can cause all sorts of problems with services that rely on the App ID, such as access to the keychain, Push Notifications, or In-App Purchasing.

  [![Hex editor showing the App ID in an iOS app binary](https://oleb.net/media/ios-binary-hex-containing-app-id.png)](https://oleb.net/media/ios-binary-hex-containing-app-id.png)

  <sub>The App ID of the provisioning profile that is used for building the app is embedded in the application binary.</sub>

  This issue will not affect you as long as you use your default “wildcard” App ID (the one that looks like `1234567890.*`). But if you use a separate concrete App ID to publish your app on the App Store, you have to make sure to build your app with a provisioning profile that uses the same App ID. You should not use your default Team Provisioning Profile for release builds in that case. Thanks for the heads-up Colin!
5. Use the Archive build command to create a release build of your app. Open Xcode’s Organizer and find the newly created archive. Now, if you click the Share button to save your Ad Hoc build, you have the chance to select the correct Ad Hoc distribution provisioning profile. Xcode will resign your app with the selected profile. If your beta testers have found no more issues, you can submit exactly the same build to the App Store: just click the Submit button and select your App Store provisioning profile and Xcode will resign your app again.

1. This was possible before with the `codesign` command line tool but not within the Xcode interface. [↩︎](#fnref:1)
2. Guillaume Campagna [told me on Twitter](https://twitter.com/gcamp/status/83178267829485568) that this feature was actually introduced in an earlier version of Xcode. Just the fact that Ad Hoc build no longer need an Entitlements file seems to be new in Xcode 4. Thanks! [↩︎](#fnref:2)
