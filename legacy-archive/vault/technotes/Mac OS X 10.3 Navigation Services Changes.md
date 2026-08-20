---
title: Mac OS X 10.3 Navigation Services Changes
apple_id: DTS10003196
resource_type: Technical Note
platform: macOS
topic: null
technology: null
published: '2004-01-30'
source_url: https://developer.apple.com/library/archive/technotes/tn2105/_index.html
archived_at: '2026-07-26T19:53:50.412531Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



# Retired Document

__Important:__
This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Technical Note TN2105

# Mac OS X 10.3 Navigation Services Changes

__Important:__ This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

In Mac OS X 10.3, aka Panther, the Navigation Services have gone through a lot of changes, both for the end-user and for the developer. Great effort was undertaken to ensure maximum compatibility with the previous versions but this compatibility is achieved only by respecting the documented programming interfaces. The Navigation Services Application Programming Interfaces (APIs) are still the same but this new implementation requires that you use them properly. This Technical Note describes the changes in Navigation Services in Mac OS X 10.3 and reiterates the compatibility rules.

[Dialogs items no more](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmjzgywugsbrfvjukq2ujfhu4mi)[The Custom Area](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmjzgywugsbrfvjukq2ujfhu4mq)[nibs and DITLS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmjzgywugsbrfvjukq2ujfhu4my)[Summary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmjzgywugsbrfvjukq2ujfhu4na)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmjzgywvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Dialogs items no more

In Mac OS X 10.3, the Navigation Services user interface was completely redesigned and now takes advantage of the HIView architecture and compositing windows. The most important consequence of this is that the Navigation Services standard items are no longer dialog items even though, as the API names suggest (for example `NavCreateGetFileDialog` , `NavDialogRun` , and so on), the windows themselves are still dialogs.

Even when the Navigation Services standard items were dialog items in Mac OS X 10.2 and earlier, Apple has always recommended that developers do not handle these standard Navigation Services items such as the "Open", "Save", "Choose", or "Cancel" buttons and other elements with the Dialog Manager APIs but use instead the Navigation Services APIs wherever possible.

Since the Navigation Services standard items are not dialog items anymore, all developer code attempting to manage these Navigation Services standard items through the Dialog Manager APIs (for example `GetDialogItem` , `GetDialogItemAsControl` , and so on) will fail.

Those items can still be managed with the Control Manager APIs or the HIView APIs but Apple's recommendation is that the Navigation Services APIs should always be used wherever possible (for example using `NavCustomControl` with the `kNavCtlSetActionState` message and any of the `kNavDontXxxState` parameters to enable and disable the standard buttons rather than looking heuristically for the appropriate control and then using `EnableControl` and `DisableControl` , or setting the labels of those standard buttons through the `NavDialogOptions` or `NavDialogCreationOptions` ).

Also, the correct way to add your own items to extend the Navigation Services Dialogs, is to use the Navigation Services API `NavCustomControl` , with either the `kNavCtlAddControl` or the `kNavCtlAddControlList` messages, when and only when the `kNavCBStart` message is sent to your EventProc.

Apple strongly recommends that you do not add controls when you deal with other messages and particularly not when you receive the `kNavCBCustomize` message (the `kNavCBCustomize` message is sent to you for area sizing only and will be sent many times over the life of the Navigation Services window). Trying to figure out the current number of items in the Navigation Services window with `CountDITL` and/or to add items with the `AutoEmbedControl` API will both fail.

[Back to Top](#)

## The Custom Area

In an effort to ensure compatibility with existing applications, the custom area of the Navigation Services windows will still act as if it were a part of a non-compositing dialog window and all Dialog Manager APIs should work on these custom items (including `GetDialogItemAsControl` ). In order to handle item numbering correctly, it is necessary to use `NavCustomControl` with the `kNavCtlGetFirstControlID` message since any other method relying incorrectly on `CountDITL` will fail.

All elements added to the custom area will be embedded in a special non-compositing user pane. Since this user pane is non-compositing, you must not attempt to write special code for compositing and non-compositing by checking the `kWindowCompositingAttribute` of the Navigation Service window. For now, in the temporary absence of compositing custom areas, it is best that your custom area items just assume that they reside in a non-compositing window as it was in the past and do not attempt to take advantage of the compositing functionality of the window itself.

Even though the custom area is non-compositing, the following practices will make your items better citizens for an eventual fully composited world:

1. Avoid erasing behind items (in most cases you are going to draw the items so erasing is unnecessary).
2. If erasing is unavoidable then don't hardcode the background brush but use `SetUpControlBackground` which will apply the correct background set up by Navigation Services just before your code was called.
3. Do not explicitly draw your controls in the custom area since the Navigation Services will draw all visible controls (including yours) of its windows.

[Back to Top](#)

## nibs and DITLS

Navigation Services windows are now nib-based (that is, created via Interface Builder) and no longer DITL- or resource-based. Although the custom area can still be managed through a DITL and added through `NavCustomControl` with the `kNavCtlAddControlList` message, developers can also use a nib-based custom area which has to be added through `NavCustomControl` with the `kNavCtlAddControl` message. A complete sample code [AddNibToNav](https://developer.apple.com/samplecode/Sample_Code/Human_Interface_Toolbox/Mac_OS_X_HIToolbox/AddNibToNav.htm) illustrating this use of nibs is available in our Sample Code section.

[Back to Top](#)

## Summary

- Using the Navigation Services APIs has always been and still is the recommended way to interact with the Navigation Services windows and their elements.
- Using the Dialog Manager APIs for any non-custom area item has always been discouraged and is not supported by Mac OS X 10.3.
- Using the Control Manager or HIView APIs for any non-custom area item still works but is still discouraged in favor of the Navigation Services APIs where applicable.
- Using Dialog Manager, Control Manager, and HIView APIs for all custom area items still works as before.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-01-30 | New document that explains Navigation Services changes in Mac OS X 10.3 Panther |

