---
title: Game Center Configuration Guide for iTunes Connect
apple_id: TP40013726
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-10-02'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/iTunesConnectGameCenter_Guide/TestingYourApp/TestingYourApp.html
archived_at: '2026-07-27T06:57:08.925312Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Game Center Configuration Guide for iTunes Connect](Introduction.md)


[Next](Distributing%20Game%20Center%20Apps.md)[Previous](Groups.md)

# Testing Your App

Apple provides a nonproduction development environment for Game Center that you can use to test how your app interacts with Game Center. To use this environment, create Sandbox Tester accounts in iTunes Connect and log in to your game in your development environment using the test account. You can begin testing leaderboards and achievements without any additional setup even when your app belongs to a group. However, testing multiplayer compatibility requires some configuration in iTunes Connect.

For specific information about testing Game Center functionality, see Testing Your Game Center-Aware Game in _Game Center Programming Guide_.

__Important:__ You can test apps that use iOS and OS X seed software releases in the development environment but you can’t submit them to the App Store until the corresponding OS ships.

## Testing Game Center Functionality in Your App

Testing a Game Center-aware app involves the following steps:

1. Configure Game Center components for your app, as described in this document.
2. Enable specific leaderboards or achievements for the app version that’s ready to submit, as described in [To enable a version of your app for Game Center](Distributing%20Game%20Center%20Apps.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrwfvjvomrz).
3. Identify any additional apps that you want to be able to play with the app you’re testing, as described in [Configuring Multiplayer Compatibility Testing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrvfvjvoni).
4. Set up iTunes Connect Sandbox Tester accounts, as described in _iTunes Connect Developer Guide_.
5. Test your app following the guidelines in Testing Your Game Center-Aware Game in _Game Center Programming Guide_.
6. Clear leaderboard test data, as described in [Cleaning Up After Testing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrvfvjvomq).

## Configuring Multiplayer Compatibility Testing

Multiplayer compatibility settings determine which users running different versions of your app see their results together in Game Center. You access the multiplayer compatibility settings on Versions in the App Details page of your app.

If you’re testing multiple apps playing together, go to the Game Center section on Versions and add the apps you want to test to the multiplayer compatibility list. If you’re testing multiple versions of the same app, no additional configuration is required.

![bullet](attachments/Resources/1282/Images/task_2x.png)To allow one app to be compatible with other apps for testing

1. Go to the Game Center page of your app, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. Navigate to the Game Center section on Versions.

   （原归档配图获取待重试：`VersionsGCOn_2x.png`）
3. In the Game Center section, enable Game Center if it’s not already enabled.

   If you don’t see a Game Center section in the Version Details, this app isn’t enabled for Game Center. See [Accessing and Enabling Game Center Functionality](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvomi).
4. In the Multiplayer Compatibility section, click the plus sign.
5. Choose other apps you want this app to be compatible with from the Add pop-up menu (+) (located below the list of apps).

   （原归档配图获取待重试：`AddMPC_2x.png`）

   The Add pop-up menu (+) displays the icon, name and platform for each app you can add. (Only Game Center-enabled apps are shown.)
6. Click Done.

## Cleaning Up After Testing

After you complete testing leaderboards, make sure to remove the leaderboard test data before submitting the app.

![bullet](attachments/Resources/1282/Images/task_2x.png)To delete leaderboard test data

1. Go to the Game Center page of your app, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. In the Leaderboards section, click Delete Test Data.

   A request to Apple is submitted to delete your test data. Requests are usually processed within one day and can’t be restored.

   （原归档配图获取待重试：`gc_lb_delete_data_2x.png`）

[Next](Distributing%20Game%20Center%20Apps.md)[Previous](Groups.md)
