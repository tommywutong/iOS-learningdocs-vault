---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/WOBatchNavigationBar.html
archived_at: '2026-07-15T08:14:40.124847Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# WOBatchNavigationBar

## Component Description

The WOBatchNavigationBar component provides the ability to
navigate through a WODisplayGroup in batches. The component has
buttons that allow the user to navigate to the next batch and to
the previous batch. It also displays the number of batches, which
batch the user is currently viewing, and how many objects are in
each batch.

![[image: Art/WOExtWOBatchNavigationBar.gif]](Art/WOExtWOBatchNavigationBar.gif)

## Synopsis

WOBatchNavigationBar { displayGroup=_aDisplayGroup_;
sortKeyList=_anArray_;
objectName=_aString_;
[width=_aNumber_;] [textColor=_hexString_;]
[border=_aString_;]
[bgcolor=_hexString_;]
};

## Bindings

**displayGroup**
: The display group that the WONavigation bar displays
in batches.

**sortKeyList**
: Array of keys for the attributes by which the displayed
objects can be sorted. The user chooses one of these attributes
and a sort ordering (ascending or descending), and the navigation
bar displays the batches accordingly.

**objectName**
: The name of the object displayed by the display group.
The navigation bar displays this name.

**width**
: Width of the navigation bar. This attribute is passed
to the HTML `TABLE` that
makes up the navigation bar.

**textColor**
: Color of the text within the bar.

**border**
: Width of the navigation bar's border. This attribute
is passed to the `TABLE` that
makes up the navigation bar.

**bgcolor**
: Background color of the navigation bar. This attribute
is passed to the `TABLE` that
makes up the navigation bar.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)
