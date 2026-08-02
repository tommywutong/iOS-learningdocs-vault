---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/CoreGraphics.html
archived_at: '2026-07-18T02:53:25.710683Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreGraphics Changes for Swift

### CoreGraphics

Removed CGBitmapInfo.init(_: UInt32)Removed CGBlendMode.init(_: UInt32)Removed CGBlendMode.valueRemoved CGColorRenderingIntent.init(_: UInt32)Removed CGColorRenderingIntent.valueRemoved CGColorSpaceModel.init(_: Int32)Removed CGColorSpaceModel.valueRemoved CGDataConsumerCallbacks.init(putBytes: CGDataConsumerPutBytesCallback, releaseConsumer: CGDataConsumerReleaseInfoCallback)Removed CGDataProviderDirectCallbacks.init(version: UInt32, getBytePointer: CGDataProviderGetBytePointerCallback, releaseBytePointer: CGDataProviderReleaseBytePointerCallback, getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback, releaseInfo: CGDataProviderReleaseInfoCallback)Removed CGDataProviderSequentialCallbacks.init(version: UInt32, getBytes: CGDataProviderGetBytesCallback, skipForward: CGDataProviderSkipForwardCallback, rewind: CGDataProviderRewindCallback, releaseInfo: CGDataProviderReleaseInfoCallback)Removed CGFloat.encode() -> [Word]Removed CGFloat.getMirror() -> MirrorTypeRemoved CGFontPostScriptFormat.init(_: UInt32)Removed CGFontPostScriptFormat.valueRemoved CGFunctionCallbacks.init(version: UInt32, evaluate: CGFunctionEvaluateCallback, releaseInfo: CGFunctionReleaseInfoCallback)Removed CGInterpolationQuality.init(_: UInt32)Removed CGInterpolationQuality.valueRemoved CGLineCap.init(_: UInt32)Removed CGLineCap.valueRemoved CGLineJoin.init(_: UInt32)Removed CGLineJoin.valueRemoved CGPathDrawingMode.init(_: UInt32)Removed CGPathDrawingMode.valueRemoved CGPathElement.init()Removed CGPathElement.init(type: CGPathElementType, points: UnsafeMutablePointer<CGPoint>)Removed CGPathElementType.init(_: UInt32)Removed CGPathElementType.valueRemoved CGPatternCallbacks.init(version: UInt32, drawPattern: CGPatternDrawPatternCallback, releaseInfo: CGPatternReleaseInfoCallback)Removed CGPatternTiling.init(_: UInt32)Removed CGPatternTiling.valueRemoved CGPDFBox.init(_: UInt32)Removed CGPDFBox.valueRemoved CGPDFDataFormat.init(_: UInt32)Removed CGPDFDataFormat.valueRemoved CGPDFObjectType.init(_: UInt32)Removed CGPDFObjectType.valueRemoved CGPoint.getMirror() -> MirrorTypeRemoved CGPoint.zeroPointRemoved CGPSConverterCallbacks.init(version: UInt32, beginDocument: CGPSConverterBeginDocumentCallback, endDocument: CGPSConverterEndDocumentCallback, beginPage: CGPSConverterBeginPageCallback, endPage: CGPSConverterEndPageCallback, noteProgress: CGPSConverterProgressCallback, noteMessage: CGPSConverterMessageCallback, releaseInfo: CGPSConverterReleaseInfoCallback)Removed CGRect.getMirror() -> MirrorTypeRemoved CGRect.infiniteRectRemoved CGRect.inset(dx: CGFloat, dy: CGFloat)Removed CGRect.integerize()Removed CGRect.integerRectRemoved CGRect.intersect(_: CGRect)Removed CGRect.nullRectRemoved CGRect.offset(dx: CGFloat, dy: CGFloat)Removed CGRect.rectByInsetting(dx: CGFloat, dy: CGFloat) -> CGRectRemoved CGRect.rectByIntersecting(_: CGRect) -> CGRectRemoved CGRect.rectByOffsetting(dx: CGFloat, dy: CGFloat) -> CGRectRemoved CGRect.rectByUnion(_: CGRect) -> CGRectRemoved CGRect.rectsByDividing(_: CGFloat, fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect)Removed CGRect.standardize()Removed CGRect.standardizedRectRemoved CGRect.union(_: CGRect)Removed CGRect.zeroRectRemoved CGSize.getMirror() -> MirrorTypeRemoved CGSize.zeroSizeRemoved CGTextDrawingMode.init(_: UInt32)Removed CGTextDrawingMode.valueRemoved CGVector.zeroVectorRemoved CGCaptureOptionsRemoved CGConfigureOptionRemoved CGDisplayChangeSummaryFlagsRemoved CGDisplayStreamFrameStatusRemoved CGDisplayStreamUpdateRectTypeRemoved CGErrorRemoved CGEventFieldRemoved CGEventFilterMaskRemoved CGEventFlagsRemoved CGEventMouseSubtypeRemoved CGEventSourceStateIDRemoved CGEventSuppressionStateRemoved CGEventTapLocationRemoved CGEventTapOptionsRemoved CGEventTapPlacementRemoved CGEventTypeRemoved CGGesturePhaseRemoved CGGradientDrawingOptionsRemoved CGMomentumScrollPhaseRemoved CGMouseButtonRemoved CGScreenUpdateOperationRemoved CGScrollEventUnitRemoved CGScrollPhaseRemoved CGVECTOR_DEFINEDRemoved CGWindowBackingTypeRemoved CGWindowImageOptionRemoved CGWindowLevelKeyRemoved CGWindowListCreate(_: CGWindowListOption, _: CGWindowID) -> Unmanaged<CFArray>!Removed CGWindowListOptionRemoved CGWindowSharingTypeRemoved kCGAnnotatedSessionEventTapRemoved kCGAssistiveTechHighWindowLevelKeyRemoved kCGBackingStoreBufferedRemoved kCGBackingStoreNonretainedRemoved kCGBackingStoreRetainedRemoved kCGBackstopMenuLevelKeyRemoved kCGBaseWindowLevelKeyRemoved kCGCaptureNoOptionsRemoved kCGConfigureForAppOnlyRemoved kCGConfigureForSessionRemoved kCGConfigurePermanentlyRemoved kCGCursorWindowLevelKeyRemoved kCGDesktopIconWindowLevelKeyRemoved kCGDesktopWindowLevelKeyRemoved kCGDisplayAddFlagRemoved kCGDisplayBeginConfigurationFlagRemoved kCGDisplayDesktopShapeChangedFlagRemoved kCGDisplayDisabledFlagRemoved kCGDisplayEnabledFlagRemoved kCGDisplayMirrorFlagRemoved kCGDisplayMovedFlagRemoved kCGDisplayRemoveFlagRemoved kCGDisplaySetMainFlagRemoved kCGDisplaySetModeFlagRemoved kCGDisplayStreamFrameStatusFrameBlankRemoved kCGDisplayStreamFrameStatusFrameCompleteRemoved kCGDisplayStreamFrameStatusFrameIdleRemoved kCGDisplayStreamFrameStatusStoppedRemoved kCGDisplayStreamUpdateDirtyRectsRemoved kCGDisplayStreamUpdateMovedRectsRemoved kCGDisplayStreamUpdateReducedDirtyRectsRemoved kCGDisplayStreamUpdateRefreshedRectsRemoved kCGDisplayUnMirrorFlagRemoved kCGDockWindowLevelKeyRemoved kCGDraggingWindowLevelKeyRemoved kCGEncodingFontSpecificRemoved kCGEncodingMacRomanRemoved kCGErrorCannotCompleteRemoved kCGErrorFailureRemoved kCGErrorIllegalArgumentRemoved kCGErrorInvalidConnectionRemoved kCGErrorInvalidContextRemoved kCGErrorInvalidOperationRemoved kCGErrorNoneAvailableRemoved kCGErrorNotImplementedRemoved kCGErrorRangeCheckRemoved kCGErrorSuccessRemoved kCGErrorTypeCheckRemoved kCGEventFilterMaskPermitLocalKeyboardEventsRemoved kCGEventFilterMaskPermitLocalMouseEventsRemoved kCGEventFilterMaskPermitSystemDefinedEventsRemoved kCGEventFlagMaskAlphaShiftRemoved kCGEventFlagMaskAlternateRemoved kCGEventFlagMaskCommandRemoved kCGEventFlagMaskControlRemoved kCGEventFlagMaskHelpRemoved kCGEventFlagMaskNonCoalescedRemoved kCGEventFlagMaskNumericPadRemoved kCGEventFlagMaskSecondaryFnRemoved kCGEventFlagMaskShiftRemoved kCGEventFlagsChangedRemoved kCGEventKeyDownRemoved kCGEventKeyUpRemoved kCGEventLeftMouseDownRemoved kCGEventLeftMouseDraggedRemoved kCGEventLeftMouseUpRemoved kCGEventMouseMovedRemoved kCGEventMouseSubtypeDefaultRemoved kCGEventMouseSubtypeTabletPointRemoved kCGEventMouseSubtypeTabletProximityRemoved kCGEventNullRemoved kCGEventOtherMouseDownRemoved kCGEventOtherMouseDraggedRemoved kCGEventOtherMouseUpRemoved kCGEventRightMouseDownRemoved kCGEventRightMouseDraggedRemoved kCGEventRightMouseUpRemoved kCGEventScrollWheelRemoved kCGEventSourceGroupIDRemoved kCGEventSourceStateCombinedSessionStateRemoved kCGEventSourceStateHIDSystemStateRemoved kCGEventSourceStateIDRemoved kCGEventSourceStatePrivateRemoved kCGEventSourceUnixProcessIDRemoved kCGEventSourceUserDataRemoved kCGEventSourceUserIDRemoved kCGEventSuppressionStateRemoteMouseDragRemoved kCGEventSuppressionStateSuppressionIntervalRemoved kCGEventTabletPointerRemoved kCGEventTabletProximityRemoved kCGEventTapDisabledByTimeoutRemoved kCGEventTapDisabledByUserInputRemoved kCGEventTapOptionDefaultRemoved kCGEventTapOptionListenOnlyRemoved kCGEventTargetProcessSerialNumberRemoved kCGEventTargetUnixProcessIDRemoved kCGFloatingWindowLevelKeyRemoved kCGGesturePhaseBeganRemoved kCGGesturePhaseCancelledRemoved kCGGesturePhaseChangedRemoved kCGGesturePhaseEndedRemoved kCGGesturePhaseMayBeginRemoved kCGGesturePhaseNoneRemoved kCGGradientDrawsAfterEndLocationRemoved kCGGradientDrawsBeforeStartLocationRemoved kCGHeadInsertEventTapRemoved kCGHelpWindowLevelKeyRemoved kCGHIDEventTapRemoved kCGKeyboardEventAutorepeatRemoved kCGKeyboardEventKeyboardTypeRemoved kCGKeyboardEventKeycodeRemoved kCGMainMenuWindowLevelKeyRemoved kCGMaximumWindowLevelKeyRemoved kCGMinimumWindowLevelKeyRemoved kCGModalPanelWindowLevelKeyRemoved kCGMomentumScrollPhaseBeginRemoved kCGMomentumScrollPhaseContinueRemoved kCGMomentumScrollPhaseEndRemoved kCGMomentumScrollPhaseNoneRemoved kCGMouseButtonCenterRemoved kCGMouseButtonLeftRemoved kCGMouseButtonRightRemoved kCGMouseEventButtonNumberRemoved kCGMouseEventClickStateRemoved kCGMouseEventDeltaXRemoved kCGMouseEventDeltaYRemoved kCGMouseEventInstantMouserRemoved kCGMouseEventNumberRemoved kCGMouseEventPressureRemoved kCGMouseEventSubtypeRemoved kCGMouseEventWindowUnderMousePointerRemoved kCGMouseEventWindowUnderMousePointerThatCanHandleThisEventRemoved kCGNormalWindowLevelKeyRemoved kCGNumberOfEventSuppressionStatesRemoved kCGNumberOfWindowLevelKeysRemoved kCGOverlayWindowLevelKeyRemoved kCGPopUpMenuWindowLevelKeyRemoved kCGScreenSaverWindowLevelKeyRemoved kCGScreenUpdateOperationMoveRemoved kCGScreenUpdateOperationReducedDirtyRectangleCountRemoved kCGScreenUpdateOperationRefreshRemoved kCGScrollEventUnitLineRemoved kCGScrollEventUnitPixelRemoved kCGScrollPhaseBeganRemoved kCGScrollPhaseCancelledRemoved kCGScrollPhaseChangedRemoved kCGScrollPhaseEndedRemoved kCGScrollPhaseMayBeginRemoved kCGScrollWheelEventDeltaAxis1Removed kCGScrollWheelEventDeltaAxis2Removed kCGScrollWheelEventDeltaAxis3Removed kCGScrollWheelEventFixedPtDeltaAxis1Removed kCGScrollWheelEventFixedPtDeltaAxis2Removed kCGScrollWheelEventFixedPtDeltaAxis3Removed kCGScrollWheelEventInstantMouserRemoved kCGScrollWheelEventIsContinuousRemoved kCGScrollWheelEventMomentumPhaseRemoved kCGScrollWheelEventPointDeltaAxis1Removed kCGScrollWheelEventPointDeltaAxis2Removed kCGScrollWheelEventPointDeltaAxis3Removed kCGScrollWheelEventScrollCountRemoved kCGScrollWheelEventScrollPhaseRemoved kCGSessionEventTapRemoved kCGStatusWindowLevelKeyRemoved kCGTabletEventDeviceIDRemoved kCGTabletEventPointButtonsRemoved kCGTabletEventPointPressureRemoved kCGTabletEventPointXRemoved kCGTabletEventPointYRemoved kCGTabletEventPointZRemoved kCGTabletEventRotationRemoved kCGTabletEventTangentialPressureRemoved kCGTabletEventTiltXRemoved kCGTabletEventTiltYRemoved kCGTabletEventVendor1Removed kCGTabletEventVendor2Removed kCGTabletEventVendor3Removed kCGTabletProximityEventCapabilityMaskRemoved kCGTabletProximityEventDeviceIDRemoved kCGTabletProximityEventEnterProximityRemoved kCGTabletProximityEventPointerIDRemoved kCGTabletProximityEventPointerTypeRemoved kCGTabletProximityEventSystemTabletIDRemoved kCGTabletProximityEventTabletIDRemoved kCGTabletProximityEventVendorIDRemoved kCGTabletProximityEventVendorPointerSerialNumberRemoved kCGTabletProximityEventVendorPointerTypeRemoved kCGTabletProximityEventVendorUniqueIDRemoved kCGTailAppendEventTapRemoved kCGTornOffMenuWindowLevelKeyRemoved kCGUtilityWindowLevelKeyRemoved kCGWindowImageBestResolutionRemoved kCGWindowImageBoundsIgnoreFramingRemoved kCGWindowImageDefaultRemoved kCGWindowImageNominalResolutionRemoved kCGWindowImageOnlyShadowsRemoved kCGWindowImageShouldBeOpaqueRemoved kCGWindowListExcludeDesktopElementsRemoved kCGWindowListOptionAllRemoved kCGWindowListOptionIncludingWindowRemoved kCGWindowListOptionOnScreenAboveWindowRemoved kCGWindowListOptionOnScreenBelowWindowRemoved kCGWindowListOptionOnScreenOnlyRemoved kCGWindowSharingNoneRemoved kCGWindowSharingReadOnlyRemoved kCGWindowSharingReadWriteAdded [CGCaptureOptions [struct]](https://developer.apple.com/documentation/coregraphics/cgcaptureoptions)Added CGCaptureOptions.init(rawValue: UInt32)Added [CGCaptureOptions.NoFill](https://developer.apple.com/documentation/coregraphics/cgcaptureoptions/kcgcapturenofill)Added [CGCaptureOptions.NoOptions](https://developer.apple.com/documentation/coregraphics/cgcaptureoptions/kcgcapturenooptions)Added [CGConfigureOption [struct]](https://developer.apple.com/documentation/coregraphics/cgconfigureoption)Added [CGConfigureOption.ForAppOnly](https://developer.apple.com/documentation/coregraphics/cgconfigureoption/kcgconfigureforapponly)Added [CGConfigureOption.ForSession](https://developer.apple.com/documentation/coregraphics/cgconfigureoption/kcgconfigureforsession)Added CGConfigureOption.init(rawValue: UInt32)Added [CGConfigureOption.Permanently](https://developer.apple.com/documentation/coregraphics/cgconfigureoption/1455394-permanently)Added CGDataConsumerCallbacks.init(putBytes: CGDataConsumerPutBytesCallback?, releaseConsumer: CGDataConsumerReleaseInfoCallback?)Added CGDataProviderDirectCallbacks.init(version: UInt32, getBytePointer: CGDataProviderGetBytePointerCallback?, releaseBytePointer: CGDataProviderReleaseBytePointerCallback?, getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback?, releaseInfo: CGDataProviderReleaseInfoCallback?)Added CGDataProviderSequentialCallbacks.init(version: UInt32, getBytes: CGDataProviderGetBytesCallback?, skipForward: CGDataProviderSkipForwardCallback?, rewind: CGDataProviderRewindCallback?, releaseInfo: CGDataProviderReleaseInfoCallback?)Added [CGDisplayChangeSummaryFlags [struct]](https://developer.apple.com/documentation/coregraphics/cgdisplaychangesummaryflags)Added [CGDisplayChangeSummaryFlags.AddFlag](https://developer.apple.com/documentation/coregraphics/cgdisplaychangesummaryflags/kcgdisplayaddflag)Added [CGDisplayChangeSummaryFlags.BeginConfigurationFlag](https://developer.apple.com/documentation/coregraphics/cgdisplaychangesummaryflags/kcgdisplaybeginconfigurationflag)Added [CGDisplayChangeSummaryFlags.DesktopShapeChangedFlag](https://developer.apple.com/documentation/coregraphics/cgdisplaychangesummaryflags/kcgdisplaydesktopshapechangedflag)Added [CGDisplayChangeSummaryFlags.DisabledFlag](https://developer.apple.com/documentation/coregraphics/cgdisplaychangesummaryflags/1456230-disabledflag)Added [CGDisplayChangeSummaryFlags.EnabledFlag](https://developer.apple.com/documentation/coregraphics/cgdisplaychangesummaryflags/1455453-enabledflag)Added CGDisplayChangeSummaryFlags.init(rawValue: UInt32)Added [CGDisplayChangeSummaryFlags.MirrorFlag](https://developer.apple.com/documentation/coregraphics/cgdisplaychangesummaryflags/kcgdisplaymirrorflag)Added [CGDisplayChangeSummaryFlags.MovedFlag](https://developer.apple.com/documentation/coregraphics/cgdisplaychangesummaryflags/1455375-movedflag)Added [CGDisplayChangeSummaryFlags.RemoveFlag](https://developer.apple.com/documentation/coregraphics/cgdisplaychangesummaryflags/1456232-removeflag)Added [CGDisplayChangeSummaryFlags.SetMainFlag](https://developer.apple.com/documentation/coregraphics/cgdisplaychangesummaryflags/1456143-setmainflag)Added [CGDisplayChangeSummaryFlags.SetModeFlag](https://developer.apple.com/documentation/coregraphics/cgdisplaychangesummaryflags/kcgdisplaysetmodeflag)Added [CGDisplayChangeSummaryFlags.UnMirrorFlag](https://developer.apple.com/documentation/coregraphics/cgdisplaychangesummaryflags/1456385-unmirrorflag)Added [CGDisplayStreamFrameStatus [enum]](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamframestatus)Added [CGDisplayStreamFrameStatus.FrameBlank](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamframestatus/frameblank)Added [CGDisplayStreamFrameStatus.FrameComplete](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamframestatus/kcgdisplaystreamframestatusframecomplete)Added [CGDisplayStreamFrameStatus.FrameIdle](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamframestatus/frameidle)Added [CGDisplayStreamFrameStatus.Stopped](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamframestatus/kcgdisplaystreamframestatusstopped)Added [CGDisplayStreamUpdateRectType [enum]](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdaterecttype)Added [CGDisplayStreamUpdateRectType.DirtyRects](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdaterecttype/kcgdisplaystreamupdatedirtyrects)Added [CGDisplayStreamUpdateRectType.MovedRects](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdaterecttype/movedrects)Added [CGDisplayStreamUpdateRectType.ReducedDirtyRects](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdaterecttype/reduceddirtyrects)Added [CGDisplayStreamUpdateRectType.RefreshedRects](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdaterecttype/kcgdisplaystreamupdaterefreshedrects)Added [CGError [enum]](https://developer.apple.com/documentation/coregraphics/cgerror)Added [CGError.CannotComplete](https://developer.apple.com/documentation/coregraphics/cgerror/cannotcomplete)Added [CGError.Failure](https://developer.apple.com/documentation/coregraphics/cgerror/failure)Added [CGError.IllegalArgument](https://developer.apple.com/documentation/coregraphics/cgerror/illegalargument)Added [CGError.InvalidConnection](https://developer.apple.com/documentation/coregraphics/cgerror/invalidconnection)Added [CGError.InvalidContext](https://developer.apple.com/documentation/coregraphics/cgerror/kcgerrorinvalidcontext)Added [CGError.InvalidOperation](https://developer.apple.com/documentation/coregraphics/cgerror/kcgerrorinvalidoperation)Added [CGError.NoneAvailable](https://developer.apple.com/documentation/coregraphics/cgerror/kcgerrornoneavailable)Added [CGError.NotImplemented](https://developer.apple.com/documentation/coregraphics/cgerror/notimplemented)Added [CGError.RangeCheck](https://developer.apple.com/documentation/coregraphics/cgerror/rangecheck)Added [CGError.Success](https://developer.apple.com/documentation/coregraphics/cgerror/kcgerrorsuccess)Added [CGError.TypeCheck](https://developer.apple.com/documentation/coregraphics/cgerror/typecheck)Added [CGEventField [enum]](https://developer.apple.com/documentation/coregraphics/cgeventfield)Added [CGEventField.EventSourceGroupID](https://developer.apple.com/documentation/coregraphics/cgeventfield/eventsourcegroupid)Added [CGEventField.EventSourceStateID](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgeventsourcestateid)Added [CGEventField.EventSourceUnixProcessID](https://developer.apple.com/documentation/coregraphics/cgeventfield/eventsourceunixprocessid)Added [CGEventField.EventSourceUserData](https://developer.apple.com/documentation/coregraphics/cgeventfield/eventsourceuserdata)Added [CGEventField.EventSourceUserID](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgeventsourceuserid)Added [CGEventField.EventTargetProcessSerialNumber](https://developer.apple.com/documentation/coregraphics/cgeventfield/eventtargetprocessserialnumber)Added [CGEventField.EventTargetUnixProcessID](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgeventtargetunixprocessid)Added [CGEventField.KeyboardEventAutorepeat](https://developer.apple.com/documentation/coregraphics/cgeventfield/keyboardeventautorepeat)Added [CGEventField.KeyboardEventKeyboardType](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgkeyboardeventkeyboardtype)Added [CGEventField.KeyboardEventKeycode](https://developer.apple.com/documentation/coregraphics/cgeventfield/keyboardeventkeycode)Added [CGEventField.MouseEventButtonNumber](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgmouseeventbuttonnumber)Added [CGEventField.MouseEventClickState](https://developer.apple.com/documentation/coregraphics/cgeventfield/mouseeventclickstate)Added [CGEventField.MouseEventDeltaX](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgmouseeventdeltax)Added [CGEventField.MouseEventDeltaY](https://developer.apple.com/documentation/coregraphics/cgeventfield/mouseeventdeltay)Added [CGEventField.MouseEventInstantMouser](https://developer.apple.com/documentation/coregraphics/cgeventfield/mouseeventinstantmouser)Added [CGEventField.MouseEventNumber](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgmouseeventnumber)Added [CGEventField.MouseEventPressure](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgmouseeventpressure)Added [CGEventField.MouseEventSubtype](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgmouseeventsubtype)Added [CGEventField.MouseEventWindowUnderMousePointer](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgmouseeventwindowundermousepointer)Added [CGEventField.MouseEventWindowUnderMousePointerThatCanHandleThisEvent](https://developer.apple.com/documentation/coregraphics/cgeventfield/mouseeventwindowundermousepointerthatcanhandlethisevent)Added [CGEventField.ScrollWheelEventDeltaAxis1](https://developer.apple.com/documentation/coregraphics/cgeventfield/scrollwheeleventdeltaaxis1)Added [CGEventField.ScrollWheelEventDeltaAxis2](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgscrollwheeleventdeltaaxis2)Added [CGEventField.ScrollWheelEventDeltaAxis3](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgscrollwheeleventdeltaaxis3)Added [CGEventField.ScrollWheelEventFixedPtDeltaAxis1](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgscrollwheeleventfixedptdeltaaxis1)Added [CGEventField.ScrollWheelEventFixedPtDeltaAxis2](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgscrollwheeleventfixedptdeltaaxis2)Added [CGEventField.ScrollWheelEventFixedPtDeltaAxis3](https://developer.apple.com/documentation/coregraphics/cgeventfield/scrollwheeleventfixedptdeltaaxis3)Added [CGEventField.ScrollWheelEventInstantMouser](https://developer.apple.com/documentation/coregraphics/cgeventfield/scrollwheeleventinstantmouser)Added [CGEventField.ScrollWheelEventIsContinuous](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgscrollwheeleventiscontinuous)Added [CGEventField.ScrollWheelEventMomentumPhase](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgscrollwheeleventmomentumphase)Added [CGEventField.ScrollWheelEventPointDeltaAxis1](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgscrollwheeleventpointdeltaaxis1)Added [CGEventField.ScrollWheelEventPointDeltaAxis2](https://developer.apple.com/documentation/coregraphics/cgeventfield/scrollwheeleventpointdeltaaxis2)Added [CGEventField.ScrollWheelEventPointDeltaAxis3](https://developer.apple.com/documentation/coregraphics/cgeventfield/scrollwheeleventpointdeltaaxis3)Added [CGEventField.ScrollWheelEventScrollCount](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgscrollwheeleventscrollcount)Added [CGEventField.ScrollWheelEventScrollPhase](https://developer.apple.com/documentation/coregraphics/cgeventfield/scrollwheeleventscrollphase)Added [CGEventField.TabletEventDeviceID](https://developer.apple.com/documentation/coregraphics/cgeventfield/tableteventdeviceid)Added [CGEventField.TabletEventPointButtons](https://developer.apple.com/documentation/coregraphics/cgeventfield/tableteventpointbuttons)Added [CGEventField.TabletEventPointPressure](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgtableteventpointpressure)Added [CGEventField.TabletEventPointX](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgtableteventpointx)Added [CGEventField.TabletEventPointY](https://developer.apple.com/documentation/coregraphics/cgeventfield/tableteventpointy)Added [CGEventField.TabletEventPointZ](https://developer.apple.com/documentation/coregraphics/cgeventfield/tableteventpointz)Added [CGEventField.TabletEventRotation](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgtableteventrotation)Added [CGEventField.TabletEventTangentialPressure](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgtableteventtangentialpressure)Added [CGEventField.TabletEventTiltX](https://developer.apple.com/documentation/coregraphics/cgeventfield/tableteventtiltx)Added [CGEventField.TabletEventTiltY](https://developer.apple.com/documentation/coregraphics/cgeventfield/tableteventtilty)Added [CGEventField.TabletEventVendor1](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgtableteventvendor1)Added [CGEventField.TabletEventVendor2](https://developer.apple.com/documentation/coregraphics/cgeventfield/tableteventvendor2)Added [CGEventField.TabletEventVendor3](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgtableteventvendor3)Added [CGEventField.TabletProximityEventCapabilityMask](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgtabletproximityeventcapabilitymask)Added [CGEventField.TabletProximityEventDeviceID](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgtabletproximityeventdeviceid)Added [CGEventField.TabletProximityEventEnterProximity](https://developer.apple.com/documentation/coregraphics/cgeventfield/tabletproximityevententerproximity)Added [CGEventField.TabletProximityEventPointerID](https://developer.apple.com/documentation/coregraphics/cgeventfield/tabletproximityeventpointerid)Added [CGEventField.TabletProximityEventPointerType](https://developer.apple.com/documentation/coregraphics/cgeventfield/tabletproximityeventpointertype)Added [CGEventField.TabletProximityEventSystemTabletID](https://developer.apple.com/documentation/coregraphics/cgeventfield/tabletproximityeventsystemtabletid)Added [CGEventField.TabletProximityEventTabletID](https://developer.apple.com/documentation/coregraphics/cgeventfield/tabletproximityeventtabletid)Added [CGEventField.TabletProximityEventVendorID](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgtabletproximityeventvendorid)Added [CGEventField.TabletProximityEventVendorPointerSerialNumber](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgtabletproximityeventvendorpointerserialnumber)Added [CGEventField.TabletProximityEventVendorPointerType](https://developer.apple.com/documentation/coregraphics/cgeventfield/tabletproximityeventvendorpointertype)Added [CGEventField.TabletProximityEventVendorUniqueID](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgtabletproximityeventvendoruniqueid)Added [CGEventFilterMask [struct]](https://developer.apple.com/documentation/coregraphics/cgeventfiltermask)Added CGEventFilterMask.init(rawValue: UInt32)Added [CGEventFilterMask.PermitLocalKeyboardEvents](https://developer.apple.com/documentation/coregraphics/cgeventfiltermask/1455360-permitlocalkeyboardevents)Added [CGEventFilterMask.PermitLocalMouseEvents](https://developer.apple.com/documentation/coregraphics/cgeventfiltermask/1454158-permitlocalmouseevents)Added [CGEventFilterMask.PermitSystemDefinedEvents](https://developer.apple.com/documentation/coregraphics/cgeventfiltermask/1456100-permitsystemdefinedevents)Added [CGEventFlags [enum]](https://developer.apple.com/documentation/coregraphics/cgeventflags)Added [CGEventFlags.MaskAlphaShift](https://developer.apple.com/documentation/coregraphics/cgeventflags/1456463-maskalphashift)Added [CGEventFlags.MaskAlternate](https://developer.apple.com/documentation/coregraphics/cgeventflags/1455191-maskalternate)Added [CGEventFlags.MaskCommand](https://developer.apple.com/documentation/coregraphics/cgeventflags/1455841-maskcommand)Added [CGEventFlags.MaskControl](https://developer.apple.com/documentation/coregraphics/cgeventflags/1455570-maskcontrol)Added [CGEventFlags.MaskHelp](https://developer.apple.com/documentation/coregraphics/cgeventflags/1454956-maskhelp)Added [CGEventFlags.MaskNonCoalesced](https://developer.apple.com/documentation/coregraphics/cgeventflags/kcgeventflagmasknoncoalesced)Added [CGEventFlags.MaskNumericPad](https://developer.apple.com/documentation/coregraphics/cgeventflags/1454790-masknumericpad)Added [CGEventFlags.MaskSecondaryFn](https://developer.apple.com/documentation/coregraphics/cgeventflags/kcgeventflagmasksecondaryfn)Added [CGEventFlags.MaskShift](https://developer.apple.com/documentation/coregraphics/cgeventflags/kcgeventflagmaskshift)Added [CGEventMouseSubtype [enum]](https://developer.apple.com/documentation/coregraphics/cgeventmousesubtype)Added [CGEventMouseSubtype.Default](https://developer.apple.com/documentation/coregraphics/cgeventmousesubtype/defaulttype)Added [CGEventMouseSubtype.TabletPoint](https://developer.apple.com/documentation/coregraphics/cgeventmousesubtype/tabletpoint)Added [CGEventMouseSubtype.TabletProximity](https://developer.apple.com/documentation/coregraphics/cgeventmousesubtype/tabletproximity)Added [CGEventSourceStateID [enum]](https://developer.apple.com/documentation/coregraphics/cgeventsourcestateid)Added [CGEventSourceStateID.CombinedSessionState](https://developer.apple.com/documentation/coregraphics/cgeventsourcestateid/combinedsessionstate)Added [CGEventSourceStateID.HIDSystemState](https://developer.apple.com/documentation/coregraphics/cgeventsourcestateid/kcgeventsourcestatehidsystemstate)Added [CGEventSourceStateID.Private](https://developer.apple.com/documentation/coregraphics/cgeventsourcestateid/kcgeventsourcestateprivate)Added [CGEventSuppressionState [enum]](https://developer.apple.com/documentation/coregraphics/cgeventsuppressionstate)Added [CGEventSuppressionState.EventSuppressionStateRemoteMouseDrag](https://developer.apple.com/documentation/coregraphics/cgeventsuppressionstate/eventsuppressionstateremotemousedrag)Added [CGEventSuppressionState.EventSuppressionStateSuppressionInterval](https://developer.apple.com/documentation/coregraphics/cgeventsuppressionstate/kcgeventsuppressionstatesuppressioninterval)Added [CGEventSuppressionState.NumberOfEventSuppressionStates](https://developer.apple.com/documentation/coregraphics/cgeventsuppressionstate/numberofeventsuppressionstates)Added [CGEventTapLocation [enum]](https://developer.apple.com/documentation/coregraphics/cgeventtaplocation)Added [CGEventTapLocation.CGAnnotatedSessionEventTap](https://developer.apple.com/documentation/coregraphics/cgeventtaplocation/cgannotatedsessioneventtap)Added [CGEventTapLocation.CGHIDEventTap](https://developer.apple.com/documentation/coregraphics/cgeventtaplocation/cghideventtap)Added [CGEventTapLocation.CGSessionEventTap](https://developer.apple.com/documentation/coregraphics/cgeventtaplocation/cgsessioneventtap)Added [CGEventTapOptions [enum]](https://developer.apple.com/documentation/coregraphics/cgeventtapoptions)Added [CGEventTapOptions.Default](https://developer.apple.com/documentation/coregraphics/cgeventtapoptions/defaulttap)Added [CGEventTapOptions.ListenOnly](https://developer.apple.com/documentation/coregraphics/cgeventtapoptions/listenonly)Added [CGEventTapPlacement [enum]](https://developer.apple.com/documentation/coregraphics/cgeventtapplacement)Added [CGEventTapPlacement.HeadInsertEventTap](https://developer.apple.com/documentation/coregraphics/cgeventtapplacement/headinserteventtap)Added [CGEventTapPlacement.TailAppendEventTap](https://developer.apple.com/documentation/coregraphics/cgeventtapplacement/kcgtailappendeventtap)Added [CGEventType [enum]](https://developer.apple.com/documentation/coregraphics/cgeventtype)Added [CGEventType.FlagsChanged](https://developer.apple.com/documentation/coregraphics/cgeventtype/kcgeventflagschanged)Added [CGEventType.KeyDown](https://developer.apple.com/documentation/coregraphics/cgeventtype/kcgeventkeydown)Added [CGEventType.KeyUp](https://developer.apple.com/documentation/coregraphics/cgeventtype/keyup)Added [CGEventType.LeftMouseDown](https://developer.apple.com/documentation/coregraphics/cgeventtype/leftmousedown)Added [CGEventType.LeftMouseDragged](https://developer.apple.com/documentation/coregraphics/cgeventtype/kcgeventleftmousedragged)Added [CGEventType.LeftMouseUp](https://developer.apple.com/documentation/coregraphics/cgeventtype/kcgeventleftmouseup)Added [CGEventType.MouseMoved](https://developer.apple.com/documentation/coregraphics/cgeventtype/mousemoved)Added [CGEventType.Null](https://developer.apple.com/documentation/coregraphics/cgeventtype/null)Added [CGEventType.OtherMouseDown](https://developer.apple.com/documentation/coregraphics/cgeventtype/othermousedown)Added [CGEventType.OtherMouseDragged](https://developer.apple.com/documentation/coregraphics/cgeventtype/kcgeventothermousedragged)Added [CGEventType.OtherMouseUp](https://developer.apple.com/documentation/coregraphics/cgeventtype/othermouseup)Added [CGEventType.RightMouseDown](https://developer.apple.com/documentation/coregraphics/cgeventtype/kcgeventrightmousedown)Added [CGEventType.RightMouseDragged](https://developer.apple.com/documentation/coregraphics/cgeventtype/kcgeventrightmousedragged)Added [CGEventType.RightMouseUp](https://developer.apple.com/documentation/coregraphics/cgeventtype/kcgeventrightmouseup)Added [CGEventType.ScrollWheel](https://developer.apple.com/documentation/coregraphics/cgeventtype/kcgeventscrollwheel)Added [CGEventType.TabletPointer](https://developer.apple.com/documentation/coregraphics/cgeventtype/tabletpointer)Added [CGEventType.TabletProximity](https://developer.apple.com/documentation/coregraphics/cgeventtype/tabletproximity)Added [CGEventType.TapDisabledByTimeout](https://developer.apple.com/documentation/coregraphics/cgeventtype/tapdisabledbytimeout)Added [CGEventType.TapDisabledByUserInput](https://developer.apple.com/documentation/coregraphics/cgeventtype/tapdisabledbyuserinput)Added CGFunctionCallbacks.init(version: UInt32, evaluate: CGFunctionEvaluateCallback?, releaseInfo: CGFunctionReleaseInfoCallback?)Added [CGGesturePhase [enum]](https://developer.apple.com/documentation/coregraphics/cggesturephase)Added [CGGesturePhase.Began](https://developer.apple.com/documentation/coregraphics/cggesturephase/began)Added [CGGesturePhase.Cancelled](https://developer.apple.com/documentation/coregraphics/cggesturephase/cancelled)Added [CGGesturePhase.Changed](https://developer.apple.com/documentation/coregraphics/cggesturephase/changed)Added [CGGesturePhase.Ended](https://developer.apple.com/documentation/coregraphics/cggesturephase/kcggesturephaseended)Added [CGGesturePhase.MayBegin](https://developer.apple.com/documentation/coregraphics/cggesturephase/kcggesturephasemaybegin)Added [CGGesturePhase.None](https://developer.apple.com/documentation/coregraphics/cggesturephase/kcggesturephasenone)Added CGGlypDeprecatedEnum [enum]Added [CGGlypDeprecatedEnum.GlyphMax](https://developer.apple.com/documentation/coregraphics/cgglyphdeprecatedenum/cgglyphmax)Added [CGGlypDeprecatedEnum.GlyphMin](https://developer.apple.com/documentation/coregraphics/cgglyphdeprecatedenum/cgglyphmin)Added [CGGradientDrawingOptions [struct]](https://developer.apple.com/documentation/coregraphics/cggradientdrawingoptions)Added [CGGradientDrawingOptions.DrawsAfterEndLocation](https://developer.apple.com/documentation/coregraphics/cggradientdrawingoptions/kcggradientdrawsafterendlocation)Added [CGGradientDrawingOptions.DrawsBeforeStartLocation](https://developer.apple.com/documentation/coregraphics/cggradientdrawingoptions/kcggradientdrawsbeforestartlocation)Added CGGradientDrawingOptions.init(rawValue: UInt32)Added [CGMomentumScrollPhase [enum]](https://developer.apple.com/documentation/coregraphics/cgmomentumscrollphase)Added [CGMomentumScrollPhase.Begin](https://developer.apple.com/documentation/coregraphics/cgmomentumscrollphase/kcgmomentumscrollphasebegin)Added [CGMomentumScrollPhase.Continue](https://developer.apple.com/documentation/coregraphics/cgmomentumscrollphase/kcgmomentumscrollphasecontinue)Added [CGMomentumScrollPhase.End](https://developer.apple.com/documentation/coregraphics/cgmomentumscrollphase/end)Added [CGMomentumScrollPhase.None](https://developer.apple.com/documentation/coregraphics/cgmomentumscrollphase/none)Added [CGMouseButton [enum]](https://developer.apple.com/documentation/coregraphics/cgmousebutton)Added [CGMouseButton.Center](https://developer.apple.com/documentation/coregraphics/cgmousebutton/kcgmousebuttoncenter)Added [CGMouseButton.Left](https://developer.apple.com/documentation/coregraphics/cgmousebutton/kcgmousebuttonleft)Added [CGMouseButton.Right](https://developer.apple.com/documentation/coregraphics/cgmousebutton/right)Added CGPatternCallbacks.init(version: UInt32, drawPattern: CGPatternDrawPatternCallback?, releaseInfo: CGPatternReleaseInfoCallback?)Added [CGPoint.zero](https://developer.apple.com/documentation/coregraphics/cgpoint/1454433-zero)Added CGPSConverterCallbacks.init(version: UInt32, beginDocument: CGPSConverterBeginDocumentCallback?, endDocument: CGPSConverterEndDocumentCallback?, beginPage: CGPSConverterBeginPageCallback?, endPage: CGPSConverterEndPageCallback?, noteProgress: CGPSConverterProgressCallback?, noteMessage: CGPSConverterMessageCallback?, releaseInfo: CGPSConverterReleaseInfoCallback?)Added CGRect.divide(_: CGFloat, fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect)Added CGRect.infiniteAdded CGRect.insetBy(dx: CGFloat, dy: CGFloat) -> CGRectAdded CGRect.insetInPlace(dx: CGFloat, dy: CGFloat)Added CGRect.integralAdded CGRect.intersect(_: CGRect) -> CGRectAdded CGRect.intersectInPlace(_: CGRect)Added CGRect.makeIntegralInPlace()Added CGRect.nullAdded CGRect.offsetBy(dx: CGFloat, dy: CGFloat) -> CGRectAdded CGRect.offsetInPlace(dx: CGFloat, dy: CGFloat)Added CGRect.standardizedAdded CGRect.standardizeInPlace()Added CGRect.union(_: CGRect) -> CGRectAdded CGRect.unionInPlace(_: CGRect)Added [CGRect.zero](https://developer.apple.com/documentation/coregraphics/cgrect/1455437-zero)Added [CGScreenUpdateOperation [struct]](https://developer.apple.com/documentation/coregraphics/cgscreenupdateoperation)Added CGScreenUpdateOperation.init(rawValue: UInt32)Added [CGScreenUpdateOperation.Move](https://developer.apple.com/documentation/coregraphics/cgscreenupdateoperation/1454568-move)Added [CGScreenUpdateOperation.ReducedDirtyRectangleCount](https://developer.apple.com/documentation/coregraphics/cgscreenupdateoperation/kcgscreenupdateoperationreduceddirtyrectanglecount)Added [CGScreenUpdateOperation.Refresh](https://developer.apple.com/documentation/coregraphics/cgscreenupdateoperation/kcgscreenupdateoperationrefresh)Added [CGScrollEventUnit [enum]](https://developer.apple.com/documentation/coregraphics/cgscrolleventunit)Added [CGScrollEventUnit.Line](https://developer.apple.com/documentation/coregraphics/cgscrolleventunit/kcgscrolleventunitline)Added [CGScrollEventUnit.Pixel](https://developer.apple.com/documentation/coregraphics/cgscrolleventunit/kcgscrolleventunitpixel)Added [CGScrollPhase [enum]](https://developer.apple.com/documentation/coregraphics/cgscrollphase)Added [CGScrollPhase.Began](https://developer.apple.com/documentation/coregraphics/cgscrollphase/kcgscrollphasebegan)Added [CGScrollPhase.Cancelled](https://developer.apple.com/documentation/coregraphics/cgscrollphase/kcgscrollphasecancelled)Added [CGScrollPhase.Changed](https://developer.apple.com/documentation/coregraphics/cgscrollphase/kcgscrollphasechanged)Added [CGScrollPhase.Ended](https://developer.apple.com/documentation/coregraphics/cgscrollphase/ended)Added [CGScrollPhase.MayBegin](https://developer.apple.com/documentation/coregraphics/cgscrollphase/kcgscrollphasemaybegin)Added [CGSize.zero](https://developer.apple.com/documentation/coregraphics/cgsize/1455512-zero)Added [CGVector.zero](https://developer.apple.com/documentation/coregraphics/cgvector/1454067-zero)Added [CGWindowBackingType [enum]](https://developer.apple.com/documentation/coregraphics/cgwindowbackingtype)Added [CGWindowBackingType.BackingStoreBuffered](https://developer.apple.com/documentation/coregraphics/cgwindowbackingtype/kcgbackingstorebuffered)Added [CGWindowBackingType.BackingStoreNonretained](https://developer.apple.com/documentation/coregraphics/cgwindowbackingtype/kcgbackingstorenonretained)Added [CGWindowBackingType.BackingStoreRetained](https://developer.apple.com/documentation/coregraphics/cgwindowbackingtype/kcgbackingstoreretained)Added [CGWindowImageOption [struct]](https://developer.apple.com/documentation/coregraphics/cgwindowimageoption)Added [CGWindowImageOption.BestResolution](https://developer.apple.com/documentation/coregraphics/cgwindowimageoption/kcgwindowimagebestresolution)Added [CGWindowImageOption.BoundsIgnoreFraming](https://developer.apple.com/documentation/coregraphics/cgwindowimageoption/kcgwindowimageboundsignoreframing)Added [CGWindowImageOption.Default](https://developer.apple.com/documentation/coregraphics/cgwindowimageoption/kcgwindowimagedefault)Added CGWindowImageOption.init(rawValue: UInt32)Added [CGWindowImageOption.NominalResolution](https://developer.apple.com/documentation/coregraphics/cgwindowimageoption/kcgwindowimagenominalresolution)Added [CGWindowImageOption.OnlyShadows](https://developer.apple.com/documentation/coregraphics/cgwindowimageoption/1455734-onlyshadows)Added [CGWindowImageOption.ShouldBeOpaque](https://developer.apple.com/documentation/coregraphics/cgwindowimageoption/kcgwindowimageshouldbeopaque)Added [CGWindowLevelKey [enum]](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey)Added [CGWindowLevelKey.AssistiveTechHighWindowLevelKey](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/assistivetechhighwindow)Added [CGWindowLevelKey.BackstopMenuLevelKey](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/kcgbackstopmenulevelkey)Added [CGWindowLevelKey.BaseWindowLevelKey](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/kcgbasewindowlevelkey)Added [CGWindowLevelKey.CursorWindowLevelKey](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/cursorwindow)Added [CGWindowLevelKey.DesktopIconWindowLevelKey](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/desktopiconwindow)Added [CGWindowLevelKey.DesktopWindowLevelKey](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/desktopwindow)Added [CGWindowLevelKey.DockWindowLevelKey](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/dockwindow)Added [CGWindowLevelKey.DraggingWindowLevelKey](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/kcgdraggingwindowlevelkey)Added [CGWindowLevelKey.FloatingWindowLevelKey](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/floatingwindow)Added [CGWindowLevelKey.HelpWindowLevelKey](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/kcghelpwindowlevelkey)Added [CGWindowLevelKey.MainMenuWindowLevelKey](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/mainmenuwindow)Added [CGWindowLevelKey.MaximumWindowLevelKey](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/maximumwindow)Added [CGWindowLevelKey.MinimumWindowLevelKey](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/minimumwindow)Added [CGWindowLevelKey.ModalPanelWindowLevelKey](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/kcgmodalpanelwindowlevelkey)Added [CGWindowLevelKey.NormalWindowLevelKey](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/kcgnormalwindowlevelkey)Added [CGWindowLevelKey.NumberOfWindowLevelKeys](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/numberofwindowlevelkeys)Added [CGWindowLevelKey.OverlayWindowLevelKey](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/overlaywindow)Added [CGWindowLevelKey.PopUpMenuWindowLevelKey](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/popupmenuwindow)Added [CGWindowLevelKey.ScreenSaverWindowLevelKey](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/kcgscreensaverwindowlevelkey)Added [CGWindowLevelKey.StatusWindowLevelKey](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/statuswindow)Added [CGWindowLevelKey.TornOffMenuWindowLevelKey](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/tornoffmenuwindow)Added [CGWindowLevelKey.UtilityWindowLevelKey](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey/kcgutilitywindowlevelkey)Added [CGWindowListOption [struct]](https://developer.apple.com/documentation/coregraphics/cgwindowlistoption)Added [CGWindowListOption.ExcludeDesktopElements](https://developer.apple.com/documentation/coregraphics/cgwindowlistoption/kcgwindowlistexcludedesktopelements)Added CGWindowListOption.init(rawValue: UInt32)Added [CGWindowListOption.OptionAll](https://developer.apple.com/documentation/coregraphics/cgwindowlistoption/1455377-optionall)Added [CGWindowListOption.OptionIncludingWindow](https://developer.apple.com/documentation/coregraphics/cgwindowlistoption/1454408-optionincludingwindow)Added [CGWindowListOption.OptionOnScreenAboveWindow](https://developer.apple.com/documentation/coregraphics/cgwindowlistoption/1455651-optiononscreenabovewindow)Added [CGWindowListOption.OptionOnScreenBelowWindow](https://developer.apple.com/documentation/coregraphics/cgwindowlistoption/1455142-optiononscreenbelowwindow)Added [CGWindowListOption.OptionOnScreenOnly](https://developer.apple.com/documentation/coregraphics/cgwindowlistoption/kcgwindowlistoptiononscreenonly)Added [CGWindowSharingType [enum]](https://developer.apple.com/documentation/coregraphics/cgwindowsharingtype)Added [CGWindowSharingType.None](https://developer.apple.com/documentation/coregraphics/cgwindowsharingtype/kcgwindowsharingnone)Added [CGWindowSharingType.ReadOnly](https://developer.apple.com/documentation/coregraphics/cgwindowsharingtype/readonly)Added [CGWindowSharingType.ReadWrite](https://developer.apple.com/documentation/coregraphics/cgwindowsharingtype/readwrite)Added CGAffineTransformIdentityAdded [CGColorCreateCopyByMatchingToColorSpace(_: CGColorSpace?, _: CGColorRenderingIntent, _: CGColor?, _: CFDictionary?) -> CGColor?](https://developer.apple.com/documentation/coregraphics/cgcolor/1455493-converted)Added [CGEventPostToPid(_: pid_t, _: CGEvent?)](https://developer.apple.com/documentation/coregraphics/cgevent/1454804-posttopid)Added [CGEventTapCreateForPid(_: pid_t, _: CGEventTapPlacement, _: CGEventTapOptions, _: CGEventMask, _: CGEventTapCallBack, _: UnsafeMutablePointer<Void>) -> CFMachPort?](https://developer.apple.com/documentation/coregraphics/1456048-cgeventtapcreateforpid)Added [CGImageGetUTType(_: CGImage?) -> CFString?](https://developer.apple.com/documentation/coregraphics/1456067-cgimagegetuttype)Added CGPointZeroAdded CGRectZeroAdded CGSizeZeroAdded [kCGColorSpaceACESCGLinear](https://developer.apple.com/documentation/coregraphics/kcgcolorspaceacescglinear)Added [kCGColorSpaceGenericXYZ](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408844-genericxyz)Added [kCGColorSpaceITUR_2020](https://developer.apple.com/documentation/coregraphics/kcgcolorspaceitur_2020)Added [kCGColorSpaceITUR_709](https://developer.apple.com/documentation/coregraphics/kcgcolorspaceitur_709)Added [kCGColorSpaceROMMRGB](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408912-rommrgb)Modified [CGBitmapInfo [struct]](https://developer.apple.com/documentation/coregraphics/cgbitmapinfo)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CGBitmapInfo : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var AlphaInfoMask: CGBitmapInfo { get }     static var FloatComponents: CGBitmapInfo { get }     static var ByteOrderMask: CGBitmapInfo { get }     static var ByteOrderDefault: CGBitmapInfo { get }     static var ByteOrder16Little: CGBitmapInfo { get }     static var ByteOrder32Little: CGBitmapInfo { get }     static var ByteOrder16Big: CGBitmapInfo { get }     static var ByteOrder32Big: CGBitmapInfo { get } } ``` | RawOptionSetType |
| To | ``` struct CGBitmapInfo : OptionSetType {     init(rawValue rawValue: UInt32)     static var AlphaInfoMask: CGBitmapInfo { get }     static var FloatComponents: CGBitmapInfo { get }     static var ByteOrderMask: CGBitmapInfo { get }     static var ByteOrderDefault: CGBitmapInfo { get }     static var ByteOrder16Little: CGBitmapInfo { get }     static var ByteOrder32Little: CGBitmapInfo { get }     static var ByteOrder16Big: CGBitmapInfo { get }     static var ByteOrder32Big: CGBitmapInfo { get } } ``` | OptionSetType |

Modified [CGBlendMode [enum]](https://developer.apple.com/documentation/coregraphics/cgblendmode)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct CGBlendMode {     init(_ value: UInt32)     var value: UInt32 } ``` | -- | OS X 10.10 | -- |
| To | ``` enum CGBlendMode : Int32 {     case Normal     case Multiply     case Screen     case Overlay     case Darken     case Lighten     case ColorDodge     case ColorBurn     case SoftLight     case HardLight     case Difference     case Exclusion     case Hue     case Saturation     case Color     case Luminosity     case Clear     case Copy     case SourceIn     case SourceOut     case SourceAtop     case DestinationOver     case DestinationIn     case DestinationOut     case DestinationAtop     case XOR     case PlusDarker     case PlusLighter } ``` | Equatable, Hashable, RawRepresentable | OS X 10.11 | Int32 |

Modified [CGBlendMode.Clear](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodeclear)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeClear | ``` var kCGBlendModeClear: CGBlendMode { get } ``` | OS X 10.10 |
| To | Clear | ``` case Clear ``` | OS X 10.11 |

Modified [CGBlendMode.Color](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodecolor)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeColor | ``` var kCGBlendModeColor: CGBlendMode { get } ``` | OS X 10.10 |
| To | Color | ``` case Color ``` | OS X 10.11 |

Modified [CGBlendMode.ColorBurn](https://developer.apple.com/documentation/coregraphics/cgblendmode/colorburn)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeColorBurn | ``` var kCGBlendModeColorBurn: CGBlendMode { get } ``` | OS X 10.10 |
| To | ColorBurn | ``` case ColorBurn ``` | OS X 10.11 |

Modified [CGBlendMode.ColorDodge](https://developer.apple.com/documentation/coregraphics/cgblendmode/colordodge)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeColorDodge | ``` var kCGBlendModeColorDodge: CGBlendMode { get } ``` | OS X 10.10 |
| To | ColorDodge | ``` case ColorDodge ``` | OS X 10.11 |

Modified [CGBlendMode.Copy](https://developer.apple.com/documentation/coregraphics/cgblendmode/copy)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeCopy | ``` var kCGBlendModeCopy: CGBlendMode { get } ``` | OS X 10.10 |
| To | Copy | ``` case Copy ``` | OS X 10.11 |

Modified [CGBlendMode.Darken](https://developer.apple.com/documentation/coregraphics/cgblendmode/darken)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeDarken | ``` var kCGBlendModeDarken: CGBlendMode { get } ``` | OS X 10.10 |
| To | Darken | ``` case Darken ``` | OS X 10.11 |

Modified [CGBlendMode.DestinationAtop](https://developer.apple.com/documentation/coregraphics/cgblendmode/destinationatop)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeDestinationAtop | ``` var kCGBlendModeDestinationAtop: CGBlendMode { get } ``` | OS X 10.10 |
| To | DestinationAtop | ``` case DestinationAtop ``` | OS X 10.11 |

Modified [CGBlendMode.DestinationIn](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodedestinationin)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeDestinationIn | ``` var kCGBlendModeDestinationIn: CGBlendMode { get } ``` | OS X 10.10 |
| To | DestinationIn | ``` case DestinationIn ``` | OS X 10.11 |

Modified [CGBlendMode.DestinationOut](https://developer.apple.com/documentation/coregraphics/cgblendmode/destinationout)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeDestinationOut | ``` var kCGBlendModeDestinationOut: CGBlendMode { get } ``` | OS X 10.10 |
| To | DestinationOut | ``` case DestinationOut ``` | OS X 10.11 |

Modified [CGBlendMode.DestinationOver](https://developer.apple.com/documentation/coregraphics/cgblendmode/destinationover)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeDestinationOver | ``` var kCGBlendModeDestinationOver: CGBlendMode { get } ``` | OS X 10.10 |
| To | DestinationOver | ``` case DestinationOver ``` | OS X 10.11 |

Modified [CGBlendMode.Difference](https://developer.apple.com/documentation/coregraphics/cgblendmode/difference)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeDifference | ``` var kCGBlendModeDifference: CGBlendMode { get } ``` | OS X 10.10 |
| To | Difference | ``` case Difference ``` | OS X 10.11 |

Modified [CGBlendMode.Exclusion](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodeexclusion)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeExclusion | ``` var kCGBlendModeExclusion: CGBlendMode { get } ``` | OS X 10.10 |
| To | Exclusion | ``` case Exclusion ``` | OS X 10.11 |

Modified [CGBlendMode.HardLight](https://developer.apple.com/documentation/coregraphics/cgblendmode/hardlight)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeHardLight | ``` var kCGBlendModeHardLight: CGBlendMode { get } ``` | OS X 10.10 |
| To | HardLight | ``` case HardLight ``` | OS X 10.11 |

Modified [CGBlendMode.Hue](https://developer.apple.com/documentation/coregraphics/cgblendmode/hue)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeHue | ``` var kCGBlendModeHue: CGBlendMode { get } ``` | OS X 10.10 |
| To | Hue | ``` case Hue ``` | OS X 10.11 |

Modified [CGBlendMode.Lighten](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodelighten)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeLighten | ``` var kCGBlendModeLighten: CGBlendMode { get } ``` | OS X 10.10 |
| To | Lighten | ``` case Lighten ``` | OS X 10.11 |

Modified [CGBlendMode.Luminosity](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodeluminosity)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeLuminosity | ``` var kCGBlendModeLuminosity: CGBlendMode { get } ``` | OS X 10.10 |
| To | Luminosity | ``` case Luminosity ``` | OS X 10.11 |

Modified [CGBlendMode.Multiply](https://developer.apple.com/documentation/coregraphics/cgblendmode/multiply)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeMultiply | ``` var kCGBlendModeMultiply: CGBlendMode { get } ``` | OS X 10.10 |
| To | Multiply | ``` case Multiply ``` | OS X 10.11 |

Modified [CGBlendMode.Normal](https://developer.apple.com/documentation/coregraphics/cgblendmode/normal)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeNormal | ``` var kCGBlendModeNormal: CGBlendMode { get } ``` | OS X 10.10 |
| To | Normal | ``` case Normal ``` | OS X 10.11 |

Modified [CGBlendMode.Overlay](https://developer.apple.com/documentation/coregraphics/cgblendmode/overlay)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeOverlay | ``` var kCGBlendModeOverlay: CGBlendMode { get } ``` | OS X 10.10 |
| To | Overlay | ``` case Overlay ``` | OS X 10.11 |

Modified [CGBlendMode.PlusDarker](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodeplusdarker)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModePlusDarker | ``` var kCGBlendModePlusDarker: CGBlendMode { get } ``` | OS X 10.10 |
| To | PlusDarker | ``` case PlusDarker ``` | OS X 10.11 |

Modified [CGBlendMode.PlusLighter](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodepluslighter)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModePlusLighter | ``` var kCGBlendModePlusLighter: CGBlendMode { get } ``` | OS X 10.10 |
| To | PlusLighter | ``` case PlusLighter ``` | OS X 10.11 |

Modified [CGBlendMode.Saturation](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodesaturation)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeSaturation | ``` var kCGBlendModeSaturation: CGBlendMode { get } ``` | OS X 10.10 |
| To | Saturation | ``` case Saturation ``` | OS X 10.11 |

Modified [CGBlendMode.Screen](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodescreen)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeScreen | ``` var kCGBlendModeScreen: CGBlendMode { get } ``` | OS X 10.10 |
| To | Screen | ``` case Screen ``` | OS X 10.11 |

Modified [CGBlendMode.SoftLight](https://developer.apple.com/documentation/coregraphics/cgblendmode/softlight)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeSoftLight | ``` var kCGBlendModeSoftLight: CGBlendMode { get } ``` | OS X 10.10 |
| To | SoftLight | ``` case SoftLight ``` | OS X 10.11 |

Modified [CGBlendMode.SourceAtop](https://developer.apple.com/documentation/coregraphics/cgblendmode/sourceatop)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeSourceAtop | ``` var kCGBlendModeSourceAtop: CGBlendMode { get } ``` | OS X 10.10 |
| To | SourceAtop | ``` case SourceAtop ``` | OS X 10.11 |

Modified [CGBlendMode.SourceIn](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodesourcein)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeSourceIn | ``` var kCGBlendModeSourceIn: CGBlendMode { get } ``` | OS X 10.10 |
| To | SourceIn | ``` case SourceIn ``` | OS X 10.11 |

Modified [CGBlendMode.SourceOut](https://developer.apple.com/documentation/coregraphics/cgblendmode/sourceout)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeSourceOut | ``` var kCGBlendModeSourceOut: CGBlendMode { get } ``` | OS X 10.10 |
| To | SourceOut | ``` case SourceOut ``` | OS X 10.11 |

Modified [CGBlendMode.XOR](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodexor)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGBlendModeXOR | ``` var kCGBlendModeXOR: CGBlendMode { get } ``` | OS X 10.10 |
| To | XOR | ``` case XOR ``` | OS X 10.11 |

Modified [CGColorRenderingIntent [enum]](https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct CGColorRenderingIntent {     init(_ value: UInt32)     var value: UInt32 } ``` | -- | OS X 10.10 | -- |
| To | ``` enum CGColorRenderingIntent : Int32 {     case RenderingIntentDefault     case RenderingIntentAbsoluteColorimetric     case RenderingIntentRelativeColorimetric     case RenderingIntentPerceptual     case RenderingIntentSaturation } ``` | Equatable, Hashable, RawRepresentable | OS X 10.11 | Int32 |

Modified [CGColorRenderingIntent.RenderingIntentAbsoluteColorimetric](https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent/absolutecolorimetric)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGRenderingIntentAbsoluteColorimetric | ``` var kCGRenderingIntentAbsoluteColorimetric: CGColorRenderingIntent { get } ``` | OS X 10.10 |
| To | RenderingIntentAbsoluteColorimetric | ``` case RenderingIntentAbsoluteColorimetric ``` | OS X 10.11 |

Modified [CGColorRenderingIntent.RenderingIntentDefault](https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent/defaultintent)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGRenderingIntentDefault | ``` var kCGRenderingIntentDefault: CGColorRenderingIntent { get } ``` | OS X 10.10 |
| To | RenderingIntentDefault | ``` case RenderingIntentDefault ``` | OS X 10.11 |

Modified [CGColorRenderingIntent.RenderingIntentPerceptual](https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent/kcgrenderingintentperceptual)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGRenderingIntentPerceptual | ``` var kCGRenderingIntentPerceptual: CGColorRenderingIntent { get } ``` | OS X 10.10 |
| To | RenderingIntentPerceptual | ``` case RenderingIntentPerceptual ``` | OS X 10.11 |

Modified [CGColorRenderingIntent.RenderingIntentRelativeColorimetric](https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent/relativecolorimetric)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGRenderingIntentRelativeColorimetric | ``` var kCGRenderingIntentRelativeColorimetric: CGColorRenderingIntent { get } ``` | OS X 10.10 |
| To | RenderingIntentRelativeColorimetric | ``` case RenderingIntentRelativeColorimetric ``` | OS X 10.11 |

Modified [CGColorRenderingIntent.RenderingIntentSaturation](https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent/kcgrenderingintentsaturation)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGRenderingIntentSaturation | ``` var kCGRenderingIntentSaturation: CGColorRenderingIntent { get } ``` | OS X 10.10 |
| To | RenderingIntentSaturation | ``` case RenderingIntentSaturation ``` | OS X 10.11 |

Modified [CGColorSpaceModel [enum]](https://developer.apple.com/documentation/coregraphics/cgcolorspacemodel)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct CGColorSpaceModel {     init(_ value: Int32)     var value: Int32 } ``` | -- | OS X 10.10 | -- |
| To | ``` enum CGColorSpaceModel : Int32 {     case Unknown     case Monochrome     case RGB     case CMYK     case Lab     case DeviceN     case Indexed     case Pattern } ``` | Equatable, Hashable, RawRepresentable | OS X 10.11 | Int32 |

Modified [CGColorSpaceModel.CMYK](https://developer.apple.com/documentation/coregraphics/cgcolorspacemodel/cmyk)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGColorSpaceModelCMYK | ``` var kCGColorSpaceModelCMYK: CGColorSpaceModel { get } ``` | OS X 10.10 |
| To | CMYK | ``` case CMYK ``` | OS X 10.11 |

Modified [CGColorSpaceModel.DeviceN](https://developer.apple.com/documentation/coregraphics/cgcolorspacemodel/kcgcolorspacemodeldevicen)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGColorSpaceModelDeviceN | ``` var kCGColorSpaceModelDeviceN: CGColorSpaceModel { get } ``` | OS X 10.10 |
| To | DeviceN | ``` case DeviceN ``` | OS X 10.11 |

Modified [CGColorSpaceModel.Indexed](https://developer.apple.com/documentation/coregraphics/cgcolorspacemodel/kcgcolorspacemodelindexed)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGColorSpaceModelIndexed | ``` var kCGColorSpaceModelIndexed: CGColorSpaceModel { get } ``` | OS X 10.10 |
| To | Indexed | ``` case Indexed ``` | OS X 10.11 |

Modified [CGColorSpaceModel.Lab](https://developer.apple.com/documentation/coregraphics/cgcolorspacemodel/lab)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGColorSpaceModelLab | ``` var kCGColorSpaceModelLab: CGColorSpaceModel { get } ``` | OS X 10.10 |
| To | Lab | ``` case Lab ``` | OS X 10.11 |

Modified [CGColorSpaceModel.Monochrome](https://developer.apple.com/documentation/coregraphics/cgcolorspacemodel/monochrome)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGColorSpaceModelMonochrome | ``` var kCGColorSpaceModelMonochrome: CGColorSpaceModel { get } ``` | OS X 10.10 |
| To | Monochrome | ``` case Monochrome ``` | OS X 10.11 |

Modified [CGColorSpaceModel.Pattern](https://developer.apple.com/documentation/coregraphics/cgcolorspacemodel/kcgcolorspacemodelpattern)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGColorSpaceModelPattern | ``` var kCGColorSpaceModelPattern: CGColorSpaceModel { get } ``` | OS X 10.10 |
| To | Pattern | ``` case Pattern ``` | OS X 10.11 |

Modified [CGColorSpaceModel.RGB](https://developer.apple.com/documentation/coregraphics/cgcolorspacemodel/rgb)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGColorSpaceModelRGB | ``` var kCGColorSpaceModelRGB: CGColorSpaceModel { get } ``` | OS X 10.10 |
| To | RGB | ``` case RGB ``` | OS X 10.11 |

Modified [CGColorSpaceModel.Unknown](https://developer.apple.com/documentation/coregraphics/cgcolorspacemodel/unknown)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGColorSpaceModelUnknown | ``` var kCGColorSpaceModelUnknown: CGColorSpaceModel { get } ``` | OS X 10.10 |
| To | Unknown | ``` case Unknown ``` | OS X 10.11 |

Modified [CGDataConsumerCallbacks [struct]](https://developer.apple.com/documentation/coregraphics/cgdataconsumercallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CGDataConsumerCallbacks {     var putBytes: CGDataConsumerPutBytesCallback     var releaseConsumer: CGDataConsumerReleaseInfoCallback     init()     init(putBytes putBytes: CGDataConsumerPutBytesCallback, releaseConsumer releaseConsumer: CGDataConsumerReleaseInfoCallback) } ``` |
| To | ``` struct CGDataConsumerCallbacks {     var putBytes: CGDataConsumerPutBytesCallback?     var releaseConsumer: CGDataConsumerReleaseInfoCallback?     init()     init(putBytes putBytes: CGDataConsumerPutBytesCallback?, releaseConsumer releaseConsumer: CGDataConsumerReleaseInfoCallback?) } ``` |

Modified [CGDataConsumerCallbacks.putBytes](https://developer.apple.com/documentation/coregraphics/cgdataconsumercallbacks/1455040-putbytes)

|  | Declaration |
| --- | --- |
| From | ``` var putBytes: CGDataConsumerPutBytesCallback ``` |
| To | ``` var putBytes: CGDataConsumerPutBytesCallback? ``` |

Modified [CGDataConsumerCallbacks.releaseConsumer](https://developer.apple.com/documentation/coregraphics/cgdataconsumercallbacks/1454472-releaseconsumer)

|  | Declaration |
| --- | --- |
| From | ``` var releaseConsumer: CGDataConsumerReleaseInfoCallback ``` |
| To | ``` var releaseConsumer: CGDataConsumerReleaseInfoCallback? ``` |

Modified [CGDataProviderDirectCallbacks [struct]](https://developer.apple.com/documentation/coregraphics/cgdataproviderdirectcallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CGDataProviderDirectCallbacks {     var version: UInt32     var getBytePointer: CGDataProviderGetBytePointerCallback     var releaseBytePointer: CGDataProviderReleaseBytePointerCallback     var getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback     var releaseInfo: CGDataProviderReleaseInfoCallback     init()     init(version version: UInt32, getBytePointer getBytePointer: CGDataProviderGetBytePointerCallback, releaseBytePointer releaseBytePointer: CGDataProviderReleaseBytePointerCallback, getBytesAtPosition getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback, releaseInfo releaseInfo: CGDataProviderReleaseInfoCallback) } ``` |
| To | ``` struct CGDataProviderDirectCallbacks {     var version: UInt32     var getBytePointer: CGDataProviderGetBytePointerCallback?     var releaseBytePointer: CGDataProviderReleaseBytePointerCallback?     var getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback?     var releaseInfo: CGDataProviderReleaseInfoCallback?     init()     init(version version: UInt32, getBytePointer getBytePointer: CGDataProviderGetBytePointerCallback?, releaseBytePointer releaseBytePointer: CGDataProviderReleaseBytePointerCallback?, getBytesAtPosition getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback?, releaseInfo releaseInfo: CGDataProviderReleaseInfoCallback?) } ``` |

Modified [CGDataProviderDirectCallbacks.getBytePointer](https://developer.apple.com/documentation/coregraphics/cgdataproviderdirectcallbacks/1408292-getbytepointer)

|  | Declaration |
| --- | --- |
| From | ``` var getBytePointer: CGDataProviderGetBytePointerCallback ``` |
| To | ``` var getBytePointer: CGDataProviderGetBytePointerCallback? ``` |

Modified [CGDataProviderDirectCallbacks.getBytesAtPosition](https://developer.apple.com/documentation/coregraphics/cgdataproviderdirectcallbacks/1408298-getbytesatposition)

|  | Declaration |
| --- | --- |
| From | ``` var getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback ``` |
| To | ``` var getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback? ``` |

Modified [CGDataProviderDirectCallbacks.releaseBytePointer](https://developer.apple.com/documentation/coregraphics/cgdataproviderdirectcallbacks/1408302-releasebytepointer)

|  | Declaration |
| --- | --- |
| From | ``` var releaseBytePointer: CGDataProviderReleaseBytePointerCallback ``` |
| To | ``` var releaseBytePointer: CGDataProviderReleaseBytePointerCallback? ``` |

Modified [CGDataProviderDirectCallbacks.releaseInfo](https://developer.apple.com/documentation/coregraphics/cgdataproviderdirectcallbacks/1408286-releaseinfo)

|  | Declaration |
| --- | --- |
| From | ``` var releaseInfo: CGDataProviderReleaseInfoCallback ``` |
| To | ``` var releaseInfo: CGDataProviderReleaseInfoCallback? ``` |

Modified [CGDataProviderSequentialCallbacks [struct]](https://developer.apple.com/documentation/coregraphics/cgdataprovidersequentialcallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CGDataProviderSequentialCallbacks {     var version: UInt32     var getBytes: CGDataProviderGetBytesCallback     var skipForward: CGDataProviderSkipForwardCallback     var rewind: CGDataProviderRewindCallback     var releaseInfo: CGDataProviderReleaseInfoCallback     init()     init(version version: UInt32, getBytes getBytes: CGDataProviderGetBytesCallback, skipForward skipForward: CGDataProviderSkipForwardCallback, rewind rewind: CGDataProviderRewindCallback, releaseInfo releaseInfo: CGDataProviderReleaseInfoCallback) } ``` |
| To | ``` struct CGDataProviderSequentialCallbacks {     var version: UInt32     var getBytes: CGDataProviderGetBytesCallback?     var skipForward: CGDataProviderSkipForwardCallback?     var rewind: CGDataProviderRewindCallback?     var releaseInfo: CGDataProviderReleaseInfoCallback?     init()     init(version version: UInt32, getBytes getBytes: CGDataProviderGetBytesCallback?, skipForward skipForward: CGDataProviderSkipForwardCallback?, rewind rewind: CGDataProviderRewindCallback?, releaseInfo releaseInfo: CGDataProviderReleaseInfoCallback?) } ``` |

Modified [CGDataProviderSequentialCallbacks.getBytes](https://developer.apple.com/documentation/coregraphics/cgdataprovidersequentialcallbacks/1408274-getbytes)

|  | Declaration |
| --- | --- |
| From | ``` var getBytes: CGDataProviderGetBytesCallback ``` |
| To | ``` var getBytes: CGDataProviderGetBytesCallback? ``` |

Modified [CGDataProviderSequentialCallbacks.releaseInfo](https://developer.apple.com/documentation/coregraphics/cgdataprovidersequentialcallbacks/1408306-releaseinfo)

|  | Declaration |
| --- | --- |
| From | ``` var releaseInfo: CGDataProviderReleaseInfoCallback ``` |
| To | ``` var releaseInfo: CGDataProviderReleaseInfoCallback? ``` |

Modified [CGDataProviderSequentialCallbacks.rewind](https://developer.apple.com/documentation/coregraphics/cgdataprovidersequentialcallbacks/1408300-rewind)

|  | Declaration |
| --- | --- |
| From | ``` var rewind: CGDataProviderRewindCallback ``` |
| To | ``` var rewind: CGDataProviderRewindCallback? ``` |

Modified [CGDataProviderSequentialCallbacks.skipForward](https://developer.apple.com/documentation/coregraphics/cgdataprovidersequentialcallbacks/1408272-skipforward)

|  | Declaration |
| --- | --- |
| From | ``` var skipForward: CGDataProviderSkipForwardCallback ``` |
| To | ``` var skipForward: CGDataProviderSkipForwardCallback? ``` |

Modified [CGFloat [struct]](https://developer.apple.com/documentation/coregraphics/cgfloat)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CGFloat {     typealias NativeType = Double     init()     init(_ value: Float)     init(_ value: Double)     var native: NativeType } extension CGFloat : FloatingPointType {     init(_ value: UInt8)     init(_ value: Int8)     init(_ value: UInt16)     init(_ value: Int16)     init(_ value: UInt32)     init(_ value: Int32)     init(_ value: UInt64)     init(_ value: Int64)     init(_ value: UInt)     init(_ value: Int)     static var infinity: CGFloat { get }     static var NaN: CGFloat { get }     static var quietNaN: CGFloat { get }     var isSignMinus: Bool { get }     var isNormal: Bool { get }     var isFinite: Bool { get }     var isZero: Bool { get }     var isSubnormal: Bool { get }     var isInfinite: Bool { get }     var isNaN: Bool { get }     var isSignaling: Bool { get }     var floatingPointClass: FloatingPointClassification { get } } extension CGFloat {     static var min: CGFloat { get }     static var max: CGFloat { get } } extension CGFloat : Reflectable {     func getMirror() -> MirrorType } extension CGFloat : Printable {     var description: String { get } } extension CGFloat : Hashable {     var hashValue: Int { get } } extension CGFloat : FloatLiteralConvertible {     init(floatLiteral value: NativeType) } extension CGFloat : IntegerLiteralConvertible {     init(integerLiteral value: Int) } extension CGFloat : AbsoluteValuable {     static func abs(_ x: CGFloat) -> CGFloat } extension CGFloat : Comparable { } extension CGFloat : Strideable {     func distanceTo(_ other: CGFloat) -> CGFloat     func advancedBy(_ amount: CGFloat) -> CGFloat } extension CGFloat : _CVarArgPassedAsDouble {     func encode() -> [Word] } extension CGFloat : _ObjectiveCBridgeable {     init(_ number: NSNumber) } ``` | AbsoluteValuable, Comparable, FloatLiteralConvertible, FloatingPointType, Hashable, IntegerLiteralConvertible, Printable, Reflectable, Strideable |
| To | ``` struct CGFloat {     typealias NativeType = Double     init()     init(_ value: Float)     init(_ value: Double)     var native: NativeType } extension CGFloat : FloatingPointType {     init(_ value: UInt8)     init(_ value: Int8)     init(_ value: UInt16)     init(_ value: Int16)     init(_ value: UInt32)     init(_ value: Int32)     init(_ value: UInt64)     init(_ value: Int64)     init(_ value: UInt)     init(_ value: Int)     static var infinity: CGFloat { get }     static var NaN: CGFloat { get }     static var quietNaN: CGFloat { get }     var isSignMinus: Bool { get }     var isNormal: Bool { get }     var isFinite: Bool { get }     var isZero: Bool { get }     var isSubnormal: Bool { get }     var isInfinite: Bool { get }     var isNaN: Bool { get }     var isSignaling: Bool { get }     var floatingPointClass: FloatingPointClassification { get } } extension CGFloat {     static var min: CGFloat { get }     static var max: CGFloat { get } } extension CGFloat : _Reflectable { } extension CGFloat : CustomStringConvertible {     var description: String { get } } extension CGFloat : Hashable {     var hashValue: Int { get } } extension CGFloat : FloatLiteralConvertible {     init(floatLiteral value: NativeType) } extension CGFloat : IntegerLiteralConvertible {     init(integerLiteral value: Int) } extension CGFloat : SignedNumberType, AbsoluteValuable {     @warn_unused_result     static func abs(_ x: CGFloat) -> CGFloat } extension CGFloat : Equatable { } extension CGFloat : Comparable { } extension CGFloat : Strideable, _Strideable {     func distanceTo(_ other: CGFloat) -> CGFloat     func advancedBy(_ amount: CGFloat) -> CGFloat } extension CGFloat : _CVarArgPassedAsDouble, CVarArgType, _CVarArgAlignedType { } extension CGFloat : _ObjectiveCBridgeable {     init(_ number: NSNumber) } ``` | AbsoluteValuable, CVarArgType, Comparable, CustomStringConvertible, Equatable, FloatLiteralConvertible, FloatingPointType, Hashable, IntegerLiteralConvertible, SignedNumberType, Strideable |

Modified CGFloat.abs(_: CGFloat) -> CGFloat [static]

|  | Declaration |
| --- | --- |
| From | ``` static func abs(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result     static func abs(_ x: CGFloat) -> CGFloat ``` |

Modified [CGFontPostScriptFormat [enum]](https://developer.apple.com/documentation/coregraphics/cgfontpostscriptformat)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct CGFontPostScriptFormat {     init(_ value: UInt32)     var value: UInt32 } ``` | -- | OS X 10.10 | -- |
| To | ``` enum CGFontPostScriptFormat : Int32 {     case Type1     case Type3     case Type42 } ``` | Equatable, Hashable, RawRepresentable | OS X 10.11 | Int32 |

Modified [CGFontPostScriptFormat.Type1](https://developer.apple.com/documentation/coregraphics/cgfontpostscriptformat/type1)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGFontPostScriptFormatType1 | ``` var kCGFontPostScriptFormatType1: CGFontPostScriptFormat { get } ``` | OS X 10.10 |
| To | Type1 | ``` case Type1 ``` | OS X 10.11 |

Modified [CGFontPostScriptFormat.Type3](https://developer.apple.com/documentation/coregraphics/cgfontpostscriptformat/kcgfontpostscriptformattype3)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGFontPostScriptFormatType3 | ``` var kCGFontPostScriptFormatType3: CGFontPostScriptFormat { get } ``` | OS X 10.10 |
| To | Type3 | ``` case Type3 ``` | OS X 10.11 |

Modified [CGFontPostScriptFormat.Type42](https://developer.apple.com/documentation/coregraphics/cgfontpostscriptformat/type42)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGFontPostScriptFormatType42 | ``` var kCGFontPostScriptFormatType42: CGFontPostScriptFormat { get } ``` | OS X 10.10 |
| To | Type42 | ``` case Type42 ``` | OS X 10.11 |

Modified [CGFunctionCallbacks [struct]](https://developer.apple.com/documentation/coregraphics/cgfunctioncallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CGFunctionCallbacks {     var version: UInt32     var evaluate: CGFunctionEvaluateCallback     var releaseInfo: CGFunctionReleaseInfoCallback     init()     init(version version: UInt32, evaluate evaluate: CGFunctionEvaluateCallback, releaseInfo releaseInfo: CGFunctionReleaseInfoCallback) } ``` |
| To | ``` struct CGFunctionCallbacks {     var version: UInt32     var evaluate: CGFunctionEvaluateCallback?     var releaseInfo: CGFunctionReleaseInfoCallback?     init()     init(version version: UInt32, evaluate evaluate: CGFunctionEvaluateCallback?, releaseInfo releaseInfo: CGFunctionReleaseInfoCallback?) } ``` |

Modified [CGFunctionCallbacks.evaluate](https://developer.apple.com/documentation/coregraphics/cgfunctioncallbacks/1390866-evaluate)

|  | Declaration |
| --- | --- |
| From | ``` var evaluate: CGFunctionEvaluateCallback ``` |
| To | ``` var evaluate: CGFunctionEvaluateCallback? ``` |

Modified [CGFunctionCallbacks.releaseInfo](https://developer.apple.com/documentation/coregraphics/cgfunctioncallbacks/1390868-releaseinfo)

|  | Declaration |
| --- | --- |
| From | ``` var releaseInfo: CGFunctionReleaseInfoCallback ``` |
| To | ``` var releaseInfo: CGFunctionReleaseInfoCallback? ``` |

Modified [CGImageAlphaInfo [enum]](https://developer.apple.com/documentation/coregraphics/cgimagealphainfo)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt32 |

Modified [CGInterpolationQuality [enum]](https://developer.apple.com/documentation/coregraphics/cginterpolationquality)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct CGInterpolationQuality {     init(_ value: UInt32)     var value: UInt32 } ``` | -- | OS X 10.10 | -- |
| To | ``` enum CGInterpolationQuality : Int32 {     case Default     case None     case Low     case Medium     case High } ``` | Equatable, Hashable, RawRepresentable | OS X 10.11 | Int32 |

Modified [CGInterpolationQuality.Default](https://developer.apple.com/documentation/coregraphics/cginterpolationquality/default)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGInterpolationDefault | ``` var kCGInterpolationDefault: CGInterpolationQuality { get } ``` | OS X 10.10 |
| To | Default | ``` case Default ``` | OS X 10.11 |

Modified [CGInterpolationQuality.High](https://developer.apple.com/documentation/coregraphics/cginterpolationquality/kcginterpolationhigh)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGInterpolationHigh | ``` var kCGInterpolationHigh: CGInterpolationQuality { get } ``` | OS X 10.10 |
| To | High | ``` case High ``` | OS X 10.11 |

Modified [CGInterpolationQuality.Low](https://developer.apple.com/documentation/coregraphics/cginterpolationquality/low)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGInterpolationLow | ``` var kCGInterpolationLow: CGInterpolationQuality { get } ``` | OS X 10.10 |
| To | Low | ``` case Low ``` | OS X 10.11 |

Modified [CGInterpolationQuality.Medium](https://developer.apple.com/documentation/coregraphics/cginterpolationquality/medium)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGInterpolationMedium | ``` var kCGInterpolationMedium: CGInterpolationQuality { get } ``` | OS X 10.10 |
| To | Medium | ``` case Medium ``` | OS X 10.11 |

Modified [CGInterpolationQuality.None](https://developer.apple.com/documentation/coregraphics/cginterpolationquality/none)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGInterpolationNone | ``` var kCGInterpolationNone: CGInterpolationQuality { get } ``` | OS X 10.10 |
| To | None | ``` case None ``` | OS X 10.11 |

Modified [CGLineCap [enum]](https://developer.apple.com/documentation/coregraphics/cglinecap)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct CGLineCap {     init(_ value: UInt32)     var value: UInt32 } ``` | -- | OS X 10.10 | -- |
| To | ``` enum CGLineCap : Int32 {     case Butt     case Round     case Square } ``` | Equatable, Hashable, RawRepresentable | OS X 10.11 | Int32 |

Modified [CGLineCap.Butt](https://developer.apple.com/documentation/coregraphics/cglinecap/kcglinecapbutt)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGLineCapButt | ``` var kCGLineCapButt: CGLineCap { get } ``` | OS X 10.10 |
| To | Butt | ``` case Butt ``` | OS X 10.11 |

Modified [CGLineCap.Round](https://developer.apple.com/documentation/coregraphics/cglinecap/round)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGLineCapRound | ``` var kCGLineCapRound: CGLineCap { get } ``` | OS X 10.10 |
| To | Round | ``` case Round ``` | OS X 10.11 |

Modified [CGLineCap.Square](https://developer.apple.com/documentation/coregraphics/cglinecap/kcglinecapsquare)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGLineCapSquare | ``` var kCGLineCapSquare: CGLineCap { get } ``` | OS X 10.10 |
| To | Square | ``` case Square ``` | OS X 10.11 |

Modified [CGLineJoin [enum]](https://developer.apple.com/documentation/coregraphics/cglinejoin)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct CGLineJoin {     init(_ value: UInt32)     var value: UInt32 } ``` | -- | OS X 10.10 | -- |
| To | ``` enum CGLineJoin : Int32 {     case Miter     case Round     case Bevel } ``` | Equatable, Hashable, RawRepresentable | OS X 10.11 | Int32 |

Modified [CGLineJoin.Bevel](https://developer.apple.com/documentation/coregraphics/cglinejoin/bevel)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGLineJoinBevel | ``` var kCGLineJoinBevel: CGLineJoin { get } ``` | OS X 10.10 |
| To | Bevel | ``` case Bevel ``` | OS X 10.11 |

Modified [CGLineJoin.Miter](https://developer.apple.com/documentation/coregraphics/cglinejoin/miter)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGLineJoinMiter | ``` var kCGLineJoinMiter: CGLineJoin { get } ``` | OS X 10.10 |
| To | Miter | ``` case Miter ``` | OS X 10.11 |

Modified [CGLineJoin.Round](https://developer.apple.com/documentation/coregraphics/cglinejoin/round)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGLineJoinRound | ``` var kCGLineJoinRound: CGLineJoin { get } ``` | OS X 10.10 |
| To | Round | ``` case Round ``` | OS X 10.11 |

Modified [CGPathDrawingMode [enum]](https://developer.apple.com/documentation/coregraphics/cgpathdrawingmode)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct CGPathDrawingMode {     init(_ value: UInt32)     var value: UInt32 } ``` | -- | OS X 10.10 | -- |
| To | ``` enum CGPathDrawingMode : Int32 {     case Fill     case EOFill     case Stroke     case FillStroke     case EOFillStroke } ``` | Equatable, Hashable, RawRepresentable | OS X 10.11 | Int32 |

Modified [CGPathDrawingMode.EOFill](https://developer.apple.com/documentation/coregraphics/cgpathdrawingmode/kcgpatheofill)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPathEOFill | ``` var kCGPathEOFill: CGPathDrawingMode { get } ``` | OS X 10.10 |
| To | EOFill | ``` case EOFill ``` | OS X 10.11 |

Modified [CGPathDrawingMode.EOFillStroke](https://developer.apple.com/documentation/coregraphics/cgpathdrawingmode/eofillstroke)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPathEOFillStroke | ``` var kCGPathEOFillStroke: CGPathDrawingMode { get } ``` | OS X 10.10 |
| To | EOFillStroke | ``` case EOFillStroke ``` | OS X 10.11 |

Modified [CGPathDrawingMode.Fill](https://developer.apple.com/documentation/coregraphics/cgpathdrawingmode/fill)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPathFill | ``` var kCGPathFill: CGPathDrawingMode { get } ``` | OS X 10.10 |
| To | Fill | ``` case Fill ``` | OS X 10.11 |

Modified [CGPathDrawingMode.FillStroke](https://developer.apple.com/documentation/coregraphics/cgpathdrawingmode/kcgpathfillstroke)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPathFillStroke | ``` var kCGPathFillStroke: CGPathDrawingMode { get } ``` | OS X 10.10 |
| To | FillStroke | ``` case FillStroke ``` | OS X 10.11 |

Modified [CGPathDrawingMode.Stroke](https://developer.apple.com/documentation/coregraphics/cgpathdrawingmode/kcgpathstroke)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPathStroke | ``` var kCGPathStroke: CGPathDrawingMode { get } ``` | OS X 10.10 |
| To | Stroke | ``` case Stroke ``` | OS X 10.11 |

Modified [CGPathElement [struct]](https://developer.apple.com/documentation/coregraphics/cgpathelement)

|  | Declaration |
| --- | --- |
| From | ``` struct CGPathElement {     var type: CGPathElementType     var points: UnsafeMutablePointer<CGPoint>     init()     init(type type: CGPathElementType, points points: UnsafeMutablePointer<CGPoint>) } ``` |
| To | ``` struct CGPathElement {     var type: CGPathElementType     var points: UnsafeMutablePointer<CGPoint> } ``` |

Modified [CGPathElementType [enum]](https://developer.apple.com/documentation/coregraphics/cgpathelementtype)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct CGPathElementType {     init(_ value: UInt32)     var value: UInt32 } ``` | -- | OS X 10.10 | -- |
| To | ``` enum CGPathElementType : Int32 {     case MoveToPoint     case AddLineToPoint     case AddQuadCurveToPoint     case AddCurveToPoint     case CloseSubpath } ``` | Equatable, Hashable, RawRepresentable | OS X 10.11 | Int32 |

Modified [CGPathElementType.AddCurveToPoint](https://developer.apple.com/documentation/coregraphics/cgpathelementtype/addcurvetopoint)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPathElementAddCurveToPoint | ``` var kCGPathElementAddCurveToPoint: CGPathElementType { get } ``` | OS X 10.10 |
| To | AddCurveToPoint | ``` case AddCurveToPoint ``` | OS X 10.11 |

Modified [CGPathElementType.AddLineToPoint](https://developer.apple.com/documentation/coregraphics/cgpathelementtype/addlinetopoint)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPathElementAddLineToPoint | ``` var kCGPathElementAddLineToPoint: CGPathElementType { get } ``` | OS X 10.10 |
| To | AddLineToPoint | ``` case AddLineToPoint ``` | OS X 10.11 |

Modified [CGPathElementType.AddQuadCurveToPoint](https://developer.apple.com/documentation/coregraphics/cgpathelementtype/addquadcurvetopoint)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPathElementAddQuadCurveToPoint | ``` var kCGPathElementAddQuadCurveToPoint: CGPathElementType { get } ``` | OS X 10.10 |
| To | AddQuadCurveToPoint | ``` case AddQuadCurveToPoint ``` | OS X 10.11 |

Modified [CGPathElementType.CloseSubpath](https://developer.apple.com/documentation/coregraphics/cgpathelementtype/closesubpath)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPathElementCloseSubpath | ``` var kCGPathElementCloseSubpath: CGPathElementType { get } ``` | OS X 10.10 |
| To | CloseSubpath | ``` case CloseSubpath ``` | OS X 10.11 |

Modified [CGPathElementType.MoveToPoint](https://developer.apple.com/documentation/coregraphics/cgpathelementtype/movetopoint)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPathElementMoveToPoint | ``` var kCGPathElementMoveToPoint: CGPathElementType { get } ``` | OS X 10.10 |
| To | MoveToPoint | ``` case MoveToPoint ``` | OS X 10.11 |

Modified [CGPatternCallbacks [struct]](https://developer.apple.com/documentation/coregraphics/cgpatterncallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CGPatternCallbacks {     var version: UInt32     var drawPattern: CGPatternDrawPatternCallback     var releaseInfo: CGPatternReleaseInfoCallback     init()     init(version version: UInt32, drawPattern drawPattern: CGPatternDrawPatternCallback, releaseInfo releaseInfo: CGPatternReleaseInfoCallback) } ``` |
| To | ``` struct CGPatternCallbacks {     var version: UInt32     var drawPattern: CGPatternDrawPatternCallback?     var releaseInfo: CGPatternReleaseInfoCallback?     init()     init(version version: UInt32, drawPattern drawPattern: CGPatternDrawPatternCallback?, releaseInfo releaseInfo: CGPatternReleaseInfoCallback?) } ``` |

Modified [CGPatternCallbacks.drawPattern](https://developer.apple.com/documentation/coregraphics/cgpatterncallbacks/1454736-drawpattern)

|  | Declaration |
| --- | --- |
| From | ``` var drawPattern: CGPatternDrawPatternCallback ``` |
| To | ``` var drawPattern: CGPatternDrawPatternCallback? ``` |

Modified [CGPatternCallbacks.releaseInfo](https://developer.apple.com/documentation/coregraphics/cgpatterncallbacks/1455379-releaseinfo)

|  | Declaration |
| --- | --- |
| From | ``` var releaseInfo: CGPatternReleaseInfoCallback ``` |
| To | ``` var releaseInfo: CGPatternReleaseInfoCallback? ``` |

Modified [CGPatternTiling [enum]](https://developer.apple.com/documentation/coregraphics/cgpatterntiling)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct CGPatternTiling {     init(_ value: UInt32)     var value: UInt32 } ``` | -- | OS X 10.10 | -- |
| To | ``` enum CGPatternTiling : Int32 {     case NoDistortion     case ConstantSpacingMinimalDistortion     case ConstantSpacing } ``` | Equatable, Hashable, RawRepresentable | OS X 10.11 | Int32 |

Modified [CGPatternTiling.ConstantSpacing](https://developer.apple.com/documentation/coregraphics/cgpatterntiling/constantspacing)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPatternTilingConstantSpacing | ``` var kCGPatternTilingConstantSpacing: CGPatternTiling { get } ``` | OS X 10.10 |
| To | ConstantSpacing | ``` case ConstantSpacing ``` | OS X 10.11 |

Modified [CGPatternTiling.ConstantSpacingMinimalDistortion](https://developer.apple.com/documentation/coregraphics/cgpatterntiling/kcgpatterntilingconstantspacingminimaldistortion)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPatternTilingConstantSpacingMinimalDistortion | ``` var kCGPatternTilingConstantSpacingMinimalDistortion: CGPatternTiling { get } ``` | OS X 10.10 |
| To | ConstantSpacingMinimalDistortion | ``` case ConstantSpacingMinimalDistortion ``` | OS X 10.11 |

Modified [CGPatternTiling.NoDistortion](https://developer.apple.com/documentation/coregraphics/cgpatterntiling/nodistortion)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPatternTilingNoDistortion | ``` var kCGPatternTilingNoDistortion: CGPatternTiling { get } ``` | OS X 10.10 |
| To | NoDistortion | ``` case NoDistortion ``` | OS X 10.11 |

Modified [CGPDFBox [enum]](https://developer.apple.com/documentation/coregraphics/cgpdfbox)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct CGPDFBox {     init(_ value: UInt32)     var value: UInt32 } ``` | -- | OS X 10.10 | -- |
| To | ``` enum CGPDFBox : Int32 {     case MediaBox     case CropBox     case BleedBox     case TrimBox     case ArtBox } ``` | Equatable, Hashable, RawRepresentable | OS X 10.11 | Int32 |

Modified [CGPDFBox.ArtBox](https://developer.apple.com/documentation/coregraphics/cgpdfbox/artbox)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPDFArtBox | ``` var kCGPDFArtBox: CGPDFBox { get } ``` | OS X 10.10 |
| To | ArtBox | ``` case ArtBox ``` | OS X 10.11 |

Modified [CGPDFBox.BleedBox](https://developer.apple.com/documentation/coregraphics/cgpdfbox/bleedbox)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPDFBleedBox | ``` var kCGPDFBleedBox: CGPDFBox { get } ``` | OS X 10.10 |
| To | BleedBox | ``` case BleedBox ``` | OS X 10.11 |

Modified [CGPDFBox.CropBox](https://developer.apple.com/documentation/coregraphics/cgpdfbox/kcgpdfcropbox)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPDFCropBox | ``` var kCGPDFCropBox: CGPDFBox { get } ``` | OS X 10.10 |
| To | CropBox | ``` case CropBox ``` | OS X 10.11 |

Modified [CGPDFBox.MediaBox](https://developer.apple.com/documentation/coregraphics/cgpdfbox/kcgpdfmediabox)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPDFMediaBox | ``` var kCGPDFMediaBox: CGPDFBox { get } ``` | OS X 10.10 |
| To | MediaBox | ``` case MediaBox ``` | OS X 10.11 |

Modified [CGPDFBox.TrimBox](https://developer.apple.com/documentation/coregraphics/cgpdfbox/kcgpdftrimbox)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPDFTrimBox | ``` var kCGPDFTrimBox: CGPDFBox { get } ``` | OS X 10.10 |
| To | TrimBox | ``` case TrimBox ``` | OS X 10.11 |

Modified [CGPDFDataFormat [enum]](https://developer.apple.com/documentation/coregraphics/cgpdfdataformat)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct CGPDFDataFormat {     init(_ value: UInt32)     var value: UInt32 } ``` | -- | OS X 10.10 | -- |
| To | ``` enum CGPDFDataFormat : Int32 {     case Raw     case JPEGEncoded     case JPEG2000 } ``` | Equatable, Hashable, RawRepresentable | OS X 10.11 | Int32 |

Modified [CGPDFDataFormat.JPEG2000](https://developer.apple.com/documentation/coregraphics/cgpdfdataformat/cgpdfdataformatjpeg2000)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | CGPDFDataFormatJPEG2000 | ``` var CGPDFDataFormatJPEG2000: CGPDFDataFormat { get } ``` | OS X 10.10 |
| To | JPEG2000 | ``` case JPEG2000 ``` | OS X 10.11 |

Modified [CGPDFDataFormat.JPEGEncoded](https://developer.apple.com/documentation/coregraphics/cgpdfdataformat/cgpdfdataformatjpegencoded)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | CGPDFDataFormatJPEGEncoded | ``` var CGPDFDataFormatJPEGEncoded: CGPDFDataFormat { get } ``` | OS X 10.10 |
| To | JPEGEncoded | ``` case JPEGEncoded ``` | OS X 10.11 |

Modified [CGPDFDataFormat.Raw](https://developer.apple.com/documentation/coregraphics/cgpdfdataformat/raw)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | CGPDFDataFormatRaw | ``` var CGPDFDataFormatRaw: CGPDFDataFormat { get } ``` | OS X 10.10 |
| To | Raw | ``` case Raw ``` | OS X 10.11 |

Modified [CGPDFObjectType [enum]](https://developer.apple.com/documentation/coregraphics/cgpdfobjecttype)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct CGPDFObjectType {     init(_ value: UInt32)     var value: UInt32 } ``` | -- | OS X 10.10 | -- |
| To | ``` enum CGPDFObjectType : Int32 {     case Null     case Boolean     case Integer     case Real     case Name     case String     case Array     case Dictionary     case Stream } ``` | Equatable, Hashable, RawRepresentable | OS X 10.11 | Int32 |

Modified [CGPDFObjectType.Array](https://developer.apple.com/documentation/coregraphics/cgpdfobjecttype/array)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPDFObjectTypeArray | ``` var kCGPDFObjectTypeArray: CGPDFObjectType { get } ``` | OS X 10.10 |
| To | Array | ``` case Array ``` | OS X 10.11 |

Modified [CGPDFObjectType.Boolean](https://developer.apple.com/documentation/coregraphics/cgpdfobjecttype/kcgpdfobjecttypeboolean)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPDFObjectTypeBoolean | ``` var kCGPDFObjectTypeBoolean: CGPDFObjectType { get } ``` | OS X 10.10 |
| To | Boolean | ``` case Boolean ``` | OS X 10.11 |

Modified [CGPDFObjectType.Dictionary](https://developer.apple.com/documentation/coregraphics/cgpdfobjecttype/dictionary)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPDFObjectTypeDictionary | ``` var kCGPDFObjectTypeDictionary: CGPDFObjectType { get } ``` | OS X 10.10 |
| To | Dictionary | ``` case Dictionary ``` | OS X 10.11 |

Modified [CGPDFObjectType.Integer](https://developer.apple.com/documentation/coregraphics/cgpdfobjecttype/kcgpdfobjecttypeinteger)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPDFObjectTypeInteger | ``` var kCGPDFObjectTypeInteger: CGPDFObjectType { get } ``` | OS X 10.10 |
| To | Integer | ``` case Integer ``` | OS X 10.11 |

Modified [CGPDFObjectType.Name](https://developer.apple.com/documentation/coregraphics/cgpdfobjecttype/kcgpdfobjecttypename)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPDFObjectTypeName | ``` var kCGPDFObjectTypeName: CGPDFObjectType { get } ``` | OS X 10.10 |
| To | Name | ``` case Name ``` | OS X 10.11 |

Modified [CGPDFObjectType.Null](https://developer.apple.com/documentation/coregraphics/cgpdfobjecttype/null)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPDFObjectTypeNull | ``` var kCGPDFObjectTypeNull: CGPDFObjectType { get } ``` | OS X 10.10 |
| To | Null | ``` case Null ``` | OS X 10.11 |

Modified [CGPDFObjectType.Real](https://developer.apple.com/documentation/coregraphics/cgpdfobjecttype/kcgpdfobjecttypereal)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPDFObjectTypeReal | ``` var kCGPDFObjectTypeReal: CGPDFObjectType { get } ``` | OS X 10.10 |
| To | Real | ``` case Real ``` | OS X 10.11 |

Modified [CGPDFObjectType.Stream](https://developer.apple.com/documentation/coregraphics/cgpdfobjecttype/stream)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPDFObjectTypeStream | ``` var kCGPDFObjectTypeStream: CGPDFObjectType { get } ``` | OS X 10.10 |
| To | Stream | ``` case Stream ``` | OS X 10.11 |

Modified [CGPDFObjectType.String](https://developer.apple.com/documentation/coregraphics/cgpdfobjecttype/string)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGPDFObjectTypeString | ``` var kCGPDFObjectTypeString: CGPDFObjectType { get } ``` | OS X 10.10 |
| To | String | ``` case String ``` | OS X 10.11 |

Modified [CGPoint [struct]](https://developer.apple.com/documentation/coregraphics/cgpoint)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CGPoint {     var x: CGFloat     var y: CGFloat     init()     init(x x: CGFloat, y y: CGFloat) } extension CGPoint {     static var zeroPoint: CGPoint { get }     init(x x: Int, y y: Int)     init(x x: Double, y y: Double) } extension CGPoint : Equatable { } extension CGPoint : Reflectable {     func getMirror() -> MirrorType } extension CGPoint : Reflectable {     func getMirror() -> MirrorType } extension CGPoint : Equatable { } extension CGPoint {     static var zeroPoint: CGPoint { get }     init(x x: Int, y y: Int)     init(x x: Double, y y: Double) } ``` | Equatable, Reflectable |
| To | ``` struct CGPoint {     var x: CGFloat     var y: CGFloat     init()     init(x x: CGFloat, y y: CGFloat) } extension CGPoint {     static var zero: CGPoint { get }     init(x x: Int, y y: Int)     init(x x: Double, y y: Double)     static var zeroPoint: CGPoint } extension CGPoint : Equatable { } extension CGPoint : _Reflectable { } extension CGPoint {     static var zero: CGPoint { get }     init(x x: Int, y y: Int)     init(x x: Double, y y: Double)     static var zeroPoint: CGPoint } extension CGPoint : Equatable { } extension CGPoint : _Reflectable { } ``` | Equatable |

Modified [CGPSConverterCallbacks [struct]](https://developer.apple.com/documentation/coregraphics/cgpsconvertercallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CGPSConverterCallbacks {     var version: UInt32     var beginDocument: CGPSConverterBeginDocumentCallback     var endDocument: CGPSConverterEndDocumentCallback     var beginPage: CGPSConverterBeginPageCallback     var endPage: CGPSConverterEndPageCallback     var noteProgress: CGPSConverterProgressCallback     var noteMessage: CGPSConverterMessageCallback     var releaseInfo: CGPSConverterReleaseInfoCallback     init()     init(version version: UInt32, beginDocument beginDocument: CGPSConverterBeginDocumentCallback, endDocument endDocument: CGPSConverterEndDocumentCallback, beginPage beginPage: CGPSConverterBeginPageCallback, endPage endPage: CGPSConverterEndPageCallback, noteProgress noteProgress: CGPSConverterProgressCallback, noteMessage noteMessage: CGPSConverterMessageCallback, releaseInfo releaseInfo: CGPSConverterReleaseInfoCallback) } ``` |
| To | ``` struct CGPSConverterCallbacks {     var version: UInt32     var beginDocument: CGPSConverterBeginDocumentCallback?     var endDocument: CGPSConverterEndDocumentCallback?     var beginPage: CGPSConverterBeginPageCallback?     var endPage: CGPSConverterEndPageCallback?     var noteProgress: CGPSConverterProgressCallback?     var noteMessage: CGPSConverterMessageCallback?     var releaseInfo: CGPSConverterReleaseInfoCallback?     init()     init(version version: UInt32, beginDocument beginDocument: CGPSConverterBeginDocumentCallback?, endDocument endDocument: CGPSConverterEndDocumentCallback?, beginPage beginPage: CGPSConverterBeginPageCallback?, endPage endPage: CGPSConverterEndPageCallback?, noteProgress noteProgress: CGPSConverterProgressCallback?, noteMessage noteMessage: CGPSConverterMessageCallback?, releaseInfo releaseInfo: CGPSConverterReleaseInfoCallback?) } ``` |

Modified [CGPSConverterCallbacks.beginDocument](https://developer.apple.com/documentation/coregraphics/cgpsconvertercallbacks/1456036-begindocument)

|  | Declaration |
| --- | --- |
| From | ``` var beginDocument: CGPSConverterBeginDocumentCallback ``` |
| To | ``` var beginDocument: CGPSConverterBeginDocumentCallback? ``` |

Modified [CGPSConverterCallbacks.beginPage](https://developer.apple.com/documentation/coregraphics/cgpsconvertercallbacks/1454345-beginpage)

|  | Declaration |
| --- | --- |
| From | ``` var beginPage: CGPSConverterBeginPageCallback ``` |
| To | ``` var beginPage: CGPSConverterBeginPageCallback? ``` |

Modified [CGPSConverterCallbacks.endDocument](https://developer.apple.com/documentation/coregraphics/cgpsconvertercallbacks/1454481-enddocument)

|  | Declaration |
| --- | --- |
| From | ``` var endDocument: CGPSConverterEndDocumentCallback ``` |
| To | ``` var endDocument: CGPSConverterEndDocumentCallback? ``` |

Modified [CGPSConverterCallbacks.endPage](https://developer.apple.com/documentation/coregraphics/cgpsconvertercallbacks/1454830-endpage)

|  | Declaration |
| --- | --- |
| From | ``` var endPage: CGPSConverterEndPageCallback ``` |
| To | ``` var endPage: CGPSConverterEndPageCallback? ``` |

Modified [CGPSConverterCallbacks.noteMessage](https://developer.apple.com/documentation/coregraphics/cgpsconvertercallbacks/1455859-notemessage)

|  | Declaration |
| --- | --- |
| From | ``` var noteMessage: CGPSConverterMessageCallback ``` |
| To | ``` var noteMessage: CGPSConverterMessageCallback? ``` |

Modified [CGPSConverterCallbacks.noteProgress](https://developer.apple.com/documentation/coregraphics/cgpsconvertercallbacks/1455344-noteprogress)

|  | Declaration |
| --- | --- |
| From | ``` var noteProgress: CGPSConverterProgressCallback ``` |
| To | ``` var noteProgress: CGPSConverterProgressCallback? ``` |

Modified [CGPSConverterCallbacks.releaseInfo](https://developer.apple.com/documentation/coregraphics/cgpsconvertercallbacks/1455599-releaseinfo)

|  | Declaration |
| --- | --- |
| From | ``` var releaseInfo: CGPSConverterReleaseInfoCallback ``` |
| To | ``` var releaseInfo: CGPSConverterReleaseInfoCallback? ``` |

Modified [CGRect [struct]](https://developer.apple.com/documentation/coregraphics/cgrect)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CGRect {     var origin: CGPoint     var size: CGSize     init()     init(origin origin: CGPoint, size size: CGSize) } extension CGRect {     static var zeroRect: CGRect { get }     static var nullRect: CGRect { get }     static var infiniteRect: CGRect { get }     init(x x: CGFloat, y y: CGFloat, width width: CGFloat, height height: CGFloat)     init(x x: Double, y y: Double, width width: Double, height height: Double)     init(x x: Int, y y: Int, width width: Int, height height: Int)     var width: CGFloat { get }     var height: CGFloat { get }     var minX: CGFloat { get }     var midX: CGFloat { get }     var maxX: CGFloat { get }     var minY: CGFloat { get }     var midY: CGFloat { get }     var maxY: CGFloat { get }     var isNull: Bool { get }     var isEmpty: Bool { get }     var isInfinite: Bool { get }     var standardizedRect: CGRect { get }     mutating func standardize()     var integerRect: CGRect { get }     mutating func integerize()     func rectByInsetting(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     mutating func inset(dx dx: CGFloat, dy dy: CGFloat)     func rectByOffsetting(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     mutating func offset(dx dx: CGFloat, dy dy: CGFloat)     func rectByUnion(_ withRect: CGRect) -> CGRect     mutating func union(_ withRect: CGRect)     func rectByIntersecting(_ withRect: CGRect) -> CGRect     mutating func intersect(_ withRect: CGRect)     func rectsByDividing(_ atDistance: CGFloat, fromEdge fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect)     func contains(_ rect: CGRect) -> Bool     func contains(_ point: CGPoint) -> Bool     func intersects(_ rect: CGRect) -> Bool } extension CGRect : Equatable { } extension CGRect : Reflectable {     func getMirror() -> MirrorType } extension CGRect : Reflectable {     func getMirror() -> MirrorType } extension CGRect : Equatable { } extension CGRect {     static var zeroRect: CGRect { get }     static var nullRect: CGRect { get }     static var infiniteRect: CGRect { get }     init(x x: CGFloat, y y: CGFloat, width width: CGFloat, height height: CGFloat)     init(x x: Double, y y: Double, width width: Double, height height: Double)     init(x x: Int, y y: Int, width width: Int, height height: Int)     var width: CGFloat { get }     var height: CGFloat { get }     var minX: CGFloat { get }     var midX: CGFloat { get }     var maxX: CGFloat { get }     var minY: CGFloat { get }     var midY: CGFloat { get }     var maxY: CGFloat { get }     var isNull: Bool { get }     var isEmpty: Bool { get }     var isInfinite: Bool { get }     var standardizedRect: CGRect { get }     mutating func standardize()     var integerRect: CGRect { get }     mutating func integerize()     func rectByInsetting(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     mutating func inset(dx dx: CGFloat, dy dy: CGFloat)     func rectByOffsetting(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     mutating func offset(dx dx: CGFloat, dy dy: CGFloat)     func rectByUnion(_ withRect: CGRect) -> CGRect     mutating func union(_ withRect: CGRect)     func rectByIntersecting(_ withRect: CGRect) -> CGRect     mutating func intersect(_ withRect: CGRect)     func rectsByDividing(_ atDistance: CGFloat, fromEdge fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect)     func contains(_ rect: CGRect) -> Bool     func contains(_ point: CGPoint) -> Bool     func intersects(_ rect: CGRect) -> Bool } ``` | Equatable, Reflectable |
| To | ``` struct CGRect {     var origin: CGPoint     var size: CGSize     init()     init(origin origin: CGPoint, size size: CGSize) } extension CGRect {     static var zero: CGRect { get }     static var null: CGRect { get }     static var infinite: CGRect { get }     init(x x: CGFloat, y y: CGFloat, width width: CGFloat, height height: CGFloat)     init(x x: Double, y y: Double, width width: Double, height height: Double)     init(x x: Int, y y: Int, width width: Int, height height: Int)     var width: CGFloat { get }     var height: CGFloat { get }     var minX: CGFloat { get }     var midX: CGFloat { get }     var maxX: CGFloat { get }     var minY: CGFloat { get }     var midY: CGFloat { get }     var maxY: CGFloat { get }     var isNull: Bool { get }     var isEmpty: Bool { get }     var isInfinite: Bool { get }     var standardized: CGRect { get }     var integral: CGRect { get }     mutating func standardizeInPlace()     mutating func makeIntegralInPlace()     @warn_unused_result(mutable_variant="insetInPlace")     func insetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     mutating func insetInPlace(dx dx: CGFloat, dy dy: CGFloat)     @warn_unused_result(mutable_variant="offsetInPlace")     func offsetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     mutating func offsetInPlace(dx dx: CGFloat, dy dy: CGFloat)     @warn_unused_result(mutable_variant="unionInPlace")     func union(_ rect: CGRect) -> CGRect     mutating func unionInPlace(_ rect: CGRect)     @warn_unused_result(mutable_variant="intersectInPlace")     func intersect(_ rect: CGRect) -> CGRect     mutating func intersectInPlace(_ rect: CGRect)     @warn_unused_result     func divide(_ atDistance: CGFloat, fromEdge fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect)     @warn_unused_result     func contains(_ rect: CGRect) -> Bool     @warn_unused_result     func contains(_ point: CGPoint) -> Bool     @warn_unused_result     func intersects(_ rect: CGRect) -> Bool     static var zeroRect: CGRect     static var infiniteRect: CGRect     static var nullRect: CGRect     var standardizedRect: CGRect { get }     var integerRect: CGRect { get }     mutating func standardize() -> CGRect     mutating func integerize()     func rectByInsetting(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     func inset(dx dx: CGFloat, dy dy: CGFloat)     func rectByOffsetting(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     func offset(dx dx: CGFloat, dy dy: CGFloat)     mutating func union(_ withRect: CGRect)     func rectByUnion(_ withRect: CGRect) -> CGRect     mutating func intersect(_ withRect: CGRect)     func rectByIntersecting(_ withRect: CGRect) -> CGRect     func rectsByDividing(_ atDistance: CGFloat, fromEdge fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect) } extension CGRect : Equatable { } extension CGRect : _Reflectable { } extension CGRect {     static var zero: CGRect { get }     static var null: CGRect { get }     static var infinite: CGRect { get }     init(x x: CGFloat, y y: CGFloat, width width: CGFloat, height height: CGFloat)     init(x x: Double, y y: Double, width width: Double, height height: Double)     init(x x: Int, y y: Int, width width: Int, height height: Int)     var width: CGFloat { get }     var height: CGFloat { get }     var minX: CGFloat { get }     var midX: CGFloat { get }     var maxX: CGFloat { get }     var minY: CGFloat { get }     var midY: CGFloat { get }     var maxY: CGFloat { get }     var isNull: Bool { get }     var isEmpty: Bool { get }     var isInfinite: Bool { get }     var standardized: CGRect { get }     var integral: CGRect { get }     mutating func standardizeInPlace()     mutating func makeIntegralInPlace()     @warn_unused_result(mutable_variant="insetInPlace")     func insetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     mutating func insetInPlace(dx dx: CGFloat, dy dy: CGFloat)     @warn_unused_result(mutable_variant="offsetInPlace")     func offsetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     mutating func offsetInPlace(dx dx: CGFloat, dy dy: CGFloat)     @warn_unused_result(mutable_variant="unionInPlace")     func union(_ rect: CGRect) -> CGRect     mutating func unionInPlace(_ rect: CGRect)     @warn_unused_result(mutable_variant="intersectInPlace")     func intersect(_ rect: CGRect) -> CGRect     mutating func intersectInPlace(_ rect: CGRect)     @warn_unused_result     func divide(_ atDistance: CGFloat, fromEdge fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect)     @warn_unused_result     func contains(_ rect: CGRect) -> Bool     @warn_unused_result     func contains(_ point: CGPoint) -> Bool     @warn_unused_result     func intersects(_ rect: CGRect) -> Bool     static var zeroRect: CGRect     static var infiniteRect: CGRect     static var nullRect: CGRect     var standardizedRect: CGRect { get }     var integerRect: CGRect { get }     mutating func standardize() -> CGRect     mutating func integerize()     func rectByInsetting(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     func inset(dx dx: CGFloat, dy dy: CGFloat)     func rectByOffsetting(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     func offset(dx dx: CGFloat, dy dy: CGFloat)     mutating func union(_ withRect: CGRect)     func rectByUnion(_ withRect: CGRect) -> CGRect     mutating func intersect(_ withRect: CGRect)     func rectByIntersecting(_ withRect: CGRect) -> CGRect     func rectsByDividing(_ atDistance: CGFloat, fromEdge fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect) } extension CGRect : Equatable { } extension CGRect : _Reflectable { } ``` | Equatable |

Modified CGRect.contains(_: CGRect) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func contains(_ rect: CGRect) -> Bool ``` |
| To | ``` @warn_unused_result     func contains(_ rect: CGRect) -> Bool ``` |

Modified CGRect.contains(_: CGPoint) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func contains(_ point: CGPoint) -> Bool ``` |
| To | ``` @warn_unused_result     func contains(_ point: CGPoint) -> Bool ``` |

Modified CGRect.intersects(_: CGRect) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func intersects(_ rect: CGRect) -> Bool ``` |
| To | ``` @warn_unused_result     func intersects(_ rect: CGRect) -> Bool ``` |

Modified [CGRectEdge [enum]](https://developer.apple.com/documentation/coregraphics/cgrectedge)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum CGRectEdge : UInt32 {     case MinXEdge     case MinYEdge     case MaxXEdge     case MaxYEdge } ``` | -- |
| To | ``` enum CGRectEdge : UInt32 {     case MinXEdge     case MinYEdge     case MaxXEdge     case MaxYEdge } extension CGRectEdge {     init(rectEdge rectEdge: NSRectEdge) } ``` | UInt32 |

Modified [CGSize [struct]](https://developer.apple.com/documentation/coregraphics/cgsize)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CGSize {     var width: CGFloat     var height: CGFloat     init()     init(width width: CGFloat, height height: CGFloat) } extension CGSize {     static var zeroSize: CGSize { get }     init(width width: Int, height height: Int)     init(width width: Double, height height: Double) } extension CGSize : Equatable { } extension CGSize : Reflectable {     func getMirror() -> MirrorType } extension CGSize : Reflectable {     func getMirror() -> MirrorType } extension CGSize : Equatable { } extension CGSize {     static var zeroSize: CGSize { get }     init(width width: Int, height height: Int)     init(width width: Double, height height: Double) } ``` | Equatable, Reflectable |
| To | ``` struct CGSize {     var width: CGFloat     var height: CGFloat     init()     init(width width: CGFloat, height height: CGFloat) } extension CGSize {     static var zero: CGSize { get }     init(width width: Int, height height: Int)     init(width width: Double, height height: Double)     static var zeroSize: CGSize } extension CGSize : Equatable { } extension CGSize : _Reflectable { } extension CGSize : _Reflectable { } extension CGSize : Equatable { } extension CGSize {     static var zero: CGSize { get }     init(width width: Int, height height: Int)     init(width width: Double, height height: Double)     static var zeroSize: CGSize } ``` | Equatable |

Modified [CGTextDrawingMode [enum]](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct CGTextDrawingMode {     init(_ value: UInt32)     var value: UInt32 } ``` | -- | OS X 10.10 | -- |
| To | ``` enum CGTextDrawingMode : Int32 {     case Fill     case Stroke     case FillStroke     case Invisible     case FillClip     case StrokeClip     case FillStrokeClip     case Clip } ``` | Equatable, Hashable, RawRepresentable | OS X 10.11 | Int32 |

Modified [CGTextDrawingMode.Clip](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode/clip)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGTextClip | ``` var kCGTextClip: CGTextDrawingMode { get } ``` | OS X 10.10 |
| To | Clip | ``` case Clip ``` | OS X 10.11 |

Modified [CGTextDrawingMode.Fill](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode/fill)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGTextFill | ``` var kCGTextFill: CGTextDrawingMode { get } ``` | OS X 10.10 |
| To | Fill | ``` case Fill ``` | OS X 10.11 |

Modified [CGTextDrawingMode.FillClip](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode/fillclip)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGTextFillClip | ``` var kCGTextFillClip: CGTextDrawingMode { get } ``` | OS X 10.10 |
| To | FillClip | ``` case FillClip ``` | OS X 10.11 |

Modified [CGTextDrawingMode.FillStroke](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode/fillstroke)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGTextFillStroke | ``` var kCGTextFillStroke: CGTextDrawingMode { get } ``` | OS X 10.10 |
| To | FillStroke | ``` case FillStroke ``` | OS X 10.11 |

Modified [CGTextDrawingMode.FillStrokeClip](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode/fillstrokeclip)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGTextFillStrokeClip | ``` var kCGTextFillStrokeClip: CGTextDrawingMode { get } ``` | OS X 10.10 |
| To | FillStrokeClip | ``` case FillStrokeClip ``` | OS X 10.11 |

Modified [CGTextDrawingMode.Invisible](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode/invisible)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGTextInvisible | ``` var kCGTextInvisible: CGTextDrawingMode { get } ``` | OS X 10.10 |
| To | Invisible | ``` case Invisible ``` | OS X 10.11 |

Modified [CGTextDrawingMode.Stroke](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode/kcgtextstroke)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGTextStroke | ``` var kCGTextStroke: CGTextDrawingMode { get } ``` | OS X 10.10 |
| To | Stroke | ``` case Stroke ``` | OS X 10.11 |

Modified [CGTextDrawingMode.StrokeClip](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode/strokeclip)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGTextStrokeClip | ``` var kCGTextStrokeClip: CGTextDrawingMode { get } ``` | OS X 10.10 |
| To | StrokeClip | ``` case StrokeClip ``` | OS X 10.11 |

Modified [CGVector [struct]](https://developer.apple.com/documentation/coregraphics/cgvector)

|  | Declaration |
| --- | --- |
| From | ``` struct CGVector {     var dx: CGFloat     var dy: CGFloat     init()     init(dx dx: CGFloat, dy dy: CGFloat) } extension CGVector {     static var zeroVector: CGVector { get }     init(dx dx: Int, dy dy: Int)     init(dx dx: Double, dy dy: Double) } extension CGVector : Equatable { } extension CGVector : Equatable { } extension CGVector {     static var zeroVector: CGVector { get }     init(dx dx: Int, dy dy: Int)     init(dx dx: Double, dy dy: Double) } ``` |
| To | ``` struct CGVector {     var dx: CGFloat     var dy: CGFloat     init()     init(dx dx: CGFloat, dy dy: CGFloat) } extension CGVector {     static var zero: CGVector { get }     init(dx dx: Int, dy dy: Int)     init(dx dx: Double, dy dy: Double)     static var zeroVector: CGVector } extension CGVector : Equatable { } extension CGVector : Equatable { } extension CGVector {     static var zero: CGVector { get }     init(dx dx: Int, dy dy: Int)     init(dx dx: Double, dy dy: Double)     static var zeroVector: CGVector } ``` |

Modified %(_: CGFloat, _: CGFloat) -> CGFloat

|  | Declaration |
| --- | --- |
| From | ``` func %(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func %(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified \*(_: CGFloat, _: CGFloat) -> CGFloat

|  | Declaration |
| --- | --- |
| From | ``` func *(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func *(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified +(_: CGFloat) -> CGFloat

|  | Declaration | Operator Fixity |
| --- | --- | --- |
| From | ``` prefix func +(_ x: CGFloat) -> CGFloat ``` | -- |
| To | ``` @warn_unused_result prefix func +(_ x: CGFloat) -> CGFloat ``` | prefix |

Modified +(_: CGFloat, _: CGFloat) -> CGFloat

|  | Declaration |
| --- | --- |
| From | ``` func +(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func +(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified ++(_: CGFloat) -> CGFloat

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ++(_: CGFloat) -> CGFloat

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified -(_: CGFloat) -> CGFloat

|  | Declaration | Operator Fixity |
| --- | --- | --- |
| From | ``` prefix func -(_ x: CGFloat) -> CGFloat ``` | -- |
| To | ``` @warn_unused_result prefix func -(_ x: CGFloat) -> CGFloat ``` | prefix |

Modified -(_: CGFloat, _: CGFloat) -> CGFloat

|  | Declaration |
| --- | --- |
| From | ``` func -(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func -(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified --(_: CGFloat) -> CGFloat

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified --(_: CGFloat) -> CGFloat

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified /(_: CGFloat, _: CGFloat) -> CGFloat

|  | Declaration |
| --- | --- |
| From | ``` func /(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func /(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified <(_: CGFloat, _: CGFloat) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func <(_ lhs: CGFloat, _ rhs: CGFloat) -> Bool ``` |
| To | ``` @warn_unused_result func <(_ lhs: CGFloat, _ rhs: CGFloat) -> Bool ``` |

Modified ==(_: CGPoint, _: CGPoint) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ==(_ lhs: CGPoint, _ rhs: CGPoint) -> Bool ``` |
| To | ``` @warn_unused_result func ==(_ lhs: CGPoint, _ rhs: CGPoint) -> Bool ``` |

Modified ==(_: CGFloat, _: CGFloat) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ==(_ lhs: CGFloat, _ rhs: CGFloat) -> Bool ``` |
| To | ``` @warn_unused_result func ==(_ lhs: CGFloat, _ rhs: CGFloat) -> Bool ``` |

Modified ==(_: CGVector, _: CGVector) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ==(_ lhs: CGVector, _ rhs: CGVector) -> Bool ``` |
| To | ``` @warn_unused_result func ==(_ lhs: CGVector, _ rhs: CGVector) -> Bool ``` |

Modified ==(_: CGRect, _: CGRect) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ==(_ lhs: CGRect, _ rhs: CGRect) -> Bool ``` |
| To | ``` @warn_unused_result func ==(_ lhs: CGRect, _ rhs: CGRect) -> Bool ``` |

Modified ==(_: CGSize, _: CGSize) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ==(_ lhs: CGSize, _ rhs: CGSize) -> Bool ``` |
| To | ``` @warn_unused_result func ==(_ lhs: CGSize, _ rhs: CGSize) -> Bool ``` |

Modified [acos(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456465-acos)

|  | Declaration |
| --- | --- |
| From | ``` func acos(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func acos(_ x: CGFloat) -> CGFloat ``` |

Modified [acosh(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455200-acosh)

|  | Declaration |
| --- | --- |
| From | ``` func acosh(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func acosh(_ x: CGFloat) -> CGFloat ``` |

Modified [asin(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454580-asin)

|  | Declaration |
| --- | --- |
| From | ``` func asin(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func asin(_ x: CGFloat) -> CGFloat ``` |

Modified [asinh(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456449-asinh)

|  | Declaration |
| --- | --- |
| From | ``` func asinh(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func asinh(_ x: CGFloat) -> CGFloat ``` |

Modified [atan(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454322-atan)

|  | Declaration |
| --- | --- |
| From | ``` func atan(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func atan(_ x: CGFloat) -> CGFloat ``` |

Modified [atan2(_: CGFloat, _: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455332-atan2)

|  | Declaration |
| --- | --- |
| From | ``` func atan2(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func atan2(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified [atanh(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454527-atanh)

|  | Declaration |
| --- | --- |
| From | ``` func atanh(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func atanh(_ x: CGFloat) -> CGFloat ``` |

Modified [cbrt(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455432-cbrt)

|  | Declaration |
| --- | --- |
| From | ``` func cbrt(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func cbrt(_ x: CGFloat) -> CGFloat ``` |

Modified ceil(_: CGFloat) -> CGFloat

|  | Declaration |
| --- | --- |
| From | ``` func ceil(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func ceil(_ x: CGFloat) -> CGFloat ``` |

Modified [CGBitmapContextCreate(_: UnsafeMutablePointer<Void>, _: Int, _: Int, _: Int, _: Int, _: CGColorSpace?, _: UInt32) -> CGContext?](https://developer.apple.com/documentation/coregraphics/cgcontext/1455939-init)

|  | Declaration |
| --- | --- |
| From | ``` func CGBitmapContextCreate(_ data: UnsafeMutablePointer<Void>, _ width: Int, _ height: Int, _ bitsPerComponent: Int, _ bytesPerRow: Int, _ space: CGColorSpace!, _ bitmapInfo: CGBitmapInfo) -> CGContext! ``` |
| To | ``` func CGBitmapContextCreate(_ data: UnsafeMutablePointer<Void>, _ width: Int, _ height: Int, _ bitsPerComponent: Int, _ bytesPerRow: Int, _ space: CGColorSpace?, _ bitmapInfo: UInt32) -> CGContext? ``` |

Modified [CGBitmapContextCreateImage(_: CGContext?) -> CGImage?](https://developer.apple.com/documentation/coregraphics/1454225-cgbitmapcontextcreateimage)

|  | Declaration |
| --- | --- |
| From | ``` func CGBitmapContextCreateImage(_ context: CGContext!) -> CGImage! ``` |
| To | ``` func CGBitmapContextCreateImage(_ context: CGContext?) -> CGImage? ``` |

Modified [CGBitmapContextCreateWithData(_: UnsafeMutablePointer<Void>, _: Int, _: Int, _: Int, _: Int, _: CGColorSpace?, _: UInt32, _: CGBitmapContextReleaseDataCallback?, _: UnsafeMutablePointer<Void>) -> CGContext?](https://developer.apple.com/documentation/coregraphics/1454984-cgbitmapcontextcreatewithdata)

|  | Declaration |
| --- | --- |
| From | ``` func CGBitmapContextCreateWithData(_ data: UnsafeMutablePointer<Void>, _ width: Int, _ height: Int, _ bitsPerComponent: Int, _ bytesPerRow: Int, _ space: CGColorSpace!, _ bitmapInfo: CGBitmapInfo, _ releaseCallback: CGBitmapContextReleaseDataCallback, _ releaseInfo: UnsafeMutablePointer<Void>) -> CGContext! ``` |
| To | ``` func CGBitmapContextCreateWithData(_ data: UnsafeMutablePointer<Void>, _ width: Int, _ height: Int, _ bitsPerComponent: Int, _ bytesPerRow: Int, _ space: CGColorSpace?, _ bitmapInfo: UInt32, _ releaseCallback: CGBitmapContextReleaseDataCallback?, _ releaseInfo: UnsafeMutablePointer<Void>) -> CGContext? ``` |

Modified [CGBitmapContextGetAlphaInfo(_: CGContext?) -> CGImageAlphaInfo](https://developer.apple.com/documentation/coregraphics/cgcontext/1454960-alphainfo)

|  | Declaration |
| --- | --- |
| From | ``` func CGBitmapContextGetAlphaInfo(_ context: CGContext!) -> CGImageAlphaInfo ``` |
| To | ``` func CGBitmapContextGetAlphaInfo(_ context: CGContext?) -> CGImageAlphaInfo ``` |

Modified [CGBitmapContextGetBitmapInfo(_: CGContext?) -> CGBitmapInfo](https://developer.apple.com/documentation/coregraphics/cgcontext/1455839-bitmapinfo)

|  | Declaration |
| --- | --- |
| From | ``` func CGBitmapContextGetBitmapInfo(_ context: CGContext!) -> CGBitmapInfo ``` |
| To | ``` func CGBitmapContextGetBitmapInfo(_ context: CGContext?) -> CGBitmapInfo ``` |

Modified [CGBitmapContextGetBitsPerComponent(_: CGContext?) -> Int](https://developer.apple.com/documentation/coregraphics/cgcontext/1455383-bitspercomponent)

|  | Declaration |
| --- | --- |
| From | ``` func CGBitmapContextGetBitsPerComponent(_ context: CGContext!) -> Int ``` |
| To | ``` func CGBitmapContextGetBitsPerComponent(_ context: CGContext?) -> Int ``` |

Modified [CGBitmapContextGetBitsPerPixel(_: CGContext?) -> Int](https://developer.apple.com/documentation/coregraphics/cgcontext/1455946-bitsperpixel)

|  | Declaration |
| --- | --- |
| From | ``` func CGBitmapContextGetBitsPerPixel(_ context: CGContext!) -> Int ``` |
| To | ``` func CGBitmapContextGetBitsPerPixel(_ context: CGContext?) -> Int ``` |

Modified [CGBitmapContextGetBytesPerRow(_: CGContext?) -> Int](https://developer.apple.com/documentation/coregraphics/1456129-cgbitmapcontextgetbytesperrow)

|  | Declaration |
| --- | --- |
| From | ``` func CGBitmapContextGetBytesPerRow(_ context: CGContext!) -> Int ``` |
| To | ``` func CGBitmapContextGetBytesPerRow(_ context: CGContext?) -> Int ``` |

Modified [CGBitmapContextGetColorSpace(_: CGContext?) -> CGColorSpace?](https://developer.apple.com/documentation/coregraphics/cgcontext/1454058-colorspace)

|  | Declaration |
| --- | --- |
| From | ``` func CGBitmapContextGetColorSpace(_ context: CGContext!) -> CGColorSpace! ``` |
| To | ``` func CGBitmapContextGetColorSpace(_ context: CGContext?) -> CGColorSpace? ``` |

Modified [CGBitmapContextGetData(_: CGContext?) -> UnsafeMutablePointer<Void>](https://developer.apple.com/documentation/coregraphics/1455517-cgbitmapcontextgetdata)

|  | Declaration |
| --- | --- |
| From | ``` func CGBitmapContextGetData(_ context: CGContext!) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func CGBitmapContextGetData(_ context: CGContext?) -> UnsafeMutablePointer<Void> ``` |

Modified [CGBitmapContextGetHeight(_: CGContext?) -> Int](https://developer.apple.com/documentation/coregraphics/1454681-cgbitmapcontextgetheight)

|  | Declaration |
| --- | --- |
| From | ``` func CGBitmapContextGetHeight(_ context: CGContext!) -> Int ``` |
| To | ``` func CGBitmapContextGetHeight(_ context: CGContext?) -> Int ``` |

Modified [CGBitmapContextGetWidth(_: CGContext?) -> Int](https://developer.apple.com/documentation/coregraphics/1455607-cgbitmapcontextgetwidth)

|  | Declaration |
| --- | --- |
| From | ``` func CGBitmapContextGetWidth(_ context: CGContext!) -> Int ``` |
| To | ``` func CGBitmapContextGetWidth(_ context: CGContext?) -> Int ``` |

Modified [CGBitmapContextReleaseDataCallback](https://developer.apple.com/documentation/coregraphics/cgbitmapcontextreleasedatacallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGBitmapContextReleaseDataCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CGBitmapContextReleaseDataCallback = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CGColorCreate(_: CGColorSpace?, _: UnsafePointer<CGFloat>) -> CGColor?](https://developer.apple.com/documentation/coregraphics/cgcolor/1455927-init)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorCreate(_ space: CGColorSpace!, _ components: UnsafePointer<CGFloat>) -> CGColor! ``` |
| To | ``` func CGColorCreate(_ space: CGColorSpace?, _ components: UnsafePointer<CGFloat>) -> CGColor? ``` |

Modified [CGColorCreateCopy(_: CGColor?) -> CGColor?](https://developer.apple.com/documentation/coregraphics/1456134-cgcolorcreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorCreateCopy(_ color: CGColor!) -> CGColor! ``` |
| To | ``` func CGColorCreateCopy(_ color: CGColor?) -> CGColor? ``` |

Modified [CGColorCreateCopyWithAlpha(_: CGColor?, _: CGFloat) -> CGColor?](https://developer.apple.com/documentation/coregraphics/cgcolor/1455986-copy)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorCreateCopyWithAlpha(_ color: CGColor!, _ alpha: CGFloat) -> CGColor! ``` |
| To | ``` func CGColorCreateCopyWithAlpha(_ color: CGColor?, _ alpha: CGFloat) -> CGColor? ``` |

Modified [CGColorCreateGenericCMYK(_: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat) -> CGColor](https://developer.apple.com/documentation/coregraphics/1454222-cgcolorcreategenericcmyk)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorCreateGenericCMYK(_ cyan: CGFloat, _ magenta: CGFloat, _ yellow: CGFloat, _ black: CGFloat, _ alpha: CGFloat) -> CGColor! ``` |
| To | ``` func CGColorCreateGenericCMYK(_ cyan: CGFloat, _ magenta: CGFloat, _ yellow: CGFloat, _ black: CGFloat, _ alpha: CGFloat) -> CGColor ``` |

Modified [CGColorCreateGenericGray(_: CGFloat, _: CGFloat) -> CGColor](https://developer.apple.com/documentation/coregraphics/1456453-cgcolorcreategenericgray)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorCreateGenericGray(_ gray: CGFloat, _ alpha: CGFloat) -> CGColor! ``` |
| To | ``` func CGColorCreateGenericGray(_ gray: CGFloat, _ alpha: CGFloat) -> CGColor ``` |

Modified [CGColorCreateGenericRGB(_: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat) -> CGColor](https://developer.apple.com/documentation/coregraphics/cgcolor/1455631-init)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorCreateGenericRGB(_ red: CGFloat, _ green: CGFloat, _ blue: CGFloat, _ alpha: CGFloat) -> CGColor! ``` |
| To | ``` func CGColorCreateGenericRGB(_ red: CGFloat, _ green: CGFloat, _ blue: CGFloat, _ alpha: CGFloat) -> CGColor ``` |

Modified [CGColorCreateWithPattern(_: CGColorSpace?, _: CGPattern?, _: UnsafePointer<CGFloat>) -> CGColor?](https://developer.apple.com/documentation/coregraphics/1455687-cgcolorcreatewithpattern)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorCreateWithPattern(_ space: CGColorSpace!, _ pattern: CGPattern!, _ components: UnsafePointer<CGFloat>) -> CGColor! ``` |
| To | ``` func CGColorCreateWithPattern(_ space: CGColorSpace?, _ pattern: CGPattern?, _ components: UnsafePointer<CGFloat>) -> CGColor? ``` |

Modified [CGColorEqualToColor(_: CGColor?, _: CGColor?) -> Bool](https://developer.apple.com/documentation/coregraphics/1455217-cgcolorequaltocolor)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorEqualToColor(_ color1: CGColor!, _ color2: CGColor!) -> Bool ``` |
| To | ``` func CGColorEqualToColor(_ color1: CGColor?, _ color2: CGColor?) -> Bool ``` |

Modified [CGColorGetAlpha(_: CGColor?) -> CGFloat](https://developer.apple.com/documentation/coregraphics/cgcolor/1456637-alpha)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorGetAlpha(_ color: CGColor!) -> CGFloat ``` |
| To | ``` func CGColorGetAlpha(_ color: CGColor?) -> CGFloat ``` |

Modified [CGColorGetColorSpace(_: CGColor?) -> CGColorSpace?](https://developer.apple.com/documentation/coregraphics/cgcolor/1455744-colorspace)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorGetColorSpace(_ color: CGColor!) -> CGColorSpace! ``` |
| To | ``` func CGColorGetColorSpace(_ color: CGColor?) -> CGColorSpace? ``` |

Modified [CGColorGetComponents(_: CGColor?) -> UnsafePointer<CGFloat>](https://developer.apple.com/documentation/coregraphics/1455930-cgcolorgetcomponents)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorGetComponents(_ color: CGColor!) -> UnsafePointer<CGFloat> ``` |
| To | ``` func CGColorGetComponents(_ color: CGColor?) -> UnsafePointer<CGFloat> ``` |

Modified [CGColorGetConstantColor(_: CFString?) -> CGColor?](https://developer.apple.com/documentation/coregraphics/1454283-cgcolorgetconstantcolor)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorGetConstantColor(_ colorName: CFString!) -> CGColor! ``` |
| To | ``` func CGColorGetConstantColor(_ colorName: CFString?) -> CGColor? ``` |

Modified [CGColorGetNumberOfComponents(_: CGColor?) -> Int](https://developer.apple.com/documentation/coregraphics/1454130-cgcolorgetnumberofcomponents)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorGetNumberOfComponents(_ color: CGColor!) -> Int ``` |
| To | ``` func CGColorGetNumberOfComponents(_ color: CGColor?) -> Int ``` |

Modified [CGColorGetPattern(_: CGColor?) -> CGPattern?](https://developer.apple.com/documentation/coregraphics/cgcolor/1455937-pattern)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorGetPattern(_ color: CGColor!) -> CGPattern! ``` |
| To | ``` func CGColorGetPattern(_ color: CGColor?) -> CGPattern? ``` |

Modified [CGColorSpaceCopyICCProfile(_: CGColorSpace?) -> CFData?](https://developer.apple.com/documentation/coregraphics/1408889-cgcolorspacecopyiccprofile)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceCopyICCProfile(_ space: CGColorSpace!) -> CFData! ``` |
| To | ``` func CGColorSpaceCopyICCProfile(_ space: CGColorSpace?) -> CFData? ``` |

Modified [CGColorSpaceCopyName(_: CGColorSpace?) -> CFString?](https://developer.apple.com/documentation/coregraphics/1408903-cgcolorspacecopyname)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceCopyName(_ space: CGColorSpace!) -> CFString! ``` |
| To | ``` func CGColorSpaceCopyName(_ space: CGColorSpace?) -> CFString? ``` |

Modified [CGColorSpaceCreateCalibratedGray(_: UnsafePointer<CGFloat>, _: UnsafePointer<CGFloat>, _: CGFloat) -> CGColorSpace?](https://developer.apple.com/documentation/coregraphics/1408887-cgcolorspacecreatecalibratedgray)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceCreateCalibratedGray(_ whitePoint: UnsafePointer<CGFloat>, _ blackPoint: UnsafePointer<CGFloat>, _ gamma: CGFloat) -> CGColorSpace! ``` |
| To | ``` func CGColorSpaceCreateCalibratedGray(_ whitePoint: UnsafePointer<CGFloat>, _ blackPoint: UnsafePointer<CGFloat>, _ gamma: CGFloat) -> CGColorSpace? ``` |

Modified [CGColorSpaceCreateCalibratedRGB(_: UnsafePointer<CGFloat>, _: UnsafePointer<CGFloat>, _: UnsafePointer<CGFloat>, _: UnsafePointer<CGFloat>) -> CGColorSpace?](https://developer.apple.com/documentation/coregraphics/1408861-cgcolorspacecreatecalibratedrgb)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceCreateCalibratedRGB(_ whitePoint: UnsafePointer<CGFloat>, _ blackPoint: UnsafePointer<CGFloat>, _ gamma: UnsafePointer<CGFloat>, _ matrix: UnsafePointer<CGFloat>) -> CGColorSpace! ``` |
| To | ``` func CGColorSpaceCreateCalibratedRGB(_ whitePoint: UnsafePointer<CGFloat>, _ blackPoint: UnsafePointer<CGFloat>, _ gamma: UnsafePointer<CGFloat>, _ matrix: UnsafePointer<CGFloat>) -> CGColorSpace? ``` |

Modified [CGColorSpaceCreateDeviceCMYK() -> CGColorSpace?](https://developer.apple.com/documentation/coregraphics/1408897-cgcolorspacecreatedevicecmyk)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceCreateDeviceCMYK() -> CGColorSpace! ``` |
| To | ``` func CGColorSpaceCreateDeviceCMYK() -> CGColorSpace? ``` |

Modified [CGColorSpaceCreateDeviceGray() -> CGColorSpace?](https://developer.apple.com/documentation/coregraphics/1408908-cgcolorspacecreatedevicegray)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceCreateDeviceGray() -> CGColorSpace! ``` |
| To | ``` func CGColorSpaceCreateDeviceGray() -> CGColorSpace? ``` |

Modified [CGColorSpaceCreateDeviceRGB() -> CGColorSpace?](https://developer.apple.com/documentation/coregraphics/1408837-cgcolorspacecreatedevicergb)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceCreateDeviceRGB() -> CGColorSpace! ``` |
| To | ``` func CGColorSpaceCreateDeviceRGB() -> CGColorSpace? ``` |

Modified [CGColorSpaceCreateICCBased(_: Int, _: UnsafePointer<CGFloat>, _: CGDataProvider?, _: CGColorSpace?) -> CGColorSpace?](https://developer.apple.com/documentation/coregraphics/1408881-cgcolorspacecreateiccbased)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceCreateICCBased(_ nComponents: Int, _ range: UnsafePointer<CGFloat>, _ profile: CGDataProvider!, _ alternate: CGColorSpace!) -> CGColorSpace! ``` |
| To | ``` func CGColorSpaceCreateICCBased(_ nComponents: Int, _ range: UnsafePointer<CGFloat>, _ profile: CGDataProvider?, _ alternate: CGColorSpace?) -> CGColorSpace? ``` |

Modified [CGColorSpaceCreateIndexed(_: CGColorSpace?, _: Int, _: UnsafePointer<UInt8>) -> CGColorSpace?](https://developer.apple.com/documentation/coregraphics/1408899-cgcolorspacecreateindexed)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceCreateIndexed(_ baseSpace: CGColorSpace!, _ lastIndex: Int, _ colorTable: UnsafePointer<UInt8>) -> CGColorSpace! ``` |
| To | ``` func CGColorSpaceCreateIndexed(_ baseSpace: CGColorSpace?, _ lastIndex: Int, _ colorTable: UnsafePointer<UInt8>) -> CGColorSpace? ``` |

Modified [CGColorSpaceCreateLab(_: UnsafePointer<CGFloat>, _: UnsafePointer<CGFloat>, _: UnsafePointer<CGFloat>) -> CGColorSpace?](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408879-init)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceCreateLab(_ whitePoint: UnsafePointer<CGFloat>, _ blackPoint: UnsafePointer<CGFloat>, _ range: UnsafePointer<CGFloat>) -> CGColorSpace! ``` |
| To | ``` func CGColorSpaceCreateLab(_ whitePoint: UnsafePointer<CGFloat>, _ blackPoint: UnsafePointer<CGFloat>, _ range: UnsafePointer<CGFloat>) -> CGColorSpace? ``` |

Modified [CGColorSpaceCreatePattern(_: CGColorSpace?) -> CGColorSpace?](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408869-init)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceCreatePattern(_ baseSpace: CGColorSpace!) -> CGColorSpace! ``` |
| To | ``` func CGColorSpaceCreatePattern(_ baseSpace: CGColorSpace?) -> CGColorSpace? ``` |

Modified [CGColorSpaceCreateWithICCProfile(_: CFData?) -> CGColorSpace?](https://developer.apple.com/documentation/coregraphics/1408895-cgcolorspacecreatewithiccprofile)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceCreateWithICCProfile(_ data: CFData!) -> CGColorSpace! ``` |
| To | ``` func CGColorSpaceCreateWithICCProfile(_ data: CFData?) -> CGColorSpace? ``` |

Modified [CGColorSpaceCreateWithName(_: CFString?) -> CGColorSpace?](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408921-init)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceCreateWithName(_ name: CFString!) -> CGColorSpace! ``` |
| To | ``` func CGColorSpaceCreateWithName(_ name: CFString?) -> CGColorSpace? ``` |

Modified [CGColorSpaceCreateWithPlatformColorSpace(_: UnsafePointer<Void>) -> CGColorSpace?](https://developer.apple.com/documentation/coregraphics/1408850-cgcolorspacecreatewithplatformco)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceCreateWithPlatformColorSpace(_ ref: UnsafePointer<Void>) -> CGColorSpace! ``` |
| To | ``` func CGColorSpaceCreateWithPlatformColorSpace(_ ref: UnsafePointer<Void>) -> CGColorSpace? ``` |

Modified [CGColorSpaceGetBaseColorSpace(_: CGColorSpace?) -> CGColorSpace?](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408839-basecolorspace)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceGetBaseColorSpace(_ space: CGColorSpace!) -> CGColorSpace! ``` |
| To | ``` func CGColorSpaceGetBaseColorSpace(_ space: CGColorSpace?) -> CGColorSpace? ``` |

Modified [CGColorSpaceGetColorTable(_: CGColorSpace?, _: UnsafeMutablePointer<UInt8>)](https://developer.apple.com/documentation/coregraphics/1408853-cgcolorspacegetcolortable)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceGetColorTable(_ space: CGColorSpace!, _ table: UnsafeMutablePointer<UInt8>) ``` |
| To | ``` func CGColorSpaceGetColorTable(_ space: CGColorSpace?, _ table: UnsafeMutablePointer<UInt8>) ``` |

Modified [CGColorSpaceGetColorTableCount(_: CGColorSpace?) -> Int](https://developer.apple.com/documentation/coregraphics/1408883-cgcolorspacegetcolortablecount)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceGetColorTableCount(_ space: CGColorSpace!) -> Int ``` |
| To | ``` func CGColorSpaceGetColorTableCount(_ space: CGColorSpace?) -> Int ``` |

Modified [CGColorSpaceGetModel(_: CGColorSpace?) -> CGColorSpaceModel](https://developer.apple.com/documentation/coregraphics/1408854-cgcolorspacegetmodel)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceGetModel(_ space: CGColorSpace!) -> CGColorSpaceModel ``` |
| To | ``` func CGColorSpaceGetModel(_ space: CGColorSpace?) -> CGColorSpaceModel ``` |

Modified [CGColorSpaceGetNumberOfComponents(_: CGColorSpace?) -> Int](https://developer.apple.com/documentation/coregraphics/1408848-cgcolorspacegetnumberofcomponent)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceGetNumberOfComponents(_ space: CGColorSpace!) -> Int ``` |
| To | ``` func CGColorSpaceGetNumberOfComponents(_ space: CGColorSpace?) -> Int ``` |

Modified [CGConfigureDisplayWithDisplayMode(_: CGDisplayConfigRef, _: CGDirectDisplayID, _: CGDisplayMode?, _: CFDictionary?) -> CGError](https://developer.apple.com/documentation/coregraphics/1454273-cgconfiguredisplaywithdisplaymod)

|  | Declaration |
| --- | --- |
| From | ``` func CGConfigureDisplayWithDisplayMode(_ config: CGDisplayConfigRef, _ display: CGDirectDisplayID, _ mode: CGDisplayMode!, _ options: CFDictionary!) -> CGError ``` |
| To | ``` func CGConfigureDisplayWithDisplayMode(_ config: CGDisplayConfigRef, _ display: CGDirectDisplayID, _ mode: CGDisplayMode?, _ options: CFDictionary?) -> CGError ``` |

Modified [CGContextAddArc(_: CGContext?, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: Int32)](https://developer.apple.com/documentation/coregraphics/1455756-cgcontextaddarc)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextAddArc(_ c: CGContext!, _ x: CGFloat, _ y: CGFloat, _ radius: CGFloat, _ startAngle: CGFloat, _ endAngle: CGFloat, _ clockwise: Int32) ``` |
| To | ``` func CGContextAddArc(_ c: CGContext?, _ x: CGFloat, _ y: CGFloat, _ radius: CGFloat, _ startAngle: CGFloat, _ endAngle: CGFloat, _ clockwise: Int32) ``` |

Modified [CGContextAddArcToPoint(_: CGContext?, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1456238-cgcontextaddarctopoint)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextAddArcToPoint(_ c: CGContext!, _ x1: CGFloat, _ y1: CGFloat, _ x2: CGFloat, _ y2: CGFloat, _ radius: CGFloat) ``` |
| To | ``` func CGContextAddArcToPoint(_ c: CGContext?, _ x1: CGFloat, _ y1: CGFloat, _ x2: CGFloat, _ y2: CGFloat, _ radius: CGFloat) ``` |

Modified [CGContextAddCurveToPoint(_: CGContext?, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1456393-cgcontextaddcurvetopoint)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextAddCurveToPoint(_ c: CGContext!, _ cp1x: CGFloat, _ cp1y: CGFloat, _ cp2x: CGFloat, _ cp2y: CGFloat, _ x: CGFloat, _ y: CGFloat) ``` |
| To | ``` func CGContextAddCurveToPoint(_ c: CGContext?, _ cp1x: CGFloat, _ cp1y: CGFloat, _ cp2x: CGFloat, _ cp2y: CGFloat, _ x: CGFloat, _ y: CGFloat) ``` |

Modified [CGContextAddEllipseInRect(_: CGContext?, _: CGRect)](https://developer.apple.com/documentation/coregraphics/1456420-cgcontextaddellipseinrect)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextAddEllipseInRect(_ context: CGContext!, _ rect: CGRect) ``` |
| To | ``` func CGContextAddEllipseInRect(_ c: CGContext?, _ rect: CGRect) ``` |

Modified [CGContextAddLines(_: CGContext?, _: UnsafePointer<CGPoint>, _: Int)](https://developer.apple.com/documentation/coregraphics/1455461-cgcontextaddlines)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextAddLines(_ c: CGContext!, _ points: UnsafePointer<CGPoint>, _ count: Int) ``` |
| To | ``` func CGContextAddLines(_ c: CGContext?, _ points: UnsafePointer<CGPoint>, _ count: Int) ``` |

Modified [CGContextAddLineToPoint(_: CGContext?, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1455213-cgcontextaddlinetopoint)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextAddLineToPoint(_ c: CGContext!, _ x: CGFloat, _ y: CGFloat) ``` |
| To | ``` func CGContextAddLineToPoint(_ c: CGContext?, _ x: CGFloat, _ y: CGFloat) ``` |

Modified [CGContextAddPath(_: CGContext?, _: CGPath?)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456628-addpath)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextAddPath(_ context: CGContext!, _ path: CGPath!) ``` |
| To | ``` func CGContextAddPath(_ c: CGContext?, _ path: CGPath?) ``` |

Modified [CGContextAddQuadCurveToPoint(_: CGContext?, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1454268-cgcontextaddquadcurvetopoint)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextAddQuadCurveToPoint(_ c: CGContext!, _ cpx: CGFloat, _ cpy: CGFloat, _ x: CGFloat, _ y: CGFloat) ``` |
| To | ``` func CGContextAddQuadCurveToPoint(_ c: CGContext?, _ cpx: CGFloat, _ cpy: CGFloat, _ x: CGFloat, _ y: CGFloat) ``` |

Modified [CGContextAddRect(_: CGContext?, _: CGRect)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456617-addrect)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextAddRect(_ c: CGContext!, _ rect: CGRect) ``` |
| To | ``` func CGContextAddRect(_ c: CGContext?, _ rect: CGRect) ``` |

Modified [CGContextAddRects(_: CGContext?, _: UnsafePointer<CGRect>, _: Int)](https://developer.apple.com/documentation/coregraphics/1454734-cgcontextaddrects)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextAddRects(_ c: CGContext!, _ rects: UnsafePointer<CGRect>, _ count: Int) ``` |
| To | ``` func CGContextAddRects(_ c: CGContext?, _ rects: UnsafePointer<CGRect>, _ count: Int) ``` |

Modified [CGContextBeginPage(_: CGContext?, _: UnsafePointer<CGRect>)](https://developer.apple.com/documentation/coregraphics/1454794-cgcontextbeginpage)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextBeginPage(_ c: CGContext!, _ mediaBox: UnsafePointer<CGRect>) ``` |
| To | ``` func CGContextBeginPage(_ c: CGContext?, _ mediaBox: UnsafePointer<CGRect>) ``` |

Modified [CGContextBeginPath(_: CGContext?)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456635-beginpath)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextBeginPath(_ c: CGContext!) ``` |
| To | ``` func CGContextBeginPath(_ c: CGContext?) ``` |

Modified [CGContextBeginTransparencyLayer(_: CGContext?, _: CFDictionary?)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456011-begintransparencylayer)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextBeginTransparencyLayer(_ context: CGContext!, _ auxiliaryInfo: CFDictionary!) ``` |
| To | ``` func CGContextBeginTransparencyLayer(_ c: CGContext?, _ auxiliaryInfo: CFDictionary?) ``` |

Modified [CGContextBeginTransparencyLayerWithRect(_: CGContext?, _: CGRect, _: CFDictionary?)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454368-begintransparencylayer)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextBeginTransparencyLayerWithRect(_ context: CGContext!, _ rect: CGRect, _ auxiliaryInfo: CFDictionary!) ``` |
| To | ``` func CGContextBeginTransparencyLayerWithRect(_ c: CGContext?, _ rect: CGRect, _ auxInfo: CFDictionary?) ``` |

Modified [CGContextClearRect(_: CGContext?, _: CGRect)](https://developer.apple.com/documentation/coregraphics/1456457-cgcontextclearrect)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextClearRect(_ c: CGContext!, _ rect: CGRect) ``` |
| To | ``` func CGContextClearRect(_ c: CGContext?, _ rect: CGRect) ``` |

Modified [CGContextClip(_: CGContext?)](https://developer.apple.com/documentation/coregraphics/1455262-cgcontextclip)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextClip(_ c: CGContext!) ``` |
| To | ``` func CGContextClip(_ c: CGContext?) ``` |

Modified [CGContextClipToMask(_: CGContext?, _: CGRect, _: CGImage?)](https://developer.apple.com/documentation/coregraphics/1456497-cgcontextcliptomask)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextClipToMask(_ c: CGContext!, _ rect: CGRect, _ mask: CGImage!) ``` |
| To | ``` func CGContextClipToMask(_ c: CGContext?, _ rect: CGRect, _ mask: CGImage?) ``` |

Modified [CGContextClipToRect(_: CGContext?, _: CGRect)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454716-clip)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextClipToRect(_ c: CGContext!, _ rect: CGRect) ``` |
| To | ``` func CGContextClipToRect(_ c: CGContext?, _ rect: CGRect) ``` |

Modified [CGContextClipToRects(_: CGContext?, _: UnsafePointer<CGRect>, _: Int)](https://developer.apple.com/documentation/coregraphics/1454626-cgcontextcliptorects)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextClipToRects(_ c: CGContext!, _ rects: UnsafePointer<CGRect>, _ count: Int) ``` |
| To | ``` func CGContextClipToRects(_ c: CGContext?, _ rects: UnsafePointer<CGRect>, _ count: Int) ``` |

Modified [CGContextClosePath(_: CGContext?)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454508-closepath)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextClosePath(_ c: CGContext!) ``` |
| To | ``` func CGContextClosePath(_ c: CGContext?) ``` |

Modified [CGContextConcatCTM(_: CGContext?, _: CGAffineTransform)](https://developer.apple.com/documentation/coregraphics/1454897-cgcontextconcatctm)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextConcatCTM(_ c: CGContext!, _ transform: CGAffineTransform) ``` |
| To | ``` func CGContextConcatCTM(_ c: CGContext?, _ transform: CGAffineTransform) ``` |

Modified [CGContextConvertPointToDeviceSpace(_: CGContext?, _: CGPoint) -> CGPoint](https://developer.apple.com/documentation/coregraphics/1455916-cgcontextconvertpointtodevicespa)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextConvertPointToDeviceSpace(_ context: CGContext!, _ point: CGPoint) -> CGPoint ``` |
| To | ``` func CGContextConvertPointToDeviceSpace(_ c: CGContext?, _ point: CGPoint) -> CGPoint ``` |

Modified [CGContextConvertPointToUserSpace(_: CGContext?, _: CGPoint) -> CGPoint](https://developer.apple.com/documentation/coregraphics/1456451-cgcontextconvertpointtouserspace)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextConvertPointToUserSpace(_ context: CGContext!, _ point: CGPoint) -> CGPoint ``` |
| To | ``` func CGContextConvertPointToUserSpace(_ c: CGContext?, _ point: CGPoint) -> CGPoint ``` |

Modified [CGContextConvertRectToDeviceSpace(_: CGContext?, _: CGRect) -> CGRect](https://developer.apple.com/documentation/coregraphics/1456017-cgcontextconvertrecttodevicespac)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextConvertRectToDeviceSpace(_ context: CGContext!, _ rect: CGRect) -> CGRect ``` |
| To | ``` func CGContextConvertRectToDeviceSpace(_ c: CGContext?, _ rect: CGRect) -> CGRect ``` |

Modified [CGContextConvertRectToUserSpace(_: CGContext?, _: CGRect) -> CGRect](https://developer.apple.com/documentation/coregraphics/1454165-cgcontextconvertrecttouserspace)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextConvertRectToUserSpace(_ context: CGContext!, _ rect: CGRect) -> CGRect ``` |
| To | ``` func CGContextConvertRectToUserSpace(_ c: CGContext?, _ rect: CGRect) -> CGRect ``` |

Modified [CGContextConvertSizeToDeviceSpace(_: CGContext?, _: CGSize) -> CGSize](https://developer.apple.com/documentation/coregraphics/1456619-cgcontextconvertsizetodevicespac)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextConvertSizeToDeviceSpace(_ context: CGContext!, _ size: CGSize) -> CGSize ``` |
| To | ``` func CGContextConvertSizeToDeviceSpace(_ c: CGContext?, _ size: CGSize) -> CGSize ``` |

Modified [CGContextConvertSizeToUserSpace(_: CGContext?, _: CGSize) -> CGSize](https://developer.apple.com/documentation/coregraphics/1456510-cgcontextconvertsizetouserspace)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextConvertSizeToUserSpace(_ context: CGContext!, _ size: CGSize) -> CGSize ``` |
| To | ``` func CGContextConvertSizeToUserSpace(_ c: CGContext?, _ size: CGSize) -> CGSize ``` |

Modified [CGContextCopyPath(_: CGContext?) -> CGPath?](https://developer.apple.com/documentation/coregraphics/cgcontext/1455397-path)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextCopyPath(_ context: CGContext!) -> CGPath! ``` |
| To | ``` func CGContextCopyPath(_ c: CGContext?) -> CGPath? ``` |

Modified [CGContextDrawImage(_: CGContext?, _: CGRect, _: CGImage?)](https://developer.apple.com/documentation/coregraphics/1454845-cgcontextdrawimage)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextDrawImage(_ c: CGContext!, _ rect: CGRect, _ image: CGImage!) ``` |
| To | ``` func CGContextDrawImage(_ c: CGContext?, _ rect: CGRect, _ image: CGImage?) ``` |

Modified [CGContextDrawLayerAtPoint(_: CGContext?, _: CGPoint, _: CGLayer?)](https://developer.apple.com/documentation/coregraphics/1450894-cgcontextdrawlayeratpoint)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextDrawLayerAtPoint(_ context: CGContext!, _ point: CGPoint, _ layer: CGLayer!) ``` |
| To | ``` func CGContextDrawLayerAtPoint(_ context: CGContext?, _ point: CGPoint, _ layer: CGLayer?) ``` |

Modified [CGContextDrawLayerInRect(_: CGContext?, _: CGRect, _: CGLayer?)](https://developer.apple.com/documentation/coregraphics/1450896-cgcontextdrawlayerinrect)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextDrawLayerInRect(_ context: CGContext!, _ rect: CGRect, _ layer: CGLayer!) ``` |
| To | ``` func CGContextDrawLayerInRect(_ context: CGContext?, _ rect: CGRect, _ layer: CGLayer?) ``` |

Modified [CGContextDrawLinearGradient(_: CGContext?, _: CGGradient?, _: CGPoint, _: CGPoint, _: CGGradientDrawingOptions)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454782-drawlineargradient)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextDrawLinearGradient(_ context: CGContext!, _ gradient: CGGradient!, _ startPoint: CGPoint, _ endPoint: CGPoint, _ options: CGGradientDrawingOptions) ``` |
| To | ``` func CGContextDrawLinearGradient(_ c: CGContext?, _ gradient: CGGradient?, _ startPoint: CGPoint, _ endPoint: CGPoint, _ options: CGGradientDrawingOptions) ``` |

Modified [CGContextDrawPath(_: CGContext?, _: CGPathDrawingMode)](https://developer.apple.com/documentation/coregraphics/1455195-cgcontextdrawpath)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextDrawPath(_ c: CGContext!, _ mode: CGPathDrawingMode) ``` |
| To | ``` func CGContextDrawPath(_ c: CGContext?, _ mode: CGPathDrawingMode) ``` |

Modified [CGContextDrawPDFPage(_: CGContext?, _: CGPDFPage?)](https://developer.apple.com/documentation/coregraphics/1456255-cgcontextdrawpdfpage)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextDrawPDFPage(_ c: CGContext!, _ page: CGPDFPage!) ``` |
| To | ``` func CGContextDrawPDFPage(_ c: CGContext?, _ page: CGPDFPage?) ``` |

Modified [CGContextDrawRadialGradient(_: CGContext?, _: CGGradient?, _: CGPoint, _: CGFloat, _: CGPoint, _: CGFloat, _: CGGradientDrawingOptions)](https://developer.apple.com/documentation/coregraphics/1455923-cgcontextdrawradialgradient)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextDrawRadialGradient(_ context: CGContext!, _ gradient: CGGradient!, _ startCenter: CGPoint, _ startRadius: CGFloat, _ endCenter: CGPoint, _ endRadius: CGFloat, _ options: CGGradientDrawingOptions) ``` |
| To | ``` func CGContextDrawRadialGradient(_ c: CGContext?, _ gradient: CGGradient?, _ startCenter: CGPoint, _ startRadius: CGFloat, _ endCenter: CGPoint, _ endRadius: CGFloat, _ options: CGGradientDrawingOptions) ``` |

Modified [CGContextDrawShading(_: CGContext?, _: CGShading?)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456643-drawshading)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextDrawShading(_ context: CGContext!, _ shading: CGShading!) ``` |
| To | ``` func CGContextDrawShading(_ c: CGContext?, _ shading: CGShading?) ``` |

Modified [CGContextDrawTiledImage(_: CGContext?, _: CGRect, _: CGImage?)](https://developer.apple.com/documentation/coregraphics/1456240-cgcontextdrawtiledimage)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextDrawTiledImage(_ c: CGContext!, _ rect: CGRect, _ image: CGImage!) ``` |
| To | ``` func CGContextDrawTiledImage(_ c: CGContext?, _ rect: CGRect, _ image: CGImage?) ``` |

Modified [CGContextEndPage(_: CGContext?)](https://developer.apple.com/documentation/coregraphics/cgcontext/1455027-endpage)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextEndPage(_ c: CGContext!) ``` |
| To | ``` func CGContextEndPage(_ c: CGContext?) ``` |

Modified [CGContextEndTransparencyLayer(_: CGContext?)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456554-endtransparencylayer)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextEndTransparencyLayer(_ context: CGContext!) ``` |
| To | ``` func CGContextEndTransparencyLayer(_ c: CGContext?) ``` |

Modified [CGContextEOClip(_: CGContext?)](https://developer.apple.com/documentation/coregraphics/1455944-cgcontexteoclip)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextEOClip(_ c: CGContext!) ``` |
| To | ``` func CGContextEOClip(_ c: CGContext?) ``` |

Modified [CGContextEOFillPath(_: CGContext?)](https://developer.apple.com/documentation/coregraphics/1454865-cgcontexteofillpath)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextEOFillPath(_ c: CGContext!) ``` |
| To | ``` func CGContextEOFillPath(_ c: CGContext?) ``` |

Modified [CGContextFillEllipseInRect(_: CGContext?, _: CGRect)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454371-fillellipse)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextFillEllipseInRect(_ context: CGContext!, _ rect: CGRect) ``` |
| To | ``` func CGContextFillEllipseInRect(_ c: CGContext?, _ rect: CGRect) ``` |

Modified [CGContextFillPath(_: CGContext?)](https://developer.apple.com/documentation/coregraphics/1456306-cgcontextfillpath)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextFillPath(_ c: CGContext!) ``` |
| To | ``` func CGContextFillPath(_ c: CGContext?) ``` |

Modified [CGContextFillRect(_: CGContext?, _: CGRect)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454700-fill)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextFillRect(_ c: CGContext!, _ rect: CGRect) ``` |
| To | ``` func CGContextFillRect(_ c: CGContext?, _ rect: CGRect) ``` |

Modified [CGContextFillRects(_: CGContext?, _: UnsafePointer<CGRect>, _: Int)](https://developer.apple.com/documentation/coregraphics/1454132-cgcontextfillrects)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextFillRects(_ c: CGContext!, _ rects: UnsafePointer<CGRect>, _ count: Int) ``` |
| To | ``` func CGContextFillRects(_ c: CGContext?, _ rects: UnsafePointer<CGRect>, _ count: Int) ``` |

Modified [CGContextFlush(_: CGContext?)](https://developer.apple.com/documentation/coregraphics/1454895-cgcontextflush)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextFlush(_ c: CGContext!) ``` |
| To | ``` func CGContextFlush(_ c: CGContext?) ``` |

Modified [CGContextGetClipBoundingBox(_: CGContext?) -> CGRect](https://developer.apple.com/documentation/coregraphics/1455387-cgcontextgetclipboundingbox)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextGetClipBoundingBox(_ c: CGContext!) -> CGRect ``` |
| To | ``` func CGContextGetClipBoundingBox(_ c: CGContext?) -> CGRect ``` |

Modified [CGContextGetCTM(_: CGContext?) -> CGAffineTransform](https://developer.apple.com/documentation/coregraphics/cgcontext/1454691-ctm)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextGetCTM(_ c: CGContext!) -> CGAffineTransform ``` |
| To | ``` func CGContextGetCTM(_ c: CGContext?) -> CGAffineTransform ``` |

Modified [CGContextGetInterpolationQuality(_: CGContext?) -> CGInterpolationQuality](https://developer.apple.com/documentation/coregraphics/cgcontext/1454940-interpolationquality)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextGetInterpolationQuality(_ context: CGContext!) -> CGInterpolationQuality ``` |
| To | ``` func CGContextGetInterpolationQuality(_ c: CGContext?) -> CGInterpolationQuality ``` |

Modified [CGContextGetPathBoundingBox(_: CGContext?) -> CGRect](https://developer.apple.com/documentation/coregraphics/cgcontext/1454577-boundingboxofpath)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextGetPathBoundingBox(_ context: CGContext!) -> CGRect ``` |
| To | ``` func CGContextGetPathBoundingBox(_ c: CGContext?) -> CGRect ``` |

Modified [CGContextGetPathCurrentPoint(_: CGContext?) -> CGPoint](https://developer.apple.com/documentation/coregraphics/cgcontext/1454788-currentpointofpath)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextGetPathCurrentPoint(_ context: CGContext!) -> CGPoint ``` |
| To | ``` func CGContextGetPathCurrentPoint(_ c: CGContext?) -> CGPoint ``` |

Modified [CGContextGetTextMatrix(_: CGContext?) -> CGAffineTransform](https://developer.apple.com/documentation/coregraphics/cgcontext/1456154-textmatrix)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextGetTextMatrix(_ c: CGContext!) -> CGAffineTransform ``` |
| To | ``` func CGContextGetTextMatrix(_ c: CGContext?) -> CGAffineTransform ``` |

Modified [CGContextGetTextPosition(_: CGContext?) -> CGPoint](https://developer.apple.com/documentation/coregraphics/1454687-cgcontextgettextposition)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextGetTextPosition(_ context: CGContext!) -> CGPoint ``` |
| To | ``` func CGContextGetTextPosition(_ c: CGContext?) -> CGPoint ``` |

Modified [CGContextGetUserSpaceToDeviceSpaceTransform(_: CGContext?) -> CGAffineTransform](https://developer.apple.com/documentation/coregraphics/1455677-cgcontextgetuserspacetodevicespa)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextGetUserSpaceToDeviceSpaceTransform(_ context: CGContext!) -> CGAffineTransform ``` |
| To | ``` func CGContextGetUserSpaceToDeviceSpaceTransform(_ c: CGContext?) -> CGAffineTransform ``` |

Modified [CGContextIsPathEmpty(_: CGContext?) -> Bool](https://developer.apple.com/documentation/coregraphics/1455772-cgcontextispathempty)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextIsPathEmpty(_ context: CGContext!) -> Bool ``` |
| To | ``` func CGContextIsPathEmpty(_ c: CGContext?) -> Bool ``` |

Modified [CGContextMoveToPoint(_: CGContext?, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1454738-cgcontextmovetopoint)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextMoveToPoint(_ c: CGContext!, _ x: CGFloat, _ y: CGFloat) ``` |
| To | ``` func CGContextMoveToPoint(_ c: CGContext?, _ x: CGFloat, _ y: CGFloat) ``` |

Modified [CGContextPathContainsPoint(_: CGContext?, _: CGPoint, _: CGPathDrawingMode) -> Bool](https://developer.apple.com/documentation/coregraphics/1454778-cgcontextpathcontainspoint)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextPathContainsPoint(_ context: CGContext!, _ point: CGPoint, _ mode: CGPathDrawingMode) -> Bool ``` |
| To | ``` func CGContextPathContainsPoint(_ c: CGContext?, _ point: CGPoint, _ mode: CGPathDrawingMode) -> Bool ``` |

Modified [CGContextReplacePathWithStrokedPath(_: CGContext?)](https://developer.apple.com/documentation/coregraphics/1454517-cgcontextreplacepathwithstrokedp)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextReplacePathWithStrokedPath(_ c: CGContext!) ``` |
| To | ``` func CGContextReplacePathWithStrokedPath(_ c: CGContext?) ``` |

Modified [CGContextRestoreGState(_: CGContext?)](https://developer.apple.com/documentation/coregraphics/1455391-cgcontextrestoregstate)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextRestoreGState(_ c: CGContext!) ``` |
| To | ``` func CGContextRestoreGState(_ c: CGContext?) ``` |

Modified [CGContextRotateCTM(_: CGContext?, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1456228-cgcontextrotatectm)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextRotateCTM(_ c: CGContext!, _ angle: CGFloat) ``` |
| To | ``` func CGContextRotateCTM(_ c: CGContext?, _ angle: CGFloat) ``` |

Modified [CGContextSaveGState(_: CGContext?)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456156-savegstate)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSaveGState(_ c: CGContext!) ``` |
| To | ``` func CGContextSaveGState(_ c: CGContext?) ``` |

Modified [CGContextScaleCTM(_: CGContext?, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454659-scaleby)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextScaleCTM(_ c: CGContext!, _ sx: CGFloat, _ sy: CGFloat) ``` |
| To | ``` func CGContextScaleCTM(_ c: CGContext?, _ sx: CGFloat, _ sy: CGFloat) ``` |

Modified [CGContextSetAllowsAntialiasing(_: CGContext?, _: Bool)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456310-setallowsantialiasing)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetAllowsAntialiasing(_ context: CGContext!, _ allowsAntialiasing: Bool) ``` |
| To | ``` func CGContextSetAllowsAntialiasing(_ c: CGContext?, _ allowsAntialiasing: Bool) ``` |

Modified [CGContextSetAllowsFontSmoothing(_: CGContext?, _: Bool)](https://developer.apple.com/documentation/coregraphics/1454767-cgcontextsetallowsfontsmoothing)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetAllowsFontSmoothing(_ context: CGContext!, _ allowsFontSmoothing: Bool) ``` |
| To | ``` func CGContextSetAllowsFontSmoothing(_ c: CGContext?, _ allowsFontSmoothing: Bool) ``` |

Modified [CGContextSetAllowsFontSubpixelPositioning(_: CGContext?, _: Bool)](https://developer.apple.com/documentation/coregraphics/1454942-cgcontextsetallowsfontsubpixelpo)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetAllowsFontSubpixelPositioning(_ context: CGContext!, _ allowsFontSubpixelPositioning: Bool) ``` |
| To | ``` func CGContextSetAllowsFontSubpixelPositioning(_ c: CGContext?, _ allowsFontSubpixelPositioning: Bool) ``` |

Modified [CGContextSetAllowsFontSubpixelQuantization(_: CGContext?, _: Bool)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456263-setallowsfontsubpixelquantizatio)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetAllowsFontSubpixelQuantization(_ context: CGContext!, _ allowsFontSubpixelQuantization: Bool) ``` |
| To | ``` func CGContextSetAllowsFontSubpixelQuantization(_ c: CGContext?, _ allowsFontSubpixelQuantization: Bool) ``` |

Modified [CGContextSetAlpha(_: CGContext?, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456404-setalpha)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetAlpha(_ c: CGContext!, _ alpha: CGFloat) ``` |
| To | ``` func CGContextSetAlpha(_ c: CGContext?, _ alpha: CGFloat) ``` |

Modified [CGContextSetBlendMode(_: CGContext?, _: CGBlendMode)](https://developer.apple.com/documentation/coregraphics/1455994-cgcontextsetblendmode)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetBlendMode(_ context: CGContext!, _ mode: CGBlendMode) ``` |
| To | ``` func CGContextSetBlendMode(_ c: CGContext?, _ mode: CGBlendMode) ``` |

Modified [CGContextSetCharacterSpacing(_: CGContext?, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1454786-cgcontextsetcharacterspacing)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetCharacterSpacing(_ context: CGContext!, _ spacing: CGFloat) ``` |
| To | ``` func CGContextSetCharacterSpacing(_ c: CGContext?, _ spacing: CGFloat) ``` |

Modified [CGContextSetCMYKFillColor(_: CGContext?, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454214-setfillcolor)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetCMYKFillColor(_ context: CGContext!, _ cyan: CGFloat, _ magenta: CGFloat, _ yellow: CGFloat, _ black: CGFloat, _ alpha: CGFloat) ``` |
| To | ``` func CGContextSetCMYKFillColor(_ c: CGContext?, _ cyan: CGFloat, _ magenta: CGFloat, _ yellow: CGFloat, _ black: CGFloat, _ alpha: CGFloat) ``` |

Modified [CGContextSetCMYKStrokeColor(_: CGContext?, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1455358-setstrokecolor)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetCMYKStrokeColor(_ context: CGContext!, _ cyan: CGFloat, _ magenta: CGFloat, _ yellow: CGFloat, _ black: CGFloat, _ alpha: CGFloat) ``` |
| To | ``` func CGContextSetCMYKStrokeColor(_ c: CGContext?, _ cyan: CGFloat, _ magenta: CGFloat, _ yellow: CGFloat, _ black: CGFloat, _ alpha: CGFloat) ``` |

Modified [CGContextSetFillColor(_: CGContext?, _: UnsafePointer<CGFloat>)](https://developer.apple.com/documentation/coregraphics/1455296-cgcontextsetfillcolor)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetFillColor(_ context: CGContext!, _ components: UnsafePointer<CGFloat>) ``` |
| To | ``` func CGContextSetFillColor(_ c: CGContext?, _ components: UnsafePointer<CGFloat>) ``` |

Modified [CGContextSetFillColorSpace(_: CGContext?, _: CGColorSpace?)](https://developer.apple.com/documentation/coregraphics/1455151-cgcontextsetfillcolorspace)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetFillColorSpace(_ context: CGContext!, _ space: CGColorSpace!) ``` |
| To | ``` func CGContextSetFillColorSpace(_ c: CGContext?, _ space: CGColorSpace?) ``` |

Modified [CGContextSetFillColorWithColor(_: CGContext?, _: CGColor?)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454079-setfillcolor)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetFillColorWithColor(_ c: CGContext!, _ color: CGColor!) ``` |
| To | ``` func CGContextSetFillColorWithColor(_ c: CGContext?, _ color: CGColor?) ``` |

Modified [CGContextSetFillPattern(_: CGContext?, _: CGPattern?, _: UnsafePointer<CGFloat>)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456334-setfillpattern)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetFillPattern(_ context: CGContext!, _ pattern: CGPattern!, _ components: UnsafePointer<CGFloat>) ``` |
| To | ``` func CGContextSetFillPattern(_ c: CGContext?, _ pattern: CGPattern?, _ components: UnsafePointer<CGFloat>) ``` |

Modified [CGContextSetFlatness(_: CGContext?, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1455798-setflatness)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetFlatness(_ c: CGContext!, _ flatness: CGFloat) ``` |
| To | ``` func CGContextSetFlatness(_ c: CGContext?, _ flatness: CGFloat) ``` |

Modified [CGContextSetFont(_: CGContext?, _: CGFont?)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454950-setfont)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetFont(_ c: CGContext!, _ font: CGFont!) ``` |
| To | ``` func CGContextSetFont(_ c: CGContext?, _ font: CGFont?) ``` |

Modified [CGContextSetFontSize(_: CGContext?, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456426-setfontsize)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetFontSize(_ c: CGContext!, _ size: CGFloat) ``` |
| To | ``` func CGContextSetFontSize(_ c: CGContext?, _ size: CGFloat) ``` |

Modified [CGContextSetGrayFillColor(_: CGContext?, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454255-setfillcolor)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetGrayFillColor(_ context: CGContext!, _ gray: CGFloat, _ alpha: CGFloat) ``` |
| To | ``` func CGContextSetGrayFillColor(_ c: CGContext?, _ gray: CGFloat, _ alpha: CGFloat) ``` |

Modified [CGContextSetGrayStrokeColor(_: CGContext?, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1455209-setstrokecolor)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetGrayStrokeColor(_ context: CGContext!, _ gray: CGFloat, _ alpha: CGFloat) ``` |
| To | ``` func CGContextSetGrayStrokeColor(_ c: CGContext?, _ gray: CGFloat, _ alpha: CGFloat) ``` |

Modified [CGContextSetInterpolationQuality(_: CGContext?, _: CGInterpolationQuality)](https://developer.apple.com/documentation/coregraphics/1455656-cgcontextsetinterpolationquality)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetInterpolationQuality(_ context: CGContext!, _ quality: CGInterpolationQuality) ``` |
| To | ``` func CGContextSetInterpolationQuality(_ c: CGContext?, _ quality: CGInterpolationQuality) ``` |

Modified [CGContextSetLineCap(_: CGContext?, _: CGLineCap)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454326-setlinecap)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetLineCap(_ c: CGContext!, _ cap: CGLineCap) ``` |
| To | ``` func CGContextSetLineCap(_ c: CGContext?, _ cap: CGLineCap) ``` |

Modified [CGContextSetLineDash(_: CGContext?, _: CGFloat, _: UnsafePointer<CGFloat>, _: Int)](https://developer.apple.com/documentation/coregraphics/1455911-cgcontextsetlinedash)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetLineDash(_ c: CGContext!, _ phase: CGFloat, _ lengths: UnsafePointer<CGFloat>, _ count: Int) ``` |
| To | ``` func CGContextSetLineDash(_ c: CGContext?, _ phase: CGFloat, _ lengths: UnsafePointer<CGFloat>, _ count: Int) ``` |

Modified [CGContextSetLineJoin(_: CGContext?, _: CGLineJoin)](https://developer.apple.com/documentation/coregraphics/1455973-cgcontextsetlinejoin)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetLineJoin(_ c: CGContext!, _ join: CGLineJoin) ``` |
| To | ``` func CGContextSetLineJoin(_ c: CGContext?, _ join: CGLineJoin) ``` |

Modified [CGContextSetLineWidth(_: CGContext?, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1455270-cgcontextsetlinewidth)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetLineWidth(_ c: CGContext!, _ width: CGFloat) ``` |
| To | ``` func CGContextSetLineWidth(_ c: CGContext?, _ width: CGFloat) ``` |

Modified [CGContextSetMiterLimit(_: CGContext?, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456499-setmiterlimit)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetMiterLimit(_ c: CGContext!, _ limit: CGFloat) ``` |
| To | ``` func CGContextSetMiterLimit(_ c: CGContext?, _ limit: CGFloat) ``` |

Modified [CGContextSetPatternPhase(_: CGContext?, _: CGSize)](https://developer.apple.com/documentation/coregraphics/1455334-cgcontextsetpatternphase)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetPatternPhase(_ context: CGContext!, _ phase: CGSize) ``` |
| To | ``` func CGContextSetPatternPhase(_ c: CGContext?, _ phase: CGSize) ``` |

Modified [CGContextSetRenderingIntent(_: CGContext?, _: CGColorRenderingIntent)](https://developer.apple.com/documentation/coregraphics/1455544-cgcontextsetrenderingintent)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetRenderingIntent(_ context: CGContext!, _ intent: CGColorRenderingIntent) ``` |
| To | ``` func CGContextSetRenderingIntent(_ c: CGContext?, _ intent: CGColorRenderingIntent) ``` |

Modified [CGContextSetRGBFillColor(_: CGContext?, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1455624-cgcontextsetrgbfillcolor)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetRGBFillColor(_ context: CGContext!, _ red: CGFloat, _ green: CGFloat, _ blue: CGFloat, _ alpha: CGFloat) ``` |
| To | ``` func CGContextSetRGBFillColor(_ c: CGContext?, _ red: CGFloat, _ green: CGFloat, _ blue: CGFloat, _ alpha: CGFloat) ``` |

Modified [CGContextSetRGBStrokeColor(_: CGContext?, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1456378-cgcontextsetrgbstrokecolor)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetRGBStrokeColor(_ context: CGContext!, _ red: CGFloat, _ green: CGFloat, _ blue: CGFloat, _ alpha: CGFloat) ``` |
| To | ``` func CGContextSetRGBStrokeColor(_ c: CGContext?, _ red: CGFloat, _ green: CGFloat, _ blue: CGFloat, _ alpha: CGFloat) ``` |

Modified [CGContextSetShadow(_: CGContext?, _: CGSize, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1456082-cgcontextsetshadow)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetShadow(_ context: CGContext!, _ offset: CGSize, _ blur: CGFloat) ``` |
| To | ``` func CGContextSetShadow(_ c: CGContext?, _ offset: CGSize, _ blur: CGFloat) ``` |

Modified [CGContextSetShadowWithColor(_: CGContext?, _: CGSize, _: CGFloat, _: CGColor?)](https://developer.apple.com/documentation/coregraphics/1455205-cgcontextsetshadowwithcolor)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetShadowWithColor(_ context: CGContext!, _ offset: CGSize, _ blur: CGFloat, _ color: CGColor!) ``` |
| To | ``` func CGContextSetShadowWithColor(_ c: CGContext?, _ offset: CGSize, _ blur: CGFloat, _ color: CGColor?) ``` |

Modified [CGContextSetShouldAntialias(_: CGContext?, _: Bool)](https://developer.apple.com/documentation/coregraphics/cgcontext/1455178-setshouldantialias)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetShouldAntialias(_ context: CGContext!, _ shouldAntialias: Bool) ``` |
| To | ``` func CGContextSetShouldAntialias(_ c: CGContext?, _ shouldAntialias: Bool) ``` |

Modified [CGContextSetShouldSmoothFonts(_: CGContext?, _: Bool)](https://developer.apple.com/documentation/coregraphics/cgcontext/1455816-setshouldsmoothfonts)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetShouldSmoothFonts(_ context: CGContext!, _ shouldSmoothFonts: Bool) ``` |
| To | ``` func CGContextSetShouldSmoothFonts(_ c: CGContext?, _ shouldSmoothFonts: Bool) ``` |

Modified [CGContextSetShouldSubpixelPositionFonts(_: CGContext?, _: Bool)](https://developer.apple.com/documentation/coregraphics/1455671-cgcontextsetshouldsubpixelpositi)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetShouldSubpixelPositionFonts(_ context: CGContext!, _ shouldSubpixelPositionFonts: Bool) ``` |
| To | ``` func CGContextSetShouldSubpixelPositionFonts(_ c: CGContext?, _ shouldSubpixelPositionFonts: Bool) ``` |

Modified [CGContextSetShouldSubpixelQuantizeFonts(_: CGContext?, _: Bool)](https://developer.apple.com/documentation/coregraphics/1455766-cgcontextsetshouldsubpixelquanti)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetShouldSubpixelQuantizeFonts(_ context: CGContext!, _ shouldSubpixelQuantizeFonts: Bool) ``` |
| To | ``` func CGContextSetShouldSubpixelQuantizeFonts(_ c: CGContext?, _ shouldSubpixelQuantizeFonts: Bool) ``` |

Modified [CGContextSetStrokeColor(_: CGContext?, _: UnsafePointer<CGFloat>)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456283-setstrokecolor)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetStrokeColor(_ context: CGContext!, _ components: UnsafePointer<CGFloat>) ``` |
| To | ``` func CGContextSetStrokeColor(_ c: CGContext?, _ components: UnsafePointer<CGFloat>) ``` |

Modified [CGContextSetStrokeColorSpace(_: CGContext?, _: CGColorSpace?)](https://developer.apple.com/documentation/coregraphics/1454396-cgcontextsetstrokecolorspace)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetStrokeColorSpace(_ context: CGContext!, _ space: CGColorSpace!) ``` |
| To | ``` func CGContextSetStrokeColorSpace(_ c: CGContext?, _ space: CGColorSpace?) ``` |

Modified [CGContextSetStrokeColorWithColor(_: CGContext?, _: CGColor?)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456196-setstrokecolor)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetStrokeColorWithColor(_ c: CGContext!, _ color: CGColor!) ``` |
| To | ``` func CGContextSetStrokeColorWithColor(_ c: CGContext?, _ color: CGColor?) ``` |

Modified [CGContextSetStrokePattern(_: CGContext?, _: CGPattern?, _: UnsafePointer<CGFloat>)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454796-setstrokepattern)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetStrokePattern(_ context: CGContext!, _ pattern: CGPattern!, _ components: UnsafePointer<CGFloat>) ``` |
| To | ``` func CGContextSetStrokePattern(_ c: CGContext?, _ pattern: CGPattern?, _ components: UnsafePointer<CGFloat>) ``` |

Modified [CGContextSetTextDrawingMode(_: CGContext?, _: CGTextDrawingMode)](https://developer.apple.com/documentation/coregraphics/1454253-cgcontextsettextdrawingmode)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetTextDrawingMode(_ c: CGContext!, _ mode: CGTextDrawingMode) ``` |
| To | ``` func CGContextSetTextDrawingMode(_ c: CGContext?, _ mode: CGTextDrawingMode) ``` |

Modified [CGContextSetTextMatrix(_: CGContext?, _: CGAffineTransform)](https://developer.apple.com/documentation/coregraphics/1455611-cgcontextsettextmatrix)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetTextMatrix(_ c: CGContext!, _ t: CGAffineTransform) ``` |
| To | ``` func CGContextSetTextMatrix(_ c: CGContext?, _ t: CGAffineTransform) ``` |

Modified [CGContextSetTextPosition(_: CGContext?, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1456069-cgcontextsettextposition)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetTextPosition(_ c: CGContext!, _ x: CGFloat, _ y: CGFloat) ``` |
| To | ``` func CGContextSetTextPosition(_ c: CGContext?, _ x: CGFloat, _ y: CGFloat) ``` |

Modified [CGContextShowGlyphsAtPositions(_: CGContext?, _: UnsafePointer<CGGlyph>, _: UnsafePointer<CGPoint>, _: Int)](https://developer.apple.com/documentation/coregraphics/1456200-cgcontextshowglyphsatpositions)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextShowGlyphsAtPositions(_ context: CGContext!, _ glyphs: UnsafePointer<CGGlyph>, _ positions: UnsafePointer<CGPoint>, _ count: Int) ``` |
| To | ``` func CGContextShowGlyphsAtPositions(_ c: CGContext?, _ glyphs: UnsafePointer<CGGlyph>, _ Lpositions: UnsafePointer<CGPoint>, _ count: Int) ``` |

Modified [CGContextStrokeEllipseInRect(_: CGContext?, _: CGRect)](https://developer.apple.com/documentation/coregraphics/cgcontext/1455774-strokeellipse)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextStrokeEllipseInRect(_ context: CGContext!, _ rect: CGRect) ``` |
| To | ``` func CGContextStrokeEllipseInRect(_ c: CGContext?, _ rect: CGRect) ``` |

Modified [CGContextStrokeLineSegments(_: CGContext?, _: UnsafePointer<CGPoint>, _: Int)](https://developer.apple.com/documentation/coregraphics/1454389-cgcontextstrokelinesegments)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextStrokeLineSegments(_ c: CGContext!, _ points: UnsafePointer<CGPoint>, _ count: Int) ``` |
| To | ``` func CGContextStrokeLineSegments(_ c: CGContext?, _ points: UnsafePointer<CGPoint>, _ count: Int) ``` |

Modified [CGContextStrokePath(_: CGContext?)](https://developer.apple.com/documentation/coregraphics/1454490-cgcontextstrokepath)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextStrokePath(_ c: CGContext!) ``` |
| To | ``` func CGContextStrokePath(_ c: CGContext?) ``` |

Modified [CGContextStrokeRect(_: CGContext?, _: CGRect)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454675-stroke)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextStrokeRect(_ c: CGContext!, _ rect: CGRect) ``` |
| To | ``` func CGContextStrokeRect(_ c: CGContext?, _ rect: CGRect) ``` |

Modified [CGContextStrokeRectWithWidth(_: CGContext?, _: CGRect, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454679-stroke)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextStrokeRectWithWidth(_ c: CGContext!, _ rect: CGRect, _ width: CGFloat) ``` |
| To | ``` func CGContextStrokeRectWithWidth(_ c: CGContext?, _ rect: CGRect, _ width: CGFloat) ``` |

Modified [CGContextSynchronize(_: CGContext?)](https://developer.apple.com/documentation/coregraphics/1455450-cgcontextsynchronize)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSynchronize(_ c: CGContext!) ``` |
| To | ``` func CGContextSynchronize(_ c: CGContext?) ``` |

Modified [CGContextTranslateCTM(_: CGContext?, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1455286-translateby)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextTranslateCTM(_ c: CGContext!, _ tx: CGFloat, _ ty: CGFloat) ``` |
| To | ``` func CGContextTranslateCTM(_ c: CGContext?, _ tx: CGFloat, _ ty: CGFloat) ``` |

Modified [CGDataConsumerCreate(_: UnsafeMutablePointer<Void>, _: UnsafePointer<CGDataConsumerCallbacks>) -> CGDataConsumer?](https://developer.apple.com/documentation/coregraphics/1456428-cgdataconsumercreate)

|  | Declaration |
| --- | --- |
| From | ``` func CGDataConsumerCreate(_ info: UnsafeMutablePointer<Void>, _ callbacks: UnsafePointer<CGDataConsumerCallbacks>) -> CGDataConsumer! ``` |
| To | ``` func CGDataConsumerCreate(_ info: UnsafeMutablePointer<Void>, _ cbks: UnsafePointer<CGDataConsumerCallbacks>) -> CGDataConsumer? ``` |

Modified [CGDataConsumerCreateWithCFData(_: CFMutableData?) -> CGDataConsumer?](https://developer.apple.com/documentation/coregraphics/1456292-cgdataconsumercreatewithcfdata)

|  | Declaration |
| --- | --- |
| From | ``` func CGDataConsumerCreateWithCFData(_ data: CFMutableData!) -> CGDataConsumer! ``` |
| To | ``` func CGDataConsumerCreateWithCFData(_ data: CFMutableData?) -> CGDataConsumer? ``` |

Modified [CGDataConsumerCreateWithURL(_: CFURL?) -> CGDataConsumer?](https://developer.apple.com/documentation/coregraphics/1454474-cgdataconsumercreatewithurl)

|  | Declaration |
| --- | --- |
| From | ``` func CGDataConsumerCreateWithURL(_ url: CFURL!) -> CGDataConsumer! ``` |
| To | ``` func CGDataConsumerCreateWithURL(_ url: CFURL?) -> CGDataConsumer? ``` |

Modified [CGDataConsumerPutBytesCallback](https://developer.apple.com/documentation/coregraphics/cgdataconsumerputbytescallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataConsumerPutBytesCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int) -> Int)> ``` |
| To | ``` typealias CGDataConsumerPutBytesCallback = (UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int) -> Int ``` |

Modified [CGDataConsumerReleaseInfoCallback](https://developer.apple.com/documentation/coregraphics/cgdataconsumerreleaseinfocallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataConsumerReleaseInfoCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CGDataConsumerReleaseInfoCallback = (UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CGDataProviderCopyData(_: CGDataProvider?) -> CFData?](https://developer.apple.com/documentation/coregraphics/1408309-cgdataprovidercopydata)

|  | Declaration |
| --- | --- |
| From | ``` func CGDataProviderCopyData(_ provider: CGDataProvider!) -> CFData! ``` |
| To | ``` func CGDataProviderCopyData(_ provider: CGDataProvider?) -> CFData? ``` |

Modified [CGDataProviderCreateDirect(_: UnsafeMutablePointer<Void>, _: off_t, _: UnsafePointer<CGDataProviderDirectCallbacks>) -> CGDataProvider?](https://developer.apple.com/documentation/coregraphics/cgdataprovider/1408282-init)

|  | Declaration |
| --- | --- |
| From | ``` func CGDataProviderCreateDirect(_ info: UnsafeMutablePointer<Void>, _ size: off_t, _ callbacks: UnsafePointer<CGDataProviderDirectCallbacks>) -> CGDataProvider! ``` |
| To | ``` func CGDataProviderCreateDirect(_ info: UnsafeMutablePointer<Void>, _ size: off_t, _ callbacks: UnsafePointer<CGDataProviderDirectCallbacks>) -> CGDataProvider? ``` |

Modified [CGDataProviderCreateSequential(_: UnsafeMutablePointer<Void>, _: UnsafePointer<CGDataProviderSequentialCallbacks>) -> CGDataProvider?](https://developer.apple.com/documentation/coregraphics/1408291-cgdataprovidercreatesequential)

|  | Declaration |
| --- | --- |
| From | ``` func CGDataProviderCreateSequential(_ info: UnsafeMutablePointer<Void>, _ callbacks: UnsafePointer<CGDataProviderSequentialCallbacks>) -> CGDataProvider! ``` |
| To | ``` func CGDataProviderCreateSequential(_ info: UnsafeMutablePointer<Void>, _ callbacks: UnsafePointer<CGDataProviderSequentialCallbacks>) -> CGDataProvider? ``` |

Modified [CGDataProviderCreateWithCFData(_: CFData?) -> CGDataProvider?](https://developer.apple.com/documentation/coregraphics/1408284-cgdataprovidercreatewithcfdata)

|  | Declaration |
| --- | --- |
| From | ``` func CGDataProviderCreateWithCFData(_ data: CFData!) -> CGDataProvider! ``` |
| To | ``` func CGDataProviderCreateWithCFData(_ data: CFData?) -> CGDataProvider? ``` |

Modified [CGDataProviderCreateWithData(_: UnsafeMutablePointer<Void>, _: UnsafePointer<Void>, _: Int, _: CGDataProviderReleaseDataCallback?) -> CGDataProvider?](https://developer.apple.com/documentation/coregraphics/1408288-cgdataprovidercreatewithdata)

|  | Declaration |
| --- | --- |
| From | ``` func CGDataProviderCreateWithData(_ info: UnsafeMutablePointer<Void>, _ data: UnsafePointer<Void>, _ size: Int, _ releaseData: CGDataProviderReleaseDataCallback) -> CGDataProvider! ``` |
| To | ``` func CGDataProviderCreateWithData(_ info: UnsafeMutablePointer<Void>, _ data: UnsafePointer<Void>, _ size: Int, _ releaseData: CGDataProviderReleaseDataCallback?) -> CGDataProvider? ``` |

Modified [CGDataProviderCreateWithFilename(_: UnsafePointer<Int8>) -> CGDataProvider?](https://developer.apple.com/documentation/coregraphics/cgdataprovider/1408294-init)

|  | Declaration |
| --- | --- |
| From | ``` func CGDataProviderCreateWithFilename(_ filename: UnsafePointer<Int8>) -> CGDataProvider! ``` |
| To | ``` func CGDataProviderCreateWithFilename(_ filename: UnsafePointer<Int8>) -> CGDataProvider? ``` |

Modified [CGDataProviderCreateWithURL(_: CFURL?) -> CGDataProvider?](https://developer.apple.com/documentation/coregraphics/cgdataprovider/1408327-init)

|  | Declaration |
| --- | --- |
| From | ``` func CGDataProviderCreateWithURL(_ url: CFURL!) -> CGDataProvider! ``` |
| To | ``` func CGDataProviderCreateWithURL(_ url: CFURL?) -> CGDataProvider? ``` |

Modified [CGDataProviderGetBytePointerCallback](https://developer.apple.com/documentation/coregraphics/cgdataprovidergetbytepointercallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderGetBytePointerCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` typealias CGDataProviderGetBytePointerCallback = (UnsafeMutablePointer<Void>) -> UnsafePointer<Void> ``` |

Modified [CGDataProviderGetBytesAtPositionCallback](https://developer.apple.com/documentation/coregraphics/cgdataprovidergetbytesatpositioncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderGetBytesAtPositionCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, off_t, Int) -> Int)> ``` |
| To | ``` typealias CGDataProviderGetBytesAtPositionCallback = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, off_t, Int) -> Int ``` |

Modified [CGDataProviderGetBytesCallback](https://developer.apple.com/documentation/coregraphics/cgdataprovidergetbytescallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderGetBytesCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Int)> ``` |
| To | ``` typealias CGDataProviderGetBytesCallback = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Int ``` |

Modified [CGDataProviderReleaseBytePointerCallback](https://developer.apple.com/documentation/coregraphics/cgdataproviderreleasebytepointercallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderReleaseBytePointerCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>) -> Void)> ``` |
| To | ``` typealias CGDataProviderReleaseBytePointerCallback = (UnsafeMutablePointer<Void>, UnsafePointer<Void>) -> Void ``` |

Modified [CGDataProviderReleaseDataCallback](https://developer.apple.com/documentation/coregraphics/cgdataproviderreleasedatacallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderReleaseDataCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int) -> Void)> ``` |
| To | ``` typealias CGDataProviderReleaseDataCallback = (UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int) -> Void ``` |

Modified [CGDataProviderReleaseInfoCallback](https://developer.apple.com/documentation/coregraphics/cgdataproviderreleaseinfocallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderReleaseInfoCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CGDataProviderReleaseInfoCallback = (UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CGDataProviderRewindCallback](https://developer.apple.com/documentation/coregraphics/cgdataproviderrewindcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderRewindCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CGDataProviderRewindCallback = (UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CGDataProviderSkipForwardCallback](https://developer.apple.com/documentation/coregraphics/cgdataproviderskipforwardcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderSkipForwardCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, off_t) -> off_t)> ``` |
| To | ``` typealias CGDataProviderSkipForwardCallback = (UnsafeMutablePointer<Void>, off_t) -> off_t ``` |

Modified [CGDisplayCopyAllDisplayModes(_: CGDirectDisplayID, _: CFDictionary?) -> CFArray?](https://developer.apple.com/documentation/coregraphics/1455537-cgdisplaycopyalldisplaymodes)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayCopyAllDisplayModes(_ display: CGDirectDisplayID, _ options: CFDictionary!) -> Unmanaged<CFArray>! ``` |
| To | ``` func CGDisplayCopyAllDisplayModes(_ display: CGDirectDisplayID, _ options: CFDictionary?) -> CFArray? ``` |

Modified [CGDisplayCopyColorSpace(_: CGDirectDisplayID) -> CGColorSpace](https://developer.apple.com/documentation/coregraphics/1454190-cgdisplaycopycolorspace)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayCopyColorSpace(_ display: CGDirectDisplayID) -> Unmanaged<CGColorSpace>! ``` |
| To | ``` func CGDisplayCopyColorSpace(_ display: CGDirectDisplayID) -> CGColorSpace ``` |

Modified [CGDisplayCopyDisplayMode(_: CGDirectDisplayID) -> CGDisplayMode?](https://developer.apple.com/documentation/coregraphics/1454099-cgdisplaycopydisplaymode)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayCopyDisplayMode(_ display: CGDirectDisplayID) -> Unmanaged<CGDisplayMode>! ``` |
| To | ``` func CGDisplayCopyDisplayMode(_ display: CGDirectDisplayID) -> CGDisplayMode? ``` |

Modified [CGDisplayCreateImage(_: CGDirectDisplayID) -> CGImage?](https://developer.apple.com/documentation/coregraphics/1455691-cgdisplaycreateimage)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayCreateImage(_ displayID: CGDirectDisplayID) -> Unmanaged<CGImage>! ``` |
| To | ``` func CGDisplayCreateImage(_ displayID: CGDirectDisplayID) -> CGImage? ``` |

Modified [CGDisplayCreateImageForRect(_: CGDirectDisplayID, _: CGRect) -> CGImage?](https://developer.apple.com/documentation/coregraphics/1454595-cgdisplaycreateimage)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayCreateImageForRect(_ display: CGDirectDisplayID, _ rect: CGRect) -> Unmanaged<CGImage>! ``` |
| To | ``` func CGDisplayCreateImageForRect(_ display: CGDirectDisplayID, _ rect: CGRect) -> CGImage? ``` |

Modified [CGDisplayGetDrawingContext(_: CGDirectDisplayID) -> CGContext?](https://developer.apple.com/documentation/coregraphics/1456576-cgdisplaygetdrawingcontext)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayGetDrawingContext(_ display: CGDirectDisplayID) -> Unmanaged<CGContext>! ``` |
| To | ``` func CGDisplayGetDrawingContext(_ display: CGDirectDisplayID) -> CGContext? ``` |

Modified [CGDisplayModeCopyPixelEncoding(_: CGDisplayMode?) -> CFString?](https://developer.apple.com/documentation/coregraphics/cgdisplaymode/1455067-pixelencoding)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func CGDisplayModeCopyPixelEncoding(_ mode: CGDisplayMode!) -> Unmanaged<CFString>! ``` | -- |
| To | ``` func CGDisplayModeCopyPixelEncoding(_ mode: CGDisplayMode?) -> CFString? ``` | OS X 10.11 |

Modified [CGDisplayModeGetHeight(_: CGDisplayMode?) -> Int](https://developer.apple.com/documentation/coregraphics/1455380-cgdisplaymodegetheight)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayModeGetHeight(_ mode: CGDisplayMode!) -> Int ``` |
| To | ``` func CGDisplayModeGetHeight(_ mode: CGDisplayMode?) -> Int ``` |

Modified [CGDisplayModeGetIODisplayModeID(_: CGDisplayMode?) -> Int32](https://developer.apple.com/documentation/coregraphics/cgdisplaymode/1454728-iodisplaymodeid)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayModeGetIODisplayModeID(_ mode: CGDisplayMode!) -> Int32 ``` |
| To | ``` func CGDisplayModeGetIODisplayModeID(_ mode: CGDisplayMode?) -> Int32 ``` |

Modified [CGDisplayModeGetIOFlags(_: CGDisplayMode?) -> UInt32](https://developer.apple.com/documentation/coregraphics/1454092-cgdisplaymodegetioflags)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayModeGetIOFlags(_ mode: CGDisplayMode!) -> UInt32 ``` |
| To | ``` func CGDisplayModeGetIOFlags(_ mode: CGDisplayMode?) -> UInt32 ``` |

Modified [CGDisplayModeGetPixelHeight(_: CGDisplayMode?) -> Int](https://developer.apple.com/documentation/coregraphics/cgdisplaymode/1456406-pixelheight)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayModeGetPixelHeight(_ mode: CGDisplayMode!) -> Int ``` |
| To | ``` func CGDisplayModeGetPixelHeight(_ mode: CGDisplayMode?) -> Int ``` |

Modified [CGDisplayModeGetPixelWidth(_: CGDisplayMode?) -> Int](https://developer.apple.com/documentation/coregraphics/cgdisplaymode/1454756-pixelwidth)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayModeGetPixelWidth(_ mode: CGDisplayMode!) -> Int ``` |
| To | ``` func CGDisplayModeGetPixelWidth(_ mode: CGDisplayMode?) -> Int ``` |

Modified [CGDisplayModeGetRefreshRate(_: CGDisplayMode?) -> Double](https://developer.apple.com/documentation/coregraphics/1454661-cgdisplaymodegetrefreshrate)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayModeGetRefreshRate(_ mode: CGDisplayMode!) -> Double ``` |
| To | ``` func CGDisplayModeGetRefreshRate(_ mode: CGDisplayMode?) -> Double ``` |

Modified [CGDisplayModeGetWidth(_: CGDisplayMode?) -> Int](https://developer.apple.com/documentation/coregraphics/cgdisplaymode/1454442-width)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayModeGetWidth(_ mode: CGDisplayMode!) -> Int ``` |
| To | ``` func CGDisplayModeGetWidth(_ mode: CGDisplayMode?) -> Int ``` |

Modified [CGDisplayModeIsUsableForDesktopGUI(_: CGDisplayMode?) -> Bool](https://developer.apple.com/documentation/coregraphics/cgdisplaymode/1454928-isusablefordesktopgui)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayModeIsUsableForDesktopGUI(_ mode: CGDisplayMode!) -> Bool ``` |
| To | ``` func CGDisplayModeIsUsableForDesktopGUI(_ mode: CGDisplayMode?) -> Bool ``` |

Modified [CGDisplayReconfigurationCallBack](https://developer.apple.com/documentation/coregraphics/cgdisplayreconfigurationcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDisplayReconfigurationCallBack = CFunctionPointer<((CGDirectDisplayID, CGDisplayChangeSummaryFlags, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CGDisplayReconfigurationCallBack = (CGDirectDisplayID, CGDisplayChangeSummaryFlags, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CGDisplayRegisterReconfigurationCallback(_: CGDisplayReconfigurationCallBack?, _: UnsafeMutablePointer<Void>) -> CGError](https://developer.apple.com/documentation/coregraphics/1455336-cgdisplayregisterreconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayRegisterReconfigurationCallback(_ callback: CGDisplayReconfigurationCallBack, _ userInfo: UnsafeMutablePointer<Void>) -> CGError ``` |
| To | ``` func CGDisplayRegisterReconfigurationCallback(_ callback: CGDisplayReconfigurationCallBack?, _ userInfo: UnsafeMutablePointer<Void>) -> CGError ``` |

Modified [CGDisplayRemoveReconfigurationCallback(_: CGDisplayReconfigurationCallBack?, _: UnsafeMutablePointer<Void>) -> CGError](https://developer.apple.com/documentation/coregraphics/1455407-cgdisplayremovereconfigurationca)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayRemoveReconfigurationCallback(_ callback: CGDisplayReconfigurationCallBack, _ userInfo: UnsafeMutablePointer<Void>) -> CGError ``` |
| To | ``` func CGDisplayRemoveReconfigurationCallback(_ callback: CGDisplayReconfigurationCallBack?, _ userInfo: UnsafeMutablePointer<Void>) -> CGError ``` |

Modified [CGDisplaySetDisplayMode(_: CGDirectDisplayID, _: CGDisplayMode?, _: CFDictionary?) -> CGError](https://developer.apple.com/documentation/coregraphics/1454760-cgdisplaysetdisplaymode)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplaySetDisplayMode(_ display: CGDirectDisplayID, _ mode: CGDisplayMode!, _ options: CFDictionary!) -> CGError ``` |
| To | ``` func CGDisplaySetDisplayMode(_ display: CGDirectDisplayID, _ mode: CGDisplayMode?, _ options: CFDictionary?) -> CGError ``` |

Modified [CGDisplayStreamCreate(_: CGDirectDisplayID, _: Int, _: Int, _: Int32, _: CFDictionary?, _: CGDisplayStreamFrameAvailableHandler?) -> CGDisplayStream?](https://developer.apple.com/documentation/coregraphics/cgdisplaystream/1455170-init)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayStreamCreate(_ display: CGDirectDisplayID, _ outputWidth: Int, _ outputHeight: Int, _ pixelFormat: Int32, _ properties: CFDictionary!, _ handler: CGDisplayStreamFrameAvailableHandler!) -> Unmanaged<CGDisplayStream>! ``` |
| To | ``` func CGDisplayStreamCreate(_ display: CGDirectDisplayID, _ outputWidth: Int, _ outputHeight: Int, _ pixelFormat: Int32, _ properties: CFDictionary?, _ handler: CGDisplayStreamFrameAvailableHandler?) -> CGDisplayStream? ``` |

Modified [CGDisplayStreamCreateWithDispatchQueue(_: CGDirectDisplayID, _: Int, _: Int, _: Int32, _: CFDictionary?, _: dispatch_queue_t, _: CGDisplayStreamFrameAvailableHandler?) -> CGDisplayStream?](https://developer.apple.com/documentation/coregraphics/1454968-cgdisplaystreamcreatewithdispatc)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayStreamCreateWithDispatchQueue(_ display: CGDirectDisplayID, _ outputWidth: Int, _ outputHeight: Int, _ pixelFormat: Int32, _ properties: CFDictionary!, _ queue: dispatch_queue_t!, _ handler: CGDisplayStreamFrameAvailableHandler!) -> Unmanaged<CGDisplayStream>! ``` |
| To | ``` func CGDisplayStreamCreateWithDispatchQueue(_ display: CGDirectDisplayID, _ outputWidth: Int, _ outputHeight: Int, _ pixelFormat: Int32, _ properties: CFDictionary?, _ queue: dispatch_queue_t, _ handler: CGDisplayStreamFrameAvailableHandler?) -> CGDisplayStream? ``` |

Modified [CGDisplayStreamFrameAvailableHandler](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamframeavailablehandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDisplayStreamFrameAvailableHandler = (CGDisplayStreamFrameStatus, UInt64, IOSurface!, CGDisplayStreamUpdate!) -> Void ``` |
| To | ``` typealias CGDisplayStreamFrameAvailableHandler = (CGDisplayStreamFrameStatus, UInt64, IOSurface?, CGDisplayStreamUpdate?) -> Void ``` |

Modified [CGDisplayStreamGetRunLoopSource(_: CGDisplayStream?) -> CFRunLoopSource?](https://developer.apple.com/documentation/coregraphics/1455403-cgdisplaystreamgetrunloopsource)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayStreamGetRunLoopSource(_ displayStream: CGDisplayStream!) -> Unmanaged<CFRunLoopSource>! ``` |
| To | ``` func CGDisplayStreamGetRunLoopSource(_ displayStream: CGDisplayStream?) -> CFRunLoopSource? ``` |

Modified [CGDisplayStreamStart(_: CGDisplayStream?) -> CGError](https://developer.apple.com/documentation/coregraphics/1454870-cgdisplaystreamstart)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayStreamStart(_ displayStream: CGDisplayStream!) -> CGError ``` |
| To | ``` func CGDisplayStreamStart(_ displayStream: CGDisplayStream?) -> CGError ``` |

Modified [CGDisplayStreamStop(_: CGDisplayStream?) -> CGError](https://developer.apple.com/documentation/coregraphics/cgdisplaystream/1455658-stop)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayStreamStop(_ displayStream: CGDisplayStream!) -> CGError ``` |
| To | ``` func CGDisplayStreamStop(_ displayStream: CGDisplayStream?) -> CGError ``` |

Modified [CGDisplayStreamUpdateCreateMergedUpdate(_: CGDisplayStreamUpdate?, _: CGDisplayStreamUpdate?) -> CGDisplayStreamUpdate?](https://developer.apple.com/documentation/coregraphics/1454341-cgdisplaystreamupdatecreatemerge)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayStreamUpdateCreateMergedUpdate(_ firstUpdate: CGDisplayStreamUpdate!, _ secondUpdate: CGDisplayStreamUpdate!) -> Unmanaged<CGDisplayStreamUpdate>! ``` |
| To | ``` func CGDisplayStreamUpdateCreateMergedUpdate(_ firstUpdate: CGDisplayStreamUpdate?, _ secondUpdate: CGDisplayStreamUpdate?) -> CGDisplayStreamUpdate? ``` |

Modified [CGDisplayStreamUpdateGetDropCount(_: CGDisplayStreamUpdate?) -> Int](https://developer.apple.com/documentation/coregraphics/1456212-cgdisplaystreamupdategetdropcoun)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayStreamUpdateGetDropCount(_ updateRef: CGDisplayStreamUpdate!) -> Int ``` |
| To | ``` func CGDisplayStreamUpdateGetDropCount(_ updateRef: CGDisplayStreamUpdate?) -> Int ``` |

Modified [CGDisplayStreamUpdateGetMovedRectsDelta(_: CGDisplayStreamUpdate?, _: UnsafeMutablePointer<CGFloat>, _: UnsafeMutablePointer<CGFloat>)](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdate/1455469-getmovedrectsdelta)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayStreamUpdateGetMovedRectsDelta(_ updateRef: CGDisplayStreamUpdate!, _ dx: UnsafeMutablePointer<CGFloat>, _ dy: UnsafeMutablePointer<CGFloat>) ``` |
| To | ``` func CGDisplayStreamUpdateGetMovedRectsDelta(_ updateRef: CGDisplayStreamUpdate?, _ dx: UnsafeMutablePointer<CGFloat>, _ dy: UnsafeMutablePointer<CGFloat>) ``` |

Modified [CGDisplayStreamUpdateGetRects(_: CGDisplayStreamUpdate?, _: CGDisplayStreamUpdateRectType, _: UnsafeMutablePointer<Int>) -> UnsafePointer<CGRect>](https://developer.apple.com/documentation/coregraphics/1455530-cgdisplaystreamupdategetrects)

|  | Declaration |
| --- | --- |
| From | ``` func CGDisplayStreamUpdateGetRects(_ updateRef: CGDisplayStreamUpdate!, _ rectType: CGDisplayStreamUpdateRectType, _ rectCount: UnsafeMutablePointer<Int>) -> UnsafePointer<CGRect> ``` |
| To | ``` func CGDisplayStreamUpdateGetRects(_ updateRef: CGDisplayStreamUpdate?, _ rectType: CGDisplayStreamUpdateRectType, _ rectCount: UnsafeMutablePointer<Int>) -> UnsafePointer<CGRect> ``` |

Modified [CGEventCreate(_: CGEventSource?) -> CGEvent?](https://developer.apple.com/documentation/coregraphics/1454913-cgeventcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventCreate(_ source: CGEventSource!) -> Unmanaged<CGEvent>! ``` |
| To | ``` func CGEventCreate(_ source: CGEventSource?) -> CGEvent? ``` |

Modified [CGEventCreateCopy(_: CGEvent?) -> CGEvent?](https://developer.apple.com/documentation/coregraphics/cgevent/1454071-copy)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventCreateCopy(_ event: CGEvent!) -> Unmanaged<CGEvent>! ``` |
| To | ``` func CGEventCreateCopy(_ event: CGEvent?) -> CGEvent? ``` |

Modified [CGEventCreateData(_: CFAllocator?, _: CGEvent?) -> CFData?](https://developer.apple.com/documentation/coregraphics/1454381-cgeventcreatedata)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventCreateData(_ allocator: CFAllocator!, _ event: CGEvent!) -> Unmanaged<CFData>! ``` |
| To | ``` func CGEventCreateData(_ allocator: CFAllocator?, _ event: CGEvent?) -> CFData? ``` |

Modified [CGEventCreateFromData(_: CFAllocator?, _: CFData?) -> CGEvent?](https://developer.apple.com/documentation/coregraphics/cgevent/1454249-init)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventCreateFromData(_ allocator: CFAllocator!, _ data: CFData!) -> Unmanaged<CGEvent>! ``` |
| To | ``` func CGEventCreateFromData(_ allocator: CFAllocator?, _ data: CFData?) -> CGEvent? ``` |

Modified [CGEventCreateKeyboardEvent(_: CGEventSource?, _: CGKeyCode, _: Bool) -> CGEvent?](https://developer.apple.com/documentation/coregraphics/cgevent/1456564-init)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventCreateKeyboardEvent(_ source: CGEventSource!, _ virtualKey: CGKeyCode, _ keyDown: Bool) -> Unmanaged<CGEvent>! ``` |
| To | ``` func CGEventCreateKeyboardEvent(_ source: CGEventSource?, _ virtualKey: CGKeyCode, _ keyDown: Bool) -> CGEvent? ``` |

Modified [CGEventCreateMouseEvent(_: CGEventSource?, _: CGEventType, _: CGPoint, _: CGMouseButton) -> CGEvent?](https://developer.apple.com/documentation/coregraphics/cgevent/1454356-init)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventCreateMouseEvent(_ source: CGEventSource!, _ mouseType: CGEventType, _ mouseCursorPosition: CGPoint, _ mouseButton: CGMouseButton) -> Unmanaged<CGEvent>! ``` |
| To | ``` func CGEventCreateMouseEvent(_ source: CGEventSource?, _ mouseType: CGEventType, _ mouseCursorPosition: CGPoint, _ mouseButton: CGMouseButton) -> CGEvent? ``` |

Modified [CGEventCreateSourceFromEvent(_: CGEvent?) -> CGEventSource?](https://developer.apple.com/documentation/coregraphics/1455393-cgeventcreatesourcefromevent)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventCreateSourceFromEvent(_ event: CGEvent!) -> Unmanaged<CGEventSource>! ``` |
| To | ``` func CGEventCreateSourceFromEvent(_ event: CGEvent?) -> CGEventSource? ``` |

Modified [CGEventGetDoubleValueField(_: CGEvent?, _: CGEventField) -> Double](https://developer.apple.com/documentation/coregraphics/1455506-cgeventgetdoublevaluefield)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventGetDoubleValueField(_ event: CGEvent!, _ field: CGEventField) -> Double ``` |
| To | ``` func CGEventGetDoubleValueField(_ event: CGEvent?, _ field: CGEventField) -> Double ``` |

Modified [CGEventGetFlags(_: CGEvent?) -> CGEventFlags](https://developer.apple.com/documentation/coregraphics/1455642-cgeventgetflags)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventGetFlags(_ event: CGEvent!) -> CGEventFlags ``` |
| To | ``` func CGEventGetFlags(_ event: CGEvent?) -> CGEventFlags ``` |

Modified [CGEventGetIntegerValueField(_: CGEvent?, _: CGEventField) -> Int64](https://developer.apple.com/documentation/coregraphics/cgevent/1455885-getintegervaluefield)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventGetIntegerValueField(_ event: CGEvent!, _ field: CGEventField) -> Int64 ``` |
| To | ``` func CGEventGetIntegerValueField(_ event: CGEvent?, _ field: CGEventField) -> Int64 ``` |

Modified [CGEventGetLocation(_: CGEvent?) -> CGPoint](https://developer.apple.com/documentation/coregraphics/cgevent/1455788-location)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventGetLocation(_ event: CGEvent!) -> CGPoint ``` |
| To | ``` func CGEventGetLocation(_ event: CGEvent?) -> CGPoint ``` |

Modified [CGEventGetTimestamp(_: CGEvent?) -> CGEventTimestamp](https://developer.apple.com/documentation/coregraphics/cgevent/1455481-timestamp)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventGetTimestamp(_ event: CGEvent!) -> CGEventTimestamp ``` |
| To | ``` func CGEventGetTimestamp(_ event: CGEvent?) -> CGEventTimestamp ``` |

Modified [CGEventGetType(_: CGEvent?) -> CGEventType](https://developer.apple.com/documentation/coregraphics/cgevent/1455634-type)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventGetType(_ event: CGEvent!) -> CGEventType ``` |
| To | ``` func CGEventGetType(_ event: CGEvent?) -> CGEventType ``` |

Modified [CGEventGetUnflippedLocation(_: CGEvent?) -> CGPoint](https://developer.apple.com/documentation/coregraphics/1455589-cgeventgetunflippedlocation)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventGetUnflippedLocation(_ event: CGEvent!) -> CGPoint ``` |
| To | ``` func CGEventGetUnflippedLocation(_ event: CGEvent?) -> CGPoint ``` |

Modified [CGEventKeyboardGetUnicodeString(_: CGEvent?, _: Int, _: UnsafeMutablePointer<Int>, _: UnsafeMutablePointer<UniChar>)](https://developer.apple.com/documentation/coregraphics/cgevent/1456120-keyboardgetunicodestring)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventKeyboardGetUnicodeString(_ event: CGEvent!, _ maxStringLength: Int, _ actualStringLength: UnsafeMutablePointer<Int>, _ unicodeString: UnsafeMutablePointer<UniChar>) ``` |
| To | ``` func CGEventKeyboardGetUnicodeString(_ event: CGEvent?, _ maxStringLength: Int, _ actualStringLength: UnsafeMutablePointer<Int>, _ unicodeString: UnsafeMutablePointer<UniChar>) ``` |

Modified [CGEventKeyboardSetUnicodeString(_: CGEvent?, _: Int, _: UnsafePointer<UniChar>)](https://developer.apple.com/documentation/coregraphics/1456028-cgeventkeyboardsetunicodestring)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventKeyboardSetUnicodeString(_ event: CGEvent!, _ stringLength: Int, _ unicodeString: UnsafePointer<UniChar>) ``` |
| To | ``` func CGEventKeyboardSetUnicodeString(_ event: CGEvent?, _ stringLength: Int, _ unicodeString: UnsafePointer<UniChar>) ``` |

Modified [CGEventPost(_: CGEventTapLocation, _: CGEvent?)](https://developer.apple.com/documentation/coregraphics/cgevent/1456527-post)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventPost(_ tap: CGEventTapLocation, _ event: CGEvent!) ``` |
| To | ``` func CGEventPost(_ tap: CGEventTapLocation, _ event: CGEvent?) ``` |

Modified [CGEventPostToPSN(_: UnsafeMutablePointer<Void>, _: CGEvent?)](https://developer.apple.com/documentation/coregraphics/1455313-cgeventposttopsn)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventPostToPSN(_ processSerialNumber: UnsafeMutablePointer<Void>, _ event: CGEvent!) ``` |
| To | ``` func CGEventPostToPSN(_ processSerialNumber: UnsafeMutablePointer<Void>, _ event: CGEvent?) ``` |

Modified [CGEventSetDoubleValueField(_: CGEvent?, _: CGEventField, _: Double)](https://developer.apple.com/documentation/coregraphics/cgevent/1455526-setdoublevaluefield)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventSetDoubleValueField(_ event: CGEvent!, _ field: CGEventField, _ value: Double) ``` |
| To | ``` func CGEventSetDoubleValueField(_ event: CGEvent?, _ field: CGEventField, _ value: Double) ``` |

Modified [CGEventSetFlags(_: CGEvent?, _: CGEventFlags)](https://developer.apple.com/documentation/coregraphics/1455044-cgeventsetflags)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventSetFlags(_ event: CGEvent!, _ flags: CGEventFlags) ``` |
| To | ``` func CGEventSetFlags(_ event: CGEvent?, _ flags: CGEventFlags) ``` |

Modified [CGEventSetIntegerValueField(_: CGEvent?, _: CGEventField, _: Int64)](https://developer.apple.com/documentation/coregraphics/cgevent/1455556-setintegervaluefield)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventSetIntegerValueField(_ event: CGEvent!, _ field: CGEventField, _ value: Int64) ``` |
| To | ``` func CGEventSetIntegerValueField(_ event: CGEvent?, _ field: CGEventField, _ value: Int64) ``` |

Modified [CGEventSetLocation(_: CGEvent?, _: CGPoint)](https://developer.apple.com/documentation/coregraphics/1456389-cgeventsetlocation)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventSetLocation(_ event: CGEvent!, _ location: CGPoint) ``` |
| To | ``` func CGEventSetLocation(_ event: CGEvent?, _ location: CGPoint) ``` |

Modified [CGEventSetSource(_: CGEvent?, _: CGEventSource?)](https://developer.apple.com/documentation/coregraphics/cgevent/1455500-setsource)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventSetSource(_ event: CGEvent!, _ source: CGEventSource!) ``` |
| To | ``` func CGEventSetSource(_ event: CGEvent?, _ source: CGEventSource?) ``` |

Modified [CGEventSetTimestamp(_: CGEvent?, _: CGEventTimestamp)](https://developer.apple.com/documentation/coregraphics/1456611-cgeventsettimestamp)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventSetTimestamp(_ event: CGEvent!, _ timestamp: CGEventTimestamp) ``` |
| To | ``` func CGEventSetTimestamp(_ event: CGEvent?, _ timestamp: CGEventTimestamp) ``` |

Modified [CGEventSetType(_: CGEvent?, _: CGEventType)](https://developer.apple.com/documentation/coregraphics/1454300-cgeventsettype)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventSetType(_ event: CGEvent!, _ type: CGEventType) ``` |
| To | ``` func CGEventSetType(_ event: CGEvent?, _ type: CGEventType) ``` |

Modified [CGEventSourceCreate(_: CGEventSourceStateID) -> CGEventSource?](https://developer.apple.com/documentation/coregraphics/1408776-cgeventsourcecreate)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventSourceCreate(_ stateID: CGEventSourceStateID) -> Unmanaged<CGEventSource>! ``` |
| To | ``` func CGEventSourceCreate(_ stateID: CGEventSourceStateID) -> CGEventSource? ``` |

Modified [CGEventSourceGetKeyboardType(_: CGEventSource?) -> CGEventSourceKeyboardType](https://developer.apple.com/documentation/coregraphics/cgeventsource/1408787-keyboardtype)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventSourceGetKeyboardType(_ source: CGEventSource!) -> CGEventSourceKeyboardType ``` |
| To | ``` func CGEventSourceGetKeyboardType(_ source: CGEventSource?) -> CGEventSourceKeyboardType ``` |

Modified [CGEventSourceGetLocalEventsFilterDuringSuppressionState(_: CGEventSource?, _: CGEventSuppressionState) -> CGEventFilterMask](https://developer.apple.com/documentation/coregraphics/cgeventsource/1408785-getlocaleventsfilterduringsuppre)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventSourceGetLocalEventsFilterDuringSuppressionState(_ source: CGEventSource!, _ state: CGEventSuppressionState) -> CGEventFilterMask ``` |
| To | ``` func CGEventSourceGetLocalEventsFilterDuringSuppressionState(_ source: CGEventSource?, _ state: CGEventSuppressionState) -> CGEventFilterMask ``` |

Modified [CGEventSourceGetLocalEventsSuppressionInterval(_: CGEventSource?) -> CFTimeInterval](https://developer.apple.com/documentation/coregraphics/1408774-cgeventsourcegetlocaleventssuppr)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventSourceGetLocalEventsSuppressionInterval(_ source: CGEventSource!) -> CFTimeInterval ``` |
| To | ``` func CGEventSourceGetLocalEventsSuppressionInterval(_ source: CGEventSource?) -> CFTimeInterval ``` |

Modified [CGEventSourceGetPixelsPerLine(_: CGEventSource?) -> Double](https://developer.apple.com/documentation/coregraphics/cgeventsource/1408775-pixelsperline)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventSourceGetPixelsPerLine(_ source: CGEventSource!) -> Double ``` |
| To | ``` func CGEventSourceGetPixelsPerLine(_ source: CGEventSource?) -> Double ``` |

Modified [CGEventSourceGetSourceStateID(_: CGEventSource?) -> CGEventSourceStateID](https://developer.apple.com/documentation/coregraphics/cgeventsource/1408772-sourcestateid)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventSourceGetSourceStateID(_ source: CGEventSource!) -> CGEventSourceStateID ``` |
| To | ``` func CGEventSourceGetSourceStateID(_ source: CGEventSource?) -> CGEventSourceStateID ``` |

Modified [CGEventSourceGetUserData(_: CGEventSource?) -> Int64](https://developer.apple.com/documentation/coregraphics/1408777-cgeventsourcegetuserdata)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventSourceGetUserData(_ source: CGEventSource!) -> Int64 ``` |
| To | ``` func CGEventSourceGetUserData(_ source: CGEventSource?) -> Int64 ``` |

Modified [CGEventSourceSetKeyboardType(_: CGEventSource?, _: CGEventSourceKeyboardType)](https://developer.apple.com/documentation/coregraphics/1408795-cgeventsourcesetkeyboardtype)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventSourceSetKeyboardType(_ source: CGEventSource!, _ keyboardType: CGEventSourceKeyboardType) ``` |
| To | ``` func CGEventSourceSetKeyboardType(_ source: CGEventSource?, _ keyboardType: CGEventSourceKeyboardType) ``` |

Modified [CGEventSourceSetLocalEventsFilterDuringSuppressionState(_: CGEventSource?, _: CGEventFilterMask, _: CGEventSuppressionState)](https://developer.apple.com/documentation/coregraphics/cgeventsource/1408770-setlocaleventsfilterduringsuppre)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventSourceSetLocalEventsFilterDuringSuppressionState(_ source: CGEventSource!, _ filter: CGEventFilterMask, _ state: CGEventSuppressionState) ``` |
| To | ``` func CGEventSourceSetLocalEventsFilterDuringSuppressionState(_ source: CGEventSource?, _ filter: CGEventFilterMask, _ state: CGEventSuppressionState) ``` |

Modified [CGEventSourceSetLocalEventsSuppressionInterval(_: CGEventSource?, _: CFTimeInterval)](https://developer.apple.com/documentation/coregraphics/1408783-cgeventsourcesetlocaleventssuppr)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventSourceSetLocalEventsSuppressionInterval(_ source: CGEventSource!, _ seconds: CFTimeInterval) ``` |
| To | ``` func CGEventSourceSetLocalEventsSuppressionInterval(_ source: CGEventSource?, _ seconds: CFTimeInterval) ``` |

Modified [CGEventSourceSetPixelsPerLine(_: CGEventSource?, _: Double)](https://developer.apple.com/documentation/coregraphics/1408766-cgeventsourcesetpixelsperline)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventSourceSetPixelsPerLine(_ source: CGEventSource!, _ pixelsPerLine: Double) ``` |
| To | ``` func CGEventSourceSetPixelsPerLine(_ source: CGEventSource?, _ pixelsPerLine: Double) ``` |

Modified [CGEventSourceSetUserData(_: CGEventSource?, _: Int64)](https://developer.apple.com/documentation/coregraphics/1408779-cgeventsourcesetuserdata)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventSourceSetUserData(_ source: CGEventSource!, _ userData: Int64) ``` |
| To | ``` func CGEventSourceSetUserData(_ source: CGEventSource?, _ userData: Int64) ``` |

Modified [CGEventTapCallBack](https://developer.apple.com/documentation/coregraphics/cgeventtapcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGEventTapCallBack = CFunctionPointer<((CGEventTapProxy, CGEventType, CGEvent!, UnsafeMutablePointer<Void>) -> Unmanaged<CGEvent>!)> ``` |
| To | ``` typealias CGEventTapCallBack = (CGEventTapProxy, CGEventType, CGEvent, UnsafeMutablePointer<Void>) -> Unmanaged<CGEvent>? ``` |

Modified [CGEventTapCreate(_: CGEventTapLocation, _: CGEventTapPlacement, _: CGEventTapOptions, _: CGEventMask, _: CGEventTapCallBack?, _: UnsafeMutablePointer<Void>) -> CFMachPort?](https://developer.apple.com/documentation/coregraphics/1454426-cgeventtapcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventTapCreate(_ tap: CGEventTapLocation, _ place: CGEventTapPlacement, _ options: CGEventTapOptions, _ eventsOfInterest: CGEventMask, _ callback: CGEventTapCallBack, _ userInfo: UnsafeMutablePointer<Void>) -> Unmanaged<CFMachPort>! ``` |
| To | ``` func CGEventTapCreate(_ tap: CGEventTapLocation, _ place: CGEventTapPlacement, _ options: CGEventTapOptions, _ eventsOfInterest: CGEventMask, _ callback: CGEventTapCallBack?, _ userInfo: UnsafeMutablePointer<Void>) -> CFMachPort? ``` |

Modified [CGEventTapCreateForPSN(_: UnsafeMutablePointer<Void>, _: CGEventTapPlacement, _: CGEventTapOptions, _: CGEventMask, _: CGEventTapCallBack?, _: UnsafeMutablePointer<Void>) -> CFMachPort?](https://developer.apple.com/documentation/coregraphics/1454828-cgeventtapcreateforpsn)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventTapCreateForPSN(_ processSerialNumber: UnsafeMutablePointer<Void>, _ place: CGEventTapPlacement, _ options: CGEventTapOptions, _ eventsOfInterest: CGEventMask, _ callback: CGEventTapCallBack, _ userInfo: UnsafeMutablePointer<Void>) -> Unmanaged<CFMachPort>! ``` |
| To | ``` func CGEventTapCreateForPSN(_ processSerialNumber: UnsafeMutablePointer<Void>, _ place: CGEventTapPlacement, _ options: CGEventTapOptions, _ eventsOfInterest: CGEventMask, _ callback: CGEventTapCallBack?, _ userInfo: UnsafeMutablePointer<Void>) -> CFMachPort? ``` |

Modified [CGEventTapEnable(_: CFMachPort, _: Bool)](https://developer.apple.com/documentation/coregraphics/cgevent/1455445-tapenable)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventTapEnable(_ tap: CFMachPort!, _ enable: Bool) ``` |
| To | ``` func CGEventTapEnable(_ tap: CFMachPort, _ enable: Bool) ``` |

Modified [CGEventTapIsEnabled(_: CFMachPort) -> Bool](https://developer.apple.com/documentation/coregraphics/1456102-cgeventtapisenabled)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventTapIsEnabled(_ tap: CFMachPort!) -> Bool ``` |
| To | ``` func CGEventTapIsEnabled(_ tap: CFMachPort) -> Bool ``` |

Modified [CGEventTapPostEvent(_: CGEventTapProxy, _: CGEvent?)](https://developer.apple.com/documentation/coregraphics/1455172-cgeventtappostevent)

|  | Declaration |
| --- | --- |
| From | ``` func CGEventTapPostEvent(_ proxy: CGEventTapProxy, _ event: CGEvent!) ``` |
| To | ``` func CGEventTapPostEvent(_ proxy: CGEventTapProxy, _ event: CGEvent?) ``` |

Modified [CGFontCanCreatePostScriptSubset(_: CGFont?, _: CGFontPostScriptFormat) -> Bool](https://developer.apple.com/documentation/coregraphics/1396365-cgfontcancreatepostscriptsubset)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontCanCreatePostScriptSubset(_ font: CGFont!, _ format: CGFontPostScriptFormat) -> Bool ``` |
| To | ``` func CGFontCanCreatePostScriptSubset(_ font: CGFont?, _ format: CGFontPostScriptFormat) -> Bool ``` |

Modified [CGFontCopyFullName(_: CGFont?) -> CFString?](https://developer.apple.com/documentation/coregraphics/1396357-cgfontcopyfullname)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontCopyFullName(_ font: CGFont!) -> CFString! ``` |
| To | ``` func CGFontCopyFullName(_ font: CGFont?) -> CFString? ``` |

Modified [CGFontCopyGlyphNameForGlyph(_: CGFont?, _: CGGlyph) -> CFString?](https://developer.apple.com/documentation/coregraphics/1396349-cgfontcopyglyphnameforglyph)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontCopyGlyphNameForGlyph(_ font: CGFont!, _ glyph: CGGlyph) -> CFString! ``` |
| To | ``` func CGFontCopyGlyphNameForGlyph(_ font: CGFont?, _ glyph: CGGlyph) -> CFString? ``` |

Modified [CGFontCopyPostScriptName(_: CGFont?) -> CFString?](https://developer.apple.com/documentation/coregraphics/cgfont/1396346-postscriptname)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontCopyPostScriptName(_ font: CGFont!) -> CFString! ``` |
| To | ``` func CGFontCopyPostScriptName(_ font: CGFont?) -> CFString? ``` |

Modified [CGFontCopyTableForTag(_: CGFont?, _: UInt32) -> CFData?](https://developer.apple.com/documentation/coregraphics/cgfont/1396402-table)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontCopyTableForTag(_ font: CGFont!, _ tag: UInt32) -> CFData! ``` |
| To | ``` func CGFontCopyTableForTag(_ font: CGFont?, _ tag: UInt32) -> CFData? ``` |

Modified [CGFontCopyTableTags(_: CGFont?) -> CFArray?](https://developer.apple.com/documentation/coregraphics/1396392-cgfontcopytabletags)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontCopyTableTags(_ font: CGFont!) -> CFArray! ``` |
| To | ``` func CGFontCopyTableTags(_ font: CGFont?) -> CFArray? ``` |

Modified [CGFontCopyVariationAxes(_: CGFont?) -> CFArray?](https://developer.apple.com/documentation/coregraphics/cgfont/1396376-variationaxes)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontCopyVariationAxes(_ font: CGFont!) -> CFArray! ``` |
| To | ``` func CGFontCopyVariationAxes(_ font: CGFont?) -> CFArray? ``` |

Modified [CGFontCopyVariations(_: CGFont?) -> CFDictionary?](https://developer.apple.com/documentation/coregraphics/1396355-cgfontcopyvariations)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontCopyVariations(_ font: CGFont!) -> CFDictionary! ``` |
| To | ``` func CGFontCopyVariations(_ font: CGFont?) -> CFDictionary? ``` |

Modified [CGFontCreateCopyWithVariations(_: CGFont?, _: CFDictionary?) -> CGFont?](https://developer.apple.com/documentation/coregraphics/1396373-cgfontcreatecopywithvariations)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontCreateCopyWithVariations(_ font: CGFont!, _ variations: CFDictionary!) -> CGFont! ``` |
| To | ``` func CGFontCreateCopyWithVariations(_ font: CGFont?, _ variations: CFDictionary?) -> CGFont? ``` |

Modified [CGFontCreatePostScriptEncoding(_: CGFont?, _: UnsafePointer<CGGlyph>) -> CFData?](https://developer.apple.com/documentation/coregraphics/1396348-cgfontcreatepostscriptencoding)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontCreatePostScriptEncoding(_ font: CGFont!, _ encoding: UnsafePointer<CGGlyph>) -> CFData! ``` |
| To | ``` func CGFontCreatePostScriptEncoding(_ font: CGFont?, _ encoding: UnsafePointer<CGGlyph>) -> CFData? ``` |

Modified [CGFontCreatePostScriptSubset(_: CGFont?, _: CFString?, _: CGFontPostScriptFormat, _: UnsafePointer<CGGlyph>, _: Int, _: UnsafePointer<CGGlyph>) -> CFData?](https://developer.apple.com/documentation/coregraphics/1396324-cgfontcreatepostscriptsubset)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontCreatePostScriptSubset(_ font: CGFont!, _ subsetName: CFString!, _ format: CGFontPostScriptFormat, _ glyphs: UnsafePointer<CGGlyph>, _ count: Int, _ encoding: UnsafePointer<CGGlyph>) -> CFData! ``` |
| To | ``` func CGFontCreatePostScriptSubset(_ font: CGFont?, _ subsetName: CFString?, _ format: CGFontPostScriptFormat, _ glyphs: UnsafePointer<CGGlyph>, _ count: Int, _ encoding: UnsafePointer<CGGlyph>) -> CFData? ``` |

Modified [CGFontCreateWithDataProvider(_: CGDataProvider?) -> CGFont?](https://developer.apple.com/documentation/coregraphics/1396367-cgfontcreatewithdataprovider)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontCreateWithDataProvider(_ provider: CGDataProvider!) -> CGFont! ``` |
| To | ``` func CGFontCreateWithDataProvider(_ provider: CGDataProvider?) -> CGFont? ``` |

Modified [CGFontCreateWithFontName(_: CFString?) -> CGFont?](https://developer.apple.com/documentation/coregraphics/1396330-cgfontcreatewithfontname)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontCreateWithFontName(_ name: CFString!) -> CGFont! ``` |
| To | ``` func CGFontCreateWithFontName(_ name: CFString?) -> CGFont? ``` |

Modified [CGFontGetAscent(_: CGFont?) -> Int32](https://developer.apple.com/documentation/coregraphics/1396359-cgfontgetascent)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontGetAscent(_ font: CGFont!) -> Int32 ``` |
| To | ``` func CGFontGetAscent(_ font: CGFont?) -> Int32 ``` |

Modified [CGFontGetCapHeight(_: CGFont?) -> Int32](https://developer.apple.com/documentation/coregraphics/1396338-cgfontgetcapheight)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontGetCapHeight(_ font: CGFont!) -> Int32 ``` |
| To | ``` func CGFontGetCapHeight(_ font: CGFont?) -> Int32 ``` |

Modified [CGFontGetDescent(_: CGFont?) -> Int32](https://developer.apple.com/documentation/coregraphics/cgfont/1396351-descent)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontGetDescent(_ font: CGFont!) -> Int32 ``` |
| To | ``` func CGFontGetDescent(_ font: CGFont?) -> Int32 ``` |

Modified [CGFontGetFontBBox(_: CGFont?) -> CGRect](https://developer.apple.com/documentation/coregraphics/cgfont/1396353-fontbbox)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontGetFontBBox(_ font: CGFont!) -> CGRect ``` |
| To | ``` func CGFontGetFontBBox(_ font: CGFont?) -> CGRect ``` |

Modified [CGFontGetGlyphAdvances(_: CGFont?, _: UnsafePointer<CGGlyph>, _: Int, _: UnsafeMutablePointer<Int32>) -> Bool](https://developer.apple.com/documentation/coregraphics/1396332-cgfontgetglyphadvances)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontGetGlyphAdvances(_ font: CGFont!, _ glyphs: UnsafePointer<CGGlyph>, _ count: Int, _ advances: UnsafeMutablePointer<Int32>) -> Bool ``` |
| To | ``` func CGFontGetGlyphAdvances(_ font: CGFont?, _ glyphs: UnsafePointer<CGGlyph>, _ count: Int, _ advances: UnsafeMutablePointer<Int32>) -> Bool ``` |

Modified [CGFontGetGlyphBBoxes(_: CGFont?, _: UnsafePointer<CGGlyph>, _: Int, _: UnsafeMutablePointer<CGRect>) -> Bool](https://developer.apple.com/documentation/coregraphics/1396342-cgfontgetglyphbboxes)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontGetGlyphBBoxes(_ font: CGFont!, _ glyphs: UnsafePointer<CGGlyph>, _ count: Int, _ bboxes: UnsafeMutablePointer<CGRect>) -> Bool ``` |
| To | ``` func CGFontGetGlyphBBoxes(_ font: CGFont?, _ glyphs: UnsafePointer<CGGlyph>, _ count: Int, _ bboxes: UnsafeMutablePointer<CGRect>) -> Bool ``` |

Modified [CGFontGetGlyphWithGlyphName(_: CGFont?, _: CFString?) -> CGGlyph](https://developer.apple.com/documentation/coregraphics/cgfont/1396340-getglyphwithglyphname)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontGetGlyphWithGlyphName(_ font: CGFont!, _ name: CFString!) -> CGGlyph ``` |
| To | ``` func CGFontGetGlyphWithGlyphName(_ font: CGFont?, _ name: CFString?) -> CGGlyph ``` |

Modified [CGFontGetItalicAngle(_: CGFont?) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1396404-cgfontgetitalicangle)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontGetItalicAngle(_ font: CGFont!) -> CGFloat ``` |
| To | ``` func CGFontGetItalicAngle(_ font: CGFont?) -> CGFloat ``` |

Modified [CGFontGetLeading(_: CGFont?) -> Int32](https://developer.apple.com/documentation/coregraphics/1396390-cgfontgetleading)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontGetLeading(_ font: CGFont!) -> Int32 ``` |
| To | ``` func CGFontGetLeading(_ font: CGFont?) -> Int32 ``` |

Modified [CGFontGetNumberOfGlyphs(_: CGFont?) -> Int](https://developer.apple.com/documentation/coregraphics/1396371-cgfontgetnumberofglyphs)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontGetNumberOfGlyphs(_ font: CGFont!) -> Int ``` |
| To | ``` func CGFontGetNumberOfGlyphs(_ font: CGFont?) -> Int ``` |

Modified [CGFontGetStemV(_: CGFont?) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1396380-cgfontgetstemv)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontGetStemV(_ font: CGFont!) -> CGFloat ``` |
| To | ``` func CGFontGetStemV(_ font: CGFont?) -> CGFloat ``` |

Modified [CGFontGetUnitsPerEm(_: CGFont?) -> Int32](https://developer.apple.com/documentation/coregraphics/1396344-cgfontgetunitsperem)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontGetUnitsPerEm(_ font: CGFont!) -> Int32 ``` |
| To | ``` func CGFontGetUnitsPerEm(_ font: CGFont?) -> Int32 ``` |

Modified [CGFontGetXHeight(_: CGFont?) -> Int32](https://developer.apple.com/documentation/coregraphics/cgfont/1396410-xheight)

|  | Declaration |
| --- | --- |
| From | ``` func CGFontGetXHeight(_ font: CGFont!) -> Int32 ``` |
| To | ``` func CGFontGetXHeight(_ font: CGFont?) -> Int32 ``` |

Modified [CGFunctionCreate(_: UnsafeMutablePointer<Void>, _: Int, _: UnsafePointer<CGFloat>, _: Int, _: UnsafePointer<CGFloat>, _: UnsafePointer<CGFunctionCallbacks>) -> CGFunction?](https://developer.apple.com/documentation/coregraphics/1390862-cgfunctioncreate)

|  | Declaration |
| --- | --- |
| From | ``` func CGFunctionCreate(_ info: UnsafeMutablePointer<Void>, _ domainDimension: Int, _ domain: UnsafePointer<CGFloat>, _ rangeDimension: Int, _ range: UnsafePointer<CGFloat>, _ callbacks: UnsafePointer<CGFunctionCallbacks>) -> CGFunction! ``` |
| To | ``` func CGFunctionCreate(_ info: UnsafeMutablePointer<Void>, _ domainDimension: Int, _ domain: UnsafePointer<CGFloat>, _ rangeDimension: Int, _ range: UnsafePointer<CGFloat>, _ callbacks: UnsafePointer<CGFunctionCallbacks>) -> CGFunction? ``` |

Modified [CGFunctionEvaluateCallback](https://developer.apple.com/documentation/coregraphics/cgfunctionevaluatecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGFunctionEvaluateCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<CGFloat>, UnsafeMutablePointer<CGFloat>) -> Void)> ``` |
| To | ``` typealias CGFunctionEvaluateCallback = (UnsafeMutablePointer<Void>, UnsafePointer<CGFloat>, UnsafeMutablePointer<CGFloat>) -> Void ``` |

Modified [CGFunctionReleaseInfoCallback](https://developer.apple.com/documentation/coregraphics/cgfunctionreleaseinfocallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGFunctionReleaseInfoCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CGFunctionReleaseInfoCallback = (UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CGGradientCreateWithColorComponents(_: CGColorSpace?, _: UnsafePointer<CGFloat>, _: UnsafePointer<CGFloat>, _: Int) -> CGGradient?](https://developer.apple.com/documentation/coregraphics/1398454-cggradientcreatewithcolorcompone)

|  | Declaration |
| --- | --- |
| From | ``` func CGGradientCreateWithColorComponents(_ space: CGColorSpace!, _ components: UnsafePointer<CGFloat>, _ locations: UnsafePointer<CGFloat>, _ count: Int) -> CGGradient! ``` |
| To | ``` func CGGradientCreateWithColorComponents(_ space: CGColorSpace?, _ components: UnsafePointer<CGFloat>, _ locations: UnsafePointer<CGFloat>, _ count: Int) -> CGGradient? ``` |

Modified [CGGradientCreateWithColors(_: CGColorSpace?, _: CFArray?, _: UnsafePointer<CGFloat>) -> CGGradient?](https://developer.apple.com/documentation/coregraphics/cggradient/1398458-init)

|  | Declaration |
| --- | --- |
| From | ``` func CGGradientCreateWithColors(_ space: CGColorSpace!, _ colors: CFArray!, _ locations: UnsafePointer<CGFloat>) -> CGGradient! ``` |
| To | ``` func CGGradientCreateWithColors(_ space: CGColorSpace?, _ colors: CFArray?, _ locations: UnsafePointer<CGFloat>) -> CGGradient? ``` |

Modified [CGImageCreate(_: Int, _: Int, _: Int, _: Int, _: Int, _: CGColorSpace?, _: CGBitmapInfo, _: CGDataProvider?, _: UnsafePointer<CGFloat>, _: Bool, _: CGColorRenderingIntent) -> CGImage?](https://developer.apple.com/documentation/coregraphics/1455149-cgimagecreate)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageCreate(_ width: Int, _ height: Int, _ bitsPerComponent: Int, _ bitsPerPixel: Int, _ bytesPerRow: Int, _ space: CGColorSpace!, _ bitmapInfo: CGBitmapInfo, _ provider: CGDataProvider!, _ decode: UnsafePointer<CGFloat>, _ shouldInterpolate: Bool, _ intent: CGColorRenderingIntent) -> CGImage! ``` |
| To | ``` func CGImageCreate(_ width: Int, _ height: Int, _ bitsPerComponent: Int, _ bitsPerPixel: Int, _ bytesPerRow: Int, _ space: CGColorSpace?, _ bitmapInfo: CGBitmapInfo, _ provider: CGDataProvider?, _ decode: UnsafePointer<CGFloat>, _ shouldInterpolate: Bool, _ intent: CGColorRenderingIntent) -> CGImage? ``` |

Modified [CGImageCreateCopy(_: CGImage?) -> CGImage?](https://developer.apple.com/documentation/coregraphics/1455615-cgimagecreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageCreateCopy(_ image: CGImage!) -> CGImage! ``` |
| To | ``` func CGImageCreateCopy(_ image: CGImage?) -> CGImage? ``` |

Modified [CGImageCreateCopyWithColorSpace(_: CGImage?, _: CGColorSpace?) -> CGImage?](https://developer.apple.com/documentation/coregraphics/cgimage/1455355-copy)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageCreateCopyWithColorSpace(_ image: CGImage!, _ space: CGColorSpace!) -> CGImage! ``` |
| To | ``` func CGImageCreateCopyWithColorSpace(_ image: CGImage?, _ space: CGColorSpace?) -> CGImage? ``` |

Modified [CGImageCreateWithImageInRect(_: CGImage?, _: CGRect) -> CGImage?](https://developer.apple.com/documentation/coregraphics/1454683-cgimagecreatewithimageinrect)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageCreateWithImageInRect(_ image: CGImage!, _ rect: CGRect) -> CGImage! ``` |
| To | ``` func CGImageCreateWithImageInRect(_ image: CGImage?, _ rect: CGRect) -> CGImage? ``` |

Modified [CGImageCreateWithJPEGDataProvider(_: CGDataProvider?, _: UnsafePointer<CGFloat>, _: Bool, _: CGColorRenderingIntent) -> CGImage?](https://developer.apple.com/documentation/coregraphics/1454920-cgimagecreatewithjpegdataprovide)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageCreateWithJPEGDataProvider(_ source: CGDataProvider!, _ decode: UnsafePointer<CGFloat>, _ shouldInterpolate: Bool, _ intent: CGColorRenderingIntent) -> CGImage! ``` |
| To | ``` func CGImageCreateWithJPEGDataProvider(_ source: CGDataProvider?, _ decode: UnsafePointer<CGFloat>, _ shouldInterpolate: Bool, _ intent: CGColorRenderingIntent) -> CGImage? ``` |

Modified [CGImageCreateWithMask(_: CGImage?, _: CGImage?) -> CGImage?](https://developer.apple.com/documentation/coregraphics/1456337-cgimagecreatewithmask)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageCreateWithMask(_ image: CGImage!, _ mask: CGImage!) -> CGImage! ``` |
| To | ``` func CGImageCreateWithMask(_ image: CGImage?, _ mask: CGImage?) -> CGImage? ``` |

Modified [CGImageCreateWithMaskingColors(_: CGImage?, _: UnsafePointer<CGFloat>) -> CGImage?](https://developer.apple.com/documentation/coregraphics/1454358-cgimagecreatewithmaskingcolors)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageCreateWithMaskingColors(_ image: CGImage!, _ components: UnsafePointer<CGFloat>) -> CGImage! ``` |
| To | ``` func CGImageCreateWithMaskingColors(_ image: CGImage?, _ components: UnsafePointer<CGFloat>) -> CGImage? ``` |

Modified [CGImageCreateWithPNGDataProvider(_: CGDataProvider?, _: UnsafePointer<CGFloat>, _: Bool, _: CGColorRenderingIntent) -> CGImage?](https://developer.apple.com/documentation/coregraphics/1454993-cgimagecreatewithpngdataprovider)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageCreateWithPNGDataProvider(_ source: CGDataProvider!, _ decode: UnsafePointer<CGFloat>, _ shouldInterpolate: Bool, _ intent: CGColorRenderingIntent) -> CGImage! ``` |
| To | ``` func CGImageCreateWithPNGDataProvider(_ source: CGDataProvider?, _ decode: UnsafePointer<CGFloat>, _ shouldInterpolate: Bool, _ intent: CGColorRenderingIntent) -> CGImage? ``` |

Modified [CGImageGetAlphaInfo(_: CGImage?) -> CGImageAlphaInfo](https://developer.apple.com/documentation/coregraphics/cgimage/1455401-alphainfo)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageGetAlphaInfo(_ image: CGImage!) -> CGImageAlphaInfo ``` |
| To | ``` func CGImageGetAlphaInfo(_ image: CGImage?) -> CGImageAlphaInfo ``` |

Modified [CGImageGetBitmapInfo(_: CGImage?) -> CGBitmapInfo](https://developer.apple.com/documentation/coregraphics/cgimage/1454200-bitmapinfo)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageGetBitmapInfo(_ image: CGImage!) -> CGBitmapInfo ``` |
| To | ``` func CGImageGetBitmapInfo(_ image: CGImage?) -> CGBitmapInfo ``` |

Modified [CGImageGetBitsPerComponent(_: CGImage?) -> Int](https://developer.apple.com/documentation/coregraphics/1454980-cgimagegetbitspercomponent)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageGetBitsPerComponent(_ image: CGImage!) -> Int ``` |
| To | ``` func CGImageGetBitsPerComponent(_ image: CGImage?) -> Int ``` |

Modified [CGImageGetBitsPerPixel(_: CGImage?) -> Int](https://developer.apple.com/documentation/coregraphics/1454599-cgimagegetbitsperpixel)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageGetBitsPerPixel(_ image: CGImage!) -> Int ``` |
| To | ``` func CGImageGetBitsPerPixel(_ image: CGImage?) -> Int ``` |

Modified [CGImageGetBytesPerRow(_: CGImage?) -> Int](https://developer.apple.com/documentation/coregraphics/cgimage/1455425-bytesperrow)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageGetBytesPerRow(_ image: CGImage!) -> Int ``` |
| To | ``` func CGImageGetBytesPerRow(_ image: CGImage?) -> Int ``` |

Modified [CGImageGetColorSpace(_: CGImage?) -> CGColorSpace?](https://developer.apple.com/documentation/coregraphics/1454858-cgimagegetcolorspace)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageGetColorSpace(_ image: CGImage!) -> CGColorSpace! ``` |
| To | ``` func CGImageGetColorSpace(_ image: CGImage?) -> CGColorSpace? ``` |

Modified [CGImageGetDataProvider(_: CGImage?) -> CGDataProvider?](https://developer.apple.com/documentation/coregraphics/1455260-cgimagegetdataprovider)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageGetDataProvider(_ image: CGImage!) -> CGDataProvider! ``` |
| To | ``` func CGImageGetDataProvider(_ image: CGImage?) -> CGDataProvider? ``` |

Modified [CGImageGetDecode(_: CGImage?) -> UnsafePointer<CGFloat>](https://developer.apple.com/documentation/coregraphics/1454575-cgimagegetdecode)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageGetDecode(_ image: CGImage!) -> UnsafePointer<CGFloat> ``` |
| To | ``` func CGImageGetDecode(_ image: CGImage?) -> UnsafePointer<CGFloat> ``` |

Modified [CGImageGetHeight(_: CGImage?) -> Int](https://developer.apple.com/documentation/coregraphics/1455829-cgimagegetheight)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageGetHeight(_ image: CGImage!) -> Int ``` |
| To | ``` func CGImageGetHeight(_ image: CGImage?) -> Int ``` |

Modified [CGImageGetRenderingIntent(_: CGImage?) -> CGColorRenderingIntent](https://developer.apple.com/documentation/coregraphics/1456350-cgimagegetrenderingintent)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageGetRenderingIntent(_ image: CGImage!) -> CGColorRenderingIntent ``` |
| To | ``` func CGImageGetRenderingIntent(_ image: CGImage?) -> CGColorRenderingIntent ``` |

Modified [CGImageGetShouldInterpolate(_: CGImage?) -> Bool](https://developer.apple.com/documentation/coregraphics/1455363-cgimagegetshouldinterpolate)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageGetShouldInterpolate(_ image: CGImage!) -> Bool ``` |
| To | ``` func CGImageGetShouldInterpolate(_ image: CGImage?) -> Bool ``` |

Modified [CGImageGetWidth(_: CGImage?) -> Int](https://developer.apple.com/documentation/coregraphics/1456148-cgimagegetwidth)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageGetWidth(_ image: CGImage!) -> Int ``` |
| To | ``` func CGImageGetWidth(_ image: CGImage?) -> Int ``` |

Modified [CGImageIsMask(_: CGImage?) -> Bool](https://developer.apple.com/documentation/coregraphics/cgimage/1454229-ismask)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageIsMask(_ image: CGImage!) -> Bool ``` |
| To | ``` func CGImageIsMask(_ image: CGImage?) -> Bool ``` |

Modified [CGImageMaskCreate(_: Int, _: Int, _: Int, _: Int, _: Int, _: CGDataProvider?, _: UnsafePointer<CGFloat>, _: Bool) -> CGImage?](https://developer.apple.com/documentation/coregraphics/1455089-cgimagemaskcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMaskCreate(_ width: Int, _ height: Int, _ bitsPerComponent: Int, _ bitsPerPixel: Int, _ bytesPerRow: Int, _ provider: CGDataProvider!, _ decode: UnsafePointer<CGFloat>, _ shouldInterpolate: Bool) -> CGImage! ``` |
| To | ``` func CGImageMaskCreate(_ width: Int, _ height: Int, _ bitsPerComponent: Int, _ bitsPerPixel: Int, _ bytesPerRow: Int, _ provider: CGDataProvider?, _ decode: UnsafePointer<CGFloat>, _ shouldInterpolate: Bool) -> CGImage? ``` |

Modified [CGLayerCreateWithContext(_: CGContext?, _: CGSize, _: CFDictionary?) -> CGLayer?](https://developer.apple.com/documentation/coregraphics/cglayer/1450892-init)

|  | Declaration |
| --- | --- |
| From | ``` func CGLayerCreateWithContext(_ context: CGContext!, _ size: CGSize, _ auxiliaryInfo: CFDictionary!) -> CGLayer! ``` |
| To | ``` func CGLayerCreateWithContext(_ context: CGContext?, _ size: CGSize, _ auxiliaryInfo: CFDictionary?) -> CGLayer? ``` |

Modified [CGLayerGetContext(_: CGLayer?) -> CGContext?](https://developer.apple.com/documentation/coregraphics/1450902-cglayergetcontext)

|  | Declaration |
| --- | --- |
| From | ``` func CGLayerGetContext(_ layer: CGLayer!) -> CGContext! ``` |
| To | ``` func CGLayerGetContext(_ layer: CGLayer?) -> CGContext? ``` |

Modified [CGLayerGetSize(_: CGLayer?) -> CGSize](https://developer.apple.com/documentation/coregraphics/1450890-cglayergetsize)

|  | Declaration |
| --- | --- |
| From | ``` func CGLayerGetSize(_ layer: CGLayer!) -> CGSize ``` |
| To | ``` func CGLayerGetSize(_ layer: CGLayer?) -> CGSize ``` |

Modified [CGPathAddArc(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: Bool)](https://developer.apple.com/documentation/coregraphics/1411147-cgpathaddarc)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathAddArc(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ x: CGFloat, _ y: CGFloat, _ radius: CGFloat, _ startAngle: CGFloat, _ endAngle: CGFloat, _ clockwise: Bool) ``` |
| To | ``` func CGPathAddArc(_ path: CGMutablePath?, _ m: UnsafePointer<CGAffineTransform>, _ x: CGFloat, _ y: CGFloat, _ radius: CGFloat, _ startAngle: CGFloat, _ endAngle: CGFloat, _ clockwise: Bool) ``` |

Modified [CGPathAddArcToPoint(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1411173-cgpathaddarctopoint)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathAddArcToPoint(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ x1: CGFloat, _ y1: CGFloat, _ x2: CGFloat, _ y2: CGFloat, _ radius: CGFloat) ``` |
| To | ``` func CGPathAddArcToPoint(_ path: CGMutablePath?, _ m: UnsafePointer<CGAffineTransform>, _ x1: CGFloat, _ y1: CGFloat, _ x2: CGFloat, _ y2: CGFloat, _ radius: CGFloat) ``` |

Modified [CGPathAddCurveToPoint(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1411212-cgpathaddcurvetopoint)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathAddCurveToPoint(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ cp1x: CGFloat, _ cp1y: CGFloat, _ cp2x: CGFloat, _ cp2y: CGFloat, _ x: CGFloat, _ y: CGFloat) ``` |
| To | ``` func CGPathAddCurveToPoint(_ path: CGMutablePath?, _ m: UnsafePointer<CGAffineTransform>, _ cp1x: CGFloat, _ cp1y: CGFloat, _ cp2x: CGFloat, _ cp2y: CGFloat, _ x: CGFloat, _ y: CGFloat) ``` |

Modified [CGPathAddEllipseInRect(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGRect)](https://developer.apple.com/documentation/coregraphics/1411222-cgpathaddellipseinrect)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathAddEllipseInRect(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ rect: CGRect) ``` |
| To | ``` func CGPathAddEllipseInRect(_ path: CGMutablePath?, _ m: UnsafePointer<CGAffineTransform>, _ rect: CGRect) ``` |

Modified [CGPathAddLines(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: UnsafePointer<CGPoint>, _: Int)](https://developer.apple.com/documentation/coregraphics/1411171-cgpathaddlines)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathAddLines(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ points: UnsafePointer<CGPoint>, _ count: Int) ``` |
| To | ``` func CGPathAddLines(_ path: CGMutablePath?, _ m: UnsafePointer<CGAffineTransform>, _ points: UnsafePointer<CGPoint>, _ count: Int) ``` |

Modified [CGPathAddLineToPoint(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1411138-cgpathaddlinetopoint)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathAddLineToPoint(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ x: CGFloat, _ y: CGFloat) ``` |
| To | ``` func CGPathAddLineToPoint(_ path: CGMutablePath?, _ m: UnsafePointer<CGAffineTransform>, _ x: CGFloat, _ y: CGFloat) ``` |

Modified [CGPathAddPath(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGPath?)](https://developer.apple.com/documentation/coregraphics/1411201-cgpathaddpath)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathAddPath(_ path1: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ path2: CGPath!) ``` |
| To | ``` func CGPathAddPath(_ path1: CGMutablePath?, _ m: UnsafePointer<CGAffineTransform>, _ path2: CGPath?) ``` |

Modified [CGPathAddQuadCurveToPoint(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1411157-cgpathaddquadcurvetopoint)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathAddQuadCurveToPoint(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ cpx: CGFloat, _ cpy: CGFloat, _ x: CGFloat, _ y: CGFloat) ``` |
| To | ``` func CGPathAddQuadCurveToPoint(_ path: CGMutablePath?, _ m: UnsafePointer<CGAffineTransform>, _ cpx: CGFloat, _ cpy: CGFloat, _ x: CGFloat, _ y: CGFloat) ``` |

Modified [CGPathAddRect(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGRect)](https://developer.apple.com/documentation/coregraphics/1411144-cgpathaddrect)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathAddRect(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ rect: CGRect) ``` |
| To | ``` func CGPathAddRect(_ path: CGMutablePath?, _ m: UnsafePointer<CGAffineTransform>, _ rect: CGRect) ``` |

Modified [CGPathAddRects(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: UnsafePointer<CGRect>, _: Int)](https://developer.apple.com/documentation/coregraphics/1411153-cgpathaddrects)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathAddRects(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ rects: UnsafePointer<CGRect>, _ count: Int) ``` |
| To | ``` func CGPathAddRects(_ path: CGMutablePath?, _ m: UnsafePointer<CGAffineTransform>, _ rects: UnsafePointer<CGRect>, _ count: Int) ``` |

Modified [CGPathAddRelativeArc(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1411136-cgpathaddrelativearc)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathAddRelativeArc(_ path: CGMutablePath!, _ matrix: UnsafePointer<CGAffineTransform>, _ x: CGFloat, _ y: CGFloat, _ radius: CGFloat, _ startAngle: CGFloat, _ delta: CGFloat) ``` |
| To | ``` func CGPathAddRelativeArc(_ path: CGMutablePath?, _ matrix: UnsafePointer<CGAffineTransform>, _ x: CGFloat, _ y: CGFloat, _ radius: CGFloat, _ startAngle: CGFloat, _ delta: CGFloat) ``` |

Modified [CGPathAddRoundedRect(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGRect, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1411124-cgpathaddroundedrect)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathAddRoundedRect(_ path: CGMutablePath!, _ transform: UnsafePointer<CGAffineTransform>, _ rect: CGRect, _ cornerWidth: CGFloat, _ cornerHeight: CGFloat) ``` |
| To | ``` func CGPathAddRoundedRect(_ path: CGMutablePath?, _ transform: UnsafePointer<CGAffineTransform>, _ rect: CGRect, _ cornerWidth: CGFloat, _ cornerHeight: CGFloat) ``` |

Modified [CGPathApplierFunction](https://developer.apple.com/documentation/coregraphics/cgpathapplierfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPathApplierFunction = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<CGPathElement>) -> Void)> ``` |
| To | ``` typealias CGPathApplierFunction = (UnsafeMutablePointer<Void>, UnsafePointer<CGPathElement>) -> Void ``` |

Modified [CGPathApply(_: CGPath?, _: UnsafeMutablePointer<Void>, _: CGPathApplierFunction?)](https://developer.apple.com/documentation/coregraphics/1411203-cgpathapply)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathApply(_ path: CGPath!, _ info: UnsafeMutablePointer<Void>, _ function: CGPathApplierFunction) ``` |
| To | ``` func CGPathApply(_ path: CGPath?, _ info: UnsafeMutablePointer<Void>, _ function: CGPathApplierFunction?) ``` |

Modified [CGPathCloseSubpath(_: CGMutablePath?)](https://developer.apple.com/documentation/coregraphics/cgmutablepath/1411188-closesubpath)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathCloseSubpath(_ path: CGMutablePath!) ``` |
| To | ``` func CGPathCloseSubpath(_ path: CGMutablePath?) ``` |

Modified [CGPathContainsPoint(_: CGPath?, _: UnsafePointer<CGAffineTransform>, _: CGPoint, _: Bool) -> Bool](https://developer.apple.com/documentation/coregraphics/1411175-cgpathcontainspoint)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathContainsPoint(_ path: CGPath!, _ m: UnsafePointer<CGAffineTransform>, _ point: CGPoint, _ eoFill: Bool) -> Bool ``` |
| To | ``` func CGPathContainsPoint(_ path: CGPath?, _ m: UnsafePointer<CGAffineTransform>, _ point: CGPoint, _ eoFill: Bool) -> Bool ``` |

Modified [CGPathCreateCopy(_: CGPath?) -> CGPath?](https://developer.apple.com/documentation/coregraphics/1411211-cgpathcreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathCreateCopy(_ path: CGPath!) -> CGPath! ``` |
| To | ``` func CGPathCreateCopy(_ path: CGPath?) -> CGPath? ``` |

Modified [CGPathCreateCopyByDashingPath(_: CGPath?, _: UnsafePointer<CGAffineTransform>, _: CGFloat, _: UnsafePointer<CGFloat>, _: Int) -> CGPath?](https://developer.apple.com/documentation/coregraphics/1411134-cgpathcreatecopybydashingpath)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathCreateCopyByDashingPath(_ path: CGPath!, _ transform: UnsafePointer<CGAffineTransform>, _ phase: CGFloat, _ lengths: UnsafePointer<CGFloat>, _ count: Int) -> CGPath! ``` |
| To | ``` func CGPathCreateCopyByDashingPath(_ path: CGPath?, _ transform: UnsafePointer<CGAffineTransform>, _ phase: CGFloat, _ lengths: UnsafePointer<CGFloat>, _ count: Int) -> CGPath? ``` |

Modified [CGPathCreateCopyByStrokingPath(_: CGPath?, _: UnsafePointer<CGAffineTransform>, _: CGFloat, _: CGLineCap, _: CGLineJoin, _: CGFloat) -> CGPath?](https://developer.apple.com/documentation/coregraphics/1411128-cgpathcreatecopybystrokingpath)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathCreateCopyByStrokingPath(_ path: CGPath!, _ transform: UnsafePointer<CGAffineTransform>, _ lineWidth: CGFloat, _ lineCap: CGLineCap, _ lineJoin: CGLineJoin, _ miterLimit: CGFloat) -> CGPath! ``` |
| To | ``` func CGPathCreateCopyByStrokingPath(_ path: CGPath?, _ transform: UnsafePointer<CGAffineTransform>, _ lineWidth: CGFloat, _ lineCap: CGLineCap, _ lineJoin: CGLineJoin, _ miterLimit: CGFloat) -> CGPath? ``` |

Modified [CGPathCreateCopyByTransformingPath(_: CGPath?, _: UnsafePointer<CGAffineTransform>) -> CGPath?](https://developer.apple.com/documentation/coregraphics/1411161-cgpathcreatecopybytransformingpa)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathCreateCopyByTransformingPath(_ path: CGPath!, _ transform: UnsafePointer<CGAffineTransform>) -> CGPath! ``` |
| To | ``` func CGPathCreateCopyByTransformingPath(_ path: CGPath?, _ transform: UnsafePointer<CGAffineTransform>) -> CGPath? ``` |

Modified [CGPathCreateMutable() -> CGMutablePath](https://developer.apple.com/documentation/coregraphics/cgmutablepath/1411209-init)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathCreateMutable() -> CGMutablePath! ``` |
| To | ``` func CGPathCreateMutable() -> CGMutablePath ``` |

Modified [CGPathCreateMutableCopy(_: CGPath?) -> CGMutablePath?](https://developer.apple.com/documentation/coregraphics/1411196-cgpathcreatemutablecopy)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathCreateMutableCopy(_ path: CGPath!) -> CGMutablePath! ``` |
| To | ``` func CGPathCreateMutableCopy(_ path: CGPath?) -> CGMutablePath? ``` |

Modified [CGPathCreateMutableCopyByTransformingPath(_: CGPath?, _: UnsafePointer<CGAffineTransform>) -> CGMutablePath?](https://developer.apple.com/documentation/coregraphics/cgpath/1411150-mutablecopy)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathCreateMutableCopyByTransformingPath(_ path: CGPath!, _ transform: UnsafePointer<CGAffineTransform>) -> CGMutablePath! ``` |
| To | ``` func CGPathCreateMutableCopyByTransformingPath(_ path: CGPath?, _ transform: UnsafePointer<CGAffineTransform>) -> CGMutablePath? ``` |

Modified [CGPathCreateWithEllipseInRect(_: CGRect, _: UnsafePointer<CGAffineTransform>) -> CGPath](https://developer.apple.com/documentation/coregraphics/1411177-cgpathcreatewithellipseinrect)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathCreateWithEllipseInRect(_ rect: CGRect, _ transform: UnsafePointer<CGAffineTransform>) -> CGPath! ``` |
| To | ``` func CGPathCreateWithEllipseInRect(_ rect: CGRect, _ transform: UnsafePointer<CGAffineTransform>) -> CGPath ``` |

Modified [CGPathCreateWithRect(_: CGRect, _: UnsafePointer<CGAffineTransform>) -> CGPath](https://developer.apple.com/documentation/coregraphics/cgpath/1411155-init)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathCreateWithRect(_ rect: CGRect, _ transform: UnsafePointer<CGAffineTransform>) -> CGPath! ``` |
| To | ``` func CGPathCreateWithRect(_ rect: CGRect, _ transform: UnsafePointer<CGAffineTransform>) -> CGPath ``` |

Modified [CGPathCreateWithRoundedRect(_: CGRect, _: CGFloat, _: CGFloat, _: UnsafePointer<CGAffineTransform>) -> CGPath](https://developer.apple.com/documentation/coregraphics/1411218-cgpathcreatewithroundedrect)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathCreateWithRoundedRect(_ rect: CGRect, _ cornerWidth: CGFloat, _ cornerHeight: CGFloat, _ transform: UnsafePointer<CGAffineTransform>) -> CGPath! ``` |
| To | ``` func CGPathCreateWithRoundedRect(_ rect: CGRect, _ cornerWidth: CGFloat, _ cornerHeight: CGFloat, _ transform: UnsafePointer<CGAffineTransform>) -> CGPath ``` |

Modified [CGPathEqualToPath(_: CGPath?, _: CGPath?) -> Bool](https://developer.apple.com/documentation/coregraphics/1411167-cgpathequaltopath)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathEqualToPath(_ path1: CGPath!, _ path2: CGPath!) -> Bool ``` |
| To | ``` func CGPathEqualToPath(_ path1: CGPath?, _ path2: CGPath?) -> Bool ``` |

Modified [CGPathGetBoundingBox(_: CGPath?) -> CGRect](https://developer.apple.com/documentation/coregraphics/1411165-cgpathgetboundingbox)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathGetBoundingBox(_ path: CGPath!) -> CGRect ``` |
| To | ``` func CGPathGetBoundingBox(_ path: CGPath?) -> CGRect ``` |

Modified [CGPathGetCurrentPoint(_: CGPath?) -> CGPoint](https://developer.apple.com/documentation/coregraphics/1411132-cgpathgetcurrentpoint)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathGetCurrentPoint(_ path: CGPath!) -> CGPoint ``` |
| To | ``` func CGPathGetCurrentPoint(_ path: CGPath?) -> CGPoint ``` |

Modified [CGPathGetPathBoundingBox(_: CGPath?) -> CGRect](https://developer.apple.com/documentation/coregraphics/1411200-cgpathgetpathboundingbox)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathGetPathBoundingBox(_ path: CGPath!) -> CGRect ``` |
| To | ``` func CGPathGetPathBoundingBox(_ path: CGPath?) -> CGRect ``` |

Modified [CGPathIsEmpty(_: CGPath?) -> Bool](https://developer.apple.com/documentation/coregraphics/1411149-cgpathisempty)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathIsEmpty(_ path: CGPath!) -> Bool ``` |
| To | ``` func CGPathIsEmpty(_ path: CGPath?) -> Bool ``` |

Modified [CGPathIsRect(_: CGPath?, _: UnsafeMutablePointer<CGRect>) -> Bool](https://developer.apple.com/documentation/coregraphics/1411163-cgpathisrect)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathIsRect(_ path: CGPath!, _ rect: UnsafeMutablePointer<CGRect>) -> Bool ``` |
| To | ``` func CGPathIsRect(_ path: CGPath?, _ rect: UnsafeMutablePointer<CGRect>) -> Bool ``` |

Modified [CGPathMoveToPoint(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1411146-cgpathmovetopoint)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathMoveToPoint(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ x: CGFloat, _ y: CGFloat) ``` |
| To | ``` func CGPathMoveToPoint(_ path: CGMutablePath?, _ m: UnsafePointer<CGAffineTransform>, _ x: CGFloat, _ y: CGFloat) ``` |

Modified [CGPatternCreate(_: UnsafeMutablePointer<Void>, _: CGRect, _: CGAffineTransform, _: CGFloat, _: CGFloat, _: CGPatternTiling, _: Bool, _: UnsafePointer<CGPatternCallbacks>) -> CGPattern?](https://developer.apple.com/documentation/coregraphics/1454997-cgpatterncreate)

|  | Declaration |
| --- | --- |
| From | ``` func CGPatternCreate(_ info: UnsafeMutablePointer<Void>, _ bounds: CGRect, _ matrix: CGAffineTransform, _ xStep: CGFloat, _ yStep: CGFloat, _ tiling: CGPatternTiling, _ isColored: Bool, _ callbacks: UnsafePointer<CGPatternCallbacks>) -> CGPattern! ``` |
| To | ``` func CGPatternCreate(_ info: UnsafeMutablePointer<Void>, _ bounds: CGRect, _ matrix: CGAffineTransform, _ xStep: CGFloat, _ yStep: CGFloat, _ tiling: CGPatternTiling, _ isColored: Bool, _ callbacks: UnsafePointer<CGPatternCallbacks>) -> CGPattern? ``` |

Modified [CGPatternDrawPatternCallback](https://developer.apple.com/documentation/coregraphics/cgpatterndrawpatterncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPatternDrawPatternCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, CGContext!) -> Void)> ``` |
| To | ``` typealias CGPatternDrawPatternCallback = (UnsafeMutablePointer<Void>, CGContext?) -> Void ``` |

Modified [CGPatternReleaseInfoCallback](https://developer.apple.com/documentation/coregraphics/cgpatternreleaseinfocallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPatternReleaseInfoCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CGPatternReleaseInfoCallback = (UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CGPDFContextAddDestinationAtPoint(_: CGContext?, _: CFString, _: CGPoint)](https://developer.apple.com/documentation/coregraphics/1455424-cgpdfcontextadddestinationatpoin)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFContextAddDestinationAtPoint(_ context: CGContext!, _ name: CFString!, _ point: CGPoint) ``` |
| To | ``` func CGPDFContextAddDestinationAtPoint(_ context: CGContext?, _ name: CFString, _ point: CGPoint) ``` |

Modified [CGPDFContextAddDocumentMetadata(_: CGContext?, _: CFData?)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456026-adddocumentmetadata)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFContextAddDocumentMetadata(_ context: CGContext!, _ metadata: CFData!) ``` |
| To | ``` func CGPDFContextAddDocumentMetadata(_ context: CGContext?, _ metadata: CFData?) ``` |

Modified [CGPDFContextBeginPage(_: CGContext?, _: CFDictionary?)](https://developer.apple.com/documentation/coregraphics/1456578-cgpdfcontextbeginpage)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFContextBeginPage(_ context: CGContext!, _ pageInfo: CFDictionary!) ``` |
| To | ``` func CGPDFContextBeginPage(_ context: CGContext?, _ pageInfo: CFDictionary?) ``` |

Modified [CGPDFContextClose(_: CGContext?)](https://developer.apple.com/documentation/coregraphics/1454306-cgpdfcontextclose)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFContextClose(_ context: CGContext!) ``` |
| To | ``` func CGPDFContextClose(_ context: CGContext?) ``` |

Modified [CGPDFContextCreate(_: CGDataConsumer?, _: UnsafePointer<CGRect>, _: CFDictionary?) -> CGContext?](https://developer.apple.com/documentation/coregraphics/cgcontext/1454204-init)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFContextCreate(_ consumer: CGDataConsumer!, _ mediaBox: UnsafePointer<CGRect>, _ auxiliaryInfo: CFDictionary!) -> CGContext! ``` |
| To | ``` func CGPDFContextCreate(_ consumer: CGDataConsumer?, _ mediaBox: UnsafePointer<CGRect>, _ auxiliaryInfo: CFDictionary?) -> CGContext? ``` |

Modified [CGPDFContextCreateWithURL(_: CFURL?, _: UnsafePointer<CGRect>, _: CFDictionary?) -> CGContext?](https://developer.apple.com/documentation/coregraphics/cgcontext/1456290-init)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFContextCreateWithURL(_ url: CFURL!, _ mediaBox: UnsafePointer<CGRect>, _ auxiliaryInfo: CFDictionary!) -> CGContext! ``` |
| To | ``` func CGPDFContextCreateWithURL(_ url: CFURL?, _ mediaBox: UnsafePointer<CGRect>, _ auxiliaryInfo: CFDictionary?) -> CGContext? ``` |

Modified [CGPDFContextEndPage(_: CGContext?)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456122-endpdfpage)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFContextEndPage(_ context: CGContext!) ``` |
| To | ``` func CGPDFContextEndPage(_ context: CGContext?) ``` |

Modified [CGPDFContextSetDestinationForRect(_: CGContext?, _: CFString, _: CGRect)](https://developer.apple.com/documentation/coregraphics/1456459-cgpdfcontextsetdestinationforrec)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFContextSetDestinationForRect(_ context: CGContext!, _ name: CFString!, _ rect: CGRect) ``` |
| To | ``` func CGPDFContextSetDestinationForRect(_ context: CGContext?, _ name: CFString, _ rect: CGRect) ``` |

Modified [CGPDFContextSetURLForRect(_: CGContext?, _: CFURL, _: CGRect)](https://developer.apple.com/documentation/coregraphics/1455622-cgpdfcontextseturlforrect)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFContextSetURLForRect(_ context: CGContext!, _ url: CFURL!, _ rect: CGRect) ``` |
| To | ``` func CGPDFContextSetURLForRect(_ context: CGContext?, _ url: CFURL, _ rect: CGRect) ``` |

Modified [CGPDFDictionaryApplierFunction](https://developer.apple.com/documentation/coregraphics/cgpdfdictionaryapplierfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFDictionaryApplierFunction = CFunctionPointer<((UnsafePointer<Int8>, CGPDFObjectRef, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CGPDFDictionaryApplierFunction = (UnsafePointer<Int8>, CGPDFObjectRef, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CGPDFDictionaryApplyFunction(_: CGPDFDictionaryRef, _: CGPDFDictionaryApplierFunction?, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/coregraphics/1430216-cgpdfdictionaryapplyfunction)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDictionaryApplyFunction(_ dict: CGPDFDictionaryRef, _ function: CGPDFDictionaryApplierFunction, _ info: UnsafeMutablePointer<Void>) ``` |
| To | ``` func CGPDFDictionaryApplyFunction(_ dict: CGPDFDictionaryRef, _ function: CGPDFDictionaryApplierFunction?, _ info: UnsafeMutablePointer<Void>) ``` |

Modified [CGPDFDocumentAllowsCopying(_: CGPDFDocument?) -> Bool](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/1402588-allowscopying)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDocumentAllowsCopying(_ document: CGPDFDocument!) -> Bool ``` |
| To | ``` func CGPDFDocumentAllowsCopying(_ document: CGPDFDocument?) -> Bool ``` |

Modified [CGPDFDocumentAllowsPrinting(_: CGPDFDocument?) -> Bool](https://developer.apple.com/documentation/coregraphics/1402594-cgpdfdocumentallowsprinting)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDocumentAllowsPrinting(_ document: CGPDFDocument!) -> Bool ``` |
| To | ``` func CGPDFDocumentAllowsPrinting(_ document: CGPDFDocument?) -> Bool ``` |

Modified [CGPDFDocumentCreateWithProvider(_: CGDataProvider?) -> CGPDFDocument?](https://developer.apple.com/documentation/coregraphics/1402603-cgpdfdocumentcreatewithprovider)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDocumentCreateWithProvider(_ provider: CGDataProvider!) -> CGPDFDocument! ``` |
| To | ``` func CGPDFDocumentCreateWithProvider(_ provider: CGDataProvider?) -> CGPDFDocument? ``` |

Modified [CGPDFDocumentCreateWithURL(_: CFURL?) -> CGPDFDocument?](https://developer.apple.com/documentation/coregraphics/1402585-cgpdfdocumentcreatewithurl)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDocumentCreateWithURL(_ url: CFURL!) -> CGPDFDocument! ``` |
| To | ``` func CGPDFDocumentCreateWithURL(_ url: CFURL?) -> CGPDFDocument? ``` |

Modified [CGPDFDocumentGetCatalog(_: CGPDFDocument?) -> CGPDFDictionaryRef](https://developer.apple.com/documentation/coregraphics/1402606-cgpdfdocumentgetcatalog)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDocumentGetCatalog(_ document: CGPDFDocument!) -> CGPDFDictionaryRef ``` |
| To | ``` func CGPDFDocumentGetCatalog(_ document: CGPDFDocument?) -> CGPDFDictionaryRef ``` |

Modified [CGPDFDocumentGetID(_: CGPDFDocument?) -> CGPDFArrayRef](https://developer.apple.com/documentation/coregraphics/1402600-cgpdfdocumentgetid)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDocumentGetID(_ document: CGPDFDocument!) -> CGPDFArrayRef ``` |
| To | ``` func CGPDFDocumentGetID(_ document: CGPDFDocument?) -> CGPDFArrayRef ``` |

Modified [CGPDFDocumentGetInfo(_: CGPDFDocument?) -> CGPDFDictionaryRef](https://developer.apple.com/documentation/coregraphics/1402589-cgpdfdocumentgetinfo)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDocumentGetInfo(_ document: CGPDFDocument!) -> CGPDFDictionaryRef ``` |
| To | ``` func CGPDFDocumentGetInfo(_ document: CGPDFDocument?) -> CGPDFDictionaryRef ``` |

Modified [CGPDFDocumentGetNumberOfPages(_: CGPDFDocument?) -> Int](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/1402595-numberofpages)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDocumentGetNumberOfPages(_ document: CGPDFDocument!) -> Int ``` |
| To | ``` func CGPDFDocumentGetNumberOfPages(_ document: CGPDFDocument?) -> Int ``` |

Modified [CGPDFDocumentGetPage(_: CGPDFDocument?, _: Int) -> CGPDFPage?](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/1402586-page)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDocumentGetPage(_ document: CGPDFDocument!, _ pageNumber: Int) -> CGPDFPage! ``` |
| To | ``` func CGPDFDocumentGetPage(_ document: CGPDFDocument?, _ pageNumber: Int) -> CGPDFPage? ``` |

Modified [CGPDFDocumentGetVersion(_: CGPDFDocument?, _: UnsafeMutablePointer<Int32>, _: UnsafeMutablePointer<Int32>)](https://developer.apple.com/documentation/coregraphics/1402604-cgpdfdocumentgetversion)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDocumentGetVersion(_ document: CGPDFDocument!, _ majorVersion: UnsafeMutablePointer<Int32>, _ minorVersion: UnsafeMutablePointer<Int32>) ``` |
| To | ``` func CGPDFDocumentGetVersion(_ document: CGPDFDocument?, _ majorVersion: UnsafeMutablePointer<Int32>, _ minorVersion: UnsafeMutablePointer<Int32>) ``` |

Modified [CGPDFDocumentIsEncrypted(_: CGPDFDocument?) -> Bool](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/1402591-isencrypted)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDocumentIsEncrypted(_ document: CGPDFDocument!) -> Bool ``` |
| To | ``` func CGPDFDocumentIsEncrypted(_ document: CGPDFDocument?) -> Bool ``` |

Modified [CGPDFDocumentIsUnlocked(_: CGPDFDocument?) -> Bool](https://developer.apple.com/documentation/coregraphics/1402607-cgpdfdocumentisunlocked)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDocumentIsUnlocked(_ document: CGPDFDocument!) -> Bool ``` |
| To | ``` func CGPDFDocumentIsUnlocked(_ document: CGPDFDocument?) -> Bool ``` |

Modified [CGPDFDocumentUnlockWithPassword(_: CGPDFDocument?, _: UnsafePointer<Int8>) -> Bool](https://developer.apple.com/documentation/coregraphics/1402599-cgpdfdocumentunlockwithpassword)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDocumentUnlockWithPassword(_ document: CGPDFDocument!, _ password: UnsafePointer<Int8>) -> Bool ``` |
| To | ``` func CGPDFDocumentUnlockWithPassword(_ document: CGPDFDocument?, _ password: UnsafePointer<Int8>) -> Bool ``` |

Modified [CGPDFOperatorCallback](https://developer.apple.com/documentation/coregraphics/cgpdfoperatorcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFOperatorCallback = CFunctionPointer<((CGPDFScannerRef, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CGPDFOperatorCallback = (CGPDFScannerRef, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CGPDFOperatorTableSetCallback(_: CGPDFOperatorTableRef, _: UnsafePointer<Int8>, _: CGPDFOperatorCallback?)](https://developer.apple.com/documentation/coregraphics/1454118-cgpdfoperatortablesetcallback)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFOperatorTableSetCallback(_ table: CGPDFOperatorTableRef, _ name: UnsafePointer<Int8>, _ callback: CGPDFOperatorCallback) ``` |
| To | ``` func CGPDFOperatorTableSetCallback(_ table: CGPDFOperatorTableRef, _ name: UnsafePointer<Int8>, _ callback: CGPDFOperatorCallback?) ``` |

Modified [CGPDFPageGetBoxRect(_: CGPDFPage?, _: CGPDFBox) -> CGRect](https://developer.apple.com/documentation/coregraphics/cgpdfpage/1456114-getboxrect)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFPageGetBoxRect(_ page: CGPDFPage!, _ box: CGPDFBox) -> CGRect ``` |
| To | ``` func CGPDFPageGetBoxRect(_ page: CGPDFPage?, _ box: CGPDFBox) -> CGRect ``` |

Modified [CGPDFPageGetDictionary(_: CGPDFPage?) -> CGPDFDictionaryRef](https://developer.apple.com/documentation/coregraphics/cgpdfpage/1455125-dictionary)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFPageGetDictionary(_ page: CGPDFPage!) -> CGPDFDictionaryRef ``` |
| To | ``` func CGPDFPageGetDictionary(_ page: CGPDFPage?) -> CGPDFDictionaryRef ``` |

Modified [CGPDFPageGetDocument(_: CGPDFPage?) -> CGPDFDocument?](https://developer.apple.com/documentation/coregraphics/cgpdfpage/1456166-document)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFPageGetDocument(_ page: CGPDFPage!) -> CGPDFDocument! ``` |
| To | ``` func CGPDFPageGetDocument(_ page: CGPDFPage?) -> CGPDFDocument? ``` |

Modified [CGPDFPageGetDrawingTransform(_: CGPDFPage?, _: CGPDFBox, _: CGRect, _: Int32, _: Bool) -> CGAffineTransform](https://developer.apple.com/documentation/coregraphics/cgpdfpage/1454893-getdrawingtransform)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFPageGetDrawingTransform(_ page: CGPDFPage!, _ box: CGPDFBox, _ rect: CGRect, _ rotate: Int32, _ preserveAspectRatio: Bool) -> CGAffineTransform ``` |
| To | ``` func CGPDFPageGetDrawingTransform(_ page: CGPDFPage?, _ box: CGPDFBox, _ rect: CGRect, _ rotate: Int32, _ preserveAspectRatio: Bool) -> CGAffineTransform ``` |

Modified [CGPDFPageGetPageNumber(_: CGPDFPage?) -> Int](https://developer.apple.com/documentation/coregraphics/1454587-cgpdfpagegetpagenumber)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFPageGetPageNumber(_ page: CGPDFPage!) -> Int ``` |
| To | ``` func CGPDFPageGetPageNumber(_ page: CGPDFPage?) -> Int ``` |

Modified [CGPDFPageGetRotationAngle(_: CGPDFPage?) -> Int32](https://developer.apple.com/documentation/coregraphics/1455550-cgpdfpagegetrotationangle)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFPageGetRotationAngle(_ page: CGPDFPage!) -> Int32 ``` |
| To | ``` func CGPDFPageGetRotationAngle(_ page: CGPDFPage?) -> Int32 ``` |

Modified [CGPDFStreamCopyData(_: CGPDFStreamRef, _: UnsafeMutablePointer<CGPDFDataFormat>) -> CFData?](https://developer.apple.com/documentation/coregraphics/1454657-cgpdfstreamcopydata)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFStreamCopyData(_ stream: CGPDFStreamRef, _ format: UnsafeMutablePointer<CGPDFDataFormat>) -> Unmanaged<CFData>! ``` |
| To | ``` func CGPDFStreamCopyData(_ stream: CGPDFStreamRef, _ format: UnsafeMutablePointer<CGPDFDataFormat>) -> CFData? ``` |

Modified [CGPDFStringCopyDate(_: CGPDFStringRef) -> CFDate?](https://developer.apple.com/documentation/coregraphics/1454295-cgpdfstringcopydate)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFStringCopyDate(_ string: CGPDFStringRef) -> Unmanaged<CFDate>! ``` |
| To | ``` func CGPDFStringCopyDate(_ string: CGPDFStringRef) -> CFDate? ``` |

Modified [CGPDFStringCopyTextString(_: CGPDFStringRef) -> CFString?](https://developer.apple.com/documentation/coregraphics/1456234-cgpdfstringcopytextstring)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFStringCopyTextString(_ string: CGPDFStringRef) -> Unmanaged<CFString>! ``` |
| To | ``` func CGPDFStringCopyTextString(_ string: CGPDFStringRef) -> CFString? ``` |

Modified [CGPointCreateDictionaryRepresentation(_: CGPoint) -> CFDictionary](https://developer.apple.com/documentation/coregraphics/cgpoint/1455382-dictionaryrepresentation)

|  | Declaration |
| --- | --- |
| From | ``` func CGPointCreateDictionaryRepresentation(_ point: CGPoint) -> CFDictionary! ``` |
| To | ``` func CGPointCreateDictionaryRepresentation(_ point: CGPoint) -> CFDictionary ``` |

Modified [CGPointMakeWithDictionaryRepresentation(_: CFDictionary?, _: UnsafeMutablePointer<CGPoint>) -> Bool](https://developer.apple.com/documentation/coregraphics/1455338-cgpointmakewithdictionaryreprese)

|  | Declaration |
| --- | --- |
| From | ``` func CGPointMakeWithDictionaryRepresentation(_ dict: CFDictionary!, _ point: UnsafeMutablePointer<CGPoint>) -> Bool ``` |
| To | ``` func CGPointMakeWithDictionaryRepresentation(_ dict: CFDictionary?, _ point: UnsafeMutablePointer<CGPoint>) -> Bool ``` |

Modified [CGPSConverterAbort(_: CGPSConverter) -> Bool](https://developer.apple.com/documentation/coregraphics/1455046-cgpsconverterabort)

|  | Declaration |
| --- | --- |
| From | ``` func CGPSConverterAbort(_ converter: CGPSConverter!) -> Bool ``` |
| To | ``` func CGPSConverterAbort(_ converter: CGPSConverter) -> Bool ``` |

Modified [CGPSConverterBeginDocumentCallback](https://developer.apple.com/documentation/coregraphics/cgpsconverterbegindocumentcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPSConverterBeginDocumentCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CGPSConverterBeginDocumentCallback = (UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CGPSConverterBeginPageCallback](https://developer.apple.com/documentation/coregraphics/cgpsconverterbeginpagecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPSConverterBeginPageCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, Int, CFDictionary!) -> Void)> ``` |
| To | ``` typealias CGPSConverterBeginPageCallback = (UnsafeMutablePointer<Void>, Int, CFDictionary) -> Void ``` |

Modified [CGPSConverterConvert(_: CGPSConverter, _: CGDataProvider, _: CGDataConsumer, _: CFDictionary?) -> Bool](https://developer.apple.com/documentation/coregraphics/cgpsconverter/1455368-convert)

|  | Declaration |
| --- | --- |
| From | ``` func CGPSConverterConvert(_ converter: CGPSConverter!, _ provider: CGDataProvider!, _ consumer: CGDataConsumer!, _ options: CFDictionary!) -> Bool ``` |
| To | ``` func CGPSConverterConvert(_ converter: CGPSConverter, _ provider: CGDataProvider, _ consumer: CGDataConsumer, _ options: CFDictionary?) -> Bool ``` |

Modified [CGPSConverterCreate(_: UnsafeMutablePointer<Void>, _: UnsafePointer<CGPSConverterCallbacks>, _: CFDictionary?) -> CGPSConverter?](https://developer.apple.com/documentation/coregraphics/1454773-cgpsconvertercreate)

|  | Declaration |
| --- | --- |
| From | ``` func CGPSConverterCreate(_ info: UnsafeMutablePointer<Void>, _ callbacks: UnsafePointer<CGPSConverterCallbacks>, _ options: CFDictionary!) -> CGPSConverter! ``` |
| To | ``` func CGPSConverterCreate(_ info: UnsafeMutablePointer<Void>, _ callbacks: UnsafePointer<CGPSConverterCallbacks>, _ options: CFDictionary?) -> CGPSConverter? ``` |

Modified [CGPSConverterEndDocumentCallback](https://developer.apple.com/documentation/coregraphics/cgpsconverterenddocumentcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPSConverterEndDocumentCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, Bool) -> Void)> ``` |
| To | ``` typealias CGPSConverterEndDocumentCallback = (UnsafeMutablePointer<Void>, Bool) -> Void ``` |

Modified [CGPSConverterEndPageCallback](https://developer.apple.com/documentation/coregraphics/cgpsconverterendpagecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPSConverterEndPageCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, Int, CFDictionary!) -> Void)> ``` |
| To | ``` typealias CGPSConverterEndPageCallback = (UnsafeMutablePointer<Void>, Int, CFDictionary) -> Void ``` |

Modified [CGPSConverterIsConverting(_: CGPSConverter) -> Bool](https://developer.apple.com/documentation/coregraphics/cgpsconverter/1454582-isconverting)

|  | Declaration |
| --- | --- |
| From | ``` func CGPSConverterIsConverting(_ converter: CGPSConverter!) -> Bool ``` |
| To | ``` func CGPSConverterIsConverting(_ converter: CGPSConverter) -> Bool ``` |

Modified [CGPSConverterMessageCallback](https://developer.apple.com/documentation/coregraphics/cgpsconvertermessagecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPSConverterMessageCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, CFString!) -> Void)> ``` |
| To | ``` typealias CGPSConverterMessageCallback = (UnsafeMutablePointer<Void>, CFString) -> Void ``` |

Modified [CGPSConverterProgressCallback](https://developer.apple.com/documentation/coregraphics/cgpsconverterprogresscallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPSConverterProgressCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CGPSConverterProgressCallback = (UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CGPSConverterReleaseInfoCallback](https://developer.apple.com/documentation/coregraphics/cgpsconverterreleaseinfocallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPSConverterReleaseInfoCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CGPSConverterReleaseInfoCallback = (UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CGRectCreateDictionaryRepresentation(_: CGRect) -> CFDictionary](https://developer.apple.com/documentation/coregraphics/cgrect/1455760-dictionaryrepresentation)

|  | Declaration |
| --- | --- |
| From | ``` func CGRectCreateDictionaryRepresentation(_ _: CGRect) -> CFDictionary! ``` |
| To | ``` func CGRectCreateDictionaryRepresentation(_ _: CGRect) -> CFDictionary ``` |

Modified [CGRectMakeWithDictionaryRepresentation(_: CFDictionary?, _: UnsafeMutablePointer<CGRect>) -> Bool](https://developer.apple.com/documentation/coregraphics/1456558-cgrectmakewithdictionaryrepresen)

|  | Declaration |
| --- | --- |
| From | ``` func CGRectMakeWithDictionaryRepresentation(_ dict: CFDictionary!, _ rect: UnsafeMutablePointer<CGRect>) -> Bool ``` |
| To | ``` func CGRectMakeWithDictionaryRepresentation(_ dict: CFDictionary?, _ rect: UnsafeMutablePointer<CGRect>) -> Bool ``` |

Modified [CGScreenRefreshCallback](https://developer.apple.com/documentation/coregraphics/cgscreenrefreshcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGScreenRefreshCallback = CFunctionPointer<((UInt32, UnsafePointer<CGRect>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CGScreenRefreshCallback = (UInt32, UnsafePointer<CGRect>, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CGScreenUpdateMoveCallback](https://developer.apple.com/documentation/coregraphics/cgscreenupdatemovecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGScreenUpdateMoveCallback = CFunctionPointer<((CGScreenUpdateMoveDelta, Int, UnsafePointer<CGRect>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CGScreenUpdateMoveCallback = (CGScreenUpdateMoveDelta, Int, UnsafePointer<CGRect>, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CGSessionCopyCurrentDictionary() -> CFDictionary?](https://developer.apple.com/documentation/coregraphics/1454780-cgsessioncopycurrentdictionary)

|  | Declaration |
| --- | --- |
| From | ``` func CGSessionCopyCurrentDictionary() -> Unmanaged<CFDictionary>! ``` |
| To | ``` func CGSessionCopyCurrentDictionary() -> CFDictionary? ``` |

Modified [CGShadingCreateAxial(_: CGColorSpace?, _: CGPoint, _: CGPoint, _: CGFunction?, _: Bool, _: Bool) -> CGShading?](https://developer.apple.com/documentation/coregraphics/cgshading/1455224-init)

|  | Declaration |
| --- | --- |
| From | ``` func CGShadingCreateAxial(_ space: CGColorSpace!, _ start: CGPoint, _ end: CGPoint, _ function: CGFunction!, _ extendStart: Bool, _ extendEnd: Bool) -> CGShading! ``` |
| To | ``` func CGShadingCreateAxial(_ space: CGColorSpace?, _ start: CGPoint, _ end: CGPoint, _ function: CGFunction?, _ extendStart: Bool, _ extendEnd: Bool) -> CGShading? ``` |

Modified [CGShadingCreateRadial(_: CGColorSpace?, _: CGPoint, _: CGFloat, _: CGPoint, _: CGFloat, _: CGFunction?, _: Bool, _: Bool) -> CGShading?](https://developer.apple.com/documentation/coregraphics/1456399-cgshadingcreateradial)

|  | Declaration |
| --- | --- |
| From | ``` func CGShadingCreateRadial(_ space: CGColorSpace!, _ start: CGPoint, _ startRadius: CGFloat, _ end: CGPoint, _ endRadius: CGFloat, _ function: CGFunction!, _ extendStart: Bool, _ extendEnd: Bool) -> CGShading! ``` |
| To | ``` func CGShadingCreateRadial(_ space: CGColorSpace?, _ start: CGPoint, _ startRadius: CGFloat, _ end: CGPoint, _ endRadius: CGFloat, _ function: CGFunction?, _ extendStart: Bool, _ extendEnd: Bool) -> CGShading? ``` |

Modified [CGSizeCreateDictionaryRepresentation(_: CGSize) -> CFDictionary](https://developer.apple.com/documentation/coregraphics/1455274-cgsizecreatedictionaryrepresenta)

|  | Declaration |
| --- | --- |
| From | ``` func CGSizeCreateDictionaryRepresentation(_ size: CGSize) -> CFDictionary! ``` |
| To | ``` func CGSizeCreateDictionaryRepresentation(_ size: CGSize) -> CFDictionary ``` |

Modified [CGSizeMakeWithDictionaryRepresentation(_: CFDictionary?, _: UnsafeMutablePointer<CGSize>) -> Bool](https://developer.apple.com/documentation/coregraphics/1454318-cgsizemakewithdictionaryrepresen)

|  | Declaration |
| --- | --- |
| From | ``` func CGSizeMakeWithDictionaryRepresentation(_ dict: CFDictionary!, _ size: UnsafeMutablePointer<CGSize>) -> Bool ``` |
| To | ``` func CGSizeMakeWithDictionaryRepresentation(_ dict: CFDictionary?, _ size: UnsafeMutablePointer<CGSize>) -> Bool ``` |

Modified [CGWindowListCopyWindowInfo(_: CGWindowListOption, _: CGWindowID) -> CFArray?](https://developer.apple.com/documentation/coregraphics/1455137-cgwindowlistcopywindowinfo)

|  | Declaration |
| --- | --- |
| From | ``` func CGWindowListCopyWindowInfo(_ option: CGWindowListOption, _ relativeToWindow: CGWindowID) -> Unmanaged<CFArray>! ``` |
| To | ``` func CGWindowListCopyWindowInfo(_ option: CGWindowListOption, _ relativeToWindow: CGWindowID) -> CFArray? ``` |

Modified [CGWindowListCreateDescriptionFromArray(_: CFArray?) -> CFArray?](https://developer.apple.com/documentation/coregraphics/1455215-cgwindowlistcreatedescriptionfro)

|  | Declaration |
| --- | --- |
| From | ``` func CGWindowListCreateDescriptionFromArray(_ windowArray: CFArray!) -> Unmanaged<CFArray>! ``` |
| To | ``` func CGWindowListCreateDescriptionFromArray(_ windowArray: CFArray?) -> CFArray? ``` |

Modified [CGWindowListCreateImage(_: CGRect, _: CGWindowListOption, _: CGWindowID, _: CGWindowImageOption) -> CGImage?](https://developer.apple.com/documentation/coregraphics/1454852-cgwindowlistcreateimage)

|  | Declaration |
| --- | --- |
| From | ``` func CGWindowListCreateImage(_ screenBounds: CGRect, _ listOption: CGWindowListOption, _ windowID: CGWindowID, _ imageOption: CGWindowImageOption) -> Unmanaged<CGImage>! ``` |
| To | ``` func CGWindowListCreateImage(_ screenBounds: CGRect, _ listOption: CGWindowListOption, _ windowID: CGWindowID, _ imageOption: CGWindowImageOption) -> CGImage? ``` |

Modified [CGWindowListCreateImageFromArray(_: CGRect, _: CFArray, _: CGWindowImageOption) -> CGImage?](https://developer.apple.com/documentation/coregraphics/1455730-cgwindowlistcreateimagefromarray)

|  | Declaration |
| --- | --- |
| From | ``` func CGWindowListCreateImageFromArray(_ screenBounds: CGRect, _ windowArray: CFArray!, _ imageOption: CGWindowImageOption) -> Unmanaged<CGImage>! ``` |
| To | ``` func CGWindowListCreateImageFromArray(_ screenBounds: CGRect, _ windowArray: CFArray, _ imageOption: CGWindowImageOption) -> CGImage? ``` |

Modified [CGWindowServerCreateServerPort() -> CFMachPort?](https://developer.apple.com/documentation/coregraphics/1454440-cgwindowservercreateserverport)

|  | Declaration |
| --- | --- |
| From | ``` func CGWindowServerCreateServerPort() -> Unmanaged<CFMachPort>! ``` |
| To | ``` func CGWindowServerCreateServerPort() -> CFMachPort? ``` |

Modified [copysign(_: CGFloat, _: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454101-copysign)

|  | Declaration |
| --- | --- |
| From | ``` func copysign(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func copysign(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified [cos(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455193-cos)

|  | Declaration |
| --- | --- |
| From | ``` func cos(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func cos(_ x: CGFloat) -> CGFloat ``` |

Modified [cosh(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455552-cosh)

|  | Declaration |
| --- | --- |
| From | ``` func cosh(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func cosh(_ x: CGFloat) -> CGFloat ``` |

Modified [erf(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454212-erf)

|  | Declaration |
| --- | --- |
| From | ``` func erf(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func erf(_ x: CGFloat) -> CGFloat ``` |

Modified [erfc(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455636-erfc)

|  | Declaration |
| --- | --- |
| From | ``` func erfc(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func erfc(_ x: CGFloat) -> CGFloat ``` |

Modified [exp(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455628-exp)

|  | Declaration |
| --- | --- |
| From | ``` func exp(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func exp(_ x: CGFloat) -> CGFloat ``` |

Modified [exp2(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455751-exp2)

|  | Declaration |
| --- | --- |
| From | ``` func exp2(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func exp2(_ x: CGFloat) -> CGFloat ``` |

Modified [expm1(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455892-expm1)

|  | Declaration |
| --- | --- |
| From | ``` func expm1(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func expm1(_ x: CGFloat) -> CGFloat ``` |

Modified fabs(_: CGFloat) -> CGFloat

|  | Declaration |
| --- | --- |
| From | ``` func fabs(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func fabs(_ x: CGFloat) -> CGFloat ``` |

Modified [fdim(_: CGFloat, _: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454169-fdim)

|  | Declaration |
| --- | --- |
| From | ``` func fdim(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func fdim(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified floor(_: CGFloat) -> CGFloat

|  | Declaration |
| --- | --- |
| From | ``` func floor(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func floor(_ x: CGFloat) -> CGFloat ``` |

Modified fma(_: CGFloat, _: CGFloat, _: CGFloat) -> CGFloat

|  | Declaration |
| --- | --- |
| From | ``` func fma(_ x: CGFloat, _ y: CGFloat, _ z: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func fma(_ x: CGFloat, _ y: CGFloat, _ z: CGFloat) -> CGFloat ``` |

Modified [fmax(_: CGFloat, _: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454365-fmax)

|  | Declaration |
| --- | --- |
| From | ``` func fmax(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func fmax(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified [fmin(_: CGFloat, _: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454631-fmin)

|  | Declaration |
| --- | --- |
| From | ``` func fmin(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func fmin(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified fmod(_: CGFloat, _: CGFloat) -> CGFloat

|  | Declaration |
| --- | --- |
| From | ``` func fmod(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func fmod(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified fpclassify(_: CGFloat) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func fpclassify(_ x: CGFloat) -> Int ``` |
| To | ``` @warn_unused_result func fpclassify(_ x: CGFloat) -> Int ``` |

Modified frexp(_: CGFloat) -> (CGFloat, Int)

|  | Declaration |
| --- | --- |
| From | ``` func frexp(_ x: CGFloat) -> (CGFloat, Int) ``` |
| To | ``` @warn_unused_result func frexp(_ x: CGFloat) -> (CGFloat, Int) ``` |

Modified [hypot(_: CGFloat, _: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456251-hypot)

|  | Declaration |
| --- | --- |
| From | ``` func hypot(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func hypot(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified [ilogb(_: CGFloat) -> Int](https://developer.apple.com/documentation/coregraphics/1454373-ilogb)

|  | Declaration |
| --- | --- |
| From | ``` func ilogb(_ x: CGFloat) -> Int ``` |
| To | ``` @warn_unused_result func ilogb(_ x: CGFloat) -> Int ``` |

Modified isfinite(_: CGFloat) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isfinite(_ x: CGFloat) -> Bool ``` |
| To | ``` @warn_unused_result func isfinite(_ x: CGFloat) -> Bool ``` |

Modified isinf(_: CGFloat) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isinf(_ x: CGFloat) -> Bool ``` |
| To | ``` @warn_unused_result func isinf(_ x: CGFloat) -> Bool ``` |

Modified isnan(_: CGFloat) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isnan(_ x: CGFloat) -> Bool ``` |
| To | ``` @warn_unused_result func isnan(_ x: CGFloat) -> Bool ``` |

Modified isnormal(_: CGFloat) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isnormal(_ x: CGFloat) -> Bool ``` |
| To | ``` @warn_unused_result func isnormal(_ x: CGFloat) -> Bool ``` |

Modified [j0(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455107-j0)

|  | Declaration |
| --- | --- |
| From | ``` func j0(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func j0(_ x: CGFloat) -> CGFloat ``` |

Modified [j1(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455116-j1)

|  | Declaration |
| --- | --- |
| From | ``` func j1(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func j1(_ x: CGFloat) -> CGFloat ``` |

Modified [jn(_: Int, _: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456281-jn)

|  | Declaration |
| --- | --- |
| From | ``` func jn(_ n: Int, _ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func jn(_ n: Int, _ x: CGFloat) -> CGFloat ``` |

Modified [kCGColorBlack](https://developer.apple.com/documentation/coregraphics/cgcolor/1456641-black)

|  | Declaration |
| --- | --- |
| From | ``` let kCGColorBlack: CFString! ``` |
| To | ``` let kCGColorBlack: CFString ``` |

Modified [kCGColorClear](https://developer.apple.com/documentation/coregraphics/cgcolor/1454809-clear)

|  | Declaration |
| --- | --- |
| From | ``` let kCGColorClear: CFString! ``` |
| To | ``` let kCGColorClear: CFString ``` |

Modified [kCGColorSpaceAdobeRGB1998](https://developer.apple.com/documentation/coregraphics/kcgcolorspaceadobergb1998)

|  | Declaration |
| --- | --- |
| From | ``` let kCGColorSpaceAdobeRGB1998: CFString! ``` |
| To | ``` let kCGColorSpaceAdobeRGB1998: CFString ``` |

Modified [kCGColorSpaceGenericCMYK](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408904-genericcmyk)

|  | Declaration |
| --- | --- |
| From | ``` let kCGColorSpaceGenericCMYK: CFString! ``` |
| To | ``` let kCGColorSpaceGenericCMYK: CFString ``` |

Modified [kCGColorSpaceGenericGray](https://developer.apple.com/documentation/coregraphics/kcgcolorspacegenericgray)

|  | Declaration |
| --- | --- |
| From | ``` let kCGColorSpaceGenericGray: CFString! ``` |
| To | ``` let kCGColorSpaceGenericGray: CFString ``` |

Modified [kCGColorSpaceGenericGrayGamma2_2](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408857-genericgraygamma2_2)

|  | Declaration |
| --- | --- |
| From | ``` let kCGColorSpaceGenericGrayGamma2_2: CFString! ``` |
| To | ``` let kCGColorSpaceGenericGrayGamma2_2: CFString ``` |

Modified [kCGColorSpaceGenericRGB](https://developer.apple.com/documentation/coregraphics/kcgcolorspacegenericrgb)

|  | Declaration |
| --- | --- |
| From | ``` let kCGColorSpaceGenericRGB: CFString! ``` |
| To | ``` let kCGColorSpaceGenericRGB: CFString ``` |

Modified [kCGColorSpaceGenericRGBLinear](https://developer.apple.com/documentation/coregraphics/kcgcolorspacegenericrgblinear)

|  | Declaration |
| --- | --- |
| From | ``` let kCGColorSpaceGenericRGBLinear: CFString! ``` |
| To | ``` let kCGColorSpaceGenericRGBLinear: CFString ``` |

Modified [kCGColorSpaceSRGB](https://developer.apple.com/documentation/coregraphics/kcgcolorspacesrgb)

|  | Declaration |
| --- | --- |
| From | ``` let kCGColorSpaceSRGB: CFString! ``` |
| To | ``` let kCGColorSpaceSRGB: CFString ``` |

Modified [kCGColorWhite](https://developer.apple.com/documentation/coregraphics/cgcolor/1455202-white)

|  | Declaration |
| --- | --- |
| From | ``` let kCGColorWhite: CFString! ``` |
| To | ``` let kCGColorWhite: CFString ``` |

Modified [kCGDisplayShowDuplicateLowResolutionModes](https://developer.apple.com/documentation/coregraphics/kcgdisplayshowduplicatelowresolutionmodes)

|  | Declaration |
| --- | --- |
| From | ``` let kCGDisplayShowDuplicateLowResolutionModes: CFString! ``` |
| To | ``` let kCGDisplayShowDuplicateLowResolutionModes: CFString ``` |

Modified [kCGDisplayStreamColorSpace](https://developer.apple.com/documentation/coregraphics/kcgdisplaystreamcolorspace)

|  | Declaration |
| --- | --- |
| From | ``` let kCGDisplayStreamColorSpace: CFString! ``` |
| To | ``` let kCGDisplayStreamColorSpace: CFString ``` |

Modified [kCGDisplayStreamDestinationRect](https://developer.apple.com/documentation/coregraphics/kcgdisplaystreamdestinationrect)

|  | Declaration |
| --- | --- |
| From | ``` let kCGDisplayStreamDestinationRect: CFString! ``` |
| To | ``` let kCGDisplayStreamDestinationRect: CFString ``` |

Modified [kCGDisplayStreamMinimumFrameTime](https://developer.apple.com/documentation/coregraphics/cgdisplaystream/1455023-minimumframetime)

|  | Declaration |
| --- | --- |
| From | ``` let kCGDisplayStreamMinimumFrameTime: CFString! ``` |
| To | ``` let kCGDisplayStreamMinimumFrameTime: CFString ``` |

Modified [kCGDisplayStreamPreserveAspectRatio](https://developer.apple.com/documentation/coregraphics/cgdisplaystream/1454952-preserveaspectratio)

|  | Declaration |
| --- | --- |
| From | ``` let kCGDisplayStreamPreserveAspectRatio: CFString! ``` |
| To | ``` let kCGDisplayStreamPreserveAspectRatio: CFString ``` |

Modified [kCGDisplayStreamQueueDepth](https://developer.apple.com/documentation/coregraphics/cgdisplaystream/1454559-queuedepth)

|  | Declaration |
| --- | --- |
| From | ``` let kCGDisplayStreamQueueDepth: CFString! ``` |
| To | ``` let kCGDisplayStreamQueueDepth: CFString ``` |

Modified [kCGDisplayStreamShowCursor](https://developer.apple.com/documentation/coregraphics/kcgdisplaystreamshowcursor)

|  | Declaration |
| --- | --- |
| From | ``` let kCGDisplayStreamShowCursor: CFString! ``` |
| To | ``` let kCGDisplayStreamShowCursor: CFString ``` |

Modified [kCGDisplayStreamSourceRect](https://developer.apple.com/documentation/coregraphics/cgdisplaystream/1456198-sourcerect)

|  | Declaration |
| --- | --- |
| From | ``` let kCGDisplayStreamSourceRect: CFString! ``` |
| To | ``` let kCGDisplayStreamSourceRect: CFString ``` |

Modified [kCGDisplayStreamYCbCrMatrix](https://developer.apple.com/documentation/coregraphics/cgdisplaystream/1454220-ycbcrmatrix)

|  | Declaration |
| --- | --- |
| From | ``` let kCGDisplayStreamYCbCrMatrix: CFString! ``` |
| To | ``` let kCGDisplayStreamYCbCrMatrix: CFString ``` |

Modified [kCGDisplayStreamYCbCrMatrix_ITU_R_601_4](https://developer.apple.com/documentation/coregraphics/cgdisplaystream/1454120-ycbcrmatrix_itu_r_601_4)

|  | Declaration |
| --- | --- |
| From | ``` let kCGDisplayStreamYCbCrMatrix_ITU_R_601_4: CFString! ``` |
| To | ``` let kCGDisplayStreamYCbCrMatrix_ITU_R_601_4: CFString ``` |

Modified [kCGDisplayStreamYCbCrMatrix_ITU_R_709_2](https://developer.apple.com/documentation/coregraphics/cgdisplaystream/1455443-ycbcrmatrix_itu_r_709_2)

|  | Declaration |
| --- | --- |
| From | ``` let kCGDisplayStreamYCbCrMatrix_ITU_R_709_2: CFString! ``` |
| To | ``` let kCGDisplayStreamYCbCrMatrix_ITU_R_709_2: CFString ``` |

Modified [kCGDisplayStreamYCbCrMatrix_SMPTE_240M_1995](https://developer.apple.com/documentation/coregraphics/kcgdisplaystreamycbcrmatrix_smpte_240m_1995)

|  | Declaration |
| --- | --- |
| From | ``` let kCGDisplayStreamYCbCrMatrix_SMPTE_240M_1995: CFString! ``` |
| To | ``` let kCGDisplayStreamYCbCrMatrix_SMPTE_240M_1995: CFString ``` |

Modified [kCGFontIndexInvalid](https://developer.apple.com/documentation/coregraphics/kcgfontindexinvalid)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCGFontIndexInvalid: Int { get } ``` | OS X 10.10 |
| To | ``` let kCGFontIndexInvalid: CGFontIndex ``` | OS X 10.11 |

Modified [kCGFontIndexMax](https://developer.apple.com/documentation/coregraphics/kcgfontindexmax)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCGFontIndexMax: Int { get } ``` | OS X 10.10 |
| To | ``` let kCGFontIndexMax: CGFontIndex ``` | OS X 10.11 |

Modified [kCGFontVariationAxisDefaultValue](https://developer.apple.com/documentation/coregraphics/cgfont/1396394-variationaxisdefaultvalue)

|  | Declaration |
| --- | --- |
| From | ``` let kCGFontVariationAxisDefaultValue: CFString! ``` |
| To | ``` let kCGFontVariationAxisDefaultValue: CFString ``` |

Modified [kCGFontVariationAxisMaxValue](https://developer.apple.com/documentation/coregraphics/kcgfontvariationaxismaxvalue)

|  | Declaration |
| --- | --- |
| From | ``` let kCGFontVariationAxisMaxValue: CFString! ``` |
| To | ``` let kCGFontVariationAxisMaxValue: CFString ``` |

Modified [kCGFontVariationAxisMinValue](https://developer.apple.com/documentation/coregraphics/cgfont/1396322-variationaxisminvalue)

|  | Declaration |
| --- | --- |
| From | ``` let kCGFontVariationAxisMinValue: CFString! ``` |
| To | ``` let kCGFontVariationAxisMinValue: CFString ``` |

Modified [kCGFontVariationAxisName](https://developer.apple.com/documentation/coregraphics/cgfont/1396398-variationaxisname)

|  | Declaration |
| --- | --- |
| From | ``` let kCGFontVariationAxisName: CFString! ``` |
| To | ``` let kCGFontVariationAxisName: CFString ``` |

Modified [kCGGlyphMax](https://developer.apple.com/documentation/coregraphics/kcgglyphmax)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCGGlyphMax: Int { get } ``` | OS X 10.10 |
| To | ``` let kCGGlyphMax: CGFontIndex ``` | OS X 10.11 |

Modified [kCGPDFContextAllowsCopying](https://developer.apple.com/documentation/coregraphics/kcgpdfcontextallowscopying)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFContextAllowsCopying: CFString! ``` |
| To | ``` let kCGPDFContextAllowsCopying: CFString ``` |

Modified [kCGPDFContextAllowsPrinting](https://developer.apple.com/documentation/coregraphics/kcgpdfcontextallowsprinting)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFContextAllowsPrinting: CFString! ``` |
| To | ``` let kCGPDFContextAllowsPrinting: CFString ``` |

Modified [kCGPDFContextArtBox](https://developer.apple.com/documentation/coregraphics/kcgpdfcontextartbox)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFContextArtBox: CFString! ``` |
| To | ``` let kCGPDFContextArtBox: CFString ``` |

Modified [kCGPDFContextAuthor](https://developer.apple.com/documentation/coregraphics/kcgpdfcontextauthor)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFContextAuthor: CFString! ``` |
| To | ``` let kCGPDFContextAuthor: CFString ``` |

Modified [kCGPDFContextBleedBox](https://developer.apple.com/documentation/coregraphics/kcgpdfcontextbleedbox)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFContextBleedBox: CFString! ``` |
| To | ``` let kCGPDFContextBleedBox: CFString ``` |

Modified [kCGPDFContextCreator](https://developer.apple.com/documentation/coregraphics/kcgpdfcontextcreator)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFContextCreator: CFString! ``` |
| To | ``` let kCGPDFContextCreator: CFString ``` |

Modified [kCGPDFContextCropBox](https://developer.apple.com/documentation/coregraphics/kcgpdfcontextcropbox)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFContextCropBox: CFString! ``` |
| To | ``` let kCGPDFContextCropBox: CFString ``` |

Modified [kCGPDFContextEncryptionKeyLength](https://developer.apple.com/documentation/coregraphics/kcgpdfcontextencryptionkeylength)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFContextEncryptionKeyLength: CFString! ``` |
| To | ``` let kCGPDFContextEncryptionKeyLength: CFString ``` |

Modified [kCGPDFContextKeywords](https://developer.apple.com/documentation/coregraphics/kcgpdfcontextkeywords)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFContextKeywords: CFString! ``` |
| To | ``` let kCGPDFContextKeywords: CFString ``` |

Modified [kCGPDFContextMediaBox](https://developer.apple.com/documentation/coregraphics/kcgpdfcontextmediabox)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFContextMediaBox: CFString! ``` |
| To | ``` let kCGPDFContextMediaBox: CFString ``` |

Modified [kCGPDFContextOutputIntent](https://developer.apple.com/documentation/coregraphics/kcgpdfcontextoutputintent)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFContextOutputIntent: CFString! ``` |
| To | ``` let kCGPDFContextOutputIntent: CFString ``` |

Modified [kCGPDFContextOutputIntents](https://developer.apple.com/documentation/coregraphics/kcgpdfcontextoutputintents)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFContextOutputIntents: CFString! ``` |
| To | ``` let kCGPDFContextOutputIntents: CFString ``` |

Modified [kCGPDFContextOwnerPassword](https://developer.apple.com/documentation/coregraphics/kcgpdfcontextownerpassword)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFContextOwnerPassword: CFString! ``` |
| To | ``` let kCGPDFContextOwnerPassword: CFString ``` |

Modified [kCGPDFContextSubject](https://developer.apple.com/documentation/coregraphics/kcgpdfcontextsubject)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFContextSubject: CFString! ``` |
| To | ``` let kCGPDFContextSubject: CFString ``` |

Modified [kCGPDFContextTitle](https://developer.apple.com/documentation/coregraphics/kcgpdfcontexttitle)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFContextTitle: CFString! ``` |
| To | ``` let kCGPDFContextTitle: CFString ``` |

Modified [kCGPDFContextTrimBox](https://developer.apple.com/documentation/coregraphics/kcgpdfcontexttrimbox)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFContextTrimBox: CFString! ``` |
| To | ``` let kCGPDFContextTrimBox: CFString ``` |

Modified [kCGPDFContextUserPassword](https://developer.apple.com/documentation/coregraphics/kcgpdfcontextuserpassword)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFContextUserPassword: CFString! ``` |
| To | ``` let kCGPDFContextUserPassword: CFString ``` |

Modified [kCGPDFXDestinationOutputProfile](https://developer.apple.com/documentation/coregraphics/kcgpdfxdestinationoutputprofile)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFXDestinationOutputProfile: CFString! ``` |
| To | ``` let kCGPDFXDestinationOutputProfile: CFString ``` |

Modified [kCGPDFXInfo](https://developer.apple.com/documentation/coregraphics/kcgpdfxinfo)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFXInfo: CFString! ``` |
| To | ``` let kCGPDFXInfo: CFString ``` |

Modified [kCGPDFXOutputCondition](https://developer.apple.com/documentation/coregraphics/kcgpdfxoutputcondition)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFXOutputCondition: CFString! ``` |
| To | ``` let kCGPDFXOutputCondition: CFString ``` |

Modified [kCGPDFXOutputConditionIdentifier](https://developer.apple.com/documentation/coregraphics/kcgpdfxoutputconditionidentifier)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFXOutputConditionIdentifier: CFString! ``` |
| To | ``` let kCGPDFXOutputConditionIdentifier: CFString ``` |

Modified [kCGPDFXOutputIntentSubtype](https://developer.apple.com/documentation/coregraphics/kcgpdfxoutputintentsubtype)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFXOutputIntentSubtype: CFString! ``` |
| To | ``` let kCGPDFXOutputIntentSubtype: CFString ``` |

Modified [kCGPDFXRegistryName](https://developer.apple.com/documentation/coregraphics/kcgpdfxregistryname)

|  | Declaration |
| --- | --- |
| From | ``` let kCGPDFXRegistryName: CFString! ``` |
| To | ``` let kCGPDFXRegistryName: CFString ``` |

Modified [kCGWindowAlpha](https://developer.apple.com/documentation/coregraphics/kcgwindowalpha)

|  | Declaration |
| --- | --- |
| From | ``` let kCGWindowAlpha: CFString! ``` |
| To | ``` let kCGWindowAlpha: CFString ``` |

Modified [kCGWindowBackingLocationVideoMemory](https://developer.apple.com/documentation/coregraphics/kcgwindowbackinglocationvideomemory)

|  | Declaration |
| --- | --- |
| From | ``` let kCGWindowBackingLocationVideoMemory: CFString! ``` |
| To | ``` let kCGWindowBackingLocationVideoMemory: CFString ``` |

Modified [kCGWindowBounds](https://developer.apple.com/documentation/coregraphics/kcgwindowbounds)

|  | Declaration |
| --- | --- |
| From | ``` let kCGWindowBounds: CFString! ``` |
| To | ``` let kCGWindowBounds: CFString ``` |

Modified [kCGWindowIsOnscreen](https://developer.apple.com/documentation/coregraphics/kcgwindowisonscreen)

|  | Declaration |
| --- | --- |
| From | ``` let kCGWindowIsOnscreen: CFString! ``` |
| To | ``` let kCGWindowIsOnscreen: CFString ``` |

Modified [kCGWindowLayer](https://developer.apple.com/documentation/coregraphics/kcgwindowlayer)

|  | Declaration |
| --- | --- |
| From | ``` let kCGWindowLayer: CFString! ``` |
| To | ``` let kCGWindowLayer: CFString ``` |

Modified [kCGWindowMemoryUsage](https://developer.apple.com/documentation/coregraphics/kcgwindowmemoryusage)

|  | Declaration |
| --- | --- |
| From | ``` let kCGWindowMemoryUsage: CFString! ``` |
| To | ``` let kCGWindowMemoryUsage: CFString ``` |

Modified [kCGWindowName](https://developer.apple.com/documentation/coregraphics/kcgwindowname)

|  | Declaration |
| --- | --- |
| From | ``` let kCGWindowName: CFString! ``` |
| To | ``` let kCGWindowName: CFString ``` |

Modified [kCGWindowNumber](https://developer.apple.com/documentation/coregraphics/kcgwindownumber)

|  | Declaration |
| --- | --- |
| From | ``` let kCGWindowNumber: CFString! ``` |
| To | ``` let kCGWindowNumber: CFString ``` |

Modified [kCGWindowOwnerName](https://developer.apple.com/documentation/coregraphics/kcgwindowownername)

|  | Declaration |
| --- | --- |
| From | ``` let kCGWindowOwnerName: CFString! ``` |
| To | ``` let kCGWindowOwnerName: CFString ``` |

Modified [kCGWindowOwnerPID](https://developer.apple.com/documentation/coregraphics/kcgwindowownerpid)

|  | Declaration |
| --- | --- |
| From | ``` let kCGWindowOwnerPID: CFString! ``` |
| To | ``` let kCGWindowOwnerPID: CFString ``` |

Modified [kCGWindowSharingState](https://developer.apple.com/documentation/coregraphics/kcgwindowsharingstate)

|  | Declaration |
| --- | --- |
| From | ``` let kCGWindowSharingState: CFString! ``` |
| To | ``` let kCGWindowSharingState: CFString ``` |

Modified [kCGWindowStoreType](https://developer.apple.com/documentation/coregraphics/kcgwindowstoretype)

|  | Declaration |
| --- | --- |
| From | ``` let kCGWindowStoreType: CFString! ``` |
| To | ``` let kCGWindowStoreType: CFString ``` |

Modified [ldexp(_: CGFloat, _: Int) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454868-ldexp)

|  | Declaration |
| --- | --- |
| From | ``` func ldexp(_ x: CGFloat, _ n: Int) -> CGFloat ``` |
| To | ``` @warn_unused_result func ldexp(_ x: CGFloat, _ n: Int) -> CGFloat ``` |

Modified [lgamma(_: CGFloat) -> (CGFloat, Int)](https://developer.apple.com/documentation/coregraphics/1455415-lgamma)

|  | Declaration |
| --- | --- |
| From | ``` func lgamma(_ x: CGFloat) -> (CGFloat, Int) ``` |
| To | ``` @warn_unused_result func lgamma(_ x: CGFloat) -> (CGFloat, Int) ``` |

Modified [log(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456382-log)

|  | Declaration |
| --- | --- |
| From | ``` func log(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func log(_ x: CGFloat) -> CGFloat ``` |

Modified [log10(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456602-log10)

|  | Declaration |
| --- | --- |
| From | ``` func log10(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func log10(_ x: CGFloat) -> CGFloat ``` |

Modified [log1p(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455279-log1p)

|  | Declaration |
| --- | --- |
| From | ``` func log1p(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func log1p(_ x: CGFloat) -> CGFloat ``` |

Modified [log2(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455770-log2)

|  | Declaration |
| --- | --- |
| From | ``` func log2(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func log2(_ x: CGFloat) -> CGFloat ``` |

Modified [logb(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455887-logb)

|  | Declaration |
| --- | --- |
| From | ``` func logb(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func logb(_ x: CGFloat) -> CGFloat ``` |

Modified modf(_: CGFloat) -> (CGFloat, CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` func modf(_ x: CGFloat) -> (CGFloat, CGFloat) ``` |
| To | ``` @warn_unused_result func modf(_ x: CGFloat) -> (CGFloat, CGFloat) ``` |

Modified [nan(_: String) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456512-nan)

|  | Declaration |
| --- | --- |
| From | ``` func nan(_ tag: String) -> CGFloat ``` |
| To | ``` @warn_unused_result func nan(_ tag: String) -> CGFloat ``` |

Modified [nearbyint(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455515-nearbyint)

|  | Declaration |
| --- | --- |
| From | ``` func nearbyint(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func nearbyint(_ x: CGFloat) -> CGFloat ``` |

Modified [nextafter(_: CGFloat, _: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454239-nextafter)

|  | Declaration |
| --- | --- |
| From | ``` func nextafter(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func nextafter(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified [pow(_: CGFloat, _: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456106-pow)

|  | Declaration |
| --- | --- |
| From | ``` func pow(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func pow(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified remainder(_: CGFloat, _: CGFloat) -> CGFloat

|  | Declaration |
| --- | --- |
| From | ``` func remainder(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func remainder(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified [remquo(_: CGFloat, _: CGFloat) -> (CGFloat, Int)](https://developer.apple.com/documentation/coregraphics/1455673-remquo)

|  | Declaration |
| --- | --- |
| From | ``` func remquo(_ x: CGFloat, _ y: CGFloat) -> (CGFloat, Int) ``` |
| To | ``` @warn_unused_result func remquo(_ x: CGFloat, _ y: CGFloat) -> (CGFloat, Int) ``` |

Modified [rint(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455975-rint)

|  | Declaration |
| --- | --- |
| From | ``` func rint(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func rint(_ x: CGFloat) -> CGFloat ``` |

Modified round(_: CGFloat) -> CGFloat

|  | Declaration |
| --- | --- |
| From | ``` func round(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func round(_ x: CGFloat) -> CGFloat ``` |

Modified scalbn(_: CGFloat, _: Int) -> CGFloat

|  | Declaration |
| --- | --- |
| From | ``` func scalbn(_ x: CGFloat, _ n: Int) -> CGFloat ``` |
| To | ``` @warn_unused_result func scalbn(_ x: CGFloat, _ n: Int) -> CGFloat ``` |

Modified signbit(_: CGFloat) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func signbit(_ x: CGFloat) -> Int ``` |
| To | ``` @warn_unused_result func signbit(_ x: CGFloat) -> Int ``` |

Modified [sin(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456063-sin)

|  | Declaration |
| --- | --- |
| From | ``` func sin(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func sin(_ x: CGFloat) -> CGFloat ``` |

Modified [sinh(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456648-sinh)

|  | Declaration |
| --- | --- |
| From | ``` func sinh(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func sinh(_ x: CGFloat) -> CGFloat ``` |

Modified sqrt(_: CGFloat) -> CGFloat

|  | Declaration |
| --- | --- |
| From | ``` func sqrt(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func sqrt(_ x: CGFloat) -> CGFloat ``` |

Modified [tan(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454519-tan)

|  | Declaration |
| --- | --- |
| From | ``` func tan(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func tan(_ x: CGFloat) -> CGFloat ``` |

Modified [tanh(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454619-tanh)

|  | Declaration |
| --- | --- |
| From | ``` func tanh(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func tanh(_ x: CGFloat) -> CGFloat ``` |

Modified [tgamma(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454069-tgamma)

|  | Declaration |
| --- | --- |
| From | ``` func tgamma(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func tgamma(_ x: CGFloat) -> CGFloat ``` |

Modified trunc(_: CGFloat) -> CGFloat

|  | Declaration |
| --- | --- |
| From | ``` func trunc(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func trunc(_ x: CGFloat) -> CGFloat ``` |

Modified [y0(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456014-y0)

|  | Declaration |
| --- | --- |
| From | ``` func y0(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func y0(_ x: CGFloat) -> CGFloat ``` |

Modified [y1(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454958-y1)

|  | Declaration |
| --- | --- |
| From | ``` func y1(_ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func y1(_ x: CGFloat) -> CGFloat ``` |

Modified [yn(_: Int, _: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455951-yn)

|  | Declaration |
| --- | --- |
| From | ``` func yn(_ n: Int, _ x: CGFloat) -> CGFloat ``` |
| To | ``` @warn_unused_result func yn(_ n: Int, _ x: CGFloat) -> CGFloat ``` |

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
