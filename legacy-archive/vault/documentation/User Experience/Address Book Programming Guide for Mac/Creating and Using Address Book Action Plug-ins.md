---
title: Address Book Programming Guide for Mac
apple_id: 10000117i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AddressBook
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/Tasks/Actions.html
archived_at: '2026-07-18T02:09:42.896139Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Address Book Programming Guide for Mac](Introduction.md)


[Next](Importing%20and%20Exporting%20Person%20and%20Group%20Records.md)[Previous](Adding%20Properties%20to%20Address%20Book%20Records.md)

# Creating and Using Address Book Action Plug-ins

A unique aspect of the Address Book application is its ability to act on data contained within a person's card. You can install your own custom plug-ins to add additional actions to a given record. An example of an existing action is the Large Type action, which works on any phone number entry. When selected from its contextual menu, it displays the number in large type across the screen.

Each action plug-in can implement only one action. Actions can only apply to items with labels. An action can display a simple window in the Address Book application. If your action actions needs to do anything else, it should launch your own application to perform the action.

The `ABActionDelegate` protocol, which must be followed for the Address Book application to recognize the plug-in, is summarized in Table 1. See _[ABActionDelegate Protocol Reference](https://developer.apple.com/documentation/addressbook/abactiondelegate)_ for full details. C-based actions must implement a function named `ABActionRegisterCallbacks`, as described in _Address Book Actions Reference_.

__Table 1__  Action methods for an Address Book action plug-in

| Method | Purpose |
| [actionProperty](https://developer.apple.com/documentation/objectivec/nsobject/1411302-actionproperty) | Returns the `NSString` constant identifying the property that the action applies to. |
| [titleForPerson:identifier:](https://developer.apple.com/documentation/objectivec/nsobject/1411304-titleforperson) | Returns the title of the menu item for the action. This method should not return `nil`. |
| [performActionForPerson:identifier:](https://developer.apple.com/documentation/objectivec/nsobject/1411298-performaction) | Performs the appropriate action for the plug-in. Each plug-in can only have one action. |
| [shouldEnableActionForPerson:identifier:](https://developer.apple.com/documentation/objectivec/nsobject/1411300-shouldenableaction) | Returns `YES` if the action is applicable and `NO` otherwise. This allows your plug-in to enable and disable its menu item. (Optional.) |

To create a plug-in, use the Address Book action plug-in template from the Xcode New Project window. The template creates an action plug-in designed to create a contextual menu item on any phone number. When the menu item is selected, the sample plug-in uses OS X’s speech synthesis framework to speak the phone number. Replace this sample code with the code you need for your new plug-in. After you build your project, place the completed bundle in `.../Library/Address Book Plug-Ins`.

After an action plug-in has been loaded, its menu item is displayed in the contextual menu with the title returned from the `titleForPerson:identifier:` method; this method should not return `nil`. The plug-in can enable and disable this menu item using the `shouldEnableActionForPerson:identifier:` method.

[Next](Importing%20and%20Exporting%20Person%20and%20Group%20Records.md)[Previous](Adding%20Properties%20to%20Address%20Book%20Records.md)

