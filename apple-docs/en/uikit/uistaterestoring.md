---
title: UIStateRestoring
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistaterestoring
source_url: 'https://developer.apple.com/documentation/uikit/uistaterestoring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistaterestoring.json'
content_hash: 'sha256:bd56dab216a9cd6d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIStateRestoring

<sub>Protocol</sub>

Methods for adding objects to your state restoration archives.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIStateRestoring : NSObjectProtocol
```

## Overview

You can add state restoring objects to an archive directly or by referencing them from another object that’s preserved, such as a view controller. The methods of the protocol let you save enough information about the object to find or recreate it during the next launch cycle.

When adopting this protocol in your custom objects, you must also remember to register those objects using the [+ registerObjectForStateRestoration:restorationIdentifier:](<uiapplication/registerobject(forstaterestoration_restorationidentifier_).md>) method of the [UIApplication](uiapplication.md) class. You don’t need to register views or view controllers explicitly because UIKit registers those objects automatically. View controllers adopt this protocol so that they may be used as the restoration parent of one of your custom objects.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIActivityViewController](uiactivityviewcontroller.md), [UIAlertController](uialertcontroller.md), [UICloudSharingController](uicloudsharingcontroller.md), [UICollectionViewController](uicollectionviewcontroller.md), [UIColorPickerViewController](uicolorpickerviewcontroller.md), [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md), [UIDocumentMenuViewController](uidocumentmenuviewcontroller.md), [UIDocumentPickerExtensionViewController](uidocumentpickerextensionviewcontroller.md), [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md), [UIDocumentViewController](uidocumentviewcontroller.md), [UIFontPickerViewController](uifontpickerviewcontroller.md), [UIImagePickerController](uiimagepickercontroller.md), [UIInputViewController](uiinputviewcontroller.md), [UINavigationController](uinavigationcontroller.md), [UIPageViewController](uipageviewcontroller.md), [UIReferenceLibraryViewController](uireferencelibraryviewcontroller.md), [UISearchContainerViewController](uisearchcontainerviewcontroller.md), [UISearchController](uisearchcontroller.md), [UISplitViewController](uisplitviewcontroller.md), [UITabBarController](uitabbarcontroller.md), [UITableViewController](uitableviewcontroller.md), [UITextFormattingViewController](uitextformattingviewcontroller.md), [UIVideoEditorController](uivideoeditorcontroller.md), [UIViewController](uiviewcontroller.md)

## Topics

### Accessing the object information

- [restorationParent](uistaterestoring/restorationparent.md) — The parent object used to scope the current object.
- [objectRestorationClass](uistaterestoring/objectrestorationclass.md) — The class responsible for creating this object when restoring the app’s state.

### Encoding and decoding the object

- [- encodeRestorableStateWithCoder:](<uistaterestoring/encoderestorablestate(with_).md>) — Encodes state-related information for the object.
- [- decodeRestorableStateWithCoder:](<uistaterestoring/decoderestorablestate(with_).md>) — Decodes and restores state-related information for the object.
- [- applicationFinishedRestoringState](<uistaterestoring/applicationfinishedrestoringstate().md>) — Called after all objects have had a chance to decode their state.

### Constants

- [State restoration keys](state-restoration-keys.md) — Keys that are available in restoration archives.

## See Also

### Interface restoration

- [Restoring your app’s state](restoring-your-app-s-state.md) — Provide continuity for the user by preserving current activities.
- [Restoring your app’s state with SwiftUI](../swiftui/restoring-your-app-s-state-with-swiftui.md) — Provide app continuity for users by preserving their current activities.
- [Preserving your app’s UI across launches](preserving-your-app-s-ui-across-launches.md) — Return your app to its previous state after the system terminates it.
- [UIViewControllerRestoration](uiviewcontrollerrestoration.md) — The methods that objects adopt so that they can act as a restoration class for view controllers during state restoration.
- [UIObjectRestoration](uiobjectrestoration.md) — The interface that restoration classes use to restore preserved objects.
