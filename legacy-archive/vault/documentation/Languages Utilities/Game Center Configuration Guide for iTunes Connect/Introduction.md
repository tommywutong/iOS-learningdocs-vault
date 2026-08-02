---
title: Game Center Configuration Guide for iTunes Connect
apple_id: TP40013726
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-10-02'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/iTunesConnectGameCenter_Guide/Introduction/Introduction.html
archived_at: '2026-07-27T06:57:08.838551Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md)

# Introduction

Game Center is an Apple network service that provides social gaming functionality to games. To support many of the Game Center features, you provide information about your app to the Apple service: information such as the text and images to display in Game Center and how to manage data collected from players. To provide this information to the Game Center servers, you create an iTunes Connect record and add the Game Center configuration details to it. This document describes how to add Game Center configuration information into an existing iTunes Connect record for an app.

You’re ready to add Game Center configuration information in iTunes Connect after you’ve started developing the app and designing its social gaming features and before you’ve tested these features in Game Center.

（原归档配图获取待重试：`gc_flow_big_picture_2x.png`）

When developing a game, you may well develop, design, configure, and test Game Center components in parallel rather than implement each step completely before moving on to the next.

If you aren’t already familiar with Game Center functionality, read _[Game Center Programming Guide](../../Networking%20Internet/Game%20Center%20Programming%20Guide/About%20Game%20Center.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmbu)_ before this document. If you aren’t already familiar with iTunes Connect, read _iTunes Connect Developer Guide_ before this document.

## At a Glance

The process involved in using iTunes Connect to configure Game Center components for your app includes enabling Game Center features, configuring Game Center components, and associating the Game Center features with the version of the app you’re submitting to the store.

（原归档配图获取待重试：`gc_flow_detail_2x.png`）

### Game Center Configuration in iTunes Connect

You enable Game Center and configure Game Center components for all versions of an app. When you’re ready to submit a version of an app to the store, you associate specific Game Center components with that app version. In this way you can configure a superset of Game Center components and then make them available gradually in successive versions of an app.

__Related Chapters:__ [Accessing and Enabling Game Center Functionality](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmryfvjvomi), [Distributing Game Center Apps](Distributing%20Game%20Center%20Apps.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrwfvjvomq)

### Game Center Components

As you configure Game Center features in iTunes Connect, you’ll encounter the following terms that describe Game Center components:

- __Leaderboards__ collect and rank player scores from your game in Game Center. You use iTunes Connect to configure the scores Game Center collects, how they’re ranked, and how they’re displayed in each language your app supports.
- __Leaderboard sets__ organize a game’s leaderboards such that the 100 leaderboard limit per game is expanded to allow 500 leaderboard organized in as many as 100 leaderboard sets.
- __Achievements__ list accomplishments players reach in your game. You use iTunes Connect to configure the achievements Game Center collects and how achievements are displayed in each language your app supports.
- __Game groups__ let you define leaderboards and achievements to rank players from multiple games—such as games from different platforms or pay levels. When adding apps to an existing group in iTunes Connect, you decide which leaderboards and achievements from individual games are used by the group.
- __Multiplayer compatibility lists__ identify the games and versions of games that can play together. You configure these lists in iTunes Connect.

Game Center includes other features such as Matchmaking and Challenges that don’t have corresponding iTunes Connect configurations.

__Related Chapters:__ [Leaderboards and Leaderboard Sets](Leaderboards%20and%20Leaderboard%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrnknltc), [Achievements](Achievements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmznknltc), [Groups](Groups.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqnbnknltc)

### Testing Game Center with Your App

Testing Game Center functionality requires access to the Game Center service before your game is available to users. In iTunes Connect, you can create test user accounts that allow development versions of your game to use Game Center. Don’t forget to delete scores from these test accounts before your game is posted to the store.

__Related Chapters:__ [Testing Your App](Testing%20Your%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztomrwfvbuqmrvfvjvomi)

### Importing Game Center Metadata

You can configure many Game Center components and deliver the metadata in an App Store package using Transporter. See _App Metadata Specification_ and _Transporter Quick Start Guide_. These documents are available to iTunes Connect users in the Resources and Help section.

（原归档配图获取待重试：`ResourcesAndHelp_2x.png`）

## How to Use This Document

Use this document to augment the instructions provided in iTunes Connect.

## Prerequisites

This document assumes that you’re developing a Game Center-aware game and you’ve already:

- Started the design of your Game Center functionality, as described in _[Game Center Programming Guide](../../Networking%20Internet/Game%20Center%20Programming%20Guide/About%20Game%20Center.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmbu)_.
- Created an iTunes Connect record for the app, as described in Creating an iTunes Connect Record for an App in _iTunes Connect Developer Guide_.

## See Also

This document describes Game Center-specific features of iTunes Connect. For information about the broader surrounding concepts and tasks, see the following documents:

- Adding Capabilities in _App Distribution Guide_ explains how to use Xcode to enable Apple services such as Game Center.
- _[Game Center Programming Guide](../../Networking%20Internet/Game%20Center%20Programming%20Guide/About%20Game%20Center.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmbu)_ contains the information you need to develop a Game Center-aware game and to prepare to use iTunes Connect to configure Game Center functionality. In particular, [Creating and Managing Game Center Resources](../../Networking%20Internet/Game%20Center%20Programming%20Guide/Developing%20a%20Game%20Center-Aware%20Game.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmbufvbuqnjnknltema) in _[Game Center Programming Guide](../../Networking%20Internet/Game%20Center%20Programming%20Guide/About%20Game%20Center.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmbu)_ describes what you’re trying to accomplish with your iTunes Connect configuration.
- _iTunes Connect Developer Guide_ contains general information about creating an iTunes Connect record for your app to submit it to the App Store or the Mac App Store. In addition, this document describes other steps you’ll need to complete to prepare to market your app—including setting up your organization’s contracts and banking information, and submitting app metadata—including artwork and localization information. It continues with information on how to monitor your app’s success and what to do if you discover potentially fraudulent leaderboard scores.

Look for links to additional documents on more specific topics throughout this document.

[Next](Accessing%20and%20Enabling%20Game%20Center%20Functionality.md)
