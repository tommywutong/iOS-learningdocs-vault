---
title: Game Center Configuration Guide for iTunes Connect
apple_id: TP40013726
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-10-02'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/iTunesConnectGameCenter_Guide/Leaderboards/Leaderboards.html
archived_at: '2026-07-27T06:57:08.881778Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Game Center Configuration Guide for iTunes Connect](Introduction.md)


[Next](Achievements.md)[Previous](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md)

# Leaderboards and Leaderboard Sets

For each leaderboard you add to your game, you use iTunes Connect to describe the scores it ranks and how it’s displayed.

（原归档配图获取待重试：`leaderboard_2x.png`）

For information about developing leaderboards in your game, see Leaderboards and Leaderboard Sets in _Game Center Programming Guide_.

In iTunes Connect, you configure:

- Single leaderboards
- Combined leaderboards
- Leaderboard sets
- Language support for leaderboards

## Creating Single Leaderboards

A single leaderboard allows players to compare their scores with the scores of other players in the same game. When you configure leaderboards in iTunes Connect, you specify details such as the scores to collect and how to order the scores. For each language you want the leaderboard to display in, you specify the leaderboard name, score format, and score unit. You can also include a localized image to illustrate the score in the leaderboard.

You can configure leaderboards for your app in iTunes Connect when the status of your app is anything other than In Review. You can’t delete a leaderboard after the leaderboard appears in a live version of the app.

Refer to [Leaderboard Properties](Game%20Center%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrzfvjvomjv) when entering information about a leaderboard.

![bullet](attachments/Resources/1282/Images/task_2x.png)To configure a single leaderboard

1. Go to the Game Center page of your app, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. If necessary, enable Game Center.
3. In the Leaderboards section, click Add Leaderboard.

   （原归档配图获取待重试：`gc_add_lb_2x.png`）
4. In the dialog that appears, select the option for a single leaderboard.

   The form that appears includes the leaderboard options described in [Leaderboard Properties](Game%20Center%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrzfvjvomjv).
5. In the Leaderboard Reference Name field, enter an internal name for the leaderboard.

   （原归档配图获取待重试：`gc_create_lb_2x.png`）

   When you add language support later, you’ll enter a localized name for the leaderboard that’s displayed to users.
6. In the Leaderboard ID field, enter an alphanumeric identifier for your leaderboard.

   The identifier can contain periods and underscores. It must be unique among leaderboard IDs for all apps in the organization.

   The Leaderboard ID is also called the _category_ in Game Kit. This value can’t be changed after the leaderboard is saved.
7. Choose a format from the Score Format Type menu.
8. Select either Best Score or Most Recent Score to indicate what type of score to save.
9. Select either “Low to High” or “High to Low” as the sort order for the scores.

   For example, set the Sort Order to “Low to High” for a score that shows the fastest times in a race.
10. If you want, enter a score range in the Score Range fields.

    This range describes the possible (legal) score values. If players report scores outside of this range, the scores are ignored.
11. Click Add Language to specify the text used to display the score.

    （原归档配图获取待重试：`gc_lb_add_lang_2x.png`）
12. In the dialog that appears, configure the display text, as described in [Configuring Leaderboard Languages](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrnknltemy).

    Repeat these steps for each language or region that the app supports.
13. Click Save.

    The new leaderboard appears in the list of leaderboards.

    （原归档配图获取待重试：`gc_add_lb_complete_2x.png`）

__Important:__ If you add a leaderboard to an app whose status is “Ready for Sale,” the leaderboard is automatically submitted for review the next time you submit a version of your app. If you don’t want to submit the leaderboard, you can change the default settings in the Game Center section on Versions of the App Details page, as described in [Distributing Game Center Apps](Distributing%20Game%20Center%20Apps.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrwfvjvomq).

## Configuring Leaderboards

When you have more than one leaderboard, you can:

- Change the default leaderboard
- Edit leaderboard properties
- Reorder how leaderboards are listed
- Delete leaderboards

For information about managing leaderboards that have been added to a group, see [Configuring Groups](Groups.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqnbnknltini).

The default leaderboard is the first leaderboard that the user sees in Game Center for the app. The first single leaderboard you create is automatically set as the default leaderboard.

![bullet](attachments/Resources/1282/Images/task_2x.png)To set the default leaderboard

1. Go to the Game Center page of your app, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. In the row of the leaderboard you want to be the default, select the Default option.

Depending on the state of your app, you may be limited in what leaderboard properties you can edit. Before you submit your app for review, you can change all leaderboard properties except the leaderboard ID. After you submit, most properties aren’t editable. Refer to [Leaderboard Properties](Game%20Center%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrzfvjvomjv) for details on what properties are editable.

![bullet](attachments/Resources/1282/Images/task_2x.png)To edit a leaderboard

1. Go to the Game Center page of your app, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. In the Leaderboards section, click the leaderboard you want to edit. (Click anywhere in the row.)
3. Change leaderboard properties as needed.

   The leaderboard properties are described in [Leaderboard Properties](Game%20Center%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrzfvjvomjv).

   （原归档配图获取待重试：`gc_edit_lb_2x.png`）
4. In the Leaderboard Localization section, select a language to change leaderboard display text for that language.

   See [Configuring Leaderboard Languages](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrnknltemy).
5. Click Save.

Leaderboards are presented to players in Game Center in the order they appear in iTunes Connect. You can change the order of the leaderboards on the app’s Game Center page.

![bullet](attachments/Resources/1282/Images/task_2x.png)To reorder leaderboards

1. Go to the Game Center page of your app, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. In the Leaderboards section, find the leaderboard you want to reorder.
3. Using the icon in the first column, drag the leaderboard to a new location in the table.

   （原归档配图获取待重试：`gc_lb_reorder_2x.png`）

The status of a leaderboard is displayed in the rightmost column of the Leaderboards table. The possible status values are described in [Leaderboard Statuses](Game%20Center%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrzfvjvomjy). If a Delete button appears in this column, the status is none of those values and the leaderboard can be deleted. After a leaderboard is available in Game Center, it can’t be deleted.

![bullet](attachments/Resources/1282/Images/task_2x.png)To delete a leaderboard

1. Go to the Game Center page of your app, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. In the Leaderboards section, find the leaderboard you want to delete.
3. In the Status column, click Delete.

   The Delete button appears and is enabled only if the leaderboard isn’t already in use in Game Center.
4. Click Delete to confirm.

## Configuring Leaderboard Languages

iTunes Connect provides configuration for leaderboard text separate from the configuration of the score itself. This allows you to repeat the text configuration for each language or region your app supports. You must provide at least one language configuration. Refer to [Leaderboard Language Properties](Game%20Center%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrzfvjvomjw) for more information about leaderboard language properties.

![bullet](attachments/Resources/1282/Images/task_2x.png)To add leaderboard display text

1. If you haven’t already created a leaderboard, do so as described in [To configure a single leaderboard](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrnknltcna).
2. In the Leaderboard Localization section of the Add Leaderboard page, click Add Language.

   （原归档配图获取待重试：`gc_lb_add_lang_2x.png`）
3. In the dialog that appears, choose a language from the Language menu.
4. In the Name field, enter a localized reference name for the leaderboard.

   For example, if you choose Finnish from the Language menu, enter the Finnish name for the leaderboard in the Name field.
5. Choose a localized score format from the Score Format menu.
6. If you want, in the Score Format Suffix field, enter a localized score suffix.

   If you want a space to appear between the score and the suffix, enter a space followed by the suffix text.

   （原归档配图获取待重试：`gc_add_lang_form_2x.png`）

   If Score Format Suffix Plural doesn’t appear, it’s not needed for the selected language.
7. If you want, click Choose File and select a localized image for the leaderboard.
8. Click Save.
9. Repeat these steps to add another language, or click Save to accept the changes to this leaderboard.

If the status of your app is anything other than In Review, you can edit the properties of a leaderboard language. Refer to [Leaderboard Language Properties](Game%20Center%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrzfvjvomjw) for which properties are editable when.

![bullet](attachments/Resources/1282/Images/task_2x.png)To edit a leaderboard language

1. Go to the Game Center page of your app, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. In the Leaderboards section, select the leaderboard that you want to edit.
3. On the page that opens, look for the Leaderboard Localization section and click the language that you want to edit.
4. In the dialog that appears, modify the properties of the leaderboard text in this language.

   See [Leaderboard Language Properties](Game%20Center%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrzfvjvomjw).
5. Click Save.
6. On the Edit Leaderboard page, click Save.

You can only delete a language if more than one language is listed in the Leaderboard Localization section of the Edit Leaderboard page.

![bullet](attachments/Resources/1282/Images/task_2x.png)To delete a leaderboard language

1. Go to the Game Center page of your app, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. In the Leaderboards section, select the leaderboard that you want to edit.
3. In the row of the language you want to remove, click Delete.
4. Click Delete to confirm.

## Configuring Combined Leaderboards

A combined leaderboard ranks player scores from multiple single leaderboards. For example, if you have a leaderboard for the lap times for each level of a race game, you can configure a combined leaderboard that ranks player scores across all levels of the game. You must have at least two single leaderboards before you can create a combined leaderboard. The leaderboards you are combining must have the same score format and sort order. Refer to [Leaderboard Properties](Game%20Center%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrzfvjvomjv) when entering information about a combined leaderboard.

（原归档配图获取待重试：`gc_lb_concept_2x.png`）

After you create a combined leaderboard, you manage it with the other leaderboards configured for the app. In the list of leaderboards, the type indicates that a leaderboard is combined; leaderboards that contributed to a combined leaderboard are listed as attached.

__Note:__ If you create a combined leaderboard after an app is available in the App Store, be aware that only new scores are displayed in the new combined leaderboard. Values collected previously in the child leaderboards aren’t shifted to the combined leaderboard.

Combined leaderboards are different from leaderboard sets. A combined leaderboard provides a single list of scores from multiple leaderboards; leaderboard sets simply organize leaderboards without affecting the content of the leaderboard. See [Configuring Leaderboard Sets](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrnknltmny).

![bullet](attachments/Resources/1282/Images/task_2x.png)To combine leaderboards

1. Go to the Game Center page of your app, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. If you haven’t already, create the single leaderboards you want to combine.

   Make sure the leaderboards you want to combine have the same score format and sort order. See [Creating Single Leaderboards](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrnknltiny).
3. In the Leaderboards section, click Add Leaderboard.
4. In the dialog that appears, select the combined leaderboard option.

   If Choose Combined Leaderboard is disabled, you need to create at least two single leaderboards before you can perform this action.
5. In the Leaderboard Reference Name field, enter a reference name for the combined leaderboard.

   You’ll enter the display name for the combined leaderboard later when you add language support.
6. In the Leaderboard ID field, enter an alphanumeric identifier for the combined leaderboard.

   The identifier can contain periods and underscores. It must be unique among leaderboard IDs for all apps in the organization.
7. In the Leaderboards to Combine section, select two or more leaderboards you want to combine.

   Only leaderboards with the same score format and sort order can be combined and appear enabled in this list. The list updates to show only the leaderboards that can be combined.

   （原归档配图获取待重试：`gc_lb_combine_2x.png`）
8. Click Add Language to specify the text used to display the combined leaderboard score.

   （原归档配图获取待重试：`gc_lb_add_lang_2x.png`）
9. In the dialog that appears, configure the display text, as described in [Configuring Leaderboard Languages](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrnknltemy).

   Repeat these steps for each language or region that the app supports.
10. Click Save.

    The new combined leaderboard appears in the list of leaderboards.

## Configuring Leaderboard Sets

Leaderboard sets organize several leaderboards into a single unit. For example, in a game that includes many levels, you could define a leaderboard set to organize the leaderboards for each level. Leaderboard sets provide you with a way to expand the number of leaderboards allowed per app: without leaderboard sets, each app can have a maximum of 100 leaderboards. With leaderboard sets, each app can have a maximum of 500 leaderboards arranged across as many as 100 leaderboard sets. A set can have a maximum of 100 leaderboards.

You must have at least one leaderboard for your app before you can create a leaderboard set. After you add leaderboard sets to your app, all future leaderboards that you configure for the app must be included in a leaderboard set.

iOS developers are able to create leaderboard sets starting with iOS 7. Leaderboard sets aren’t supported in OS X v10.9.

For more information about the use of leaderboard sets in your game, see Leaderboard Sets.

Leaderboard sets are different from combined leaderboards: a leaderboard set simply organizes existing leaderboards and does not affect the content of the individual leaderboards. A combined leaderboard is an additional leaderboard that ranks scores together from multiple leaderboards. See [Configuring Combined Leaderboards](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrnknltcny).

### Creating Leaderboard Sets

The process to start using leaderboard sets to organize your app’s leaderboards includes these steps:

- Create the first leaderboard set.
- Create additional leaderboard sets.
- Add new leaderboards directly into leaderboard sets.

When you create the first leaderboard set, iTunes Connect ensures that all existing leaderboards for the app are included in at least one leaderboard set. Just as you did for a leaderboard, a leaderboard set requires that you configure an internal name and ID and display text for each language the app supports.

![bullet](attachments/Resources/1282/Images/task_2x.png)To create the first leaderboard set

1. Go to the Game Center page of your app, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. In the Leaderboards section, click “Move All Leaderboards into Leaderboard Sets.”

   （原归档配图获取待重试：`gc_lb_sets_initial_move_2x.png`）
3. In the Leaderboard Set Reference Name field, enter an internal name for the leaderboard set.

   When you add language support, you’ll enter a localized name for the leaderboard that’s displayed to users.
4. In the Leaderboard Set ID field, enter an alphanumeric identifier for the leaderboard set.

   The identifier can contain periods and underscores. It must be unique among leaderboard IDs for all apps in the organization.
5. Click Continue.
6. On the Move Leaderboards Into Sets page, click “Add to Leaderboard Set.”

   （原归档配图获取待重试：`gc_lb_set_add_to_set_2x.png`）
7. In the Add Leaderboard to Set dialog, configure each leaderboard you want to include in this set.

   - Choose a leaderboard.
   - Choose a language.
   - Set the display name for the leaderboard in this language.
   - Click Save.（原归档配图获取待重试：`gc_lb_add_to_set_dialog_2x.png`）

   This is your opportunity to give the leaderboard a different name in the context of this leaderboard set. For example, a single leaderboard named “Level 1 Laps” can be named “Laps” when included in the leaderboard set for Level 1.

   Repeat for each leaderboard to include in this set.
8. Make sure that all leaderboards are included in sets.

   You can either:

   - Add leaderboards to existing sets by choosing a leaderboard set from the Leaderboard Set menu and clicking “Add to Leaderboard Set,” as described in steps 6 through 7.
   - Create additional leaderboard sets by clicking Add Leaderboard Set, as described in [To add a new leaderboard set](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrnknltmoi).
9. On the Move Leaderboards Into Sets page, click Add Language to specify the display name for the leaderboard set.
10. In the dialog that appears, select the language, display name, and image for the leaderboard set.
11. Click Save.
12. Repeat steps 9 through 11 for each language or region your app supports.
13. Click Save to accept the new leaderboard set configuration.

You can add new leaderboard sets to your app to further customize how your leaderboards are displayed. Each set provides you with the ability to specify how a particular leaderboard is displayed within the set. You can put the same leaderboard into more than one set and configure a different display name for the leaderboard within each set.

![bullet](attachments/Resources/1282/Images/task_2x.png)To add a new leaderboard set

1. Go to the Game Center page of your app, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. In the Leaderboards section, click Add Leaderboard Set.

   （原归档配图获取待重试：`gc_lb_set_add_set_redbox_2x.png`）
3. In the dialog that appears, in the Leaderboard Set Reference Name field, enter an internal name for the leaderboard set.

   When you add language support, you’ll enter a localized name for the leaderboard that’s displayed to users.
4. In the Leaderboard Set ID field, enter an alphanumeric identifier for the leaderboard set.

   The identifier can contain periods and underscores. It must be unique among leaderboard IDs for all apps in the organization.
5. Click “Add to Leaderboard Set” to add a leaderboard to the set.

   （原归档配图获取待重试：`gc_lb_set_add_new_redbox_2x.png`）
6. In the Add Leaderboard to Set dialog, configure each leaderboard you want to include in this set.

   - Choose a leaderboard.
   - Choose a language.
   - Set the display name for the leaderboard in this language.
   - Click Save.（原归档配图获取待重试：`gc_lb_add_to_set_dialog_2x.png`）

   This is your opportunity to give the leaderboard a different name in the context of this leaderboard set. For example, a single leaderboard named “Level 1 Laps” can be named “Laps” when included in the leaderboard set for Level 1.

   Repeat this step for each leaderboard to include in this set.
7. Review the order of the leaderboards in the set.

   The order that leaderboards appear in the table is the order they appear when displayed in Game Center.
8. On the Add Leaderboard Set page, click Add Language to configure at least one language the leaderboard set name will be displayed in.
9. In the dialog that appears, select the language, display name, and image for the leaderboard set.

   The Language and Display Name fields are required. The Image field is optional.
10. Click Save.
11. Repeat steps 8 through 10 to include support for additional languages.
12. Click Save to save the new leaderboard set configuration.

Creating a new leaderboard differs slightly after you start using leaderboard sets in your app. You must associate the new leaderboard with a leaderboard set before you can save the configuration.

![bullet](attachments/Resources/1282/Images/task_2x.png)To create a new leaderboard and add it to a leaderboard set

1. Create a new leaderboard following the steps in [To configure a single leaderboard](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrnknltcna).
2. On the Add Leaderboard page, click “Add to a Leaderboard Set.”

   This section of the page only appears after you’ve configured leaderboard sets for the app.

   （原归档配图获取待重试：`gc_lb_add_lb_to_set_2x.png`）
3. In the Add Leaderboard to Leaderboard Set dialog, select the leaderboard set.
4. Set the display language and name for this leaderboard when it appears in the leaderboard set.

   Repeat this step for each language or region the app supports.
5. Click Save.
6. In the Leaderboard Localization section, click Add Language to complete the configuration of the single leaderboard.

   See [To add leaderboard display text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrnknltemq).
7. Click Save.

You can reorder the leaderboard sets by dragging a set name to the desired location. Click the name of the leaderboard set to edit its contents or change the order of the leaderboards it contains.

（原归档配图获取待重试：`gc_lb_sets_reorder_2x.png`）

To see which leaderboards are included in which leaderboard sets, click “View Leaderboards in Leaderboard Sets.” The dialog shows all leaderboards defined for the app, by name and reference ID with checks to indicate in which sets each leaderboard appears.

（原归档配图获取待重试：`gc_lb_sets_matrix_2x.png`）

### Deleting Leaderboard Sets

Before you can delete a leaderboard set, you must make sure all leaderboards in the set are also in another set and then you must remove the leaderboards from the set you want to delete. You can’t remove a leaderboard from a leaderboard set unless that leaderboard is already in another set.

![bullet](attachments/Resources/1282/Images/task_2x.png)To delete a leaderboard set

1. Go to the Game Center page of your app, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).
2. Find the leaderboard set you want to delete.
3. Click the leaderboard set to open its configuration page.

   （原归档配图获取待重试：`gc_lb_sets_cursor_2x.png`）
4. In the Leaderboards in This Set section, click Remove for each leaderboard.

   （原归档配图获取待重试：`gc_lb_sets_remove_lb_2x.png`）
5. Click Done after removing all of the associated leaderboards.
6. Back on the Game Center page, click Delete to remove the leaderboard set.

   （原归档配图获取待重试：`gc_lb_sets_delete_2x.png`）
7. Click Delete to confirm.

If your app contains 100 leaderboards or fewer, you can click “Remove All Leaderboards in Leaderboard Sets” and all of your current leaderboard sets are deleted. This option doesn’t appear for apps with over 100 leaderboards. You must remove any leaderboards over 100 before you can use the “Remove All Leaderboards in Leaderboard Sets” button.

### Merging Leaderboard Sets into a Group’s Leaderboard Sets

Merging games into a group provides a way to share leaderboards and achievements across multiple games. Each game is still limited to 500 leaderboards and 100 leaderboard sets. However, the total number of leaderboards and leaderboard sets in a group can surpass these numbers. Each group can have a maximum of 500 leaderboards and 100 leaderboard sets multiplied by the number of games in the group. For example, a group with three games can have a total of 1500 leaderboards and 300 leaderboard sets in the group. For information about creating and managing groups, see [Groups](Groups.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqnbnknltc).

You merge games into a group one at a time. A single game that has leaderboard sets can only be merged into a game group if one of the following two conditions applies:

- The group already uses leaderboard sets.
- You’re creating a new group starting with this game.

You can’t merge a game without leaderboard sets into a group with leaderboard sets. You have to add leaderboard sets to the single game before merging it into the existing group.

Similarly, you can’t merge a game with leaderboard sets into an existing group without leaderboard sets. You first have to move all of the group leaderboards into leaderboard sets before you can merge the single game into the group.

![bullet](attachments/Resources/1282/Images/task_2x.png)To convert all leaderboards used by a group into leaderboard sets

1. Go to the Game Center page of one of the apps in the group, as described in [Navigating to Your App’s Game Center Page](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvonrv).

   Because the app is part of a group, the page that appears describes Game Center options for the group.
2. In the Group Leaderboards section, click “Move All Leaderboards into Leaderboard Sets.”
3. In the dialog that appears, enter information for the first new leaderboard set.

   - In the Leaderboard Set Reference Name field, enter an internal name for the leaderboard set.
   - In the Leaderboard Set ID field, enter an alphanumeric identifier for the leaderboard set.

     The Set ID of each leaderboard and leaderboard set is automatically prefaced with the `grp.` prefix when the game is part of a group. You can change the leaderboard and leaderboard set Set IDs but must keep the `grp.` prefix in the new name. These IDs must be unique among leaderboard IDs across all apps in the organization.
4. Click Continue to open the Move Leaderboards into Sets page.

   On this page you can do the following:

   - Click Add Leaderboard Set to create an additional leaderboard set for the group, as described in step 3.
   - Click “Add to Leaderboard Set” to add leaderboards to the set selected at the top of the page.

     You’re prompted to select the leaderboard and specify the display name used for this leaderboard in the set. Specify the display name for each language or region your app supports.
   - Click Add Language to specify the display name for the leaderboard set selected at the top of the page.

     You’re prompted to specify the display name used for this leaderboard set. Specify the display name for each language or region your app supports. You can also provide an image for the leaderboard set for each language.
5. When you’ve assigned all leaderboards in the group to one or more leaderboard sets, click Save.

## Bulk Uploading Leaderboard Metadata to iTunes Connect

If you have many leaderboards to configure in iTunes Connect, you can deliver leaderboard and other iTunes Connect configuration metadata in batch in an App Store package using Transporter. See _App Metadata Specification_ and _Transporter Quick Start Guide_. These documents are available to iTunes Connect users within Resources and Help.

（原归档配图获取待重试：`ResourcesAndHelpIcon_2x.png`）

[Next](Achievements.md)[Previous](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md)
