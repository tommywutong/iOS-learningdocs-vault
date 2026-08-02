---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/ImageCaptureCore.html
archived_at: '2026-07-18T02:53:07.844740Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# ImageCaptureCore Changes for Objective-C

### ImageCaptureCore

#### ICCameraDevice.h

Added ICCameraDeviceSupportsFastPTPModified ICCameraDevice.contents

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *contents ``` |
| To | ``` @property(readonly, nullable) NSArray<ICCameraItem *> *contents ``` |

Modified -[ICCameraDevice filesOfType:]

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)filesOfType:(NSString *)fileUTType ``` |
| To | ``` - (NSArray<NSString *> * _Nonnull)filesOfType:(NSString * _Nonnull)fileUTType ``` |

Modified ICCameraDevice.mediaFiles

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *mediaFiles ``` |
| To | ``` @property(readonly, nullable) NSArray<ICCameraItem *> *mediaFiles ``` |

Modified ICCameraDevice.mountPoint

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *mountPoint ``` |
| To | ``` @property(readonly, nullable) NSString *mountPoint ``` |

Modified -[ICCameraDevice requestDeleteFiles:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)requestDeleteFiles:(NSArray *)files ``` |
| To | ``` - (void)requestDeleteFiles:(NSArray<ICCameraItem *> * _Nonnull)files ``` |

Modified -[ICCameraDevice requestDownloadFile:options:downloadDelegate:didDownloadSelector:contextInfo:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)requestDownloadFile:(ICCameraFile *)file options:(NSDictionary *)options downloadDelegate:(id<ICCameraDeviceDownloadDelegate>)downloadDelegate didDownloadSelector:(SEL)selector contextInfo:(void *)contextInfo ``` |
| To | ``` - (void)requestDownloadFile:(ICCameraFile * _Nonnull)file options:(NSDictionary<NSString *,id> * _Nullable)options downloadDelegate:(id<ICCameraDeviceDownloadDelegate> _Nonnull)downloadDelegate didDownloadSelector:(SEL _Nonnull)selector contextInfo:(void * _Nullable)contextInfo ``` |

Modified -[ICCameraDevice requestReadDataFromFile:atOffset:length:readDelegate:didReadDataSelector:contextInfo:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)requestReadDataFromFile:(ICCameraFile *)file atOffset:(off_t)offset length:(off_t)length readDelegate:(id)readDelegate didReadDataSelector:(SEL)selector contextInfo:(void *)contextInfo ``` |
| To | ``` - (void)requestReadDataFromFile:(ICCameraFile * _Nonnull)file atOffset:(off_t)offset length:(off_t)length readDelegate:(id _Nonnull)readDelegate didReadDataSelector:(SEL _Nonnull)selector contextInfo:(void * _Nullable)contextInfo ``` |

Modified -[ICCameraDevice requestSendPTPCommand:outData:sendCommandDelegate:didSendCommandSelector:contextInfo:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)requestSendPTPCommand:(NSData *)command outData:(NSData *)data sendCommandDelegate:(id)sendCommandDelegate didSendCommandSelector:(SEL)selector contextInfo:(void *)contextInfo ``` |
| To | ``` - (void)requestSendPTPCommand:(NSData * _Nonnull)command outData:(NSData * _Nonnull)data sendCommandDelegate:(id _Nonnull)sendCommandDelegate didSendCommandSelector:(SEL _Nonnull)selector contextInfo:(void * _Nullable)contextInfo ``` |

Modified -[ICCameraDevice requestUploadFile:options:uploadDelegate:didUploadSelector:contextInfo:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)requestUploadFile:(NSURL *)fileURL options:(NSDictionary *)options uploadDelegate:(id)uploadDelegate didUploadSelector:(SEL)selector contextInfo:(void *)contextInfo ``` |
| To | ``` - (void)requestUploadFile:(NSURL * _Nonnull)fileURL options:(NSDictionary<NSString *,id> * _Nullable)options uploadDelegate:(id _Nonnull)uploadDelegate didUploadSelector:(SEL _Nonnull)selector contextInfo:(void * _Nullable)contextInfo ``` |

Modified -[ICCameraDeviceDelegate cameraDevice:didAddItem:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)cameraDevice:(ICCameraDevice *)camera didAddItem:(ICCameraItem *)item ``` |
| To | ``` - (void)cameraDevice:(ICCameraDevice * _Nonnull)camera didAddItem:(ICCameraItem * _Nonnull)item ``` |

Modified -[ICCameraDeviceDelegate cameraDevice:didAddItems:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)cameraDevice:(ICCameraDevice *)camera didAddItems:(NSArray *)items ``` |
| To | ``` - (void)cameraDevice:(ICCameraDevice * _Nonnull)camera didAddItems:(NSArray<ICCameraItem *> * _Nonnull)items ``` |

Modified -[ICCameraDeviceDelegate cameraDevice:didCompleteDeleteFilesWithError:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)cameraDevice:(ICCameraDevice *)scanner didCompleteDeleteFilesWithError:(NSError *)error ``` |
| To | ``` - (void)cameraDevice:(ICCameraDevice * _Nonnull)scanner didCompleteDeleteFilesWithError:(NSError * _Nullable)error ``` |

Modified -[ICCameraDeviceDelegate cameraDevice:didReceiveMetadataForItem:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)cameraDevice:(ICCameraDevice *)camera didReceiveMetadataForItem:(ICCameraItem *)item ``` |
| To | ``` - (void)cameraDevice:(ICCameraDevice * _Nonnull)camera didReceiveMetadataForItem:(ICCameraItem * _Nonnull)item ``` |

Modified -[ICCameraDeviceDelegate cameraDevice:didReceivePTPEvent:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)cameraDevice:(ICCameraDevice *)camera didReceivePTPEvent:(NSData *)eventData ``` |
| To | ``` - (void)cameraDevice:(ICCameraDevice * _Nonnull)camera didReceivePTPEvent:(NSData * _Nonnull)eventData ``` |

Modified -[ICCameraDeviceDelegate cameraDevice:didReceiveThumbnailForItem:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)cameraDevice:(ICCameraDevice *)camera didReceiveThumbnailForItem:(ICCameraItem *)item ``` |
| To | ``` - (void)cameraDevice:(ICCameraDevice * _Nonnull)camera didReceiveThumbnailForItem:(ICCameraItem * _Nonnull)item ``` |

Modified -[ICCameraDeviceDelegate cameraDevice:didRemoveItem:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)cameraDevice:(ICCameraDevice *)camera didRemoveItem:(ICCameraItem *)item ``` |
| To | ``` - (void)cameraDevice:(ICCameraDevice * _Nonnull)camera didRemoveItem:(ICCameraItem * _Nonnull)item ``` |

Modified -[ICCameraDeviceDelegate cameraDevice:didRemoveItems:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)cameraDevice:(ICCameraDevice *)camera didRemoveItems:(NSArray *)items ``` |
| To | ``` - (void)cameraDevice:(ICCameraDevice * _Nonnull)camera didRemoveItems:(NSArray<ICCameraItem *> * _Nonnull)items ``` |

Modified -[ICCameraDeviceDelegate cameraDevice:didRenameItems:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)cameraDevice:(ICCameraDevice *)camera didRenameItems:(NSArray *)items ``` |
| To | ``` - (void)cameraDevice:(ICCameraDevice * _Nonnull)camera didRenameItems:(NSArray<ICCameraItem *> * _Nonnull)items ``` |

Modified -[ICCameraDeviceDelegate cameraDevice:shouldGetMetadataOfItem:]

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)cameraDevice:(ICCameraDevice *)cameraDevice shouldGetMetadataOfItem:(ICCameraItem *)item ``` |
| To | ``` - (BOOL)cameraDevice:(ICCameraDevice * _Nonnull)cameraDevice shouldGetMetadataOfItem:(ICCameraItem * _Nonnull)item ``` |

Modified -[ICCameraDeviceDelegate cameraDevice:shouldGetThumbnailOfItem:]

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)cameraDevice:(ICCameraDevice *)cameraDevice shouldGetThumbnailOfItem:(ICCameraItem *)item ``` |
| To | ``` - (BOOL)cameraDevice:(ICCameraDevice * _Nonnull)cameraDevice shouldGetThumbnailOfItem:(ICCameraItem * _Nonnull)item ``` |

Modified -[ICCameraDeviceDelegate cameraDeviceDidChangeCapability:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)cameraDeviceDidChangeCapability:(ICCameraDevice *)camera ``` |
| To | ``` - (void)cameraDeviceDidChangeCapability:(ICCameraDevice * _Nonnull)camera ``` |

Modified -[ICCameraDeviceDelegate deviceDidBecomeReadyWithCompleteContentCatalog:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)deviceDidBecomeReadyWithCompleteContentCatalog:(ICDevice *)device ``` |
| To | ``` - (void)deviceDidBecomeReadyWithCompleteContentCatalog:(ICDevice * _Nonnull)device ``` |

Modified -[ICCameraDeviceDownloadDelegate didDownloadFile:error:options:contextInfo:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)didDownloadFile:(ICCameraFile *)file error:(NSError *)error options:(NSDictionary *)options contextInfo:(void *)contextInfo ``` |
| To | ``` - (void)didDownloadFile:(ICCameraFile * _Nonnull)file error:(NSError * _Nullable)error options:(NSDictionary<NSString *,id> * _Nullable)options contextInfo:(void * _Nullable)contextInfo ``` |

Modified -[ICCameraDeviceDownloadDelegate didReceiveDownloadProgressForFile:downloadedBytes:maxBytes:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)didReceiveDownloadProgressForFile:(ICCameraFile *)file downloadedBytes:(off_t)downloadedBytes maxBytes:(off_t)maxBytes ``` |
| To | ``` - (void)didReceiveDownloadProgressForFile:(ICCameraFile * _Nonnull)file downloadedBytes:(off_t)downloadedBytes maxBytes:(off_t)maxBytes ``` |

#### ICCameraItem.h

Modified ICCameraFile.sidecarFiles

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *sidecarFiles ``` |
| To | ``` @property(readonly, nonnull) NSArray<ICCameraItem *> *sidecarFiles ``` |

Modified ICCameraFolder.contents

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *contents ``` |
| To | ``` @property(readonly, nonnull) NSArray<ICCameraItem *> *contents ``` |

Modified ICCameraItem.creationDate

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSDate *creationDate ``` |
| To | ``` @property(readonly, nonnull) NSDate *creationDate ``` |

Modified ICCameraItem.device

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) ICCameraDevice *device ``` |
| To | ``` @property(readonly, nonnull) ICCameraDevice *device ``` |

Modified ICCameraItem.fileSystemPath

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *fileSystemPath ``` |
| To | ``` @property(readonly, nonnull) NSString *fileSystemPath ``` |

Modified ICCameraItem.largeThumbnailIfAvailable

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) CGImageRef largeThumbnailIfAvailable ``` |
| To | ``` @property(readonly, nullable) CGImageRef largeThumbnailIfAvailable ``` |

Modified ICCameraItem.metadataIfAvailable

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSDictionary *metadataIfAvailable ``` |
| To | ``` @property(readonly, nullable) NSDictionary<NSString *,id> *metadataIfAvailable ``` |

Modified ICCameraItem.modificationDate

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSDate *modificationDate ``` |
| To | ``` @property(readonly, nonnull) NSDate *modificationDate ``` |

Modified ICCameraItem.name

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *name ``` |
| To | ``` @property(readonly, nonnull) NSString *name ``` |

Modified ICCameraItem.parentFolder

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) ICCameraFolder *parentFolder ``` |
| To | ``` @property(readonly, nonnull) ICCameraFolder *parentFolder ``` |

Modified ICCameraItem.thumbnailIfAvailable

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) CGImageRef thumbnailIfAvailable ``` |
| To | ``` @property(readonly, nullable) CGImageRef thumbnailIfAvailable ``` |

Modified ICCameraItem.userData

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSMutableDictionary *userData ``` |
| To | ``` @property(readonly, nullable) NSMutableDictionary *userData ``` |

Modified ICCameraItem.UTI

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *UTI ``` |
| To | ``` @property(readonly, nonnull) NSString *UTI ``` |

#### ICCommonConstants.h

Added ICReturnDeviceNeedsCredentials

#### ICDevice.h

Modified ICDevice.autolaunchApplicationPath

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, copy) NSString *autolaunchApplicationPath ``` |
| To | ``` @property(readwrite, copy, nullable) NSString *autolaunchApplicationPath ``` |

Modified ICDevice.buttonPressed

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *buttonPressed ``` |
| To | ``` @property(readonly, nonnull) NSString *buttonPressed ``` |

Modified ICDevice.capabilities

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *capabilities ``` |
| To | ``` @property(readonly, nonnull) NSArray<NSString *> *capabilities ``` |

Modified ICDevice.delegate

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<ICDeviceDelegate> delegate ``` |
| To | ``` @property(assign, nullable) id<ICDeviceDelegate> delegate ``` |

Modified ICDevice.icon

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) CGImageRef icon ``` |
| To | ``` @property(readonly, nullable) CGImageRef icon ``` |

Modified ICDevice.locationDescription

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *locationDescription ``` |
| To | ``` @property(readonly, nullable) NSString *locationDescription ``` |

Modified ICDevice.modulePath

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *modulePath ``` |
| To | ``` @property(readonly, nonnull) NSString *modulePath ``` |

Modified ICDevice.moduleVersion

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *moduleVersion ``` |
| To | ``` @property(readonly, nonnull) NSString *moduleVersion ``` |

Modified ICDevice.name

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *name ``` |
| To | ``` @property(readonly, nullable) NSString *name ``` |

Modified ICDevice.persistentIDString

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *persistentIDString ``` |
| To | ``` @property(readonly, nullable) NSString *persistentIDString ``` |

Modified -[ICDevice requestSendMessage:outData:maxReturnedDataSize:sendMessageDelegate:didSendMessageSelector:contextInfo:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)requestSendMessage:(unsigned int)messageCode outData:(NSData *)data maxReturnedDataSize:(unsigned int)maxReturnedDataSize sendMessageDelegate:(id)sendMessageDelegate didSendMessageSelector:(SEL)selector contextInfo:(void *)contextInfo ``` |
| To | ``` - (void)requestSendMessage:(unsigned int)messageCode outData:(NSData * _Nonnull)data maxReturnedDataSize:(unsigned int)maxReturnedDataSize sendMessageDelegate:(id _Nonnull)sendMessageDelegate didSendMessageSelector:(SEL _Nonnull)selector contextInfo:(void * _Nullable)contextInfo ``` |

Modified ICDevice.serialNumberString

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *serialNumberString ``` |
| To | ``` @property(readonly, nullable) NSString *serialNumberString ``` |

Modified ICDevice.transportType

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *transportType ``` |
| To | ``` @property(readonly, nonnull) NSString *transportType ``` |

Modified ICDevice.userData

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSMutableDictionary *userData ``` |
| To | ``` @property(readonly, nullable) NSMutableDictionary *userData ``` |

Modified ICDevice.UUIDString

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *UUIDString ``` |
| To | ``` @property(readonly, nullable) NSString *UUIDString ``` |

Modified -[ICDeviceDelegate device:didCloseSessionWithError:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)device:(ICDevice *)device didCloseSessionWithError:(NSError *)error ``` |
| To | ``` - (void)device:(ICDevice * _Nonnull)device didCloseSessionWithError:(NSError * _Nullable)error ``` |

Modified -[ICDeviceDelegate device:didEncounterError:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)device:(ICDevice *)device didEncounterError:(NSError *)error ``` |
| To | ``` - (void)device:(ICDevice * _Nonnull)device didEncounterError:(NSError * _Nullable)error ``` |

Modified -[ICDeviceDelegate device:didOpenSessionWithError:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)device:(ICDevice *)device didOpenSessionWithError:(NSError *)error ``` |
| To | ``` - (void)device:(ICDevice * _Nonnull)device didOpenSessionWithError:(NSError * _Nullable)error ``` |

Modified -[ICDeviceDelegate device:didReceiveButtonPress:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)device:(ICDevice *)device didReceiveButtonPress:(NSString *)buttonType ``` |
| To | ``` - (void)device:(ICDevice * _Nonnull)device didReceiveButtonPress:(NSString * _Nonnull)buttonType ``` |

Modified -[ICDeviceDelegate device:didReceiveCustomNotification:data:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)device:(ICDevice *)device didReceiveCustomNotification:(NSDictionary *)notification data:(NSData *)data ``` |
| To | ``` - (void)device:(ICDevice * _Nonnull)device didReceiveCustomNotification:(NSDictionary<NSString *,id> * _Nonnull)notification data:(NSData * _Nonnull)data ``` |

Modified -[ICDeviceDelegate device:didReceiveStatusInformation:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)device:(ICDevice *)device didReceiveStatusInformation:(NSDictionary *)status ``` |
| To | ``` - (void)device:(ICDevice * _Nonnull)device didReceiveStatusInformation:(NSDictionary<NSString *,id> * _Nonnull)status ``` |

Modified -[ICDeviceDelegate deviceDidBecomeReady:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)deviceDidBecomeReady:(ICDevice *)device ``` |
| To | ``` - (void)deviceDidBecomeReady:(ICDevice * _Nonnull)device ``` |

Modified -[ICDeviceDelegate deviceDidChangeName:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)deviceDidChangeName:(ICDevice *)device ``` |
| To | ``` - (void)deviceDidChangeName:(ICDevice * _Nonnull)device ``` |

Modified -[ICDeviceDelegate deviceDidChangeSharingState:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)deviceDidChangeSharingState:(ICDevice *)device ``` |
| To | ``` - (void)deviceDidChangeSharingState:(ICDevice * _Nonnull)device ``` |

Modified -[ICDeviceDelegate didRemoveDevice:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)didRemoveDevice:(ICDevice *)device ``` |
| To | ``` - (void)didRemoveDevice:(ICDevice * _Nonnull)device ``` |

#### ICDeviceBrowser.h

Modified ICDeviceBrowser.delegate

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<ICDeviceBrowserDelegate> delegate ``` |
| To | ``` @property(assign, nullable) id<ICDeviceBrowserDelegate> delegate ``` |

Modified ICDeviceBrowser.devices

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *devices ``` |
| To | ``` @property(readonly, nullable) NSArray<ICDevice *> *devices ``` |

Modified -[ICDeviceBrowser init]

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (id _Nonnull)init ``` |

Modified -[ICDeviceBrowser preferredDevice]

|  | Declaration |
| --- | --- |
| From | ``` - (ICDevice *)preferredDevice ``` |
| To | ``` - (ICDevice * _Nonnull)preferredDevice ``` |

Modified -[ICDeviceBrowserDelegate deviceBrowser:deviceDidChangeName:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)deviceBrowser:(ICDeviceBrowser *)browser deviceDidChangeName:(ICDevice *)device ``` |
| To | ``` - (void)deviceBrowser:(ICDeviceBrowser * _Nonnull)browser deviceDidChangeName:(ICDevice * _Nonnull)device ``` |

Modified -[ICDeviceBrowserDelegate deviceBrowser:deviceDidChangeSharingState:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)deviceBrowser:(ICDeviceBrowser *)browser deviceDidChangeSharingState:(ICDevice *)device ``` |
| To | ``` - (void)deviceBrowser:(ICDeviceBrowser * _Nonnull)browser deviceDidChangeSharingState:(ICDevice * _Nonnull)device ``` |

Modified -[ICDeviceBrowserDelegate deviceBrowser:didAddDevice:moreComing:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)deviceBrowser:(ICDeviceBrowser *)browser didAddDevice:(ICDevice *)device moreComing:(BOOL)moreComing ``` |
| To | ``` - (void)deviceBrowser:(ICDeviceBrowser * _Nonnull)browser didAddDevice:(ICDevice * _Nonnull)device moreComing:(BOOL)moreComing ``` |

Modified -[ICDeviceBrowserDelegate deviceBrowser:didRemoveDevice:moreGoing:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)deviceBrowser:(ICDeviceBrowser *)browser didRemoveDevice:(ICDevice *)device moreGoing:(BOOL)moreGoing ``` |
| To | ``` - (void)deviceBrowser:(ICDeviceBrowser * _Nonnull)browser didRemoveDevice:(ICDevice * _Nonnull)device moreGoing:(BOOL)moreGoing ``` |

Modified -[ICDeviceBrowserDelegate deviceBrowser:requestsSelectDevice:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)deviceBrowser:(ICDeviceBrowser *)browser requestsSelectDevice:(ICDevice *)device ``` |
| To | ``` - (void)deviceBrowser:(ICDeviceBrowser * _Nonnull)browser requestsSelectDevice:(ICDevice * _Nonnull)device ``` |

Modified -[ICDeviceBrowserDelegate deviceBrowserDidEnumerateLocalDevices:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)deviceBrowserDidEnumerateLocalDevices:(ICDeviceBrowser *)browser ``` |
| To | ``` - (void)deviceBrowserDidEnumerateLocalDevices:(ICDeviceBrowser * _Nonnull)browser ``` |

#### ICScannerBandData.h

Modified ICScannerBandData.colorSyncProfilePath

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) NSString *colorSyncProfilePath ``` |
| To | ``` @property(readonly, retain, nullable) NSString *colorSyncProfilePath ``` |

Modified ICScannerBandData.dataBuffer

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) NSData *dataBuffer ``` |
| To | ``` @property(readonly, retain, nullable) NSData *dataBuffer ``` |

#### ICScannerDevice.h

Modified ICScannerDevice.availableFunctionalUnitTypes

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *availableFunctionalUnitTypes ``` |
| To | ``` @property(readonly, nonnull) NSArray<NSNumber *> *availableFunctionalUnitTypes ``` |

Modified ICScannerDevice.documentName

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *documentName ``` |
| To | ``` @property(copy, nonnull) NSString *documentName ``` |

Modified ICScannerDevice.documentUTI

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *documentUTI ``` |
| To | ``` @property(copy, nonnull) NSString *documentUTI ``` |

Modified ICScannerDevice.downloadsDirectory

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) NSURL *downloadsDirectory ``` |
| To | ``` @property(retain, nonnull) NSURL *downloadsDirectory ``` |

Modified ICScannerDevice.selectedFunctionalUnit

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) ICScannerFunctionalUnit *selectedFunctionalUnit ``` |
| To | ``` @property(readonly, nonnull) ICScannerFunctionalUnit *selectedFunctionalUnit ``` |

Modified -[ICScannerDeviceDelegate scannerDevice:didCompleteOverviewScanWithError:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)scannerDevice:(ICScannerDevice *)scanner didCompleteOverviewScanWithError:(NSError *)error ``` |
| To | ``` - (void)scannerDevice:(ICScannerDevice * _Nonnull)scanner didCompleteOverviewScanWithError:(NSError * _Nullable)error ``` |

Modified -[ICScannerDeviceDelegate scannerDevice:didCompleteScanWithError:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)scannerDevice:(ICScannerDevice *)scanner didCompleteScanWithError:(NSError *)error ``` |
| To | ``` - (void)scannerDevice:(ICScannerDevice * _Nonnull)scanner didCompleteScanWithError:(NSError * _Nullable)error ``` |

Modified -[ICScannerDeviceDelegate scannerDevice:didScanToBandData:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)scannerDevice:(ICScannerDevice *)scanner didScanToBandData:(ICScannerBandData *)data ``` |
| To | ``` - (void)scannerDevice:(ICScannerDevice * _Nonnull)scanner didScanToBandData:(ICScannerBandData * _Nonnull)data ``` |

Modified -[ICScannerDeviceDelegate scannerDevice:didScanToURL:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)scannerDevice:(ICScannerDevice *)scanner didScanToURL:(NSURL *)url ``` |
| To | ``` - (void)scannerDevice:(ICScannerDevice * _Nonnull)scanner didScanToURL:(NSURL * _Nonnull)url ``` |

Modified -[ICScannerDeviceDelegate scannerDevice:didScanToURL:data:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)scannerDevice:(ICScannerDevice *)scanner didScanToURL:(NSURL *)url data:(NSData *)data ``` |
| To | ``` - (void)scannerDevice:(ICScannerDevice * _Nonnull)scanner didScanToURL:(NSURL * _Nonnull)url data:(NSData * _Nonnull)data ``` |

Modified -[ICScannerDeviceDelegate scannerDevice:didSelectFunctionalUnit:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)scannerDevice:(ICScannerDevice *)scanner didSelectFunctionalUnit:(ICScannerFunctionalUnit *)functionalUnit error:(NSError *)error ``` |
| To | ``` - (void)scannerDevice:(ICScannerDevice * _Nonnull)scanner didSelectFunctionalUnit:(ICScannerFunctionalUnit * _Nonnull)functionalUnit error:(NSError * _Nullable)error ``` |

Modified -[ICScannerDeviceDelegate scannerDeviceDidBecomeAvailable:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)scannerDeviceDidBecomeAvailable:(ICScannerDevice *)scanner ``` |
| To | ``` - (void)scannerDeviceDidBecomeAvailable:(ICScannerDevice * _Nonnull)scanner ``` |

#### ICScannerFunctionalUnits.h

Modified ICScannerFeature.humanReadableName

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *humanReadableName ``` |
| To | ``` @property(readonly, nullable) NSString *humanReadableName ``` |

Modified ICScannerFeature.internalName

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *internalName ``` |
| To | ``` @property(readonly, nullable) NSString *internalName ``` |

Modified ICScannerFeature.tooltip

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *tooltip ``` |
| To | ``` @property(readonly, nullable) NSString *tooltip ``` |

Modified ICScannerFeatureEnumeration.currentValue

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id currentValue ``` |
| To | ``` @property(assign, nonnull) id currentValue ``` |

Modified ICScannerFeatureEnumeration.defaultValue

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) id defaultValue ``` |
| To | ``` @property(readonly, nonnull) id defaultValue ``` |

Modified ICScannerFeatureEnumeration.menuItemLabels

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *menuItemLabels ``` |
| To | ``` @property(readonly, nonnull) NSArray<NSString *> *menuItemLabels ``` |

Modified ICScannerFeatureEnumeration.menuItemLabelsTooltips

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *menuItemLabelsTooltips ``` |
| To | ``` @property(readonly, nonnull) NSArray<NSString *> *menuItemLabelsTooltips ``` |

Modified ICScannerFeatureEnumeration.values

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *values ``` |
| To | ``` @property(readonly, nonnull) NSArray<NSNumber *> *values ``` |

Modified ICScannerFeatureTemplate.targets

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *targets ``` |
| To | ``` @property(readonly, nonnull) NSArray<NSMutableArray *> *targets ``` |

Modified ICScannerFunctionalUnit.overviewImage

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) CGImageRef overviewImage ``` |
| To | ``` @property(readonly, nullable) CGImageRef overviewImage ``` |

Modified ICScannerFunctionalUnit.preferredResolutions

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSIndexSet *preferredResolutions ``` |
| To | ``` @property(readonly, nonnull) NSIndexSet *preferredResolutions ``` |

Modified ICScannerFunctionalUnit.preferredScaleFactors

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSIndexSet *preferredScaleFactors ``` |
| To | ``` @property(readonly, nonnull) NSIndexSet *preferredScaleFactors ``` |

Modified ICScannerFunctionalUnit.supportedBitDepths

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSIndexSet *supportedBitDepths ``` |
| To | ``` @property(readonly, nonnull) NSIndexSet *supportedBitDepths ``` |

Modified ICScannerFunctionalUnit.supportedMeasurementUnits

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSIndexSet *supportedMeasurementUnits ``` |
| To | ``` @property(readonly, nonnull) NSIndexSet *supportedMeasurementUnits ``` |

Modified ICScannerFunctionalUnit.supportedResolutions

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSIndexSet *supportedResolutions ``` |
| To | ``` @property(readonly, nonnull) NSIndexSet *supportedResolutions ``` |

Modified ICScannerFunctionalUnit.supportedScaleFactors

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSIndexSet *supportedScaleFactors ``` |
| To | ``` @property(readonly, nonnull) NSIndexSet *supportedScaleFactors ``` |

Modified ICScannerFunctionalUnit.templates

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *templates ``` |
| To | ``` @property(readonly, nonnull) NSArray<ICScannerFeatureTemplate *> *templates ``` |

Modified ICScannerFunctionalUnit.vendorFeatures

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *vendorFeatures ``` |
| To | ``` @property(readonly, nullable) NSArray<ICScannerFeature *> *vendorFeatures ``` |

Modified ICScannerFunctionalUnitDocumentFeeder.supportedDocumentTypes

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSIndexSet *supportedDocumentTypes ``` |
| To | ``` @property(readonly, nonnull) NSIndexSet *supportedDocumentTypes ``` |

Modified ICScannerFunctionalUnitFlatbed.supportedDocumentTypes

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSIndexSet *supportedDocumentTypes ``` |
| To | ``` @property(readonly, nonnull) NSIndexSet *supportedDocumentTypes ``` |

Modified ICScannerFunctionalUnitNegativeTransparency.supportedDocumentTypes

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSIndexSet *supportedDocumentTypes ``` |
| To | ``` @property(readonly, nonnull) NSIndexSet *supportedDocumentTypes ``` |

Modified ICScannerFunctionalUnitPositiveTransparency.supportedDocumentTypes

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSIndexSet *supportedDocumentTypes ``` |
| To | ``` @property(readonly, nonnull) NSIndexSet *supportedDocumentTypes ``` |

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
