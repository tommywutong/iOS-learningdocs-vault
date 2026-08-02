---
title: Resolving the Invalid Signature binary rejection
apple_id: DTS40014941
resource_type: QA
platform: iOS
topic: Languages & Utilities
technology: Security
published: '2015-09-29'
source_url: https://developer.apple.com/library/archive/qa/qa1510/_index.html
archived_at: '2026-07-18T02:31:40.494581Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1510

# Resolving the Invalid Signature binary rejection

## Q:  How do I resolve the Invalid Signature binary rejection?

A: The Invalid Signature binary rejection can be caused by the following reasons. Steps are provided to diagnose and resolve each cause.

__Listing 1__  Example Invalid Signature binary rejection email.

```
Invalid Signature - Make sure you have signed your application with a distribution certificate, not an ad hoc certificate or a development certificate. Verify that the code signing settings in Xcode are correct at the target level (which override any values at the project level). Additionally, make sure the bundle you are uploading was built using a Release target in Xcode, not a Simulator target. If you are certain your code signing settings are correct, choose "Clean All" in Xcode, delete the "build" directory in the Finder, and rebuild your release target.
```


The __Code Signing Resource Rules Path__ build setting is no longer used as of Xcode 6. New projects created in Xcode 6+ do not define a value for this build setting. In addition, if your Xcode project is still defining a value for this build setting it can cause the Invalid Signature binary rejection. To resolve this cause of the error, remove values defined for this build setting using the following steps:

1. Open the project level build settings using the Xcode project editor.
2. Select the value portion of the `Code Signing Resource Rules Path` build setting and press delete.
3. Repeat step 1 for all app targets (main app, extensions, other plugins or frameworks that are bundled with your app).
4. Re-create the Xcode archive and re-submit the app.

__Figure 1__  Blank value properly defined for Code Signing Resource Rules Path build setting.

!!

Dot files are a problem that result from copying an unzipped Xcode project to and from a non HFS+ formatted hard drive. Dot files are also referred to as Apple Double files, or resource forks. Use the following steps to diagnose and resolve this situation:

- Run the terminal command diagnostic in Technical Note TN2318 - Troubleshooting Failed Signature Verification > [How do I check if my application's signature has been corrupted?](https://developer.apple.com/library/ios/technotes/tn2318/_index.html#//apple_ref/doc/uid/DTS40013777-CH1-TNTAG38)
- Compare the command results with subsection: [List of Signature Verification Failure Root Causes](https://developer.apple.com/library/ios/technotes/tn2318/_index.html#//apple_ref/doc/uid/DTS40013777-CH1-TNTAG39). The issue is diagnosed with a result stating:


```
resource missing: my.app/._*
```
- Follow these steps to remove the problematic files:

  The file prefixed with "._" is problematic and a was the result of copying certain Mac OS X files to a non-HFS+ formatted disk. These files are invisible to Finder but can be removed using the `dot_clean` utility. The Xcode Project Folder is the argument to `dot_clean` as illustrated below.


```
 dot_clean /path/to/My_Xcode_Project
```
- After running `dot_clean` on your Xcode project, create a new app archive and then re-attempt submission.
- To prevent this issue, be sure to zip Xcode project folders using Finder before transferring them to a non-HFS+ formatted drives.

App Store apps are required to be built with GM versions of OS X and Xcode. If apps are instead built with a beta version of OS X or Xcode, they will be rejected on those grounds. Beta, Seed, Developer Preview and Pre-Release software are synonymous in this context.

Executable files within your app that contain special characters (i.e. non-numeric, and non-alpha) can cause this rejection. To resolve the problem, change the Xcode target’s Product Name build setting from `${TARGET_NAME}` to a string containing only alpha/numeric characters. Also, ensure the value of the Info.plist key "Executable file" is equal to `${EXECUTABLE_NAME}`. If identified to be the cause, please file a bug report using [Apple Bug Reporter](https://developer.apple.com/bug-reporting/) identifying the problematic characters.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-09-29 | Add obsolete code signing resource rules. |
| 2014-09-10 | New document that walks thru resolving the Invalid Signature binary rejection. |

