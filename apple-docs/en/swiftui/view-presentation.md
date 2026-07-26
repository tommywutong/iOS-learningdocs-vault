---
title: Presentation modifiers
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-presentation
source_url: 'https://developer.apple.com/documentation/swiftui/view-presentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-presentation.json'
content_hash: 'sha256:802dcf2ae1161b2b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [View fundamentals](view-fundamentals.md) · [View](view.md)

# Presentation modifiers

<sub>API Collection</sub>

Define additional views for the view to present under specified conditions.

## Overview

Use presentation modifiers to show different kinds of modal presentations, like alerts, popovers, sheets, and confirmation dialogs.

Because SwiftUI is a declarative framework, you don’t call a method at the moment you want to present the modal. Rather, you define how the presentation looks and the condition under which SwiftUI should present it. SwiftUI detects when the condition changes and makes the presentation for you. Because you provide a [Binding](binding.md) to the condition that initiates the presentation, SwiftUI can reset the underlying value when the user dismisses the presentation.

For more information about how to use these modifiers, see [Modal presentations](modal-presentations.md).

## Topics

### Alerts

- [alert(_:isPresented:actions:)](<view/alert(__ispresented_actions_).md>) — Presents an alert when a given condition is true, using a localized string resource for the title.
- [alert(_:isPresented:presenting:actions:)](<view/alert(__ispresented_presenting_actions_).md>) — Presents an alert using the given data to produce the alert’s content and a localized string resource for a title.
- [alert(_:item:actions:)](<view/alert(__item_actions_).md>) — Presents an alert using the given data to produce the alert’s content and a text view as a title.
- [alert(error:actions:)](<view/alert(error_actions_).md>) — Presents an alert when an error is present.
- [alert(isPresented:error:actions:)](<view/alert(ispresented_error_actions_).md>) — Presents an alert when an error is present.

### Alerts with a message

- [alert(_:isPresented:actions:message:)](<view/alert(__ispresented_actions_message_).md>) — Presents an alert with a message when a given condition is true, using a localized string resource for a title.
- [alert(_:isPresented:presenting:actions:message:)](<view/alert(__ispresented_presenting_actions_message_).md>) — Presents an alert with a message using the given data to produce the alert’s content and a localized string resource for a title.
- [alert(_:item:actions:message:)](<view/alert(__item_actions_message_).md>) — Presents an alert with a message using the given data to produce the alert’s content and a localized string key for a title.
- [alert(error:actions:message:)](<view/alert(error_actions_message_).md>) — Presents an alert with a message when an error is present.
- [alert(isPresented:error:actions:message:)](<view/alert(ispresented_error_actions_message_).md>) — Presents an alert with a message when an error is present.

### Confirmation dialogs

- [confirmationDialog(_:isPresented:titleVisibility:actions:)](<view/confirmationdialog(__ispresented_titlevisibility_actions_).md>) — Presents a confirmation dialog when a given condition is true, using a localized string resource for the title.
- [confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)](<view/confirmationdialog(__ispresented_titlevisibility_presenting_actions_).md>) — Presents a confirmation dialog using data to produce the dialog’s content and a localized string resource for the title.
- [confirmationDialog(_:item:titleVisibility:actions:)](<view/confirmationdialog(__item_titlevisibility_actions_).md>) — Presents a confirmation dialog using data to produce the dialog’s content and a text view for the title.
- [dismissalConfirmationDialog(_:shouldPresent:actions:)](<view/dismissalconfirmationdialog(__shouldpresent_actions_).md>) — Presents a confirmation dialog when a dismiss action has been triggered.

### Confirmation dialogs with a message

- [confirmationDialog(_:isPresented:titleVisibility:actions:message:)](<view/confirmationdialog(__ispresented_titlevisibility_actions_message_).md>) — Presents a confirmation dialog with a message when a given condition is true, using a localized string resource for the title.
- [confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)](<view/confirmationdialog(__ispresented_titlevisibility_presenting_actions_message_).md>) — Presents a confirmation dialog with a message using data to produce the dialog’s content and a localized string resource for the title.
- [confirmationDialog(_:item:titleVisibility:actions:message:)](<view/confirmationdialog(__item_titlevisibility_actions_message_).md>) — Presents a confirmation dialog with a message using data to produce the dialog’s content and a text view for the message.
- [dismissalConfirmationDialog(_:shouldPresent:actions:message:)](<view/dismissalconfirmationdialog(__shouldpresent_actions_message_).md>) — Presents a confirmation dialog when a dismiss action has been triggered.

### Dialog configuration

- [dialogIcon(_:)](<view/dialogicon(__).md>) — Configures the icon used by dialogs within this view.
- [dialogSeverity(_:)](<view/dialogseverity(__).md>)
- [dialogSuppressionToggle(isSuppressed:)](<view/dialogsuppressiontoggle(issuppressed_).md>) — Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [dialogSuppressionToggle(_:isSuppressed:)](<view/dialogsuppressiontoggle(__issuppressed_).md>) — Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [dialogPreventsAppTermination(_:)](<view/dialogpreventsapptermination(__).md>) — Whether the alert or confirmation dialog prevents the app from being quit/terminated by the system or app termination menu item.

### Sheets

- [sheet(isPresented:onDismiss:content:)](<view/sheet(ispresented_ondismiss_content_).md>) — Presents a sheet when a binding to a Boolean value that you provide is true.
- [sheet(item:onDismiss:content:)](<view/sheet(item_ondismiss_content_).md>) — Presents a sheet using the given item as a data source for the sheet’s content.
- [fullScreenCover(isPresented:onDismiss:content:)](<view/fullscreencover(ispresented_ondismiss_content_).md>) — Presents a modal view that covers as much of the screen as possible when binding to a Boolean value you provide is true.
- [fullScreenCover(item:onDismiss:content:)](<view/fullscreencover(item_ondismiss_content_).md>) — Presents a modal view that covers as much of the screen as possible using the binding you provide as a data source for the sheet’s content.

### Popovers

- [popover(item:attachmentAnchor:arrowEdge:content:)](<view/popover(item_attachmentanchor_arrowedge_content_).md>) — Presents a popover using the given item as a data source for the popover’s content.
- [popover(isPresented:attachmentAnchor:arrowEdge:content:)](<view/popover(ispresented_attachmentanchor_arrowedge_content_).md>) — Presents a popover when a given condition is true.

### Sheet and popover configuration

- [interactiveDismissDisabled(_:)](<view/interactivedismissdisabled(__).md>) — Conditionally prevents interactive dismissal of presentations like popovers, sheets, and inspectors.
- [presentationDetents(_:)](<view/presentationdetents(__).md>) — Sets the available detents for the enclosing sheet.
- [presentationDetents(_:selection:)](<view/presentationdetents(__selection_).md>) — Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [presentationDragIndicator(_:)](<view/presentationdragindicator(__).md>) — Sets the visibility of the drag indicator on top of a sheet.
- [presentationBackground(_:)](<view/presentationbackground(__).md>) — Sets the presentation background of the enclosing sheet using a shape style.
- [presentationBackground(alignment:content:)](<view/presentationbackground(alignment_content_).md>) — Sets the presentation background of the enclosing sheet to a custom view.
- [presentationBackgroundInteraction(_:)](<view/presentationbackgroundinteraction(__).md>) — Controls whether people can interact with the view behind a presentation.
- [presentationCompactAdaptation(horizontal:vertical:)](<view/presentationcompactadaptation(horizontal_vertical_).md>) — Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [presentationCompactAdaptation(_:)](<view/presentationcompactadaptation(__).md>) — Specifies how to adapt a presentation to compact size classes.
- [presentationContentInteraction(_:)](<view/presentationcontentinteraction(__).md>) — Configures the behavior of swipe gestures on a presentation.
- [presentationCornerRadius(_:)](<view/presentationcornerradius(__).md>) — Requests that the presentation have a specific corner radius.
- [presentationSizing(_:)](<view/presentationsizing(__).md>) — Sets the sizing of the containing presentation.
- [presentationBreakthroughEffect(_:)](<view/presentationbreakthrougheffect(__).md>) — Changes the way the enclosing presentation breaks through content occluding it.
- [presentationPreventsAppTermination(_:)](<view/presentationpreventsapptermination(__).md>) — Whether a presentation prevents the app from being terminated/quit by the system or app termination menu item.

### File exporter

- [fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)](<view/fileexporter(ispresented_document_contenttype_defaultfilename_oncompletion_).md>) — Presents a system dialog for exporting a document that’s stored in a value type, like a structure, to a file on disk. _(deprecated)_
- [fileExporter(isPresented:documents:contentType:onCompletion:)](<view/fileexporter(ispresented_documents_contenttype_oncompletion_).md>) — Presents a system dialog for exporting a collection of value type documents to files on disk. _(deprecated)_
- [fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:onCancellation:)](<view/fileexporter(ispresented_document_contenttype_defaultfilename_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to export a `WritableDocument` to a file on disk. _(beta)_
- [fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)](<view/fileexporter(ispresented_document_contenttypes_defaultfilename_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to export a `FileDocument` to a file on disk. _(deprecated)_
- [fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)](<view/fileexporter(ispresented_documents_contenttypes_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to export a collection of objects conforming to `WritableDocument` to files on disk. _(beta)_
- [fileExporter(isPresented:item:contentTypes:defaultFilename:onCompletion:onCancellation:)](<view/fileexporter(ispresented_item_contenttypes_defaultfilename_oncompletion_oncancellation_).md>) — Presents a system dialog allowing the user to export a `Transferable` item to a file on disk.
- [fileExporter(isPresented:items:contentTypes:onCompletion:onCancellation:)](<view/fileexporter(ispresented_items_contenttypes_oncompletion_oncancellation_).md>) — Presents a system dialog allowing the user to export a collection of `Transferable` items to files on disk.
- [fileExporterFilenameLabel(_:)](<view/fileexporterfilenamelabel(__).md>) — On macOS, configures the `fileExporter` with a label for the file name field.

### File importer

- [fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:)](<view/fileimporter(ispresented_allowedcontenttypes_allowsmultipleselection_oncompletion_).md>) — Presents a system dialog for allowing the user to import multiple files.
- [fileImporter(isPresented:allowedContentTypes:onCompletion:)](<view/fileimporter(ispresented_allowedcontenttypes_oncompletion_).md>) — Presents a system dialog for allowing the user to import an existing file.
- [fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:onCancellation:)](<view/fileimporter(ispresented_allowedcontenttypes_allowsmultipleselection_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to import multiple files.

### File mover

- [fileMover(isPresented:file:onCompletion:)](<view/filemover(ispresented_file_oncompletion_).md>) — Presents a system dialog for allowing the user to move an existing file to a new location.
- [fileMover(isPresented:files:onCompletion:)](<view/filemover(ispresented_files_oncompletion_).md>) — Presents a system dialog for allowing the user to move a collection of existing files to a new location.
- [fileMover(isPresented:file:onCompletion:onCancellation:)](<view/filemover(ispresented_file_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to move an existing file to a new location.
- [fileMover(isPresented:files:onCompletion:onCancellation:)](<view/filemover(ispresented_files_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to move a collection of existing files to a new location.

### File dialog configuration

- [fileDialogBrowserOptions(_:)](<view/filedialogbrowseroptions(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to provide a refined URL search experience: include or exclude hidden files, allow searching by tag, etc.
- [fileDialogConfirmationLabel(_:)](<view/filedialogconfirmationlabel(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [fileDialogCustomizationID(_:)](<view/filedialogcustomizationid(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to persist and restore the file dialog configuration.
- [fileDialogDefaultDirectory(_:)](<view/filedialogdefaultdirectory(__).md>) — Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the specified default directory.
- [fileDialogImportsUnresolvedAliases(_:)](<view/filedialogimportsunresolvedaliases(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` behavior when a user chooses an alias.
- [fileDialogMessage(_:)](<view/filedialogmessage(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [fileDialogURLEnabled(_:)](<view/filedialogurlenabled(__).md>) — On macOS, configures the `fileImporter` or `fileMover` to conditionally disable presented URLs.

### Foveated streaming

- [foveatedStreamingPauseSheet(session:)](<view/foveatedstreamingpausesheet(session_).md>) — Tells the system to present a sheet with controls for resuming or ending the foveated streaming session when it pauses.

### Screen capture

- [recordingEditor(_:)](<view/recordingeditor(__).md>) — Presents the recording editor for the given recording URL. _(beta)_
- [recordingEditor(_:mode:)](<view/recordingeditor(__mode_).md>) — Presents the recording editor for the given recording URL with a specific mode. _(beta)_

### Document browser

- [documentLaunchTitle(_:)](<view/documentlaunchtitle(__).md>) — Sets the title displayed on the document launch card. _(beta)_
- [documentLaunchSubtitle(_:)](<view/documentlaunchsubtitle(__).md>) — Sets the subtitle displayed beneath the title on the document launch card. _(beta)_
- [documentBrowserContextMenu(_:)](<view/documentbrowsercontextmenu(__).md>) — Adds to a `DocumentLaunchView` actions that accept a list of selected files as their parameter.

### Inspectors

- [inspector(isPresented:content:)](<view/inspector(ispresented_content_).md>) — Inserts an inspector at the applied position in the view hierarchy.
- [inspectorColumnWidth(_:)](<view/inspectorcolumnwidth(__).md>) — Sets a fixed, preferred width for the inspector containing this view when presented as a trailing column.
- [inspectorColumnWidth(min:ideal:max:)](<view/inspectorcolumnwidth(min_ideal_max_).md>) — Sets a flexible, preferred width for the inspector in a trailing-column presentation.

### Quick look previews

- [quickLookPreview(_:)](<view/quicklookpreview(__).md>) — Presents a Quick Look preview of the contents of a single URL.
- [quickLookPreview(_:in:)](<view/quicklookpreview(__in_).md>) — Presents a Quick Look preview of the URLs you provide.

### Family Sharing

- [familyActivityPicker(isPresented:selection:)](<view/familyactivitypicker(ispresented_selection_).md>) — Presents an activity picker view as a sheet.
- [familyActivityPicker(headerText:footerText:isPresented:selection:)](<view/familyactivitypicker(headertext_footertext_ispresented_selection_).md>) — Presents an activity picker view as a sheet.
- [familyActivityPicker(title:headerText:footerText:isPresented:selection:)](<view/familyactivitypicker(title_headertext_footertext_ispresented_selection_).md>) — Present an activity picker sheet for selecting apps and websites to manage.

### Live Activities

- [activitySystemActionForegroundColor(_:)](<view/activitysystemactionforegroundcolor(__).md>) — The text color for the auxiliary action button that the system shows next to a Live Activity on the Lock Screen.
- [activityBackgroundTint(_:)](<view/activitybackgroundtint(__).md>) — Sets the tint color for the background of a Live Activity that appears on the Lock Screen.

### Game saving

- [gameSaveSyncingAlert(directory:finishedLoading:)](<view/gamesavesyncingalert(directory_finishedloading_).md>) — Presents a modal view while the game synced directory loads.

### Apple Music

- [musicSubscriptionOffer(isPresented:options:onLoadCompletion:)](<view/musicsubscriptionoffer(ispresented_options_onloadcompletion_).md>) — Initiates the process of presenting a sheet with subscription offers for Apple Music when the `isPresented` binding is `true`.

### Contacts

- [contactAccessButtonCaption(_:)](<view/contactaccessbuttoncaption(__).md>)
- [contactAccessButtonStyle(_:)](<view/contactaccessbuttonstyle(__).md>)
- [contactAccessPicker(isPresented:completionHandler:)](<view/contactaccesspicker(ispresented_completionhandler_).md>) — Modally present UI which allows the user to select which contacts your app has access to.

### StoreKit

- [appStoreOverlay(isPresented:configuration:)](<view/appstoreoverlay(ispresented_configuration_).md>) — Presents a StoreKit overlay when a given condition is true.
- [appStoreMerchandising(isPresented:kind:onDismiss:)](<view/appstoremerchandising(ispresented_kind_ondismiss_).md>) — Display a merchandising view.
- [manageSubscriptionsSheet(isPresented:)](<view/managesubscriptionssheet(ispresented_).md>)
- [refundRequestSheet(for:isPresented:onDismiss:)](<view/refundrequestsheet(for_ispresented_ondismiss_).md>) — Display the refund request sheet for the given transaction.
- [offerCodeRedemption(options:isPresented:onCompletion:)](<view/offercoderedemption(options_ispresented_oncompletion_).md>) — Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect. _(beta)_

### PhotoKit

- [photosPicker(isPresented:selection:matching:preferredItemEncoding:)](<view/photospicker(ispresented_selection_matching_preferreditemencoding_).md>) — Presents a Photos picker that selects a `PhotosPickerItem`.
- [photosPicker(isPresented:selection:matching:preferredItemEncoding:photoLibrary:)](<view/photospicker(ispresented_selection_matching_preferreditemencoding_photolibrary_).md>) — Presents a Photos picker that selects a `PhotosPickerItem` from a given photo library.
- [photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:)](<view/photospicker(ispresented_selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_).md>) — Presents a Photos picker that selects a collection of `PhotosPickerItem`.
- [photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:photoLibrary:)](<view/photospicker(ispresented_selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_photolibrary_).md>) — Presents a Photos picker that selects a collection of `PhotosPickerItem` from a given photo library.
- [photosPickerAccessoryVisibility(_:edges:)](<view/photospickeraccessoryvisibility(__edges_).md>) — Sets the accessory visibility of the Photos picker. Accessories include anything between the content and the edge, like the navigation bar or the sidebar.
- [photosPickerDisabledCapabilities(_:)](<view/photospickerdisabledcapabilities(__).md>) — Disables capabilities of the Photos picker.
- [photosPickerSearchText(_:)](<view/photospickersearchtext(__).md>) — Sets search text of the Photos picker. _(beta)_
- [photosPickerStyle(_:)](<view/photospickerstyle(__).md>) — Sets the mode of the Photos picker.
- [photosSharedAlbumCreationSheet(isPresented:defaultTitle:defaultSharingPolicy:photoLibrary:onCompletion:)](<view/photossharedalbumcreationsheet(ispresented_defaulttitle_defaultsharingpolicy_photolibrary_oncompletion_).md>) — Presents a view for allowing the user to create a new shared album. _(beta)_
- [photosSharedAlbumCustomizationSheet(isPresented:albumIdentifier:photoLibrary:onCompletion:)](<view/photossharedalbumcustomizationsheet(ispresented_albumidentifier_photolibrary_oncompletion_).md>) — Presents a view for allowing the user to customize a specified shared album. _(beta)_
- [photosSharedAlbumPostingSheet(isPresented:items:defaultAlbumIdentifier:photoLibrary:completion:)](<view/photossharedalbumpostingsheet(ispresented_items_defaultalbumidentifier_photolibrary_completion_).md>) — Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album. _(beta)_

### Translation

- [translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)](<view/translationpresentation(ispresented_text_attachmentanchor_arrowedge_replacementaction_).md>) — Presents a translation popover when a given condition is true.
- [translationTask(_:action:)](<view/translationtask(__action_).md>) — Adds a task to perform before this view appears or when the translation configuration changes.
- [translationTask(source:target:action:)](<view/translationtask(source_target_action_).md>) — Adds a task to perform before this view appears or when the specified source or target languages change.
- [translationTask(source:target:preferredStrategy:action:)](<view/translationtask(source_target_preferredstrategy_action_).md>) — Adds a task to perform before this view appears or when the specified source or target languages change.

### Security

- [certificateSheet(trust:title:message:help:)](<view/certificatesheet(trust_title_message_help_).md>) — Displays a certificate sheet using the provided certificate trust.

## See Also

### Providing interactivity

- [Input and event modifiers](view-input-and-events.md) — Supply actions for a view to perform in response to user input and system events.
- [Search modifiers](view-search.md) — Enable people to search for content in your app.
- [State modifiers](view-state.md) — Access storage and provide child views with configuration data.
