---
title: 'Your Second iOS App: Storyboards'
apple_id: TP40011318
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/SecondiOSAppTutorial/Troubleshooting/Troubleshooting.html
archived_at: '2026-07-18T02:28:01.944039Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Your Second iOS App: Storyboards](About%20Creating%20Your%20Second%20iOS%20App.md)


[Next](Next%20Steps.md)[Previous](Enabling%20the%20Addition%20of%20New%20Items.md)

# Troubleshooting

If you have trouble getting the BirdWatching app to work correctly, try the problem-solving approaches described in this chapter.

If the app isn’t working as it should, first compare your code with the code in [Code Listings](Code%20Listings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjyfvbuqojnknltc).

The tutorial code should compile without any warnings. If Xcode reports a warning, it’s a good idea to treat the warning in the same way that you treat errors. Objective-C is a very flexible language, and sometimes a warning is the only indication you receive when there is an issue that might cause an error.

When you’re accustomed to fixing all of an app’s problems in code, it’s easy to forget to check the objects in the storyboard. A great advantage of a storyboard is that, because it captures both the appearance and some of the configuration of app objects, you have less coding to do. To benefit from this advantage, it’s important to examine the storyboard, as well as the code, when an app doesn’t behave as you expect. Here are some examples.

__A scene does not seem to receive the data you send to it in the prepareForSegue method.__ Check the segue’s identifier in the Attributes inspector. If you forget to give the segue the same identifier that you use in the `prepareForSegue` method, you can still transition to the scene during testing, but the scene won’t display the data that you send to it.

The same result occurs when you misspell a segue’s identifier in the `prepareForSegue` method. Xcode does not warn you when a segue is missing its identifier, or when the `prepareForSegue` method uses an incorrect identifier, so it’s important to check these values for yourself.

__None of your changes to a custom view controller class seem to affect its scene.__ Check the scene’s class in the Identity inspector. If the name of your custom view controller class is not displayed in the Class pop-up menu, Xcode does not apply your changes to the scene.

__Nothing happens when you click the Cancel or Done buttons in the add scene’s navigation bar.__ Make sure each button is connected to its unwind action. Control-click the button on the canvas or in the document outline and confirm that the connection in the Triggered Segues section is active and correct.

__the text fields appear to work, but the data you enter is not displayed in the master list.__ Make sure the view controller’s outlets are connected to the text fields.

A common mistake related to using delegates is to misspell the delegate method name. Even if you’ve set the delegate object correctly, if the delegate doesn’t use the right name in its method implementation, the correct method won’t be invoked. It’s usually best to copy and paste delegate method declarations—such as `textFieldShouldReturn:`—from a reliable source (such as the documentation or the declaration in a header file).

[Next](Next%20Steps.md)[Previous](Enabling%20the%20Addition%20of%20New%20Items.md)

