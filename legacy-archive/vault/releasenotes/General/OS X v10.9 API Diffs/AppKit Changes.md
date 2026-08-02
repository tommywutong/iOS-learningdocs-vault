---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/AppKit.html
archived_at: '2026-07-18T02:54:08.334755Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# AppKit Changes

## AppKit

AppKitDefines.hAdded #def APPKIT_PRIVATEAppKitErrors.hAdded [NSSharingServiceErrorMaximum](https://developer.apple.com/documentation/appkit/1534813-appkit_errors/nssharingserviceerrormaximum)Added [NSSharingServiceErrorMinimum](https://developer.apple.com/documentation/appkit/1534813-appkit_errors/nssharingserviceerrorminimum)Added [NSSharingServiceNotConfiguredError](https://developer.apple.com/documentation/appkit/1534813-appkit_errors/nssharingservicenotconfigurederror)NSAccessibility.hAdded [-[NSObject accessibilityNotifiesWhenDestroyed]](https://developer.apple.com/documentation/objectivec/nsobject/1534050-accessibilitynotifieswhendestroy)Added [NSAccessibilityAnnouncementKey](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationuserinfokey/1528310-announcement)Added [NSAccessibilityAnnouncementRequestedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1530633-announcementrequested)Added [NSAccessibilityContainsProtectedContentAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitycontainsprotectedcontentattribute)Added [NSAccessibilityDescriptionListSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysubrole/1532769-descriptionlist)Added [NSAccessibilityLayoutChangedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1524251-layoutchanged)Added [NSAccessibilityMarkedMisspelledTextAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitymarkedmisspelledtextattribute)Added [NSAccessibilityPostNotificationWithUserInfo()](https://developer.apple.com/documentation/appkit/1534572-nsaccessibilitypostnotificationw)Added [NSAccessibilityPriorityHigh](https://developer.apple.com/documentation/appkit/nsaccessibilityprioritylevel/nsaccessibilitypriorityhigh)Added [NSAccessibilityPriorityKey](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationuserinfokey/1531038-priority)Added [NSAccessibilityPriorityLevel](https://developer.apple.com/documentation/appkit/nsaccessibilityprioritylevel)Added [NSAccessibilityPriorityLow](https://developer.apple.com/documentation/appkit/nsaccessibilityprioritylevel/low)Added [NSAccessibilityPriorityMedium](https://developer.apple.com/documentation/appkit/nsaccessibilityprioritylevel/nsaccessibilityprioritymedium)Added [NSAccessibilitySetMayContainProtectedContent()](https://developer.apple.com/documentation/appkit/1533132-nsaccessibilitysetmaycontainprot)Added [NSAccessibilityShowAlternateUIAction](https://developer.apple.com/documentation/appkit/nsaccessibilityshowalternateuiaction)Added [NSAccessibilityShowDefaultUIAction](https://developer.apple.com/documentation/appkit/nsaccessibilityactionname/1526573-showdefaultui)Added [NSAccessibilitySwitchSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilityswitchsubrole)Added [NSAccessibilityToggleSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysubrole/1525391-toggle)Added [NSAccessibilityUIElementsKey](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationuserinfokey/1534944-uielements)NSAlert.hAdded [-[NSAlert beginSheetModalForWindow:completionHandler:]](https://developer.apple.com/documentation/appkit/nsalert/1524296-beginsheetmodal)Modified [-[NSAlert runModal]](https://developer.apple.com/documentation/appkit/nsalert/1535441-runmodal)

|  | Declaration |
| --- | --- |
| From | - (NSInteger)runModal |
| To | - (NSModalResponse)runModal |

NSAnimation.hModified [-[NSAnimatablePropertyContainer animator]](https://developer.apple.com/documentation/appkit/nsanimatablepropertycontainer/1530511-animator)

|  | Declaration |
| --- | --- |
| From | - (id)animator |
| To | - (instancetype)animator |

NSAppearance.hAdded [NSAppearance](https://developer.apple.com/documentation/appkit/nsappearance)Added [+[NSAppearance appearanceNamed:]](https://developer.apple.com/documentation/appkit/nsappearance/1529612-appearancenamed)Added [+[NSAppearance currentAppearance]](https://developer.apple.com/documentation/appkit/nsappearance/1531945-currentappearance)Added [-[NSAppearance initWithAppearanceNamed:bundle:]](https://developer.apple.com/documentation/appkit/nsappearance/1529131-init)Added +[NSAppearance setCurrentAppearance:]Added [NSAppearanceCustomization](https://developer.apple.com/documentation/appkit/nsappearancecustomization)Added [NSAppearanceCustomization.appearance](https://developer.apple.com/documentation/appkit/nsappearancecustomization/1533925-appearance)Added [NSAppearanceCustomization.effectiveAppearance](https://developer.apple.com/documentation/appkit/nsappearancecustomization/1535147-effectiveappearance)Added [NSAppearanceNameAqua](https://developer.apple.com/documentation/appkit/nsappearance/name/1534115-aqua)Added [NSAppearanceNameLightContent](https://developer.apple.com/documentation/appkit/nsappearance/name/1527091-lightcontent)NSApplication.hRemoved [-[NSObject readSelectionFromPasteboard:]](https://developer.apple.com/documentation/appkit/nsservicesmenurequestor/1428481-readselection)Removed [-[NSObject writeSelectionToPasteboard:types:]](https://developer.apple.com/documentation/appkit/nsservicesmenurequestor/1428477-writeselection)Removed NSObject(NSServicesRequests)Added [-[NSApplication occlusionState]](https://developer.apple.com/documentation/appkit/nsapplication/1428656-occlusionstate)Added [-[NSApplicationDelegate applicationDidChangeOcclusionState:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428362-applicationdidchangeocclusionsta)Added [NSServicesMenuRequestor](https://developer.apple.com/documentation/appkit/nsservicesmenurequestor)Added [-[NSServicesMenuRequestor readSelectionFromPasteboard:]](https://developer.apple.com/documentation/appkit/nsservicesmenurequestor/1428481-readselection)Added [-[NSServicesMenuRequestor writeSelectionToPasteboard:types:]](https://developer.apple.com/documentation/appkit/nsservicesmenurequestor/1428477-writeselection)Added [#def NSAppKitVersionNumber10_7_3](https://developer.apple.com/documentation/appkit/nsappkitversion/1428412-macos10_7_3)Added [#def NSAppKitVersionNumber10_7_4](https://developer.apple.com/documentation/appkit/nsappkitversion/1428650-macos10_7_4)Added [#def NSAppKitVersionNumber10_8](https://developer.apple.com/documentation/appkit/nsappkitversionnumber10_8)Added [NSApplicationDidChangeOcclusionStateNotification](https://developer.apple.com/documentation/appkit/nsapplication/1428627-didchangeocclusionstatenotificat)Added [NSApplicationOcclusionState](https://developer.apple.com/documentation/appkit/nsapplication/occlusionstate)Added [NSApplicationOcclusionStateVisible](https://developer.apple.com/documentation/appkit/nsapplicationocclusionstate/nsapplicationocclusionstatevisible)Added [NSModalResponse](https://developer.apple.com/documentation/appkit/nsapplication/modalresponse)Added [NSModalResponseAbort](https://developer.apple.com/documentation/appkit/nsmodalresponseabort)Added [NSModalResponseContinue](https://developer.apple.com/documentation/appkit/nsmodalresponsecontinue)Added [NSModalResponseStop](https://developer.apple.com/documentation/appkit/nsmodalresponsestop)Modified [-[NSApplication beginSheet:modalForWindow:modalDelegate:didEndSelector:contextInfo:]](https://developer.apple.com/documentation/appkit/nsapplication/1428505-beginsheet)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSApplication endSheet:]](https://developer.apple.com/documentation/appkit/nsapplication/1428503-endsheet)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSApplication endSheet:returnCode:]](https://developer.apple.com/documentation/appkit/nsapplication/1428629-endsheet)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

NSAttributedString.hModified [NSUnderlineStrikethroughMask](https://developer.apple.com/documentation/appkit/nsunderlinestrikethroughmask)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

NSBox.hRemoved NSBox(NSCustomBoxTypeProperties)Removed NSBox(NSKeyboardUI)Added NSBox(NSDeprecated)NSButtonCell.hModified [NSMomentaryLight](https://developer.apple.com/documentation/appkit/nsmomentarylight)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [NSMomentaryPushButton](https://developer.apple.com/documentation/appkit/nsmomentarypushbutton)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [NSSmallIconButtonBezelStyle](https://developer.apple.com/documentation/appkit/nssmalliconbuttonbezelstyle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.0 |

NSClipView.hAdded [-[NSClipView constrainBoundsRect:]](https://developer.apple.com/documentation/appkit/nsclipview/1534160-constrainboundsrect)Added NSClipView(NSDeprecated)Modified [-[NSClipView constrainScrollPoint:]](https://developer.apple.com/documentation/appkit/nsclipview/1526678-constrainscroll)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

NSColor.hAdded [+[NSColor colorWithHue:saturation:brightness:alpha:]](https://developer.apple.com/documentation/appkit/nscolor/1530601-colorwithhue)Added [+[NSColor colorWithRed:green:blue:alpha:]](https://developer.apple.com/documentation/appkit/nscolor/1535804-init)Added [+[NSColor colorWithWhite:alpha:]](https://developer.apple.com/documentation/appkit/nscolor/1525501-colorwithwhite)Modified [-[NSCoder decodeNXColor]](https://developer.apple.com/documentation/foundation/nscoder/1551277-decodenxcolor)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

NSControl.hAdded -[NSControl setUserInterfaceLayoutDirection:]Added -[NSControl userInterfaceLayoutDirection]NSDocument.hAdded [-[NSDocument PDFPrintOperation]](https://developer.apple.com/documentation/appkit/nsdocument/1515246-pdfprintoperation)Added [-[NSDocument saveDocumentToPDF:]](https://developer.apple.com/documentation/appkit/nsdocument/1515176-savedocumenttopdf)NSFont.hModified NSGlyphRelation

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.4 |

NSImage.hAdded [-[NSImage drawInRect:]](https://developer.apple.com/documentation/appkit/nsimage/1519863-drawinrect)NSInterfaceStyle.hModified [NSInterfaceStyle](https://developer.apple.com/documentation/appkit/nsinterfacestyle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

NSLayoutConstraint.hAdded [NSLayoutConstraint.identifier](https://developer.apple.com/documentation/uikit/nslayoutconstraint/1526879-identifier)Added NSLayoutConstraint(NSIdentifier)NSMediaLibraryBrowserController.hAdded [NSMediaLibraryBrowserController](https://developer.apple.com/documentation/appkit/nsmedialibrarybrowsercontroller)Added [NSMediaLibraryBrowserController.frame](https://developer.apple.com/documentation/appkit/nsmedialibrarybrowsercontroller/1423477-frame)Added [NSMediaLibraryBrowserController.mediaLibraries](https://developer.apple.com/documentation/appkit/nsmedialibrarybrowsercontroller/1423481-medialibraries)Added [+[NSMediaLibraryBrowserController sharedMediaLibraryBrowserController]](https://developer.apple.com/documentation/appkit/nsmedialibrarybrowsercontroller/1423485-shared)Added [-[NSMediaLibraryBrowserController togglePanel:]](https://developer.apple.com/documentation/appkit/nsmedialibrarybrowsercontroller/1423479-togglepanel)Added [NSMediaLibraryBrowserController.visible](https://developer.apple.com/documentation/appkit/nsmedialibrarybrowsercontroller/1423473-visible)Added [NSMediaLibrary](https://developer.apple.com/documentation/appkit/nsmedialibrarybrowsercontroller/library)Added [NSMediaLibraryAudio](https://developer.apple.com/documentation/appkit/nsmedialibrarybrowsercontroller/library/1423470-audio)Added [NSMediaLibraryImage](https://developer.apple.com/documentation/appkit/nsmedialibrary/nsmedialibraryimage)Added [NSMediaLibraryMovie](https://developer.apple.com/documentation/appkit/nsmedialibrary/nsmedialibrarymovie)NSNib.hModified [NSNibOwner](https://developer.apple.com/documentation/appkit/nsnibowner)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [NSNibTopLevelObjects](https://developer.apple.com/documentation/appkit/nsnibtoplevelobjects)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

NSOutlineView.hAdded [-[NSOutlineView setUserInterfaceLayoutDirection:]](https://developer.apple.com/documentation/appkit/nsoutlineview/1524564-userinterfacelayoutdirection)Added [-[NSOutlineView userInterfaceLayoutDirection]](https://developer.apple.com/documentation/appkit/nsoutlineview/1524564-userinterfacelayoutdirection)Added [NSOutlineViewDisclosureButtonKey](https://developer.apple.com/documentation/appkit/nsoutlineview/1532905-disclosurebuttonidentifier)Added [NSOutlineViewShowHideButtonKey](https://developer.apple.com/documentation/appkit/nsoutlineviewshowhidebuttonkey)NSPDFInfo.hAdded [NSPDFInfo](https://developer.apple.com/documentation/appkit/nspdfinfo)Added [NSPDFInfo.URL](https://developer.apple.com/documentation/appkit/nspdfinfo/1528885-url)Added [NSPDFInfo.attributes](https://developer.apple.com/documentation/appkit/nspdfinfo/1528715-attributes)Added [NSPDFInfo.fileExtensionHidden](https://developer.apple.com/documentation/appkit/nspdfinfo/1527208-fileextensionhidden)Added [NSPDFInfo.orientation](https://developer.apple.com/documentation/appkit/nspdfinfo/1524848-orientation)Added [NSPDFInfo.paperSize](https://developer.apple.com/documentation/appkit/nspdfinfo/1532272-papersize)Added [NSPDFInfo.tagNames](https://developer.apple.com/documentation/appkit/nspdfinfo/1525418-tagnames)NSPDFPanel.hAdded [NSPDFPanel](https://developer.apple.com/documentation/appkit/nspdfpanel)Added [NSPDFPanel.accessoryController](https://developer.apple.com/documentation/appkit/nspdfpanel/1524637-accessorycontroller)Added [-[NSPDFPanel beginSheetWithPDFInfo:modalForWindow:completionHandler:]](https://developer.apple.com/documentation/appkit/nspdfpanel/1529098-beginsheet)Added [NSPDFPanel.defaultFileName](https://developer.apple.com/documentation/appkit/nspdfpanel/1532720-defaultfilename)Added [NSPDFPanel.options](https://developer.apple.com/documentation/appkit/nspdfpanel/1532479-options)Added [+[NSPDFPanel panel]](https://developer.apple.com/documentation/appkit/nspdfpanel/1577141-panel)Added [NSPDFPanelOptions](https://developer.apple.com/documentation/appkit/nspdfpaneloptions)Added [NSPDFPanelRequestsParentDirectory](https://developer.apple.com/documentation/appkit/nspdfpanel/options/1531323-requestsparentdirectory)Added [NSPDFPanelShowsOrientation](https://developer.apple.com/documentation/appkit/nspdfpaneloptions/nspdfpanelshowsorientation)Added [NSPDFPanelShowsPaperSize](https://developer.apple.com/documentation/appkit/nspdfpanel/options/1525423-showspapersize)NSPrintInfo.hAdded [-[NSPrintInfo takeSettingsFromPDFInfo:]](https://developer.apple.com/documentation/appkit/nsprintinfo/1530099-takesettings)Added [NSPaperOrientation](https://developer.apple.com/documentation/appkit/nspaperorientation)Added [NSPaperOrientationLandscape](https://developer.apple.com/documentation/appkit/nsprintinfo/paperorientation/landscape)Added [NSPaperOrientationPortrait](https://developer.apple.com/documentation/appkit/nspaperorientation/nspaperorientationportrait)Modified [-[NSPrintInfo orientation]](https://developer.apple.com/documentation/appkit/nsprintinfo/1533755-orientation)

|  | Declaration |
| --- | --- |
| From | - (NSPrintingOrientation)orientation |
| To | - (NSPaperOrientation)orientation |

Modified [-[NSPrintInfo setOrientation:]](https://developer.apple.com/documentation/appkit/nsprintinfo/1533755-orientation)

|  | Declaration |
| --- | --- |
| From | - (void)setOrientation:(NSPrintingOrientation)orientation |
| To | - (void)setOrientation:(NSPaperOrientation)orientation |

NSPrintOperation.hAdded [-[NSPrintOperation PDFPanel]](https://developer.apple.com/documentation/appkit/nsprintoperation/1526838-pdfpanel)Added [-[NSPrintOperation setPDFPanel:]](https://developer.apple.com/documentation/appkit/nsprintoperation/1526838-pdfpanel)NSPrinter.hModified [-[NSPrinter booleanForKey:inTable:]](https://developer.apple.com/documentation/appkit/nsprinter/1525212-booleanforkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSPrinter floatForKey:inTable:]](https://developer.apple.com/documentation/appkit/nsprinter/1525195-floatforkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSPrinter intForKey:inTable:]](https://developer.apple.com/documentation/appkit/nsprinter/1525214-intforkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSPrinter isKey:inTable:]](https://developer.apple.com/documentation/appkit/nsprinter/1525200-iskey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSPrinter rectForKey:inTable:]](https://developer.apple.com/documentation/appkit/nsprinter/1525198-rectforkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSPrinter sizeForKey:inTable:]](https://developer.apple.com/documentation/appkit/nsprinter/1525205-sizeforkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSPrinter statusForTable:]](https://developer.apple.com/documentation/appkit/nsprinter/1525218-statusfortable)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSPrinter stringForKey:inTable:]](https://developer.apple.com/documentation/appkit/nsprinter/1525217-stringforkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSPrinter stringListForKey:inTable:]](https://developer.apple.com/documentation/appkit/nsprinter/1525219-stringlistforkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

NSSavePanel.hAdded [-[NSSavePanel setShowsTagField:]](https://developer.apple.com/documentation/appkit/nssavepanel/1525589-showstagfield)Added [-[NSSavePanel setTagNames:]](https://developer.apple.com/documentation/appkit/nssavepanel/1535928-tagnames)Added [-[NSSavePanel showsTagField]](https://developer.apple.com/documentation/appkit/nssavepanel/1525589-showstagfield)Added [-[NSSavePanel tagNames]](https://developer.apple.com/documentation/appkit/nssavepanel/1535928-tagnames)NSScreen.hAdded [+[NSScreen screensHaveSeparateSpaces]](https://developer.apple.com/documentation/appkit/nsscreen/1388365-screenshaveseparatespaces)NSScrollView.hAdded [-[NSScrollView addFloatingSubview:forAxis:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403546-addfloatingsubview)Added [NSScrollViewDidEndLiveScrollNotification](https://developer.apple.com/documentation/appkit/nsscrollviewdidendlivescrollnotification)Added [NSScrollViewDidLiveScrollNotification](https://developer.apple.com/documentation/appkit/nsscrollviewdidlivescrollnotification)Added [NSScrollViewWillStartLiveScrollNotification](https://developer.apple.com/documentation/appkit/nsscrollview/1403514-willstartlivescrollnotification)NSSharingService.hAdded [NSSharingService.accountName](https://developer.apple.com/documentation/appkit/nssharingservice/1402683-accountname)Added [NSSharingService.attachmentFileURLs](https://developer.apple.com/documentation/appkit/nssharingservice/1402707-attachmentfileurls)Added [NSSharingService.menuItemTitle](https://developer.apple.com/documentation/appkit/nssharingservice/1402693-menuitemtitle)Added [NSSharingService.messageBody](https://developer.apple.com/documentation/appkit/nssharingservice/1402644-messagebody)Added [NSSharingService.permanentLink](https://developer.apple.com/documentation/appkit/nssharingservice/1402685-permanentlink)Added [NSSharingService.recipients](https://developer.apple.com/documentation/appkit/nssharingservice/1402652-recipients)Added [NSSharingService.subject](https://developer.apple.com/documentation/appkit/nssharingservice/1402626-subject)Added [NSSharingServiceNamePostOnLinkedIn](https://developer.apple.com/documentation/appkit/nssharingservicenamepostonlinkedin)Added [NSSharingServiceNamePostOnTencentWeibo](https://developer.apple.com/documentation/appkit/nssharingservice/name/1402714-postontencentweibo)Added [NSSharingServiceNameUseAsFacebookProfileImage](https://developer.apple.com/documentation/appkit/nssharingservice/name/1402700-useasfacebookprofileimage)Added [NSSharingServiceNameUseAsLinkedInProfileImage](https://developer.apple.com/documentation/appkit/nssharingservicenameuseaslinkedinprofileimage)NSSlider.hModified [-[NSSlider image]](https://developer.apple.com/documentation/appkit/nsslider/1532906-image)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSSlider setImage:]](https://developer.apple.com/documentation/appkit/nsslider/1532926-setimage)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSSlider setKnobThickness:]](https://developer.apple.com/documentation/appkit/nsslider/1532899-setknobthickness)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSSlider setTitle:]](https://developer.apple.com/documentation/appkit/nsslider/1532915-settitle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSSlider setTitleCell:]](https://developer.apple.com/documentation/appkit/nsslider/1532904-settitlecell)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSSlider setTitleColor:]](https://developer.apple.com/documentation/appkit/nsslider/1532911-settitlecolor)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSSlider setTitleFont:]](https://developer.apple.com/documentation/appkit/nsslider/1532927-settitlefont)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSSlider title]](https://developer.apple.com/documentation/appkit/nsslider/1532913-title)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSSlider titleCell]](https://developer.apple.com/documentation/appkit/nsslider/1532902-titlecell)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSSlider titleColor]](https://developer.apple.com/documentation/appkit/nsslider/1532896-titlecolor)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSSlider titleFont]](https://developer.apple.com/documentation/appkit/nsslider/1532907-titlefont)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

NSSliderCell.hAdded [-[NSSliderCell barRectFlipped:]](https://developer.apple.com/documentation/appkit/nsslidercell/1444629-barrect)Added [-[NSSliderCell drawTickMarks]](https://developer.apple.com/documentation/appkit/nsslidercell/1444633-drawtickmarks)Modified [-[NSSliderCell setKnobThickness:]](https://developer.apple.com/documentation/appkit/nsslidercell/1444612-setknobthickness)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSSliderCell setTitle:]](https://developer.apple.com/documentation/appkit/nsslidercell/1444631-settitle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSSliderCell setTitleCell:]](https://developer.apple.com/documentation/appkit/nsslidercell/1444619-settitlecell)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSSliderCell setTitleColor:]](https://developer.apple.com/documentation/appkit/nsslidercell/1444637-settitlecolor)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSSliderCell setTitleFont:]](https://developer.apple.com/documentation/appkit/nsslidercell/1444623-settitlefont)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSSliderCell title]](https://developer.apple.com/documentation/appkit/nsslidercell/1444610-title)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSSliderCell titleCell]](https://developer.apple.com/documentation/appkit/nsslidercell/1444639-titlecell)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSSliderCell titleColor]](https://developer.apple.com/documentation/appkit/nsslidercell/1444577-titlecolor)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSSliderCell titleFont]](https://developer.apple.com/documentation/appkit/nsslidercell/1444591-titlefont)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

NSSound.hModified [-[NSSound channelMapping]](https://developer.apple.com/documentation/appkit/nssound/1477326-channelmapping)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSSound setChannelMapping:]](https://developer.apple.com/documentation/appkit/nssound/1477317-setchannelmapping)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

NSSpellChecker.hAdded +[NSSpellChecker isAutomaticDashSubstitutionEnabled]Added +[NSSpellChecker isAutomaticQuoteSubstitutionEnabled]Added [NSSpellCheckerDidChangeAutomaticDashSubstitutionNotification](https://developer.apple.com/documentation/appkit/nsspellcheckerdidchangeautomaticdashsubstitutionnotification)Added [NSSpellCheckerDidChangeAutomaticQuoteSubstitutionNotification](https://developer.apple.com/documentation/appkit/nsspellchecker/1534337-didchangeautomaticquotesubstitut)NSStackView.hAdded [NSStackView](https://developer.apple.com/documentation/appkit/nsstackview)Added [-[NSStackView addView:inGravity:]](https://developer.apple.com/documentation/appkit/nsstackview/1488897-addview)Added [NSStackView.alignment](https://developer.apple.com/documentation/appkit/nsstackview/1488906-alignment)Added [-[NSStackView clippingResistancePriorityForOrientation:]](https://developer.apple.com/documentation/appkit/nsstackview/1488936-clippingresistancepriority)Added [-[NSStackView customSpacingAfterView:]](https://developer.apple.com/documentation/appkit/nsstackview/1488888-customspacing)Added [NSStackView.delegate](https://developer.apple.com/documentation/appkit/nsstackview/1488946-delegate)Added [NSStackView.detachedViews](https://developer.apple.com/documentation/appkit/nsstackview/1488952-detachedviews)Added [NSStackView.edgeInsets](https://developer.apple.com/documentation/appkit/nsstackview/1488931-edgeinsets)Added [NSStackView.hasEqualSpacing](https://developer.apple.com/documentation/appkit/nsstackview/1488957-hasequalspacing)Added [-[NSStackView huggingPriorityForOrientation:]](https://developer.apple.com/documentation/appkit/nsstackview/1488912-huggingpriority)Added [-[NSStackView insertView:atIndex:inGravity:]](https://developer.apple.com/documentation/appkit/nsstackview/1488933-insertview)Added [NSStackView.orientation](https://developer.apple.com/documentation/appkit/nsstackview/1488950-orientation)Added [-[NSStackView removeView:]](https://developer.apple.com/documentation/appkit/nsstackview/1488916-removeview)Added [-[NSStackView setClippingResistancePriority:forOrientation:]](https://developer.apple.com/documentation/appkit/nsstackview/1488880-setclippingresistancepriority)Added [-[NSStackView setCustomSpacing:afterView:]](https://developer.apple.com/documentation/appkit/nsstackview/1488874-setcustomspacing)Added [-[NSStackView setHuggingPriority:forOrientation:]](https://developer.apple.com/documentation/appkit/nsstackview/1488904-sethuggingpriority)Added [-[NSStackView setViews:inGravity:]](https://developer.apple.com/documentation/appkit/nsstackview/1488883-setviews)Added [-[NSStackView setVisibilityPriority:forView:]](https://developer.apple.com/documentation/appkit/nsstackview/1488890-setvisibilitypriority)Added [NSStackView.spacing](https://developer.apple.com/documentation/appkit/nsstackview/1488945-spacing)Added [+[NSStackView stackViewWithViews:]](https://developer.apple.com/documentation/appkit/nsstackview/1488929-init)Added [NSStackView.views](https://developer.apple.com/documentation/appkit/nsstackview/1488914-views)Added [-[NSStackView viewsInGravity:]](https://developer.apple.com/documentation/appkit/nsstackview/1488876-viewsingravity)Added [-[NSStackView visibilityPriorityForView:]](https://developer.apple.com/documentation/appkit/nsstackview/1488934-visibilitypriorityforview)Added [NSStackViewDelegate](https://developer.apple.com/documentation/appkit/nsstackviewdelegate)Added [-[NSStackViewDelegate stackView:didReattachViews:]](https://developer.apple.com/documentation/appkit/nsstackviewdelegate/1488921-stackview)Added [-[NSStackViewDelegate stackView:willDetachViews:]](https://developer.apple.com/documentation/appkit/nsstackviewdelegate/1488953-stackview)Added [NSStackViewGravity](https://developer.apple.com/documentation/appkit/nsstackviewgravity)Added [NSStackViewGravityBottom](https://developer.apple.com/documentation/appkit/nsstackview/gravity/bottom)Added [NSStackViewGravityCenter](https://developer.apple.com/documentation/appkit/nsstackviewgravity/nsstackviewgravitycenter)Added [NSStackViewGravityLeading](https://developer.apple.com/documentation/appkit/nsstackview/gravity/1488885-leading)Added [NSStackViewGravityTop](https://developer.apple.com/documentation/appkit/nsstackview/gravity/top)Added [NSStackViewGravityTrailing](https://developer.apple.com/documentation/appkit/nsstackview/gravity/1488907-trailing)Added [#def NSStackViewSpacingUseDefault](https://developer.apple.com/documentation/appkit/nsstackview/nsstackviewspacingusedefault/nsstackviewspacingusedefault)Added [NSStackViewVisibilityPriority](https://developer.apple.com/documentation/appkit/nsstackview/visibilitypriority)Added [NSStackViewVisibilityPriorityDetachOnlyIfNecessary](https://developer.apple.com/documentation/appkit/nsstackviewvisibilitypriority/nsstackviewvisibilityprioritydetachonlyifnecessary)Added [NSStackViewVisibilityPriorityMustHold](https://developer.apple.com/documentation/appkit/nsstackviewvisibilitypriority/nsstackviewvisibilityprioritymusthold)Added [NSStackViewVisibilityPriorityNotVisible](https://developer.apple.com/documentation/appkit/nsstackviewvisibilitypriority/nsstackviewvisibilityprioritynotvisible)Added [NSUserInterfaceLayoutOrientation](https://developer.apple.com/documentation/appkit/nsuserinterfacelayoutorientation)Added [NSUserInterfaceLayoutOrientationHorizontal](https://developer.apple.com/documentation/appkit/nsuserinterfacelayoutorientation/nsuserinterfacelayoutorientationhorizontal)Added [NSUserInterfaceLayoutOrientationVertical](https://developer.apple.com/documentation/appkit/nsuserinterfacelayoutorientation/nsuserinterfacelayoutorientationvertical)NSTableView.hAdded [-[NSTableView didAddRowView:forRow:]](https://developer.apple.com/documentation/appkit/nstableview/1534008-didaddrowview)Added [-[NSTableView didRemoveRowView:forRow:]](https://developer.apple.com/documentation/appkit/nstableview/1532903-didremoverowview)Added [NSTableViewDraggingDestinationFeedbackStyleGap](https://developer.apple.com/documentation/appkit/nstableviewdraggingdestinationfeedbackstyle/nstableviewdraggingdestinationfeedbackstylegap)NSView.hAdded [-[NSView canDrawSubviewsIntoLayer]](https://developer.apple.com/documentation/appkit/nsview/1483347-candrawsubviewsintolayer)Added +[NSView isCompatibleWithResponsiveScrolling]Added [-[NSView layerUsesCoreImageFilters]](https://developer.apple.com/documentation/appkit/nsview/1483576-layerusescoreimagefilters)Added [-[NSView prepareContentInRect:]](https://developer.apple.com/documentation/appkit/nsview/1483427-preparecontentinrect)Added [-[NSView prepareForReuse]](https://developer.apple.com/documentation/appkit/nsview/1483626-prepareforreuse)Added [NSView.preparedContentRect](https://developer.apple.com/documentation/appkit/nsview/1483215-preparedcontentrect)Added [-[NSView setCanDrawSubviewsIntoLayer:]](https://developer.apple.com/documentation/appkit/nsview/1483347-candrawsubviewsintolayer)Added [-[NSView setLayerUsesCoreImageFilters:]](https://developer.apple.com/documentation/appkit/nsview/1483576-layerusescoreimagefilters)Added [-[NSView setUserInterfaceLayoutDirection:]](https://developer.apple.com/documentation/appkit/nsview/1483254-userinterfacelayoutdirection)Added [-[NSView userInterfaceLayoutDirection]](https://developer.apple.com/documentation/appkit/nsview/1483254-userinterfacelayoutdirection)Added [NSViewLayerContentsRedrawCrossfade](https://developer.apple.com/documentation/appkit/nsviewlayercontentsredrawpolicy/nsviewlayercontentsredrawcrossfade)Modified [NSView](https://developer.apple.com/documentation/appkit/nsview)

|  | Protocols |
| --- | --- |
| From | NSAnimatablePropertyContainer, NSUserInterfaceItemIdentification, NSDraggingDestination |
| To | NSAnimatablePropertyContainer, NSAppearanceCustomization, NSDraggingDestination, NSUserInterfaceItemIdentification |

NSWindow.hAdded [-[NSWindow beginCriticalSheet:completionHandler:]](https://developer.apple.com/documentation/appkit/nswindow/1419198-begincriticalsheet)Added [-[NSWindow beginSheet:completionHandler:]](https://developer.apple.com/documentation/appkit/nswindow/1419653-beginsheet)Added [-[NSWindow endSheet:]](https://developer.apple.com/documentation/appkit/nswindow/1419318-endsheet)Added [-[NSWindow endSheet:returnCode:]](https://developer.apple.com/documentation/appkit/nswindow/1419497-endsheet)Added [-[NSWindow occlusionState]](https://developer.apple.com/documentation/appkit/nswindow/1419321-occlusionstate)Added [-[NSWindow sheetParent]](https://developer.apple.com/documentation/appkit/nswindow/1419052-sheetparent)Added [-[NSWindow sheets]](https://developer.apple.com/documentation/appkit/nswindow/1419765-sheets)Added [-[NSWindowDelegate customWindowsToEnterFullScreenForWindow:onScreen:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419557-customwindowstoenterfullscreen)Added [-[NSWindowDelegate window:startCustomAnimationToEnterFullScreenOnScreen:withDuration:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419709-window)Added [-[NSWindowDelegate windowDidChangeOcclusionState:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419424-windowdidchangeocclusionstate)Added [NSModalResponseCancel](https://developer.apple.com/documentation/appkit/nsmodalresponsecancel)Added [NSModalResponseOK](https://developer.apple.com/documentation/appkit/nsapplication/modalresponse/1419254-ok)Added [NSWindowDidChangeOcclusionStateNotification](https://developer.apple.com/documentation/appkit/nswindow/1419549-didchangeocclusionstatenotificat)Added [NSWindowOcclusionState](https://developer.apple.com/documentation/appkit/nswindowocclusionstate)Added [NSWindowOcclusionStateVisible](https://developer.apple.com/documentation/appkit/nswindowocclusionstate/nswindowocclusionstatevisible)Modified [NSWindow](https://developer.apple.com/documentation/appkit/nswindow)

|  | Protocols |
| --- | --- |
| From | NSUserInterfaceValidations, NSAnimatablePropertyContainer, NSUserInterfaceItemIdentification |
| To | NSAnimatablePropertyContainer, NSAppearanceCustomization, NSUserInterfaceItemIdentification, NSUserInterfaceValidations |

Modified -[NSWindow canBeVisibleOnAllSpaces]

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

Modified -[NSWindow setCanBeVisibleOnAllSpaces:]

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.5 |

NSWorkspace.hAdded [NSWorkspaceLaunchWithErrorPresentation](https://developer.apple.com/documentation/appkit/nsworkspace/launchoptions/1524293-witherrorpresentation)

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
