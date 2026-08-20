---
title: Game Center Configuration Guide for iTunes Connect
apple_id: TP40013726
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-10-02'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/iTunesConnectGameCenter_Guide/AccessAndEnable/AccessAndEnable.html
archived_at: '2026-07-27T06:57:08.847014Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Game Center Configuration Guide for iTunes Connect](Introduction.md)


[Next](Leaderboards%20and%20Leaderboard%20Sets.md)[Previous](Introduction.md)

# Accessing and Enabling Game Center Functionality

Game Center information appears in iTunes Connect at two levels: at the app level, you configure all the details for leaderboards and achievements. At the version level, you identify which leaderboards and achievements to associate with that version of the app. This section describes how to access the two configuration levels.

__Note:__ Only iTunes Connect users with an Admin, Legal, or Technical role have access to Game Center features. For information on assigning user roles, see Setting Up an iTunes Connect User in _iTunes Connect Developer Guide_.

## Navigating to Your App’s Game Center Page

To get started using Game Center with your app, navigate to your app’s Game Center page, and if this is the first time through the process, enable your app for Game Center.

![bullet](attachments/Resources/1282/Images/task_2x.png)To go to your app’s Game Center page in iTunes Connect

1. Sign in to [iTunes Connect](https://itunesconnect.apple.com) using your Apple ID user name and password.
2. Click My Apps.

   （原归档配图获取待重试：`MyAppsIcon_2x.png`）
3. Find the app in the list of apps or search for the app.

   If you don't see the app you are looking for on the My Apps page, you can search for the app using a variety of criteria. In the Search box, enter the criteria you want to use to search for an app. The view starts filtering the list of apps as soon as you start typing:

   - __Name.__ Enter the name or a portion of the name.
   - __Apple ID.__ Enter the Apple ID of the app. This value must match exactly to return an app.
   - __SKU.__ Enter the SKU of the app.

   If no apps are listed, then the criteria you type match no apps.
4. In the Search Results, click on the name of an app to open the App Details page.
5. Select Game Center.

   （原归档配图获取待重试：`AppDetails-menu-5_2x.png`）
6. If the app has been enabled for Game Center previously, the Game Center page opens.

   If this is the first time that this app has been configured for Game Center, you’re prompted to enable Game Center. Select one of these options:

   - Select “Enable for Single Game” if you’re configuring Game Center components specifically for this app.
   - Select “Enable for Group Games” if you want the Game Center components you configure to be used by more than one app.

   The appropriate Game Center page opens.

From this page you can configure Game Center components: [Leaderboards and Leaderboard Sets](Leaderboards%20and%20Leaderboard%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrnknltc), [Achievements](Achievements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmznknltc), and [Groups](Groups.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqnbnknltc).

## Enabling Game Center for Your App

You can enable your app for Game Center by going to the Game Center page. See [To go to your app’s Game Center page in iTunes Connect](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvooa).

From the Game Center page you configure all of the Game Center components used by your app. Enabling Game Center on this page allows this app to communicate with Game Center and adds Game Center metadata, as described in [Game Center Properties](Game%20Center%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrzfvjvomi), to the iTunes Connect record for the app.

To give your app access to configured components through Game Center, you also need to enable Game Center in the Game Center section on the Versions tab before you submit it for review.

## Disabling Game Center for Apps

Up until a version of your app is approved, you can disable Game Center for an app. This action disables Game Center for all versions. To disable Game Center for a specific version of the app, see [To disable a version of your app for Game Center](Distributing%20Game%20Center%20Apps.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrwfvjvomzy).

![bullet](attachments/Resources/1282/Images/task_2x.png)To disable your app for Game Center

1. Go to the Game Center page of your app, as described in [Navigating to Your App’s Game Center Page](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. In the Game Center section, click the toggle to disable Game Center.

[Next](Leaderboards%20and%20Leaderboard%20Sets.md)[Previous](Introduction.md)
