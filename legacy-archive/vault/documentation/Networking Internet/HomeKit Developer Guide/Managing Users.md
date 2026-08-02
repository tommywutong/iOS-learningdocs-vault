---
title: HomeKit Developer Guide
apple_id: TP40015050
resource_type: Guide
platform: watchOS|iOS
topic: null
technology: HomeKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/HomeKitDeveloperGuide/ManagingUsers/ManagingUsers.html
archived_at: '2026-07-27T06:57:09.478314Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HomeKit Developer Guide](Introduction%20to%20HomeKit.md)


[Next](Document%20Revision%20History.md)[Previous](Creating%20Action%20Sets%20and%20Triggers.md)

# Managing Users

The user who creates a home is the admin for the home and can perform all operations including adding guest users to a home. Any user ([HMUser](https://developer.apple.com/documentation/homekit/hmuser)) that an admin adds to a home has restricted privileges. Guests can’t modify the home layout in any way but can perform these types of actions:

- Identify accessories
- Read and write characteristic values
- Observe changes to characteristic values
- Execute action sets

For example, the head of a household creates a home layout and adds family members to the home. Each family member must have a personal iOS device and Apple ID with an associated iCloud account. The iCloud credentials that family members enter on their iOS devices must match the Apple ID provided by the head of a household in order for them to access the home. For privacy reasons, the Apple ID is hidden from your app.

Adding a guest to a home requires the following actions on the admin’s iOS device:

1. The admin user invokes an action to add a guest to a home.
2. Your app invokes the [addUserWithCompletionHandler:](https://developer.apple.com/documentation/homekit/hmhome/1620213-adduserwithcompletionhandler) asynchronous method.
3. HomeKit displays a dialog requesting the guest’s Apple ID.
4. The user enters the guest’s Apple ID in the dialog.
5. The completion handler returns the new user object.
6. Your app displays the guest’s name.

Adding a guest to a home requires the following actions on the guest’s iOS device:

1. The user enters the user’s iCloud credentials (the Apple ID and password) in iCloud preferences.
2. The user launches your app.
3. Your app gets the collection of homes from the home manager object.
4. If the iCloud credentials match the Apple ID entered by the admin, the admin’s home appears in the [homes](https://developer.apple.com/documentation/homekit/hmhomemanager/1616751-homes) property.

Some operations performed by a guest may fail. If an asynchronous message to HomeKit fails with error code [HMErrorCodeInsufficientPrivileges](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodeinsufficientprivileges), the user is not allowed to perform the action—the user is probably a guest, not the admin.

To test whether your app handles guest users correctly, read [Testing Multiple iOS Devices and Users](Testing%20Your%20HomeKit%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnznknltcmq).

## Adding and Removing Users

To add a guest user to a home, use the [addUserWithCompletionHandler:](https://developer.apple.com/documentation/homekit/hmhome/1620213-adduserwithcompletionhandler) asynchronous method.

```
[self.home addUserWithCompletionHandler:^(HMUser *user, NSError *error) {
    if (error == nil) {
        // Successfully added a user
    }
    else {
       // Unable to add a user
    }
}];
```

To remove a user from a home, use the [removeUser:completionHandler:](https://developer.apple.com/documentation/homekit/hmhome/1620251-removeuser) method in the [HMHome](https://developer.apple.com/documentation/homekit/hmhome) class.

Implement the [home:didAddUser:](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620217-home) and [home:didRemoveUser:](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620232-home) delegate methods in the [HMHomeDelegate](https://developer.apple.com/documentation/homekit/hmhomedelegate) protocol to update views when other apps add and remove users. To create a home delegate, read [Observing Changes to Individual Homes](Observing%20HomeKit%20Database%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnjnknlti).

## Getting User Names

For privacy reasons, your app has read-only access to the name of a user, not read or write access to the Apple ID of a user. Use the [users](https://developer.apple.com/documentation/homekit/hmhome/1620254-users) property in the [HMHome](https://developer.apple.com/documentation/homekit/hmhome) class to get the users of a home. Use the [name](https://developer.apple.com/documentation/homekit/hmuser/1620011-name) property of the [HMUser](https://developer.apple.com/documentation/homekit/hmuser) class to get the name of a user.

[Next](Document%20Revision%20History.md)[Previous](Creating%20Action%20Sets%20and%20Triggers.md)
