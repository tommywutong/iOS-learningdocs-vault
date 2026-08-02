---
title: Address Book Programming Guide for Mac
apple_id: 10000117i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AddressBook
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/Tasks/AddingProperties.html
archived_at: '2026-07-18T02:09:43.476716Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Address Book Programming Guide for Mac](Introduction.md)


[Next](Creating%20and%20Using%20Address%20Book%20Action%20Plug-ins.md)[Previous](Using%20Address%20Book%20Groups%20as%20Distribution%20Lists.md)

# Adding Properties to Address Book Records

You can add your own properties to the people and groups in the address book. For example, if you’re creating a small application to manage a dog club, you could add properties to each person that specify the name and breed of that person’s dog. Or if you’re creating an application to manage business contacts, you could add a property that lists all the meetings and phone calls a user has had with that person. These properties are stored in the Address Book database. Applications that don’t know about the new properties aren’t affected by them and don’t modify them.

When deciding whether to add a property to the Address Book record, keep these issues in mind:

- Avoid properties for confidential information, such as credit card numbers. The Address Book framework does not provide any security above what’s provided by OS X. Anyone who has read and write access to a user’s home folder can also read and write that user’s address book.
- Avoid properties that are not useful for everyone in the address book database. If you want to store information for just the logged-in user, for Cocoa applications refer to _[NSUserDefaults Class Reference](https://developer.apple.com/documentation/foundation/nsuserdefaults)_, and for C-based applications refer to _[Preferences Utilities Reference](https://developer.apple.com/documentation/corefoundation/preferences_utilities)_.
- Use a multivalue list if you think a person may have more than one of that property. Your new multivalue list has the same capabilities as the other multivalue lists in the address book. The user can choose a primary value in the list and can create distribution lists for it.

To add properties to every person or group, use the `ABPerson` or `ABGroup` class method [addPropertiesAndTypes:](https://developer.apple.com/documentation/addressbook/abgroup/1427944-addpropertiesandtypes). These procedures take a dictionary, in which the keys are the names of the new properties and the values are their types. Note that the property names must be unique. You may want to use reverse-DNS style names for your properties, to make sure no one else uses the same name; for example, `org.dogclub.dogname` or `com.mycompany.buildingNumber`. The type can be one of the types or a multivalue list of one of the types listed in [Property Types](https://developer.apple.com/documentation/addressbook/address_book_objective_c_constants/property_types).

The following code listing adds a custom property, and then removes it:

```
    NSNumber* stringProperty = [NSNumber numberWithInteger:kABStringProperty];
    NSString* testProperty = @"com.example.myProperty";
    NSDictionary* dict = [NSDictionary dictionaryWithObject:stringProperty
                                                     forKey:testProperty];

    NSInteger result = [ABPerson addPropertiesAndTypes:dict];
    NSLog(@"Added %d properties.", result);

    result = [ABPerson removeProperties:[NSArray arrayWithObject:testProperty]];
    NSLog(@"Removed %d properties.", result);
```

[Next](Creating%20and%20Using%20Address%20Book%20Action%20Plug-ins.md)[Previous](Using%20Address%20Book%20Groups%20as%20Distribution%20Lists.md)

