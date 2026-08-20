---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/Introduction.html
archived_at: '2026-07-15T08:14:39.611528Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

# WebObjectsExtensions Component Specifications

## Introduction

The WebObjects Extensions are non-synchronizing reusable components
defined in the WebObjects Extensions Framework, which is included
in every WebObjects Application project. Feel free to examine the
source code for this framework available at `Developer/Examples/WebObjects/Source/WOExtensions` relative
to the directory in which you installed WebObjects.

For more information about reusable components see "Creating
Reusable Components" in the _WebObjects Developer's
Guide_.

Here are the WebObjects Extensions defined in the WebObjects
Extensions Framework:

: [JSAlertPanel](JSAlertPanel.md#apple-ijaucq2eineei)
: [JSConfirmPanel](JSConfirmPanel.md#apple-indekqseijdui)
: [JSImageFlyover](JSImageFlyover.md#apple-ineeerkbizeeu)
: [JSModalWindow](JSModalWindow.md#apple-ijeuiq2ciffeu)
: [JSTextFlyover](JSTextFlyover.md#apple-ijbesrkcifauu)
: [JSValidatedField](JSValidatedField.md#apple-ijduorchi5duq)
: [WOAnyField](WOAnyField.md#apple-infecrcgivdeq)
: [WOAppleScript](WOAppleScript.md#apple-ijeugqsfiffem)
: [WOBatchNavigationBar](WOBatchNavigationBar.md#apple-incuoq2direuq)
: [WOCheckboxMatrix](WOCheckboxMatrix.md#apple-infeqqsgivaue)
: [WOCollapsibleComponentContent](WOCollapsibleComponentContent.md#apple-ijbeoq2jjbbek)
: [WOCompletionBar](WOCompletionBar.md#apple-ijdemqski5eue)
: [WODictionaryRepetition](WODictionaryRepetition.md#apple-ijaucrchirbuo)
: [WOEventDisplayPage](WOEventDisplayPage.md#apple-inbeorcfijfek)
: [WOEventSetupPage](WOEventSetupPage.md#apple-ijdumqsgincuk)
: [WOIFrame](WOIFrame.md#apple-ijauerccineuo)
: [WOKeyValueConditional](WOKeyValueConditional.md#apple-incucqsfjfeus)
: [WOMetaRefresh](WOMetaRefresh.md#apple-ijdeercgjjduq)
: [WOPageRestorationErrorPage](WOPageRestorationErrorPage.md#apple-inbeorkcizeuk)
: [WORadioButtonMatrix](WORadioButtonMatrix.md#apple-incemrckjfdeg)
: [WORedirect](WORedirect-2.md#apple-inbuuq2fiveuc)
: [WOSessionCreationErrorPage](WOSessionCreationErrorPage.md#apple-inbeorckjbaug)
: [WOSessionRestorationErrorPage](WOSessionRestorationErrorPage.md#apple-ijeeiq2iireui)
: [WOSimpleArrayDisplay](WOSimpleArrayDisplay.md#apple-incumqsbjbaui)
: [WOSimpleArrayDisplay2](WOSimpleArrayDisplay2.md#apple-ijcusrciiraug)
: [WOSortOrder](WOSortOrder.md#apple-inceqq2jjjcee)
: [WOSortOrderManyKey](WOSortOrderManyKey.md#apple-ijbecq2kjfeuu)
: [WOStatsPage](WOStatsPage.md#apple-ineesrcfifaue)
: [WOTable](WOTable.md#apple-ijbesq2fi5cuu)
: [WOTabPanel](WOTabPanel.md#apple-indekqskifdec)
: [WOThresholdColoredNumber](WOThresholdColoredNumber.md#apple-ijbesq2gi5ceg)
: [WOToManyRelationship](WOToManyRelationship.md#apple-incukq2jizeum)
: [WOToOneRelationship](WOToOneRelationship.md#apple-ineeuqsdivcug)

## How to Use These Specifications

Each component specification that follows is divided into
three sections: a synopsis, a description, and a set of bindings.
The synopsis is designed to give you ready reference to the element's
attributes, showing which ones are mandatory and which ones optional.
The description explains the purpose of the element. Finally, the
bindings describe in detail each of the component's attributes.

The synopses use several conventions that you should be aware
of. For example:

> ```
> WOSubmitButton { action=submitForm; value=aString; [disabled=YES|NO;] [name=aName;] };
> ```

- _Italic_ denotes
  words that represent something else or that can be varied. For example, _submitForm_ represents
  a method in your script-the exact name of the method is your choice.
- Square brackets ([ ]) mean that the enclosed attribute or
  attributes are optional. The name attribute and its value are optional
  in the synopsis above.
- A vertical bar (|) separates two options that are mutually
  exclusive, as in `disabled=YES|NO` where the
  attribute's value must be either `YES` or `NO`.
- The remaining words or characters are to be taken literally
  (that is, they should be typed as they appear). For example, the __action__ and __value__ attributes
  are to be take literally in the synopsis above.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
