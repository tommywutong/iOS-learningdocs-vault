---
title: Game Center Configuration Guide for iTunes Connect
apple_id: TP40013726
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-10-02'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/iTunesConnectGameCenter_Guide/Achievements/Achievements.html
archived_at: '2026-07-27T06:57:08.899069Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Game Center Configuration Guide for iTunes Connect](Introduction.md)


[Next](Groups.md)[Previous](Leaderboards%20and%20Leaderboard%20Sets.md)

# Achievements

For each achievement you add to your game, you use iTunes Connect to enter the data Game Center needs to display achievements to players. See [Achievements](../../Networking%20Internet/Game%20Center%20Programming%20Guide/Leaderboards%2C%20Achievements%2C%20and%20Challenges.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmbufvbuqny) in _Game Center Programming Guide_ for design and development information.

（原归档配图获取待重试：`achievement_2x.png`）

## Creating Achievements

When you configure achievements in iTunes Connect, you specify details about the achievement, such as the points earned, whether the achievement is hidden from players before they reach its goal, and whether players can earn the achievement more than once. For each language or region you want the achievement to display in, you also specify the achievement name and messages for before and after players earn the achievement. You also specify an image to represent the achievement. You can create up to 100 achievements per app.

You can configure achievements for your app in iTunes Connect when the status of your app is anything other than In Review.

__Note:__ After an achievement is available to players for any version of your app, it can’t be deleted.

Refer to [Achievement Properties](Game%20Center%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrzfvjvomjz) when entering information about an achievement.

![bullet](attachments/Resources/1282/Images/task_2x.png)To add an achievement

1. Go to the Game Center page of your app, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. If necessary, enable Game Center.
3. In the Achievements section, click Add Achievement.

   （原归档配图获取待重试：`gc_add_achievement_2x.png`）

   The form that appears includes the Achievement options described in [Achievement Properties](Game%20Center%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrzfvjvomjz).
4. In the Achievement Reference Name field, enter an internal reference name for the achievement.
5. In the Achievement ID field, enter an alphanumeric identifier.

   The identifier can contain periods and underscores. It must be unique among achievement IDs for all apps in the organization.
6. In the Point Value field, enter the amount of points the achievement is worth.

   The remaining points are displayed below this field. The maximum number of points allowed for all achievements in the app is 1000.
7. Select Yes for Hidden if you want the achievement to be hidden until the user earns it; otherwise, select No.
8. Select Yes for Achievable More Than Once if the user can earn the achievement multiple times; otherwise, select No.
9. Click Add Language to specify the text used to display the achievement.

   For each language or region the app supports, repeat the steps described in [To add an achievement language](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmznknlteoa).

   （原归档配图获取待重试：`gc_ach_add_filled_2x.png`）
10. Click Save.

## Configuring Achievements

You can modify any of your app’s achievement properties until you submit the app for review. After your app is submitted, you can no longer edit the Achievement ID. After an achievement is available to players for any version of your app, it can’t be deleted and the point value can’t be changed.

For information about managing achievements that have been added to a group, see [Moving App Data to Groups](Groups.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqnbnknltima) and [Configuring Groups](Groups.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqnbnknltini).

Refer to [Achievement Properties](Game%20Center%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrzfvjvomjz) when entering information about an achievement. Refer to [Achievement Statuses](Game%20Center%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrzfvjvomrr) for the meaning of achievement statuses.

![bullet](attachments/Resources/1282/Images/task_2x.png)To edit an achievement

1. Go to the Game Center page of your app, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. In the Achievements section, click the achievement you want to edit (click anywhere in the row).
3. Edit achievement properties as needed.

   The properties are described in [Achievement Properties](Game%20Center%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrzfvjvomjz).
4. Click Save.

Achievements are presented to players in Game Center in the order they appear in iTunes Connect. You can change the order of the achievements on the app’s Game Center page.

![bullet](attachments/Resources/1282/Images/task_2x.png)To reorder an achievement

1. Go to the Game Center page of your app, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. In the Achievements section, find the achievement you want to reorder.
3. Using the icon in the first column, drag the achievement to a new location in the table.

   （原归档配图获取待重试：`gc_ach_reorder_2x.png`）

The status of an achievement is displayed in the rightmost column of the Achievements table. The possible status values are described in [Achievement Statuses](Game%20Center%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrzfvjvomrr). If a Delete button appears in this column, the status is none of those values and the achievement can be deleted.

![bullet](attachments/Resources/1282/Images/task_2x.png)To delete an achievement

1. Go to the Game Center page of your app, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. In the Achievements section, find the achievement you want to delete.
3. In the Status column, click Delete.

   The Delete button appears and is enabled only if you can delete the achievement.
4. In the dialog that appears, click Delete.

## Configuring Achievement Languages

Because you need to be able to configure achievement descriptions and images for each language that the app supports, these values are included as part of the language configuration. To include achievement descriptions, you need to add at least one language when you create an achievement. If your app is available in multiple countries, you should localize your achievements. Refer to [Achievement Language Properties](Game%20Center%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrzfvjvomrq) when localizing an achievement.

![bullet](attachments/Resources/1282/Images/task_2x.png)To add an achievement language

1. Go to the Game Center page of your app, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. In the Achievements section, click the achievement you want to edit (click anywhere in the row).
3. In the Achievement Localization section, click Add Language.
4. Choose a language from the Language menu.
5. In the Title field, enter a localized name for the achievement.
6. In the Pre-earned Description field, enter a localized description of the achievement.
7. In the Earned Description field, enter a localized description of the achievement.
8. Click Choose File and select a localized image for the achievement.

   （原归档配图获取待重试：`gc_ach_lang_2x.png`）
9. Click Save.
10. On the Add Achievement (or Edit Achievement) page, click Save.

If the status of your app is anything other than In Review, you can edit the properties of an achievement language.

![bullet](attachments/Resources/1282/Images/task_2x.png)To edit an achievement language

1. Go to the Game Center page of the app, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. In the Achievements section, select the achievement you want to edit.
3. In the Achievement Localization section, click the language that you want to edit (click anywhere in the row).
4. In the dialog that appears, modify the properties.
5. Click Save.
6. On the Edit Achievement page, click Save.

You can only delete an achievement language if you have more than one configured.

![bullet](attachments/Resources/1282/Images/task_2x.png)To delete an achievement language

1. Go to the Game Center page of the app, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. In the Achievements section, select the achievement you want to edit.
3. On the Edit Achievement page, find the language you want to delete in the Achievement Localization section.
4. In the last column of the language you want to delete, click Delete.
5. In the dialog that appears, click Delete.
6. On the Edit Achievement page, click Save.

## Bulk Uploading Achievement Metadata to iTunes Connect

If you have many achievements to configure in iTunes Connect, you can deliver achievement and other iTunes Connect configuration metadata in an App Store package using Transporter. See _App Metadata Specification_ and _Transporter Quick Start Guide_. These documents are available to iTunes Connect users within Resources and Help.

（原归档配图未能恢复：`ResourcesAndHelpIcon_2x.png`）

[Next](Groups.md)[Previous](Leaderboards%20and%20Leaderboard%20Sets.md)
