---
title: Address Book Programming Guide for Mac
apple_id: 10000117i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AddressBook
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/Tasks/AccessingData.html
archived_at: '2026-07-18T02:09:42.473849Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Address Book Programming Guide for Mac](Introduction.md)


[Next](Searching%20an%20Address%20Book.md)[Previous](Managing%20Address%20Book%20Records.md)

# Accessing Address Book Records

After you have a record, you can retrieve the data within it. This chapter shows you how the data is organized and how to access it. It shows how to access properties from a records property list, how to handle properties that can have more than one value (such as addresses and phone numbers), how to get localized names for properties and labels, and how to associate a picture with a person.

Both groups and people store their data in property lists. This lets your application add properties to the Address Book records that other applications will ignore. See [Adding Properties to Address Book Records](Adding%20Properties%20to%20Address%20Book%20Records.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgazdmlkcifbeqscjjbbq).

- To get data from a record, such as a group’s description or a person’s first name, use the [valueForProperty:](https://developer.apple.com/documentation/addressbook/abrecord/1400523-valueforproperty) method or the C function `ABRecordCopyValue`. For example, to get the first name for `aPerson`, use:

```
[aPerson valueForProperty:kABFirstNameProperty];
```
- To set data, use the [setValue:forProperty:](https://developer.apple.com/documentation/addressbook/abrecord/1400509-setvalue) method. For example, to set the name of `aGroup`, use:

```
[aGroup setValue:@"Book Club" forProperty:kABGroupNameProperty];
```
- To find the names of the default properties, refer to Table 1.

__Table 1__  The documentation for property-list constants

| Documentation | Class | Language |
| [Default Record Properties](https://developer.apple.com/documentation/addressbook/address_book_objective_c_constants/default_record_properties) | `ABRecord` | Objective-C |
| [Default Person Properties](https://developer.apple.com/documentation/addressbook/address_book_objective_c_constants/default_person_properties) | `ABPerson` | Objective-C |
| [Default Group Properties](https://developer.apple.com/documentation/addressbook/address_book_objective_c_constants/default_group_properties) | `ABGroup` | Objective-C |
| Constants | `ABPersonRef` | Procedural C |
| Constants | `ABGroupRef` | Procedural C |

Many properties can have multiple values. For example, a person can have several addresses, including work, home, summer home, and mailing addresses. These properties are stored as multivalue lists, of type [ABMultiValue](https://developer.apple.com/documentation/addressbook/abmultivalue). Each item in a multivalue list has a numeric index, a unique identifier, a string label (such as Home or Work), and a value. Every value in the multivalue list must be of the same type. The label does not need to be unique; after all, someone could have more than one home or work address.

- To add an item to a multivalue list, use the [addValue:withLabel:](https://developer.apple.com/documentation/addressbook/abmutablemultivalue/1458374-add) or [insertValue:withLabel:atIndex:](https://developer.apple.com/documentation/addressbook/abmutablemultivalue/1458362-insert) method.
- To retrieve an item, use the [valueAtIndex:](https://developer.apple.com/documentation/addressbook/abmultivalue/1458515-valueatindex) or [labelAtIndex:](https://developer.apple.com/documentation/addressbook/abmultivalue/1458668-label) method.
- To remove an entry in a multivalue list, use the [removeValueAndLabelAtIndex:](https://developer.apple.com/documentation/addressbook/abmutablemultivalue/1458405-removevalueandlabelatindex) method.
- To replace values and labels, use the [replaceLabelAtIndex:withLabel:](https://developer.apple.com/documentation/addressbook/abmutablemultivalue/1458689-replacelabelatindex) or [replaceValueAtIndex:withValue:](https://developer.apple.com/documentation/addressbook/abmutablemultivalue/1458609-replacevalueatindex) methods.

You use the numeric index to access items in a multivalue list, but these indices may change as the user adds and removes values. If you want to save a reference to a specific value, use the unique identifier, which is guaranteed not to change. You can convert back and forth between indices and unique identifiers:

- To get the unique identifier for a value at a particular index, use the [identifierAtIndex:](https://developer.apple.com/documentation/addressbook/abmultivalue/1458743-identifieratindex) method.
- To get the index for a identifier, use the [indexForIdentifier:](https://developer.apple.com/documentation/addressbook/abmultivalue/1458700-indexforidentifier) method.

Each multivalue list also has a primary value, which is the item the user most strongly associates with that person. For example, friends may have both home and work addresses, but the home address is their primary address. And coworkers may have both home and work phone numbers, but the work number is their primary number.

- To get the identifier for a multivalue list’s primary value, use the [primaryIdentifier](https://developer.apple.com/documentation/addressbook/abmultivalue/1458525-primaryidentifier) method.
- To set the multivalue list’s primary value, use the [setPrimaryIdentifier:](https://developer.apple.com/documentation/addressbook/abmutablemultivalue/1458716-setprimaryidentifier) method.

A person may also have an associated picture or image. The image is not actually stored in the Address Book database (a property list)—it’s stored in a separate image file. This means you need to use different methods to access the image data. You can set a person’s image using the [setImageData:](https://developer.apple.com/documentation/addressbook/abperson/1392513-setimagedata) method, or get an image using the [imageData](https://developer.apple.com/documentation/addressbook/abperson/1392509-imagedata) method. Use the `NSImage` [initWithData:](https://developer.apple.com/documentation/appkit/nsimage/1519941-initwithdata) method to convert the `NSData` object returned by the `imageData` method to an `NSImage` object.

The Address Book framework locates images through a specific search hierarchy, in this order:

1. Check for an image set specifically by the user.
2. Check Directory Services for the local user’s login picture.
3. Check for an image in `/Network/Library/Images/People/`_email_, where _email_ is the user’s primary email address.
4. Check for an image from the user’s MobileMe account, first against the cache at `~/Library/Caches/com.apple.AddressBook/`_email_ and then against the MobileMe servers.

Image files may be local or remote. Local images are any images in `.../Library/Images/People` and any images the user has set using the Address Book application. Remote images are images stored on the network. Remote images take time to download, so an asynchronous API for fetching remote images is provided.

Use the [beginLoadingImageDataForClient:](https://developer.apple.com/documentation/addressbook/abperson/1392507-beginloadingimagedataforclient) method if an image file is not local and you want to perform an asynchronous fetch. You pass a client object that implements the `ABImageClient` protocol as an argument to this method. The [beginLoadingImageDataForClient:](https://developer.apple.com/documentation/addressbook/abperson/1392507-beginloadingimagedataforclient) method returns an image tracking number. A [consumeImageData:forTag:](https://developer.apple.com/documentation/addressbook/abimageclient/1392505-consumeimagedata) message is sent to your client object when the fetch is done. Implement this method to handle the new fetched image. Use the [cancelLoadingImageDataForTag:](https://developer.apple.com/documentation/addressbook/abperson/1392511-cancelloadingimagedatafortag) class method if you want to cancel an asynchronous fetch.

Use the [beginLoadingImageDataForClient:](https://developer.apple.com/documentation/addressbook/abperson/1392507-beginloadingimagedataforclient) method if an image file is not local and you want to perform an asynchronous fetch:

1. Pass a client object that implements the [ABImageClient](https://developer.apple.com/documentation/addressbook/abimageclient) protocol as an argument to this method.
2. The [beginLoadingImageDataForClient:](https://developer.apple.com/documentation/addressbook/abperson/1392507-beginloadingimagedataforclient) method returns an image tracking number.
3. A [consumeImageData:forTag:](https://developer.apple.com/documentation/addressbook/abimageclient/1392505-consumeimagedata) message is sent to your client object when the fetch is done. Implement this method to handle the new fetched image.
4. Use the [cancelLoadingImageDataForTag:](https://developer.apple.com/documentation/addressbook/abperson/1392511-cancelloadingimagedatafortag) class method if you want to cancel an asynchronous fetch.

You can find the localized name for any of the default property names and labels that are listed in _[Address Book Objective-C Constants Reference](https://developer.apple.com/documentation/addressbook/address_book_objective_c_constants)_. The functions [ABLocalizedPropertyOrLabel](https://developer.apple.com/documentation/addressbook/1458691-ablocalizedpropertyorlabel) and [ABCopyLocalizedPropertyOrLabel](https://developer.apple.com/documentation/addressbook/1430176-abcopylocalizedpropertyorlabel) returned a name that is localized for the user’s selected language.

You must handle the localization of the names for the properties and labels you create; the Address Book framework does not provide any specific support for this.

Listing 1 is an Objective-C code sample that retrieves the country for the primary address of the logged-in user. If the country is a null string, it sets the country to USA.

__Listing 1__  Changing a person’s address

```
ABPerson *aPerson = [[ABAddressBook sharedAddressBook] me];
ABMutableMultiValue *anAddressList =
    [[aPerson valueForProperty:kABAddressProperty] mutableCopy];
NSUInteger primaryIndex =
    [anAddressList indexForIdentifier:[anAddressList primaryIdentifier]];
NSMutableDictionary *anAddress =
    [[anAddressList valueAtIndex:primaryIndex] mutableCopy];
NSString *country =
    (NSString*) [anAddress objectForKey:kABAddressCountryKey];
if ([country isEqualToString:@""]) {
    [anAddress setObject:@"USA" forKey:kABAddressCountryKey];
    [anAddressList replaceValueAtIndex:primaryIndex withValue:anAddress];
    [aPerson setValue:anAddressList forProperty:kABAddressProperty];
    [[ABAddressBook sharedAddressBook] save];
}
```


The people picker is a view that provides access to the contents of a user’s address book from any application. It offers a searchable, selectable list of people and groups that can be customized for your application.

To use a people picker in a Cocoa application, drag it from the library palette into your window. If you need to, you can create an instance of `ABPeoplePickerView` programmatically instead. There are two ways to set up the behavior of the people picker view—from Interface Builder and programmatically.

To set up the behavior from Interface Builder, open the Get Info panel. The attributes you can set include which columns are displayed by the view, whether or not multiple selections are allowed, whether or not group selections are allowed, and the autosave name for the view. These changes are reflected immediately within Interface Builder. Using the Test Interface feature of Interface Builder, a people picker view will display the address book of the logged-in user.

To set up the behavior programmatically, create an outlet of the type [ABPeoplePickerView](https://developer.apple.com/documentation/addressbook/abpeoplepickerview) from your controller and connect it to the people picker view. Then use the appropriate instance methods to change attributes of the picker.

For Cocoa applications, the people picker also provides methods for using autosave data, so that it can retain the filter selections and column positions. Use the `ABPeoplePickerView` methods [autosaveName](https://developer.apple.com/documentation/addressbook/abpeoplepickerview/1458748-autosavename) and [autosaveName](https://developer.apple.com/documentation/addressbook/abpeoplepickerview/1458748-autosavename).

Using the C API, the people picker is available only in a window form and cannot be used as a custom view. It must be created with [ABPickerCreate](https://developer.apple.com/documentation/addressbook/1591597-abpickercreate) and made visible with [ABPickerSetVisibility](https://developer.apple.com/documentation/addressbook/1591602-abpickersetvisibility), as follows:

```
ABPickerRef peoplePicker = ABPickerCreate();
ABPickerSetVisibility(peoplePicker, true);
```


The code from this example should be placed in the window controller for the people picker. Developers using the C API should refer to the _ABPicker C Reference_ to construct the analogue for their applications; most of the functions are named similarly. Instead of using notifications, you will need to register event handlers to handle changes to the window.

The following listing shows how you can set the attributes of a people picker programmatically. This code is typically part of the `awakeFromNib` method. All of these settings are also available in the attributes inspector, in Interface Builder.

```
    // Disallow multiple selections in the name list.
    [peoplePicker setAllowsMultipleSelection:NO];

    // Add the e-mail and telephone properties to the view.
    // By default, the people picker displays only the
    // Name column.
    [peoplePicker addProperty:kABEmailProperty];
    [peoplePicker addProperty:kABPhoneProperty];
```

The following listing shows how to register for a notification when the user selects a person record in the people picker. This code is typically part of the `awakeFromNib` method.

```
    NSNotificationCenter* center;
    center = [NSNotificationCenter defaultCenter];

    // Set up a responder for one of the four available notifications,
    // in this case to tell us when the selection in the people picker
    // has changed.
    [center addObserver:self
            selector:@selector(recordChanged:)
            name:ABPeoplePickerNameSelectionDidChangeNotification
            object:peoplePicker];
```

The following listing shows an example of how to respond to the user selecting a person record in the people picker:

```objc
- (void)recordChanged:(NSNotification*)notification {
    NSArray *array;
    NSImage *personImage;
    NSString *personFirstName;
    NSString *personLastName;

    array = [peoplePicker selectedRecords];
    NSAssert([array count] == 1,
             @"Picker returned multiple selected records");
    ABPerson *person = [array objectAtIndex:0];

    personImage = [[NSImage alloc] initWithData:[person imageData]];
    personFirstName = [person valueForProperty:kABFirstNameProperty],
    personLastName = [person valueForProperty:kABLastNameProperty];
```

[Next](Searching%20an%20Address%20Book.md)[Previous](Managing%20Address%20Book%20Records.md)

