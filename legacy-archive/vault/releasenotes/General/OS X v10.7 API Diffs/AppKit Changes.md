---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/AppKit.html
archived_at: '2026-07-18T02:54:24.500808Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# AppKit Changes

## AppKit

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

AppKitDefines.hAdded #def AVAILABLE_MAC_OS_X_VERSION_10_0_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_0Added #def AVAILABLE_MAC_OS_X_VERSION_10_1_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_1Added #def AVAILABLE_MAC_OS_X_VERSION_10_2_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_2Added #def AVAILABLE_MAC_OS_X_VERSION_10_3_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_3Added #def AVAILABLE_MAC_OS_X_VERSION_10_4_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_4Added #def AVAILABLE_MAC_OS_X_VERSION_10_5_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_5Added #def AVAILABLE_MAC_OS_X_VERSION_10_6_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_6Added #def AVAILABLE_MAC_OS_X_VERSION_10_7_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_7NSATSTypesetter.hModified -[NSATSTypesetter insertGlyph:atGlyphIndex:characterIndex:]

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter setHyphenationFactor:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1526758-hyphenationfactor)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter layoutManager]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1535366-layoutmanager)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter shouldBreakLineByHyphenatingBeforeCharacterAtIndex:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1534510-shouldbreaklinebyhyphenatingbefo)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter textTabForGlyphLocation:writingDirection:maxLocation:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1531288-texttabforglyphlocation)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter getLineFragmentRect:usedRect:forParagraphSeparatorGlyphRange:atProposedOrigin:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1528343-getlinefragmentrect)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified -[NSATSTypesetter setDrawsOutsideLineFragment:forGlyphRange:]

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter typesetterBehavior]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1533819-typesetterbehavior)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter setTypesetterBehavior:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1533819-typesetterbehavior)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter usesFontLeading]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1533331-usesfontleading)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified -[NSATSTypesetter characterRangeForGlyphRange:actualGlyphRange:]

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter paragraphSpacingBeforeGlyphAtIndex:withProposedLineFragmentRect:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1530080-paragraphspacingbeforeglyphatind)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter substituteFontForFont:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1535433-substitutefont)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter layoutParagraphAtPoint:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1525179-layoutparagraphatpoint)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter paragraphGlyphRange]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1528373-paragraphglyphrange)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter boundingBoxForControlGlyphAtIndex:forTextContainer:proposedLineFragment:glyphPosition:characterIndex:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1535434-boundingbox)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified -[NSATSTypesetter setAttachmentSize:forGlyphRange:]

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified -[NSATSTypesetter setLineFragmentRect:forGlyphRange:usedRect:baselineOffset:]

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter setBidiProcessingEnabled:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1524295-bidiprocessingenabled)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter attributedString]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1530598-attributedstring)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter currentTextContainer]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1527830-currenttextcontainer)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter setAttributedString:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1530598-attributedstring)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter shouldBreakLineByWordBeforeCharacterAtIndex:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1528327-shouldbreaklinebywordbeforechara)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter setParagraphGlyphRange:separatorGlyphRange:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1534099-setparagraphglyphrange)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter getGlyphsInRange:glyphs:characterIndexes:glyphInscriptions:elasticBits:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1527411-getglyphsinrange)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter paragraphSeparatorGlyphRange]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1531108-paragraphseparatorglyphrange)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified -[NSATSTypesetter deleteGlyphsInRange:]

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter setUsesFontLeading:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1533331-usesfontleading)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter hyphenationFactorForGlyphAtIndex:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1533979-hyphenationfactorforglyphatindex)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter paragraphSpacingAfterGlyphAtIndex:withProposedLineFragmentRect:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1532075-paragraphspacingafterglyphatinde)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter bidiProcessingEnabled]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1524295-bidiprocessingenabled)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter setLineFragmentPadding:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1532628-linefragmentpadding)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter setHardInvalidation:forGlyphRange:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1526532-sethardinvalidation)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified NSATSTypesetter(NSGlyphStorageInterface)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified -[NSATSTypesetter setLocation:withAdvancements:forStartOfGlyphRange:]

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter hyphenationFactor]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1526758-hyphenationfactor)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified NSATSTypesetter(NSLayoutPhaseInterface)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified NSATSTypesetter(NSPrimitiveInterface)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter hyphenCharacterForGlyphAtIndex:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1525948-hyphencharacter)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified -[NSATSTypesetter glyphRangeForCharacterRange:actualCharacterRange:]

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter lineSpacingAfterGlyphAtIndex:withProposedLineFragmentRect:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1533513-linespacingafterglyphatindex)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter lineFragmentPadding]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1532628-linefragmentpadding)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified -[NSATSTypesetter setNotShownAttribute:forGlyphRange:]

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified -[NSATSTypesetter setBidiLevels:forGlyphRange:]

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified -[NSATSTypesetter substituteGlyphsInRange:withGlyphs:]

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

Modified [-[NSATSTypesetter willSetLineFragmentRect:forGlyphRange:usedRect:baselineOffset:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1526615-willsetlinefragmentrect)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

NSAccessibility.hRemoved NSAccessibilityHorizontialUnitDescriptionAttributeRemoved NSAccessibilityHorizontialUnitsAttributeAdded [NSAccessibilityAutocorrectedTextAttribute](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1529894-accessibilityautocorrected)Added [NSAccessibilityFullScreenButtonAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1533541-fullscreenbutton)Added [NSAccessibilityFullScreenButtonSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysubrole/1533410-fullscreenbutton)Added [NSAccessibilityIdentifierAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1528737-identifier)Added [NSAccessibilityPopoverRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1531574-popover)NSAnimationContext.hAdded [-[NSAnimationContext completionHandler]](https://developer.apple.com/documentation/appkit/nsanimationcontext/1531132-completionhandler)Added [+[NSAnimationContext runAnimationGroup:completionHandler:]](https://developer.apple.com/documentation/appkit/nsanimationcontext/1529847-runanimationgroup)Added [-[NSAnimationContext setCompletionHandler:]](https://developer.apple.com/documentation/appkit/nsanimationcontext/1531132-completionhandler)Added [-[NSAnimationContext setTimingFunction:]](https://developer.apple.com/documentation/appkit/nsanimationcontext/1524985-timingfunction)Added [-[NSAnimationContext timingFunction]](https://developer.apple.com/documentation/appkit/nsanimationcontext/1524985-timingfunction)NSApplication.hAdded [-[NSApplication disableRelaunchOnLogin]](https://developer.apple.com/documentation/appkit/nsapplication/1428376-disablerelaunchonlogin)Added [-[NSApplication enableRelaunchOnLogin]](https://developer.apple.com/documentation/appkit/nsapplication/1428453-enablerelaunchonlogin)Added [-[NSApplication enabledRemoteNotificationTypes]](https://developer.apple.com/documentation/appkit/nsapplication/1428776-enabledremotenotificationtypes)Added [-[NSApplication registerForRemoteNotificationTypes:]](https://developer.apple.com/documentation/appkit/nsapplication/1428476-registerforremotenotifications)Added [-[NSApplication unregisterForRemoteNotifications]](https://developer.apple.com/documentation/appkit/nsapplication/1428747-unregisterforremotenotifications)Added [-[NSApplicationDelegate application:didDecodeRestorableState:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428693-application)Added [-[NSApplicationDelegate application:didFailToRegisterForRemoteNotificationsWithError:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428554-application)Added [-[NSApplicationDelegate application:didReceiveRemoteNotification:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428430-application)Added [-[NSApplicationDelegate application:didRegisterForRemoteNotificationsWithDeviceToken:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428766-application)Added [-[NSApplicationDelegate application:willEncodeRestorableState:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428400-application)Added [#def NSAppKitVersionNumber10_6](https://developer.apple.com/documentation/appkit/nsappkitversionnumber10_6)Added NSApplication(NSRemoteNotifications)Added NSApplication(NSRestorableUserInterface)Added [NSApplicationLaunchIsDefaultLaunchKey](https://developer.apple.com/documentation/appkit/nsapplicationlaunchisdefaultlaunchkey)Added [NSApplicationLaunchRemoteNotificationKey](https://developer.apple.com/documentation/appkit/nsapplicationlaunchremotenotificationkey)Added [NSApplicationPresentationAutoHideToolbar](https://developer.apple.com/documentation/appkit/nsapplicationpresentationoptions/nsapplicationpresentationautohidetoolbar)Added [NSApplicationPresentationFullScreen](https://developer.apple.com/documentation/appkit/nsapplication/presentationoptions/1428685-fullscreen)Added [NSRemoteNotificationType](https://developer.apple.com/documentation/appkit/nsremotenotificationtype)Added [NSRemoteNotificationTypeBadge](https://developer.apple.com/documentation/appkit/nsapplication/remotenotificationtype/1428404-badge)Added [NSRemoteNotificationTypeNone](https://developer.apple.com/documentation/appkit/nsremotenotificationtype/nsremotenotificationtypenone)Modified [-[NSApplication beginModalSessionForWindow:relativeToWindow:]](https://developer.apple.com/documentation/appkit/nsapplication/1428604-beginmodalsessionforwindow)

|  | Declaration |
| --- | --- |
| From | - (NSModalSession)beginModalSessionForWindow:(NSWindow \*)theWindow relativeToWindow:(NSWindow \*)docWindow |
| To | - (NSModalSession)beginModalSessionForWindow:(NSWindow \*)theWindow relativeToWindow:(NSWindow \*)__AVAILABILITY_INTERNAL__MAC_10_0_DEP__MAC_10_0 |

Modified [-[NSApplication runModalForWindow:relativeToWindow:]](https://developer.apple.com/documentation/appkit/nsapplication/1428777-runmodalforwindow)

|  | Declaration |
| --- | --- |
| From | - (NSInteger)runModalForWindow:(NSWindow \*)theWindow relativeToWindow:(NSWindow \*)docWindow |
| To | - (NSInteger)runModalForWindow:(NSWindow \*)theWindow relativeToWindow:(NSWindow \*)__AVAILABILITY_INTERNAL__MAC_10_0_DEP__MAC_10_0 |

NSAttributedString.hAdded [NSTextLayoutSectionOrientation](https://developer.apple.com/documentation/foundation/nsattributedstring/textlayoutsectionkey/1533613-orientation)Added [NSTextLayoutSectionRange](https://developer.apple.com/documentation/appkit/nstextlayoutsectionrange)Added [NSTextLayoutSectionsAttribute](https://developer.apple.com/documentation/appkit/nstextlayoutsectionsattribute)Added [NSVerticalGlyphFormAttributeName](https://developer.apple.com/documentation/appkit/nsverticalglyphformattributename)NSBezierPath.hModified [-[NSBezierPath cachesBezierPath]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520706-cachesbezierpath)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | Both | i386,ppc,x86_64 |
| To | _Unknown_ | Unknown |

Modified [-[NSBezierPath setCachesBezierPath:]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520702-setcachesbezierpath)

|  | Declaration |
| --- | --- |
| From | - (void)setCachesBezierPath:(BOOL)flag |
| To | - (void)setCachesBezierPath:(BOOL)__AVAILABILITY_INTERNAL__MAC_10_0_DEP__MAC_10_0 |

NSButtonCell.hAdded [NSInlineBezelStyle](https://developer.apple.com/documentation/appkit/nsinlinebezelstyle)NSCell.hAdded [-[NSCell draggingImageComponentsWithFrame:inView:]](https://developer.apple.com/documentation/appkit/nscell/1532987-draggingimagecomponentswithframe)Added [-[NSCell drawFocusRingMaskWithFrame:inView:]](https://developer.apple.com/documentation/appkit/nscell/1524608-drawfocusringmask)Added [-[NSCell focusRingMaskBoundsForFrame:inView:]](https://developer.apple.com/documentation/appkit/nscell/1534929-focusringmaskbounds)Modified [-[NSCell setFloatingPointFormat:left:right:]](https://developer.apple.com/documentation/appkit/nscell/1560888-setfloatingpointformat)

|  | Declaration |
| --- | --- |
| From | - (void)setFloatingPointFormat:(BOOL)autoRange left:(NSUInteger)leftDigits right:(NSUInteger)rightDigits |
| To | - (void)setFloatingPointFormat:(BOOL)autoRange left:(NSUInteger)leftDigits right:(NSUInteger)__AVAILABILITY_INTERNAL__MAC_10_0_DEP__MAC_10_0 |

Modified [-[NSCell setEntryType:]](https://developer.apple.com/documentation/appkit/nscell/1560876-setentrytype)

|  | Declaration |
| --- | --- |
| From | - (void)setEntryType:(NSInteger)aType |
| To | - (void)setEntryType:(NSInteger)__AVAILABILITY_INTERNAL__MAC_10_0_DEP__MAC_10_0 |

Modified [-[NSCell isEntryAcceptable:]](https://developer.apple.com/documentation/appkit/nscell/1560879-isentryacceptable)

|  | Deprecation | Declaration |
| --- | --- | --- |
| From | _none_ | - (BOOL)isEntryAcceptable:(NSString \*)aString |
| To | OS X v10.0 | - (BOOL)isEntryAcceptable:(NSString \*)__AVAILABILITY_INTERNAL__MAC_10_0_DEP__MAC_10_0 |

Modified [-[NSCell entryType]](https://developer.apple.com/documentation/appkit/nscell/1560897-entrytype)

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | Both | i386,ppc,x86_64 |
| To | _Unknown_ | Unknown |

Modified [NSCell](https://developer.apple.com/documentation/appkit/nscell)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCoding, NSCopying, NSUserInterfaceItemIdentification |

NSCollectionView.hRemoved [-[NSCollectionViewItem collectionView]](https://developer.apple.com/documentation/appkit/nscollectionviewitem/1528221-collectionview)Removed [-[NSCollectionViewItem isSelected]](https://developer.apple.com/documentation/appkit/nscollectionviewitem/1528214-selected)Removed [-[NSCollectionViewItem setSelected:]](https://developer.apple.com/documentation/appkit/nscollectionviewitem/1528214-selected)Added [-[NSCollectionView frameForItemAtIndex:withNumberOfItems:]](https://developer.apple.com/documentation/appkit/nscollectionview/1528209-frameforitem)Added [-[NSCollectionViewDelegate collectionView:draggingSession:endedAtPoint:dragOperation:]](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/1528224-collectionview)Added [-[NSCollectionViewDelegate collectionView:draggingSession:willBeginAtPoint:forItemsAtIndexes:]](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/1524615-collectionview)Added [-[NSCollectionViewDelegate collectionView:pasteboardWriterForItemAtIndex:]](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/1528257-collectionview)Added [-[NSCollectionViewDelegate collectionView:updateDraggingItemsForDrag:]](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/1526881-collectionview)Added [NSCollectionViewItem.collectionView](https://developer.apple.com/documentation/appkit/nscollectionviewitem/1528221-collectionview)Added [NSCollectionViewItem.draggingImageComponents](https://developer.apple.com/documentation/appkit/nscollectionviewitem/1528303-draggingimagecomponents)Added [NSCollectionViewItem.imageView](https://developer.apple.com/documentation/appkit/nscollectionviewitem/1525366-imageview)Added [NSCollectionViewItem.selected](https://developer.apple.com/documentation/appkit/nscollectionviewitem/1528214-selected)Added [NSCollectionViewItem.textField](https://developer.apple.com/documentation/appkit/nscollectionviewitem/1527126-textfield)Modified [NSCollectionView](https://developer.apple.com/documentation/appkit/nscollectionview)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSDraggingDestination, NSDraggingSource |

NSColor.hAdded [+[NSColor colorWithGenericGamma22White:alpha:]](https://developer.apple.com/documentation/appkit/nscolor/1525670-init)Added [+[NSColor colorWithSRGBRed:green:blue:alpha:]](https://developer.apple.com/documentation/appkit/nscolor/1532666-colorwithsrgbred)NSControl.hModified [-[NSControl setFloatingPointFormat:left:right:]](https://developer.apple.com/documentation/appkit/nscontrol/1428931-setfloatingpointformat)

|  | Declaration |
| --- | --- |
| From | - (void)setFloatingPointFormat:(BOOL)autoRange left:(NSUInteger)leftDigits right:(NSUInteger)rightDigits |
| To | - (void)setFloatingPointFormat:(BOOL)autoRange left:(NSUInteger)leftDigits right:(NSUInteger)__AVAILABILITY_INTERNAL__MAC_10_0_DEP__MAC_10_0 |

NSCursor.hAdded [+[NSCursor IBeamCursorForVerticalLayout]](https://developer.apple.com/documentation/appkit/nscursor/1525182-ibeamcursorforverticallayout)NSDocument.hAdded [-[NSDocument autosaveWithImplicitCancellability:completionHandler:]](https://developer.apple.com/documentation/appkit/nsdocument/1515096-autosave)Added [+[NSDocument autosavesInPlace]](https://developer.apple.com/documentation/appkit/nsdocument/1515106-autosavesinplace)Added [-[NSDocument autosavingIsImplicitlyCancellable]](https://developer.apple.com/documentation/appkit/nsdocument/1515149-autosavingisimplicitlycancellabl)Added [-[NSDocument canAsynchronouslyWriteToURL:ofType:forSaveOperation:]](https://developer.apple.com/documentation/appkit/nsdocument/1515177-canasynchronouslywrite)Added [-[NSDocument changeCountTokenForSaveOperation:]](https://developer.apple.com/documentation/appkit/nsdocument/1515129-changecounttokenforsaveoperation)Added [-[NSDocument checkAutosavingSafetyAndReturnError:]](https://developer.apple.com/documentation/appkit/nsdocument/1515061-checkautosavingsafety)Added [-[NSDocument continueActivityUsingBlock:]](https://developer.apple.com/documentation/appkit/nsdocument/1515151-continueactivityusingblock)Added [-[NSDocument continueAsynchronousWorkOnMainThreadUsingBlock:]](https://developer.apple.com/documentation/appkit/nsdocument/1515069-continueasynchronousworkonmainth)Added [-[NSDocument duplicateAndReturnError:]](https://developer.apple.com/documentation/appkit/nsdocument/1515201-duplicateandreturnerror)Added [-[NSDocument duplicateDocument:]](https://developer.apple.com/documentation/appkit/nsdocument/1515226-duplicatedocument)Added [-[NSDocument duplicateDocumentWithDelegate:didDuplicateSelector:contextInfo:]](https://developer.apple.com/documentation/appkit/nsdocument/1515133-duplicatedocumentwithdelegate)Added [-[NSDocument isEntireFileLoaded]](https://developer.apple.com/documentation/appkit/nsdocument/1515053-isentirefileloaded)Added [-[NSDocument isInViewingMode]](https://developer.apple.com/documentation/appkit/nsdocument/1515086-inviewingmode)Added [-[NSDocument performActivityWithSynchronousWaiting:usingBlock:]](https://developer.apple.com/documentation/appkit/nsdocument/1515066-performactivitywithsynchronouswa)Added [-[NSDocument performAsynchronousFileAccessUsingBlock:]](https://developer.apple.com/documentation/appkit/nsdocument/1515124-performasynchronousfileaccessusi)Added [-[NSDocument performSynchronousFileAccessUsingBlock:]](https://developer.apple.com/documentation/appkit/nsdocument/1515227-performsynchronousfileaccessusin)Added [+[NSDocument preservesVersions]](https://developer.apple.com/documentation/appkit/nsdocument/1515114-preservesversions)Added [-[NSDocument saveToURL:ofType:forSaveOperation:completionHandler:]](https://developer.apple.com/documentation/appkit/nsdocument/1515178-savetourl)Added [-[NSDocument scheduleAutosaving]](https://developer.apple.com/documentation/appkit/nsdocument/1515119-scheduleautosaving)Added [-[NSDocument setDisplayName:]](https://developer.apple.com/documentation/appkit/nsdocument/1515143-setdisplayname)Added [-[NSDocument unblockUserInteraction]](https://developer.apple.com/documentation/appkit/nsdocument/1515238-unblockuserinteraction)Added [-[NSDocument updateChangeCountWithToken:forSaveOperation:]](https://developer.apple.com/documentation/appkit/nsdocument/1515083-updatechangecountwithtoken)Added [-[NSDocument willNotPresentError:]](https://developer.apple.com/documentation/appkit/nsdocument/1515188-willnotpresenterror)Added [NSAutosaveElsewhereOperation](https://developer.apple.com/documentation/appkit/nsdocument/saveoperationtype/autosaveelsewhereoperation)Added [NSAutosaveInPlaceOperation](https://developer.apple.com/documentation/appkit/nsdocument/saveoperationtype/autosaveinplaceoperation)Modified [-[NSDocument setAutosavedContentsFileURL:]](https://developer.apple.com/documentation/appkit/nsdocument/1515232-autosavedcontentsfileurl)

|  | Declaration |
| --- | --- |
| From | - (void)setAutosavedContentsFileURL:(NSURL \*)absoluteURL |
| To | - (void)setAutosavedContentsFileURL:(NSURL \*)url |

Modified [-[NSDocument revertToContentsOfURL:ofType:error:]](https://developer.apple.com/documentation/appkit/nsdocument/1515122-reverttocontentsofurl)

|  | Declaration |
| --- | --- |
| From | - (BOOL)revertToContentsOfURL:(NSURL \*)absoluteURL ofType:(NSString \*)typeName error:(NSError \*\*)outError |
| To | - (BOOL)revertToContentsOfURL:(NSURL \*)url ofType:(NSString \*)typeName error:(NSError \*\*)outError |

Modified [-[NSDocument saveToURL:ofType:forSaveOperation:delegate:didSaveSelector:contextInfo:]](https://developer.apple.com/documentation/appkit/nsdocument/1515148-savetourl)

|  | Declaration |
| --- | --- |
| From | - (void)saveToURL:(NSURL \*)absoluteURL ofType:(NSString \*)typeName forSaveOperation:(NSSaveOperationType)saveOperation delegate:(id)delegate didSaveSelector:(SEL)didSaveSelector contextInfo:(void \*)contextInfo |
| To | - (void)saveToURL:(NSURL \*)url ofType:(NSString \*)typeName forSaveOperation:(NSSaveOperationType)saveOperation delegate:(id)delegate didSaveSelector:(SEL)didSaveSelector contextInfo:(void \*)contextInfo |

Modified [-[NSDocument initForURL:withContentsOfURL:ofType:error:]](https://developer.apple.com/documentation/appkit/nsdocument/1515041-init)

|  | Declaration |
| --- | --- |
| From | - (id)initForURL:(NSURL \*)absoluteDocumentURL withContentsOfURL:(NSURL \*)absoluteDocumentContentsURL ofType:(NSString \*)typeName error:(NSError \*\*)outError |
| To | - (id)initForURL:(NSURL \*)urlOrNil withContentsOfURL:(NSURL \*)contentsURL ofType:(NSString \*)typeName error:(NSError \*\*)outError |

Modified [-[NSDocument fileAttributesToWriteToURL:ofType:forSaveOperation:originalContentsURL:error:]](https://developer.apple.com/documentation/appkit/nsdocument/1515062-fileattributestowrite)

|  | Declaration |
| --- | --- |
| From | - (NSDictionary \*)fileAttributesToWriteToURL:(NSURL \*)absoluteURL ofType:(NSString \*)typeName forSaveOperation:(NSSaveOperationType)saveOperation originalContentsURL:(NSURL \*)absoluteOriginalContentsURL error:(NSError \*\*)outError |
| To | - (NSDictionary \*)fileAttributesToWriteToURL:(NSURL \*)url ofType:(NSString \*)typeName forSaveOperation:(NSSaveOperationType)saveOperation originalContentsURL:(NSURL \*)absoluteOriginalContentsURL error:(NSError \*\*)outError |

Modified [-[NSDocument writeSafelyToURL:ofType:forSaveOperation:error:]](https://developer.apple.com/documentation/appkit/nsdocument/1515150-writesafely)

|  | Declaration |
| --- | --- |
| From | - (BOOL)writeSafelyToURL:(NSURL \*)absoluteURL ofType:(NSString \*)typeName forSaveOperation:(NSSaveOperationType)saveOperation error:(NSError \*\*)outError |
| To | - (BOOL)writeSafelyToURL:(NSURL \*)url ofType:(NSString \*)typeName forSaveOperation:(NSSaveOperationType)saveOperation error:(NSError \*\*)outError |

Modified [-[NSDocument setFileURL:]](https://developer.apple.com/documentation/appkit/nsdocument/1515038-fileurl)

|  | Declaration |
| --- | --- |
| From | - (void)setFileURL:(NSURL \*)absoluteURL |
| To | - (void)setFileURL:(NSURL \*)url |

Modified [-[NSDocument writeToURL:ofType:forSaveOperation:originalContentsURL:error:]](https://developer.apple.com/documentation/appkit/nsdocument/1515203-write)

|  | Declaration |
| --- | --- |
| From | - (BOOL)writeToURL:(NSURL \*)absoluteURL ofType:(NSString \*)typeName forSaveOperation:(NSSaveOperationType)saveOperation originalContentsURL:(NSURL \*)absoluteOriginalContentsURL error:(NSError \*\*)outError |
| To | - (BOOL)writeToURL:(NSURL \*)url ofType:(NSString \*)typeName forSaveOperation:(NSSaveOperationType)saveOperation originalContentsURL:(NSURL \*)absoluteOriginalContentsURL error:(NSError \*\*)outError |

Modified [-[NSDocument saveToURL:ofType:forSaveOperation:error:]](https://developer.apple.com/documentation/appkit/nsdocument/1515187-savetourl)

|  | Deprecation | Declaration |
| --- | --- | --- |
| From | _none_ | - (BOOL)saveToURL:(NSURL \*)absoluteURL ofType:(NSString \*)typeName forSaveOperation:(NSSaveOperationType)saveOperation error:(NSError \*\*)outError |
| To | OS X v10.7 | - (BOOL)saveToURL:(NSURL \*)url ofType:(NSString \*)typeName forSaveOperation:(NSSaveOperationType)saveOperation error:(NSError \*\*)outError |

Modified [-[NSDocument initWithContentsOfURL:ofType:]](https://developer.apple.com/documentation/appkit/nsdocument/1515101-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | - (id)initWithContentsOfURL:(NSURL \*)absoluteURL ofType:(NSString \*)typeName |
| To | - (id)initWithContentsOfURL:(NSURL \*)url ofType:(NSString \*)typeName |

Modified [-[NSDocument initWithContentsOfURL:ofType:error:]](https://developer.apple.com/documentation/appkit/nsdocument/1515097-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithContentsOfURL:(NSURL \*)absoluteURL ofType:(NSString \*)typeName error:(NSError \*\*)outError |
| To | - (id)initWithContentsOfURL:(NSURL \*)url ofType:(NSString \*)typeName error:(NSError \*\*)outError |

Modified [-[NSDocument writeToURL:ofType:error:]](https://developer.apple.com/documentation/appkit/nsdocument/1515076-write)

|  | Declaration |
| --- | --- |
| From | - (BOOL)writeToURL:(NSURL \*)absoluteURL ofType:(NSString \*)typeName error:(NSError \*\*)outError |
| To | - (BOOL)writeToURL:(NSURL \*)url ofType:(NSString \*)typeName error:(NSError \*\*)outError |

Modified [-[NSDocument readFromURL:ofType:error:]](https://developer.apple.com/documentation/appkit/nsdocument/1515144-readfromurl)

|  | Declaration |
| --- | --- |
| From | - (BOOL)readFromURL:(NSURL \*)absoluteURL ofType:(NSString \*)typeName error:(NSError \*\*)outError |
| To | - (BOOL)readFromURL:(NSURL \*)url ofType:(NSString \*)typeName error:(NSError \*\*)outError |

Modified [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument)

|  | Protocols |
| --- | --- |
| From | NSUserInterfaceValidations |
| To | NSFilePresenter, NSUserInterfaceValidations |

NSDocumentController.hAdded [-[NSDocumentController duplicateDocumentWithContentsOfURL:copying:displayName:error:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514982-duplicatedocumentwithcontentsofu)Added [-[NSDocumentController openDocumentWithContentsOfURL:display:completionHandler:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514992-opendocument)Added [-[NSDocumentController reopenDocumentForURL:withContentsOfURL:display:completionHandler:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514935-reopendocumentforurl)Modified [-[NSDocumentController makeDocumentForURL:withContentsOfURL:ofType:error:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514930-makedocument)

|  | Declaration |
| --- | --- |
| From | - (id)makeDocumentForURL:(NSURL \*)absoluteDocumentURL withContentsOfURL:(NSURL \*)absoluteDocumentContentsURL ofType:(NSString \*)typeName error:(NSError \*\*)outError |
| To | - (id)makeDocumentForURL:(NSURL \*)urlOrNil withContentsOfURL:(NSURL \*)contentsURL ofType:(NSString \*)typeName error:(NSError \*\*)outError |

Modified [-[NSDocumentController typeForContentsOfURL:error:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514946-typeforcontentsofurl)

|  | Declaration |
| --- | --- |
| From | - (NSString \*)typeForContentsOfURL:(NSURL \*)inAbsoluteURL error:(NSError \*\*)outError |
| To | - (NSString \*)typeForContentsOfURL:(NSURL \*)url error:(NSError \*\*)outError |

Modified [-[NSDocumentController noteNewRecentDocumentURL:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514967-notenewrecentdocumenturl)

|  | Declaration |
| --- | --- |
| From | - (void)noteNewRecentDocumentURL:(NSURL \*)absoluteURL |
| To | - (void)noteNewRecentDocumentURL:(NSURL \*)url |

Modified [-[NSDocumentController openDocumentWithContentsOfURL:display:error:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514951-opendocumentwithcontentsofurl)

|  | Deprecation | Declaration |
| --- | --- | --- |
| From | _none_ | - (id)openDocumentWithContentsOfURL:(NSURL \*)absoluteURL display:(BOOL)displayDocument error:(NSError \*\*)outError |
| To | OS X v10.7 | - (id)openDocumentWithContentsOfURL:(NSURL \*)url display:(BOOL)displayDocument error:(NSError \*\*)outError |

Modified [-[NSDocumentController reopenDocumentForURL:withContentsOfURL:error:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514979-reopendocumentforurl)

|  | Deprecation | Declaration |
| --- | --- | --- |
| From | _none_ | - (BOOL)reopenDocumentForURL:(NSURL \*)absoluteDocumentURL withContentsOfURL:(NSURL \*)absoluteDocumentContentsURL error:(NSError \*\*)outError |
| To | OS X v10.7 | - (BOOL)reopenDocumentForURL:(NSURL \*)url withContentsOfURL:(NSURL \*)contentsURL error:(NSError \*\*)outError |

Modified [-[NSDocumentController documentForURL:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514939-documentforurl)

|  | Declaration |
| --- | --- |
| From | - (id)documentForURL:(NSURL \*)absoluteURL |
| To | - (id)documentForURL:(NSURL \*)url |

Modified [-[NSDocumentController makeDocumentWithContentsOfURL:ofType:error:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514949-makedocument)

|  | Declaration |
| --- | --- |
| From | - (id)makeDocumentWithContentsOfURL:(NSURL \*)absoluteURL ofType:(NSString \*)typeName error:(NSError \*\*)outError |
| To | - (id)makeDocumentWithContentsOfURL:(NSURL \*)url ofType:(NSString \*)typeName error:(NSError \*\*)outError |

NSDragging.hRemoved -[NSObject concludeDragOperation:]Removed -[NSObject draggingEnded:]Removed -[NSObject draggingEntered:]Removed -[NSObject draggingExited:]Removed -[NSObject draggingUpdated:]Removed -[NSObject performDragOperation:]Removed -[NSObject prepareForDragOperation:]Removed -[NSObject wantsPeriodicDraggingUpdates]Removed NSObject(NSDraggingDestination)Removed NSObject(NSDraggingSource)Added [NSDraggingDestination](https://developer.apple.com/documentation/appkit/nsdraggingdestination)Added [-[NSDraggingDestination concludeDragOperation:]](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1416010-concludedragoperation)Added [-[NSDraggingDestination draggingEnded:]](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1416096-draggingended)Added [-[NSDraggingDestination draggingEntered:]](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1416019-draggingentered)Added [-[NSDraggingDestination draggingExited:]](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1416056-draggingexited)Added [-[NSDraggingDestination draggingUpdated:]](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1415998-draggingupdated)Added [-[NSDraggingDestination performDragOperation:]](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1415970-performdragoperation)Added [-[NSDraggingDestination prepareForDragOperation:]](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1416066-preparefordragoperation)Added [-[NSDraggingDestination updateDraggingItemsForDrag:]](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1416050-updatedraggingitemsfordrag)Added [-[NSDraggingDestination wantsPeriodicDraggingUpdates]](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1416049-wantsperiodicdraggingupdates)Added [NSDraggingInfo.animatesToDestination](https://developer.apple.com/documentation/appkit/nsdragginginfo/1416098-animatestodestination)Added [NSDraggingInfo.draggingFormation](https://developer.apple.com/documentation/appkit/nsdragginginfo/1416041-draggingformation)Added [-[NSDraggingInfo enumerateDraggingItemsWithOptions:forView:classes:searchOptions:usingBlock:]](https://developer.apple.com/documentation/appkit/nsdragginginfo/1416074-enumeratedraggingitemswithoption)Added [NSDraggingInfo.numberOfValidItemsForDrop](https://developer.apple.com/documentation/appkit/nsdragginginfo/1416033-numberofvaliditemsfordrop)Added [NSDraggingSource](https://developer.apple.com/documentation/appkit/nsdraggingsource)Added [-[NSDraggingSource draggingSession:endedAtPoint:operation:]](https://developer.apple.com/documentation/appkit/nsdraggingsource/1416017-draggingsession)Added [-[NSDraggingSource draggingSession:movedToPoint:]](https://developer.apple.com/documentation/appkit/nsdraggingsource/1416079-draggingsession)Added [-[NSDraggingSource draggingSession:sourceOperationMaskForDraggingContext:]](https://developer.apple.com/documentation/appkit/nsdraggingsource/1416000-draggingsession)Added [-[NSDraggingSource draggingSession:willBeginAtPoint:]](https://developer.apple.com/documentation/appkit/nsdraggingsource/1415960-draggingsession)Added [-[NSDraggingSource ignoreModifierKeysForDraggingSession:]](https://developer.apple.com/documentation/appkit/nsdraggingsource/1415974-ignoremodifierkeys)Added [NSDraggingContext](https://developer.apple.com/documentation/appkit/nsdraggingcontext)Added [NSDraggingContextOutsideApplication](https://developer.apple.com/documentation/appkit/nsdraggingcontext/nsdraggingcontextoutsideapplication)Added [NSDraggingContextWithinApplication](https://developer.apple.com/documentation/appkit/nsdraggingcontext/withinapplication)Added [NSDraggingFormation](https://developer.apple.com/documentation/appkit/nsdraggingformation)Added [NSDraggingFormationDefault](https://developer.apple.com/documentation/appkit/nsdraggingformation/default)Added [NSDraggingFormationList](https://developer.apple.com/documentation/appkit/nsdraggingformation/nsdraggingformationlist)Added [NSDraggingFormationNone](https://developer.apple.com/documentation/appkit/nsdraggingformation/none)Added [NSDraggingFormationPile](https://developer.apple.com/documentation/appkit/nsdraggingformation/pile)Added [NSDraggingFormationStack](https://developer.apple.com/documentation/appkit/nsdraggingformation/stack)Added [NSDraggingItemEnumerationClearNonenumeratedImages](https://developer.apple.com/documentation/appkit/nsdraggingitemenumerationoptions/1416023-clearnonenumeratedimages)Added [NSDraggingItemEnumerationConcurrent](https://developer.apple.com/documentation/appkit/nsdraggingitemenumerationoptions/nsdraggingitemenumerationconcurrent)Added [NSDraggingItemEnumerationOptions](https://developer.apple.com/documentation/appkit/nsdraggingitemenumerationoptions)Modified [-[NSObject draggedImage:endedAt:operation:]](https://developer.apple.com/documentation/objectivec/nsobject/1416054-draggedimage)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [-[NSObject draggingSourceOperationMaskForLocal:]](https://developer.apple.com/documentation/objectivec/nsobject/1415984-draggingsourceoperationmaskforlo)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [-[NSObject namesOfPromisedFilesDroppedAtDestination:]](https://developer.apple.com/documentation/objectivec/nsobject/1416082-namesofpromisedfilesdroppedatdes)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [NSDraggingInfo](https://developer.apple.com/documentation/appkit/nsdragginginfo)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSObject |

Modified [-[NSObject draggedImage:beganAt:]](https://developer.apple.com/documentation/objectivec/nsobject/1415986-draggedimage)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [-[NSObject ignoreModifierKeysWhileDragging]](https://developer.apple.com/documentation/objectivec/nsobject/1416100-ignoremodifierkeyswhiledragging)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [-[NSObject draggedImage:movedTo:]](https://developer.apple.com/documentation/objectivec/nsobject/1416008-draggedimage)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

NSDraggingItem.hAdded [NSDraggingImageComponent](https://developer.apple.com/documentation/appkit/nsdraggingimagecomponent)Added [NSDraggingImageComponent.contents](https://developer.apple.com/documentation/appkit/nsdraggingimagecomponent/1529426-contents)Added [+[NSDraggingImageComponent draggingImageComponentWithKey:]](https://developer.apple.com/documentation/appkit/nsdraggingimagecomponent/1557913-draggingimagecomponentwithkey)Added [NSDraggingImageComponent.frame](https://developer.apple.com/documentation/appkit/nsdraggingimagecomponent/1535507-frame)Added [-[NSDraggingImageComponent initWithKey:]](https://developer.apple.com/documentation/appkit/nsdraggingimagecomponent/1534187-initwithkey)Added [NSDraggingImageComponent.key](https://developer.apple.com/documentation/appkit/nsdraggingimagecomponent/1535631-key)Added [NSDraggingItem](https://developer.apple.com/documentation/appkit/nsdraggingitem)Added [NSDraggingItem.draggingFrame](https://developer.apple.com/documentation/appkit/nsdraggingitem/1528559-draggingframe)Added [NSDraggingItem.imageComponents](https://developer.apple.com/documentation/appkit/nsdraggingitem/1524302-imagecomponents)Added [NSDraggingItem.imageComponentsProvider](https://developer.apple.com/documentation/appkit/nsdraggingitem/1535607-imagecomponentsprovider)Added [-[NSDraggingItem initWithPasteboardWriter:]](https://developer.apple.com/documentation/appkit/nsdraggingitem/1535417-init)Added [NSDraggingItem.item](https://developer.apple.com/documentation/appkit/nsdraggingitem/1533258-item)Added [-[NSDraggingItem setDraggingFrame:contents:]](https://developer.apple.com/documentation/appkit/nsdraggingitem/1528746-setdraggingframe)Added [NSDraggingImageComponentIconKey](https://developer.apple.com/documentation/appkit/nsdraggingitem/imagecomponentkey/1527587-icon)Added [NSDraggingImageComponentLabelKey](https://developer.apple.com/documentation/appkit/nsdraggingimagecomponentlabelkey)NSDraggingSession.hAdded [NSDraggingSession](https://developer.apple.com/documentation/appkit/nsdraggingsession)Added [NSDraggingSession.animatesToStartingPositionsOnCancelOrFail](https://developer.apple.com/documentation/appkit/nsdraggingsession/1531277-animatestostartingpositionsoncan)Added [NSDraggingSession.draggingFormation](https://developer.apple.com/documentation/appkit/nsdraggingsession/1524544-draggingformation)Added [NSDraggingSession.draggingLeaderIndex](https://developer.apple.com/documentation/appkit/nsdraggingsession/1533729-draggingleaderindex)Added [NSDraggingSession.draggingLocation](https://developer.apple.com/documentation/appkit/nsdraggingsession/1529395-dragginglocation)Added [NSDraggingSession.draggingPasteboard](https://developer.apple.com/documentation/appkit/nsdraggingsession/1534103-draggingpasteboard)Added [NSDraggingSession.draggingSequenceNumber](https://developer.apple.com/documentation/appkit/nsdraggingsession/1533229-draggingsequencenumber)Added [-[NSDraggingSession enumerateDraggingItemsWithOptions:forView:classes:searchOptions:usingBlock:]](https://developer.apple.com/documentation/appkit/nsdraggingsession/1532445-enumeratedraggingitems)NSEvent.hAdded [-[NSEvent hasPreciseScrollingDeltas]](https://developer.apple.com/documentation/appkit/nsevent/1525758-hasprecisescrollingdeltas)Added [-[NSEvent isDirectionInvertedFromDevice]](https://developer.apple.com/documentation/appkit/nsevent/1525151-isdirectioninvertedfromdevice)Added +[NSEvent isSwipeTrackingFromScrollEventsEnabled]Added [-[NSEvent momentumPhase]](https://developer.apple.com/documentation/appkit/nsevent/1525439-momentumphase)Added [-[NSEvent phase]](https://developer.apple.com/documentation/appkit/nsevent/1533550-phase)Added [-[NSEvent scrollingDeltaX]](https://developer.apple.com/documentation/appkit/nsevent/1524505-scrollingdeltax)Added [-[NSEvent scrollingDeltaY]](https://developer.apple.com/documentation/appkit/nsevent/1535387-scrollingdeltay)Added [-[NSEvent trackSwipeEventWithOptions:dampenAmountThresholdMin:max:usingHandler:]](https://developer.apple.com/documentation/appkit/nsevent/1533300-trackswipeevent)Added [NSEventGestureAxis](https://developer.apple.com/documentation/appkit/nsevent/gestureaxis)Added [NSEventGestureAxisHorizontal](https://developer.apple.com/documentation/appkit/nseventgestureaxis/nseventgestureaxishorizontal)Added [NSEventGestureAxisNone](https://developer.apple.com/documentation/appkit/nseventgestureaxis/nseventgestureaxisnone)Added [NSEventGestureAxisVertical](https://developer.apple.com/documentation/appkit/nsevent/gestureaxis/vertical)Added [NSEventPhase](https://developer.apple.com/documentation/appkit/nsevent/phase)Added [NSEventPhaseBegan](https://developer.apple.com/documentation/appkit/nseventphase/nseventphasebegan)Added [NSEventPhaseCancelled](https://developer.apple.com/documentation/appkit/nsevent/phase/1534443-cancelled)Added [NSEventPhaseChanged](https://developer.apple.com/documentation/appkit/nsevent/phase/1534418-changed)Added [NSEventPhaseEnded](https://developer.apple.com/documentation/appkit/nsevent/phase/1529162-ended)Added [NSEventPhaseNone](https://developer.apple.com/documentation/appkit/nseventphase/nseventphasenone)Added [NSEventPhaseStationary](https://developer.apple.com/documentation/appkit/nsevent/phase/1530513-stationary)Added [NSEventSwipeTrackingClampGestureAmount](https://developer.apple.com/documentation/appkit/nseventswipetrackingoptions/nseventswipetrackingclampgestureamount)Added [NSEventSwipeTrackingLockDirection](https://developer.apple.com/documentation/appkit/nsevent/swipetrackingoptions/1525083-lockdirection)Added [NSEventSwipeTrackingOptions](https://developer.apple.com/documentation/appkit/nsevent/swipetrackingoptions)NSFileWrapper.hRemoved [NSFileWrapper](https://developer.apple.com/documentation/foundation/filewrapper)Removed [-[NSFileWrapper addFileWithPath:]](https://developer.apple.com/documentation/foundation/filewrapper/1417211-addfile)Removed [-[NSFileWrapper addFileWrapper:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1415067-addfilewrapper)Removed [-[NSFileWrapper addRegularFileWithContents:preferredFilename:]](https://developer.apple.com/documentation/foundation/filewrapper/1418374-addregularfile)Removed [-[NSFileWrapper addSymbolicLinkWithDestination:preferredFilename:]](https://developer.apple.com/documentation/foundation/filewrapper/1414604-addsymboliclink)Removed [-[NSFileWrapper fileAttributes]](https://developer.apple.com/documentation/foundation/filewrapper/1412745-fileattributes)Removed [-[NSFileWrapper fileWrappers]](https://developer.apple.com/documentation/foundation/filewrapper/1409437-filewrappers)Removed [-[NSFileWrapper filename]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1416684-filename)Removed [-[NSFileWrapper initDirectoryWithFileWrappers:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1415121-initdirectorywithfilewrappers)Removed [-[NSFileWrapper initRegularFileWithContents:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1409508-initregularfilewithcontents)Removed [-[NSFileWrapper initSymbolicLinkWithDestination:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1411268-initsymboliclinkwithdestination)Removed [-[NSFileWrapper initSymbolicLinkWithDestinationURL:]](https://developer.apple.com/documentation/foundation/filewrapper/1415098-init)Removed [-[NSFileWrapper initWithPath:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1408388-initwithpath)Removed [-[NSFileWrapper initWithSerializedRepresentation:]](https://developer.apple.com/documentation/foundation/filewrapper/1407515-init)Removed [-[NSFileWrapper initWithURL:options:error:]](https://developer.apple.com/documentation/foundation/filewrapper/1415658-init)Removed [-[NSFileWrapper isDirectory]](https://developer.apple.com/documentation/foundation/filewrapper/1409030-isdirectory)Removed [-[NSFileWrapper isRegularFile]](https://developer.apple.com/documentation/foundation/filewrapper/1415680-isregularfile)Removed [-[NSFileWrapper isSymbolicLink]](https://developer.apple.com/documentation/foundation/filewrapper/1408125-issymboliclink)Removed [-[NSFileWrapper keyForFileWrapper:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1407541-keyforfilewrapper)Removed [-[NSFileWrapper matchesContentsOfURL:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1408360-matchescontentsofurl)Removed [-[NSFileWrapper needsToBeUpdatedFromPath:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1407738-needstobeupdatedfrompath)Removed [-[NSFileWrapper preferredFilename]](https://developer.apple.com/documentation/foundation/filewrapper/1409368-preferredfilename)Removed [-[NSFileWrapper readFromURL:options:error:]](https://developer.apple.com/documentation/foundation/filewrapper/1411645-read)Removed [-[NSFileWrapper regularFileContents]](https://developer.apple.com/documentation/foundation/filewrapper/1410178-regularfilecontents)Removed [-[NSFileWrapper removeFileWrapper:]](https://developer.apple.com/documentation/foundation/filewrapper/1417343-removefilewrapper)Removed [-[NSFileWrapper serializedRepresentation]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1412119-serializedrepresentation)Removed [-[NSFileWrapper setFileAttributes:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1412745-fileattributes)Removed [-[NSFileWrapper setFilename:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1416684-filename)Removed [-[NSFileWrapper setPreferredFilename:]](https://developer.apple.com/documentation/foundation/filewrapper/1409368-preferredfilename)Removed [-[NSFileWrapper symbolicLinkDestination]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1418302-symboliclinkdestination)Removed [-[NSFileWrapper symbolicLinkDestinationURL]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1408364-symboliclinkdestinationurl)Removed [-[NSFileWrapper updateFromPath:]](https://developer.apple.com/documentation/foundation/filewrapper/1416300-update)Removed [-[NSFileWrapper writeToFile:atomically:updateFilenames:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1415079-writetofile)Removed [-[NSFileWrapper writeToURL:options:originalContentsURL:error:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1415981-writetourl)Removed NSFileWrapper(NSDeprecated)Removed [NSFileWrapperReadingImmediate](https://developer.apple.com/documentation/foundation/nsfilewrapperreadingoptions/nsfilewrapperreadingimmediate)Removed [NSFileWrapperReadingOptions](https://developer.apple.com/documentation/foundation/filewrapper/readingoptions)Removed [NSFileWrapperReadingWithoutMapping](https://developer.apple.com/documentation/foundation/nsfilewrapperreadingoptions/nsfilewrapperreadingwithoutmapping)Removed [NSFileWrapperWritingAtomic](https://developer.apple.com/documentation/foundation/nsfilewrapperwritingoptions/nsfilewrapperwritingatomic)Removed [NSFileWrapperWritingOptions](https://developer.apple.com/documentation/foundation/nsfilewrapperwritingoptions)Removed [NSFileWrapperWritingWithNameUpdating](https://developer.apple.com/documentation/foundation/filewrapper/writingoptions/1408447-withnameupdating)NSFileWrapperExtensions.hAdded NSFileWrapper(NSExtensions)Modified [-[NSFileWrapper setIcon:]](https://developer.apple.com/documentation/foundation/filewrapper/1413123-icon)

|  | Header |
| --- | --- |
| From | NSFileWrapper.h |
| To | NSFileWrapperExtensions.h |

Modified [-[NSFileWrapper icon]](https://developer.apple.com/documentation/foundation/filewrapper/1413123-icon)

|  | Header |
| --- | --- |
| From | NSFileWrapper.h |
| To | NSFileWrapperExtensions.h |

NSFont.hAdded [-[NSFont isVertical]](https://developer.apple.com/documentation/appkit/nsfont/1534644-vertical)Added [-[NSFont verticalFont]](https://developer.apple.com/documentation/appkit/nsfont/1535152-verticalfont)NSFontCollection.hAdded [NSFontCollection](https://developer.apple.com/documentation/appkit/nsfontcollection)Added [+[NSFontCollection allFontCollectionNames]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497477-allfontcollectionnames)Added [-[NSFontCollection exclusionDescriptors]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497456-exclusiondescriptors)Added [+[NSFontCollection fontCollectionWithAllAvailableDescriptors]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497473-fontcollectionwithallavailablede)Added [+[NSFontCollection fontCollectionWithDescriptors:]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497467-init)Added [+[NSFontCollection fontCollectionWithLocale:]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497481-init)Added [+[NSFontCollection fontCollectionWithName:]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497514-init)Added [+[NSFontCollection fontCollectionWithName:visibility:]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497475-fontcollectionwithname)Added [+[NSFontCollection hideFontCollectionWithName:visibility:error:]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497459-hidefontcollectionwithname)Added [-[NSFontCollection matchingDescriptors]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497523-matchingdescriptors)Added [-[NSFontCollection matchingDescriptorsForFamily:]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497496-matchingdescriptors)Added [-[NSFontCollection matchingDescriptorsForFamily:options:]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497522-matchingdescriptors)Added [-[NSFontCollection matchingDescriptorsWithOptions:]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497510-matchingdescriptors)Added [-[NSFontCollection queryDescriptors]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497441-querydescriptors)Added [+[NSFontCollection renameFontCollectionWithName:visibility:toName:error:]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497521-renamefontcollectionwithname)Added [+[NSFontCollection showFontCollection:withName:visibility:error:]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497512-show)Added [NSMutableFontCollection](https://developer.apple.com/documentation/appkit/nsmutablefontcollection)Added [-[NSMutableFontCollection addQueryForDescriptors:]](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/1497446-addqueryfordescriptors)Added [-[NSMutableFontCollection removeQueryForDescriptors:]](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/1497471-removequery)Added [-[NSMutableFontCollection setExclusionDescriptors:]](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/1497442-exclusiondescriptors)Added [-[NSMutableFontCollection setQueryDescriptors:]](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/1497457-querydescriptors)Added [NSFontCollectionActionKey](https://developer.apple.com/documentation/appkit/nsfontcollectionactionkey)Added [NSFontCollectionAllFonts](https://developer.apple.com/documentation/appkit/nsfontcollection/name/1497444-allfonts)Added [NSFontCollectionDidChangeNotification](https://developer.apple.com/documentation/appkit/nsfontcollectiondidchangenotification)Added [NSFontCollectionDisallowAutoActivationOption](https://developer.apple.com/documentation/appkit/nsfontcollectionmatchingoptionkey/1497494-disallowautoactivationoption)Added [NSFontCollectionFavorites](https://developer.apple.com/documentation/appkit/nsfontcollectionfavorites)Added [NSFontCollectionIncludeDisabledFontsOption](https://developer.apple.com/documentation/appkit/nsfontcollectionmatchingoptionkey/1497508-includedisabledfontsoption)Added [NSFontCollectionNameKey](https://developer.apple.com/documentation/appkit/nsfontcollectionnamekey)Added [NSFontCollectionOldNameKey](https://developer.apple.com/documentation/appkit/nsfontcollection/userinfokey/1497465-oldname)Added [NSFontCollectionRecentlyUsed](https://developer.apple.com/documentation/appkit/nsfontcollection/name/1497463-recentlyused)Added [NSFontCollectionRemoveDuplicatesOption](https://developer.apple.com/documentation/appkit/nsfontcollectionremoveduplicatesoption)Added [NSFontCollectionUser](https://developer.apple.com/documentation/appkit/nsfontcollectionuser)Added [NSFontCollectionVisibility](https://developer.apple.com/documentation/appkit/nsfontcollectionvisibility)Added [NSFontCollectionVisibilityComputer](https://developer.apple.com/documentation/appkit/nsfontcollection/visibility/1497513-computer)Added [NSFontCollectionVisibilityKey](https://developer.apple.com/documentation/appkit/nsfontcollectionvisibilitykey)Added [NSFontCollectionVisibilityProcess](https://developer.apple.com/documentation/appkit/nsfontcollection/visibility/1497499-process)Added [NSFontCollectionVisibilityUser](https://developer.apple.com/documentation/appkit/nsfontcollectionvisibility/nsfontcollectionvisibilityuser)Added [NSFontCollectionWasHidden](https://developer.apple.com/documentation/appkit/nsfontcollectionwashidden)Added [NSFontCollectionWasRenamed](https://developer.apple.com/documentation/appkit/nsfontcollectionwasrenamed)Added [NSFontCollectionWasShown](https://developer.apple.com/documentation/appkit/nsfontcollection/actiontypekey/1497515-shown)NSGraphics.hModified [NSRectFillListWithColors()](https://developer.apple.com/documentation/appkit/1473733-nsrectfilllistwithcolors)

|  | Declaration |
| --- | --- |
| From | void NSRectFillListWithColors ( const NSRect \*rects, NSColor \*\*colors, NSInteger num); |
| To | void NSRectFillListWithColors ( const NSRect \*rects, NSColor \*const \*colors, NSInteger num); |

Modified [NSRectFillListWithColorsUsingOperation()](https://developer.apple.com/documentation/appkit/1473686-nsrectfilllistwithcolorsusingope)

|  | Declaration |
| --- | --- |
| From | void NSRectFillListWithColorsUsingOperation ( const NSRect \*rects, NSColor \*\*colors, NSInteger num, NSCompositingOperation op); |
| To | void NSRectFillListWithColorsUsingOperation ( const NSRect \*rects, NSColor \*const \*colors, NSInteger num, NSCompositingOperation op); |

NSImage.hAdded [-[NSBundle imageForResource:]](https://developer.apple.com/documentation/foundation/nsbundle/1519901-imageforresource)NSKeyValueBinding.hAdded [-[NSObject commitEditingAndReturnError:]](https://developer.apple.com/documentation/objectivec/nsobject/1458181-commiteditingandreturnerror)Added [NSPositioningRectBinding](https://developer.apple.com/documentation/appkit/nsbindingname/1458215-positioningrect)NSLayoutConstraint.hAdded [-[NSControl invalidateIntrinsicContentSizeForCell:]](https://developer.apple.com/documentation/appkit/nscontrol/1526876-invalidateintrinsiccontentsizefo)Added [NSLayoutConstraint](https://developer.apple.com/documentation/uikit/nslayoutconstraint)Added [NSLayoutConstraint.constant](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526928-constant)Added [+[NSLayoutConstraint constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:]](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526954-init)Added [+[NSLayoutConstraint constraintsWithVisualFormat:options:metrics:views:]](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526944-constraints)Added [NSLayoutConstraint.firstAttribute](https://developer.apple.com/documentation/uikit/nslayoutconstraint/1525204-firstattribute)Added [NSLayoutConstraint.firstItem](https://developer.apple.com/documentation/uikit/nslayoutconstraint/1526860-firstitem)Added [NSLayoutConstraint.multiplier](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526920-multiplier)Added [NSLayoutConstraint.priority](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526946-priority)Added [NSLayoutConstraint.relation](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526549-relation)Added [NSLayoutConstraint.secondAttribute](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526941-secondattribute)Added [NSLayoutConstraint.secondItem](https://developer.apple.com/documentation/uikit/nslayoutconstraint/1526868-seconditem)Added [NSLayoutConstraint.shouldBeArchived](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1525647-shouldbearchived)Added [-[NSView addConstraint:]](https://developer.apple.com/documentation/appkit/nsview/1526969-addconstraint)Added [-[NSView addConstraints:]](https://developer.apple.com/documentation/appkit/nsview/1526931-addconstraints)Added [-[NSView alignmentRectForFrame:]](https://developer.apple.com/documentation/appkit/nsview/1526905-alignmentrect)Added [-[NSView alignmentRectInsets]](https://developer.apple.com/documentation/appkit/nsview/1526870-alignmentrectinsets)Added [-[NSView baselineOffsetFromBottom]](https://developer.apple.com/documentation/appkit/nsview/1526949-baselineoffsetfrombottom)Added [-[NSView constraints]](https://developer.apple.com/documentation/appkit/nsview/1526917-constraints)Added [-[NSView constraintsAffectingLayoutForOrientation:]](https://developer.apple.com/documentation/appkit/nsview/1525968-constraintsaffectinglayout)Added [-[NSView contentCompressionResistancePriorityForOrientation:]](https://developer.apple.com/documentation/appkit/nsview/1526991-contentcompressionresistanceprio)Added [-[NSView contentHuggingPriorityForOrientation:]](https://developer.apple.com/documentation/appkit/nsview/1526979-contenthuggingpriorityfororienta)Added [-[NSView exerciseAmbiguityInLayout]](https://developer.apple.com/documentation/appkit/nsview/1526934-exerciseambiguityinlayout)Added [-[NSView fittingSize]](https://developer.apple.com/documentation/appkit/nsview/1526904-fittingsize)Added [-[NSView frameForAlignmentRect:]](https://developer.apple.com/documentation/appkit/nsview/1525584-frame)Added [-[NSView hasAmbiguousLayout]](https://developer.apple.com/documentation/appkit/nsview/1526907-hasambiguouslayout)Added [-[NSView intrinsicContentSize]](https://developer.apple.com/documentation/appkit/nsview/1526996-intrinsiccontentsize)Added [-[NSView invalidateIntrinsicContentSize]](https://developer.apple.com/documentation/appkit/nsview/1526864-invalidateintrinsiccontentsize)Added [-[NSView layout]](https://developer.apple.com/documentation/appkit/nsview/1526146-layout)Added [-[NSView layoutSubtreeIfNeeded]](https://developer.apple.com/documentation/appkit/nsview/1526871-layoutsubtreeifneeded)Added [-[NSView needsLayout]](https://developer.apple.com/documentation/appkit/nsview/1526912-needslayout)Added [-[NSView needsUpdateConstraints]](https://developer.apple.com/documentation/appkit/nsview/1526856-needsupdateconstraints)Added [-[NSView removeConstraint:]](https://developer.apple.com/documentation/appkit/nsview/1524333-removeconstraint)Added [-[NSView removeConstraints:]](https://developer.apple.com/documentation/appkit/nsview/1526932-removeconstraints)Added [+[NSView requiresConstraintBasedLayout]](https://developer.apple.com/documentation/appkit/nsview/1526926-requiresconstraintbasedlayout)Added [-[NSView setContentCompressionResistancePriority:forOrientation:]](https://developer.apple.com/documentation/appkit/nsview/1524974-setcontentcompressionresistancep)Added [-[NSView setContentHuggingPriority:forOrientation:]](https://developer.apple.com/documentation/appkit/nsview/1526937-setcontenthuggingpriority)Added [-[NSView setNeedsLayout:]](https://developer.apple.com/documentation/appkit/nsview/1526912-needslayout)Added [-[NSView setNeedsUpdateConstraints:]](https://developer.apple.com/documentation/appkit/nsview/1526856-needsupdateconstraints)Added [-[NSView setTranslatesAutoresizingMaskIntoConstraints:]](https://developer.apple.com/documentation/appkit/nsview/1526961-translatesautoresizingmaskintoco)Added [-[NSView translatesAutoresizingMaskIntoConstraints]](https://developer.apple.com/documentation/appkit/nsview/1526961-translatesautoresizingmaskintoco)Added [-[NSView updateConstraints]](https://developer.apple.com/documentation/appkit/nsview/1526891-updateconstraints)Added [-[NSView updateConstraintsForSubtreeIfNeeded]](https://developer.apple.com/documentation/appkit/nsview/1526939-updateconstraintsforsubtreeifnee)Added [-[NSWindow anchorAttributeForOrientation:]](https://developer.apple.com/documentation/appkit/nswindow/1526957-anchorattributefororientation)Added [-[NSWindow layoutIfNeeded]](https://developer.apple.com/documentation/appkit/nswindow/1526910-layoutifneeded)Added [-[NSWindow setAnchorAttribute:forOrientation:]](https://developer.apple.com/documentation/appkit/nswindow/1526985-setanchorattribute)Added [-[NSWindow updateConstraintsIfNeeded]](https://developer.apple.com/documentation/appkit/nswindow/1526915-updateconstraintsifneeded)Added [-[NSWindow visualizeConstraints:]](https://developer.apple.com/documentation/appkit/nswindow/1526997-visualizeconstraints)Added NSControl(NSConstraintBasedLayoutLayering)Added [#def NSDictionaryOfVariableBindings](https://developer.apple.com/documentation/uikit/nsdictionaryofvariablebindings)Added [NSEdgeInsets](https://developer.apple.com/documentation/foundation/nsedgeinsets)Added [NSEdgeInsetsMake()](https://developer.apple.com/documentation/foundation/1391130-nsedgeinsetsmake)Added [NSLayoutAttribute](https://developer.apple.com/documentation/uikit/nslayoutattribute)Added [NSLayoutAttributeBaseline](https://developer.apple.com/documentation/appkit/nslayoutattribute/nslayoutattributebaseline)Added [NSLayoutAttributeBottom](https://developer.apple.com/documentation/uikit/nslayoutconstraint/attribute/bottom)Added [NSLayoutAttributeCenterX](https://developer.apple.com/documentation/uikit/nslayoutattribute/nslayoutattributecenterx)Added [NSLayoutAttributeCenterY](https://developer.apple.com/documentation/appkit/nslayoutattribute/nslayoutattributecentery)Added [NSLayoutAttributeHeight](https://developer.apple.com/documentation/appkit/nslayoutconstraint/attribute/height)Added [NSLayoutAttributeLeading](https://developer.apple.com/documentation/uikit/nslayoutattribute/nslayoutattributeleading)Added [NSLayoutAttributeLeft](https://developer.apple.com/documentation/appkit/nslayoutconstraint/attribute/left)Added [NSLayoutAttributeNotAnAttribute](https://developer.apple.com/documentation/appkit/nslayoutattribute/nslayoutattributenotanattribute)Added [NSLayoutAttributeRight](https://developer.apple.com/documentation/appkit/nslayoutconstraint/attribute/right)Added [NSLayoutAttributeTop](https://developer.apple.com/documentation/uikit/nslayoutconstraint/attribute/top)Added [NSLayoutAttributeTrailing](https://developer.apple.com/documentation/uikit/nslayoutattribute/nslayoutattributetrailing)Added [NSLayoutAttributeWidth](https://developer.apple.com/documentation/appkit/nslayoutconstraint/attribute/width)Added [NSLayoutConstraintOrientation](https://developer.apple.com/documentation/appkit/nslayoutconstraint/orientation)Added [NSLayoutConstraintOrientationHorizontal](https://developer.apple.com/documentation/appkit/nslayoutconstraint/orientation/horizontal)Added [NSLayoutConstraintOrientationVertical](https://developer.apple.com/documentation/appkit/nslayoutconstraintorientation/nslayoutconstraintorientationvertical)Added [NSLayoutFormatAlignAllBaseline](https://developer.apple.com/documentation/appkit/nslayoutformatoptions/nslayoutformatalignallbaseline)Added [NSLayoutFormatAlignAllBottom](https://developer.apple.com/documentation/appkit/nslayoutconstraint/formatoptions/1526947-alignallbottom)Added [NSLayoutFormatAlignAllCenterX](https://developer.apple.com/documentation/uikit/nslayoutformatoptions/nslayoutformatalignallcenterx)Added [NSLayoutFormatAlignAllCenterY](https://developer.apple.com/documentation/appkit/nslayoutformatoptions/nslayoutformatalignallcentery)Added [NSLayoutFormatAlignAllLeading](https://developer.apple.com/documentation/appkit/nslayoutconstraint/formatoptions/1526925-alignallleading)Added [NSLayoutFormatAlignAllLeft](https://developer.apple.com/documentation/uikit/nslayoutformatoptions/nslayoutformatalignallleft)Added [NSLayoutFormatAlignAllRight](https://developer.apple.com/documentation/uikit/nslayoutconstraint/formatoptions/1525250-alignallright)Added [NSLayoutFormatAlignAllTop](https://developer.apple.com/documentation/uikit/nslayoutconstraint/formatoptions/1526952-alignalltop)Added [NSLayoutFormatAlignAllTrailing](https://developer.apple.com/documentation/uikit/nslayoutformatoptions/nslayoutformatalignalltrailing)Added [NSLayoutFormatAlignmentMask](https://developer.apple.com/documentation/uikit/nslayoutformatoptions/nslayoutformatalignmentmask)Added [NSLayoutFormatDirectionLeadingToTrailing](https://developer.apple.com/documentation/uikit/nslayoutformatoptions/nslayoutformatdirectionleadingtotrailing)Added [NSLayoutFormatDirectionLeftToRight](https://developer.apple.com/documentation/uikit/nslayoutformatoptions/nslayoutformatdirectionlefttoright)Added [NSLayoutFormatDirectionMask](https://developer.apple.com/documentation/uikit/nslayoutformatoptions/nslayoutformatdirectionmask)Added [NSLayoutFormatDirectionRightToLeft](https://developer.apple.com/documentation/appkit/nslayoutformatoptions/nslayoutformatdirectionrighttoleft)Added [NSLayoutFormatOptions](https://developer.apple.com/documentation/appkit/nslayoutformatoptions)Added [NSLayoutPriority](https://developer.apple.com/documentation/appkit/nslayoutpriority)Added NSLayoutPriorityDefaultHighAdded NSLayoutPriorityDefaultLowAdded NSLayoutPriorityDragThatCanResizeWindowAdded NSLayoutPriorityDragThatCannotResizeWindowAdded NSLayoutPriorityFittingSizeCompressionAdded NSLayoutPriorityRequiredAdded NSLayoutPriorityWindowSizeStayPutAdded [NSLayoutRelation](https://developer.apple.com/documentation/appkit/nslayoutrelation)Added [NSLayoutRelationEqual](https://developer.apple.com/documentation/appkit/nslayoutrelation/nslayoutrelationequal)Added [NSLayoutRelationGreaterThanOrEqual](https://developer.apple.com/documentation/uikit/nslayoutrelation/nslayoutrelationgreaterthanorequal)Added [NSLayoutRelationLessThanOrEqual](https://developer.apple.com/documentation/uikit/nslayoutrelation/nslayoutrelationlessthanorequal)Added NSView(NSConstraintBasedCompatibility)Added NSView(NSConstraintBasedLayoutCoreMethods)Added NSView(NSConstraintBasedLayoutDebugging)Added NSView(NSConstraintBasedLayoutFittingSize)Added NSView(NSConstraintBasedLayoutInstallingConstraints)Added NSView(NSConstraintBasedLayoutLayering)Added [NSViewNoInstrinsicMetric](https://developer.apple.com/documentation/appkit/nsviewnoinstrinsicmetric)Added NSWindow(NSConstraintBasedLayoutAnchoring)Added NSWindow(NSConstraintBasedLayoutCoreMethods)Added NSWindow(NSConstraintBasedLayoutDebugging)NSLayoutManager.hAdded [-[NSLayoutManager showCGGlyphs:positions:count:font:matrix:attributes:inContext:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403247-showcgglyphs)Added [NSTextLayoutOrientationProvider](https://developer.apple.com/documentation/appkit/nstextlayoutorientationprovider)Added [-[NSTextLayoutOrientationProvider layoutOrientation]](https://developer.apple.com/documentation/appkit/nstextlayoutorientationprovider/1402990-layoutorientation)Added [NSTextLayoutOrientation](https://developer.apple.com/documentation/uikit/nstextlayoutorientation)Added [NSTextLayoutOrientationHorizontal](https://developer.apple.com/documentation/appkit/nstextlayoutorientation/nstextlayoutorientationhorizontal)Added [NSTextLayoutOrientationVertical](https://developer.apple.com/documentation/uikit/nslayoutmanager/textlayoutorientation/vertical)Modified [-[NSLayoutManager showPackedGlyphs:length:glyphRange:atPoint:font:color:printingAdjustment:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403154-showpackedglyphs)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

NSOpenGL.hAdded [NSOpenGLCPCurrentRendererID](https://developer.apple.com/documentation/appkit/nsopenglcpcurrentrendererid)Added [NSOpenGLCPGPUFragmentProcessing](https://developer.apple.com/documentation/appkit/nsopenglcpgpufragmentprocessing)Added [NSOpenGLCPGPUVertexProcessing](https://developer.apple.com/documentation/appkit/nsopenglcpgpuvertexprocessing)Added [NSOpenGLCPHasDrawable](https://developer.apple.com/documentation/appkit/nsopenglcphasdrawable)Added [NSOpenGLCPMPSwapsInFlight](https://developer.apple.com/documentation/appkit/nsopenglcpmpswapsinflight)Added [NSOpenGLCPReclaimResources](https://developer.apple.com/documentation/appkit/nsopenglcpreclaimresources)Added [NSOpenGLCPSurfaceBackingSize](https://developer.apple.com/documentation/appkit/nsopenglcpsurfacebackingsize)Added [NSOpenGLCPSurfaceSurfaceVolatile](https://developer.apple.com/documentation/appkit/nsopenglcpsurfacesurfacevolatile)Added [NSOpenGLGOUseBuildCache](https://developer.apple.com/documentation/appkit/nsopenglglobaloption/usebuildcache)Added [NSOpenGLPFAOpenGLProfile](https://developer.apple.com/documentation/appkit/nsopenglpfaopenglprofile)Added [NSOpenGLPFATripleBuffer](https://developer.apple.com/documentation/appkit/nsopenglpfatriplebuffer)Added [NSOpenGLProfileVersion3_2Core](https://developer.apple.com/documentation/appkit/nsopenglprofileversion3_2core)Added [NSOpenGLProfileVersionLegacy](https://developer.apple.com/documentation/appkit/1436146-opengl_profiles/nsopenglprofileversionlegacy)NSOpenGLView.hAdded [-[NSView setWantsBestResolutionOpenGLSurface:]](https://developer.apple.com/documentation/appkit/nsview/1414938-wantsbestresolutionopenglsurface)Added [-[NSView wantsBestResolutionOpenGLSurface]](https://developer.apple.com/documentation/appkit/nsview/1414938-wantsbestresolutionopenglsurface)Added NSView(NSOpenGLSurfaceResolution)NSOutlineView.hRemoved -[NSObject outlineViewColumnDidMove:]Removed -[NSObject outlineViewColumnDidResize:]Removed -[NSObject outlineViewItemDidCollapse:]Removed -[NSObject outlineViewItemDidExpand:]Removed -[NSObject outlineViewItemWillCollapse:]Removed -[NSObject outlineViewItemWillExpand:]Removed -[NSObject outlineViewSelectionDidChange:]Removed -[NSObject outlineViewSelectionIsChanging:]Removed NSObject(NSOutlineViewNotifications)Added [-[NSOutlineView insertItemsAtIndexes:inParent:withAnimation:]](https://developer.apple.com/documentation/appkit/nsoutlineview/1528656-insertitemsatindexes)Added -[NSOutlineView insertRowsAtIndexes:withAnimation:] (no architecture available)Added [-[NSOutlineView moveItemAtIndex:inParent:toIndex:inParent:]](https://developer.apple.com/documentation/appkit/nsoutlineview/1530467-moveitem)Added -[NSOutlineView moveRowAtIndex:toIndex:] (no architecture available)Added [-[NSOutlineView removeItemsAtIndexes:inParent:withAnimation:]](https://developer.apple.com/documentation/appkit/nsoutlineview/1527168-removeitemsatindexes)Added -[NSOutlineView removeRowsAtIndexes:withAnimation:] (no architecture available)Added [-[NSOutlineViewDataSource outlineView:draggingSession:endedAtPoint:operation:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1532073-outlineview)Added [-[NSOutlineViewDataSource outlineView:draggingSession:willBeginAtPoint:forItems:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1535142-outlineview)Added [-[NSOutlineViewDataSource outlineView:pasteboardWriterForItem:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1525837-outlineview)Added [-[NSOutlineViewDataSource outlineView:updateDraggingItemsForDrag:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1534424-outlineview)Added [-[NSOutlineViewDelegate outlineView:didAddRowView:forRow:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1528320-outlineview)Added [-[NSOutlineViewDelegate outlineView:didRemoveRowView:forRow:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1530612-outlineview)Added [-[NSOutlineViewDelegate outlineView:rowViewForItem:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1532140-outlineview)Added [-[NSOutlineViewDelegate outlineView:viewForTableColumn:item:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1535566-outlineview)Added [-[NSOutlineViewDelegate outlineViewColumnDidMove:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1525297-outlineviewcolumndidmove)Added [-[NSOutlineViewDelegate outlineViewColumnDidResize:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1533372-outlineviewcolumndidresize)Added [-[NSOutlineViewDelegate outlineViewItemDidCollapse:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1535557-outlineviewitemdidcollapse)Added [-[NSOutlineViewDelegate outlineViewItemDidExpand:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1530869-outlineviewitemdidexpand)Added [-[NSOutlineViewDelegate outlineViewItemWillCollapse:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1526896-outlineviewitemwillcollapse)Added [-[NSOutlineViewDelegate outlineViewItemWillExpand:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1535847-outlineviewitemwillexpand)Added [-[NSOutlineViewDelegate outlineViewSelectionDidChange:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1526913-outlineviewselectiondidchange)Added [-[NSOutlineViewDelegate outlineViewSelectionIsChanging:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1532481-outlineviewselectionischanging)NSPasteboard.hAdded [NSPasteboardTypeTextFinderOptions](https://developer.apple.com/documentation/appkit/nspasteboard/pasteboardtype/1529222-textfinderoptions)NSPopover.hAdded [NSPopover](https://developer.apple.com/documentation/appkit/nspopover)Added [NSPopover.animates](https://developer.apple.com/documentation/appkit/nspopover/1526527-animates)Added [NSPopover.appearance](https://developer.apple.com/documentation/appkit/nspopover/1529859-appearance)Added [NSPopover.behavior](https://developer.apple.com/documentation/appkit/nspopover/1533539-behavior)Added [-[NSPopover close]](https://developer.apple.com/documentation/appkit/nspopover/1526823-close)Added [NSPopover.contentSize](https://developer.apple.com/documentation/appkit/nspopover/1524677-contentsize)Added [NSPopover.contentViewController](https://developer.apple.com/documentation/appkit/nspopover/1526794-contentviewcontroller)Added [NSPopover.delegate](https://developer.apple.com/documentation/appkit/nspopover/1526708-delegate)Added [-[NSPopover performClose:]](https://developer.apple.com/documentation/appkit/nspopover/1534290-performclose)Added [NSPopover.positioningRect](https://developer.apple.com/documentation/appkit/nspopover/1526090-positioningrect)Added [-[NSPopover showRelativeToRect:ofView:preferredEdge:]](https://developer.apple.com/documentation/appkit/nspopover/1532113-show)Added [NSPopover.shown](https://developer.apple.com/documentation/appkit/nspopover/1535120-isshown)Added [NSPopoverDelegate](https://developer.apple.com/documentation/appkit/nspopoverdelegate)Added [-[NSPopoverDelegate detachableWindowForPopover:]](https://developer.apple.com/documentation/appkit/nspopoverdelegate/1534822-detachablewindowforpopover)Added [-[NSPopoverDelegate popoverDidClose:]](https://developer.apple.com/documentation/appkit/nspopoverdelegate/1526581-popoverdidclose)Added [-[NSPopoverDelegate popoverDidShow:]](https://developer.apple.com/documentation/appkit/nspopoverdelegate/1533573-popoverdidshow)Added [-[NSPopoverDelegate popoverShouldClose:]](https://developer.apple.com/documentation/appkit/nspopoverdelegate/1532593-popovershouldclose)Added [-[NSPopoverDelegate popoverWillClose:]](https://developer.apple.com/documentation/appkit/nspopoverdelegate/1535119-popoverwillclose)Added [-[NSPopoverDelegate popoverWillShow:]](https://developer.apple.com/documentation/appkit/nspopoverdelegate/1532556-popoverwillshow)Added [NSPopoverAppearance](https://developer.apple.com/documentation/appkit/nspopover/appearance)Added [NSPopoverAppearanceHUD](https://developer.apple.com/documentation/appkit/nspopover/appearance/hud)Added [NSPopoverAppearanceMinimal](https://developer.apple.com/documentation/appkit/nspopoverappearance/nspopoverappearanceminimal)Added [NSPopoverBehavior](https://developer.apple.com/documentation/appkit/nspopover/behavior)Added [NSPopoverBehaviorApplicationDefined](https://developer.apple.com/documentation/appkit/nspopover/behavior/applicationdefined)Added [NSPopoverBehaviorSemitransient](https://developer.apple.com/documentation/appkit/nspopoverbehavior/nspopoverbehaviorsemitransient)Added [NSPopoverBehaviorTransient](https://developer.apple.com/documentation/appkit/nspopoverbehavior/nspopoverbehaviortransient)Added [NSPopoverCloseReasonDetachToWindow](https://developer.apple.com/documentation/appkit/nspopover/closereason/1530670-detachtowindow)Added [NSPopoverCloseReasonKey](https://developer.apple.com/documentation/appkit/nspopoverclosereasonkey)Added [NSPopoverCloseReasonStandard](https://developer.apple.com/documentation/appkit/nspopoverclosereasonstandard)Added [NSPopoverDidCloseNotification](https://developer.apple.com/documentation/appkit/nspopover/1528535-didclosenotification)Added [NSPopoverDidShowNotification](https://developer.apple.com/documentation/appkit/nspopover/1533267-didshownotification)Added [NSPopoverWillCloseNotification](https://developer.apple.com/documentation/appkit/nspopoverwillclosenotification)Added [NSPopoverWillShowNotification](https://developer.apple.com/documentation/appkit/nspopoverwillshownotification)NSPrintOperation.hAdded [-[NSPrintOperation preferredRenderingQuality]](https://developer.apple.com/documentation/appkit/nsprintoperation/1529716-preferredrenderingquality)Added [NSPrintRenderingQuality](https://developer.apple.com/documentation/appkit/nsprintoperation/renderingquality)Added [NSPrintRenderingQualityBest](https://developer.apple.com/documentation/appkit/nsprintrenderingquality/nsprintrenderingqualitybest)Added [NSPrintRenderingQualityResponsive](https://developer.apple.com/documentation/appkit/nsprintrenderingquality/nsprintrenderingqualityresponsive)NSResponder.hAdded [-[NSResponder performTextFinderAction:]](https://developer.apple.com/documentation/appkit/nsresponder/1525967-performtextfinderaction)Added [-[NSResponder supplementalTargetForAction:sender:]](https://developer.apple.com/documentation/appkit/nsresponder/1535269-supplementaltarget)Added [-[NSResponder validateProposedFirstResponder:forEvent:]](https://developer.apple.com/documentation/appkit/nsresponder/1527066-validateproposedfirstresponder)Added [-[NSResponder wantsForwardedScrollEventsForAxis:]](https://developer.apple.com/documentation/appkit/nsresponder/1534209-wantsforwardedscrolleventsforaxi)Added [-[NSResponder wantsScrollEventsForSwipeTrackingOnAxis:]](https://developer.apple.com/documentation/appkit/nsresponder/1527456-wantsscrolleventsforswipetrackin)Added NSResponder(NSControlEditingSupport)Added NSResponder(NSTextFinderSupport)NSRulerView.hAdded [-[NSView rulerView:locationForPoint:]](https://developer.apple.com/documentation/appkit/nsview/1535261-rulerview)Added [-[NSView rulerView:pointForLocation:]](https://developer.apple.com/documentation/appkit/nsview/1524292-rulerview)NSRunningApplication.hAdded [NSRunningApplication.ownsMenuBar](https://developer.apple.com/documentation/appkit/nsrunningapplication/1525915-ownsmenubar)Added [+[NSRunningApplication terminateAutomaticallyTerminableApplications]](https://developer.apple.com/documentation/appkit/nsrunningapplication/1529538-terminateautomaticallyterminable)NSScreen.hAdded [-[NSScreen backingAlignedRect:options:]](https://developer.apple.com/documentation/appkit/nsscreen/1388381-backingalignedrect)Added [-[NSScreen backingScaleFactor]](https://developer.apple.com/documentation/appkit/nsscreen/1388385-backingscalefactor)Added [-[NSScreen convertRectFromBacking:]](https://developer.apple.com/documentation/appkit/nsscreen/1388364-convertrectfrombacking)Added [-[NSScreen convertRectToBacking:]](https://developer.apple.com/documentation/appkit/nsscreen/1388389-convertrecttobacking)Added NSScreen(NSDeprecated)Modified [-[NSScreen userSpaceScaleFactor]](https://developer.apple.com/documentation/appkit/nsscreen/1388375-userspacescalefactor)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

NSScrollView.hAdded [+[NSScrollView contentSizeForFrameSize:horizontalScrollerClass:verticalScrollerClass:borderType:controlSize:scrollerStyle:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403471-contentsizeforframesize)Added [-[NSScrollView findBarPosition]](https://developer.apple.com/documentation/appkit/nsscrollview/1403501-findbarposition)Added [-[NSScrollView flashScrollers]](https://developer.apple.com/documentation/appkit/nsscrollview/1403460-flashscrollers)Added [+[NSScrollView frameSizeForContentSize:horizontalScrollerClass:verticalScrollerClass:borderType:controlSize:scrollerStyle:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403545-framesizeforcontentsize)Added [-[NSScrollView horizontalScrollElasticity]](https://developer.apple.com/documentation/appkit/nsscrollview/1403540-horizontalscrollelasticity)Added [-[NSScrollView scrollerKnobStyle]](https://developer.apple.com/documentation/appkit/nsscrollview/1403544-scrollerknobstyle)Added [-[NSScrollView scrollerStyle]](https://developer.apple.com/documentation/appkit/nsscrollview/1403520-scrollerstyle)Added [-[NSScrollView setFindBarPosition:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403501-findbarposition)Added [-[NSScrollView setHorizontalScrollElasticity:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403540-horizontalscrollelasticity)Added [-[NSScrollView setScrollerKnobStyle:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403544-scrollerknobstyle)Added [-[NSScrollView setScrollerStyle:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403520-scrollerstyle)Added [-[NSScrollView setUsesPredominantAxisScrolling:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403489-usespredominantaxisscrolling)Added [-[NSScrollView setVerticalScrollElasticity:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403475-verticalscrollelasticity)Added [-[NSScrollView usesPredominantAxisScrolling]](https://developer.apple.com/documentation/appkit/nsscrollview/1403489-usespredominantaxisscrolling)Added [-[NSScrollView verticalScrollElasticity]](https://developer.apple.com/documentation/appkit/nsscrollview/1403475-verticalscrollelasticity)Added [NSScrollElasticity](https://developer.apple.com/documentation/appkit/nsscrollview/elasticity)Added [NSScrollElasticityAllowed](https://developer.apple.com/documentation/appkit/nsscrollview/elasticity/allowed)Added [NSScrollElasticityAutomatic](https://developer.apple.com/documentation/appkit/nsscrollview/elasticity/automatic)Added [NSScrollElasticityNone](https://developer.apple.com/documentation/appkit/nsscrollview/elasticity/none)Added NSScrollView(NSFindBarSupport)Added [NSScrollViewFindBarPosition](https://developer.apple.com/documentation/appkit/nsscrollview/findbarposition)Added [NSScrollViewFindBarPositionAboveContent](https://developer.apple.com/documentation/appkit/nsscrollview/findbarposition/abovecontent)Added [NSScrollViewFindBarPositionAboveHorizontalRuler](https://developer.apple.com/documentation/appkit/nsscrollviewfindbarposition/nsscrollviewfindbarpositionabovehorizontalruler)Added [NSScrollViewFindBarPositionBelowContent](https://developer.apple.com/documentation/appkit/nsscrollviewfindbarposition/nsscrollviewfindbarpositionbelowcontent)Modified [NSScrollView](https://developer.apple.com/documentation/appkit/nsscrollview)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSTextFinderBarContainer |

NSScroller.hAdded +[NSScroller isCompatibleWithOverlayScrollers]Added [-[NSScroller knobStyle]](https://developer.apple.com/documentation/appkit/nsscroller/1523666-knobstyle)Added [+[NSScroller preferredScrollerStyle]](https://developer.apple.com/documentation/appkit/nsscroller/1523620-preferredscrollerstyle)Added [-[NSScroller scrollerStyle]](https://developer.apple.com/documentation/appkit/nsscroller/1523591-scrollerstyle)Added [+[NSScroller scrollerWidthForControlSize:scrollerStyle:]](https://developer.apple.com/documentation/appkit/nsscroller/1523603-scrollerwidthforcontrolsize)Added [-[NSScroller setKnobStyle:]](https://developer.apple.com/documentation/appkit/nsscroller/1523666-knobstyle)Added [-[NSScroller setScrollerStyle:]](https://developer.apple.com/documentation/appkit/nsscroller/1523591-scrollerstyle)Added [NSPreferredScrollerStyleDidChangeNotification](https://developer.apple.com/documentation/appkit/nsscroller/1523618-preferredscrollerstyledidchangen)Added [NSScrollerKnobStyle](https://developer.apple.com/documentation/appkit/nsscroller/knobstyle)Added [NSScrollerKnobStyleDark](https://developer.apple.com/documentation/appkit/nsscrollerknobstyle/nsscrollerknobstyledark)Added [NSScrollerKnobStyleDefault](https://developer.apple.com/documentation/appkit/nsscrollerknobstyle/nsscrollerknobstyledefault)Added [NSScrollerKnobStyleLight](https://developer.apple.com/documentation/appkit/nsscroller/knobstyle/light)Added [NSScrollerStyle](https://developer.apple.com/documentation/appkit/nsscroller/style)Added [NSScrollerStyleLegacy](https://developer.apple.com/documentation/appkit/nsscrollerstyle/nsscrollerstylelegacy)Added [NSScrollerStyleOverlay](https://developer.apple.com/documentation/appkit/nsscrollerstyle/nsscrollerstyleoverlay)Modified [-[NSScroller drawParts]](https://developer.apple.com/documentation/appkit/nsscroller/1523674-drawparts)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

NSSpellChecker.hAdded [-[NSSpellChecker correctionForWordRange:inString:language:inSpellDocumentWithTag:]](https://developer.apple.com/documentation/appkit/nsspellchecker/1531542-correctionforwordrange)Added [-[NSSpellChecker dismissCorrectionIndicatorForView:]](https://developer.apple.com/documentation/appkit/nsspellchecker/1535527-dismisscorrectionindicator)Added +[NSSpellChecker isAutomaticSpellingCorrectionEnabled]Added +[NSSpellChecker isAutomaticTextReplacementEnabled]Added [-[NSSpellChecker recordResponse:toCorrection:forWord:language:inSpellDocumentWithTag:]](https://developer.apple.com/documentation/appkit/nsspellchecker/1535568-recordresponse)Added [-[NSSpellChecker showCorrectionIndicatorOfType:primaryString:alternativeStrings:forStringInRect:view:completionHandler:]](https://developer.apple.com/documentation/appkit/nsspellchecker/1524316-showcorrectionindicator)Added [NSCorrectionIndicatorType](https://developer.apple.com/documentation/appkit/nsspellchecker/correctionindicatortype)Added [NSCorrectionIndicatorTypeDefault](https://developer.apple.com/documentation/appkit/nscorrectionindicatortype/nscorrectionindicatortypedefault)Added [NSCorrectionIndicatorTypeGuesses](https://developer.apple.com/documentation/appkit/nscorrectionindicatortype/nscorrectionindicatortypeguesses)Added [NSCorrectionIndicatorTypeReversion](https://developer.apple.com/documentation/appkit/nscorrectionindicatortype/nscorrectionindicatortypereversion)Added [NSCorrectionResponse](https://developer.apple.com/documentation/appkit/nscorrectionresponse)Added [NSCorrectionResponseAccepted](https://developer.apple.com/documentation/appkit/nscorrectionresponse/nscorrectionresponseaccepted)Added [NSCorrectionResponseEdited](https://developer.apple.com/documentation/appkit/nsspellchecker/correctionresponse/edited)Added [NSCorrectionResponseIgnored](https://developer.apple.com/documentation/appkit/nsspellchecker/correctionresponse/ignored)Added [NSCorrectionResponseNone](https://developer.apple.com/documentation/appkit/nsspellchecker/correctionresponse/none)Added [NSCorrectionResponseRejected](https://developer.apple.com/documentation/appkit/nscorrectionresponse/nscorrectionresponserejected)Added [NSCorrectionResponseReverted](https://developer.apple.com/documentation/appkit/nscorrectionresponse/nscorrectionresponsereverted)Added [NSSpellCheckerDidChangeAutomaticSpellingCorrectionNotification](https://developer.apple.com/documentation/appkit/nsspellchecker/1529393-didchangeautomaticspellingcorrec)Added [NSSpellCheckerDidChangeAutomaticTextReplacementNotification](https://developer.apple.com/documentation/appkit/nsspellcheckerdidchangeautomatictextreplacementnotification)Added [NSTextCheckingRegularExpressionsKey](https://developer.apple.com/documentation/appkit/nstextcheckingregularexpressionskey)NSTabView.hModified [-[NSTabViewDelegate tabViewDidChangeNumberOfTabViewItems:]](https://developer.apple.com/documentation/appkit/nstabviewdelegate/1391657-tabviewdidchangenumberoftabviewi)

|  | Declaration |
| --- | --- |
| From | - (void)tabViewDidChangeNumberOfTabViewItems:(NSTabView \*)TabView |
| To | - (void)tabViewDidChangeNumberOfTabViewItems:(NSTabView \*)tabView |

NSTableCellView.hAdded [NSTableCellView](https://developer.apple.com/documentation/appkit/nstablecellview)Added [NSTableCellView.backgroundStyle](https://developer.apple.com/documentation/appkit/nstablecellview/1483206-backgroundstyle)Added [NSTableCellView.draggingImageComponents](https://developer.apple.com/documentation/appkit/nstablecellview/1483199-draggingimagecomponents)Added [NSTableCellView.imageView](https://developer.apple.com/documentation/appkit/nstablecellview/1483213-imageview)Added [NSTableCellView.objectValue](https://developer.apple.com/documentation/appkit/nstablecellview/1483204-objectvalue)Added [NSTableCellView.rowSizeStyle](https://developer.apple.com/documentation/appkit/nstablecellview/1483211-rowsizestyle)Added [NSTableCellView.textField](https://developer.apple.com/documentation/appkit/nstablecellview/1483202-textfield)NSTableColumn.hModified [NSTableColumn](https://developer.apple.com/documentation/appkit/nstablecolumn)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSCoding, NSUserInterfaceItemIdentification |

Modified [-[NSTableColumn setIdentifier:]](https://developer.apple.com/documentation/appkit/nstablecolumn/1531113-identifier)

|  | Declaration |
| --- | --- |
| From | - (void)setIdentifier:(id)identifier |
| To | - (void)setIdentifier:(NSString \*)identifier |

Modified [-[NSTableColumn initWithIdentifier:]](https://developer.apple.com/documentation/appkit/nstablecolumn/1526749-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithIdentifier:(id)identifier |
| To | - (id)initWithIdentifier:(NSString \*)identifier |

Modified [-[NSTableColumn identifier]](https://developer.apple.com/documentation/appkit/nstablecolumn/1531113-identifier)

|  | Declaration |
| --- | --- |
| From | - (id)identifier |
| To | - (NSString \*)identifier |

NSTableRowView.hAdded [NSTableRowView](https://developer.apple.com/documentation/appkit/nstablerowview)Added [NSTableRowView.backgroundColor](https://developer.apple.com/documentation/appkit/nstablerowview/1534057-backgroundcolor)Added [NSTableRowView.draggingDestinationFeedbackStyle](https://developer.apple.com/documentation/appkit/nstablerowview/1525012-draggingdestinationfeedbackstyle)Added [-[NSTableRowView drawBackgroundInRect:]](https://developer.apple.com/documentation/appkit/nstablerowview/1531936-drawbackgroundinrect)Added [-[NSTableRowView drawDraggingDestinationFeedbackInRect:]](https://developer.apple.com/documentation/appkit/nstablerowview/1528434-drawdraggingdestinationfeedbacki)Added [-[NSTableRowView drawSelectionInRect:]](https://developer.apple.com/documentation/appkit/nstablerowview/1526425-drawselection)Added [-[NSTableRowView drawSeparatorInRect:]](https://developer.apple.com/documentation/appkit/nstablerowview/1525167-drawseparatorinrect)Added [NSTableRowView.emphasized](https://developer.apple.com/documentation/appkit/nstablerowview/1526258-emphasized)Added [NSTableRowView.floating](https://developer.apple.com/documentation/appkit/nstablerowview/1534291-isfloating)Added [NSTableRowView.groupRowStyle](https://developer.apple.com/documentation/appkit/nstablerowview/1530499-grouprowstyle)Added [NSTableRowView.indentationForDropOperation](https://developer.apple.com/documentation/appkit/nstablerowview/1535836-indentationfordropoperation)Added [NSTableRowView.interiorBackgroundStyle](https://developer.apple.com/documentation/appkit/nstablerowview/1535905-interiorbackgroundstyle)Added [NSTableRowView.numberOfColumns](https://developer.apple.com/documentation/appkit/nstablerowview/1525610-numberofcolumns)Added [NSTableRowView.selected](https://developer.apple.com/documentation/appkit/nstablerowview/1529508-isselected)Added [NSTableRowView.selectionHighlightStyle](https://developer.apple.com/documentation/appkit/nstablerowview/1531083-selectionhighlightstyle)Added [NSTableRowView.targetForDropOperation](https://developer.apple.com/documentation/appkit/nstablerowview/1533914-targetfordropoperation)Added [-[NSTableRowView viewAtColumn:]](https://developer.apple.com/documentation/appkit/nstablerowview/1534440-viewatcolumn)NSTableView.hAdded [-[NSTableView beginUpdates]](https://developer.apple.com/documentation/appkit/nstableview/1527288-beginupdates)Added [-[NSTableView columnForView:]](https://developer.apple.com/documentation/appkit/nstableview/1529415-columnforview)Added [-[NSTableView effectiveRowSizeStyle]](https://developer.apple.com/documentation/appkit/nstableview/1531825-effectiverowsizestyle)Added [-[NSTableView endUpdates]](https://developer.apple.com/documentation/appkit/nstableview/1526267-endupdates)Added [-[NSTableView enumerateAvailableRowViewsUsingBlock:]](https://developer.apple.com/documentation/appkit/nstableview/1532750-enumerateavailablerowviewsusingb)Added [-[NSTableView floatsGroupRows]](https://developer.apple.com/documentation/appkit/nstableview/1528624-floatsgrouprows)Added [-[NSTableView insertRowsAtIndexes:withAnimation:]](https://developer.apple.com/documentation/appkit/nstableview/1532406-insertrows)Added [-[NSTableView makeViewWithIdentifier:owner:]](https://developer.apple.com/documentation/appkit/nstableview/1535482-makeviewwithidentifier)Added [-[NSTableView moveRowAtIndex:toIndex:]](https://developer.apple.com/documentation/appkit/nstableview/1535835-moverowatindex)Added [-[NSTableView removeRowsAtIndexes:withAnimation:]](https://developer.apple.com/documentation/appkit/nstableview/1524655-removerowsatindexes)Added [-[NSTableView rowForView:]](https://developer.apple.com/documentation/appkit/nstableview/1526732-rowforview)Added [-[NSTableView rowSizeStyle]](https://developer.apple.com/documentation/appkit/nstableview/1534438-rowsizestyle)Added [-[NSTableView rowViewAtRow:makeIfNecessary:]](https://developer.apple.com/documentation/appkit/nstableview/1525162-rowviewatrow)Added [-[NSTableView setFloatsGroupRows:]](https://developer.apple.com/documentation/appkit/nstableview/1528624-floatsgrouprows)Added [-[NSTableView setRowSizeStyle:]](https://developer.apple.com/documentation/appkit/nstableview/1534438-rowsizestyle)Added [-[NSTableView viewAtColumn:row:makeIfNecessary:]](https://developer.apple.com/documentation/appkit/nstableview/1528831-view)Added [-[NSTableViewDataSource tableView:draggingSession:endedAtPoint:operation:]](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1534355-tableview)Added [-[NSTableViewDataSource tableView:draggingSession:willBeginAtPoint:forRowIndexes:]](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1528890-tableview)Added [-[NSTableViewDataSource tableView:pasteboardWriterForRow:]](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1535294-tableview)Added [-[NSTableViewDataSource tableView:updateDraggingItemsForDrag:]](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1535273-tableview)Added [-[NSTableViewDelegate tableView:didAddRowView:forRow:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1527434-tableview)Added [-[NSTableViewDelegate tableView:didRemoveRowView:forRow:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1528674-tableview)Added [-[NSTableViewDelegate tableView:rowViewForRow:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1532417-tableview)Added [-[NSTableViewDelegate tableView:viewForTableColumn:row:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1527449-tableview)Added [NSTableViewAnimationEffectFade](https://developer.apple.com/documentation/appkit/nstableview/animationoptions/1526754-effectfade)Added [NSTableViewAnimationEffectGap](https://developer.apple.com/documentation/appkit/nstableview/animationoptions/1535457-effectgap)Added [NSTableViewAnimationEffectNone](https://developer.apple.com/documentation/appkit/nstableviewanimationoptions/nstableviewanimationeffectnone)Added [NSTableViewAnimationOptions](https://developer.apple.com/documentation/appkit/nstableview/animationoptions)Added [NSTableViewAnimationSlideDown](https://developer.apple.com/documentation/appkit/nstableviewanimationoptions/nstableviewanimationslidedown)Added [NSTableViewAnimationSlideLeft](https://developer.apple.com/documentation/appkit/nstableviewanimationoptions/nstableviewanimationslideleft)Added [NSTableViewAnimationSlideRight](https://developer.apple.com/documentation/appkit/nstableviewanimationoptions/nstableviewanimationslideright)Added [NSTableViewAnimationSlideUp](https://developer.apple.com/documentation/appkit/nstableview/animationoptions/1527196-slideup)Added [NSTableViewDashedHorizontalGridLineMask](https://developer.apple.com/documentation/appkit/nstableview/gridlinestyle/1524632-dashedhorizontalgridlinemask)Added [NSTableViewGridLineStyle](https://developer.apple.com/documentation/appkit/nstableviewgridlinestyle)Added [NSTableViewRowSizeStyle](https://developer.apple.com/documentation/appkit/nstableviewrowsizestyle)Added [NSTableViewRowSizeStyleCustom](https://developer.apple.com/documentation/appkit/nstableviewrowsizestyle/nstableviewrowsizestylecustom)Added [NSTableViewRowSizeStyleDefault](https://developer.apple.com/documentation/appkit/nstableview/rowsizestyle/default)Added [NSTableViewRowSizeStyleLarge](https://developer.apple.com/documentation/appkit/nstableview/rowsizestyle/large)Added [NSTableViewRowSizeStyleMedium](https://developer.apple.com/documentation/appkit/nstableview/rowsizestyle/medium)Added [NSTableViewRowSizeStyleSmall](https://developer.apple.com/documentation/appkit/nstableview/rowsizestyle/small)Added [NSTableViewRowViewKey](https://developer.apple.com/documentation/appkit/nstableview/1524585-rowviewidentifier)Modified [-[NSTableView setGridStyleMask:]](https://developer.apple.com/documentation/appkit/nstableview/1528689-gridstylemask)

|  | Declaration |
| --- | --- |
| From | - (void)setGridStyleMask:(NSUInteger)gridType |
| To | - (void)setGridStyleMask:(NSTableViewGridLineStyle)gridStyle |

Modified [-[NSTableView tableColumnWithIdentifier:]](https://developer.apple.com/documentation/appkit/nstableview/1531134-tablecolumnwithidentifier)

|  | Declaration |
| --- | --- |
| From | - (NSTableColumn \*)tableColumnWithIdentifier:(id)identifier |
| To | - (NSTableColumn \*)tableColumnWithIdentifier:(NSString \*)identifier |

Modified [NSTableView](https://developer.apple.com/documentation/appkit/nstableview)

|  | Protocols |
| --- | --- |
| From | NSUserInterfaceValidations, NSTextViewDelegate |
| To | NSDraggingSource, NSTextViewDelegate, NSUserInterfaceValidations |

Modified [-[NSTableView gridStyleMask]](https://developer.apple.com/documentation/appkit/nstableview/1528689-gridstylemask)

|  | Declaration |
| --- | --- |
| From | - (NSUInteger)gridStyleMask |
| To | - (NSTableViewGridLineStyle)gridStyleMask |

Modified [-[NSTableView columnWithIdentifier:]](https://developer.apple.com/documentation/appkit/nstableview/1526734-columnwithidentifier)

|  | Declaration |
| --- | --- |
| From | - (NSInteger)columnWithIdentifier:(id)identifier |
| To | - (NSInteger)columnWithIdentifier:(NSString \*)identifier |

NSTextContainer.hModified [NSTextContainer](https://developer.apple.com/documentation/appkit/nstextcontainer)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSCoding, NSTextLayoutOrientationProvider |

NSTextFinder.hAdded [NSTextFinder](https://developer.apple.com/documentation/appkit/nstextfinder)Added [-[NSTextFinder cancelFindIndicator]](https://developer.apple.com/documentation/appkit/nstextfinder/1525467-cancelfindindicator)Added [NSTextFinder.client](https://developer.apple.com/documentation/appkit/nstextfinder/1533813-client)Added [+[NSTextFinder drawIncrementalMatchHighlightInRect:]](https://developer.apple.com/documentation/appkit/nstextfinder/1526120-drawincrementalmatchhighlight)Added [NSTextFinder.findBarContainer](https://developer.apple.com/documentation/appkit/nstextfinder/1526748-findbarcontainer)Added [NSTextFinder.findIndicatorNeedsUpdate](https://developer.apple.com/documentation/appkit/nstextfinder/1534431-findindicatorneedsupdate)Added [NSTextFinder.incrementalMatchRanges](https://developer.apple.com/documentation/appkit/nstextfinder/1528304-incrementalmatchranges)Added [NSTextFinder.incrementalSearchingEnabled](https://developer.apple.com/documentation/appkit/nstextfinder/1535849-isincrementalsearchingenabled)Added [NSTextFinder.incrementalSearchingShouldDimContentView](https://developer.apple.com/documentation/appkit/nstextfinder/1528196-incrementalsearchingshoulddimcon)Added [-[NSTextFinder init]](https://developer.apple.com/documentation/appkit/nstextfinder/1535019-init)Added [-[NSTextFinder noteClientStringWillChange]](https://developer.apple.com/documentation/appkit/nstextfinder/1534184-noteclientstringwillchange)Added [-[NSTextFinder performAction:]](https://developer.apple.com/documentation/appkit/nstextfinder/1526414-performaction)Added [-[NSTextFinder validateAction:]](https://developer.apple.com/documentation/appkit/nstextfinder/1527203-validateaction)Added [NSTextFinderBarContainer](https://developer.apple.com/documentation/appkit/nstextfinderbarcontainer)Added [-[NSTextFinderBarContainer contentView]](https://developer.apple.com/documentation/appkit/nstextfinderbarcontainer/1532766-contentview)Added [NSTextFinderBarContainer.findBarView](https://developer.apple.com/documentation/appkit/nstextfinderbarcontainer/1531692-findbarview)Added [-[NSTextFinderBarContainer findBarViewDidChangeHeight]](https://developer.apple.com/documentation/appkit/nstextfinderbarcontainer/1529109-findbarviewdidchangeheight)Added [NSTextFinderBarContainer.findBarVisible](https://developer.apple.com/documentation/appkit/nstextfinderbarcontainer/1528587-findbarvisible)Added [NSTextFinderClient](https://developer.apple.com/documentation/appkit/nstextfinderclient)Added [NSTextFinderClient.allowsMultipleSelection](https://developer.apple.com/documentation/appkit/nstextfinderclient/1530815-allowsmultipleselection)Added [-[NSTextFinderClient contentViewAtIndex:effectiveCharacterRange:]](https://developer.apple.com/documentation/appkit/nstextfinderclient/1524830-contentview)Added [-[NSTextFinderClient didReplaceCharacters]](https://developer.apple.com/documentation/appkit/nstextfinderclient/1534301-didreplacecharacters)Added [-[NSTextFinderClient drawCharactersInRange:forContentView:]](https://developer.apple.com/documentation/appkit/nstextfinderclient/1533760-drawcharactersinrange)Added [NSTextFinderClient.editable](https://developer.apple.com/documentation/appkit/nstextfinderclient/1528515-editable)Added [NSTextFinderClient.firstSelectedRange](https://developer.apple.com/documentation/appkit/nstextfinderclient/1526936-firstselectedrange)Added [-[NSTextFinderClient rectsForCharacterRange:]](https://developer.apple.com/documentation/appkit/nstextfinderclient/1529980-rects)Added [-[NSTextFinderClient replaceCharactersInRange:withString:]](https://developer.apple.com/documentation/appkit/nstextfinderclient/1527702-replacecharactersinrange)Added [-[NSTextFinderClient scrollRangeToVisible:]](https://developer.apple.com/documentation/appkit/nstextfinderclient/1526989-scrollrangetovisible)Added [NSTextFinderClient.selectable](https://developer.apple.com/documentation/appkit/nstextfinderclient/1533766-selectable)Added [NSTextFinderClient.selectedRanges](https://developer.apple.com/documentation/appkit/nstextfinderclient/1524696-selectedranges)Added [-[NSTextFinderClient shouldReplaceCharactersInRanges:withStrings:]](https://developer.apple.com/documentation/appkit/nstextfinderclient/1529811-shouldreplacecharacters)Added [NSTextFinderClient.string](https://developer.apple.com/documentation/appkit/nstextfinderclient/1529462-string)Added [-[NSTextFinderClient stringAtIndex:effectiveRange:endsWithSearchBoundary:]](https://developer.apple.com/documentation/appkit/nstextfinderclient/1529466-string)Added [-[NSTextFinderClient stringLength]](https://developer.apple.com/documentation/appkit/nstextfinderclient/1534333-stringlength)Added [NSTextFinderClient.visibleCharacterRanges](https://developer.apple.com/documentation/appkit/nstextfinderclient/1524834-visiblecharacterranges)Added [NSTextFinderAction](https://developer.apple.com/documentation/appkit/nstextfinder/action)Added [NSTextFinderActionHideFindInterface](https://developer.apple.com/documentation/appkit/nstextfinderaction/nstextfinderactionhidefindinterface)Added [NSTextFinderActionHideReplaceInterface](https://developer.apple.com/documentation/appkit/nstextfinderaction/nstextfinderactionhidereplaceinterface)Added [NSTextFinderActionNextMatch](https://developer.apple.com/documentation/appkit/nstextfinderaction/nstextfinderactionnextmatch)Added [NSTextFinderActionPreviousMatch](https://developer.apple.com/documentation/appkit/nstextfinderaction/nstextfinderactionpreviousmatch)Added [NSTextFinderActionReplace](https://developer.apple.com/documentation/appkit/nstextfinder/action/replace)Added [NSTextFinderActionReplaceAll](https://developer.apple.com/documentation/appkit/nstextfinder/action/replaceall)Added [NSTextFinderActionReplaceAllInSelection](https://developer.apple.com/documentation/appkit/nstextfinder/action/replaceallinselection)Added [NSTextFinderActionReplaceAndFind](https://developer.apple.com/documentation/appkit/nstextfinderaction/nstextfinderactionreplaceandfind)Added [NSTextFinderActionSelectAll](https://developer.apple.com/documentation/appkit/nstextfinder/action/selectall)Added [NSTextFinderActionSelectAllInSelection](https://developer.apple.com/documentation/appkit/nstextfinderaction/nstextfinderactionselectallinselection)Added [NSTextFinderActionSetSearchString](https://developer.apple.com/documentation/appkit/nstextfinderaction/nstextfinderactionsetsearchstring)Added [NSTextFinderActionShowFindInterface](https://developer.apple.com/documentation/appkit/nstextfinderaction/nstextfinderactionshowfindinterface)Added [NSTextFinderActionShowReplaceInterface](https://developer.apple.com/documentation/appkit/nstextfinder/action/showreplaceinterface)Added [NSTextFinderCaseInsensitiveKey](https://developer.apple.com/documentation/appkit/nstextfindercaseinsensitivekey)Added [NSTextFinderMatchingType](https://developer.apple.com/documentation/appkit/nstextfinder/matchingtype)Added [NSTextFinderMatchingTypeContains](https://developer.apple.com/documentation/appkit/nstextfindermatchingtype/nstextfindermatchingtypecontains)Added [NSTextFinderMatchingTypeEndsWith](https://developer.apple.com/documentation/appkit/nstextfindermatchingtype/nstextfindermatchingtypeendswith)Added [NSTextFinderMatchingTypeFullWord](https://developer.apple.com/documentation/appkit/nstextfindermatchingtype/nstextfindermatchingtypefullword)Added [NSTextFinderMatchingTypeKey](https://developer.apple.com/documentation/appkit/nspasteboard/pasteboardtype/textfinderoptionkey/1533736-textfindermatchingtypekey)Added [NSTextFinderMatchingTypeStartsWith](https://developer.apple.com/documentation/appkit/nstextfindermatchingtype/nstextfindermatchingtypestartswith)NSTextView.hAdded [-[NSTextView changeLayoutOrientation:]](https://developer.apple.com/documentation/appkit/nstextview/1449286-changelayoutorientation)Added [-[NSTextView isIncrementalSearchingEnabled]](https://developer.apple.com/documentation/appkit/nstextview/1449458-incrementalsearchingenabled)Added [-[NSTextView quickLookPreviewableItemsInRanges:]](https://developer.apple.com/documentation/appkit/nstextview/1449426-quicklookpreviewableitemsinrange)Added [-[NSTextView setIncrementalSearchingEnabled:]](https://developer.apple.com/documentation/appkit/nstextview/1449458-incrementalsearchingenabled)Added [-[NSTextView setLayoutOrientation:]](https://developer.apple.com/documentation/appkit/nstextview/1449483-setlayoutorientation)Added [-[NSTextView setUsesFindBar:]](https://developer.apple.com/documentation/appkit/nstextview/1449456-usesfindbar)Added [-[NSTextView setUsesInspectorBar:]](https://developer.apple.com/documentation/appkit/nstextview/1449407-usesinspectorbar)Added [-[NSTextView toggleQuickLookPreviewPanel:]](https://developer.apple.com/documentation/appkit/nstextview/1449415-togglequicklookpreviewpanel)Added [-[NSTextView updateQuickLookPreviewPanel]](https://developer.apple.com/documentation/appkit/nstextview/1449409-updatequicklookpreviewpanel)Added [-[NSTextView usesFindBar]](https://developer.apple.com/documentation/appkit/nstextview/1449456-usesfindbar)Added [-[NSTextView usesInspectorBar]](https://developer.apple.com/documentation/appkit/nstextview/1449407-usesinspectorbar)Added [-[NSTextViewDelegate textView:URLForContentsOfTextAttachment:atIndex:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449194-textview)Added NSTextView(NSQuickLookPreview)Modified [NSTextView](https://developer.apple.com/documentation/appkit/nstextview)

|  | Protocols |
| --- | --- |
| From | NSTextInput, NSUserInterfaceValidations, NSTextInputClient |
| To | NSDraggingSource, NSTextInput, NSTextInputClient, NSTextLayoutOrientationProvider, NSUserInterfaceValidations |

NSUserInterfaceItemIdentification.hAdded [NSUserInterfaceItemIdentification](https://developer.apple.com/documentation/appkit/nsuserinterfaceitemidentification)Added [NSUserInterfaceItemIdentification.identifier](https://developer.apple.com/documentation/appkit/nsuserinterfaceitemidentification/1396829-identifier)NSView.hAdded [-[NSView backingAlignedRect:options:]](https://developer.apple.com/documentation/appkit/nsview/1483321-backingalignedrect)Added [-[NSView beginDraggingSessionWithItems:event:source:]](https://developer.apple.com/documentation/appkit/nsview/1483791-begindraggingsession)Added [-[NSView convertPointFromBacking:]](https://developer.apple.com/documentation/appkit/nsview/1483456-convertpointfrombacking)Added [-[NSView convertPointFromLayer:]](https://developer.apple.com/documentation/appkit/nsview/1483554-convertpointfromlayer)Added [-[NSView convertPointToBacking:]](https://developer.apple.com/documentation/appkit/nsview/1483803-converttobacking)Added [-[NSView convertPointToLayer:]](https://developer.apple.com/documentation/appkit/nsview/1483315-convertpointtolayer)Added [-[NSView convertRectFromBacking:]](https://developer.apple.com/documentation/appkit/nsview/1483819-convertrectfrombacking)Added [-[NSView convertRectFromLayer:]](https://developer.apple.com/documentation/appkit/nsview/1483404-convertrectfromlayer)Added [-[NSView convertRectToBacking:]](https://developer.apple.com/documentation/appkit/nsview/1483648-convertrecttobacking)Added [-[NSView convertRectToLayer:]](https://developer.apple.com/documentation/appkit/nsview/1483776-converttolayer)Added [-[NSView convertSizeFromBacking:]](https://developer.apple.com/documentation/appkit/nsview/1483319-convertfrombacking)Added [-[NSView convertSizeFromLayer:]](https://developer.apple.com/documentation/appkit/nsview/1483479-convertsizefromlayer)Added [-[NSView convertSizeToBacking:]](https://developer.apple.com/documentation/appkit/nsview/1483227-convertsizetobacking)Added [-[NSView convertSizeToLayer:]](https://developer.apple.com/documentation/appkit/nsview/1483701-convertsizetolayer)Added [-[NSView drawFocusRingMask]](https://developer.apple.com/documentation/appkit/nsview/1483335-drawfocusringmask)Added [-[NSView focusRingMaskBounds]](https://developer.apple.com/documentation/appkit/nsview/1483287-focusringmaskbounds)Added [-[NSView isDrawingFindIndicator]](https://developer.apple.com/documentation/appkit/nsview/1483317-drawingfindindicator)Added [-[NSView noteFocusRingMaskChanged]](https://developer.apple.com/documentation/appkit/nsview/1483809-notefocusringmaskchanged)Added NSView(NSFindIndicator)Modified [NSView](https://developer.apple.com/documentation/appkit/nsview)

|  | Protocols |
| --- | --- |
| From | NSAnimatablePropertyContainer |
| To | NSAnimatablePropertyContainer, NSDraggingDestination, NSUserInterfaceItemIdentification |

NSWindow.hAdded [-[NSWindow animationBehavior]](https://developer.apple.com/documentation/appkit/nswindow/1419763-animationbehavior)Added [-[NSWindow backingAlignedRect:options:]](https://developer.apple.com/documentation/appkit/nswindow/1419319-backingalignedrect)Added [-[NSWindow backingScaleFactor]](https://developer.apple.com/documentation/appkit/nswindow/1419459-backingscalefactor)Added [-[NSWindow convertRectFromBacking:]](https://developer.apple.com/documentation/appkit/nswindow/1419273-convertfrombacking)Added [-[NSWindow convertRectFromScreen:]](https://developer.apple.com/documentation/appkit/nswindow/1419603-convertfromscreen)Added [-[NSWindow convertRectToBacking:]](https://developer.apple.com/documentation/appkit/nswindow/1419260-converttobacking)Added [-[NSWindow convertRectToScreen:]](https://developer.apple.com/documentation/appkit/nswindow/1419286-convertrecttoscreen)Added [-[NSWindow setAnimationBehavior:]](https://developer.apple.com/documentation/appkit/nswindow/1419763-animationbehavior)Added [-[NSWindow toggleFullScreen:]](https://developer.apple.com/documentation/appkit/nswindow/1419527-togglefullscreen)Added [-[NSWindowDelegate customWindowsToEnterFullScreenForWindow:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419521-customwindowstoenterfullscreen)Added [-[NSWindowDelegate customWindowsToExitFullScreenForWindow:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419070-customwindowstoexitfullscreenfor)Added [-[NSWindowDelegate window:didDecodeRestorableState:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419475-window)Added [-[NSWindowDelegate window:startCustomAnimationToEnterFullScreenWithDuration:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419406-window)Added [-[NSWindowDelegate window:startCustomAnimationToExitFullScreenWithDuration:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419705-window)Added [-[NSWindowDelegate window:willEncodeRestorableState:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419619-window)Added -[NSWindowDelegate window:willResizeForVersionBrowserWithMaxPreferredSize:]Added [-[NSWindowDelegate window:willUseFullScreenContentSize:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419282-window)Added [-[NSWindowDelegate window:willUseFullScreenPresentationOptions:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419144-window)Added [-[NSWindowDelegate windowDidEnterFullScreen:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419116-windowdidenterfullscreen)Added [-[NSWindowDelegate windowDidEnterVersionBrowser:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419064-windowdidenterversionbrowser)Added [-[NSWindowDelegate windowDidExitFullScreen:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419146-windowdidexitfullscreen)Added [-[NSWindowDelegate windowDidExitVersionBrowser:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419501-windowdidexitversionbrowser)Added [-[NSWindowDelegate windowDidFailToEnterFullScreen:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419591-windowdidfailtoenterfullscreen)Added [-[NSWindowDelegate windowDidFailToExitFullScreen:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419573-windowdidfailtoexitfullscreen)Added [-[NSWindowDelegate windowWillEnterFullScreen:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419563-windowwillenterfullscreen)Added [-[NSWindowDelegate windowWillEnterVersionBrowser:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419463-windowwillenterversionbrowser)Added [-[NSWindowDelegate windowWillExitFullScreen:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419332-windowwillexitfullscreen)Added [-[NSWindowDelegate windowWillExitVersionBrowser:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419252-windowwillexitversionbrowser)Added [NSFullScreenWindowMask](https://developer.apple.com/documentation/appkit/nsfullscreenwindowmask)Added [NSWindowAnimationBehavior](https://developer.apple.com/documentation/appkit/nswindow/animationbehavior)Added [NSWindowAnimationBehaviorAlertPanel](https://developer.apple.com/documentation/appkit/nswindow/animationbehavior/alertpanel)Added [NSWindowAnimationBehaviorDefault](https://developer.apple.com/documentation/appkit/nswindowanimationbehavior/nswindowanimationbehaviordefault)Added [NSWindowAnimationBehaviorDocumentWindow](https://developer.apple.com/documentation/appkit/nswindow/animationbehavior/documentwindow)Added [NSWindowAnimationBehaviorNone](https://developer.apple.com/documentation/appkit/nswindow/animationbehavior/none)Added [NSWindowAnimationBehaviorUtilityWindow](https://developer.apple.com/documentation/appkit/nswindowanimationbehavior/nswindowanimationbehaviorutilitywindow)Added [NSWindowCollectionBehaviorFullScreenAuxiliary](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior/1419617-fullscreenauxiliary)Added [NSWindowCollectionBehaviorFullScreenPrimary](https://developer.apple.com/documentation/appkit/nswindowcollectionbehavior/nswindowcollectionbehaviorfullscreenprimary)Added [NSWindowDidEnterFullScreenNotification](https://developer.apple.com/documentation/appkit/nswindowdidenterfullscreennotification)Added [NSWindowDidEnterVersionBrowserNotification](https://developer.apple.com/documentation/appkit/nswindowdidenterversionbrowsernotification)Added [NSWindowDidExitFullScreenNotification](https://developer.apple.com/documentation/appkit/nswindowdidexitfullscreennotification)Added [NSWindowDidExitVersionBrowserNotification](https://developer.apple.com/documentation/appkit/nswindowdidexitversionbrowsernotification)Added [NSWindowDocumentVersionsButton](https://developer.apple.com/documentation/appkit/nswindowbutton/nswindowdocumentversionsbutton)Added [NSWindowFullScreenButton](https://developer.apple.com/documentation/appkit/nswindowfullscreenbutton)Added [NSWindowWillEnterFullScreenNotification](https://developer.apple.com/documentation/appkit/nswindow/1419589-willenterfullscreennotification)Added [NSWindowWillEnterVersionBrowserNotification](https://developer.apple.com/documentation/appkit/nswindow/1419761-willenterversionbrowsernotificat)Added [NSWindowWillExitFullScreenNotification](https://developer.apple.com/documentation/appkit/nswindowwillexitfullscreennotification)Added [NSWindowWillExitVersionBrowserNotification](https://developer.apple.com/documentation/appkit/nswindow/1419278-willexitversionbrowsernotificati)Modified -[NSWindow setCanBeVisibleOnAllSpaces:]

|  | Declaration |
| --- | --- |
| From | - (void)setCanBeVisibleOnAllSpaces:(BOOL)flag |
| To | - (void)setCanBeVisibleOnAllSpaces:(BOOL)__AVAILABILITY_INTERNAL__MAC_10_5_DEP__MAC_10_5 |

Modified -[NSWindow canBeVisibleOnAllSpaces]

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | Both | i386,ppc,x86_64 |
| To | _Unknown_ | Unknown |

Modified [NSWindow](https://developer.apple.com/documentation/appkit/nswindow)

|  | Protocols |
| --- | --- |
| From | NSUserInterfaceValidations, NSAnimatablePropertyContainer |
| To | NSAnimatablePropertyContainer, NSUserInterfaceItemIdentification, NSUserInterfaceValidations |

NSWindowRestoration.hAdded [-[NSApplication completeStateRestoration]](https://developer.apple.com/documentation/appkit/nsapplication/1526245-completestaterestoration)Added [-[NSApplication extendStateRestoration]](https://developer.apple.com/documentation/appkit/nsapplication/1526248-extendstaterestoration)Added [-[NSApplication restoreWindowWithIdentifier:state:completionHandler:]](https://developer.apple.com/documentation/appkit/nsapplication/1526233-restorewindowwithidentifier)Added [-[NSDocument encodeRestorableStateWithCoder:]](https://developer.apple.com/documentation/appkit/nsdocument/1526257-encoderestorablestate)Added [-[NSDocument invalidateRestorableState]](https://developer.apple.com/documentation/appkit/nsdocument/1526250-invalidaterestorablestate)Added [+[NSDocument restorableStateKeyPaths]](https://developer.apple.com/documentation/appkit/nsdocument/1526232-restorablestatekeypaths)Added [-[NSDocument restoreDocumentWindowWithIdentifier:state:completionHandler:]](https://developer.apple.com/documentation/appkit/nsdocument/1524586-restoredocumentwindowwithidentif)Added [-[NSDocument restoreStateWithCoder:]](https://developer.apple.com/documentation/appkit/nsdocument/1526237-restorestate)Added [-[NSResponder encodeRestorableStateWithCoder:]](https://developer.apple.com/documentation/appkit/nsresponder/1526236-encoderestorablestate)Added [-[NSResponder invalidateRestorableState]](https://developer.apple.com/documentation/appkit/nsresponder/1526243-invalidaterestorablestate)Added [+[NSResponder restorableStateKeyPaths]](https://developer.apple.com/documentation/appkit/nsresponder/1526242-restorablestatekeypaths)Added [-[NSResponder restoreStateWithCoder:]](https://developer.apple.com/documentation/appkit/nsresponder/1526253-restorestate)Added [-[NSWindow disableSnapshotRestoration]](https://developer.apple.com/documentation/appkit/nswindow/1526239-disablesnapshotrestoration)Added [-[NSWindow enableSnapshotRestoration]](https://developer.apple.com/documentation/appkit/nswindow/1525288-enablesnapshotrestoration)Added [-[NSWindow isRestorable]](https://developer.apple.com/documentation/appkit/nswindow/1526255-isrestorable)Added [-[NSWindow restorationClass]](https://developer.apple.com/documentation/appkit/nswindow/1526241-restorationclass)Added [-[NSWindow setRestorable:]](https://developer.apple.com/documentation/appkit/nswindow/1526255-restorable)Added [-[NSWindow setRestorationClass:]](https://developer.apple.com/documentation/appkit/nswindow/1526241-restorationclass)Added [NSWindowRestoration](https://developer.apple.com/documentation/appkit/nswindowrestoration)Added [+[NSWindowRestoration restoreWindowWithIdentifier:state:completionHandler:]](https://developer.apple.com/documentation/appkit/nswindowrestoration/1526251-restorewindowwithidentifier)Added NSApplication(NSRestorableStateExtension)Added NSApplication(NSWindowRestoration)Added [NSApplicationDidFinishRestoringWindowsNotification](https://developer.apple.com/documentation/appkit/nsapplication/1526252-didfinishrestoringwindowsnotific)Added NSDocument(NSRestorableState)Added NSDocumentController(NSWindowRestoration)Added NSResponder(NSRestorableState)Added NSWindow(NSUserInterfaceRestoration)NSWorkspace.hAdded [-[NSWorkspace frontmostApplication]](https://developer.apple.com/documentation/appkit/nsworkspace/1532097-frontmostapplication)Added [-[NSWorkspace menuBarOwningApplication]](https://developer.apple.com/documentation/appkit/nsworkspace/1525848-menubarowningapplication)Modified [-[NSWorkspace activeApplication]](https://developer.apple.com/documentation/appkit/nsworkspace/1530411-activeapplication)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [-[NSWorkspace launchedApplications]](https://developer.apple.com/documentation/appkit/nsworkspace/1579272-launchedapplications)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

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
