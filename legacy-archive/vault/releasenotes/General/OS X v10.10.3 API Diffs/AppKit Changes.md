---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/frameworks/AppKit.html
archived_at: '2026-07-18T02:51:48.188303Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# AppKit Changes

## AppKit

NSAccessibility.hAdded [NSWorkspace.accessibilityDisplayShouldDifferentiateWithoutColor](https://developer.apple.com/documentation/appkit/nsworkspace/1524656-accessibilitydisplayshoulddiffer)Added [NSWorkspace.accessibilityDisplayShouldIncreaseContrast](https://developer.apple.com/documentation/appkit/nsworkspace/1526290-accessibilitydisplayshouldincrea)Added [NSWorkspace.accessibilityDisplayShouldReduceTransparency](https://developer.apple.com/documentation/appkit/nsworkspace/1533006-accessibilitydisplayshouldreduce)Added NSWorkspace(NSWorkspaceAccessibilityDisplay)Added [NSWorkspaceAccessibilityDisplayOptionsDidChangeNotification](https://developer.apple.com/documentation/appkit/nsworkspace/1534227-accessibilitydisplayoptionsdidch)NSApplication.hAdded [#def NSAppKitVersionNumber10_10](https://developer.apple.com/documentation/appkit/nsappkitversion/1428575-macos10_10)NSButton.hAdded [NSButton.maxAcceleratorLevel](https://developer.apple.com/documentation/appkit/nsbutton/1534413-maxacceleratorlevel)Added [NSButton.springLoaded](https://developer.apple.com/documentation/appkit/nsbutton/1532300-springloaded)NSButtonCell.hAdded [NSAcceleratorButton](https://developer.apple.com/documentation/appkit/nsacceleratorbutton)Added [NSMultiLevelAcceleratorButton](https://developer.apple.com/documentation/appkit/nsmultilevelacceleratorbutton)NSClipView.hAdded [NSClipView.automaticallyAdjustsContentInsets](https://developer.apple.com/documentation/appkit/nsclipview/1527540-automaticallyadjustscontentinset)Added [NSClipView.contentInsets](https://developer.apple.com/documentation/appkit/nsclipview/1524329-contentinsets)NSCollectionView.hModified [NSCollectionViewItem.imageView](https://developer.apple.com/documentation/appkit/nscollectionviewitem/1525366-imageview)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) NSImageView *imageView ``` |
| To | ``` @property(assign) IBOutlet NSImageView *imageView ``` |

Modified [NSCollectionViewItem.textField](https://developer.apple.com/documentation/appkit/nscollectionviewitem/1527126-textfield)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) NSTextField *textField ``` |
| To | ``` @property(assign) IBOutlet NSTextField *textField ``` |

NSColor.hAdded [+[NSColor quaternaryLabelColor]](https://developer.apple.com/documentation/appkit/nscolor/1534635-quaternarylabelcolor)Added [+[NSColor tertiaryLabelColor]](https://developer.apple.com/documentation/appkit/nscolor/1532376-tertiarylabelcolor)Modified [-[NSColor init]](https://developer.apple.com/documentation/appkit/nscolor/1533939-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSColor initWithCoder:]](https://developer.apple.com/documentation/appkit/nscolor/1527272-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSControl.hModified [-[NSControl initWithCoder:]](https://developer.apple.com/documentation/appkit/nscontrol/1428861-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSControl initWithFrame:]](https://developer.apple.com/documentation/appkit/nscontrol/1428900-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSController.hModified [-[NSController init]](https://developer.apple.com/documentation/appkit/nscontroller/1528092-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSController initWithCoder:]](https://developer.apple.com/documentation/appkit/nscontroller/1525048-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSDocument.hModified [-[NSDocument browseDocumentVersions:]](https://developer.apple.com/documentation/appkit/nsdocument/1515193-browsedocumentversions)

|  | Declaration |
| --- | --- |
| From | ``` - (void)browseDocumentVersions:(id)sender ``` |
| To | ``` - (IBAction)browseDocumentVersions:(id)sender ``` |

Modified [-[NSDocument duplicateDocument:]](https://developer.apple.com/documentation/appkit/nsdocument/1515226-duplicatedocument)

|  | Declaration |
| --- | --- |
| From | ``` - (void)duplicateDocument:(id)sender ``` |
| To | ``` - (IBAction)duplicateDocument:(id)sender ``` |

Modified [-[NSDocument init]](https://developer.apple.com/documentation/appkit/nsdocument/1515181-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDocument lockDocument:]](https://developer.apple.com/documentation/appkit/nsdocument/1515218-lock)

|  | Declaration |
| --- | --- |
| From | ``` - (void)lockDocument:(id)sender ``` |
| To | ``` - (IBAction)lockDocument:(id)sender ``` |

Modified [-[NSDocument moveDocument:]](https://developer.apple.com/documentation/appkit/nsdocument/1515118-move)

|  | Declaration |
| --- | --- |
| From | ``` - (void)moveDocument:(id)sender ``` |
| To | ``` - (IBAction)moveDocument:(id)sender ``` |

Modified [-[NSDocument moveDocumentToUbiquityContainer:]](https://developer.apple.com/documentation/appkit/nsdocument/1515210-movedocumenttoubiquitycontainer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)moveDocumentToUbiquityContainer:(id)sender ``` |
| To | ``` - (IBAction)moveDocumentToUbiquityContainer:(id)sender ``` |

Modified [-[NSDocument printDocument:]](https://developer.apple.com/documentation/appkit/nsdocument/1515154-printdocument)

|  | Declaration |
| --- | --- |
| From | ``` - (void)printDocument:(id)sender ``` |
| To | ``` - (IBAction)printDocument:(id)sender ``` |

Modified [-[NSDocument renameDocument:]](https://developer.apple.com/documentation/appkit/nsdocument/1515231-renamedocument)

|  | Declaration |
| --- | --- |
| From | ``` - (void)renameDocument:(id)sender ``` |
| To | ``` - (IBAction)renameDocument:(id)sender ``` |

Modified [-[NSDocument revertDocumentToSaved:]](https://developer.apple.com/documentation/appkit/nsdocument/1515059-reverttosaved)

|  | Declaration |
| --- | --- |
| From | ``` - (void)revertDocumentToSaved:(id)sender ``` |
| To | ``` - (IBAction)revertDocumentToSaved:(id)sender ``` |

Modified [-[NSDocument runPageLayout:]](https://developer.apple.com/documentation/appkit/nsdocument/1515140-runpagelayout)

|  | Declaration |
| --- | --- |
| From | ``` - (void)runPageLayout:(id)sender ``` |
| To | ``` - (IBAction)runPageLayout:(id)sender ``` |

Modified [-[NSDocument saveDocument:]](https://developer.apple.com/documentation/appkit/nsdocument/1515147-savedocument)

|  | Declaration |
| --- | --- |
| From | ``` - (void)saveDocument:(id)sender ``` |
| To | ``` - (IBAction)saveDocument:(id)sender ``` |

Modified [-[NSDocument saveDocumentAs:]](https://developer.apple.com/documentation/appkit/nsdocument/1515171-savedocumentas)

|  | Declaration |
| --- | --- |
| From | ``` - (void)saveDocumentAs:(id)sender ``` |
| To | ``` - (IBAction)saveDocumentAs:(id)sender ``` |

Modified [-[NSDocument saveDocumentTo:]](https://developer.apple.com/documentation/appkit/nsdocument/1515208-savedocumentto)

|  | Declaration |
| --- | --- |
| From | ``` - (void)saveDocumentTo:(id)sender ``` |
| To | ``` - (IBAction)saveDocumentTo:(id)sender ``` |

Modified [-[NSDocument saveDocumentToPDF:]](https://developer.apple.com/documentation/appkit/nsdocument/1515176-savedocumenttopdf)

|  | Declaration |
| --- | --- |
| From | ``` - (void)saveDocumentToPDF:(id)sender ``` |
| To | ``` - (IBAction)saveDocumentToPDF:(id)sender ``` |

Modified [-[NSDocument unlockDocument:]](https://developer.apple.com/documentation/appkit/nsdocument/1515068-unlock)

|  | Declaration |
| --- | --- |
| From | ``` - (void)unlockDocument:(id)sender ``` |
| To | ``` - (IBAction)unlockDocument:(id)sender ``` |

NSDocumentController.hModified [-[NSDocumentController clearRecentDocuments:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514933-clearrecentdocuments)

|  | Declaration |
| --- | --- |
| From | ``` - (void)clearRecentDocuments:(id)sender ``` |
| To | ``` - (IBAction)clearRecentDocuments:(id)sender ``` |

Modified [-[NSDocumentController init]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1515007-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDocumentController initWithCoder:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514955-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDocumentController newDocument:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514997-newdocument)

|  | Declaration |
| --- | --- |
| From | ``` - (void)newDocument:(id)sender ``` |
| To | ``` - (IBAction)newDocument:(id)sender ``` |

Modified [-[NSDocumentController openDocument:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1515005-opendocument)

|  | Declaration |
| --- | --- |
| From | ``` - (void)openDocument:(id)sender ``` |
| To | ``` - (IBAction)openDocument:(id)sender ``` |

Modified [-[NSDocumentController saveAllDocuments:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514959-savealldocuments)

|  | Declaration |
| --- | --- |
| From | ``` - (void)saveAllDocuments:(id)sender ``` |
| To | ``` - (IBAction)saveAllDocuments:(id)sender ``` |

NSEvent.hAdded [NSEvent.associatedEventsMask](https://developer.apple.com/documentation/appkit/nsevent/1529610-associatedeventsmask)Added [NSEvent.stage](https://developer.apple.com/documentation/appkit/nsevent/1527242-stage)Added [NSEvent.stageTransition](https://developer.apple.com/documentation/appkit/nsevent/1526739-stagetransition)Added [NSEventMaskPressure](https://developer.apple.com/documentation/appkit/nseventmask/nseventmaskpressure)Added [NSEventTypePressure](https://developer.apple.com/documentation/appkit/nseventtype/nseventtypepressure)NSFont.hModified [NSFont](https://developer.apple.com/documentation/appkit/nsfont)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSForm.hModified [-[NSForm addEntry:]](https://developer.apple.com/documentation/appkit/nsform/1534075-addentry)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSForm cellAtIndex:]](https://developer.apple.com/documentation/appkit/nsform/1532662-cellatindex)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSForm drawCellAtIndex:]](https://developer.apple.com/documentation/appkit/nsform/1526339-drawcell)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSForm indexOfCellWithTag:]](https://developer.apple.com/documentation/appkit/nsform/1524629-indexofcell)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSForm indexOfSelectedItem]](https://developer.apple.com/documentation/appkit/nsform/1527869-indexofselecteditem)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSForm insertEntry:atIndex:]](https://developer.apple.com/documentation/appkit/nsform/1531754-insertentry)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSForm preferredTextFieldWidth]](https://developer.apple.com/documentation/appkit/nsform/1530873-preferredtextfieldwidth)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSForm removeEntryAtIndex:]](https://developer.apple.com/documentation/appkit/nsform/1526791-removeentry)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSForm selectTextAtIndex:]](https://developer.apple.com/documentation/appkit/nsform/1535000-selecttext)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSForm setBezeled:]](https://developer.apple.com/documentation/appkit/nsform/1533560-setbezeled)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSForm setBordered:]](https://developer.apple.com/documentation/appkit/nsform/1528565-setbordered)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSForm setEntryWidth:]](https://developer.apple.com/documentation/appkit/nsform/1529751-setentrywidth)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSForm setFrameSize:]](https://developer.apple.com/documentation/appkit/nsform/1533815-setframesize)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSForm setInterlineSpacing:]](https://developer.apple.com/documentation/appkit/nsform/1532029-setinterlinespacing)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSForm setPreferredTextFieldWidth:]](https://developer.apple.com/documentation/appkit/nsform/1526047-setpreferredtextfieldwidth)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSForm setTextAlignment:]](https://developer.apple.com/documentation/appkit/nsform/1527095-settextalignment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSForm setTextBaseWritingDirection:]](https://developer.apple.com/documentation/appkit/nsform/1524441-settextbasewritingdirection)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSForm setTextFont:]](https://developer.apple.com/documentation/appkit/nsform/1533476-settextfont)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSForm setTitleAlignment:]](https://developer.apple.com/documentation/appkit/nsform/1535551-settitlealignment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSForm setTitleBaseWritingDirection:]](https://developer.apple.com/documentation/appkit/nsform/1527429-settitlebasewritingdirection)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSForm setTitleFont:]](https://developer.apple.com/documentation/appkit/nsform/1535413-settitlefont)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

NSGestureRecognizer.hRemoved -[NSGestureRecognizerDelegate gestureRecognizer:shouldReceiveEvent:]Added [-[NSGestureRecognizer pressureChangeWithEvent:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1527009-pressurechangewithevent)Modified [-[NSGestureRecognizer initWithCoder:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1534865-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSGestureRecognizer initWithTarget:action:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1535012-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSImageRep.hModified [-[NSImageRep init]](https://developer.apple.com/documentation/appkit/nsimagerep/1530271-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSImageRep initWithCoder:]](https://developer.apple.com/documentation/appkit/nsimagerep/1535319-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSLayoutManager.hModified [-[NSLayoutManager init]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402975-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSMediaLibraryBrowserController.hModified [-[NSMediaLibraryBrowserController togglePanel:]](https://developer.apple.com/documentation/appkit/nsmedialibrarybrowsercontroller/1423479-togglepanel)

|  | Declaration |
| --- | --- |
| From | ``` - (void)togglePanel:(id)sender ``` |
| To | ``` - (IBAction)togglePanel:(id)sender ``` |

NSNibDeclarations.hRemoved #def IBInspectableRemoved #def IB_DESIGNABLENSObjectController.hModified [-[NSObjectController initWithCoder:]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1532995-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSObjectController initWithContent:]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1529422-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSOpenPanel.hAdded [NSOpenPanel.canDownloadUbiquitousContents](https://developer.apple.com/documentation/appkit/nsopenpanel/1533418-candownloadubiquitouscontents)Added [NSOpenPanel.canResolveUbiquitousConflicts](https://developer.apple.com/documentation/appkit/nsopenpanel/1533261-canresolveubiquitousconflicts)NSPageController.hModified [NSPageController.delegate](https://developer.apple.com/documentation/appkit/nspagecontroller/1435019-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<NSPageControllerDelegate> delegate ``` |
| To | ``` @property(assign) IBOutlet id<NSPageControllerDelegate> delegate ``` |

Modified [-[NSPageController navigateBack:]](https://developer.apple.com/documentation/appkit/nspagecontroller/1435017-navigateback)

|  | Declaration |
| --- | --- |
| From | ``` - (void)navigateBack:(id)sender ``` |
| To | ``` - (IBAction)navigateBack:(id)sender ``` |

Modified [-[NSPageController navigateForward:]](https://developer.apple.com/documentation/appkit/nspagecontroller/1435004-navigateforward)

|  | Declaration |
| --- | --- |
| From | ``` - (void)navigateForward:(id)sender ``` |
| To | ``` - (IBAction)navigateForward:(id)sender ``` |

Modified [-[NSPageController takeSelectedIndexFrom:]](https://developer.apple.com/documentation/appkit/nspagecontroller/1435011-takeselectedindexfrom)

|  | Declaration |
| --- | --- |
| From | ``` - (void)takeSelectedIndexFrom:(id)sender ``` |
| To | ``` - (IBAction)takeSelectedIndexFrom:(id)sender ``` |

NSPopover.hModified [NSPopover.contentViewController](https://developer.apple.com/documentation/appkit/nspopover/1526794-contentviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) NSViewController *contentViewController ``` |
| To | ``` @property(retain) IBOutlet NSViewController *contentViewController ``` |

Modified [NSPopover.delegate](https://developer.apple.com/documentation/appkit/nspopover/1526708-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<NSPopoverDelegate> delegate ``` |
| To | ``` @property(assign) IBOutlet id<NSPopoverDelegate> delegate ``` |

Modified [-[NSPopover init]](https://developer.apple.com/documentation/appkit/nspopover/1526851-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPopover initWithCoder:]](https://developer.apple.com/documentation/appkit/nspopover/1524631-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPopover performClose:]](https://developer.apple.com/documentation/appkit/nspopover/1534290-performclose)

|  | Declaration |
| --- | --- |
| From | ``` - (void)performClose:(id)sender ``` |
| To | ``` - (IBAction)performClose:(id)sender ``` |

NSPressGestureRecognizer.hModified [NSPressGestureRecognizer](https://developer.apple.com/documentation/appkit/nspressgesturerecognizer)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSCoding |

NSResponder.hAdded [-[NSResponder pressureChangeWithEvent:]](https://developer.apple.com/documentation/appkit/nsresponder/1534071-pressurechangewithevent)Modified [-[NSResponder init]](https://developer.apple.com/documentation/appkit/nsresponder/1525437-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSResponder initWithCoder:]](https://developer.apple.com/documentation/appkit/nsresponder/1535389-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSSavePanel.hModified [-[NSSavePanel cancel:]](https://developer.apple.com/documentation/appkit/nssavepanel/1534357-cancel)

|  | Declaration |
| --- | --- |
| From | ``` - (void)cancel:(id)sender ``` |
| To | ``` - (IBAction)cancel:(id)sender ``` |

Modified [-[NSSavePanel ok:]](https://developer.apple.com/documentation/appkit/nssavepanel/1535364-ok)

|  | Declaration |
| --- | --- |
| From | ``` - (void)ok:(id)sender ``` |
| To | ``` - (IBAction)ok:(id)sender ``` |

Modified [-[NSSavePanel selectText:]](https://developer.apple.com/documentation/appkit/nssavepanel/1539012-selecttext)

|  | Declaration |
| --- | --- |
| From | ``` - (void)selectText:(id)sender ``` |
| To | ``` - (IBAction)selectText:(id)sender ``` |

NSScrollView.hAdded [NSScrollView.automaticallyAdjustsContentInsets](https://developer.apple.com/documentation/appkit/nsscrollview/1403502-automaticallyadjustscontentinset)Added [NSScrollView.contentInsets](https://developer.apple.com/documentation/appkit/nsscrollview/1403461-contentinsets)Added [NSScrollView.scrollerInsets](https://developer.apple.com/documentation/appkit/nsscrollview/1403529-scrollerinsets)Modified [-[NSScrollView initWithCoder:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403527-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSScrollView initWithFrame:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403450-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSSegmentedControl.hAdded [-[NSSegmentedControl doubleValueForSelectedSegment]](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/1529727-doublevalueforselectedsegment)Added [NSSegmentedControl.springLoaded](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/1534122-isspringloaded)Added [NSSegmentedControl.trackingMode](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/1526285-trackingmode)Added [NSSegmentSwitchTrackingMomentaryAccelerator](https://developer.apple.com/documentation/appkit/nssegmentswitchtracking/nssegmentswitchtrackingmomentaryaccelerator)Modified [NSSegmentSwitchTracking](https://developer.apple.com/documentation/appkit/nssegmentswitchtracking)

|  | Header |
| --- | --- |
| From | AppKit/NSSegmentedCell.h |
| To | AppKit/NSSegmentedControl.h |

Modified [NSSegmentSwitchTrackingMomentary](https://developer.apple.com/documentation/appkit/nssegmentswitchtracking/nssegmentswitchtrackingmomentary)

|  | Header |
| --- | --- |
| From | AppKit/NSSegmentedCell.h |
| To | AppKit/NSSegmentedControl.h |

Modified [NSSegmentSwitchTrackingSelectAny](https://developer.apple.com/documentation/appkit/nssegmentswitchtracking/nssegmentswitchtrackingselectany)

|  | Header |
| --- | --- |
| From | AppKit/NSSegmentedCell.h |
| To | AppKit/NSSegmentedControl.h |

Modified [NSSegmentSwitchTrackingSelectOne](https://developer.apple.com/documentation/appkit/nssegmentswitchtracking/nssegmentswitchtrackingselectone)

|  | Header |
| --- | --- |
| From | AppKit/NSSegmentedCell.h |
| To | AppKit/NSSegmentedControl.h |

NSSplitViewController.hModified [-[NSSplitViewController splitView:additionalEffectiveRectOfDividerAtIndex:]](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/1388922-splitview)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSplitViewController splitView:canCollapseSubview:]](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/1388861-splitview)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSplitViewController splitView:effectiveRect:forDrawnRect:ofDividerAtIndex:]](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/1388897-splitview)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSplitViewController splitView:shouldCollapseSubview:forDoubleClickOnDividerAtIndex:]](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/1388909-splitview)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSplitViewController splitView:shouldHideDividerAtIndex:]](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/1388882-splitview)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSplitViewController viewDidLoad]](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/1388874-viewdidload)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

NSStoryboardSegue.hModified [-[NSStoryboardSegue initWithIdentifier:source:destination:]](https://developer.apple.com/documentation/appkit/nsstoryboardsegue/1409572-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSTabViewController.hRemoved NSTabViewController.segmentedControlModified [-[NSTabViewController tabView:didSelectTabViewItem:]](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428243-tabview)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTabViewController tabView:shouldSelectTabViewItem:]](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428237-tabview)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTabViewController tabView:willSelectTabViewItem:]](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428231-tabview)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTabViewController toolbar:itemForItemIdentifier:willBeInsertedIntoToolbar:]](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428218-toolbar)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTabViewController toolbarAllowedItemIdentifiers:]](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428229-toolbaralloweditemidentifiers)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTabViewController toolbarDefaultItemIdentifiers:]](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428251-toolbardefaultitemidentifiers)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTabViewController toolbarSelectableItemIdentifiers:]](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428261-toolbarselectableitemidentifiers)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTabViewController viewDidLoad]](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428253-viewdidload)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

NSTableCellView.hModified [NSTableCellView.imageView](https://developer.apple.com/documentation/appkit/nstablecellview/1483213-imageview)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) NSImageView *imageView ``` |
| To | ``` @property(assign) IBOutlet NSImageView *imageView ``` |

Modified [NSTableCellView.textField](https://developer.apple.com/documentation/appkit/nstablecellview/1483202-textfield)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) NSTextField *textField ``` |
| To | ``` @property(assign) IBOutlet NSTextField *textField ``` |

NSTableView.hModified [-[NSTableView initWithCoder:]](https://developer.apple.com/documentation/appkit/nstableview/1528481-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableView initWithFrame:]](https://developer.apple.com/documentation/appkit/nstableview/1525511-initwithframe)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSText.hModified [-[NSText initWithCoder:]](https://developer.apple.com/documentation/appkit/nstext/1535093-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSText initWithFrame:]](https://developer.apple.com/documentation/appkit/nstext/1525191-initwithframe)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSTextFinder.hModified [NSTextFinder.client](https://developer.apple.com/documentation/appkit/nstextfinder/1533813-client)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<NSTextFinderClient> client ``` |
| To | ``` @property(assign) IBOutlet id<NSTextFinderClient> client ``` |

Modified [NSTextFinder.findBarContainer](https://developer.apple.com/documentation/appkit/nstextfinder/1526748-findbarcontainer)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<NSTextFinderBarContainer> findBarContainer ``` |
| To | ``` @property(assign) IBOutlet id<NSTextFinderBarContainer> findBarContainer ``` |

NSTextView.hModified [-[NSTextView initWithCoder:]](https://developer.apple.com/documentation/appkit/nstextview/1449489-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextView initWithFrame:textContainer:]](https://developer.apple.com/documentation/appkit/nstextview/1449347-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextView orderFrontSharingServicePicker:]](https://developer.apple.com/documentation/appkit/nstextview/1449150-orderfrontsharingservicepicker)

|  | Declaration |
| --- | --- |
| From | ``` - (void)orderFrontSharingServicePicker:(id)sender ``` |
| To | ``` - (IBAction)orderFrontSharingServicePicker:(id)sender ``` |

Modified [-[NSTextView toggleQuickLookPreviewPanel:]](https://developer.apple.com/documentation/appkit/nstextview/1449415-togglequicklookpreviewpanel)

|  | Declaration |
| --- | --- |
| From | ``` - (void)toggleQuickLookPreviewPanel:(id)sender ``` |
| To | ``` - (IBAction)toggleQuickLookPreviewPanel:(id)sender ``` |

NSTitlebarAccessoryViewController.hModified [-[NSTitlebarAccessoryViewController viewDidAppear]](https://developer.apple.com/documentation/appkit/nstitlebaraccessoryviewcontroller/1397780-viewdidappear)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTitlebarAccessoryViewController viewDidDisappear]](https://developer.apple.com/documentation/appkit/nstitlebaraccessoryviewcontroller/1397776-viewdiddisappear)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTitlebarAccessoryViewController viewWillAppear]](https://developer.apple.com/documentation/appkit/nstitlebaraccessoryviewcontroller/1397774-viewwillappear)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

NSTokenFieldCell.hRemoved [NSDefaultTokenStyle](https://developer.apple.com/documentation/appkit/nstokenstyle/nsdefaulttokenstyle)Removed [NSPlainTextTokenStyle](https://developer.apple.com/documentation/appkit/nstokenstyle/nsplaintexttokenstyle)Removed [NSRoundedTokenStyle](https://developer.apple.com/documentation/appkit/nstokenstyle/nsroundedtokenstyle)Added [NSDefaultTokenStyle](https://developer.apple.com/documentation/appkit/nsdefaulttokenstyle)Added [NSPlainTextTokenStyle](https://developer.apple.com/documentation/appkit/nsplaintexttokenstyle)Added [NSRoundedTokenStyle](https://developer.apple.com/documentation/appkit/nsroundedtokenstyle)Added [NSTokenStyleDefault](https://developer.apple.com/documentation/appkit/nstokenfield/tokenstyle/default)Added [NSTokenStyleNone](https://developer.apple.com/documentation/appkit/nstokenfield/tokenstyle/none)Added [NSTokenStylePlainSquared](https://developer.apple.com/documentation/appkit/nstokenstyle/nstokenstyleplainsquared)Added [NSTokenStyleRounded](https://developer.apple.com/documentation/appkit/nstokenfield/tokenstyle/rounded)Added [NSTokenStyleSquared](https://developer.apple.com/documentation/appkit/nstokenstyle/nstokenstylesquared)NSToolbar.hModified [-[NSToolbar initWithIdentifier:]](https://developer.apple.com/documentation/appkit/nstoolbar/1516975-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSToolbarItem.hModified [-[NSToolbarItem initWithItemIdentifier:]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1534084-initwithitemidentifier)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSTreeNode.hModified [NSTreeNode.parentNode](https://developer.apple.com/documentation/appkit/nstreenode/1530728-parentnode)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSTreeNode *parentNode ``` |
| To | ``` @property(readonly, assign) NSTreeNode *parentNode ``` |

NSUserDefaultsController.hModified [-[NSUserDefaultsController initWithCoder:]](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/1388172-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSUserDefaultsController initWithDefaults:initialValues:]](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/1388184-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSView.hModified [-[NSView initWithCoder:]](https://developer.apple.com/documentation/appkit/nsview/1483715-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSView initWithFrame:]](https://developer.apple.com/documentation/appkit/nsview/1483458-initwithframe)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSViewController.hModified [-[NSViewController dismissController:]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434447-dismisscontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)dismissController:(id)sender ``` |
| To | ``` - (IBAction)dismissController:(id)sender ``` |

Modified [-[NSViewController initWithCoder:]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434441-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSViewController initWithNibName:bundle:]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434481-initwithnibname)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [NSViewController.sourceItemView](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434479-sourceitemview)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSView *sourceItemView ``` |
| To | ``` @property(strong) IBOutlet NSView *sourceItemView ``` |

NSVisualEffectView.hModified [-[NSVisualEffectView viewDidMoveToWindow]](https://developer.apple.com/documentation/appkit/nsvisualeffectview/1534300-viewdidmovetowindow)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSVisualEffectView viewWillMoveToWindow:]](https://developer.apple.com/documentation/appkit/nsvisualeffectview/1534276-viewwillmovetowindow)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

NSWindow.hRemoved NSWindowTitleHiddenWhenActiveNSWindowController.hModified [-[NSWindowController dismissController:]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1531963-dismisscontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)dismissController:(id)sender ``` |
| To | ``` - (IBAction)dismissController:(id)sender ``` |

Modified [-[NSWindowController initWithCoder:]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1529004-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowController initWithWindow:]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1533442-initwithwindow)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowController showWindow:]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1534037-showwindow)

|  | Declaration |
| --- | --- |
| From | ``` - (void)showWindow:(id)sender ``` |
| To | ``` - (IBAction)showWindow:(id)sender ``` |

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
