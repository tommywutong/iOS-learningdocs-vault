---
title: Address Book Programming Guide for Mac
apple_id: 10000117i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AddressBook
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/Tasks/Searching.html
archived_at: '2026-07-18T02:09:45.464611Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Address Book Programming Guide for Mac](Introduction.md)


[Next](Using%20Address%20Book%20Groups%20as%20Distribution%20Lists.md)[Previous](Accessing%20Address%20Book%20Records.md)

# Searching an Address Book

You can quickly search a user’s address book, using arbitrarily complex criteria. For example, you can search for all people named Smith, or for all people who work at Acme and live in San Francisco, or for all people who work at Ajax and live in Seattle.

To perform the search, you encapsulate the criteria in a search element to pass it to the Address Book framework. The framework performs the search on your behalf, and returns the results. Letting the framework handle the search can yield significant performance benefits compared to performing the search inside your application, because the framework is aware of the low-level layout of the underlying database, and it can optimize disk access accordingly.

To create a search element for a person, use the `ABPerson` class method [searchElementForProperty:label:key:value:comparison:](https://developer.apple.com/documentation/addressbook/abperson/1458332-searchelementforproperty). To create a search element for a group, use the `ABGroup` class method [searchElementForProperty:label:key:value:comparison:](https://developer.apple.com/documentation/addressbook/abgroup/1427946-searchelement).

If you want to search for people or groups that have a particular property set, regardless of the value it is set to, pass `nil` as the value and `kABNotEqual` as the comparison. To search for people or groups that do not have a property set, pass `nil` as the value and `kABEqual` as the comparison.

To combine search elements, use the `ABSearchElement` class method [searchElementForConjunction:children:](https://developer.apple.com/documentation/addressbook/absearchelement/1458423-searchelementforconjunction). This method takes two arguments:

- _conjunctionOperator_ describes how to combine the search elements. It can be `kABSearchAnd` or `kABSearchOr`.
- _children_ is an NSArray of search elements. The search elements can be a simple elements that specifies only one property, or complex elements that specifies several. This lets you create arbitrarily complex search elements. You cannot combine search elements for groups with search elements for people.

To search the address book for records that match a search element, use the `ABAddressBook` method [recordsMatchingSearchElement:](https://developer.apple.com/documentation/addressbook/abaddressbook/1458410-records), which returns an `NSArray` of records. Use the `ABSearchElement` method [matchesRecord:](https://developer.apple.com/documentation/addressbook/absearchelement/1458642-matchesrecord) to test whether a specific record matches a query.

Listing 1 shows the code to find everyone whose last name is Smith.

__Listing 1__  A simple search

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

Listing 2 shows the code to find everyone who lives in San Francisco and works for Acme, or who lives in Seattle and works for Ajax. Note that the addresses are searched using the [kABHomeLabel](https://developer.apple.com/documentation/addressbook/kabhomelabel) label—we only want to know if they live in the city we are searching, not if they work in the same city.

__Listing 2__  A complex search

```
ABAddressBook *AB = [ABAddressBook sharedAddressBook];
ABSearchElement *inSF =
    [ABPerson searchElementForProperty:kABAddressProperty
                                 label:kABHomeLabel
                                   key:kABAddressCityKey
                                 value:@"San Francisco"
                            comparison:kABEqualCaseInsensitive];
ABSearchElement *atAcme =
    [ABPerson searchElementForProperty:kABOrganizationProperty
                                 label:nil
                                   key:nil
                                 value:@"Acme"
                            comparison:kABContainsSubStringCaseInsensitive];
ABSearchElement *inSeattle =
    [ABPerson searchElementForProperty:kABAddressProperty
                                 label:kABHomeLabel
                                   key:kABAddressCityKey
                                 value:@"Seattle"
                            comparison:kABEqualCaseInsensitive];
ABSearchElement *atAjax =
    [ABPerson searchElementForProperty:kABOrganizationProperty
                                 label:nil
                                   key:nil
                                 value:@"Ajax"
                            comparison:kABContainsSubStringCaseInsensitive];
ABSearchElement *inSFAndAtAcme =
    [ABSearchElement searchElementForConjunction:kABSearchAnd
                                        children:[NSArray arrayWithObjects:
                                            inSF, atAcme, nil]];
ABSearchElement *inSeattleAndAtAjax =
    [ABSearchElement searchElementForConjunction:kABSearchAnd
                                        children:[NSArray arrayWithObjects:
                                            inSeattle, atAjax, nil]];
ABSearchElement *inSFAndAtAcmeOrInSeattleAndAtAjax =
    [ABSearchElement searchElementForConjunction:kABSearchOr
                                        children:[NSArray arrayWithObjects:
                                            inSFAndAtAcme, inSeattleAndAtAjax, nil]];
NSArray *peopleFound =
    [AB recordsMatchingSearchElement:inSFAndAtAcmeOrInSeattleAndAtAjax];
```

[Next](Using%20Address%20Book%20Groups%20as%20Distribution%20Lists.md)[Previous](Accessing%20Address%20Book%20Records.md)

