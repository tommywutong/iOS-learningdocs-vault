---
title: Navigation Services Programming Guide
apple_id: TP30001147
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-07-10'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProvidingNavigationDialogs/nsx_intro/nsx_intro.html
archived_at: '2026-07-15T05:24:20.387964Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Navigation%20Services%20Concepts.md)

# Introduction to Navigation Services Programming Guide

Navigation Services is an application programming interface that allows your application to provide a user interface for navigating to, opening, and saving Mac OS files. Navigation Services displays a dialog that allows the user to navigate to a location. After the user responds to the dialog by choosing a file, setting a save location, or canceling the dialog, Navigation Services provides the information your application needs to comply with the user action.

This document is for application developers who want to use Navigation Services for such tasks as opening and saving files and choosing files. Those who plan to implement custom features in Navigation Services dialogs will also find this document useful.

This document contains the following chapters:

- [Navigation Services Concepts](Navigation%20Services%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbxfvbuqmrqgiwugskijfduuskf) describes the user interface for navigation dialogs in Mac OS X, describes user settings and how they are handled, and provides an overview of the programming model.
- [Navigation Services Tasks](Navigation%20Services%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbxfvbuqmrqgmwueqkci5eucr2h) gives guidelines for using the Navigation Services API, outlines the programming steps you must take to provide navigation dialogs, lists sample functions with explanations of what the code does, and discusses ways you can customize navigation dialogs.

- Navigation Services Reference provides a complete reference for the Navigation Services application programming interface.
- _Apple Human Interface Guidelines_ contains guidelines for you to follow if you plan to customize the navigation dialogs provided by Navigation Services. It also lists examples of Open and Save dialogs that are not in [Navigation Services Concepts](Navigation%20Services%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbxfvbuqmrqgiwugskijfduuskf).
- _File Manager Reference_ provides a complete reference for the File Manager application programming interface. You use the File Manager API to open, save, and close the files users navigate to with the navigation dialogs.
[Next](Navigation%20Services%20Concepts.md)

