---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/Carbon.html
archived_at: '2026-07-18T02:53:50.405508Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# Carbon Changes for Swift

### Carbon

Removed ICACloseSessionPB.init()Removed ICACloseSessionPB.init(header: ICAHeader, sessionID: ICASessionID)Removed ICACopyObjectDataPB.init()Removed ICACopyObjectDataPB.init(header: ICAHeader, object: ICAObject, startByte: Int, requestedSize: Int, data: UnsafeMutablePointer<Unmanaged<CFData>?>)Removed ICACopyObjectPropertyDictionaryPB.init()Removed ICACopyObjectPropertyDictionaryPB.init(header: ICAHeader, object: ICAObject, theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>)Removed ICACopyObjectThumbnailPB.init()Removed ICACopyObjectThumbnailPB.init(header: ICAHeader, object: ICAObject, thumbnailFormat: OSType, thumbnailData: UnsafeMutablePointer<Unmanaged<CFData>?>)Removed ICADownloadFilePB.init()Removed ICADownloadFilePB.init(header: ICAHeader, object: ICAObject, dirFSRef: UnsafeMutablePointer<FSRef>, flags: UInt32, fileType: OSType, fileCreator: OSType, rotationAngle: Fixed, fileFSRef: UnsafeMutablePointer<FSRef>)Removed ICAGetDeviceListPB.init()Removed ICAGetDeviceListPB.init(header: ICAHeader, object: ICAObject)Removed ICAHeader.init()Removed ICAHeader.init(err: ICAError, refcon: UInt)Removed ICAImportImagePB.init()Removed ICAImportImagePB.init(header: ICAHeader, deviceObject: ICAObject, flags: UInt32, supportedFileTypes: Unmanaged<CFArray>!, filterProc: ICAImportFilterProc!, importedImages: UnsafeMutablePointer<Unmanaged<CFArray>?>)Removed ICALoadDeviceModulePB.init()Removed ICALoadDeviceModulePB.init(header: ICAHeader, paramDictionary: Unmanaged<CFDictionary>!)Removed ICAMessage.init()Removed ICAMessage.init(messageType: OSType, startByte: UInt32, dataPtr: UnsafeMutablePointer<Void>, dataSize: UInt32, dataType: OSType)Removed ICAObjectInfo.init()Removed ICAObjectInfo.init(objectType: OSType, objectSubtype: OSType)Removed ICAObjectSendMessagePB.init()Removed ICAObjectSendMessagePB.init(header: ICAHeader, object: ICAObject, message: ICAMessage, result: UInt32)Removed ICAOpenSessionPB.init()Removed ICAOpenSessionPB.init(header: ICAHeader, deviceObject: ICAObject, sessionID: ICASessionID)Removed ICAPTPEventDataset.init()Removed ICAPTPEventDataset.init(dataLength: UInt32, containerType: UInt16, eventCode: UInt16, transactionID: UInt32, params: (UInt32, UInt32, UInt32))Removed ICAPTPPassThroughPB.init()Removed ICAPTPPassThroughPB.init(commandCode: UInt32, resultCode: UInt32, numOfInputParams: UInt32, numOfOutputParams: UInt32, params: (UInt32, UInt32, UInt32, UInt32), dataUsageMode: UInt32, flags: UInt32, dataSize: UInt32, data: (UInt8))Removed ICARegisterForEventNotificationPB.init()Removed ICARegisterForEventNotificationPB.init(header: ICAHeader, objectOfInterest: ICAObject, eventsOfInterest: Unmanaged<CFArray>!, notificationProc: ICANotification!, options: Unmanaged<CFDictionary>!)Removed ICAScannerCloseSessionPB.init()Removed ICAScannerCloseSessionPB.init(header: ICAHeader, sessionID: ICAScannerSessionID)Removed ICAScannerGetParametersPB.init()Removed ICAScannerGetParametersPB.init(header: ICAHeader, sessionID: ICAScannerSessionID, theDict: Unmanaged<CFMutableDictionary>!)Removed ICAScannerInitializePB.init()Removed ICAScannerInitializePB.init(header: ICAHeader, sessionID: ICAScannerSessionID)Removed ICAScannerOpenSessionPB.init()Removed ICAScannerOpenSessionPB.init(header: ICAHeader, object: ICAObject, sessionID: ICAScannerSessionID)Removed ICAScannerSetParametersPB.init()Removed ICAScannerSetParametersPB.init(header: ICAHeader, sessionID: ICAScannerSessionID, theDict: Unmanaged<CFMutableDictionary>!)Removed ICAScannerStartPB.init()Removed ICAScannerStartPB.init(header: ICAHeader, sessionID: ICAScannerSessionID)Removed ICAScannerStatusPB.init()Removed ICAScannerStatusPB.init(header: ICAHeader, sessionID: ICAScannerSessionID, status: UInt32)Removed ICASendNotificationPB.init()Removed ICASendNotificationPB.init(header: ICAHeader, notificationDictionary: Unmanaged<CFMutableDictionary>!, replyCode: UInt32)Removed ICAUnloadDeviceModulePB.init()Removed ICAUnloadDeviceModulePB.init(header: ICAHeader, deviceObject: ICAObject)Removed ICAUploadFilePB.init()Removed ICAUploadFilePB.init(header: ICAHeader, parentObject: ICAObject, fileFSRef: UnsafeMutablePointer<FSRef>, flags: UInt32)Removed ICD_DisposeObjectPB.init()Removed ICD_DisposeObjectPB.init(header: ICDHeader, object: ICAObject)Removed ICD_NewObjectPB.init()Removed ICD_NewObjectPB.init(header: ICDHeader, parentObject: ICAObject, objectInfo: ICAObjectInfo, object: ICAObject)Removed ICDHeader.init()Removed ICDHeader.init(err: ICAError, refcon: UInt)Added BasicWindowDescription.init(descriptionSize: UInt32, windowContentRect: Rect, windowZoomRect: Rect, windowRefCon: URefCon, windowStateFlags: UInt32, windowPositionMethod: WindowPositionMethod, windowDefinitionVersion: UInt32, windowDefinition: BasicWindowDescription.__Unnamed_union_windowDefinition)Added BasicWindowDescription.windowDefinitionAdded ControlImageContentInfo.init(contentType: ControlContentType, u: ControlImageContentInfo.__Unnamed_union_u)Added ControlImageContentInfo.uAdded DataBrowserAccessibilityItemInfo.init(version: UInt32, u: DataBrowserAccessibilityItemInfo.__Unnamed_union_u)Added DataBrowserAccessibilityItemInfo.uAdded DataBrowserCallbacks.init(version: UInt32, u: DataBrowserCallbacks.__Unnamed_union_u)Added DataBrowserCallbacks.uAdded DataBrowserCustomCallbacks.init(version: UInt32, u: DataBrowserCustomCallbacks.__Unnamed_union_u)Added DataBrowserCustomCallbacks.uAdded HICommand.init(attributes: UInt32, commandID: UInt32, menu: HICommand.__Unnamed_struct_menu)Added HICommand.menuAdded HICommandExtended.init(attributes: UInt32, commandID: UInt32, source: HICommandExtended.__Unnamed_union_source)Added HICommandExtended.sourceAdded HIThemeButtonDrawInfo.animationAdded HIThemeButtonDrawInfo.init(version: UInt32, state: ThemeDrawState, kind: ThemeButtonKind, value: ThemeButtonValue, adornment: ThemeButtonAdornment, animation: HIThemeButtonDrawInfo.__Unnamed_union_animation)Added HIThemeTrackDrawInfo.init(version: UInt32, kind: ThemeTrackKind, bounds: HIRect, min: Int32, max: Int32, value: Int32, reserved: UInt32, attributes: ThemeTrackAttributes, enableState: ThemeTrackEnableState, filler1: UInt8, trackInfo: HIThemeTrackDrawInfo.__Unnamed_union_trackInfo)Added HIThemeTrackDrawInfo.trackInfoAdded HIViewContentInfo.init(contentType: HIViewContentType, u: HIViewContentInfo.__Unnamed_union_u)Added HIViewContentInfo.uAdded HMHelpContent.init(contentType: HMContentType, u: HMHelpContent.__Unnamed_union_u)Added HMHelpContent.uAdded ICACloseSessionPB.init()Added ICACloseSessionPB.init(header: ICAHeader, sessionID: ICASessionID)Added ICACopyObjectDataPB.init()Added ICACopyObjectDataPB.init(header: ICAHeader, object: ICAObject, startByte: Int, requestedSize: Int, data: UnsafeMutablePointer<Unmanaged<CFData>?>)Added ICACopyObjectPropertyDictionaryPB.init()Added ICACopyObjectPropertyDictionaryPB.init(header: ICAHeader, object: ICAObject, theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>)Added ICACopyObjectThumbnailPB.init()Added ICACopyObjectThumbnailPB.init(header: ICAHeader, object: ICAObject, thumbnailFormat: OSType, thumbnailData: UnsafeMutablePointer<Unmanaged<CFData>?>)Added ICADownloadFilePB.init()Added ICADownloadFilePB.init(header: ICAHeader, object: ICAObject, dirFSRef: UnsafeMutablePointer<FSRef>, flags: UInt32, fileType: OSType, fileCreator: OSType, rotationAngle: Fixed, fileFSRef: UnsafeMutablePointer<FSRef>)Added ICAGetDeviceListPB.init()Added ICAGetDeviceListPB.init(header: ICAHeader, object: ICAObject)Added ICAHeader.init()Added ICAHeader.init(err: ICAError, refcon: UInt)Added ICAImportImagePB.init()Added ICAImportImagePB.init(header: ICAHeader, deviceObject: ICAObject, flags: UInt32, supportedFileTypes: Unmanaged<CFArray>!, filterProc: ICAImportFilterProc!, importedImages: UnsafeMutablePointer<Unmanaged<CFArray>?>)Added ICALoadDeviceModulePB.init()Added ICALoadDeviceModulePB.init(header: ICAHeader, paramDictionary: Unmanaged<CFDictionary>!)Added ICAMessage.init()Added ICAMessage.init(messageType: OSType, startByte: UInt32, dataPtr: UnsafeMutablePointer<Void>, dataSize: UInt32, dataType: OSType)Added ICAObjectInfo.init()Added ICAObjectInfo.init(objectType: OSType, objectSubtype: OSType)Added ICAObjectSendMessagePB.init()Added ICAObjectSendMessagePB.init(header: ICAHeader, object: ICAObject, message: ICAMessage, result: UInt32)Added ICAOpenSessionPB.init()Added ICAOpenSessionPB.init(header: ICAHeader, deviceObject: ICAObject, sessionID: ICASessionID)Added ICAPTPEventDataset.init()Added ICAPTPEventDataset.init(dataLength: UInt32, containerType: UInt16, eventCode: UInt16, transactionID: UInt32, params: (UInt32, UInt32, UInt32))Added ICAPTPPassThroughPB.init()Added ICAPTPPassThroughPB.init(commandCode: UInt32, resultCode: UInt32, numOfInputParams: UInt32, numOfOutputParams: UInt32, params: (UInt32, UInt32, UInt32, UInt32), dataUsageMode: UInt32, flags: UInt32, dataSize: UInt32, data: (UInt8))Added ICARegisterForEventNotificationPB.init()Added ICARegisterForEventNotificationPB.init(header: ICAHeader, objectOfInterest: ICAObject, eventsOfInterest: Unmanaged<CFArray>!, notificationProc: ICANotification!, options: Unmanaged<CFDictionary>!)Added ICAScannerCloseSessionPB.init()Added ICAScannerCloseSessionPB.init(header: ICAHeader, sessionID: ICAScannerSessionID)Added ICAScannerGetParametersPB.init()Added ICAScannerGetParametersPB.init(header: ICAHeader, sessionID: ICAScannerSessionID, theDict: Unmanaged<CFMutableDictionary>!)Added ICAScannerInitializePB.init()Added ICAScannerInitializePB.init(header: ICAHeader, sessionID: ICAScannerSessionID)Added ICAScannerOpenSessionPB.init()Added ICAScannerOpenSessionPB.init(header: ICAHeader, object: ICAObject, sessionID: ICAScannerSessionID)Added ICAScannerSetParametersPB.init()Added ICAScannerSetParametersPB.init(header: ICAHeader, sessionID: ICAScannerSessionID, theDict: Unmanaged<CFMutableDictionary>!)Added ICAScannerStartPB.init()Added ICAScannerStartPB.init(header: ICAHeader, sessionID: ICAScannerSessionID)Added ICAScannerStatusPB.init()Added ICAScannerStatusPB.init(header: ICAHeader, sessionID: ICAScannerSessionID, status: UInt32)Added ICASendNotificationPB.init()Added ICASendNotificationPB.init(header: ICAHeader, notificationDictionary: Unmanaged<CFMutableDictionary>!, replyCode: UInt32)Added ICAUnloadDeviceModulePB.init()Added ICAUnloadDeviceModulePB.init(header: ICAHeader, deviceObject: ICAObject)Added ICAUploadFilePB.init()Added ICAUploadFilePB.init(header: ICAHeader, parentObject: ICAObject, fileFSRef: UnsafeMutablePointer<FSRef>, flags: UInt32)Added ICD_DisposeObjectPB.init()Added ICD_DisposeObjectPB.init(header: ICDHeader, object: ICAObject)Added ICD_NewObjectPB.init()Added ICD_NewObjectPB.init(header: ICDHeader, parentObject: ICAObject, objectInfo: ICAObjectInfo, object: ICAObject)Added ICDHeader.init()Added ICDHeader.init(err: ICAError, refcon: UInt)Added ListDefSpec.init(defType: ListDefType, u: ListDefSpec.__Unnamed_union_u)Added ListDefSpec.uAdded MenuDefSpec.init(defType: MenuDefType, u: MenuDefSpec.__Unnamed_union_u)Added MenuDefSpec.uAdded NavFileOrFolderInfo.fileAndFolderAdded NavFileOrFolderInfo.init(version: UInt16, isFolder: DarwinBoolean, visible: DarwinBoolean, creationDate: UInt32, modificationDate: UInt32, fileAndFolder: NavFileOrFolderInfo.__Unnamed_union_fileAndFolder)Added ThemeTrackDrawInfo.init(kind: ThemeTrackKind, bounds: Rect, min: Int32, max: Int32, value: Int32, reserved: UInt32, attributes: ThemeTrackAttributes, enableState: ThemeTrackEnableState, filler1: UInt8, trackInfo: ThemeTrackDrawInfo.__Unnamed_union_trackInfo)Added ThemeTrackDrawInfo.trackInfoAdded WindowDefSpec.init(defType: WindowDefType, u: WindowDefSpec.__Unnamed_union_u)Added WindowDefSpec.uModified BasicWindowDescription [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BasicWindowDescription {     var descriptionSize: UInt32     var windowContentRect: Rect     var windowZoomRect: Rect     var windowRefCon: URefCon     var windowStateFlags: UInt32     var windowPositionMethod: WindowPositionMethod     var windowDefinitionVersion: UInt32     init() } ``` |
| To | ``` struct BasicWindowDescription {     struct __Unnamed_union_windowDefinition {         struct __Unnamed_struct_versionOne {             var windowDefProc: Int16             var windowHasCloseBox: DarwinBoolean             init()             init(windowDefProc windowDefProc: Int16, windowHasCloseBox windowHasCloseBox: DarwinBoolean)         }         struct __Unnamed_struct_versionTwo {             var windowClass: WindowClass             var windowAttributes: WindowAttributes             init()             init(windowClass windowClass: WindowClass, windowAttributes windowAttributes: WindowAttributes)         }         var versionOne: BasicWindowDescription.__Unnamed_union_windowDefinition.__Unnamed_struct_versionOne         var versionTwo: BasicWindowDescription.__Unnamed_union_windowDefinition.__Unnamed_struct_versionTwo         init(versionOne versionOne: BasicWindowDescription.__Unnamed_union_windowDefinition.__Unnamed_struct_versionOne)         init(versionTwo versionTwo: BasicWindowDescription.__Unnamed_union_windowDefinition.__Unnamed_struct_versionTwo)         init()     }     var descriptionSize: UInt32     var windowContentRect: Rect     var windowZoomRect: Rect     var windowRefCon: URefCon     var windowStateFlags: UInt32     var windowPositionMethod: WindowPositionMethod     var windowDefinitionVersion: UInt32     var windowDefinition: BasicWindowDescription.__Unnamed_union_windowDefinition     init()     init(descriptionSize descriptionSize: UInt32, windowContentRect windowContentRect: Rect, windowZoomRect windowZoomRect: Rect, windowRefCon windowRefCon: URefCon, windowStateFlags windowStateFlags: UInt32, windowPositionMethod windowPositionMethod: WindowPositionMethod, windowDefinitionVersion windowDefinitionVersion: UInt32, windowDefinition windowDefinition: BasicWindowDescription.__Unnamed_union_windowDefinition) } ``` |

Modified Control

|  | Name | Declaration |
| --- | --- | --- |
| From | ControlRef | ``` typealias ControlRef = Control ``` |
| To | Control | ``` class Control { } ``` |

Modified ControlImageContentInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ControlImageContentInfo {     var contentType: ControlContentType     init() } ``` |
| To | ``` struct ControlImageContentInfo {     struct __Unnamed_union_u {         var resID: Int16         var iconRef: IconRef         var imageRef: Unmanaged<CGImage>!         init(resID resID: Int16)         init(iconRef iconRef: IconRef)         init(imageRef imageRef: Unmanaged<CGImage>!)         init()     }     var contentType: ControlContentType     var u: ControlImageContentInfo.__Unnamed_union_u     init()     init(contentType contentType: ControlContentType, u u: ControlImageContentInfo.__Unnamed_union_u) } ``` |

Modified DataBrowserAccessibilityItemInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DataBrowserAccessibilityItemInfo {     var version: UInt32     init() } ``` |
| To | ``` struct DataBrowserAccessibilityItemInfo {     struct __Unnamed_union_u {         var v0: DataBrowserAccessibilityItemInfoV0         var v1: DataBrowserAccessibilityItemInfoV1         init(v0 v0: DataBrowserAccessibilityItemInfoV0)         init(v1 v1: DataBrowserAccessibilityItemInfoV1)         init()     }     var version: UInt32     var u: DataBrowserAccessibilityItemInfo.__Unnamed_union_u     init()     init(version version: UInt32, u u: DataBrowserAccessibilityItemInfo.__Unnamed_union_u) } ``` |

Modified DataBrowserCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DataBrowserCallbacks {     var version: UInt32     init() } ``` |
| To | ``` struct DataBrowserCallbacks {     struct __Unnamed_union_u {         struct __Unnamed_struct_v1 {             var itemDataCallback: DataBrowserItemDataUPP!             var itemCompareCallback: DataBrowserItemCompareUPP!             var itemNotificationCallback: DataBrowserItemNotificationUPP!             var addDragItemCallback: DataBrowserAddDragItemUPP!             var acceptDragCallback: DataBrowserAcceptDragUPP!             var receiveDragCallback: DataBrowserReceiveDragUPP!             var postProcessDragCallback: DataBrowserPostProcessDragUPP!             var itemHelpContentCallback: DataBrowserItemHelpContentUPP!             var getContextualMenuCallback: DataBrowserGetContextualMenuUPP!             var selectContextualMenuCallback: DataBrowserSelectContextualMenuUPP!             init()             init(itemDataCallback itemDataCallback: DataBrowserItemDataUPP!, itemCompareCallback itemCompareCallback: DataBrowserItemCompareUPP!, itemNotificationCallback itemNotificationCallback: DataBrowserItemNotificationUPP!, addDragItemCallback addDragItemCallback: DataBrowserAddDragItemUPP!, acceptDragCallback acceptDragCallback: DataBrowserAcceptDragUPP!, receiveDragCallback receiveDragCallback: DataBrowserReceiveDragUPP!, postProcessDragCallback postProcessDragCallback: DataBrowserPostProcessDragUPP!, itemHelpContentCallback itemHelpContentCallback: DataBrowserItemHelpContentUPP!, getContextualMenuCallback getContextualMenuCallback: DataBrowserGetContextualMenuUPP!, selectContextualMenuCallback selectContextualMenuCallback: DataBrowserSelectContextualMenuUPP!)         }         var v1: DataBrowserCallbacks.__Unnamed_union_u.__Unnamed_struct_v1         init(v1 v1: DataBrowserCallbacks.__Unnamed_union_u.__Unnamed_struct_v1)         init()     }     var version: UInt32     var u: DataBrowserCallbacks.__Unnamed_union_u     init()     init(version version: UInt32, u u: DataBrowserCallbacks.__Unnamed_union_u) } ``` |

Modified DataBrowserCustomCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DataBrowserCustomCallbacks {     var version: UInt32     init() } ``` |
| To | ``` struct DataBrowserCustomCallbacks {     struct __Unnamed_union_u {         struct __Unnamed_struct_v1 {             var drawItemCallback: DataBrowserDrawItemUPP!             var editTextCallback: DataBrowserEditItemUPP!             var hitTestCallback: DataBrowserHitTestUPP!             var trackingCallback: DataBrowserTrackingUPP!             var dragRegionCallback: DataBrowserItemDragRgnUPP!             var acceptDragCallback: DataBrowserItemAcceptDragUPP!             var receiveDragCallback: DataBrowserItemReceiveDragUPP!             init()             init(drawItemCallback drawItemCallback: DataBrowserDrawItemUPP!, editTextCallback editTextCallback: DataBrowserEditItemUPP!, hitTestCallback hitTestCallback: DataBrowserHitTestUPP!, trackingCallback trackingCallback: DataBrowserTrackingUPP!, dragRegionCallback dragRegionCallback: DataBrowserItemDragRgnUPP!, acceptDragCallback acceptDragCallback: DataBrowserItemAcceptDragUPP!, receiveDragCallback receiveDragCallback: DataBrowserItemReceiveDragUPP!)         }         var v1: DataBrowserCustomCallbacks.__Unnamed_union_u.__Unnamed_struct_v1         init(v1 v1: DataBrowserCustomCallbacks.__Unnamed_union_u.__Unnamed_struct_v1)         init()     }     var version: UInt32     var u: DataBrowserCustomCallbacks.__Unnamed_union_u     init()     init(version version: UInt32, u u: DataBrowserCustomCallbacks.__Unnamed_union_u) } ``` |

Modified EventLoopTimer

|  | Name | Declaration |
| --- | --- | --- |
| From | EventLoopTimerRef | ``` typealias EventLoopTimerRef = EventLoopTimer ``` |
| To | EventLoopTimer | ``` class EventLoopTimer { } ``` |

Modified EventRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct EventRecord {     var what: EventKind     var message: UInt     var when: UInt32     var `where`: Point     var modifiers: EventModifiers     init()     init(what what: EventKind, message message: UInt, when when: UInt32, `where` `where`: Point, modifiers modifiers: EventModifiers) } ``` |
| To | ``` struct EventRecord {     var what: EventKind     var message: UInt     var when: UInt32     var `where`: Point     var modifiers: EventModifiers     init()     init(what what: EventKind, message message: UInt, when when: UInt32, where where: Point, modifiers modifiers: EventModifiers) } ``` |

Modified EventRecord.init(what: EventKind, message: UInt, when: UInt32, where: Point, modifiers: EventModifiers)

|  | Declaration |
| --- | --- |
| From | ``` init(what what: EventKind, message message: UInt, when when: UInt32, `where` `where`: Point, modifiers modifiers: EventModifiers) ``` |
| To | ``` init(what what: EventKind, message message: UInt, when when: UInt32, where where: Point, modifiers modifiers: EventModifiers) ``` |

Modified FCFontDescriptor

|  | Name | Declaration |
| --- | --- | --- |
| From | FCFontDescriptorRef | ``` typealias FCFontDescriptorRef = FCFontDescriptor ``` |
| To | FCFontDescriptor | ``` class FCFontDescriptor { } ``` |

Modified HIArchive

|  | Name | Declaration |
| --- | --- | --- |
| From | HIArchiveRef | ``` typealias HIArchiveRef = HIArchive ``` |
| To | HIArchive | ``` class HIArchive { } ``` |

Modified HICommand [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HICommand {     var attributes: UInt32     var commandID: UInt32     init() } ``` |
| To | ``` struct HICommand {     struct __Unnamed_struct_menu {         var menuRef: Unmanaged<Menu>!         var menuItemIndex: MenuItemIndex         init()         init(menuRef menuRef: Unmanaged<Menu>!, menuItemIndex menuItemIndex: MenuItemIndex)     }     var attributes: UInt32     var commandID: UInt32     var menu: HICommand.__Unnamed_struct_menu     init()     init(attributes attributes: UInt32, commandID commandID: UInt32, menu menu: HICommand.__Unnamed_struct_menu) } ``` |

Modified HICommandExtended [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HICommandExtended {     var attributes: UInt32     var commandID: UInt32     init() } ``` |
| To | ``` struct HICommandExtended {     struct __Unnamed_union_source {         struct __Unnamed_struct_menu {             var menuRef: Unmanaged<Menu>!             var menuItemIndex: MenuItemIndex             init()             init(menuRef menuRef: Unmanaged<Menu>!, menuItemIndex menuItemIndex: MenuItemIndex)         }         var control: Unmanaged<Control>!         var window: WindowRef         var menu: HICommandExtended.__Unnamed_union_source.__Unnamed_struct_menu         init(control control: Unmanaged<Control>!)         init(window window: WindowRef)         init(menu menu: HICommandExtended.__Unnamed_union_source.__Unnamed_struct_menu)         init()     }     var attributes: UInt32     var commandID: UInt32     var source: HICommandExtended.__Unnamed_union_source     init()     init(attributes attributes: UInt32, commandID commandID: UInt32, source source: HICommandExtended.__Unnamed_union_source) } ``` |

Modified HIObject

|  | Name | Declaration |
| --- | --- | --- |
| From | HIObjectRef | ``` typealias HIObjectRef = HIObject ``` |
| To | HIObject | ``` class HIObject { } ``` |

Modified HIObjectClass

|  | Name | Declaration |
| --- | --- | --- |
| From | HIObjectClassRef | ``` typealias HIObjectClassRef = HIObjectClass ``` |
| To | HIObjectClass | ``` class HIObjectClass { } ``` |

Modified HIThemeButtonDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeButtonDrawInfo {     var version: UInt32     var state: ThemeDrawState     var kind: ThemeButtonKind     var value: ThemeButtonValue     var adornment: ThemeButtonAdornment     init() } ``` |
| To | ``` struct HIThemeButtonDrawInfo {     struct __Unnamed_union_animation {         var time: HIThemeAnimationTimeInfo         var frame: HIThemeAnimationFrameInfo         init(time time: HIThemeAnimationTimeInfo)         init(frame frame: HIThemeAnimationFrameInfo)         init()     }     var version: UInt32     var state: ThemeDrawState     var kind: ThemeButtonKind     var value: ThemeButtonValue     var adornment: ThemeButtonAdornment     var animation: HIThemeButtonDrawInfo.__Unnamed_union_animation     init()     init(version version: UInt32, state state: ThemeDrawState, kind kind: ThemeButtonKind, value value: ThemeButtonValue, adornment adornment: ThemeButtonAdornment, animation animation: HIThemeButtonDrawInfo.__Unnamed_union_animation) } ``` |

Modified HIThemeTrackDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIThemeTrackDrawInfo {     var version: UInt32     var kind: ThemeTrackKind     var bounds: HIRect     var min: Int32     var max: Int32     var value: Int32     var reserved: UInt32     var attributes: ThemeTrackAttributes     var enableState: ThemeTrackEnableState     var filler1: UInt8     init() } ``` |
| To | ``` struct HIThemeTrackDrawInfo {     struct __Unnamed_union_trackInfo {         var scrollbar: ScrollBarTrackInfo         var slider: SliderTrackInfo         var progress: ProgressTrackInfo         init(scrollbar scrollbar: ScrollBarTrackInfo)         init(slider slider: SliderTrackInfo)         init(progress progress: ProgressTrackInfo)         init()     }     var version: UInt32     var kind: ThemeTrackKind     var bounds: HIRect     var min: Int32     var max: Int32     var value: Int32     var reserved: UInt32     var attributes: ThemeTrackAttributes     var enableState: ThemeTrackEnableState     var filler1: UInt8     var trackInfo: HIThemeTrackDrawInfo.__Unnamed_union_trackInfo     init()     init(version version: UInt32, kind kind: ThemeTrackKind, bounds bounds: HIRect, min min: Int32, max max: Int32, value value: Int32, reserved reserved: UInt32, attributes attributes: ThemeTrackAttributes, enableState enableState: ThemeTrackEnableState, filler1 filler1: UInt8, trackInfo trackInfo: HIThemeTrackDrawInfo.__Unnamed_union_trackInfo) } ``` |

Modified HIViewContentInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HIViewContentInfo {     var contentType: HIViewContentType     init() } ``` |
| To | ``` struct HIViewContentInfo {     struct __Unnamed_union_u {         var iconRef: IconRef         var iconTypeAndCreator: HITypeAndCreator         var imageRef: Unmanaged<CGImage>!         var imageResource: Unmanaged<CFString>!         var imageFile: Unmanaged<CFURL>!         init(iconRef iconRef: IconRef)         init(iconTypeAndCreator iconTypeAndCreator: HITypeAndCreator)         init(imageRef imageRef: Unmanaged<CGImage>!)         init(imageResource imageResource: Unmanaged<CFString>!)         init(imageFile imageFile: Unmanaged<CFURL>!)         init()     }     var contentType: HIViewContentType     var u: HIViewContentInfo.__Unnamed_union_u     init()     init(contentType contentType: HIViewContentType, u u: HIViewContentInfo.__Unnamed_union_u) } ``` |

Modified HMHelpContent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HMHelpContent {     var contentType: HMContentType     init() } ``` |
| To | ``` struct HMHelpContent {     struct __Unnamed_union_u {         var tagCFString: Unmanaged<CFString>!         var tagString: Str255         var tagStringRes: HMStringResType         var tagTEHandle: TEHandle         var tagTextRes: Int16         var tagStrRes: Int16         init(tagCFString tagCFString: Unmanaged<CFString>!)         init(tagString tagString: Str255)         init(tagStringRes tagStringRes: HMStringResType)         init(tagTEHandle tagTEHandle: TEHandle)         init(tagTextRes tagTextRes: Int16)         init(tagStrRes tagStrRes: Int16)         init()     }     var contentType: HMContentType     var u: HMHelpContent.__Unnamed_union_u     init()     init(contentType contentType: HMContentType, u u: HMHelpContent.__Unnamed_union_u) } ``` |

Modified InkStroke

|  | Name | Declaration |
| --- | --- | --- |
| From | InkStrokeRef | ``` typealias InkStrokeRef = InkStroke ``` |
| To | InkStroke | ``` class InkStroke { } ``` |

Modified InkText

|  | Name | Declaration |
| --- | --- | --- |
| From | InkTextRef | ``` typealias InkTextRef = InkText ``` |
| To | InkText | ``` class InkText { } ``` |

Modified ListDefSpec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ListDefSpec {     var defType: ListDefType     init() } ``` |
| To | ``` struct ListDefSpec {     struct __Unnamed_union_u {         var userProc: ListDefUPP!         init(userProc userProc: ListDefUPP!)         init()     }     var defType: ListDefType     var u: ListDefSpec.__Unnamed_union_u     init()     init(defType defType: ListDefType, u u: ListDefSpec.__Unnamed_union_u) } ``` |

Modified Menu

|  | Name | Declaration |
| --- | --- | --- |
| From | MenuRef | ``` typealias MenuRef = Menu ``` |
| To | Menu | ``` class Menu { } ``` |

Modified MenuDefSpec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MenuDefSpec {     var defType: MenuDefType     init() } ``` |
| To | ``` struct MenuDefSpec {     struct __Unnamed_union_u {         struct __Unnamed_struct_view {             var classID: Unmanaged<CFString>!             var initEvent: EventRef             init()             init(classID classID: Unmanaged<CFString>!, initEvent initEvent: EventRef)         }         var defProc: MenuDefUPP         var view: MenuDefSpec.__Unnamed_union_u.__Unnamed_struct_view         init(defProc defProc: MenuDefUPP)         init(view view: MenuDefSpec.__Unnamed_union_u.__Unnamed_struct_view)         init()     }     var defType: MenuDefType     var u: MenuDefSpec.__Unnamed_union_u     init()     init(defType defType: MenuDefType, u u: MenuDefSpec.__Unnamed_union_u) } ``` |

Modified NavDialog

|  | Name | Declaration |
| --- | --- | --- |
| From | NavDialogRef | ``` typealias NavDialogRef = NavDialog ``` |
| To | NavDialog | ``` class NavDialog { } ``` |

Modified NavFileOrFolderInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NavFileOrFolderInfo {     var version: UInt16     var isFolder: DarwinBoolean     var visible: DarwinBoolean     var creationDate: UInt32     var modificationDate: UInt32     init() } ``` |
| To | ``` struct NavFileOrFolderInfo {     struct __Unnamed_union_fileAndFolder {         struct __Unnamed_struct_fileInfo {             var locked: DarwinBoolean             var resourceOpen: DarwinBoolean             var dataOpen: DarwinBoolean             var reserved1: DarwinBoolean             var dataSize: Int             var resourceSize: Int             var finderInfo: FInfo             var finderXInfo: FXInfo             init()             init(locked locked: DarwinBoolean, resourceOpen resourceOpen: DarwinBoolean, dataOpen dataOpen: DarwinBoolean, reserved1 reserved1: DarwinBoolean, dataSize dataSize: Int, resourceSize resourceSize: Int, finderInfo finderInfo: FInfo, finderXInfo finderXInfo: FXInfo)         }         struct __Unnamed_struct_folderInfo {             var shareable: DarwinBoolean             var sharePoint: DarwinBoolean             var mounted: DarwinBoolean             var readable: DarwinBoolean             var writeable: DarwinBoolean             var reserved2: DarwinBoolean             var numberOfFiles: Int             var finderDInfo: DInfo             var finderDXInfo: DXInfo             var folderType: OSType             var folderCreator: OSType             var reserved3: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)             init()             init(shareable shareable: DarwinBoolean, sharePoint sharePoint: DarwinBoolean, mounted mounted: DarwinBoolean, readable readable: DarwinBoolean, writeable writeable: DarwinBoolean, reserved2 reserved2: DarwinBoolean, numberOfFiles numberOfFiles: Int, finderDInfo finderDInfo: DInfo, finderDXInfo finderDXInfo: DXInfo, folderType folderType: OSType, folderCreator folderCreator: OSType, reserved3 reserved3: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))         }         var fileInfo: NavFileOrFolderInfo.__Unnamed_union_fileAndFolder.__Unnamed_struct_fileInfo         var folderInfo: NavFileOrFolderInfo.__Unnamed_union_fileAndFolder.__Unnamed_struct_folderInfo         init(fileInfo fileInfo: NavFileOrFolderInfo.__Unnamed_union_fileAndFolder.__Unnamed_struct_fileInfo)         init(folderInfo folderInfo: NavFileOrFolderInfo.__Unnamed_union_fileAndFolder.__Unnamed_struct_folderInfo)         init()     }     var version: UInt16     var isFolder: DarwinBoolean     var visible: DarwinBoolean     var creationDate: UInt32     var modificationDate: UInt32     var fileAndFolder: NavFileOrFolderInfo.__Unnamed_union_fileAndFolder     init()     init(version version: UInt16, isFolder isFolder: DarwinBoolean, visible visible: DarwinBoolean, creationDate creationDate: UInt32, modificationDate modificationDate: UInt32, fileAndFolder fileAndFolder: NavFileOrFolderInfo.__Unnamed_union_fileAndFolder) } ``` |

Modified ThemeTrackDrawInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ThemeTrackDrawInfo {     var kind: ThemeTrackKind     var bounds: Rect     var min: Int32     var max: Int32     var value: Int32     var reserved: UInt32     var attributes: ThemeTrackAttributes     var enableState: ThemeTrackEnableState     var filler1: UInt8     init() } ``` |
| To | ``` struct ThemeTrackDrawInfo {     struct __Unnamed_union_trackInfo {         var scrollbar: ScrollBarTrackInfo         var slider: SliderTrackInfo         var progress: ProgressTrackInfo         init(scrollbar scrollbar: ScrollBarTrackInfo)         init(slider slider: SliderTrackInfo)         init(progress progress: ProgressTrackInfo)         init()     }     var kind: ThemeTrackKind     var bounds: Rect     var min: Int32     var max: Int32     var value: Int32     var reserved: UInt32     var attributes: ThemeTrackAttributes     var enableState: ThemeTrackEnableState     var filler1: UInt8     var trackInfo: ThemeTrackDrawInfo.__Unnamed_union_trackInfo     init()     init(kind kind: ThemeTrackKind, bounds bounds: Rect, min min: Int32, max max: Int32, value value: Int32, reserved reserved: UInt32, attributes attributes: ThemeTrackAttributes, enableState enableState: ThemeTrackEnableState, filler1 filler1: UInt8, trackInfo trackInfo: ThemeTrackDrawInfo.__Unnamed_union_trackInfo) } ``` |

Modified TISInputSource

|  | Name | Declaration |
| --- | --- | --- |
| From | TISInputSourceRef | ``` typealias TISInputSourceRef = TISInputSource ``` |
| To | TISInputSource | ``` class TISInputSource { } ``` |

Modified WindowDefSpec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct WindowDefSpec {     var defType: WindowDefType     init() } ``` |
| To | ``` struct WindowDefSpec {     struct __Unnamed_union_u {         var defProc: WindowDefUPP         var classRef: UnsafeMutablePointer<Void>         var procID: Int16         var rootView: UnsafeMutablePointer<Void>         init(defProc defProc: WindowDefUPP)         init(classRef classRef: UnsafeMutablePointer<Void>)         init(procID procID: Int16)         init(rootView rootView: UnsafeMutablePointer<Void>)         init()     }     var defType: WindowDefType     var u: WindowDefSpec.__Unnamed_union_u     init()     init(defType defType: WindowDefType, u u: WindowDefSpec.__Unnamed_union_u) } ``` |

Modified ControlHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias ControlHandle = ControlHandle ``` |
| To | ``` typealias ControlHandle = ControlRef ``` |

Modified GetColor(_: Point, _: ConstStr255Param, _: UnsafePointer<RGBColor>, _: UnsafeMutablePointer<RGBColor>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func GetColor(_ `where`: Point, _ prompt: ConstStr255Param, _ inColor: UnsafePointer<RGBColor>, _ outColor: UnsafeMutablePointer<RGBColor>) -> Bool ``` |
| To | ``` func GetColor(_ where: Point, _ prompt: ConstStr255Param, _ inColor: UnsafePointer<RGBColor>, _ outColor: UnsafeMutablePointer<RGBColor>) -> Bool ``` |

Modified HIToolbar

|  | Declaration |
| --- | --- |
| From | ``` typealias HIToolbarRef = HIToolbar ``` |
| To | ``` typealias HIToolbar = HIObjectRef ``` |

Modified HIToolbarItem

|  | Declaration |
| --- | --- |
| From | ``` typealias HIToolbarItemRef = HIToolbarItem ``` |
| To | ``` typealias HIToolbarItem = HIObjectRef ``` |

Modified InvokeControlUserPaneHitTestUPP(_: Control!, _: Point, _: ControlUserPaneHitTestUPP!) -> ControlPartCode

|  | Declaration |
| --- | --- |
| From | ``` func InvokeControlUserPaneHitTestUPP(_ control: Control!, _ `where`: Point, _ userUPP: ControlUserPaneHitTestUPP!) -> ControlPartCode ``` |
| To | ``` func InvokeControlUserPaneHitTestUPP(_ control: Control!, _ where: Point, _ userUPP: ControlUserPaneHitTestUPP!) -> ControlPartCode ``` |

Modified MenuHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias MenuHandle = MenuHandle ``` |
| To | ``` typealias MenuHandle = MenuRef ``` |

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
