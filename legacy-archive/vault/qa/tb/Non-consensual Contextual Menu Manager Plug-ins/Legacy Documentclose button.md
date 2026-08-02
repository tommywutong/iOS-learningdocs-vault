---
title: Non-consensual Contextual Menu Manager Plug-ins
apple_id: DTS10002245
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-02-08'
source_url: https://developer.apple.com/library/archive/qa/tb/tb59.html
archived_at: '2026-07-18T02:38:57.905835Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Human Interface Toolbox](https://developer.apple.com/referencelibrary/Carbon/idxHumanInterfaceToolbox-date.html)

|  |
| --- |
| Technical Q&A TB59Non-consensual Contextual Menu Manager Plug-ins |

|  |  |
| --- | --- |
| ---   __Q:__ Some applications fool my contextual menu plug-in into adding its menu items at inappropriate times. Then, when the user selects one of my items, my plug-in understandably gets confused when trying to extract the offered data and process it. What gives?  __A:__ This usually occurs as a result of both complex data in the descriptor offered to your plug-in and a bug in Apple Event Manager.  Sometimes an application will offer your plug-in a descriptor of `typeAERecord`. This kind of descriptor is really just a fancy descriptor list which associates a keyword with each list item. If your code doesn't detect that it has been passed a `typeAERecord`, it may attempt to do something which coerces it to another data type. The coercion may not be explicit; remember, asking for a descriptor list item as a specific type can implicitly coerce the item into the specified type. Coercion is ordinarily not a bad thing, but there are two reasons why it is bad in this case:   0. Apple Event Manager has a bug such that it will appear to    coerce `typeAERecord` to anything requested without    actually performing any coercion. 1. Since `typeAERecord` is a list, you'd be better off traversing its items to see what they are, rather than attempting to coerce the whole list into a single item.   So, suppose your plug-in is interested in processing file system objects (files, folders, volumes). It's probably going to want to determine whether it has been offered `typeAlias`. If it implicitly converts `typeAERecord` to `typeAlias`, it is not only going to exercise the bug in the Apple Event Manager and get confused, but even if the bug were not present, your plug-in would be throwing away an opportunity to process an an embedded list of `typeAlias` descriptors.  Here's some code which shows how to properly traverse embedded lists. A side-effect of this code is to avoid the Apple Event Manager bug.   |  | | --- | | ``` static pascal OSStatus SearchForAcceptableDescriptors     (DescType acceptableDescType, const AEDesc *desc, Boolean *allOK) {     OSStatus err = noErr;      *allOK = true;      if (desc->descriptorType != acceptableDescType)     {         if (desc->descriptorType == typeAERecord         || desc->descriptorType == typeAEList)         {             long index;              if (!(err = AECountItems (desc,&index)) && index) do             {                 AEDesc      nthDesc;                 AEKeyword   keyword;                 OSStatus    err2;                  err = AEGetNthDesc (desc,index,                         typeWildCard,&keyword,&nthDesc);                 if (err) break;                 err = SearchForAcceptableDescriptors(                           acceptableDescType,&nthDesc,allOK);                 err2 = AEDisposeDesc (&nthDesc);                 if (err) break;                 err = err2;                 if (err) break;                 if (!*allOK) break;             }             while (--index);         }         else         {             AEDesc coerced;              if (!(err = AECoerceDesc (desc,acceptableDescType,&coerced)))                 err = AEDisposeDesc (&coerced);             else if (err == errAECoercionFail)             {                 err = noErr;                 *allOK = false;             }         }     }      return err; } ``` |    To this function, you should pass the pointer to the descriptor offered to your plug-in, the descriptor type of the descriptors your plug-in is willing to process, and a pointer to a Boolean (which will be set according to whether the descriptor contains only descriptors of the specified type). When you take action on the descriptors, you'll need to recurse similarly. [Feb 08 1999] |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
