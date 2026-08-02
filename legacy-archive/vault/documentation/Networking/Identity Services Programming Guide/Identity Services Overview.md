---
title: Identity Services Programming Guide
apple_id: TP40004490
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: Collaboration
published: '2012-02-16'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/IdentityServices_ProgGuide/architecture/architecture.html
archived_at: '2026-07-15T08:18:13.059734Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Identity Services Programming Guide](Introduction%20to%20Identity%20Services%20Programming%20Guide.md)


[Next](Using%20the%20Identity%20Picker.md)[Previous](Introduction%20to%20Identity%20Services%20Programming%20Guide.md)

# Identity Services Overview

To use the Identity Services APIs, it is important to know how identities work, and how they can be used. The following chapter describes the different types of identities and explains how to use them in OS X. It also explains the APIs available for using identities in your applications.

When most people think about a user account, they think about a home directory. However, a user account is much more complicated than that.

A user account, or _user_, works in a similar manner to a debit card. You normally think of your debit card as a method to purchase items. When you go to a store, you find what you want to buy and hand it to the cashier along with your debit card. The cashier scans the card, and makes sure your PIN number matches what the bank has on file. Assuming it does, you receive your items and walk out.

A user account on a computer works in a similar fashion. When you log into the computer, the computer asks for a user name and password. The user name is like the debit card number, it specifies who you are. The password is like your PIN number, because it proves you are who you say you are. After you’re approved, the computer can give you access to your files.

But what is really happening when you use your debit card? When the cashier scans the card, the debit card number is sent to the bank. The bank has information about you, such as your name, birthday, social security number, and balance. The bank then tells the cashier whether the card is valid, so he knows if you can buy the item. The basis of the account is really the information stored on the computers at your bank, not the card itself.

In much the same way, a user is defined by its _identity_, which is a record that contains information about the user. Each identity is stored in a trusted directory known as an _identity authority_. Your user name is sent to the identity authority and your record is found. Then, if your password matches that on the record, you can get access to any file that your identity has access to.

Each identity contains the following required attributes:

- A universally unique identifier (UUID)
- A full name (must be unique throughout the system)
- A POSIX ID (UID for a user, GID for a group)
- A systemwide unique name (POSIX name)

Additionally, identities can contain the following optional attributes:

- A home directory (only for users)
- Alternate names, known as aliases
- An email address
- An image

You can edit these attributes using the Accounts preference pane in System Preferences by Control-clicking on the user. See Figure 1-1.

__Figure 1-1__  Advanced user options

!

Fundamentally, identities are used to control who has access to files and services. If you view the Get Info panel on a file in the Finder, you’ve seen the Ownership and Permissions section (Figure 1-2). This section displays what access users and groups have to the file or folder. These permissions (no access, read only, or read and write) are stored in an _access control list_ (ACL). Every single folder and file on your computer has an associated ACL. Thus you can create very specific, customized access permissions for the files on your computer.

__Figure 1-2__  Ownership and permissions panel

!

Each sharing service (for example, SSH or AFP) on your computer also has an ACL. An ACL associated with a service is referred to as a _service access control list_, or SACL. The ability to create and customize ACLs and SACLs with users and groups helps make very secure, very adjustable applications.

An identity can represent either a user or group:

A _user_ is an identity that has _authentication credentials_. There are two forms of credentials: a traditional password, and a certificate. A user can be added to ACLs to access files or services. There are four different types of users: administrators, standard, child, and sharing. The list of user types and their features is available in Figure 1-3.

__Figure 1-3__  User properties

!

A _group_ is an identity that has other identities as members. Groups can be added to ACLs and provide a powerful way to manage permissions. A group can contain an unlimited number of members.

There are two levels to the Identity Services APIs: the C-based Core Services Identity API and the Objective-C-based Collaboration framework. The Core Services Identity API is comprised of three Core Foundation-based objects that allow you to create, manipulate, and remove users and groups: an identity object, an identity query object, and an identity authority object. The Collaboration framework is a set of wrapper classes for the Core Services Identity API objects. Additionally, it provides user interface support for applications.

An _identity object_ (`CSIdentity`) represents an identity in an identity authority and contains the attributes of that user or group. The required attributes are a full name, a POSIX name, a UUID, and a POSIX ID. Of these attributes, the POSIX name, the UUID and the POSIX ID can all be autogenerated by the API. User identities also include authentication information (password and/or certificate), and group identities have a list of members. These attributes can be set and retrieved using the appropriate methods, and the user or group represented by the identity object can be stored in the identity’s authority database using a commit method. Each instantiation of the identity class represents one user or group. Identity objects are not limited to sharing users but can also be used to access standard users.

An _identity query_ object (`CSIdentityQuery`) allows an application to search an identity authority database for users and groups and monitor them for changes. It provides methods for searching for identities by name, UUID, POSIX ID, reference data, or current user. In addition, an identity query object can register to be notified for changes to an identity. For example, if you have an identity object that represents a group, you can use an identity query object to notify you when the group membership changes.

An _identity authority object_  (`CSIdentityAuthority`) represents a repository of identities. Every OS X system contains a local identity authority that stores the identities local to the system. When you first create a user on a brand new OS X system, the user identity is stored in the local identity authority. An identity authority can also exist on a network directory server. An identity authority object can represent either the local authority, the network-bound authorities, or both.

For a visual representation of how `CSIdentity` objects and `CSIdentityQuery` objects interact with an identity authority, see Figure 1-4.

__Figure 1-4__  Identity class interaction

!

The Collaboration framework allows you to access identities with Objective-C APIs. It also houses the the Identity Picker user interface element. The `CBIdentity` and `CBIdentityAuthority` APIs provide the read-only access to attributes of the `CSIdentity` and `CSIdentityAuthority` objects.

The Collaboration framework also has methods to convert between the `CSIdentity` objects and `CBIdentity` objects. If you have a `CSIdentity` object and want to use it in Cocoa, use the `identityWithCSIdentity:` class factory method to create a `CBIdentity` object from the same identity. Similarly, if you have a `CBIdentity` object and want to use it in C, use the `CSIdentity` method on the identity object to return a `CSIdentity` object from the same identity.

The Identity Picker’s relationship with Identity Services is analogous to the People Picker’s relationship with the Address Book. Just as the People Picker is a user interface element for selecting a person from the Address Book, the Identity Picker is a user interface element for selecting identities. The Identity Picker is a sheet or a modal dialog that allows someone to select users on the system and promote Address Book entries to sharing users. It is managed by a `CBIdentityPicker` object. More information about the Identity Picker is available in [Using the Identity Picker](Using%20the%20Identity%20Picker.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diojqfvbuqnjnknlti). The class hierarchy of the Collaboration framework can be seen in Figure 1-5.

__Figure 1-5__  Identity Services class hierarchy

!

With a strong understanding of the structure of identities, you’ll find the APIs much easier to use, and more powerful.

[Next](Using%20the%20Identity%20Picker.md)[Previous](Introduction%20to%20Identity%20Services%20Programming%20Guide.md)

