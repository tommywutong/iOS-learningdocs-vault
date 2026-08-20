---
title: Testing Distribution Builds of Mac Apps
apple_id: DTS40015141
resource_type: QA
platform: macOS
topic: Languages & Utilities
technology: Security
published: '2015-01-26'
source_url: https://developer.apple.com/library/archive/qa/qa1884/_index.html
archived_at: '2026-07-18T02:35:16.249404Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1884

# Testing Distribution Builds of Mac Apps

## Q:  When I run my Mac app, it crashes immediately, and the crash log says Exception Type: EXC_CRASH (Code Signature Invalid). What is going on here?

A: The crash log indicates that your app is signed with your Mac App Store distribution identity, with the certificate’s Subject Common Name starting with “3rd Party Mac Developer Application.” Mac apps signed this way can no longer be run directly. Here’s the background on this.

Over time, more Mac App Store technologies have been added that require entitlements that come from a provisioning profile. This started with push notifications and iCloud. Later, Game Center and Maps were added to the list.

Distribution builds of apps that use those technologies may be submitted to iTunes Connect for review, but until then, aren’t allowed to run and are killed on launch. This is because distribution provisioning profiles do not contain a list of hardware UUIDs that restrict the app to a specific set of devices. This is similar to iOS where distribution builds have never been allowed to run on a device.

Recently, the `com.apple.developer.team-identifier` entitlement was added to all new Mac provisioning profiles. This means that, going forward, distribution builds of Mac apps cannot be run directly; they are for submitting to iTunes Connect for app review only.

Instead, developers should adopt the Archive Build Workflow in [QA1778: How to reproduce bugs reported against Mac App Store submissions](https://developer.apple.com/library/mac/qa/qa1778/_index.html) for testing the builds that they plan to submit for the Mac App Store. On Xcode 6, select `Export as a Mac Application`. You won't see any chance to select your development signing identity, but Xcode will export the app from the archive as it was signed at build time. So the result will be the same.

You can create an installer package containing your development-signed app by hand with the `productbuild` tool, like this:


```
$ productbuild --component Sample.app /Applications --sign “3rd Party Mac Developer Installer:" Sample.pkg
```

Then install the package as documented in [Testing the Mac Installer Package](https://developer.apple.com/library/mac/documentation/IDEs/Conceptual/AppDistributionGuide/SubmittingYourApp/SubmittingYourApp.html#//apple_ref/doc/uid/TP40012582-CH9-SW40):


```
$ sudo installer -store -pkg Sample.pkg -target /
```

This workflow means that you will need to add your beta testers’ test systems to your Mac Developer Program account so they will be able to run your app.

Another possibility is to use `Xcode Organizer > Export > Export a Developer ID-signed Application`. Developer ID-signed apps can be run by anyone. However, code that uses technologies only available to Mac App Store apps, such as receipt validation, iCloud, and push notifications, will not work if your app is Developer ID-signed. You might need to temporarily disable those parts of your app if you opt for the Developer ID testing approach.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-01-26 | New document that informs developers that distribution builds of Mac apps can no longer be run. |

