---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/Quartz.html
archived_at: '2026-07-18T02:52:37.086490Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# Quartz Changes

## Quartz

Added CIFilter.viewForUIConfiguration([NSObject: AnyObject]!, excludedKeys:[AnyObject]!) -> IKFilterUIView!Added NSObject.PDFViewOpenPDF(PDFView!, forRemoteGoToAction: PDFActionRemoteGoTo!)Added NSObject.PDFViewPerformFind(PDFView!)Added NSObject.PDFViewPerformGoToPage(PDFView!)Added NSObject.PDFViewPerformPrint(PDFView!)Added NSObject.PDFViewPrintJobTitle(PDFView!) -> String!Added NSObject.PDFViewWillChangeScaleFactor(PDFView!, toScale: CGFloat) -> CGFloatAdded NSObject.PDFViewWillClickOnLink(PDFView!, withURL: NSURL!)Added NSObject.acceptsPreviewPanelControl(QLPreviewPanel!) -> BoolAdded NSObject.beginPreviewPanelControl(QLPreviewPanel!)Added NSObject.classForAnnotationClass(AnyClass!) -> AnyClass!Added NSObject.classForPage() -> AnyClass!Added NSObject.compositionParameterView(QCCompositionParameterView!, didChangeParameterWithKey: String!)Added NSObject.compositionParameterView(QCCompositionParameterView!, shouldDisplayParameterWithKey: String!, attributes:[NSObject: AnyObject]!) -> BoolAdded NSObject.compositionPickerView(QCCompositionPickerView!, didSelectComposition: QCComposition!)Added NSObject.compositionPickerViewDidStartAnimating(QCCompositionPickerView!)Added NSObject.compositionPickerViewWillStopAnimating(QCCompositionPickerView!)Added NSObject.didMatchString(PDFSelection!)Added NSObject.documentDidBeginDocumentFind(NSNotification!)Added NSObject.documentDidBeginPageFind(NSNotification!)Added NSObject.documentDidEndDocumentFind(NSNotification!)Added NSObject.documentDidEndPageFind(NSNotification!)Added NSObject.documentDidFindMatch(NSNotification!)Added NSObject.documentDidUnlock(NSNotification!)Added NSObject.endPreviewPanelControl(QLPreviewPanel!)Added NSObject.imageBrowser(IKImageBrowserView!, backgroundWasRightClickedWithEvent: NSEvent!)Added NSObject.imageBrowser(IKImageBrowserView!, cellWasDoubleClickedAtIndex: Int)Added NSObject.imageBrowser(IKImageBrowserView!, cellWasRightClickedAtIndex: Int, withEvent: NSEvent!)Added NSObject.imageBrowser(IKImageBrowserView!, groupAtIndex: Int) -> [NSObject: AnyObject]!Added NSObject.imageBrowser(IKImageBrowserView!, itemAtIndex: Int) -> AnyObject!Added NSObject.imageBrowser(IKImageBrowserView!, moveItemsAtIndexes: NSIndexSet!, toIndex: Int) -> BoolAdded NSObject.imageBrowser(IKImageBrowserView!, removeItemsAtIndexes: NSIndexSet!)Added NSObject.imageBrowser(IKImageBrowserView!, writeItemsAtIndexes: NSIndexSet!, toPasteboard: NSPasteboard!) -> IntAdded NSObject.imageBrowserSelectionDidChange(IKImageBrowserView!)Added NSObject.imageRepresentation() -> AnyObject!Added NSObject.imageRepresentationType() -> String!Added NSObject.imageSubtitle() -> String!Added NSObject.imageTitle() -> String!Added NSObject.imageUID() -> String!Added NSObject.imageVersion() -> IntAdded NSObject.isSelectable() -> BoolAdded NSObject.numberOfGroupsInImageBrowser(IKImageBrowserView!) -> IntAdded NSObject.numberOfItemsInImageBrowser(IKImageBrowserView!) -> IntAdded NSObject.quartzFilterManager(QuartzFilterManager!, didAddFilter: QuartzFilter!)Added NSObject.quartzFilterManager(QuartzFilterManager!, didModifyFilter: QuartzFilter!)Added NSObject.quartzFilterManager(QuartzFilterManager!, didRemoveFilter: QuartzFilter!)Added NSObject.quartzFilterManager(QuartzFilterManager!, didSelectFilter: QuartzFilter!)Added NSObject.saveOptions(IKSaveOptions!, shouldShowUTType: String!) -> BoolAdded PDFView.areaOfInterestForPoint(NSPoint) -> PDFAreaOfInterestAdded IK_PhotosBundleIdentifierAdded kPDFImageAreaModified IKCameraDeviceView.cameraDevice

|  | Declaration |
| --- | --- |
| From | ``` var cameraDevice: ICCameraDevice! ``` |
| To | ``` unowned(unsafe) var cameraDevice: ICCameraDevice! ``` |

Modified IKCameraDeviceView.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: IKCameraDeviceViewDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: IKCameraDeviceViewDelegate! ``` |

Modified IKCameraDeviceViewDelegate.cameraDeviceView(IKCameraDeviceView!, didDownloadFile: ICCameraFile!, location: NSURL!, fileData: NSData!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IKCameraDeviceViewDelegate.cameraDeviceView(IKCameraDeviceView!, didEncounterError: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IKCameraDeviceViewDelegate.cameraDeviceViewSelectionDidChange(IKCameraDeviceView!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IKDeviceBrowserView.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: IKDeviceBrowserViewDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: IKDeviceBrowserViewDelegate! ``` |

Modified IKDeviceBrowserViewDelegate.deviceBrowserView(IKDeviceBrowserView!, didEncounterError: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IKFilterBrowserPanel.beginSheetWithOptions([NSObject: AnyObject]!, modalForWindow: NSWindow!, modalDelegate: AnyObject!, didEndSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func beginSheetWithOptions(_ inOptions: [NSObject : AnyObject]!, modalForWindow docWindow: NSWindow!, modalDelegate modalDelegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafePointer<()>) ``` |
| To | ``` func beginSheetWithOptions(_ inOptions: [NSObject : AnyObject]!, modalForWindow docWindow: NSWindow!, modalDelegate modalDelegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |

Modified IKFilterBrowserPanel.beginWithOptions([NSObject: AnyObject]!, modelessDelegate: AnyObject!, didEndSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func beginWithOptions(_ inOptions: [NSObject : AnyObject]!, modelessDelegate modelessDelegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafePointer<()>) ``` |
| To | ``` func beginWithOptions(_ inOptions: [NSObject : AnyObject]!, modelessDelegate modelessDelegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |

Modified IKFilterUIView.init(frame: NSRect, filter: CIFilter!)

|  | Declaration |
| --- | --- |
| From | ``` init(frame frameRect: NSRect, filter inFilter: CIFilter!) ``` |
| To | ``` init!(frame frameRect: NSRect, filter inFilter: CIFilter!) ``` |

Modified IKImageBrowserView.init(frame: NSRect)

|  | Declaration |
| --- | --- |
| From | ``` init(frame frame: NSRect) ``` |
| To | ``` init!(frame frame: NSRect) ``` |

Modified IKImageEditPanel.dataSource

|  | Declaration |
| --- | --- |
| From | ``` var dataSource: IKImageEditPanelDataSource! ``` |
| To | ``` unowned(unsafe) var dataSource: IKImageEditPanelDataSource! ``` |

Modified IKImageEditPanelDataSource.hasAdjustMode() -> Bool

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IKImageEditPanelDataSource.hasDetailsMode() -> Bool

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IKImageEditPanelDataSource.hasEffectsMode() -> Bool

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IKImageEditPanelDataSource.imageProperties() -> [NSObject: AnyObject]!

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IKImageEditPanelDataSource.thumbnailWithMaximumSize(NSSize) -> Unmanaged<CGImage>!

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IKImageView.backgroundColor

|  | Declaration |
| --- | --- |
| From | ``` var backgroundColor: NSColor! ``` |
| To | ``` unowned(unsafe) var backgroundColor: NSColor! ``` |

Modified IKImageView.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: AnyObject! ``` |
| To | ``` unowned(unsafe) var delegate: AnyObject! ``` |

Modified IKImageView.imageCorrection

|  | Declaration |
| --- | --- |
| From | ``` var imageCorrection: CIFilter! ``` |
| To | ``` unowned(unsafe) var imageCorrection: CIFilter! ``` |

Modified IKPictureTaker.beginPictureTakerSheetForWindow(NSWindow!, withDelegate: AnyObject!, didEndSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func beginPictureTakerSheetForWindow(_ aWindow: NSWindow!, withDelegate delegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafePointer<()>) ``` |
| To | ``` func beginPictureTakerSheetForWindow(_ aWindow: NSWindow!, withDelegate delegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |

Modified IKPictureTaker.beginPictureTakerWithDelegate(AnyObject!, didEndSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func beginPictureTakerWithDelegate(_ delegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafePointer<()>) ``` |
| To | ``` func beginPictureTakerWithDelegate(_ delegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |

Modified IKPictureTaker.popUpRecentsMenuForView(NSView!, withDelegate: AnyObject!, didEndSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func popUpRecentsMenuForView(_ aView: NSView!, withDelegate delegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafePointer<()>) ``` |
| To | ``` func popUpRecentsMenuForView(_ aView: NSView!, withDelegate delegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |

Modified IKSaveOptions.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: AnyObject! ``` |
| To | ``` unowned(unsafe) var delegate: AnyObject! ``` |

Modified IKSaveOptions.init(imageProperties: [NSObject: AnyObject]!, imageUTType: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(imageProperties imageProperties: [NSObject : AnyObject]!, imageUTType imageUTType: String!) ``` |
| To | ``` init!(imageProperties imageProperties: [NSObject : AnyObject]!, imageUTType imageUTType: String!) ``` |

Modified IKScannerDeviceView.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: IKScannerDeviceViewDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: IKScannerDeviceViewDelegate! ``` |

Modified IKScannerDeviceView.scannerDevice

|  | Declaration |
| --- | --- |
| From | ``` var scannerDevice: ICScannerDevice! ``` |
| To | ``` unowned(unsafe) var scannerDevice: ICScannerDevice! ``` |

Modified IKScannerDeviceViewDelegate.scannerDeviceView(IKScannerDeviceView!, didEncounterError: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IKScannerDeviceViewDelegate.scannerDeviceView(IKScannerDeviceView!, didScanToBandData: ICScannerBandData!, scanInfo:[NSObject: AnyObject]!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IKScannerDeviceViewDelegate.scannerDeviceView(IKScannerDeviceView!, didScanToURL: NSURL!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IKScannerDeviceViewDelegate.scannerDeviceView(IKScannerDeviceView!, didScanToURL: NSURL!, fileData: NSData!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IKSlideshowDataSource.canExportSlideshowItemAtIndex(Int, toApplication: String!) -> Bool

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IKSlideshowDataSource.nameOfSlideshowItemAtIndex(Int) -> String!

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IKSlideshowDataSource.slideshowDidChangeCurrentIndex(Int)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IKSlideshowDataSource.slideshowDidStop()

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified IKSlideshowDataSource.slideshowWillStart()

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified PDFActionGoTo.init(destination: PDFDestination!)

|  | Declaration |
| --- | --- |
| From | ``` init(destination destination: PDFDestination!) ``` |
| To | ``` init!(destination destination: PDFDestination!) ``` |

Modified PDFActionNamed.init(name: PDFActionNamedName)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: PDFActionNamedName) ``` |
| To | ``` init!(name name: PDFActionNamedName) ``` |

Modified PDFActionRemoteGoTo.init(pageIndex: Int, atPoint: NSPoint, fileURL: NSURL!)

|  | Declaration |
| --- | --- |
| From | ``` init(pageIndex pageIndex: Int, atPoint point: NSPoint, fileURL url: NSURL!) ``` |
| To | ``` init!(pageIndex pageIndex: Int, atPoint point: NSPoint, fileURL url: NSURL!) ``` |

Modified PDFActionResetForm.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified PDFActionURL.init(URL: NSURL!)

|  | Declaration |
| --- | --- |
| From | ``` init(URL url: NSURL!) ``` |
| To | ``` init!(URL url: NSURL!) ``` |

Modified PDFAnnotation.init(bounds: NSRect)

|  | Declaration |
| --- | --- |
| From | ``` init(bounds bounds: NSRect) ``` |
| To | ``` init!(bounds bounds: NSRect) ``` |

Modified PDFDestination.init(page: PDFPage!, atPoint: NSPoint)

|  | Declaration |
| --- | --- |
| From | ``` init(page page: PDFPage!, atPoint point: NSPoint) ``` |
| To | ``` init!(page page: PDFPage!, atPoint point: NSPoint) ``` |

Modified PDFDocument.init(URL: NSURL!)

|  | Declaration |
| --- | --- |
| From | ``` init(URL url: NSURL!) ``` |
| To | ``` init!(URL url: NSURL!) ``` |

Modified PDFDocument.init(data: NSData!)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData!) ``` |
| To | ``` init!(data data: NSData!) ``` |

Modified PDFOutline.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified PDFPage.init(image: NSImage!)

|  | Declaration |
| --- | --- |
| From | ``` init(image image: NSImage!) ``` |
| To | ``` init!(image image: NSImage!) ``` |

Modified PDFSelection.init(document: PDFDocument!)

|  | Declaration |
| --- | --- |
| From | ``` init(document document: PDFDocument!) ``` |
| To | ``` init!(document document: PDFDocument!) ``` |

Modified PDFView

|  | Protocols |
| --- | --- |
| From | AnyObject, NSAnimationDelegate, NSObjectProtocol |
| To | AnyObject, NSAnimationDelegate, NSMenuDelegate, NSObjectProtocol |

Modified QCComposition.init(data: NSData!)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData!) -> QCComposition ``` |
| To | ``` init!(data data: NSData!) -> QCComposition ``` |

Modified QCComposition.init(file: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(file path: String!) -> QCComposition ``` |
| To | ``` init!(file path: String!) -> QCComposition ``` |

Modified QCCompositionLayer.init(composition: QCComposition!)

|  | Declaration |
| --- | --- |
| From | ``` init(composition composition: QCComposition!) ``` |
| To | ``` init!(composition composition: QCComposition!) ``` |

Modified QCCompositionLayer.init(file: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(file path: String!) ``` |
| To | ``` init!(file path: String!) ``` |

Modified QCPlugInContext.outputImageProviderFromBufferWithPixelFormat(String!, pixelsWide: Int, pixelsHigh: Int, baseAddress: UnsafePointer<Void>, bytesPerRow: Int, releaseCallback: QCPlugInBufferReleaseCallback, releaseContext: UnsafeMutablePointer<Void>, colorSpace: CGColorSpace!, shouldColorMatch: Bool) -> AnyObject!

|  | Declaration |
| --- | --- |
| From | ``` func outputImageProviderFromBufferWithPixelFormat(_ format: String!, pixelsWide width: Int, pixelsHigh height: Int, baseAddress baseAddress: ConstUnsafePointer<()>, bytesPerRow rowBytes: Int, releaseCallback callback: QCPlugInBufferReleaseCallback, releaseContext context: UnsafePointer<()>, colorSpace colorSpace: CGColorSpace!, shouldColorMatch colorMatch: Bool) -> AnyObject! ``` |
| To | ``` func outputImageProviderFromBufferWithPixelFormat(_ format: String!, pixelsWide width: Int, pixelsHigh height: Int, baseAddress baseAddress: UnsafePointer<Void>, bytesPerRow rowBytes: Int, releaseCallback callback: QCPlugInBufferReleaseCallback, releaseContext context: UnsafeMutablePointer<Void>, colorSpace colorSpace: CGColorSpace!, shouldColorMatch colorMatch: Bool) -> AnyObject! ``` |

Modified QCPlugInContext.outputImageProviderFromTextureWithPixelFormat(String!, pixelsWide: Int, pixelsHigh: Int, name: GLuint, flipped: Bool, releaseCallback: QCPlugInTextureReleaseCallback, releaseContext: UnsafeMutablePointer<Void>, colorSpace: CGColorSpace!, shouldColorMatch: Bool) -> AnyObject!

|  | Declaration |
| --- | --- |
| From | ``` func outputImageProviderFromTextureWithPixelFormat(_ format: String!, pixelsWide width: Int, pixelsHigh height: Int, name name: GLuint, flipped flipped: Bool, releaseCallback callback: QCPlugInTextureReleaseCallback, releaseContext context: UnsafePointer<()>, colorSpace colorSpace: CGColorSpace!, shouldColorMatch colorMatch: Bool) -> AnyObject! ``` |
| To | ``` func outputImageProviderFromTextureWithPixelFormat(_ format: String!, pixelsWide width: Int, pixelsHigh height: Int, name name: GLuint, flipped flipped: Bool, releaseCallback callback: QCPlugInTextureReleaseCallback, releaseContext context: UnsafeMutablePointer<Void>, colorSpace colorSpace: CGColorSpace!, shouldColorMatch colorMatch: Bool) -> AnyObject! ``` |

Modified QCPlugInInputImageSource.bufferBaseAddress() -> UnsafePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func bufferBaseAddress() -> ConstUnsafePointer<()> ``` |
| To | ``` func bufferBaseAddress() -> UnsafePointer<Void> ``` |

Modified QCPlugInInputImageSource.textureMatrix() -> UnsafePointer<GLfloat>

|  | Declaration |
| --- | --- |
| From | ``` func textureMatrix() -> ConstUnsafePointer<GLfloat> ``` |
| To | ``` func textureMatrix() -> UnsafePointer<GLfloat> ``` |

Modified QCPlugInOutputImageProvider.canRenderWithCGLContext(CGLContextObj) -> Bool

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified QCPlugInOutputImageProvider.copyRenderedTextureForCGLContext(CGLContextObj, pixelFormat: String!, bounds: NSRect, isFlipped: UnsafeMutablePointer<ObjCBool>) -> GLuint

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func copyRenderedTextureForCGLContext(_ cgl_ctx: CGLContextObj, pixelFormat format: String!, bounds bounds: NSRect, isFlipped flipped: UnsafePointer<ObjCBool>) -> GLuint ``` | -- |
| To | ``` optional func copyRenderedTextureForCGLContext(_ cgl_ctx: CGLContextObj, pixelFormat format: String!, bounds bounds: NSRect, isFlipped flipped: UnsafeMutablePointer<ObjCBool>) -> GLuint ``` | yes |

Modified QCPlugInOutputImageProvider.releaseRenderedTexture(GLuint, forCGLContext: CGLContextObj)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified QCPlugInOutputImageProvider.renderToBuffer(UnsafeMutablePointer<Void>, withBytesPerRow: Int, pixelFormat: String!, forBounds: NSRect) -> Bool

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func renderToBuffer(_ baseAddress: UnsafePointer<()>, withBytesPerRow rowBytes: Int, pixelFormat format: String!, forBounds bounds: NSRect) -> Bool ``` | -- |
| To | ``` optional func renderToBuffer(_ baseAddress: UnsafeMutablePointer<Void>, withBytesPerRow rowBytes: Int, pixelFormat format: String!, forBounds bounds: NSRect) -> Bool ``` | yes |

Modified QCPlugInOutputImageProvider.renderWithCGLContext(CGLContextObj, forBounds: NSRect) -> Bool

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified QCPlugInOutputImageProvider.shouldColorMatch() -> Bool

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified QCPlugInOutputImageProvider.supportedBufferPixelFormats() -> [AnyObject]!

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified QCPlugInOutputImageProvider.supportedRenderedTexturePixelFormats() -> [AnyObject]!

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified QCPlugInViewController.init(plugIn: QCPlugIn!, viewNibName: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(plugIn plugIn: QCPlugIn!, viewNibName name: String!) ``` |
| To | ``` init!(plugIn plugIn: QCPlugIn!, viewNibName name: String!) ``` |

Modified QCRenderer.init(CGLContext: CGLContextObj, pixelFormat: CGLPixelFormatObj, colorSpace: CGColorSpace!, composition: QCComposition!)

|  | Declaration |
| --- | --- |
| From | ``` init(CGLContext context: CGLContextObj, pixelFormat format: CGLPixelFormatObj, colorSpace colorSpace: CGColorSpace!, composition composition: QCComposition!) ``` |
| To | ``` init!(CGLContext context: CGLContextObj, pixelFormat format: CGLPixelFormatObj, colorSpace colorSpace: CGColorSpace!, composition composition: QCComposition!) ``` |

Modified QCRenderer.init(composition: QCComposition!, colorSpace: CGColorSpace!)

|  | Declaration |
| --- | --- |
| From | ``` init(composition composition: QCComposition!, colorSpace colorSpace: CGColorSpace!) ``` |
| To | ``` init!(composition composition: QCComposition!, colorSpace colorSpace: CGColorSpace!) ``` |

Modified QCRenderer.init(offScreenWithSize: NSSize, colorSpace: CGColorSpace!, composition: QCComposition!)

|  | Declaration |
| --- | --- |
| From | ``` init(offScreenWithSize size: NSSize, colorSpace colorSpace: CGColorSpace!, composition composition: QCComposition!) ``` |
| To | ``` init!(offScreenWithSize size: NSSize, colorSpace colorSpace: CGColorSpace!, composition composition: QCComposition!) ``` |

Modified QCRenderer.init(openGLContext: NSOpenGLContext!, pixelFormat: NSOpenGLPixelFormat!, file: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(openGLContext context: NSOpenGLContext!, pixelFormat format: NSOpenGLPixelFormat!, file path: String!) ``` |
| To | ``` init!(openGLContext context: NSOpenGLContext!, pixelFormat format: NSOpenGLPixelFormat!, file path: String!) ``` |

Modified QLPreviewItem

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified QLPreviewItem.previewItemDisplayState

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified QLPreviewItem.previewItemTitle

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified QLPreviewPanel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified QLPreviewPanel.dataSource

|  | Declaration |
| --- | --- |
| From | ``` var dataSource: QLPreviewPanelDataSource! ``` |
| To | ``` unowned(unsafe) var dataSource: QLPreviewPanelDataSource! ``` |

Modified QLPreviewPanel.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: QLPreviewPanelDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: QLPreviewPanelDelegate! ``` |

Modified QLPreviewPanelDelegate.previewPanel(QLPreviewPanel!, handleEvent: NSEvent!) -> Bool

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified QLPreviewPanelDelegate.previewPanel(QLPreviewPanel!, sourceFrameOnScreenForPreviewItem: QLPreviewItem!) -> NSRect

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified QLPreviewPanelDelegate.previewPanel(QLPreviewPanel!, transitionImageForPreviewItem: QLPreviewItem!, contentRect: UnsafeMutablePointer<NSRect>) -> AnyObject!

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func previewPanel(_ panel: QLPreviewPanel!, transitionImageForPreviewItem item: QLPreviewItem!, contentRect contentRect: UnsafePointer<NSRect>) -> AnyObject! ``` | -- |
| To | ``` optional func previewPanel(_ panel: QLPreviewPanel!, transitionImageForPreviewItem item: QLPreviewItem!, contentRect contentRect: UnsafeMutablePointer<NSRect>) -> AnyObject! ``` | yes |

Modified QLPreviewView

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified QLPreviewView.init(frame: NSRect)

|  | Declaration |
| --- | --- |
| From | ``` init(frame frame: NSRect) ``` |
| To | ``` init!(frame frame: NSRect) ``` |

Modified QLPreviewView.init(frame: NSRect, style: QLPreviewViewStyle)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(frame frame: NSRect, style style: QLPreviewViewStyle) ``` | OS X 10.10 |
| To | ``` init!(frame frame: NSRect, style style: QLPreviewViewStyle) ``` | OS X 10.7 |

Modified QLPreviewViewStyle [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified QuartzFilter.init(URL: NSURL!)

|  | Declaration |
| --- | --- |
| From | ``` init(URL aURL: NSURL!) -> QuartzFilter ``` |
| To | ``` init!(URL aURL: NSURL!) -> QuartzFilter ``` |

Modified QuartzFilter.init(outputIntents: [AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(outputIntents outputIntents: [AnyObject]!) -> QuartzFilter ``` |
| To | ``` init!(outputIntents outputIntents: [AnyObject]!) -> QuartzFilter ``` |

Modified QuartzFilter.init(properties: [NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(properties properties: [NSObject : AnyObject]!) -> QuartzFilter ``` |
| To | ``` init!(properties properties: [NSObject : AnyObject]!) -> QuartzFilter ``` |

Modified IKFilterBrowserDefaultInputImage

|  | Declaration |
| --- | --- |
| From | ``` let IKFilterBrowserDefaultInputImage: NSString! ``` |
| To | ``` let IKFilterBrowserDefaultInputImage: String ``` |

Modified IKFilterBrowserExcludeCategories

|  | Declaration |
| --- | --- |
| From | ``` let IKFilterBrowserExcludeCategories: NSString! ``` |
| To | ``` let IKFilterBrowserExcludeCategories: String ``` |

Modified IKFilterBrowserExcludeFilters

|  | Declaration |
| --- | --- |
| From | ``` let IKFilterBrowserExcludeFilters: NSString! ``` |
| To | ``` let IKFilterBrowserExcludeFilters: String ``` |

Modified IKFilterBrowserFilterDoubleClickNotification

|  | Declaration |
| --- | --- |
| From | ``` let IKFilterBrowserFilterDoubleClickNotification: NSString! ``` |
| To | ``` let IKFilterBrowserFilterDoubleClickNotification: String ``` |

Modified IKFilterBrowserFilterSelectedNotification

|  | Declaration |
| --- | --- |
| From | ``` let IKFilterBrowserFilterSelectedNotification: NSString! ``` |
| To | ``` let IKFilterBrowserFilterSelectedNotification: String ``` |

Modified IKFilterBrowserShowCategories

|  | Declaration |
| --- | --- |
| From | ``` let IKFilterBrowserShowCategories: NSString! ``` |
| To | ``` let IKFilterBrowserShowCategories: String ``` |

Modified IKFilterBrowserShowPreview

|  | Declaration |
| --- | --- |
| From | ``` let IKFilterBrowserShowPreview: NSString! ``` |
| To | ``` let IKFilterBrowserShowPreview: String ``` |

Modified IKFilterBrowserWillPreviewFilterNotification

|  | Declaration |
| --- | --- |
| From | ``` let IKFilterBrowserWillPreviewFilterNotification: NSString! ``` |
| To | ``` let IKFilterBrowserWillPreviewFilterNotification: String ``` |

Modified IKImageBrowserBackgroundColorKey

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserBackgroundColorKey: NSString! ``` |
| To | ``` let IKImageBrowserBackgroundColorKey: String ``` |

Modified IKImageBrowserCGImageRepresentationType

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserCGImageRepresentationType: NSString! ``` |
| To | ``` let IKImageBrowserCGImageRepresentationType: String ``` |

Modified IKImageBrowserCGImageSourceRepresentationType

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserCGImageSourceRepresentationType: NSString! ``` |
| To | ``` let IKImageBrowserCGImageSourceRepresentationType: String ``` |

Modified IKImageBrowserCellBackgroundLayer

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserCellBackgroundLayer: NSString! ``` |
| To | ``` let IKImageBrowserCellBackgroundLayer: String ``` |

Modified IKImageBrowserCellForegroundLayer

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserCellForegroundLayer: NSString! ``` |
| To | ``` let IKImageBrowserCellForegroundLayer: String ``` |

Modified IKImageBrowserCellPlaceHolderLayer

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserCellPlaceHolderLayer: NSString! ``` |
| To | ``` let IKImageBrowserCellPlaceHolderLayer: String ``` |

Modified IKImageBrowserCellSelectionLayer

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserCellSelectionLayer: NSString! ``` |
| To | ``` let IKImageBrowserCellSelectionLayer: String ``` |

Modified IKImageBrowserCellsHighlightedTitleAttributesKey

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserCellsHighlightedTitleAttributesKey: NSString! ``` |
| To | ``` let IKImageBrowserCellsHighlightedTitleAttributesKey: String ``` |

Modified IKImageBrowserCellsOutlineColorKey

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserCellsOutlineColorKey: NSString! ``` |
| To | ``` let IKImageBrowserCellsOutlineColorKey: String ``` |

Modified IKImageBrowserCellsSubtitleAttributesKey

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserCellsSubtitleAttributesKey: NSString! ``` |
| To | ``` let IKImageBrowserCellsSubtitleAttributesKey: String ``` |

Modified IKImageBrowserCellsTitleAttributesKey

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserCellsTitleAttributesKey: NSString! ``` |
| To | ``` let IKImageBrowserCellsTitleAttributesKey: String ``` |

Modified IKImageBrowserGroupBackgroundColorKey

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserGroupBackgroundColorKey: NSString! ``` |
| To | ``` let IKImageBrowserGroupBackgroundColorKey: String ``` |

Modified IKImageBrowserGroupFooterLayer

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserGroupFooterLayer: NSString! ``` |
| To | ``` let IKImageBrowserGroupFooterLayer: String ``` |

Modified IKImageBrowserGroupHeaderLayer

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserGroupHeaderLayer: NSString! ``` |
| To | ``` let IKImageBrowserGroupHeaderLayer: String ``` |

Modified IKImageBrowserGroupRangeKey

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserGroupRangeKey: NSString! ``` |
| To | ``` let IKImageBrowserGroupRangeKey: String ``` |

Modified IKImageBrowserGroupStyleKey

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserGroupStyleKey: NSString! ``` |
| To | ``` let IKImageBrowserGroupStyleKey: String ``` |

Modified IKImageBrowserGroupTitleKey

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserGroupTitleKey: NSString! ``` |
| To | ``` let IKImageBrowserGroupTitleKey: String ``` |

Modified IKImageBrowserIconRefPathRepresentationType

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserIconRefPathRepresentationType: NSString! ``` |
| To | ``` let IKImageBrowserIconRefPathRepresentationType: String ``` |

Modified IKImageBrowserIconRefRepresentationType

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserIconRefRepresentationType: NSString! ``` |
| To | ``` let IKImageBrowserIconRefRepresentationType: String ``` |

Modified IKImageBrowserNSBitmapImageRepresentationType

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserNSBitmapImageRepresentationType: NSString! ``` |
| To | ``` let IKImageBrowserNSBitmapImageRepresentationType: String ``` |

Modified IKImageBrowserNSDataRepresentationType

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserNSDataRepresentationType: NSString! ``` |
| To | ``` let IKImageBrowserNSDataRepresentationType: String ``` |

Modified IKImageBrowserNSImageRepresentationType

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserNSImageRepresentationType: NSString! ``` |
| To | ``` let IKImageBrowserNSImageRepresentationType: String ``` |

Modified IKImageBrowserNSURLRepresentationType

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserNSURLRepresentationType: NSString! ``` |
| To | ``` let IKImageBrowserNSURLRepresentationType: String ``` |

Modified IKImageBrowserPDFPageRepresentationType

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserPDFPageRepresentationType: NSString! ``` |
| To | ``` let IKImageBrowserPDFPageRepresentationType: String ``` |

Modified IKImageBrowserPathRepresentationType

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserPathRepresentationType: NSString! ``` |
| To | ``` let IKImageBrowserPathRepresentationType: String ``` |

Modified IKImageBrowserQCCompositionPathRepresentationType

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserQCCompositionPathRepresentationType: NSString! ``` |
| To | ``` let IKImageBrowserQCCompositionPathRepresentationType: String ``` |

Modified IKImageBrowserQCCompositionRepresentationType

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserQCCompositionRepresentationType: NSString! ``` |
| To | ``` let IKImageBrowserQCCompositionRepresentationType: String ``` |

Modified IKImageBrowserQTMoviePathRepresentationType

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserQTMoviePathRepresentationType: NSString! ``` |
| To | ``` let IKImageBrowserQTMoviePathRepresentationType: String ``` |

Modified IKImageBrowserQTMovieRepresentationType

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserQTMovieRepresentationType: NSString! ``` |
| To | ``` let IKImageBrowserQTMovieRepresentationType: String ``` |

Modified IKImageBrowserQuickLookPathRepresentationType

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserQuickLookPathRepresentationType: NSString! ``` |
| To | ``` let IKImageBrowserQuickLookPathRepresentationType: String ``` |

Modified IKImageBrowserSelectionColorKey

|  | Declaration |
| --- | --- |
| From | ``` let IKImageBrowserSelectionColorKey: NSString! ``` |
| To | ``` let IKImageBrowserSelectionColorKey: String ``` |

Modified IKOverlayTypeBackground

|  | Declaration |
| --- | --- |
| From | ``` let IKOverlayTypeBackground: NSString! ``` |
| To | ``` let IKOverlayTypeBackground: String ``` |

Modified IKOverlayTypeImage

|  | Declaration |
| --- | --- |
| From | ``` let IKOverlayTypeImage: NSString! ``` |
| To | ``` let IKOverlayTypeImage: String ``` |

Modified IKPictureTakerAllowsEditingKey

|  | Declaration |
| --- | --- |
| From | ``` let IKPictureTakerAllowsEditingKey: NSString! ``` |
| To | ``` let IKPictureTakerAllowsEditingKey: String ``` |

Modified IKPictureTakerAllowsFileChoosingKey

|  | Declaration |
| --- | --- |
| From | ``` let IKPictureTakerAllowsFileChoosingKey: NSString! ``` |
| To | ``` let IKPictureTakerAllowsFileChoosingKey: String ``` |

Modified IKPictureTakerAllowsVideoCaptureKey

|  | Declaration |
| --- | --- |
| From | ``` let IKPictureTakerAllowsVideoCaptureKey: NSString! ``` |
| To | ``` let IKPictureTakerAllowsVideoCaptureKey: String ``` |

Modified IKPictureTakerImageTransformsKey

|  | Declaration |
| --- | --- |
| From | ``` let IKPictureTakerImageTransformsKey: NSString! ``` |
| To | ``` let IKPictureTakerImageTransformsKey: String ``` |

Modified IKPictureTakerInformationalTextKey

|  | Declaration |
| --- | --- |
| From | ``` let IKPictureTakerInformationalTextKey: NSString! ``` |
| To | ``` let IKPictureTakerInformationalTextKey: String ``` |

Modified IKPictureTakerOutputImageMaxSizeKey

|  | Declaration |
| --- | --- |
| From | ``` let IKPictureTakerOutputImageMaxSizeKey: NSString! ``` |
| To | ``` let IKPictureTakerOutputImageMaxSizeKey: String ``` |

Modified IKPictureTakerRemainOpenAfterValidateKey

|  | Declaration |
| --- | --- |
| From | ``` let IKPictureTakerRemainOpenAfterValidateKey: NSString! ``` |
| To | ``` let IKPictureTakerRemainOpenAfterValidateKey: String ``` |

Modified IKPictureTakerShowAddressBookPictureKey

|  | Declaration |
| --- | --- |
| From | ``` let IKPictureTakerShowAddressBookPictureKey: NSString! ``` |
| To | ``` let IKPictureTakerShowAddressBookPictureKey: String ``` |

Modified IKPictureTakerShowEffectsKey

|  | Declaration |
| --- | --- |
| From | ``` let IKPictureTakerShowEffectsKey: NSString! ``` |
| To | ``` let IKPictureTakerShowEffectsKey: String ``` |

Modified IKPictureTakerShowEmptyPictureKey

|  | Declaration |
| --- | --- |
| From | ``` let IKPictureTakerShowEmptyPictureKey: NSString! ``` |
| To | ``` let IKPictureTakerShowEmptyPictureKey: String ``` |

Modified IKPictureTakerShowRecentPictureKey

|  | Declaration |
| --- | --- |
| From | ``` let IKPictureTakerShowRecentPictureKey: NSString! ``` |
| To | ``` let IKPictureTakerShowRecentPictureKey: String ``` |

Modified IKPictureTakerUpdateRecentPictureKey

|  | Declaration |
| --- | --- |
| From | ``` let IKPictureTakerUpdateRecentPictureKey: NSString! ``` |
| To | ``` let IKPictureTakerUpdateRecentPictureKey: String ``` |

Modified IKSlideshowAudioFile

|  | Declaration |
| --- | --- |
| From | ``` let IKSlideshowAudioFile: NSString! ``` |
| To | ``` let IKSlideshowAudioFile: String ``` |

Modified IKSlideshowModeImages

|  | Declaration |
| --- | --- |
| From | ``` let IKSlideshowModeImages: NSString! ``` |
| To | ``` let IKSlideshowModeImages: String ``` |

Modified IKSlideshowModeOther

|  | Declaration |
| --- | --- |
| From | ``` let IKSlideshowModeOther: NSString! ``` |
| To | ``` let IKSlideshowModeOther: String ``` |

Modified IKSlideshowModePDF

|  | Declaration |
| --- | --- |
| From | ``` let IKSlideshowModePDF: NSString! ``` |
| To | ``` let IKSlideshowModePDF: String ``` |

Modified IKSlideshowPDFDisplayBox

|  | Declaration |
| --- | --- |
| From | ``` let IKSlideshowPDFDisplayBox: NSString! ``` |
| To | ``` let IKSlideshowPDFDisplayBox: String ``` |

Modified IKSlideshowPDFDisplayMode

|  | Declaration |
| --- | --- |
| From | ``` let IKSlideshowPDFDisplayMode: NSString! ``` |
| To | ``` let IKSlideshowPDFDisplayMode: String ``` |

Modified IKSlideshowPDFDisplaysAsBook

|  | Declaration |
| --- | --- |
| From | ``` let IKSlideshowPDFDisplaysAsBook: NSString! ``` |
| To | ``` let IKSlideshowPDFDisplaysAsBook: String ``` |

Modified IKSlideshowScreen

|  | Declaration |
| --- | --- |
| From | ``` let IKSlideshowScreen: NSString! ``` |
| To | ``` let IKSlideshowScreen: String ``` |

Modified IKSlideshowStartIndex

|  | Declaration |
| --- | --- |
| From | ``` let IKSlideshowStartIndex: NSString! ``` |
| To | ``` let IKSlideshowStartIndex: String ``` |

Modified IKSlideshowStartPaused

|  | Declaration |
| --- | --- |
| From | ``` let IKSlideshowStartPaused: NSString! ``` |
| To | ``` let IKSlideshowStartPaused: String ``` |

Modified IKSlideshowWrapAround

|  | Declaration |
| --- | --- |
| From | ``` let IKSlideshowWrapAround: NSString! ``` |
| To | ``` let IKSlideshowWrapAround: String ``` |

Modified IKToolModeAnnotate

|  | Declaration |
| --- | --- |
| From | ``` let IKToolModeAnnotate: NSString! ``` |
| To | ``` let IKToolModeAnnotate: String ``` |

Modified IKToolModeCrop

|  | Declaration |
| --- | --- |
| From | ``` let IKToolModeCrop: NSString! ``` |
| To | ``` let IKToolModeCrop: String ``` |

Modified IKToolModeMove

|  | Declaration |
| --- | --- |
| From | ``` let IKToolModeMove: NSString! ``` |
| To | ``` let IKToolModeMove: String ``` |

Modified IKToolModeNone

|  | Declaration |
| --- | --- |
| From | ``` let IKToolModeNone: NSString! ``` |
| To | ``` let IKToolModeNone: String ``` |

Modified IKToolModeRotate

|  | Declaration |
| --- | --- |
| From | ``` let IKToolModeRotate: NSString! ``` |
| To | ``` let IKToolModeRotate: String ``` |

Modified IKToolModeSelect

|  | Declaration |
| --- | --- |
| From | ``` let IKToolModeSelect: NSString! ``` |
| To | ``` let IKToolModeSelect: String ``` |

Modified IKToolModeSelectEllipse

|  | Declaration |
| --- | --- |
| From | ``` let IKToolModeSelectEllipse: NSString! ``` |
| To | ``` let IKToolModeSelectEllipse: String ``` |

Modified IKToolModeSelectLasso

|  | Declaration |
| --- | --- |
| From | ``` let IKToolModeSelectLasso: NSString! ``` |
| To | ``` let IKToolModeSelectLasso: String ``` |

Modified IKToolModeSelectRect

|  | Declaration |
| --- | --- |
| From | ``` let IKToolModeSelectRect: NSString! ``` |
| To | ``` let IKToolModeSelectRect: String ``` |

Modified IKUIFlavorAllowFallback

|  | Declaration |
| --- | --- |
| From | ``` var IKUIFlavorAllowFallback: NSString! ``` |
| To | ``` let IKUIFlavorAllowFallback: String ``` |

Modified IKUISizeFlavor

|  | Declaration |
| --- | --- |
| From | ``` var IKUISizeFlavor: NSString! ``` |
| To | ``` let IKUISizeFlavor: String ``` |

Modified IKUISizeMini

|  | Declaration |
| --- | --- |
| From | ``` var IKUISizeMini: NSString! ``` |
| To | ``` let IKUISizeMini: String ``` |

Modified IKUISizeRegular

|  | Declaration |
| --- | --- |
| From | ``` var IKUISizeRegular: NSString! ``` |
| To | ``` let IKUISizeRegular: String ``` |

Modified IKUISizeSmall

|  | Declaration |
| --- | --- |
| From | ``` var IKUISizeSmall: NSString! ``` |
| To | ``` let IKUISizeSmall: String ``` |

Modified IKUImaxSize

|  | Declaration |
| --- | --- |
| From | ``` var IKUImaxSize: NSString! ``` |
| To | ``` let IKUImaxSize: String ``` |

Modified IK_ApertureBundleIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let IK_ApertureBundleIdentifier: NSString! ``` |
| To | ``` let IK_ApertureBundleIdentifier: String ``` |

Modified IK_MailBundleIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let IK_MailBundleIdentifier: NSString! ``` |
| To | ``` let IK_MailBundleIdentifier: String ``` |

Modified IK_iPhotoBundleIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let IK_iPhotoBundleIdentifier: NSString! ``` |
| To | ``` let IK_iPhotoBundleIdentifier: String ``` |

Modified PDFDocumentAuthorAttribute

|  | Declaration |
| --- | --- |
| From | ``` var PDFDocumentAuthorAttribute: NSString! ``` |
| To | ``` let PDFDocumentAuthorAttribute: String ``` |

Modified PDFDocumentCreationDateAttribute

|  | Declaration |
| --- | --- |
| From | ``` var PDFDocumentCreationDateAttribute: NSString! ``` |
| To | ``` let PDFDocumentCreationDateAttribute: String ``` |

Modified PDFDocumentCreatorAttribute

|  | Declaration |
| --- | --- |
| From | ``` var PDFDocumentCreatorAttribute: NSString! ``` |
| To | ``` let PDFDocumentCreatorAttribute: String ``` |

Modified PDFDocumentDidBeginFindNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFDocumentDidBeginFindNotification: NSString! ``` |
| To | ``` let PDFDocumentDidBeginFindNotification: String ``` |

Modified PDFDocumentDidBeginPageFindNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFDocumentDidBeginPageFindNotification: NSString! ``` |
| To | ``` let PDFDocumentDidBeginPageFindNotification: String ``` |

Modified PDFDocumentDidBeginPageWriteNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFDocumentDidBeginPageWriteNotification: NSString! ``` |
| To | ``` let PDFDocumentDidBeginPageWriteNotification: String ``` |

Modified PDFDocumentDidBeginWriteNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFDocumentDidBeginWriteNotification: NSString! ``` |
| To | ``` let PDFDocumentDidBeginWriteNotification: String ``` |

Modified PDFDocumentDidEndFindNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFDocumentDidEndFindNotification: NSString! ``` |
| To | ``` let PDFDocumentDidEndFindNotification: String ``` |

Modified PDFDocumentDidEndPageFindNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFDocumentDidEndPageFindNotification: NSString! ``` |
| To | ``` let PDFDocumentDidEndPageFindNotification: String ``` |

Modified PDFDocumentDidEndPageWriteNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFDocumentDidEndPageWriteNotification: NSString! ``` |
| To | ``` let PDFDocumentDidEndPageWriteNotification: String ``` |

Modified PDFDocumentDidEndWriteNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFDocumentDidEndWriteNotification: NSString! ``` |
| To | ``` let PDFDocumentDidEndWriteNotification: String ``` |

Modified PDFDocumentDidFindMatchNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFDocumentDidFindMatchNotification: NSString! ``` |
| To | ``` let PDFDocumentDidFindMatchNotification: String ``` |

Modified PDFDocumentDidUnlockNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFDocumentDidUnlockNotification: NSString! ``` |
| To | ``` let PDFDocumentDidUnlockNotification: String ``` |

Modified PDFDocumentKeywordsAttribute

|  | Declaration |
| --- | --- |
| From | ``` var PDFDocumentKeywordsAttribute: NSString! ``` |
| To | ``` let PDFDocumentKeywordsAttribute: String ``` |

Modified PDFDocumentModificationDateAttribute

|  | Declaration |
| --- | --- |
| From | ``` var PDFDocumentModificationDateAttribute: NSString! ``` |
| To | ``` let PDFDocumentModificationDateAttribute: String ``` |

Modified PDFDocumentProducerAttribute

|  | Declaration |
| --- | --- |
| From | ``` var PDFDocumentProducerAttribute: NSString! ``` |
| To | ``` let PDFDocumentProducerAttribute: String ``` |

Modified PDFDocumentSubjectAttribute

|  | Declaration |
| --- | --- |
| From | ``` var PDFDocumentSubjectAttribute: NSString! ``` |
| To | ``` let PDFDocumentSubjectAttribute: String ``` |

Modified PDFDocumentTitleAttribute

|  | Declaration |
| --- | --- |
| From | ``` var PDFDocumentTitleAttribute: NSString! ``` |
| To | ``` let PDFDocumentTitleAttribute: String ``` |

Modified PDFThumbnailViewDocumentEditedNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFThumbnailViewDocumentEditedNotification: NSString! ``` |
| To | ``` let PDFThumbnailViewDocumentEditedNotification: String ``` |

Modified PDFViewAnnotationHitNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFViewAnnotationHitNotification: NSString! ``` |
| To | ``` let PDFViewAnnotationHitNotification: String ``` |

Modified PDFViewAnnotationWillHitNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFViewAnnotationWillHitNotification: NSString! ``` |
| To | ``` let PDFViewAnnotationWillHitNotification: String ``` |

Modified PDFViewChangedHistoryNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFViewChangedHistoryNotification: NSString! ``` |
| To | ``` let PDFViewChangedHistoryNotification: String ``` |

Modified PDFViewCopyPermissionNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFViewCopyPermissionNotification: NSString! ``` |
| To | ``` let PDFViewCopyPermissionNotification: String ``` |

Modified PDFViewDisplayBoxChangedNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFViewDisplayBoxChangedNotification: NSString! ``` |
| To | ``` let PDFViewDisplayBoxChangedNotification: String ``` |

Modified PDFViewDisplayModeChangedNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFViewDisplayModeChangedNotification: NSString! ``` |
| To | ``` let PDFViewDisplayModeChangedNotification: String ``` |

Modified PDFViewDocumentChangedNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFViewDocumentChangedNotification: NSString! ``` |
| To | ``` let PDFViewDocumentChangedNotification: String ``` |

Modified PDFViewPageChangedNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFViewPageChangedNotification: NSString! ``` |
| To | ``` let PDFViewPageChangedNotification: String ``` |

Modified PDFViewPrintPermissionNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFViewPrintPermissionNotification: NSString! ``` |
| To | ``` let PDFViewPrintPermissionNotification: String ``` |

Modified PDFViewScaleChangedNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFViewScaleChangedNotification: NSString! ``` |
| To | ``` let PDFViewScaleChangedNotification: String ``` |

Modified PDFViewSelectionChangedNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFViewSelectionChangedNotification: NSString! ``` |
| To | ``` let PDFViewSelectionChangedNotification: String ``` |

Modified PDFViewVisiblePagesChangedNotification

|  | Declaration |
| --- | --- |
| From | ``` var PDFViewVisiblePagesChangedNotification: NSString! ``` |
| To | ``` let PDFViewVisiblePagesChangedNotification: String ``` |

Modified QCCompositionAttributeBuiltInKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionAttributeBuiltInKey: NSString! ``` |
| To | ``` let QCCompositionAttributeBuiltInKey: String ``` |

Modified QCCompositionAttributeCategoryKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionAttributeCategoryKey: NSString! ``` |
| To | ``` let QCCompositionAttributeCategoryKey: String ``` |

Modified QCCompositionAttributeCopyrightKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionAttributeCopyrightKey: NSString! ``` |
| To | ``` let QCCompositionAttributeCopyrightKey: String ``` |

Modified QCCompositionAttributeDescriptionKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionAttributeDescriptionKey: NSString! ``` |
| To | ``` let QCCompositionAttributeDescriptionKey: String ``` |

Modified QCCompositionAttributeHasConsumersKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionAttributeHasConsumersKey: NSString! ``` |
| To | ``` let QCCompositionAttributeHasConsumersKey: String ``` |

Modified QCCompositionAttributeIsTimeDependentKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionAttributeIsTimeDependentKey: NSString! ``` |
| To | ``` let QCCompositionAttributeIsTimeDependentKey: String ``` |

Modified QCCompositionAttributeNameKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionAttributeNameKey: NSString! ``` |
| To | ``` let QCCompositionAttributeNameKey: String ``` |

Modified QCCompositionCategoryDistortion

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionCategoryDistortion: NSString! ``` |
| To | ``` let QCCompositionCategoryDistortion: String ``` |

Modified QCCompositionCategoryStylize

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionCategoryStylize: NSString! ``` |
| To | ``` let QCCompositionCategoryStylize: String ``` |

Modified QCCompositionCategoryUtility

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionCategoryUtility: NSString! ``` |
| To | ``` let QCCompositionCategoryUtility: String ``` |

Modified QCCompositionInputAudioPeakKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionInputAudioPeakKey: NSString! ``` |
| To | ``` let QCCompositionInputAudioPeakKey: String ``` |

Modified QCCompositionInputAudioSpectrumKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionInputAudioSpectrumKey: NSString! ``` |
| To | ``` let QCCompositionInputAudioSpectrumKey: String ``` |

Modified QCCompositionInputDestinationImageKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionInputDestinationImageKey: NSString! ``` |
| To | ``` let QCCompositionInputDestinationImageKey: String ``` |

Modified QCCompositionInputImageKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionInputImageKey: NSString! ``` |
| To | ``` let QCCompositionInputImageKey: String ``` |

Modified QCCompositionInputPaceKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionInputPaceKey: NSString! ``` |
| To | ``` let QCCompositionInputPaceKey: String ``` |

Modified QCCompositionInputPreviewModeKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionInputPreviewModeKey: NSString! ``` |
| To | ``` let QCCompositionInputPreviewModeKey: String ``` |

Modified QCCompositionInputPrimaryColorKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionInputPrimaryColorKey: NSString! ``` |
| To | ``` let QCCompositionInputPrimaryColorKey: String ``` |

Modified QCCompositionInputRSSArticleDurationKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionInputRSSArticleDurationKey: NSString! ``` |
| To | ``` let QCCompositionInputRSSArticleDurationKey: String ``` |

Modified QCCompositionInputRSSFeedURLKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionInputRSSFeedURLKey: NSString! ``` |
| To | ``` let QCCompositionInputRSSFeedURLKey: String ``` |

Modified QCCompositionInputScreenImageKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionInputScreenImageKey: NSString! ``` |
| To | ``` let QCCompositionInputScreenImageKey: String ``` |

Modified QCCompositionInputSecondaryColorKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionInputSecondaryColorKey: NSString! ``` |
| To | ``` let QCCompositionInputSecondaryColorKey: String ``` |

Modified QCCompositionInputSourceImageKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionInputSourceImageKey: NSString! ``` |
| To | ``` let QCCompositionInputSourceImageKey: String ``` |

Modified QCCompositionInputTrackInfoKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionInputTrackInfoKey: NSString! ``` |
| To | ``` let QCCompositionInputTrackInfoKey: String ``` |

Modified QCCompositionInputTrackPositionKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionInputTrackPositionKey: NSString! ``` |
| To | ``` let QCCompositionInputTrackPositionKey: String ``` |

Modified QCCompositionInputTrackSignalKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionInputTrackSignalKey: NSString! ``` |
| To | ``` let QCCompositionInputTrackSignalKey: String ``` |

Modified QCCompositionInputXKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionInputXKey: NSString! ``` |
| To | ``` let QCCompositionInputXKey: String ``` |

Modified QCCompositionInputYKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionInputYKey: NSString! ``` |
| To | ``` let QCCompositionInputYKey: String ``` |

Modified QCCompositionOutputImageKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionOutputImageKey: NSString! ``` |
| To | ``` let QCCompositionOutputImageKey: String ``` |

Modified QCCompositionOutputWebPageURLKey

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionOutputWebPageURLKey: NSString! ``` |
| To | ``` let QCCompositionOutputWebPageURLKey: String ``` |

Modified QCCompositionPickerPanelDidSelectCompositionNotification

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionPickerPanelDidSelectCompositionNotification: NSString! ``` |
| To | ``` let QCCompositionPickerPanelDidSelectCompositionNotification: String ``` |

Modified QCCompositionPickerViewDidSelectCompositionNotification

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionPickerViewDidSelectCompositionNotification: NSString! ``` |
| To | ``` let QCCompositionPickerViewDidSelectCompositionNotification: String ``` |

Modified QCCompositionProtocolGraphicAnimation

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionProtocolGraphicAnimation: NSString! ``` |
| To | ``` let QCCompositionProtocolGraphicAnimation: String ``` |

Modified QCCompositionProtocolGraphicTransition

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionProtocolGraphicTransition: NSString! ``` |
| To | ``` let QCCompositionProtocolGraphicTransition: String ``` |

Modified QCCompositionProtocolImageFilter

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionProtocolImageFilter: NSString! ``` |
| To | ``` let QCCompositionProtocolImageFilter: String ``` |

Modified QCCompositionProtocolMusicVisualizer

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionProtocolMusicVisualizer: NSString! ``` |
| To | ``` let QCCompositionProtocolMusicVisualizer: String ``` |

Modified QCCompositionProtocolRSSVisualizer

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionProtocolRSSVisualizer: NSString! ``` |
| To | ``` let QCCompositionProtocolRSSVisualizer: String ``` |

Modified QCCompositionProtocolScreenSaver

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionProtocolScreenSaver: NSString! ``` |
| To | ``` let QCCompositionProtocolScreenSaver: String ``` |

Modified QCCompositionRepositoryDidUpdateNotification

|  | Declaration |
| --- | --- |
| From | ``` let QCCompositionRepositoryDidUpdateNotification: NSString! ``` |
| To | ``` let QCCompositionRepositoryDidUpdateNotification: String ``` |

Modified QCPlugInAttributeCategoriesKey

|  | Declaration |
| --- | --- |
| From | ``` let QCPlugInAttributeCategoriesKey: NSString! ``` |
| To | ``` let QCPlugInAttributeCategoriesKey: String ``` |

Modified QCPlugInAttributeCopyrightKey

|  | Declaration |
| --- | --- |
| From | ``` let QCPlugInAttributeCopyrightKey: NSString! ``` |
| To | ``` let QCPlugInAttributeCopyrightKey: String ``` |

Modified QCPlugInAttributeDescriptionKey

|  | Declaration |
| --- | --- |
| From | ``` let QCPlugInAttributeDescriptionKey: NSString! ``` |
| To | ``` let QCPlugInAttributeDescriptionKey: String ``` |

Modified QCPlugInAttributeExamplesKey

|  | Declaration |
| --- | --- |
| From | ``` let QCPlugInAttributeExamplesKey: NSString! ``` |
| To | ``` let QCPlugInAttributeExamplesKey: String ``` |

Modified QCPlugInAttributeNameKey

|  | Declaration |
| --- | --- |
| From | ``` let QCPlugInAttributeNameKey: NSString! ``` |
| To | ``` let QCPlugInAttributeNameKey: String ``` |

Modified QCPlugInBufferReleaseCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias QCPlugInBufferReleaseCallback = CFunctionPointer<((ConstUnsafePointer<()>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias QCPlugInBufferReleaseCallback = CFunctionPointer<((UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified QCPlugInExecutionArgumentEventKey

|  | Declaration |
| --- | --- |
| From | ``` let QCPlugInExecutionArgumentEventKey: NSString! ``` |
| To | ``` let QCPlugInExecutionArgumentEventKey: String ``` |

Modified QCPlugInExecutionArgumentMouseLocationKey

|  | Declaration |
| --- | --- |
| From | ``` let QCPlugInExecutionArgumentMouseLocationKey: NSString! ``` |
| To | ``` let QCPlugInExecutionArgumentMouseLocationKey: String ``` |

Modified QCPlugInPixelFormatARGB8

|  | Declaration |
| --- | --- |
| From | ``` let QCPlugInPixelFormatARGB8: NSString! ``` |
| To | ``` let QCPlugInPixelFormatARGB8: String ``` |

Modified QCPlugInPixelFormatBGRA8

|  | Declaration |
| --- | --- |
| From | ``` let QCPlugInPixelFormatBGRA8: NSString! ``` |
| To | ``` let QCPlugInPixelFormatBGRA8: String ``` |

Modified QCPlugInPixelFormatI8

|  | Declaration |
| --- | --- |
| From | ``` let QCPlugInPixelFormatI8: NSString! ``` |
| To | ``` let QCPlugInPixelFormatI8: String ``` |

Modified QCPlugInPixelFormatIf

|  | Declaration |
| --- | --- |
| From | ``` let QCPlugInPixelFormatIf: NSString! ``` |
| To | ``` let QCPlugInPixelFormatIf: String ``` |

Modified QCPlugInPixelFormatRGBAf

|  | Declaration |
| --- | --- |
| From | ``` let QCPlugInPixelFormatRGBAf: NSString! ``` |
| To | ``` let QCPlugInPixelFormatRGBAf: String ``` |

Modified QCPlugInTextureReleaseCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias QCPlugInTextureReleaseCallback = CFunctionPointer<((CGLContextObj, GLuint, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias QCPlugInTextureReleaseCallback = CFunctionPointer<((CGLContextObj, GLuint, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified QCPortAttributeDefaultValueKey

|  | Declaration |
| --- | --- |
| From | ``` let QCPortAttributeDefaultValueKey: NSString! ``` |
| To | ``` let QCPortAttributeDefaultValueKey: String ``` |

Modified QCPortAttributeMaximumValueKey

|  | Declaration |
| --- | --- |
| From | ``` let QCPortAttributeMaximumValueKey: NSString! ``` |
| To | ``` let QCPortAttributeMaximumValueKey: String ``` |

Modified QCPortAttributeMenuItemsKey

|  | Declaration |
| --- | --- |
| From | ``` let QCPortAttributeMenuItemsKey: NSString! ``` |
| To | ``` let QCPortAttributeMenuItemsKey: String ``` |

Modified QCPortAttributeMinimumValueKey

|  | Declaration |
| --- | --- |
| From | ``` let QCPortAttributeMinimumValueKey: NSString! ``` |
| To | ``` let QCPortAttributeMinimumValueKey: String ``` |

Modified QCPortAttributeNameKey

|  | Declaration |
| --- | --- |
| From | ``` let QCPortAttributeNameKey: NSString! ``` |
| To | ``` let QCPortAttributeNameKey: String ``` |

Modified QCPortAttributeTypeKey

|  | Declaration |
| --- | --- |
| From | ``` let QCPortAttributeTypeKey: NSString! ``` |
| To | ``` let QCPortAttributeTypeKey: String ``` |

Modified QCPortTypeBoolean

|  | Declaration |
| --- | --- |
| From | ``` let QCPortTypeBoolean: NSString! ``` |
| To | ``` let QCPortTypeBoolean: String ``` |

Modified QCPortTypeColor

|  | Declaration |
| --- | --- |
| From | ``` let QCPortTypeColor: NSString! ``` |
| To | ``` let QCPortTypeColor: String ``` |

Modified QCPortTypeImage

|  | Declaration |
| --- | --- |
| From | ``` let QCPortTypeImage: NSString! ``` |
| To | ``` let QCPortTypeImage: String ``` |

Modified QCPortTypeIndex

|  | Declaration |
| --- | --- |
| From | ``` let QCPortTypeIndex: NSString! ``` |
| To | ``` let QCPortTypeIndex: String ``` |

Modified QCPortTypeNumber

|  | Declaration |
| --- | --- |
| From | ``` let QCPortTypeNumber: NSString! ``` |
| To | ``` let QCPortTypeNumber: String ``` |

Modified QCPortTypeString

|  | Declaration |
| --- | --- |
| From | ``` let QCPortTypeString: NSString! ``` |
| To | ``` let QCPortTypeString: String ``` |

Modified QCPortTypeStructure

|  | Declaration |
| --- | --- |
| From | ``` let QCPortTypeStructure: NSString! ``` |
| To | ``` let QCPortTypeStructure: String ``` |

Modified QCRendererEventKey

|  | Declaration |
| --- | --- |
| From | ``` let QCRendererEventKey: NSString! ``` |
| To | ``` let QCRendererEventKey: String ``` |

Modified QCRendererMouseLocationKey

|  | Declaration |
| --- | --- |
| From | ``` let QCRendererMouseLocationKey: NSString! ``` |
| To | ``` let QCRendererMouseLocationKey: String ``` |

Modified QCViewDidStartRenderingNotification

|  | Declaration |
| --- | --- |
| From | ``` let QCViewDidStartRenderingNotification: NSString! ``` |
| To | ``` let QCViewDidStartRenderingNotification: String ``` |

Modified QCViewDidStopRenderingNotification

|  | Declaration |
| --- | --- |
| From | ``` let QCViewDidStopRenderingNotification: NSString! ``` |
| To | ``` let QCViewDidStopRenderingNotification: String ``` |

Modified kQuartzFilterApplicationDomain

|  | Declaration |
| --- | --- |
| From | ``` var kQuartzFilterApplicationDomain: NSString! ``` |
| To | ``` let kQuartzFilterApplicationDomain: String ``` |

Modified kQuartzFilterManagerDidAddFilterNotification

|  | Declaration |
| --- | --- |
| From | ``` var kQuartzFilterManagerDidAddFilterNotification: NSString! ``` |
| To | ``` let kQuartzFilterManagerDidAddFilterNotification: String ``` |

Modified kQuartzFilterManagerDidModifyFilterNotification

|  | Declaration |
| --- | --- |
| From | ``` var kQuartzFilterManagerDidModifyFilterNotification: NSString! ``` |
| To | ``` let kQuartzFilterManagerDidModifyFilterNotification: String ``` |

Modified kQuartzFilterManagerDidRemoveFilterNotification

|  | Declaration |
| --- | --- |
| From | ``` var kQuartzFilterManagerDidRemoveFilterNotification: NSString! ``` |
| To | ``` let kQuartzFilterManagerDidRemoveFilterNotification: String ``` |

Modified kQuartzFilterManagerDidSelectFilterNotification

|  | Declaration |
| --- | --- |
| From | ``` var kQuartzFilterManagerDidSelectFilterNotification: NSString! ``` |
| To | ``` let kQuartzFilterManagerDidSelectFilterNotification: String ``` |

Modified kQuartzFilterPDFWorkflowDomain

|  | Declaration |
| --- | --- |
| From | ``` var kQuartzFilterPDFWorkflowDomain: NSString! ``` |
| To | ``` let kQuartzFilterPDFWorkflowDomain: String ``` |

Modified kQuartzFilterPrintingDomain

|  | Declaration |
| --- | --- |
| From | ``` var kQuartzFilterPrintingDomain: NSString! ``` |
| To | ``` let kQuartzFilterPrintingDomain: String ``` |

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
