---
title: Wallet Developer Guide
apple_id: TP40012195
resource_type: Guide
platform: watchOS|iOS
topic: User Experience
technology: PassKit
published: '2018-01-16'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PassKit_PG/Apps.html
archived_at: '2026-07-18T02:12:08.190661Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Wallet Developer Guide](index.md)



## Interacting with Passes in Your App

There are two main reasons apps interact with passes: to provide an integrated user experience or to serve as a conduit for passes. An event venue’s app is an example of an integrated user experience. This app can show the performance schedule, play short video clips, and let users buy tickets. After buying a ticket, it can add a pass for that ticket to Wallet and create an event in the user’s calendar. It can also include UI for managing the tickets that users have purchased. An email or instant messaging client is an example of an app serving as a conduit. Just as it supports attachments such as images, it can also support passes attached to a message like Mail does. The app can display UI that indicates that the message has a pass attached and allow users to add the pass to their library. Supporting passes in your app should add value for the user; avoid trying to duplicate functionality of the Wallet app.

### Enabling Passbook Capabilities

Your app must have the appropriate entitlements before it can read, update, or delete passes. Use the Xcode Capabilities tab to turn on entitlements. If your provisioning profile is associated with multiple pass type identifiers, you can specify which of the identifiers your app can interact with. For more information, see Configuring Passbook for iOS Apps.

> [!NOTE]
> 

### Accessing Passes

The PassKit framework provides model-level access to pass data. The [PKPassLibrary](https://developer.apple.com/documentation/passkit/pkpasslibrary) class represents the pass library, and the [PKPass](https://developer.apple.com/documentation/passkit/pkpass) class represents individual passes. The framework also provides a view controller, the [PKAddPassesViewController](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller) class, which displays a pass and lets users add it to their pass library. Your app is responsible for the views it needs to display passes. To present a pass, use the [passURL](https://developer.apple.com/documentation/passkit/pkpass/1618781-passurl) property of a pass to show it in Wallet.

1. `[[UIApplication sharedApplication] openURL:[pass passURL]]`

A pass should not depend on your app to be useful. Passes need to be self-contained and useful by themselves, even if your app is not installed.

### Checking Whether the Pass Library Is Available

The presence of the PassKit framework and its classes doesn’t mean that the pass library is available. To check for its availability, call the [isPassLibraryAvailable](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617080-ispasslibraryavailable) method of the `PKPassLibrary` class.

> [!NOTE]
> 

### Checking Whether a Pass Is in the Library

You can determine whether a pass is in the library even if you don’t have the entitlement to read the pass. This feature allows apps to act as a conduit for passes that they did not create. When you receive a new pass, check to see if it is in Wallet, and present the correct UI. If the pass is already in Wallet, indicate that the pass already exists. If the pass is not present, let users add it to Wallet.

To check whether a pass is in the library:

1. Create an instance of the [PKPass](https://developer.apple.com/documentation/passkit/pkpass) class for the pass.
2. Create an instance of the [PKPassLibrary](https://developer.apple.com/documentation/passkit/pkpasslibrary) class.
3. Call the [containsPass:](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617110-containspass) method of the `PKPassLibrary` class with the pass you just created.

### Getting Passes

Use the [passes](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617109-passes) method of the `PKPassLibrary` class to get all passes that your app is entitled to access. Passes are returned in an arbitrary order. If your app displays a list of passes, it should sort them in some meaningful way such as by date.

To receive notifications when the pass library changes, register for the [PKPassLibraryDidChangeNotification](https://developer.apple.com/documentation/passkit/pkpasslibrarydidchangenotification) notification. Pass the instance of `PKPassLibrary` as the object. The pass library isn’t a singleton; each instance sends its own notifications, and you want the notifications from this particular instance. Use the [addObserverForName:object:queue:usingBlock:](https://developer.apple.com/documentation/foundation/nsnotificationcenter/1411723-addobserverforname) method to specify that you want to respond on the main queue and provide a block to handle the notification. The user info dictionary of the notification describes what changed. Alternatively, use the `dispatch_async` and `dispatch_get_main_queue` functions to respond on the main thread.

### Reading a Pass

Use the [passWithPassTypeIdentifier:serialNumber:](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617104-passwithpasstypeidentifier) method of the `PKPassLibrary` class to read a particular pass from the pass library.

You can access certain common bits of data, such as the organization name and description, using the properties of the [PKPass](https://developer.apple.com/documentation/passkit/pkpass) class. You can access the description using the [localizedDescription](https://developer.apple.com/documentation/passkit/pkpass/1618770-localizeddescription) method. These properties are useful if your app is acting as a conduit passes that you didn’t create, so you don’t know their fields’ keys.

You can access specific fields of a pass using the their key with the [localizedValueForFieldKey:](https://developer.apple.com/documentation/passkit/pkpass/1618798-localizedvalueforfieldkey) method. This method is useful if you created the pass, because then you know the keys for specific fields.

### Adding a New Pass

To add a pass to the library:

1. Create an instance of the `PKPass` class for the pass, initializing it with the pass’s data.
2. Use the [containsPass:](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617110-containspass) method of the `PKPassLibrary` class to check whether the pass is in the library. Your app can use this method to detect the presence of a pass even if it doesn’t have the entitlements to read passes in the library.
3. If the pass isn’t in the library, use an instance of the `PKAddPassesViewController` class to let the user add it.

   Present the add passes view controller modally, with animation.

### Changing a Pass

Passes cannot be changed directly on the device. Changing the contents of a pass would invalidate its signature. An updated pass needs to be signed using your private key, and distributing your private key as part of your app would be a particularly poor security practice.

To change a pass, coordinate with your server:

1. Your app connects to your server. It identifies the pass by serial number and pass type identifier and describes the change to your server.
2. Your server updates your business records as needed, creates a new version of the pass, and signs it.
3. Your app downloads the new pass from your server and uses the [replacePassWithPass:](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617082-replacepasswithpass) method of the `PKPassLibrary` class to install it.

After creating a new version of the pass, your server should also send a push notification so that other devices with this pass installed will get the latest copy.

### Removing a Pass

Use the [removePass:](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617083-removepass) method of the `PKPassLibrary` class to remove a pass.

Remember that passes belong to the user, not to your app. Passes should be removed only in response to a direct user action. Never remove a pass without the user’s consent, even if the pass has expired or is outdated.

[Updating a Pass](Updating.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdcojvfvbuqnjnknltc)

[Rewards Enrollment](PassPersonalization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdcojvfvbuqmjsfvjvomq)
