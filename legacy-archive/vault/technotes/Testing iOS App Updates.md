---
title: Testing iOS App Updates
apple_id: DTS40011323
resource_type: Technical Note
platform: iOS
topic: General
technology: null
published: '2014-10-07'
source_url: https://developer.apple.com/library/archive/technotes/tn2285/_index.html
archived_at: '2026-07-26T19:54:10.131125Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2285

# Testing iOS App Updates

This technote discusses how to test an update to an iOS app that has already been deployed through the App Store. General testing methodology is beyond the scope of this document. For information on optimizing update delivery, see "[Reducing Download Size for iOS App Updates](https://developer.apple.com/library/ios/qa/qa1779/)" and "[Reducing the Size of my App](https://developer.apple.com/library/ios/qa/qa1795/)".

[Recommended Testing Procedure](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzsgmwugsbrfvee6v2jkrjuit2oiu)[To create an Archived build that you can both test and submit:](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzsgmwugsbrfvbfkskmirevi)[Managing Data Across Updates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzsgmwugsbrfvdestcfkm)[New Hardware](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzsgmwugsbrfvdestcfkmwu4rkxl5eecusek5averi)[Debugging Ad Hoc Builds](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzsgmwugsbrfvcekqsvi5dustsh)[Next Steps](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzsgmwugsbrfvhekwcuknkekuct)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzsgmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Recommended Testing Procedure

Install an ad hoc distribution of an archived build of the update using iTunes on a device that already has the old version of the app installed.

__Warning:__ Install your app with iTunes and launch it __without__ Xcode for quality assurance testing.

Xcode's app install process is optimized for development, but is slightly different than how iTunes and the App Store install apps. This is good during development because it's faster, but using Xcode to install an app over an older old build may create a "frankenbuild" with legacy files inside the `.app` bundle that won't exist after an App Store update.

When an app is updated, the old `.app` bundle is completely replaced, and all data in the old app container __may__ be preserved as well.

Additionally, running with Xcode's debugger attached will mask "[watchdog crashes](https://developer.apple.com/library/ios/qa/qa1592/)" that can happen if an upgrade takes too long to launch.

[Back to Top](#)

## To create an Archived build that you can both test and submit:

__1)__ In Xcode choose "Archive" from the "Product" menu to archive a build of your app. You can find the archive in the Archives tab in the Organizer window.

__Note:__ If you have problems with this step, see [Troubleshooting application archiving in Xcode](https://developer.apple.com/library/ios/technotes/tn2215/).

__2)__ Package the build as an "Ad Hoc" `.ipa` file by selecting it in the Organizer window and pressing "Distribute…"; then select "Save for Enterprise or Ad-Hoc Deployment". Choose any "Code Signing Identity:" that will let you install on your test device.

__Warning:__ Do __not__ choose your App Store Distribution profile for this step. It will sign the `.ipa` file so it can only be used by the App Store, preventing you from installing it yourself and testing.

__3)__ Test updating to that build by opening the `.ipa` file with iTunes and syncing to install it on a device that has the previous version of your app installed. Be sure you've used the previous version of the app enough that it's saved any data it might save during use. The most common problem updates have is not properly dealing with data created by the previous version of the app.

__Note:__ If you have trouble installing the `.ipa` file, refer to [Installation Failure Troubleshooting for iOS](https://developer.apple.com/library/ios/technotes/tn2319/).

[Back to Top](#)

## Managing Data Across Updates

The most common cause of bugs after an update is the new version of the app not handling data created by a previous version of the app.

When an app is updated, the very latest version available in the App Store for the target device is installed. Intermediate updates are __not__ run. Your app needs to handle data created by __any__ previous versions of the app.

When an app is updated, the `.app` bundle is completely replaced by the latest version of the app. Also, the absolute path to the app's container ("`Application_Home`") and thus all files inside it, will change. For this reason, you must only save paths to files relative to your application container.

`NSSearchPathForDirectoriesInDomains`() or `-[NSFileManager` `URLsForDirectory:inDomains:]` will always give you a valid path to the current <`Application_Home`> or a standard subdirectory inside it.

__Listing 1__  A method that returns a URL to the current `Application_Home/Documents` directory

```objc
- (NSURL *)applicationDocumentsDirectory {
    return [[[NSFileManager defaultManager] URLsForDirectory:NSDocumentDirectory inDomains:NSUserDomainMask] lastObject];
}
```

Any data inside the app container __may__ be preserved when the app is updated. From a practical standpoints, this means your app needs to gracefully handle (or ignore) old caches and temporary files.

`<Application_Home>/Documents/` and `<Application_Home>/Library` (excluding the `<Application_Home>/Library/Caches` subdirectory) are the only directories that are __guaranteed__ to be preserved across updates. Although other <`Application_Home`> subdirectories may be moved over, you should not rely on this as an API contract.

### New Hardware

When a user migrates to a new device for the first time, backed up data from their older device is installed on the new device, along with the latest version of any apps that were installed on the old device. This scenario is the same as a regular update, except for two considerations. Temporary data will absolutely not be installed, because it was never backed up. Also, any files that were marked as "[do not backup](https://developer.apple.com/library/IOS/qa/qa1719/)" will not be installed.

[Back to Top](#)

## Debugging Ad Hoc Builds

If a problem only reproduces in an Ad Hoc build, you'll need to analyze Crash Logs and Console output from the device to debug it. [Debugging Deployed iOS Apps](https://developer.apple.com/library/ios/qa/qa1747/) explains how to gather this information. See [Understanding and Analyzing iOS Application Crash Reports](https://developer.apple.com/library/ios/#technotes/tn2151/_index.html) and the [Understanding Crash Reports on iOS](https://developer.apple.com/videos/wwdc/2010/?id=317) WWDC Session for tips.

[Back to Top](#)

## Next Steps

After testing an archived build to your satisfaction, you can submit it to the App Store, [by following these steps](https://developer.apple.com/library/etc/redirect/DTS/iOSAppDistGuide). It is important to submit the __exact same build__ you have tested.

For information on making sure your app and update are small enough to be downloaded without a Wi-Fi connection, see "[Reducing the Size of my App](https://developer.apple.com/library/ios/qa/qa1795/)" and "[Reducing Download Size for iOS App Updates](https://developer.apple.com/library/ios/qa/qa1779/)".

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-10-07 | Added more details on the update process and what files are preserved. |
| 2014-05-14 | Removed list of overly-specific possible issues. |
| 2013-02-13 | Editorial changes. |
| 2011-10-27 | New document that discusses some best practices for testing an update to an iOS app that has already been deployed through the App Store. |

