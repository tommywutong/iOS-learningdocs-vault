---
title: Address Book Programming Guide for Mac
apple_id: 10000117i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AddressBook
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/Tasks/CreatingMailingLists.html
archived_at: '2026-07-18T02:09:43.862156Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Address Book Programming Guide for Mac](Introduction.md)


[Next](Adding%20Properties%20to%20Address%20Book%20Records.md)[Previous](Searching%20an%20Address%20Book.md)

# Using Address Book Groups as Distribution Lists

An Address Book group can be used as a distribution list. For example, suppose you lead a book discussion club on the weekends. You can use a group to keep a list of all the people in the group. For multivalue properties such as telephone number and email address, the distribution list lets the you indicate which value should be used when sending a message to this group.

Generally, users will want to use the value marked as primary as the distribution identifier, but in some cases they will want to make an exception. For example, for coworkers, their primary email addresses are probably their work address. But messages about your weekend book club should be sent to their home addresses. This is accomplished by setting distribution identifier for the Book Club group to their home addresses.

To choose the value of a multivalue property that a group should use, use the `ABGroup` method [setDistributionIdentifier:forProperty:person:](https://developer.apple.com/documentation/addressbook/abgroup/1427936-setdistributionidentifier). Every group can use a different value for each person. Users can also edit this from the Address Book application, by selecting Edit Distribution List from the Edit menu.

To get a group’s chosen value for a multivalue property, use the `ABGroup` method [distributionIdentifierForProperty:person:](https://developer.apple.com/documentation/addressbook/abgroup/1427942-distributionidentifierforpropert). If a distribution identifier is not set, this method returns the multivalue’s primary identifier. If either the property or the person is `nil`, the method returns `nil`. the method also returns `nil` if the property is not a multivalue list property, or if the person is not a member of the group. Use the `ABMultiValue` method [valueForIdentifier:](https://developer.apple.com/documentation/addressbook/abmultivalue/1458427-valueforidentifier) to get the value from with the distribution identifier.

[Next](Adding%20Properties%20to%20Address%20Book%20Records.md)[Previous](Searching%20an%20Address%20Book.md)

