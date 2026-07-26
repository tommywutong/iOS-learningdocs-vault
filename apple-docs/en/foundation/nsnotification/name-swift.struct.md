---
title: NSNotification.Name
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct.json'
content_hash: 'sha256:c322989d121f6120'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSNotification](../nsnotification.md)

# NSNotification.Name

<sub>Structure</sub>

A structure that defines the name of a notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Name
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### AddressBook

- [abDatabaseChanged](name-swift.struct/abdatabasechanged.md) — Posted when this process has changed the Address Book database.
- [abDatabaseChangedExternally](name-swift.struct/abdatabasechangedexternally.md) — Posted when a process other than the current one has changed the Address Book database.
- [ABPeoplePickerDisplayedPropertyDidChange](name-swift.struct/abpeoplepickerdisplayedpropertydidchange.md) — Posted when the displayed property in the record list is changed.
- [ABPeoplePickerGroupSelectionDidChange](name-swift.struct/abpeoplepickergroupselectiondidchange.md) — Posted when the selection in the group list is changed.
- [ABPeoplePickerNameSelectionDidChange](name-swift.struct/abpeoplepickernameselectiondidchange.md) — Posted when the selection in the name list is changed.
- [ABPeoplePickerValueSelectionDidChange](name-swift.struct/abpeoplepickervalueselectiondidchange.md) — Posted when the selection in a multivalue property is changed.

### AppKit

- [unsupportedAttributeAddedNotification](name-swift.struct/unsupportedattributeaddednotification.md)
- [didProcessEditingNotification](../../appkit/nstextstorage/didprocesseditingnotification.md) — A notification that posts after a text storage finishes processing edits.
- [willProcessEditingNotification](../../appkit/nstextstorage/willprocesseditingnotification.md) — A notification that posts before a text storage begins processing edits.
- [didChangeSelectionNotification](../../appkit/nstextview/didchangeselectionnotification.md) — Posted when the selected range of characters changes.
- [didChangeTypingAttributesNotification](../../appkit/nstextview/didchangetypingattributesnotification.md) — Posted when there is a change in the typing attributes within a text view.
- [willChangeNotifyingTextViewNotification](../../appkit/nstextview/willchangenotifyingtextviewnotification.md) — Posted when a new text view is established as the text view that sends notifications.
- [didRemoveItemNotification](../../appkit/nstoolbar/didremoveitemnotification.md) — Posted after an item is removed from a toolbar.
- [willAddItemNotification](../../appkit/nstoolbar/willadditemnotification.md) — Posts before the toolbar adds a new item.
- [boundsDidChangeNotification](../../appkit/nsview/boundsdidchangenotification.md) — A notification that posts when the view’s bounds rectangle changes to a new value independently of the frame rectangle.
- [didUpdateTrackingAreasNotification](../../appkit/nsview/didupdatetrackingareasnotification.md) — Posted whenever a view recalculates its tracking areas.
- [frameDidChangeNotification](../../appkit/nsview/framedidchangenotification.md) — A notification that posts when the view’s frame rectangle changes to a new value.
- [didBecomeKeyNotification](../../appkit/nswindow/didbecomekeynotification.md) — A notification that the window object became the key window.
- [didBecomeMainNotification](../../appkit/nswindow/didbecomemainnotification.md) — A notification that the window object became the main window.
- [didChangeBackingPropertiesNotification](../../appkit/nswindow/didchangebackingpropertiesnotification.md) — A notification that the window object backing properties changed.
- [didChangeOcclusionStateNotification](../../appkit/nswindow/didchangeocclusionstatenotification.md) — A notification that the window object’s occlusion state changed.
- [didChangeScreenNotification](../../appkit/nswindow/didchangescreennotification.md) — A notification that a portion of the window object’s frame moved onto or off of a screen.
- [didChangeScreenProfileNotification](../../appkit/nswindow/didchangescreenprofilenotification.md) — A notification that the screen containing the window changed.
- [didDeminiaturizeNotification](../../appkit/nswindow/diddeminiaturizenotification.md) — A notification that the window is no longer minimized.
- [didEndLiveResizeNotification](../../appkit/nswindow/didendliveresizenotification.md) — A notification that the user resized the window object.
- [didEndSheetNotification](../../appkit/nswindow/didendsheetnotification.md) — A notification that the window object closed an attached sheet.
- [didEnterFullScreenNotification](../../appkit/nswindow/didenterfullscreennotification.md) — A notification that the window entered full-screen mode.
- [didEnterVersionBrowserNotification](../../appkit/nswindow/didenterversionbrowsernotification.md) — A notification that the window object entered version browser mode.
- [didExitFullScreenNotification](../../appkit/nswindow/didexitfullscreennotification.md) — A notification that the window object exited full-screen mode.
- [didExitVersionBrowserNotification](../../appkit/nswindow/didexitversionbrowsernotification.md) — A notification that the window object exited version browser mode.
- [didExposeNotification](../../appkit/nswindow/didexposenotification.md) — A notification that a window exposed a portion of its nonretained content.
- [didMiniaturizeNotification](../../appkit/nswindow/didminiaturizenotification.md) — A notification that the window object minimized.
- [didMoveNotification](../../appkit/nswindow/didmovenotification.md) — A notification that the window object moved.
- [didResignKeyNotification](../../appkit/nswindow/didresignkeynotification.md) — A notification that the window object resigned its status as key window.
- [didResignMainNotification](../../appkit/nswindow/didresignmainnotification.md) — A notification that the window object resigned its status as main window.
- [didResizeNotification](../../appkit/nswindow/didresizenotification.md) — A notification that the window object size changed.
- [didUpdateNotification](../../appkit/nswindow/didupdatenotification.md) — A notification that the window object received an update message.
- [willBeginSheetNotification](../../appkit/nswindow/willbeginsheetnotification.md) — A notification that the window object is about to open a sheet.
- [willCloseNotification](../../appkit/nswindow/willclosenotification.md) — A notification that the window object is about to close.
- [willEnterFullScreenNotification](../../appkit/nswindow/willenterfullscreennotification.md) — A notification that the window will enter full-screen mode.
- [willEnterVersionBrowserNotification](../../appkit/nswindow/willenterversionbrowsernotification.md) — A notification that the window object will enter version browser mode.
- [willExitFullScreenNotification](../../appkit/nswindow/willexitfullscreennotification.md) — A notification that the window object will exit full-screen mode.
- [willExitVersionBrowserNotification](../../appkit/nswindow/willexitversionbrowsernotification.md) — A notification that the window object will exit version browser mode.
- [willMiniaturizeNotification](../../appkit/nswindow/willminiaturizenotification.md) — A notification that the window object is about to minimize.
- [willMoveNotification](../../appkit/nswindow/willmovenotification.md) — A notification that the window object is about to move.
- [willStartLiveResizeNotification](../../appkit/nswindow/willstartliveresizenotification.md) — A notification that the user is about to resize the window.
- [accessibilityDisplayOptionsDidChangeNotification](../../appkit/nsworkspace/accessibilitydisplayoptionsdidchangenotification.md) — A notification that the workspace posts when any of the accessibility display options change.
- [activeSpaceDidChangeNotification](../../appkit/nsworkspace/activespacedidchangenotification.md) — A notification that the workspace posts when a Spaces change occurs.
- [didActivateApplicationNotification](../../appkit/nsworkspace/didactivateapplicationnotification.md) — A notification that the workspace posts when the Finder is about to activate an app.
- [didChangeFileLabelsNotification](../../appkit/nsworkspace/didchangefilelabelsnotification.md) — A notification that the workspace posts when the Finder file labels or colors change.
- [didDeactivateApplicationNotification](../../appkit/nsworkspace/diddeactivateapplicationnotification.md) — A notification that the workspace posts when the Finder deactivates an app.
- [didHideApplicationNotification](../../appkit/nsworkspace/didhideapplicationnotification.md) — A notification that the workspace posts when the Finder hides an app.
- [didLaunchApplicationNotification](../../appkit/nsworkspace/didlaunchapplicationnotification.md) — A notification that the workspace posts when a new app starts up.
- [didMountNotification](../../appkit/nsworkspace/didmountnotification.md) — A notification that the workspace posts when a new device mounts.
- [didPerformFileOperationNotification](../../appkit/nsworkspace/didperformfileoperationnotification.md) — Posted when a file operation has been performed in the receiving app. _(deprecated)_
- [didRenameVolumeNotification](../../appkit/nsworkspace/didrenamevolumenotification.md) — A notification that the workspace posts when a volume changes its name or mount path.
- [didTerminateApplicationNotification](../../appkit/nsworkspace/didterminateapplicationnotification.md) — A notification that the workspace posts when an app finishes executing.
- [didUnhideApplicationNotification](../../appkit/nsworkspace/didunhideapplicationnotification.md) — A notification that the workspace posts when the Finder unhides an app.
- [didUnmountNotification](../../appkit/nsworkspace/didunmountnotification.md) — A notification that the workspace posts when the Finder unmounts a device.
- [didWakeNotification](../../appkit/nsworkspace/didwakenotification.md) — A notification that the workspace posts when the device wakes from sleep.
- [screensDidSleepNotification](../../appkit/nsworkspace/screensdidsleepnotification.md) — A notification that the workspace posts when the device’s screen goes to sleep.
- [screensDidWakeNotification](../../appkit/nsworkspace/screensdidwakenotification.md) — A notification that the workspace posts when the device’s screens wake.
- [sessionDidBecomeActiveNotification](../../appkit/nsworkspace/sessiondidbecomeactivenotification.md) — A notification that the workspace posts after a user session switches in.
- [sessionDidResignActiveNotification](../../appkit/nsworkspace/sessiondidresignactivenotification.md) — A notification that the workspace posts before a user session switches out.
- [willLaunchApplicationNotification](../../appkit/nsworkspace/willlaunchapplicationnotification.md) — A notification that the workspace posts when the Finder is about to launch an app.
- [willPowerOffNotification](../../appkit/nsworkspace/willpoweroffnotification.md) — A notification that the workspace posts when the user requests a logout or powers off the device.
- [willSleepNotification](../../appkit/nsworkspace/willsleepnotification.md) — A notification that the workspace posts before the device goes to sleep.
- [willUnmountNotification](../../appkit/nsworkspace/willunmountnotification.md) — A notification that the workspace posts when the Finder is about to unmount a device.
- [didChangeNotification](../../appkit/nscolorlist/didchangenotification.md) — Posted whenever a color list changes.
- [didChangeNotification](../../appkit/nscolorlist/didchangenotification.md) — Posted whenever a color list changes.
- [selectionDidChangeNotification](../../appkit/nscombobox/selectiondidchangenotification.md) — Posted after the pop-up list selection of the `NSComboBox` changes.
- [selectionIsChangingNotification](../../appkit/nscombobox/selectionischangingnotification.md) — Posted whenever the pop-up list selection of the `NSComboBox` is changing.
- [willDismissNotification](../../appkit/nscombobox/willdismissnotification.md) — Posted whenever the pop-up list of the `NSComboBox` is about to be dismissed.
- [willPopUpNotification](../../appkit/nscombobox/willpopupnotification.md) — Posted whenever the pop-up list of the `NSComboBox` is going to be displayed.
- [contextHelpModeDidActivateNotification](../../appkit/nshelpmanager/contexthelpmodedidactivatenotification.md) — Posted when the application enters context-sensitive help mode. This typically happens when the user holds down the Help key.
- [contextHelpModeDidDeactivateNotification](../../appkit/nshelpmanager/contexthelpmodediddeactivatenotification.md) — Posted when the application exits context-sensitive help mode. This happens when the user clicks the mouse button while the cursor is anywhere on the screen after displaying a context-sensitive help topic.
- [textDidBeginEditingNotification](../../appkit/nscontrol/textdidbegineditingnotification.md) — Sent when a control with editable cells begins an edit session.
- [textDidChangeNotification](../../appkit/nscontrol/textdidchangenotification.md) — Sent when the text in the receiving control changes.
- [textDidEndEditingNotification](../../appkit/nscontrol/textdidendeditingnotification.md) — Sent when a control with editable cells ends an editing session.
- [currentControlTintDidChangeNotification](../../appkit/nscolor/currentcontroltintdidchangenotification.md) — Sent after the user changes control tint preference. _(deprecated)_
- [didCloseNotification](../../appkit/nsdrawer/didclosenotification.md) — Posted whenever the drawer is closed. _(deprecated)_
- [didOpenNotification](../../appkit/nsdrawer/didopennotification.md) — Posted whenever the drawer is opened. _(deprecated)_
- [willCloseNotification](../../appkit/nsdrawer/willclosenotification.md) — Posted whenever the drawer is about to close. _(deprecated)_
- [willOpenNotification](../../appkit/nsdrawer/willopennotification.md) — Posted whenever the drawer is about to open. _(deprecated)_
- [didChangeNotification](../../appkit/nsfontcollection/didchangenotification.md) — Posted whenever a font collection is changed.
- [fontSetChangedNotification](../../appkit/nsfont/fontsetchangednotification.md) — Posted after the currently-set font changes.
- [registryDidChangeNotification](../../appkit/nsimagerep/registrydidchangenotification.md) — Posted whenever the image representation class registry changes.
- [didAddItemNotification](../../appkit/nsmenu/didadditemnotification.md) — Posted after a menu item is added to the menu.
- [didBeginTrackingNotification](../../appkit/nsmenu/didbegintrackingnotification.md) — Posted when menu tracking begins.
- [didChangeItemNotification](../../appkit/nsmenu/didchangeitemnotification.md) — Posted after a menu item in the menu changes appearance.
- [didEndTrackingNotification](../../appkit/nsmenu/didendtrackingnotification.md) — Posted when menu tracking ends, even if no action is sent.
- [didRemoveItemNotification](../../appkit/nsmenu/didremoveitemnotification.md) — Posted after a menu item is removed from the menu.
- [didSendActionNotification](../../appkit/nsmenu/didsendactionnotification.md) — Posted just after the application dispatches a menu item’s action method to the menu item’s target.
- [willSendActionNotification](../../appkit/nsmenu/willsendactionnotification.md) — Posted just before the application dispatches a menu item’s action method to the menu item’s target.
- [columnDidMoveNotification](../../appkit/nsoutlineview/columndidmovenotification.md) — Posted whenever a column is moved by user action in an `NSOutlineView` object.
- [columnDidResizeNotification](../../appkit/nsoutlineview/columndidresizenotification.md) — Posted whenever a column is resized in an `NSOutlineView` object.
- [itemDidCollapseNotification](../../appkit/nsoutlineview/itemdidcollapsenotification.md) — Posted whenever an item is collapsed in an `NSOutlineView` object.
- [itemDidExpandNotification](../../appkit/nsoutlineview/itemdidexpandnotification.md) — Posted whenever an item is expanded in an `NSOutlineView` object.
- [itemWillCollapseNotification](../../appkit/nsoutlineview/itemwillcollapsenotification.md) — Posted before an item is collapsed (after the user clicks the arrow but before the item is collapsed).
- [itemWillExpandNotification](../../appkit/nsoutlineview/itemwillexpandnotification.md) — Posted before an item is expanded (after the user clicks the arrow but before the item is collapsed).
- [selectionDidChangeNotification](../../appkit/nsoutlineview/selectiondidchangenotification.md) — Posted after the outline view’s selection changes.
- [selectionIsChangingNotification](../../appkit/nsoutlineview/selectionischangingnotification.md) — Posted as the outline view’s selection changes (while the mouse button is still down).
- [willPopUpNotification](../../appkit/nspopupbuttoncell/willpopupnotification.md) — This notification is posted just before a pop-up menu is attached to its window frame.
- [willPopUpNotification](../../appkit/nspopupbutton/willpopupnotification.md) — Posted when an `NSPopUpButton` object receives a mouse-down event—that is, when the user is about to select an item from the menu.
- [didCloseNotification](../../appkit/nspopover/didclosenotification.md) — Sent after the popover has finished animating offscreen.
- [didShowNotification](../../appkit/nspopover/didshownotification.md) — Sent after the popover has finished animating onscreen.
- [willCloseNotification](../../appkit/nspopover/willclosenotification.md) — Sent before the popover is closed.
- [willShowNotification](../../appkit/nspopover/willshownotification.md) — Sent before the popover is shown.
- [preferredScrollerStyleDidChangeNotification](../../appkit/nsscroller/preferredscrollerstyledidchangenotification.md) — Posted if the preferred scroller style changes.
- [rowsDidChangeNotification](../../appkit/nsruleeditor/rowsdidchangenotification.md) — This notification is posted to the default notification center whenever the view’s rows change.
- [colorSpaceDidChangeNotification](../../appkit/nsscreen/colorspacedidchangenotification.md) — Posted when the color space of the screen has changed.
- [didEndLiveMagnifyNotification](../../appkit/nsscrollview/didendlivemagnifynotification.md) — Posted at the end of a magnify gesture.
- [didEndLiveScrollNotification](../../appkit/nsscrollview/didendlivescrollnotification.md) — Posted on the main thread at the end of live scroll tracking.
- [didLiveScrollNotification](../../appkit/nsscrollview/didlivescrollnotification.md) — Posted on the main thread after changing the clipview bounds origin due to a user-initiated event.
- [willStartLiveMagnifyNotification](../../appkit/nsscrollview/willstartlivemagnifynotification.md) — Posted at the beginning of a magnify gesture.
- [willStartLiveScrollNotification](../../appkit/nsscrollview/willstartlivescrollnotification.md) — Posted on the main thread at the beginning of user-initiated live scroll tracking (gesture scroll or scroller tracking, for example, thumb dragging).
- [didChangeAutomaticCapitalizationNotification](../../appkit/nsspellchecker/didchangeautomaticcapitalizationnotification.md) — To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticCapitalizationMessage`](doc://com.apple.appkit/documentation/AppKit/NSSpellChecker/DidChangeAutomaticCapitalizationMessage).
- [didChangeAutomaticDashSubstitutionNotification](../../appkit/nsspellchecker/didchangeautomaticdashsubstitutionnotification.md) — To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticDashSubstitutionMessage`](doc://com.apple.appkit/documentation/AppKit/NSSpellChecker/DidChangeAutomaticDashSubstitutionMessage).
- [didChangeAutomaticPeriodSubstitutionNotification](../../appkit/nsspellchecker/didchangeautomaticperiodsubstitutionnotification.md) — To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticPeriodSubstitutionMessage`](doc://com.apple.appkit/documentation/AppKit/NSSpellChecker/DidChangeAutomaticPeriodSubstitutionMessage).
- [didChangeAutomaticQuoteSubstitutionNotification](../../appkit/nsspellchecker/didchangeautomaticquotesubstitutionnotification.md) — To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticQuoteSubstitutionMessage`](doc://com.apple.appkit/documentation/AppKit/NSSpellChecker/DidChangeAutomaticQuoteSubstitutionMessage).
- [didChangeAutomaticSpellingCorrectionNotification](../../appkit/nsspellchecker/didchangeautomaticspellingcorrectionnotification.md) — This notification is posted when the spell checker did change text using automatic spell checking correction. The are posted to the application’s default notification center.
- [didChangeAutomaticTextReplacementNotification](../../appkit/nsspellchecker/didchangeautomatictextreplacementnotification.md) — Posted when the spell checker changed text using automatic text replacement.  This notification is posted to the app’s default notification center.
- [didResizeSubviewsNotification](../../appkit/nssplitview/didresizesubviewsnotification.md) — A notification that posts after a change to the size of some or all subviews of a split view.
- [willResizeSubviewsNotification](../../appkit/nssplitview/willresizesubviewsnotification.md) — A notification that posts before a change to the size of some or all subviews of a split view.
- [systemColorsDidChangeNotification](../../appkit/nscolor/systemcolorsdidchangenotification.md) — Sent when the system colors have changed, such as through a system control panel interface.
- [columnDidMoveNotification](../../appkit/nstableview/columndidmovenotification.md) — Posted whenever a column is moved by user action in an `NSTableView` object.
- [columnDidResizeNotification](../../appkit/nstableview/columndidresizenotification.md) — Posted whenever a column is resized in an `NSTableView` object.
- [selectionDidChangeNotification](../../appkit/nstableview/selectiondidchangenotification.md) — Posted after an `NSTableView` object’s selection changes.
- [selectionIsChangingNotification](../../appkit/nstableview/selectionischangingnotification.md) — Posted as an `NSTableView` object’s selection changes (while the mouse button is still down).
- [selectedAlternativeStringNotification](../../appkit/nstextalternatives/selectedalternativestringnotification.md) — Posted when the user selects an alternate string.
- [didBeginEditingNotification](../../appkit/nstext/didbegineditingnotification.md) — Posted when an `NSText` object begins any operation that changes characters or formatting attributes.
- [didChangeNotification](../../appkit/nstext/didchangenotification.md) — Posted after an `NSText` object performs any operation that changes characters or formatting attributes.
- [didEndEditingNotification](../../appkit/nstext/didendeditingnotification.md) — Posted when focus leaves an `NSText` object, whether or not any operation has changed characters or formatting attributes.
- [keyboardSelectionDidChangeNotification](../../appkit/nstextinputcontext/keyboardselectiondidchangenotification.md) — Posted after the selected text input source changes.
- [didChangeAutomaticTextCompletionNotification](../../appkit/nsspellchecker/didchangeautomatictextcompletionnotification.md) — To observe this notification using Swift concurrency, use [`NSSpellChecker.DidChangeAutomaticTextCompletionMessage`](doc://com.apple.appkit/documentation/AppKit/NSSpellChecker/DidChangeAutomaticTextCompletionMessage).
- [didBecomeActiveNotification](../../appkit/nsapplication/didbecomeactivenotification.md) — Posted immediately after the app becomes active.
- [didChangeOcclusionStateNotification](../../appkit/nsapplication/didchangeocclusionstatenotification.md) — Posted when the app’s occlusion state changes.
- [didChangeScreenParametersNotification](../../appkit/nsapplication/didchangescreenparametersnotification.md) — Posted when the configuration of the displays attached to the computer is changed.
- [didFinishLaunchingNotification](../../appkit/nsapplication/didfinishlaunchingnotification.md) — Posted at the end of the [`finishLaunching()`](doc://com.apple.appkit/documentation/AppKit/NSApplication/finishLaunching()) method to indicate that the app has completed launching and is ready to run.
- [didFinishRestoringWindowsNotification](../../appkit/nsapplication/didfinishrestoringwindowsnotification.md) — Posted when the app has finished restoring windows.
- [didHideNotification](../../appkit/nsapplication/didhidenotification.md) — Posted at the end of the [`hide(_:)`](doc://com.apple.appkit/documentation/AppKit/NSApplication/hide(_:)) method to indicate that the app is now hidden.
- [didResignActiveNotification](../../appkit/nsapplication/didresignactivenotification.md) — Posted immediately after the app gives up its active status to another app.
- [didUnhideNotification](../../appkit/nsapplication/didunhidenotification.md) — Posted at the end of the [`unhideWithoutActivation()`](doc://com.apple.appkit/documentation/AppKit/NSApplication/unhideWithoutActivation()) method to indicate that the app is now visible.
- [didUpdateNotification](../../appkit/nsapplication/didupdatenotification.md) — Posted at the end of the [`updateWindows()`](doc://com.apple.appkit/documentation/AppKit/NSApplication/updateWindows()) method to indicate that the app has finished updating its windows.
- [willBecomeActiveNotification](../../appkit/nsapplication/willbecomeactivenotification.md) — Posted immediately before the app becomes active.
- [willFinishLaunchingNotification](../../appkit/nsapplication/willfinishlaunchingnotification.md) — Posted at the start of the [`finishLaunching()`](doc://com.apple.appkit/documentation/AppKit/NSApplication/finishLaunching()) method to indicate that the app has completed its initialization process and is about to finish launching.
- [willHideNotification](../../appkit/nsapplication/willhidenotification.md) — Posted at the start of the [`hide(_:)`](doc://com.apple.appkit/documentation/AppKit/NSApplication/hide(_:)) method to indicate that the app is about to be hidden.
- [willResignActiveNotification](../../appkit/nsapplication/willresignactivenotification.md) — Posted immediately before the app gives up its active status to another app.
- [willTerminateNotification](../../appkit/nsapplication/willterminatenotification.md) — Sends a notification to terminate the app.
- [willUnhideNotification](../../appkit/nsapplication/willunhidenotification.md) — Posted at the start of the [`unhideWithoutActivation()`](doc://com.apple.appkit/documentation/AppKit/NSApplication/unhideWithoutActivation()) method to indicate that the app is about to become visible.
- [willUpdateNotification](../../appkit/nsapplication/willupdatenotification.md) — Posted at the start of the [`updateWindows()`](doc://com.apple.appkit/documentation/AppKit/NSApplication/updateWindows()) method to indicate that the app is about to update its windows.
- [columnConfigurationDidChangeNotification](../../appkit/nsbrowser/columnconfigurationdidchangenotification.md) — Notifies the delegate when the width of a browser column has changed.
- [NSClassDescriptionNeededForClassNotification](name-swift.struct/nsclassdescriptionneededforclass.md) — Posted by [+ classDescriptionForClass:](<../nsclassdescription/init(for_).md>) when a class description cannot be found for a class.
- [NSApplicationProtectedDataDidBecomeAvailable](name-swift.struct/nsapplicationprotecteddatadidbecomeavailable.md)
- [NSApplicationProtectedDataWillBecomeUnavailable](name-swift.struct/nsapplicationprotecteddatawillbecomeunavailable.md)
- [announcementRequested](../../appkit/nsaccessibility-swift.struct/notification/announcementrequested.md) — This notification posts when an app needs to make an announcement to the user. If VoiceOver is enabled, it’s presented via speech and/or braille. Otherwise, it does nothing.
- [applicationActivated](../../appkit/nsaccessibility-swift.struct/notification/applicationactivated.md) — This notification is posted after the app has been activated. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [applicationDeactivated](../../appkit/nsaccessibility-swift.struct/notification/applicationdeactivated.md) — This notification is posted after the app has been deactivated.  Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [applicationHidden](../../appkit/nsaccessibility-swift.struct/notification/applicationhidden.md) — This notification is posted after the app is hidden. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [applicationShown](../../appkit/nsaccessibility-swift.struct/notification/applicationshown.md) — This notification is posted after the app is shown. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [created](../../appkit/nsaccessibility-swift.struct/notification/created.md) — This notification is posted after an accessibility element is created. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [drawerCreated](../../appkit/nsaccessibility-swift.struct/notification/drawercreated.md) — This notification is posted after a drawer appears. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [focusedUIElementChanged](../../appkit/nsaccessibility-swift.struct/notification/focuseduielementchanged.md) — This notification is posted after an accessibility element gains focus. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [focusedWindowChanged](../../appkit/nsaccessibility-swift.struct/notification/focusedwindowchanged.md) — This notification is posted after the key window changes. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [helpTagCreated](../../appkit/nsaccessibility-swift.struct/notification/helptagcreated.md) — This notification is posted after a help tag appears. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [layoutChanged](../../appkit/nsaccessibility-swift.struct/notification/layoutchanged.md) — This notification is posted after the UI changes in a way that requires the attention of an accessibility client. This notification should be accompanied by a `userInfo` dictionary with the key [`uiElements`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/NotificationUserInfoKey/uiElements) and an array containing the UI elements that have been added or changed. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [mainWindowChanged](../../appkit/nsaccessibility-swift.struct/notification/mainwindowchanged.md) — This notification is posted after the main window changes. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [moved](../../appkit/nsaccessibility-swift.struct/notification/moved.md) — This notification is posted after an accessibility element moves. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [resized](../../appkit/nsaccessibility-swift.struct/notification/resized.md) — This notification is posted after an accessibility element’s size changes. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [rowCollapsed](../../appkit/nsaccessibility-swift.struct/notification/rowcollapsed.md) — This notification is posted after a row collapses. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [rowCountChanged](../../appkit/nsaccessibility-swift.struct/notification/rowcountchanged.md) — This notification is posted after a row is added or deleted. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [rowExpanded](../../appkit/nsaccessibility-swift.struct/notification/rowexpanded.md) — This notification is posted after a row expands. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [selectedCellsChanged](../../appkit/nsaccessibility-swift.struct/notification/selectedcellschanged.md) — This notification is posted after one or more cells in a cell-based table are selected or deselected. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [selectedChildrenChanged](../../appkit/nsaccessibility-swift.struct/notification/selectedchildrenchanged.md) — This notification is posted after one or more child elements are selected or deselected. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [selectedChildrenMoved](../../appkit/nsaccessibility-swift.struct/notification/selectedchildrenmoved.md) — This notification is posted after the selected items in a layout area move. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [selectedColumnsChanged](../../appkit/nsaccessibility-swift.struct/notification/selectedcolumnschanged.md) — This notification is posted after one or more columns are selected or deselected. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [selectedRowsChanged](../../appkit/nsaccessibility-swift.struct/notification/selectedrowschanged.md) — This notification is posted after one or more rows are selected or deselected. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [selectedTextChanged](../../appkit/nsaccessibility-swift.struct/notification/selectedtextchanged.md) — This notification is posted after text is selected or deselected.  Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [sheetCreated](../../appkit/nsaccessibility-swift.struct/notification/sheetcreated.md) — This notification is posted after a sheet appears.  Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [titleChanged](../../appkit/nsaccessibility-swift.struct/notification/titlechanged.md) — This notification is posted after an accessibility element’s title changes. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [uiElementDestroyed](../../appkit/nsaccessibility-swift.struct/notification/uielementdestroyed.md) — This notification is posted after an accessibility element is destroyed. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [unitsChanged](../../appkit/nsaccessibility-swift.struct/notification/unitschanged.md) — This notification is posted after the units in a layout area change. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [valueChanged](../../appkit/nsaccessibility-swift.struct/notification/valuechanged.md) — This notification is posted after an accessibility element’s value changes. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [windowCreated](../../appkit/nsaccessibility-swift.struct/notification/windowcreated.md) — This notification is posted after a new window appears. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [windowDeminiaturized](../../appkit/nsaccessibility-swift.struct/notification/windowdeminiaturized.md) — This notification is posted after a window is restored to full size from the Dock.  Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [windowMiniaturized](../../appkit/nsaccessibility-swift.struct/notification/windowminiaturized.md) — This notification is posted after a window is put in the Dock. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [windowMoved](../../appkit/nsaccessibility-swift.struct/notification/windowmoved.md) — This notification is posted after a window moves.  Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [windowResized](../../appkit/nsaccessibility-swift.struct/notification/windowresized.md) — This notification is posted after a window’s size changes. Post this notification using the [`post(element:notification:)`](doc://com.apple.appkit/documentation/AppKit/NSAccessibility-swift.struct/post(element:notification:)) function instead of an `NSNotificationCenter` instance.
- [progressMarkNotification](../../appkit/nsanimation/progressmarknotification.md) — Posted when the current progress of a running animation reaches one of its progress marks.
- [antialiasThresholdChangedNotification](../../appkit/nsfont/antialiasthresholdchangednotification.md) — Posted after the threshold for antialiasing changes.
- [globalFrameDidChangeNotification](../../appkit/nsview/globalframedidchangenotification.md) — Posted whenever an `NSView` object that has attached surfaces (that is, `NSOpenGLContext` objects) moves to a different screen, or other cases where the `NSOpenGLContext` object needs to be updated. _(deprecated)_

### AVFAudio

- [AVAudioEngineConfigurationChange](name-swift.struct/avaudioengineconfigurationchange.md) — A notification the framework posts when the audio engine configuration changes.
- [AVAudioUnitComponentTagsDidChange](name-swift.struct/avaudiounitcomponenttagsdidchange.md) — A notification that indicates when component tags change.
- [interruptionNotification](../../avfaudio/avaudiosession/interruptionnotification.md) — A notification the system posts when an audio interruption occurs. _(deprecated)_
- [mediaServicesWereLostNotification](../../avfaudio/avaudiosession/mediaserviceswerelostnotification.md) — A notification the system posts when it terminates the media server.
- [mediaServicesWereResetNotification](../../avfaudio/avaudiosession/mediaserviceswereresetnotification.md) — A notification the system posts when the media server restarts.
- [routeChangeNotification](../../avfaudio/avaudiosession/routechangenotification.md) — A notification the system posts when its audio route changes.
- [silenceSecondaryAudioHintNotification](../../avfaudio/avaudiosession/silencesecondaryaudiohintnotification.md) — A notification the system posts when the primary audio from other apps starts and stops.

### AVFoundation

- [AVAssetChapterMetadataGroupsDidChange](name-swift.struct/avassetchaptermetadatagroupsdidchange.md) — A notification the system posts when an asset’s chapter metadata groups change.
- [AVAssetContainsFragmentsDidChange](name-swift.struct/avassetcontainsfragmentsdidchange.md) — A notification the system posts when an asset’s fragments change.
- [AVAssetDurationDidChange](name-swift.struct/avassetdurationdidchange.md) — A notification the system posts when a fragmented asset minder observes a change to a fragmented asset’s duration.
- [AVAssetMediaSelectionGroupsDidChange](name-swift.struct/avassetmediaselectiongroupsdidchange.md) — A notification the system posts when an asset’s media selection groups change.
- [AVAssetTrackSegmentsDidChange](name-swift.struct/avassettracksegmentsdidchange.md) — A notification the system posts when a fragmented asset minder observes a change to a fragmented asset track’s segments.
- [AVAssetTrackTimeRangeDidChange](name-swift.struct/avassettracktimerangedidchange.md) — A notification the system posts when a fragmented asset minder observes a change to a fragmented asset track’s time range.
- [AVAssetTrackTrackAssociationsDidChange](name-swift.struct/avassettracktrackassociationsdidchange.md) — A notification the system posts when the track associations for an asset track change.
- [AVAssetWasDefragmented](name-swift.struct/avassetwasdefragmented.md) — A notification the system posts when a fragmented asset minder observes that the system defragments the asset on disk.
- [subjectAreaDidChangeNotification](../../avfoundation/avcapturedevice/subjectareadidchangenotification.md) — A notification the system posts when a capture device detects a substantial change to the video subject area.
- [wasConnectedNotification](../../avfoundation/avcapturedevice/wasconnectednotification.md) — A notification the system posts when a new capture device becomes available.
- [wasDisconnectedNotification](../../avfoundation/avcapturedevice/wasdisconnectednotification.md) — A notification the system posts when an existing device becomes unavailable.
- [formatDescriptionDidChangeNotification](../../avfoundation/avcaptureinput/port/formatdescriptiondidchangenotification.md) — A notification the system posts when the capture input port’s format description changes.
- [didStartRunningNotification](../../avfoundation/avcapturesession/didstartrunningnotification.md) — A notification the system posts when a capture session starts.
- [didStopRunningNotification](../../avfoundation/avcapturesession/didstoprunningnotification.md) — A notification the system posts when a capture session stops.
- [interruptionEndedNotification](../../avfoundation/avcapturesession/interruptionendednotification.md) — A notification the system posts when an interruption to a capture session finishes.
- [runtimeErrorNotification](../../avfoundation/avcapturesession/runtimeerrornotification.md) — A notification the system posts when an error occurs during a capture session.
- [wasInterruptedNotification](../../avfoundation/avcapturesession/wasinterruptednotification.md) — A notification the system posts when it interrupts a capture session.
- [AVFragmentedMovieContainsMovieFragmentsDidChange](name-swift.struct/avfragmentedmoviecontainsmoviefragmentsdidchange.md) — A notification the system posts when a fragmented movie minder observes a change to a movie’s fragments.
- [AVFragmentedMovieDurationDidChange](name-swift.struct/avfragmentedmoviedurationdidchange.md) — A notification the system posts when a fragmented movie minder observes a change to a movie’s duration.
- [AVFragmentedMovieTrackSegmentsDidChange](name-swift.struct/avfragmentedmovietracksegmentsdidchange.md) — A notification the system posts when a fragmented movie minder observes a change to a fragmented movie track’s segments.
- [AVFragmentedMovieTrackTimeRangeDidChange](name-swift.struct/avfragmentedmovietracktimerangedidchange.md) — A notification the system posts when a fragmented movie minder observes a change to a movie track’s time range.
- [AVFragmentedMovieWasDefragmented](name-swift.struct/avfragmentedmoviewasdefragmented.md) — A notification the system posts when a fragmented movie minder observes that the system defragments the asset on disk.
- [AVPlayerAvailableHDRModesDidChange](name-swift.struct/avplayeravailablehdrmodesdidchange.md) — A notification the system posts when a player’s available HDR modes change. _(deprecated)_
- [assetListResponseStatusDidChangeNotification](../../avfoundation/avplayerinterstitialeventmonitor/assetlistresponsestatusdidchangenotification.md) — A notification the system posts when the status of an interstitial event’s asset list response changes.
- [didPlayToEndTimeNotification](../../avfoundation/avplayeritem/didplaytoendtimenotification.md) — A notification the system posts when a player item plays to its end time.
- [failedToPlayToEndTimeNotification](../../avfoundation/avplayeritem/failedtoplaytoendtimenotification.md) — A notification that the system posts when a player item fails to play to its end time.
- [newAccessLogEntryNotification](../../avfoundation/avplayeritem/newaccesslogentrynotification.md) — A notification the system posts when a player item adds a new entry to its access log.
- [newErrorLogEntryNotification](../../avfoundation/avplayeritem/newerrorlogentrynotification.md) — A notification the system posts when a player item adds a new entry to its error log.
- [playbackStalledNotification](../../avfoundation/avplayeritem/playbackstallednotification.md) — A notification the system posts when a player item media doesn’t arrive in time to continue playback.
- [AVRouteDetectorMultipleRoutesDetectedDidChange](name-swift.struct/avroutedetectormultipleroutesdetecteddidchange.md) — A notification the system posts when changes occur to its detected routes.
- [AVSampleBufferAudioRendererOutputConfigurationDidChange](name-swift.struct/avsamplebufferaudiorendereroutputconfigurationdidchange.md) — A notification the system posts to indicate that the hardware configuration doesn’t match the enqueued data format. _(deprecated)_
- [AVSampleBufferAudioRendererWasFlushedAutomatically](name-swift.struct/avsamplebufferaudiorendererwasflushedautomatically.md) — A notification the system posts when a renderer flushes its enqueued media data without an explicit request to do so. _(deprecated)_
- [AVSampleBufferDisplayLayerFailedToDecode](name-swift.struct/avsamplebufferdisplaylayerfailedtodecode.md) — A notification the system posts when a sample buffer display layer fails to decode.
- [AVSampleBufferDisplayLayerOutputObscuredDueToInsufficientExternalProtectionDidChange](name-swift.struct/avsamplebufferdisplaylayeroutputobscuredduetoinsufficientexternalprotectiondidchange.md) — A notification the system posts when the current device configuration doesn’t support the external content protection mechanism.
- [AVSampleBufferDisplayLayerRequiresFlushToResumeDecodingDidChange](name-swift.struct/avsamplebufferdisplaylayerrequiresflushtoresumedecodingdidchange.md) — A notification the system posts when a sample buffer display layer changes its decoding requirements.
- [timeJumpedNotification](../../avfoundation/avplayeritem/timejumpednotification.md) — A notification the system posts when a player item’s time changes discontinuously.
- [AVFragmentedMovieTrackTotalSampleDataLengthDidChange](name-swift.struct/avfragmentedmovietracktotalsampledatalengthdidchange.md) — A notification the system posts when the sample data length of a fragmented movie track changes. _(deprecated)_
- [AVPlayerItemTimeJumped](name-swift.struct/avplayeritemtimejumped.md) — A notification the system posts to indicate a jump in a player item’s current time. _(deprecated)_
- [timeJumpedNotification](../../avfoundation/avplayeritem/timejumpednotification.md) — A notification the system posts when a player item’s time changes discontinuously.

### AVKit

- [AVDisplayManagerModeSwitchSettingsChanged](name-swift.struct/avdisplaymanagermodeswitchsettingschanged.md) — A notification the display manager posts when a user changes their Match Content settings in the tvOS Settings app.
- [AVDisplayManagerModeSwitchStart](name-swift.struct/avdisplaymanagermodeswitchstart.md) — A notification the display manager posts when a display begins a mode switch.
- [AVDisplayManagerModeSwitchEnd](name-swift.struct/avdisplaymanagermodeswitchend.md) — A notification the display manager posts when a display ends a mode switch.

### ClockKit

- [CLKComplicationServerActiveComplicationsDidChange](name-swift.struct/clkcomplicationserveractivecomplicationsdidchange.md) — Posted when the set of active complications changes. _(deprecated)_

### CloudKit

- [CKAccountChanged](name-swift.struct/ckaccountchanged.md) — A notification that a container posts when the status of an iCloud account changes.

### Contacts

- [CNContactStoreDidChange](name-swift.struct/cncontactstoredidchange.md) — Posted when changes occur to the contact store.

### Core Data

- [NSManagedObjectContextDidSave](name-swift.struct/nsmanagedobjectcontextdidsave.md) — A notification that posts after a context finishes writing unsaved changes.
- [NSManagedObjectContextObjectsDidChange](name-swift.struct/nsmanagedobjectcontextobjectsdidchange.md) — A notification that posts when there are changes to context’s registered managed objects.
- [NSManagedObjectContextWillSave](name-swift.struct/nsmanagedobjectcontextwillsave.md) — A notification that posts before a context writes unsaved changes.
- [NSPersistentStoreCoordinatorStoresDidChange](name-swift.struct/nspersistentstorecoordinatorstoresdidchange.md) — A notification that the coordinator posts after its registered stores change.
- [NSPersistentStoreCoordinatorStoresWillChange](name-swift.struct/nspersistentstorecoordinatorstoreswillchange.md) — A notification that posts before a coordinator changes its registered stores.
- [NSPersistentStoreCoordinatorWillRemoveStore](name-swift.struct/nspersistentstorecoordinatorwillremovestore.md) — A notification that posts before a coordinator removes a store.
- [NSCoreDataCoreSpotlightDelegateIndexDidUpdate](name-swift.struct/nscoredatacorespotlightdelegateindexdidupdate.md) — A notification that posts after Spotlight completes an index update.
- [NSManagedObjectContextDidMergeChangesObjectIDs](name-swift.struct/nsmanagedobjectcontextdidmergechangesobjectids.md) — A notification that posts after a context merges changes from a different notification.
- [NSManagedObjectContextDidSaveObjectIDs](name-swift.struct/nsmanagedobjectcontextdidsaveobjectids.md) — A notification that posts after a context finishes writing changes.
- [NSPersistentStoreRemoteChange](name-swift.struct/nspersistentstoreremotechange.md) — A notification that posts after another process writes to a persistent store.
- [NSPersistentStoreDidImportUbiquitousContentChanges](name-swift.struct/nspersistentstoredidimportubiquitouscontentchanges.md) — Posted after records are imported from the ubiquitous content store. _(deprecated)_

### Core Telephony

- [CTServiceRadioAccessTechnologyDidChange](name-swift.struct/ctserviceradioaccesstechnologydidchange.md) — A notification that posts when radio access technology changes.
- [CTRadioAccessTechnologyDidChange](name-swift.struct/ctradioaccesstechnologydidchange.md) — The name of the notification indicating that the radio access technology changed for one of the services. _(deprecated)_

### Core WLAN

- [CWBSSIDDidChange](name-swift.struct/cwbssiddidchange.md) _(deprecated)_
- [CWCountryCodeDidChange](name-swift.struct/cwcountrycodedidchange.md) _(deprecated)_
- [CWLinkDidChange](name-swift.struct/cwlinkdidchange.md) _(deprecated)_
- [CWLinkQualityDidChange](name-swift.struct/cwlinkqualitydidchange.md) _(deprecated)_
- [CWModeDidChange](name-swift.struct/cwmodedidchange.md) _(deprecated)_
- [CWPowerDidChange](name-swift.struct/cwpowerdidchange.md) _(deprecated)_
- [CWSSIDDidChange](name-swift.struct/cwssiddidchange.md) _(deprecated)_
- [CWScanCacheDidUpdate](name-swift.struct/cwscancachedidupdate.md) _(deprecated)_

### EventKit

- [EKEventStoreChanged](name-swift.struct/ekeventstorechanged.md) — A notification posted when changes are made to the Calendar database.

### External Accessory

- [EAAccessoryDidConnect](name-swift.struct/eaaccessorydidconnect.md) — A notification that the system sends when an accessory becomes connected and available for your application to use.
- [EAAccessoryDidDisconnect](name-swift.struct/eaaccessorydiddisconnect.md) — A notification that is posted when an accessory is disconnected and no longer available for your application to use.

### File Provider

- [fileProviderDomainDidChange](name-swift.struct/fileproviderdomaindidchange.md)
- [fileProviderMaterializedSetDidChange](name-swift.struct/fileprovidermaterializedsetdidchange.md)
- [fileProviderPendingSetDidChange](name-swift.struct/fileproviderpendingsetdidchange.md)

### Foundation

- [NSUbiquityIdentityDidChangeNotification](name-swift.struct/nsubiquityidentitydidchange.md) — Sent after the iCloud (“ubiquity”) identity has changed.
- [NSAppleEventManagerWillProcessFirstEventNotification](name-swift.struct/nsappleeventmanagerwillprocessfirstevent.md) — Posted by `NSAppleEventManager` before it first dispatches an Apple event. Your application can use this notification to avoid registering any Apple event handlers until the first time at which they may be needed.
- [NSUndoManagerCheckpointNotification](name-swift.struct/nsundomanagercheckpoint.md) — Posted whenever an undo manager opens or closes an undo group (except when it opens a top-level group) and when checking the redo stack.
- [NSUndoManagerDidCloseUndoGroupNotification](name-swift.struct/nsundomanagerdidcloseundogroup.md) — Posted after an undo manager closes an undo group.
- [NSUndoManagerDidOpenUndoGroupNotification](name-swift.struct/nsundomanagerdidopenundogroup.md) — Posted whenever an undo manager opens an undo group.
- [NSUndoManagerDidRedoChangeNotification](name-swift.struct/nsundomanagerdidredochange.md) — Posted just after an undo manager performs a redo operation.
- [NSUndoManagerDidUndoChangeNotification](name-swift.struct/nsundomanagerdidundochange.md) — Posted just after an undo manager performs an undo operation.
- [NSUndoManagerWillCloseUndoGroupNotification](name-swift.struct/nsundomanagerwillcloseundogroup.md) — Posted before an undo manager closes an undo group.
- [NSUndoManagerWillRedoChangeNotification](name-swift.struct/nsundomanagerwillredochange.md) — Posted just before an undo manager performs a redo operation.
- [NSUndoManagerWillUndoChangeNotification](name-swift.struct/nsundomanagerwillundochange.md) — Posted just before an undo manager performs an undo operation.
- [NSWillBecomeMultiThreadedNotification](name-swift.struct/nswillbecomemultithreaded.md) — Posted when the first thread is detached from the current thread. The `NSThread` class posts this notification at most once—the first time a thread is detached using [+ detachNewThreadSelector:toTarget:withObject:](<../thread/detachnewthreadselector(__totarget_with_).md>) or the [- start](<../thread/start().md>) method. Subsequent invocations of those methods do not post this notification. Observers of this notification have their notification method invoked in the main thread, not the new thread. The observer notification methods always execute before the new thread begins executing. _(deprecated)_
- [NSBundleResourceRequestLowDiskSpaceNotification](name-swift.struct/nsbundleresourcerequestlowdiskspace.md) — Posted after the system detects that the amount of available disk space is getting low. The notification is posted to the default notification center. _(deprecated)_
- [NSCalendarDayChangedNotification](name-swift.struct/nscalendardaychanged.md) — A notification that is posted whenever the calendar day of the system changes, as determined by the system calendar, locale, and time zone.
- [NSDidBecomeSingleThreadedNotification](name-swift.struct/nsdidbecomesinglethreaded.md) — Not implemented. _(deprecated)_
- [NSExtensionHostDidBecomeActiveNotification](name-swift.struct/nsextensionhostdidbecomeactive.md) — Posted when the extension’s host app moves from the inactive to the active state.
- [NSExtensionHostDidEnterBackgroundNotification](name-swift.struct/nsextensionhostdidenterbackground.md) — Posted when the extension’s host app begins running in the background.
- [NSExtensionHostWillEnterForegroundNotification](name-swift.struct/nsextensionhostwillenterforeground.md) — Posted when the extension’s host app begins running in the foreground.
- [NSExtensionHostWillResignActiveNotification](name-swift.struct/nsextensionhostwillresignactive.md) — Posted when the extension’s host app moves from the active to the inactive state.
- [NSFileHandleConnectionAcceptedNotification](name-swift.struct/nsfilehandleconnectionaccepted.md) — Posted when a file handle object establishes a socket connection between two processes, creates a file handle object for one end of the connection, and makes this object available to observers.
- [NSFileHandleDataAvailableNotification](name-swift.struct/nsfilehandledataavailable.md) — Posted when the file handle determines that data is currently available for reading in a file or at a communications channel.
- [NSFileHandleReadToEndOfFileCompletionNotification](name-swift.struct/nsfilehandlereadtoendoffilecompletion.md) — Posted when the file handle reads all data in the file or, in a communications channel, until the other process signals the end of data.
- [NSHTTPCookieManagerAcceptPolicyChangedNotification](name-swift.struct/nshttpcookiemanageracceptpolicychanged.md) — A notification posted when the acceptance policy of the cookie storage has changed. _(deprecated)_
- [NSHTTPCookieManagerCookiesChangedNotification](name-swift.struct/nshttpcookiemanagercookieschanged.md) — A notification posted when the cookies stored in the cookie storage have changed.
- [NSMetadataQueryDidFinishGatheringNotification](name-swift.struct/nsmetadataquerydidfinishgathering.md) — Posted when the receiver has finished with the initial result-gathering phase of the query.
- [NSMetadataQueryDidStartGatheringNotification](name-swift.struct/nsmetadataquerydidstartgathering.md) — Posted when the receiver begins with the initial result-gathering phase of the query.
- [NSMetadataQueryDidUpdateNotification](name-swift.struct/nsmetadataquerydidupdate.md) — Posted when the receiver’s results have changed during the live-update phase of the query.
- [NSMetadataQueryGatheringProgressNotification](name-swift.struct/nsmetadataquerygatheringprogress.md) — Posted as the receiver is collecting results during the initial result-gathering phase of the query.
- [NSProcessInfoPowerStateDidChangeNotification](name-swift.struct/nsprocessinfopowerstatedidchange.md) — Posts when the power state of a device changes.
- [NSSystemClockDidChangeNotification](name-swift.struct/nssystemclockdidchange.md) — A notification posted whenever the system clock is changed.
- [NSSystemTimeZoneDidChangeNotification](name-swift.struct/nssystemtimezonedidchange.md) — A notification posted when the time zone changes.
- [NSThreadWillExitNotification](name-swift.struct/nsthreadwillexit.md) — An `NSThread` object posts this notification when it receives the [+ exit](<../thread/exit().md>) message, before the thread exits. Observer methods invoked to receive this notification execute in the exiting thread, before it exits. _(deprecated)_
- [NSURLCredentialStorageChangedNotification](name-swift.struct/nsurlcredentialstoragechanged.md) — A notification posted when the set of stored credentials changes. _(deprecated)_

### Game Controller

- [GCControllerDidConnect](name-swift.struct/gccontrollerdidconnect.md) — A notification that posts after a controller connects to the device.
- [GCControllerDidDisconnect](name-swift.struct/gccontrollerdiddisconnect.md) — A notification that posts after a controller disconnects from the device.
- [GCControllerDidBecomeCurrent](name-swift.struct/gccontrollerdidbecomecurrent.md) — A notification that posts when a controller becomes the current controller.
- [GCControllerDidStopBeingCurrent](name-swift.struct/gccontrollerdidstopbeingcurrent.md) — A notification that posts when a controller stops being the current controller.
- [GCControllerUserCustomizationsDidChange](name-swift.struct/gccontrollerusercustomizationsdidchange.md) — A notification that posts when the user customizes the button mappings or other settings of a controller.
- [GCKeyboardDidConnect](name-swift.struct/gckeyboarddidconnect.md) — A notification that posts after a keyboard connects to the device.
- [GCKeyboardDidDisconnect](name-swift.struct/gckeyboarddiddisconnect.md) — A notification that posts after a single keyboard, or the last of multiple keyboards, disconnects from the device.
- [GCMouseDidBecomeCurrent](name-swift.struct/gcmousedidbecomecurrent.md) — A notification that posts when a mouse becomes the most recent mouse that the user connects.
- [GCMouseDidConnect](name-swift.struct/gcmousedidconnect.md) — A notification that posts after a mouse connects to the device.
- [GCMouseDidDisconnect](name-swift.struct/gcmousediddisconnect.md) — A notification that posts after a mouse disconnects from the device.
- [GCMouseDidStopBeingCurrent](name-swift.struct/gcmousedidstopbeingcurrent.md) — A notification that posts when a mouse stops being the most recent mouse that the user connects.
- [GCRacingWheelDidConnect](name-swift.struct/gcracingwheeldidconnect.md) — A notification that posts after a racing wheel controller connects to the device.
- [GCRacingWheelDidDisconnect](name-swift.struct/gcracingwheeldiddisconnect.md) — A notification that posts after a racing wheel controller disconnects from the device.

### GameKit

- [GKPlayerAuthenticationDidChangeNotificationName](name-swift.struct/gkplayerauthenticationdidchangenotificationname.md) — A notification that posts after GameKit authenticates the local player.
- [GKPlayerDidChangeNotificationName](name-swift.struct/gkplayerdidchangenotificationname.md) — A notification that posts when a player object’s data changes.

### HealthKit

- [HKUserPreferencesDidChange](name-swift.struct/hkuserpreferencesdidchange.md) — Notifies observers whenever the user changes his or her preferred units.

### HomeKit

- [HMCharacteristicPropertySupportsEventNotification](../../homekit/hmcharacteristicpropertysupportseventnotification-2f0ml.md) — The characteristic supports event notifications.

### IOBluetooth

- [IOBluetoothHostControllerPoweredOff](name-swift.struct/iobluetoothhostcontrollerpoweredoff.md)
- [IOBluetoothHostControllerPoweredOn](name-swift.struct/iobluetoothhostcontrollerpoweredon.md)
- [IOBluetoothL2CAPChannelPublished](name-swift.struct/iobluetoothl2capchannelpublished.md)
- [IOBluetoothL2CAPChannelTerminated](name-swift.struct/iobluetoothl2capchannelterminated.md)

### iTunes Library

- [ITLibraryDidChange](name-swift.struct/itlibrarydidchange.md) — A notification the system posts when a library change occurs.

### MapKit

- [MKAnnotationCalloutInfoDidChange](name-swift.struct/mkannotationcalloutinfodidchange.md) — A property to observe to determine when the title or subtitle information of an annotation object changes. _(deprecated)_

### MediaPlayer

- [MPMusicPlayerControllerQueueDidChange](name-swift.struct/mpmusicplayercontrollerqueuedidchange.md) — Indicates the music player’s queue changed.
- [MPMediaLibraryDidChange](name-swift.struct/mpmedialibrarydidchange.md) — Indicates the media library has changed.
- [MPMediaPlaybackIsPreparedToPlayDidChange](name-swift.struct/mpmediaplaybackispreparedtoplaydidchange.md) — Indicates that the prepared to play status of the media player has changed. _(deprecated)_
- [MPMusicPlayerControllerNowPlayingItemDidChange](name-swift.struct/mpmusicplayercontrollernowplayingitemdidchange.md) — Posted when the currently playing media item has changed.
- [MPMusicPlayerControllerPlaybackStateDidChange](name-swift.struct/mpmusicplayercontrollerplaybackstatedidchange.md) — Posted when the playback state changes programmatically or by user action.
- [MPMusicPlayerControllerVolumeDidChange](name-swift.struct/mpmusicplayercontrollervolumedidchange.md) — Posted when the audio playback volume for the music player has changed.
- [MPMovieDurationAvailable](name-swift.struct/mpmoviedurationavailable.md) — Posted when the duration of a movie has been determined. There is no `userInfo` dictionary. _(deprecated)_
- [MPMovieMediaTypesAvailable](name-swift.struct/mpmoviemediatypesavailable.md) — Posted when the available media types in a movie are determined. There is no `userInfo` dictionary. _(deprecated)_
- [MPMovieNaturalSizeAvailable](name-swift.struct/mpmovienaturalsizeavailable.md) — Posted when the natural frame size of a movie is first determined or subsequently changes. There is no `userInfo` dictionary. _(deprecated)_
- [MPMoviePlayerDidEnterFullscreen](name-swift.struct/mpmovieplayerdidenterfullscreen.md) — Posted when a movie player has entered full-screen mode. There is no `userInfo` dictionary. _(deprecated)_
- [MPMoviePlayerDidExitFullscreen](name-swift.struct/mpmovieplayerdidexitfullscreen.md) — Posted when a movie player has exited full-screen mode. There is no `userInfo` dictionary. _(deprecated)_
- [MPMoviePlayerIsAirPlayVideoActiveDidChange](name-swift.struct/mpmovieplayerisairplayvideoactivedidchange.md) — Posted when a movie player has started or ended playing a movie via AirPlay. There is no `userInfo` dictionary. _(deprecated)_
- [MPMoviePlayerLoadStateDidChange](name-swift.struct/mpmovieplayerloadstatedidchange.md) — Posted when a movie player’s network buffering state has changed. There is no `userInfo` dictionary. _(deprecated)_
- [MPMoviePlayerNowPlayingMovieDidChange](name-swift.struct/mpmovieplayernowplayingmoviedidchange.md) — Posted when the currently playing movie has changed. There is no `userInfo` dictionary. _(deprecated)_
- [MPMoviePlayerPlaybackDidFinish](name-swift.struct/mpmovieplayerplaybackdidfinish.md) — Posted when a movie has finished playing. _(deprecated)_
- [MPMoviePlayerPlaybackStateDidChange](name-swift.struct/mpmovieplayerplaybackstatedidchange.md) — Posted when a movie player’s playback state has changed. There is no `userInfo` dictionary. _(deprecated)_
- [MPMoviePlayerReadyForDisplayDidChange](name-swift.struct/mpmovieplayerreadyfordisplaydidchange.md) — Posted when the ready for display state changes. _(deprecated)_
- [MPMoviePlayerScalingModeDidChange](name-swift.struct/mpmovieplayerscalingmodedidchange.md) — Posted when the scaling mode of a movie player has changed. There is no `userInfo` dictionary. _(deprecated)_
- [MPMoviePlayerThumbnailImageRequestDidFinish](name-swift.struct/mpmovieplayerthumbnailimagerequestdidfinish.md) — Posted when a request to capture a thumbnail from a movie has finished whether the request succeeded or failed. Upon successful capture of a thumbnail, the `userInfo` dictionary contains values for the following keys: _(deprecated)_
- [MPMoviePlayerTimedMetadataUpdated](name-swift.struct/mpmovieplayertimedmetadataupdated.md) — Posted when new timed metadata arrives. _(deprecated)_
- [MPMoviePlayerWillEnterFullscreen](name-swift.struct/mpmovieplayerwillenterfullscreen.md) — Posted when a movie player is about to enter full-screen mode. _(deprecated)_
- [MPMoviePlayerWillExitFullscreen](name-swift.struct/mpmovieplayerwillexitfullscreen.md) — Posted when a movie player is about to exit full-screen mode. _(deprecated)_
- [MPMovieSourceTypeAvailable](name-swift.struct/mpmoviesourcetypeavailable.md) — Posted when the source type of a movie was previously unknown and is newly available. There is no `userInfo` dictionary. _(deprecated)_
- [MPVolumeViewWirelessRouteActiveDidChange](name-swift.struct/mpvolumeviewwirelessrouteactivedidchange.md) — Indicates the active wireless route changed. _(deprecated)_
- [MPVolumeViewWirelessRoutesAvailableDidChange](name-swift.struct/mpvolumeviewwirelessroutesavailabledidchange.md) — Indicates the available wireless routes changed. _(deprecated)_

### MessageUI

- [MFMessageComposeViewControllerTextMessageAvailabilityDidChange](name-swift.struct/mfmessagecomposeviewcontrollertextmessageavailabilitydidchange.md) — Posted when the current device’s ability to send text messages changes.
- [MFMessageComposeViewControllerTextMessageAvailabilityDidChange](name-swift.struct/mfmessagecomposeviewcontrollertextmessageavailabilitydidchange.md) — Posted when the current device’s ability to send text messages changes.

### NetworkExtension

- [NEFilterConfigurationDidChange](name-swift.struct/nefilterconfigurationdidchange.md) — Posted after the filter configuration stored in the Network Extension preferences changes.
- [NEVPNConfigurationChange](name-swift.struct/nevpnconfigurationchange.md) — Posted after the VPN configuration stored in the Network Extension preferences changes.
- [NEVPNStatusDidChange](name-swift.struct/nevpnstatusdidchange.md) — Posted when the status of the VPN connection changes.
- [NEDNSProxyConfigurationDidChange](name-swift.struct/nednsproxyconfigurationdidchange.md) — A notification that is posted when the DNS proxy configuration changes.
- [NEDNSSettingsConfigurationDidChange](name-swift.struct/nednssettingsconfigurationdidchange.md)

### PassKit

- [PKPassLibraryDidChange](../../passkit/pkpasslibrarynotificationname/pkpasslibrarydidchange.md) — A notification that PassKit posts when the pass library changes.
- [PKPassLibraryRemotePaymentPassesDidChange](../../passkit/pkpasslibrarynotificationname/pkpasslibraryremotepaymentpassesdidchange.md) — A notification that PassKit posts when it adds or removes a pass on a paired remote device.

### PDFKit

- [PDFDocumentDidBeginFind](name-swift.struct/pdfdocumentdidbeginfind.md) — A notification that the document began a find operation.
- [PDFDocumentDidBeginPageFind](name-swift.struct/pdfdocumentdidbeginpagefind.md) — A notification that a find operation begins working on a new page of a document.
- [PDFDocumentDidBeginPageWrite](name-swift.struct/pdfdocumentdidbeginpagewrite.md) — A notification that a write operation begins working on a page in a document.
- [PDFDocumentDidBeginWrite](name-swift.struct/pdfdocumentdidbeginwrite.md) — A notification that a write operation begins working on a document.
- [PDFDocumentDidEndFind](name-swift.struct/pdfdocumentdidendfind.md) — A notification that the document finished a find operation.
- [PDFDocumentDidEndPageFind](name-swift.struct/pdfdocumentdidendpagefind.md) — A notification that a find operation finishes working on a page in a document.
- [PDFDocumentDidEndPageWrite](name-swift.struct/pdfdocumentdidendpagewrite.md) — A notification that a write operation finishes working on a page in a document.
- [PDFDocumentDidEndWrite](name-swift.struct/pdfdocumentdidendwrite.md) — A notification that a write operation finishes working on a document.
- [PDFDocumentDidFindMatch](name-swift.struct/pdfdocumentdidfindmatch.md) — A notification that a string match is found in a document.
- [PDFDocumentDidUnlock](name-swift.struct/pdfdocumentdidunlock.md) — A notification that a document unlocked.
- [PDFThumbnailViewDocumentEdited](name-swift.struct/pdfthumbnailviewdocumentedited.md)
- [PDFViewAnnotationHit](name-swift.struct/pdfviewannotationhit.md) — A notification posted when the user clicks on an annotation.
- [PDFViewAnnotationWillHit](name-swift.struct/pdfviewannotationwillhit.md) — A notification posted before the user clicks an annotation.
- [PDFViewChangedHistory](name-swift.struct/pdfviewchangedhistory.md) — A notification posted when the page history changes.
- [PDFViewCopyPermission](name-swift.struct/pdfviewcopypermission.md) — A notification posted when the user attempts to copy to the pasteboard without the appropriate permissions.
- [PDFViewDisplayBoxChanged](name-swift.struct/pdfviewdisplayboxchanged.md) — A notification posted when the display box has changed.
- [PDFViewDisplayModeChanged](name-swift.struct/pdfviewdisplaymodechanged.md) — A notification posted when the display mode has changed.
- [PDFViewDocumentChanged](name-swift.struct/pdfviewdocumentchanged.md) — A notification posted when a new document is associated with the view.
- [PDFViewPageChanged](name-swift.struct/pdfviewpagechanged.md) — A notification posted when a new page becomes the current page.
- [PDFViewPrintPermission](name-swift.struct/pdfviewprintpermission.md) — A notification posted when the user attempts to print without the appropriate permissions.
- [PDFViewScaleChanged](name-swift.struct/pdfviewscalechanged.md) — A notification posted when the scale factor changes.
- [PDFViewSelectionChanged](name-swift.struct/pdfviewselectionchanged.md) — A notification posted when the current selection has changed.
- [PDFViewVisiblePagesChanged](name-swift.struct/pdfviewvisiblepageschanged.md) — A notification posted when the visible pages have changed.

### PreferencePanes

- [NSPreferencePaneCancelUnselect](name-swift.struct/nspreferencepanecancelunselect.md) — Notifies observers that the preference pane should not be deselected.
- [NSPreferencePaneDoUnselect](name-swift.struct/nspreferencepanedounselect.md) — Notifies observers that the preference pane may be deselected.
- [NSPreferencePaneSwitchToPane](name-swift.struct/nspreferencepaneswitchtopane.md) — Notifies observers that the user selected a new preference pane.
- [NSPreferencePaneUpdateHelpMenu](name-swift.struct/nspreferencepaneupdatehelpmenu.md) — Notifies observers that your help menu content changed.
- [NSPreferencePrefPaneIsAvailable](name-swift.struct/nspreferenceprefpaneisavailable.md) — Notifies observers that the system preferences app is available to display your preferences.

### Quartz

- [IKFilterBrowserFilterDoubleClick](name-swift.struct/ikfilterbrowserfilterdoubleclick.md) — Posted when the user double-clicks a filter in the filter browser.
- [IKFilterBrowserFilterSelected](name-swift.struct/ikfilterbrowserfilterselected.md) — Posted when the user clicks a filter name in the filter browser.
- [IKFilterBrowserWillPreviewFilter](name-swift.struct/ikfilterbrowserwillpreviewfilter.md) — Posted before showing a filter preview, allowing an application to set the parameters of a filter.
- [quartzFilterManagerDidAddFilter](name-swift.struct/quartzfiltermanagerdidaddfilter.md)
- [quartzFilterManagerDidModifyFilter](name-swift.struct/quartzfiltermanagerdidmodifyfilter.md)
- [quartzFilterManagerDidRemoveFilter](name-swift.struct/quartzfiltermanagerdidremovefilter.md)
- [quartzFilterManagerDidSelectFilter](name-swift.struct/quartzfiltermanagerdidselectfilter.md)
- [QCCompositionPickerPanelDidSelectComposition](name-swift.struct/qccompositionpickerpaneldidselectcomposition.md) — Posted when the user chooses a composition. _(deprecated)_
- [QCCompositionPickerViewDidSelectComposition](name-swift.struct/qccompositionpickerviewdidselectcomposition.md) — Posted when the user selects a composition in the picker view. _(deprecated)_
- [QCCompositionRepositoryDidUpdate](name-swift.struct/qccompositionrepositorydidupdate.md) — Posted whenever the list of compositions in the composition repository is updated. _(deprecated)_
- [QCViewDidStartRendering](name-swift.struct/qcviewdidstartrendering.md) — Posted when the view starts rendering. _(deprecated)_
- [QCViewDidStopRendering](name-swift.struct/qcviewdidstoprendering.md) — Posted when the view stops rendering. _(deprecated)_

### StoreKit

- [SKCloudServiceCapabilitiesDidChange](name-swift.struct/skcloudservicecapabilitiesdidchange.md) — A notification name for indicating a change in the capabilities associated with the Music library on the device. _(deprecated)_
- [SKStorefrontIdentifierDidChange](name-swift.struct/skstorefrontidentifierdidchange.md) — A notification name for indicating a change in the storefront identifier associated with the device. _(deprecated)_
- [SKStorefrontCountryCodeDidChange](name-swift.struct/skstorefrontcountrycodedidchange.md) — A notification name for indicating a change in the storefront country or region code associated with the device. _(deprecated)_

### TV Services

- [TVTopShelfItemsDidChange](name-swift.struct/tvtopshelfitemsdidchange.md) — A notification to post when your app’s Top Shelf content has changed. _(deprecated)_

### UIKit

- [announcementDidFinishNotification](../../uikit/uiaccessibility/announcementdidfinishnotification.md) — A notification that UIKit posts when the system finishes reading an announcement.
- [elementFocusedNotification](../../uikit/uiaccessibility/elementfocusednotification.md) — A notification that UIKit posts when an assistive app focuses on an accessibility element.
- [assistiveTouchStatusDidChangeNotification](../../uikit/uiaccessibility/assistivetouchstatusdidchangenotification.md) — A notification that indicates a change in the status of AssistiveTouch.
- [boldTextStatusDidChangeNotification](../../uikit/uiaccessibility/boldtextstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Bold Text setting changes.
- [closedCaptioningStatusDidChangeNotification](../../uikit/uiaccessibility/closedcaptioningstatusdidchangenotification.md) — A notification that UIKit posts when the setting for Closed Captions + SDH changes.
- [darkerSystemColorsStatusDidChangeNotification](../../uikit/uiaccessibility/darkersystemcolorsstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Increase Contrast setting changes.
- [grayscaleStatusDidChangeNotification](../../uikit/uiaccessibility/grayscalestatusdidchangenotification.md) — A notification that UIKit posts when the system’s Grayscale setting changes.
- [guidedAccessStatusDidChangeNotification](../../uikit/uiaccessibility/guidedaccessstatusdidchangenotification.md) — A notification that indicates when a Guided Access session starts or ends.
- [hearingDevicePairedEarDidChangeNotification](../../uikit/uiaccessibility/hearingdevicepairedeardidchangenotification.md) — A notification that UIKit posts when there’s a change to the currently paired hearing devices.
- [invertColorsStatusDidChangeNotification](../../uikit/uiaccessibility/invertcolorsstatusdidchangenotification.md) — A notification that UIKit posts when the settings for inverted colors change.
- [monoAudioStatusDidChangeNotification](../../uikit/uiaccessibility/monoaudiostatusdidchangenotification.md) — A notification that UIKit posts when system audio changes from stereo to mono.
- [reduceMotionStatusDidChangeNotification](../../uikit/uiaccessibility/reducemotionstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Reduce Motion setting changes.
- [reduceTransparencyStatusDidChangeNotification](../../uikit/uiaccessibility/reducetransparencystatusdidchangenotification.md) — A notification that UIKit posts when the system’s Reduce Transparency setting changes.
- [shakeToUndoDidChangeNotification](../../uikit/uiaccessibility/shaketoundodidchangenotification.md) — A notification that UIKit posts when the system’s Shake to Undo setting changes.
- [speakScreenStatusDidChangeNotification](../../uikit/uiaccessibility/speakscreenstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Speak Screen setting changes.
- [speakSelectionStatusDidChangeNotification](../../uikit/uiaccessibility/speakselectionstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Speak Selection setting changes.
- [switchControlStatusDidChangeNotification](../../uikit/uiaccessibility/switchcontrolstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Switch Control setting changes.
- [didBecomeActiveNotification](../../uikit/uiapplication/didbecomeactivenotification.md) — A notification that posts when the app becomes active.
- [didEnterBackgroundNotification](../../uikit/uiapplication/didenterbackgroundnotification.md) — A notification that posts when the app enters the background.
- [didFinishLaunchingNotification](../../uikit/uiapplication/didfinishlaunchingnotification.md) — A notification that posts immediately after the app finishes launching.
- [didReceiveMemoryWarningNotification](../../uikit/uiapplication/didreceivememorywarningnotification.md) — A notification that posts when the app receives a warning from the operating system about low memory availability.
- [significantTimeChangeNotification](../../uikit/uiapplication/significanttimechangenotification.md) — A notification that posts when there’s a significant change in time.
- [userDidTakeScreenshotNotification](../../uikit/uiapplication/userdidtakescreenshotnotification.md) — A notification that posts when a person takes a screenshot on the device.
- [willEnterForegroundNotification](../../uikit/uiapplication/willenterforegroundnotification.md) — A notification that posts shortly before an app leaves the background state on its way to becoming the active app.
- [willResignActiveNotification](../../uikit/uiapplication/willresignactivenotification.md) — A notification that posts when the app is no longer active and loses focus.
- [willTerminateNotification](../../uikit/uiapplication/willterminatenotification.md) — A notification that posts when the app is about to terminate.
- [didChangeNotification](../../uikit/uicontentsizecategory/didchangenotification.md) — A notification that posts when the user changes the preferred content size setting.
- [proximityStateDidChangeNotification](../../uikit/uidevice/proximitystatedidchangenotification.md) — A notification that posts when the state of the proximity sensor changes.
- [brightnessDidChangeNotification](../../uikit/uiscreen/brightnessdidchangenotification.md) — A notification that posts when a screen’s brightness changes.
- [didConnectNotification](../../uikit/uiscreen/didconnectnotification.md) — A notification the system posts when a new screen connects to the device. _(deprecated)_
- [didDisconnectNotification](../../uikit/uiscreen/diddisconnectnotification.md) — A notification the system posts when a screen disconnects from the device. _(deprecated)_
- [modeDidChangeNotification](../../uikit/uiscreen/modedidchangenotification.md) — A notification that posts when a screen’s mode changes.
- [selectionDidChangeNotification](../../uikit/uitableview/selectiondidchangenotification.md) — A notification that posts when the selected row in the posting table view changes.
- [textDidBeginEditingNotification](../../uikit/uitextfield/textdidbegineditingnotification.md) — A notification that alerts observers when an editing session begins in a text field.
- [textDidChangeNotification](../../uikit/uitextfield/textdidchangenotification.md) — A notification that alerts observers when the text in a text field changes.
- [textDidEndEditingNotification](../../uikit/uitextfield/textdidendeditingnotification.md) — A notification that alerts observers when the editing session ends for a text field.
- [currentInputModeDidChangeNotification](../../uikit/uitextinputmode/currentinputmodedidchangenotification.md) — A notification that posts when the current input mode changes.
- [textDidBeginEditingNotification](../../uikit/uitextview/textdidbegineditingnotification.md) — A notification that alerts observers when an editing session begins in a text view.
- [textDidChangeNotification](../../uikit/uitextview/textdidchangenotification.md) — A notification that alerts observers when the text in a text view changes.
- [textDidEndEditingNotification](../../uikit/uitextview/textdidendeditingnotification.md) — A notification that alerts observers when the editing session ends for a text view.
- [showDetailTargetDidChangeNotification](../../uikit/uiviewcontroller/showdetailtargetdidchangenotification.md) — Posted when a split view controller is expanded or collapsed.
- [didBecomeHiddenNotification](../../uikit/uiwindow/didbecomehiddennotification.md) — A notification that posts when a window becomes hidden.
- [didBecomeKeyNotification](../../uikit/uiwindow/didbecomekeynotification.md) — A notification that posts whenever a window becomes the key window.
- [didBecomeVisibleNotification](../../uikit/uiwindow/didbecomevisiblenotification.md) — A notification that posts when a window becomes visible.
- [didResignKeyNotification](../../uikit/uiwindow/didresignkeynotification.md) — A notification that posts whenever a window resigns its status as main window.
- [backgroundRefreshStatusDidChangeNotification](../../uikit/uiapplication/backgroundrefreshstatusdidchangenotification.md) — A notification that posts when the app’s status for downloading content in the background changes.
- [didChangeStatusBarFrameNotification](../../uikit/uiapplication/didchangestatusbarframenotification.md) — Posted when the frame of the status bar changes. _(deprecated)_
- [didChangeStatusBarOrientationNotification](../../uikit/uiapplication/didchangestatusbarorientationnotification.md) — Posted when the orientation of the app’s user interface changes. _(deprecated)_
- [willChangeStatusBarFrameNotification](../../uikit/uiapplication/willchangestatusbarframenotification.md) — Posted when the app is about to change the frame of the status bar. _(deprecated)_
- [willChangeStatusBarOrientationNotification](../../uikit/uiapplication/willchangestatusbarorientationnotification.md) — Posted when the app is about to change the orientation of its interface. _(deprecated)_
- [batteryLevelDidChangeNotification](../../uikit/uidevice/batteryleveldidchangenotification.md) — A notification that posts when the battery level changes.
- [batteryStateDidChangeNotification](../../uikit/uidevice/batterystatedidchangenotification.md) — A notification that posts when battery state changes.
- [orientationDidChangeNotification](../../uikit/uidevice/orientationdidchangenotification.md) — A notification that posts when the orientation of the device changes.
- [stateChangedNotification](../../uikit/uidocument/statechangednotification.md) — A notification the document object posts when there’s a change in the state of the document.
- [keyboardDidChangeFrameNotification](../../uikit/uiresponder/keyboarddidchangeframenotification.md) — A notification that posts immediately after a change in the keyboard’s frame.
- [keyboardDidHideNotification](../../uikit/uiresponder/keyboarddidhidenotification.md) — A notification that posts immediately after dismissing the keyboard.
- [keyboardDidShowNotification](../../uikit/uiresponder/keyboarddidshownotification.md) — A notification that posts immediately after displaying the keyboard.
- [keyboardWillChangeFrameNotification](../../uikit/uiresponder/keyboardwillchangeframenotification.md) — A notification that posts immediately prior to a change in the keyboard’s frame.
- [keyboardWillHideNotification](../../uikit/uiresponder/keyboardwillhidenotification.md) — A notification that posts immediately prior to dismissing the keyboard.
- [keyboardWillShowNotification](../../uikit/uiresponder/keyboardwillshownotification.md) — A notification that posts immediately prior to displaying the keyboard.
- [didHideMenuNotification](../../uikit/uimenucontroller/didhidemenunotification.md) — Posted by the menu controller just after it hides the menu. _(deprecated)_
- [didShowMenuNotification](../../uikit/uimenucontroller/didshowmenunotification.md) — Posted by the menu controller just after it shows the menu. _(deprecated)_
- [menuFrameDidChangeNotification](../../uikit/uimenucontroller/menuframedidchangenotification.md) — Posted when the frame of a visible menu changes. _(deprecated)_
- [willHideMenuNotification](../../uikit/uimenucontroller/willhidemenunotification.md) — Posted by the menu controller just before it hides the menu. _(deprecated)_
- [willShowMenuNotification](../../uikit/uimenucontroller/willshowmenunotification.md) — Posted by the menu controller just before it shows the menu. _(deprecated)_
- [changedNotification](../../uikit/uipasteboard/changednotification.md) — A notification that a pasteboard object posts when its contents change.
- [removedNotification](../../uikit/uipasteboard/removednotification.md) — A notification that a pasteboard object posts just before an app removes it.
- [protectedDataDidBecomeAvailableNotification](../../uikit/uiapplication/protecteddatadidbecomeavailablenotification.md) — A notification that posts when the protected files become available for your code to access.
- [protectedDataWillBecomeUnavailableNotification](../../uikit/uiapplication/protecteddatawillbecomeunavailablenotification.md) — A notification that posts shortly before protected files are locked down and become inaccessible.

### WatchKit

- [WKAccessibilityReduceMotionStatusDidChange](name-swift.struct/wkaccessibilityreducemotionstatusdidchange.md) — Tells the interface controller that the reduce motion status has changed.
- [WKAudioFilePlayerItemDidPlayToEndTime](name-swift.struct/wkaudiofileplayeritemdidplaytoendtime.md) — A notification that the item has played successfully to its end. _(deprecated)_
- [WKAudioFilePlayerItemFailedToPlayToEndTime](name-swift.struct/wkaudiofileplayeritemfailedtoplaytoendtime.md) — A notification that the item failed to play to its end. _(deprecated)_
- [WKAudioFilePlayerItemTimeJumped](name-swift.struct/wkaudiofileplayeritemtimejumped.md) — A notification that the item’s current time has changed discontinuously. _(deprecated)_

### WebKit

- [WebHistoryAllItemsRemoved](name-swift.struct/webhistoryallitemsremoved.md) — Posted when all history items have been removed from the web history. _(deprecated)_
- [WebHistoryItemChanged](name-swift.struct/webhistoryitemchanged.md) — Posted by a WebHistoryItem object when the value of the history item’s title, alternate title, URL strings, or last visited interval changes. _(deprecated)_
- [WebHistoryItemsAdded](name-swift.struct/webhistoryitemsadded.md) — Posted when history items have been added to a web history. _(deprecated)_
- [WebHistoryItemsRemoved](name-swift.struct/webhistoryitemsremoved.md) — Posted when items have been removed from the web history. _(deprecated)_
- [WebHistoryLoaded](name-swift.struct/webhistoryloaded.md) — Posted when web history items have been loaded from a URL. _(deprecated)_
- [WebHistorySaved](name-swift.struct/webhistorysaved.md) — Posted when web history items have been saved to a URL. _(deprecated)_
- [WebPreferencesChanged](name-swift.struct/webpreferenceschanged.md) — Posted when the web preference settings are changed. _(deprecated)_
- [WebViewDidBeginEditing](name-swift.struct/webviewdidbeginediting.md) — Posted when a web view begins any operation that changes its contents in response to user editing. _(deprecated)_
- [WebViewDidChange](name-swift.struct/webviewdidchange.md) — Posted when a web view performs any operation that changes its contents in response to user editing. _(deprecated)_
- [WebViewDidChangeSelection](name-swift.struct/webviewdidchangeselection.md) — Posted when a web view changes its typing selection. _(deprecated)_
- [WebViewDidChangeTypingStyle](name-swift.struct/webviewdidchangetypingstyle.md) — Posted when a web view changes its typing style. _(deprecated)_
- [WebViewDidEndEditing](name-swift.struct/webviewdidendediting.md) — Posted when a web view ends any operation that changes its contents in response to user editing. _(deprecated)_
- [WebViewProgressEstimateChanged](name-swift.struct/webviewprogressestimatechanged.md) — Posted by a WebView object when the estimated progress value of a load changes. _(deprecated)_
- [WebViewProgressFinished](name-swift.struct/webviewprogressfinished.md) — Posted by a WebView object when the load has finished. _(deprecated)_
- [WebViewProgressStarted](name-swift.struct/webviewprogressstarted.md) — Posted by a WebView object when a load begins, including a load that is initiated in a subframe. _(deprecated)_

### Accounts

- [ACAccountStoreDidChange](name-swift.struct/acaccountstoredidchange.md) — Posted when the accounts managed by this account store changed in the database. _(deprecated)_

### Initializers

- [init(_:)](<name-swift.struct/init(__).md>)
- [init(rawValue:)](<name-swift.struct/init(rawvalue_).md>)

### Type Properties

- [AVCaptureDeviceSubjectAreaDidChange](name-swift.struct/avcapturedevicesubjectareadidchange.md) _(deprecated)_
- [AVCaptureDeviceWasConnected](name-swift.struct/avcapturedevicewasconnected.md) _(deprecated)_
- [AVCaptureDeviceWasDisconnected](name-swift.struct/avcapturedevicewasdisconnected.md) _(deprecated)_
- [AVCaptureInputPortFormatDescriptionDidChange](name-swift.struct/avcaptureinputportformatdescriptiondidchange.md) _(deprecated)_
- [AVCaptureSessionDidStartRunning](name-swift.struct/avcapturesessiondidstartrunning.md) _(deprecated)_
- [AVCaptureSessionDidStopRunning](name-swift.struct/avcapturesessiondidstoprunning.md) _(deprecated)_
- [AVCaptureSessionInterruptionEnded](name-swift.struct/avcapturesessioninterruptionended.md) _(deprecated)_
- [AVCaptureSessionRuntimeError](name-swift.struct/avcapturesessionruntimeerror.md) _(deprecated)_
- [AVCaptureSessionWasInterrupted](name-swift.struct/avcapturesessionwasinterrupted.md) _(deprecated)_
- [AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChange](name-swift.struct/avplayerinterstitialeventmonitorassetlistresponsestatusdidchange.md) _(deprecated)_
- [AVPlayerInterstitialEventMonitorScheduleRequestCompleted](name-swift.struct/avplayerinterstitialeventmonitorschedulerequestcompleted.md)
- [AVPlayerItemDidPlayToEndTime](name-swift.struct/avplayeritemdidplaytoendtime.md) _(deprecated)_
- [AVPlayerItemFailedToPlayToEndTime](name-swift.struct/avplayeritemfailedtoplaytoendtime.md) _(deprecated)_
- [AVPlayerItemNewAccessLogEntry](name-swift.struct/avplayeritemnewaccesslogentry.md) _(deprecated)_
- [AVPlayerItemNewErrorLogEntry](name-swift.struct/avplayeritemnewerrorlogentry.md) _(deprecated)_
- [AVPlayerItemPlaybackStalled](name-swift.struct/avplayeritemplaybackstalled.md) _(deprecated)_
- [AVSampleBufferDisplayLayerReadyForDisplayDidChange](name-swift.struct/avsamplebufferdisplaylayerreadyfordisplaydidchange.md)
- [AXAnimatedImagesEnabledDidChange](name-swift.struct/axanimatedimagesenableddidchange.md)
- [AXPrefersHeadAnchorAlternativeDidChange](name-swift.struct/axprefersheadanchoralternativedidchange.md) _(deprecated)_
- [AXPrefersHorizontalTextLayoutDidChange](name-swift.struct/axprefershorizontaltextlayoutdidchange.md)
- [DRBurnProgressPanelDidFinish](name-swift.struct/drburnprogresspaneldidfinish.md)
- [DRBurnProgressPanelWillBegin](name-swift.struct/drburnprogresspanelwillbegin.md)
- [DRBurnStatusChanged](name-swift.struct/drburnstatuschanged.md)
- [DRDeviceAppeared](name-swift.struct/drdeviceappeared.md)
- [DRDeviceDisappeared](name-swift.struct/drdevicedisappeared.md)
- [DRDeviceStatusChanged](name-swift.struct/drdevicestatuschanged.md)
- [DREraseProgressPanelDidFinish](name-swift.struct/dreraseprogresspaneldidfinish.md)
- [DREraseProgressPanelWillBegin](name-swift.struct/dreraseprogresspanelwillbegin.md)
- [DREraseStatusChanged](name-swift.struct/drerasestatuschanged.md)
- [DRSetupPanelDeviceSelectionChanged](name-swift.struct/drsetuppaneldeviceselectionchanged.md)
- [GCSpatialAccessoryDidConnect](name-swift.struct/gcspatialaccessorydidconnect.md) _(beta)_
- [GCSpatialAccessoryDidDisconnect](name-swift.struct/gcspatialaccessorydiddisconnect.md) _(beta)_
- [GCStylusDidConnect](name-swift.struct/gcstylusdidconnect.md)
- [GCStylusDidDisconnect](name-swift.struct/gcstylusdiddisconnect.md)
- [HMCharacteristicPropertySupportsEvent](name-swift.struct/hmcharacteristicpropertysupportsevent.md)
- [MEVideoDecoderReadyForMoreMediaDataDidChange](name-swift.struct/mevideodecoderreadyformoremediadatadidchange.md)
- [NERelayConfigurationDidChange](name-swift.struct/nerelayconfigurationdidchange.md)
- [NEURLFilterConfigurationDidChange](name-swift.struct/neurlfilterconfigurationdidchange.md) — Name of the NSNotification that is posted when the URL filter configuration changes.
- [NEURLFilterStatusDidChange](name-swift.struct/neurlfilterstatusdidchange.md) — Name of the NSNotification that is posted when the URL filter status changes.
- [NSApplicationShouldBeginSuppressingHighDynamicRangeContent](name-swift.struct/nsapplicationshouldbeginsuppressinghighdynamicrangecontent.md)
- [NSApplicationShouldEndSuppressingHighDynamicRangeContent](name-swift.struct/nsapplicationshouldendsuppressinghighdynamicrangecontent.md)
- [NSProcessInfoPerformanceProfileDidChange](name-swift.struct/nsprocessinfoperformanceprofiledidchange.md)
- [NSSpellCheckerDidChangeAutomaticInlinePrediction](name-swift.struct/nsspellcheckerdidchangeautomaticinlineprediction.md)

## See Also

### Creating Notifications

- [- initWithCoder:](<init(coder_).md>) — Initializes a notification with the data from an unarchiver.
- [+ notificationWithName:object:](<init(name_object_).md>) — Returns a new notification object with a specified name and object.
- [- initWithName:object:userInfo:](<init(name_object_userinfo_).md>) — Initializes a notification with a specified name, object, and user information.
