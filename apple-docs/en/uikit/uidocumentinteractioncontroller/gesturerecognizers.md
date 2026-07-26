---
title: gestureRecognizers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentinteractioncontroller/gesturerecognizers
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/gesturerecognizers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontroller/gesturerecognizers.json'
content_hash: 'sha256:2e82882e5630553d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionController](../uidocumentinteractioncontroller.md)

# gestureRecognizers

<sub>Instance Property</sub>

The system-supplied gesture recognizers for presenting a document interaction controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var gestureRecognizers: [UIGestureRecognizer] { get }
```

## Discussion

The objects in the `gestureRecognizers` array each descend from the [UIGestureRecognizer](../uigesturerecognizer.md) class. You can attach these gesture recognizers to the view you use to represent a document. For example, if you represent a document by name or icon in a table view cell , you can attach a document interaction controller’s gesture recognizers using code like this:

```objc
cell.contentView.gestureRecognizers = self.docInteractionController.gestureRecognizers;
```

(In this statement, the `cell` object is an instance of the [UITableViewCell](../uitableviewcell.md) class and the `docInteractionController` instance variable points to the document interaction controller for the document named in the cell.)

With gesture recognizers so attached, a user gesture automatically initiates the appropriate action. A tap gestures initiates a preview of the associated document. A long press gesture displays the options menu relevant to the document.

The [UIDocumentInteractionController](../uidocumentinteractioncontroller.md) class supports only the tap ([UITapGestureRecognizer](../uitapgesturerecognizer.md)) and long press ([UILongPressGestureRecognizer](../uilongpressgesturerecognizer.md)) gesture recognizers.
