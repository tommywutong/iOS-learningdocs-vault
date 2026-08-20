---
title: OS X v10.8 API Diffs
apple_id: TP40011748
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_8/AppKit.html
archived_at: '2026-07-18T02:53:55.839359Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.8 API Diffs](OS%20X%20v10.7%20to%20OS%20X%20v10.8%20API%20Differences.md)


# AppKit Changes

## AppKit

NSAccessibility.hAdded [NSAccessibilityExtrasMenuBarAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityextrasmenubarattribute)NSAnimation.hModified [-[NSAnimatablePropertyContainer setAnimations:]](https://developer.apple.com/documentation/appkit/nsanimatablepropertycontainer/1534096-animations)

|  | Declaration |
| --- | --- |
| From | - (void)setAnimations:(NSDictionary \*)dict |
| To | - (void)setAnimations:(NSDictionary \*)animations |

NSAnimationContext.hRemoved [-[NSAnimationContext completionHandler]](https://developer.apple.com/documentation/appkit/nsanimationcontext/1531132-completionhandler)Removed [-[NSAnimationContext duration]](https://developer.apple.com/documentation/appkit/nsanimationcontext/1526780-duration)Removed [-[NSAnimationContext setCompletionHandler:]](https://developer.apple.com/documentation/appkit/nsanimationcontext/1531132-completionhandler)Removed [-[NSAnimationContext setDuration:]](https://developer.apple.com/documentation/appkit/nsanimationcontext/1526780-duration)Removed [-[NSAnimationContext setTimingFunction:]](https://developer.apple.com/documentation/appkit/nsanimationcontext/1524985-timingfunction)Removed [-[NSAnimationContext timingFunction]](https://developer.apple.com/documentation/appkit/nsanimationcontext/1524985-timingfunction)Added [NSAnimationContext.allowsImplicitAnimation](https://developer.apple.com/documentation/appkit/nsanimationcontext/1525870-allowsimplicitanimation)Added [NSAnimationContext.completionHandler](https://developer.apple.com/documentation/appkit/nsanimationcontext/1531132-completionhandler)Added [NSAnimationContext.duration](https://developer.apple.com/documentation/appkit/nsanimationcontext/1526780-duration)Added [NSAnimationContext.timingFunction](https://developer.apple.com/documentation/appkit/nsanimationcontext/1524985-timingfunction)NSApplication.hAdded [#def NSAppKitVersionNumber10_7](https://developer.apple.com/documentation/appkit/nsappkitversion/1428354-macos10_7)Added [#def NSAppKitVersionNumber10_7_2](https://developer.apple.com/documentation/appkit/nsappkitversionnumber10_7_2)Added [NSApplicationLaunchUserNotificationKey](https://developer.apple.com/documentation/appkit/nsapplicationlaunchusernotificationkey)Added [NSRemoteNotificationTypeAlert](https://developer.apple.com/documentation/appkit/nsapplication/remotenotificationtype/1428654-alert)Added [NSRemoteNotificationTypeSound](https://developer.apple.com/documentation/appkit/nsapplication/remotenotificationtype/1428525-sound)Modified [NSApplicationLaunchRemoteNotificationKey](https://developer.apple.com/documentation/appkit/nsapplicationlaunchremotenotificationkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

NSAttributedString.hAdded [NSTextAlternativesAttributeName](https://developer.apple.com/documentation/appkit/nstextalternativesattributename)Added [NSUsesScreenFontsDocumentAttribute](https://developer.apple.com/documentation/appkit/nsusesscreenfontsdocumentattribute)NSBox.hModified [-[NSBox setTitleWithMnemonic:]](https://developer.apple.com/documentation/appkit/nsbox/1429800-settitlewithmnemonic)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

NSButton.hModified [-[NSButton setTitleWithMnemonic:]](https://developer.apple.com/documentation/appkit/nsbutton/1579931-settitlewithmnemonic)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

NSButtonCell.hModified [-[NSButtonCell setTitleWithMnemonic:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1589263-settitlewithmnemonic)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [-[NSButtonCell alternateMnemonic]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1589270-alternatemnemonic)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [-[NSButtonCell setAlternateMnemonicLocation:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1589288-setalternatemnemoniclocation)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [-[NSButtonCell setAlternateTitleWithMnemonic:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1589291-setalternatetitlewithmnemonic)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [-[NSButtonCell alternateMnemonicLocation]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1589282-alternatemnemoniclocation)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

NSCell.hModified [-[NSCell mnemonicLocation]](https://developer.apple.com/documentation/appkit/nscell/1560903-mnemoniclocation)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [-[NSCell setTitleWithMnemonic:]](https://developer.apple.com/documentation/appkit/nscell/1560861-settitlewithmnemonic)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [-[NSCell mnemonic]](https://developer.apple.com/documentation/appkit/nscell/1560878-mnemonic)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [-[NSCell setMnemonicLocation:]](https://developer.apple.com/documentation/appkit/nscell/1560877-setmnemoniclocation)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

NSColor.hAdded [-[NSColor CGColor]](https://developer.apple.com/documentation/appkit/nscolor/1527738-cgcolor)Added [+[NSColor colorWithCGColor:]](https://developer.apple.com/documentation/appkit/nscolor/1524265-colorwithcgcolor)Added [+[NSColor underPageBackgroundColor]](https://developer.apple.com/documentation/appkit/nscolor/1534707-underpagebackgroundcolor)NSControl.hAdded [-[NSControl allowsExpansionToolTips]](https://developer.apple.com/documentation/appkit/nscontrol/1428962-allowsexpansiontooltips)Added [-[NSControl setAllowsExpansionToolTips:]](https://developer.apple.com/documentation/appkit/nscontrol/1428962-allowsexpansiontooltips)NSCustomImageRep.hAdded [-[NSCustomImageRep drawingHandler]](https://developer.apple.com/documentation/appkit/nscustomimagerep/1527316-drawinghandler)Added [-[NSCustomImageRep initWithSize:flipped:drawingHandler:]](https://developer.apple.com/documentation/appkit/nscustomimagerep/1526521-initwithsize)NSDocument.hAdded [+[NSDocument autosavesDrafts]](https://developer.apple.com/documentation/appkit/nsdocument/1515109-autosavesdrafts)Added [-[NSDocument backupFileURL]](https://developer.apple.com/documentation/appkit/nsdocument/1515200-backupfileurl)Added [-[NSDocument browseDocumentVersions:]](https://developer.apple.com/documentation/appkit/nsdocument/1515193-browsedocumentversions)Added [-[NSDocument defaultDraftName]](https://developer.apple.com/documentation/appkit/nsdocument/1515245-defaultdraftname)Added [-[NSDocument isDraft]](https://developer.apple.com/documentation/appkit/nsdocument/1515065-isdraft)Added [-[NSDocument isLocked]](https://developer.apple.com/documentation/appkit/nsdocument/1515212-locked)Added [-[NSDocument lockDocument:]](https://developer.apple.com/documentation/appkit/nsdocument/1515218-lock)Added [-[NSDocument lockDocumentWithCompletionHandler:]](https://developer.apple.com/documentation/appkit/nsdocument/1515233-lockdocumentwithcompletionhandle)Added [-[NSDocument lockWithCompletionHandler:]](https://developer.apple.com/documentation/appkit/nsdocument/1515189-lock)Added [-[NSDocument moveDocument:]](https://developer.apple.com/documentation/appkit/nsdocument/1515118-move)Added [-[NSDocument moveDocumentToUbiquityContainer:]](https://developer.apple.com/documentation/appkit/nsdocument/1515210-movedocumenttoubiquitycontainer)Added [-[NSDocument moveDocumentWithCompletionHandler:]](https://developer.apple.com/documentation/appkit/nsdocument/1515043-move)Added [-[NSDocument moveToURL:completionHandler:]](https://developer.apple.com/documentation/appkit/nsdocument/1515057-movetourl)Added [-[NSDocument renameDocument:]](https://developer.apple.com/documentation/appkit/nsdocument/1515231-renamedocument)Added [-[NSDocument setDraft:]](https://developer.apple.com/documentation/appkit/nsdocument/1515065-draft)Added [-[NSDocument unlockDocument:]](https://developer.apple.com/documentation/appkit/nsdocument/1515068-unlock)Added [-[NSDocument unlockDocumentWithCompletionHandler:]](https://developer.apple.com/documentation/appkit/nsdocument/1515248-unlockdocumentwithcompletionhand)Added [-[NSDocument unlockWithCompletionHandler:]](https://developer.apple.com/documentation/appkit/nsdocument/1515131-unlock)Added [+[NSDocument usesUbiquitousStorage]](https://developer.apple.com/documentation/appkit/nsdocument/1515085-usesubiquitousstorage)Added [NSAutosaveAsOperation](https://developer.apple.com/documentation/appkit/nssaveoperationtype/nsautosaveasoperation)Added NS_ENUM_AVAILABLE_MAC (no architecture available)NSDocumentController.hAdded [-[NSDocumentController beginOpenPanel:forTypes:completionHandler:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514969-beginopenpanel)Added [-[NSDocumentController beginOpenPanelWithCompletionHandler:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1515001-beginopenpanel)NSEvent.hAdded [NSEventMaskSmartMagnify](https://developer.apple.com/documentation/appkit/nsevent/eventtypemask/1535440-smartmagnify)Added [NSEventPhaseMayBegin](https://developer.apple.com/documentation/appkit/nsevent/phase/1528100-maybegin)Added [NSEventTypeQuickLook](https://developer.apple.com/documentation/appkit/nsevent/eventtype/quicklook)Added [NSEventTypeSmartMagnify](https://developer.apple.com/documentation/appkit/nsevent/eventtype/smartmagnify)NSForm.hAdded [-[NSForm preferredTextFieldWidth]](https://developer.apple.com/documentation/appkit/nsform/1530873-preferredtextfieldwidth)Added [-[NSForm setPreferredTextFieldWidth:]](https://developer.apple.com/documentation/appkit/nsform/1526047-setpreferredtextfieldwidth)NSFormCell.hAdded [-[NSFormCell preferredTextFieldWidth]](https://developer.apple.com/documentation/appkit/nsformcell/1527483-preferredtextfieldwidth)Added [-[NSFormCell setPreferredTextFieldWidth:]](https://developer.apple.com/documentation/appkit/nsformcell/1527483-preferredtextfieldwidth)Modified [-[NSFormCell setTitleWithMnemonic:]](https://developer.apple.com/documentation/appkit/nsformcell/1560758-settitlewithmnemonic)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

NSImage.hAdded [+[NSImage imageWithSize:flipped:drawingHandler:]](https://developer.apple.com/documentation/appkit/nsimage/1519860-imagewithsize)Added [-[NSImage layerContentsForContentsScale:]](https://developer.apple.com/documentation/appkit/nsimage/1519851-layercontentsforcontentsscale)Added [-[NSImage matchesOnlyOnBestFittingAxis]](https://developer.apple.com/documentation/appkit/nsimage/1519848-matchesonlyonbestfittingaxis)Added [-[NSImage recommendedLayerContentsScale:]](https://developer.apple.com/documentation/appkit/nsimage/1519878-recommendedlayercontentsscale)Added [-[NSImage setMatchesOnlyOnBestFittingAxis:]](https://developer.apple.com/documentation/appkit/nsimage/1519848-matchesonlyonbestfittingaxis)Added [NSImageNameShareTemplate](https://developer.apple.com/documentation/appkit/nsimage/1520013-sharetemplatename)NSInterfaceStyle.hModified [NSInterfaceStyleForKey()](https://developer.apple.com/documentation/appkit/1555070-nsinterfacestyleforkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [-[NSResponder interfaceStyle]](https://developer.apple.com/documentation/appkit/nsresponder/1555071-interfacestyle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [NSInterfaceStyleDefault](https://developer.apple.com/documentation/appkit/nsinterfacestyledefault)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [-[NSResponder setInterfaceStyle:]](https://developer.apple.com/documentation/appkit/nsresponder/1555072-setinterfacestyle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

NSMatrix.hAdded [-[NSMatrix autorecalculatesCellSize]](https://developer.apple.com/documentation/appkit/nsmatrix/1436501-autorecalculatescellsize)Added [-[NSMatrix setAutorecalculatesCellSize:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436501-autorecalculatescellsize)NSNib.hAdded [-[NSNib initWithNibData:bundle:]](https://developer.apple.com/documentation/appkit/nsnib/1535865-init)Added [-[NSNib instantiateWithOwner:topLevelObjects:]](https://developer.apple.com/documentation/appkit/nsnib/1527173-instantiatewithowner)Added NSNib(NSDeprecated)Modified [-[NSNib instantiateNibWithOwner:topLevelObjects:]](https://developer.apple.com/documentation/appkit/nsnib/1547297-instantiatenibwithowner)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [-[NSNib initWithContentsOfURL:]](https://developer.apple.com/documentation/appkit/nsnib/1547299-initwithcontentsofurl)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [-[NSNib instantiateNibWithExternalNameTable:]](https://developer.apple.com/documentation/appkit/nsnib/1547300-instantiatenibwithexternalnameta)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

NSNibLoading.hAdded [-[NSBundle loadNibNamed:owner:topLevelObjects:]](https://developer.apple.com/documentation/foundation/nsbundle/1402909-loadnibnamed)Added NSBundle(NSNibLoadingDeprecated)Modified [+[NSBundle loadNibNamed:owner:]](https://developer.apple.com/documentation/foundation/nsbundle/1402904-loadnibnamed)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [-[NSBundle loadNibFile:externalNameTable:withZone:]](https://developer.apple.com/documentation/foundation/nsbundle/1402910-loadnibfile)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [+[NSBundle loadNibFile:externalNameTable:withZone:]](https://developer.apple.com/documentation/foundation/nsbundle/1402906-loadnibfile)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

NSPageController.hAdded [NSPageController](https://developer.apple.com/documentation/appkit/nspagecontroller)Added [NSPageController.arrangedObjects](https://developer.apple.com/documentation/appkit/nspagecontroller/1435001-arrangedobjects)Added [-[NSPageController completeTransition]](https://developer.apple.com/documentation/appkit/nspagecontroller/1434994-completetransition)Added [NSPageController.delegate](https://developer.apple.com/documentation/appkit/nspagecontroller/1435019-delegate)Added [-[NSPageController navigateBack:]](https://developer.apple.com/documentation/appkit/nspagecontroller/1435017-navigateback)Added [-[NSPageController navigateForward:]](https://developer.apple.com/documentation/appkit/nspagecontroller/1435004-navigateforward)Added [-[NSPageController navigateForwardToObject:]](https://developer.apple.com/documentation/appkit/nspagecontroller/1434990-navigateforward)Added [NSPageController.selectedIndex](https://developer.apple.com/documentation/appkit/nspagecontroller/1434988-selectedindex)Added [NSPageController.selectedViewController](https://developer.apple.com/documentation/appkit/nspagecontroller/1435013-selectedviewcontroller)Added [-[NSPageController takeSelectedIndexFrom:]](https://developer.apple.com/documentation/appkit/nspagecontroller/1435011-takeselectedindexfrom)Added [NSPageController.transitionStyle](https://developer.apple.com/documentation/appkit/nspagecontroller/1434999-transitionstyle)Added [NSPageControllerDelegate](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate)Added [-[NSPageControllerDelegate pageController:didTransitionToObject:]](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/1435021-pagecontroller)Added [-[NSPageControllerDelegate pageController:frameForObject:]](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/1434992-pagecontroller)Added [-[NSPageControllerDelegate pageController:identifierForObject:]](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/1435007-pagecontroller)Added [-[NSPageControllerDelegate pageController:prepareViewController:withObject:]](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/1434983-pagecontroller)Added [-[NSPageControllerDelegate pageController:viewControllerForIdentifier:]](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/1435015-pagecontroller)Added [-[NSPageControllerDelegate pageControllerDidEndLiveTransition:]](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/1434985-pagecontrollerdidendlivetransiti)Added [-[NSPageControllerDelegate pageControllerWillStartLiveTransition:]](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/1435009-pagecontrollerwillstartlivetrans)Added NA (no architecture available)Added [NSPageControllerTransitionStyle](https://developer.apple.com/documentation/appkit/nspagecontrollertransitionstyle)Added [NSPageControllerTransitionStyleHorizontalStrip](https://developer.apple.com/documentation/appkit/nspagecontrollertransitionstyle/nspagecontrollertransitionstylehorizontalstrip)Added [NSPageControllerTransitionStyleStackBook](https://developer.apple.com/documentation/appkit/nspagecontrollertransitionstyle/nspagecontrollertransitionstylestackbook)Added [NSPageControllerTransitionStyleStackHistory](https://developer.apple.com/documentation/appkit/nspagecontrollertransitionstyle/nspagecontrollertransitionstylestackhistory)NSPasteboard.hModified [-[NSPasteboard releaseGlobally]](https://developer.apple.com/documentation/appkit/nspasteboard/1527044-releaseglobally)

|  | Declaration |
| --- | --- |
| From | - (void)releaseGlobally |
| To | - (oneway void)releaseGlobally |

NSResponder.hRemoved NSResponder(NSKeyboardUI)Added -[NSResponder quickLookPreviewItems:]Added [-[NSResponder quickLookWithEvent:]](https://developer.apple.com/documentation/appkit/nsresponder/1535080-quicklookwithevent)Added [-[NSResponder smartMagnifyWithEvent:]](https://developer.apple.com/documentation/appkit/nsresponder/1532984-smartmagnify)Added NSResponder(NSDeprecated)Modified [-[NSResponder performMnemonic:]](https://developer.apple.com/documentation/appkit/nsresponder/1584388-performmnemonic)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

NSScrollView.hAdded [NSScrollView.allowsMagnification](https://developer.apple.com/documentation/appkit/nsscrollview/1403531-allowsmagnification)Added [NSScrollView.magnification](https://developer.apple.com/documentation/appkit/nsscrollview/1403497-magnification)Added [-[NSScrollView magnifyToFitRect:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403508-magnify)Added [NSScrollView.maxMagnification](https://developer.apple.com/documentation/appkit/nsscrollview/1403510-maxmagnification)Added [NSScrollView.minMagnification](https://developer.apple.com/documentation/appkit/nsscrollview/1403524-minmagnification)Added [-[NSScrollView setMagnification:centeredAtPoint:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403459-setmagnification)Added [NSScrollViewDidEndLiveMagnifyNotification](https://developer.apple.com/documentation/appkit/nsscrollview/1403464-didendlivemagnifynotification)Added [NSScrollViewWillStartLiveMagnifyNotification](https://developer.apple.com/documentation/appkit/nsscrollviewwillstartlivemagnifynotification)NSSharingService.hAdded [NSSharingService](https://developer.apple.com/documentation/appkit/nssharingservice)Added [NSSharingService.alternateImage](https://developer.apple.com/documentation/appkit/nssharingservice/1402650-alternateimage)Added [-[NSSharingService canPerformWithItems:]](https://developer.apple.com/documentation/appkit/nssharingservice/1402662-canperformwithitems)Added [NSSharingService.delegate](https://developer.apple.com/documentation/appkit/nssharingservice/1402681-delegate)Added [NSSharingService.image](https://developer.apple.com/documentation/appkit/nssharingservice/1402654-image)Added [-[NSSharingService initWithTitle:image:alternateImage:handler:]](https://developer.apple.com/documentation/appkit/nssharingservice/1402614-init)Added [-[NSSharingService performWithItems:]](https://developer.apple.com/documentation/appkit/nssharingservice/1402669-performwithitems)Added [+[NSSharingService sharingServiceNamed:]](https://developer.apple.com/documentation/appkit/nssharingservice/1402673-sharingservicenamed)Added [+[NSSharingService sharingServicesForItems:]](https://developer.apple.com/documentation/appkit/nssharingservice/1402646-sharingservices)Added [NSSharingService.title](https://developer.apple.com/documentation/appkit/nssharingservice/1402637-title)Added [NSSharingServiceDelegate](https://developer.apple.com/documentation/appkit/nssharingservicedelegate)Added [-[NSSharingServiceDelegate sharingService:didFailToShareItems:error:]](https://developer.apple.com/documentation/appkit/nssharingservicedelegate/1402710-sharingservice)Added [-[NSSharingServiceDelegate sharingService:didShareItems:]](https://developer.apple.com/documentation/appkit/nssharingservicedelegate/1402638-sharingservice)Added [-[NSSharingServiceDelegate sharingService:sourceFrameOnScreenForShareItem:]](https://developer.apple.com/documentation/appkit/nssharingservicedelegate/1402695-sharingservice)Added [-[NSSharingServiceDelegate sharingService:sourceWindowForShareItems:sharingContentScope:]](https://developer.apple.com/documentation/appkit/nssharingservicedelegate/1402679-sharingservice)Added [-[NSSharingServiceDelegate sharingService:transitionImageForShareItem:contentRect:]](https://developer.apple.com/documentation/appkit/nssharingservicedelegate/1402622-sharingservice)Added [-[NSSharingServiceDelegate sharingService:willShareItems:]](https://developer.apple.com/documentation/appkit/nssharingservicedelegate/1402642-sharingservice)Added [NSSharingServicePicker](https://developer.apple.com/documentation/appkit/nssharingservicepicker)Added [NSSharingServicePicker.delegate](https://developer.apple.com/documentation/appkit/nssharingservicepicker/1402687-delegate)Added [-[NSSharingServicePicker initWithItems:]](https://developer.apple.com/documentation/appkit/nssharingservicepicker/1402691-init)Added [-[NSSharingServicePicker showRelativeToRect:ofView:preferredEdge:]](https://developer.apple.com/documentation/appkit/nssharingservicepicker/1402706-showrelativetorect)Added [NSSharingServicePickerDelegate](https://developer.apple.com/documentation/appkit/nssharingservicepickerdelegate)Added [-[NSSharingServicePickerDelegate sharingServicePicker:delegateForSharingService:]](https://developer.apple.com/documentation/appkit/nssharingservicepickerdelegate/1402608-sharingservicepicker)Added [-[NSSharingServicePickerDelegate sharingServicePicker:didChooseSharingService:]](https://developer.apple.com/documentation/appkit/nssharingservicepickerdelegate/1402610-sharingservicepicker)Added [-[NSSharingServicePickerDelegate sharingServicePicker:sharingServicesForItems:proposedSharingServices:]](https://developer.apple.com/documentation/appkit/nssharingservicepickerdelegate/1402664-sharingservicepicker)Added [NSSharingContentScope](https://developer.apple.com/documentation/appkit/nssharingcontentscope)Added [NSSharingContentScopeFull](https://developer.apple.com/documentation/appkit/nssharingservice/sharingcontentscope/full)Added [NSSharingContentScopeItem](https://developer.apple.com/documentation/appkit/nssharingcontentscope/nssharingcontentscopeitem)Added [NSSharingContentScopePartial](https://developer.apple.com/documentation/appkit/nssharingservice/sharingcontentscope/partial)Added [NSSharingServiceNameAddToAperture](https://developer.apple.com/documentation/appkit/nssharingservice/name/1402618-addtoaperture)Added [NSSharingServiceNameAddToIPhoto](https://developer.apple.com/documentation/appkit/nssharingservice/name/1402675-addtoiphoto)Added [NSSharingServiceNameAddToSafariReadingList](https://developer.apple.com/documentation/appkit/nssharingservice/name/1402689-addtosafarireadinglist)Added [NSSharingServiceNameComposeEmail](https://developer.apple.com/documentation/appkit/nssharingservicenamecomposeemail)Added [NSSharingServiceNameComposeMessage](https://developer.apple.com/documentation/appkit/nssharingservicenamecomposemessage)Added [NSSharingServiceNamePostImageOnFlickr](https://developer.apple.com/documentation/appkit/nssharingservicenamepostimageonflickr)Added [NSSharingServiceNamePostOnFacebook](https://developer.apple.com/documentation/appkit/nssharingservicenamepostonfacebook)Added [NSSharingServiceNamePostOnSinaWeibo](https://developer.apple.com/documentation/appkit/nssharingservicenamepostonsinaweibo)Added [NSSharingServiceNamePostOnTwitter](https://developer.apple.com/documentation/appkit/nssharingservice/name/1402612-postontwitter)Added [NSSharingServiceNamePostVideoOnTudou](https://developer.apple.com/documentation/appkit/nssharingservice/name/1402616-postvideoontudou)Added [NSSharingServiceNamePostVideoOnVimeo](https://developer.apple.com/documentation/appkit/nssharingservicenamepostvideoonvimeo)Added [NSSharingServiceNamePostVideoOnYouku](https://developer.apple.com/documentation/appkit/nssharingservice/name/1402708-postvideoonyouku)Added [NSSharingServiceNameSendViaAirDrop](https://developer.apple.com/documentation/appkit/nssharingservicenamesendviaairdrop)Added [NSSharingServiceNameUseAsDesktopPicture](https://developer.apple.com/documentation/appkit/nssharingservice/name/1402671-useasdesktoppicture)Added [NSSharingServiceNameUseAsTwitterProfileImage](https://developer.apple.com/documentation/appkit/nssharingservicenameuseastwitterprofileimage)Added NS_ENUM() (no architecture available)Added NS_ENUM_AVAILABLE_MAC() (no architecture available)NSSpellChecker.hAdded [-[NSSpellChecker languageForWordRange:inString:orthography:]](https://developer.apple.com/documentation/appkit/nsspellchecker/1530303-languageforwordrange)NSSplitView.hAdded [-[NSSplitView holdingPriorityForSubviewAtIndex:]](https://developer.apple.com/documentation/appkit/nssplitview/1455287-holdingpriorityforsubview)Added [-[NSSplitView setHoldingPriority:forSubviewAtIndex:]](https://developer.apple.com/documentation/appkit/nssplitview/1455320-setholdingpriority)NSTableView.hAdded [-[NSTableView registerNib:forIdentifier:]](https://developer.apple.com/documentation/appkit/nstableview/1524297-register)Added [-[NSTableView registeredNibsByIdentifier]](https://developer.apple.com/documentation/appkit/nstableview/1530663-registerednibsbyidentifier)NSTextAlternatives.hAdded [NSTextAlternatives](https://developer.apple.com/documentation/appkit/nstextalternatives)Added [NSTextAlternatives.alternativeStrings](https://developer.apple.com/documentation/appkit/nstextalternatives/1527585-alternativestrings)Added [-[NSTextAlternatives initWithPrimaryString:alternativeStrings:]](https://developer.apple.com/documentation/appkit/nstextalternatives/1529445-initwithprimarystring)Added [-[NSTextAlternatives noteSelectedAlternativeString:]](https://developer.apple.com/documentation/appkit/nstextalternatives/1525721-noteselectedalternativestring)Added [NSTextAlternatives.primaryString](https://developer.apple.com/documentation/appkit/nstextalternatives/1526166-primarystring)Added [NSTextAlternativesSelectedAlternativeStringNotification](https://developer.apple.com/documentation/appkit/nstextalternatives/1534781-selectedalternativestringnotific)NSTextField.hRemoved NSTextField(NSKeyboardUI)Added [-[NSTextField preferredMaxLayoutWidth]](https://developer.apple.com/documentation/appkit/nstextfield/1399395-preferredmaxlayoutwidth)Added [-[NSTextField setPreferredMaxLayoutWidth:]](https://developer.apple.com/documentation/appkit/nstextfield/1399395-preferredmaxlayoutwidth)Added NSTextField(NSDeprecated)Modified [-[NSTextField setTitleWithMnemonic:]](https://developer.apple.com/documentation/appkit/nstextfield/1399411-settitlewithmnemonic)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

NSTextView.hAdded [-[NSTextView orderFrontSharingServicePicker:]](https://developer.apple.com/documentation/appkit/nstextview/1449150-orderfrontsharingservicepicker)Added [-[NSTextViewDelegate textView:willShowSharingServicePicker:forItems:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449339-textview)Added NSTextView(NSTextView_SharingService)NSView.hAdded [-[NSObject layer:shouldInheritContentsScale:fromWindow:]](https://developer.apple.com/documentation/objectivec/nsobject/1483574-layer)Added [-[NSView rectForSmartMagnificationAtPoint:inRect:]](https://developer.apple.com/documentation/appkit/nsview/1483305-rectforsmartmagnificationatpoint)Added [-[NSView updateLayer]](https://developer.apple.com/documentation/appkit/nsview/1483580-updatelayer)Added [-[NSView viewDidChangeBackingProperties]](https://developer.apple.com/documentation/appkit/nsview/1483742-viewdidchangebackingproperties)Added [-[NSView wantsUpdateLayer]](https://developer.apple.com/documentation/appkit/nsview/1483461-wantsupdatelayer)Added NSObject(NSLayerDelegateContentsScaleUpdating)Added NSView(NSDeprecated)Modified [-[NSView performMnemonic:]](https://developer.apple.com/documentation/appkit/nsview/1483585-performmnemonic)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [-[NSView releaseGState]](https://developer.apple.com/documentation/appkit/nsview/1483761-releasegstate)

|  | Declaration |
| --- | --- |
| From | - (void)releaseGState |
| To | - (oneway void)releaseGState |

NSWindow.hAdded [-[NSWindowDelegate windowDidChangeBackingProperties:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419517-windowdidchangebackingproperties)Added [NSBackingPropertyOldColorSpaceKey](https://developer.apple.com/documentation/appkit/nswindow/1419054-oldcolorspaceuserinfokey)Added [NSBackingPropertyOldScaleFactorKey](https://developer.apple.com/documentation/appkit/nsbackingpropertyoldscalefactorkey)Added [NSWindowDidChangeBackingPropertiesNotification](https://developer.apple.com/documentation/appkit/nswindowdidchangebackingpropertiesnotification)Modified -[NSWindow setCanBeVisibleOnAllSpaces:]

|  | Declaration |
| --- | --- |
| From | - (void)setCanBeVisibleOnAllSpaces:(BOOL)__AVAILABILITY_INTERNAL__MAC_10_5_DEP__MAC_10_5 |
| To | - (void)setCanBeVisibleOnAllSpaces:(BOOL)flag |

NSWorkspace.hModified [-[NSWorkspace mountedRemovableMedia]](https://developer.apple.com/documentation/appkit/nsworkspace/1535898-mountedremovablemedia)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.7 |

Modified [-[NSWorkspace mountedLocalVolumePaths]](https://developer.apple.com/documentation/appkit/nsworkspace/1535834-mountedlocalvolumepaths)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.7 |

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
