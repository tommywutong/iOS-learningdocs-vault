---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/ImageCaptureCore.html
archived_at: '2026-07-18T02:53:36.680361Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# ImageCaptureCore Changes for Swift

### ImageCaptureCore

Removed ICReturnCode.init(_: Int32)Removed ICReturnCode.valueRemoved ICDeviceLocationTypeRemoved ICDeviceLocationTypeBluetoothRemoved ICDeviceLocationTypeBonjourRemoved ICDeviceLocationTypeLocalRemoved ICDeviceLocationTypeMaskRemoved ICDeviceLocationTypeMaskBluetoothRemoved ICDeviceLocationTypeMaskBonjourRemoved ICDeviceLocationTypeMaskLocalRemoved ICDeviceLocationTypeMaskRemoteRemoved ICDeviceLocationTypeMaskSharedRemoved ICDeviceLocationTypeSharedRemoved ICDeviceTypeRemoved ICDeviceTypeCameraRemoved ICDeviceTypeMaskRemoved ICDeviceTypeMaskCameraRemoved ICDeviceTypeMaskScannerRemoved ICDeviceTypeScannerRemoved ICEXIFOrientation1Removed ICEXIFOrientation2Removed ICEXIFOrientation3Removed ICEXIFOrientation4Removed ICEXIFOrientation5Removed ICEXIFOrientation6Removed ICEXIFOrientation7Removed ICEXIFOrientation8Removed ICEXIFOrientationTypeRemoved ICScannerBitDepthRemoved ICScannerBitDepth16BitsRemoved ICScannerBitDepth1BitRemoved ICScannerBitDepth8BitsRemoved ICScannerColorDataFormatTypeRemoved ICScannerColorDataFormatTypeChunkyRemoved ICScannerColorDataFormatTypePlanarRemoved ICScannerDocumentTypeRemoved ICScannerDocumentType10Removed ICScannerDocumentType10RRemoved ICScannerDocumentType110Removed ICScannerDocumentType11RRemoved ICScannerDocumentType12RRemoved ICScannerDocumentType135Removed ICScannerDocumentType2A0Removed ICScannerDocumentType3RRemoved ICScannerDocumentType4A0Removed ICScannerDocumentType4RRemoved ICScannerDocumentType5RRemoved ICScannerDocumentType6RRemoved ICScannerDocumentType8RRemoved ICScannerDocumentTypeA0Removed ICScannerDocumentTypeA1Removed ICScannerDocumentTypeA2Removed ICScannerDocumentTypeA3Removed ICScannerDocumentTypeA4Removed ICScannerDocumentTypeA5Removed ICScannerDocumentTypeA6Removed ICScannerDocumentTypeA7Removed ICScannerDocumentTypeA8Removed ICScannerDocumentTypeA9Removed ICScannerDocumentTypeAPSCRemoved ICScannerDocumentTypeAPSHRemoved ICScannerDocumentTypeAPSPRemoved ICScannerDocumentTypeB5Removed ICScannerDocumentTypeBusinessCardRemoved ICScannerDocumentTypeC0Removed ICScannerDocumentTypeC1Removed ICScannerDocumentTypeC10Removed ICScannerDocumentTypeC2Removed ICScannerDocumentTypeC3Removed ICScannerDocumentTypeC4Removed ICScannerDocumentTypeC5Removed ICScannerDocumentTypeC6Removed ICScannerDocumentTypeC7Removed ICScannerDocumentTypeC8Removed ICScannerDocumentTypeC9Removed ICScannerDocumentTypeDefaultRemoved ICScannerDocumentTypeERemoved ICScannerDocumentTypeISOB0Removed ICScannerDocumentTypeISOB1Removed ICScannerDocumentTypeISOB10Removed ICScannerDocumentTypeISOB2Removed ICScannerDocumentTypeISOB3Removed ICScannerDocumentTypeISOB4Removed ICScannerDocumentTypeISOB5Removed ICScannerDocumentTypeISOB6Removed ICScannerDocumentTypeISOB7Removed ICScannerDocumentTypeISOB8Removed ICScannerDocumentTypeISOB9Removed ICScannerDocumentTypeJISB0Removed ICScannerDocumentTypeJISB1Removed ICScannerDocumentTypeJISB10Removed ICScannerDocumentTypeJISB2Removed ICScannerDocumentTypeJISB3Removed ICScannerDocumentTypeJISB4Removed ICScannerDocumentTypeJISB6Removed ICScannerDocumentTypeJISB7Removed ICScannerDocumentTypeJISB8Removed ICScannerDocumentTypeJISB9Removed ICScannerDocumentTypeLFRemoved ICScannerDocumentTypeMFRemoved ICScannerDocumentTypeS10RRemoved ICScannerDocumentTypeS12RRemoved ICScannerDocumentTypeS8RRemoved ICScannerDocumentTypeUSExecutiveRemoved ICScannerDocumentTypeUSLedgerRemoved ICScannerDocumentTypeUSLegalRemoved ICScannerDocumentTypeUSLetterRemoved ICScannerDocumentTypeUSStatementRemoved ICScannerFeatureTypeRemoved ICScannerFeatureTypeBooleanRemoved ICScannerFeatureTypeEnumerationRemoved ICScannerFeatureTypeRangeRemoved ICScannerFeatureTypeTemplateRemoved ICScannerFunctionalUnitStateRemoved ICScannerFunctionalUnitStateOverviewScanInProgressRemoved ICScannerFunctionalUnitStateReadyRemoved ICScannerFunctionalUnitStateScanInProgressRemoved ICScannerFunctionalUnitTypeRemoved ICScannerFunctionalUnitTypeDocumentFeederRemoved ICScannerFunctionalUnitTypeFlatbedRemoved ICScannerFunctionalUnitTypeNegativeTransparencyRemoved ICScannerFunctionalUnitTypePositiveTransparencyRemoved ICScannerMeasurementUnitRemoved ICScannerMeasurementUnitCentimetersRemoved ICScannerMeasurementUnitInchesRemoved ICScannerMeasurementUnitPicasRemoved ICScannerMeasurementUnitPixelsRemoved ICScannerMeasurementUnitPointsRemoved ICScannerMeasurementUnitTwipsRemoved ICScannerPixelDataTypeRemoved ICScannerPixelDataTypeBWRemoved ICScannerPixelDataTypeCIEXYZRemoved ICScannerPixelDataTypeCMYRemoved ICScannerPixelDataTypeCMYKRemoved ICScannerPixelDataTypeGrayRemoved ICScannerPixelDataTypePaletteRemoved ICScannerPixelDataTypeRGBRemoved ICScannerPixelDataTypeYUVRemoved ICScannerPixelDataTypeYUVKRemoved ICScannerTransferModeRemoved ICScannerTransferModeFileBasedRemoved ICScannerTransferModeMemoryBasedAdded ICDeviceLocationType [enum]Added ICDeviceLocationType.BluetoothAdded ICDeviceLocationType.BonjourAdded ICDeviceLocationType.LocalAdded ICDeviceLocationType.SharedAdded ICDeviceLocationTypeMask [enum]Added ICDeviceLocationTypeMask.BluetoothAdded ICDeviceLocationTypeMask.BonjourAdded ICDeviceLocationTypeMask.LocalAdded ICDeviceLocationTypeMask.RemoteAdded ICDeviceLocationTypeMask.SharedAdded ICDeviceType [enum]Added ICDeviceType.CameraAdded ICDeviceType.ScannerAdded ICDeviceTypeMask [enum]Added ICDeviceTypeMask.CameraAdded ICDeviceTypeMask.ScannerAdded ICEXIFOrientationType [enum]Added ICEXIFOrientationType.Orientation1Added ICEXIFOrientationType.Orientation2Added ICEXIFOrientationType.Orientation3Added ICEXIFOrientationType.Orientation4Added ICEXIFOrientationType.Orientation5Added ICEXIFOrientationType.Orientation6Added ICEXIFOrientationType.Orientation7Added ICEXIFOrientationType.Orientation8Added ICReturnCode.DeviceNeedsCredentialsAdded ICScannerBitDepth [enum]Added ICScannerBitDepth.Depth16BitsAdded ICScannerBitDepth.Depth1BitAdded ICScannerBitDepth.Depth8BitsAdded ICScannerColorDataFormatType [enum]Added ICScannerColorDataFormatType.ChunkyAdded ICScannerColorDataFormatType.PlanarAdded ICScannerDocumentType [enum]Added ICScannerDocumentType.Type10Added ICScannerDocumentType.Type10RAdded ICScannerDocumentType.Type110Added ICScannerDocumentType.Type11RAdded ICScannerDocumentType.Type12RAdded ICScannerDocumentType.Type135Added ICScannerDocumentType.Type2A0Added ICScannerDocumentType.Type3RAdded ICScannerDocumentType.Type4A0Added ICScannerDocumentType.Type4RAdded ICScannerDocumentType.Type5RAdded ICScannerDocumentType.Type6RAdded ICScannerDocumentType.Type8RAdded ICScannerDocumentType.TypeA0Added ICScannerDocumentType.TypeA1Added ICScannerDocumentType.TypeA2Added ICScannerDocumentType.TypeA3Added ICScannerDocumentType.TypeA4Added ICScannerDocumentType.TypeA5Added ICScannerDocumentType.TypeA6Added ICScannerDocumentType.TypeA7Added ICScannerDocumentType.TypeA8Added ICScannerDocumentType.TypeA9Added ICScannerDocumentType.TypeAPSCAdded ICScannerDocumentType.TypeAPSHAdded ICScannerDocumentType.TypeAPSPAdded ICScannerDocumentType.TypeB5Added ICScannerDocumentType.TypeBusinessCardAdded ICScannerDocumentType.TypeC0Added ICScannerDocumentType.TypeC1Added ICScannerDocumentType.TypeC10Added ICScannerDocumentType.TypeC2Added ICScannerDocumentType.TypeC3Added ICScannerDocumentType.TypeC4Added ICScannerDocumentType.TypeC5Added ICScannerDocumentType.TypeC6Added ICScannerDocumentType.TypeC7Added ICScannerDocumentType.TypeC8Added ICScannerDocumentType.TypeC9Added ICScannerDocumentType.TypeDefaultAdded ICScannerDocumentType.TypeEAdded ICScannerDocumentType.TypeISOB0Added ICScannerDocumentType.TypeISOB1Added ICScannerDocumentType.TypeISOB10Added ICScannerDocumentType.TypeISOB2Added ICScannerDocumentType.TypeISOB3Added ICScannerDocumentType.TypeISOB4Added ICScannerDocumentType.TypeISOB5Added ICScannerDocumentType.TypeISOB6Added ICScannerDocumentType.TypeISOB7Added ICScannerDocumentType.TypeISOB8Added ICScannerDocumentType.TypeISOB9Added ICScannerDocumentType.TypeJISB0Added ICScannerDocumentType.TypeJISB1Added ICScannerDocumentType.TypeJISB10Added ICScannerDocumentType.TypeJISB2Added ICScannerDocumentType.TypeJISB3Added ICScannerDocumentType.TypeJISB4Added ICScannerDocumentType.TypeJISB6Added ICScannerDocumentType.TypeJISB7Added ICScannerDocumentType.TypeJISB8Added ICScannerDocumentType.TypeJISB9Added ICScannerDocumentType.TypeLFAdded ICScannerDocumentType.TypeMFAdded ICScannerDocumentType.TypeS10RAdded ICScannerDocumentType.TypeS12RAdded ICScannerDocumentType.TypeS8RAdded ICScannerDocumentType.TypeUSExecutiveAdded ICScannerDocumentType.TypeUSLedgerAdded ICScannerDocumentType.TypeUSLegalAdded ICScannerDocumentType.TypeUSLetterAdded ICScannerDocumentType.TypeUSStatementAdded ICScannerFeatureType [enum]Added ICScannerFeatureType.BooleanAdded ICScannerFeatureType.EnumerationAdded ICScannerFeatureType.RangeAdded ICScannerFeatureType.TemplateAdded ICScannerFunctionalUnitState [enum]Added ICScannerFunctionalUnitState.OverviewScanInProgressAdded ICScannerFunctionalUnitState.ReadyAdded ICScannerFunctionalUnitState.ScanInProgressAdded ICScannerFunctionalUnitType [enum]Added ICScannerFunctionalUnitType.DocumentFeederAdded ICScannerFunctionalUnitType.FlatbedAdded ICScannerFunctionalUnitType.NegativeTransparencyAdded ICScannerFunctionalUnitType.PositiveTransparencyAdded ICScannerMeasurementUnit [enum]Added ICScannerMeasurementUnit.CentimetersAdded ICScannerMeasurementUnit.InchesAdded ICScannerMeasurementUnit.PicasAdded ICScannerMeasurementUnit.PixelsAdded ICScannerMeasurementUnit.PointsAdded ICScannerMeasurementUnit.TwipsAdded ICScannerPixelDataType [enum]Added ICScannerPixelDataType.BWAdded ICScannerPixelDataType.CIEXYZAdded ICScannerPixelDataType.CMYAdded ICScannerPixelDataType.CMYKAdded ICScannerPixelDataType.GrayAdded ICScannerPixelDataType.PaletteAdded ICScannerPixelDataType.RGBAdded ICScannerPixelDataType.YUVAdded ICScannerPixelDataType.YUVKAdded ICScannerTransferMode [enum]Added ICScannerTransferMode.FileBasedAdded ICScannerTransferMode.MemoryBasedAdded ICCameraDeviceSupportsFastPTPModified ICCameraDevice

|  | Declaration |
| --- | --- |
| From | ``` class ICCameraDevice : ICDevice {     var batteryLevelAvailable: Bool { get }     var batteryLevel: Int { get }     var contentCatalogPercentCompleted: Int { get }     var contents: [AnyObject]! { get }     var mediaFiles: [AnyObject]! { get }     var timeOffset: NSTimeInterval { get }     var isAccessRestrictedAppleDevice: Bool { get }     var mountPoint: String! { get }     var tetheredCaptureEnabled: Bool     func filesOfType(_ fileUTType: String!) -> [AnyObject]!     func requestSyncClock()     func requestEnableTethering()     func requestDisableTethering()     func requestTakePicture()     func requestDeleteFiles(_ files: [AnyObject]!)     func cancelDelete()     func requestDownloadFile(_ file: ICCameraFile!, options options: [NSObject : AnyObject]!, downloadDelegate downloadDelegate: ICCameraDeviceDownloadDelegate!, didDownloadSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func cancelDownload()     func requestUploadFile(_ fileURL: NSURL!, options options: [NSObject : AnyObject]!, uploadDelegate uploadDelegate: AnyObject!, didUploadSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func requestReadDataFromFile(_ file: ICCameraFile!, atOffset offset: off_t, length length: off_t, readDelegate readDelegate: AnyObject!, didReadDataSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func requestSendPTPCommand(_ command: NSData!, outData data: NSData!, sendCommandDelegate sendCommandDelegate: AnyObject!, didSendCommandSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) } ``` |
| To | ``` class ICCameraDevice : ICDevice {     var batteryLevelAvailable: Bool { get }     var batteryLevel: Int { get }     var contentCatalogPercentCompleted: Int { get }     var contents: [ICCameraItem]? { get }     var mediaFiles: [ICCameraItem]? { get }     var timeOffset: NSTimeInterval { get }     var isAccessRestrictedAppleDevice: Bool { get }     var mountPoint: String? { get }     var tetheredCaptureEnabled: Bool     func filesOfType(_ fileUTType: String) -> [String]     func requestSyncClock()     func requestEnableTethering()     func requestDisableTethering()     func requestTakePicture()     func requestDeleteFiles(_ files: [ICCameraItem])     func cancelDelete()     func requestDownloadFile(_ file: ICCameraFile, options options: [String : AnyObject]?, downloadDelegate downloadDelegate: ICCameraDeviceDownloadDelegate, didDownloadSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func cancelDownload()     func requestUploadFile(_ fileURL: NSURL, options options: [String : AnyObject]?, uploadDelegate uploadDelegate: AnyObject, didUploadSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func requestReadDataFromFile(_ file: ICCameraFile, atOffset offset: off_t, length length: off_t, readDelegate readDelegate: AnyObject, didReadDataSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func requestSendPTPCommand(_ command: NSData, outData data: NSData, sendCommandDelegate sendCommandDelegate: AnyObject, didSendCommandSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) } ``` |

Modified ICCameraDevice.contents

|  | Declaration |
| --- | --- |
| From | ``` var contents: [AnyObject]! { get } ``` |
| To | ``` var contents: [ICCameraItem]? { get } ``` |

Modified ICCameraDevice.filesOfType(_: String) -> [String]

|  | Declaration |
| --- | --- |
| From | ``` func filesOfType(_ fileUTType: String!) -> [AnyObject]! ``` |
| To | ``` func filesOfType(_ fileUTType: String) -> [String] ``` |

Modified ICCameraDevice.mediaFiles

|  | Declaration |
| --- | --- |
| From | ``` var mediaFiles: [AnyObject]! { get } ``` |
| To | ``` var mediaFiles: [ICCameraItem]? { get } ``` |

Modified ICCameraDevice.mountPoint

|  | Declaration |
| --- | --- |
| From | ``` var mountPoint: String! { get } ``` |
| To | ``` var mountPoint: String? { get } ``` |

Modified ICCameraDevice.requestDeleteFiles(_: [ICCameraItem])

|  | Declaration |
| --- | --- |
| From | ``` func requestDeleteFiles(_ files: [AnyObject]!) ``` |
| To | ``` func requestDeleteFiles(_ files: [ICCameraItem]) ``` |

Modified ICCameraDevice.requestDownloadFile(_: ICCameraFile, options: [String : AnyObject]?, downloadDelegate: ICCameraDeviceDownloadDelegate, didDownloadSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func requestDownloadFile(_ file: ICCameraFile!, options options: [NSObject : AnyObject]!, downloadDelegate downloadDelegate: ICCameraDeviceDownloadDelegate!, didDownloadSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` func requestDownloadFile(_ file: ICCameraFile, options options: [String : AnyObject]?, downloadDelegate downloadDelegate: ICCameraDeviceDownloadDelegate, didDownloadSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |

Modified ICCameraDevice.requestReadDataFromFile(_: ICCameraFile, atOffset: off_t, length: off_t, readDelegate: AnyObject, didReadDataSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func requestReadDataFromFile(_ file: ICCameraFile!, atOffset offset: off_t, length length: off_t, readDelegate readDelegate: AnyObject!, didReadDataSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` func requestReadDataFromFile(_ file: ICCameraFile, atOffset offset: off_t, length length: off_t, readDelegate readDelegate: AnyObject, didReadDataSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |

Modified ICCameraDevice.requestSendPTPCommand(_: NSData, outData: NSData, sendCommandDelegate: AnyObject, didSendCommandSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func requestSendPTPCommand(_ command: NSData!, outData data: NSData!, sendCommandDelegate sendCommandDelegate: AnyObject!, didSendCommandSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` func requestSendPTPCommand(_ command: NSData, outData data: NSData, sendCommandDelegate sendCommandDelegate: AnyObject, didSendCommandSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |

Modified ICCameraDevice.requestUploadFile(_: NSURL, options: [String : AnyObject]?, uploadDelegate: AnyObject, didUploadSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func requestUploadFile(_ fileURL: NSURL!, options options: [NSObject : AnyObject]!, uploadDelegate uploadDelegate: AnyObject!, didUploadSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` func requestUploadFile(_ fileURL: NSURL, options options: [String : AnyObject]?, uploadDelegate uploadDelegate: AnyObject, didUploadSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |

Modified ICCameraDeviceDelegate

|  | Declaration |
| --- | --- |
| From | ``` protocol ICCameraDeviceDelegate : ICDeviceDelegate, NSObjectProtocol {     optional func cameraDevice(_ camera: ICCameraDevice!, didAddItem item: ICCameraItem!)     optional func cameraDevice(_ camera: ICCameraDevice!, didAddItems items: [AnyObject]!)     optional func cameraDevice(_ camera: ICCameraDevice!, didRemoveItem item: ICCameraItem!)     optional func cameraDevice(_ camera: ICCameraDevice!, didRemoveItems items: [AnyObject]!)     optional func cameraDevice(_ camera: ICCameraDevice!, didRenameItems items: [AnyObject]!)     optional func cameraDevice(_ scanner: ICCameraDevice!, didCompleteDeleteFilesWithError error: NSError!)     optional func cameraDeviceDidChangeCapability(_ camera: ICCameraDevice!)     optional func cameraDevice(_ camera: ICCameraDevice!, didReceiveThumbnailForItem item: ICCameraItem!)     optional func cameraDevice(_ camera: ICCameraDevice!, didReceiveMetadataForItem item: ICCameraItem!)     optional func cameraDevice(_ camera: ICCameraDevice!, didReceivePTPEvent eventData: NSData!)     optional func deviceDidBecomeReadyWithCompleteContentCatalog(_ device: ICDevice!)     optional func cameraDevice(_ cameraDevice: ICCameraDevice!, shouldGetThumbnailOfItem item: ICCameraItem!) -> Bool     optional func cameraDevice(_ cameraDevice: ICCameraDevice!, shouldGetMetadataOfItem item: ICCameraItem!) -> Bool } ``` |
| To | ``` protocol ICCameraDeviceDelegate : ICDeviceDelegate, NSObjectProtocol {     optional func cameraDevice(_ camera: ICCameraDevice, didAddItem item: ICCameraItem)     optional func cameraDevice(_ camera: ICCameraDevice, didAddItems items: [ICCameraItem])     optional func cameraDevice(_ camera: ICCameraDevice, didRemoveItem item: ICCameraItem)     optional func cameraDevice(_ camera: ICCameraDevice, didRemoveItems items: [ICCameraItem])     optional func cameraDevice(_ camera: ICCameraDevice, didRenameItems items: [ICCameraItem])     optional func cameraDevice(_ scanner: ICCameraDevice, didCompleteDeleteFilesWithError error: NSError?)     optional func cameraDeviceDidChangeCapability(_ camera: ICCameraDevice)     optional func cameraDevice(_ camera: ICCameraDevice, didReceiveThumbnailForItem item: ICCameraItem)     optional func cameraDevice(_ camera: ICCameraDevice, didReceiveMetadataForItem item: ICCameraItem)     optional func cameraDevice(_ camera: ICCameraDevice, didReceivePTPEvent eventData: NSData)     optional func deviceDidBecomeReadyWithCompleteContentCatalog(_ device: ICDevice)     optional func cameraDevice(_ cameraDevice: ICCameraDevice, shouldGetThumbnailOfItem item: ICCameraItem) -> Bool     optional func cameraDevice(_ cameraDevice: ICCameraDevice, shouldGetMetadataOfItem item: ICCameraItem) -> Bool } ``` |

Modified ICCameraDeviceDelegate.cameraDevice(_: ICCameraDevice, didAddItem: ICCameraItem)

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDevice(_ camera: ICCameraDevice!, didAddItem item: ICCameraItem!) ``` |
| To | ``` optional func cameraDevice(_ camera: ICCameraDevice, didAddItem item: ICCameraItem) ``` |

Modified ICCameraDeviceDelegate.cameraDevice(_: ICCameraDevice, didAddItems: [ICCameraItem])

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDevice(_ camera: ICCameraDevice!, didAddItems items: [AnyObject]!) ``` |
| To | ``` optional func cameraDevice(_ camera: ICCameraDevice, didAddItems items: [ICCameraItem]) ``` |

Modified ICCameraDeviceDelegate.cameraDevice(_: ICCameraDevice, didCompleteDeleteFilesWithError: NSError?)

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDevice(_ scanner: ICCameraDevice!, didCompleteDeleteFilesWithError error: NSError!) ``` |
| To | ``` optional func cameraDevice(_ scanner: ICCameraDevice, didCompleteDeleteFilesWithError error: NSError?) ``` |

Modified ICCameraDeviceDelegate.cameraDevice(_: ICCameraDevice, didReceiveMetadataForItem: ICCameraItem)

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDevice(_ camera: ICCameraDevice!, didReceiveMetadataForItem item: ICCameraItem!) ``` |
| To | ``` optional func cameraDevice(_ camera: ICCameraDevice, didReceiveMetadataForItem item: ICCameraItem) ``` |

Modified ICCameraDeviceDelegate.cameraDevice(_: ICCameraDevice, didReceivePTPEvent: NSData)

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDevice(_ camera: ICCameraDevice!, didReceivePTPEvent eventData: NSData!) ``` |
| To | ``` optional func cameraDevice(_ camera: ICCameraDevice, didReceivePTPEvent eventData: NSData) ``` |

Modified ICCameraDeviceDelegate.cameraDevice(_: ICCameraDevice, didReceiveThumbnailForItem: ICCameraItem)

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDevice(_ camera: ICCameraDevice!, didReceiveThumbnailForItem item: ICCameraItem!) ``` |
| To | ``` optional func cameraDevice(_ camera: ICCameraDevice, didReceiveThumbnailForItem item: ICCameraItem) ``` |

Modified ICCameraDeviceDelegate.cameraDevice(_: ICCameraDevice, didRemoveItem: ICCameraItem)

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDevice(_ camera: ICCameraDevice!, didRemoveItem item: ICCameraItem!) ``` |
| To | ``` optional func cameraDevice(_ camera: ICCameraDevice, didRemoveItem item: ICCameraItem) ``` |

Modified ICCameraDeviceDelegate.cameraDevice(_: ICCameraDevice, didRemoveItems: [ICCameraItem])

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDevice(_ camera: ICCameraDevice!, didRemoveItems items: [AnyObject]!) ``` |
| To | ``` optional func cameraDevice(_ camera: ICCameraDevice, didRemoveItems items: [ICCameraItem]) ``` |

Modified ICCameraDeviceDelegate.cameraDevice(_: ICCameraDevice, didRenameItems: [ICCameraItem])

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDevice(_ camera: ICCameraDevice!, didRenameItems items: [AnyObject]!) ``` |
| To | ``` optional func cameraDevice(_ camera: ICCameraDevice, didRenameItems items: [ICCameraItem]) ``` |

Modified ICCameraDeviceDelegate.cameraDevice(_: ICCameraDevice, shouldGetMetadataOfItem: ICCameraItem) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDevice(_ cameraDevice: ICCameraDevice!, shouldGetMetadataOfItem item: ICCameraItem!) -> Bool ``` |
| To | ``` optional func cameraDevice(_ cameraDevice: ICCameraDevice, shouldGetMetadataOfItem item: ICCameraItem) -> Bool ``` |

Modified ICCameraDeviceDelegate.cameraDevice(_: ICCameraDevice, shouldGetThumbnailOfItem: ICCameraItem) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDevice(_ cameraDevice: ICCameraDevice!, shouldGetThumbnailOfItem item: ICCameraItem!) -> Bool ``` |
| To | ``` optional func cameraDevice(_ cameraDevice: ICCameraDevice, shouldGetThumbnailOfItem item: ICCameraItem) -> Bool ``` |

Modified ICCameraDeviceDelegate.cameraDeviceDidChangeCapability(_: ICCameraDevice)

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDeviceDidChangeCapability(_ camera: ICCameraDevice!) ``` |
| To | ``` optional func cameraDeviceDidChangeCapability(_ camera: ICCameraDevice) ``` |

Modified ICCameraDeviceDelegate.deviceDidBecomeReadyWithCompleteContentCatalog(_: ICDevice)

|  | Declaration |
| --- | --- |
| From | ``` optional func deviceDidBecomeReadyWithCompleteContentCatalog(_ device: ICDevice!) ``` |
| To | ``` optional func deviceDidBecomeReadyWithCompleteContentCatalog(_ device: ICDevice) ``` |

Modified ICCameraDeviceDownloadDelegate

|  | Declaration |
| --- | --- |
| From | ``` protocol ICCameraDeviceDownloadDelegate : NSObjectProtocol {     optional func didDownloadFile(_ file: ICCameraFile!, error error: NSError!, options options: [NSObject : AnyObject]!, contextInfo contextInfo: UnsafeMutablePointer<Void>)     optional func didReceiveDownloadProgressForFile(_ file: ICCameraFile!, downloadedBytes downloadedBytes: off_t, maxBytes maxBytes: off_t) } ``` |
| To | ``` protocol ICCameraDeviceDownloadDelegate : NSObjectProtocol {     optional func didDownloadFile(_ file: ICCameraFile, error error: NSError?, options options: [String : AnyObject]?, contextInfo contextInfo: UnsafeMutablePointer<Void>)     optional func didReceiveDownloadProgressForFile(_ file: ICCameraFile, downloadedBytes downloadedBytes: off_t, maxBytes maxBytes: off_t) } ``` |

Modified ICCameraDeviceDownloadDelegate.didDownloadFile(_: ICCameraFile, error: NSError?, options: [String : AnyObject]?, contextInfo: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` optional func didDownloadFile(_ file: ICCameraFile!, error error: NSError!, options options: [NSObject : AnyObject]!, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` optional func didDownloadFile(_ file: ICCameraFile, error error: NSError?, options options: [String : AnyObject]?, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |

Modified ICCameraDeviceDownloadDelegate.didReceiveDownloadProgressForFile(_: ICCameraFile, downloadedBytes: off_t, maxBytes: off_t)

|  | Declaration |
| --- | --- |
| From | ``` optional func didReceiveDownloadProgressForFile(_ file: ICCameraFile!, downloadedBytes downloadedBytes: off_t, maxBytes maxBytes: off_t) ``` |
| To | ``` optional func didReceiveDownloadProgressForFile(_ file: ICCameraFile, downloadedBytes downloadedBytes: off_t, maxBytes maxBytes: off_t) ``` |

Modified ICCameraFile

|  | Declaration |
| --- | --- |
| From | ``` class ICCameraFile : ICCameraItem {     var fileSize: off_t { get }     var orientation: ICEXIFOrientationType     var duration: Double { get }     var sidecarFiles: [AnyObject]! { get } } ``` |
| To | ``` class ICCameraFile : ICCameraItem {     var fileSize: off_t { get }     var orientation: ICEXIFOrientationType     var duration: Double { get }     var sidecarFiles: [ICCameraItem] { get } } ``` |

Modified ICCameraFile.sidecarFiles

|  | Declaration |
| --- | --- |
| From | ``` var sidecarFiles: [AnyObject]! { get } ``` |
| To | ``` var sidecarFiles: [ICCameraItem] { get } ``` |

Modified ICCameraFolder

|  | Declaration |
| --- | --- |
| From | ``` class ICCameraFolder : ICCameraItem {     var contents: [AnyObject]! { get } } ``` |
| To | ``` class ICCameraFolder : ICCameraItem {     var contents: [ICCameraItem] { get } } ``` |

Modified ICCameraFolder.contents

|  | Declaration |
| --- | --- |
| From | ``` var contents: [AnyObject]! { get } ``` |
| To | ``` var contents: [ICCameraItem] { get } ``` |

Modified ICCameraItem

|  | Declaration |
| --- | --- |
| From | ``` class ICCameraItem : NSObject {     var device: ICCameraDevice! { get }     var parentFolder: ICCameraFolder! { get }     var name: String! { get }     var UTI: String! { get }     var fileSystemPath: String! { get }     var locked: Bool { get }     var raw: Bool { get }     var inTemporaryStore: Bool { get }     var creationDate: NSDate! { get }     var modificationDate: NSDate! { get }     var thumbnailIfAvailable: CGImage! { get }     var largeThumbnailIfAvailable: CGImage! { get }     var metadataIfAvailable: [NSObject : AnyObject]! { get }     var userData: NSMutableDictionary! { get }     var ptpObjectHandle: UInt32 { get }     var addedAfterContentCatalogCompleted: Bool { get } } ``` |
| To | ``` class ICCameraItem : NSObject {     var device: ICCameraDevice { get }     var parentFolder: ICCameraFolder { get }     var name: String { get }     var UTI: String { get }     var fileSystemPath: String { get }     var locked: Bool { get }     var raw: Bool { get }     var inTemporaryStore: Bool { get }     var creationDate: NSDate { get }     var modificationDate: NSDate { get }     var thumbnailIfAvailable: CGImage? { get }     var largeThumbnailIfAvailable: CGImage? { get }     var metadataIfAvailable: [String : AnyObject]? { get }     var userData: NSMutableDictionary? { get }     var ptpObjectHandle: UInt32 { get }     var addedAfterContentCatalogCompleted: Bool { get } } ``` |

Modified ICCameraItem.creationDate

|  | Declaration |
| --- | --- |
| From | ``` var creationDate: NSDate! { get } ``` |
| To | ``` var creationDate: NSDate { get } ``` |

Modified ICCameraItem.device

|  | Declaration |
| --- | --- |
| From | ``` var device: ICCameraDevice! { get } ``` |
| To | ``` var device: ICCameraDevice { get } ``` |

Modified ICCameraItem.fileSystemPath

|  | Declaration |
| --- | --- |
| From | ``` var fileSystemPath: String! { get } ``` |
| To | ``` var fileSystemPath: String { get } ``` |

Modified ICCameraItem.largeThumbnailIfAvailable

|  | Declaration |
| --- | --- |
| From | ``` var largeThumbnailIfAvailable: CGImage! { get } ``` |
| To | ``` var largeThumbnailIfAvailable: CGImage? { get } ``` |

Modified ICCameraItem.metadataIfAvailable

|  | Declaration |
| --- | --- |
| From | ``` var metadataIfAvailable: [NSObject : AnyObject]! { get } ``` |
| To | ``` var metadataIfAvailable: [String : AnyObject]? { get } ``` |

Modified ICCameraItem.modificationDate

|  | Declaration |
| --- | --- |
| From | ``` var modificationDate: NSDate! { get } ``` |
| To | ``` var modificationDate: NSDate { get } ``` |

Modified ICCameraItem.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified ICCameraItem.parentFolder

|  | Declaration |
| --- | --- |
| From | ``` var parentFolder: ICCameraFolder! { get } ``` |
| To | ``` var parentFolder: ICCameraFolder { get } ``` |

Modified ICCameraItem.thumbnailIfAvailable

|  | Declaration |
| --- | --- |
| From | ``` var thumbnailIfAvailable: CGImage! { get } ``` |
| To | ``` var thumbnailIfAvailable: CGImage? { get } ``` |

Modified ICCameraItem.userData

|  | Declaration |
| --- | --- |
| From | ``` var userData: NSMutableDictionary! { get } ``` |
| To | ``` var userData: NSMutableDictionary? { get } ``` |

Modified ICCameraItem.UTI

|  | Declaration |
| --- | --- |
| From | ``` var UTI: String! { get } ``` |
| To | ``` var UTI: String { get } ``` |

Modified ICDevice

|  | Declaration |
| --- | --- |
| From | ``` class ICDevice : NSObject {     unowned(unsafe) var delegate: ICDeviceDelegate!     var type: ICDeviceType { get }     var name: String! { get }     var icon: CGImage! { get }     var capabilities: [AnyObject]! { get }     var modulePath: String! { get }     var moduleVersion: String! { get }     var moduleExecutableArchitecture: Int32 { get }     var remote: Bool { get }     var shared: Bool { get }     var hasConfigurableWiFiInterface: Bool { get }     var transportType: String! { get }     var usbLocationID: Int32 { get }     var usbProductID: Int32 { get }     var usbVendorID: Int32 { get }     var fwGUID: Int64 { get }     var serialNumberString: String! { get }     var locationDescription: String! { get }     var hasOpenSession: Bool { get }     var UUIDString: String! { get }     var persistentIDString: String! { get }     var buttonPressed: String! { get }     var autolaunchApplicationPath: String!     var userData: NSMutableDictionary! { get }     func requestOpenSession()     func requestCloseSession()     func requestYield()     func requestSendMessage(_ messageCode: UInt32, outData data: NSData!, maxReturnedDataSize maxReturnedDataSize: UInt32, sendMessageDelegate sendMessageDelegate: AnyObject!, didSendMessageSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func requestEjectOrDisconnect() } ``` |
| To | ``` class ICDevice : NSObject {     unowned(unsafe) var delegate: ICDeviceDelegate?     var type: ICDeviceType { get }     var name: String? { get }     var icon: CGImage? { get }     var capabilities: [String] { get }     var modulePath: String { get }     var moduleVersion: String { get }     var moduleExecutableArchitecture: Int32 { get }     var remote: Bool { get }     var shared: Bool { get }     var hasConfigurableWiFiInterface: Bool { get }     var transportType: String { get }     var usbLocationID: Int32 { get }     var usbProductID: Int32 { get }     var usbVendorID: Int32 { get }     var fwGUID: Int64 { get }     var serialNumberString: String? { get }     var locationDescription: String? { get }     var hasOpenSession: Bool { get }     var UUIDString: String? { get }     var persistentIDString: String? { get }     var buttonPressed: String { get }     var autolaunchApplicationPath: String?     var userData: NSMutableDictionary? { get }     func requestOpenSession()     func requestCloseSession()     func requestYield()     func requestSendMessage(_ messageCode: UInt32, outData data: NSData, maxReturnedDataSize maxReturnedDataSize: UInt32, sendMessageDelegate sendMessageDelegate: AnyObject, didSendMessageSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func requestEjectOrDisconnect() } ``` |

Modified ICDevice.autolaunchApplicationPath

|  | Declaration |
| --- | --- |
| From | ``` var autolaunchApplicationPath: String! ``` |
| To | ``` var autolaunchApplicationPath: String? ``` |

Modified ICDevice.buttonPressed

|  | Declaration |
| --- | --- |
| From | ``` var buttonPressed: String! { get } ``` |
| To | ``` var buttonPressed: String { get } ``` |

Modified ICDevice.capabilities

|  | Declaration |
| --- | --- |
| From | ``` var capabilities: [AnyObject]! { get } ``` |
| To | ``` var capabilities: [String] { get } ``` |

Modified ICDevice.delegate

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: ICDeviceDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: ICDeviceDelegate? ``` |

Modified ICDevice.icon

|  | Declaration |
| --- | --- |
| From | ``` var icon: CGImage! { get } ``` |
| To | ``` var icon: CGImage? { get } ``` |

Modified ICDevice.locationDescription

|  | Declaration |
| --- | --- |
| From | ``` var locationDescription: String! { get } ``` |
| To | ``` var locationDescription: String? { get } ``` |

Modified ICDevice.modulePath

|  | Declaration |
| --- | --- |
| From | ``` var modulePath: String! { get } ``` |
| To | ``` var modulePath: String { get } ``` |

Modified ICDevice.moduleVersion

|  | Declaration |
| --- | --- |
| From | ``` var moduleVersion: String! { get } ``` |
| To | ``` var moduleVersion: String { get } ``` |

Modified ICDevice.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String? { get } ``` |

Modified ICDevice.persistentIDString

|  | Declaration |
| --- | --- |
| From | ``` var persistentIDString: String! { get } ``` |
| To | ``` var persistentIDString: String? { get } ``` |

Modified ICDevice.requestSendMessage(_: UInt32, outData: NSData, maxReturnedDataSize: UInt32, sendMessageDelegate: AnyObject, didSendMessageSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func requestSendMessage(_ messageCode: UInt32, outData data: NSData!, maxReturnedDataSize maxReturnedDataSize: UInt32, sendMessageDelegate sendMessageDelegate: AnyObject!, didSendMessageSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` func requestSendMessage(_ messageCode: UInt32, outData data: NSData, maxReturnedDataSize maxReturnedDataSize: UInt32, sendMessageDelegate sendMessageDelegate: AnyObject, didSendMessageSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |

Modified ICDevice.serialNumberString

|  | Declaration |
| --- | --- |
| From | ``` var serialNumberString: String! { get } ``` |
| To | ``` var serialNumberString: String? { get } ``` |

Modified ICDevice.transportType

|  | Declaration |
| --- | --- |
| From | ``` var transportType: String! { get } ``` |
| To | ``` var transportType: String { get } ``` |

Modified ICDevice.userData

|  | Declaration |
| --- | --- |
| From | ``` var userData: NSMutableDictionary! { get } ``` |
| To | ``` var userData: NSMutableDictionary? { get } ``` |

Modified ICDevice.UUIDString

|  | Declaration |
| --- | --- |
| From | ``` var UUIDString: String! { get } ``` |
| To | ``` var UUIDString: String? { get } ``` |

Modified ICDeviceBrowser

|  | Declaration |
| --- | --- |
| From | ``` class ICDeviceBrowser : NSObject {     unowned(unsafe) var delegate: ICDeviceBrowserDelegate!     var browsing: Bool { get }     var browsedDeviceTypeMask: ICDeviceTypeMask     var devices: [AnyObject]! { get }     func preferredDevice() -> ICDevice!     init!()     func start()     func stop() } ``` |
| To | ``` class ICDeviceBrowser : NSObject {     unowned(unsafe) var delegate: ICDeviceBrowserDelegate?     var browsing: Bool { get }     var browsedDeviceTypeMask: ICDeviceTypeMask     var devices: [ICDevice]? { get }     func preferredDevice() -> ICDevice     init()     func start()     func stop() } ``` |

Modified ICDeviceBrowser.delegate

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: ICDeviceBrowserDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: ICDeviceBrowserDelegate? ``` |

Modified ICDeviceBrowser.devices

|  | Declaration |
| --- | --- |
| From | ``` var devices: [AnyObject]! { get } ``` |
| To | ``` var devices: [ICDevice]? { get } ``` |

Modified ICDeviceBrowser.init()

|  | Declaration |
| --- | --- |
| From | ``` init!() ``` |
| To | ``` init() ``` |

Modified ICDeviceBrowser.preferredDevice() -> ICDevice

|  | Declaration |
| --- | --- |
| From | ``` func preferredDevice() -> ICDevice! ``` |
| To | ``` func preferredDevice() -> ICDevice ``` |

Modified ICDeviceBrowserDelegate

|  | Declaration |
| --- | --- |
| From | ``` protocol ICDeviceBrowserDelegate : NSObjectProtocol {     func deviceBrowser(_ browser: ICDeviceBrowser!, didAddDevice device: ICDevice!, moreComing moreComing: Bool)     func deviceBrowser(_ browser: ICDeviceBrowser!, didRemoveDevice device: ICDevice!, moreGoing moreGoing: Bool)     optional func deviceBrowser(_ browser: ICDeviceBrowser!, deviceDidChangeName device: ICDevice!)     optional func deviceBrowser(_ browser: ICDeviceBrowser!, deviceDidChangeSharingState device: ICDevice!)     optional func deviceBrowser(_ browser: ICDeviceBrowser!, requestsSelectDevice device: ICDevice!)     optional func deviceBrowserDidEnumerateLocalDevices(_ browser: ICDeviceBrowser!) } ``` |
| To | ``` protocol ICDeviceBrowserDelegate : NSObjectProtocol {     func deviceBrowser(_ browser: ICDeviceBrowser, didAddDevice device: ICDevice, moreComing moreComing: Bool)     func deviceBrowser(_ browser: ICDeviceBrowser, didRemoveDevice device: ICDevice, moreGoing moreGoing: Bool)     optional func deviceBrowser(_ browser: ICDeviceBrowser, deviceDidChangeName device: ICDevice)     optional func deviceBrowser(_ browser: ICDeviceBrowser, deviceDidChangeSharingState device: ICDevice)     optional func deviceBrowser(_ browser: ICDeviceBrowser, requestsSelectDevice device: ICDevice)     optional func deviceBrowserDidEnumerateLocalDevices(_ browser: ICDeviceBrowser) } ``` |

Modified ICDeviceBrowserDelegate.deviceBrowser(_: ICDeviceBrowser, deviceDidChangeName: ICDevice)

|  | Declaration |
| --- | --- |
| From | ``` optional func deviceBrowser(_ browser: ICDeviceBrowser!, deviceDidChangeName device: ICDevice!) ``` |
| To | ``` optional func deviceBrowser(_ browser: ICDeviceBrowser, deviceDidChangeName device: ICDevice) ``` |

Modified ICDeviceBrowserDelegate.deviceBrowser(_: ICDeviceBrowser, deviceDidChangeSharingState: ICDevice)

|  | Declaration |
| --- | --- |
| From | ``` optional func deviceBrowser(_ browser: ICDeviceBrowser!, deviceDidChangeSharingState device: ICDevice!) ``` |
| To | ``` optional func deviceBrowser(_ browser: ICDeviceBrowser, deviceDidChangeSharingState device: ICDevice) ``` |

Modified ICDeviceBrowserDelegate.deviceBrowser(_: ICDeviceBrowser, didAddDevice: ICDevice, moreComing: Bool)

|  | Declaration |
| --- | --- |
| From | ``` func deviceBrowser(_ browser: ICDeviceBrowser!, didAddDevice device: ICDevice!, moreComing moreComing: Bool) ``` |
| To | ``` func deviceBrowser(_ browser: ICDeviceBrowser, didAddDevice device: ICDevice, moreComing moreComing: Bool) ``` |

Modified ICDeviceBrowserDelegate.deviceBrowser(_: ICDeviceBrowser, didRemoveDevice: ICDevice, moreGoing: Bool)

|  | Declaration |
| --- | --- |
| From | ``` func deviceBrowser(_ browser: ICDeviceBrowser!, didRemoveDevice device: ICDevice!, moreGoing moreGoing: Bool) ``` |
| To | ``` func deviceBrowser(_ browser: ICDeviceBrowser, didRemoveDevice device: ICDevice, moreGoing moreGoing: Bool) ``` |

Modified ICDeviceBrowserDelegate.deviceBrowser(_: ICDeviceBrowser, requestsSelectDevice: ICDevice)

|  | Declaration |
| --- | --- |
| From | ``` optional func deviceBrowser(_ browser: ICDeviceBrowser!, requestsSelectDevice device: ICDevice!) ``` |
| To | ``` optional func deviceBrowser(_ browser: ICDeviceBrowser, requestsSelectDevice device: ICDevice) ``` |

Modified ICDeviceBrowserDelegate.deviceBrowserDidEnumerateLocalDevices(_: ICDeviceBrowser)

|  | Declaration |
| --- | --- |
| From | ``` optional func deviceBrowserDidEnumerateLocalDevices(_ browser: ICDeviceBrowser!) ``` |
| To | ``` optional func deviceBrowserDidEnumerateLocalDevices(_ browser: ICDeviceBrowser) ``` |

Modified ICDeviceDelegate

|  | Declaration |
| --- | --- |
| From | ``` protocol ICDeviceDelegate : NSObjectProtocol {     func didRemoveDevice(_ device: ICDevice!)     optional func device(_ device: ICDevice!, didOpenSessionWithError error: NSError!)     optional func deviceDidBecomeReady(_ device: ICDevice!)     optional func device(_ device: ICDevice!, didCloseSessionWithError error: NSError!)     optional func deviceDidChangeName(_ device: ICDevice!)     optional func deviceDidChangeSharingState(_ device: ICDevice!)     optional func device(_ device: ICDevice!, didReceiveStatusInformation status: [NSObject : AnyObject]!)     optional func device(_ device: ICDevice!, didEncounterError error: NSError!)     optional func device(_ device: ICDevice!, didReceiveButtonPress buttonType: String!)     optional func device(_ device: ICDevice!, didReceiveCustomNotification notification: [NSObject : AnyObject]!, data data: NSData!) } ``` |
| To | ``` protocol ICDeviceDelegate : NSObjectProtocol {     func didRemoveDevice(_ device: ICDevice)     optional func device(_ device: ICDevice, didOpenSessionWithError error: NSError?)     optional func deviceDidBecomeReady(_ device: ICDevice)     optional func device(_ device: ICDevice, didCloseSessionWithError error: NSError?)     optional func deviceDidChangeName(_ device: ICDevice)     optional func deviceDidChangeSharingState(_ device: ICDevice)     optional func device(_ device: ICDevice, didReceiveStatusInformation status: [String : AnyObject])     optional func device(_ device: ICDevice, didEncounterError error: NSError?)     optional func device(_ device: ICDevice, didReceiveButtonPress buttonType: String)     optional func device(_ device: ICDevice, didReceiveCustomNotification notification: [String : AnyObject], data data: NSData) } ``` |

Modified ICDeviceDelegate.device(_: ICDevice, didCloseSessionWithError: NSError?)

|  | Declaration |
| --- | --- |
| From | ``` optional func device(_ device: ICDevice!, didCloseSessionWithError error: NSError!) ``` |
| To | ``` optional func device(_ device: ICDevice, didCloseSessionWithError error: NSError?) ``` |

Modified ICDeviceDelegate.device(_: ICDevice, didEncounterError: NSError?)

|  | Declaration |
| --- | --- |
| From | ``` optional func device(_ device: ICDevice!, didEncounterError error: NSError!) ``` |
| To | ``` optional func device(_ device: ICDevice, didEncounterError error: NSError?) ``` |

Modified ICDeviceDelegate.device(_: ICDevice, didOpenSessionWithError: NSError?)

|  | Declaration |
| --- | --- |
| From | ``` optional func device(_ device: ICDevice!, didOpenSessionWithError error: NSError!) ``` |
| To | ``` optional func device(_ device: ICDevice, didOpenSessionWithError error: NSError?) ``` |

Modified ICDeviceDelegate.device(_: ICDevice, didReceiveButtonPress: String)

|  | Declaration |
| --- | --- |
| From | ``` optional func device(_ device: ICDevice!, didReceiveButtonPress buttonType: String!) ``` |
| To | ``` optional func device(_ device: ICDevice, didReceiveButtonPress buttonType: String) ``` |

Modified ICDeviceDelegate.device(_: ICDevice, didReceiveCustomNotification: [String : AnyObject], data: NSData)

|  | Declaration |
| --- | --- |
| From | ``` optional func device(_ device: ICDevice!, didReceiveCustomNotification notification: [NSObject : AnyObject]!, data data: NSData!) ``` |
| To | ``` optional func device(_ device: ICDevice, didReceiveCustomNotification notification: [String : AnyObject], data data: NSData) ``` |

Modified ICDeviceDelegate.device(_: ICDevice, didReceiveStatusInformation: [String : AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` optional func device(_ device: ICDevice!, didReceiveStatusInformation status: [NSObject : AnyObject]!) ``` |
| To | ``` optional func device(_ device: ICDevice, didReceiveStatusInformation status: [String : AnyObject]) ``` |

Modified ICDeviceDelegate.deviceDidBecomeReady(_: ICDevice)

|  | Declaration |
| --- | --- |
| From | ``` optional func deviceDidBecomeReady(_ device: ICDevice!) ``` |
| To | ``` optional func deviceDidBecomeReady(_ device: ICDevice) ``` |

Modified ICDeviceDelegate.deviceDidChangeName(_: ICDevice)

|  | Declaration |
| --- | --- |
| From | ``` optional func deviceDidChangeName(_ device: ICDevice!) ``` |
| To | ``` optional func deviceDidChangeName(_ device: ICDevice) ``` |

Modified ICDeviceDelegate.deviceDidChangeSharingState(_: ICDevice)

|  | Declaration |
| --- | --- |
| From | ``` optional func deviceDidChangeSharingState(_ device: ICDevice!) ``` |
| To | ``` optional func deviceDidChangeSharingState(_ device: ICDevice) ``` |

Modified ICDeviceDelegate.didRemoveDevice(_: ICDevice)

|  | Declaration |
| --- | --- |
| From | ``` func didRemoveDevice(_ device: ICDevice!) ``` |
| To | ``` func didRemoveDevice(_ device: ICDevice) ``` |

Modified ICReturnCode [enum]

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct ICReturnCode {     init(_ value: Int32)     var value: Int32 } ``` | -- | OS X 10.10 | -- |
| To | ``` enum ICReturnCode : Int {     case Success     case InvalidParam     case CommunicationTimedOut     case ScanOperationCanceled     case ScannerInUseByLocalUser     case ScannerInUseByRemoteUser     case DeviceFailedToOpenSession     case DeviceFailedToCloseSession     case ScannerFailedToSelectFunctionalUnit     case ScannerFailedToCompleteOverviewScan     case ScannerFailedToCompleteScan     case ReceivedUnsolicitedScannerStatusInfo     case ReceivedUnsolicitedScannerErrorInfo     case DownloadFailed     case UploadFailed     case FailedToCompletePassThroughCommand     case DownloadCanceled     case FailedToEnabeTethering     case FailedToDisabeTethering     case FailedToCompleteSendMessageRequest     case DeleteFilesFailed     case DeleteFilesCanceled     case DeviceIsPasscodeLocked     case DeviceFailedToTakePicture     case DeviceSoftwareNotInstalled     case DeviceSoftwareIsBeingInstalled     case DeviceSoftwareInstallationCompleted     case DeviceSoftwareInstallationCanceled     case DeviceSoftwareInstallationFailed     case DeviceSoftwareNotAvailable     case DeviceCouldNotPair     case DeviceCouldNotUnpair     case DeviceNeedsCredentials } ``` | Equatable, Hashable, RawRepresentable | OS X 10.11 | Int |

Modified ICReturnCode.CommunicationTimedOut

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnCommunicationTimedOut | ``` var ICReturnCommunicationTimedOut: ICReturnCode { get } ``` | OS X 10.10 |
| To | CommunicationTimedOut | ``` case CommunicationTimedOut ``` | OS X 10.11 |

Modified ICReturnCode.DeleteFilesCanceled

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnDeleteFilesCanceled | ``` var ICReturnDeleteFilesCanceled: ICReturnCode { get } ``` | OS X 10.10 |
| To | DeleteFilesCanceled | ``` case DeleteFilesCanceled ``` | OS X 10.11 |

Modified ICReturnCode.DeleteFilesFailed

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnDeleteFilesFailed | ``` var ICReturnDeleteFilesFailed: ICReturnCode { get } ``` | OS X 10.10 |
| To | DeleteFilesFailed | ``` case DeleteFilesFailed ``` | OS X 10.11 |

Modified ICReturnCode.DeviceCouldNotPair

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnDeviceCouldNotPair | ``` var ICReturnDeviceCouldNotPair: ICReturnCode { get } ``` | OS X 10.10.3 |
| To | DeviceCouldNotPair | ``` case DeviceCouldNotPair ``` | OS X 10.11 |

Modified ICReturnCode.DeviceCouldNotUnpair

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnDeviceCouldNotUnpair | ``` var ICReturnDeviceCouldNotUnpair: ICReturnCode { get } ``` | OS X 10.10.3 |
| To | DeviceCouldNotUnpair | ``` case DeviceCouldNotUnpair ``` | OS X 10.11 |

Modified ICReturnCode.DeviceFailedToCloseSession

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnDeviceFailedToCloseSession | ``` var ICReturnDeviceFailedToCloseSession: ICReturnCode { get } ``` | OS X 10.10 |
| To | DeviceFailedToCloseSession | ``` case DeviceFailedToCloseSession ``` | OS X 10.11 |

Modified ICReturnCode.DeviceFailedToOpenSession

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnDeviceFailedToOpenSession | ``` var ICReturnDeviceFailedToOpenSession: ICReturnCode { get } ``` | OS X 10.10 |
| To | DeviceFailedToOpenSession | ``` case DeviceFailedToOpenSession ``` | OS X 10.11 |

Modified ICReturnCode.DeviceFailedToTakePicture

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnDeviceFailedToTakePicture | ``` var ICReturnDeviceFailedToTakePicture: ICReturnCode { get } ``` | OS X 10.10 |
| To | DeviceFailedToTakePicture | ``` case DeviceFailedToTakePicture ``` | OS X 10.11 |

Modified ICReturnCode.DeviceIsPasscodeLocked

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnDeviceIsPasscodeLocked | ``` var ICReturnDeviceIsPasscodeLocked: ICReturnCode { get } ``` | OS X 10.10 |
| To | DeviceIsPasscodeLocked | ``` case DeviceIsPasscodeLocked ``` | OS X 10.11 |

Modified ICReturnCode.DeviceSoftwareInstallationCanceled

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnDeviceSoftwareInstallationCanceled | ``` var ICReturnDeviceSoftwareInstallationCanceled: ICReturnCode { get } ``` | OS X 10.10 |
| To | DeviceSoftwareInstallationCanceled | ``` case DeviceSoftwareInstallationCanceled ``` | OS X 10.11 |

Modified ICReturnCode.DeviceSoftwareInstallationCompleted

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnDeviceSoftwareInstallationCompleted | ``` var ICReturnDeviceSoftwareInstallationCompleted: ICReturnCode { get } ``` | OS X 10.10 |
| To | DeviceSoftwareInstallationCompleted | ``` case DeviceSoftwareInstallationCompleted ``` | OS X 10.11 |

Modified ICReturnCode.DeviceSoftwareInstallationFailed

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnDeviceSoftwareInstallationFailed | ``` var ICReturnDeviceSoftwareInstallationFailed: ICReturnCode { get } ``` | OS X 10.10 |
| To | DeviceSoftwareInstallationFailed | ``` case DeviceSoftwareInstallationFailed ``` | OS X 10.11 |

Modified ICReturnCode.DeviceSoftwareIsBeingInstalled

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnDeviceSoftwareIsBeingInstalled | ``` var ICReturnDeviceSoftwareIsBeingInstalled: ICReturnCode { get } ``` | OS X 10.10 |
| To | DeviceSoftwareIsBeingInstalled | ``` case DeviceSoftwareIsBeingInstalled ``` | OS X 10.11 |

Modified ICReturnCode.DeviceSoftwareNotAvailable

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnDeviceSoftwareNotAvailable | ``` var ICReturnDeviceSoftwareNotAvailable: ICReturnCode { get } ``` | OS X 10.10 |
| To | DeviceSoftwareNotAvailable | ``` case DeviceSoftwareNotAvailable ``` | OS X 10.11 |

Modified ICReturnCode.DeviceSoftwareNotInstalled

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnDeviceSoftwareNotInstalled | ``` var ICReturnDeviceSoftwareNotInstalled: ICReturnCode { get } ``` | OS X 10.10 |
| To | DeviceSoftwareNotInstalled | ``` case DeviceSoftwareNotInstalled ``` | OS X 10.11 |

Modified ICReturnCode.DownloadCanceled

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnDownloadCanceled | ``` var ICReturnDownloadCanceled: ICReturnCode { get } ``` | OS X 10.10 |
| To | DownloadCanceled | ``` case DownloadCanceled ``` | OS X 10.11 |

Modified ICReturnCode.DownloadFailed

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnDownloadFailed | ``` var ICReturnDownloadFailed: ICReturnCode { get } ``` | OS X 10.10 |
| To | DownloadFailed | ``` case DownloadFailed ``` | OS X 10.11 |

Modified ICReturnCode.FailedToCompletePassThroughCommand

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnFailedToCompletePassThroughCommand | ``` var ICReturnFailedToCompletePassThroughCommand: ICReturnCode { get } ``` | OS X 10.10 |
| To | FailedToCompletePassThroughCommand | ``` case FailedToCompletePassThroughCommand ``` | OS X 10.11 |

Modified ICReturnCode.FailedToCompleteSendMessageRequest

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnFailedToCompleteSendMessageRequest | ``` var ICReturnFailedToCompleteSendMessageRequest: ICReturnCode { get } ``` | OS X 10.10 |
| To | FailedToCompleteSendMessageRequest | ``` case FailedToCompleteSendMessageRequest ``` | OS X 10.11 |

Modified ICReturnCode.FailedToDisabeTethering

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnFailedToDisabeTethering | ``` var ICReturnFailedToDisabeTethering: ICReturnCode { get } ``` | OS X 10.10 |
| To | FailedToDisabeTethering | ``` case FailedToDisabeTethering ``` | OS X 10.11 |

Modified ICReturnCode.FailedToEnabeTethering

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnFailedToEnabeTethering | ``` var ICReturnFailedToEnabeTethering: ICReturnCode { get } ``` | OS X 10.10 |
| To | FailedToEnabeTethering | ``` case FailedToEnabeTethering ``` | OS X 10.11 |

Modified ICReturnCode.InvalidParam

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnInvalidParam | ``` var ICReturnInvalidParam: ICReturnCode { get } ``` | OS X 10.10 |
| To | InvalidParam | ``` case InvalidParam ``` | OS X 10.11 |

Modified ICReturnCode.ReceivedUnsolicitedScannerErrorInfo

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnReceivedUnsolicitedScannerErrorInfo | ``` var ICReturnReceivedUnsolicitedScannerErrorInfo: ICReturnCode { get } ``` | OS X 10.10 |
| To | ReceivedUnsolicitedScannerErrorInfo | ``` case ReceivedUnsolicitedScannerErrorInfo ``` | OS X 10.11 |

Modified ICReturnCode.ReceivedUnsolicitedScannerStatusInfo

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnReceivedUnsolicitedScannerStatusInfo | ``` var ICReturnReceivedUnsolicitedScannerStatusInfo: ICReturnCode { get } ``` | OS X 10.10 |
| To | ReceivedUnsolicitedScannerStatusInfo | ``` case ReceivedUnsolicitedScannerStatusInfo ``` | OS X 10.11 |

Modified ICReturnCode.ScannerFailedToCompleteOverviewScan

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnScannerFailedToCompleteOverviewScan | ``` var ICReturnScannerFailedToCompleteOverviewScan: ICReturnCode { get } ``` | OS X 10.10 |
| To | ScannerFailedToCompleteOverviewScan | ``` case ScannerFailedToCompleteOverviewScan ``` | OS X 10.11 |

Modified ICReturnCode.ScannerFailedToCompleteScan

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnScannerFailedToCompleteScan | ``` var ICReturnScannerFailedToCompleteScan: ICReturnCode { get } ``` | OS X 10.10 |
| To | ScannerFailedToCompleteScan | ``` case ScannerFailedToCompleteScan ``` | OS X 10.11 |

Modified ICReturnCode.ScannerFailedToSelectFunctionalUnit

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnScannerFailedToSelectFunctionalUnit | ``` var ICReturnScannerFailedToSelectFunctionalUnit: ICReturnCode { get } ``` | OS X 10.10 |
| To | ScannerFailedToSelectFunctionalUnit | ``` case ScannerFailedToSelectFunctionalUnit ``` | OS X 10.11 |

Modified ICReturnCode.ScannerInUseByLocalUser

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnScannerInUseByLocalUser | ``` var ICReturnScannerInUseByLocalUser: ICReturnCode { get } ``` | OS X 10.10 |
| To | ScannerInUseByLocalUser | ``` case ScannerInUseByLocalUser ``` | OS X 10.11 |

Modified ICReturnCode.ScannerInUseByRemoteUser

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnScannerInUseByRemoteUser | ``` var ICReturnScannerInUseByRemoteUser: ICReturnCode { get } ``` | OS X 10.10 |
| To | ScannerInUseByRemoteUser | ``` case ScannerInUseByRemoteUser ``` | OS X 10.11 |

Modified ICReturnCode.ScanOperationCanceled

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnScanOperationCanceled | ``` var ICReturnScanOperationCanceled: ICReturnCode { get } ``` | OS X 10.10 |
| To | ScanOperationCanceled | ``` case ScanOperationCanceled ``` | OS X 10.11 |

Modified ICReturnCode.Success

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnSuccess | ``` var ICReturnSuccess: ICReturnCode { get } ``` | OS X 10.10 |
| To | Success | ``` case Success ``` | OS X 10.11 |

Modified ICReturnCode.UploadFailed

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | ICReturnUploadFailed | ``` var ICReturnUploadFailed: ICReturnCode { get } ``` | OS X 10.10 |
| To | UploadFailed | ``` case UploadFailed ``` | OS X 10.11 |

Modified ICScannerBandData

|  | Declaration |
| --- | --- |
| From | ``` class ICScannerBandData : NSObject {     var fullImageWidth: Int { get }     var fullImageHeight: Int { get }     var bitsPerPixel: Int { get }     var bitsPerComponent: Int { get }     var numComponents: Int { get }     var bigEndian: Bool { get }     var pixelDataType: ICScannerPixelDataType { get }     var colorSyncProfilePath: String! { get }     var bytesPerRow: Int { get }     var dataStartRow: Int { get }     var dataNumRows: Int { get }     var dataSize: Int { get }     var dataBuffer: NSData! { get } } ``` |
| To | ``` class ICScannerBandData : NSObject {     var fullImageWidth: Int { get }     var fullImageHeight: Int { get }     var bitsPerPixel: Int { get }     var bitsPerComponent: Int { get }     var numComponents: Int { get }     var bigEndian: Bool { get }     var pixelDataType: ICScannerPixelDataType { get }     var colorSyncProfilePath: String? { get }     var bytesPerRow: Int { get }     var dataStartRow: Int { get }     var dataNumRows: Int { get }     var dataSize: Int { get }     var dataBuffer: NSData? { get } } ``` |

Modified ICScannerBandData.colorSyncProfilePath

|  | Declaration |
| --- | --- |
| From | ``` var colorSyncProfilePath: String! { get } ``` |
| To | ``` var colorSyncProfilePath: String? { get } ``` |

Modified ICScannerBandData.dataBuffer

|  | Declaration |
| --- | --- |
| From | ``` var dataBuffer: NSData! { get } ``` |
| To | ``` var dataBuffer: NSData? { get } ``` |

Modified ICScannerDevice

|  | Declaration |
| --- | --- |
| From | ``` class ICScannerDevice : ICDevice {     var availableFunctionalUnitTypes: [AnyObject]! { get }     var selectedFunctionalUnit: ICScannerFunctionalUnit! { get }     var transferMode: ICScannerTransferMode     var maxMemoryBandSize: UInt32     var downloadsDirectory: NSURL!     var documentName: String!     var documentUTI: String!     func requestSelectFunctionalUnit(_ type: ICScannerFunctionalUnitType)     func requestOverviewScan()     func requestScan()     func cancelScan() } ``` |
| To | ``` class ICScannerDevice : ICDevice {     var availableFunctionalUnitTypes: [NSNumber] { get }     var selectedFunctionalUnit: ICScannerFunctionalUnit { get }     var transferMode: ICScannerTransferMode     var maxMemoryBandSize: UInt32     var downloadsDirectory: NSURL     var documentName: String     var documentUTI: String     func requestSelectFunctionalUnit(_ type: ICScannerFunctionalUnitType)     func requestOverviewScan()     func requestScan()     func cancelScan() } ``` |

Modified ICScannerDevice.availableFunctionalUnitTypes

|  | Declaration |
| --- | --- |
| From | ``` var availableFunctionalUnitTypes: [AnyObject]! { get } ``` |
| To | ``` var availableFunctionalUnitTypes: [NSNumber] { get } ``` |

Modified ICScannerDevice.documentName

|  | Declaration |
| --- | --- |
| From | ``` var documentName: String! ``` |
| To | ``` var documentName: String ``` |

Modified ICScannerDevice.documentUTI

|  | Declaration |
| --- | --- |
| From | ``` var documentUTI: String! ``` |
| To | ``` var documentUTI: String ``` |

Modified ICScannerDevice.downloadsDirectory

|  | Declaration |
| --- | --- |
| From | ``` var downloadsDirectory: NSURL! ``` |
| To | ``` var downloadsDirectory: NSURL ``` |

Modified ICScannerDevice.selectedFunctionalUnit

|  | Declaration |
| --- | --- |
| From | ``` var selectedFunctionalUnit: ICScannerFunctionalUnit! { get } ``` |
| To | ``` var selectedFunctionalUnit: ICScannerFunctionalUnit { get } ``` |

Modified ICScannerDeviceDelegate

|  | Declaration |
| --- | --- |
| From | ``` protocol ICScannerDeviceDelegate : ICDeviceDelegate, NSObjectProtocol {     optional func scannerDeviceDidBecomeAvailable(_ scanner: ICScannerDevice!)     optional func scannerDevice(_ scanner: ICScannerDevice!, didSelectFunctionalUnit functionalUnit: ICScannerFunctionalUnit!, error error: NSError!)     optional func scannerDevice(_ scanner: ICScannerDevice!, didScanToURL url: NSURL!, data data: NSData!)     optional func scannerDevice(_ scanner: ICScannerDevice!, didScanToURL url: NSURL!)     optional func scannerDevice(_ scanner: ICScannerDevice!, didScanToBandData data: ICScannerBandData!)     optional func scannerDevice(_ scanner: ICScannerDevice!, didCompleteOverviewScanWithError error: NSError!)     optional func scannerDevice(_ scanner: ICScannerDevice!, didCompleteScanWithError error: NSError!) } ``` |
| To | ``` protocol ICScannerDeviceDelegate : ICDeviceDelegate, NSObjectProtocol {     optional func scannerDeviceDidBecomeAvailable(_ scanner: ICScannerDevice)     optional func scannerDevice(_ scanner: ICScannerDevice, didSelectFunctionalUnit functionalUnit: ICScannerFunctionalUnit, error error: NSError?)     optional func scannerDevice(_ scanner: ICScannerDevice, didScanToURL url: NSURL, data data: NSData)     optional func scannerDevice(_ scanner: ICScannerDevice, didScanToURL url: NSURL)     optional func scannerDevice(_ scanner: ICScannerDevice, didScanToBandData data: ICScannerBandData)     optional func scannerDevice(_ scanner: ICScannerDevice, didCompleteOverviewScanWithError error: NSError?)     optional func scannerDevice(_ scanner: ICScannerDevice, didCompleteScanWithError error: NSError?) } ``` |

Modified ICScannerDeviceDelegate.scannerDevice(_: ICScannerDevice, didCompleteOverviewScanWithError: NSError?)

|  | Declaration |
| --- | --- |
| From | ``` optional func scannerDevice(_ scanner: ICScannerDevice!, didCompleteOverviewScanWithError error: NSError!) ``` |
| To | ``` optional func scannerDevice(_ scanner: ICScannerDevice, didCompleteOverviewScanWithError error: NSError?) ``` |

Modified ICScannerDeviceDelegate.scannerDevice(_: ICScannerDevice, didCompleteScanWithError: NSError?)

|  | Declaration |
| --- | --- |
| From | ``` optional func scannerDevice(_ scanner: ICScannerDevice!, didCompleteScanWithError error: NSError!) ``` |
| To | ``` optional func scannerDevice(_ scanner: ICScannerDevice, didCompleteScanWithError error: NSError?) ``` |

Modified ICScannerDeviceDelegate.scannerDevice(_: ICScannerDevice, didScanToBandData: ICScannerBandData)

|  | Declaration |
| --- | --- |
| From | ``` optional func scannerDevice(_ scanner: ICScannerDevice!, didScanToBandData data: ICScannerBandData!) ``` |
| To | ``` optional func scannerDevice(_ scanner: ICScannerDevice, didScanToBandData data: ICScannerBandData) ``` |

Modified ICScannerDeviceDelegate.scannerDevice(_: ICScannerDevice, didScanToURL: NSURL)

|  | Declaration |
| --- | --- |
| From | ``` optional func scannerDevice(_ scanner: ICScannerDevice!, didScanToURL url: NSURL!) ``` |
| To | ``` optional func scannerDevice(_ scanner: ICScannerDevice, didScanToURL url: NSURL) ``` |

Modified ICScannerDeviceDelegate.scannerDevice(_: ICScannerDevice, didSelectFunctionalUnit: ICScannerFunctionalUnit, error: NSError?)

|  | Declaration |
| --- | --- |
| From | ``` optional func scannerDevice(_ scanner: ICScannerDevice!, didSelectFunctionalUnit functionalUnit: ICScannerFunctionalUnit!, error error: NSError!) ``` |
| To | ``` optional func scannerDevice(_ scanner: ICScannerDevice, didSelectFunctionalUnit functionalUnit: ICScannerFunctionalUnit, error error: NSError?) ``` |

Modified ICScannerDeviceDelegate.scannerDeviceDidBecomeAvailable(_: ICScannerDevice)

|  | Declaration |
| --- | --- |
| From | ``` optional func scannerDeviceDidBecomeAvailable(_ scanner: ICScannerDevice!) ``` |
| To | ``` optional func scannerDeviceDidBecomeAvailable(_ scanner: ICScannerDevice) ``` |

Modified ICScannerFeature

|  | Declaration |
| --- | --- |
| From | ``` class ICScannerFeature : NSObject {     var type: ICScannerFeatureType { get }     var internalName: String! { get }     var humanReadableName: String! { get }     var tooltip: String! { get } } ``` |
| To | ``` class ICScannerFeature : NSObject {     var type: ICScannerFeatureType { get }     var internalName: String? { get }     var humanReadableName: String? { get }     var tooltip: String? { get } } ``` |

Modified ICScannerFeature.humanReadableName

|  | Declaration |
| --- | --- |
| From | ``` var humanReadableName: String! { get } ``` |
| To | ``` var humanReadableName: String? { get } ``` |

Modified ICScannerFeature.internalName

|  | Declaration |
| --- | --- |
| From | ``` var internalName: String! { get } ``` |
| To | ``` var internalName: String? { get } ``` |

Modified ICScannerFeature.tooltip

|  | Declaration |
| --- | --- |
| From | ``` var tooltip: String! { get } ``` |
| To | ``` var tooltip: String? { get } ``` |

Modified ICScannerFeatureEnumeration

|  | Declaration |
| --- | --- |
| From | ``` class ICScannerFeatureEnumeration : ICScannerFeature {     unowned(unsafe) var currentValue: AnyObject!     var defaultValue: AnyObject! { get }     var values: [AnyObject]! { get }     var menuItemLabels: [AnyObject]! { get }     var menuItemLabelsTooltips: [AnyObject]! { get } } ``` |
| To | ``` class ICScannerFeatureEnumeration : ICScannerFeature {     unowned(unsafe) var currentValue: AnyObject     var defaultValue: AnyObject { get }     var values: [NSNumber] { get }     var menuItemLabels: [String] { get }     var menuItemLabelsTooltips: [String] { get } } ``` |

Modified ICScannerFeatureEnumeration.currentValue

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var currentValue: AnyObject! ``` |
| To | ``` unowned(unsafe) var currentValue: AnyObject ``` |

Modified ICScannerFeatureEnumeration.defaultValue

|  | Declaration |
| --- | --- |
| From | ``` var defaultValue: AnyObject! { get } ``` |
| To | ``` var defaultValue: AnyObject { get } ``` |

Modified ICScannerFeatureEnumeration.menuItemLabels

|  | Declaration |
| --- | --- |
| From | ``` var menuItemLabels: [AnyObject]! { get } ``` |
| To | ``` var menuItemLabels: [String] { get } ``` |

Modified ICScannerFeatureEnumeration.menuItemLabelsTooltips

|  | Declaration |
| --- | --- |
| From | ``` var menuItemLabelsTooltips: [AnyObject]! { get } ``` |
| To | ``` var menuItemLabelsTooltips: [String] { get } ``` |

Modified ICScannerFeatureEnumeration.values

|  | Declaration |
| --- | --- |
| From | ``` var values: [AnyObject]! { get } ``` |
| To | ``` var values: [NSNumber] { get } ``` |

Modified ICScannerFeatureTemplate

|  | Declaration |
| --- | --- |
| From | ``` class ICScannerFeatureTemplate : ICScannerFeature {     var targets: [AnyObject]! { get } } ``` |
| To | ``` class ICScannerFeatureTemplate : ICScannerFeature {     var targets: [NSMutableArray] { get } } ``` |

Modified ICScannerFeatureTemplate.targets

|  | Declaration |
| --- | --- |
| From | ``` var targets: [AnyObject]! { get } ``` |
| To | ``` var targets: [NSMutableArray] { get } ``` |

Modified ICScannerFunctionalUnit

|  | Declaration |
| --- | --- |
| From | ``` class ICScannerFunctionalUnit : NSObject {     var type: ICScannerFunctionalUnitType { get }     var pixelDataType: ICScannerPixelDataType     var supportedBitDepths: NSIndexSet! { get }     var bitDepth: ICScannerBitDepth     var supportedMeasurementUnits: NSIndexSet! { get }     var measurementUnit: ICScannerMeasurementUnit     var supportedResolutions: NSIndexSet! { get }     var preferredResolutions: NSIndexSet! { get }     var resolution: Int     var nativeXResolution: Int { get }     var nativeYResolution: Int { get }     var supportedScaleFactors: NSIndexSet! { get }     var preferredScaleFactors: NSIndexSet! { get }     var scaleFactor: Int     var templates: [AnyObject]! { get }     var vendorFeatures: [AnyObject]! { get }     var physicalSize: NSSize { get }     var scanArea: NSRect     var scanAreaOrientation: ICEXIFOrientationType     var acceptsThresholdForBlackAndWhiteScanning: Bool { get }     var usesThresholdForBlackAndWhiteScanning: Bool     var defaultThresholdForBlackAndWhiteScanning: UInt8 { get }     var thresholdForBlackAndWhiteScanning: UInt8     var state: ICScannerFunctionalUnitState { get }     var scanInProgress: Bool { get }     var scanProgressPercentDone: CGFloat { get }     var canPerformOverviewScan: Bool { get }     var overviewScanInProgress: Bool { get }     var overviewImage: CGImage! { get }     var overviewResolution: Int } ``` |
| To | ``` class ICScannerFunctionalUnit : NSObject {     var type: ICScannerFunctionalUnitType { get }     var pixelDataType: ICScannerPixelDataType     var supportedBitDepths: NSIndexSet { get }     var bitDepth: ICScannerBitDepth     var supportedMeasurementUnits: NSIndexSet { get }     var measurementUnit: ICScannerMeasurementUnit     var supportedResolutions: NSIndexSet { get }     var preferredResolutions: NSIndexSet { get }     var resolution: Int     var nativeXResolution: Int { get }     var nativeYResolution: Int { get }     var supportedScaleFactors: NSIndexSet { get }     var preferredScaleFactors: NSIndexSet { get }     var scaleFactor: Int     var templates: [ICScannerFeatureTemplate] { get }     var vendorFeatures: [ICScannerFeature]? { get }     var physicalSize: NSSize { get }     var scanArea: NSRect     var scanAreaOrientation: ICEXIFOrientationType     var acceptsThresholdForBlackAndWhiteScanning: Bool { get }     var usesThresholdForBlackAndWhiteScanning: Bool     var defaultThresholdForBlackAndWhiteScanning: UInt8 { get }     var thresholdForBlackAndWhiteScanning: UInt8     var state: ICScannerFunctionalUnitState { get }     var scanInProgress: Bool { get }     var scanProgressPercentDone: CGFloat { get }     var canPerformOverviewScan: Bool { get }     var overviewScanInProgress: Bool { get }     var overviewImage: CGImage? { get }     var overviewResolution: Int } ``` |

Modified ICScannerFunctionalUnit.overviewImage

|  | Declaration |
| --- | --- |
| From | ``` var overviewImage: CGImage! { get } ``` |
| To | ``` var overviewImage: CGImage? { get } ``` |

Modified ICScannerFunctionalUnit.preferredResolutions

|  | Declaration |
| --- | --- |
| From | ``` var preferredResolutions: NSIndexSet! { get } ``` |
| To | ``` var preferredResolutions: NSIndexSet { get } ``` |

Modified ICScannerFunctionalUnit.preferredScaleFactors

|  | Declaration |
| --- | --- |
| From | ``` var preferredScaleFactors: NSIndexSet! { get } ``` |
| To | ``` var preferredScaleFactors: NSIndexSet { get } ``` |

Modified ICScannerFunctionalUnit.supportedBitDepths

|  | Declaration |
| --- | --- |
| From | ``` var supportedBitDepths: NSIndexSet! { get } ``` |
| To | ``` var supportedBitDepths: NSIndexSet { get } ``` |

Modified ICScannerFunctionalUnit.supportedMeasurementUnits

|  | Declaration |
| --- | --- |
| From | ``` var supportedMeasurementUnits: NSIndexSet! { get } ``` |
| To | ``` var supportedMeasurementUnits: NSIndexSet { get } ``` |

Modified ICScannerFunctionalUnit.supportedResolutions

|  | Declaration |
| --- | --- |
| From | ``` var supportedResolutions: NSIndexSet! { get } ``` |
| To | ``` var supportedResolutions: NSIndexSet { get } ``` |

Modified ICScannerFunctionalUnit.supportedScaleFactors

|  | Declaration |
| --- | --- |
| From | ``` var supportedScaleFactors: NSIndexSet! { get } ``` |
| To | ``` var supportedScaleFactors: NSIndexSet { get } ``` |

Modified ICScannerFunctionalUnit.templates

|  | Declaration |
| --- | --- |
| From | ``` var templates: [AnyObject]! { get } ``` |
| To | ``` var templates: [ICScannerFeatureTemplate] { get } ``` |

Modified ICScannerFunctionalUnit.vendorFeatures

|  | Declaration |
| --- | --- |
| From | ``` var vendorFeatures: [AnyObject]! { get } ``` |
| To | ``` var vendorFeatures: [ICScannerFeature]? { get } ``` |

Modified ICScannerFunctionalUnitDocumentFeeder

|  | Declaration |
| --- | --- |
| From | ``` class ICScannerFunctionalUnitDocumentFeeder : ICScannerFunctionalUnit {     var supportedDocumentTypes: NSIndexSet! { get }     var documentType: ICScannerDocumentType     var documentSize: NSSize { get }     var supportsDuplexScanning: Bool { get }     var duplexScanningEnabled: Bool     var documentLoaded: Bool { get }     var oddPageOrientation: ICEXIFOrientationType     var evenPageOrientation: ICEXIFOrientationType     var reverseFeederPageOrder: Bool { get } } ``` |
| To | ``` class ICScannerFunctionalUnitDocumentFeeder : ICScannerFunctionalUnit {     var supportedDocumentTypes: NSIndexSet { get }     var documentType: ICScannerDocumentType     var documentSize: NSSize { get }     var supportsDuplexScanning: Bool { get }     var duplexScanningEnabled: Bool     var documentLoaded: Bool { get }     var oddPageOrientation: ICEXIFOrientationType     var evenPageOrientation: ICEXIFOrientationType     var reverseFeederPageOrder: Bool { get } } ``` |

Modified ICScannerFunctionalUnitDocumentFeeder.supportedDocumentTypes

|  | Declaration |
| --- | --- |
| From | ``` var supportedDocumentTypes: NSIndexSet! { get } ``` |
| To | ``` var supportedDocumentTypes: NSIndexSet { get } ``` |

Modified ICScannerFunctionalUnitFlatbed

|  | Declaration |
| --- | --- |
| From | ``` class ICScannerFunctionalUnitFlatbed : ICScannerFunctionalUnit {     var supportedDocumentTypes: NSIndexSet! { get }     var documentType: ICScannerDocumentType     var documentSize: NSSize { get } } ``` |
| To | ``` class ICScannerFunctionalUnitFlatbed : ICScannerFunctionalUnit {     var supportedDocumentTypes: NSIndexSet { get }     var documentType: ICScannerDocumentType     var documentSize: NSSize { get } } ``` |

Modified ICScannerFunctionalUnitFlatbed.supportedDocumentTypes

|  | Declaration |
| --- | --- |
| From | ``` var supportedDocumentTypes: NSIndexSet! { get } ``` |
| To | ``` var supportedDocumentTypes: NSIndexSet { get } ``` |

Modified ICScannerFunctionalUnitNegativeTransparency

|  | Declaration |
| --- | --- |
| From | ``` class ICScannerFunctionalUnitNegativeTransparency : ICScannerFunctionalUnit {     var supportedDocumentTypes: NSIndexSet! { get }     var documentType: ICScannerDocumentType     var documentSize: NSSize { get } } ``` |
| To | ``` class ICScannerFunctionalUnitNegativeTransparency : ICScannerFunctionalUnit {     var supportedDocumentTypes: NSIndexSet { get }     var documentType: ICScannerDocumentType     var documentSize: NSSize { get } } ``` |

Modified ICScannerFunctionalUnitNegativeTransparency.supportedDocumentTypes

|  | Declaration |
| --- | --- |
| From | ``` var supportedDocumentTypes: NSIndexSet! { get } ``` |
| To | ``` var supportedDocumentTypes: NSIndexSet { get } ``` |

Modified ICScannerFunctionalUnitPositiveTransparency

|  | Declaration |
| --- | --- |
| From | ``` class ICScannerFunctionalUnitPositiveTransparency : ICScannerFunctionalUnit {     var supportedDocumentTypes: NSIndexSet! { get }     var documentType: ICScannerDocumentType     var documentSize: NSSize { get } } ``` |
| To | ``` class ICScannerFunctionalUnitPositiveTransparency : ICScannerFunctionalUnit {     var supportedDocumentTypes: NSIndexSet { get }     var documentType: ICScannerDocumentType     var documentSize: NSSize { get } } ``` |

Modified ICScannerFunctionalUnitPositiveTransparency.supportedDocumentTypes

|  | Declaration |
| --- | --- |
| From | ``` var supportedDocumentTypes: NSIndexSet! { get } ``` |
| To | ``` var supportedDocumentTypes: NSIndexSet { get } ``` |

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
