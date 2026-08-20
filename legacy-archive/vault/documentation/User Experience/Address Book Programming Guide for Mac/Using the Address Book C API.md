---
title: Address Book Programming Guide for Mac
apple_id: 10000117i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AddressBook
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/Concepts/ForCarbonDev.html
archived_at: '2026-07-18T02:09:40.667564Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Address Book Programming Guide for Mac](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Showing%20Records%20in%20the%20Contacts%20App.md)

# Using the Address Book C API

For the most part, the Objective-C API has close method and syntax parity with the C API. This makes it easy to determine, for example, which function corresponds to a given Objective-C method.

There are a couple of primary differences that developers need to be aware of when using the Address Book C API:

- The people picker comes only in window form and does not have a C API for setting an accessory view. In addition, changes in selection and displayed properties are sent via Carbon Events.
- When creating a C-based action plug-in, your bundle must implement a function called `ABActionRegisterCallbacks`, which will return an [ABActionCallbacks](https://developer.apple.com/documentation/addressbook/abactioncallbacks) structure. The structure needs to be formed according to this type definition:

```
typedef struct {
    // The version of this struct is 0
    CFIndex                      version;

    // A pointer to a function that returns the AddressBook
    // property this action applies to.
    ABActionPropertyCallback     property;

    // A pointer to a function that returns the AddressBook
    // property this action applies to. Only items with labels
    // may have actions at this time.
    ABActionTitleCallback        title;

    // A pointer to a function which returns YES if the action
    // should be enabled for the passed ABPersonRef and item
    // identifier. The item identifier will be NULL for single value
    // properties. This field may be NULL. Actions with NULL enabled
    // callbacks will always be enabled.
    ABActionEnabledCallback      enabled;

    // A pointer to a function which will be called when the user
    // selects this action. It's passed an ABPersonRef and item
    // identifier. The item identifier will be NULL for single
    // value properties.
    ABActionSelectedCallback     selected;

} ABActionCallbacks
```

To access the user’s shared address book using the C programming interface, you need to use the value returned by [ABGetSharedAddressBook](https://developer.apple.com/documentation/addressbook/1430178-abgetsharedaddressbook).

```
ABAddressBookRef addressBook = ABGetSharedAddressBook();
```

Compare this with the corresponding code using the Objective-C programming interface, noting the mapping between corresponding method and function names.

```
ABAddressBook *addressBook = [ABAddressBook sharedAddressBook];
```

This example from [Searching an Address Book](Searching%20an%20Address%20Book.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgazdilkcifbeqscjjbbq), Listing 1, searches for anyone named Smith in the current user’s address book and returns an array of results.

__Listing 1__  A simple search, in Objective-C

```
ABAddressBook *AB = [ABAddressBook sharedAddressBook];

ABSearchElement *nameIsSmith =
    [ABPerson searchElementForProperty:kABLastNameProperty
                                 label:nil
                                   key:nil
                                 value:@"Smith"
                            comparison:kABEqualCaseInsensitive];

NSArray *peopleFound =
    [AB recordsMatchingSearchElement:nameIsSmith];
```

Listing 2 performs the same search using the C API. Again, note the mapping between corresponding method and function names.

__Listing 2__  A simple search, in C

```
ABAddressBookRef AB = ABGetSharedAddressBook();

ABSearchElementRef nameIsSmith =
    ABPersonCreateSearchElement(kABLastNameProperty,
                    NULL,
                    NULL,
                    CFSTR("Smith"),
                    kABEqualCaseInsensitive);

CFArrayRef peopleFound =
    ABCopyArrayOfMatchingRecords(AB, nameIsSmith);
```

For more details about using the C API for the Address Book framework, refer to _Address Book C Framework Reference for Mac_.

[Next](Document%20Revision%20History.md)[Previous](Showing%20Records%20in%20the%20Contacts%20App.md)

