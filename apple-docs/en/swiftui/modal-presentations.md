---
title: Modal presentations
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/modal-presentations
source_url: 'https://developer.apple.com/documentation/swiftui/modal-presentations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modal-presentations.json'
content_hash: 'sha256:f6c88f816da532b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Modal presentations

<sub>API Collection</sub>

Present content in a separate view that offers focused interaction.

## Overview

To draw attention to an important, narrowly scoped task, you display a modal presentation, like an alert, popover, sheet, or confirmation dialog.

![](../../../attachments/669dc3d73261bcf3bda09c163d0c4f64/modal-presentations-hero@2x.png)

In SwiftUI, you create a modal presentation using a view modifier that defines how the presentation looks and the condition under which SwiftUI presents it. SwiftUI detects when the condition changes and makes the presentation for you. Because you provide a [Binding](binding.md) to the condition that initiates the presentation, SwiftUI can reset the underlying value when the user dismisses the presentation.

For design guidance, see [Modality](../design/human-interface-guidelines/modality.md) in the Human Interface Guidelines.

## Topics

### Configuring a dialog

- [DialogSeverity](dialogseverity.md) — The severity of an alert or confirmation dialog.

### Showing a sheet, cover, or popover

- [sheet(isPresented:onDismiss:content:)](<view/sheet(ispresented_ondismiss_content_).md>) — Presents a sheet when a binding to a Boolean value that you provide is true.
- [sheet(item:onDismiss:content:)](<view/sheet(item_ondismiss_content_).md>) — Presents a sheet using the given item as a data source for the sheet’s content.
- [fullScreenCover(isPresented:onDismiss:content:)](<view/fullscreencover(ispresented_ondismiss_content_).md>) — Presents a modal view that covers as much of the screen as possible when binding to a Boolean value you provide is true.
- [fullScreenCover(item:onDismiss:content:)](<view/fullscreencover(item_ondismiss_content_).md>) — Presents a modal view that covers as much of the screen as possible using the binding you provide as a data source for the sheet’s content.
- [popover(item:attachmentAnchor:arrowEdge:content:)](<view/popover(item_attachmentanchor_arrowedge_content_).md>) — Presents a popover using the given item as a data source for the popover’s content.
- [popover(isPresented:attachmentAnchor:arrowEdge:content:)](<view/popover(ispresented_attachmentanchor_arrowedge_content_).md>) — Presents a popover when a given condition is true.
- [PopoverAttachmentAnchor](popoverattachmentanchor.md) — An attachment anchor for a popover.

### Adapting a presentation size

- [presentationCompactAdaptation(horizontal:vertical:)](<view/presentationcompactadaptation(horizontal_vertical_).md>) — Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [presentationCompactAdaptation(_:)](<view/presentationcompactadaptation(__).md>) — Specifies how to adapt a presentation to compact size classes.
- [PresentationAdaptation](presentationadaptation.md) — Strategies for adapting a presentation to a different size class.
- [presentationSizing(_:)](<view/presentationsizing(__).md>) — Sets the sizing of the containing presentation.
- [PresentationSizing](presentationsizing.md) — A type that defines the size of the presentation content and how the presentation size adjusts to its content’s size changing.
- [PresentationSizingRoot](presentationsizingroot.md) — A proxy to a view provided to the presentation with a defined presentation size.
- [PresentationSizingContext](presentationsizingcontext.md) — Contextual information about a presentation.

### Configuring a sheet’s height

- [presentationDetents(_:)](<view/presentationdetents(__).md>) — Sets the available detents for the enclosing sheet.
- [presentationDetents(_:selection:)](<view/presentationdetents(__selection_).md>) — Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [presentationContentInteraction(_:)](<view/presentationcontentinteraction(__).md>) — Configures the behavior of swipe gestures on a presentation.
- [presentationDragIndicator(_:)](<view/presentationdragindicator(__).md>) — Sets the visibility of the drag indicator on top of a sheet.
- [PresentationDetent](presentationdetent.md) — A type that represents a height where a sheet naturally rests.
- [CustomPresentationDetent](custompresentationdetent.md) — The definition of a custom detent with a calculated height.
- [PresentationContentInteraction](presentationcontentinteraction.md) — A behavior that you can use to influence how a presentation responds to swipe gestures.

### Styling a sheet and its background

- [presentationCornerRadius(_:)](<view/presentationcornerradius(__).md>) — Requests that the presentation have a specific corner radius.
- [presentationBackground(_:)](<view/presentationbackground(__).md>) — Sets the presentation background of the enclosing sheet using a shape style.
- [presentationBackground(alignment:content:)](<view/presentationbackground(alignment_content_).md>) — Sets the presentation background of the enclosing sheet to a custom view.
- [presentationBackgroundInteraction(_:)](<view/presentationbackgroundinteraction(__).md>) — Controls whether people can interact with the view behind a presentation.
- [PresentationBackgroundInteraction](presentationbackgroundinteraction.md) — The kinds of interaction available to views behind a presentation.

### Presenting an alert

- [AlertScene](alertscene.md) — A scene that renders itself as a standalone alert dialog.
- [alert(_:isPresented:actions:)](<view/alert(__ispresented_actions_).md>) — Presents an alert when a given condition is true, using a localized string resource for the title.
- [alert(_:isPresented:presenting:actions:)](<view/alert(__ispresented_presenting_actions_).md>) — Presents an alert using the given data to produce the alert’s content and a localized string resource for a title.
- [alert(_:item:actions:)](<view/alert(__item_actions_).md>) — Presents an alert using the given data to produce the alert’s content and a text view as a title.
- [alert(error:actions:)](<view/alert(error_actions_).md>) — Presents an alert when an error is present.
- [alert(isPresented:error:actions:)](<view/alert(ispresented_error_actions_).md>) — Presents an alert when an error is present.
- [alert(_:isPresented:actions:message:)](<view/alert(__ispresented_actions_message_).md>) — Presents an alert with a message when a given condition is true, using a localized string resource for a title.
- [alert(_:isPresented:presenting:actions:message:)](<view/alert(__ispresented_presenting_actions_message_).md>) — Presents an alert with a message using the given data to produce the alert’s content and a localized string resource for a title.
- [alert(_:item:actions:message:)](<view/alert(__item_actions_message_).md>) — Presents an alert with a message using the given data to produce the alert’s content and a localized string key for a title.
- [alert(error:actions:message:)](<view/alert(error_actions_message_).md>) — Presents an alert with a message when an error is present.
- [alert(isPresented:error:actions:message:)](<view/alert(ispresented_error_actions_message_).md>) — Presents an alert with a message when an error is present.

### Getting confirmation for an action

- [confirmationDialog(_:isPresented:titleVisibility:actions:)](<view/confirmationdialog(__ispresented_titlevisibility_actions_).md>) — Presents a confirmation dialog when a given condition is true, using a localized string resource for the title.
- [confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)](<view/confirmationdialog(__ispresented_titlevisibility_presenting_actions_).md>) — Presents a confirmation dialog using data to produce the dialog’s content and a localized string resource for the title.
- [dismissalConfirmationDialog(_:shouldPresent:actions:)](<view/dismissalconfirmationdialog(__shouldpresent_actions_).md>) — Presents a confirmation dialog when a dismiss action has been triggered.

### Showing a confirmation dialog with a message

- [confirmationDialog(_:isPresented:titleVisibility:actions:message:)](<view/confirmationdialog(__ispresented_titlevisibility_actions_message_).md>) — Presents a confirmation dialog with a message when a given condition is true, using a localized string resource for the title.
- [confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)](<view/confirmationdialog(__ispresented_titlevisibility_presenting_actions_message_).md>) — Presents a confirmation dialog with a message using data to produce the dialog’s content and a localized string resource for the title.
- [dismissalConfirmationDialog(_:shouldPresent:actions:message:)](<view/dismissalconfirmationdialog(__shouldpresent_actions_message_).md>) — Presents a confirmation dialog when a dismiss action has been triggered.

### Configuring a dialog

- [dialogIcon(_:)](<view/dialogicon(__).md>) — Configures the icon used by dialogs within this view.
- [dialogIcon(_:)](<scene/dialogicon(__).md>) — Configures the icon used by alerts.
- [dialogSeverity(_:)](<view/dialogseverity(__).md>)
- [dialogSeverity(_:)](<scene/dialogseverity(__).md>) — Sets the severity for alerts.
- [dialogSuppressionToggle(isSuppressed:)](<view/dialogsuppressiontoggle(issuppressed_).md>) — Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [dialogSuppressionToggle(isSuppressed:)](<scene/dialogsuppressiontoggle(issuppressed_).md>) — Enables user suppression of an alert with a custom suppression message.
- [dialogSuppressionToggle(_:isSuppressed:)](<view/dialogsuppressiontoggle(__issuppressed_).md>) — Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [dialogSuppressionToggle(_:isSuppressed:)](<scene/dialogsuppressiontoggle(__issuppressed_).md>) — Enables user suppression of an alert with a custom suppression message.
- [dialogPreventsAppTermination(_:)](<view/dialogpreventsapptermination(__).md>) — Whether the alert or confirmation dialog prevents the app from being quit/terminated by the system or app termination menu item.

### Exporting to file

- [fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)](<view/fileexporter(ispresented_document_contenttype_defaultfilename_oncompletion_).md>) — Presents a system dialog for exporting a document that’s stored in a value type, like a structure, to a file on disk. _(deprecated)_
- [fileExporter(isPresented:documents:contentType:onCompletion:)](<view/fileexporter(ispresented_documents_contenttype_oncompletion_).md>) — Presents a system dialog for exporting a collection of value type documents to files on disk. _(deprecated)_
- [fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:onCancellation:)](<view/fileexporter(ispresented_document_contenttype_defaultfilename_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to export a `WritableDocument` to a file on disk. _(beta)_
- [fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)](<view/fileexporter(ispresented_document_contenttypes_defaultfilename_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to export a `FileDocument` to a file on disk. _(deprecated)_
- [fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)](<view/fileexporter(ispresented_documents_contenttypes_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to export a collection of objects conforming to `WritableDocument` to files on disk. _(beta)_
- [fileExporter(isPresented:item:contentTypes:defaultFilename:onCompletion:onCancellation:)](<view/fileexporter(ispresented_item_contenttypes_defaultfilename_oncompletion_oncancellation_).md>) — Presents a system dialog allowing the user to export a `Transferable` item to a file on disk.
- [fileExporter(isPresented:items:contentTypes:onCompletion:onCancellation:)](<view/fileexporter(ispresented_items_contenttypes_oncompletion_oncancellation_).md>) — Presents a system dialog allowing the user to export a collection of `Transferable` items to files on disk.
- [fileExporterFilenameLabel(_:)](<view/fileexporterfilenamelabel(__).md>) — On macOS, configures the `fileExporter` with a label for the file name field.

### Importing from file

- [fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:)](<view/fileimporter(ispresented_allowedcontenttypes_allowsmultipleselection_oncompletion_).md>) — Presents a system dialog for allowing the user to import multiple files.
- [fileImporter(isPresented:allowedContentTypes:onCompletion:)](<view/fileimporter(ispresented_allowedcontenttypes_oncompletion_).md>) — Presents a system dialog for allowing the user to import an existing file.
- [fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:onCancellation:)](<view/fileimporter(ispresented_allowedcontenttypes_allowsmultipleselection_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to import multiple files.

### Moving a file

- [fileMover(isPresented:file:onCompletion:)](<view/filemover(ispresented_file_oncompletion_).md>) — Presents a system dialog for allowing the user to move an existing file to a new location.
- [fileMover(isPresented:files:onCompletion:)](<view/filemover(ispresented_files_oncompletion_).md>) — Presents a system dialog for allowing the user to move a collection of existing files to a new location.
- [fileMover(isPresented:file:onCompletion:onCancellation:)](<view/filemover(ispresented_file_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to move an existing file to a new location.
- [fileMover(isPresented:files:onCompletion:onCancellation:)](<view/filemover(ispresented_files_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to move a collection of existing files to a new location.

### Configuring a file dialog

- [fileDialogBrowserOptions(_:)](<view/filedialogbrowseroptions(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to provide a refined URL search experience: include or exclude hidden files, allow searching by tag, etc.
- [fileDialogConfirmationLabel(_:)](<view/filedialogconfirmationlabel(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [fileDialogCustomizationID(_:)](<view/filedialogcustomizationid(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to persist and restore the file dialog configuration.
- [fileDialogDefaultDirectory(_:)](<view/filedialogdefaultdirectory(__).md>) — Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the specified default directory.
- [fileDialogImportsUnresolvedAliases(_:)](<view/filedialogimportsunresolvedaliases(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` behavior when a user chooses an alias.
- [fileDialogMessage(_:)](<view/filedialogmessage(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [fileDialogURLEnabled(_:)](<view/filedialogurlenabled(__).md>) — On macOS, configures the `fileImporter` or `fileMover` to conditionally disable presented URLs.
- [FileDialogBrowserOptions](filedialogbrowseroptions.md) — The way that file dialogs present the file system.

### Presenting an inspector

- [inspector(isPresented:content:)](<view/inspector(ispresented_content_).md>) — Inserts an inspector at the applied position in the view hierarchy.
- [inspectorColumnWidth(_:)](<view/inspectorcolumnwidth(__).md>) — Sets a fixed, preferred width for the inspector containing this view when presented as a trailing column.
- [inspectorColumnWidth(min:ideal:max:)](<view/inspectorcolumnwidth(min_ideal_max_).md>) — Sets a flexible, preferred width for the inspector in a trailing-column presentation.

### Dismissing a presentation

- [isPresented](environmentvalues/ispresented.md) — A Boolean value that indicates whether the view associated with this environment is currently presented.
- [dismiss](environmentvalues/dismiss.md) — An action that dismisses the current presentation.
- [DismissAction](dismissaction.md) — An action that dismisses a presentation.
- [interactiveDismissDisabled(_:)](<view/interactivedismissdisabled(__).md>) — Conditionally prevents interactive dismissal of presentations like popovers, sheets, and inspectors.

### Deprecated modal presentations

- [Alert](alert.md) — A representation of an alert presentation. _(deprecated)_
- [ActionSheet](actionsheet.md) — A representation of an action sheet presentation. _(deprecated)_

## See Also

### App structure

- [App organization](app-organization.md) — Define the entry point and top-level structure of your app.
- [Scenes](scenes.md) — Declare the user interface groupings that make up the parts of your app.
- [Windows](windows.md) — Display user interface content in a window or a collection of windows.
- [Immersive spaces](immersive-spaces.md) — Display unbounded content in a person’s surroundings.
- [Documents](documents.md) — Enable people to open and manage documents.
- [Navigation](navigation.md) — Enable people to move between different parts of your app’s view hierarchy within a scene.
- [Toolbars](toolbars.md) — Provide immediate access to frequently used commands and controls.
- [Search](search.md) — Enable people to search for text or other content within your app.
- [App extensions](app-extensions.md) — Extend your app’s basic functionality to other parts of the system, like by adding a Widget.
