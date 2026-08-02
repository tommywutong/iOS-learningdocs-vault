---
title: PC Card 3.x Custom Actions
apple_id: DTS10001179
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-10-25'
source_url: https://developer.apple.com/library/archive/qa/dv/dv38.html
archived_at: '2026-07-18T02:29:27.866515Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > PCI and PC Card](https://developer.apple.com/referencelibrary/HardwareDrivers/idxPCIandPCCard-date.html)

|  |
| --- |
| Technical Q&A DV38PC Card 3.x Custom Actions |

|  |  |  |
| --- | --- | --- |
| ---   Q: How do you implement a custom action in PC Card Manager 3.x? When the user double-clicks our card's desktop icon, we want to open up our card's application. In PC Card Manager 2.x, this was easily done by responding to the `kCSActionProcSubfunction` message, but this isn't present in PC Card Manager 3.x.  A: You do this by means of a special resource in your custom card enabler file. The resource is of type `'pccd'` and is loaded by name. The resource name must match the card name, as returned by `PCCardGetCardInfo`.  The resource's format is defined by the `PCCardCustomResource`, which is declared in "PCCardEnablerPlugin.h" in Universal Interfaces. A copy of the definition is given below for your convenience.   |  | | --- | | ``` struct PCCardCustomResource {     long                            version;     short                           customIconID;     short                           customStringsID;     short                           customTypeStringIndex;     short                           customHelpStringIndex;     OSType                          customAction;     long                            customActionParam1;     long                            customActionParam2; }; typedef struct PCCardCustomResource PCCardCustomResource; ``` |    The fields are defined as follows:   - `version` - This field must be set to   `kPCCardCustomInfoVersion` (0). - `customIconID` - This field must contain the resource ID of an icon   suite in your custom card enabler file, or -1. If it   contains an icon resource ID, the Finder displays that   icon to represent your card on the desktop. If it   contains -1, the Finder does not display an icon for your   card. In that case, the remaining fields in the   `'pccd'` resource are ignored (you should set   them to 0). - `customStringsID` - This field must contain the ID of a   `'STR#'` resource in your custom card enabler   file. - `customTypeStringIndex` - This field must contain the index in the above   `'STR#'` resource of the user-visible card   type string for your card. - `customHelpStringIndex` - This field must contain the index in the above   `'STR#'` resource of the help string for your   card. - `customAction` - This field must contain a `FindFolder`   selector of the folder containing the custom action   application for your card, or 0 to define no custom   action. - `customActionParam1` - This field must contain the __creator   code__ of your custom action application, or 0   when you are using no custom action. - `customActionParam2` - This field must contain the __file   type__ of your custom action application, or 0   when you are using no custom action. The file type must   be "launchable," that is, one of the standard   application-like file types that a user can launch in the   Finder. For example, `'APPL'` and   `'APPC'` are acceptable, but   `'appe'` is not.   When the user double-clicks your PC Card on the desktop, the Finder will look for an application of type `customActionParam2` and creator `customActionParam1` in the folder that `FindFolder` returns when called with `customAction` as the `folderType` parameter. The Finder will then launch that application as it would launch any other. Your custom action application will typically present a user interface directly, but it might just launch some other application and script its user interface. The choice is yours.  The following Rez code builds a `'pccd'` resource that specifies a custom action, in this case to launch an application of type `'APPC'` and creator `'Frog'` in the Control Panels folder.    |  | | --- | | ``` #include "MacTypes.r" #include "Folders.r" #include "PCCardEnablerPlugin.r"   resource 'pccd' (0, "Frog Card Name") {     kPCCardCustomInfoVersion,     128,                        // resource ID of icon suite     128,                        // resource ID of 'STR#'     1,                          // type string     2,                          // help string     kControlPanelFolderType,    // custom action in Control Panels folder     'Frog',                     // custom action creator code     'APPC'                      // custom action file type };   resource 'STR#' (128) {     {         "Frog PC Card",         "Frog PC Card\n\n"          "This PC Card allows your computer to nee-deep."     } }; ``` | |

#### [Oct 05 1999]

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

---
