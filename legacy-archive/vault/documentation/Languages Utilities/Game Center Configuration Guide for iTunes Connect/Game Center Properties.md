---
title: Game Center Configuration Guide for iTunes Connect
apple_id: TP40013726
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-10-02'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/iTunesConnectGameCenter_Guide/GameCenterProperties/GameCenterProperties.html
archived_at: '2026-07-27T06:57:08.955455Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Game Center Configuration Guide for iTunes Connect](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Distributing%20Game%20Center%20Apps.md)

# Game Center Properties

This appendix describes the metadata that iTunes Connect collects to configure the interface between a version of your game and Game Center and to display leaderboards and achievements in Game Center.

## Leaderboards

Leaderboard metadata identify each leaderboard in iTunes Connect, describe its scores, and collect language-specific text used in leaderboard display. iTunes Connect tracks metadata for the type of leaderboard and displays a status indicating whether the leaderboard has been approved and made live with the app.

Set these properties in the Leaderboard section of the Game Center page for an app, as described in [Leaderboards and Leaderboard Sets](Leaderboards%20and%20Leaderboard%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrnknltc).

### Leaderboard Properties

The main leaderboard properties identify each leaderboard in iTunes Connect and describe how the scores are organized and formatted.

| Property | Description | Can Be Edited |
| --- | --- | --- |
| Leaderboard Reference Name | An internal name that you must provide for each leaderboard. This is the name that you use if you search for your leaderboard in iTunes Connect. | - Prior to binary being approved - Developer Rejected status - Rejected status - After one binary is approved |
| Leaderboard ID | An alphanumeric identifier you choose for your leaderboard. This ID is limited to 100 characters (assumes single-byte characters). Note that the leaderboard ID is equivalent to the “category” in Game Kit API. Your leaderboard ID is a permanent setting and therefore can’t be edited at a later date. | Not editable after the binary is submitted |
| Score Format Type | The type of format in which you want scores for this app to be expressed in your leaderboard—for example, integer, elapsed time, or money. | - Prior to binary being approved - Developer Rejected status - Rejected status |
| Score Submission Type | The score from players to display in the leaderboard: Best Score or Most Recent Score. | - Prior to binary being approved - Developer Rejected status - Rejected status |
| Sort Order | The order of the score: choose between “Low to High” and “High to Low.” Choose “Low to High” if you want lowest scores displayed first. Choose “High to Low” if you want highest scores displayed first. | - Prior to binary being approved - Developer Rejected status - Rejected status |
| Score Range | The score range using 64-bit signed integers. The values must be between the long min (-2^63) and long max (2^63 - 1). Any scores outside of this range are deleted. Score range values are optional, but if they’re added, both values must be set and they must not be equal. When first adding a score range, or when changing it in the future to a smaller range that will restrict data, all data outside of the range is lost and can’t be recovered. | - Prior to binary being approved - Developer Rejected status - Rejected status - After one binary is approved |

### Leaderboard Language Properties

Leaderboard language properties collect language-specific text used in leaderboard display. You must include these properties for at least one language.

| Property | Description | Can Be Edited |
| --- | --- | --- |
| Language | This language is the one in which your leaderboard will appear. | - Prior to binary being approved - Developer Rejected status - Rejected status - After one binary is approved   There must be at least one language defined. The last language can’t be deleted. |
| Name | The reference name of the leaderboard in the specified language. | - Prior to binary being approved - Developer Rejected status - Rejected status - After one binary is approved |
| Score Format | This format determines how your scores are displayed on your leaderboard for the specified language. For example, if your app is scored with money, you may want to specify different types of money based on the language you select. The values in this menu reflect the Score Format Type for the leaderboard. | - Prior to binary being approved - Developer Rejected status - Rejected status - After one binary is approved |
| Score Format Suffix (Singular) | This suffix is added to the end of scores displayed in the singular form. This suffix is optional but is useful for clarifying the type of score stored in the leaderboard. Examples include “point,” “coin,” and “hit.” | - Prior to binary being approved - Developer Rejected status - Rejected status - After one binary is approved |
| Score Format Suffix (Plural) | This suffix is added to the end of scores displayed in the plural form. This suffix is optional but is useful for clarifying the type of score stored in the leaderboard. Examples include “points,” “coins,” and “hits.” | - Prior to binary being approved - Developer Rejected status - Rejected status - After one binary is approved |
| Image | A localized image that represents the leaderboard. The image must be a `.jpeg`, `.jpg`, `.tif`, `.tiff`, or `.png` file that’s 512 x 512 or 1024 x 1024 pixels, at least 72 dpi, and in the RGB color space. This property is optional. | - Prior to binary being approved - Developer Rejected status - Rejected status - After one binary is approved |

### Leaderboard Types

iTunes Connect tracks metadata for the type of leaderboard, which determines which scores are included in the leaderboard.

| Type | Description |
| --- | --- |
| Single | A single leaderboard that isn’t combined with other leaderboards. |
| Combined | A leaderboard that combines and ranks together the players’ scores from multiple single leaderboards. |
| Attached | A single leaderboard that’s combined with other leaderboards—the attached child of a combined leaderboard. |

### Leaderboard Statuses

Leaderboard statuses indicate whether the leaderboard has been approved and made live with the app.

| Status | Description |
| --- | --- |
| In Review | The leaderboard was submitted to Apple for review. |
| Live | The leaderboard was approved with the app. |
| Not Live | The leaderboard was previously Live for an app but has since been moved to a group and hasn’t been approved for the group yet. Only applicable to leaderboards added to a group. |

## Achievements

Achievement metadata identify each achievement and its behavior in iTunes Connect and collect the language-specific text used in achievement display. iTunes Connect also tracks a status to indicate whether the achievement has been approved and made live with the app.

Set these properties in the Achievements section of the Game Center page for an app, as described in [Achievements](Achievements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmznknltc).

### Achievement Properties

The main achievement properties identify each achievement in iTunes Connect and describe how the achievement behaves.

| Property | Description | Can Be Edited |
| --- | --- | --- |
| Achievement Reference Name | An internal name that you must provide for each achievement. This is the name you use if you search for the achievement within iTunes Connect. | - Prior to binary being approved - Developer Rejected status - Rejected status - After one binary is approved |
| Achievement ID | A chosen alphanumeric identifier for your achievement. This ID is limited to 100 characters (assumes single-byte characters). Your Achievement ID is a permanent setting and therefore can’t be edited at a later date. | Not editable after the achievement is saved |
| Point Value | The points that your achievement is worth. There is a maximum of 100 points per achievement and a maximum of 1000 points total for all achievements. | - Prior to binary being approved - Developer Rejected status - Rejected status |
| Hidden | Achievements marked as Hidden remain hidden in Game Center until a player has achieved them. | - Prior to binary being approved - Developer Rejected status - Rejected status - After one binary is approved |
| Achievable More Than Once | An indication of whether the player can earn the achievement multiple times. | - Prior to binary being approved - Developer Rejected status - Rejected status - After one binary is approved |

### Achievement Language Properties

Achievement language properties collect language-specific text used in achievement display. You must include these properties for at least one language.

| Property | Description | Can Be Edited |
| --- | --- | --- |
| Language | The language in which you’d like this achievement to appear. | - Prior to binary being approved - Developer Rejected status - Rejected status - After one binary is approved   There must be at least one language defined. The last language can’t be deleted. |
| Title | The localized title of this achievement as you’d like it to appear in Game Center. | - Prior to binary being approved - Developer Rejected status - Rejected status - After one binary is approved |
| Pre-earned Description | The description of your achievement as it appears to Game Center users before they earn it. | - Prior to binary being approved - Developer Rejected status - Rejected status - After one binary is approved |
| Earned Description | The description of your achievement as it appears to Game Center users after they earn it. | - Prior to binary being approved - Developer Rejected status - Rejected status - After one binary is approved |
| Image | A localized image that represents the achievement. The image must be a `.jpeg`, `.jpg`, `.tif`, `.tiff`, or `.png` file that’s 512 x 512 or 1024 x 1024 pixels, at least 72 dpi, and in the RGB color space. This property is required. | - Prior to binary being approved - Developer Rejected status - Rejected status - After one binary is approved |

### Achievement Statuses

Achievement statuses indicate whether the achievement has been approved and made live with the app.

| Status | Description |
| --- | --- |
| In Review | The achievement was submitted to Apple for review. |
| Live | The achievement was approved with the app. |
| Not Live | The achievement was previously Live for an app but has since been moved to a group and hasn’t been approved for the group yet. Only applicable to achievements added to a group. |

## Group Properties

Group properties identify the apps, leaderboards, and achievements that are included in a group. Set these properties on the Game Center page for the app, as described in [Groups](Groups.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqnbnknltc).

| Property | Description |
| --- | --- |
| Reference Name | An internal name that you must provide for each group. This is the name you see in iTunes Connect. |
| Apps in this Group | The apps attached to this group. |
| Group Leaderboards | The shared leaderboards for this group. |
| Group Achievements | The shared achievements for this group. |
| Default Leaderboard | The leaderboard that’s displayed by default in your app. |

## App Versions

App version properties allow iTunes Connect to track which Game Center properties apply to a specific app version. Your choices in the Game Center section on Versions, as described in [Turning On Game Center for the App Version](Distributing%20Game%20Center%20Apps.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrwfvjvomrq), set these metadata properties.

| Property | Description |
| --- | --- |
| leaderboards | A leaderboard displays the top scores of all Game Center users who play your app. You can’t remove a leaderboard that’s in use in Game Center for any version of your app. Each app can have a maximum of 100 leaderboards. Leaderboards are optional. |
| achievements | An achievement is a distinction that a player earns for reaching a milestone, or performing an action, defined by your app. You can’t delete an achievement that’s in use in Game Center for any version of your app. Achievements are optional. |

[Next](Document%20Revision%20History.md)[Previous](Distributing%20Game%20Center%20Apps.md)
