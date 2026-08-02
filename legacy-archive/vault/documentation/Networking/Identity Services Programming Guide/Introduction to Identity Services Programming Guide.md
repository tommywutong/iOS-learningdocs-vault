---
title: Identity Services Programming Guide
apple_id: TP40004490
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: Collaboration
published: '2012-02-16'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/IdentityServices_ProgGuide/Introduction/Introduction.html
archived_at: '2026-07-15T08:18:13.033478Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Identity%20Services%20Overview.md)

# Introduction to Identity Services Programming Guide

Identity Services is a new technology in OS X v10.5 that allows developers to access users and groups on a system in order to create customized access controls. Identity Services also introduces a new type of user, known as a sharing user. Sharing users are similar to standard users but do not have login access or a home directory. They are designed for users who only need access to network services such as file sharing or screen sharing.

Identity Services provides access to users and groups through two APIs. The Core Services Identity API supports user and group creation, enumeration, attribute inspection, credential management, and group membership management. The Collaboration framework is an Objective-C API providing access to identities, as well as managing a user interface element for selecting identities. All of these features can be combined for use in managing access control lists (ACLs).

This book describes the Identity Services architecture and explains how to leverage that architecture in new and existing Cocoa and Carbon applications. It is intended both for developers who want to use the Identity Services API and for system administrators who want to understand the infrastructure for users, groups, and access control lists.

This book contains the following chapters:

- [Identity Services Overview](Identity%20Services%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diojqfvbuqmznknlte) describes the underlying structure of Identity Services.
- [Using the Identity Picker](Using%20the%20Identity%20Picker.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diojqfvbuqnjnknlti) explains how to select and create identities in a GUI-based application.
- [Finding and Monitoring Identities](Finding%20and%20Monitoring%20Identities.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diojqfvbuqnrnknltc) explains how to search for identities using the `CSIdentityQuery` and `CBIdentity` classes.
- [Working with Access Control Lists](Working%20with%20Access%20Control%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diojqfvbuqnznknltg) explains how to create, store, and load an ACL.

Refer to the following reference documents for Identity Services:

- _Identity Services Reference Collection_
- _[Collaboration Framework Reference](https://developer.apple.com/documentation/collaboration)_
- _[Core Services Identity Reference](../Core%20Services%20Identity%20Reference/Core%20Services%20Identity%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmnzt)_
[Next](Identity%20Services%20Overview.md)

