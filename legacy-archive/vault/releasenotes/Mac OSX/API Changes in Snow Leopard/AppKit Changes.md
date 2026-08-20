---
title: API Changes in Snow Leopard
apple_id: TP40007673
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/SnowLeopard_API_ReleaseNote/AppKit.html
archived_at: '2026-07-18T02:58:41.197996Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [API Changes in Snow Leopard](API%20Changes%20in%20Snow%20Leopard.md)


[ADC Home](https://developer.apple.com/) >
[Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) >
Release Notes >
OS X >
[API Changes in Snow Leopard Developer Preview](API%20Changes%20in%20Snow%20Leopard.md) >

# AppKit Changes

## AppKit

NSAccessibility.hAdded [NSAccessibilityCriticalValueAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1535723-criticalvalue)Added [NSAccessibilityLevelIndicatorRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1527049-levelindicator)Added [NSAccessibilityPlaceholderValueAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1526634-placeholdervalue)Added [NSAccessibilityRatingIndicatorSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilityratingindicatorsubrole)Added [NSAccessibilityRelevanceIndicatorRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrelevanceindicatorrole)Added [NSAccessibilitySortButtonSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysortbuttonsubrole)Added [NSAccessibilityUnknownOrientationValue](https://developer.apple.com/documentation/appkit/nsaccessibilityunknownorientationvalue)Added [NSAccessibilityWarningValueAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitywarningvalueattribute)Modified [NSAccessibilitySortButtonRole](https://developer.apple.com/documentation/appkit/nsaccessibilitysortbuttonrole)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

NSActionCell.hRemoved [-[NSActionCell controlView]](https://developer.apple.com/documentation/appkit/nsactioncell/1807051-controlview)Removed -[NSActionCell doubleValue]Removed [-[NSActionCell floatValue]](https://developer.apple.com/documentation/appkit/nsactioncell/1807042-floatvalue)Removed [-[NSActionCell intValue]](https://developer.apple.com/documentation/appkit/nsactioncell/1807044-intvalue)Removed [-[NSActionCell integerValue]](https://developer.apple.com/documentation/appkit/nsactioncell/1807046-integervalue)Removed -[NSActionCell setAlignment:]Removed -[NSActionCell setBezeled:]Removed -[NSActionCell setBordered:]Removed [-[NSActionCell setControlView:]](https://developer.apple.com/documentation/appkit/nsactioncell/1807052-setcontrolview)Removed -[NSActionCell setEnabled:]Removed [-[NSActionCell setFloatingPointFormat:left:right:]](https://developer.apple.com/documentation/appkit/nsactioncell/1807039-setfloatingpointformat)Removed -[NSActionCell setFont:]Removed -[NSActionCell setImage:]Removed [-[NSActionCell setObjectValue:]](https://developer.apple.com/documentation/appkit/nsactioncell/1807049-setobjectvalue)Removed [-[NSActionCell stringValue]](https://developer.apple.com/documentation/appkit/nsactioncell/1807047-stringvalue)NSApplication.hAdded [-[NSApplication activationPolicy]](https://developer.apple.com/documentation/appkit/nsapplication/1428703-activationpolicy)Added [-[NSApplication isFullKeyboardAccessEnabled]](https://developer.apple.com/documentation/appkit/nsapplication/1428469-fullkeyboardaccessenabled)Added [-[NSApplication setActivationPolicy:]](https://developer.apple.com/documentation/appkit/nsapplication/1428621-setactivationpolicy)Added [-[NSApplication userInterfaceLayoutDirection]](https://developer.apple.com/documentation/appkit/nsapplication/1428556-userinterfacelayoutdirection)Added [#def NSAppKitVersionNumber10_4_1](https://developer.apple.com/documentation/appkit/nsappkitversion/1428617-macos10_4_1)Added [#def NSAppKitVersionNumber10_4_3](https://developer.apple.com/documentation/appkit/nsappkitversion/1428583-macos10_4_3)Added [#def NSAppKitVersionNumber10_4_4](https://developer.apple.com/documentation/appkit/nsappkitversionnumber10_4_4)Added [#def NSAppKitVersionNumber10_4_7](https://developer.apple.com/documentation/appkit/nsappkitversionnumber10_4_7)Added [#def NSAppKitVersionNumber10_5](https://developer.apple.com/documentation/appkit/nsappkitversion/1428527-macos10_5)Added [#def NSAppKitVersionNumber10_5_2](https://developer.apple.com/documentation/appkit/nsappkitversionnumber10_5_2)Added [#def NSAppKitVersionNumber10_5_3](https://developer.apple.com/documentation/appkit/nsappkitversionnumber10_5_3)Added NSApplication(NSApplicationLayoutDirection)Added NSApplication(NSFullKeyboardAccess)Added [NSUserInterfaceLayoutDirection](https://developer.apple.com/documentation/appkit/nsuserinterfacelayoutdirection)Added [NSUserInterfaceLayoutDirectionLeftToRight](https://developer.apple.com/documentation/appkit/nsuserinterfacelayoutdirection/lefttoright)Added [NSUserInterfaceLayoutDirectionRightToLeft](https://developer.apple.com/documentation/appkit/nsuserinterfacelayoutdirection/nsuserinterfacelayoutdirectionrighttoleft)NSAttributedString.hAdded [NSCategoryDocumentAttribute](https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/1525890-category)Added [NSFileTypeDocumentAttribute](https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/1529913-filetype)Added [NSFileTypeDocumentOption](https://developer.apple.com/documentation/appkit/nsfiletypedocumentoption)Added [NSManagerDocumentAttribute](https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/1533567-manager)NSBezierPath.hAdded NSBezierPath(NSBezierPathDeprecated)Modified [-[NSBezierPath setCachesBezierPath:]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520702-setcachesbezierpath)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.0 |

Modified [-[NSBezierPath cachesBezierPath]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520706-cachesbezierpath)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.0 |

NSBrowser.hAdded [-[NSBrowser autohidesScroller]](https://developer.apple.com/documentation/appkit/nsbrowser/1407696-autohidesscroller)Added [-[NSBrowser clickedColumn]](https://developer.apple.com/documentation/appkit/nsbrowser/1407590-clickedcolumn)Added [-[NSBrowser clickedRow]](https://developer.apple.com/documentation/appkit/nsbrowser/1407671-clickedrow)Added [-[NSBrowser defaultColumnWidth]](https://developer.apple.com/documentation/appkit/nsbrowser/1407615-defaultcolumnwidth)Added [-[NSBrowser editItemAtIndexPath:withEvent:select:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407558-edititematindexpath)Added [-[NSBrowser indexPathForColumn:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407739-indexpath)Added -[NSBrowser indexPathForItem:]Added [-[NSBrowser isLeafItem:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407713-isleafitem)Added [-[NSBrowser itemAtIndexPath:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407673-item)Added -[NSBrowser parentForItem:]Added [-[NSBrowser parentForItemsInColumn:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407570-parentforitemsincolumn)Added -[NSBrowser reloadItem:reloadChildren:]Added [-[NSBrowser scrollRowToVisible:inColumn:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407719-scrollrowtovisible)Added [-[NSBrowser selectionIndexPath]](https://developer.apple.com/documentation/appkit/nsbrowser/1407507-selectionindexpath)Added [-[NSBrowser selectionIndexPaths]](https://developer.apple.com/documentation/appkit/nsbrowser/1407536-selectionindexpaths)Added [-[NSBrowser setAutohidesScroller:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407696-autohidesscroller)Added [-[NSBrowser setDefaultColumnWidth:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407651-setdefaultcolumnwidth)Added [-[NSBrowser setSelectionIndexPath:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407507-selectionindexpath)Added [-[NSBrowser setSelectionIndexPaths:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407536-selectionindexpaths)Added -[NSObject browser:child:ofItem:]Added -[NSObject browser:headerViewControllerForItem:]Added -[NSObject browser:isLeafItem:]Added -[NSObject browser:numberOfChildrenOfItem:]Added -[NSObject browser:objectValueForItem:]Added -[NSObject browser:previewViewControllerForLeafItem:]Added -[NSObject browser:setObjectValue:forItem:]Added -[NSObject browser:shouldEditItem:]Added -[NSObject rootItemForBrowser:]Added NSBrowser(NSDeprecated)Modified [-[NSBrowser acceptsArrowKeys]](https://developer.apple.com/documentation/appkit/nsbrowser/1407546-acceptsarrowkeys)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSBrowser setAcceptsArrowKeys:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407680-setacceptsarrowkeys)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSBrowser displayAllColumns]](https://developer.apple.com/documentation/appkit/nsbrowser/1407753-displayallcolumns)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.3 |

Modified [-[NSBrowser updateScroller]](https://developer.apple.com/documentation/appkit/nsbrowser/1407743-updatescroller)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.3 |

Modified [-[NSBrowser displayColumn:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407760-displaycolumn)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.3 |

Modified [-[NSBrowser scrollViaScroller:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407655-scrollviascroller)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.3 |

NSCachedImageRep.hModified [-[NSCachedImageRep window]](https://developer.apple.com/documentation/appkit/nscachedimagerep/1431040-window)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSCachedImageRep initWithWindow:rect:]](https://developer.apple.com/documentation/appkit/nscachedimagerep/1431036-initwithwindow)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSCachedImageRep initWithSize:depth:separate:alpha:]](https://developer.apple.com/documentation/appkit/nscachedimagerep/1431038-initwithsize)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSCachedImageRep rect]](https://developer.apple.com/documentation/appkit/nscachedimagerep/1431032-rect)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

NSCell.hAdded [-[NSCell setUserInterfaceLayoutDirection:]](https://developer.apple.com/documentation/appkit/nscell/1529213-userinterfacelayoutdirection)Added [-[NSCell userInterfaceLayoutDirection]](https://developer.apple.com/documentation/appkit/nscell/1529213-userinterfacelayoutdirection)Added NSCell(NSDeprecated)Modified [-[NSCell setFloatingPointFormat:left:right:]](https://developer.apple.com/documentation/appkit/nscell/1560888-setfloatingpointformat)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.0 |

Modified [NSScaleProportionally](https://developer.apple.com/documentation/appkit/nsimagescaling/1534465-nsscaleproportionally)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [NSScaleToFit](https://developer.apple.com/documentation/appkit/nsimagescaling/nsscaletofit)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [NSScaleNone](https://developer.apple.com/documentation/appkit/nsimagescaling/nsscalenone)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSCell entryType]](https://developer.apple.com/documentation/appkit/nscell/1560897-entrytype)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.0 |

Modified [-[NSCell setEntryType:]](https://developer.apple.com/documentation/appkit/nscell/1560876-setentrytype)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.0 |

NSControl.hAdded NSControl(NSDeprecated)Modified [-[NSControl setFloatingPointFormat:left:right:]](https://developer.apple.com/documentation/appkit/nscontrol/1428931-setfloatingpointformat)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.0 |

NSCursor.hAdded [+[NSCursor contextualMenuCursor]](https://developer.apple.com/documentation/appkit/nscursor/1529142-contextualmenucursor)Added [+[NSCursor currentSystemCursor]](https://developer.apple.com/documentation/appkit/nscursor/1533611-currentsystem)Added [+[NSCursor dragCopyCursor]](https://developer.apple.com/documentation/appkit/nscursor/1529900-dragcopy)Added [+[NSCursor dragLinkCursor]](https://developer.apple.com/documentation/appkit/nscursor/1534435-draglink)Added [+[NSCursor operationNotAllowedCursor]](https://developer.apple.com/documentation/appkit/nscursor/1525180-operationnotallowedcursor)NSDocument.hAdded [+[NSDocument canConcurrentlyReadDocumentsOfType:]](https://developer.apple.com/documentation/appkit/nsdocument/1515216-canconcurrentlyreaddocumentsofty)NSEvent.hAdded [+[NSEvent doubleClickInterval]](https://developer.apple.com/documentation/appkit/nsevent/1528384-doubleclickinterval)Added [+[NSEvent keyRepeatDelay]](https://developer.apple.com/documentation/appkit/nsevent/1530832-keyrepeatdelay)Added [+[NSEvent keyRepeatInterval]](https://developer.apple.com/documentation/appkit/nsevent/1526076-keyrepeatinterval)Added [-[NSEvent magnification]](https://developer.apple.com/documentation/appkit/nsevent/1531642-magnification)Added [NSEventMaskBeginGesture](https://developer.apple.com/documentation/appkit/nseventmask/nseventmaskbegingesture)Added [NSEventMaskEndGesture](https://developer.apple.com/documentation/appkit/nseventmask/nseventmaskendgesture)Added [NSEventMaskGesture](https://developer.apple.com/documentation/appkit/nseventmask/nseventmaskgesture)Added [NSEventMaskMagnify](https://developer.apple.com/documentation/appkit/nsevent/eventtypemask/1528004-magnify)Added [NSEventMaskRotate](https://developer.apple.com/documentation/appkit/nsevent/eventtypemask/1535086-rotate)Added [NSEventMaskSwipe](https://developer.apple.com/documentation/appkit/nseventmask/nseventmaskswipe)Added [NSEventTypeBeginGesture](https://developer.apple.com/documentation/appkit/nsevent/eventtype/begingesture)Added [NSEventTypeEndGesture](https://developer.apple.com/documentation/appkit/nsevent/eventtype/endgesture)Added [NSEventTypeGesture](https://developer.apple.com/documentation/appkit/nseventtype/nseventtypegesture)Added [NSEventTypeMagnify](https://developer.apple.com/documentation/appkit/nsevent/eventtype/magnify)Added [NSEventTypeRotate](https://developer.apple.com/documentation/appkit/nsevent/eventtype/rotate)Added [NSEventTypeSwipe](https://developer.apple.com/documentation/appkit/nseventtype/nseventtypeswipe)NSFileWrapper.hAdded [-[NSFileWrapper initSymbolicLinkWithDestinationURL:]](https://developer.apple.com/documentation/foundation/filewrapper/1415098-init)Added [-[NSFileWrapper initWithURL:options:error:]](https://developer.apple.com/documentation/foundation/filewrapper/1415658-init)Added [-[NSFileWrapper matchesContentsOfURL:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1408360-matchescontentsofurl)Added [-[NSFileWrapper readFromURL:options:error:]](https://developer.apple.com/documentation/foundation/filewrapper/1411645-read)Added [-[NSFileWrapper symbolicLinkDestinationURL]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1408364-symboliclinkdestinationurl)Added [-[NSFileWrapper writeToURL:options:originalContentsURL:error:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1415981-writetourl)Added NSFileWrapper(NSDeprecated)Added [NSFileWrapperReadingImmediate](https://developer.apple.com/documentation/foundation/nsfilewrapperreadingoptions/nsfilewrapperreadingimmediate)Added [NSFileWrapperReadingOptions](https://developer.apple.com/documentation/foundation/filewrapper/readingoptions)Added [NSFileWrapperReadingWithoutMapping](https://developer.apple.com/documentation/foundation/nsfilewrapperreadingoptions/nsfilewrapperreadingwithoutmapping)Added [NSFileWrapperWritingAtomic](https://developer.apple.com/documentation/foundation/nsfilewrapperwritingoptions/nsfilewrapperwritingatomic)Added [NSFileWrapperWritingOptions](https://developer.apple.com/documentation/foundation/nsfilewrapperwritingoptions)Added [NSFileWrapperWritingWithNameUpdating](https://developer.apple.com/documentation/foundation/filewrapper/writingoptions/1408447-withnameupdating)Modified [-[NSFileWrapper keyForFileWrapper:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1407541-keyforfilewrapper)

|  | Declaration |
| --- | --- |
| Old | - (NSString \*)keyForFileWrapper:(NSFileWrapper \*)doc |
| New | - (NSString \*)keyForFileWrapper:(NSFileWrapper \*)child |

Modified [-[NSFileWrapper initWithSerializedRepresentation:]](https://developer.apple.com/documentation/foundation/filewrapper/1407515-init)

|  | Declaration |
| --- | --- |
| Old | - (id)initWithSerializedRepresentation:(NSData \*)data |
| New | - (id)initWithSerializedRepresentation:(NSData \*)serializeRepresentation |

Modified [-[NSFileWrapper addFileWrapper:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1415067-addfilewrapper)

|  | Declaration |
| --- | --- |
| Old | - (NSString \*)addFileWrapper:(NSFileWrapper \*)doc |
| New | - (NSString \*)addFileWrapper:(NSFileWrapper \*)child |

Modified [-[NSFileWrapper addFileWithPath:]](https://developer.apple.com/documentation/foundation/filewrapper/1417211-addfile)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSFileWrapper initRegularFileWithContents:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1409508-initregularfilewithcontents)

|  | Declaration |
| --- | --- |
| Old | - (id)initRegularFileWithContents:(NSData \*)data |
| New | - (id)initRegularFileWithContents:(NSData \*)contents |

Modified [-[NSFileWrapper removeFileWrapper:]](https://developer.apple.com/documentation/foundation/filewrapper/1417343-removefilewrapper)

|  | Declaration |
| --- | --- |
| Old | - (void)removeFileWrapper:(NSFileWrapper \*)doc |
| New | - (void)removeFileWrapper:(NSFileWrapper \*)child |

Modified [-[NSFileWrapper needsToBeUpdatedFromPath:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1407738-needstobeupdatedfrompath)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSFileWrapper setFilename:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1416684-filename)

|  | Declaration |
| --- | --- |
| Old | - (void)setFilename:(NSString \*)filename |
| New | - (void)setFilename:(NSString \*)fileName |

Modified [-[NSFileWrapper setPreferredFilename:]](https://developer.apple.com/documentation/foundation/filewrapper/1409368-preferredfilename)

|  | Declaration |
| --- | --- |
| Old | - (void)setPreferredFilename:(NSString \*)filename |
| New | - (void)setPreferredFilename:(NSString \*)fileName |

Modified [-[NSFileWrapper initSymbolicLinkWithDestination:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1411268-initsymboliclinkwithdestination)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSFileWrapper updateFromPath:]](https://developer.apple.com/documentation/foundation/filewrapper/1416300-update)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSFileWrapper initDirectoryWithFileWrappers:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1415121-initdirectorywithfilewrappers)

|  | Declaration |
| --- | --- |
| Old | - (id)initDirectoryWithFileWrappers:(NSDictionary \*)docs |
| New | - (id)initDirectoryWithFileWrappers:(NSDictionary \*)childrenByPreferredName |

Modified [-[NSFileWrapper symbolicLinkDestination]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1418302-symboliclinkdestination)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSFileWrapper addSymbolicLinkWithDestination:preferredFilename:]](https://developer.apple.com/documentation/foundation/filewrapper/1414604-addsymboliclink)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSFileWrapper writeToFile:atomically:updateFilenames:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1415079-writetofile)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSFileWrapper setFileAttributes:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1412745-fileattributes)

|  | Declaration |
| --- | --- |
| Old | - (void)setFileAttributes:(NSDictionary \*)attributes |
| New | - (void)setFileAttributes:(NSDictionary \*)fileAttributes |

Modified [-[NSFileWrapper addRegularFileWithContents:preferredFilename:]](https://developer.apple.com/documentation/foundation/filewrapper/1418374-addregularfile)

|  | Declaration |
| --- | --- |
| Old | - (NSString \*)addRegularFileWithContents:(NSData \*)data preferredFilename:(NSString \*)filename |
| New | - (NSString \*)addRegularFileWithContents:(NSData \*)data preferredFilename:(NSString \*)fileName |

Modified [-[NSFileWrapper initWithPath:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1408388-initwithpath)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

NSGraphicsContext.hAdded NSGraphicsContext(NSGraphicsContextDeprecate) (no architecture available)Modified [-[NSGraphicsContext focusStack]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1564181-focusstack)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified [-[NSGraphicsContext setFocusStack:]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1564182-setfocusstack)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

NSImage.hAdded [-[NSImage CGImageForProposedRect:context:hints:]](https://developer.apple.com/documentation/appkit/nsimage/1519861-cgimageforproposedrect)Added [-[NSImage accessibilityDescription]](https://developer.apple.com/documentation/appkit/nsimage/1519943-accessibilitydescription)Added [-[NSImage bestRepresentationForRect:context:hints:]](https://developer.apple.com/documentation/appkit/nsimage/1519961-bestrepresentationforrect)Added [-[NSImage initWithCGImage:size:]](https://developer.apple.com/documentation/appkit/nsimage/1519939-init)Added [-[NSImage setAccessibilityDescription:]](https://developer.apple.com/documentation/appkit/nsimage/1519943-accessibilitydescription)Added [NSImageHintCTM](https://developer.apple.com/documentation/appkit/nsimagerep/hintkey/1520065-ctm)Added [NSImageHintInterpolation](https://developer.apple.com/documentation/appkit/nsimagehintinterpolation)Added [NSImageNameMenuMixedStateTemplate](https://developer.apple.com/documentation/appkit/nsimage/1519975-menumixedstatetemplatename)Added [NSImageNameMenuOnStateTemplate](https://developer.apple.com/documentation/appkit/nsimage/1519996-menuonstatetemplatename)Modified [-[NSImage bestRepresentationForDevice:]](https://developer.apple.com/documentation/appkit/nsimage/1519925-bestrepresentationfordevice)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

NSImageRep.hAdded [-[NSImageRep CGImageForProposedRect:context:hints:]](https://developer.apple.com/documentation/appkit/nsimagerep/1533478-cgimageforproposedrect)NSLayoutManager.hAdded [-[NSLayoutManager characterIndexForPoint:inTextContainer:fractionOfDistanceBetweenInsertionPoints:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403028-characterindex)NSMenu.hAdded [-[NSMenu allowsContextMenuPlugIns]](https://developer.apple.com/documentation/appkit/nsmenu/1518220-allowscontextmenuplugins)Added [-[NSMenu cancelTrackingWithoutAnimation]](https://developer.apple.com/documentation/appkit/nsmenu/1518244-canceltrackingwithoutanimation)Added [-[NSMenu font]](https://developer.apple.com/documentation/appkit/nsmenu/1518230-font)Added [-[NSMenu minimumWidth]](https://developer.apple.com/documentation/appkit/nsmenu/1518221-minimumwidth)Added [-[NSMenu popUpMenuPositioningItem:atLocation:inView:]](https://developer.apple.com/documentation/appkit/nsmenu/1518212-popupmenupositioningitem)Added [-[NSMenu removeAllItems]](https://developer.apple.com/documentation/appkit/nsmenu/1518234-removeallitems)Added [-[NSMenu setAllowsContextMenuPlugIns:]](https://developer.apple.com/documentation/appkit/nsmenu/1518220-allowscontextmenuplugins)Added [-[NSMenu setFont:]](https://developer.apple.com/documentation/appkit/nsmenu/1518230-font)Added [-[NSMenu setMinimumWidth:]](https://developer.apple.com/documentation/appkit/nsmenu/1518221-minimumwidth)Added [-[NSMenu size]](https://developer.apple.com/documentation/appkit/nsmenu/1518185-size)Added -[NSObject confinementRectForMenu:onScreen:]NSMenuItem.hAdded [-[NSMenuItem parentItem]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514813-parent)NSOutlineView.hAdded -[NSObject outlineView:shouldReorderColumn:toColumn:]Added -[NSObject outlineView:shouldShowOutlineCellForItem:]Added -[NSObject outlineView:sizeToFitWidthOfColumn:]NSProgressIndicator.hAdded NSProgressIndicator(NSProgressIndicatorDeprecated)Modified [-[NSProgressIndicator animate:]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501139-animate)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSProgressIndicator animationDelay]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501178-animationdelay)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSProgressIndicator setAnimationDelay:]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501151-setanimationdelay)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

NSResponder.hAdded [-[NSResponder beginGestureWithEvent:]](https://developer.apple.com/documentation/appkit/nsresponder/1526368-begingesturewithevent)Added [-[NSResponder endGestureWithEvent:]](https://developer.apple.com/documentation/appkit/nsresponder/1531251-endgesturewithevent)Added [-[NSResponder magnifyWithEvent:]](https://developer.apple.com/documentation/appkit/nsresponder/1525862-magnifywithevent)Added [-[NSResponder rotateWithEvent:]](https://developer.apple.com/documentation/appkit/nsresponder/1525572-rotatewithevent)Added [-[NSResponder swipeWithEvent:]](https://developer.apple.com/documentation/appkit/nsresponder/1524275-swipewithevent)NSRunningApplication.hAdded [NSRunningApplication](https://developer.apple.com/documentation/appkit/nsrunningapplication)Added [-[NSRunningApplication activateWithOptions:]](https://developer.apple.com/documentation/appkit/nsrunningapplication/1528725-activatewithoptions)Added [NSRunningApplication.activationPolicy](https://developer.apple.com/documentation/appkit/nsrunningapplication/1533103-activationpolicy)Added [NSRunningApplication.active](https://developer.apple.com/documentation/appkit/nsrunningapplication/1528778-isactive)Added [NSRunningApplication.bundleIdentifier](https://developer.apple.com/documentation/appkit/nsrunningapplication/1529140-bundleidentifier)Added [NSRunningApplication.bundleURL](https://developer.apple.com/documentation/appkit/nsrunningapplication/1535500-bundleurl)Added [+[NSRunningApplication currentApplication]](https://developer.apple.com/documentation/appkit/nsrunningapplication/1533604-current)Added [NSRunningApplication.executableArchitecture](https://developer.apple.com/documentation/appkit/nsrunningapplication/1524287-executablearchitecture)Added [NSRunningApplication.executableURL](https://developer.apple.com/documentation/appkit/nsrunningapplication/1531062-executableurl)Added [NSRunningApplication.finishedLaunching](https://developer.apple.com/documentation/appkit/nsrunningapplication/1532002-isfinishedlaunching)Added [-[NSRunningApplication forceTerminate]](https://developer.apple.com/documentation/appkit/nsrunningapplication/1530370-forceterminate)Added [NSRunningApplication.hidden](https://developer.apple.com/documentation/appkit/nsrunningapplication/1525949-ishidden)Added [-[NSRunningApplication hide]](https://developer.apple.com/documentation/appkit/nsrunningapplication/1526608-hide)Added [NSRunningApplication.icon](https://developer.apple.com/documentation/appkit/nsrunningapplication/1529885-icon)Added [NSRunningApplication.launchDate](https://developer.apple.com/documentation/appkit/nsrunningapplication/1532595-launchdate)Added [NSRunningApplication.localizedName](https://developer.apple.com/documentation/appkit/nsrunningapplication/1526751-localizedname)Added [NSRunningApplication.processIdentifier](https://developer.apple.com/documentation/appkit/nsrunningapplication/1526998-processidentifier)Added [+[NSRunningApplication runningApplicationWithProcessIdentifier:]](https://developer.apple.com/documentation/appkit/nsrunningapplication/1530730-init)Added [+[NSRunningApplication runningApplicationsWithBundleIdentifier:]](https://developer.apple.com/documentation/appkit/nsrunningapplication/1530798-runningapplications)Added [-[NSRunningApplication terminate]](https://developer.apple.com/documentation/appkit/nsrunningapplication/1528922-terminate)Added [NSRunningApplication.terminated](https://developer.apple.com/documentation/appkit/nsrunningapplication/1532239-isterminated)Added [-[NSRunningApplication unhide]](https://developer.apple.com/documentation/appkit/nsrunningapplication/1534676-unhide)Added [-[NSWorkspace runningApplications]](https://developer.apple.com/documentation/appkit/nsworkspace/1534059-runningapplications)Added [NSApplicationActivateAllWindows](https://developer.apple.com/documentation/appkit/nsapplicationactivationoptions/nsapplicationactivateallwindows)Added [NSApplicationActivateIgnoringOtherApps](https://developer.apple.com/documentation/appkit/nsapplicationactivationoptions/nsapplicationactivateignoringotherapps)Added [NSApplicationActivationOptions](https://developer.apple.com/documentation/appkit/nsapplicationactivationoptions)Added [NSApplicationActivationPolicy](https://developer.apple.com/documentation/appkit/nsapplication/activationpolicy)Added [NSApplicationActivationPolicyAccessory](https://developer.apple.com/documentation/appkit/nsapplicationactivationpolicy/nsapplicationactivationpolicyaccessory)Added [NSApplicationActivationPolicyProhibited](https://developer.apple.com/documentation/appkit/nsapplicationactivationpolicy/nsapplicationactivationpolicyprohibited)Added [NSApplicationActivationPolicyRegular](https://developer.apple.com/documentation/appkit/nsapplication/activationpolicy/regular)Added NSWorkspace(NSWorkspaceRunningApplications)NSSavePanel.hAdded NSSavePanel(NSDeprecated)Modified [-[NSSavePanel selectText:]](https://developer.apple.com/documentation/appkit/nssavepanel/1539012-selecttext)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.3 |

NSSpellChecker.hAdded [-[NSSpellChecker automaticallyIdentifiesLanguages]](https://developer.apple.com/documentation/appkit/nsspellchecker/1534335-automaticallyidentifieslanguages)Added [-[NSSpellChecker checkString:range:types:options:inSpellDocumentWithTag:orthography:wordCount:]](https://developer.apple.com/documentation/appkit/nsspellchecker/1535739-checkstring)Added [-[NSSpellChecker guessesForWordRange:inString:language:inSpellDocumentWithTag:]](https://developer.apple.com/documentation/appkit/nsspellchecker/1527419-guesses)Added [-[NSSpellChecker setAutomaticallyIdentifiesLanguages:]](https://developer.apple.com/documentation/appkit/nsspellchecker/1534335-automaticallyidentifieslanguages)Added [NSTextCheckingOrthographyKey](https://developer.apple.com/documentation/appkit/nsspellchecker/optionkey/1530305-orthography)Added [NSTextCheckingQuotesKey](https://developer.apple.com/documentation/appkit/nstextcheckingquoteskey)Added [NSTextCheckingReplacementsKey](https://developer.apple.com/documentation/appkit/nstextcheckingreplacementskey)NSTabViewItem.hAdded [-[NSTabViewItem setToolTip:]](https://developer.apple.com/documentation/appkit/nstabviewitem/1477515-tooltip)Added [-[NSTabViewItem toolTip]](https://developer.apple.com/documentation/appkit/nstabviewitem/1477515-tooltip)NSTableColumn.hAdded NSTableColumn(NSDeprecated)Modified [-[NSTableColumn setResizable:]](https://developer.apple.com/documentation/appkit/nstablecolumn/1579359-setresizable)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.4 |

Modified [-[NSTableColumn isResizable]](https://developer.apple.com/documentation/appkit/nstablecolumn/1579360-isresizable)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.4 |

NSTableView.hRemoved NSObject(NSTableDataSource)Added -[NSObject tableView:shouldReorderColumn:toColumn:]Added -[NSObject tableView:sizeToFitWidthOfColumn:]Added [-[NSTableView focusedColumn]](https://developer.apple.com/documentation/appkit/nstableview/1533870-focusedcolumn)Added [-[NSTableView performClickOnCellAtColumn:row:]](https://developer.apple.com/documentation/appkit/nstableview/1527932-performclickoncellatcolumn)Added [-[NSTableView reloadDataForRowIndexes:columnIndexes:]](https://developer.apple.com/documentation/appkit/nstableview/1527621-reloaddata)Added [-[NSTableView setFocusedColumn:]](https://developer.apple.com/documentation/appkit/nstableview/1534977-setfocusedcolumn)Added [-[NSTableView shouldFocusCell:atColumn:row:]](https://developer.apple.com/documentation/appkit/nstableview/1531629-shouldfocuscell)Added NSObject(NSTableViewDataSource)Added NSObject(NSTableViewDataSourceDeprecated)Added [NSTableViewSelectionHighlightStyleNone](https://developer.apple.com/documentation/appkit/nstableview/selectionhighlightstyle/none)Modified [-[NSTableView indicatorImageInTableColumn:]](https://developer.apple.com/documentation/appkit/nstableview/1524846-indicatorimage)

|  | Declaration |
| --- | --- |
| Old | - (NSImage \*)indicatorImageInTableColumn:(NSTableColumn \*)tc |
| New | - (NSImage \*)indicatorImageInTableColumn:(NSTableColumn \*)tableColumn |

Modified [-[NSTableView setDropRow:dropOperation:]](https://developer.apple.com/documentation/appkit/nstableview/1535123-setdroprow)

|  | Declaration |
| --- | --- |
| Old | - (void)setDropRow:(NSInteger)row dropOperation:(NSTableViewDropOperation)op |
| New | - (void)setDropRow:(NSInteger)row dropOperation:(NSTableViewDropOperation)dropOperation |

Modified [-[NSTableView setIndicatorImage:inTableColumn:]](https://developer.apple.com/documentation/appkit/nstableview/1534381-setindicatorimage)

|  | Declaration |
| --- | --- |
| Old | - (void)setIndicatorImage:(NSImage \*)anImage inTableColumn:(NSTableColumn \*)tc |
| New | - (void)setIndicatorImage:(NSImage \*)anImage inTableColumn:(NSTableColumn \*)tableColumn |

Modified [-[NSTableView moveColumn:toColumn:]](https://developer.apple.com/documentation/appkit/nstableview/1530719-movecolumn)

|  | Declaration |
| --- | --- |
| Old | - (void)moveColumn:(NSInteger)column toColumn:(NSInteger)newIndex |
| New | - (void)moveColumn:(NSInteger)oldIndex toColumn:(NSInteger)newIndex |

Modified [-[NSTableView addTableColumn:]](https://developer.apple.com/documentation/appkit/nstableview/1534098-addtablecolumn)

|  | Declaration |
| --- | --- |
| Old | - (void)addTableColumn:(NSTableColumn \*)column |
| New | - (void)addTableColumn:(NSTableColumn \*)tableColumn |

Modified [-[NSTableView setHighlightedTableColumn:]](https://developer.apple.com/documentation/appkit/nstableview/1524980-highlightedtablecolumn)

|  | Declaration |
| --- | --- |
| Old | - (void)setHighlightedTableColumn:(NSTableColumn \*)tc |
| New | - (void)setHighlightedTableColumn:(NSTableColumn \*)tableColumn |

Modified [-[NSObject tableView:writeRows:toPasteboard:]](https://developer.apple.com/documentation/objectivec/nsobject/1539424-tableview)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.4 |

Modified [-[NSTableView removeTableColumn:]](https://developer.apple.com/documentation/appkit/nstableview/1535381-removetablecolumn)

|  | Declaration |
| --- | --- |
| Old | - (void)removeTableColumn:(NSTableColumn \*)column |
| New | - (void)removeTableColumn:(NSTableColumn \*)tableColumn |

NSTextList.hAdded [-[NSTextList setStartingItemNumber:]](https://developer.apple.com/documentation/appkit/nstextlist/1528597-startingitemnumber)Added [-[NSTextList startingItemNumber]](https://developer.apple.com/documentation/appkit/nstextlist/1528597-startingitemnumber)NSTextView.hAdded -[NSObject textView:didCheckTextInRange:results:orthography:wordCount:]Added -[NSObject textView:willCheckTextInRange:options:types:]Added [-[NSTextView checkTextInRange:types:options:]](https://developer.apple.com/documentation/appkit/nstextview/1449240-checktextinrange)Added [-[NSTextView enabledTextCheckingTypes]](https://developer.apple.com/documentation/appkit/nstextview/1449529-enabledtextcheckingtypes)Added -[NSTextView handleTextCheckingResults:forRange:orthography:wordCount:]Added [-[NSTextView isAutomaticDashSubstitutionEnabled]](https://developer.apple.com/documentation/appkit/nstextview/1449403-automaticdashsubstitutionenabled)Added [-[NSTextView isAutomaticDataDetectionEnabled]](https://developer.apple.com/documentation/appkit/nstextview/1449192-automaticdatadetectionenabled)Added [-[NSTextView isAutomaticSpellingCorrectionEnabled]](https://developer.apple.com/documentation/appkit/nstextview/1449254-automaticspellingcorrectionenabl)Added [-[NSTextView isAutomaticTextReplacementEnabled]](https://developer.apple.com/documentation/appkit/nstextview/1449210-automatictextreplacementenabled)Added [-[NSTextView isCoalescingUndo]](https://developer.apple.com/documentation/appkit/nstextview/1449368-coalescingundo)Added [-[NSTextView setAutomaticDashSubstitutionEnabled:]](https://developer.apple.com/documentation/appkit/nstextview/1449403-automaticdashsubstitutionenabled)Added [-[NSTextView setAutomaticDataDetectionEnabled:]](https://developer.apple.com/documentation/appkit/nstextview/1449192-automaticdatadetectionenabled)Added [-[NSTextView setAutomaticSpellingCorrectionEnabled:]](https://developer.apple.com/documentation/appkit/nstextview/1449254-automaticspellingcorrectionenabl)Added [-[NSTextView setAutomaticTextReplacementEnabled:]](https://developer.apple.com/documentation/appkit/nstextview/1449210-isautomatictextreplacementenable)Added [-[NSTextView setEnabledTextCheckingTypes:]](https://developer.apple.com/documentation/appkit/nstextview/1449529-enabledtextcheckingtypes)Added [-[NSTextView toggleAutomaticDashSubstitution:]](https://developer.apple.com/documentation/appkit/nstextview/1449305-toggleautomaticdashsubstitution)Added [-[NSTextView toggleAutomaticDataDetection:]](https://developer.apple.com/documentation/appkit/nstextview/1449499-toggleautomaticdatadetection)Added [-[NSTextView toggleAutomaticSpellingCorrection:]](https://developer.apple.com/documentation/appkit/nstextview/1449178-toggleautomaticspellingcorrectio)Added [-[NSTextView toggleAutomaticTextReplacement:]](https://developer.apple.com/documentation/appkit/nstextview/1449200-toggleautomatictextreplacement)NSView.hAdded [-[NSView canDrawConcurrently]](https://developer.apple.com/documentation/appkit/nsview/1483425-candrawconcurrently)Added [-[NSView setCanDrawConcurrently:]](https://developer.apple.com/documentation/appkit/nsview/1483425-candrawconcurrently)NSWindow.hAdded [-[NSWindow allowsConcurrentViewDrawing]](https://developer.apple.com/documentation/appkit/nswindow/1419300-allowsconcurrentviewdrawing)Added [-[NSWindow setAllowsConcurrentViewDrawing:]](https://developer.apple.com/documentation/appkit/nswindow/1419300-allowsconcurrentviewdrawing)NSWorkspace.hAdded [-[NSWorkspace desktopImageOptionsForScreen:]](https://developer.apple.com/documentation/appkit/nsworkspace/1530855-desktopimageoptionsforscreen)Added [-[NSWorkspace desktopImageURLForScreen:]](https://developer.apple.com/documentation/appkit/nsworkspace/1530635-desktopimageurlforscreen)Added [-[NSWorkspace fileLabelColors]](https://developer.apple.com/documentation/appkit/nsworkspace/1527553-filelabelcolors)Added [-[NSWorkspace fileLabels]](https://developer.apple.com/documentation/appkit/nsworkspace/1533953-filelabels)Added [-[NSWorkspace setDesktopImageURL:forScreen:options:error:]](https://developer.apple.com/documentation/appkit/nsworkspace/1527228-setdesktopimageurl)Added [-[NSWorkspace showSearchResultsForQueryString:]](https://developer.apple.com/documentation/appkit/nsworkspace/1532131-showsearchresults)Added NSWorkspace(NSDeprecated)Added NSWorkspace(NSDesktopImages)Added [NSWorkspaceApplicationKey](https://developer.apple.com/documentation/appkit/nsworkspace/1531626-applicationuserinfokey)Added [NSWorkspaceDesktopImageAllowClippingKey](https://developer.apple.com/documentation/appkit/nsworkspace/desktopimageoptionkey/1532597-allowclipping)Added [NSWorkspaceDesktopImageFillColorKey](https://developer.apple.com/documentation/appkit/nsworkspacedesktopimagefillcolorkey)Added [NSWorkspaceDesktopImageScalingKey](https://developer.apple.com/documentation/appkit/nsworkspacedesktopimagescalingkey)Added [NSWorkspaceDidActivateApplicationNotification](https://developer.apple.com/documentation/appkit/nsworkspace/1535049-didactivateapplicationnotificati)Added [NSWorkspaceDidChangeFileLabelsNotification](https://developer.apple.com/documentation/appkit/nsworkspace/1524966-didchangefilelabelsnotification)Added [NSWorkspaceDidDeactivateApplicationNotification](https://developer.apple.com/documentation/appkit/nsworkspacediddeactivateapplicationnotification)Added [NSWorkspaceDidHideApplicationNotification](https://developer.apple.com/documentation/appkit/nsworkspace/1534328-didhideapplicationnotification)Added [NSWorkspaceDidRenameVolumeNotification](https://developer.apple.com/documentation/appkit/nsworkspacedidrenamevolumenotification)Added [NSWorkspaceDidUnhideApplicationNotification](https://developer.apple.com/documentation/appkit/nsworkspacedidunhideapplicationnotification)Added [NSWorkspaceScreensDidSleepNotification](https://developer.apple.com/documentation/appkit/nsworkspace/1530288-screensdidsleepnotification)Added [NSWorkspaceScreensDidWakeNotification](https://developer.apple.com/documentation/appkit/nsworkspacescreensdidwakenotification)Added [NSWorkspaceVolumeLocalizedNameKey](https://developer.apple.com/documentation/appkit/nsworkspace/1529705-localizedvolumenameuserinfokey)Added [NSWorkspaceVolumeOldLocalizedNameKey](https://developer.apple.com/documentation/appkit/nsworkspacevolumeoldlocalizednamekey)Added [NSWorkspaceVolumeOldURLKey](https://developer.apple.com/documentation/appkit/nsworkspace/1535192-oldvolumeurluserinfokey)Added [NSWorkspaceVolumeURLKey](https://developer.apple.com/documentation/appkit/nsworkspace/1525104-volumeurluserinfokey)Modified [-[NSWorkspace selectFile:inFileViewerRootedAtPath:]](https://developer.apple.com/documentation/appkit/nsworkspace/1524399-selectfile)

|  | Declaration |
| --- | --- |
| Old | - (BOOL)selectFile:(NSString \*)fullPath inFileViewerRootedAtPath:(NSString \*)rootFullpath |
| New | - (BOOL)selectFile:(NSString \*)fullPath inFileViewerRootedAtPath:(NSString \*)rootFullPath |

Modified [NSApplicationFileType](https://developer.apple.com/documentation/appkit/nsapplicationfiletype)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSWorkspace noteUserDefaultsChanged]](https://developer.apple.com/documentation/appkit/nsworkspace/1579277-noteuserdefaultschanged)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [NSDirectoryFileType](https://developer.apple.com/documentation/appkit/nsdirectoryfiletype)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSWorkspace mountNewRemovableMedia]](https://developer.apple.com/documentation/appkit/nsworkspace/1579278-mountnewremovablemedia)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [NSPlainFileType](https://developer.apple.com/documentation/appkit/nsplainfiletype)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSWorkspace userDefaultsChanged]](https://developer.apple.com/documentation/appkit/nsworkspace/1579273-userdefaultschanged)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSWorkspace openTempFile:]](https://developer.apple.com/documentation/appkit/nsworkspace/1579274-opentempfile)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSWorkspace findApplications]](https://developer.apple.com/documentation/appkit/nsworkspace/1579271-findapplications)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSWorkspace checkForRemovableMedia]](https://developer.apple.com/documentation/appkit/nsworkspace/1579281-checkforremovablemedia)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSWorkspace noteFileSystemChanged]](https://developer.apple.com/documentation/appkit/nsworkspace/1579268-notefilesystemchanged)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSWorkspace fileSystemChanged]](https://developer.apple.com/documentation/appkit/nsworkspace/1579275-filesystemchanged)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [NSShellCommandFileType](https://developer.apple.com/documentation/appkit/nsshellcommandfiletype)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSWorkspace slideImage:from:to:]](https://developer.apple.com/documentation/appkit/nsworkspace/1579270-slideimage)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [NSFilesystemFileType](https://developer.apple.com/documentation/appkit/nsfilesystemfiletype)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

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
