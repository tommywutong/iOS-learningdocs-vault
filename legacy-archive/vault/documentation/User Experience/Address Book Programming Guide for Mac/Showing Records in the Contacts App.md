---
title: Address Book Programming Guide for Mac
apple_id: 10000117i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AddressBook
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/Tasks/URLScheme.html
archived_at: '2026-07-18T02:09:45.907524Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Address Book Programming Guide for Mac](Introduction.md)


[Next](Using%20the%20Address%20Book%20C%20API.md)[Previous](Importing%20and%20Exporting%20Person%20and%20Group%20Records.md)

# Showing Records in the Contacts App

Your app can use the `addressbook` URL scheme to launch the Contacts app, displaying a particular person record. This URL scheme takes the unique identifier of the person and an optional “edit” parameter, as shown in the following code listing:

```
ABPerson * aPerson = <#assume this exists#>;

// Open the Contacts app, showing the person record.
NSString * urlString = [NSString stringWithFormat:@"addressbook://%@", [aPerson uniqueId]];
[[NSWorkspace sharedWorkspace] openURL:[NSURL URLWithString:urlString]];

// Open the Contacts app, editing the person record.
NSString *urlString = [NSString stringWithFormat:@"addressbook://%@?edit", [aPerson uniqueId]];
[[NSWorkspace sharedWorkspace] openURL:[NSURL URLWithString:urlString]];
```

[Next](Using%20the%20Address%20Book%20C%20API.md)[Previous](Importing%20and%20Exporting%20Person%20and%20Group%20Records.md)

