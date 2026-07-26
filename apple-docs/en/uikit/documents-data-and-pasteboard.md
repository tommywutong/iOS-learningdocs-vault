---
title: Documents, data, and pasteboard
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/documents-data-and-pasteboard
source_url: 'https://developer.apple.com/documentation/uikit/documents-data-and-pasteboard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/documents-data-and-pasteboard.json'
content_hash: 'sha256:5b3253276b823117'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# Documents, data, and pasteboard

<sub>API Collection</sub>

Organize your app’s data and share that data on the pasteboard.

## Topics

### Documents

- [UIDocument](uidocument.md) — An abstract base class for managing discrete portions of your app’s data.
- [UIManagedDocument](uimanageddocument.md) — A managed document object that integrates with Core Data.
- [Synchronizing documents in the iCloud environment](synchronizing-documents-in-the-icloud-environment.md) — Manage documents across multiple devices to create a seamless editing and collaboration experience.

### Document presentation

- [UIDocumentViewController](uidocumentviewcontroller.md) — A view controller that manages and presents a document stored locally or in the cloud.

### Data management

- [UIDataSourceModelAssociation](uidatasourcemodelassociation.md) — A set of methods that defines an interface for providing persistent references to data objects in your app.

### Pasteboard

- [UIPasteControl](uipastecontrol.md) — A button that a person taps to place pasteboard contents in your app.
- [Configuration](uipastecontrol/configuration-swift.class.md) — An object that determines a paste button’s color, corner style, icon, and text.
- [DisplayMode](uipastecontrol/displaymode.md) — Options that determine whether a paste button composes an icon, textual label, or both.
- [UIPasteboard](uipasteboard.md) — An object that helps a user share data from one place to another within your app, and from your app to other apps.
- [UIPasteConfiguration](uipasteconfiguration.md) — The interface that an object implements to declare its ability to accept specific data types for pasting and for drag-and-drop activities.
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md) — The interface that determines whether a responder object supports paste configuration.

## See Also

### App structure

- [App and environment](app-and-environment.md) — Manage life-cycle events and your app’s UI scenes, and get information about traits and the environment in which your app runs.
- [Resource management](resource-management.md) — Manage the images, strings, storyboards, and nib files that you use to implement your app’s interface.
- [App extensions](app-extensions.md) — Extend your app’s basic functionality to other parts of the system.
- [Interprocess communication](interprocess-communication.md) — Display activity-based services to people.
- [Mac Catalyst](mac-catalyst.md) — Create a version of your iPad app that users can run on a Mac device.
