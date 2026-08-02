---
title: Game Center Configuration Guide for iTunes Connect
apple_id: TP40013726
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-10-02'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/iTunesConnectGameCenter_Guide/DistributingGameCenterApps/DistributingGameCenterApps.html
archived_at: '2026-07-27T06:57:08.933337Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Game Center Configuration Guide for iTunes Connect](Introduction.md)


[Next](Game%20Center%20Properties.md)[Previous](Testing%20Your%20App.md)

# Distributing Game Center Apps

When you’re ready to submit your app to the App Store or Mac App Store, use the Game Center section on Versions of the App Details page. There you’ll enable this version of your app to include Game Center functionality and indicate which leaderboards and achievements it will support.

## Turning On Game Center for the App Version

In the app’s Game Center section on Versions, you turn on the Game Center functionality you want to apply to this version of the app.

- Enable Game Center for the version.
- Select leaderboards to support in this app version.
- Select achievements to support in this app version.
- Select which apps and versions that you want this app to be compatible with.

Enabling Game Center functionality is one part of the overall app submission process described in Submitting the App to App Review in _iTunes Connect Developer Guide_.

![bullet](attachments/Resources/1282/Images/task_2x.png)To enable a version of your app for Game Center

1. Go to the App Details page as described in Creating an iTunes Connect Record for an App in _iTunes Connect Developer Guide_.
2. In the Game Center section on Versions, click the switch to enable Game Center.

   （原归档配图未能恢复：`VersionsGCOn_2x.png`）
3. If the app uses leaderboard sets and you have leaderboards to submit with this version of your app, edit the Leaderboard Set information as follows.

   1. In the Leaderboard Sets section, click the plus sign.
   2. Select the plus sign to choose a leaderboard set that includes leaderboards you want to submit.
   3. In the right pane, select the individual leaderboards from that set to submit.

      （原归档配图获取待重试：`AddLBSet_2x.png`）
   4. Click Done.
4. If you have leaderboards to submit with this version of your app, edit the leaderboard information as follows.

   If the app uses leaderboard sets and you selected your leaderboards through the sets, you can skip this step.

   1. In the Leaderboards section, click the plus sign.
   2. Select the leaderboards you want to submit.

      （原归档配图获取待重试：`AddLB_2x.png`）
   3. Click Done.
5. If you have achievements to submit with this version of your app, edit the Achievements section as follows.

   1. In the Achievements section, click the plus sign.
   2. Select the achievements you want to submit.

      （原归档配图获取待重试：`AddAchiev_2x.png`）
   3. Click Done.
6. If the app is part of a group or if you want this app to be compatible with other apps, edit the multiplayer compatibility section as follows.

   1. In the Multiplayer Compatibility section, click the plus sign.
   2. Choose a compatible app from the Add pop-up menu (+) (located below the list of apps).

      （原归档配图未能恢复：`AddMPC_2x.png`）

      The Add pop-up menu (+) displays the icon, name, and platform for each Game Center-enabled app you can add.
   3. Select the versions of the app that will be compatible with the app you’re submitting.
   4. Click Done.
7. Click "Submit for Review".

## Disabling Game Center in Your App

If a version of your app was previously approved, you can no longer disable Game Center for all versions of your app. Instead, you must change Game Center properties for a new version of your app when you update it. If you disable a version of your app for Game Center, you need to change the multiplayer compatibility settings, as described in [To enable a version of your app for Game Center](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrwfvjvomrz).

__Note:__ Any leaderboards that are in use in Game Center remain available to users even if you disable Game Center for the current version of the app.

![bullet](attachments/Resources/1282/Images/task_2x.png)To disable a version of your app for Game Center

1. Select the app from My Apps.
2. On Versions, go to the Game Center section of the app.
3. Toggle the Game Center switch to the off position.

[Next](Game%20Center%20Properties.md)[Previous](Testing%20Your%20App.md)
