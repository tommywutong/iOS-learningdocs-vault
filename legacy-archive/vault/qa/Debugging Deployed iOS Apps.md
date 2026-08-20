---
title: Debugging Deployed iOS Apps
apple_id: DTS40011341
resource_type: QA
platform: iOS
topic: Languages & Utilities
technology: null
published: '2015-07-30'
source_url: https://developer.apple.com/library/archive/qa/qa1747/_index.html
archived_at: '2026-07-27T07:25:59.530350Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1747

# Debugging Deployed iOS Apps

## Q:  How can I debug a deployed app without Xcode's debugger?

A: Once you have deployed your app, either through the App Store or as an Ad Hoc or Enterprise build, you won't be able to attach Xcode's debugger to it. To debug problems, you need to analyze Crash Logs and Console output from the device.

Apple Watch crash logs will be available on the paired device and can also be obtained using the methods described below.

For more information on writing rich `NSLog` statements, see [Improved logging in Objective-C](https://developer.apple.com/library/ios/#qa/qa1669/_index.html).

## Getting Crash Logs and Console Output

### Getting Crash Logs Directly From a Device Without Xcode

Your users can retrieve crash reports from their device and send them to you via email by following these instructions.

(It is not possible to get device console logs directly from a device)

1) Open Settings app

2) Go to Privacy, then Diagnostics & Usage

3) Select Diagnostics & Usage Data

4) Locate the log for the crashed app. The logs will be named in the format: <AppName>_<DateTime>_<DeviceName>

5) Select the desired log. Then, using the text selection UI select the entire text of the log. Once the text is selected, tap Copy

6) Paste the copied text to Mail and send to an email address as desired

### Getting Crash Logs and Console Output From a Device Using Xcode

Even though you won't be able to run the app in Xcode's debugger, Xcode can still give you all the information you need to debug the problem.

#### Using Xcode 6

1) Plug in the device and open Xcode

2) Choose Window -> Devices from the menu bar

3) Under the DEVICES section in the left column, choose the device

4) To see the device console, click the up-triangle at the bottom left of the right hand panel

5) Click the down arrow on the bottom right to save the console as a file

6) To see crash logs, select the View Device Logs button under the Device Information section on the right hand panel

7) Find your app in the Process column and select the Crash log to see the contents.

8) To save a crash log, right click the entry on the left column and choose "Export Log"

9) Xcode 6 will also list low memory logs here. These will be shown with a Process name "Unknown" and Type "Unknown". You should examine the contents of these logs to determine whether any of these are caused by your app. For more information about low memory logs, see [Understanding and Analyzing iOS Application Crash Reports](https://developer.apple.com/library/ios/#technotes/tn2151/_index.html).

#### Using Xcode 5

1) Plug in the device and open Xcode

2) Open the Organizer window and select the Devices tab

3) Under the DEVICES section in the left column, expand the listing for the device

4) Select Device Logs to see crash logs or select Console to see Console output

[Back to Top](#)

## Enabling App Store Diagnostic Reporting

Crash logs are automatically collected from customers who have opted in to sending diagnostic and usage information to Apple.

Beginning with Xcode 6.3, crash logs from App Store customers running at least iOS 8.3 and TestFlight beta testers can be found in the Xcode Organizer. To obtain these crash logs:

1) Open the Organizer window in Xcode 6.3 and above

2) Select "Crashes" at the top. The available crash logs can then be found within this window.

The [App Distribution Guide](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/AnalyzingCrashReports/AnalyzingCrashReports.html) contains further information about the Crash Reporting service.

Crash reports from customers running older iOS versions may be found in [iTunes Connect](https://itunesconnect.apple.com/).

If someone is reporting a crash, and you do not see a corresponding report in iTunes Connect, you should direct them to the following knowledge base articles [for Mac](http://support.apple.com/kb/PH19602) or [for Windows](http://support.apple.com/kb/PH12477) so they can opt-in to sending you crash reports.

[Back to Top](#)

## Understanding Crash Logs and Console Output

The first and most important step to understanding crash logs is to symbolicate them. Symbolication replaces memory addresses with human-readable function names and line numbers.

If you get crash logs off a device through Xcode's Devices window, then they will be symbolicated for you automatically after a few seconds. Otherwise you will need to symbolicate the .crash file yourself by importing it to the Xcode. Open the Xcode Devices window, select the device in question, drag the crash file to the left hand column, control-click the file you just added and select “Re-Symbolicate Log” from the menu.

For more information on interpreting crash logs, see the [Understanding and Analyzing iOS Application Crash Reports](https://developer.apple.com/library/ios/#technotes/tn2151/_index.html) technote and the [Understanding Crash Reports on iPhone OS WWDC 2010 Session](https://developer.apple.com/videos/wwdc/2010/?id=317).

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-07-30 | Added comment for Apple Watch crash logs, and instructions on how to obtain App Store and TestFlight crash logs from Xcode. |
| 2015-05-14 | Added method to obtain crash logs directly from a device without using Xcode |
| 2015-01-08 | Updated links and removed sections no longer relevant. |
| 2014-12-15 | Updated instructions for obtaining device console and logs with Xcode 6 |
| 2012-03-28 | Added notes about low memory logs. |
| 2011-11-09 | New document that describes how to debug apps that have been deployed, either through the App Store or as Ad Hoc builds |
