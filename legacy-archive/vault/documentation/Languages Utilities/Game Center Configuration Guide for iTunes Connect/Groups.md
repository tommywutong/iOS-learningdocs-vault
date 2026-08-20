---
title: Game Center Configuration Guide for iTunes Connect
apple_id: TP40013726
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-10-02'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/iTunesConnectGameCenter_Guide/Groups/Groups.html
archived_at: '2026-07-27T06:57:08.917668Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Game Center Configuration Guide for iTunes Connect](Introduction.md)


[Next](Testing%20Your%20App.md)[Previous](Achievements.md)

# Groups

In the context of Game Center, a _group_ is two or more apps that share leaderboards and achievements. Once an app is part of a group, it no longer has its own leaderboards or achievements: it participates in the leaderboards and achievements defined for the group.

You can define leaderboards and achievements for a group in two ways:

1. You can define leaderboards and achievements for individual apps; then when you move the app to a group, you specify how the app leaderboards and achievements are merged with the group leaderboards and achievements.
2. You can add an app to a group that already has leaderboards and achievements defined. The app will use the existing group leaderboards and apps.

Like apps, groups can organize leaderboards in sets. If a group uses leaderboard sets, apps you add to the group either already use leaderboard sets or can’t have any leaderboards defined.

When you’re ready to release a version of an app that’s part of a group, you determine which of the group leaderboards and achievements go live with the app. In addition, you set the app’s multiplayer compatibility options to include the other apps from the group. See [Turning On Game Center for the App Version](Distributing%20Game%20Center%20Apps.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrwfvjvomrq).

This chapter describes how to create a group in iTunes Connect, how to merge an app’s leaderboards and achievements into those of a group, and how to add to and manage groups.

## How Groups Work

There’s no restriction on the type of apps that can belong to a group, but an app can belong to only one group. For example, you can create a group containing iOS and Mac apps that share the same leaderboards and achievements. There’s no limit to the number of groups or to the number of apps that can belong to a group.

When you move an app that already has leaderboards or achievements to a group, iTunes Connect makes it easy to decide which of the app leaderboards and achievements to move to the group.

（原归档配图获取待重试：`gc_group_concepts_2x.png`）

## Creating Groups

A group can’t exist without containing at least one app, so you create a group by selecting an app and starting the group from the app.

### Creating New Groups

The following workflow for creating a new group differs depending on whether the app is already enabled for Game Center.

Refer to [Group Properties](Game%20Center%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrzfvjvomjt) when entering information about a group.

![bullet](attachments/Resources/1282/Images/task_2x.png)To create a new group

1. Go to the Game Center page of the app you want to use as the start of your group, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. Click Manage Game Center.
3. Add the app to a group.

   - If the app isn’t enabled for Game Center, click “Enable for Group Games.”

     （原归档配图获取待重试：`gc_grp_enable_grp_2x.png`）
   - If the app is enabled for Game Center but isn’t in a group, click “Move to Group.”

     （原归档配图获取待重试：`gc_grp_move_to_group_2x.png`）
4. On the Group page, in the Group Reference Name field, enter an internal name for the new group.
5. Click Create Group.
6. Review the IDs for leaderboards and achievements for the app that will be moved to the group.

   The leaderboards and achievements in this app become the leaderboards and achievements for the group. The IDs from the app are prepended with a `grp.` prefix. If you want, you can change the IDs to make them more appropriate for the group. The prefix can’t be changed.
7. Select “All changes are accurate.”
8. Click Save.
9. On the Game Center page for the app, click Save.

### Adding Apps to Groups

After you create a group, you can add other apps to the group. If the app and group have existing leaderboards and achievements, you need to decide whether to add or merge the app’s components with those in the group. Adding the leaderboard or achievement moves it to the group as it appears in the app. Merging the leaderboard or achievement replaces the version in the app with the one you choose from the group.

The options that iTunes Connect presents to you are dependent on your specific app and group data. You won’t see options for types of assets that the app doesn’t have.

__Important:__ If the group uses leaderboard sets, the app you add to the group must use leaderboard sets. See [Configuring Leaderboard Sets](Leaderboards%20and%20Leaderboard%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrnknltmny).

![bullet](attachments/Resources/1282/Images/task_2x.png)To add an app to an existing group

1. Go to the Game Center page of the app you want to include in the group, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).

   The app can’t already be in another group.
2. Click Manage Game Center.
3. Enable the app for the group.

   - If the app isn’t enabled for Game Center, click “Enable for Group Games.”
   - If the app is enabled for Game Center but isn’t in a group, click “Move to Group.”
4. In the Move to an Existing Group section, select a group in the table.

   If either the app or the group has leaderboard sets enabled, but the other doesn’t, you won’t be able to add this app to the group. See [To create the first leaderboard set](Leaderboards%20and%20Leaderboard%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrnknltmoa).
5. If the app includes combined leaderboards, you’re prompted to merge or add each to the group.

   There are limitations to how leaderboards can be merged, as described in [Rules for Moving Leaderboards](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqnbnknltina).

   - To add a combined leaderboard, click Add (if it’s shown). You can modify the provided Leaderboard ID if needed, except that you need to keep the `grp.` prefix.
   - To merge a combined leaderboard, click Merge and choose a compatible group leaderboard from the Select Group Leaderboard menu. Choose whether to merge or add its attached leaderboards.
6. If the app includes single leaderboards, you’re prompted to merge or add each to the group.

   Configure the leaderboards you want to merge first, and then configure the leaderboards you want to add.

   - To merge a leaderboard, click Merge and choose a compatible group leaderboard from the Select Group Leaderboard menu.
   - To add a leaderboard, click Add (if it’s shown). You can modify the provided Leaderboard ID if needed, except that you need to keep the `grp.` prefix.

   There are limitations to how leaderboards can be merged, as described in [Rules for Moving Leaderboards](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqnbnknltina).
7. If the app includes achievements, you’re prompted to merge or add each to the group.

   Configure the achievements you want to merge first, and then configure the achievements you want to add.

   - To merge an achievement, click Merge and choose a group achievement from the menu.
   - To add an achievement, click Add (if it’s shown). You can modify the provided Achievement ID if needed, except that you need to keep the `grp.` prefix.

   For more information about how achievements are moved to the group, see [Rules for Moving Achievements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqnbnknltkna).
8. Click Continue.
9. If the group uses leaderboard sets, decide whether you want to add the app’s sets to the group.

   Select “Add Set to Group” to keep the set in the group as it appears for the app. Otherwise, the set is merged with the leaderboard set listed in Matching Group Leaderboard Sets.
10. Click Continue.
11. Review the leaderboards and achievements that will move to the group.

    For example, in the Moved Leaderboards section, the first column displays the app’s leaderboards that are being added or merged with a corresponding group leaderboard displayed in the second column.
12. If you want to change the settings, click Go Back.
13. Otherwise, select “All changes are accurate.” and click Save.

## Moving App Data to Groups

The purpose of adding an app to a group is to share data, specifically to share leaderboards and achievements. When you add an app with existing Game Center assets to a group, you decide which of the app’s leaderboards and achievements are retained as part of the group. iTunes Connect guides you through this process by presenting only compatible assets and available options at each step.

After an app is added to a group, iTunes Connect no longer maintains the app’s single leaderboards and achievements.

There are no restrictions on adding leaderboards and achievements to groups or merging achievements. However, there are some constraints when merging leaderboards.

### Rules for Moving Leaderboards

When you move an app to a group, you determine what happens to each of the app’s leaderboards:

- __Add__ an app’s leaderboard to the leaderboards already defined for the group. The leaderboard appears in the group just as it did for the app.
- __Merge__ an app’s leaderboard with an existing leaderboard in the group. If the app’s leaderboard ranks the same information as one of the group leaderboards, you can choose to use the group’s leaderboard for the app.

The choices you have to merge leaderboards depend on the type of leaderboard, its property values, and your previous selections.

These are the rules for merging leaderboards:

- A leaderboard can only merge with a compatible leaderboard.

  Leaderboards are compatible if the values of the Score Format Type and Sort Order properties are the same.
- A combined leaderboard can only merge with a combined leaderboard.

  If a compatible combined leaderboard isn’t available, it needs to be added to the group.
- An attached leaderboard can merge with an attached leaderboard only if their combined (parent) leaderboards are also being merged with each other.
- An attached leaderboard can merge with a single leaderboard.

  The single leaderboard will be attached to the corresponding group combined leaderboard.
- A single leaderboard can merge with a single leaderboard.
- A single leaderboard can merge with an attached leaderboard.

（原归档配图获取待重试：`gc_group_lb_move_2x.png`）

After merging two leaderboards, all of the group’s leaderboard property values remain the same with the exception of these properties:

- __Score Range__ If the app’s score range is larger than the group’s, the group’s score range expands to include the app’s. For example, if the range of the app’s leaderboard is 1–500 and the range of the group’s leaderboard is 1–250, the range of the group’s leaderboard is set to 1–500.
- __Languages__ If the app has a language of the same type as the group, the group’s language is used. If the app has a language that the group doesn’t have, the app’s language is added to the group.

Leaderboards need to be moved in the order iTunes Connect presents them.

### Rules for Moving Achievements

There are no restrictions on adding achievements to a group. However, when merging achievements, the maximum number of points for each achievement is 100 and the total maximum number of points for all app achievements is 1000, but there are no restrictions on the total points for all group achievements. After the merge, the total number of points for the app is still enforced. When an app is added to a group, the points remaining count is no longer displayed on the App Summary page.

After the merge, all of the group’s achievement property values remain the same with the exception of the languages, which follow this rule:

- __Languages__ If the app has a language of the same type as the group, the group’s language is used. If the app has a language that the group doesn’t have, the app’s language is added to the group.

## Configuring Groups

After you create and add apps to a group, you can edit the group from the Game Center Groups page.

### Editing Group Properties

You use the same controls to edit group properties when you first create a group as you use later to edit an existing group.

![bullet](attachments/Resources/1282/Images/task_2x.png)To edit an existing group

1. In the Ellipsis Game Center menu "…" on the App Details page, click Game Center Groups.

   （原归档配图获取待重试：`EllipsesMenuGC_2x.png`）

   The Game Center Groups page opens.
2. In the Manage Existing Groups section, select the group you want to edit.

   The page for the group opens, which includes the group Reference Name, the apps that are part of the group, and the group’s leaderboards and achievements.

   （原归档配图获取待重试：`gc_grp_edit_group_2x.png`）
3. To change the reference name of the group, in the Reference Name section, click Edit.
4. To add another app to this group, exit this page and follow the steps in [To add an app to an existing group](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqnbnknltimi).
5. To add a leaderboard set to the group, in the Group Leaderboards section, click Add Leaderboard Set.

   Follow the same steps to create a leaderboard set for an app described in [To add a new leaderboard set](Leaderboards%20and%20Leaderboard%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrnknltmoi) except prepend the Leaderboard Set ID with the `grp.` prefix.
6. To change the default leaderboard of an app, click Edit in the Default Leaderboard column of the app’s row, select a new default leaderboard, and click Save.

   If there’s only one group leaderboard, you can’t change the default leaderboard; click Cancel.
7. To add a leaderboard to the group, in the Group Leaderboards section, click Add Leaderboard.

   Follow the same steps to create a leaderboard for an app described in [To configure a single leaderboard](Leaderboards%20and%20Leaderboard%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrnknltcna) except prepend the Leaderboard ID with the `grp.` prefix.
8. To add an achievement to the group, in the Group Achievements section, click Add Achievement.

   Follow the same steps to create an achievement for an app described in [To add an achievement](Achievements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmznknlteny) except prepend the Achievement ID with the `grp.` prefix.
9. Click Done.

### Creating Group Leaderboards and Achievements

You follow the same steps to create and edit group leaderboards and achievements as you do for app leaderboards and achievements, as described in [Configuring Leaderboards](Leaderboards%20and%20Leaderboard%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrnknltcnq) and [Configuring Achievements](Achievements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmznknltenq). You can also create combined leaderboards owned by a group, as described in [Configuring Combined Leaderboards](Leaderboards%20and%20Leaderboard%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrnknltcny).

### Removing an App from a Group

If an app hasn’t been reviewed and approved, you can remove it from a group. When you remove the last app from a group, the group is deleted.

![bullet](attachments/Resources/1282/Images/task_2x.png)To convert an app from a group game to a single game

1. Open the Game Center page for your app, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. Make the app into a single app.

   - If the app is the only app listed in the group, click Delete Group.

     （原归档配图获取待重试：`gc_grp_delete_2x.png`）
   - If the app is one of multiple apps listed in Apps in this Group, in the row for the app you want to remove from the group, click Delete.

When you need to submit a version of your app without groups and multiplayer compatibility enabled, you can submit a version of an app outside the group. An example is if you created a new binary that fixes a bug but isn’t ready to be released with groups or multiplayer compatibility. In this case, you would remove the app from the group and deselect versions of this app (and any other apps) from the multiplayer compatibility settings.

![bullet](attachments/Resources/1282/Images/task_2x.png)To release a version of an app outside of a group

1. Remove the app from the group, as described in [To convert an app from a group game to a single game](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqnbnknltg).
2. Remove any multiplayer compatibility settings defined for the app version, as described in [To allow one app to be compatible with other apps for testing](Testing%20Your%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrvfvjvomrr).

[Next](Testing%20Your%20App.md)[Previous](Achievements.md)
