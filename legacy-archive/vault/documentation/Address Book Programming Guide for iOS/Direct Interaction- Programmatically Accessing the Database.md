---
title: Address Book Programming Guide for iOS
apple_id: TP40007744
resource_type: Guide
platform: iOS
topic: Data Management
technology: AddressBookUI
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/ContactData/Conceptual/AddressBookProgrammingGuideforiPhone/Chapters/DirectInteraction.html
archived_at: '2026-07-15T07:22:01.593342Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Address Book Programming Guide for iOS](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](User%20Interaction-%20Prompting%20for%20and%20Displaying%20Data.md)

# Direct Interaction: Programmatically Accessing the Database

Although many common Address Book database tasks depend on user interaction, in some cases appropriate for the application needs to interact with the Address Book database directly. There are several functions in the Address Book framework that provide this ability.

In order to provide a uniform user experience, it is important to use these functions only when they are appropriate. Rather than using these functions to create new view or navigation controllers, your program should call the provided view or navigation controllers whenever possible. For more information, see [User Interaction: Prompting for and Displaying Data](User%20Interaction-%20Prompting%20for%20and%20Displaying%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tonbufvbuqnjnknltc).

Remember that the Address Book database is ultimately owned by the user, so applications must be careful not to make unexpected changes to it. Generally, changes should be initiated or confirmed by the user. This is especially true for groups, because there is no interface on the device for the user to manage groups and undo your application’s changes.

Every record in the Address Book database has a unique record identifier. This identifier always refers to the same record, unless that record is deleted or the data is reset. Record identifiers can be safely passed between threads. They are not guaranteed to remain the same across devices.

The recommended way to keep a long-term reference to a particular record is to store the first and last name, or a hash of the first and last name, in addition to the identifier. When you look up a record by ID, compare the record’s name to your stored name. If they don’t match, use the stored name to find the record, and store the new ID for the record.

To get the record identifier of a record, use the function [ABRecordGetRecordID](https://developer.apple.com/documentation/addressbook/1614734-abrecordgetrecordid). To find a person record by identifier, use the function [ABAddressBookGetPersonWithRecordID](https://developer.apple.com/documentation/addressbook/1619820-abaddressbookgetpersonwithrecord). To find a group by identifier, use the function [ABAddressBookGetGroupWithRecordID](https://developer.apple.com/documentation/addressbook/1616120-abaddressbookgetgroupwithrecordi). To find a person record by name, use the function [ABAddressBookCopyPeopleWithName](https://developer.apple.com/documentation/addressbook/1619789-abaddressbookcopypeoplewithname).

You can add and remove records from the Address Book database using the functions [ABAddressBookAddRecord](https://developer.apple.com/documentation/addressbook/1621987-abaddressbookaddrecord) and [ABAddressBookRemoveRecord](https://developer.apple.com/documentation/addressbook/1622008-abaddressbookremoverecord).

There are two ways to find a person record in the Address Book database: by name, using the function [ABAddressBookCopyPeopleWithName](https://developer.apple.com/documentation/addressbook/1619789-abaddressbookcopypeoplewithname), and by record identifier, using the function [ABAddressBookGetPersonWithRecordID](https://developer.apple.com/documentation/addressbook/1619820-abaddressbookgetpersonwithrecord). To accomplish other kinds of searches, use the function [ABAddressBookCopyArrayOfAllPeople](https://developer.apple.com/documentation/addressbook/1619817-abaddressbookcopyarrayofallpeopl) and then filter the results using the `NSArray` method [filteredArrayUsingPredicate:](https://developer.apple.com/documentation/foundation/nsarray/1411033-filtered), as shown in the following code listing.

```
NSArray* allContacts = /* assume this exists */ ;

// Build a predicate that searches for contacts with at least one phone number starting with (408).
NSPredicate* predicate = [NSPredicate predicateWithBlock: ^(id record, NSDictionary* bindings) {
    ABMultiValueRef phoneNumbers = ABRecordCopyValue( (__bridge ABRecordRef)record, kABPersonPhoneProperty);
    BOOL result = NO;

    for (CFIndex i = 0; i < ABMultiValueGetCount(phoneNumbers); i++) {
        NSString* phoneNumber = (__bridge_transfer NSString*) ABMultiValueCopyValueAtIndex(phoneNumbers, i);
        if ([phoneNumber hasPrefix:@"(408)"]) {
            result = YES;
            break;
        }
    }

    CFRelease(phoneNumbers);
    return result;
}];
NSArray* filteredContacts = [allContacts filteredArrayUsingPredicate:predicate];
```

To sort an array of people, use the function [CFArraySortValues](https://developer.apple.com/documentation/corefoundation/1388749-cfarraysortvalues) with the function [ABPersonComparePeopleByName](https://developer.apple.com/documentation/addressbook/1619777-abpersoncomparepeoplebyname) as the comparator and a context of the type [ABPersonSortOrdering](https://developer.apple.com/documentation/addressbook/abpersonsortordering). The user’s desired sort order, as returned by [ABPersonGetSortOrdering](https://developer.apple.com/documentation/addressbook/1619717-abpersongetsortordering), is generally the preferred context.

The following code listing shows an example of sorting the entire Address Book database:

```
ABAddressBookRef addressBook = ABAddressBookCreate();
CFArrayRef people = ABAddressBookCopyArrayOfAllPeople(addressBook);
CFMutableArrayRef peopleMutable = CFArrayCreateMutableCopy(
                                          kCFAllocatorDefault,
                                          CFArrayGetCount(people),
                                          people
                                  );


CFArraySortValues(
        peopleMutable,
        CFRangeMake(0, CFArrayGetCount(peopleMutable)),
        (CFComparatorFunction) ABPersonComparePeopleByName,
        (void*) ABPersonGetSortOrdering()
);

CFRelease(addressBook);
CFRelease(people);
CFRelease(peopleMutable);
```


You can find a specific group by record identifier using the function [ABAddressBookGetGroupWithRecordID](https://developer.apple.com/documentation/addressbook/1616120-abaddressbookgetgroupwithrecordi). You can also retrieve an array of all the groups in an address book using [ABAddressBookCopyArrayOfAllGroups](https://developer.apple.com/documentation/addressbook/1616131-abaddressbookcopyarrayofallgroup), and get a count of how many groups there are in an address book using the function [ABAddressBookGetGroupCount](https://developer.apple.com/documentation/addressbook/1616124-abaddressbookgetgroupcount).

You can modify the members of a group programatically. To add a person to a group, use the function [ABGroupAddMember](https://developer.apple.com/documentation/addressbook/1430147-abgroupaddmember); to remove a person from a group, use the function [ABGroupRemoveMember](https://developer.apple.com/documentation/addressbook/1430206-abgroupremovemember).

[Next](Document%20Revision%20History.md)[Previous](User%20Interaction-%20Prompting%20for%20and%20Displaying%20Data.md)

