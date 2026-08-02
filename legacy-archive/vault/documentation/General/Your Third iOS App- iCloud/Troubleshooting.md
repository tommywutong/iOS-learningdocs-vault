---
title: 'Your Third iOS App: iCloud'
apple_id: TP40011317
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloud101/Troubleshooting/Troubleshooting.html
archived_at: '2026-07-15T07:34:35.953411Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Your Third iOS App: iCloud](About%20Your%20Third%20iOS%20App.md)


[Next](Next%20Steps.md)[Previous](Searching%20for%20iCloud%20Documents.md)

# Troubleshooting

If you have trouble getting your app to work correctly, try the problem-solving approaches described in this chapter.

If you are able to compile your code but the build fails to install on your device, you need to check the provisioning information for your app.

- If you are unable to install the app on a device, check the value for the Code Signing Identity build setting and make sure it is set to the correct provisioning profile.
- If the provisioning profile shows up as invalid, make sure you have the correct development certificates installed on the current machine. You can check the available certificates using the Keychain Access application.
- If the provisioning profile appears disabled in the Code Signing Identity pop-up menu, make sure the bundle identifier of your project matches the bundle identifier in the provisioning profile. Profiles can also appear disabled if the installed certificates do not match the ones selected for the provisioning profile.

When your app calls the [URLForUbiquityContainerIdentifier:](https://developer.apple.com/documentation/foundation/nsfilemanager/1411653-urlforubiquitycontaineridentifie) method to retrieve the iCloud container directory, that method should return a valid URL if everything is configured correctly. If the method returns `nil`, it could be for one of the following reasons:

- The device has not yet been configured with an iCloud account, or the Documents & Data option is disabled.
- Your app’s entitlements are not configured properly.

The most likely problem to occur during development is that your app’s entitlements are not configured properly. You should double-check the steps laid out in [Getting Started](Getting%20Started.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjxfvbuqmrnknltc) to make sure your entitlements are specified correctly and that your app ID and provisioning profile are up to date and being used by your Xcode project.

If things are not working as they should, first compare your code with the complete listings in [Code Listings](Code%20Listings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjxfvbuqobnknltc).

Your code should compile without any warnings. If you do receive warnings, it is recommended that you treat them as very likely to be errors. The reason for this is that Objective-C is a very flexible language, so that sometimes the most you get from the compiler is a warning.

When one method calls another method, the method being called must be defined before the method that calls it. If the compiler reports an error that your class does not declare a method with a given selector name, try rearranging the methods in your source file to fix the problem. Except where otherwise noted, you should not need to include the methods in this tutorial in your class declarations.

As a developer, if things do not work correctly, your natural instinct might be to check your source code for bugs. But when you use Cocoa Touch, another dimension is added. Much of your app’s configuration is “encoded” in the storyboard file. If you haven’t made the correct connections, your app will not behave as you might expect.

- If the table does not display any data, even after you explicitly add some, you might have forgotten to set the master view controller as the delegate of the table view.
- If tapping a cell does not display the detail view, make sure you configured the segue. Changing the content type for the table removes the existing segue in the project, so you must recreate it.
- If tapping the Add button does not have the desired effect, you might have forgotten to connect the action method to it.

A common mistake with notifications is to misspell the method name of the notification handler. If when registering the notification observer, you provide a name that is different from the actual method name, the correct method is not called. It is usually better to copy and paste method names when specifying the handlers.

[Next](Next%20Steps.md)[Previous](Searching%20for%20iCloud%20Documents.md)

