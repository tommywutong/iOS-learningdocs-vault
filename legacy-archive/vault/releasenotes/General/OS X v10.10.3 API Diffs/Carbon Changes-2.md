---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/Carbon.html
archived_at: '2026-07-18T02:52:07.691910Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# Carbon Changes

## Carbon

Added AlertStdAlertParamRec.init()Added AlertStdAlertParamRec.init(movable: Boolean, helpButton: Boolean, filterProc: ModalFilterUPP, defaultText: ConstStringPtr, cancelText: ConstStringPtr, otherText: ConstStringPtr, defaultButton: Int16, cancelButton: Int16, position: UInt16)Added AlertStdCFStringAlertParamRec.init()Added AlertStdCFStringAlertParamRec.init(version: UInt32, movable: Boolean, helpButton: Boolean, defaultText: Unmanaged<CFString>!, cancelText: Unmanaged<CFString>!, otherText: Unmanaged<CFString>!, defaultButton: Int16, cancelButton: Int16, position: UInt16, flags: OptionBits, icon: IconRef)Added AlertTemplate.init()Added AlertTemplate.init(boundsRect: Rect, itemsID: Int16, stages: StageList)Added BasicWindowDescription.init()Added CalibratorInfo.init()Added CalibratorInfo.init(dataSize: UInt32, displayID: CMDisplayIDType, profileLocationSize: UInt32, profileLocationPtr: UnsafeMutablePointer<CMProfileLocation>, eventProc: CalibrateEventUPP, isGood: Boolean)Added ContextualMenuInterfaceStruct.init()Added ContextualMenuInterfaceStruct.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, CFUUIDBytes, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int32)>, AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UInt32)>, Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UInt32)>, ExamineContext: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<AEDesc>, UnsafeMutablePointer<AEDescList>) -> OSStatus)>, HandleSelection: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<AEDesc>, Int32) -> OSStatus)>, PostMenuCleanup: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>)Added ControlEditTextSelectionRec.init()Added ControlEditTextSelectionRec.init(selStart: Int16, selEnd: Int16)Added ControlFontStyleRec.init()Added ControlFontStyleRec.init(flags: Int16, font: Int16, size: Int16, style: Int16, mode: Int16, just: Int16, foreColor: RGBColor, backColor: RGBColor)Added ControlID.init()Added ControlID.init(signature: OSType, id: Int32)Added ControlImageContentInfo.init()Added ControlKind.init()Added ControlKind.init(signature: OSType, kind: OSType)Added ControlTabEntry.init()Added ControlTabEntry.init(icon: UnsafeMutablePointer<ControlButtonContentInfo>, name: Unmanaged<CFString>!, enabled: Boolean)Added ControlTabInfoRec.init()Added ControlTabInfoRec.init(version: Int16, iconSuiteID: Int16, name: Str255)Added ControlTabInfoRecV1.init()Added ControlTabInfoRecV1.init(version: Int16, iconSuiteID: Int16, name: Unmanaged<CFString>!)Added ControlTemplate.init()Added ControlTemplate.init(controlRect: Rect, controlValue: Int16, controlVisible: Boolean, fill: UInt8, controlMaximum: Int16, controlMinimum: Int16, controlDefProcID: Int16, controlReference: Int32, controlTitle: Str255)Added CtlCTab.init()Added CtlCTab.init(ccSeed: Int32, ccRider: Int16, ctSize: Int16, ctTable:(ColorSpec, ColorSpec, ColorSpec, ColorSpec))Added DataBrowserAccessibilityItemInfo.init()Added DataBrowserAccessibilityItemInfoV0.init()Added DataBrowserAccessibilityItemInfoV0.init(container: DataBrowserItemID, item: DataBrowserItemID, columnProperty: DataBrowserPropertyID, propertyPart: DataBrowserPropertyPart)Added DataBrowserAccessibilityItemInfoV1.init()Added DataBrowserAccessibilityItemInfoV1.init(container: DataBrowserItemID, item: DataBrowserItemID, columnProperty: DataBrowserPropertyID, propertyPart: DataBrowserPropertyPart, rowIndex: DataBrowserTableViewRowIndex, columnIndex: DataBrowserTableViewColumnIndex)Added DataBrowserCallbacks.init()Added DataBrowserCustomCallbacks.init()Added DataBrowserListViewColumnDesc.init()Added DataBrowserListViewColumnDesc.init(propertyDesc: DataBrowserTableViewColumnDesc, headerBtnDesc: DataBrowserListViewHeaderDesc)Added DataBrowserListViewHeaderDesc.init()Added DataBrowserListViewHeaderDesc.init(version: UInt32, minimumWidth: UInt16, maximumWidth: UInt16, titleOffset: Int16, titleString: Unmanaged<CFString>!, initialOrder: DataBrowserSortOrder, btnFontStyle: ControlFontStyleRec, btnContentInfo: ControlButtonContentInfo)Added DataBrowserPropertyDesc.init()Added DataBrowserPropertyDesc.init(propertyID: DataBrowserPropertyID, propertyType: DataBrowserPropertyType, propertyFlags: DataBrowserPropertyFlags)Added DialogTemplate.init()Added DialogTemplate.init(boundsRect: Rect, procID: Int16, visible: Boolean, filler1: Boolean, goAwayFlag: Boolean, filler2: Boolean, refCon: Int32, itemsID: Int16, title: Str255)Added EvQEl.init()Added EvQEl.init(qLink: QElemPtr, qType: Int16, evtQWhat: EventKind, evtQMessage: UInt, evtQWhen: UInt32, evtQWhere: Point, evtQModifiers: EventModifiers)Added EventHotKeyID.init()Added EventHotKeyID.init(signature: OSType, id: UInt32)Added EventRecord.init()Added EventRecord.init(what: EventKind, message: UInt, when: UInt32, where: Point, modifiers: EventModifiers)Added EventTypeSpec.init()Added EventTypeSpec.init(eventClass: OSType, eventKind: UInt32)Added FileTranslationList.init()Added FileTranslationList.init(modDate: UInt, groupCount: UInt)Added FileTranslationSpec.init()Added FileTranslationSpec.init(componentSignature: OSType, translationSystemInfo: UnsafePointer<Void>, src: FileTypeSpec, dst: FileTypeSpec)Added FileTypeSpec.init()Added FileTypeSpec.init(format: FileType, hint: Int, flags: TranslationAttributes, catInfoType: OSType, catInfoCreator: OSType)Added FontSelectionQDStyle.init()Added FontSelectionQDStyle.init(version: UInt32, instance: FMFontFamilyInstance, size: FMFontSize, hasColor: Boolean, reserved: UInt8, color: RGBColor)Added GetGrowImageRegionRec.init()Added GetGrowImageRegionRec.init(growRect: Rect, growImageRegion: RgnHandle)Added GetWindowRegionRec.init()Added GetWindowRegionRec.init(winRgn: RgnHandle, regionCode: WindowRegionCode)Added HFSFlavor.init()Added HFSFlavor.init(fileType: OSType, fileCreator: OSType, fdFlags: UInt16, fileSpec: FSSpec)Added HIAxisPosition.init()Added HIAxisPosition.init(toView: Unmanaged<HIView>!, kind: HIPositionKind, offset: CGFloat)Added HIAxisScale.init()Added HIAxisScale.init(toView: Unmanaged<HIView>!, kind: HIScaleKind, ratio: CGFloat)Added HIBinding.init()Added HIBinding.init(top: HISideBinding, left: HISideBinding, bottom: HISideBinding, right: HISideBinding)Added HICommand.init()Added HICommandExtended.init()Added HIContentBorderMetrics.init()Added HIContentBorderMetrics.init(top: CGFloat, left: CGFloat, bottom: CGFloat, right: CGFloat)Added HILayoutInfo.init()Added HILayoutInfo.init(version: UInt32, binding: HIBinding, scale: HIScaling, position: HIPositioning)Added HIPositioning.init()Added HIPositioning.init(x: HIAxisPosition, y: HIAxisPosition)Added HIScaling.init()Added HIScaling.init(x: HIAxisScale, y: HIAxisScale)Added HIScrollBarTrackInfo.init()Added HIScrollBarTrackInfo.init(version: UInt32, enableState: ThemeTrackEnableState, pressState: ThemeTrackPressState, viewsize: CGFloat)Added HISideBinding.init()Added HISideBinding.init(toView: Unmanaged<HIView>!, kind: HIBindingKind, offset: CGFloat)Added HIThemeAnimationFrameInfo.init()Added HIThemeAnimationFrameInfo.init(index: UInt32)Added HIThemeAnimationTimeInfo.init()Added HIThemeAnimationTimeInfo.init(start: CFAbsoluteTime, current: CFAbsoluteTime)Added HIThemeBackgroundDrawInfo.init()Added HIThemeBackgroundDrawInfo.init(version: UInt32, state: ThemeDrawState, kind: ThemeBackgroundKind)Added HIThemeButtonDrawInfo.init()Added HIThemeChasingArrowsDrawInfo.init()Added HIThemeChasingArrowsDrawInfo.init(version: UInt32, state: ThemeDrawState, index: UInt32)Added HIThemeFrameDrawInfo.init()Added HIThemeFrameDrawInfo.init(version: UInt32, kind: HIThemeFrameKind, state: ThemeDrawState, isFocused: Boolean)Added HIThemeGrabberDrawInfo.init()Added HIThemeGrabberDrawInfo.init(version: UInt32, state: ThemeDrawState)Added HIThemeGroupBoxDrawInfo.init()Added HIThemeGroupBoxDrawInfo.init(version: UInt32, state: ThemeDrawState, kind: HIThemeGroupBoxKind)Added HIThemeGrowBoxDrawInfo.init()Added HIThemeGrowBoxDrawInfo.init(version: UInt32, state: ThemeDrawState, kind: HIThemeGrowBoxKind, direction: ThemeGrowDirection, size: HIThemeGrowBoxSize)Added HIThemeHeaderDrawInfo.init()Added HIThemeHeaderDrawInfo.init(version: UInt32, state: ThemeDrawState, kind: HIThemeHeaderKind)Added HIThemeMenuBarDrawInfo.init()Added HIThemeMenuBarDrawInfo.init(version: UInt32, state: ThemeMenuBarState, attributes: OptionBits)Added HIThemeMenuDrawInfo.init()Added HIThemeMenuDrawInfo.init(version: UInt32, menuType: ThemeMenuType, reserved1: UInt, reserved2: CGFloat, menuDirection: UInt32, reserved3: CGFloat, reserved4: CGFloat)Added HIThemeMenuDrawInfoVersionZero.init()Added HIThemeMenuDrawInfoVersionZero.init(version: UInt32, menuType: ThemeMenuType)Added HIThemeMenuItemDrawInfo.init()Added HIThemeMenuItemDrawInfo.init(version: UInt32, itemType: ThemeMenuItemType, state: ThemeMenuState)Added HIThemeMenuTitleDrawInfo.init()Added HIThemeMenuTitleDrawInfo.init(version: UInt32, state: ThemeMenuState, attributes: OptionBits, condensedTitleExtra: CGFloat)Added HIThemePlacardDrawInfo.init()Added HIThemePlacardDrawInfo.init(version: UInt32, state: ThemeDrawState)Added HIThemePopupArrowDrawInfo.init()Added HIThemePopupArrowDrawInfo.init(version: UInt32, state: ThemeDrawState, orientation: ThemeArrowOrientation, size: ThemePopupArrowSize)Added HIThemeScrollBarDelimitersDrawInfo.init()Added HIThemeScrollBarDelimitersDrawInfo.init(version: UInt32, state: ThemeDrawState, windowType: ThemeWindowType, attributes: ThemeWindowAttributes)Added HIThemeSegmentDrawInfo.init()Added HIThemeSegmentDrawInfo.init(version: UInt32, state: ThemeDrawState, value: ThemeButtonValue, size: HIThemeSegmentSize, kind: HIThemeSegmentKind, position: HIThemeSegmentPosition, adornment: HIThemeSegmentAdornment)Added HIThemeSeparatorDrawInfo.init()Added HIThemeSeparatorDrawInfo.init(version: UInt32, state: ThemeDrawState)Added HIThemeSplitterDrawInfo.init()Added HIThemeSplitterDrawInfo.init(version: UInt32, state: ThemeDrawState, adornment: HIThemeSplitterAdornment)Added HIThemeTabDrawInfo.init()Added HIThemeTabDrawInfo.init(version: UInt32, style: ThemeTabStyle, direction: ThemeTabDirection, size: HIThemeTabSize, adornment: HIThemeTabAdornment, kind: HIThemeTabKind, position: HIThemeTabPosition)Added HIThemeTabDrawInfoVersionZero.init()Added HIThemeTabDrawInfoVersionZero.init(version: UInt32, style: ThemeTabStyle, direction: ThemeTabDirection, size: HIThemeTabSize, adornment: HIThemeTabAdornment)Added HIThemeTabPaneDrawInfo.init()Added HIThemeTabPaneDrawInfo.init(version: UInt32, state: ThemeDrawState, direction: ThemeTabDirection, size: HIThemeTabSize, kind: HIThemeTabKind, adornment: HIThemeTabPaneAdornment)Added HIThemeTabPaneDrawInfoVersionZero.init()Added HIThemeTabPaneDrawInfoVersionZero.init(version: UInt32, state: ThemeDrawState, direction: ThemeTabDirection, size: HIThemeTabSize)Added HIThemeTextInfo.init()Added HIThemeTextInfo.init(version: UInt32, state: ThemeDrawState, fontID: ThemeFontID, horizontalFlushness: HIThemeTextHorizontalFlush, verticalFlushness: HIThemeTextVerticalFlush, options: HIThemeTextBoxOptions, truncationPosition: HIThemeTextTruncation, truncationMaxLines: UInt32, truncationHappened: Boolean, filler1: UInt8, font: Unmanaged<CTFont>!)Added HIThemeTickMarkDrawInfo.init()Added HIThemeTickMarkDrawInfo.init(version: UInt32, state: ThemeDrawState)Added HIThemeTrackDrawInfo.init()Added HIThemeWindowDrawInfo.init()Added HIThemeWindowDrawInfo.init(version: UInt32, state: ThemeDrawState, windowType: ThemeWindowType, attributes: ThemeWindowAttributes, titleHeight: CGFloat, titleWidth: CGFloat)Added HIThemeWindowWidgetDrawInfo.init()Added HIThemeWindowWidgetDrawInfo.init(version: UInt32, widgetState: ThemeDrawState, widgetType: ThemeTitleBarWidget, windowState: ThemeDrawState, windowType: ThemeWindowType, attributes: ThemeWindowAttributes, titleHeight: CGFloat, titleWidth: CGFloat)Added HITypeAndCreator.init()Added HITypeAndCreator.init(type: OSType, creator: OSType)Added HIViewContentInfo.init()Added HIViewFrameMetrics.init()Added HIViewFrameMetrics.init(top: CGFloat, left: CGFloat, bottom: CGFloat, right: CGFloat)Added HIViewKind.init()Added HIViewKind.init(signature: OSType, kind: OSType)Added HMHelpContent.init()Added HMHelpContentRec.init()Added HMHelpContentRec.init(version: Int32, absHotRect: Rect, tagSide: HMTagDisplaySide, content:(HMHelpContent, HMHelpContent))Added HMStringResType.init()Added HMStringResType.init(hmmResID: Int16, hmmIndex: Int16)Added HMenuBarHeader.init()Added HMenuBarHeader.init(lastHMenu: UInt16, menuTitleBits: PixMapHandle)Added HMenuBarMenu.init()Added HMenuBarMenu.init(menu: Unmanaged<Menu>!, reserved: Int16)Added ICACloseSessionPB.init()Added ICACloseSessionPB.init(header: ICAHeader, sessionID: ICASessionID)Added ICACopyObjectDataPB.init()Added ICACopyObjectDataPB.init(header: ICAHeader, object: ICAObject, startByte: Int, requestedSize: Int, data: UnsafeMutablePointer<Unmanaged<CFData>?>)Added ICACopyObjectPropertyDictionaryPB.init()Added ICACopyObjectPropertyDictionaryPB.init(header: ICAHeader, object: ICAObject, theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>)Added ICACopyObjectThumbnailPB.init()Added ICACopyObjectThumbnailPB.init(header: ICAHeader, object: ICAObject, thumbnailFormat: OSType, thumbnailData: UnsafeMutablePointer<Unmanaged<CFData>?>)Added ICADownloadFilePB.init()Added ICADownloadFilePB.init(header: ICAHeader, object: ICAObject, dirFSRef: UnsafeMutablePointer<FSRef>, flags: UInt32, fileType: OSType, fileCreator: OSType, rotationAngle: Fixed, fileFSRef: UnsafeMutablePointer<FSRef>)Added ICAGetDeviceListPB.init()Added ICAGetDeviceListPB.init(header: ICAHeader, object: ICAObject)Added ICAHeader.init()Added ICAHeader.init(err: ICAError, refcon: UInt)Added ICAImportImagePB.init()Added ICAImportImagePB.init(header: ICAHeader, deviceObject: ICAObject, flags: UInt32, supportedFileTypes: Unmanaged<CFArray>!, filterProc: ICAImportFilterProc, importedImages: UnsafeMutablePointer<Unmanaged<CFArray>?>)Added ICALoadDeviceModulePB.init()Added ICALoadDeviceModulePB.init(header: ICAHeader, paramDictionary: Unmanaged<CFDictionary>!)Added ICAMessage.init()Added ICAMessage.init(messageType: OSType, startByte: UInt32, dataPtr: UnsafeMutablePointer<Void>, dataSize: UInt32, dataType: OSType)Added ICAObjectInfo.init()Added ICAObjectInfo.init(objectType: OSType, objectSubtype: OSType)Added ICAObjectSendMessagePB.init()Added ICAObjectSendMessagePB.init(header: ICAHeader, object: ICAObject, message: ICAMessage, result: UInt32)Added ICAOpenSessionPB.init()Added ICAOpenSessionPB.init(header: ICAHeader, deviceObject: ICAObject, sessionID: ICASessionID)Added ICAPTPEventDataset.init()Added ICAPTPEventDataset.init(dataLength: UInt32, containerType: UInt16, eventCode: UInt16, transactionID: UInt32, params:(UInt32, UInt32, UInt32))Added ICAPTPPassThroughPB.init()Added ICAPTPPassThroughPB.init(commandCode: UInt32, resultCode: UInt32, numOfInputParams: UInt32, numOfOutputParams: UInt32, params:(UInt32, UInt32, UInt32, UInt32), dataUsageMode: UInt32, flags: UInt32, dataSize: UInt32, data:(UInt8))Added ICARegisterForEventNotificationPB.init()Added ICARegisterForEventNotificationPB.init(header: ICAHeader, objectOfInterest: ICAObject, eventsOfInterest: Unmanaged<CFArray>!, notificationProc: ICANotification, options: Unmanaged<CFDictionary>!)Added ICAScannerCloseSessionPB.init()Added ICAScannerCloseSessionPB.init(header: ICAHeader, sessionID: ICAScannerSessionID)Added ICAScannerGetParametersPB.init()Added ICAScannerGetParametersPB.init(header: ICAHeader, sessionID: ICAScannerSessionID, theDict: Unmanaged<CFMutableDictionary>!)Added ICAScannerInitializePB.init()Added ICAScannerInitializePB.init(header: ICAHeader, sessionID: ICAScannerSessionID)Added ICAScannerOpenSessionPB.init()Added ICAScannerOpenSessionPB.init(header: ICAHeader, object: ICAObject, sessionID: ICAScannerSessionID)Added ICAScannerSetParametersPB.init()Added ICAScannerSetParametersPB.init(header: ICAHeader, sessionID: ICAScannerSessionID, theDict: Unmanaged<CFMutableDictionary>!)Added ICAScannerStartPB.init()Added ICAScannerStartPB.init(header: ICAHeader, sessionID: ICAScannerSessionID)Added ICAScannerStatusPB.init()Added ICAScannerStatusPB.init(header: ICAHeader, sessionID: ICAScannerSessionID, status: UInt32)Added ICASendNotificationPB.init()Added ICASendNotificationPB.init(header: ICAHeader, notificationDictionary: Unmanaged<CFMutableDictionary>!, replyCode: UInt32)Added ICAUnloadDeviceModulePB.init()Added ICAUnloadDeviceModulePB.init(header: ICAHeader, deviceObject: ICAObject)Added ICAUploadFilePB.init()Added ICAUploadFilePB.init(header: ICAHeader, parentObject: ICAObject, fileFSRef: UnsafeMutablePointer<FSRef>, flags: UInt32)Added ICDHeader.init()Added ICDHeader.init(err: ICAError, refcon: UInt)Added ICD_DisposeObjectPB.init()Added ICD_DisposeObjectPB.init(header: ICDHeader, object: ICAObject)Added ICD_NewObjectPB.init()Added ICD_NewObjectPB.init(header: ICDHeader, parentObject: ICAObject, objectInfo: ICAObjectInfo, object: ICAObject)Added IndicatorDragConstraint.init()Added IndicatorDragConstraint.init(limitRect: Rect, slopRect: Rect, axis: DragConstraint)Added InkPoint.init()Added InkPoint.init(point: HIPoint, tabletPointData: TabletPointRec, keyModifiers: UInt32)Added LHElement.init()Added LHElement.init(lhHeight: Int16, lhAscent: Int16)Added ListDefSpec.init()Added ListRec.init()Added ListRec.init(rView: Rect, port: GrafPtr, indent: Point, cellSize: Point, visible: ListBounds, vScroll: Unmanaged<Control>!, hScroll: Unmanaged<Control>!, selFlags: Int8, lActive: Boolean, lReserved: Int8, listFlags: Int8, clikTime: Int, clikLoc: Point, mouseLoc: Point, lClickLoop: ListClickLoopUPP, lastClick: Cell, refCon: Int, listDefProc: Handle, userHandle: Handle, dataBounds: ListBounds, cells: DataHandle, maxIndex: Int16, cellArray:(Int16))Added MCEntry.init()Added MCEntry.init(mctID: MenuID, mctItem: Int16, mctRGB1: RGBColor, mctRGB2: RGBColor, mctRGB3: RGBColor, mctRGB4: RGBColor, mctReserved: Int16)Added MDEFDrawData.init()Added MDEFDrawData.init(trackingData: MenuTrackingData, context: UnsafeMutablePointer<Void>)Added MDEFDrawItemsData.init()Added MDEFDrawItemsData.init(firstItem: MenuItemIndex, lastItem: MenuItemIndex, trackingData: UnsafeMutablePointer<MenuTrackingData>, context: UnsafeMutablePointer<Void>)Added MDEFFindItemData.init()Added MDEFFindItemData.init(trackingData: MenuTrackingData, context: UnsafeMutablePointer<Void>)Added MDEFHiliteItemData.init()Added MDEFHiliteItemData.init(previousItem: MenuItemIndex, newItem: MenuItemIndex, context: UnsafeMutablePointer<Void>)Added MeasureWindowTitleRec.init()Added MeasureWindowTitleRec.init(fullTitleWidth: Int16, titleTextWidth: Int16, isUnicodeTitle: Boolean, unused: Boolean)Added MenuBarHeader.init()Added MenuBarHeader.init(lastMenu: UInt16, lastRight: Int16, mbResID: Int16)Added MenuBarMenu.init()Added MenuBarMenu.init(menu: Unmanaged<Menu>!, menuLeft: Int16)Added MenuCRsrc.init()Added MenuCRsrc.init(numEntries: Int16, mcEntryRecs: MCTable)Added MenuDefSpec.init()Added MenuItemDataRec.init()Added MenuItemDataRec.init(whichData: MenuItemDataFlags, text: StringPtr, mark: UniChar, cmdKey: UniChar, cmdKeyGlyph: UInt32, cmdKeyModifiers: UInt32, style: Style, enabled: Boolean, iconEnabled: Boolean, filler1: UInt8, iconID: Int32, iconType: UInt32, iconHandle: Handle, cmdID: MenuCommand, encoding: TextEncoding, submenuID: MenuID, submenuHandle: Unmanaged<Menu>!, fontID: Int32, refcon: URefCon, attr: OptionBits, cfText: Unmanaged<CFString>!, properties: Collection, indent: UInt32, cmdVirtualKey: UInt16, attributedText: Unmanaged<CFAttributedString>!, font: Unmanaged<CTFont>!)Added MenuTrackingData.init()Added MenuTrackingData.init(menu: Unmanaged<Menu>!, itemSelected: MenuItemIndex, itemUnderMouse: MenuItemIndex, itemRect: Rect, virtualMenuTop: Int32, virtualMenuBottom: Int32)Added NColorPickerInfo.init()Added NColorPickerInfo.init(theColor: NPMColor, dstProfile: CMProfileRef, flags: UInt32, placeWhere: DialogPlacementSpec, dialogOrigin: Point, pickerType: OSType, colorProc: NColorChangedUPP, colorProcData: URefCon, prompt: Str255, mInfo: PickerMenuItemInfo, newColorChosen: Boolean, reserved: UInt8)Added NMRec.init()Added NMRec.init(qLink: QElemPtr, qType: Int16, nmFlags: Int16, nmPrivate: SRefCon, nmReserved: Int16, nmMark: Int16, nmIcon: Handle, nmSound: Handle, nmStr: StringPtr, nmResp: NMUPP, nmRefCon: SRefCon)Added NPMColor.init()Added NPMColor.colorAdded NPMColor.init(profile: CMProfileRef, color: CMColor)Added NavCBRec.init()Added NavCBRec.init(version: UInt16, context: Unmanaged<NavDialog>!, window: WindowRef, customRect: Rect, previewRect: Rect, eventData: NavEventData, userAction: NavUserAction, reserved:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added NavDialogCreationOptions.init()Added NavDialogCreationOptions.init(version: UInt16, optionFlags: NavDialogOptionFlags, location: Point, clientName: Unmanaged<CFString>!, windowTitle: Unmanaged<CFString>!, actionButtonLabel: Unmanaged<CFString>!, cancelButtonLabel: Unmanaged<CFString>!, saveFileName: Unmanaged<CFString>!, message: Unmanaged<CFString>!, preferenceKey: UInt32, popupExtension: Unmanaged<CFArray>!, modality: WindowModality, parentWindow: WindowRef, reserved:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added NavDialogOptions.init()Added NavDialogOptions.init(version: UInt16, dialogOptionFlags: NavDialogOptionFlags, location: Point, clientName: Str255, windowTitle: Str255, actionButtonLabel: Str255, cancelButtonLabel: Str255, savedFileName: Str255, message: Str255, preferenceKey: UInt32, popupExtension: NavMenuItemSpecArrayHandle, reserved:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added NavEventData.init()Added NavEventData.eventDataParmsAdded NavEventData.init(eventDataParms: NavEventDataInfo, itemHit: Int16)Added NavEventDataInfo [struct]Added NavEventDataInfo.init()Added NavFileOrFolderInfo.init()Added NavMenuItemSpec.init()Added NavMenuItemSpec.init(version: UInt16, menuCreator: OSType, menuType: OSType, menuItemName: Str255, reserved:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added NavReplyRecord.init()Added NavReplyRecord.init(version: UInt16, validRecord: Boolean, replacing: Boolean, isStationery: Boolean, translationNeeded: Boolean, selection: AEDescList, keyScript: ScriptCode, fileTranslation: FileTranslationSpecArrayHandle, reserved1: UInt32, saveFileName: Unmanaged<CFString>!, saveFileExtensionHidden: Boolean, reserved2: UInt8, reserved:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added NavTypeList.init()Added NavTypeList.init(componentSignature: OSType, reserved: Int16, osTypeCount: Int16, osType:(OSType))Added NullStRec.init()Added NullStRec.init(teReserved: Int, nullScrap: StScrpHandle)Added PickerMenuItemInfo.init()Added PickerMenuItemInfo.init(editMenuID: Int16, cutItem: Int16, copyItem: Int16, pasteItem: Int16, clearItem: Int16, undoItem: Int16)Added ProgressTrackInfo.init()Added ProgressTrackInfo.init(phase: UInt8)Added PromiseHFSFlavor.init()Added PromiseHFSFlavor.init(fileType: OSType, fileCreator: OSType, fdFlags: UInt16, promisedFlavor: FlavorType)Added SRCallBackParam.init()Added SRCallBackParam.init(callBack: SRCallBackUPP, refCon: SRefCon)Added SRCallBackStruct.init()Added SRCallBackStruct.init(what: UInt32, message: Int, instance: SRRecognizer, status: OSErr, flags: Int16, refCon: SRefCon)Added STElement.init()Added STElement.init(stCount: Int16, stHeight: Int16, stAscent: Int16, stFont: Int16, stFace: StyleField, stSize: Int16, stColor: RGBColor)Added ScrapFlavorInfo.init()Added ScrapFlavorInfo.init(flavorType: ScrapFlavorType, flavorFlags: ScrapFlavorFlags)Added ScrapTranslationList.init()Added ScrapTranslationList.init(modDate: UInt, groupCount: UInt)Added ScrapTypeSpec.init()Added ScrapTypeSpec.init(format: ScrapType, hint: Int)Added ScriptLanguageRecord.init()Added ScriptLanguageRecord.init(fScript: ScriptCode, fLanguage: LangCode)Added ScriptLanguageSupport.init()Added ScriptLanguageSupport.init(fScriptLanguageCount: Int16, fScriptLanguageArray:(ScriptLanguageRecord))Added ScrollBarTrackInfo.init()Added ScrollBarTrackInfo.init(viewsize: Int32, pressState: ThemeTrackPressState)Added ScrpSTElement.init()Added ScrpSTElement.init(scrpStartChar: Int32, scrpHeight: Int16, scrpAscent: Int16, scrpFont: Int16, scrpFace: StyleField, scrpSize: Int16, scrpColor: RGBColor)Added SetupWindowProxyDragImageRec.init()Added SetupWindowProxyDragImageRec.init(imageGWorld: GWorldPtr, imageRgn: RgnHandle, outlineRgn: RgnHandle)Added SliderTrackInfo.init()Added SliderTrackInfo.init(thumbDir: ThemeThumbDirection, pressState: ThemeTrackPressState)Added StScrpRec.init()Added StScrpRec.init(scrpNStyles: Int16, scrpStyleTab: ScrpSTTable)Added StandardIconListCellDataRec.init()Added StandardIconListCellDataRec.init(iconHandle: Handle, font: Int16, face: Int16, size: Int16, name: Str255)Added StyleRun.init()Added StyleRun.init(startChar: Int16, styleIndex: Int16)Added TERec.init()Added TEStyleRec.init()Added TSMGlyphInfo.init()Added TSMGlyphInfo.init(range: CFRange, fontRef: ATSFontRef, collection: UInt16, glyphID: UInt16)Added TSMGlyphInfoArray.init()Added TSMGlyphInfoArray.init(numGlyphInfo: Int, glyphInfo:(TSMGlyphInfo))Added TXNATSUIFeatures.init()Added TXNATSUIFeatures.init(featureCount: Int, featureTypes: UnsafeMutablePointer<ATSUFontFeatureType>, featureSelectors: UnsafeMutablePointer<ATSUFontFeatureSelector>)Added TXNATSUIVariations.init()Added TXNATSUIVariations.init(variationCount: Int, variationAxis: UnsafeMutablePointer<ATSUFontVariationAxis>, variationValues: UnsafeMutablePointer<ATSUFontVariationValue>)Added TXNAttributeData [struct]Added TXNAttributeData.init()Added TXNBackground.init()Added TXNBackground.init(bgType: TXNBackgroundType, bg: TXNBackgroundData)Added TXNBackgroundData.init()Added TXNBackgroundData.init(color: RGBColor)Added TXNCarbonEventInfo.init()Added TXNCarbonEventInfo.init(useCarbonEvents: Boolean, filler: UInt8, flags: UInt16, fDictionary: Unmanaged<CFDictionary>!)Added TXNControlData [struct]Added TXNControlData.init()Added TXNLongRect.init()Added TXNLongRect.init(top: Int32, left: Int32, bottom: Int32, right: Int32)Added TXNMargins.init()Added TXNMargins.init(topMargin: Int16, leftMargin: Int16, bottomMargin: Int16, rightMargin: Int16)Added TXNMatchTextRecord.init()Added TXNMatchTextRecord.init(iTextPtr: UnsafePointer<Void>, iTextToMatchLength: Int, iTextEncoding: TextEncoding)Added TXNTab.init()Added TXNTab.init(value: Int16, tabType: TXNTabType, filler: UInt8)Added TXNTypeAttributes.init()Added TXNTypeAttributes.dataAdded TXNTypeAttributes.init(tag: TXNTypeRunAttributes, size: Int, data: TXNAttributeData)Added TabletPointRec.init()Added TabletPointRec.init(absX: Int32, absY: Int32, absZ: Int32, buttons: UInt16, pressure: UInt16, tiltX: Int16, tiltY: Int16, rotation: UInt16, tangentialPressure: Int16, deviceID: UInt16, vendor1: Int16, vendor2: Int16, vendor3: Int16)Added TabletProximityRec.init()Added TabletProximityRec.init(vendorID: UInt16, tabletID: UInt16, pointerID: UInt16, deviceID: UInt16, systemTabletID: UInt16, vendorPointerType: UInt16, pointerSerialNumber: UInt32, uniqueID: UInt64, capabilityMask: UInt32, pointerType: UInt8, enterProximity: UInt8)Added TextServiceInfo.init()Added TextServiceInfo.init(fComponent: Component, fItemName: Str255)Added TextServiceList.init()Added TextServiceList.init(fTextServiceCount: Int16, fServices:(TextServiceInfo))Added TextStyle.init()Added TextStyle.init(tsFont: Int16, tsFace: StyleField, tsSize: Int16, tsColor: RGBColor)Added ThemeButtonDrawInfo.init()Added ThemeButtonDrawInfo.init(state: ThemeDrawState, value: ThemeButtonValue, adornment: ThemeButtonAdornment)Added ThemeTrackDrawInfo.init()Added ThemeWindowMetrics.init()Added ThemeWindowMetrics.init(metricSize: UInt16, titleHeight: Int16, titleWidth: Int16, popupTabOffset: Int16, popupTabWidth: Int16, popupTabPosition: UInt16)Added TransitionWindowOptions.init()Added TransitionWindowOptions.init(version: UInt32, duration: EventTime, window: WindowRef, userData: UnsafeMutablePointer<Void>)Added TypeSelectRecord.init()Added TypeSelectRecord.init(tsrLastKeyTime: UInt32, tsrScript: ScriptCode, tsrKeyStrokes: Str63)Added URLCallbackInfo.init()Added URLCallbackInfo.init(version: UInt32, urlRef: URLReference, property: UnsafePointer<Int8>, currentSize: UInt32, systemEvent: UnsafeMutablePointer<EventRecord>)Added WStateData.init()Added WStateData.init(userState: Rect, stdState: Rect)Added WinCTab.init()Added WinCTab.init(wCSeed: Int, wCReserved: Int16, ctSize: Int16, ctTable:(ColorSpec, ColorSpec, ColorSpec, ColorSpec, ColorSpec))Added WindowDefSpec.init()Added kComponentBundleInputModeDictKeyAdded kComponentBundleInvisibleInSystemUIKeyAdded kHIAboutBoxCopyrightKeyAdded kHIAboutBoxDescriptionKeyAdded kHIAboutBoxNameKeyAdded kHIAboutBoxStringFileKeyAdded kHIAboutBoxVersionKeyAdded kHIApplicationClassIDAdded kHIBevelButtonClassIDAdded kHIChasingArrowsClassIDAdded kHICheckBoxClassIDAdded kHICheckBoxGroupClassIDAdded kHIClockViewClassIDAdded kHICocoaViewClassIDAdded kHIComboBoxClassIDAdded kHIDataBrowserClassIDAdded kHIDisclosureButtonClassIDAdded kHIDisclosureTriangleClassIDAdded kHIGroupBoxClassIDAdded kHIGrowBoxViewClassIDAdded kHIIconViewClassIDAdded kHIImageViewClassIDAdded kHIImageWellClassIDAdded kHILittleArrowsClassIDAdded kHIMenuViewClassIDAdded kHIPictureViewClassIDAdded kHIPlacardViewClassIDAdded kHIPopupArrowClassIDAdded kHIPopupButtonClassIDAdded kHIProgressBarClassIDAdded kHIPushButtonClassIDAdded kHIRadioButtonClassIDAdded kHIRadioGroupClassIDAdded kHIRelevanceBarClassIDAdded kHIRoundButtonClassIDAdded kHIScrollBarClassIDAdded kHIScrollViewClassIDAdded kHISearchFieldClassIDAdded kHISegmentedViewClassIDAdded kHIServicesMenuCharCodeAdded kHIServicesMenuItemNameAdded kHIServicesMenuKeyModifiersAdded kHIServicesMenuProviderNameAdded kHISliderClassIDAdded kHIStandardMenuViewClassIDAdded kHIStaticTextViewClassIDAdded kHISymbolicHotKeyCodeAdded kHISymbolicHotKeyEnabledAdded kHISymbolicHotKeyModifiersAdded kHITabbedViewClassIDAdded kHITextFieldClassIDAdded kHITextLengthFilterClassIDAdded kHIToolbarCustomizeIdentifierAdded kHIToolbarDataKeyAdded kHIToolbarFlexibleSpaceIdentifierAdded kHIToolbarFontsItemIdentifierAdded kHIToolbarIdentifierKeyAdded kHIToolbarItemClassIDAdded kHIToolbarPrintItemIdentifierAdded kHIToolbarSeparatorIdentifierAdded kHIToolbarSpaceIdentifierAdded kHIUserPaneClassIDAdded kHIViewClassIDAdded kHIVisualSeparatorClassIDAdded kHIWindowHeaderViewClassIDAdded kScrapClipboardScrapAdded kScrapFindScrapAdded kTSInputMethodAlternateIconFileKeyAdded kTSInputMethodIconFileKeyAdded kTSInputModeAlternateMenuIconFileKeyAdded kTSInputModeDefaultStateKeyAdded kTSInputModeIsVisibleKeyAdded kTSInputModeJISKeyboardShortcutKeyAdded kTSInputModeKeyEquivalentKeyAdded kTSInputModeKeyEquivalentModifiersKeyAdded kTSInputModeListKeyAdded kTSInputModeMenuIconFileKeyAdded kTSInputModePaletteIconFileKeyAdded kTSInputModePaletteItemAltIconKeyAdded kTSInputModePaletteItemEnabledKeyAdded kTSInputModePaletteItemIDKeyAdded kTSInputModePaletteItemIconKeyAdded kTSInputModePaletteItemKeyEquivalentKeyAdded kTSInputModePaletteItemKeyEquivalentModifiersKeyAdded kTSInputModePaletteItemStateKeyAdded kTSInputModePaletteItemTitleKeyAdded kTSInputModePaletteItemTypeKeyAdded kTSInputModePrimaryInScriptKeyAdded kTSInputModeScriptKeyAdded kTSVisibleInputModeOrderedArrayKeyAdded kTXNActionKeyMapperKeyAdded kTXNActionNameMapperKeyAdded kTXNCommandTargetKeyAdded kTXNCommandUpdateKeyAdded kTXNFontPanelEventHandlerKeyAdded kTXNTSMDocumentAccessHandlerKeyAdded kTXNTextHandlerKeyAdded kTXNWheelMouseEventHandlerKeyAdded kTXNWindowEventHandlerKeyAdded kTXNWindowResizeEventHandlerKeyAdded kTextServiceInputModeBopomofoAdded kTextServiceInputModeHangulAdded kTextServiceInputModeJapaneseAdded kTextServiceInputModeJapaneseFirstNameAdded kTextServiceInputModeJapaneseFullWidthRomanAdded kTextServiceInputModeJapaneseHalfWidthKanaAdded kTextServiceInputModeJapaneseHiraganaAdded kTextServiceInputModeJapaneseKatakanaAdded kTextServiceInputModeJapaneseLastNameAdded kTextServiceInputModeJapanesePlaceNameAdded kTextServiceInputModeKoreanAdded kTextServiceInputModePasswordAdded kTextServiceInputModeRomanAdded kTextServiceInputModeSimpChineseAdded kTextServiceInputModeTradChineseAdded kTextServiceInputModeTradChinesePlaceNameAdded kThemeAppearanceAquaAdded kThemeAppearanceAquaBlueAdded kThemeAppearanceAquaGraphiteAdded kThemeAppearancePlatinumAdded kThemeMenuBarInactiveModified AlertStdAlertParamRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AlertStdAlertParamRec {     var movable: Boolean     var helpButton: Boolean     var filterProc: ModalFilterUPP     var defaultText: ConstStringPtr     var cancelText: ConstStringPtr     var otherText: ConstStringPtr     var defaultButton: Int16     var cancelButton: Int16     var position: UInt16 } ``` |
| To | ``` struct AlertStdAlertParamRec {     var movable: Boolean     var helpButton: Boolean     var filterProc: ModalFilterUPP     var defaultText: ConstStringPtr     var cancelText: ConstStringPtr     var otherText: ConstStringPtr     var defaultButton: Int16     var cancelButton: Int16     var position: UInt16     init()     init(movable movable: Boolean, helpButton helpButton: Boolean, filterProc filterProc: ModalFilterUPP, defaultText defaultText: ConstStringPtr, cancelText cancelText: ConstStringPtr, otherText otherText: ConstStringPtr, defaultButton defaultButton: Int16, cancelButton cancelButton: Int16, position position: UInt16) } ``` |

Modified AlertStdCFStringAlertParamRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AlertStdCFStringAlertParamRec {     var version: UInt32     var movable: Boolean     var helpButton: Boolean     var defaultText: Unmanaged<CFString>!     var cancelText: Unmanaged<CFString>!     var otherText: Unmanaged<CFString>!     var defaultButton: Int16     var cancelButton: Int16     var position: UInt16     var flags: OptionBits     var icon: Unmanaged<Icon>! } ``` |
| To | ``` struct AlertStdCFStringAlertParamRec {     var version: UInt32     var movable: Boolean     var helpButton: Boolean     var defaultText: Unmanaged<CFString>!     var cancelText: Unmanaged<CFString>!     var otherText: Unmanaged<CFString>!     var defaultButton: Int16     var cancelButton: Int16     var position: UInt16     var flags: OptionBits     var icon: IconRef     init()     init(version version: UInt32, movable movable: Boolean, helpButton helpButton: Boolean, defaultText defaultText: Unmanaged<CFString>!, cancelText cancelText: Unmanaged<CFString>!, otherText otherText: Unmanaged<CFString>!, defaultButton defaultButton: Int16, cancelButton cancelButton: Int16, position position: UInt16, flags flags: OptionBits, icon icon: IconRef) } ``` |

Modified AlertStdCFStringAlertParamRec.icon

|  | Declaration |
| --- | --- |
| From | ``` var icon: Unmanaged<Icon>! ``` |
| To | ``` var icon: IconRef ``` |

Modified AlertTemplate [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AlertTemplate {     var boundsRect: Rect     var itemsID: Int16     var stages: StageList } ``` |
| To | ``` struct AlertTemplate {     var boundsRect: Rect     var itemsID: Int16     var stages: StageList     init()     init(boundsRect boundsRect: Rect, itemsID itemsID: Int16, stages stages: StageList) } ``` |

Modified BasicWindowDescription [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BasicWindowDescription {     var descriptionSize: UInt32     var windowContentRect: Rect     var windowZoomRect: Rect     var windowRefCon: URefCon     var windowStateFlags: UInt32     var windowPositionMethod: WindowPositionMethod     var windowDefinitionVersion: UInt32 } ``` |
| To | ``` struct BasicWindowDescription {     var descriptionSize: UInt32     var windowContentRect: Rect     var windowZoomRect: Rect     var windowRefCon: URefCon     var windowStateFlags: UInt32     var windowPositionMethod: WindowPositionMethod     var windowDefinitionVersion: UInt32     init() } ``` |

Modified CalibratorInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CalibratorInfo {     var dataSize: UInt32     var displayID: CMDisplayIDType     var profileLocationSize: UInt32     var profileLocationPtr: UnsafePointer<CMProfileLocation>     var eventProc: CalibrateEventUPP     var isGood: Boolean } ``` |
| To | ``` struct CalibratorInfo {     var dataSize: UInt32     var displayID: CMDisplayIDType     var profileLocationSize: UInt32     var profileLocationPtr: UnsafeMutablePointer<CMProfileLocation>     var eventProc: CalibrateEventUPP     var isGood: Boolean     init()     init(dataSize dataSize: UInt32, displayID displayID: CMDisplayIDType, profileLocationSize profileLocationSize: UInt32, profileLocationPtr profileLocationPtr: UnsafeMutablePointer<CMProfileLocation>, eventProc eventProc: CalibrateEventUPP, isGood isGood: Boolean) } ``` |

Modified CalibratorInfo.profileLocationPtr

|  | Declaration |
| --- | --- |
| From | ``` var profileLocationPtr: UnsafePointer<CMProfileLocation> ``` |
| To | ``` var profileLocationPtr: UnsafeMutablePointer<CMProfileLocation> ``` |

Modified ContextualMenuInterfaceStruct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ContextualMenuInterfaceStruct {     var _reserved: UnsafePointer<()>     var QueryInterface: CFunctionPointer<((UnsafePointer<()>, CFUUIDBytes, UnsafePointer<UnsafePointer<()>>) -> Int32)>     var AddRef: CFunctionPointer<((UnsafePointer<()>) -> UInt32)>     var Release: CFunctionPointer<((UnsafePointer<()>) -> UInt32)>     var ExamineContext: CFunctionPointer<((UnsafePointer<()>, ConstUnsafePointer<AEDesc>, UnsafePointer<AEDescList>) -> OSStatus)>     var HandleSelection: CFunctionPointer<((UnsafePointer<()>, UnsafePointer<AEDesc>, Int32) -> OSStatus)>     var PostMenuCleanup: CFunctionPointer<((UnsafePointer<()>) -> Void)> } ``` |
| To | ``` struct ContextualMenuInterfaceStruct {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, CFUUIDBytes, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int32)>     var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UInt32)>     var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UInt32)>     var ExamineContext: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<AEDesc>, UnsafeMutablePointer<AEDescList>) -> OSStatus)>     var HandleSelection: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<AEDesc>, Int32) -> OSStatus)>     var PostMenuCleanup: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, CFUUIDBytes, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int32)>, AddRef AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UInt32)>, Release Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UInt32)>, ExamineContext ExamineContext: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<AEDesc>, UnsafeMutablePointer<AEDescList>) -> OSStatus)>, HandleSelection HandleSelection: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<AEDesc>, Int32) -> OSStatus)>, PostMenuCleanup PostMenuCleanup: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>) } ``` |

Modified ContextualMenuInterfaceStruct.AddRef

|  | Declaration |
| --- | --- |
| From | ``` var AddRef: CFunctionPointer<((UnsafePointer<()>) -> UInt32)> ``` |
| To | ``` var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UInt32)> ``` |

Modified ContextualMenuInterfaceStruct.ExamineContext

|  | Declaration |
| --- | --- |
| From | ``` var ExamineContext: CFunctionPointer<((UnsafePointer<()>, ConstUnsafePointer<AEDesc>, UnsafePointer<AEDescList>) -> OSStatus)> ``` |
| To | ``` var ExamineContext: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<AEDesc>, UnsafeMutablePointer<AEDescList>) -> OSStatus)> ``` |

Modified ContextualMenuInterfaceStruct.HandleSelection

|  | Declaration |
| --- | --- |
| From | ``` var HandleSelection: CFunctionPointer<((UnsafePointer<()>, UnsafePointer<AEDesc>, Int32) -> OSStatus)> ``` |
| To | ``` var HandleSelection: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<AEDesc>, Int32) -> OSStatus)> ``` |

Modified ContextualMenuInterfaceStruct.PostMenuCleanup

|  | Declaration |
| --- | --- |
| From | ``` var PostMenuCleanup: CFunctionPointer<((UnsafePointer<()>) -> Void)> ``` |
| To | ``` var PostMenuCleanup: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified ContextualMenuInterfaceStruct.QueryInterface

|  | Declaration |
| --- | --- |
| From | ``` var QueryInterface: CFunctionPointer<((UnsafePointer<()>, CFUUIDBytes, UnsafePointer<UnsafePointer<()>>) -> Int32)> ``` |
| To | ``` var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, CFUUIDBytes, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int32)> ``` |

Modified ContextualMenuInterfaceStruct.Release

|  | Declaration |
| --- | --- |
| From | ``` var Release: CFunctionPointer<((UnsafePointer<()>) -> UInt32)> ``` |
| To | ``` var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UInt32)> ``` |

Modified ControlEditTextSelectionRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ControlEditTextSelectionRec {     var selStart: Int16     var selEnd: Int16 } ``` |
| To | ``` struct ControlEditTextSelectionRec {     var selStart: Int16     var selEnd: Int16     init()     init(selStart selStart: Int16, selEnd selEnd: Int16) } ``` |

Modified ControlFontStyleRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ControlFontStyleRec {     var flags: Int16     var font: Int16     var size: Int16     var style: Int16     var mode: Int16     var just: Int16     var foreColor: RGBColor     var backColor: RGBColor } ``` |
| To | ``` struct ControlFontStyleRec {     var flags: Int16     var font: Int16     var size: Int16     var style: Int16     var mode: Int16     var just: Int16     var foreColor: RGBColor     var backColor: RGBColor     init()     init(flags flags: Int16, font font: Int16, size size: Int16, style style: Int16, mode mode: Int16, just just: Int16, foreColor foreColor: RGBColor, backColor backColor: RGBColor) } ``` |

Modified ControlID [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ControlID {     var signature: OSType     var id: Int32 } ``` |
| To | ``` struct ControlID {     var signature: OSType     var id: Int32     init()     init(signature signature: OSType, id id: Int32) } ``` |

Modified ControlImageContentInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ControlImageContentInfo {     var contentType: ControlContentType } ``` |
| To | ``` struct ControlImageContentInfo {     var contentType: ControlContentType     init() } ``` |

Modified ControlKind [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ControlKind {     var signature: OSType     var kind: OSType } ``` |
| To | ``` struct ControlKind {     var signature: OSType     var kind: OSType     init()     init(signature signature: OSType, kind kind: OSType) } ``` |

Modified ControlTabEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ControlTabEntry {     var icon: UnsafePointer<ControlButtonContentInfo>     var name: Unmanaged<CFString>!     var enabled: Boolean } ``` |
| To | ``` struct ControlTabEntry {     var icon: UnsafeMutablePointer<ControlButtonContentInfo>     var name: Unmanaged<CFString>!     var enabled: Boolean     init()     init(icon icon: UnsafeMutablePointer<ControlButtonContentInfo>, name name: Unmanaged<CFString>!, enabled enabled: Boolean) } ``` |

Modified ControlTabEntry.icon

|  | Declaration |
| --- | --- |
| From | ``` var icon: UnsafePointer<ControlButtonContentInfo> ``` |
| To | ``` var icon: UnsafeMutablePointer<ControlButtonContentInfo> ``` |

Modified ControlTabInfoRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ControlTabInfoRec {     var version: Int16     var iconSuiteID: Int16     var name: Str255 } ``` |
| To | ``` struct ControlTabInfoRec {     var version: Int16     var iconSuiteID: Int16     var name: Str255     init()     init(version version: Int16, iconSuiteID iconSuiteID: Int16, name name: Str255) } ``` |

Modified ControlTabInfoRecV1 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ControlTabInfoRecV1 {     var version: Int16     var iconSuiteID: Int16     var name: Unmanaged<CFString>! } ``` |
| To | ``` struct ControlTabInfoRecV1 {     var version: Int16     var iconSuiteID: Int16     var name: Unmanaged<CFString>!     init()     init(version version: Int16, iconSuiteID iconSuiteID: Int16, name name: Unmanaged<CFString>!) } ``` |

Modified ControlTemplate [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ControlTemplate {     var controlRect: Rect     var controlValue: Int16     var controlVisible: Boolean     var fill: UInt8     var controlMaximum: Int16     var controlMinimum: Int16     var controlDefProcID: Int16     var controlReference: Int32     var controlTitle: Str255 } ``` |
| To | ``` struct ControlTemplate {     var controlRect: Rect     var controlValue: Int16     var controlVisible: Boolean     var fill: UInt8     var controlMaximum: Int16     var controlMinimum: Int16     var controlDefProcID: Int16     var controlReference: Int32     var controlTitle: Str255     init()     init(controlRect controlRect: Rect, controlValue controlValue: Int16, controlVisible controlVisible: Boolean, fill fill: UInt8, controlMaximum controlMaximum: Int16, controlMinimum controlMinimum: Int16, controlDefProcID controlDefProcID: Int16, controlReference controlReference: Int32, controlTitle controlTitle: Str255) } ``` |

Modified CtlCTab [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CtlCTab {     var ccSeed: Int32     var ccRider: Int16     var ctSize: Int16     var ctTable: (ColorSpec, ColorSpec, ColorSpec, ColorSpec) } ``` |
| To | ``` struct CtlCTab {     var ccSeed: Int32     var ccRider: Int16     var ctSize: Int16     var ctTable: (ColorSpec, ColorSpec, ColorSpec, ColorSpec)     init()     init(ccSeed ccSeed: Int32, ccRider ccRider: Int16, ctSize ctSize: Int16, ctTable ctTable: (ColorSpec, ColorSpec, ColorSpec, ColorSpec)) } ``` |

Modified DataBrowserAccessibilityItemInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DataBrowserAccessibilityItemInfo {     var version: UInt32 } ``` |
| To | ``` struct DataBrowserAccessibilityItemInfo {     var version: UInt32     init() } ``` |

Modified DataBrowserAccessibilityItemInfoV0 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DataBrowserAccessibilityItemInfoV0 {     var container: DataBrowserItemID     var item: DataBrowserItemID     var columnProperty: DataBrowserPropertyID     var propertyPart: DataBrowserPropertyPart } ``` |
| To | ``` struct DataBrowserAccessibilityItemInfoV0 {     var container: DataBrowserItemID     var item: DataBrowserItemID     var columnProperty: DataBrowserPropertyID     var propertyPart: DataBrowserPropertyPart     init()     init(container container: DataBrowserItemID, item item: DataBrowserItemID, columnProperty columnProperty: DataBrowserPropertyID, propertyPart propertyPart: DataBrowserPropertyPart) } ``` |

Modified DataBrowserAccessibilityItemInfoV1 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DataBrowserAccessibilityItemInfoV1 {     var container: DataBrowserItemID     var item: DataBrowserItemID     var columnProperty: DataBrowserPropertyID     var propertyPart: DataBrowserPropertyPart     var rowIndex: DataBrowserTableViewRowIndex     var columnIndex: DataBrowserTableViewColumnIndex } ``` |
| To | ``` struct DataBrowserAccessibilityItemInfoV1 {     var container: DataBrowserItemID     var item: DataBrowserItemID     var columnProperty: DataBrowserPropertyID     var propertyPart: DataBrowserPropertyPart     var rowIndex: DataBrowserTableViewRowIndex     var columnIndex: DataBrowserTableViewColumnIndex     init()     init(container container: DataBrowserItemID, item item: DataBrowserItemID, columnProperty columnProperty: DataBrowserPropertyID, propertyPart propertyPart: DataBrowserPropertyPart, rowIndex rowIndex: DataBrowserTableViewRowIndex, columnIndex columnIndex: DataBrowserTableViewColumnIndex) } ``` |

Modified DataBrowserCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DataBrowserCallbacks {     var version: UInt32 } ``` |
| To | ``` struct DataBrowserCallbacks {     var version: UInt32     init() } ``` |

Modified DataBrowserCustomCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DataBrowserCustomCallbacks {     var version: UInt32 } ``` |
| To | ``` struct DataBrowserCustomCallbacks {     var version: UInt32     init() } ``` |

Modified DataBrowserListViewColumnDesc [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DataBrowserListViewColumnDesc {     var propertyDesc: DataBrowserTableViewColumnDesc     var headerBtnDesc: DataBrowserListViewHeaderDesc } ``` |
| To | ``` struct DataBrowserListViewColumnDesc {     var propertyDesc: DataBrowserTableViewColumnDesc     var headerBtnDesc: DataBrowserListViewHeaderDesc     init()     init(propertyDesc propertyDesc: DataBrowserTableViewColumnDesc, headerBtnDesc headerBtnDesc: DataBrowserListViewHeaderDesc) } ``` |

Modified DataBrowserListViewHeaderDesc [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DataBrowserListViewHeaderDesc {     var version: UInt32     var minimumWidth: UInt16     var maximumWidth: UInt16     var titleOffset: Int16     var titleString: Unmanaged<CFString>!     var initialOrder: DataBrowserSortOrder     var btnFontStyle: ControlFontStyleRec     var btnContentInfo: ControlButtonContentInfo } ``` |
| To | ``` struct DataBrowserListViewHeaderDesc {     var version: UInt32     var minimumWidth: UInt16     var maximumWidth: UInt16     var titleOffset: Int16     var titleString: Unmanaged<CFString>!     var initialOrder: DataBrowserSortOrder     var btnFontStyle: ControlFontStyleRec     var btnContentInfo: ControlButtonContentInfo     init()     init(version version: UInt32, minimumWidth minimumWidth: UInt16, maximumWidth maximumWidth: UInt16, titleOffset titleOffset: Int16, titleString titleString: Unmanaged<CFString>!, initialOrder initialOrder: DataBrowserSortOrder, btnFontStyle btnFontStyle: ControlFontStyleRec, btnContentInfo btnContentInfo: ControlButtonContentInfo) } ``` |

Modified DataBrowserPropertyDesc [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DataBrowserPropertyDesc {     var propertyID: DataBrowserPropertyID     var propertyType: DataBrowserPropertyType     var propertyFlags: DataBrowserPropertyFlags } ``` |
| To | ``` struct DataBrowserPropertyDesc {     var propertyID: DataBrowserPropertyID     var propertyType: DataBrowserPropertyType     var propertyFlags: DataBrowserPropertyFlags     init()     init(propertyID propertyID: DataBrowserPropertyID, propertyType propertyType: DataBrowserPropertyType, propertyFlags propertyFlags: DataBrowserPropertyFlags) } ``` |

Modified DialogTemplate [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DialogTemplate {     var boundsRect: Rect     var procID: Int16     var visible: Boolean     var filler1: Boolean     var goAwayFlag: Boolean     var filler2: Boolean     var refCon: Int32     var itemsID: Int16     var title: Str255 } ``` |
| To | ``` struct DialogTemplate {     var boundsRect: Rect     var procID: Int16     var visible: Boolean     var filler1: Boolean     var goAwayFlag: Boolean     var filler2: Boolean     var refCon: Int32     var itemsID: Int16     var title: Str255     init()     init(boundsRect boundsRect: Rect, procID procID: Int16, visible visible: Boolean, filler1 filler1: Boolean, goAwayFlag goAwayFlag: Boolean, filler2 filler2: Boolean, refCon refCon: Int32, itemsID itemsID: Int16, title title: Str255) } ``` |

Modified EvQEl [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct EvQEl {     var qLink: QElemPtr     var qType: Int16     var evtQWhat: EventKind     var evtQMessage: UInt     var evtQWhen: UInt32     var evtQWhere: Point     var evtQModifiers: EventModifiers } ``` |
| To | ``` struct EvQEl {     var qLink: QElemPtr     var qType: Int16     var evtQWhat: EventKind     var evtQMessage: UInt     var evtQWhen: UInt32     var evtQWhere: Point     var evtQModifiers: EventModifiers     init()     init(qLink qLink: QElemPtr, qType qType: Int16, evtQWhat evtQWhat: EventKind, evtQMessage evtQMessage: UInt, evtQWhen evtQWhen: UInt32, evtQWhere evtQWhere: Point, evtQModifiers evtQModifiers: EventModifiers) } ``` |

Modified EventHotKeyID [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct EventHotKeyID {     var signature: OSType     var id: UInt32 } ``` |
| To | ``` struct EventHotKeyID {     var signature: OSType     var id: UInt32     init()     init(signature signature: OSType, id id: UInt32) } ``` |

Modified EventRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct EventRecord {     var what: EventKind     var message: UInt     var when: UInt32     var `where`: Point     var modifiers: EventModifiers } ``` |
| To | ``` struct EventRecord {     var what: EventKind     var message: UInt     var when: UInt32     var `where`: Point     var modifiers: EventModifiers     init()     init(what what: EventKind, message message: UInt, when when: UInt32, `where` `where`: Point, modifiers modifiers: EventModifiers) } ``` |

Modified EventTypeSpec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct EventTypeSpec {     var eventClass: OSType     var eventKind: UInt32 } ``` |
| To | ``` struct EventTypeSpec {     var eventClass: OSType     var eventKind: UInt32     init()     init(eventClass eventClass: OSType, eventKind eventKind: UInt32) } ``` |

Modified FileTranslationList [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FileTranslationList {     var modDate: UInt     var groupCount: UInt } ``` |
| To | ``` struct FileTranslationList {     var modDate: UInt     var groupCount: UInt     init()     init(modDate modDate: UInt, groupCount groupCount: UInt) } ``` |

Modified FileTranslationSpec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FileTranslationSpec {     var componentSignature: OSType     var translationSystemInfo: ConstUnsafePointer<()>     var src: FileTypeSpec     var dst: FileTypeSpec } ``` |
| To | ``` struct FileTranslationSpec {     var componentSignature: OSType     var translationSystemInfo: UnsafePointer<Void>     var src: FileTypeSpec     var dst: FileTypeSpec     init()     init(componentSignature componentSignature: OSType, translationSystemInfo translationSystemInfo: UnsafePointer<Void>, src src: FileTypeSpec, dst dst: FileTypeSpec) } ``` |

Modified FileTranslationSpec.translationSystemInfo

|  | Declaration |
| --- | --- |
| From | ``` var translationSystemInfo: ConstUnsafePointer<()> ``` |
| To | ``` var translationSystemInfo: UnsafePointer<Void> ``` |

Modified FileTypeSpec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FileTypeSpec {     var format: FileType     var hint: Int     var flags: TranslationAttributes     var catInfoType: OSType     var catInfoCreator: OSType } ``` |
| To | ``` struct FileTypeSpec {     var format: FileType     var hint: Int     var flags: TranslationAttributes     var catInfoType: OSType     var catInfoCreator: OSType     init()     init(format format: FileType, hint hint: Int, flags flags: TranslationAttributes, catInfoType catInfoType: OSType, catInfoCreator catInfoCreator: OSType) } ``` |

Modified FontSelectionQDStyle [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FontSelectionQDStyle {     var version: UInt32     var instance: FMFontFamilyInstance     var size: FMFontSize     var hasColor: Boolean     var reserved: UInt8     var color: RGBColor } ``` |
| To | ``` struct FontSelectionQDStyle {     var version: UInt32     var instance: FMFontFamilyInstance     var size: FMFontSize     var hasColor: Boolean     var reserved: UInt8     var color: RGBColor     init()     init(version version: UInt32, instance instance: FMFontFamilyInstance, size size: FMFontSize, hasColor hasColor: Boolean, reserved reserved: UInt8, color color: RGBColor) } ``` |

Modified GetGrowImageRegionRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct GetGrowImageRegionRec {     var growRect: Rect     var growImageRegion: RgnHandle } ``` |
| To | ``` struct GetGrowImageRegionRec {     var growRect: Rect     var growImageRegion: RgnHandle     init()     init(growRect growRect: Rect, growImageRegion growImageRegion: RgnHandle) } ``` |

Modified GetWindowRegionRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct GetWindowRegionRec {     var winRgn: RgnHandle     var regionCode: WindowRegionCode } ``` |
| To | ``` struct GetWindowRegionRec {     var winRgn: RgnHandle     var regionCode: WindowRegionCode     init()     init(winRgn winRgn: RgnHandle, regionCode regionCode: WindowRegionCode) } ``` |

Modified HFSFlavor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HFSFlavor {     var fileType: OSType     var fileCreator: OSType     var fdFlags: UInt16     var fileSpec: FSSpec } ``` |
| To | ``` struct HFSFlavor {     var fileType: OSType     var fileCreator: OSType     var fdFlags: UInt16     var fileSpec: FSSpec     init()     init(fileType fileType: OSType, fileCreator fileCreator: OSType, fdFlags fdFlags: UInt16, fileSpec fileSpec: FSSpec) } ``` |

Modified HIAxisPosition [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIAxisPosition {     var toView: Unmanaged<HIView>!     var kind: HIPositionKind     var offset: CGFloat } ``` |
| To | ``` struct HIAxisPosition {     var toView: Unmanaged<HIView>!     var kind: HIPositionKind     var offset: CGFloat     init()     init(toView toView: Unmanaged<HIView>!, kind kind: HIPositionKind, offset offset: CGFloat) } ``` |

Modified HIAxisScale [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIAxisScale {     var toView: Unmanaged<HIView>!     var kind: HIScaleKind     var ratio: CGFloat } ``` |
| To | ``` struct HIAxisScale {     var toView: Unmanaged<HIView>!     var kind: HIScaleKind     var ratio: CGFloat     init()     init(toView toView: Unmanaged<HIView>!, kind kind: HIScaleKind, ratio ratio: CGFloat) } ``` |

Modified HIBinding [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIBinding {     var top: HISideBinding     var left: HISideBinding     var bottom: HISideBinding     var right: HISideBinding } ``` |
| To | ``` struct HIBinding {     var top: HISideBinding     var left: HISideBinding     var bottom: HISideBinding     var right: HISideBinding     init()     init(top top: HISideBinding, left left: HISideBinding, bottom bottom: HISideBinding, right right: HISideBinding) } ``` |

Modified HICommand [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HICommand {     var attributes: UInt32     var commandID: UInt32 } ``` |
| To | ``` struct HICommand {     var attributes: UInt32     var commandID: UInt32     init() } ``` |

Modified HICommandExtended [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HICommandExtended {     var attributes: UInt32     var commandID: UInt32 } ``` |
| To | ``` struct HICommandExtended {     var attributes: UInt32     var commandID: UInt32     init() } ``` |

Modified HIContentBorderMetrics [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIContentBorderMetrics {     var top: CGFloat     var left: CGFloat     var bottom: CGFloat     var right: CGFloat } ``` |
| To | ``` struct HIContentBorderMetrics {     var top: CGFloat     var left: CGFloat     var bottom: CGFloat     var right: CGFloat     init()     init(top top: CGFloat, left left: CGFloat, bottom bottom: CGFloat, right right: CGFloat) } ``` |

Modified HILayoutInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HILayoutInfo {     var version: UInt32     var binding: HIBinding     var scale: HIScaling     var position: HIPositioning } ``` |
| To | ``` struct HILayoutInfo {     var version: UInt32     var binding: HIBinding     var scale: HIScaling     var position: HIPositioning     init()     init(version version: UInt32, binding binding: HIBinding, scale scale: HIScaling, position position: HIPositioning) } ``` |

Modified HIPositioning [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIPositioning {     var x: HIAxisPosition     var y: HIAxisPosition } ``` |
| To | ``` struct HIPositioning {     var x: HIAxisPosition     var y: HIAxisPosition     init()     init(x x: HIAxisPosition, y y: HIAxisPosition) } ``` |

Modified HIScaling [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIScaling {     var x: HIAxisScale     var y: HIAxisScale } ``` |
| To | ``` struct HIScaling {     var x: HIAxisScale     var y: HIAxisScale     init()     init(x x: HIAxisScale, y y: HIAxisScale) } ``` |

Modified HIScrollBarTrackInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIScrollBarTrackInfo {     var version: UInt32     var enableState: ThemeTrackEnableState     var pressState: ThemeTrackPressState     var viewsize: CGFloat } ``` |
| To | ``` struct HIScrollBarTrackInfo {     var version: UInt32     var enableState: ThemeTrackEnableState     var pressState: ThemeTrackPressState     var viewsize: CGFloat     init()     init(version version: UInt32, enableState enableState: ThemeTrackEnableState, pressState pressState: ThemeTrackPressState, viewsize viewsize: CGFloat) } ``` |

Modified HISideBinding [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HISideBinding {     var toView: Unmanaged<HIView>!     var kind: HIBindingKind     var offset: CGFloat } ``` |
| To | ``` struct HISideBinding {     var toView: Unmanaged<HIView>!     var kind: HIBindingKind     var offset: CGFloat     init()     init(toView toView: Unmanaged<HIView>!, kind kind: HIBindingKind, offset offset: CGFloat) } ``` |

Modified HIThemeAnimationFrameInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeAnimationFrameInfo {     var index: UInt32 } ``` |
| To | ``` struct HIThemeAnimationFrameInfo {     var index: UInt32     init()     init(index index: UInt32) } ``` |

Modified HIThemeAnimationTimeInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeAnimationTimeInfo {     var start: CFAbsoluteTime     var current: CFAbsoluteTime } ``` |
| To | ``` struct HIThemeAnimationTimeInfo {     var start: CFAbsoluteTime     var current: CFAbsoluteTime     init()     init(start start: CFAbsoluteTime, current current: CFAbsoluteTime) } ``` |

Modified HIThemeBackgroundDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeBackgroundDrawInfo {     var version: UInt32     var state: ThemeDrawState     var kind: ThemeBackgroundKind } ``` |
| To | ``` struct HIThemeBackgroundDrawInfo {     var version: UInt32     var state: ThemeDrawState     var kind: ThemeBackgroundKind     init()     init(version version: UInt32, state state: ThemeDrawState, kind kind: ThemeBackgroundKind) } ``` |

Modified HIThemeButtonDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeButtonDrawInfo {     var version: UInt32     var state: ThemeDrawState     var kind: ThemeButtonKind     var value: ThemeButtonValue     var adornment: ThemeButtonAdornment } ``` |
| To | ``` struct HIThemeButtonDrawInfo {     var version: UInt32     var state: ThemeDrawState     var kind: ThemeButtonKind     var value: ThemeButtonValue     var adornment: ThemeButtonAdornment     init() } ``` |

Modified HIThemeChasingArrowsDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeChasingArrowsDrawInfo {     var version: UInt32     var state: ThemeDrawState     var index: UInt32 } ``` |
| To | ``` struct HIThemeChasingArrowsDrawInfo {     var version: UInt32     var state: ThemeDrawState     var index: UInt32     init()     init(version version: UInt32, state state: ThemeDrawState, index index: UInt32) } ``` |

Modified HIThemeFrameDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeFrameDrawInfo {     var version: UInt32     var kind: HIThemeFrameKind     var state: ThemeDrawState     var isFocused: Boolean } ``` |
| To | ``` struct HIThemeFrameDrawInfo {     var version: UInt32     var kind: HIThemeFrameKind     var state: ThemeDrawState     var isFocused: Boolean     init()     init(version version: UInt32, kind kind: HIThemeFrameKind, state state: ThemeDrawState, isFocused isFocused: Boolean) } ``` |

Modified HIThemeGrabberDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeGrabberDrawInfo {     var version: UInt32     var state: ThemeDrawState } ``` |
| To | ``` struct HIThemeGrabberDrawInfo {     var version: UInt32     var state: ThemeDrawState     init()     init(version version: UInt32, state state: ThemeDrawState) } ``` |

Modified HIThemeGroupBoxDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeGroupBoxDrawInfo {     var version: UInt32     var state: ThemeDrawState     var kind: HIThemeGroupBoxKind } ``` |
| To | ``` struct HIThemeGroupBoxDrawInfo {     var version: UInt32     var state: ThemeDrawState     var kind: HIThemeGroupBoxKind     init()     init(version version: UInt32, state state: ThemeDrawState, kind kind: HIThemeGroupBoxKind) } ``` |

Modified HIThemeGrowBoxDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeGrowBoxDrawInfo {     var version: UInt32     var state: ThemeDrawState     var kind: HIThemeGrowBoxKind     var direction: ThemeGrowDirection     var size: HIThemeGrowBoxSize } ``` |
| To | ``` struct HIThemeGrowBoxDrawInfo {     var version: UInt32     var state: ThemeDrawState     var kind: HIThemeGrowBoxKind     var direction: ThemeGrowDirection     var size: HIThemeGrowBoxSize     init()     init(version version: UInt32, state state: ThemeDrawState, kind kind: HIThemeGrowBoxKind, direction direction: ThemeGrowDirection, size size: HIThemeGrowBoxSize) } ``` |

Modified HIThemeHeaderDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeHeaderDrawInfo {     var version: UInt32     var state: ThemeDrawState     var kind: HIThemeHeaderKind } ``` |
| To | ``` struct HIThemeHeaderDrawInfo {     var version: UInt32     var state: ThemeDrawState     var kind: HIThemeHeaderKind     init()     init(version version: UInt32, state state: ThemeDrawState, kind kind: HIThemeHeaderKind) } ``` |

Modified HIThemeMenuBarDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeMenuBarDrawInfo {     var version: UInt32     var state: ThemeMenuBarState     var attributes: OptionBits } ``` |
| To | ``` struct HIThemeMenuBarDrawInfo {     var version: UInt32     var state: ThemeMenuBarState     var attributes: OptionBits     init()     init(version version: UInt32, state state: ThemeMenuBarState, attributes attributes: OptionBits) } ``` |

Modified HIThemeMenuDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeMenuDrawInfo {     var version: UInt32     var menuType: ThemeMenuType     var reserved1: UInt     var reserved2: CGFloat     var menuDirection: UInt32     var reserved3: CGFloat     var reserved4: CGFloat } ``` |
| To | ``` struct HIThemeMenuDrawInfo {     var version: UInt32     var menuType: ThemeMenuType     var reserved1: UInt     var reserved2: CGFloat     var menuDirection: UInt32     var reserved3: CGFloat     var reserved4: CGFloat     init()     init(version version: UInt32, menuType menuType: ThemeMenuType, reserved1 reserved1: UInt, reserved2 reserved2: CGFloat, menuDirection menuDirection: UInt32, reserved3 reserved3: CGFloat, reserved4 reserved4: CGFloat) } ``` |

Modified HIThemeMenuDrawInfoVersionZero [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeMenuDrawInfoVersionZero {     var version: UInt32     var menuType: ThemeMenuType } ``` |
| To | ``` struct HIThemeMenuDrawInfoVersionZero {     var version: UInt32     var menuType: ThemeMenuType     init()     init(version version: UInt32, menuType menuType: ThemeMenuType) } ``` |

Modified HIThemeMenuItemDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeMenuItemDrawInfo {     var version: UInt32     var itemType: ThemeMenuItemType     var state: ThemeMenuState } ``` |
| To | ``` struct HIThemeMenuItemDrawInfo {     var version: UInt32     var itemType: ThemeMenuItemType     var state: ThemeMenuState     init()     init(version version: UInt32, itemType itemType: ThemeMenuItemType, state state: ThemeMenuState) } ``` |

Modified HIThemeMenuTitleDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeMenuTitleDrawInfo {     var version: UInt32     var state: ThemeMenuState     var attributes: OptionBits     var condensedTitleExtra: CGFloat } ``` |
| To | ``` struct HIThemeMenuTitleDrawInfo {     var version: UInt32     var state: ThemeMenuState     var attributes: OptionBits     var condensedTitleExtra: CGFloat     init()     init(version version: UInt32, state state: ThemeMenuState, attributes attributes: OptionBits, condensedTitleExtra condensedTitleExtra: CGFloat) } ``` |

Modified HIThemePlacardDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemePlacardDrawInfo {     var version: UInt32     var state: ThemeDrawState } ``` |
| To | ``` struct HIThemePlacardDrawInfo {     var version: UInt32     var state: ThemeDrawState     init()     init(version version: UInt32, state state: ThemeDrawState) } ``` |

Modified HIThemePopupArrowDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemePopupArrowDrawInfo {     var version: UInt32     var state: ThemeDrawState     var orientation: ThemeArrowOrientation     var size: ThemePopupArrowSize } ``` |
| To | ``` struct HIThemePopupArrowDrawInfo {     var version: UInt32     var state: ThemeDrawState     var orientation: ThemeArrowOrientation     var size: ThemePopupArrowSize     init()     init(version version: UInt32, state state: ThemeDrawState, orientation orientation: ThemeArrowOrientation, size size: ThemePopupArrowSize) } ``` |

Modified HIThemeScrollBarDelimitersDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeScrollBarDelimitersDrawInfo {     var version: UInt32     var state: ThemeDrawState     var windowType: ThemeWindowType     var attributes: ThemeWindowAttributes } ``` |
| To | ``` struct HIThemeScrollBarDelimitersDrawInfo {     var version: UInt32     var state: ThemeDrawState     var windowType: ThemeWindowType     var attributes: ThemeWindowAttributes     init()     init(version version: UInt32, state state: ThemeDrawState, windowType windowType: ThemeWindowType, attributes attributes: ThemeWindowAttributes) } ``` |

Modified HIThemeSegmentDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeSegmentDrawInfo {     var version: UInt32     var state: ThemeDrawState     var value: ThemeButtonValue     var size: HIThemeSegmentSize     var kind: HIThemeSegmentKind     var position: HIThemeSegmentPosition     var adornment: HIThemeSegmentAdornment } ``` |
| To | ``` struct HIThemeSegmentDrawInfo {     var version: UInt32     var state: ThemeDrawState     var value: ThemeButtonValue     var size: HIThemeSegmentSize     var kind: HIThemeSegmentKind     var position: HIThemeSegmentPosition     var adornment: HIThemeSegmentAdornment     init()     init(version version: UInt32, state state: ThemeDrawState, value value: ThemeButtonValue, size size: HIThemeSegmentSize, kind kind: HIThemeSegmentKind, position position: HIThemeSegmentPosition, adornment adornment: HIThemeSegmentAdornment) } ``` |

Modified HIThemeSeparatorDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeSeparatorDrawInfo {     var version: UInt32     var state: ThemeDrawState } ``` |
| To | ``` struct HIThemeSeparatorDrawInfo {     var version: UInt32     var state: ThemeDrawState     init()     init(version version: UInt32, state state: ThemeDrawState) } ``` |

Modified HIThemeSplitterDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeSplitterDrawInfo {     var version: UInt32     var state: ThemeDrawState     var adornment: HIThemeSplitterAdornment } ``` |
| To | ``` struct HIThemeSplitterDrawInfo {     var version: UInt32     var state: ThemeDrawState     var adornment: HIThemeSplitterAdornment     init()     init(version version: UInt32, state state: ThemeDrawState, adornment adornment: HIThemeSplitterAdornment) } ``` |

Modified HIThemeTabDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeTabDrawInfo {     var version: UInt32     var style: ThemeTabStyle     var direction: ThemeTabDirection     var size: HIThemeTabSize     var adornment: HIThemeTabAdornment     var kind: HIThemeTabKind     var position: HIThemeTabPosition } ``` |
| To | ``` struct HIThemeTabDrawInfo {     var version: UInt32     var style: ThemeTabStyle     var direction: ThemeTabDirection     var size: HIThemeTabSize     var adornment: HIThemeTabAdornment     var kind: HIThemeTabKind     var position: HIThemeTabPosition     init()     init(version version: UInt32, style style: ThemeTabStyle, direction direction: ThemeTabDirection, size size: HIThemeTabSize, adornment adornment: HIThemeTabAdornment, kind kind: HIThemeTabKind, position position: HIThemeTabPosition) } ``` |

Modified HIThemeTabDrawInfoVersionZero [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeTabDrawInfoVersionZero {     var version: UInt32     var style: ThemeTabStyle     var direction: ThemeTabDirection     var size: HIThemeTabSize     var adornment: HIThemeTabAdornment } ``` |
| To | ``` struct HIThemeTabDrawInfoVersionZero {     var version: UInt32     var style: ThemeTabStyle     var direction: ThemeTabDirection     var size: HIThemeTabSize     var adornment: HIThemeTabAdornment     init()     init(version version: UInt32, style style: ThemeTabStyle, direction direction: ThemeTabDirection, size size: HIThemeTabSize, adornment adornment: HIThemeTabAdornment) } ``` |

Modified HIThemeTabPaneDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeTabPaneDrawInfo {     var version: UInt32     var state: ThemeDrawState     var direction: ThemeTabDirection     var size: HIThemeTabSize     var kind: HIThemeTabKind     var adornment: HIThemeTabPaneAdornment } ``` |
| To | ``` struct HIThemeTabPaneDrawInfo {     var version: UInt32     var state: ThemeDrawState     var direction: ThemeTabDirection     var size: HIThemeTabSize     var kind: HIThemeTabKind     var adornment: HIThemeTabPaneAdornment     init()     init(version version: UInt32, state state: ThemeDrawState, direction direction: ThemeTabDirection, size size: HIThemeTabSize, kind kind: HIThemeTabKind, adornment adornment: HIThemeTabPaneAdornment) } ``` |

Modified HIThemeTabPaneDrawInfoVersionZero [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeTabPaneDrawInfoVersionZero {     var version: UInt32     var state: ThemeDrawState     var direction: ThemeTabDirection     var size: HIThemeTabSize } ``` |
| To | ``` struct HIThemeTabPaneDrawInfoVersionZero {     var version: UInt32     var state: ThemeDrawState     var direction: ThemeTabDirection     var size: HIThemeTabSize     init()     init(version version: UInt32, state state: ThemeDrawState, direction direction: ThemeTabDirection, size size: HIThemeTabSize) } ``` |

Modified HIThemeTextInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeTextInfo {     var version: UInt32     var state: ThemeDrawState     var fontID: ThemeFontID     var horizontalFlushness: HIThemeTextHorizontalFlush     var verticalFlushness: HIThemeTextVerticalFlush     var options: HIThemeTextBoxOptions     var truncationPosition: HIThemeTextTruncation     var truncationMaxLines: UInt32     var truncationHappened: Boolean     var filler1: UInt8     var font: Unmanaged<CTFont>! } ``` |
| To | ``` struct HIThemeTextInfo {     var version: UInt32     var state: ThemeDrawState     var fontID: ThemeFontID     var horizontalFlushness: HIThemeTextHorizontalFlush     var verticalFlushness: HIThemeTextVerticalFlush     var options: HIThemeTextBoxOptions     var truncationPosition: HIThemeTextTruncation     var truncationMaxLines: UInt32     var truncationHappened: Boolean     var filler1: UInt8     var font: Unmanaged<CTFont>!     init()     init(version version: UInt32, state state: ThemeDrawState, fontID fontID: ThemeFontID, horizontalFlushness horizontalFlushness: HIThemeTextHorizontalFlush, verticalFlushness verticalFlushness: HIThemeTextVerticalFlush, options options: HIThemeTextBoxOptions, truncationPosition truncationPosition: HIThemeTextTruncation, truncationMaxLines truncationMaxLines: UInt32, truncationHappened truncationHappened: Boolean, filler1 filler1: UInt8, font font: Unmanaged<CTFont>!) } ``` |

Modified HIThemeTickMarkDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeTickMarkDrawInfo {     var version: UInt32     var state: ThemeDrawState } ``` |
| To | ``` struct HIThemeTickMarkDrawInfo {     var version: UInt32     var state: ThemeDrawState     init()     init(version version: UInt32, state state: ThemeDrawState) } ``` |

Modified HIThemeTrackDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeTrackDrawInfo {     var version: UInt32     var kind: ThemeTrackKind     var bounds: HIRect     var min: Int32     var max: Int32     var value: Int32     var reserved: UInt32     var attributes: ThemeTrackAttributes     var enableState: ThemeTrackEnableState     var filler1: UInt8 } ``` |
| To | ``` struct HIThemeTrackDrawInfo {     var version: UInt32     var kind: ThemeTrackKind     var bounds: HIRect     var min: Int32     var max: Int32     var value: Int32     var reserved: UInt32     var attributes: ThemeTrackAttributes     var enableState: ThemeTrackEnableState     var filler1: UInt8     init() } ``` |

Modified HIThemeWindowDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeWindowDrawInfo {     var version: UInt32     var state: ThemeDrawState     var windowType: ThemeWindowType     var attributes: ThemeWindowAttributes     var titleHeight: CGFloat     var titleWidth: CGFloat } ``` |
| To | ``` struct HIThemeWindowDrawInfo {     var version: UInt32     var state: ThemeDrawState     var windowType: ThemeWindowType     var attributes: ThemeWindowAttributes     var titleHeight: CGFloat     var titleWidth: CGFloat     init()     init(version version: UInt32, state state: ThemeDrawState, windowType windowType: ThemeWindowType, attributes attributes: ThemeWindowAttributes, titleHeight titleHeight: CGFloat, titleWidth titleWidth: CGFloat) } ``` |

Modified HIThemeWindowWidgetDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeWindowWidgetDrawInfo {     var version: UInt32     var widgetState: ThemeDrawState     var widgetType: ThemeTitleBarWidget     var windowState: ThemeDrawState     var windowType: ThemeWindowType     var attributes: ThemeWindowAttributes     var titleHeight: CGFloat     var titleWidth: CGFloat } ``` |
| To | ``` struct HIThemeWindowWidgetDrawInfo {     var version: UInt32     var widgetState: ThemeDrawState     var widgetType: ThemeTitleBarWidget     var windowState: ThemeDrawState     var windowType: ThemeWindowType     var attributes: ThemeWindowAttributes     var titleHeight: CGFloat     var titleWidth: CGFloat     init()     init(version version: UInt32, widgetState widgetState: ThemeDrawState, widgetType widgetType: ThemeTitleBarWidget, windowState windowState: ThemeDrawState, windowType windowType: ThemeWindowType, attributes attributes: ThemeWindowAttributes, titleHeight titleHeight: CGFloat, titleWidth titleWidth: CGFloat) } ``` |

Modified HITypeAndCreator [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HITypeAndCreator {     var type: OSType     var creator: OSType } ``` |
| To | ``` struct HITypeAndCreator {     var type: OSType     var creator: OSType     init()     init(type type: OSType, creator creator: OSType) } ``` |

Modified HIViewContentInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIViewContentInfo {     var contentType: HIViewContentType } ``` |
| To | ``` struct HIViewContentInfo {     var contentType: HIViewContentType     init() } ``` |

Modified HIViewFrameMetrics [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIViewFrameMetrics {     var top: CGFloat     var left: CGFloat     var bottom: CGFloat     var right: CGFloat } ``` |
| To | ``` struct HIViewFrameMetrics {     var top: CGFloat     var left: CGFloat     var bottom: CGFloat     var right: CGFloat     init()     init(top top: CGFloat, left left: CGFloat, bottom bottom: CGFloat, right right: CGFloat) } ``` |

Modified HIViewKind [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIViewKind {     var signature: OSType     var kind: OSType } ``` |
| To | ``` struct HIViewKind {     var signature: OSType     var kind: OSType     init()     init(signature signature: OSType, kind kind: OSType) } ``` |

Modified HMHelpContent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HMHelpContent {     var contentType: HMContentType } ``` |
| To | ``` struct HMHelpContent {     var contentType: HMContentType     init() } ``` |

Modified HMHelpContentRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HMHelpContentRec {     var version: Int32     var absHotRect: Rect     var tagSide: HMTagDisplaySide     var content: (HMHelpContent, HMHelpContent) } ``` |
| To | ``` struct HMHelpContentRec {     var version: Int32     var absHotRect: Rect     var tagSide: HMTagDisplaySide     var content: (HMHelpContent, HMHelpContent)     init()     init(version version: Int32, absHotRect absHotRect: Rect, tagSide tagSide: HMTagDisplaySide, content content: (HMHelpContent, HMHelpContent)) } ``` |

Modified HMStringResType [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HMStringResType {     var hmmResID: Int16     var hmmIndex: Int16 } ``` |
| To | ``` struct HMStringResType {     var hmmResID: Int16     var hmmIndex: Int16     init()     init(hmmResID hmmResID: Int16, hmmIndex hmmIndex: Int16) } ``` |

Modified HMenuBarHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HMenuBarHeader {     var lastHMenu: UInt16     var menuTitleBits: PixMapHandle } ``` |
| To | ``` struct HMenuBarHeader {     var lastHMenu: UInt16     var menuTitleBits: PixMapHandle     init()     init(lastHMenu lastHMenu: UInt16, menuTitleBits menuTitleBits: PixMapHandle) } ``` |

Modified HMenuBarMenu [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HMenuBarMenu {     var menu: Unmanaged<Menu>!     var reserved: Int16 } ``` |
| To | ``` struct HMenuBarMenu {     var menu: Unmanaged<Menu>!     var reserved: Int16     init()     init(menu menu: Unmanaged<Menu>!, reserved reserved: Int16) } ``` |

Modified ICACloseSessionPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICACloseSessionPB {     var header: ICAHeader     var sessionID: ICASessionID } ``` |
| To | ``` struct ICACloseSessionPB {     var header: ICAHeader     var sessionID: ICASessionID     init()     init(header header: ICAHeader, sessionID sessionID: ICASessionID) } ``` |

Modified ICACopyObjectDataPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICACopyObjectDataPB {     var header: ICAHeader     var object: ICAObject     var startByte: UInt     var requestedSize: UInt     var data: UnsafePointer<Unmanaged<CFData>?> } ``` |
| To | ``` struct ICACopyObjectDataPB {     var header: ICAHeader     var object: ICAObject     var startByte: Int     var requestedSize: Int     var data: UnsafeMutablePointer<Unmanaged<CFData>?>     init()     init(header header: ICAHeader, object object: ICAObject, startByte startByte: Int, requestedSize requestedSize: Int, data data: UnsafeMutablePointer<Unmanaged<CFData>?>) } ``` |

Modified ICACopyObjectDataPB.data

|  | Declaration |
| --- | --- |
| From | ``` var data: UnsafePointer<Unmanaged<CFData>?> ``` |
| To | ``` var data: UnsafeMutablePointer<Unmanaged<CFData>?> ``` |

Modified ICACopyObjectDataPB.requestedSize

|  | Declaration |
| --- | --- |
| From | ``` var requestedSize: UInt ``` |
| To | ``` var requestedSize: Int ``` |

Modified ICACopyObjectDataPB.startByte

|  | Declaration |
| --- | --- |
| From | ``` var startByte: UInt ``` |
| To | ``` var startByte: Int ``` |

Modified ICACopyObjectPropertyDictionaryPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICACopyObjectPropertyDictionaryPB {     var header: ICAHeader     var object: ICAObject     var theDict: UnsafePointer<Unmanaged<CFDictionary>?> } ``` |
| To | ``` struct ICACopyObjectPropertyDictionaryPB {     var header: ICAHeader     var object: ICAObject     var theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>     init()     init(header header: ICAHeader, object object: ICAObject, theDict theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) } ``` |

Modified ICACopyObjectPropertyDictionaryPB.theDict

|  | Declaration |
| --- | --- |
| From | ``` var theDict: UnsafePointer<Unmanaged<CFDictionary>?> ``` |
| To | ``` var theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?> ``` |

Modified ICACopyObjectThumbnailPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICACopyObjectThumbnailPB {     var header: ICAHeader     var object: ICAObject     var thumbnailFormat: OSType     var thumbnailData: UnsafePointer<Unmanaged<CFData>?> } ``` |
| To | ``` struct ICACopyObjectThumbnailPB {     var header: ICAHeader     var object: ICAObject     var thumbnailFormat: OSType     var thumbnailData: UnsafeMutablePointer<Unmanaged<CFData>?>     init()     init(header header: ICAHeader, object object: ICAObject, thumbnailFormat thumbnailFormat: OSType, thumbnailData thumbnailData: UnsafeMutablePointer<Unmanaged<CFData>?>) } ``` |

Modified ICACopyObjectThumbnailPB.thumbnailData

|  | Declaration |
| --- | --- |
| From | ``` var thumbnailData: UnsafePointer<Unmanaged<CFData>?> ``` |
| To | ``` var thumbnailData: UnsafeMutablePointer<Unmanaged<CFData>?> ``` |

Modified ICADownloadFilePB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICADownloadFilePB {     var header: ICAHeader     var object: ICAObject     var dirFSRef: UnsafePointer<FSRef>     var flags: UInt32     var fileType: OSType     var fileCreator: OSType     var rotationAngle: Fixed     var fileFSRef: UnsafePointer<FSRef> } ``` |
| To | ``` struct ICADownloadFilePB {     var header: ICAHeader     var object: ICAObject     var dirFSRef: UnsafeMutablePointer<FSRef>     var flags: UInt32     var fileType: OSType     var fileCreator: OSType     var rotationAngle: Fixed     var fileFSRef: UnsafeMutablePointer<FSRef>     init()     init(header header: ICAHeader, object object: ICAObject, dirFSRef dirFSRef: UnsafeMutablePointer<FSRef>, flags flags: UInt32, fileType fileType: OSType, fileCreator fileCreator: OSType, rotationAngle rotationAngle: Fixed, fileFSRef fileFSRef: UnsafeMutablePointer<FSRef>) } ``` |

Modified ICADownloadFilePB.dirFSRef

|  | Declaration |
| --- | --- |
| From | ``` var dirFSRef: UnsafePointer<FSRef> ``` |
| To | ``` var dirFSRef: UnsafeMutablePointer<FSRef> ``` |

Modified ICADownloadFilePB.fileFSRef

|  | Declaration |
| --- | --- |
| From | ``` var fileFSRef: UnsafePointer<FSRef> ``` |
| To | ``` var fileFSRef: UnsafeMutablePointer<FSRef> ``` |

Modified ICAGetDeviceListPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAGetDeviceListPB {     var header: ICAHeader     var object: ICAObject } ``` |
| To | ``` struct ICAGetDeviceListPB {     var header: ICAHeader     var object: ICAObject     init()     init(header header: ICAHeader, object object: ICAObject) } ``` |

Modified ICAHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAHeader {     var err: ICAError     var refcon: UInt } ``` |
| To | ``` struct ICAHeader {     var err: ICAError     var refcon: UInt     init()     init(err err: ICAError, refcon refcon: UInt) } ``` |

Modified ICAImportImagePB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAImportImagePB {     var header: ICAHeader     var deviceObject: ICAObject     var flags: UInt32     var supportedFileTypes: Unmanaged<CFArray>!     var filterProc: ICAImportFilterProc     var importedImages: UnsafePointer<Unmanaged<CFArray>?> } ``` |
| To | ``` struct ICAImportImagePB {     var header: ICAHeader     var deviceObject: ICAObject     var flags: UInt32     var supportedFileTypes: Unmanaged<CFArray>!     var filterProc: ICAImportFilterProc     var importedImages: UnsafeMutablePointer<Unmanaged<CFArray>?>     init()     init(header header: ICAHeader, deviceObject deviceObject: ICAObject, flags flags: UInt32, supportedFileTypes supportedFileTypes: Unmanaged<CFArray>!, filterProc filterProc: ICAImportFilterProc, importedImages importedImages: UnsafeMutablePointer<Unmanaged<CFArray>?>) } ``` |

Modified ICAImportImagePB.importedImages

|  | Declaration |
| --- | --- |
| From | ``` var importedImages: UnsafePointer<Unmanaged<CFArray>?> ``` |
| To | ``` var importedImages: UnsafeMutablePointer<Unmanaged<CFArray>?> ``` |

Modified ICALoadDeviceModulePB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICALoadDeviceModulePB {     var header: ICAHeader     var paramDictionary: Unmanaged<CFDictionary>! } ``` |
| To | ``` struct ICALoadDeviceModulePB {     var header: ICAHeader     var paramDictionary: Unmanaged<CFDictionary>!     init()     init(header header: ICAHeader, paramDictionary paramDictionary: Unmanaged<CFDictionary>!) } ``` |

Modified ICAMessage [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAMessage {     var messageType: OSType     var startByte: UInt32     var dataPtr: UnsafePointer<()>     var dataSize: UInt32     var dataType: OSType } ``` |
| To | ``` struct ICAMessage {     var messageType: OSType     var startByte: UInt32     var dataPtr: UnsafeMutablePointer<Void>     var dataSize: UInt32     var dataType: OSType     init()     init(messageType messageType: OSType, startByte startByte: UInt32, dataPtr dataPtr: UnsafeMutablePointer<Void>, dataSize dataSize: UInt32, dataType dataType: OSType) } ``` |

Modified ICAMessage.dataPtr

|  | Declaration |
| --- | --- |
| From | ``` var dataPtr: UnsafePointer<()> ``` |
| To | ``` var dataPtr: UnsafeMutablePointer<Void> ``` |

Modified ICAObjectInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAObjectInfo {     var objectType: OSType     var objectSubtype: OSType } ``` |
| To | ``` struct ICAObjectInfo {     var objectType: OSType     var objectSubtype: OSType     init()     init(objectType objectType: OSType, objectSubtype objectSubtype: OSType) } ``` |

Modified ICAObjectSendMessagePB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAObjectSendMessagePB {     var header: ICAHeader     var object: ICAObject     var message: ICAMessage     var result: UInt32 } ``` |
| To | ``` struct ICAObjectSendMessagePB {     var header: ICAHeader     var object: ICAObject     var message: ICAMessage     var result: UInt32     init()     init(header header: ICAHeader, object object: ICAObject, message message: ICAMessage, result result: UInt32) } ``` |

Modified ICAOpenSessionPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAOpenSessionPB {     var header: ICAHeader     var deviceObject: ICAObject     var sessionID: ICASessionID } ``` |
| To | ``` struct ICAOpenSessionPB {     var header: ICAHeader     var deviceObject: ICAObject     var sessionID: ICASessionID     init()     init(header header: ICAHeader, deviceObject deviceObject: ICAObject, sessionID sessionID: ICASessionID) } ``` |

Modified ICAPTPEventDataset [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAPTPEventDataset {     var dataLength: UInt32     var containerType: UInt16     var eventCode: UInt16     var transactionID: UInt32     var params: (UInt32, UInt32, UInt32) } ``` |
| To | ``` struct ICAPTPEventDataset {     var dataLength: UInt32     var containerType: UInt16     var eventCode: UInt16     var transactionID: UInt32     var params: (UInt32, UInt32, UInt32)     init()     init(dataLength dataLength: UInt32, containerType containerType: UInt16, eventCode eventCode: UInt16, transactionID transactionID: UInt32, params params: (UInt32, UInt32, UInt32)) } ``` |

Modified ICAPTPPassThroughPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAPTPPassThroughPB {     var commandCode: UInt32     var resultCode: UInt32     var numOfInputParams: UInt32     var numOfOutputParams: UInt32     var params: (UInt32, UInt32, UInt32, UInt32)     var dataUsageMode: UInt32     var flags: UInt32     var dataSize: UInt32     var data: (UInt8) } ``` |
| To | ``` struct ICAPTPPassThroughPB {     var commandCode: UInt32     var resultCode: UInt32     var numOfInputParams: UInt32     var numOfOutputParams: UInt32     var params: (UInt32, UInt32, UInt32, UInt32)     var dataUsageMode: UInt32     var flags: UInt32     var dataSize: UInt32     var data: (UInt8)     init()     init(commandCode commandCode: UInt32, resultCode resultCode: UInt32, numOfInputParams numOfInputParams: UInt32, numOfOutputParams numOfOutputParams: UInt32, params params: (UInt32, UInt32, UInt32, UInt32), dataUsageMode dataUsageMode: UInt32, flags flags: UInt32, dataSize dataSize: UInt32, data data: (UInt8)) } ``` |

Modified ICARegisterForEventNotificationPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICARegisterForEventNotificationPB {     var header: ICAHeader     var objectOfInterest: ICAObject     var eventsOfInterest: Unmanaged<CFArray>!     var notificationProc: ICANotification     var options: Unmanaged<CFDictionary>! } ``` |
| To | ``` struct ICARegisterForEventNotificationPB {     var header: ICAHeader     var objectOfInterest: ICAObject     var eventsOfInterest: Unmanaged<CFArray>!     var notificationProc: ICANotification     var options: Unmanaged<CFDictionary>!     init()     init(header header: ICAHeader, objectOfInterest objectOfInterest: ICAObject, eventsOfInterest eventsOfInterest: Unmanaged<CFArray>!, notificationProc notificationProc: ICANotification, options options: Unmanaged<CFDictionary>!) } ``` |

Modified ICAScannerCloseSessionPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAScannerCloseSessionPB {     var header: ICAHeader     var sessionID: ICAScannerSessionID } ``` |
| To | ``` struct ICAScannerCloseSessionPB {     var header: ICAHeader     var sessionID: ICAScannerSessionID     init()     init(header header: ICAHeader, sessionID sessionID: ICAScannerSessionID) } ``` |

Modified ICAScannerGetParametersPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAScannerGetParametersPB {     var header: ICAHeader     var sessionID: ICAScannerSessionID     var theDict: Unmanaged<CFMutableDictionary>! } ``` |
| To | ``` struct ICAScannerGetParametersPB {     var header: ICAHeader     var sessionID: ICAScannerSessionID     var theDict: Unmanaged<CFMutableDictionary>!     init()     init(header header: ICAHeader, sessionID sessionID: ICAScannerSessionID, theDict theDict: Unmanaged<CFMutableDictionary>!) } ``` |

Modified ICAScannerInitializePB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAScannerInitializePB {     var header: ICAHeader     var sessionID: ICAScannerSessionID } ``` |
| To | ``` struct ICAScannerInitializePB {     var header: ICAHeader     var sessionID: ICAScannerSessionID     init()     init(header header: ICAHeader, sessionID sessionID: ICAScannerSessionID) } ``` |

Modified ICAScannerOpenSessionPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAScannerOpenSessionPB {     var header: ICAHeader     var object: ICAObject     var sessionID: ICAScannerSessionID } ``` |
| To | ``` struct ICAScannerOpenSessionPB {     var header: ICAHeader     var object: ICAObject     var sessionID: ICAScannerSessionID     init()     init(header header: ICAHeader, object object: ICAObject, sessionID sessionID: ICAScannerSessionID) } ``` |

Modified ICAScannerSetParametersPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAScannerSetParametersPB {     var header: ICAHeader     var sessionID: ICAScannerSessionID     var theDict: Unmanaged<CFMutableDictionary>! } ``` |
| To | ``` struct ICAScannerSetParametersPB {     var header: ICAHeader     var sessionID: ICAScannerSessionID     var theDict: Unmanaged<CFMutableDictionary>!     init()     init(header header: ICAHeader, sessionID sessionID: ICAScannerSessionID, theDict theDict: Unmanaged<CFMutableDictionary>!) } ``` |

Modified ICAScannerStartPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAScannerStartPB {     var header: ICAHeader     var sessionID: ICAScannerSessionID } ``` |
| To | ``` struct ICAScannerStartPB {     var header: ICAHeader     var sessionID: ICAScannerSessionID     init()     init(header header: ICAHeader, sessionID sessionID: ICAScannerSessionID) } ``` |

Modified ICAScannerStatusPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAScannerStatusPB {     var header: ICAHeader     var sessionID: ICAScannerSessionID     var status: UInt32 } ``` |
| To | ``` struct ICAScannerStatusPB {     var header: ICAHeader     var sessionID: ICAScannerSessionID     var status: UInt32     init()     init(header header: ICAHeader, sessionID sessionID: ICAScannerSessionID, status status: UInt32) } ``` |

Modified ICASendNotificationPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICASendNotificationPB {     var header: ICAHeader     var notificationDictionary: Unmanaged<CFMutableDictionary>!     var replyCode: UInt32 } ``` |
| To | ``` struct ICASendNotificationPB {     var header: ICAHeader     var notificationDictionary: Unmanaged<CFMutableDictionary>!     var replyCode: UInt32     init()     init(header header: ICAHeader, notificationDictionary notificationDictionary: Unmanaged<CFMutableDictionary>!, replyCode replyCode: UInt32) } ``` |

Modified ICAUnloadDeviceModulePB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAUnloadDeviceModulePB {     var header: ICAHeader     var deviceObject: ICAObject } ``` |
| To | ``` struct ICAUnloadDeviceModulePB {     var header: ICAHeader     var deviceObject: ICAObject     init()     init(header header: ICAHeader, deviceObject deviceObject: ICAObject) } ``` |

Modified ICAUploadFilePB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAUploadFilePB {     var header: ICAHeader     var parentObject: ICAObject     var fileFSRef: UnsafePointer<FSRef>     var flags: UInt32 } ``` |
| To | ``` struct ICAUploadFilePB {     var header: ICAHeader     var parentObject: ICAObject     var fileFSRef: UnsafeMutablePointer<FSRef>     var flags: UInt32     init()     init(header header: ICAHeader, parentObject parentObject: ICAObject, fileFSRef fileFSRef: UnsafeMutablePointer<FSRef>, flags flags: UInt32) } ``` |

Modified ICAUploadFilePB.fileFSRef

|  | Declaration |
| --- | --- |
| From | ``` var fileFSRef: UnsafePointer<FSRef> ``` |
| To | ``` var fileFSRef: UnsafeMutablePointer<FSRef> ``` |

Modified ICDHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICDHeader {     var err: ICAError     var refcon: UInt } ``` |
| To | ``` struct ICDHeader {     var err: ICAError     var refcon: UInt     init()     init(err err: ICAError, refcon refcon: UInt) } ``` |

Modified ICD_DisposeObjectPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICD_DisposeObjectPB {     var header: ICDHeader     var object: ICAObject } ``` |
| To | ``` struct ICD_DisposeObjectPB {     var header: ICDHeader     var object: ICAObject     init()     init(header header: ICDHeader, object object: ICAObject) } ``` |

Modified ICD_NewObjectPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICD_NewObjectPB {     var header: ICDHeader     var parentObject: ICAObject     var objectInfo: ICAObjectInfo     var object: ICAObject } ``` |
| To | ``` struct ICD_NewObjectPB {     var header: ICDHeader     var parentObject: ICAObject     var objectInfo: ICAObjectInfo     var object: ICAObject     init()     init(header header: ICDHeader, parentObject parentObject: ICAObject, objectInfo objectInfo: ICAObjectInfo, object object: ICAObject) } ``` |

Modified IMKTextInput.attributesForCharacterIndex(Int, lineHeightRectangle: UnsafeMutablePointer<NSRect>) -> [NSObject: AnyObject]!

|  | Declaration |
| --- | --- |
| From | ``` func attributesForCharacterIndex(_ index: Int, lineHeightRectangle lineRect: UnsafePointer<NSRect>) -> [NSObject : AnyObject]! ``` |
| To | ``` func attributesForCharacterIndex(_ index: Int, lineHeightRectangle lineRect: UnsafeMutablePointer<NSRect>) -> [NSObject : AnyObject]! ``` |

Modified IMKTextInput.characterIndexForPoint(NSPoint, tracking: IMKLocationToOffsetMappingMode, inMarkedRange: UnsafeMutablePointer<ObjCBool>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func characterIndexForPoint(_ point: NSPoint, tracking mappingMode: IMKLocationToOffsetMappingMode, inMarkedRange inMarkedRange: UnsafePointer<ObjCBool>) -> Int ``` |
| To | ``` func characterIndexForPoint(_ point: NSPoint, tracking mappingMode: IMKLocationToOffsetMappingMode, inMarkedRange inMarkedRange: UnsafeMutablePointer<ObjCBool>) -> Int ``` |

Modified IMKTextInput.firstRectForCharacterRange(NSRange, actualRange: NSRangePointer) -> NSRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IMKTextInput.stringFromRange(NSRange, actualRange: NSRangePointer) -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IMKTextInput.uniqueClientIdentifierString() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified IndicatorDragConstraint [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct IndicatorDragConstraint {     var limitRect: Rect     var slopRect: Rect     var axis: DragConstraint } ``` |
| To | ``` struct IndicatorDragConstraint {     var limitRect: Rect     var slopRect: Rect     var axis: DragConstraint     init()     init(limitRect limitRect: Rect, slopRect slopRect: Rect, axis axis: DragConstraint) } ``` |

Modified InkPoint [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct InkPoint {     var point: HIPoint     var tabletPointData: TabletPointRec     var keyModifiers: UInt32 } ``` |
| To | ``` struct InkPoint {     var point: HIPoint     var tabletPointData: TabletPointRec     var keyModifiers: UInt32     init()     init(point point: HIPoint, tabletPointData tabletPointData: TabletPointRec, keyModifiers keyModifiers: UInt32) } ``` |

Modified LHElement [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct LHElement {     var lhHeight: Int16     var lhAscent: Int16 } ``` |
| To | ``` struct LHElement {     var lhHeight: Int16     var lhAscent: Int16     init()     init(lhHeight lhHeight: Int16, lhAscent lhAscent: Int16) } ``` |

Modified ListDefSpec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ListDefSpec {     var defType: ListDefType } ``` |
| To | ``` struct ListDefSpec {     var defType: ListDefType     init() } ``` |

Modified ListRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ListRec {     var rView: Rect     var port: GrafPtr     var indent: Point     var cellSize: Point     var visible: ListBounds     var vScroll: Unmanaged<Control>!     var hScroll: Unmanaged<Control>!     var selFlags: Int8     var lActive: Boolean     var lReserved: Int8     var listFlags: Int8     var clikTime: Int     var clikLoc: Point     var mouseLoc: Point     var lClickLoop: ListClickLoopUPP     var lastClick: Cell     var refCon: Int     var listDefProc: Handle     var userHandle: Handle     var dataBounds: ListBounds     var cells: DataHandle     var maxIndex: Int16     var cellArray: (Int16) } ``` |
| To | ``` struct ListRec {     var rView: Rect     var port: GrafPtr     var indent: Point     var cellSize: Point     var visible: ListBounds     var vScroll: Unmanaged<Control>!     var hScroll: Unmanaged<Control>!     var selFlags: Int8     var lActive: Boolean     var lReserved: Int8     var listFlags: Int8     var clikTime: Int     var clikLoc: Point     var mouseLoc: Point     var lClickLoop: ListClickLoopUPP     var lastClick: Cell     var refCon: Int     var listDefProc: Handle     var userHandle: Handle     var dataBounds: ListBounds     var cells: DataHandle     var maxIndex: Int16     var cellArray: (Int16)     init()     init(rView rView: Rect, port port: GrafPtr, indent indent: Point, cellSize cellSize: Point, visible visible: ListBounds, vScroll vScroll: Unmanaged<Control>!, hScroll hScroll: Unmanaged<Control>!, selFlags selFlags: Int8, lActive lActive: Boolean, lReserved lReserved: Int8, listFlags listFlags: Int8, clikTime clikTime: Int, clikLoc clikLoc: Point, mouseLoc mouseLoc: Point, lClickLoop lClickLoop: ListClickLoopUPP, lastClick lastClick: Cell, refCon refCon: Int, listDefProc listDefProc: Handle, userHandle userHandle: Handle, dataBounds dataBounds: ListBounds, cells cells: DataHandle, maxIndex maxIndex: Int16, cellArray cellArray: (Int16)) } ``` |

Modified MCEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MCEntry {     var mctID: MenuID     var mctItem: Int16     var mctRGB1: RGBColor     var mctRGB2: RGBColor     var mctRGB3: RGBColor     var mctRGB4: RGBColor     var mctReserved: Int16 } ``` |
| To | ``` struct MCEntry {     var mctID: MenuID     var mctItem: Int16     var mctRGB1: RGBColor     var mctRGB2: RGBColor     var mctRGB3: RGBColor     var mctRGB4: RGBColor     var mctReserved: Int16     init()     init(mctID mctID: MenuID, mctItem mctItem: Int16, mctRGB1 mctRGB1: RGBColor, mctRGB2 mctRGB2: RGBColor, mctRGB3 mctRGB3: RGBColor, mctRGB4 mctRGB4: RGBColor, mctReserved mctReserved: Int16) } ``` |

Modified MDEFDrawData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MDEFDrawData {     var trackingData: MenuTrackingData     var context: UnsafePointer<()> } ``` |
| To | ``` struct MDEFDrawData {     var trackingData: MenuTrackingData     var context: UnsafeMutablePointer<Void>     init()     init(trackingData trackingData: MenuTrackingData, context context: UnsafeMutablePointer<Void>) } ``` |

Modified MDEFDrawData.context

|  | Declaration |
| --- | --- |
| From | ``` var context: UnsafePointer<()> ``` |
| To | ``` var context: UnsafeMutablePointer<Void> ``` |

Modified MDEFDrawItemsData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MDEFDrawItemsData {     var firstItem: MenuItemIndex     var lastItem: MenuItemIndex     var trackingData: UnsafePointer<MenuTrackingData>     var context: UnsafePointer<()> } ``` |
| To | ``` struct MDEFDrawItemsData {     var firstItem: MenuItemIndex     var lastItem: MenuItemIndex     var trackingData: UnsafeMutablePointer<MenuTrackingData>     var context: UnsafeMutablePointer<Void>     init()     init(firstItem firstItem: MenuItemIndex, lastItem lastItem: MenuItemIndex, trackingData trackingData: UnsafeMutablePointer<MenuTrackingData>, context context: UnsafeMutablePointer<Void>) } ``` |

Modified MDEFDrawItemsData.context

|  | Declaration |
| --- | --- |
| From | ``` var context: UnsafePointer<()> ``` |
| To | ``` var context: UnsafeMutablePointer<Void> ``` |

Modified MDEFDrawItemsData.trackingData

|  | Declaration |
| --- | --- |
| From | ``` var trackingData: UnsafePointer<MenuTrackingData> ``` |
| To | ``` var trackingData: UnsafeMutablePointer<MenuTrackingData> ``` |

Modified MDEFFindItemData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MDEFFindItemData {     var trackingData: MenuTrackingData     var context: UnsafePointer<()> } ``` |
| To | ``` struct MDEFFindItemData {     var trackingData: MenuTrackingData     var context: UnsafeMutablePointer<Void>     init()     init(trackingData trackingData: MenuTrackingData, context context: UnsafeMutablePointer<Void>) } ``` |

Modified MDEFFindItemData.context

|  | Declaration |
| --- | --- |
| From | ``` var context: UnsafePointer<()> ``` |
| To | ``` var context: UnsafeMutablePointer<Void> ``` |

Modified MDEFHiliteItemData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MDEFHiliteItemData {     var previousItem: MenuItemIndex     var newItem: MenuItemIndex     var context: UnsafePointer<()> } ``` |
| To | ``` struct MDEFHiliteItemData {     var previousItem: MenuItemIndex     var newItem: MenuItemIndex     var context: UnsafeMutablePointer<Void>     init()     init(previousItem previousItem: MenuItemIndex, newItem newItem: MenuItemIndex, context context: UnsafeMutablePointer<Void>) } ``` |

Modified MDEFHiliteItemData.context

|  | Declaration |
| --- | --- |
| From | ``` var context: UnsafePointer<()> ``` |
| To | ``` var context: UnsafeMutablePointer<Void> ``` |

Modified MeasureWindowTitleRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MeasureWindowTitleRec {     var fullTitleWidth: Int16     var titleTextWidth: Int16     var isUnicodeTitle: Boolean     var unused: Boolean } ``` |
| To | ``` struct MeasureWindowTitleRec {     var fullTitleWidth: Int16     var titleTextWidth: Int16     var isUnicodeTitle: Boolean     var unused: Boolean     init()     init(fullTitleWidth fullTitleWidth: Int16, titleTextWidth titleTextWidth: Int16, isUnicodeTitle isUnicodeTitle: Boolean, unused unused: Boolean) } ``` |

Modified MenuBarHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MenuBarHeader {     var lastMenu: UInt16     var lastRight: Int16     var mbResID: Int16 } ``` |
| To | ``` struct MenuBarHeader {     var lastMenu: UInt16     var lastRight: Int16     var mbResID: Int16     init()     init(lastMenu lastMenu: UInt16, lastRight lastRight: Int16, mbResID mbResID: Int16) } ``` |

Modified MenuBarMenu [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MenuBarMenu {     var menu: Unmanaged<Menu>!     var menuLeft: Int16 } ``` |
| To | ``` struct MenuBarMenu {     var menu: Unmanaged<Menu>!     var menuLeft: Int16     init()     init(menu menu: Unmanaged<Menu>!, menuLeft menuLeft: Int16) } ``` |

Modified MenuCRsrc [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MenuCRsrc {     var numEntries: Int16     var mcEntryRecs: MCTable } ``` |
| To | ``` struct MenuCRsrc {     var numEntries: Int16     var mcEntryRecs: MCTable     init()     init(numEntries numEntries: Int16, mcEntryRecs mcEntryRecs: MCTable) } ``` |

Modified MenuDefSpec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MenuDefSpec {     var defType: MenuDefType } ``` |
| To | ``` struct MenuDefSpec {     var defType: MenuDefType     init() } ``` |

Modified MenuItemDataRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MenuItemDataRec {     var whichData: MenuItemDataFlags     var text: StringPtr     var mark: UniChar     var cmdKey: UniChar     var cmdKeyGlyph: UInt32     var cmdKeyModifiers: UInt32     var style: Style     var enabled: Boolean     var iconEnabled: Boolean     var filler1: UInt8     var iconID: Int32     var iconType: UInt32     var iconHandle: Handle     var cmdID: MenuCommand     var encoding: TextEncoding     var submenuID: MenuID     var submenuHandle: Unmanaged<Menu>!     var fontID: Int32     var refcon: URefCon     var attr: OptionBits     var cfText: Unmanaged<CFString>!     var properties: Collection     var indent: UInt32     var cmdVirtualKey: UInt16     var attributedText: Unmanaged<CFAttributedString>!     var font: Unmanaged<CTFont>! } ``` |
| To | ``` struct MenuItemDataRec {     var whichData: MenuItemDataFlags     var text: StringPtr     var mark: UniChar     var cmdKey: UniChar     var cmdKeyGlyph: UInt32     var cmdKeyModifiers: UInt32     var style: Style     var enabled: Boolean     var iconEnabled: Boolean     var filler1: UInt8     var iconID: Int32     var iconType: UInt32     var iconHandle: Handle     var cmdID: MenuCommand     var encoding: TextEncoding     var submenuID: MenuID     var submenuHandle: Unmanaged<Menu>!     var fontID: Int32     var refcon: URefCon     var attr: OptionBits     var cfText: Unmanaged<CFString>!     var properties: Collection     var indent: UInt32     var cmdVirtualKey: UInt16     var attributedText: Unmanaged<CFAttributedString>!     var font: Unmanaged<CTFont>!     init()     init(whichData whichData: MenuItemDataFlags, text text: StringPtr, mark mark: UniChar, cmdKey cmdKey: UniChar, cmdKeyGlyph cmdKeyGlyph: UInt32, cmdKeyModifiers cmdKeyModifiers: UInt32, style style: Style, enabled enabled: Boolean, iconEnabled iconEnabled: Boolean, filler1 filler1: UInt8, iconID iconID: Int32, iconType iconType: UInt32, iconHandle iconHandle: Handle, cmdID cmdID: MenuCommand, encoding encoding: TextEncoding, submenuID submenuID: MenuID, submenuHandle submenuHandle: Unmanaged<Menu>!, fontID fontID: Int32, refcon refcon: URefCon, attr attr: OptionBits, cfText cfText: Unmanaged<CFString>!, properties properties: Collection, indent indent: UInt32, cmdVirtualKey cmdVirtualKey: UInt16, attributedText attributedText: Unmanaged<CFAttributedString>!, font font: Unmanaged<CTFont>!) } ``` |

Modified MenuTrackingData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MenuTrackingData {     var menu: Unmanaged<Menu>!     var itemSelected: MenuItemIndex     var itemUnderMouse: MenuItemIndex     var itemRect: Rect     var virtualMenuTop: Int32     var virtualMenuBottom: Int32 } ``` |
| To | ``` struct MenuTrackingData {     var menu: Unmanaged<Menu>!     var itemSelected: MenuItemIndex     var itemUnderMouse: MenuItemIndex     var itemRect: Rect     var virtualMenuTop: Int32     var virtualMenuBottom: Int32     init()     init(menu menu: Unmanaged<Menu>!, itemSelected itemSelected: MenuItemIndex, itemUnderMouse itemUnderMouse: MenuItemIndex, itemRect itemRect: Rect, virtualMenuTop virtualMenuTop: Int32, virtualMenuBottom virtualMenuBottom: Int32) } ``` |

Modified NColorPickerInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NColorPickerInfo {     var theColor: NPMColor     var dstProfile: Unmanaged<CMProfile>!     var flags: UInt32     var placeWhere: DialogPlacementSpec     var dialogOrigin: Point     var pickerType: OSType     var colorProc: NColorChangedUPP     var colorProcData: URefCon     var prompt: Str255     var mInfo: PickerMenuItemInfo     var newColorChosen: Boolean     var reserved: UInt8 } ``` |
| To | ``` struct NColorPickerInfo {     var theColor: NPMColor     var dstProfile: CMProfileRef     var flags: UInt32     var placeWhere: DialogPlacementSpec     var dialogOrigin: Point     var pickerType: OSType     var colorProc: NColorChangedUPP     var colorProcData: URefCon     var prompt: Str255     var mInfo: PickerMenuItemInfo     var newColorChosen: Boolean     var reserved: UInt8     init()     init(theColor theColor: NPMColor, dstProfile dstProfile: CMProfileRef, flags flags: UInt32, placeWhere placeWhere: DialogPlacementSpec, dialogOrigin dialogOrigin: Point, pickerType pickerType: OSType, colorProc colorProc: NColorChangedUPP, colorProcData colorProcData: URefCon, prompt prompt: Str255, mInfo mInfo: PickerMenuItemInfo, newColorChosen newColorChosen: Boolean, reserved reserved: UInt8) } ``` |

Modified NColorPickerInfo.dstProfile

|  | Declaration |
| --- | --- |
| From | ``` var dstProfile: Unmanaged<CMProfile>! ``` |
| To | ``` var dstProfile: CMProfileRef ``` |

Modified NMRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NMRec {     var qLink: QElemPtr     var qType: Int16     var nmFlags: Int16     var nmPrivate: SRefCon     var nmReserved: Int16     var nmMark: Int16     var nmIcon: Handle     var nmSound: Handle     var nmStr: StringPtr     var nmResp: NMUPP     var nmRefCon: SRefCon } ``` |
| To | ``` struct NMRec {     var qLink: QElemPtr     var qType: Int16     var nmFlags: Int16     var nmPrivate: SRefCon     var nmReserved: Int16     var nmMark: Int16     var nmIcon: Handle     var nmSound: Handle     var nmStr: StringPtr     var nmResp: NMUPP     var nmRefCon: SRefCon     init()     init(qLink qLink: QElemPtr, qType qType: Int16, nmFlags nmFlags: Int16, nmPrivate nmPrivate: SRefCon, nmReserved nmReserved: Int16, nmMark nmMark: Int16, nmIcon nmIcon: Handle, nmSound nmSound: Handle, nmStr nmStr: StringPtr, nmResp nmResp: NMUPP, nmRefCon nmRefCon: SRefCon) } ``` |

Modified NPMColor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NPMColor {     var profile: Unmanaged<CMProfile>! } ``` |
| To | ``` struct NPMColor {     var profile: CMProfileRef     var color: CMColor     init()     init(profile profile: CMProfileRef, color color: CMColor) } ``` |

Modified NPMColor.profile

|  | Declaration |
| --- | --- |
| From | ``` var profile: Unmanaged<CMProfile>! ``` |
| To | ``` var profile: CMProfileRef ``` |

Modified NavCBRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NavCBRec {     var version: UInt16     var context: Unmanaged<NavDialog>!     var window: Unmanaged<Window>!     var customRect: Rect     var previewRect: Rect     var eventData: NavEventData     var userAction: NavUserAction     var reserved: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct NavCBRec {     var version: UInt16     var context: Unmanaged<NavDialog>!     var window: WindowRef     var customRect: Rect     var previewRect: Rect     var eventData: NavEventData     var userAction: NavUserAction     var reserved: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(version version: UInt16, context context: Unmanaged<NavDialog>!, window window: WindowRef, customRect customRect: Rect, previewRect previewRect: Rect, eventData eventData: NavEventData, userAction userAction: NavUserAction, reserved reserved: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified NavCBRec.window

|  | Declaration |
| --- | --- |
| From | ``` var window: Unmanaged<Window>! ``` |
| To | ``` var window: WindowRef ``` |

Modified NavDialogCreationOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NavDialogCreationOptions {     var version: UInt16     var optionFlags: NavDialogOptionFlags     var location: Point     var clientName: Unmanaged<CFString>!     var windowTitle: Unmanaged<CFString>!     var actionButtonLabel: Unmanaged<CFString>!     var cancelButtonLabel: Unmanaged<CFString>!     var saveFileName: Unmanaged<CFString>!     var message: Unmanaged<CFString>!     var preferenceKey: UInt32     var popupExtension: Unmanaged<CFArray>!     var modality: WindowModality     var parentWindow: Unmanaged<Window>!     var reserved: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct NavDialogCreationOptions {     var version: UInt16     var optionFlags: NavDialogOptionFlags     var location: Point     var clientName: Unmanaged<CFString>!     var windowTitle: Unmanaged<CFString>!     var actionButtonLabel: Unmanaged<CFString>!     var cancelButtonLabel: Unmanaged<CFString>!     var saveFileName: Unmanaged<CFString>!     var message: Unmanaged<CFString>!     var preferenceKey: UInt32     var popupExtension: Unmanaged<CFArray>!     var modality: WindowModality     var parentWindow: WindowRef     var reserved: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(version version: UInt16, optionFlags optionFlags: NavDialogOptionFlags, location location: Point, clientName clientName: Unmanaged<CFString>!, windowTitle windowTitle: Unmanaged<CFString>!, actionButtonLabel actionButtonLabel: Unmanaged<CFString>!, cancelButtonLabel cancelButtonLabel: Unmanaged<CFString>!, saveFileName saveFileName: Unmanaged<CFString>!, message message: Unmanaged<CFString>!, preferenceKey preferenceKey: UInt32, popupExtension popupExtension: Unmanaged<CFArray>!, modality modality: WindowModality, parentWindow parentWindow: WindowRef, reserved reserved: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified NavDialogCreationOptions.parentWindow

|  | Declaration |
| --- | --- |
| From | ``` var parentWindow: Unmanaged<Window>! ``` |
| To | ``` var parentWindow: WindowRef ``` |

Modified NavDialogOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NavDialogOptions {     var version: UInt16     var dialogOptionFlags: NavDialogOptionFlags     var location: Point     var clientName: Str255     var windowTitle: Str255     var actionButtonLabel: Str255     var cancelButtonLabel: Str255     var savedFileName: Str255     var message: Str255     var preferenceKey: UInt32     var popupExtension: NavMenuItemSpecArrayHandle     var reserved: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ```  ``` |

Modified NavEventData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NavEventData {     var itemHit: Int16 } ``` |
| To | ``` struct NavEventData {     var eventDataParms: NavEventDataInfo     var itemHit: Int16     init()     init(eventDataParms eventDataParms: NavEventDataInfo, itemHit itemHit: Int16) } ``` |

Modified NavFileOrFolderInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NavFileOrFolderInfo {     var version: UInt16     var isFolder: Boolean     var visible: Boolean     var creationDate: UInt32     var modificationDate: UInt32 } ``` |
| To | ``` struct NavFileOrFolderInfo {     var version: UInt16     var isFolder: Boolean     var visible: Boolean     var creationDate: UInt32     var modificationDate: UInt32     init() } ``` |

Modified NavMenuItemSpec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NavMenuItemSpec {     var version: UInt16     var menuCreator: OSType     var menuType: OSType     var menuItemName: Str255     var reserved: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct NavMenuItemSpec {     var version: UInt16     var menuCreator: OSType     var menuType: OSType     var menuItemName: Str255     var reserved: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(version version: UInt16, menuCreator menuCreator: OSType, menuType menuType: OSType, menuItemName menuItemName: Str255, reserved reserved: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified NavReplyRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NavReplyRecord {     var version: UInt16     var validRecord: Boolean     var replacing: Boolean     var isStationery: Boolean     var translationNeeded: Boolean     var selection: AEDescList     var keyScript: ScriptCode     var fileTranslation: FileTranslationSpecArrayHandle     var reserved1: UInt32     var saveFileName: Unmanaged<CFString>!     var saveFileExtensionHidden: Boolean     var reserved2: UInt8     var reserved: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct NavReplyRecord {     var version: UInt16     var validRecord: Boolean     var replacing: Boolean     var isStationery: Boolean     var translationNeeded: Boolean     var selection: AEDescList     var keyScript: ScriptCode     var fileTranslation: FileTranslationSpecArrayHandle     var reserved1: UInt32     var saveFileName: Unmanaged<CFString>!     var saveFileExtensionHidden: Boolean     var reserved2: UInt8     var reserved: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(version version: UInt16, validRecord validRecord: Boolean, replacing replacing: Boolean, isStationery isStationery: Boolean, translationNeeded translationNeeded: Boolean, selection selection: AEDescList, keyScript keyScript: ScriptCode, fileTranslation fileTranslation: FileTranslationSpecArrayHandle, reserved1 reserved1: UInt32, saveFileName saveFileName: Unmanaged<CFString>!, saveFileExtensionHidden saveFileExtensionHidden: Boolean, reserved2 reserved2: UInt8, reserved reserved: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified NavTypeList [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NavTypeList {     var componentSignature: OSType     var reserved: Int16     var osTypeCount: Int16     var osType: (OSType) } ``` |
| To | ``` struct NavTypeList {     var componentSignature: OSType     var reserved: Int16     var osTypeCount: Int16     var osType: (OSType)     init()     init(componentSignature componentSignature: OSType, reserved reserved: Int16, osTypeCount osTypeCount: Int16, osType osType: (OSType)) } ``` |

Modified NullStRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NullStRec {     var teReserved: Int     var nullScrap: StScrpHandle } ``` |
| To | ``` struct NullStRec {     var teReserved: Int     var nullScrap: StScrpHandle     init()     init(teReserved teReserved: Int, nullScrap nullScrap: StScrpHandle) } ``` |

Modified PickerMenuItemInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PickerMenuItemInfo {     var editMenuID: Int16     var cutItem: Int16     var copyItem: Int16     var pasteItem: Int16     var clearItem: Int16     var undoItem: Int16 } ``` |
| To | ``` struct PickerMenuItemInfo {     var editMenuID: Int16     var cutItem: Int16     var copyItem: Int16     var pasteItem: Int16     var clearItem: Int16     var undoItem: Int16     init()     init(editMenuID editMenuID: Int16, cutItem cutItem: Int16, copyItem copyItem: Int16, pasteItem pasteItem: Int16, clearItem clearItem: Int16, undoItem undoItem: Int16) } ``` |

Modified ProgressTrackInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ProgressTrackInfo {     var phase: UInt8 } ``` |
| To | ``` struct ProgressTrackInfo {     var phase: UInt8     init()     init(phase phase: UInt8) } ``` |

Modified PromiseHFSFlavor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PromiseHFSFlavor {     var fileType: OSType     var fileCreator: OSType     var fdFlags: UInt16     var promisedFlavor: FlavorType } ``` |
| To | ``` struct PromiseHFSFlavor {     var fileType: OSType     var fileCreator: OSType     var fdFlags: UInt16     var promisedFlavor: FlavorType     init()     init(fileType fileType: OSType, fileCreator fileCreator: OSType, fdFlags fdFlags: UInt16, promisedFlavor promisedFlavor: FlavorType) } ``` |

Modified SRCallBackParam [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SRCallBackParam {     var callBack: SRCallBackUPP     var refCon: SRefCon } ``` |
| To | ``` struct SRCallBackParam {     var callBack: SRCallBackUPP     var refCon: SRefCon     init()     init(callBack callBack: SRCallBackUPP, refCon refCon: SRefCon) } ``` |

Modified SRCallBackStruct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SRCallBackStruct {     var what: UInt32     var message: Int     var instance: SRRecognizer     var status: OSErr     var flags: Int16     var refCon: SRefCon } ``` |
| To | ``` struct SRCallBackStruct {     var what: UInt32     var message: Int     var instance: SRRecognizer     var status: OSErr     var flags: Int16     var refCon: SRefCon     init()     init(what what: UInt32, message message: Int, instance instance: SRRecognizer, status status: OSErr, flags flags: Int16, refCon refCon: SRefCon) } ``` |

Modified STElement [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct STElement {     var stCount: Int16     var stHeight: Int16     var stAscent: Int16     var stFont: Int16     var stFace: StyleField     var stSize: Int16     var stColor: RGBColor } ``` |
| To | ``` struct STElement {     var stCount: Int16     var stHeight: Int16     var stAscent: Int16     var stFont: Int16     var stFace: StyleField     var stSize: Int16     var stColor: RGBColor     init()     init(stCount stCount: Int16, stHeight stHeight: Int16, stAscent stAscent: Int16, stFont stFont: Int16, stFace stFace: StyleField, stSize stSize: Int16, stColor stColor: RGBColor) } ``` |

Modified ScrapFlavorInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ScrapFlavorInfo {     var flavorType: ScrapFlavorType     var flavorFlags: ScrapFlavorFlags } ``` |
| To | ``` struct ScrapFlavorInfo {     var flavorType: ScrapFlavorType     var flavorFlags: ScrapFlavorFlags     init()     init(flavorType flavorType: ScrapFlavorType, flavorFlags flavorFlags: ScrapFlavorFlags) } ``` |

Modified ScrapTranslationList [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ScrapTranslationList {     var modDate: UInt     var groupCount: UInt } ``` |
| To | ``` struct ScrapTranslationList {     var modDate: UInt     var groupCount: UInt     init()     init(modDate modDate: UInt, groupCount groupCount: UInt) } ``` |

Modified ScrapTypeSpec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ScrapTypeSpec {     var format: ScrapType     var hint: Int } ``` |
| To | ``` struct ScrapTypeSpec {     var format: ScrapType     var hint: Int     init()     init(format format: ScrapType, hint hint: Int) } ``` |

Modified ScriptLanguageRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ScriptLanguageRecord {     var fScript: ScriptCode     var fLanguage: LangCode } ``` |
| To | ``` struct ScriptLanguageRecord {     var fScript: ScriptCode     var fLanguage: LangCode     init()     init(fScript fScript: ScriptCode, fLanguage fLanguage: LangCode) } ``` |

Modified ScriptLanguageSupport [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ScriptLanguageSupport {     var fScriptLanguageCount: Int16     var fScriptLanguageArray: (ScriptLanguageRecord) } ``` |
| To | ``` struct ScriptLanguageSupport {     var fScriptLanguageCount: Int16     var fScriptLanguageArray: (ScriptLanguageRecord)     init()     init(fScriptLanguageCount fScriptLanguageCount: Int16, fScriptLanguageArray fScriptLanguageArray: (ScriptLanguageRecord)) } ``` |

Modified ScrollBarTrackInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ScrollBarTrackInfo {     var viewsize: Int32     var pressState: ThemeTrackPressState } ``` |
| To | ``` struct ScrollBarTrackInfo {     var viewsize: Int32     var pressState: ThemeTrackPressState     init()     init(viewsize viewsize: Int32, pressState pressState: ThemeTrackPressState) } ``` |

Modified ScrpSTElement [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ScrpSTElement {     var scrpStartChar: Int32     var scrpHeight: Int16     var scrpAscent: Int16     var scrpFont: Int16     var scrpFace: StyleField     var scrpSize: Int16     var scrpColor: RGBColor } ``` |
| To | ``` struct ScrpSTElement {     var scrpStartChar: Int32     var scrpHeight: Int16     var scrpAscent: Int16     var scrpFont: Int16     var scrpFace: StyleField     var scrpSize: Int16     var scrpColor: RGBColor     init()     init(scrpStartChar scrpStartChar: Int32, scrpHeight scrpHeight: Int16, scrpAscent scrpAscent: Int16, scrpFont scrpFont: Int16, scrpFace scrpFace: StyleField, scrpSize scrpSize: Int16, scrpColor scrpColor: RGBColor) } ``` |

Modified SetupWindowProxyDragImageRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SetupWindowProxyDragImageRec {     var imageGWorld: GWorldPtr     var imageRgn: RgnHandle     var outlineRgn: RgnHandle } ``` |
| To | ``` struct SetupWindowProxyDragImageRec {     var imageGWorld: GWorldPtr     var imageRgn: RgnHandle     var outlineRgn: RgnHandle     init()     init(imageGWorld imageGWorld: GWorldPtr, imageRgn imageRgn: RgnHandle, outlineRgn outlineRgn: RgnHandle) } ``` |

Modified SliderTrackInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SliderTrackInfo {     var thumbDir: ThemeThumbDirection     var pressState: ThemeTrackPressState } ``` |
| To | ``` struct SliderTrackInfo {     var thumbDir: ThemeThumbDirection     var pressState: ThemeTrackPressState     init()     init(thumbDir thumbDir: ThemeThumbDirection, pressState pressState: ThemeTrackPressState) } ``` |

Modified StScrpRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct StScrpRec {     var scrpNStyles: Int16     var scrpStyleTab: ScrpSTTable } ``` |
| To | ``` struct StScrpRec {     var scrpNStyles: Int16     var scrpStyleTab: ScrpSTTable     init()     init(scrpNStyles scrpNStyles: Int16, scrpStyleTab scrpStyleTab: ScrpSTTable) } ``` |

Modified StandardIconListCellDataRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct StandardIconListCellDataRec {     var iconHandle: Handle     var font: Int16     var face: Int16     var size: Int16     var name: Str255 } ``` |
| To | ``` struct StandardIconListCellDataRec {     var iconHandle: Handle     var font: Int16     var face: Int16     var size: Int16     var name: Str255     init()     init(iconHandle iconHandle: Handle, font font: Int16, face face: Int16, size size: Int16, name name: Str255) } ``` |

Modified StyleRun [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct StyleRun {     var startChar: Int16     var styleIndex: Int16 } ``` |
| To | ``` struct StyleRun {     var startChar: Int16     var styleIndex: Int16     init()     init(startChar startChar: Int16, styleIndex styleIndex: Int16) } ``` |

Modified TSMGlyphInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TSMGlyphInfo {     var range: CFRange     var fontRef: ATSFontRef     var collection: UInt16     var glyphID: UInt16 } ``` |
| To | ``` struct TSMGlyphInfo {     var range: CFRange     var fontRef: ATSFontRef     var collection: UInt16     var glyphID: UInt16     init()     init(range range: CFRange, fontRef fontRef: ATSFontRef, collection collection: UInt16, glyphID glyphID: UInt16) } ``` |

Modified TSMGlyphInfoArray [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TSMGlyphInfoArray {     var numGlyphInfo: ItemCount     var glyphInfo: (TSMGlyphInfo) } ``` |
| To | ``` struct TSMGlyphInfoArray {     var numGlyphInfo: Int     var glyphInfo: (TSMGlyphInfo)     init()     init(numGlyphInfo numGlyphInfo: Int, glyphInfo glyphInfo: (TSMGlyphInfo)) } ``` |

Modified TSMGlyphInfoArray.numGlyphInfo

|  | Declaration |
| --- | --- |
| From | ``` var numGlyphInfo: ItemCount ``` |
| To | ``` var numGlyphInfo: Int ``` |

Modified TXNATSUIFeatures [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TXNATSUIFeatures {     var featureCount: ItemCount     var featureTypes: UnsafePointer<ATSUFontFeatureType>     var featureSelectors: UnsafePointer<ATSUFontFeatureSelector> } ``` |
| To | ``` struct TXNATSUIFeatures {     var featureCount: Int     var featureTypes: UnsafeMutablePointer<ATSUFontFeatureType>     var featureSelectors: UnsafeMutablePointer<ATSUFontFeatureSelector>     init()     init(featureCount featureCount: Int, featureTypes featureTypes: UnsafeMutablePointer<ATSUFontFeatureType>, featureSelectors featureSelectors: UnsafeMutablePointer<ATSUFontFeatureSelector>) } ``` |

Modified TXNATSUIFeatures.featureCount

|  | Declaration |
| --- | --- |
| From | ``` var featureCount: ItemCount ``` |
| To | ``` var featureCount: Int ``` |

Modified TXNATSUIFeatures.featureSelectors

|  | Declaration |
| --- | --- |
| From | ``` var featureSelectors: UnsafePointer<ATSUFontFeatureSelector> ``` |
| To | ``` var featureSelectors: UnsafeMutablePointer<ATSUFontFeatureSelector> ``` |

Modified TXNATSUIFeatures.featureTypes

|  | Declaration |
| --- | --- |
| From | ``` var featureTypes: UnsafePointer<ATSUFontFeatureType> ``` |
| To | ``` var featureTypes: UnsafeMutablePointer<ATSUFontFeatureType> ``` |

Modified TXNATSUIVariations [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TXNATSUIVariations {     var variationCount: ItemCount     var variationAxis: UnsafePointer<ATSUFontVariationAxis>     var variationValues: UnsafePointer<ATSUFontVariationValue> } ``` |
| To | ``` struct TXNATSUIVariations {     var variationCount: Int     var variationAxis: UnsafeMutablePointer<ATSUFontVariationAxis>     var variationValues: UnsafeMutablePointer<ATSUFontVariationValue>     init()     init(variationCount variationCount: Int, variationAxis variationAxis: UnsafeMutablePointer<ATSUFontVariationAxis>, variationValues variationValues: UnsafeMutablePointer<ATSUFontVariationValue>) } ``` |

Modified TXNATSUIVariations.variationAxis

|  | Declaration |
| --- | --- |
| From | ``` var variationAxis: UnsafePointer<ATSUFontVariationAxis> ``` |
| To | ``` var variationAxis: UnsafeMutablePointer<ATSUFontVariationAxis> ``` |

Modified TXNATSUIVariations.variationCount

|  | Declaration |
| --- | --- |
| From | ``` var variationCount: ItemCount ``` |
| To | ``` var variationCount: Int ``` |

Modified TXNATSUIVariations.variationValues

|  | Declaration |
| --- | --- |
| From | ``` var variationValues: UnsafePointer<ATSUFontVariationValue> ``` |
| To | ``` var variationValues: UnsafeMutablePointer<ATSUFontVariationValue> ``` |

Modified TXNBackground [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TXNBackground {     var bgType: TXNBackgroundType     var bg: TXNBackgroundData } ``` |
| To | ``` struct TXNBackground {     var bgType: TXNBackgroundType     var bg: TXNBackgroundData     init()     init(bgType bgType: TXNBackgroundType, bg bg: TXNBackgroundData) } ``` |

Modified TXNBackgroundData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TXNBackgroundData {     var color: RGBColor } ``` |
| To | ``` struct TXNBackgroundData {     var color: RGBColor     init()     init(color color: RGBColor) } ``` |

Modified TXNCarbonEventInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TXNCarbonEventInfo {     var useCarbonEvents: Boolean     var filler: UInt8     var flags: UInt16     var fDictionary: Unmanaged<CFDictionary>! } ``` |
| To | ``` struct TXNCarbonEventInfo {     var useCarbonEvents: Boolean     var filler: UInt8     var flags: UInt16     var fDictionary: Unmanaged<CFDictionary>!     init()     init(useCarbonEvents useCarbonEvents: Boolean, filler filler: UInt8, flags flags: UInt16, fDictionary fDictionary: Unmanaged<CFDictionary>!) } ``` |

Modified TXNLongRect [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TXNLongRect {     var top: Int32     var left: Int32     var bottom: Int32     var right: Int32 } ``` |
| To | ``` struct TXNLongRect {     var top: Int32     var left: Int32     var bottom: Int32     var right: Int32     init()     init(top top: Int32, left left: Int32, bottom bottom: Int32, right right: Int32) } ``` |

Modified TXNMargins [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TXNMargins {     var topMargin: Int16     var leftMargin: Int16     var bottomMargin: Int16     var rightMargin: Int16 } ``` |
| To | ``` struct TXNMargins {     var topMargin: Int16     var leftMargin: Int16     var bottomMargin: Int16     var rightMargin: Int16     init()     init(topMargin topMargin: Int16, leftMargin leftMargin: Int16, bottomMargin bottomMargin: Int16, rightMargin rightMargin: Int16) } ``` |

Modified TXNMatchTextRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TXNMatchTextRecord {     var iTextPtr: ConstUnsafePointer<()>     var iTextToMatchLength: Int     var iTextEncoding: TextEncoding } ``` |
| To | ``` struct TXNMatchTextRecord {     var iTextPtr: UnsafePointer<Void>     var iTextToMatchLength: Int     var iTextEncoding: TextEncoding     init()     init(iTextPtr iTextPtr: UnsafePointer<Void>, iTextToMatchLength iTextToMatchLength: Int, iTextEncoding iTextEncoding: TextEncoding) } ``` |

Modified TXNMatchTextRecord.iTextPtr

|  | Declaration |
| --- | --- |
| From | ``` var iTextPtr: ConstUnsafePointer<()> ``` |
| To | ``` var iTextPtr: UnsafePointer<Void> ``` |

Modified TXNTab [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TXNTab {     var value: Int16     var tabType: TXNTabType     var filler: UInt8 } ``` |
| To | ``` struct TXNTab {     var value: Int16     var tabType: TXNTabType     var filler: UInt8     init()     init(value value: Int16, tabType tabType: TXNTabType, filler filler: UInt8) } ``` |

Modified TXNTypeAttributes [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TXNTypeAttributes {     var tag: TXNTypeRunAttributes     var size: ByteCount } ``` |
| To | ``` struct TXNTypeAttributes {     var tag: TXNTypeRunAttributes     var size: Int     var data: TXNAttributeData     init()     init(tag tag: TXNTypeRunAttributes, size size: Int, data data: TXNAttributeData) } ``` |

Modified TXNTypeAttributes.size

|  | Declaration |
| --- | --- |
| From | ``` var size: ByteCount ``` |
| To | ``` var size: Int ``` |

Modified TabletPointRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TabletPointRec {     var absX: Int32     var absY: Int32     var absZ: Int32     var buttons: UInt16     var pressure: UInt16     var tiltX: Int16     var tiltY: Int16     var rotation: UInt16     var tangentialPressure: Int16     var deviceID: UInt16     var vendor1: Int16     var vendor2: Int16     var vendor3: Int16 } ``` |
| To | ``` struct TabletPointRec {     var absX: Int32     var absY: Int32     var absZ: Int32     var buttons: UInt16     var pressure: UInt16     var tiltX: Int16     var tiltY: Int16     var rotation: UInt16     var tangentialPressure: Int16     var deviceID: UInt16     var vendor1: Int16     var vendor2: Int16     var vendor3: Int16     init()     init(absX absX: Int32, absY absY: Int32, absZ absZ: Int32, buttons buttons: UInt16, pressure pressure: UInt16, tiltX tiltX: Int16, tiltY tiltY: Int16, rotation rotation: UInt16, tangentialPressure tangentialPressure: Int16, deviceID deviceID: UInt16, vendor1 vendor1: Int16, vendor2 vendor2: Int16, vendor3 vendor3: Int16) } ``` |

Modified TabletProximityRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TabletProximityRec {     var vendorID: UInt16     var tabletID: UInt16     var pointerID: UInt16     var deviceID: UInt16     var systemTabletID: UInt16     var vendorPointerType: UInt16     var pointerSerialNumber: UInt32     var uniqueID: UInt64     var capabilityMask: UInt32     var pointerType: UInt8     var enterProximity: UInt8 } ``` |
| To | ``` struct TabletProximityRec {     var vendorID: UInt16     var tabletID: UInt16     var pointerID: UInt16     var deviceID: UInt16     var systemTabletID: UInt16     var vendorPointerType: UInt16     var pointerSerialNumber: UInt32     var uniqueID: UInt64     var capabilityMask: UInt32     var pointerType: UInt8     var enterProximity: UInt8     init()     init(vendorID vendorID: UInt16, tabletID tabletID: UInt16, pointerID pointerID: UInt16, deviceID deviceID: UInt16, systemTabletID systemTabletID: UInt16, vendorPointerType vendorPointerType: UInt16, pointerSerialNumber pointerSerialNumber: UInt32, uniqueID uniqueID: UInt64, capabilityMask capabilityMask: UInt32, pointerType pointerType: UInt8, enterProximity enterProximity: UInt8) } ``` |

Modified TextServiceInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TextServiceInfo {     var fComponent: Component     var fItemName: Str255 } ``` |
| To | ``` struct TextServiceInfo {     var fComponent: Component     var fItemName: Str255     init()     init(fComponent fComponent: Component, fItemName fItemName: Str255) } ``` |

Modified TextServiceList [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TextServiceList {     var fTextServiceCount: Int16     var fServices: (TextServiceInfo) } ``` |
| To | ``` struct TextServiceList {     var fTextServiceCount: Int16     var fServices: (TextServiceInfo)     init()     init(fTextServiceCount fTextServiceCount: Int16, fServices fServices: (TextServiceInfo)) } ``` |

Modified TextStyle [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TextStyle {     var tsFont: Int16     var tsFace: StyleField     var tsSize: Int16     var tsColor: RGBColor } ``` |
| To | ``` struct TextStyle {     var tsFont: Int16     var tsFace: StyleField     var tsSize: Int16     var tsColor: RGBColor     init()     init(tsFont tsFont: Int16, tsFace tsFace: StyleField, tsSize tsSize: Int16, tsColor tsColor: RGBColor) } ``` |

Modified ThemeButtonDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ThemeButtonDrawInfo {     var state: ThemeDrawState     var value: ThemeButtonValue     var adornment: ThemeButtonAdornment } ``` |
| To | ``` struct ThemeButtonDrawInfo {     var state: ThemeDrawState     var value: ThemeButtonValue     var adornment: ThemeButtonAdornment     init()     init(state state: ThemeDrawState, value value: ThemeButtonValue, adornment adornment: ThemeButtonAdornment) } ``` |

Modified ThemeTrackDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ThemeTrackDrawInfo {     var kind: ThemeTrackKind     var bounds: Rect     var min: Int32     var max: Int32     var value: Int32     var reserved: UInt32     var attributes: ThemeTrackAttributes     var enableState: ThemeTrackEnableState     var filler1: UInt8 } ``` |
| To | ``` struct ThemeTrackDrawInfo {     var kind: ThemeTrackKind     var bounds: Rect     var min: Int32     var max: Int32     var value: Int32     var reserved: UInt32     var attributes: ThemeTrackAttributes     var enableState: ThemeTrackEnableState     var filler1: UInt8     init() } ``` |

Modified ThemeWindowMetrics [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ThemeWindowMetrics {     var metricSize: UInt16     var titleHeight: Int16     var titleWidth: Int16     var popupTabOffset: Int16     var popupTabWidth: Int16     var popupTabPosition: UInt16 } ``` |
| To | ``` struct ThemeWindowMetrics {     var metricSize: UInt16     var titleHeight: Int16     var titleWidth: Int16     var popupTabOffset: Int16     var popupTabWidth: Int16     var popupTabPosition: UInt16     init()     init(metricSize metricSize: UInt16, titleHeight titleHeight: Int16, titleWidth titleWidth: Int16, popupTabOffset popupTabOffset: Int16, popupTabWidth popupTabWidth: Int16, popupTabPosition popupTabPosition: UInt16) } ``` |

Modified TransitionWindowOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TransitionWindowOptions {     var version: UInt32     var duration: EventTime     var window: Unmanaged<Window>!     var userData: UnsafePointer<()> } ``` |
| To | ``` struct TransitionWindowOptions {     var version: UInt32     var duration: EventTime     var window: WindowRef     var userData: UnsafeMutablePointer<Void>     init()     init(version version: UInt32, duration duration: EventTime, window window: WindowRef, userData userData: UnsafeMutablePointer<Void>) } ``` |

Modified TransitionWindowOptions.userData

|  | Declaration |
| --- | --- |
| From | ``` var userData: UnsafePointer<()> ``` |
| To | ``` var userData: UnsafeMutablePointer<Void> ``` |

Modified TransitionWindowOptions.window

|  | Declaration |
| --- | --- |
| From | ``` var window: Unmanaged<Window>! ``` |
| To | ``` var window: WindowRef ``` |

Modified TypeSelectRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TypeSelectRecord {     var tsrLastKeyTime: UInt32     var tsrScript: ScriptCode     var tsrKeyStrokes: Str63 } ``` |
| To | ``` struct TypeSelectRecord {     var tsrLastKeyTime: UInt32     var tsrScript: ScriptCode     var tsrKeyStrokes: Str63     init()     init(tsrLastKeyTime tsrLastKeyTime: UInt32, tsrScript tsrScript: ScriptCode, tsrKeyStrokes tsrKeyStrokes: Str63) } ``` |

Modified URLCallbackInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct URLCallbackInfo {     var version: UInt32     var urlRef: URLReference     var property: ConstUnsafePointer<Int8>     var currentSize: UInt32     var systemEvent: UnsafePointer<EventRecord> } ``` |
| To | ``` struct URLCallbackInfo {     var version: UInt32     var urlRef: URLReference     var property: UnsafePointer<Int8>     var currentSize: UInt32     var systemEvent: UnsafeMutablePointer<EventRecord>     init()     init(version version: UInt32, urlRef urlRef: URLReference, property property: UnsafePointer<Int8>, currentSize currentSize: UInt32, systemEvent systemEvent: UnsafeMutablePointer<EventRecord>) } ``` |

Modified URLCallbackInfo.property

|  | Declaration |
| --- | --- |
| From | ``` var property: ConstUnsafePointer<Int8> ``` |
| To | ``` var property: UnsafePointer<Int8> ``` |

Modified URLCallbackInfo.systemEvent

|  | Declaration |
| --- | --- |
| From | ``` var systemEvent: UnsafePointer<EventRecord> ``` |
| To | ``` var systemEvent: UnsafeMutablePointer<EventRecord> ``` |

Modified WStateData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct WStateData {     var userState: Rect     var stdState: Rect } ``` |
| To | ``` struct WStateData {     var userState: Rect     var stdState: Rect     init()     init(userState userState: Rect, stdState stdState: Rect) } ``` |

Modified WinCTab [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct WinCTab {     var wCSeed: Int     var wCReserved: Int16     var ctSize: Int16     var ctTable: (ColorSpec, ColorSpec, ColorSpec, ColorSpec, ColorSpec) } ``` |
| To | ``` struct WinCTab {     var wCSeed: Int     var wCReserved: Int16     var ctSize: Int16     var ctTable: (ColorSpec, ColorSpec, ColorSpec, ColorSpec, ColorSpec)     init()     init(wCSeed wCSeed: Int, wCReserved wCReserved: Int16, ctSize ctSize: Int16, ctTable ctTable: (ColorSpec, ColorSpec, ColorSpec, ColorSpec, ColorSpec)) } ``` |

Modified WindowDefSpec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct WindowDefSpec {     var defType: WindowDefType } ``` |
| To | ``` struct WindowDefSpec {     var defType: WindowDefType     init() } ``` |

Modified AEFilterProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias AEFilterProcPtr = CFunctionPointer<((UnsafePointer<EventRecord>, Int32, AETransactionID, ConstUnsafePointer<AEAddressDesc>) -> Boolean)> ``` |
| To | ``` typealias AEFilterProcPtr = CFunctionPointer<((UnsafeMutablePointer<EventRecord>, Int32, AETransactionID, UnsafePointer<AEAddressDesc>) -> Boolean)> ``` |

Modified AEGetInteractionAllowed(UnsafeMutablePointer<AEInteractAllowed>) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func AEGetInteractionAllowed(_ level: UnsafePointer<AEInteractAllowed>) -> OSErr ``` |
| To | ``` func AEGetInteractionAllowed(_ level: UnsafeMutablePointer<AEInteractAllowed>) -> OSErr ``` |

Modified AEGetTheCurrentEvent(UnsafeMutablePointer<AppleEvent>) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func AEGetTheCurrentEvent(_ theAppleEvent: UnsafePointer<AppleEvent>) -> OSErr ``` |
| To | ``` func AEGetTheCurrentEvent(_ theAppleEvent: UnsafeMutablePointer<AppleEvent>) -> OSErr ``` |

Modified AEIdleProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias AEIdleProcPtr = CFunctionPointer<((UnsafePointer<EventRecord>, UnsafePointer<Int32>, UnsafePointer<RgnHandle>) -> Boolean)> ``` |
| To | ``` typealias AEIdleProcPtr = CFunctionPointer<((UnsafeMutablePointer<EventRecord>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<RgnHandle>) -> Boolean)> ``` |

Modified AEProcessAppleEvent(UnsafePointer<EventRecord>) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func AEProcessAppleEvent(_ theEventRecord: ConstUnsafePointer<EventRecord>) -> OSErr ``` |
| To | ``` func AEProcessAppleEvent(_ theEventRecord: UnsafePointer<EventRecord>) -> OSErr ``` |

Modified AEProcessEvent(EventRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AEProcessEvent(_ inEvent: Event!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AEProcessEvent(_ inEvent: EventRef) -> OSStatus ``` | OS X 10.5 |

Modified AEResetTimer(UnsafePointer<AppleEvent>) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func AEResetTimer(_ reply: ConstUnsafePointer<AppleEvent>) -> OSErr ``` |
| To | ``` func AEResetTimer(_ reply: UnsafePointer<AppleEvent>) -> OSErr ``` |

Modified AEResumeTheCurrentEvent(UnsafePointer<AppleEvent>, UnsafePointer<AppleEvent>, AEEventHandlerUPP, SRefCon) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func AEResumeTheCurrentEvent(_ theAppleEvent: ConstUnsafePointer<AppleEvent>, _ reply: ConstUnsafePointer<AppleEvent>, _ dispatcher: AEEventHandlerUPP, _ handlerRefcon: SRefCon) -> OSErr ``` |
| To | ``` func AEResumeTheCurrentEvent(_ theAppleEvent: UnsafePointer<AppleEvent>, _ reply: UnsafePointer<AppleEvent>, _ dispatcher: AEEventHandlerUPP, _ handlerRefcon: SRefCon) -> OSErr ``` |

Modified AESend(UnsafePointer<AppleEvent>, UnsafeMutablePointer<AppleEvent>, AESendMode, AESendPriority, Int32, AEIdleUPP, AEFilterUPP) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func AESend(_ theAppleEvent: ConstUnsafePointer<AppleEvent>, _ reply: UnsafePointer<AppleEvent>, _ sendMode: AESendMode, _ sendPriority: AESendPriority, _ timeOutInTicks: Int32, _ idleProc: AEIdleUPP, _ filterProc: AEFilterUPP) -> OSErr ``` |
| To | ``` func AESend(_ theAppleEvent: UnsafePointer<AppleEvent>, _ reply: UnsafeMutablePointer<AppleEvent>, _ sendMode: AESendMode, _ sendPriority: AESendPriority, _ timeOutInTicks: Int32, _ idleProc: AEIdleUPP, _ filterProc: AEFilterUPP) -> OSErr ``` |

Modified AESetTheCurrentEvent(UnsafePointer<AppleEvent>) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func AESetTheCurrentEvent(_ theAppleEvent: ConstUnsafePointer<AppleEvent>) -> OSErr ``` |
| To | ``` func AESetTheCurrentEvent(_ theAppleEvent: UnsafePointer<AppleEvent>) -> OSErr ``` |

Modified AESuspendTheCurrentEvent(UnsafePointer<AppleEvent>) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func AESuspendTheCurrentEvent(_ theAppleEvent: ConstUnsafePointer<AppleEvent>) -> OSErr ``` |
| To | ``` func AESuspendTheCurrentEvent(_ theAppleEvent: UnsafePointer<AppleEvent>) -> OSErr ``` |

Modified AHRegisterHelpBook(UnsafePointer<FSRef>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func AHRegisterHelpBook(_ appBundleRef: ConstUnsafePointer<FSRef>) -> OSStatus ``` |
| To | ``` func AHRegisterHelpBook(_ appBundleRef: UnsafePointer<FSRef>) -> OSStatus ``` |

Modified AHRegisterHelpBookWithURL(CFURL!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ASCopySourceAttributes(ComponentInstance, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ASCopySourceAttributes(_ scriptingComponent: ComponentInstance, _ resultingSourceAttributes: UnsafePointer<Unmanaged<CFArray>?>) -> OSAError ``` | OS X 10.10 |
| To | ``` func ASCopySourceAttributes(_ scriptingComponent: ComponentInstance, _ resultingSourceAttributes: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSAError ``` | OS X 10.5 |

Modified ASGetSourceStyleNames(ComponentInstance, Int32, UnsafeMutablePointer<AEDescList>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ASGetSourceStyleNames(_ scriptingComponent: ComponentInstance, _ modeFlags: Int32, _ resultingSourceStyleNamesList: UnsafePointer<AEDescList>) -> OSAError ``` | OS X 10.10 |
| To | ``` func ASGetSourceStyleNames(_ scriptingComponent: ComponentInstance, _ modeFlags: Int32, _ resultingSourceStyleNamesList: UnsafeMutablePointer<AEDescList>) -> OSAError ``` | OS X 10.0 |

Modified ASInit(ComponentInstance, Int32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32) -> OSAError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified ASSetSourceAttributes(ComponentInstance, CFArray!) -> OSAError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified AcquireFirstMatchingEventInQueue(EventQueueRef, Int, UnsafePointer<EventTypeSpec>, OptionBits) -> EventRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AcquireFirstMatchingEventInQueue(_ inQueue: EventQueue!, _ inNumTypes: ItemCount, _ inList: ConstUnsafePointer<EventTypeSpec>, _ inOptions: OptionBits) -> Unmanaged<Event>! ``` | OS X 10.10 |
| To | ``` func AcquireFirstMatchingEventInQueue(_ inQueue: EventQueueRef, _ inNumTypes: Int, _ inList: UnsafePointer<EventTypeSpec>, _ inOptions: OptionBits) -> EventRef ``` | OS X 10.3 |

Modified AddEventTypesToHandler(EventHandlerRef, Int, UnsafePointer<EventTypeSpec>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AddEventTypesToHandler(_ inHandlerRef: EventHandler!, _ inNumTypes: ItemCount, _ inList: ConstUnsafePointer<EventTypeSpec>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AddEventTypesToHandler(_ inHandlerRef: EventHandlerRef, _ inNumTypes: Int, _ inList: UnsafePointer<EventTypeSpec>) -> OSStatus ``` | OS X 10.10.3 |

Modified AlertStdAlertParamPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias AlertStdAlertParamPtr = UnsafePointer<AlertStdAlertParamRec> ``` |
| To | ``` typealias AlertStdAlertParamPtr = UnsafeMutablePointer<AlertStdAlertParamRec> ``` |

Modified AlertStdCFStringAlertParamPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias AlertStdCFStringAlertParamPtr = UnsafePointer<AlertStdCFStringAlertParamRec> ``` |
| To | ``` typealias AlertStdCFStringAlertParamPtr = UnsafeMutablePointer<AlertStdCFStringAlertParamRec> ``` |

Modified AlertTHndl

|  | Declaration |
| --- | --- |
| From | ``` typealias AlertTHndl = UnsafePointer<AlertTPtr> ``` |
| To | ``` typealias AlertTHndl = UnsafeMutablePointer<AlertTPtr> ``` |

Modified AlertTPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias AlertTPtr = UnsafePointer<AlertTemplate> ``` |
| To | ``` typealias AlertTPtr = UnsafeMutablePointer<AlertTemplate> ``` |

Modified CCTabHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias CCTabHandle = UnsafePointer<CCTabPtr> ``` |
| To | ``` typealias CCTabHandle = UnsafeMutablePointer<CCTabPtr> ``` |

Modified CCTabPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias CCTabPtr = UnsafePointer<CtlCTab> ``` |
| To | ``` typealias CCTabPtr = UnsafeMutablePointer<CtlCTab> ``` |

Modified CMCalibrateDisplay(UnsafeMutablePointer<CalibratorInfo>) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func CMCalibrateDisplay(_ theInfo: UnsafePointer<CalibratorInfo>) -> OSErr ``` |
| To | ``` func CMCalibrateDisplay(_ theInfo: UnsafeMutablePointer<CalibratorInfo>) -> OSErr ``` |

Modified CMPluginExamineContext(UnsafeMutablePointer<Void>, UnsafePointer<AEDesc>, UnsafeMutablePointer<AEDescList>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMPluginExamineContext(_ thisInstance: UnsafePointer<()>, _ inContext: ConstUnsafePointer<AEDesc>, _ outCommandPairs: UnsafePointer<AEDescList>) -> OSStatus ``` |
| To | ``` func CMPluginExamineContext(_ thisInstance: UnsafeMutablePointer<Void>, _ inContext: UnsafePointer<AEDesc>, _ outCommandPairs: UnsafeMutablePointer<AEDescList>) -> OSStatus ``` |

Modified CMPluginHandleSelection(UnsafeMutablePointer<Void>, UnsafeMutablePointer<AEDesc>, Int32) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMPluginHandleSelection(_ thisInstance: UnsafePointer<()>, _ inContext: UnsafePointer<AEDesc>, _ inCommandID: Int32) -> OSStatus ``` |
| To | ``` func CMPluginHandleSelection(_ thisInstance: UnsafeMutablePointer<Void>, _ inContext: UnsafeMutablePointer<AEDesc>, _ inCommandID: Int32) -> OSStatus ``` |

Modified CMPluginPostMenuCleanup(UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func CMPluginPostMenuCleanup(_ thisInstance: UnsafePointer<()>) ``` |
| To | ``` func CMPluginPostMenuCleanup(_ thisInstance: UnsafeMutablePointer<Void>) ``` |

Modified CalibrateEventProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias CalibrateEventProcPtr = CFunctionPointer<((UnsafePointer<EventRecord>) -> Void)> ``` |
| To | ``` typealias CalibrateEventProcPtr = CFunctionPointer<((UnsafeMutablePointer<EventRecord>) -> Void)> ``` |

Modified CalibrateProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias CalibrateProcPtr = CFunctionPointer<((UnsafePointer<CalibratorInfo>) -> OSErr)> ``` |
| To | ``` typealias CalibrateProcPtr = CFunctionPointer<((UnsafeMutablePointer<CalibratorInfo>) -> OSErr)> ``` |

Modified CallNextEventHandler(EventHandlerCallRef, EventRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CallNextEventHandler(_ inCallRef: EventHandlerCall!, _ inEvent: Event!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CallNextEventHandler(_ inCallRef: EventHandlerCallRef, _ inEvent: EventRef) -> OSStatus ``` | OS X 10.10.3 |

Modified CanCalibrateProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias CanCalibrateProcPtr = CFunctionPointer<((CMDisplayIDType, UnsafePointer<UInt8>) -> Boolean)> ``` |
| To | ``` typealias CanCalibrateProcPtr = CFunctionPointer<((CMDisplayIDType, UnsafeMutablePointer<UInt8>) -> Boolean)> ``` |

Modified CaretHookProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias CaretHookProcPtr = CFunctionPointer<((ConstUnsafePointer<Rect>, TEPtr) -> Void)> ``` |
| To | ``` typealias CaretHookProcPtr = CFunctionPointer<((UnsafePointer<Rect>, TEPtr) -> Void)> ``` |

Modified CharsHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias CharsHandle = UnsafePointer<CharsPtr> ``` |
| To | ``` typealias CharsHandle = UnsafeMutablePointer<CharsPtr> ``` |

Modified CharsPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias CharsPtr = UnsafePointer<Int8> ``` |
| To | ``` typealias CharsPtr = UnsafeMutablePointer<Int8> ``` |

Modified ColorChangedUPP

|  | Declaration |
| --- | --- |
| From | ``` typealias ColorChangedUPP = UnsafePointer<()> ``` |
| To | ``` typealias ColorChangedUPP = UnsafeMutablePointer<Void> ``` |

Modified ControlButtonContentInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ControlButtonContentInfoPtr = UnsafePointer<ControlButtonContentInfo> ``` |
| To | ``` typealias ControlButtonContentInfoPtr = UnsafeMutablePointer<ControlButtonContentInfo> ``` |

Modified ControlEditTextSelectionPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ControlEditTextSelectionPtr = UnsafePointer<ControlEditTextSelectionRec> ``` |
| To | ``` typealias ControlEditTextSelectionPtr = UnsafeMutablePointer<ControlEditTextSelectionRec> ``` |

Modified ControlFontStylePtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ControlFontStylePtr = UnsafePointer<ControlFontStyleRec> ``` |
| To | ``` typealias ControlFontStylePtr = UnsafeMutablePointer<ControlFontStyleRec> ``` |

Modified ControlHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias ControlHandle = Control ``` |
| To | ``` typealias ControlHandle = ControlHandle ``` |

Modified ControlImageContentInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ControlImageContentInfoPtr = UnsafePointer<ControlImageContentInfo> ``` |
| To | ``` typealias ControlImageContentInfoPtr = UnsafeMutablePointer<ControlImageContentInfo> ``` |

Modified ControlKeyFilterProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ControlKeyFilterProcPtr = CFunctionPointer<((Control!, UnsafePointer<Int16>, UnsafePointer<Int16>, UnsafePointer<EventModifiers>) -> ControlKeyFilterResult)> ``` |
| To | ``` typealias ControlKeyFilterProcPtr = CFunctionPointer<((Control!, UnsafeMutablePointer<Int16>, UnsafeMutablePointer<Int16>, UnsafeMutablePointer<EventModifiers>) -> ControlKeyFilterResult)> ``` |

Modified ControlTemplateHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias ControlTemplateHandle = UnsafePointer<ControlTemplatePtr> ``` |
| To | ``` typealias ControlTemplateHandle = UnsafeMutablePointer<ControlTemplatePtr> ``` |

Modified ControlTemplatePtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ControlTemplatePtr = UnsafePointer<ControlTemplate> ``` |
| To | ``` typealias ControlTemplatePtr = UnsafeMutablePointer<ControlTemplate> ``` |

Modified CopyEvent(EventRef) -> EventRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CopyEvent(_ inOther: Event!) -> Unmanaged<Event>! ``` | OS X 10.10 |
| To | ``` func CopyEvent(_ inOther: EventRef) -> EventRef ``` | OS X 10.10.3 |

Modified CopyEventAs(CFAllocator!, EventRef, OSType, UInt32) -> EventRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CopyEventAs(_ inAllocator: CFAllocator!, _ inOther: Event!, _ inEventClass: OSType, _ inEventKind: UInt32) -> Unmanaged<Event>! ``` | OS X 10.10 |
| To | ``` func CopyEventAs(_ inAllocator: CFAllocator!, _ inOther: EventRef, _ inEventClass: OSType, _ inEventKind: UInt32) -> EventRef ``` | OS X 10.3 |

Modified CopyEventCGEvent(EventRef) -> Unmanaged<CGEvent>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CopyEventCGEvent(_ inEvent: Event!) -> Unmanaged<CGEvent>! ``` | OS X 10.10 |
| To | ``` func CopyEventCGEvent(_ inEvent: EventRef) -> Unmanaged<CGEvent>! ``` | OS X 10.5 |

Modified CopySymbolicHotKeys(UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CopySymbolicHotKeys(_ outHotKeyArray: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CopySymbolicHotKeys(_ outHotKeyArray: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.3 |

Modified CopyThemeIdentifier(UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CopyThemeIdentifier(_ outIdentifier: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CopyThemeIdentifier(_ outIdentifier: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.1 |

Modified CreateEvent(CFAllocator!, OSType, UInt32, EventTime, EventAttributes, UnsafeMutablePointer<EventRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CreateEvent(_ inAllocator: CFAllocator!, _ inClassID: OSType, _ inKind: UInt32, _ inWhen: EventTime, _ inAttributes: EventAttributes, _ outEvent: UnsafePointer<Unmanaged<Event>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CreateEvent(_ inAllocator: CFAllocator!, _ inClassID: OSType, _ inKind: UInt32, _ inWhen: EventTime, _ inAttributes: EventAttributes, _ outEvent: UnsafeMutablePointer<EventRef>) -> OSStatus ``` | OS X 10.10.3 |

Modified CreateEventWithCGEvent(CFAllocator!, CGEvent!, EventAttributes, UnsafeMutablePointer<EventRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CreateEventWithCGEvent(_ inAllocator: CFAllocator!, _ inEvent: CGEvent!, _ inAttributes: EventAttributes, _ outEvent: UnsafePointer<Unmanaged<Event>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CreateEventWithCGEvent(_ inAllocator: CFAllocator!, _ inEvent: CGEvent!, _ inAttributes: EventAttributes, _ outEvent: UnsafeMutablePointer<EventRef>) -> OSStatus ``` | OS X 10.5 |

Modified DataBrowserAcceptDragProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DataBrowserAcceptDragProcPtr = CFunctionPointer<((Control!, DragReference!, DataBrowserItemID) -> Boolean)> ``` |
| To | ``` typealias DataBrowserAcceptDragProcPtr = CFunctionPointer<((Control!, DragReference, DataBrowserItemID) -> Boolean)> ``` |

Modified DataBrowserAddDragItemProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DataBrowserAddDragItemProcPtr = CFunctionPointer<((Control!, DragReference!, DataBrowserItemID, UnsafePointer<ItemReference>) -> Boolean)> ``` |
| To | ``` typealias DataBrowserAddDragItemProcPtr = CFunctionPointer<((Control!, DragReference, DataBrowserItemID, UnsafeMutablePointer<ItemReference>) -> Boolean)> ``` |

Modified DataBrowserDrawItemProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DataBrowserDrawItemProcPtr = CFunctionPointer<((Control!, DataBrowserItemID, DataBrowserPropertyID, DataBrowserItemState, ConstUnsafePointer<Rect>, Int16, Boolean) -> Void)> ``` |
| To | ``` typealias DataBrowserDrawItemProcPtr = CFunctionPointer<((Control!, DataBrowserItemID, DataBrowserPropertyID, DataBrowserItemState, UnsafePointer<Rect>, Int16, Boolean) -> Void)> ``` |

Modified DataBrowserEditItemProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DataBrowserEditItemProcPtr = CFunctionPointer<((Control!, DataBrowserItemID, DataBrowserPropertyID, CFString!, UnsafePointer<Rect>, UnsafePointer<Boolean>) -> Boolean)> ``` |
| To | ``` typealias DataBrowserEditItemProcPtr = CFunctionPointer<((Control!, DataBrowserItemID, DataBrowserPropertyID, CFString!, UnsafeMutablePointer<Rect>, UnsafeMutablePointer<Boolean>) -> Boolean)> ``` |

Modified DataBrowserGetContextualMenuProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DataBrowserGetContextualMenuProcPtr = CFunctionPointer<((Control!, UnsafePointer<Unmanaged<Menu>?>, UnsafePointer<UInt32>, UnsafePointer<Unmanaged<CFString>?>, UnsafePointer<AEDesc>) -> Void)> ``` |
| To | ``` typealias DataBrowserGetContextualMenuProcPtr = CFunctionPointer<((Control!, UnsafeMutablePointer<Unmanaged<Menu>?>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Unmanaged<CFString>?>, UnsafeMutablePointer<AEDesc>) -> Void)> ``` |

Modified DataBrowserHitTestProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DataBrowserHitTestProcPtr = CFunctionPointer<((Control!, DataBrowserItemID, DataBrowserPropertyID, ConstUnsafePointer<Rect>, ConstUnsafePointer<Rect>) -> Boolean)> ``` |
| To | ``` typealias DataBrowserHitTestProcPtr = CFunctionPointer<((Control!, DataBrowserItemID, DataBrowserPropertyID, UnsafePointer<Rect>, UnsafePointer<Rect>) -> Boolean)> ``` |

Modified DataBrowserItemAcceptDragProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DataBrowserItemAcceptDragProcPtr = CFunctionPointer<((Control!, DataBrowserItemID, DataBrowserPropertyID, ConstUnsafePointer<Rect>, DragReference!) -> DataBrowserDragFlags)> ``` |
| To | ``` typealias DataBrowserItemAcceptDragProcPtr = CFunctionPointer<((Control!, DataBrowserItemID, DataBrowserPropertyID, UnsafePointer<Rect>, DragReference) -> DataBrowserDragFlags)> ``` |

Modified DataBrowserItemDataRef

|  | Declaration |
| --- | --- |
| From | ``` typealias DataBrowserItemDataRef = UnsafePointer<()> ``` |
| To | ``` typealias DataBrowserItemDataRef = UnsafeMutablePointer<Void> ``` |

Modified DataBrowserItemDragRgnProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DataBrowserItemDragRgnProcPtr = CFunctionPointer<((Control!, DataBrowserItemID, DataBrowserPropertyID, ConstUnsafePointer<Rect>, RgnHandle) -> Void)> ``` |
| To | ``` typealias DataBrowserItemDragRgnProcPtr = CFunctionPointer<((Control!, DataBrowserItemID, DataBrowserPropertyID, UnsafePointer<Rect>, RgnHandle) -> Void)> ``` |

Modified DataBrowserItemHelpContentProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DataBrowserItemHelpContentProcPtr = CFunctionPointer<((Control!, DataBrowserItemID, DataBrowserPropertyID, HMContentRequest, UnsafePointer<HMContentProvidedType>, UnsafePointer<HMHelpContentRec>) -> Void)> ``` |
| To | ``` typealias DataBrowserItemHelpContentProcPtr = CFunctionPointer<((Control!, DataBrowserItemID, DataBrowserPropertyID, HMContentRequest, UnsafeMutablePointer<HMContentProvidedType>, UnsafeMutablePointer<HMHelpContentRec>) -> Void)> ``` |

Modified DataBrowserItemProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DataBrowserItemProcPtr = CFunctionPointer<((DataBrowserItemID, DataBrowserItemState, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias DataBrowserItemProcPtr = CFunctionPointer<((DataBrowserItemID, DataBrowserItemState, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified DataBrowserItemReceiveDragProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DataBrowserItemReceiveDragProcPtr = CFunctionPointer<((Control!, DataBrowserItemID, DataBrowserPropertyID, DataBrowserDragFlags, DragReference!) -> Boolean)> ``` |
| To | ``` typealias DataBrowserItemReceiveDragProcPtr = CFunctionPointer<((Control!, DataBrowserItemID, DataBrowserPropertyID, DataBrowserDragFlags, DragReference) -> Boolean)> ``` |

Modified DataBrowserPostProcessDragProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DataBrowserPostProcessDragProcPtr = CFunctionPointer<((Control!, DragReference!, OSStatus) -> Void)> ``` |
| To | ``` typealias DataBrowserPostProcessDragProcPtr = CFunctionPointer<((Control!, DragReference, OSStatus) -> Void)> ``` |

Modified DataBrowserReceiveDragProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DataBrowserReceiveDragProcPtr = CFunctionPointer<((Control!, DragReference!, DataBrowserItemID) -> Boolean)> ``` |
| To | ``` typealias DataBrowserReceiveDragProcPtr = CFunctionPointer<((Control!, DragReference, DataBrowserItemID) -> Boolean)> ``` |

Modified DataBrowserTrackingProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DataBrowserTrackingProcPtr = CFunctionPointer<((Control!, DataBrowserItemID, DataBrowserPropertyID, ConstUnsafePointer<Rect>, Point, EventModifiers) -> DataBrowserTrackingResult)> ``` |
| To | ``` typealias DataBrowserTrackingProcPtr = CFunctionPointer<((Control!, DataBrowserItemID, DataBrowserPropertyID, UnsafePointer<Rect>, Point, EventModifiers) -> DataBrowserTrackingResult)> ``` |

Modified DataHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias DataHandle = UnsafePointer<DataPtr> ``` |
| To | ``` typealias DataHandle = UnsafeMutablePointer<DataPtr> ``` |

Modified DataPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DataPtr = UnsafePointer<Int8> ``` |
| To | ``` typealias DataPtr = UnsafeMutablePointer<Int8> ``` |

Modified DebugPrintEvent(EventRef)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DebugPrintEvent(_ inEvent: Event!) ``` | OS X 10.10 |
| To | ``` func DebugPrintEvent(_ inEvent: EventRef) ``` | OS X 10.5 |

Modified DebugPrintMainEventQueue()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DeskHookProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DeskHookProcPtr = CFunctionPointer<((Boolean, UnsafePointer<EventRecord>) -> Void)> ``` |
| To | ``` typealias DeskHookProcPtr = CFunctionPointer<((Boolean, UnsafeMutablePointer<EventRecord>) -> Void)> ``` |

Modified DialogRef

|  | Declaration |
| --- | --- |
| From | ``` typealias DialogRef = Dialog ``` |
| To | ``` typealias DialogRef = DialogPtr ``` |

Modified DialogTHndl

|  | Declaration |
| --- | --- |
| From | ``` typealias DialogTHndl = UnsafePointer<DialogTPtr> ``` |
| To | ``` typealias DialogTHndl = UnsafeMutablePointer<DialogTPtr> ``` |

Modified DialogTPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DialogTPtr = UnsafePointer<DialogTemplate> ``` |
| To | ``` typealias DialogTPtr = UnsafeMutablePointer<DialogTemplate> ``` |

Modified DisableSecureEventInput() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DisposeDataBrowserDrawItemUPP(DataBrowserDrawItemUPP)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified DisposeDataBrowserEditItemUPP(DataBrowserEditItemUPP)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified DisposeDataBrowserHitTestUPP(DataBrowserHitTestUPP)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified DisposeDataBrowserItemAcceptDragUPP(DataBrowserItemAcceptDragUPP)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified DisposeDataBrowserItemDragRgnUPP(DataBrowserItemDragRgnUPP)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified DisposeDataBrowserItemNotificationWithItemUPP(DataBrowserItemNotificationWithItemUPP)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified DisposeDataBrowserItemReceiveDragUPP(DataBrowserItemReceiveDragUPP)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified DisposeDataBrowserTrackingUPP(DataBrowserTrackingUPP)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified DisposeEventLoopIdleTimerUPP(EventLoopIdleTimerUPP)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified DisposeOSAActiveUPP(OSAActiveUPP)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified DisposeOSACreateAppleEventUPP(OSACreateAppleEventUPP)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified DisposeOSASendUPP(OSASendUPP)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified DisposeTXNActionNameMapperUPP(TXNActionNameMapperUPP)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DisposeTXNContextualMenuSetupUPP(TXNContextualMenuSetupUPP)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DisposeTXNScrollInfoUPP(TXNScrollInfoUPP)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified DoGetTranslatedFilenameProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DoGetTranslatedFilenameProcPtr = CFunctionPointer<((ComponentInstance, FileType, Int, UnsafePointer<FSSpec>) -> ComponentResult)> ``` |
| To | ``` typealias DoGetTranslatedFilenameProcPtr = CFunctionPointer<((ComponentInstance, FileType, Int, UnsafeMutablePointer<FSSpec>) -> ComponentResult)> ``` |

Modified DoIdentifyFileProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DoIdentifyFileProcPtr = CFunctionPointer<((ComponentInstance, ConstUnsafePointer<FSSpec>, UnsafePointer<FileType>) -> ComponentResult)> ``` |
| To | ``` typealias DoIdentifyFileProcPtr = CFunctionPointer<((ComponentInstance, UnsafePointer<FSSpec>, UnsafeMutablePointer<FileType>) -> ComponentResult)> ``` |

Modified DoIdentifyScrapProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DoIdentifyScrapProcPtr = CFunctionPointer<((ComponentInstance, ConstUnsafePointer<()>, Size, UnsafePointer<ScrapType>) -> ComponentResult)> ``` |
| To | ``` typealias DoIdentifyScrapProcPtr = CFunctionPointer<((ComponentInstance, UnsafePointer<Void>, Size, UnsafeMutablePointer<ScrapType>) -> ComponentResult)> ``` |

Modified DoTranslateFileProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DoTranslateFileProcPtr = CFunctionPointer<((ComponentInstance, TranslationRefNum, ConstUnsafePointer<FSSpec>, FileType, Int, ConstUnsafePointer<FSSpec>, FileType, Int) -> ComponentResult)> ``` |
| To | ``` typealias DoTranslateFileProcPtr = CFunctionPointer<((ComponentInstance, TranslationRefNum, UnsafePointer<FSSpec>, FileType, Int, UnsafePointer<FSSpec>, FileType, Int) -> ComponentResult)> ``` |

Modified DoTranslateScrapProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DoTranslateScrapProcPtr = CFunctionPointer<((ComponentInstance, TranslationRefNum, ConstUnsafePointer<()>, Size, ScrapType, Int, Handle, ScrapType, Int) -> ComponentResult)> ``` |
| To | ``` typealias DoTranslateScrapProcPtr = CFunctionPointer<((ComponentInstance, TranslationRefNum, UnsafePointer<Void>, Size, ScrapType, Int, Handle, ScrapType, Int) -> ComponentResult)> ``` |

Modified DragDrawingProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DragDrawingProcPtr = CFunctionPointer<((DragRegionMessage, RgnHandle, Point, RgnHandle, Point, UnsafePointer<()>, Drag!) -> OSErr)> ``` |
| To | ``` typealias DragDrawingProcPtr = CFunctionPointer<((DragRegionMessage, RgnHandle, Point, RgnHandle, Point, UnsafeMutablePointer<Void>, DragRef) -> OSErr)> ``` |

Modified DragInputProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DragInputProcPtr = CFunctionPointer<((UnsafePointer<Point>, UnsafePointer<Int16>, UnsafePointer<()>, Drag!) -> OSErr)> ``` |
| To | ``` typealias DragInputProcPtr = CFunctionPointer<((UnsafeMutablePointer<Point>, UnsafeMutablePointer<Int16>, UnsafeMutablePointer<Void>, DragRef) -> OSErr)> ``` |

Modified DragReceiveHandlerProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DragReceiveHandlerProcPtr = CFunctionPointer<((Window!, UnsafePointer<()>, Drag!) -> OSErr)> ``` |
| To | ``` typealias DragReceiveHandlerProcPtr = CFunctionPointer<((WindowRef, UnsafeMutablePointer<Void>, DragRef) -> OSErr)> ``` |

Modified DragRef

|  | Declaration |
| --- | --- |
| From | ``` typealias DragRef = Drag ``` |
| To | ``` typealias DragRef = COpaquePointer ``` |

Modified DragReference

|  | Declaration |
| --- | --- |
| From | ``` typealias DragReference = Drag ``` |
| To | ``` typealias DragReference = DragRef ``` |

Modified DragSendDataProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DragSendDataProcPtr = CFunctionPointer<((FlavorType, UnsafePointer<()>, DragItemRef, Drag!) -> OSErr)> ``` |
| To | ``` typealias DragSendDataProcPtr = CFunctionPointer<((FlavorType, UnsafeMutablePointer<Void>, DragItemRef, DragRef) -> OSErr)> ``` |

Modified DragTrackingHandlerProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DragTrackingHandlerProcPtr = CFunctionPointer<((DragTrackingMessage, Window!, UnsafePointer<()>, Drag!) -> OSErr)> ``` |
| To | ``` typealias DragTrackingHandlerProcPtr = CFunctionPointer<((DragTrackingMessage, WindowRef, UnsafeMutablePointer<Void>, DragRef) -> OSErr)> ``` |

Modified DrawHookProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DrawHookProcPtr = CFunctionPointer<((UInt16, UInt16, UnsafePointer<()>, TEPtr, TEHandle) -> Void)> ``` |
| To | ``` typealias DrawHookProcPtr = CFunctionPointer<((UInt16, UInt16, UnsafeMutablePointer<Void>, TEPtr, TEHandle) -> Void)> ``` |

Modified EditUnicodePostUpdateProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias EditUnicodePostUpdateProcPtr = CFunctionPointer<((UniCharArrayHandle, UniCharCount, UniCharArrayOffset, UniCharArrayOffset, UnsafePointer<()>) -> Boolean)> ``` |
| To | ``` typealias EditUnicodePostUpdateProcPtr = CFunctionPointer<((UniCharArrayHandle, Int, UniCharArrayOffset, UniCharArrayOffset, UnsafeMutablePointer<Void>) -> Boolean)> ``` |

Modified EnableSecureEventInput() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified EvQElPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias EvQElPtr = UnsafePointer<EvQEl> ``` |
| To | ``` typealias EvQElPtr = UnsafeMutablePointer<EvQEl> ``` |

Modified EventComparatorProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias EventComparatorProcPtr = CFunctionPointer<((Event!, UnsafePointer<()>) -> Boolean)> ``` |
| To | ``` typealias EventComparatorProcPtr = CFunctionPointer<((EventRef, UnsafeMutablePointer<Void>) -> Boolean)> ``` |

Modified EventHandlerCallRef

|  | Declaration |
| --- | --- |
| From | ``` typealias EventHandlerCallRef = EventHandlerCall ``` |
| To | ``` typealias EventHandlerCallRef = COpaquePointer ``` |

Modified EventHandlerProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias EventHandlerProcPtr = CFunctionPointer<((EventHandlerCall!, Event!, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias EventHandlerProcPtr = CFunctionPointer<((EventHandlerCallRef, EventRef, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified EventHandlerRef

|  | Declaration |
| --- | --- |
| From | ``` typealias EventHandlerRef = EventHandler ``` |
| To | ``` typealias EventHandlerRef = COpaquePointer ``` |

Modified EventHotKeyRef

|  | Declaration |
| --- | --- |
| From | ``` typealias EventHotKeyRef = EventHotKey ``` |
| To | ``` typealias EventHotKeyRef = COpaquePointer ``` |

Modified EventLoopIdleTimerProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias EventLoopIdleTimerProcPtr = CFunctionPointer<((EventLoopTimer!, EventLoopIdleTimerMessage, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias EventLoopIdleTimerProcPtr = CFunctionPointer<((EventLoopTimer!, EventLoopIdleTimerMessage, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified EventLoopRef

|  | Declaration |
| --- | --- |
| From | ``` typealias EventLoopRef = EventLoop ``` |
| To | ``` typealias EventLoopRef = COpaquePointer ``` |

Modified EventLoopTimerProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias EventLoopTimerProcPtr = CFunctionPointer<((EventLoopTimer!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias EventLoopTimerProcPtr = CFunctionPointer<((EventLoopTimer!, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified EventQueueRef

|  | Declaration |
| --- | --- |
| From | ``` typealias EventQueueRef = EventQueue ``` |
| To | ``` typealias EventQueueRef = COpaquePointer ``` |

Modified EventRef

|  | Declaration |
| --- | --- |
| From | ``` typealias EventRef = Event ``` |
| To | ``` typealias EventRef = COpaquePointer ``` |

Modified EventTargetRef

|  | Declaration |
| --- | --- |
| From | ``` typealias EventTargetRef = EventTarget ``` |
| To | ``` typealias EventTargetRef = COpaquePointer ``` |

Modified FCAddCollection(CFString!, OptionBits) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified FCAddFontDescriptorToCollection(FCFontDescriptor!, CFString!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified FCCopyCollectionNames() -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified FCCopyFontDescriptorsInCollection(CFString!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified FCFontDescriptorCreateWithFontAttributes(CFDictionary!) -> Unmanaged<FCFontDescriptor>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified FCFontDescriptorCreateWithName(CFString!, CGFloat) -> Unmanaged<FCFontDescriptor>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified FCRemoveCollection(CFString!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified FCRemoveFontDescriptorFromCollection(FCFontDescriptor!, CFString!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified FPIsFontPanelVisible() -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified FPShowHideFontPanel() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified FileTranslationListHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias FileTranslationListHandle = UnsafePointer<FileTranslationListPtr> ``` |
| To | ``` typealias FileTranslationListHandle = UnsafeMutablePointer<FileTranslationListPtr> ``` |

Modified FileTranslationListPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias FileTranslationListPtr = UnsafePointer<FileTranslationList> ``` |
| To | ``` typealias FileTranslationListPtr = UnsafeMutablePointer<FileTranslationList> ``` |

Modified FileTranslationSpecArrayHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias FileTranslationSpecArrayHandle = UnsafePointer<FileTranslationSpecArrayPtr> ``` |
| To | ``` typealias FileTranslationSpecArrayHandle = UnsafeMutablePointer<FileTranslationSpecArrayPtr> ``` |

Modified FileTranslationSpecArrayPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias FileTranslationSpecArrayPtr = UnsafePointer<FileTranslationSpec> ``` |
| To | ``` typealias FileTranslationSpecArrayPtr = UnsafeMutablePointer<FileTranslationSpec> ``` |

Modified FindSpecificEventInQueue(EventQueueRef, EventComparatorUPP, UnsafeMutablePointer<Void>) -> EventRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FindSpecificEventInQueue(_ inQueue: EventQueue!, _ inComparator: EventComparatorUPP, _ inCompareData: UnsafePointer<()>) -> Unmanaged<Event>! ``` | OS X 10.10 |
| To | ``` func FindSpecificEventInQueue(_ inQueue: EventQueueRef, _ inComparator: EventComparatorUPP, _ inCompareData: UnsafeMutablePointer<Void>) -> EventRef ``` | OS X 10.10.3 |

Modified FlushEventQueue(EventQueueRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FlushEventQueue(_ inQueue: EventQueue!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FlushEventQueue(_ inQueue: EventQueueRef) -> OSStatus ``` | OS X 10.10.3 |

Modified FlushEventsMatchingListFromQueue(EventQueueRef, Int, UnsafePointer<EventTypeSpec>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FlushEventsMatchingListFromQueue(_ inQueue: EventQueue!, _ inNumTypes: ItemCount, _ inList: ConstUnsafePointer<EventTypeSpec>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FlushEventsMatchingListFromQueue(_ inQueue: EventQueueRef, _ inNumTypes: Int, _ inList: UnsafePointer<EventTypeSpec>) -> OSStatus ``` | OS X 10.10.3 |

Modified FlushSpecificEventsFromQueue(EventQueueRef, EventComparatorUPP, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func FlushSpecificEventsFromQueue(_ inQueue: EventQueue!, _ inComparator: EventComparatorUPP, _ inCompareData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func FlushSpecificEventsFromQueue(_ inQueue: EventQueueRef, _ inComparator: EventComparatorUPP, _ inCompareData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.10.3 |

Modified FontSelectionQDStylePtr

|  | Declaration |
| --- | --- |
| From | ``` typealias FontSelectionQDStylePtr = UnsafePointer<FontSelectionQDStyle> ``` |
| To | ``` typealias FontSelectionQDStylePtr = UnsafeMutablePointer<FontSelectionQDStyle> ``` |

Modified GetApplicationEventTarget() -> EventTargetRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func GetApplicationEventTarget() -> Unmanaged<EventTarget>! ``` | OS X 10.10 |
| To | ``` func GetApplicationEventTarget() -> EventTargetRef ``` | OS X 10.10.3 |

Modified GetCFRunLoopFromEventLoop(EventLoopRef) -> Unmanaged<AnyObject>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func GetCFRunLoopFromEventLoop(_ inEventLoop: EventLoop!) -> Unmanaged<AnyObject>! ``` | OS X 10.10 |
| To | ``` func GetCFRunLoopFromEventLoop(_ inEventLoop: EventLoopRef) -> Unmanaged<AnyObject>! ``` | OS X 10.1 |

Modified GetColor(Point, ConstStr255Param, UnsafePointer<RGBColor>, UnsafeMutablePointer<RGBColor>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func GetColor(_ `where`: Point, _ prompt: ConstStr255Param, _ inColor: ConstUnsafePointer<RGBColor>, _ outColor: UnsafePointer<RGBColor>) -> Boolean ``` |
| To | ``` func GetColor(_ `where`: Point, _ prompt: ConstStr255Param, _ inColor: UnsafePointer<RGBColor>, _ outColor: UnsafeMutablePointer<RGBColor>) -> Boolean ``` |

Modified GetCurrentButtonState() -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified GetCurrentEvent() -> EventRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func GetCurrentEvent() -> Unmanaged<Event>! ``` | OS X 10.10 |
| To | ``` func GetCurrentEvent() -> EventRef ``` | OS X 10.2 |

Modified GetCurrentEventButtonState() -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified GetCurrentEventKeyModifiers() -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified GetCurrentEventLoop() -> EventLoopRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func GetCurrentEventLoop() -> Unmanaged<EventLoop>! ``` | OS X 10.10 |
| To | ``` func GetCurrentEventLoop() -> EventLoopRef ``` | OS X 10.10.3 |

Modified GetCurrentEventQueue() -> EventQueueRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func GetCurrentEventQueue() -> Unmanaged<EventQueue>! ``` | OS X 10.10 |
| To | ``` func GetCurrentEventQueue() -> EventQueueRef ``` | OS X 10.10.3 |

Modified GetEventClass(EventRef) -> OSType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func GetEventClass(_ inEvent: Event!) -> OSType ``` | OS X 10.10 |
| To | ``` func GetEventClass(_ inEvent: EventRef) -> OSType ``` | OS X 10.10.3 |

Modified GetEventDispatcherTarget() -> EventTargetRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func GetEventDispatcherTarget() -> Unmanaged<EventTarget>! ``` | OS X 10.10 |
| To | ``` func GetEventDispatcherTarget() -> EventTargetRef ``` | OS X 10.10.3 |

Modified GetEventKind(EventRef) -> UInt32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func GetEventKind(_ inEvent: Event!) -> UInt32 ``` | OS X 10.10 |
| To | ``` func GetEventKind(_ inEvent: EventRef) -> UInt32 ``` | OS X 10.10.3 |

Modified GetEventMonitorTarget() -> EventTargetRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func GetEventMonitorTarget() -> Unmanaged<EventTarget>! ``` | OS X 10.10 |
| To | ``` func GetEventMonitorTarget() -> EventTargetRef ``` | OS X 10.3 |

Modified GetEventParameter(EventRef, EventParamName, EventParamType, UnsafeMutablePointer<EventParamType>, Int, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func GetEventParameter(_ inEvent: Event!, _ inName: EventParamName, _ inDesiredType: EventParamType, _ outActualType: UnsafePointer<EventParamType>, _ inBufferSize: ByteCount, _ outActualSize: UnsafePointer<ByteCount>, _ outData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func GetEventParameter(_ inEvent: EventRef, _ inName: EventParamName, _ inDesiredType: EventParamType, _ outActualType: UnsafeMutablePointer<EventParamType>, _ inBufferSize: Int, _ outActualSize: UnsafeMutablePointer<Int>, _ outData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.10.3 |

Modified GetEventRetainCount(EventRef) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func GetEventRetainCount(_ inEvent: Event!) -> ItemCount ``` | OS X 10.10 |
| To | ``` func GetEventRetainCount(_ inEvent: EventRef) -> Int ``` | OS X 10.10.3 |

Modified GetEventTime(EventRef) -> EventTime

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func GetEventTime(_ inEvent: Event!) -> EventTime ``` | OS X 10.10 |
| To | ``` func GetEventTime(_ inEvent: EventRef) -> EventTime ``` | OS X 10.10.3 |

Modified GetKeys(UnsafeMutablePointer<BigEndianUInt32>)

|  | Declaration |
| --- | --- |
| From | ``` func GetKeys(_ theKeys: UnsafePointer<BigEndianUInt32>) ``` |
| To | ``` func GetKeys(_ theKeys: UnsafeMutablePointer<BigEndianUInt32>) ``` |

Modified GetMainEventLoop() -> EventLoopRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func GetMainEventLoop() -> Unmanaged<EventLoop>! ``` | OS X 10.10 |
| To | ``` func GetMainEventLoop() -> EventLoopRef ``` | OS X 10.10.3 |

Modified GetMainEventQueue() -> EventQueueRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func GetMainEventQueue() -> Unmanaged<EventQueue>! ``` | OS X 10.10 |
| To | ``` func GetMainEventQueue() -> EventQueueRef ``` | OS X 10.10.3 |

Modified GetMenuTrackingData(Menu!, UnsafeMutablePointer<MenuTrackingData>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func GetMenuTrackingData(_ theMenu: Menu!, _ outData: UnsafePointer<MenuTrackingData>) -> OSStatus ``` |
| To | ``` func GetMenuTrackingData(_ theMenu: Menu!, _ outData: UnsafeMutablePointer<MenuTrackingData>) -> OSStatus ``` |

Modified GetNextEventFilterProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias GetNextEventFilterProcPtr = CFunctionPointer<((UnsafePointer<EventRecord>, UnsafePointer<Boolean>) -> Void)> ``` |
| To | ``` typealias GetNextEventFilterProcPtr = CFunctionPointer<((UnsafeMutablePointer<EventRecord>, UnsafeMutablePointer<Boolean>) -> Void)> ``` |

Modified GetNumEventsInQueue(EventQueueRef) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func GetNumEventsInQueue(_ inQueue: EventQueue!) -> ItemCount ``` | OS X 10.10 |
| To | ``` func GetNumEventsInQueue(_ inQueue: EventQueueRef) -> Int ``` | OS X 10.10.3 |

Modified GetScrapDataProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias GetScrapDataProcPtr = CFunctionPointer<((ScrapType, Handle, UnsafePointer<()>) -> OSErr)> ``` |
| To | ``` typealias GetScrapDataProcPtr = CFunctionPointer<((ScrapType, Handle, UnsafeMutablePointer<Void>) -> OSErr)> ``` |

Modified GetSymbolicHotKeyMode() -> OptionBits

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified GetSystemUIMode(UnsafeMutablePointer<SystemUIMode>, UnsafeMutablePointer<SystemUIOptions>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func GetSystemUIMode(_ outMode: UnsafePointer<SystemUIMode>, _ outOptions: UnsafePointer<SystemUIOptions>) ``` | OS X 10.10 |
| To | ``` func GetSystemUIMode(_ outMode: UnsafeMutablePointer<SystemUIMode>, _ outOptions: UnsafeMutablePointer<SystemUIOptions>) ``` | OS X 10.2 |

Modified GetThemeMenuItemExtra(ThemeMenuItemType, UnsafeMutablePointer<Int16>, UnsafeMutablePointer<Int16>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func GetThemeMenuItemExtra(_ inItemType: ThemeMenuItemType, _ outHeight: UnsafePointer<Int16>, _ outWidth: UnsafePointer<Int16>) -> OSStatus ``` |
| To | ``` func GetThemeMenuItemExtra(_ inItemType: ThemeMenuItemType, _ outHeight: UnsafeMutablePointer<Int16>, _ outWidth: UnsafeMutablePointer<Int16>) -> OSStatus ``` |

Modified GetThemeMenuSeparatorHeight(UnsafeMutablePointer<Int16>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func GetThemeMenuSeparatorHeight(_ outHeight: UnsafePointer<Int16>) -> OSStatus ``` |
| To | ``` func GetThemeMenuSeparatorHeight(_ outHeight: UnsafeMutablePointer<Int16>) -> OSStatus ``` |

Modified GetThemeMenuTitleExtra(UnsafeMutablePointer<Int16>, Boolean) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func GetThemeMenuTitleExtra(_ outWidth: UnsafePointer<Int16>, _ inIsSquished: Boolean) -> OSStatus ``` |
| To | ``` func GetThemeMenuTitleExtra(_ outWidth: UnsafeMutablePointer<Int16>, _ inIsSquished: Boolean) -> OSStatus ``` |

Modified GetThemeMetric(ThemeMetric, UnsafeMutablePointer<Int32>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func GetThemeMetric(_ inMetric: ThemeMetric, _ outMetric: UnsafePointer<Int32>) -> OSStatus ``` |
| To | ``` func GetThemeMetric(_ inMetric: ThemeMetric, _ outMetric: UnsafeMutablePointer<Int32>) -> OSStatus ``` |

Modified GetWindowRegionPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias GetWindowRegionPtr = UnsafePointer<GetWindowRegionRec> ``` |
| To | ``` typealias GetWindowRegionPtr = UnsafeMutablePointer<GetWindowRegionRec> ``` |

Modified GetWindowRegionRecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias GetWindowRegionRecPtr = UnsafePointer<GetWindowRegionRec> ``` |
| To | ``` typealias GetWindowRegionRecPtr = UnsafeMutablePointer<GetWindowRegionRec> ``` |

Modified HIDictionaryWindowShow(DCSDictionary!, AnyObject!, CFRange, CTFont!, CGPoint, Boolean, UnsafePointer<CGAffineTransform>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIDictionaryWindowShow(_ dictionary: DCSDictionary!, _ textString: AnyObject!, _ selectionRange: CFRange, _ textFont: CTFont!, _ textOrigin: CGPoint, _ verticalText: Boolean, _ viewTransform: ConstUnsafePointer<CGAffineTransform>) ``` | OS X 10.10 |
| To | ``` func HIDictionaryWindowShow(_ dictionary: DCSDictionary!, _ textString: AnyObject!, _ selectionRange: CFRange, _ textFont: CTFont!, _ textOrigin: CGPoint, _ verticalText: Boolean, _ viewTransform: UnsafePointer<CGAffineTransform>) ``` | OS X 10.5 |

Modified HIGetMousePosition(HICoordinateSpace, UnsafeMutablePointer<Void>, UnsafeMutablePointer<HIPoint>) -> UnsafeMutablePointer<HIPoint>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIGetMousePosition(_ inSpace: HICoordinateSpace, _ inObject: UnsafePointer<()>, _ outPoint: UnsafePointer<HIPoint>) -> UnsafePointer<HIPoint> ``` | OS X 10.10 |
| To | ``` func HIGetMousePosition(_ inSpace: HICoordinateSpace, _ inObject: UnsafeMutablePointer<Void>, _ outPoint: UnsafeMutablePointer<HIPoint>) -> UnsafeMutablePointer<HIPoint> ``` | OS X 10.5 |

Modified HIMouseTrackingGetParameters(OSType, UnsafeMutablePointer<EventTime>, UnsafeMutablePointer<HISize>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIMouseTrackingGetParameters(_ inSelector: OSType, _ outTime: UnsafePointer<EventTime>, _ outDistance: UnsafePointer<HISize>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIMouseTrackingGetParameters(_ inSelector: OSType, _ outTime: UnsafeMutablePointer<EventTime>, _ outDistance: UnsafeMutablePointer<HISize>) -> OSStatus ``` | OS X 10.3 |

Modified HIObjectAddDelegate(HIObject!, HIObject!, HIDelegatePosition) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified HIObjectCopyClassID(HIObject!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified HIObjectCopyDelegates(HIObject!, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIObjectCopyDelegates(_ inObject: HIObject!, _ outDelegates: UnsafePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIObjectCopyDelegates(_ inObject: HIObject!, _ outDelegates: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` | OS X 10.5 |

Modified HIObjectCreate(CFString!, EventRef, UnsafeMutablePointer<Unmanaged<HIObject>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIObjectCreate(_ inClassID: CFString!, _ inConstructData: Event!, _ outObject: UnsafePointer<Unmanaged<HIObject>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIObjectCreate(_ inClassID: CFString!, _ inConstructData: EventRef, _ outObject: UnsafeMutablePointer<Unmanaged<HIObject>?>) -> OSStatus ``` | OS X 10.2 |

Modified HIObjectCreateFromBundle(CFBundle!, UnsafeMutablePointer<Unmanaged<HIObject>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIObjectCreateFromBundle(_ inBundle: CFBundle!, _ outObject: UnsafePointer<Unmanaged<HIObject>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIObjectCreateFromBundle(_ inBundle: CFBundle!, _ outObject: UnsafeMutablePointer<Unmanaged<HIObject>?>) -> OSStatus ``` | OS X 10.2 |

Modified HIObjectDynamicCast(HIObject!, CFString!) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIObjectDynamicCast(_ inObject: HIObject!, _ inClassID: CFString!) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func HIObjectDynamicCast(_ inObject: HIObject!, _ inClassID: CFString!) -> UnsafeMutablePointer<Void> ``` | OS X 10.2 |

Modified HIObjectFromEventTarget(EventTargetRef) -> Unmanaged<HIObject>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIObjectFromEventTarget(_ inTarget: EventTarget!) -> Unmanaged<HIObject>! ``` | OS X 10.10 |
| To | ``` func HIObjectFromEventTarget(_ inTarget: EventTargetRef) -> Unmanaged<HIObject>! ``` | OS X 10.5 |

Modified HIObjectGetEventHandlerObject(EventHandlerCallRef) -> Unmanaged<HIObject>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIObjectGetEventHandlerObject(_ inRef: EventHandlerCall!) -> Unmanaged<HIObject>! ``` | OS X 10.10 |
| To | ``` func HIObjectGetEventHandlerObject(_ inRef: EventHandlerCallRef) -> Unmanaged<HIObject>! ``` | OS X 10.5 |

Modified HIObjectGetEventTarget(HIObject!) -> EventTargetRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIObjectGetEventTarget(_ inObject: HIObject!) -> Unmanaged<EventTarget>! ``` | OS X 10.10 |
| To | ``` func HIObjectGetEventTarget(_ inObject: HIObject!) -> EventTargetRef ``` | OS X 10.2 |

Modified HIObjectIsArchivingIgnored(HIObject!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified HIObjectIsOfClass(HIObject!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified HIObjectPrintDebugInfo(HIObject!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified HIObjectRegisterSubclass(CFString!, CFString!, OptionBits, EventHandlerUPP, Int, UnsafePointer<EventTypeSpec>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Unmanaged<HIObjectClass>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIObjectRegisterSubclass(_ inClassID: CFString!, _ inBaseClassID: CFString!, _ inOptions: OptionBits, _ inConstructProc: EventHandlerUPP, _ inNumEvents: ItemCount, _ inEventList: ConstUnsafePointer<EventTypeSpec>, _ inConstructData: UnsafePointer<()>, _ outClassRef: UnsafePointer<Unmanaged<HIObjectClass>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIObjectRegisterSubclass(_ inClassID: CFString!, _ inBaseClassID: CFString!, _ inOptions: OptionBits, _ inConstructProc: EventHandlerUPP, _ inNumEvents: Int, _ inEventList: UnsafePointer<EventTypeSpec>, _ inConstructData: UnsafeMutablePointer<Void>, _ outClassRef: UnsafeMutablePointer<Unmanaged<HIObjectClass>?>) -> OSStatus ``` | OS X 10.2 |

Modified HIObjectRemoveDelegate(HIObject!, HIObject!, HIDelegatePosition) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified HIObjectUnregisterClass(HIObjectClass!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified HIPointConvert(UnsafeMutablePointer<HIPoint>, HICoordinateSpace, UnsafeMutablePointer<Void>, HICoordinateSpace, UnsafeMutablePointer<Void>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIPointConvert(_ ioPoint: UnsafePointer<HIPoint>, _ inSourceSpace: HICoordinateSpace, _ inSourceObject: UnsafePointer<()>, _ inDestinationSpace: HICoordinateSpace, _ inDestinationObject: UnsafePointer<()>) ``` | OS X 10.10 |
| To | ``` func HIPointConvert(_ ioPoint: UnsafeMutablePointer<HIPoint>, _ inSourceSpace: HICoordinateSpace, _ inSourceObject: UnsafeMutablePointer<Void>, _ inDestinationSpace: HICoordinateSpace, _ inDestinationObject: UnsafeMutablePointer<Void>) ``` | OS X 10.4 |

Modified HIRectConvert(UnsafeMutablePointer<HIRect>, HICoordinateSpace, UnsafeMutablePointer<Void>, HICoordinateSpace, UnsafeMutablePointer<Void>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIRectConvert(_ ioRect: UnsafePointer<HIRect>, _ inSourceSpace: HICoordinateSpace, _ inSourceObject: UnsafePointer<()>, _ inDestinationSpace: HICoordinateSpace, _ inDestinationObject: UnsafePointer<()>) ``` | OS X 10.10 |
| To | ``` func HIRectConvert(_ ioRect: UnsafeMutablePointer<HIRect>, _ inSourceSpace: HICoordinateSpace, _ inSourceObject: UnsafeMutablePointer<Void>, _ inDestinationSpace: HICoordinateSpace, _ inDestinationObject: UnsafeMutablePointer<Void>) ``` | OS X 10.4 |

Modified HISearchWindowShow(CFString!, OptionBits) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified HISizeConvert(UnsafeMutablePointer<HISize>, HICoordinateSpace, UnsafeMutablePointer<Void>, HICoordinateSpace, UnsafeMutablePointer<Void>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HISizeConvert(_ ioSize: UnsafePointer<HISize>, _ inSourceSpace: HICoordinateSpace, _ inSourceObject: UnsafePointer<()>, _ inDestinationSpace: HICoordinateSpace, _ inDestinationObject: UnsafePointer<()>) ``` | OS X 10.10 |
| To | ``` func HISizeConvert(_ ioSize: UnsafeMutablePointer<HISize>, _ inSourceSpace: HICoordinateSpace, _ inSourceObject: UnsafeMutablePointer<Void>, _ inDestinationSpace: HICoordinateSpace, _ inDestinationObject: UnsafeMutablePointer<Void>) ``` | OS X 10.4 |

Modified HIThemeApplyBackground(UnsafePointer<HIRect>, UnsafePointer<HIThemeBackgroundDrawInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeApplyBackground(_ inBounds: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeBackgroundDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeApplyBackground(_ inBounds: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeBackgroundDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeBackgroundDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemeBackgroundDrawInfoPtr = UnsafePointer<HIThemeBackgroundDrawInfo> ``` |
| To | ``` typealias HIThemeBackgroundDrawInfoPtr = UnsafeMutablePointer<HIThemeBackgroundDrawInfo> ``` |

Modified HIThemeBeginFocus(CGContext!, HIThemeFocusRing, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeBeginFocus(_ inContext: CGContext!, _ inRing: HIThemeFocusRing, _ inReserved: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeBeginFocus(_ inContext: CGContext!, _ inRing: HIThemeFocusRing, _ inReserved: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.5 |

Modified HIThemeBrushCreateCGColor(ThemeBrush, UnsafeMutablePointer<Unmanaged<CGColor>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeBrushCreateCGColor(_ inBrush: ThemeBrush, _ outColor: UnsafePointer<Unmanaged<CGColor>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeBrushCreateCGColor(_ inBrush: ThemeBrush, _ outColor: UnsafeMutablePointer<Unmanaged<CGColor>?>) -> OSStatus ``` | OS X 10.4 |

Modified HIThemeButtonDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemeButtonDrawInfoPtr = UnsafePointer<HIThemeButtonDrawInfo> ``` |
| To | ``` typealias HIThemeButtonDrawInfoPtr = UnsafeMutablePointer<HIThemeButtonDrawInfo> ``` |

Modified HIThemeChasingArrowsDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemeChasingArrowsDrawInfoPtr = UnsafePointer<HIThemeChasingArrowsDrawInfo> ``` |
| To | ``` typealias HIThemeChasingArrowsDrawInfoPtr = UnsafeMutablePointer<HIThemeChasingArrowsDrawInfo> ``` |

Modified HIThemeDrawBackground(UnsafePointer<HIRect>, UnsafePointer<HIThemeBackgroundDrawInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawBackground(_ inBounds: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeBackgroundDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawBackground(_ inBounds: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeBackgroundDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawButton(UnsafePointer<HIRect>, UnsafePointer<HIThemeButtonDrawInfo>, CGContext!, HIThemeOrientation, UnsafeMutablePointer<HIRect>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawButton(_ inBounds: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeButtonDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation, _ outLabelRect: UnsafePointer<HIRect>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawButton(_ inBounds: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeButtonDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation, _ outLabelRect: UnsafeMutablePointer<HIRect>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawChasingArrows(UnsafePointer<HIRect>, UnsafePointer<HIThemeChasingArrowsDrawInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawChasingArrows(_ inBounds: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeChasingArrowsDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawChasingArrows(_ inBounds: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeChasingArrowsDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawFocusRect(UnsafePointer<HIRect>, Boolean, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawFocusRect(_ inRect: ConstUnsafePointer<HIRect>, _ inHasFocus: Boolean, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawFocusRect(_ inRect: UnsafePointer<HIRect>, _ inHasFocus: Boolean, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawFrame(UnsafePointer<HIRect>, UnsafePointer<HIThemeFrameDrawInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawFrame(_ inRect: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeFrameDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawFrame(_ inRect: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeFrameDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawGenericWell(UnsafePointer<HIRect>, UnsafePointer<HIThemeButtonDrawInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawGenericWell(_ inRect: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeButtonDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawGenericWell(_ inRect: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeButtonDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawGrabber(UnsafePointer<HIRect>, UnsafePointer<HIThemeGrabberDrawInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawGrabber(_ inRect: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeGrabberDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawGrabber(_ inRect: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeGrabberDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawGroupBox(UnsafePointer<HIRect>, UnsafePointer<HIThemeGroupBoxDrawInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawGroupBox(_ inRect: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeGroupBoxDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawGroupBox(_ inRect: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeGroupBoxDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawGrowBox(UnsafePointer<HIPoint>, UnsafePointer<HIThemeGrowBoxDrawInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawGrowBox(_ inOrigin: ConstUnsafePointer<HIPoint>, _ inDrawInfo: ConstUnsafePointer<HIThemeGrowBoxDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawGrowBox(_ inOrigin: UnsafePointer<HIPoint>, _ inDrawInfo: UnsafePointer<HIThemeGrowBoxDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawHeader(UnsafePointer<HIRect>, UnsafePointer<HIThemeHeaderDrawInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawHeader(_ inRect: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeHeaderDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawHeader(_ inRect: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeHeaderDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawMenuBackground(UnsafePointer<HIRect>, UnsafePointer<HIThemeMenuDrawInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawMenuBackground(_ inMenuRect: ConstUnsafePointer<HIRect>, _ inMenuDrawInfo: ConstUnsafePointer<HIThemeMenuDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawMenuBackground(_ inMenuRect: UnsafePointer<HIRect>, _ inMenuDrawInfo: UnsafePointer<HIThemeMenuDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawMenuBarBackground(UnsafePointer<HIRect>, UnsafePointer<HIThemeMenuBarDrawInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawMenuBarBackground(_ inBounds: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeMenuBarDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawMenuBarBackground(_ inBounds: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeMenuBarDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawMenuItem(UnsafePointer<HIRect>, UnsafePointer<HIRect>, UnsafePointer<HIThemeMenuItemDrawInfo>, CGContext!, HIThemeOrientation, UnsafeMutablePointer<HIRect>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawMenuItem(_ inMenuRect: ConstUnsafePointer<HIRect>, _ inItemRect: ConstUnsafePointer<HIRect>, _ inItemDrawInfo: ConstUnsafePointer<HIThemeMenuItemDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation, _ outContentRect: UnsafePointer<HIRect>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawMenuItem(_ inMenuRect: UnsafePointer<HIRect>, _ inItemRect: UnsafePointer<HIRect>, _ inItemDrawInfo: UnsafePointer<HIThemeMenuItemDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation, _ outContentRect: UnsafeMutablePointer<HIRect>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawMenuSeparator(UnsafePointer<HIRect>, UnsafePointer<HIRect>, UnsafePointer<HIThemeMenuItemDrawInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawMenuSeparator(_ inMenuRect: ConstUnsafePointer<HIRect>, _ inItemRect: ConstUnsafePointer<HIRect>, _ inItemDrawInfo: ConstUnsafePointer<HIThemeMenuItemDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawMenuSeparator(_ inMenuRect: UnsafePointer<HIRect>, _ inItemRect: UnsafePointer<HIRect>, _ inItemDrawInfo: UnsafePointer<HIThemeMenuItemDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawMenuTitle(UnsafePointer<HIRect>, UnsafePointer<HIRect>, UnsafePointer<HIThemeMenuTitleDrawInfo>, CGContext!, HIThemeOrientation, UnsafeMutablePointer<HIRect>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawMenuTitle(_ inMenuBarRect: ConstUnsafePointer<HIRect>, _ inTitleRect: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeMenuTitleDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation, _ outLabelRect: UnsafePointer<HIRect>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawMenuTitle(_ inMenuBarRect: UnsafePointer<HIRect>, _ inTitleRect: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeMenuTitleDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation, _ outLabelRect: UnsafeMutablePointer<HIRect>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawPaneSplitter(UnsafePointer<HIRect>, UnsafePointer<HIThemeSplitterDrawInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawPaneSplitter(_ inRect: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeSplitterDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawPaneSplitter(_ inRect: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeSplitterDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawPlacard(UnsafePointer<HIRect>, UnsafePointer<HIThemePlacardDrawInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawPlacard(_ inRect: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemePlacardDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawPlacard(_ inRect: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemePlacardDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawPopupArrow(UnsafePointer<HIRect>, UnsafePointer<HIThemePopupArrowDrawInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawPopupArrow(_ inBounds: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemePopupArrowDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawPopupArrow(_ inBounds: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemePopupArrowDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawScrollBarDelimiters(UnsafePointer<HIRect>, UnsafePointer<HIThemeScrollBarDelimitersDrawInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawScrollBarDelimiters(_ inContRect: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeScrollBarDelimitersDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawScrollBarDelimiters(_ inContRect: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeScrollBarDelimitersDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawSegment(UnsafePointer<HIRect>, UnsafePointer<HIThemeSegmentDrawInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawSegment(_ inBounds: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeSegmentDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawSegment(_ inBounds: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeSegmentDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.4 |

Modified HIThemeDrawSeparator(UnsafePointer<HIRect>, UnsafePointer<HIThemeSeparatorDrawInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawSeparator(_ inRect: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeSeparatorDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawSeparator(_ inRect: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeSeparatorDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawTab(UnsafePointer<HIRect>, UnsafePointer<HIThemeTabDrawInfo>, CGContext!, HIThemeOrientation, UnsafeMutablePointer<HIRect>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawTab(_ inRect: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeTabDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation, _ outLabelRect: UnsafePointer<HIRect>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawTab(_ inRect: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeTabDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation, _ outLabelRect: UnsafeMutablePointer<HIRect>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawTabPane(UnsafePointer<HIRect>, UnsafePointer<HIThemeTabPaneDrawInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawTabPane(_ inRect: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeTabPaneDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawTabPane(_ inRect: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeTabPaneDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawTextBox(AnyObject!, UnsafePointer<HIRect>, UnsafeMutablePointer<HIThemeTextInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawTextBox(_ inString: AnyObject!, _ inBounds: ConstUnsafePointer<HIRect>, _ inTextInfo: UnsafePointer<HIThemeTextInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawTextBox(_ inString: AnyObject!, _ inBounds: UnsafePointer<HIRect>, _ inTextInfo: UnsafeMutablePointer<HIThemeTextInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawTickMark(UnsafePointer<HIRect>, UnsafePointer<HIThemeTickMarkDrawInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawTickMark(_ inBounds: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeTickMarkDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawTickMark(_ inBounds: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeTickMarkDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawTitleBarWidget(UnsafePointer<HIRect>, UnsafePointer<HIThemeWindowWidgetDrawInfo>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawTitleBarWidget(_ inContRect: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeWindowWidgetDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawTitleBarWidget(_ inContRect: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeWindowWidgetDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawTrack(UnsafePointer<HIThemeTrackDrawInfo>, UnsafePointer<HIRect>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawTrack(_ inDrawInfo: ConstUnsafePointer<HIThemeTrackDrawInfo>, _ inGhostRect: ConstUnsafePointer<HIRect>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawTrack(_ inDrawInfo: UnsafePointer<HIThemeTrackDrawInfo>, _ inGhostRect: UnsafePointer<HIRect>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawTrackTickMarks(UnsafePointer<HIThemeTrackDrawInfo>, Int, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawTrackTickMarks(_ inDrawInfo: ConstUnsafePointer<HIThemeTrackDrawInfo>, _ inNumTicks: ItemCount, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawTrackTickMarks(_ inDrawInfo: UnsafePointer<HIThemeTrackDrawInfo>, _ inNumTicks: Int, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeDrawWindowFrame(UnsafePointer<HIRect>, UnsafePointer<HIThemeWindowDrawInfo>, CGContext!, HIThemeOrientation, UnsafeMutablePointer<HIRect>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeDrawWindowFrame(_ inContRect: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeWindowDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation, _ outTitleRect: UnsafePointer<HIRect>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeDrawWindowFrame(_ inContRect: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeWindowDrawInfo>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation, _ outTitleRect: UnsafeMutablePointer<HIRect>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeEndFocus(CGContext!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified HIThemeFrameDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemeFrameDrawInfoPtr = UnsafePointer<HIThemeFrameDrawInfo> ``` |
| To | ``` typealias HIThemeFrameDrawInfoPtr = UnsafeMutablePointer<HIThemeFrameDrawInfo> ``` |

Modified HIThemeGetButtonBackgroundBounds(UnsafePointer<HIRect>, UnsafePointer<HIThemeButtonDrawInfo>, UnsafeMutablePointer<HIRect>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetButtonBackgroundBounds(_ inBounds: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeButtonDrawInfo>, _ outBounds: UnsafePointer<HIRect>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeGetButtonBackgroundBounds(_ inBounds: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeButtonDrawInfo>, _ outBounds: UnsafeMutablePointer<HIRect>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeGetButtonContentBounds(UnsafePointer<HIRect>, UnsafePointer<HIThemeButtonDrawInfo>, UnsafeMutablePointer<HIRect>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetButtonContentBounds(_ inBounds: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeButtonDrawInfo>, _ outBounds: UnsafePointer<HIRect>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeGetButtonContentBounds(_ inBounds: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeButtonDrawInfo>, _ outBounds: UnsafeMutablePointer<HIRect>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeGetButtonShape(UnsafePointer<HIRect>, UnsafePointer<HIThemeButtonDrawInfo>, UnsafeMutablePointer<Unmanaged<HIShape>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetButtonShape(_ inBounds: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeButtonDrawInfo>, _ outShape: UnsafePointer<Unmanaged<HIShape>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeGetButtonShape(_ inBounds: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeButtonDrawInfo>, _ outShape: UnsafeMutablePointer<Unmanaged<HIShape>?>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeGetGrowBoxBounds(UnsafePointer<HIPoint>, UnsafePointer<HIThemeGrowBoxDrawInfo>, UnsafeMutablePointer<HIRect>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetGrowBoxBounds(_ inOrigin: ConstUnsafePointer<HIPoint>, _ inDrawInfo: ConstUnsafePointer<HIThemeGrowBoxDrawInfo>, _ outBounds: UnsafePointer<HIRect>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeGetGrowBoxBounds(_ inOrigin: UnsafePointer<HIPoint>, _ inDrawInfo: UnsafePointer<HIThemeGrowBoxDrawInfo>, _ outBounds: UnsafeMutablePointer<HIRect>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeGetMenuBackgroundShape(UnsafePointer<HIRect>, UnsafePointer<HIThemeMenuDrawInfo>, UnsafeMutablePointer<Unmanaged<HIShape>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetMenuBackgroundShape(_ inMenuRect: ConstUnsafePointer<HIRect>, _ inMenuDrawInfo: ConstUnsafePointer<HIThemeMenuDrawInfo>, _ outShape: UnsafePointer<Unmanaged<HIShape>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeGetMenuBackgroundShape(_ inMenuRect: UnsafePointer<HIRect>, _ inMenuDrawInfo: UnsafePointer<HIThemeMenuDrawInfo>, _ outShape: UnsafeMutablePointer<Unmanaged<HIShape>?>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeGetScrollBarTrackRect(UnsafePointer<HIRect>, UnsafePointer<HIScrollBarTrackInfo>, Boolean, UnsafeMutablePointer<HIRect>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetScrollBarTrackRect(_ inBounds: ConstUnsafePointer<HIRect>, _ inTrackInfo: ConstUnsafePointer<HIScrollBarTrackInfo>, _ inIsHoriz: Boolean, _ outTrackBounds: UnsafePointer<HIRect>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeGetScrollBarTrackRect(_ inBounds: UnsafePointer<HIRect>, _ inTrackInfo: UnsafePointer<HIScrollBarTrackInfo>, _ inIsHoriz: Boolean, _ outTrackBounds: UnsafeMutablePointer<HIRect>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeGetTabDrawShape(UnsafePointer<HIRect>, UnsafePointer<HIThemeTabDrawInfo>, UnsafeMutablePointer<Unmanaged<HIShape>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetTabDrawShape(_ inRect: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeTabDrawInfo>, _ outShape: UnsafePointer<Unmanaged<HIShape>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeGetTabDrawShape(_ inRect: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeTabDrawInfo>, _ outShape: UnsafeMutablePointer<Unmanaged<HIShape>?>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeGetTabPaneContentShape(UnsafePointer<HIRect>, ThemeTabDirection, HIThemeTabSize, UnsafeMutablePointer<Unmanaged<HIShape>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetTabPaneContentShape(_ inRect: ConstUnsafePointer<HIRect>, _ inDirection: ThemeTabDirection, _ inTabSize: HIThemeTabSize, _ outShape: UnsafePointer<Unmanaged<HIShape>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeGetTabPaneContentShape(_ inRect: UnsafePointer<HIRect>, _ inDirection: ThemeTabDirection, _ inTabSize: HIThemeTabSize, _ outShape: UnsafeMutablePointer<Unmanaged<HIShape>?>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeGetTabPaneDrawShape(UnsafePointer<HIRect>, ThemeTabDirection, HIThemeTabSize, UnsafeMutablePointer<Unmanaged<HIShape>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetTabPaneDrawShape(_ inRect: ConstUnsafePointer<HIRect>, _ inDirection: ThemeTabDirection, _ inTabSize: HIThemeTabSize, _ outShape: UnsafePointer<Unmanaged<HIShape>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeGetTabPaneDrawShape(_ inRect: UnsafePointer<HIRect>, _ inDirection: ThemeTabDirection, _ inTabSize: HIThemeTabSize, _ outShape: UnsafeMutablePointer<Unmanaged<HIShape>?>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeGetTabShape(UnsafePointer<HIRect>, UnsafePointer<HIThemeTabDrawInfo>, UnsafeMutablePointer<Unmanaged<HIShape>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetTabShape(_ inRect: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeTabDrawInfo>, _ outShape: UnsafePointer<Unmanaged<HIShape>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeGetTabShape(_ inRect: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeTabDrawInfo>, _ outShape: UnsafeMutablePointer<Unmanaged<HIShape>?>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeGetTextColorForThemeBrush(ThemeBrush, Boolean, UnsafeMutablePointer<ThemeTextColor>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetTextColorForThemeBrush(_ inBrush: ThemeBrush, _ inWindowIsActive: Boolean, _ outColor: UnsafePointer<ThemeTextColor>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeGetTextColorForThemeBrush(_ inBrush: ThemeBrush, _ inWindowIsActive: Boolean, _ outColor: UnsafeMutablePointer<ThemeTextColor>) -> OSStatus ``` | OS X 10.5 |

Modified HIThemeGetTextDimensions(AnyObject!, CGFloat, UnsafeMutablePointer<HIThemeTextInfo>, UnsafeMutablePointer<CGFloat>, UnsafeMutablePointer<CGFloat>, UnsafeMutablePointer<CGFloat>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetTextDimensions(_ inString: AnyObject!, _ inWidth: CGFloat, _ inTextInfo: UnsafePointer<HIThemeTextInfo>, _ outWidth: UnsafePointer<CGFloat>, _ outHeight: UnsafePointer<CGFloat>, _ outBaseline: UnsafePointer<CGFloat>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeGetTextDimensions(_ inString: AnyObject!, _ inWidth: CGFloat, _ inTextInfo: UnsafeMutablePointer<HIThemeTextInfo>, _ outWidth: UnsafeMutablePointer<CGFloat>, _ outHeight: UnsafeMutablePointer<CGFloat>, _ outBaseline: UnsafeMutablePointer<CGFloat>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeGetTrackBounds(UnsafePointer<HIThemeTrackDrawInfo>, UnsafeMutablePointer<HIRect>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetTrackBounds(_ inDrawInfo: ConstUnsafePointer<HIThemeTrackDrawInfo>, _ outBounds: UnsafePointer<HIRect>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeGetTrackBounds(_ inDrawInfo: UnsafePointer<HIThemeTrackDrawInfo>, _ outBounds: UnsafeMutablePointer<HIRect>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeGetTrackDragRect(UnsafePointer<HIThemeTrackDrawInfo>, UnsafeMutablePointer<HIRect>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetTrackDragRect(_ inDrawInfo: ConstUnsafePointer<HIThemeTrackDrawInfo>, _ outDragRect: UnsafePointer<HIRect>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeGetTrackDragRect(_ inDrawInfo: UnsafePointer<HIThemeTrackDrawInfo>, _ outDragRect: UnsafeMutablePointer<HIRect>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeGetTrackLiveValue(UnsafePointer<HIThemeTrackDrawInfo>, CGFloat, UnsafeMutablePointer<Int32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetTrackLiveValue(_ inDrawInfo: ConstUnsafePointer<HIThemeTrackDrawInfo>, _ inRelativePosition: CGFloat, _ outValue: UnsafePointer<Int32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeGetTrackLiveValue(_ inDrawInfo: UnsafePointer<HIThemeTrackDrawInfo>, _ inRelativePosition: CGFloat, _ outValue: UnsafeMutablePointer<Int32>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeGetTrackPartBounds(UnsafePointer<HIThemeTrackDrawInfo>, ControlPartCode, UnsafeMutablePointer<HIRect>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetTrackPartBounds(_ inDrawInfo: ConstUnsafePointer<HIThemeTrackDrawInfo>, _ inPartCode: ControlPartCode, _ outPartBounds: UnsafePointer<HIRect>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeGetTrackPartBounds(_ inDrawInfo: UnsafePointer<HIThemeTrackDrawInfo>, _ inPartCode: ControlPartCode, _ outPartBounds: UnsafeMutablePointer<HIRect>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeGetTrackParts(UnsafePointer<HIThemeTrackDrawInfo>, UnsafeMutablePointer<UInt32>, UInt32, UnsafeMutablePointer<ControlPartCode>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetTrackParts(_ inDrawInfo: ConstUnsafePointer<HIThemeTrackDrawInfo>, _ outNumberOfParts: UnsafePointer<UInt32>, _ inMaxParts: UInt32, _ ioPartsBuffer: UnsafePointer<ControlPartCode>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeGetTrackParts(_ inDrawInfo: UnsafePointer<HIThemeTrackDrawInfo>, _ outNumberOfParts: UnsafeMutablePointer<UInt32>, _ inMaxParts: UInt32, _ ioPartsBuffer: UnsafeMutablePointer<ControlPartCode>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeGetTrackThumbPositionFromBounds(UnsafePointer<HIThemeTrackDrawInfo>, UnsafePointer<HIRect>, UnsafeMutablePointer<CGFloat>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetTrackThumbPositionFromBounds(_ inDrawInfo: ConstUnsafePointer<HIThemeTrackDrawInfo>, _ inThumbBounds: ConstUnsafePointer<HIRect>, _ outRelativePosition: UnsafePointer<CGFloat>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeGetTrackThumbPositionFromBounds(_ inDrawInfo: UnsafePointer<HIThemeTrackDrawInfo>, _ inThumbBounds: UnsafePointer<HIRect>, _ outRelativePosition: UnsafeMutablePointer<CGFloat>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeGetTrackThumbPositionFromOffset(UnsafePointer<HIThemeTrackDrawInfo>, UnsafePointer<HIPoint>, UnsafeMutablePointer<CGFloat>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetTrackThumbPositionFromOffset(_ inDrawInfo: ConstUnsafePointer<HIThemeTrackDrawInfo>, _ inThumbOffset: ConstUnsafePointer<HIPoint>, _ outRelativePosition: UnsafePointer<CGFloat>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeGetTrackThumbPositionFromOffset(_ inDrawInfo: UnsafePointer<HIThemeTrackDrawInfo>, _ inThumbOffset: UnsafePointer<HIPoint>, _ outRelativePosition: UnsafeMutablePointer<CGFloat>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeGetTrackThumbShape(UnsafePointer<HIThemeTrackDrawInfo>, UnsafeMutablePointer<Unmanaged<HIShape>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetTrackThumbShape(_ inDrawInfo: ConstUnsafePointer<HIThemeTrackDrawInfo>, _ outThumbShape: UnsafePointer<Unmanaged<HIShape>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeGetTrackThumbShape(_ inDrawInfo: UnsafePointer<HIThemeTrackDrawInfo>, _ outThumbShape: UnsafeMutablePointer<Unmanaged<HIShape>?>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeGetUIFontType(ThemeFontID) -> CTFontUIFontType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified HIThemeGetWindowRegionHit(UnsafePointer<HIRect>, UnsafePointer<HIThemeWindowDrawInfo>, UnsafePointer<HIPoint>, UnsafeMutablePointer<WindowRegionCode>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetWindowRegionHit(_ inContRect: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeWindowDrawInfo>, _ inPoint: ConstUnsafePointer<HIPoint>, _ outRegionHit: UnsafePointer<WindowRegionCode>) -> Boolean ``` | OS X 10.10 |
| To | ``` func HIThemeGetWindowRegionHit(_ inContRect: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeWindowDrawInfo>, _ inPoint: UnsafePointer<HIPoint>, _ outRegionHit: UnsafeMutablePointer<WindowRegionCode>) -> Boolean ``` | OS X 10.3 |

Modified HIThemeGetWindowShape(UnsafePointer<HIRect>, UnsafePointer<HIThemeWindowDrawInfo>, WindowRegionCode, UnsafeMutablePointer<Unmanaged<HIShape>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeGetWindowShape(_ inContRect: ConstUnsafePointer<HIRect>, _ inDrawInfo: ConstUnsafePointer<HIThemeWindowDrawInfo>, _ inWinRegion: WindowRegionCode, _ outShape: UnsafePointer<Unmanaged<HIShape>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeGetWindowShape(_ inContRect: UnsafePointer<HIRect>, _ inDrawInfo: UnsafePointer<HIThemeWindowDrawInfo>, _ inWinRegion: WindowRegionCode, _ outShape: UnsafeMutablePointer<Unmanaged<HIShape>?>) -> OSStatus ``` | OS X 10.3 |

Modified HIThemeGrabberDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemeGrabberDrawInfoPtr = UnsafePointer<HIThemeGrabberDrawInfo> ``` |
| To | ``` typealias HIThemeGrabberDrawInfoPtr = UnsafeMutablePointer<HIThemeGrabberDrawInfo> ``` |

Modified HIThemeGroupBoxDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemeGroupBoxDrawInfoPtr = UnsafePointer<HIThemeGroupBoxDrawInfo> ``` |
| To | ``` typealias HIThemeGroupBoxDrawInfoPtr = UnsafeMutablePointer<HIThemeGroupBoxDrawInfo> ``` |

Modified HIThemeGrowBoxDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemeGrowBoxDrawInfoPtr = UnsafePointer<HIThemeGrowBoxDrawInfo> ``` |
| To | ``` typealias HIThemeGrowBoxDrawInfoPtr = UnsafeMutablePointer<HIThemeGrowBoxDrawInfo> ``` |

Modified HIThemeHeaderDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemeHeaderDrawInfoPtr = UnsafePointer<HIThemeHeaderDrawInfo> ``` |
| To | ``` typealias HIThemeHeaderDrawInfoPtr = UnsafeMutablePointer<HIThemeHeaderDrawInfo> ``` |

Modified HIThemeHitTestScrollBarArrows(UnsafePointer<HIRect>, UnsafePointer<HIScrollBarTrackInfo>, Boolean, UnsafePointer<HIPoint>, UnsafeMutablePointer<HIRect>, UnsafeMutablePointer<ControlPartCode>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeHitTestScrollBarArrows(_ inScrollBarBounds: ConstUnsafePointer<HIRect>, _ inTrackInfo: ConstUnsafePointer<HIScrollBarTrackInfo>, _ inIsHoriz: Boolean, _ inPtHit: ConstUnsafePointer<HIPoint>, _ outTrackBounds: UnsafePointer<HIRect>, _ outPartCode: UnsafePointer<ControlPartCode>) -> Boolean ``` | OS X 10.10 |
| To | ``` func HIThemeHitTestScrollBarArrows(_ inScrollBarBounds: UnsafePointer<HIRect>, _ inTrackInfo: UnsafePointer<HIScrollBarTrackInfo>, _ inIsHoriz: Boolean, _ inPtHit: UnsafePointer<HIPoint>, _ outTrackBounds: UnsafeMutablePointer<HIRect>, _ outPartCode: UnsafeMutablePointer<ControlPartCode>) -> Boolean ``` | OS X 10.3 |

Modified HIThemeHitTestTrack(UnsafePointer<HIThemeTrackDrawInfo>, UnsafePointer<HIPoint>, UnsafeMutablePointer<ControlPartCode>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeHitTestTrack(_ inDrawInfo: ConstUnsafePointer<HIThemeTrackDrawInfo>, _ inMousePoint: ConstUnsafePointer<HIPoint>, _ outPartHit: UnsafePointer<ControlPartCode>) -> Boolean ``` | OS X 10.10 |
| To | ``` func HIThemeHitTestTrack(_ inDrawInfo: UnsafePointer<HIThemeTrackDrawInfo>, _ inMousePoint: UnsafePointer<HIPoint>, _ outPartHit: UnsafeMutablePointer<ControlPartCode>) -> Boolean ``` | OS X 10.3 |

Modified HIThemeMenuBarDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemeMenuBarDrawInfoPtr = UnsafePointer<HIThemeMenuBarDrawInfo> ``` |
| To | ``` typealias HIThemeMenuBarDrawInfoPtr = UnsafeMutablePointer<HIThemeMenuBarDrawInfo> ``` |

Modified HIThemeMenuDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemeMenuDrawInfoPtr = UnsafePointer<HIThemeMenuDrawInfo> ``` |
| To | ``` typealias HIThemeMenuDrawInfoPtr = UnsafeMutablePointer<HIThemeMenuDrawInfo> ``` |

Modified HIThemeMenuDrawInfoVersionZeroPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemeMenuDrawInfoVersionZeroPtr = UnsafePointer<HIThemeMenuDrawInfoVersionZero> ``` |
| To | ``` typealias HIThemeMenuDrawInfoVersionZeroPtr = UnsafeMutablePointer<HIThemeMenuDrawInfoVersionZero> ``` |

Modified HIThemeMenuItemDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemeMenuItemDrawInfoPtr = UnsafePointer<HIThemeMenuItemDrawInfo> ``` |
| To | ``` typealias HIThemeMenuItemDrawInfoPtr = UnsafeMutablePointer<HIThemeMenuItemDrawInfo> ``` |

Modified HIThemeMenuTitleDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemeMenuTitleDrawInfoPtr = UnsafePointer<HIThemeMenuTitleDrawInfo> ``` |
| To | ``` typealias HIThemeMenuTitleDrawInfoPtr = UnsafeMutablePointer<HIThemeMenuTitleDrawInfo> ``` |

Modified HIThemePlacardDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemePlacardDrawInfoPtr = UnsafePointer<HIThemePlacardDrawInfo> ``` |
| To | ``` typealias HIThemePlacardDrawInfoPtr = UnsafeMutablePointer<HIThemePlacardDrawInfo> ``` |

Modified HIThemePopupArrowDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemePopupArrowDrawInfoPtr = UnsafePointer<HIThemePopupArrowDrawInfo> ``` |
| To | ``` typealias HIThemePopupArrowDrawInfoPtr = UnsafeMutablePointer<HIThemePopupArrowDrawInfo> ``` |

Modified HIThemeScrollBarDelimitersDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemeScrollBarDelimitersDrawInfoPtr = UnsafePointer<HIThemeScrollBarDelimitersDrawInfo> ``` |
| To | ``` typealias HIThemeScrollBarDelimitersDrawInfoPtr = UnsafeMutablePointer<HIThemeScrollBarDelimitersDrawInfo> ``` |

Modified HIThemeSegmentDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemeSegmentDrawInfoPtr = UnsafePointer<HIThemeSegmentDrawInfo> ``` |
| To | ``` typealias HIThemeSegmentDrawInfoPtr = UnsafeMutablePointer<HIThemeSegmentDrawInfo> ``` |

Modified HIThemeSeparatorDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemeSeparatorDrawInfoPtr = UnsafePointer<HIThemeSeparatorDrawInfo> ``` |
| To | ``` typealias HIThemeSeparatorDrawInfoPtr = UnsafeMutablePointer<HIThemeSeparatorDrawInfo> ``` |

Modified HIThemeSetFill(ThemeBrush, UnsafeMutablePointer<Void>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeSetFill(_ inBrush: ThemeBrush, _ inInfo: UnsafePointer<()>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeSetFill(_ inBrush: ThemeBrush, _ inInfo: UnsafeMutablePointer<Void>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.4 |

Modified HIThemeSetStroke(ThemeBrush, UnsafeMutablePointer<Void>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeSetStroke(_ inBrush: ThemeBrush, _ inInfo: UnsafePointer<()>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeSetStroke(_ inBrush: ThemeBrush, _ inInfo: UnsafeMutablePointer<Void>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.4 |

Modified HIThemeSetTextFill(ThemeTextColor, UnsafeMutablePointer<Void>, CGContext!, HIThemeOrientation) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIThemeSetTextFill(_ inColor: ThemeTextColor, _ inInfo: UnsafePointer<()>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIThemeSetTextFill(_ inColor: ThemeTextColor, _ inInfo: UnsafeMutablePointer<Void>, _ inContext: CGContext!, _ inOrientation: HIThemeOrientation) -> OSStatus ``` | OS X 10.4 |

Modified HIThemeSplitterDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemeSplitterDrawInfoPtr = UnsafePointer<HIThemeSplitterDrawInfo> ``` |
| To | ``` typealias HIThemeSplitterDrawInfoPtr = UnsafeMutablePointer<HIThemeSplitterDrawInfo> ``` |

Modified HIThemeTickMarkDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemeTickMarkDrawInfoPtr = UnsafePointer<HIThemeTickMarkDrawInfo> ``` |
| To | ``` typealias HIThemeTickMarkDrawInfoPtr = UnsafeMutablePointer<HIThemeTickMarkDrawInfo> ``` |

Modified HIThemeWindowDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemeWindowDrawInfoPtr = UnsafePointer<HIThemeWindowDrawInfo> ``` |
| To | ``` typealias HIThemeWindowDrawInfoPtr = UnsafeMutablePointer<HIThemeWindowDrawInfo> ``` |

Modified HIThemeWindowWidgetDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIThemeWindowWidgetDrawInfoPtr = UnsafePointer<HIThemeWindowWidgetDrawInfo> ``` |
| To | ``` typealias HIThemeWindowWidgetDrawInfoPtr = UnsafeMutablePointer<HIThemeWindowWidgetDrawInfo> ``` |

Modified HIViewContentInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIViewContentInfoPtr = UnsafePointer<HIViewContentInfo> ``` |
| To | ``` typealias HIViewContentInfoPtr = UnsafeMutablePointer<HIViewContentInfo> ``` |

Modified HIViewTrackingAreaRef

|  | Declaration |
| --- | --- |
| From | ``` typealias HIViewTrackingAreaRef = HIViewTrackingArea ``` |
| To | ``` typealias HIViewTrackingAreaRef = COpaquePointer ``` |

Modified HIWindowRef

|  | Declaration |
| --- | --- |
| From | ``` typealias HIWindowRef = HIWindow ``` |
| To | ``` typealias HIWindowRef = WindowRef ``` |

Modified HMControlContentProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HMControlContentProcPtr = CFunctionPointer<((Control!, Point, HMContentRequest, UnsafePointer<HMContentProvidedType>, UnsafePointer<HMHelpContentRec>) -> OSStatus)> ``` |
| To | ``` typealias HMControlContentProcPtr = CFunctionPointer<((Control!, Point, HMContentRequest, UnsafeMutablePointer<HMContentProvidedType>, UnsafeMutablePointer<HMHelpContentRec>) -> OSStatus)> ``` |

Modified HMHelpContentPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HMHelpContentPtr = UnsafePointer<HMHelpContentRec> ``` |
| To | ``` typealias HMHelpContentPtr = UnsafeMutablePointer<HMHelpContentRec> ``` |

Modified HMMenuItemContentProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HMMenuItemContentProcPtr = CFunctionPointer<((ConstUnsafePointer<MenuTrackingData>, HMContentRequest, UnsafePointer<HMContentProvidedType>, UnsafePointer<HMHelpContentRec>) -> OSStatus)> ``` |
| To | ``` typealias HMMenuItemContentProcPtr = CFunctionPointer<((UnsafePointer<MenuTrackingData>, HMContentRequest, UnsafeMutablePointer<HMContentProvidedType>, UnsafeMutablePointer<HMHelpContentRec>) -> OSStatus)> ``` |

Modified HMMenuTitleContentProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HMMenuTitleContentProcPtr = CFunctionPointer<((Menu!, HMContentRequest, UnsafePointer<HMContentProvidedType>, UnsafePointer<HMHelpContentRec>) -> OSStatus)> ``` |
| To | ``` typealias HMMenuTitleContentProcPtr = CFunctionPointer<((Menu!, HMContentRequest, UnsafeMutablePointer<HMContentProvidedType>, UnsafeMutablePointer<HMHelpContentRec>) -> OSStatus)> ``` |

Modified HMWindowContentProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HMWindowContentProcPtr = CFunctionPointer<((Window!, Point, HMContentRequest, UnsafePointer<HMContentProvidedType>, UnsafePointer<HMHelpContentRec>) -> OSStatus)> ``` |
| To | ``` typealias HMWindowContentProcPtr = CFunctionPointer<((WindowRef, Point, HMContentRequest, UnsafeMutablePointer<HMContentProvidedType>, UnsafeMutablePointer<HMHelpContentRec>) -> OSStatus)> ``` |

Modified HighHookProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HighHookProcPtr = CFunctionPointer<((ConstUnsafePointer<Rect>, TEPtr) -> Void)> ``` |
| To | ``` typealias HighHookProcPtr = CFunctionPointer<((UnsafePointer<Rect>, TEPtr) -> Void)> ``` |

Modified HitTestHookProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HitTestHookProcPtr = CFunctionPointer<((UInt16, UInt16, UInt16, UnsafePointer<()>, TEPtr, TEHandle, UnsafePointer<UInt16>, UnsafePointer<UInt16>, UnsafePointer<Boolean>) -> Boolean)> ``` |
| To | ``` typealias HitTestHookProcPtr = CFunctionPointer<((UInt16, UInt16, UInt16, UnsafeMutablePointer<Void>, TEPtr, TEHandle, UnsafeMutablePointer<UInt16>, UnsafeMutablePointer<UInt16>, UnsafeMutablePointer<Boolean>) -> Boolean)> ``` |

Modified IBNibRef

|  | Declaration |
| --- | --- |
| From | ``` typealias IBNibRef = IBNib ``` |
| To | ``` typealias IBNibRef = COpaquePointer ``` |

Modified ICACompletion

|  | Declaration |
| --- | --- |
| From | ``` typealias ICACompletion = CFunctionPointer<((UnsafePointer<ICAHeader>) -> Void)> ``` |
| To | ``` typealias ICACompletion = CFunctionPointer<((UnsafeMutablePointer<ICAHeader>) -> Void)> ``` |

Modified ICDCompletion

|  | Declaration |
| --- | --- |
| From | ``` typealias ICDCompletion = CFunctionPointer<((UnsafePointer<ICDHeader>) -> Void)> ``` |
| To | ``` typealias ICDCompletion = CFunctionPointer<((UnsafeMutablePointer<ICDHeader>) -> Void)> ``` |

Modified IMKTextOrientationName

|  | Declaration |
| --- | --- |
| From | ``` var IMKTextOrientationName: NSString! ``` |
| To | ``` let IMKTextOrientationName: String ``` |

Modified IndicatorDragConstraintPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias IndicatorDragConstraintPtr = UnsafePointer<IndicatorDragConstraint> ``` |
| To | ``` typealias IndicatorDragConstraintPtr = UnsafeMutablePointer<IndicatorDragConstraint> ``` |

Modified InkAddStrokeToCurrentPhrase(UInt, UnsafeMutablePointer<InkPoint>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InkAddStrokeToCurrentPhrase(_ iPointCount: UInt, _ iPointArray: UnsafePointer<InkPoint>) ``` | OS X 10.10 |
| To | ``` func InkAddStrokeToCurrentPhrase(_ iPointCount: UInt, _ iPointArray: UnsafeMutablePointer<InkPoint>) ``` | OS X 10.3 |

Modified InkIsPhraseInProgress() -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified InkPointPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias InkPointPtr = UnsafePointer<InkPoint> ``` |
| To | ``` typealias InkPointPtr = UnsafeMutablePointer<InkPoint> ``` |

Modified InkSetApplicationRecognitionMode(InkRecognitionType)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified InkSetApplicationWritingMode(InkApplicationWritingModeType)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified InkSetDrawingMode(InkDrawingModeType)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified InkSetPhraseTerminationMode(InkSourceType, InkTerminationType)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified InkStrokeGetPointCount(InkStroke!) -> CFIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified InkStrokeGetPoints(InkStroke!, UnsafeMutablePointer<InkPoint>) -> UnsafeMutablePointer<InkPoint>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InkStrokeGetPoints(_ iStrokeRef: InkStroke!, _ oPointBuffer: UnsafePointer<InkPoint>) -> UnsafePointer<InkPoint> ``` | OS X 10.10 |
| To | ``` func InkStrokeGetPoints(_ iStrokeRef: InkStroke!, _ oPointBuffer: UnsafeMutablePointer<InkPoint>) -> UnsafeMutablePointer<InkPoint> ``` | OS X 10.4 |

Modified InkStrokeGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified InkTerminateCurrentPhrase(InkSourceType)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified InkTextAlternatesCount(InkText!) -> CFIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified InkTextBounds(InkText!) -> HIRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified InkTextCopy(InkText!) -> Unmanaged<InkText>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified InkTextCreateCFString(InkText!, CFIndex) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified InkTextCreateFromCFData(CFData!, CFIndex) -> Unmanaged<InkText>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified InkTextDraw(InkText!, CGContext!, UnsafePointer<CGRect>, InkTextDrawFlagsType)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InkTextDraw(_ iTextRef: InkText!, _ iContext: CGContext!, _ iBounds: ConstUnsafePointer<CGRect>, _ iFlags: InkTextDrawFlagsType) ``` | OS X 10.10 |
| To | ``` func InkTextDraw(_ iTextRef: InkText!, _ iContext: CGContext!, _ iBounds: UnsafePointer<CGRect>, _ iFlags: InkTextDrawFlagsType) ``` | OS X 10.3 |

Modified InkTextFlatten(InkText!, CFMutableData!, CFIndex) -> CFIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified InkTextGetStroke(InkText!, CFIndex) -> Unmanaged<InkStroke>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified InkTextGetStrokeCount(InkText!) -> CFIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified InkTextGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified InkTextKeyModifiers(InkText!) -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified InkUserWritingMode() -> InkUserWritingModeType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified InstallEventHandler(EventTargetRef, EventHandlerUPP, Int, UnsafePointer<EventTypeSpec>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<EventHandlerRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InstallEventHandler(_ inTarget: EventTarget!, _ inHandler: EventHandlerUPP, _ inNumTypes: ItemCount, _ inList: ConstUnsafePointer<EventTypeSpec>, _ inUserData: UnsafePointer<()>, _ outRef: UnsafePointer<Unmanaged<EventHandler>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func InstallEventHandler(_ inTarget: EventTargetRef, _ inHandler: EventHandlerUPP, _ inNumTypes: Int, _ inList: UnsafePointer<EventTypeSpec>, _ inUserData: UnsafeMutablePointer<Void>, _ outRef: UnsafeMutablePointer<EventHandlerRef>) -> OSStatus ``` | OS X 10.10.3 |

Modified InstallEventLoopTimer(EventLoopRef, EventTimerInterval, EventTimerInterval, EventLoopTimerUPP, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Unmanaged<EventLoopTimer>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InstallEventLoopTimer(_ inEventLoop: EventLoop!, _ inFireDelay: EventTimerInterval, _ inInterval: EventTimerInterval, _ inTimerProc: EventLoopTimerUPP, _ inTimerData: UnsafePointer<()>, _ outTimer: UnsafePointer<Unmanaged<EventLoopTimer>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func InstallEventLoopTimer(_ inEventLoop: EventLoopRef, _ inFireDelay: EventTimerInterval, _ inInterval: EventTimerInterval, _ inTimerProc: EventLoopTimerUPP, _ inTimerData: UnsafeMutablePointer<Void>, _ outTimer: UnsafeMutablePointer<Unmanaged<EventLoopTimer>?>) -> OSStatus ``` | OS X 10.10.3 |

Modified InvokeAEFilterUPP(UnsafeMutablePointer<EventRecord>, Int32, AETransactionID, UnsafePointer<AEAddressDesc>, AEFilterUPP) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func InvokeAEFilterUPP(_ theEvent: UnsafePointer<EventRecord>, _ returnID: Int32, _ transactionID: AETransactionID, _ sender: ConstUnsafePointer<AEAddressDesc>, _ userUPP: AEFilterUPP) -> Boolean ``` |
| To | ``` func InvokeAEFilterUPP(_ theEvent: UnsafeMutablePointer<EventRecord>, _ returnID: Int32, _ transactionID: AETransactionID, _ sender: UnsafePointer<AEAddressDesc>, _ userUPP: AEFilterUPP) -> Boolean ``` |

Modified InvokeAEIdleUPP(UnsafeMutablePointer<EventRecord>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<RgnHandle>, AEIdleUPP) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func InvokeAEIdleUPP(_ theEvent: UnsafePointer<EventRecord>, _ sleepTime: UnsafePointer<Int32>, _ mouseRgn: UnsafePointer<RgnHandle>, _ userUPP: AEIdleUPP) -> Boolean ``` |
| To | ``` func InvokeAEIdleUPP(_ theEvent: UnsafeMutablePointer<EventRecord>, _ sleepTime: UnsafeMutablePointer<Int32>, _ mouseRgn: UnsafeMutablePointer<RgnHandle>, _ userUPP: AEIdleUPP) -> Boolean ``` |

Modified InvokeCalibrateEventUPP(UnsafeMutablePointer<EventRecord>, CalibrateEventUPP)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeCalibrateEventUPP(_ event: UnsafePointer<EventRecord>, _ userUPP: CalibrateEventUPP) ``` |
| To | ``` func InvokeCalibrateEventUPP(_ event: UnsafeMutablePointer<EventRecord>, _ userUPP: CalibrateEventUPP) ``` |

Modified InvokeCalibrateUPP(UnsafeMutablePointer<CalibratorInfo>, CalibrateUPP) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func InvokeCalibrateUPP(_ theInfo: UnsafePointer<CalibratorInfo>, _ userUPP: CalibrateUPP) -> OSErr ``` |
| To | ``` func InvokeCalibrateUPP(_ theInfo: UnsafeMutablePointer<CalibratorInfo>, _ userUPP: CalibrateUPP) -> OSErr ``` |

Modified InvokeCanCalibrateUPP(CMDisplayIDType, UnsafeMutablePointer<UInt8>, CanCalibrateUPP) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func InvokeCanCalibrateUPP(_ displayID: CMDisplayIDType, _ errMessage: UnsafePointer<UInt8>, _ userUPP: CanCalibrateUPP) -> Boolean ``` |
| To | ``` func InvokeCanCalibrateUPP(_ displayID: CMDisplayIDType, _ errMessage: UnsafeMutablePointer<UInt8>, _ userUPP: CanCalibrateUPP) -> Boolean ``` |

Modified InvokeControlKeyFilterUPP(Control!, UnsafeMutablePointer<Int16>, UnsafeMutablePointer<Int16>, UnsafeMutablePointer<EventModifiers>, ControlKeyFilterUPP) -> ControlKeyFilterResult

|  | Declaration |
| --- | --- |
| From | ``` func InvokeControlKeyFilterUPP(_ theControl: Control!, _ keyCode: UnsafePointer<Int16>, _ charCode: UnsafePointer<Int16>, _ modifiers: UnsafePointer<EventModifiers>, _ userUPP: ControlKeyFilterUPP) -> ControlKeyFilterResult ``` |
| To | ``` func InvokeControlKeyFilterUPP(_ theControl: Control!, _ keyCode: UnsafeMutablePointer<Int16>, _ charCode: UnsafeMutablePointer<Int16>, _ modifiers: UnsafeMutablePointer<EventModifiers>, _ userUPP: ControlKeyFilterUPP) -> ControlKeyFilterResult ``` |

Modified InvokeDataBrowserAcceptDragUPP(Control!, DragReference, DataBrowserItemID, DataBrowserAcceptDragUPP) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeDataBrowserAcceptDragUPP(_ browser: Control!, _ theDrag: DragReference!, _ item: DataBrowserItemID, _ userUPP: DataBrowserAcceptDragUPP) -> Boolean ``` | OS X 10.10 |
| To | ``` func InvokeDataBrowserAcceptDragUPP(_ browser: Control!, _ theDrag: DragReference, _ item: DataBrowserItemID, _ userUPP: DataBrowserAcceptDragUPP) -> Boolean ``` | OS X 10.10.3 |

Modified InvokeDataBrowserAddDragItemUPP(Control!, DragReference, DataBrowserItemID, UnsafeMutablePointer<ItemReference>, DataBrowserAddDragItemUPP) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeDataBrowserAddDragItemUPP(_ browser: Control!, _ theDrag: DragReference!, _ item: DataBrowserItemID, _ itemRef: UnsafePointer<ItemReference>, _ userUPP: DataBrowserAddDragItemUPP) -> Boolean ``` | OS X 10.10 |
| To | ``` func InvokeDataBrowserAddDragItemUPP(_ browser: Control!, _ theDrag: DragReference, _ item: DataBrowserItemID, _ itemRef: UnsafeMutablePointer<ItemReference>, _ userUPP: DataBrowserAddDragItemUPP) -> Boolean ``` | OS X 10.10.3 |

Modified InvokeDataBrowserDrawItemUPP(Control!, DataBrowserItemID, DataBrowserPropertyID, DataBrowserItemState, UnsafePointer<Rect>, Int16, Boolean, DataBrowserDrawItemUPP)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeDataBrowserDrawItemUPP(_ browser: Control!, _ item: DataBrowserItemID, _ property: DataBrowserPropertyID, _ itemState: DataBrowserItemState, _ theRect: ConstUnsafePointer<Rect>, _ gdDepth: Int16, _ colorDevice: Boolean, _ userUPP: DataBrowserDrawItemUPP) ``` | OS X 10.10 |
| To | ``` func InvokeDataBrowserDrawItemUPP(_ browser: Control!, _ item: DataBrowserItemID, _ property: DataBrowserPropertyID, _ itemState: DataBrowserItemState, _ theRect: UnsafePointer<Rect>, _ gdDepth: Int16, _ colorDevice: Boolean, _ userUPP: DataBrowserDrawItemUPP) ``` | OS X 10.1 |

Modified InvokeDataBrowserEditItemUPP(Control!, DataBrowserItemID, DataBrowserPropertyID, CFString!, UnsafeMutablePointer<Rect>, UnsafeMutablePointer<Boolean>, DataBrowserEditItemUPP) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeDataBrowserEditItemUPP(_ browser: Control!, _ item: DataBrowserItemID, _ property: DataBrowserPropertyID, _ theString: CFString!, _ maxEditTextRect: UnsafePointer<Rect>, _ shrinkToFit: UnsafePointer<Boolean>, _ userUPP: DataBrowserEditItemUPP) -> Boolean ``` | OS X 10.10 |
| To | ``` func InvokeDataBrowserEditItemUPP(_ browser: Control!, _ item: DataBrowserItemID, _ property: DataBrowserPropertyID, _ theString: CFString!, _ maxEditTextRect: UnsafeMutablePointer<Rect>, _ shrinkToFit: UnsafeMutablePointer<Boolean>, _ userUPP: DataBrowserEditItemUPP) -> Boolean ``` | OS X 10.1 |

Modified InvokeDataBrowserGetContextualMenuUPP(Control!, UnsafeMutablePointer<Unmanaged<Menu>?>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Unmanaged<CFString>?>, UnsafeMutablePointer<AEDesc>, DataBrowserGetContextualMenuUPP)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeDataBrowserGetContextualMenuUPP(_ browser: Control!, _ menu: UnsafePointer<Unmanaged<Menu>?>, _ helpType: UnsafePointer<UInt32>, _ helpItemString: UnsafePointer<Unmanaged<CFString>?>, _ selection: UnsafePointer<AEDesc>, _ userUPP: DataBrowserGetContextualMenuUPP) ``` |
| To | ``` func InvokeDataBrowserGetContextualMenuUPP(_ browser: Control!, _ menu: UnsafeMutablePointer<Unmanaged<Menu>?>, _ helpType: UnsafeMutablePointer<UInt32>, _ helpItemString: UnsafeMutablePointer<Unmanaged<CFString>?>, _ selection: UnsafeMutablePointer<AEDesc>, _ userUPP: DataBrowserGetContextualMenuUPP) ``` |

Modified InvokeDataBrowserHitTestUPP(Control!, DataBrowserItemID, DataBrowserPropertyID, UnsafePointer<Rect>, UnsafePointer<Rect>, DataBrowserHitTestUPP) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeDataBrowserHitTestUPP(_ browser: Control!, _ itemID: DataBrowserItemID, _ property: DataBrowserPropertyID, _ theRect: ConstUnsafePointer<Rect>, _ mouseRect: ConstUnsafePointer<Rect>, _ userUPP: DataBrowserHitTestUPP) -> Boolean ``` | OS X 10.10 |
| To | ``` func InvokeDataBrowserHitTestUPP(_ browser: Control!, _ itemID: DataBrowserItemID, _ property: DataBrowserPropertyID, _ theRect: UnsafePointer<Rect>, _ mouseRect: UnsafePointer<Rect>, _ userUPP: DataBrowserHitTestUPP) -> Boolean ``` | OS X 10.1 |

Modified InvokeDataBrowserItemAcceptDragUPP(Control!, DataBrowserItemID, DataBrowserPropertyID, UnsafePointer<Rect>, DragReference, DataBrowserItemAcceptDragUPP) -> DataBrowserDragFlags

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeDataBrowserItemAcceptDragUPP(_ browser: Control!, _ itemID: DataBrowserItemID, _ property: DataBrowserPropertyID, _ theRect: ConstUnsafePointer<Rect>, _ theDrag: DragReference!, _ userUPP: DataBrowserItemAcceptDragUPP) -> DataBrowserDragFlags ``` | OS X 10.10 |
| To | ``` func InvokeDataBrowserItemAcceptDragUPP(_ browser: Control!, _ itemID: DataBrowserItemID, _ property: DataBrowserPropertyID, _ theRect: UnsafePointer<Rect>, _ theDrag: DragReference, _ userUPP: DataBrowserItemAcceptDragUPP) -> DataBrowserDragFlags ``` | OS X 10.1 |

Modified InvokeDataBrowserItemDragRgnUPP(Control!, DataBrowserItemID, DataBrowserPropertyID, UnsafePointer<Rect>, RgnHandle, DataBrowserItemDragRgnUPP)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeDataBrowserItemDragRgnUPP(_ browser: Control!, _ itemID: DataBrowserItemID, _ property: DataBrowserPropertyID, _ theRect: ConstUnsafePointer<Rect>, _ dragRgn: RgnHandle, _ userUPP: DataBrowserItemDragRgnUPP) ``` | OS X 10.10 |
| To | ``` func InvokeDataBrowserItemDragRgnUPP(_ browser: Control!, _ itemID: DataBrowserItemID, _ property: DataBrowserPropertyID, _ theRect: UnsafePointer<Rect>, _ dragRgn: RgnHandle, _ userUPP: DataBrowserItemDragRgnUPP) ``` | OS X 10.1 |

Modified InvokeDataBrowserItemHelpContentUPP(Control!, DataBrowserItemID, DataBrowserPropertyID, HMContentRequest, UnsafeMutablePointer<HMContentProvidedType>, UnsafeMutablePointer<HMHelpContentRec>, DataBrowserItemHelpContentUPP)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeDataBrowserItemHelpContentUPP(_ browser: Control!, _ item: DataBrowserItemID, _ property: DataBrowserPropertyID, _ inRequest: HMContentRequest, _ outContentProvided: UnsafePointer<HMContentProvidedType>, _ ioHelpContent: UnsafePointer<HMHelpContentRec>, _ userUPP: DataBrowserItemHelpContentUPP) ``` |
| To | ``` func InvokeDataBrowserItemHelpContentUPP(_ browser: Control!, _ item: DataBrowserItemID, _ property: DataBrowserPropertyID, _ inRequest: HMContentRequest, _ outContentProvided: UnsafeMutablePointer<HMContentProvidedType>, _ ioHelpContent: UnsafeMutablePointer<HMHelpContentRec>, _ userUPP: DataBrowserItemHelpContentUPP) ``` |

Modified InvokeDataBrowserItemNotificationWithItemUPP(Control!, DataBrowserItemID, DataBrowserItemNotification, DataBrowserItemDataRef, DataBrowserItemNotificationWithItemUPP)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified InvokeDataBrowserItemReceiveDragUPP(Control!, DataBrowserItemID, DataBrowserPropertyID, DataBrowserDragFlags, DragReference, DataBrowserItemReceiveDragUPP) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeDataBrowserItemReceiveDragUPP(_ browser: Control!, _ itemID: DataBrowserItemID, _ property: DataBrowserPropertyID, _ dragFlags: DataBrowserDragFlags, _ theDrag: DragReference!, _ userUPP: DataBrowserItemReceiveDragUPP) -> Boolean ``` | OS X 10.10 |
| To | ``` func InvokeDataBrowserItemReceiveDragUPP(_ browser: Control!, _ itemID: DataBrowserItemID, _ property: DataBrowserPropertyID, _ dragFlags: DataBrowserDragFlags, _ theDrag: DragReference, _ userUPP: DataBrowserItemReceiveDragUPP) -> Boolean ``` | OS X 10.1 |

Modified InvokeDataBrowserItemUPP(DataBrowserItemID, DataBrowserItemState, UnsafeMutablePointer<Void>, DataBrowserItemUPP)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeDataBrowserItemUPP(_ item: DataBrowserItemID, _ state: DataBrowserItemState, _ clientData: UnsafePointer<()>, _ userUPP: DataBrowserItemUPP) ``` |
| To | ``` func InvokeDataBrowserItemUPP(_ item: DataBrowserItemID, _ state: DataBrowserItemState, _ clientData: UnsafeMutablePointer<Void>, _ userUPP: DataBrowserItemUPP) ``` |

Modified InvokeDataBrowserPostProcessDragUPP(Control!, DragReference, OSStatus, DataBrowserPostProcessDragUPP)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeDataBrowserPostProcessDragUPP(_ browser: Control!, _ theDrag: DragReference!, _ trackDragResult: OSStatus, _ userUPP: DataBrowserPostProcessDragUPP) ``` | OS X 10.10 |
| To | ``` func InvokeDataBrowserPostProcessDragUPP(_ browser: Control!, _ theDrag: DragReference, _ trackDragResult: OSStatus, _ userUPP: DataBrowserPostProcessDragUPP) ``` | OS X 10.10.3 |

Modified InvokeDataBrowserReceiveDragUPP(Control!, DragReference, DataBrowserItemID, DataBrowserReceiveDragUPP) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeDataBrowserReceiveDragUPP(_ browser: Control!, _ theDrag: DragReference!, _ item: DataBrowserItemID, _ userUPP: DataBrowserReceiveDragUPP) -> Boolean ``` | OS X 10.10 |
| To | ``` func InvokeDataBrowserReceiveDragUPP(_ browser: Control!, _ theDrag: DragReference, _ item: DataBrowserItemID, _ userUPP: DataBrowserReceiveDragUPP) -> Boolean ``` | OS X 10.10.3 |

Modified InvokeDataBrowserTrackingUPP(Control!, DataBrowserItemID, DataBrowserPropertyID, UnsafePointer<Rect>, Point, EventModifiers, DataBrowserTrackingUPP) -> DataBrowserTrackingResult

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeDataBrowserTrackingUPP(_ browser: Control!, _ itemID: DataBrowserItemID, _ property: DataBrowserPropertyID, _ theRect: ConstUnsafePointer<Rect>, _ startPt: Point, _ modifiers: EventModifiers, _ userUPP: DataBrowserTrackingUPP) -> DataBrowserTrackingResult ``` | OS X 10.10 |
| To | ``` func InvokeDataBrowserTrackingUPP(_ browser: Control!, _ itemID: DataBrowserItemID, _ property: DataBrowserPropertyID, _ theRect: UnsafePointer<Rect>, _ startPt: Point, _ modifiers: EventModifiers, _ userUPP: DataBrowserTrackingUPP) -> DataBrowserTrackingResult ``` | OS X 10.1 |

Modified InvokeDragInputUPP(UnsafeMutablePointer<Point>, UnsafeMutablePointer<Int16>, UnsafeMutablePointer<Void>, DragRef, DragInputUPP) -> OSErr

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeDragInputUPP(_ mouse: UnsafePointer<Point>, _ modifiers: UnsafePointer<Int16>, _ dragInputRefCon: UnsafePointer<()>, _ theDrag: Drag!, _ userUPP: DragInputUPP) -> OSErr ``` | OS X 10.10 |
| To | ``` func InvokeDragInputUPP(_ mouse: UnsafeMutablePointer<Point>, _ modifiers: UnsafeMutablePointer<Int16>, _ dragInputRefCon: UnsafeMutablePointer<Void>, _ theDrag: DragRef, _ userUPP: DragInputUPP) -> OSErr ``` | OS X 10.10.3 |

Modified InvokeEditUnicodePostUpdateUPP(UniCharArrayHandle, Int, UniCharArrayOffset, UniCharArrayOffset, UnsafeMutablePointer<Void>, EditUnicodePostUpdateUPP) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeEditUnicodePostUpdateUPP(_ uniText: UniCharArrayHandle, _ uniTextLength: UniCharCount, _ iStartOffset: UniCharArrayOffset, _ iEndOffset: UniCharArrayOffset, _ refcon: UnsafePointer<()>, _ userUPP: EditUnicodePostUpdateUPP) -> Boolean ``` | OS X 10.10 |
| To | ``` func InvokeEditUnicodePostUpdateUPP(_ uniText: UniCharArrayHandle, _ uniTextLength: Int, _ iStartOffset: UniCharArrayOffset, _ iEndOffset: UniCharArrayOffset, _ refcon: UnsafeMutablePointer<Void>, _ userUPP: EditUnicodePostUpdateUPP) -> Boolean ``` | OS X 10.10.3 |

Modified InvokeEventComparatorUPP(EventRef, UnsafeMutablePointer<Void>, EventComparatorUPP) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeEventComparatorUPP(_ inEvent: Event!, _ inCompareData: UnsafePointer<()>, _ userUPP: EventComparatorUPP) -> Boolean ``` | OS X 10.10 |
| To | ``` func InvokeEventComparatorUPP(_ inEvent: EventRef, _ inCompareData: UnsafeMutablePointer<Void>, _ userUPP: EventComparatorUPP) -> Boolean ``` | OS X 10.10.3 |

Modified InvokeEventHandlerUPP(EventHandlerCallRef, EventRef, UnsafeMutablePointer<Void>, EventHandlerUPP) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeEventHandlerUPP(_ inHandlerCallRef: EventHandlerCall!, _ inEvent: Event!, _ inUserData: UnsafePointer<()>, _ userUPP: EventHandlerUPP) -> OSStatus ``` | OS X 10.10 |
| To | ``` func InvokeEventHandlerUPP(_ inHandlerCallRef: EventHandlerCallRef, _ inEvent: EventRef, _ inUserData: UnsafeMutablePointer<Void>, _ userUPP: EventHandlerUPP) -> OSStatus ``` | OS X 10.10.3 |

Modified InvokeEventLoopIdleTimerUPP(EventLoopTimer!, EventLoopIdleTimerMessage, UnsafeMutablePointer<Void>, EventLoopIdleTimerUPP)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeEventLoopIdleTimerUPP(_ inTimer: EventLoopTimer!, _ inState: EventLoopIdleTimerMessage, _ inUserData: UnsafePointer<()>, _ userUPP: EventLoopIdleTimerUPP) ``` | OS X 10.10 |
| To | ``` func InvokeEventLoopIdleTimerUPP(_ inTimer: EventLoopTimer!, _ inState: EventLoopIdleTimerMessage, _ inUserData: UnsafeMutablePointer<Void>, _ userUPP: EventLoopIdleTimerUPP) ``` | OS X 10.2 |

Modified InvokeEventLoopTimerUPP(EventLoopTimer!, UnsafeMutablePointer<Void>, EventLoopTimerUPP)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeEventLoopTimerUPP(_ inTimer: EventLoopTimer!, _ inUserData: UnsafePointer<()>, _ userUPP: EventLoopTimerUPP) ``` |
| To | ``` func InvokeEventLoopTimerUPP(_ inTimer: EventLoopTimer!, _ inUserData: UnsafeMutablePointer<Void>, _ userUPP: EventLoopTimerUPP) ``` |

Modified InvokeHMControlContentUPP(Control!, Point, HMContentRequest, UnsafeMutablePointer<HMContentProvidedType>, UnsafeMutablePointer<HMHelpContentRec>, HMControlContentUPP) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func InvokeHMControlContentUPP(_ inControl: Control!, _ inGlobalMouse: Point, _ inRequest: HMContentRequest, _ outContentProvided: UnsafePointer<HMContentProvidedType>, _ ioHelpContent: UnsafePointer<HMHelpContentRec>, _ userUPP: HMControlContentUPP) -> OSStatus ``` |
| To | ``` func InvokeHMControlContentUPP(_ inControl: Control!, _ inGlobalMouse: Point, _ inRequest: HMContentRequest, _ outContentProvided: UnsafeMutablePointer<HMContentProvidedType>, _ ioHelpContent: UnsafeMutablePointer<HMHelpContentRec>, _ userUPP: HMControlContentUPP) -> OSStatus ``` |

Modified InvokeHMMenuItemContentUPP(UnsafePointer<MenuTrackingData>, HMContentRequest, UnsafeMutablePointer<HMContentProvidedType>, UnsafeMutablePointer<HMHelpContentRec>, HMMenuItemContentUPP) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func InvokeHMMenuItemContentUPP(_ inTrackingData: ConstUnsafePointer<MenuTrackingData>, _ inRequest: HMContentRequest, _ outContentProvided: UnsafePointer<HMContentProvidedType>, _ ioHelpContent: UnsafePointer<HMHelpContentRec>, _ userUPP: HMMenuItemContentUPP) -> OSStatus ``` |
| To | ``` func InvokeHMMenuItemContentUPP(_ inTrackingData: UnsafePointer<MenuTrackingData>, _ inRequest: HMContentRequest, _ outContentProvided: UnsafeMutablePointer<HMContentProvidedType>, _ ioHelpContent: UnsafeMutablePointer<HMHelpContentRec>, _ userUPP: HMMenuItemContentUPP) -> OSStatus ``` |

Modified InvokeHMMenuTitleContentUPP(Menu!, HMContentRequest, UnsafeMutablePointer<HMContentProvidedType>, UnsafeMutablePointer<HMHelpContentRec>, HMMenuTitleContentUPP) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func InvokeHMMenuTitleContentUPP(_ inMenu: Menu!, _ inRequest: HMContentRequest, _ outContentProvided: UnsafePointer<HMContentProvidedType>, _ ioHelpContent: UnsafePointer<HMHelpContentRec>, _ userUPP: HMMenuTitleContentUPP) -> OSStatus ``` |
| To | ``` func InvokeHMMenuTitleContentUPP(_ inMenu: Menu!, _ inRequest: HMContentRequest, _ outContentProvided: UnsafeMutablePointer<HMContentProvidedType>, _ ioHelpContent: UnsafeMutablePointer<HMHelpContentRec>, _ userUPP: HMMenuTitleContentUPP) -> OSStatus ``` |

Modified InvokeHMWindowContentUPP(WindowRef, Point, HMContentRequest, UnsafeMutablePointer<HMContentProvidedType>, UnsafeMutablePointer<HMHelpContentRec>, HMWindowContentUPP) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeHMWindowContentUPP(_ inWindow: Window!, _ inGlobalMouse: Point, _ inRequest: HMContentRequest, _ outContentProvided: UnsafePointer<HMContentProvidedType>, _ ioHelpContent: UnsafePointer<HMHelpContentRec>, _ userUPP: HMWindowContentUPP) -> OSStatus ``` | OS X 10.10 |
| To | ``` func InvokeHMWindowContentUPP(_ inWindow: WindowRef, _ inGlobalMouse: Point, _ inRequest: HMContentRequest, _ outContentProvided: UnsafeMutablePointer<HMContentProvidedType>, _ ioHelpContent: UnsafeMutablePointer<HMHelpContentRec>, _ userUPP: HMWindowContentUPP) -> OSStatus ``` | OS X 10.10.3 |

Modified InvokeModalFilterUPP(DialogRef, UnsafeMutablePointer<EventRecord>, UnsafeMutablePointer<DialogItemIndex>, ModalFilterUPP) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeModalFilterUPP(_ theDialog: Dialog!, _ theEvent: UnsafePointer<EventRecord>, _ itemHit: UnsafePointer<DialogItemIndex>, _ userUPP: ModalFilterUPP) -> Boolean ``` | OS X 10.10 |
| To | ``` func InvokeModalFilterUPP(_ theDialog: DialogRef, _ theEvent: UnsafeMutablePointer<EventRecord>, _ itemHit: UnsafeMutablePointer<DialogItemIndex>, _ userUPP: ModalFilterUPP) -> Boolean ``` | OS X 10.10.3 |

Modified InvokeModalFilterYDUPP(DialogRef, UnsafeMutablePointer<EventRecord>, UnsafeMutablePointer<Int16>, UnsafeMutablePointer<Void>, ModalFilterYDUPP) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeModalFilterYDUPP(_ theDialog: Dialog!, _ theEvent: UnsafePointer<EventRecord>, _ itemHit: UnsafePointer<Int16>, _ yourDataPtr: UnsafePointer<()>, _ userUPP: ModalFilterYDUPP) -> Boolean ``` | OS X 10.10 |
| To | ``` func InvokeModalFilterYDUPP(_ theDialog: DialogRef, _ theEvent: UnsafeMutablePointer<EventRecord>, _ itemHit: UnsafeMutablePointer<Int16>, _ yourDataPtr: UnsafeMutablePointer<Void>, _ userUPP: ModalFilterYDUPP) -> Boolean ``` | OS X 10.10.3 |

Modified InvokeNColorChangedUPP(SRefCon, UnsafeMutablePointer<NPMColor>, NColorChangedUPP)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeNColorChangedUPP(_ userData: SRefCon, _ newColor: UnsafePointer<NPMColor>, _ userUPP: NColorChangedUPP) ``` |
| To | ``` func InvokeNColorChangedUPP(_ userData: SRefCon, _ newColor: UnsafeMutablePointer<NPMColor>, _ userUPP: NColorChangedUPP) ``` |

Modified InvokeNavEventUPP(NavEventCallbackMessage, NavCBRecPtr, UnsafeMutablePointer<Void>, NavEventUPP)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeNavEventUPP(_ callBackSelector: NavEventCallbackMessage, _ callBackParms: NavCBRecPtr, _ callBackUD: UnsafePointer<()>, _ userUPP: NavEventUPP) ``` |
| To | ``` func InvokeNavEventUPP(_ callBackSelector: NavEventCallbackMessage, _ callBackParms: NavCBRecPtr, _ callBackUD: UnsafeMutablePointer<Void>, _ userUPP: NavEventUPP) ``` |

Modified InvokeNavObjectFilterUPP(UnsafeMutablePointer<AEDesc>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, NavFilterModes, NavObjectFilterUPP) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func InvokeNavObjectFilterUPP(_ theItem: UnsafePointer<AEDesc>, _ info: UnsafePointer<()>, _ callBackUD: UnsafePointer<()>, _ filterMode: NavFilterModes, _ userUPP: NavObjectFilterUPP) -> Boolean ``` |
| To | ``` func InvokeNavObjectFilterUPP(_ theItem: UnsafeMutablePointer<AEDesc>, _ info: UnsafeMutablePointer<Void>, _ callBackUD: UnsafeMutablePointer<Void>, _ filterMode: NavFilterModes, _ userUPP: NavObjectFilterUPP) -> Boolean ``` |

Modified InvokeNavPreviewUPP(NavCBRecPtr, UnsafeMutablePointer<Void>, NavPreviewUPP) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func InvokeNavPreviewUPP(_ callBackParms: NavCBRecPtr, _ callBackUD: UnsafePointer<()>, _ userUPP: NavPreviewUPP) -> Boolean ``` |
| To | ``` func InvokeNavPreviewUPP(_ callBackParms: NavCBRecPtr, _ callBackUD: UnsafeMutablePointer<Void>, _ userUPP: NavPreviewUPP) -> Boolean ``` |

Modified InvokeOSAActiveUPP(SRefCon, OSAActiveUPP) -> OSErr

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified InvokeOSACreateAppleEventUPP(AEEventClass, AEEventID, UnsafePointer<AEAddressDesc>, Int16, Int32, UnsafeMutablePointer<AppleEvent>, SRefCon, OSACreateAppleEventUPP) -> OSErr

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeOSACreateAppleEventUPP(_ theAEEventClass: AEEventClass, _ theAEEventID: AEEventID, _ target: ConstUnsafePointer<AEAddressDesc>, _ returnID: Int16, _ transactionID: Int32, _ result: UnsafePointer<AppleEvent>, _ refCon: SRefCon, _ userUPP: OSACreateAppleEventUPP) -> OSErr ``` | OS X 10.10 |
| To | ``` func InvokeOSACreateAppleEventUPP(_ theAEEventClass: AEEventClass, _ theAEEventID: AEEventID, _ target: UnsafePointer<AEAddressDesc>, _ returnID: Int16, _ transactionID: Int32, _ result: UnsafeMutablePointer<AppleEvent>, _ refCon: SRefCon, _ userUPP: OSACreateAppleEventUPP) -> OSErr ``` | OS X 10.0 |

Modified InvokeOSASendUPP(UnsafePointer<AppleEvent>, UnsafeMutablePointer<AppleEvent>, AESendMode, AESendPriority, Int32, AEIdleUPP, AEFilterUPP, SRefCon, OSASendUPP) -> OSErr

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeOSASendUPP(_ theAppleEvent: ConstUnsafePointer<AppleEvent>, _ reply: UnsafePointer<AppleEvent>, _ sendMode: AESendMode, _ sendPriority: AESendPriority, _ timeOutInTicks: Int32, _ idleProc: AEIdleUPP, _ filterProc: AEFilterUPP, _ refCon: SRefCon, _ userUPP: OSASendUPP) -> OSErr ``` | OS X 10.10 |
| To | ``` func InvokeOSASendUPP(_ theAppleEvent: UnsafePointer<AppleEvent>, _ reply: UnsafeMutablePointer<AppleEvent>, _ sendMode: AESendMode, _ sendPriority: AESendPriority, _ timeOutInTicks: Int32, _ idleProc: AEIdleUPP, _ filterProc: AEFilterUPP, _ refCon: SRefCon, _ userUPP: OSASendUPP) -> OSErr ``` | OS X 10.0 |

Modified InvokeSRCallBackUPP(UnsafeMutablePointer<SRCallBackStruct>, SRCallBackUPP)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeSRCallBackUPP(_ param: UnsafePointer<SRCallBackStruct>, _ userUPP: SRCallBackUPP) ``` |
| To | ``` func InvokeSRCallBackUPP(_ param: UnsafeMutablePointer<SRCallBackStruct>, _ userUPP: SRCallBackUPP) ``` |

Modified InvokeTXNActionNameMapperUPP(CFString!, UInt32, UnsafeMutablePointer<Void>, TXNActionNameMapperUPP) -> Unmanaged<CFString>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeTXNActionNameMapperUPP(_ actionName: CFString!, _ commandID: UInt32, _ inUserData: UnsafePointer<()>, _ userUPP: TXNActionNameMapperUPP) -> Unmanaged<CFString>! ``` | OS X 10.10 |
| To | ``` func InvokeTXNActionNameMapperUPP(_ actionName: CFString!, _ commandID: UInt32, _ inUserData: UnsafeMutablePointer<Void>, _ userUPP: TXNActionNameMapperUPP) -> Unmanaged<CFString>! ``` | OS X 10.4 |

Modified InvokeTXNContextualMenuSetupUPP(Menu!, TXNObject, UnsafeMutablePointer<Void>, TXNContextualMenuSetupUPP)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeTXNContextualMenuSetupUPP(_ iContextualMenu: Menu!, _ object: TXNObject, _ inUserData: UnsafePointer<()>, _ userUPP: TXNContextualMenuSetupUPP) ``` | OS X 10.10 |
| To | ``` func InvokeTXNContextualMenuSetupUPP(_ iContextualMenu: Menu!, _ object: TXNObject, _ inUserData: UnsafeMutablePointer<Void>, _ userUPP: TXNContextualMenuSetupUPP) ``` | OS X 10.4 |

Modified InvokeTXNFindUPP(UnsafePointer<TXNMatchTextRecord>, TXNDataType, TXNMatchOptions, UnsafePointer<Void>, TextEncoding, TXNOffset, Int, UnsafeMutablePointer<TXNOffset>, UnsafeMutablePointer<TXNOffset>, UnsafeMutablePointer<Boolean>, URefCon, TXNFindUPP) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeTXNFindUPP(_ matchData: ConstUnsafePointer<TXNMatchTextRecord>, _ iDataType: TXNDataType, _ iMatchOptions: TXNMatchOptions, _ iSearchTextPtr: ConstUnsafePointer<()>, _ encoding: TextEncoding, _ absStartOffset: TXNOffset, _ searchTextLength: ByteCount, _ oStartMatch: UnsafePointer<TXNOffset>, _ oEndMatch: UnsafePointer<TXNOffset>, _ ofound: UnsafePointer<Boolean>, _ refCon: URefCon, _ userUPP: TXNFindUPP) -> OSStatus ``` | OS X 10.10 |
| To | ``` func InvokeTXNFindUPP(_ matchData: UnsafePointer<TXNMatchTextRecord>, _ iDataType: TXNDataType, _ iMatchOptions: TXNMatchOptions, _ iSearchTextPtr: UnsafePointer<Void>, _ encoding: TextEncoding, _ absStartOffset: TXNOffset, _ searchTextLength: Int, _ oStartMatch: UnsafeMutablePointer<TXNOffset>, _ oEndMatch: UnsafeMutablePointer<TXNOffset>, _ ofound: UnsafeMutablePointer<Boolean>, _ refCon: URefCon, _ userUPP: TXNFindUPP) -> OSStatus ``` | OS X 10.10.3 |

Modified InvokeTXNScrollInfoUPP(Int32, Int32, TXNScrollBarOrientation, SRefCon, TXNScrollInfoUPP)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified InvokeUserItemUPP(DialogRef, DialogItemIndex, UserItemUPP)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func InvokeUserItemUPP(_ theDialog: Dialog!, _ itemNo: DialogItemIndex, _ userUPP: UserItemUPP) ``` | OS X 10.10 |
| To | ``` func InvokeUserItemUPP(_ theDialog: DialogRef, _ itemNo: DialogItemIndex, _ userUPP: UserItemUPP) ``` | OS X 10.10.3 |

Modified IsEventInQueue(EventQueueRef, EventRef) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IsEventInQueue(_ inQueue: EventQueue!, _ inEvent: Event!) -> Boolean ``` | OS X 10.10 |
| To | ``` func IsEventInQueue(_ inQueue: EventQueueRef, _ inEvent: EventRef) -> Boolean ``` | OS X 10.10.3 |

Modified IsSecureEventInputEnabled() -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified IsUserCancelEventRef(EventRef) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IsUserCancelEventRef(_ event: Event!) -> Boolean ``` | OS X 10.10 |
| To | ``` func IsUserCancelEventRef(_ event: EventRef) -> Boolean ``` | OS X 10.10.3 |

Modified KeyboardLayoutRef

|  | Declaration |
| --- | --- |
| From | ``` typealias KeyboardLayoutRef = KeyboardLayout ``` |
| To | ``` typealias KeyboardLayoutRef = COpaquePointer ``` |

Modified LHHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias LHHandle = UnsafePointer<LHPtr> ``` |
| To | ``` typealias LHHandle = UnsafeMutablePointer<LHPtr> ``` |

Modified LHPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias LHPtr = UnsafePointer<LHElement> ``` |
| To | ``` typealias LHPtr = UnsafeMutablePointer<LHElement> ``` |

Modified ListDefProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ListDefProcPtr = CFunctionPointer<((Int16, Boolean, UnsafePointer<Rect>, Cell, Int16, Int16, ListHandle) -> Void)> ``` |
| To | ``` typealias ListDefProcPtr = CFunctionPointer<((Int16, Boolean, UnsafeMutablePointer<Rect>, Cell, Int16, Int16, ListHandle) -> Void)> ``` |

Modified ListDefSpecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ListDefSpecPtr = UnsafePointer<ListDefSpec> ``` |
| To | ``` typealias ListDefSpecPtr = UnsafeMutablePointer<ListDefSpec> ``` |

Modified ListHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias ListHandle = UnsafePointer<ListPtr> ``` |
| To | ``` typealias ListHandle = UnsafeMutablePointer<ListPtr> ``` |

Modified ListPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ListPtr = UnsafePointer<ListRec> ``` |
| To | ``` typealias ListPtr = UnsafeMutablePointer<ListRec> ``` |

Modified MBarHookProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias MBarHookProcPtr = CFunctionPointer<((UnsafePointer<Rect>) -> Int16)> ``` |
| To | ``` typealias MBarHookProcPtr = CFunctionPointer<((UnsafeMutablePointer<Rect>) -> Int16)> ``` |

Modified MCEntryPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias MCEntryPtr = UnsafePointer<MCEntry> ``` |
| To | ``` typealias MCEntryPtr = UnsafeMutablePointer<MCEntry> ``` |

Modified MCTableHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias MCTableHandle = UnsafePointer<MCTablePtr> ``` |
| To | ``` typealias MCTableHandle = UnsafeMutablePointer<MCTablePtr> ``` |

Modified MCTablePtr

|  | Declaration |
| --- | --- |
| From | ``` typealias MCTablePtr = UnsafePointer<MCEntry> ``` |
| To | ``` typealias MCTablePtr = UnsafeMutablePointer<MCEntry> ``` |

Modified MDEFDrawDataPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias MDEFDrawDataPtr = UnsafePointer<MDEFDrawData> ``` |
| To | ``` typealias MDEFDrawDataPtr = UnsafeMutablePointer<MDEFDrawData> ``` |

Modified MDEFDrawItemsDataPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias MDEFDrawItemsDataPtr = UnsafePointer<MDEFDrawItemsData> ``` |
| To | ``` typealias MDEFDrawItemsDataPtr = UnsafeMutablePointer<MDEFDrawItemsData> ``` |

Modified MDEFFindItemDataPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias MDEFFindItemDataPtr = UnsafePointer<MDEFFindItemData> ``` |
| To | ``` typealias MDEFFindItemDataPtr = UnsafeMutablePointer<MDEFFindItemData> ``` |

Modified MDEFHiliteItemDataPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias MDEFHiliteItemDataPtr = UnsafePointer<MDEFHiliteItemData> ``` |
| To | ``` typealias MDEFHiliteItemDataPtr = UnsafeMutablePointer<MDEFHiliteItemData> ``` |

Modified MeasureWindowTitleRecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias MeasureWindowTitleRecPtr = UnsafePointer<MeasureWindowTitleRec> ``` |
| To | ``` typealias MeasureWindowTitleRecPtr = UnsafeMutablePointer<MeasureWindowTitleRec> ``` |

Modified MenuCRsrcHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias MenuCRsrcHandle = UnsafePointer<MenuCRsrcPtr> ``` |
| To | ``` typealias MenuCRsrcHandle = UnsafeMutablePointer<MenuCRsrcPtr> ``` |

Modified MenuCRsrcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias MenuCRsrcPtr = UnsafePointer<MenuCRsrc> ``` |
| To | ``` typealias MenuCRsrcPtr = UnsafeMutablePointer<MenuCRsrc> ``` |

Modified MenuDefSpecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias MenuDefSpecPtr = UnsafePointer<MenuDefSpec> ``` |
| To | ``` typealias MenuDefSpecPtr = UnsafeMutablePointer<MenuDefSpec> ``` |

Modified MenuDefUPP

|  | Declaration |
| --- | --- |
| From | ``` typealias MenuDefUPP = UnsafePointer<()> ``` |
| To | ``` typealias MenuDefUPP = UnsafeMutablePointer<Void> ``` |

Modified MenuHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias MenuHandle = Menu ``` |
| To | ``` typealias MenuHandle = MenuHandle ``` |

Modified MenuItemDataPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias MenuItemDataPtr = UnsafePointer<MenuItemDataRec> ``` |
| To | ``` typealias MenuItemDataPtr = UnsafeMutablePointer<MenuItemDataRec> ``` |

Modified MenuItemDrawingProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias MenuItemDrawingProcPtr = CFunctionPointer<((ConstUnsafePointer<Rect>, Int16, Boolean, SRefCon) -> Void)> ``` |
| To | ``` typealias MenuItemDrawingProcPtr = CFunctionPointer<((UnsafePointer<Rect>, Int16, Boolean, SRefCon) -> Void)> ``` |

Modified MenuTitleDrawingProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias MenuTitleDrawingProcPtr = CFunctionPointer<((ConstUnsafePointer<Rect>, Int16, Boolean, SRefCon) -> Void)> ``` |
| To | ``` typealias MenuTitleDrawingProcPtr = CFunctionPointer<((UnsafePointer<Rect>, Int16, Boolean, SRefCon) -> Void)> ``` |

Modified MenuTrackingDataPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias MenuTrackingDataPtr = UnsafePointer<MenuTrackingData> ``` |
| To | ``` typealias MenuTrackingDataPtr = UnsafeMutablePointer<MenuTrackingData> ``` |

Modified ModalFilterProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ModalFilterProcPtr = CFunctionPointer<((Dialog!, UnsafePointer<EventRecord>, UnsafePointer<DialogItemIndex>) -> Boolean)> ``` |
| To | ``` typealias ModalFilterProcPtr = CFunctionPointer<((DialogRef, UnsafeMutablePointer<EventRecord>, UnsafeMutablePointer<DialogItemIndex>) -> Boolean)> ``` |

Modified ModalFilterYDProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ModalFilterYDProcPtr = CFunctionPointer<((Dialog!, UnsafePointer<EventRecord>, UnsafePointer<Int16>, UnsafePointer<()>) -> Boolean)> ``` |
| To | ``` typealias ModalFilterYDProcPtr = CFunctionPointer<((DialogRef, UnsafeMutablePointer<EventRecord>, UnsafeMutablePointer<Int16>, UnsafeMutablePointer<Void>) -> Boolean)> ``` |

Modified NColorChangedProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias NColorChangedProcPtr = CFunctionPointer<((SRefCon, UnsafePointer<NPMColor>) -> Void)> ``` |
| To | ``` typealias NColorChangedProcPtr = CFunctionPointer<((SRefCon, UnsafeMutablePointer<NPMColor>) -> Void)> ``` |

Modified NMRecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias NMRecPtr = UnsafePointer<NMRec> ``` |
| To | ``` typealias NMRecPtr = UnsafeMutablePointer<NMRec> ``` |

Modified NPMColorPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias NPMColorPtr = UnsafePointer<NPMColor> ``` |
| To | ``` typealias NPMColorPtr = UnsafeMutablePointer<NPMColor> ``` |

Modified NPickColor(UnsafeMutablePointer<NColorPickerInfo>) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func NPickColor(_ theColorInfo: UnsafePointer<NColorPickerInfo>) -> OSErr ``` |
| To | ``` func NPickColor(_ theColorInfo: UnsafeMutablePointer<NColorPickerInfo>) -> OSErr ``` |

Modified NWidthHookProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias NWidthHookProcPtr = CFunctionPointer<((UInt16, UInt16, Int16, Int16, UnsafePointer<()>, UnsafePointer<Int16>, TEPtr, TEHandle) -> UInt16)> ``` |
| To | ``` typealias NWidthHookProcPtr = CFunctionPointer<((UInt16, UInt16, Int16, Int16, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int16>, TEPtr, TEHandle) -> UInt16)> ``` |

Modified NavCBRecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias NavCBRecPtr = UnsafePointer<NavCBRec> ``` |
| To | ``` typealias NavCBRecPtr = UnsafeMutablePointer<NavCBRec> ``` |

Modified NavCallBackUserData

|  | Declaration |
| --- | --- |
| From | ``` typealias NavCallBackUserData = UnsafePointer<()> ``` |
| To | ``` typealias NavCallBackUserData = UnsafeMutablePointer<Void> ``` |

Modified NavEventProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias NavEventProcPtr = CFunctionPointer<((NavEventCallbackMessage, NavCBRecPtr, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias NavEventProcPtr = CFunctionPointer<((NavEventCallbackMessage, NavCBRecPtr, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified NavMenuItemSpecArrayHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias NavMenuItemSpecArrayHandle = UnsafePointer<NavMenuItemSpecArrayPtr> ``` |
| To | ``` typealias NavMenuItemSpecArrayHandle = UnsafeMutablePointer<NavMenuItemSpecArrayPtr> ``` |

Modified NavMenuItemSpecArrayPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias NavMenuItemSpecArrayPtr = UnsafePointer<NavMenuItemSpec> ``` |
| To | ``` typealias NavMenuItemSpecArrayPtr = UnsafeMutablePointer<NavMenuItemSpec> ``` |

Modified NavObjectFilterProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias NavObjectFilterProcPtr = CFunctionPointer<((UnsafePointer<AEDesc>, UnsafePointer<()>, UnsafePointer<()>, NavFilterModes) -> Boolean)> ``` |
| To | ``` typealias NavObjectFilterProcPtr = CFunctionPointer<((UnsafeMutablePointer<AEDesc>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, NavFilterModes) -> Boolean)> ``` |

Modified NavPreviewProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias NavPreviewProcPtr = CFunctionPointer<((NavCBRecPtr, UnsafePointer<()>) -> Boolean)> ``` |
| To | ``` typealias NavPreviewProcPtr = CFunctionPointer<((NavCBRecPtr, UnsafeMutablePointer<Void>) -> Boolean)> ``` |

Modified NavTypeListHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias NavTypeListHandle = UnsafePointer<NavTypeListPtr> ``` |
| To | ``` typealias NavTypeListHandle = UnsafeMutablePointer<NavTypeListPtr> ``` |

Modified NavTypeListPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias NavTypeListPtr = UnsafePointer<NavTypeList> ``` |
| To | ``` typealias NavTypeListPtr = UnsafeMutablePointer<NavTypeList> ``` |

Modified NewDataBrowserDrawItemUPP(DataBrowserDrawItemProcPtr) -> DataBrowserDrawItemUPP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified NewDataBrowserEditItemUPP(DataBrowserEditItemProcPtr) -> DataBrowserEditItemUPP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified NewDataBrowserHitTestUPP(DataBrowserHitTestProcPtr) -> DataBrowserHitTestUPP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified NewDataBrowserItemAcceptDragUPP(DataBrowserItemAcceptDragProcPtr) -> DataBrowserItemAcceptDragUPP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified NewDataBrowserItemDragRgnUPP(DataBrowserItemDragRgnProcPtr) -> DataBrowserItemDragRgnUPP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified NewDataBrowserItemNotificationWithItemUPP(DataBrowserItemNotificationWithItemProcPtr) -> DataBrowserItemNotificationWithItemUPP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified NewDataBrowserItemReceiveDragUPP(DataBrowserItemReceiveDragProcPtr) -> DataBrowserItemReceiveDragUPP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified NewDataBrowserTrackingUPP(DataBrowserTrackingProcPtr) -> DataBrowserTrackingUPP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified NewEventLoopIdleTimerUPP(EventLoopIdleTimerProcPtr) -> EventLoopIdleTimerUPP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified NewOSAActiveUPP(OSAActiveProcPtr) -> OSAActiveUPP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified NewOSACreateAppleEventUPP(OSACreateAppleEventProcPtr) -> OSACreateAppleEventUPP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified NewOSASendUPP(OSASendProcPtr) -> OSASendUPP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified NewTXNActionNameMapperUPP(TXNActionNameMapperProcPtr) -> TXNActionNameMapperUPP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NewTXNContextualMenuSetupUPP(TXNContextualMenuSetupProcPtr) -> TXNContextualMenuSetupUPP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NewTXNScrollInfoUPP(TXNScrollInfoProcPtr) -> TXNScrollInfoUPP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified NullStHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias NullStHandle = UnsafePointer<NullStPtr> ``` |
| To | ``` typealias NullStHandle = UnsafeMutablePointer<NullStPtr> ``` |

Modified NullStPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias NullStPtr = UnsafePointer<NullStRec> ``` |
| To | ``` typealias NullStPtr = UnsafeMutablePointer<NullStRec> ``` |

Modified OSAAddStorageType(AEDataStorage, DescType) -> OSErr

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified OSAAvailableDialectCodeList(ComponentInstance, UnsafeMutablePointer<AEDesc>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAAvailableDialectCodeList(_ scriptingComponent: ComponentInstance, _ resultingDialectCodeList: UnsafePointer<AEDesc>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAAvailableDialectCodeList(_ scriptingComponent: ComponentInstance, _ resultingDialectCodeList: UnsafeMutablePointer<AEDesc>) -> OSAError ``` | OS X 10.0 |

Modified OSAAvailableDialects(ComponentInstance, UnsafeMutablePointer<AEDesc>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAAvailableDialects(_ scriptingComponent: ComponentInstance, _ resultingDialectInfoList: UnsafePointer<AEDesc>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAAvailableDialects(_ scriptingComponent: ComponentInstance, _ resultingDialectInfoList: UnsafeMutablePointer<AEDesc>) -> OSAError ``` | OS X 10.0 |

Modified OSACoerceFromDesc(ComponentInstance, UnsafePointer<AEDesc>, Int32, UnsafeMutablePointer<OSAID>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSACoerceFromDesc(_ scriptingComponent: ComponentInstance, _ scriptData: ConstUnsafePointer<AEDesc>, _ modeFlags: Int32, _ resultingScriptID: UnsafePointer<OSAID>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSACoerceFromDesc(_ scriptingComponent: ComponentInstance, _ scriptData: UnsafePointer<AEDesc>, _ modeFlags: Int32, _ resultingScriptID: UnsafeMutablePointer<OSAID>) -> OSAError ``` | OS X 10.0 |

Modified OSACoerceToDesc(ComponentInstance, OSAID, DescType, Int32, UnsafeMutablePointer<AEDesc>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSACoerceToDesc(_ scriptingComponent: ComponentInstance, _ scriptID: OSAID, _ desiredType: DescType, _ modeFlags: Int32, _ result: UnsafePointer<AEDesc>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSACoerceToDesc(_ scriptingComponent: ComponentInstance, _ scriptID: OSAID, _ desiredType: DescType, _ modeFlags: Int32, _ result: UnsafeMutablePointer<AEDesc>) -> OSAError ``` | OS X 10.0 |

Modified OSACompile(ComponentInstance, UnsafePointer<AEDesc>, Int32, UnsafeMutablePointer<OSAID>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSACompile(_ scriptingComponent: ComponentInstance, _ sourceData: ConstUnsafePointer<AEDesc>, _ modeFlags: Int32, _ previousAndResultingScriptID: UnsafePointer<OSAID>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSACompile(_ scriptingComponent: ComponentInstance, _ sourceData: UnsafePointer<AEDesc>, _ modeFlags: Int32, _ previousAndResultingScriptID: UnsafeMutablePointer<OSAID>) -> OSAError ``` | OS X 10.0 |

Modified OSACompileExecute(ComponentInstance, UnsafePointer<AEDesc>, OSAID, Int32, UnsafeMutablePointer<OSAID>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSACompileExecute(_ scriptingComponent: ComponentInstance, _ sourceData: ConstUnsafePointer<AEDesc>, _ contextID: OSAID, _ modeFlags: Int32, _ resultingScriptValueID: UnsafePointer<OSAID>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSACompileExecute(_ scriptingComponent: ComponentInstance, _ sourceData: UnsafePointer<AEDesc>, _ contextID: OSAID, _ modeFlags: Int32, _ resultingScriptValueID: UnsafeMutablePointer<OSAID>) -> OSAError ``` | OS X 10.0 |

Modified OSACopyDisplayString(ComponentInstance, OSAID, Int32, UnsafeMutablePointer<Unmanaged<CFAttributedString>?>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSACopyDisplayString(_ scriptingComponent: ComponentInstance, _ scriptID: OSAID, _ modeFlags: Int32, _ result: UnsafePointer<Unmanaged<CFAttributedString>?>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSACopyDisplayString(_ scriptingComponent: ComponentInstance, _ scriptID: OSAID, _ modeFlags: Int32, _ result: UnsafeMutablePointer<Unmanaged<CFAttributedString>?>) -> OSAError ``` | OS X 10.5 |

Modified OSACopyID(ComponentInstance, OSAID, UnsafeMutablePointer<OSAID>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSACopyID(_ scriptingComponent: ComponentInstance, _ fromID: OSAID, _ toID: UnsafePointer<OSAID>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSACopyID(_ scriptingComponent: ComponentInstance, _ fromID: OSAID, _ toID: UnsafeMutablePointer<OSAID>) -> OSAError ``` | OS X 10.0 |

Modified OSACopyScript(ComponentInstance, OSAID, UnsafeMutablePointer<OSAID>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSACopyScript(_ scriptingComponent: ComponentInstance, _ fromID: OSAID, _ toID: UnsafePointer<OSAID>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSACopyScript(_ scriptingComponent: ComponentInstance, _ fromID: OSAID, _ toID: UnsafeMutablePointer<OSAID>) -> OSAError ``` | OS X 10.6 |

Modified OSACopyScriptingDefinition(UnsafePointer<FSRef>, Int32, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSACopyScriptingDefinition(_ ref: ConstUnsafePointer<FSRef>, _ modeFlags: Int32, _ sdef: UnsafePointer<Unmanaged<CFData>?>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSACopyScriptingDefinition(_ ref: UnsafePointer<FSRef>, _ modeFlags: Int32, _ sdef: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSAError ``` | OS X 10.4 |

Modified OSACopyScriptingDefinitionFromURL(CFURL!, Int32, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSACopyScriptingDefinitionFromURL(_ url: CFURL!, _ modeFlags: Int32, _ sdef: UnsafePointer<Unmanaged<CFData>?>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSACopyScriptingDefinitionFromURL(_ url: CFURL!, _ modeFlags: Int32, _ sdef: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSAError ``` | OS X 10.5 |

Modified OSACopySourceString(ComponentInstance, OSAID, Int32, UnsafeMutablePointer<Unmanaged<CFAttributedString>?>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSACopySourceString(_ scriptingComponent: ComponentInstance, _ scriptID: OSAID, _ modeFlags: Int32, _ result: UnsafePointer<Unmanaged<CFAttributedString>?>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSACopySourceString(_ scriptingComponent: ComponentInstance, _ scriptID: OSAID, _ modeFlags: Int32, _ result: UnsafeMutablePointer<Unmanaged<CFAttributedString>?>) -> OSAError ``` | OS X 10.5 |

Modified OSACreateAppleEventProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias OSACreateAppleEventProcPtr = CFunctionPointer<((AEEventClass, AEEventID, ConstUnsafePointer<AEAddressDesc>, Int16, Int32, UnsafePointer<AppleEvent>, SRefCon) -> OSErr)> ``` |
| To | ``` typealias OSACreateAppleEventProcPtr = CFunctionPointer<((AEEventClass, AEEventID, UnsafePointer<AEAddressDesc>, Int16, Int32, UnsafeMutablePointer<AppleEvent>, SRefCon) -> OSErr)> ``` |

Modified OSADisplay(ComponentInstance, OSAID, DescType, Int32, UnsafeMutablePointer<AEDesc>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSADisplay(_ scriptingComponent: ComponentInstance, _ scriptValueID: OSAID, _ desiredType: DescType, _ modeFlags: Int32, _ resultingText: UnsafePointer<AEDesc>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSADisplay(_ scriptingComponent: ComponentInstance, _ scriptValueID: OSAID, _ desiredType: DescType, _ modeFlags: Int32, _ resultingText: UnsafeMutablePointer<AEDesc>) -> OSAError ``` | OS X 10.0 |

Modified OSADispose(ComponentInstance, OSAID) -> OSAError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified OSADoEvent(ComponentInstance, UnsafePointer<AppleEvent>, OSAID, Int32, UnsafeMutablePointer<AppleEvent>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSADoEvent(_ scriptingComponent: ComponentInstance, _ theAppleEvent: ConstUnsafePointer<AppleEvent>, _ contextID: OSAID, _ modeFlags: Int32, _ reply: UnsafePointer<AppleEvent>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSADoEvent(_ scriptingComponent: ComponentInstance, _ theAppleEvent: UnsafePointer<AppleEvent>, _ contextID: OSAID, _ modeFlags: Int32, _ reply: UnsafeMutablePointer<AppleEvent>) -> OSAError ``` | OS X 10.0 |

Modified OSADoScript(ComponentInstance, UnsafePointer<AEDesc>, OSAID, DescType, Int32, UnsafeMutablePointer<AEDesc>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSADoScript(_ scriptingComponent: ComponentInstance, _ sourceData: ConstUnsafePointer<AEDesc>, _ contextID: OSAID, _ desiredType: DescType, _ modeFlags: Int32, _ resultingText: UnsafePointer<AEDesc>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSADoScript(_ scriptingComponent: ComponentInstance, _ sourceData: UnsafePointer<AEDesc>, _ contextID: OSAID, _ desiredType: DescType, _ modeFlags: Int32, _ resultingText: UnsafeMutablePointer<AEDesc>) -> OSAError ``` | OS X 10.0 |

Modified OSADoScriptFile(ComponentInstance, UnsafePointer<FSRef>, OSAID, DescType, Int32, UnsafeMutablePointer<AEDesc>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSADoScriptFile(_ scriptingComponent: ComponentInstance, _ scriptFile: ConstUnsafePointer<FSRef>, _ contextID: OSAID, _ desiredType: DescType, _ modeFlags: Int32, _ resultingText: UnsafePointer<AEDesc>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSADoScriptFile(_ scriptingComponent: ComponentInstance, _ scriptFile: UnsafePointer<FSRef>, _ contextID: OSAID, _ desiredType: DescType, _ modeFlags: Int32, _ resultingText: UnsafeMutablePointer<AEDesc>) -> OSAError ``` | OS X 10.3 |

Modified OSAExecute(ComponentInstance, OSAID, OSAID, Int32, UnsafeMutablePointer<OSAID>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAExecute(_ scriptingComponent: ComponentInstance, _ compiledScriptID: OSAID, _ contextID: OSAID, _ modeFlags: Int32, _ resultingScriptValueID: UnsafePointer<OSAID>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAExecute(_ scriptingComponent: ComponentInstance, _ compiledScriptID: OSAID, _ contextID: OSAID, _ modeFlags: Int32, _ resultingScriptValueID: UnsafeMutablePointer<OSAID>) -> OSAError ``` | OS X 10.0 |

Modified OSAExecuteEvent(ComponentInstance, UnsafePointer<AppleEvent>, OSAID, Int32, UnsafeMutablePointer<OSAID>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAExecuteEvent(_ scriptingComponent: ComponentInstance, _ theAppleEvent: ConstUnsafePointer<AppleEvent>, _ contextID: OSAID, _ modeFlags: Int32, _ resultingScriptValueID: UnsafePointer<OSAID>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAExecuteEvent(_ scriptingComponent: ComponentInstance, _ theAppleEvent: UnsafePointer<AppleEvent>, _ contextID: OSAID, _ modeFlags: Int32, _ resultingScriptValueID: UnsafeMutablePointer<OSAID>) -> OSAError ``` | OS X 10.0 |

Modified OSAGenericToRealID(ComponentInstance, UnsafeMutablePointer<OSAID>, UnsafeMutablePointer<ComponentInstance>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAGenericToRealID(_ genericScriptingComponent: ComponentInstance, _ theScriptID: UnsafePointer<OSAID>, _ theExactComponent: UnsafePointer<ComponentInstance>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAGenericToRealID(_ genericScriptingComponent: ComponentInstance, _ theScriptID: UnsafeMutablePointer<OSAID>, _ theExactComponent: UnsafeMutablePointer<ComponentInstance>) -> OSAError ``` | OS X 10.0 |

Modified OSAGetActiveProc(ComponentInstance, UnsafeMutablePointer<OSAActiveUPP>, UnsafeMutablePointer<SRefCon>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAGetActiveProc(_ scriptingComponent: ComponentInstance, _ activeProc: UnsafePointer<OSAActiveUPP>, _ refCon: UnsafePointer<SRefCon>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAGetActiveProc(_ scriptingComponent: ComponentInstance, _ activeProc: UnsafeMutablePointer<OSAActiveUPP>, _ refCon: UnsafeMutablePointer<SRefCon>) -> OSAError ``` | OS X 10.0 |

Modified OSAGetCreateProc(ComponentInstance, UnsafeMutablePointer<OSACreateAppleEventUPP>, UnsafeMutablePointer<SRefCon>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAGetCreateProc(_ scriptingComponent: ComponentInstance, _ createProc: UnsafePointer<OSACreateAppleEventUPP>, _ refCon: UnsafePointer<SRefCon>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAGetCreateProc(_ scriptingComponent: ComponentInstance, _ createProc: UnsafeMutablePointer<OSACreateAppleEventUPP>, _ refCon: UnsafeMutablePointer<SRefCon>) -> OSAError ``` | OS X 10.0 |

Modified OSAGetCurrentDialect(ComponentInstance, UnsafeMutablePointer<Int16>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAGetCurrentDialect(_ scriptingComponent: ComponentInstance, _ resultingDialectCode: UnsafePointer<Int16>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAGetCurrentDialect(_ scriptingComponent: ComponentInstance, _ resultingDialectCode: UnsafeMutablePointer<Int16>) -> OSAError ``` | OS X 10.0 |

Modified OSAGetDefaultScriptingComponent(ComponentInstance, UnsafeMutablePointer<ScriptingComponentSelector>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAGetDefaultScriptingComponent(_ genericScriptingComponent: ComponentInstance, _ scriptingSubType: UnsafePointer<ScriptingComponentSelector>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAGetDefaultScriptingComponent(_ genericScriptingComponent: ComponentInstance, _ scriptingSubType: UnsafeMutablePointer<ScriptingComponentSelector>) -> OSAError ``` | OS X 10.0 |

Modified OSAGetDialectInfo(ComponentInstance, Int16, OSType, UnsafeMutablePointer<AEDesc>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAGetDialectInfo(_ scriptingComponent: ComponentInstance, _ dialectCode: Int16, _ selector: OSType, _ resultingDialectInfo: UnsafePointer<AEDesc>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAGetDialectInfo(_ scriptingComponent: ComponentInstance, _ dialectCode: Int16, _ selector: OSType, _ resultingDialectInfo: UnsafeMutablePointer<AEDesc>) -> OSAError ``` | OS X 10.0 |

Modified OSAGetHandler(ComponentInstance, Int32, OSAID, UnsafePointer<AEDesc>, UnsafeMutablePointer<OSAID>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAGetHandler(_ scriptingComponent: ComponentInstance, _ modeFlags: Int32, _ contextID: OSAID, _ handlerName: ConstUnsafePointer<AEDesc>, _ resultingCompiledScriptID: UnsafePointer<OSAID>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAGetHandler(_ scriptingComponent: ComponentInstance, _ modeFlags: Int32, _ contextID: OSAID, _ handlerName: UnsafePointer<AEDesc>, _ resultingCompiledScriptID: UnsafeMutablePointer<OSAID>) -> OSAError ``` | OS X 10.0 |

Modified OSAGetHandlerNames(ComponentInstance, Int32, OSAID, UnsafeMutablePointer<AEDescList>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAGetHandlerNames(_ scriptingComponent: ComponentInstance, _ modeFlags: Int32, _ contextID: OSAID, _ resultingHandlerNames: UnsafePointer<AEDescList>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAGetHandlerNames(_ scriptingComponent: ComponentInstance, _ modeFlags: Int32, _ contextID: OSAID, _ resultingHandlerNames: UnsafeMutablePointer<AEDescList>) -> OSAError ``` | OS X 10.0 |

Modified OSAGetProperty(ComponentInstance, Int32, OSAID, UnsafePointer<AEDesc>, UnsafeMutablePointer<OSAID>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAGetProperty(_ scriptingComponent: ComponentInstance, _ modeFlags: Int32, _ contextID: OSAID, _ variableName: ConstUnsafePointer<AEDesc>, _ resultingScriptValueID: UnsafePointer<OSAID>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAGetProperty(_ scriptingComponent: ComponentInstance, _ modeFlags: Int32, _ contextID: OSAID, _ variableName: UnsafePointer<AEDesc>, _ resultingScriptValueID: UnsafeMutablePointer<OSAID>) -> OSAError ``` | OS X 10.0 |

Modified OSAGetPropertyNames(ComponentInstance, Int32, OSAID, UnsafeMutablePointer<AEDescList>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAGetPropertyNames(_ scriptingComponent: ComponentInstance, _ modeFlags: Int32, _ contextID: OSAID, _ resultingPropertyNames: UnsafePointer<AEDescList>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAGetPropertyNames(_ scriptingComponent: ComponentInstance, _ modeFlags: Int32, _ contextID: OSAID, _ resultingPropertyNames: UnsafeMutablePointer<AEDescList>) -> OSAError ``` | OS X 10.0 |

Modified OSAGetResumeDispatchProc(ComponentInstance, UnsafeMutablePointer<AEEventHandlerUPP>, UnsafeMutablePointer<SRefCon>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAGetResumeDispatchProc(_ scriptingComponent: ComponentInstance, _ resumeDispatchProc: UnsafePointer<AEEventHandlerUPP>, _ refCon: UnsafePointer<SRefCon>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAGetResumeDispatchProc(_ scriptingComponent: ComponentInstance, _ resumeDispatchProc: UnsafeMutablePointer<AEEventHandlerUPP>, _ refCon: UnsafeMutablePointer<SRefCon>) -> OSAError ``` | OS X 10.0 |

Modified OSAGetScriptDataFromURL(CFURL!, UnsafeMutablePointer<Boolean>, Int32, UnsafeMutablePointer<AEDesc>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAGetScriptDataFromURL(_ scriptURL: CFURL!, _ storable: UnsafePointer<Boolean>, _ modeFlags: Int32, _ resultingScriptData: UnsafePointer<AEDesc>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAGetScriptDataFromURL(_ scriptURL: CFURL!, _ storable: UnsafeMutablePointer<Boolean>, _ modeFlags: Int32, _ resultingScriptData: UnsafeMutablePointer<AEDesc>) -> OSAError ``` | OS X 10.6 |

Modified OSAGetScriptInfo(ComponentInstance, OSAID, OSType, UnsafeMutablePointer<Int>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAGetScriptInfo(_ scriptingComponent: ComponentInstance, _ scriptID: OSAID, _ selector: OSType, _ result: UnsafePointer<Int>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAGetScriptInfo(_ scriptingComponent: ComponentInstance, _ scriptID: OSAID, _ selector: OSType, _ result: UnsafeMutablePointer<Int>) -> OSAError ``` | OS X 10.0 |

Modified OSAGetScriptingComponent(ComponentInstance, ScriptingComponentSelector, UnsafeMutablePointer<ComponentInstance>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAGetScriptingComponent(_ genericScriptingComponent: ComponentInstance, _ scriptingSubType: ScriptingComponentSelector, _ scriptingInstance: UnsafePointer<ComponentInstance>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAGetScriptingComponent(_ genericScriptingComponent: ComponentInstance, _ scriptingSubType: ScriptingComponentSelector, _ scriptingInstance: UnsafeMutablePointer<ComponentInstance>) -> OSAError ``` | OS X 10.0 |

Modified OSAGetScriptingComponentFromStored(ComponentInstance, UnsafePointer<AEDesc>, UnsafeMutablePointer<ScriptingComponentSelector>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAGetScriptingComponentFromStored(_ genericScriptingComponent: ComponentInstance, _ scriptData: ConstUnsafePointer<AEDesc>, _ scriptingSubType: UnsafePointer<ScriptingComponentSelector>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAGetScriptingComponentFromStored(_ genericScriptingComponent: ComponentInstance, _ scriptData: UnsafePointer<AEDesc>, _ scriptingSubType: UnsafeMutablePointer<ScriptingComponentSelector>) -> OSAError ``` | OS X 10.0 |

Modified OSAGetSendProc(ComponentInstance, UnsafeMutablePointer<OSASendUPP>, UnsafeMutablePointer<SRefCon>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAGetSendProc(_ scriptingComponent: ComponentInstance, _ sendProc: UnsafePointer<OSASendUPP>, _ refCon: UnsafePointer<SRefCon>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAGetSendProc(_ scriptingComponent: ComponentInstance, _ sendProc: UnsafeMutablePointer<OSASendUPP>, _ refCon: UnsafeMutablePointer<SRefCon>) -> OSAError ``` | OS X 10.0 |

Modified OSAGetSource(ComponentInstance, OSAID, DescType, UnsafeMutablePointer<AEDesc>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAGetSource(_ scriptingComponent: ComponentInstance, _ scriptID: OSAID, _ desiredType: DescType, _ resultingSourceData: UnsafePointer<AEDesc>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAGetSource(_ scriptingComponent: ComponentInstance, _ scriptID: OSAID, _ desiredType: DescType, _ resultingSourceData: UnsafeMutablePointer<AEDesc>) -> OSAError ``` | OS X 10.0 |

Modified OSAGetStorageType(AEDataStorage, UnsafeMutablePointer<DescType>) -> OSErr

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAGetStorageType(_ scriptData: AEDataStorage, _ dscType: UnsafePointer<DescType>) -> OSErr ``` | OS X 10.10 |
| To | ``` func OSAGetStorageType(_ scriptData: AEDataStorage, _ dscType: UnsafeMutablePointer<DescType>) -> OSErr ``` | OS X 10.0 |

Modified OSAGetSysTerminology(ComponentInstance, Int32, Int16, UnsafeMutablePointer<AEDesc>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAGetSysTerminology(_ scriptingComponent: ComponentInstance, _ modeFlags: Int32, _ terminologyID: Int16, _ terminologyList: UnsafePointer<AEDesc>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAGetSysTerminology(_ scriptingComponent: ComponentInstance, _ modeFlags: Int32, _ terminologyID: Int16, _ terminologyList: UnsafeMutablePointer<AEDesc>) -> OSAError ``` | OS X 10.0 |

Modified OSALoad(ComponentInstance, UnsafePointer<AEDesc>, Int32, UnsafeMutablePointer<OSAID>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSALoad(_ scriptingComponent: ComponentInstance, _ scriptData: ConstUnsafePointer<AEDesc>, _ modeFlags: Int32, _ resultingScriptID: UnsafePointer<OSAID>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSALoad(_ scriptingComponent: ComponentInstance, _ scriptData: UnsafePointer<AEDesc>, _ modeFlags: Int32, _ resultingScriptID: UnsafeMutablePointer<OSAID>) -> OSAError ``` | OS X 10.0 |

Modified OSALoadExecute(ComponentInstance, UnsafePointer<AEDesc>, OSAID, Int32, UnsafeMutablePointer<OSAID>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSALoadExecute(_ scriptingComponent: ComponentInstance, _ scriptData: ConstUnsafePointer<AEDesc>, _ contextID: OSAID, _ modeFlags: Int32, _ resultingScriptValueID: UnsafePointer<OSAID>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSALoadExecute(_ scriptingComponent: ComponentInstance, _ scriptData: UnsafePointer<AEDesc>, _ contextID: OSAID, _ modeFlags: Int32, _ resultingScriptValueID: UnsafeMutablePointer<OSAID>) -> OSAError ``` | OS X 10.0 |

Modified OSALoadExecuteFile(ComponentInstance, UnsafePointer<FSRef>, OSAID, Int32, UnsafeMutablePointer<OSAID>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSALoadExecuteFile(_ scriptingComponent: ComponentInstance, _ scriptFile: ConstUnsafePointer<FSRef>, _ contextID: OSAID, _ modeFlags: Int32, _ resultingScriptValueID: UnsafePointer<OSAID>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSALoadExecuteFile(_ scriptingComponent: ComponentInstance, _ scriptFile: UnsafePointer<FSRef>, _ contextID: OSAID, _ modeFlags: Int32, _ resultingScriptValueID: UnsafeMutablePointer<OSAID>) -> OSAError ``` | OS X 10.3 |

Modified OSALoadFile(ComponentInstance, UnsafePointer<FSRef>, UnsafeMutablePointer<Boolean>, Int32, UnsafeMutablePointer<OSAID>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSALoadFile(_ scriptingComponent: ComponentInstance, _ scriptFile: ConstUnsafePointer<FSRef>, _ storable: UnsafePointer<Boolean>, _ modeFlags: Int32, _ resultingScriptID: UnsafePointer<OSAID>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSALoadFile(_ scriptingComponent: ComponentInstance, _ scriptFile: UnsafePointer<FSRef>, _ storable: UnsafeMutablePointer<Boolean>, _ modeFlags: Int32, _ resultingScriptID: UnsafeMutablePointer<OSAID>) -> OSAError ``` | OS X 10.3 |

Modified OSALoadScriptData(ComponentInstance, UnsafePointer<AEDesc>, CFURL!, Int32, UnsafeMutablePointer<OSAID>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSALoadScriptData(_ scriptingComponent: ComponentInstance, _ scriptData: ConstUnsafePointer<AEDesc>, _ fromURL: CFURL!, _ modeFlags: Int32, _ resultingScriptID: UnsafePointer<OSAID>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSALoadScriptData(_ scriptingComponent: ComponentInstance, _ scriptData: UnsafePointer<AEDesc>, _ fromURL: CFURL!, _ modeFlags: Int32, _ resultingScriptID: UnsafeMutablePointer<OSAID>) -> OSAError ``` | OS X 10.6 |

Modified OSAMakeContext(ComponentInstance, UnsafePointer<AEDesc>, OSAID, UnsafeMutablePointer<OSAID>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAMakeContext(_ scriptingComponent: ComponentInstance, _ contextName: ConstUnsafePointer<AEDesc>, _ parentContext: OSAID, _ resultingContextID: UnsafePointer<OSAID>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAMakeContext(_ scriptingComponent: ComponentInstance, _ contextName: UnsafePointer<AEDesc>, _ parentContext: OSAID, _ resultingContextID: UnsafeMutablePointer<OSAID>) -> OSAError ``` | OS X 10.0 |

Modified OSARealToGenericID(ComponentInstance, UnsafeMutablePointer<OSAID>, ComponentInstance) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSARealToGenericID(_ genericScriptingComponent: ComponentInstance, _ theScriptID: UnsafePointer<OSAID>, _ theExactComponent: ComponentInstance) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSARealToGenericID(_ genericScriptingComponent: ComponentInstance, _ theScriptID: UnsafeMutablePointer<OSAID>, _ theExactComponent: ComponentInstance) -> OSAError ``` | OS X 10.0 |

Modified OSARemoveStorageType(AEDataStorage) -> OSErr

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified OSAScriptError(ComponentInstance, OSType, DescType, UnsafeMutablePointer<AEDesc>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAScriptError(_ scriptingComponent: ComponentInstance, _ selector: OSType, _ desiredType: DescType, _ resultingErrorDescription: UnsafePointer<AEDesc>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAScriptError(_ scriptingComponent: ComponentInstance, _ selector: OSType, _ desiredType: DescType, _ resultingErrorDescription: UnsafeMutablePointer<AEDesc>) -> OSAError ``` | OS X 10.0 |

Modified OSAScriptingComponentName(ComponentInstance, UnsafeMutablePointer<AEDesc>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAScriptingComponentName(_ scriptingComponent: ComponentInstance, _ resultingScriptingComponentName: UnsafePointer<AEDesc>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAScriptingComponentName(_ scriptingComponent: ComponentInstance, _ resultingScriptingComponentName: UnsafeMutablePointer<AEDesc>) -> OSAError ``` | OS X 10.0 |

Modified OSASendProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias OSASendProcPtr = CFunctionPointer<((ConstUnsafePointer<AppleEvent>, UnsafePointer<AppleEvent>, AESendMode, AESendPriority, Int32, AEIdleUPP, AEFilterUPP, SRefCon) -> OSErr)> ``` |
| To | ``` typealias OSASendProcPtr = CFunctionPointer<((UnsafePointer<AppleEvent>, UnsafeMutablePointer<AppleEvent>, AESendMode, AESendPriority, Int32, AEIdleUPP, AEFilterUPP, SRefCon) -> OSErr)> ``` |

Modified OSASetActiveProc(ComponentInstance, OSAActiveUPP, SRefCon) -> OSAError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified OSASetCreateProc(ComponentInstance, OSACreateAppleEventUPP, SRefCon) -> OSAError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified OSASetCurrentDialect(ComponentInstance, Int16) -> OSAError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified OSASetDefaultScriptingComponent(ComponentInstance, ScriptingComponentSelector) -> OSAError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified OSASetDefaultTarget(ComponentInstance, UnsafePointer<AEAddressDesc>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSASetDefaultTarget(_ scriptingComponent: ComponentInstance, _ target: ConstUnsafePointer<AEAddressDesc>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSASetDefaultTarget(_ scriptingComponent: ComponentInstance, _ target: UnsafePointer<AEAddressDesc>) -> OSAError ``` | OS X 10.0 |

Modified OSASetHandler(ComponentInstance, Int32, OSAID, UnsafePointer<AEDesc>, OSAID) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSASetHandler(_ scriptingComponent: ComponentInstance, _ modeFlags: Int32, _ contextID: OSAID, _ handlerName: ConstUnsafePointer<AEDesc>, _ compiledScriptID: OSAID) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSASetHandler(_ scriptingComponent: ComponentInstance, _ modeFlags: Int32, _ contextID: OSAID, _ handlerName: UnsafePointer<AEDesc>, _ compiledScriptID: OSAID) -> OSAError ``` | OS X 10.0 |

Modified OSASetProperty(ComponentInstance, Int32, OSAID, UnsafePointer<AEDesc>, OSAID) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSASetProperty(_ scriptingComponent: ComponentInstance, _ modeFlags: Int32, _ contextID: OSAID, _ variableName: ConstUnsafePointer<AEDesc>, _ scriptValueID: OSAID) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSASetProperty(_ scriptingComponent: ComponentInstance, _ modeFlags: Int32, _ contextID: OSAID, _ variableName: UnsafePointer<AEDesc>, _ scriptValueID: OSAID) -> OSAError ``` | OS X 10.0 |

Modified OSASetResumeDispatchProc(ComponentInstance, AEEventHandlerUPP, SRefCon) -> OSAError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified OSASetScriptInfo(ComponentInstance, OSAID, OSType, Int) -> OSAError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified OSASetSendProc(ComponentInstance, OSASendUPP, SRefCon) -> OSAError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified OSAStartRecording(ComponentInstance, UnsafeMutablePointer<OSAID>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAStartRecording(_ scriptingComponent: ComponentInstance, _ compiledScriptToModifyID: UnsafePointer<OSAID>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAStartRecording(_ scriptingComponent: ComponentInstance, _ compiledScriptToModifyID: UnsafeMutablePointer<OSAID>) -> OSAError ``` | OS X 10.0 |

Modified OSAStopRecording(ComponentInstance, OSAID) -> OSAError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified OSAStore(ComponentInstance, OSAID, DescType, Int32, UnsafeMutablePointer<AEDesc>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAStore(_ scriptingComponent: ComponentInstance, _ scriptID: OSAID, _ desiredType: DescType, _ modeFlags: Int32, _ resultingScriptData: UnsafePointer<AEDesc>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAStore(_ scriptingComponent: ComponentInstance, _ scriptID: OSAID, _ desiredType: DescType, _ modeFlags: Int32, _ resultingScriptData: UnsafeMutablePointer<AEDesc>) -> OSAError ``` | OS X 10.0 |

Modified OSAStoreFile(ComponentInstance, OSAID, DescType, Int32, UnsafePointer<FSRef>) -> OSAError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func OSAStoreFile(_ scriptingComponent: ComponentInstance, _ scriptID: OSAID, _ desiredType: DescType, _ modeFlags: Int32, _ scriptFile: ConstUnsafePointer<FSRef>) -> OSAError ``` | OS X 10.10 |
| To | ``` func OSAStoreFile(_ scriptingComponent: ComponentInstance, _ scriptID: OSAID, _ desiredType: DescType, _ modeFlags: Int32, _ scriptFile: UnsafePointer<FSRef>) -> OSAError ``` | OS X 10.3 |

Modified PopSymbolicHotKeyMode(UnsafeMutablePointer<Void>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PopSymbolicHotKeyMode(_ inToken: UnsafePointer<()>) ``` | OS X 10.10 |
| To | ``` func PopSymbolicHotKeyMode(_ inToken: UnsafeMutablePointer<Void>) ``` | OS X 10.4 |

Modified PostEventToQueue(EventQueueRef, EventRef, EventPriority) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PostEventToQueue(_ inQueue: EventQueue!, _ inEvent: Event!, _ inPriority: EventPriority) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PostEventToQueue(_ inQueue: EventQueueRef, _ inEvent: EventRef, _ inPriority: EventPriority) -> OSStatus ``` | OS X 10.10.3 |

Modified ProcessHICommand(UnsafePointer<HICommand>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func ProcessHICommand(_ inCommand: ConstUnsafePointer<HICommand>) -> OSStatus ``` |
| To | ``` func ProcessHICommand(_ inCommand: UnsafePointer<HICommand>) -> OSStatus ``` |

Modified PushSymbolicHotKeyMode(OptionBits) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PushSymbolicHotKeyMode(_ inOptions: OptionBits) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func PushSymbolicHotKeyMode(_ inOptions: OptionBits) -> UnsafeMutablePointer<Void> ``` | OS X 10.4 |

Modified QuitEventLoop(EventLoopRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func QuitEventLoop(_ inEventLoop: EventLoop!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func QuitEventLoop(_ inEventLoop: EventLoopRef) -> OSStatus ``` | OS X 10.10.3 |

Modified ReceiveNextEvent(Int, UnsafePointer<EventTypeSpec>, EventTimeout, Boolean, UnsafeMutablePointer<EventRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ReceiveNextEvent(_ inNumTypes: ItemCount, _ inList: ConstUnsafePointer<EventTypeSpec>, _ inTimeout: EventTimeout, _ inPullEvent: Boolean, _ outEvent: UnsafePointer<Unmanaged<Event>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func ReceiveNextEvent(_ inNumTypes: Int, _ inList: UnsafePointer<EventTypeSpec>, _ inTimeout: EventTimeout, _ inPullEvent: Boolean, _ outEvent: UnsafeMutablePointer<EventRef>) -> OSStatus ``` | OS X 10.10.3 |

Modified RegisterEventHotKey(UInt32, UInt32, EventHotKeyID, EventTargetRef, OptionBits, UnsafeMutablePointer<EventHotKeyRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func RegisterEventHotKey(_ inHotKeyCode: UInt32, _ inHotKeyModifiers: UInt32, _ inHotKeyID: EventHotKeyID, _ inTarget: EventTarget!, _ inOptions: OptionBits, _ outRef: UnsafePointer<Unmanaged<EventHotKey>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func RegisterEventHotKey(_ inHotKeyCode: UInt32, _ inHotKeyModifiers: UInt32, _ inHotKeyID: EventHotKeyID, _ inTarget: EventTargetRef, _ inOptions: OptionBits, _ outRef: UnsafeMutablePointer<EventHotKeyRef>) -> OSStatus ``` | OS X 10.10.3 |

Modified ReleaseEvent(EventRef)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ReleaseEvent(_ inEvent: Event!) ``` | OS X 10.10 |
| To | ``` func ReleaseEvent(_ inEvent: EventRef) ``` | OS X 10.10.3 |

Modified RemoveEventFromQueue(EventQueueRef, EventRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func RemoveEventFromQueue(_ inQueue: EventQueue!, _ inEvent: Event!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func RemoveEventFromQueue(_ inQueue: EventQueueRef, _ inEvent: EventRef) -> OSStatus ``` | OS X 10.10.3 |

Modified RemoveEventHandler(EventHandlerRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func RemoveEventHandler(_ inHandlerRef: EventHandler!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func RemoveEventHandler(_ inHandlerRef: EventHandlerRef) -> OSStatus ``` | OS X 10.10.3 |

Modified RemoveEventParameter(EventRef, EventParamName) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func RemoveEventParameter(_ inEvent: Event!, _ inName: EventParamName) -> OSStatus ``` | OS X 10.10 |
| To | ``` func RemoveEventParameter(_ inEvent: EventRef, _ inName: EventParamName) -> OSStatus ``` | OS X 10.5 |

Modified RemoveEventTypesFromHandler(EventHandlerRef, Int, UnsafePointer<EventTypeSpec>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func RemoveEventTypesFromHandler(_ inHandlerRef: EventHandler!, _ inNumTypes: ItemCount, _ inList: ConstUnsafePointer<EventTypeSpec>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func RemoveEventTypesFromHandler(_ inHandlerRef: EventHandlerRef, _ inNumTypes: Int, _ inList: UnsafePointer<EventTypeSpec>) -> OSStatus ``` | OS X 10.10.3 |

Modified RetainEvent(EventRef) -> EventRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func RetainEvent(_ inEvent: Event!) -> Unmanaged<Event>! ``` | OS X 10.10 |
| To | ``` func RetainEvent(_ inEvent: EventRef) -> EventRef ``` | OS X 10.10.3 |

Modified SRAddText(SRLanguageObject, UnsafePointer<Void>, Int32, SRefCon) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func SRAddText(_ base: SRLanguageObject, _ text: ConstUnsafePointer<()>, _ textLength: Int32, _ refCon: SRefCon) -> OSErr ``` |
| To | ``` func SRAddText(_ base: SRLanguageObject, _ text: UnsafePointer<Void>, _ textLength: Int32, _ refCon: SRefCon) -> OSErr ``` |

Modified SRCallBackProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias SRCallBackProcPtr = CFunctionPointer<((UnsafePointer<SRCallBackStruct>) -> Void)> ``` |
| To | ``` typealias SRCallBackProcPtr = CFunctionPointer<((UnsafeMutablePointer<SRCallBackStruct>) -> Void)> ``` |

Modified SRChangeLanguageObject(SRLanguageObject, UnsafePointer<Void>, Int32) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func SRChangeLanguageObject(_ languageObject: SRLanguageObject, _ text: ConstUnsafePointer<()>, _ textLength: Int32) -> OSErr ``` |
| To | ``` func SRChangeLanguageObject(_ languageObject: SRLanguageObject, _ text: UnsafePointer<Void>, _ textLength: Int32) -> OSErr ``` |

Modified SRCountItems(SRSpeechObject, UnsafeMutablePointer<Int>) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func SRCountItems(_ container: SRSpeechObject, _ count: UnsafePointer<Int>) -> OSErr ``` |
| To | ``` func SRCountItems(_ container: SRSpeechObject, _ count: UnsafeMutablePointer<Int>) -> OSErr ``` |

Modified SRDrawRecognizedText(SRRecognizer, UnsafePointer<Void>, Int32) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func SRDrawRecognizedText(_ recognizer: SRRecognizer, _ dispText: ConstUnsafePointer<()>, _ dispLength: Int32) -> OSErr ``` |
| To | ``` func SRDrawRecognizedText(_ recognizer: SRRecognizer, _ dispText: UnsafePointer<Void>, _ dispLength: Int32) -> OSErr ``` |

Modified SRDrawText(SRRecognizer, UnsafePointer<Void>, Int32) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func SRDrawText(_ recognizer: SRRecognizer, _ dispText: ConstUnsafePointer<()>, _ dispLength: Int32) -> OSErr ``` |
| To | ``` func SRDrawText(_ recognizer: SRRecognizer, _ dispText: UnsafePointer<Void>, _ dispLength: Int32) -> OSErr ``` |

Modified SRGetIndexedItem(SRSpeechObject, UnsafeMutablePointer<SRSpeechObject>, Int) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func SRGetIndexedItem(_ container: SRSpeechObject, _ item: UnsafePointer<SRSpeechObject>, _ index: Int) -> OSErr ``` |
| To | ``` func SRGetIndexedItem(_ container: SRSpeechObject, _ item: UnsafeMutablePointer<SRSpeechObject>, _ index: Int) -> OSErr ``` |

Modified SRGetLanguageModel(SRRecognizer, UnsafeMutablePointer<SRLanguageModel>) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func SRGetLanguageModel(_ recognizer: SRRecognizer, _ languageModel: UnsafePointer<SRLanguageModel>) -> OSErr ``` |
| To | ``` func SRGetLanguageModel(_ recognizer: SRRecognizer, _ languageModel: UnsafeMutablePointer<SRLanguageModel>) -> OSErr ``` |

Modified SRGetProperty(SRSpeechObject, OSType, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Size>) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func SRGetProperty(_ srObject: SRSpeechObject, _ selector: OSType, _ property: UnsafePointer<()>, _ propertyLen: UnsafePointer<Size>) -> OSErr ``` |
| To | ``` func SRGetProperty(_ srObject: SRSpeechObject, _ selector: OSType, _ property: UnsafeMutablePointer<Void>, _ propertyLen: UnsafeMutablePointer<Size>) -> OSErr ``` |

Modified SRGetReference(SRSpeechObject, UnsafeMutablePointer<SRSpeechObject>) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func SRGetReference(_ srObject: SRSpeechObject, _ newObjectRef: UnsafePointer<SRSpeechObject>) -> OSErr ``` |
| To | ``` func SRGetReference(_ srObject: SRSpeechObject, _ newObjectRef: UnsafeMutablePointer<SRSpeechObject>) -> OSErr ``` |

Modified SRNewLanguageModel(SRRecognitionSystem, UnsafeMutablePointer<SRLanguageModel>, UnsafePointer<Void>, Int32) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func SRNewLanguageModel(_ system: SRRecognitionSystem, _ model: UnsafePointer<SRLanguageModel>, _ name: ConstUnsafePointer<()>, _ nameLength: Int32) -> OSErr ``` |
| To | ``` func SRNewLanguageModel(_ system: SRRecognitionSystem, _ model: UnsafeMutablePointer<SRLanguageModel>, _ name: UnsafePointer<Void>, _ nameLength: Int32) -> OSErr ``` |

Modified SRNewLanguageObjectFromDataFile(SRRecognitionSystem, UnsafeMutablePointer<SRLanguageObject>, Int16) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func SRNewLanguageObjectFromDataFile(_ system: SRRecognitionSystem, _ languageObject: UnsafePointer<SRLanguageObject>, _ fRefNum: Int16) -> OSErr ``` |
| To | ``` func SRNewLanguageObjectFromDataFile(_ system: SRRecognitionSystem, _ languageObject: UnsafeMutablePointer<SRLanguageObject>, _ fRefNum: Int16) -> OSErr ``` |

Modified SRNewLanguageObjectFromHandle(SRRecognitionSystem, UnsafeMutablePointer<SRLanguageObject>, Handle) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func SRNewLanguageObjectFromHandle(_ system: SRRecognitionSystem, _ languageObject: UnsafePointer<SRLanguageObject>, _ lObjHandle: Handle) -> OSErr ``` |
| To | ``` func SRNewLanguageObjectFromHandle(_ system: SRRecognitionSystem, _ languageObject: UnsafeMutablePointer<SRLanguageObject>, _ lObjHandle: Handle) -> OSErr ``` |

Modified SRNewPath(SRRecognitionSystem, UnsafeMutablePointer<SRPath>) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func SRNewPath(_ system: SRRecognitionSystem, _ path: UnsafePointer<SRPath>) -> OSErr ``` |
| To | ``` func SRNewPath(_ system: SRRecognitionSystem, _ path: UnsafeMutablePointer<SRPath>) -> OSErr ``` |

Modified SRNewPhrase(SRRecognitionSystem, UnsafeMutablePointer<SRPhrase>, UnsafePointer<Void>, Int32) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func SRNewPhrase(_ system: SRRecognitionSystem, _ phrase: UnsafePointer<SRPhrase>, _ text: ConstUnsafePointer<()>, _ textLength: Int32) -> OSErr ``` |
| To | ``` func SRNewPhrase(_ system: SRRecognitionSystem, _ phrase: UnsafeMutablePointer<SRPhrase>, _ text: UnsafePointer<Void>, _ textLength: Int32) -> OSErr ``` |

Modified SRNewRecognizer(SRRecognitionSystem, UnsafeMutablePointer<SRRecognizer>, OSType) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func SRNewRecognizer(_ system: SRRecognitionSystem, _ recognizer: UnsafePointer<SRRecognizer>, _ sourceID: OSType) -> OSErr ``` |
| To | ``` func SRNewRecognizer(_ system: SRRecognitionSystem, _ recognizer: UnsafeMutablePointer<SRRecognizer>, _ sourceID: OSType) -> OSErr ``` |

Modified SRNewWord(SRRecognitionSystem, UnsafeMutablePointer<SRWord>, UnsafePointer<Void>, Int32) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func SRNewWord(_ system: SRRecognitionSystem, _ word: UnsafePointer<SRWord>, _ text: ConstUnsafePointer<()>, _ textLength: Int32) -> OSErr ``` |
| To | ``` func SRNewWord(_ system: SRRecognitionSystem, _ word: UnsafeMutablePointer<SRWord>, _ text: UnsafePointer<Void>, _ textLength: Int32) -> OSErr ``` |

Modified SROpenRecognitionSystem(UnsafeMutablePointer<SRRecognitionSystem>, OSType) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func SROpenRecognitionSystem(_ system: UnsafePointer<SRRecognitionSystem>, _ systemID: OSType) -> OSErr ``` |
| To | ``` func SROpenRecognitionSystem(_ system: UnsafeMutablePointer<SRRecognitionSystem>, _ systemID: OSType) -> OSErr ``` |

Modified SRSetProperty(SRSpeechObject, OSType, UnsafePointer<Void>, Size) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func SRSetProperty(_ srObject: SRSpeechObject, _ selector: OSType, _ property: ConstUnsafePointer<()>, _ propertyLen: Size) -> OSErr ``` |
| To | ``` func SRSetProperty(_ srObject: SRSpeechObject, _ selector: OSType, _ property: UnsafePointer<Void>, _ propertyLen: Size) -> OSErr ``` |

Modified SRSpeakAndDrawText(SRRecognizer, UnsafePointer<Void>, Int32) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func SRSpeakAndDrawText(_ recognizer: SRRecognizer, _ text: ConstUnsafePointer<()>, _ textLength: Int32) -> OSErr ``` |
| To | ``` func SRSpeakAndDrawText(_ recognizer: SRRecognizer, _ text: UnsafePointer<Void>, _ textLength: Int32) -> OSErr ``` |

Modified SRSpeakText(SRRecognizer, UnsafePointer<Void>, Int32) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func SRSpeakText(_ recognizer: SRRecognizer, _ speakText: ConstUnsafePointer<()>, _ speakLength: Int32) -> OSErr ``` |
| To | ``` func SRSpeakText(_ recognizer: SRRecognizer, _ speakText: UnsafePointer<Void>, _ speakLength: Int32) -> OSErr ``` |

Modified STHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias STHandle = UnsafePointer<STPtr> ``` |
| To | ``` typealias STHandle = UnsafeMutablePointer<STPtr> ``` |

Modified STPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias STPtr = UnsafePointer<STElement> ``` |
| To | ``` typealias STPtr = UnsafeMutablePointer<STElement> ``` |

Modified ScrapPromiseKeeperProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ScrapPromiseKeeperProcPtr = CFunctionPointer<((Scrap!, ScrapFlavorType, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias ScrapPromiseKeeperProcPtr = CFunctionPointer<((ScrapRef, ScrapFlavorType, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified ScrapRef

|  | Declaration |
| --- | --- |
| From | ``` typealias ScrapRef = Scrap ``` |
| To | ``` typealias ScrapRef = COpaquePointer ``` |

Modified ScrapTranslationListHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias ScrapTranslationListHandle = UnsafePointer<ScrapTranslationListPtr> ``` |
| To | ``` typealias ScrapTranslationListHandle = UnsafeMutablePointer<ScrapTranslationListPtr> ``` |

Modified ScrapTranslationListPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ScrapTranslationListPtr = UnsafePointer<ScrapTranslationList> ``` |
| To | ``` typealias ScrapTranslationListPtr = UnsafeMutablePointer<ScrapTranslationList> ``` |

Modified ScriptLanguageSupportHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias ScriptLanguageSupportHandle = UnsafePointer<ScriptLanguageSupportPtr> ``` |
| To | ``` typealias ScriptLanguageSupportHandle = UnsafeMutablePointer<ScriptLanguageSupportPtr> ``` |

Modified ScriptLanguageSupportPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ScriptLanguageSupportPtr = UnsafePointer<ScriptLanguageSupport> ``` |
| To | ``` typealias ScriptLanguageSupportPtr = UnsafeMutablePointer<ScriptLanguageSupport> ``` |

Modified SendEventToEventTarget(EventRef, EventTargetRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SendEventToEventTarget(_ inEvent: Event!, _ inTarget: EventTarget!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SendEventToEventTarget(_ inEvent: EventRef, _ inTarget: EventTargetRef) -> OSStatus ``` | OS X 10.10.3 |

Modified SendEventToEventTargetWithOptions(EventRef, EventTargetRef, OptionBits) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SendEventToEventTargetWithOptions(_ inEvent: Event!, _ inTarget: EventTarget!, _ inOptions: OptionBits) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SendEventToEventTargetWithOptions(_ inEvent: EventRef, _ inTarget: EventTargetRef, _ inOptions: OptionBits) -> OSStatus ``` | OS X 10.2 |

Modified SetEventParameter(EventRef, EventParamName, EventParamType, Int, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SetEventParameter(_ inEvent: Event!, _ inName: EventParamName, _ inType: EventParamType, _ inSize: ByteCount, _ inDataPtr: ConstUnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SetEventParameter(_ inEvent: EventRef, _ inName: EventParamName, _ inType: EventParamType, _ inSize: Int, _ inDataPtr: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.10.3 |

Modified SetEventTime(EventRef, EventTime) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SetEventTime(_ inEvent: Event!, _ inTime: EventTime) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SetEventTime(_ inEvent: EventRef, _ inTime: EventTime) -> OSStatus ``` | OS X 10.10.3 |

Modified SetFontInfoForSelection(OSType, UInt32, UnsafeMutablePointer<Void>, EventTargetRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SetFontInfoForSelection(_ iStyleType: OSType, _ iNumStyles: UInt32, _ iStyles: UnsafePointer<()>, _ iFPEventTarget: EventTarget!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SetFontInfoForSelection(_ iStyleType: OSType, _ iNumStyles: UInt32, _ iStyles: UnsafeMutablePointer<Void>, _ iFPEventTarget: EventTargetRef) -> OSStatus ``` | OS X 10.2 |

Modified SetSystemUIMode(SystemUIMode, SystemUIOptions) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified StScrpHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias StScrpHandle = UnsafePointer<StScrpPtr> ``` |
| To | ``` typealias StScrpHandle = UnsafeMutablePointer<StScrpPtr> ``` |

Modified StScrpPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias StScrpPtr = UnsafePointer<StScrpRec> ``` |
| To | ``` typealias StScrpPtr = UnsafeMutablePointer<StScrpRec> ``` |

Modified StandardIconListCellDataPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias StandardIconListCellDataPtr = UnsafePointer<StandardIconListCellDataRec> ``` |
| To | ``` typealias StandardIconListCellDataPtr = UnsafeMutablePointer<StandardIconListCellDataRec> ``` |

Modified TEDoTextProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias TEDoTextProcPtr = CFunctionPointer<((TEPtr, UInt16, UInt16, Int16, UnsafePointer<GrafPtr>, UnsafePointer<Int16>) -> Void)> ``` |
| To | ``` typealias TEDoTextProcPtr = CFunctionPointer<((TEPtr, UInt16, UInt16, Int16, UnsafeMutablePointer<GrafPtr>, UnsafeMutablePointer<Int16>) -> Void)> ``` |

Modified TEFindWordProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias TEFindWordProcPtr = CFunctionPointer<((UInt16, Int16, TEPtr, TEHandle, UnsafePointer<UInt16>, UnsafePointer<UInt16>) -> Void)> ``` |
| To | ``` typealias TEFindWordProcPtr = CFunctionPointer<((UInt16, Int16, TEPtr, TEHandle, UnsafeMutablePointer<UInt16>, UnsafeMutablePointer<UInt16>) -> Void)> ``` |

Modified TEHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias TEHandle = UnsafePointer<TEPtr> ``` |
| To | ``` typealias TEHandle = UnsafeMutablePointer<TEPtr> ``` |

Modified TEPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias TEPtr = UnsafePointer<TERec> ``` |
| To | ``` typealias TEPtr = UnsafeMutablePointer<TERec> ``` |

Modified TERecalcProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias TERecalcProcPtr = CFunctionPointer<((TEPtr, UInt16, UnsafePointer<UInt16>, UnsafePointer<UInt16>, UnsafePointer<UInt16>) -> Void)> ``` |
| To | ``` typealias TERecalcProcPtr = CFunctionPointer<((TEPtr, UInt16, UnsafeMutablePointer<UInt16>, UnsafeMutablePointer<UInt16>, UnsafeMutablePointer<UInt16>) -> Void)> ``` |

Modified TEStyleHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias TEStyleHandle = UnsafePointer<TEStylePtr> ``` |
| To | ``` typealias TEStyleHandle = UnsafeMutablePointer<TEStylePtr> ``` |

Modified TEStylePtr

|  | Declaration |
| --- | --- |
| From | ``` typealias TEStylePtr = UnsafePointer<TEStyleRec> ``` |
| To | ``` typealias TEStylePtr = UnsafeMutablePointer<TEStyleRec> ``` |

Modified TISCopyCurrentASCIICapableKeyboardInputSource() -> Unmanaged<TISInputSource>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified TISCopyCurrentASCIICapableKeyboardLayoutInputSource() -> Unmanaged<TISInputSource>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified TISCopyCurrentKeyboardInputSource() -> Unmanaged<TISInputSource>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified TISCopyCurrentKeyboardLayoutInputSource() -> Unmanaged<TISInputSource>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified TISCopyInputMethodKeyboardLayoutOverride() -> Unmanaged<TISInputSource>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified TISCopyInputSourceForLanguage(CFString!) -> Unmanaged<TISInputSource>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified TISCreateASCIICapableInputSourceList() -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified TISCreateInputSourceList(CFDictionary!, Boolean) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified TISDeselectInputSource(TISInputSource!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified TISDisableInputSource(TISInputSource!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified TISEnableInputSource(TISInputSource!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified TISGetInputSourceProperty(TISInputSource!, CFString!) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func TISGetInputSourceProperty(_ inputSource: TISInputSource!, _ propertyKey: CFString!) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func TISGetInputSourceProperty(_ inputSource: TISInputSource!, _ propertyKey: CFString!) -> UnsafeMutablePointer<Void> ``` | OS X 10.5 |

Modified TISInputSourceGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified TISRegisterInputSource(CFURL!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified TISSelectInputSource(TISInputSource!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified TISSetInputMethodKeyboardLayoutOverride(TISInputSource!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified TSMGetDocumentProperty(TSMDocumentID, TSMDocumentPropertyTag, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func TSMGetDocumentProperty(_ docID: TSMDocumentID, _ propertyTag: TSMDocumentPropertyTag, _ bufferSize: UInt32, _ actualSize: UnsafePointer<UInt32>, _ propertyBuffer: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func TSMGetDocumentProperty(_ docID: TSMDocumentID, _ propertyTag: TSMDocumentPropertyTag, _ bufferSize: UInt32, _ actualSize: UnsafeMutablePointer<UInt32>, _ propertyBuffer: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.2 |

Modified TSMRemoveDocumentProperty(TSMDocumentID, TSMDocumentPropertyTag) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified TSMSetDocumentProperty(TSMDocumentID, TSMDocumentPropertyTag, UInt32, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func TSMSetDocumentProperty(_ docID: TSMDocumentID, _ propertyTag: TSMDocumentPropertyTag, _ propertySize: UInt32, _ propertyData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func TSMSetDocumentProperty(_ docID: TSMDocumentID, _ propertyTag: TSMDocumentPropertyTag, _ propertySize: UInt32, _ propertyData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.2 |

Modified TXNActionNameMapperProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias TXNActionNameMapperProcPtr = CFunctionPointer<((CFString!, UInt32, UnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` typealias TXNActionNameMapperProcPtr = CFunctionPointer<((CFString!, UInt32, UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified TXNContextualMenuSetupProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias TXNContextualMenuSetupProcPtr = CFunctionPointer<((Menu!, TXNObject, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias TXNContextualMenuSetupProcPtr = CFunctionPointer<((Menu!, TXNObject, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified TXNFindProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias TXNFindProcPtr = CFunctionPointer<((ConstUnsafePointer<TXNMatchTextRecord>, TXNDataType, TXNMatchOptions, ConstUnsafePointer<()>, TextEncoding, TXNOffset, ByteCount, UnsafePointer<TXNOffset>, UnsafePointer<TXNOffset>, UnsafePointer<Boolean>, URefCon) -> OSStatus)> ``` |
| To | ``` typealias TXNFindProcPtr = CFunctionPointer<((UnsafePointer<TXNMatchTextRecord>, TXNDataType, TXNMatchOptions, UnsafePointer<Void>, TextEncoding, TXNOffset, Int, UnsafeMutablePointer<TXNOffset>, UnsafeMutablePointer<TXNOffset>, UnsafeMutablePointer<Boolean>, URefCon) -> OSStatus)> ``` |

Modified TXNObjectRefcon

|  | Declaration |
| --- | --- |
| From | ``` typealias TXNObjectRefcon = UnsafePointer<()> ``` |
| To | ``` typealias TXNObjectRefcon = UnsafeMutablePointer<Void> ``` |

Modified TXNTypeRunAttributeSizes

|  | Declaration |
| --- | --- |
| From | ``` typealias TXNTypeRunAttributeSizes = ByteCount ``` |
| To | ``` typealias TXNTypeRunAttributeSizes = Int ``` |

Modified TextServiceInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias TextServiceInfoPtr = UnsafePointer<TextServiceInfo> ``` |
| To | ``` typealias TextServiceInfoPtr = UnsafeMutablePointer<TextServiceInfo> ``` |

Modified TextServiceListHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias TextServiceListHandle = UnsafePointer<TextServiceListPtr> ``` |
| To | ``` typealias TextServiceListHandle = UnsafeMutablePointer<TextServiceListPtr> ``` |

Modified TextServiceListPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias TextServiceListPtr = UnsafePointer<TextServiceList> ``` |
| To | ``` typealias TextServiceListPtr = UnsafeMutablePointer<TextServiceList> ``` |

Modified TextServicePropertyValue

|  | Declaration |
| --- | --- |
| From | ``` typealias TextServicePropertyValue = UnsafePointer<()> ``` |
| To | ``` typealias TextServicePropertyValue = UnsafeMutablePointer<Void> ``` |

Modified TextStyleHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias TextStyleHandle = UnsafePointer<TextStylePtr> ``` |
| To | ``` typealias TextStyleHandle = UnsafeMutablePointer<TextStylePtr> ``` |

Modified TextStylePtr

|  | Declaration |
| --- | --- |
| From | ``` typealias TextStylePtr = UnsafePointer<TextStyle> ``` |
| To | ``` typealias TextStylePtr = UnsafeMutablePointer<TextStyle> ``` |

Modified TextWidthHookProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias TextWidthHookProcPtr = CFunctionPointer<((UInt16, UInt16, UnsafePointer<()>, TEPtr, TEHandle) -> UInt16)> ``` |
| To | ``` typealias TextWidthHookProcPtr = CFunctionPointer<((UInt16, UInt16, UnsafeMutablePointer<Void>, TEPtr, TEHandle) -> UInt16)> ``` |

Modified ThemeButtonDrawInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ThemeButtonDrawInfoPtr = UnsafePointer<ThemeButtonDrawInfo> ``` |
| To | ``` typealias ThemeButtonDrawInfoPtr = UnsafeMutablePointer<ThemeButtonDrawInfo> ``` |

Modified ThemeButtonDrawProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ThemeButtonDrawProcPtr = CFunctionPointer<((ConstUnsafePointer<Rect>, ThemeButtonKind, ConstUnsafePointer<ThemeButtonDrawInfo>, URefCon, Int16, Boolean) -> Void)> ``` |
| To | ``` typealias ThemeButtonDrawProcPtr = CFunctionPointer<((UnsafePointer<Rect>, ThemeButtonKind, UnsafePointer<ThemeButtonDrawInfo>, URefCon, Int16, Boolean) -> Void)> ``` |

Modified ThemeEraseProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ThemeEraseProcPtr = CFunctionPointer<((ConstUnsafePointer<Rect>, URefCon, Int16, Boolean) -> Void)> ``` |
| To | ``` typealias ThemeEraseProcPtr = CFunctionPointer<((UnsafePointer<Rect>, URefCon, Int16, Boolean) -> Void)> ``` |

Modified ThemeTabTitleDrawProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ThemeTabTitleDrawProcPtr = CFunctionPointer<((ConstUnsafePointer<Rect>, ThemeTabStyle, ThemeTabDirection, Int16, Boolean, URefCon) -> Void)> ``` |
| To | ``` typealias ThemeTabTitleDrawProcPtr = CFunctionPointer<((UnsafePointer<Rect>, ThemeTabStyle, ThemeTabDirection, Int16, Boolean, URefCon) -> Void)> ``` |

Modified ThemeWindowMetricsPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ThemeWindowMetricsPtr = UnsafePointer<ThemeWindowMetrics> ``` |
| To | ``` typealias ThemeWindowMetricsPtr = UnsafeMutablePointer<ThemeWindowMetrics> ``` |

Modified ToolboxObjectClassRef

|  | Declaration |
| --- | --- |
| From | ``` typealias ToolboxObjectClassRef = ToolboxObjectClass ``` |
| To | ``` typealias ToolboxObjectClassRef = COpaquePointer ``` |

Modified TypesBlockPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias TypesBlockPtr = UnsafePointer<OSType> ``` |
| To | ``` typealias TypesBlockPtr = UnsafeMutablePointer<OSType> ``` |

Modified URLNotifyProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias URLNotifyProcPtr = CFunctionPointer<((UnsafePointer<()>, URLEvent, UnsafePointer<URLCallbackInfo>) -> OSStatus)> ``` |
| To | ``` typealias URLNotifyProcPtr = CFunctionPointer<((UnsafeMutablePointer<Void>, URLEvent, UnsafeMutablePointer<URLCallbackInfo>) -> OSStatus)> ``` |

Modified URLSystemEventProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias URLSystemEventProcPtr = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<EventRecord>) -> OSStatus)> ``` |
| To | ``` typealias URLSystemEventProcPtr = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<EventRecord>) -> OSStatus)> ``` |

Modified UnregisterEventHotKey(EventHotKeyRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func UnregisterEventHotKey(_ inHotKey: EventHotKey!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func UnregisterEventHotKey(_ inHotKey: EventHotKeyRef) -> OSStatus ``` | OS X 10.10.3 |

Modified UserEventUPP

|  | Declaration |
| --- | --- |
| From | ``` typealias UserEventUPP = UnsafePointer<()> ``` |
| To | ``` typealias UserEventUPP = UnsafeMutablePointer<Void> ``` |

Modified UserItemProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias UserItemProcPtr = CFunctionPointer<((Dialog!, DialogItemIndex) -> Void)> ``` |
| To | ``` typealias UserItemProcPtr = CFunctionPointer<((DialogRef, DialogItemIndex) -> Void)> ``` |

Modified WCTabHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias WCTabHandle = UnsafePointer<WCTabPtr> ``` |
| To | ``` typealias WCTabHandle = UnsafeMutablePointer<WCTabPtr> ``` |

Modified WCTabPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias WCTabPtr = UnsafePointer<WinCTab> ``` |
| To | ``` typealias WCTabPtr = UnsafeMutablePointer<WinCTab> ``` |

Modified WStateDataHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias WStateDataHandle = UnsafePointer<WStateDataPtr> ``` |
| To | ``` typealias WStateDataHandle = UnsafeMutablePointer<WStateDataPtr> ``` |

Modified WStateDataPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias WStateDataPtr = UnsafePointer<WStateData> ``` |
| To | ``` typealias WStateDataPtr = UnsafeMutablePointer<WStateData> ``` |

Modified WidthHookProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias WidthHookProcPtr = CFunctionPointer<((UInt16, UInt16, UnsafePointer<()>, TEPtr, TEHandle) -> UInt16)> ``` |
| To | ``` typealias WidthHookProcPtr = CFunctionPointer<((UInt16, UInt16, UnsafeMutablePointer<Void>, TEPtr, TEHandle) -> UInt16)> ``` |

Modified WindowDefSpecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias WindowDefSpecPtr = UnsafePointer<WindowDefSpec> ``` |
| To | ``` typealias WindowDefSpecPtr = UnsafeMutablePointer<WindowDefSpec> ``` |

Modified WindowDefUPP

|  | Declaration |
| --- | --- |
| From | ``` typealias WindowDefUPP = UnsafePointer<()> ``` |
| To | ``` typealias WindowDefUPP = UnsafeMutablePointer<Void> ``` |

Modified WindowGroupRef

|  | Declaration |
| --- | --- |
| From | ``` typealias WindowGroupRef = WindowGroup ``` |
| To | ``` typealias WindowGroupRef = COpaquePointer ``` |

Modified WindowPaintProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias WindowPaintProcPtr = CFunctionPointer<((GDHandle, GrafPtr, Window!, RgnHandle, RgnHandle, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias WindowPaintProcPtr = CFunctionPointer<((GDHandle, GrafPtr, WindowRef, RgnHandle, RgnHandle, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified WindowTitleDrawingProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias WindowTitleDrawingProcPtr = CFunctionPointer<((ConstUnsafePointer<Rect>, Int16, Boolean, URefCon) -> Void)> ``` |
| To | ``` typealias WindowTitleDrawingProcPtr = CFunctionPointer<((UnsafePointer<Rect>, Int16, Boolean, URefCon) -> Void)> ``` |

Modified kFCFontCGColorAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kFCFontFaceAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kFCFontFamilyAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kFCFontNameAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kFCFontSizeAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kFCFontVisibleNameAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kFontPanelATSUFontIDKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kFontPanelAttributeSizesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kFontPanelAttributeTagsKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kFontPanelAttributeValuesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kFontPanelAttributesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kFontPanelBackgroundColorAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kFontPanelFeatureSelectorsKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kFontPanelFeatureTypesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kFontPanelMouseTrackingState

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kFontPanelVariationAxesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kFontPanelVariationValuesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kHIDelegateAfterKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kHIDelegateBeforeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kHIObjectCustomDataCDEFProcIDKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kHIObjectCustomDataClassIDKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kHIObjectCustomDataDelegateGroupParametersKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kHIObjectCustomDataParameterNamesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kHIObjectCustomDataParameterTypesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kHIObjectCustomDataParameterValuesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kHIObjectCustomDataSuperClassIDKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kHIObjectInitParamDescription

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kHIObjectInitParamEventName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kHIObjectInitParamEventType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kHIObjectInitParamUserName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kHITextViewClassID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kHIToolboxVersionNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kHIViewMenuContentID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kHIViewWindowCloseBoxID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kHIViewWindowCollapseBoxID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kHIViewWindowContentID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kHIViewWindowGrowBoxID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kHIViewWindowTitleID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kHIViewWindowToolbarButtonID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kHIViewWindowToolbarID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kHIViewWindowZoomBoxID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICABluetoothAddressKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kICABluetoothTransportType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kICABonjourServiceNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICABonjourServiceTypeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICABonjourTXTRecordKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICACreationDateStringKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADataPropertyKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADataSizeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADataTypeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADeviceBrowserDeviceRefKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADeviceCapabilitiesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADeviceIconPathKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADeviceModulePathKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kICADevicePropArtist

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropBatteryLevel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropBurstInterval

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropBurstNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropCaptureDelay

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropCompressionSetting

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropContrast

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropCopyrightInfo

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropDateTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropDigitalZoom

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropEffectMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropExposureBiasCompensation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropExposureIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropExposureMeteringMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropExposureProgramMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropExposureTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropFNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropFlashMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropFocalLength

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropFocusDistance

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropFocusMeteringMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropFocusMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropFunctionalMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropImageSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropRGBGain

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropSharpness

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropStillCaptureMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropTimelapseInterval

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropTimelapseNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropUndefined

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropUploadURL

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicePropWhiteBalance

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADeviceSharedKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADeviceTypeCamera

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADeviceTypeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADeviceTypeScanner

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADeviceUsedKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADeviceWebSharedKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICADevicesArrayKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICAErrorKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICAExecutableArchitectureKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICAFireWireGUIDKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kICAFireWireTransportType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kICAIOServicePathKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kICAIPAddressKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kICAIPGUIDKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kICAIPNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kICAIPPortKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kICALockStatusKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICAMediaDurationInSecondsKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICAMediaHeightKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kICAMediaWidthKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kICAModificationDateStringKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationClassKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationClassPTPStandard

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationClassPTPVendor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationClassProprietary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationDataCookieKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationDataIsBigEndianKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationDataKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationDataSizeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationDeviceICAObjectKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationDeviceListICAObjectKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationICAObjectKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationImageBytesPerRowKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationImageDataKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationImageDataSizeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationImageHeightKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationImageKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationImageNumberOfRowsKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationImageStartRowKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationImageWidthKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationNumerOfImagesRemainingKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationPercentDownloadedKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationRawEventKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationScannerButtonTypeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationScannerDocumentNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationSubTypeDocumentLoaded

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kICANotificationSubTypeDocumentNotLoaded

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kICANotificationSubTypeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationSubTypePerformOverviewScan

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kICANotificationSubTypeWarmUpDone

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationSubTypeWarmUpStarted

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeCaptureComplete

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeDeviceAdded

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeDeviceConnectionProgress

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeDeviceInfoChanged

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeDevicePropertyChanged

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeDeviceRemoved

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeDeviceStatusError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeDeviceStatusInfo

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeDeviceWasReset

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeDownloadProgressStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeObjectAdded

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeObjectInfoChanged

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeObjectRemoved

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeProprietary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeRequestObjectTransfer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeScanProgressStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeScannerButtonPressed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeScannerOverviewOverlayAvailable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kICANotificationTypeScannerPageDone

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeScannerScanDone

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeScannerSessionClosed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeStoreAdded

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeStoreFull

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeStoreInfoChanged

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeStoreRemoved

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeTransactionCanceled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationTypeUnreportedStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICANotificationVendorErrorCodeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICAObjectKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICAObjectNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICARawKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICARefconKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICARemoteDeviceKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICASCSITransportType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kICATCPIPTransportType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kICATWAINDSPathKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kICATWAINTransportType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kICAThumbnailPropertyKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICAThumbnailSizeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICATransportTypeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kICAUSBLocationIDKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kICAUSBProductIDKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICAUSBTransportType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kICAUSBVendorIDKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kICAUserAssignedDeviceNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kMetaDataDictionaryKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISCategoryInkInputSource

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISCategoryKeyboardInputSource

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISCategoryPaletteInputSource

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISNotifyEnabledKeyboardInputSourcesChanged

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISNotifySelectedKeyboardInputSourceChanged

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISPropertyBundleID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISPropertyIconImageURL

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISPropertyIconRef

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISPropertyInputModeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISPropertyInputSourceCategory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISPropertyInputSourceID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISPropertyInputSourceIsASCIICapable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISPropertyInputSourceIsEnableCapable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISPropertyInputSourceIsEnabled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISPropertyInputSourceIsSelectCapable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISPropertyInputSourceIsSelected

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISPropertyInputSourceLanguages

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISPropertyInputSourceType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISPropertyLocalizedName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISPropertyUnicodeKeyLayoutData

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISTypeCharacterPalette

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISTypeInk

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISTypeKeyboardInputMethodModeEnabled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISTypeKeyboardInputMethodWithoutModes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISTypeKeyboardInputMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISTypeKeyboardLayout

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTISTypeKeyboardViewer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kTXNActionAlignCenter

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNActionAlignLeft

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNActionAlignRight

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNActionChangeColor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNActionChangeFont

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNActionChangeFontFeature

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNActionChangeFontVariation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNActionChangeGlyphVariation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNActionChangeSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNActionChangeStyle

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNActionChangeTextPosition

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNActionClear

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNActionCountOfAllChanges

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNActionCountOfStyleChanges

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNActionCountOfTextChanges

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNActionCut

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNActionDrop

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNActionMove

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNActionPaste

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNActionTyping

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNActionUndoLast

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNDataOptionCharacterEncodingKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNDataOptionDocumentTypeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNDocumentAttributeAuthorKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNDocumentAttributeCommentKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNDocumentAttributeCompanyNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNDocumentAttributeCopyrightKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNDocumentAttributeCreationTimeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNDocumentAttributeEditorKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNDocumentAttributeKeywordsKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNDocumentAttributeModificationTimeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNDocumentAttributeSubjectKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNDocumentAttributeTitleKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNMLTEDocumentType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNPlainTextDocumentType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNQuickTimeDocumentType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kTXNRTFDocumentType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

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
