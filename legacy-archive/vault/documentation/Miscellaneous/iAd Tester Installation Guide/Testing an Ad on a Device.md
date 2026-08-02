---
title: iAd Tester Installation Guide
apple_id: TP40011958
resource_type: Guide
platform: iAd System JS|iAd Producer|iOS
topic: General
technology: null
published: '2012-04-02'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/iAd_Tester_Installation_Guide/TestinganAdonaDevice/TestinganAdonaDevice.html
archived_at: '2026-07-15T08:17:10.379167Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Document%20Revision%20History.md)

# Testing an Ad on a Device

iAd Tester enables you to test your ads on iPad and iPhone devices using the following methods:

- Uploading ads to the iAd Creative Management Sandbox, enabling you to view ads in ways that are similar to how users view them on their devices in the live environment. (You must be a registered iAd developer to do this.)
- Exporting the ad to disk and then transferring the ad to a device using iTunes File Sharing.

Before you can do any testing on a device, you must install iAd Tester on it.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To obtain the iAd Tester app:

1. Download and install iAd Producer from the iOS Dev Center at [https://developer.apple.com/iad/iadproducer/](https://developer.apple.com/iad/iadproducer/).
2. Locate `iAd Producer.app` in `/Applications/`.
3. Control-click (right-click) on iAd Producer.app and select Show Package Contents.
4. Locate `iAdTester.app` in `iAd Producer.app/Contents/SharedSupport/iAdTester/Device`.
![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To install iAd Tester on a device

1. After you have installed the latest iAd Producer, locate the iAd Tester app on your computer.
2. Make sure you have the latest version of iTunes installed on your computer by performing a Software Update check from the Apple menu.
3. Drag `iAdTester.app` to either the iTunes Dock icon or to the Library panel in an open iTunes window.
4. With your device connected to the computer, make sure the iAd Tester app is checked in the Apps pane for the device.
5. Click Apply to sync apps.

After you’ve installed iAd Tester on your device, you can test ads that you've uploaded to the iAd Creative Management Sandbox. You can also use iTunes File Sharing to test an exported ad on your device.

Testing an ad that you’ve uploaded to the iAd Creative Management Sandbox simulates the real-world environment, giving you the best approximation of the user’s actual experience.

After you upload a rich media ad bundle to the iAd Creative Management Sandbox and receive staging ad URLs from Apple, you can test the ad on your device.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To test an ad in the iAd Creative Management Sandbox

1. To launch the app, tap the iAd Tester app icon on the Home screen.
2. In the confirmation email you received from the iAd Creative Management portal, tap on one of the links.
3. iAd Tester displays the ad’s banner in the placeholder app UI.

You can use iTunes File Sharing to transfer an ad from your Mac to a device for testing.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To test an exported ad on your device

1. In the Finder, locate your ad bundle compressed zip file.
2. Connect your device to the computer.
3. In iTunes, select the device and click the Apps tab.
4. In the File Sharing area at the bottom of the iTunes window, select iAd Tester in the Apps pane.
5. Drag the compressed ad project to the iAd Tester Documents pane and sync your device.

   Another way to add the file to the pane is to click the Add button at the bottom of the iAd Tester Documents pane, navigate to the compressed ad project, and click Choose.
6. On your device, tap the iAd Tester app icon on the Home screen.
7. In the iAd Library page, tap On My Device to see a list of exported ads that you’ve synced to your device.

   To open an ad, tap the name of the exported ad project in the list.

[Next](Document%20Revision%20History.md)

