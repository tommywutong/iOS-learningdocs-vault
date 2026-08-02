---
title: iOS Team Administration Guide
apple_id: TP40011159
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/DevPortalGuide/Introduction/Introduction.html
archived_at: '2026-07-18T02:08:48.090467Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Managing%20Your%20Team.md)

# About iOS Development Team Administration

iOS app development is a mix of coding and administrative tasks. Often, a team works together to develop an app. However, a single developer can perform all of the necessary tasks. This document describes the administrative tasks and is required reading for the team admin. Each team should designate someone to act as their team’s admin; an individual is automatically the team admin.

The [iOS Provisioning Portal](https://developer.apple.com/ios/manage/overview/index.action) is where you, the team admin, manage certificates and create profiles for developing, testing, and distributing your app. You can also authorize iOS devices for app development and testing.

You are responsible for coordinating with your team. The steps in this guide are presented in a logical order for most development teams. The tasks are divided into two main phases: development and distribution. During the development phase, you create a development provisioning profile so that your team can run your app on iOS devices specifically configured for development. It is important to test your app on actual devices, not just in the iOS Simulator. In the distribution phase, you create a distribution provisioning profile for your team so that you can distribute your app.

![A figure shows the ordered steps that a team admin performs. Step 1 is Create Your Team. This includes managing team members. Step 2 is Creating a Development Provisioning Profile which inclues three parts: an Apple UDID, iOS development certificates and app IDs. Step 3 is Creating a Distribution Provisioning Profile which includes iOS distribution certificates. Step 4, the last step, is Distributing an Application.](attachments/Art/intro.jpg)

### Team Admins Manage Team Membership and Assign Roles in the Member Center

The team admin is responsible for managing the development team by adding new members and assigning team roles. A developer can be a team agent, team admin, or a team member. Each development team has one team agent who is the primary contact for the team. A team with more than one member is required to have at least two team admins (including the team agent). The team agent and team admins are responsible for the configuration and provisioning of an app.

### Development Devices Must Be Registered in the iOS Provisioning Portal

To run an app on an iOS device during the app’s development stage, you must register the device in the iOS Provisioning Portal by adding its device ID. This device must also be specified as a development device.

### To Develop Apps, You Need a Development Certificate

In iOS development, apps must be [cryptographically signed](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/AppSigning.html#//apple_ref/doc/uid/TP40008195-CH63) before they can run on an iOS device. Each team member who wants to develop an app needs to have his or her own authorized development certificate. A team member requests a development certificate using Xcode but it is not created until the team admin approve the request.

### To Install an App on a Development Device, You Need a Development Provisioning Profile

To install an app on a device, you need three things:

- App ID that identifies the set of apps it authorizes to run.
- List of devices your team wants to use for testing.
- List of developers permitted to sign the app.

These three things are bundled in a development provisioning profile.

### To Distribute an App, You Need a Distribution Certificate and a Distribution Provisioning Profile

When your app is ready for distribution, the team admin creates a distribution certificate that your team uses to sign your app. This certificate must be included in a distribution provisioning profile. Similar to a development provisioning profile, a distribution provisioning profile bundles together the things you need to distribute your app: an app ID and your team’s distribution certificate. A distribution provisioning profile allows your app to run on nondevelopment iOS devices.

### Publish Your App to the App Store or Distribute on Your Own

You can submit your app to the App Store or distribute it to testers through ad hoc distribution. Or, if you are enrolled in the Enterprise Program, you can distribute your app in-house. Apps published in the App Store must go through the approval process before they are available to users.

This document is intended for both developers and nondevelopers. It is required reading for team admins (which includes the team agent).

This guide does not require familiarity with Xcode or that you be involved in any of the app programming.

If you have never used the iOS Provisioning Portal before, you should read this document in its entirety, starting with [Managing Your Team](Managing%20Your%20Team.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnjzfvbuqmrvfvjvomi).

If you have previously acted as your development team’s agent or admin, use this guide as a checklist, referencing the relevant chapters to learn about specific tasks.

This guide assumes that you, or your company, are already registered in the iOS Developer Program. If not, you can register at [http://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/). After you are registered, you have access to the [Member Center](https://developer.apple.com/membercenter/) and the [iOS Provisioning Portal](https://developer.apple.com/ios/manage/overview/index.action).

Before you read this guide, read _[Developing for the App Store](../../General/Developing%20for%20the%20App%20Store/About%20the%20Application%20Development%20Process.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobw)_ to understand all the steps you must perform to develop and distribute your apps.

If you are an individual developer, who is not using any of the specialized technologies that require an explicit app ID, read this tutorial to get started:

- _[App Store Submission Tutorial](../App%20Store%20Submission%20Tutorial/About%20Your%20First%20App%20Store%20Submission.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgnzv)_ teaches you the process of provisioning devices and submitting your iOS app to the App Store.

The following guides are intended for team members responsible for writing your app’s code:

- _App Distribution Guide_ explains how a team member obtains a development certificate and development provisioning profile using Xcode.
- _[Start Developing iOS Apps Today (Retired)](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/RoadMapiOS-Legacy/index.html#//apple_ref/doc/uid/TP40011343)_ is the starting point for learning how to create apps. It describes fundamental app architecture, explains coding processes, and gives tips for designing your app.
[Next](Managing%20Your%20Team.md)

