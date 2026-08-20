---
title: 'Your Second iOS App: Storyboards'
apple_id: TP40011318
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/SecondiOSAppTutorial/NextSteps/NextSteps.html
archived_at: '2026-07-18T02:28:01.879138Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Your Second iOS App: Storyboards](About%20Creating%20Your%20Second%20iOS%20App.md)


[Next](Code%20Listings.md)[Previous](Troubleshooting.md)

# Next Steps

In this tutorial, you created a simple but functional app. To build on the knowledge you gained, consider extending the BirdWatching app in some of the ways described in this chapter.

To meet the high expectations of iOS users, an app must have a great user interface and user experience. Although it’s usually best to avoid adding excessive decoration, the BirdWatching app might look better if it displayed coloring or even a subtle image in some of the view backgrounds.

iOS users generally expect to be able to use iOS-based devices in any orientation, so it’s a good idea to support different orientations in the apps you develop. As you update the app’s UI, be sure to define constraints that help UI elements remain properly positioned when the device is rotated.

Although the BirdWatching app makes it easy to add a new bird-sighting event, the user experience isn’t ideal. For one thing, the Done button is active as soon as the add scene appears; it would be better if it became active after the user taps a key on the keyboard. In addition, the text fields don’t provide a Clear button that allows users to quickly erase their input.

The best iOS apps include just the right amount of functionality to make it easy and enjoyable for users to accomplish the main task. The BirdWatching app makes it easy to perform the main task, but it could be more enjoyable to use. Here are a few improvements to consider:

- Instead of asking users to enter a bird name in a text field, display a list of bird names from which they can choose.
- Allow users to enter a specific date, rather than automatically using today’s date.
- Ask users to enable Location Services so that the app can suggest the current location as the bird-sighting location. And instead of asking users to enter a location in a text field, display a map on which they can select a location.
- Let users edit and sort the master list. For some advice on how to enable these actions, see _[Table View Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/TableView_iPhone/AboutTableViewsiPhone/AboutTableViewsiPhone.html#//apple_ref/doc/uid/TP40007451)_. And recall that the Master-Detail template provides an Edit button (and some support for rearranging the table) by default. You might start on this task by removing the comment symbols around the appropriate code in `BirdsMasterViewController.m`.
- Allow users to add an image to a bird sighting. The app could let users choose from a set of stock images or from their own photos.
- Make the master list persistent so that users’s bird sightings are displayed every time they restart the app.
- Adopt iCloud storage. When you support iCloud, changes that users make in one instance of an app are automatically propagated to their other devices, so that other instances of the app can see them, too. To get started learning how to enable iCloud in an app, see _[Your Third iOS App: iCloud](../../General/Your%20Third%20iOS%20App-%20iCloud/About%20Your%20Third%20iOS%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjx)_.

As you learn more about iOS app development, consider making the following changes to the BirdWatching app:

- Support localization and accessibility. An app that is localized for different locales and accessible to users with disabilities enjoys a much wider customer base than an app without these features. Xcode and Auto Layout help make the [internationalization](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Internationalization.html#//apple_ref/doc/uid/TP40008195-CH23) and localization processes easy; to learn more, start by reading [Localized Resource Files](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Inter-AppCommunication/Inter-AppCommunication.html#//apple_ref/doc/uid/TP40007072-CH6-SW8). Use Accessibility Inspector in iOS Simulator to find places where your app can provide a better experience for VoiceOver users; to learn more, see _Testing the Accessibility of Your iOS App.
- Optimize the code. High performance is critical to a good user experience on iOS. Learn to use the various performance tools provided with Xcode, such as Instruments, to tune your app so that it minimizes its resource requirements.
- Add unit tests. Testing ensures that if the implementation of a method changes, the method still works as advertised. You can either create a new version of the project that sets up unit testing from the start, or you can use the current project and choose File > New > New Target, select the Other category, and then select the template Cocoa Unit Testing Bundle. Examine the project to see what Xcode adds when you incorporate unit testing. To learn about unit testing, see _[Xcode Unit Testing Guide](../../Developer%20Tools/Xcode%20Unit%20Testing%20Guide/About%20Unit%20Testing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnbt)_.
- Use Core Data to manage the model layer. Although it takes some work to learn how to use Core Data, it can help streamline the code required to support the model layer. Consider working through _Core Data Tutorial for iOS_ to get started learning about this technology.
- Ensure that the app runs on a device. It’s a good idea to familiarize yourself with the process of installing and testing an app on a device, because these tasks are prerequisites for submitting an app to the App Store.
- Make the app universal. iOS users often expect to be able to run their favorite apps on all types of iOS-based devices. Making an app universal can require additional work on your part; in particular, it generally requires that you create two different user interfaces, even if you reuse most of the same underlying code. To learn more about the steps you need to take to make an app universal, see Creating a Universal App.

[Next](Code%20Listings.md)[Previous](Troubleshooting.md)

