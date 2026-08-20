---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/Quartz.html
archived_at: '2026-07-18T02:53:41.014264Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# Quartz Changes for Swift

### Quartz

Removed IKImageBrowserCellState.valueRemoved IKImageBrowserDropOperation.valueRemoved QCPlugInExecutionMode.valueRemoved QCPlugInTimeMode.valueAdded IKImageBrowserCellState.init(rawValue: UInt32)Added IKImageBrowserCellState.rawValueAdded IKImageBrowserDropOperation.init(rawValue: UInt32)Added IKImageBrowserDropOperation.rawValueAdded [IKPictureTaker.pictureTaker() -> IKPictureTaker! [class]](https://developer.apple.com/documentation/quartz/ikpicturetaker/1503805-picturetaker)Added QCPlugInExecutionMode.init(rawValue: UInt32)Added QCPlugInExecutionMode.rawValueAdded QCPlugInTimeMode.init(rawValue: UInt32)Added QCPlugInTimeMode.rawValueAdded [IKPictureTakerCropAreaSizeKey](https://developer.apple.com/documentation/quartz/ikpicturetakercropareasizekey)Added [IKPictureTakerShowAddressBookPicture](https://developer.apple.com/documentation/quartz/ikpicturetakershowaddressbookpicture)Added [IKPictureTakerShowEmptyPicture](https://developer.apple.com/documentation/quartz/ikpicturetakershowemptypicture)Modified [IKCameraDeviceViewDisplayMode [enum]](https://developer.apple.com/documentation/quartz/ikcameradeviceviewdisplaymode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [IKCameraDeviceViewTransferMode [enum]](https://developer.apple.com/documentation/quartz/ikcameradeviceviewtransfermode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [IKDeviceBrowserViewDisplayMode [enum]](https://developer.apple.com/documentation/quartz/ikdevicebrowserviewdisplaymode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [IKFilterCustomUIProvider.provideViewForUIConfiguration(_: [NSObject : AnyObject]!, excludedKeys: [AnyObject]!) -> IKFilterUIView!](https://developer.apple.com/documentation/quartz/ikfiltercustomuiprovider/1427525-provideviewforuiconfiguration)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified [IKImageBrowserCellState [struct]](https://developer.apple.com/documentation/quartz/ikimagebrowsercellstate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct IKImageBrowserCellState {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct IKImageBrowserCellState : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [IKImageBrowserDropOperation [struct]](https://developer.apple.com/documentation/quartz/ikimagebrowserdropoperation)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct IKImageBrowserDropOperation {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct IKImageBrowserDropOperation : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [IKImageBrowserView](https://developer.apple.com/documentation/quartz/ikimagebrowserview)

|  | Declaration |
| --- | --- |
| From | ``` class IKImageBrowserView : NSView, NSDraggingSource, NSObjectProtocol { } extension IKImageBrowserView {     init!(frame frame: NSRect)     func setDataSource(_ source: AnyObject!)     func dataSource() -> AnyObject!     func reloadData()     func setDelegate(_ aDelegate: AnyObject!)     func delegate() -> AnyObject! } extension IKImageBrowserView {     func setCellsStyleMask(_ mask: Int)     func cellsStyleMask() -> Int     func setConstrainsToOriginalSize(_ flag: Bool)     func constrainsToOriginalSize() -> Bool     func setBackgroundLayer(_ aLayer: CALayer!)     func backgroundLayer() -> CALayer!     func setForegroundLayer(_ aLayer: CALayer!)     func foregroundLayer() -> CALayer!     func newCellForRepresentedItem(_ anItem: AnyObject!) -> IKImageBrowserCell!     func cellForItemAtIndex(_ index: Int) -> IKImageBrowserCell! } extension IKImageBrowserView {     func setZoomValue(_ aValue: Float)     func zoomValue() -> Float     func setContentResizingMask(_ mask: Int)     func contentResizingMask() -> Int     func scrollIndexToVisible(_ index: Int)     func setCellSize(_ size: NSSize)     func cellSize() -> NSSize     func intercellSpacing() -> NSSize     func setIntercellSpacing(_ aSize: NSSize)     func indexOfItemAtPoint(_ point: NSPoint) -> Int     func itemFrameAtIndex(_ index: Int) -> NSRect     func visibleItemIndexes() -> NSIndexSet!     func rowIndexesInRect(_ rect: NSRect) -> NSIndexSet!     func columnIndexesInRect(_ rect: NSRect) -> NSIndexSet!     func rectOfColumn(_ columnIndex: Int) -> NSRect     func rectOfRow(_ rowIndex: Int) -> NSRect     func numberOfRows() -> Int     func numberOfColumns() -> Int     func setCanControlQuickLookPanel(_ flag: Bool)     func canControlQuickLookPanel() -> Bool } extension IKImageBrowserView {     func selectionIndexes() -> NSIndexSet!     func setSelectionIndexes(_ indexes: NSIndexSet!, byExtendingSelection extendSelection: Bool)     func setAllowsMultipleSelection(_ flag: Bool)     func allowsMultipleSelection() -> Bool     func setAllowsEmptySelection(_ flag: Bool)     func allowsEmptySelection() -> Bool     func setAllowsReordering(_ flag: Bool)     func allowsReordering() -> Bool     func setAnimates(_ flag: Bool)     func animates() -> Bool     func expandGroupAtIndex(_ index: Int)     func collapseGroupAtIndex(_ index: Int)     func isGroupExpandedAtIndex(_ index: Int) -> Bool } extension IKImageBrowserView {     func setDraggingDestinationDelegate(_ delegate: AnyObject!)     func draggingDestinationDelegate() -> AnyObject!     func indexAtLocationOfDroppedItem() -> Int     func dropOperation() -> IKImageBrowserDropOperation     func setAllowsDroppingOnItems(_ flag: Bool)     func allowsDroppingOnItems() -> Bool     func setDropIndex(_ index: Int, dropOperation operation: IKImageBrowserDropOperation) } ``` |
| To | ``` class IKImageBrowserView : NSView, NSDraggingSource { } extension IKImageBrowserView {     init!(frame frame: NSRect)     func setDataSource(_ source: AnyObject!)     func dataSource() -> AnyObject!     func reloadData()     func setDelegate(_ aDelegate: AnyObject!)     func delegate() -> AnyObject! } extension IKImageBrowserView {     func setCellsStyleMask(_ mask: Int)     func cellsStyleMask() -> Int     func setConstrainsToOriginalSize(_ flag: Bool)     func constrainsToOriginalSize() -> Bool     func setBackgroundLayer(_ aLayer: CALayer!)     func backgroundLayer() -> CALayer!     func setForegroundLayer(_ aLayer: CALayer!)     func foregroundLayer() -> CALayer!     func newCellForRepresentedItem(_ anItem: AnyObject!) -> IKImageBrowserCell!     func cellForItemAtIndex(_ index: Int) -> IKImageBrowserCell! } extension IKImageBrowserView {     func setZoomValue(_ aValue: Float)     func zoomValue() -> Float     func setContentResizingMask(_ mask: Int)     func contentResizingMask() -> Int     func scrollIndexToVisible(_ index: Int)     func setCellSize(_ size: NSSize)     func cellSize() -> NSSize     func intercellSpacing() -> NSSize     func setIntercellSpacing(_ aSize: NSSize)     func indexOfItemAtPoint(_ point: NSPoint) -> Int     func itemFrameAtIndex(_ index: Int) -> NSRect     func visibleItemIndexes() -> NSIndexSet!     func rowIndexesInRect(_ rect: NSRect) -> NSIndexSet!     func columnIndexesInRect(_ rect: NSRect) -> NSIndexSet!     func rectOfColumn(_ columnIndex: Int) -> NSRect     func rectOfRow(_ rowIndex: Int) -> NSRect     func numberOfRows() -> Int     func numberOfColumns() -> Int     func setCanControlQuickLookPanel(_ flag: Bool)     func canControlQuickLookPanel() -> Bool } extension IKImageBrowserView {     func selectionIndexes() -> NSIndexSet!     func setSelectionIndexes(_ indexes: NSIndexSet!, byExtendingSelection extendSelection: Bool)     func setAllowsMultipleSelection(_ flag: Bool)     func allowsMultipleSelection() -> Bool     func setAllowsEmptySelection(_ flag: Bool)     func allowsEmptySelection() -> Bool     func setAllowsReordering(_ flag: Bool)     func allowsReordering() -> Bool     func setAnimates(_ flag: Bool)     func animates() -> Bool     func expandGroupAtIndex(_ index: Int)     func collapseGroupAtIndex(_ index: Int)     func isGroupExpandedAtIndex(_ index: Int) -> Bool } extension IKImageBrowserView {     func setDraggingDestinationDelegate(_ delegate: AnyObject!)     func draggingDestinationDelegate() -> AnyObject!     func indexAtLocationOfDroppedItem() -> Int     func dropOperation() -> IKImageBrowserDropOperation     func setAllowsDroppingOnItems(_ flag: Bool)     func allowsDroppingOnItems() -> Bool     func setDropIndex(_ index: Int, dropOperation operation: IKImageBrowserDropOperation) } ``` |

Modified [IKImageEditPanelDataSource.imageProperties() -> [NSObject : AnyObject]!](https://developer.apple.com/documentation/quartz/ikimageeditpaneldatasource/1504167-imageproperties)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified [IKImageEditPanelDataSource.setImage(_: CGImage!, imageProperties: [NSObject : AnyObject]!)](https://developer.apple.com/documentation/quartz/ikimageeditpaneldatasource/1503517-setimage)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified [IKPictureTaker](https://developer.apple.com/documentation/quartz/ikpicturetaker)

|  | Declaration |
| --- | --- |
| From | ``` class IKPictureTaker : NSPanel {     init!() -> IKPictureTaker     class func pictureTaker() -> IKPictureTaker!     func runModal() -> Int     func beginPictureTakerWithDelegate(_ delegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func beginPictureTakerSheetForWindow(_ aWindow: NSWindow!, withDelegate delegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func popUpRecentsMenuForView(_ aView: NSView!, withDelegate delegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func setInputImage(_ image: NSImage!)     func inputImage() -> NSImage!     func outputImage() -> NSImage!     func setMirroring(_ b: Bool)     func mirroring() -> Bool } ``` |
| To | ``` class IKPictureTaker : NSPanel {     class func pictureTaker() -> IKPictureTaker!     func runModal() -> Int     func beginPictureTakerWithDelegate(_ delegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func beginPictureTakerSheetForWindow(_ aWindow: NSWindow!, withDelegate delegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func popUpRecentsMenuForView(_ aView: NSView!, withDelegate delegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func setInputImage(_ image: NSImage!)     func inputImage() -> NSImage!     func outputImage() -> NSImage!     func setMirroring(_ b: Bool)     func mirroring() -> Bool } ``` |

Modified [IKScannerDeviceViewDelegate.scannerDeviceView(_: IKScannerDeviceView!, didScanToBandData: ICScannerBandData!, scanInfo: [NSObject : AnyObject]!, error: NSError!)](https://developer.apple.com/documentation/quartz/ikscannerdeviceviewdelegate/1503867-scannerdeviceview)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified [IKScannerDeviceViewDisplayMode [enum]](https://developer.apple.com/documentation/quartz/ikscannerdeviceviewdisplaymode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [IKScannerDeviceViewTransferMode [enum]](https://developer.apple.com/documentation/quartz/ikscannerdeviceviewtransfermode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [PDFActionGoTo](https://developer.apple.com/documentation/pdfkit/pdfactiongoto)

|  | Declaration |
| --- | --- |
| From | ``` class PDFActionGoTo : PDFAction, NSCopying {     init!(destination destination: PDFDestination!)     func destination() -> PDFDestination!     func setDestination(_ destination: PDFDestination!) } ``` |
| To | ``` class PDFActionGoTo : PDFAction {     init!(destination destination: PDFDestination!)     func destination() -> PDFDestination!     func setDestination(_ destination: PDFDestination!) } ``` |

Modified [PDFActionNamed](https://developer.apple.com/documentation/pdfkit/pdfactionnamed)

|  | Declaration |
| --- | --- |
| From | ``` class PDFActionNamed : PDFAction, NSCopying {     init!(name name: PDFActionNamedName)     func name() -> PDFActionNamedName     func setName(_ name: PDFActionNamedName) } ``` |
| To | ``` class PDFActionNamed : PDFAction {     init!(name name: PDFActionNamedName)     func name() -> PDFActionNamedName     func setName(_ name: PDFActionNamedName) } ``` |

Modified [PDFActionRemoteGoTo](https://developer.apple.com/documentation/quartz/pdfactionremotegoto)

|  | Declaration |
| --- | --- |
| From | ``` class PDFActionRemoteGoTo : PDFAction, NSCopying {     init!(pageIndex pageIndex: Int, atPoint point: NSPoint, fileURL url: NSURL!)     func pageIndex() -> Int     func setPageIndex(_ pageIndex: Int)     func point() -> NSPoint     func setPoint(_ point: NSPoint)     func URL() -> NSURL!     func setURL(_ url: NSURL!) } ``` |
| To | ``` class PDFActionRemoteGoTo : PDFAction {     init!(pageIndex pageIndex: Int, atPoint point: NSPoint, fileURL url: NSURL!)     func pageIndex() -> Int     func setPageIndex(_ pageIndex: Int)     func point() -> NSPoint     func setPoint(_ point: NSPoint)     func URL() -> NSURL!     func setURL(_ url: NSURL!) } ``` |

Modified [PDFActionResetForm](https://developer.apple.com/documentation/pdfkit/pdfactionresetform)

|  | Declaration |
| --- | --- |
| From | ``` class PDFActionResetForm : PDFAction, NSCopying {     init!()     func fields() -> [AnyObject]!     func setFields(_ fields: [AnyObject]!)     func fieldsIncludedAreCleared() -> Bool     func setFieldsIncludedAreCleared(_ include: Bool) } ``` |
| To | ``` class PDFActionResetForm : PDFAction {     init!()     func fields() -> [AnyObject]!     func setFields(_ fields: [AnyObject]!)     func fieldsIncludedAreCleared() -> Bool     func setFieldsIncludedAreCleared(_ include: Bool) } ``` |

Modified [PDFActionURL](https://developer.apple.com/documentation/pdfkit/pdfactionurl)

|  | Declaration |
| --- | --- |
| From | ``` class PDFActionURL : PDFAction, NSCopying {     init!(URL url: NSURL!)     func URL() -> NSURL!     func setURL(_ url: NSURL!) } ``` |
| To | ``` class PDFActionURL : PDFAction {     init!(URL url: NSURL!)     func URL() -> NSURL!     func setURL(_ url: NSURL!) } ``` |

Modified [PDFAnnotationButtonWidget](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget)

|  | Declaration |
| --- | --- |
| From | ``` class PDFAnnotationButtonWidget : PDFAnnotation, NSCopying {     func controlType() -> PDFWidgetControlType     func setControlType(_ type: PDFWidgetControlType)     func state() -> Int     func setState(_ value: Int)     func isHighlighted() -> Bool     func setHighlighted(_ flag: Bool)     func backgroundColor() -> NSColor!     func setBackgroundColor(_ color: NSColor!)     func allowsToggleToOff() -> Bool     func setAllowsToggleToOff(_ allowOff: Bool)     func font() -> NSFont!     func setFont(_ font: NSFont!)     func fontColor() -> NSColor!     func setFontColor(_ color: NSColor!)     func caption() -> String!     func setCaption(_ name: String!)     func fieldName() -> String!     func setFieldName(_ name: String!)     func onStateValue() -> String!     func setOnStateValue(_ name: String!) } ``` |
| To | ``` class PDFAnnotationButtonWidget : PDFAnnotation {     func controlType() -> PDFWidgetControlType     func setControlType(_ type: PDFWidgetControlType)     func state() -> Int     func setState(_ value: Int)     func isHighlighted() -> Bool     func setHighlighted(_ flag: Bool)     func backgroundColor() -> NSColor!     func setBackgroundColor(_ color: NSColor!)     func allowsToggleToOff() -> Bool     func setAllowsToggleToOff(_ allowOff: Bool)     func font() -> NSFont!     func setFont(_ font: NSFont!)     func fontColor() -> NSColor!     func setFontColor(_ color: NSColor!)     func caption() -> String!     func setCaption(_ name: String!)     func fieldName() -> String!     func setFieldName(_ name: String!)     func onStateValue() -> String!     func setOnStateValue(_ name: String!) } ``` |

Modified [PDFAnnotationChoiceWidget](https://developer.apple.com/documentation/quartz/pdfannotationchoicewidget)

|  | Declaration |
| --- | --- |
| From | ``` class PDFAnnotationChoiceWidget : PDFAnnotation, NSCopying {     func stringValue() -> String!     func setStringValue(_ value: String!)     func backgroundColor() -> NSColor!     func setBackgroundColor(_ color: NSColor!)     func font() -> NSFont!     func setFont(_ font: NSFont!)     func fontColor() -> NSColor!     func setFontColor(_ color: NSColor!)     func fieldName() -> String!     func setFieldName(_ name: String!)     func isListChoice() -> Bool     func setIsListChoice(_ isList: Bool)     func choices() -> [AnyObject]!     func setChoices(_ options: [AnyObject]!) } ``` |
| To | ``` class PDFAnnotationChoiceWidget : PDFAnnotation {     func stringValue() -> String!     func setStringValue(_ value: String!)     func backgroundColor() -> NSColor!     func setBackgroundColor(_ color: NSColor!)     func font() -> NSFont!     func setFont(_ font: NSFont!)     func fontColor() -> NSColor!     func setFontColor(_ color: NSColor!)     func fieldName() -> String!     func setFieldName(_ name: String!)     func isListChoice() -> Bool     func setIsListChoice(_ isList: Bool)     func choices() -> [AnyObject]!     func setChoices(_ options: [AnyObject]!) } ``` |

Modified [PDFAnnotationCircle](https://developer.apple.com/documentation/quartz/pdfannotationcircle)

|  | Declaration |
| --- | --- |
| From | ``` class PDFAnnotationCircle : PDFAnnotation, NSCopying {     func interiorColor() -> NSColor!     func setInteriorColor(_ color: NSColor!) } ``` |
| To | ``` class PDFAnnotationCircle : PDFAnnotation {     func interiorColor() -> NSColor!     func setInteriorColor(_ color: NSColor!) } ``` |

Modified [PDFAnnotationFreeText](https://developer.apple.com/documentation/quartz/pdfannotationfreetext)

|  | Declaration |
| --- | --- |
| From | ``` class PDFAnnotationFreeText : PDFAnnotation, NSCopying, NSCoding {     func font() -> NSFont!     func setFont(_ font: NSFont!)     func fontColor() -> NSColor!     func setFontColor(_ color: NSColor!)     func alignment() -> NSTextAlignment     func setAlignment(_ alignment: NSTextAlignment) } ``` |
| To | ``` class PDFAnnotationFreeText : PDFAnnotation {     func font() -> NSFont!     func setFont(_ font: NSFont!)     func fontColor() -> NSColor!     func setFontColor(_ color: NSColor!)     func alignment() -> NSTextAlignment     func setAlignment(_ alignment: NSTextAlignment) } ``` |

Modified [PDFAnnotationInk](https://developer.apple.com/documentation/quartz/pdfannotationink)

|  | Declaration |
| --- | --- |
| From | ``` class PDFAnnotationInk : PDFAnnotation, NSCopying, NSCoding {     func paths() -> [AnyObject]!     func addBezierPath(_ path: NSBezierPath!)     func removeBezierPath(_ path: NSBezierPath!) } ``` |
| To | ``` class PDFAnnotationInk : PDFAnnotation {     func paths() -> [AnyObject]!     func addBezierPath(_ path: NSBezierPath!)     func removeBezierPath(_ path: NSBezierPath!) } ``` |

Modified [PDFAnnotationLine](https://developer.apple.com/documentation/quartz/pdfannotationline)

|  | Declaration |
| --- | --- |
| From | ``` class PDFAnnotationLine : PDFAnnotation, NSCopying, NSCoding {     func startPoint() -> NSPoint     func setStartPoint(_ point: NSPoint)     func endPoint() -> NSPoint     func setEndPoint(_ point: NSPoint)     func startLineStyle() -> PDFLineStyle     func setStartLineStyle(_ style: PDFLineStyle)     func endLineStyle() -> PDFLineStyle     func setEndLineStyle(_ style: PDFLineStyle)     func interiorColor() -> NSColor!     func setInteriorColor(_ color: NSColor!) } ``` |
| To | ``` class PDFAnnotationLine : PDFAnnotation {     func startPoint() -> NSPoint     func setStartPoint(_ point: NSPoint)     func endPoint() -> NSPoint     func setEndPoint(_ point: NSPoint)     func startLineStyle() -> PDFLineStyle     func setStartLineStyle(_ style: PDFLineStyle)     func endLineStyle() -> PDFLineStyle     func setEndLineStyle(_ style: PDFLineStyle)     func interiorColor() -> NSColor!     func setInteriorColor(_ color: NSColor!) } ``` |

Modified [PDFAnnotationLink](https://developer.apple.com/documentation/quartz/pdfannotationlink)

|  | Declaration |
| --- | --- |
| From | ``` class PDFAnnotationLink : PDFAnnotation, NSCopying {     func destination() -> PDFDestination!     func setDestination(_ destination: PDFDestination!)     func URL() -> NSURL!     func setURL(_ url: NSURL!)     func setHighlighted(_ flag: Bool) } ``` |
| To | ``` class PDFAnnotationLink : PDFAnnotation {     func destination() -> PDFDestination!     func setDestination(_ destination: PDFDestination!)     func URL() -> NSURL!     func setURL(_ url: NSURL!)     func setHighlighted(_ flag: Bool) } ``` |

Modified [PDFAnnotationMarkup](https://developer.apple.com/documentation/quartz/pdfannotationmarkup)

|  | Declaration |
| --- | --- |
| From | ``` class PDFAnnotationMarkup : PDFAnnotation, NSCopying, NSCoding {     func quadrilateralPoints() -> [AnyObject]!     func setQuadrilateralPoints(_ points: [AnyObject]!)     func markupType() -> PDFMarkupType     func setMarkupType(_ type: PDFMarkupType) } ``` |
| To | ``` class PDFAnnotationMarkup : PDFAnnotation {     func quadrilateralPoints() -> [AnyObject]!     func setQuadrilateralPoints(_ points: [AnyObject]!)     func markupType() -> PDFMarkupType     func setMarkupType(_ type: PDFMarkupType) } ``` |

Modified [PDFAnnotationPopup](https://developer.apple.com/documentation/quartz/pdfannotationpopup)

|  | Declaration |
| --- | --- |
| From | ``` class PDFAnnotationPopup : PDFAnnotation, NSCopying, NSCoding {     func isOpen() -> Bool     func setIsOpen(_ isOpen: Bool) } ``` |
| To | ``` class PDFAnnotationPopup : PDFAnnotation {     func isOpen() -> Bool     func setIsOpen(_ isOpen: Bool) } ``` |

Modified [PDFAnnotationSquare](https://developer.apple.com/documentation/quartz/pdfannotationsquare)

|  | Declaration |
| --- | --- |
| From | ``` class PDFAnnotationSquare : PDFAnnotation, NSCopying, NSCoding {     func interiorColor() -> NSColor!     func setInteriorColor(_ color: NSColor!) } ``` |
| To | ``` class PDFAnnotationSquare : PDFAnnotation {     func interiorColor() -> NSColor!     func setInteriorColor(_ color: NSColor!) } ``` |

Modified [PDFAnnotationStamp](https://developer.apple.com/documentation/quartz/pdfannotationstamp)

|  | Declaration |
| --- | --- |
| From | ``` class PDFAnnotationStamp : PDFAnnotation, NSCopying {     func name() -> String!     func setName(_ name: String!) } ``` |
| To | ``` class PDFAnnotationStamp : PDFAnnotation {     func name() -> String!     func setName(_ name: String!) } ``` |

Modified [PDFAnnotationText](https://developer.apple.com/documentation/quartz/pdfannotationtext)

|  | Declaration |
| --- | --- |
| From | ``` class PDFAnnotationText : PDFAnnotation, NSCopying, NSCoding {     func iconType() -> PDFTextAnnotationIconType     func setIconType(_ type: PDFTextAnnotationIconType) } ``` |
| To | ``` class PDFAnnotationText : PDFAnnotation {     func iconType() -> PDFTextAnnotationIconType     func setIconType(_ type: PDFTextAnnotationIconType) } ``` |

Modified [PDFAnnotationTextWidget](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget)

|  | Declaration |
| --- | --- |
| From | ``` class PDFAnnotationTextWidget : PDFAnnotation, NSCopying {     func stringValue() -> String!     func setStringValue(_ value: String!)     func attributedStringValue() -> NSAttributedString!     func setAttributedStringValue(_ value: NSAttributedString!)     func backgroundColor() -> NSColor!     func setBackgroundColor(_ color: NSColor!)     func rotation() -> Int32     func setRotation(_ rotation: Int32)     func font() -> NSFont!     func setFont(_ font: NSFont!)     func fontColor() -> NSColor!     func setFontColor(_ color: NSColor!)     func alignment() -> NSTextAlignment     func setAlignment(_ alignment: NSTextAlignment)     func maximumLength() -> Int     func setMaximumLength(_ maxLen: Int)     func fieldName() -> String!     func setFieldName(_ name: String!)     func isMultiline() -> Bool     func setIsMultiline(_ multiline: Bool) } ``` |
| To | ``` class PDFAnnotationTextWidget : PDFAnnotation {     func stringValue() -> String!     func setStringValue(_ value: String!)     func attributedStringValue() -> NSAttributedString!     func setAttributedStringValue(_ value: NSAttributedString!)     func backgroundColor() -> NSColor!     func setBackgroundColor(_ color: NSColor!)     func rotation() -> Int32     func setRotation(_ rotation: Int32)     func font() -> NSFont!     func setFont(_ font: NSFont!)     func fontColor() -> NSColor!     func setFontColor(_ color: NSColor!)     func alignment() -> NSTextAlignment     func setAlignment(_ alignment: NSTextAlignment)     func maximumLength() -> Int     func setMaximumLength(_ maxLen: Int)     func fieldName() -> String!     func setFieldName(_ name: String!)     func isMultiline() -> Bool     func setIsMultiline(_ multiline: Bool) } ``` |

Modified [PDFThumbnailView](https://developer.apple.com/documentation/quartz/pdfthumbnailview)

|  | Declaration |
| --- | --- |
| From | ``` class PDFThumbnailView : NSView, NSCoding {     func setPDFView(_ view: PDFView!)     func PDFView() -> PDFView!     func setThumbnailSize(_ size: NSSize)     func thumbnailSize() -> NSSize     func setMaximumNumberOfColumns(_ maxColumns: Int)     func maximumNumberOfColumns() -> Int     func setLabelFont(_ font: NSFont!)     func labelFont() -> NSFont!     func setBackgroundColor(_ color: NSColor!)     func backgroundColor() -> NSColor!     func setAllowsDragging(_ allow: Bool)     func allowsDragging() -> Bool     func setAllowsMultipleSelection(_ flag: Bool)     func allowsMultipleSelection() -> Bool     func selectedPages() -> [AnyObject]! } ``` |
| To | ``` class PDFThumbnailView : NSView {     func setPDFView(_ view: PDFView!)     func PDFView() -> PDFView!     func setThumbnailSize(_ size: NSSize)     func thumbnailSize() -> NSSize     func setMaximumNumberOfColumns(_ maxColumns: Int)     func maximumNumberOfColumns() -> Int     func setLabelFont(_ font: NSFont!)     func labelFont() -> NSFont!     func setBackgroundColor(_ color: NSColor!)     func backgroundColor() -> NSColor!     func setAllowsDragging(_ allow: Bool)     func allowsDragging() -> Bool     func setAllowsMultipleSelection(_ flag: Bool)     func allowsMultipleSelection() -> Bool     func selectedPages() -> [AnyObject]! } ``` |

Modified [PDFView](https://developer.apple.com/documentation/pdfkit/pdfview)

|  | Declaration |
| --- | --- |
| From | ``` class PDFView : NSView, NSAnimationDelegate, NSObjectProtocol, NSMenuDelegate {     func document() -> PDFDocument!     func setDocument(_ document: PDFDocument!)     func canGoToFirstPage() -> Bool     @IBAction func goToFirstPage(_ sender: AnyObject!)     func canGoToLastPage() -> Bool     @IBAction func goToLastPage(_ sender: AnyObject!)     func canGoToNextPage() -> Bool     @IBAction func goToNextPage(_ sender: AnyObject!)     func canGoToPreviousPage() -> Bool     @IBAction func goToPreviousPage(_ sender: AnyObject!)     func canGoBack() -> Bool     @IBAction func goBack(_ sender: AnyObject!)     func canGoForward() -> Bool     @IBAction func goForward(_ sender: AnyObject!)     func currentPage() -> PDFPage!     func goToPage(_ page: PDFPage!)     func currentDestination() -> PDFDestination!     func goToDestination(_ destination: PDFDestination!)     func goToSelection(_ selection: PDFSelection!)     func goToRect(_ rect: NSRect, onPage page: PDFPage!)     func setDisplayMode(_ mode: PDFDisplayMode)     func displayMode() -> PDFDisplayMode     func setDisplaysPageBreaks(_ breaks: Bool)     func displaysPageBreaks() -> Bool     func setDisplayBox(_ box: PDFDisplayBox)     func displayBox() -> PDFDisplayBox     func setDisplaysAsBook(_ asBook: Bool)     func displaysAsBook() -> Bool     func setShouldAntiAlias(_ aliasing: Bool)     func shouldAntiAlias() -> Bool     func setGreekingThreshold(_ threshold: CGFloat)     func greekingThreshold() -> CGFloat     @IBAction func takeBackgroundColorFrom(_ sender: AnyObject!)     func setBackgroundColor(_ newColor: NSColor!)     func backgroundColor() -> NSColor!     func setInterpolationQuality(_ quality: PDFInterpolationQuality)     func interpolationQuality() -> PDFInterpolationQuality     func setDelegate(_ anObject: AnyObject!)     func delegate() -> AnyObject!     func setScaleFactor(_ scale: CGFloat)     func scaleFactor() -> CGFloat     @IBAction func zoomIn(_ sender: AnyObject!)     func canZoomIn() -> Bool     @IBAction func zoomOut(_ sender: AnyObject!)     func canZoomOut() -> Bool     func setAutoScales(_ newAuto: Bool)     func autoScales() -> Bool     func areaOfInterestForMouse(_ event: NSEvent!) -> PDFAreaOfInterest     func areaOfInterestForPoint(_ cursorLocation: NSPoint) -> PDFAreaOfInterest     func setCursorForAreaOfInterest(_ area: PDFAreaOfInterest)     func performAction(_ action: PDFAction!)     func currentSelection() -> PDFSelection!     func setCurrentSelection(_ selection: PDFSelection!)     func setCurrentSelection(_ selection: PDFSelection!, animate animate: Bool)     func clearSelection()     @IBAction func selectAll(_ sender: AnyObject!)     func scrollSelectionToVisible(_ sender: AnyObject!)     func setHighlightedSelections(_ selections: [AnyObject]!)     func highlightedSelections() -> [AnyObject]!     func takePasswordFrom(_ sender: AnyObject!)     func drawPage(_ page: PDFPage!)     func drawPagePost(_ page: PDFPage!)     func copy(_ sender: AnyObject!)     func printWithInfo(_ printInfo: NSPrintInfo!, autoRotate doRotate: Bool)     func printWithInfo(_ printInfo: NSPrintInfo!, autoRotate doRotate: Bool, pageScaling scale: PDFPrintScalingMode)     func pageForPoint(_ point: NSPoint, nearest nearest: Bool) -> PDFPage!     func convertPoint(_ point: NSPoint, toPage page: PDFPage!) -> NSPoint     func convertRect(_ rect: NSRect, toPage page: PDFPage!) -> NSRect     func convertPoint(_ point: NSPoint, fromPage page: PDFPage!) -> NSPoint     func convertRect(_ rect: NSRect, fromPage page: PDFPage!) -> NSRect     func documentView() -> NSView!     func layoutDocumentView()     func annotationsChangedOnPage(_ page: PDFPage!)     func rowSizeForPage(_ page: PDFPage!) -> NSSize     func setAllowsDragging(_ allow: Bool)     func allowsDragging() -> Bool     func visiblePages() -> [AnyObject]!     func setEnableDataDetectors(_ enable: Bool)     func enableDataDetectors() -> Bool } ``` |
| To | ``` class PDFView : NSView, NSAnimationDelegate, NSMenuDelegate {     func document() -> PDFDocument!     func setDocument(_ document: PDFDocument!)     func canGoToFirstPage() -> Bool     @IBAction func goToFirstPage(_ sender: AnyObject!)     func canGoToLastPage() -> Bool     @IBAction func goToLastPage(_ sender: AnyObject!)     func canGoToNextPage() -> Bool     @IBAction func goToNextPage(_ sender: AnyObject!)     func canGoToPreviousPage() -> Bool     @IBAction func goToPreviousPage(_ sender: AnyObject!)     func canGoBack() -> Bool     @IBAction func goBack(_ sender: AnyObject!)     func canGoForward() -> Bool     @IBAction func goForward(_ sender: AnyObject!)     func currentPage() -> PDFPage!     func goToPage(_ page: PDFPage!)     func currentDestination() -> PDFDestination!     func goToDestination(_ destination: PDFDestination!)     func goToSelection(_ selection: PDFSelection!)     func goToRect(_ rect: NSRect, onPage page: PDFPage!)     func setDisplayMode(_ mode: PDFDisplayMode)     func displayMode() -> PDFDisplayMode     func setDisplaysPageBreaks(_ breaks: Bool)     func displaysPageBreaks() -> Bool     func setDisplayBox(_ box: PDFDisplayBox)     func displayBox() -> PDFDisplayBox     func setDisplaysAsBook(_ asBook: Bool)     func displaysAsBook() -> Bool     func setShouldAntiAlias(_ aliasing: Bool)     func shouldAntiAlias() -> Bool     func setGreekingThreshold(_ threshold: CGFloat)     func greekingThreshold() -> CGFloat     @IBAction func takeBackgroundColorFrom(_ sender: AnyObject!)     func setBackgroundColor(_ newColor: NSColor!)     func backgroundColor() -> NSColor!     func setInterpolationQuality(_ quality: PDFInterpolationQuality)     func interpolationQuality() -> PDFInterpolationQuality     func setDelegate(_ anObject: AnyObject!)     func delegate() -> AnyObject!     func setScaleFactor(_ scale: CGFloat)     func scaleFactor() -> CGFloat     @IBAction func zoomIn(_ sender: AnyObject!)     func canZoomIn() -> Bool     @IBAction func zoomOut(_ sender: AnyObject!)     func canZoomOut() -> Bool     func setAutoScales(_ newAuto: Bool)     func autoScales() -> Bool     func areaOfInterestForMouse(_ event: NSEvent!) -> PDFAreaOfInterest     func areaOfInterestForPoint(_ cursorLocation: NSPoint) -> PDFAreaOfInterest     func setCursorForAreaOfInterest(_ area: PDFAreaOfInterest)     func performAction(_ action: PDFAction!)     func currentSelection() -> PDFSelection!     func setCurrentSelection(_ selection: PDFSelection!)     func setCurrentSelection(_ selection: PDFSelection!, animate animate: Bool)     func clearSelection()     @IBAction func selectAll(_ sender: AnyObject!)     func scrollSelectionToVisible(_ sender: AnyObject!)     func setHighlightedSelections(_ selections: [AnyObject]!)     func highlightedSelections() -> [AnyObject]!     func takePasswordFrom(_ sender: AnyObject!)     func drawPage(_ page: PDFPage!)     func drawPagePost(_ page: PDFPage!)     func copy(_ sender: AnyObject!)     func printWithInfo(_ printInfo: NSPrintInfo!, autoRotate doRotate: Bool)     func printWithInfo(_ printInfo: NSPrintInfo!, autoRotate doRotate: Bool, pageScaling scale: PDFPrintScalingMode)     func pageForPoint(_ point: NSPoint, nearest nearest: Bool) -> PDFPage!     func convertPoint(_ point: NSPoint, toPage page: PDFPage!) -> NSPoint     func convertRect(_ rect: NSRect, toPage page: PDFPage!) -> NSRect     func convertPoint(_ point: NSPoint, fromPage page: PDFPage!) -> NSPoint     func convertRect(_ rect: NSRect, fromPage page: PDFPage!) -> NSRect     func documentView() -> NSView!     func layoutDocumentView()     func annotationsChangedOnPage(_ page: PDFPage!)     func rowSizeForPage(_ page: PDFPage!) -> NSSize     func setAllowsDragging(_ allow: Bool)     func allowsDragging() -> Bool     func visiblePages() -> [AnyObject]!     func setEnableDataDetectors(_ enable: Bool)     func enableDataDetectors() -> Bool } ``` |

Modified [QCComposition](https://developer.apple.com/documentation/quartz/qccomposition)

|  | Declaration |
| --- | --- |
| From | ``` class QCComposition : NSObject, NSCopying {     init!(file path: String!) -> QCComposition     class func compositionWithFile(_ path: String!) -> QCComposition!     init!(data data: NSData!) -> QCComposition     class func compositionWithData(_ data: NSData!) -> QCComposition!     func protocols() -> [AnyObject]!     func attributes() -> [NSObject : AnyObject]!     func inputKeys() -> [AnyObject]!     func outputKeys() -> [AnyObject]! } extension QCComposition {     func identifier() -> String! } ``` |
| To | ``` class QCComposition : NSObject, NSCopying {      init!(file path: String!)     class func compositionWithFile(_ path: String!) -> QCComposition!      init!(data data: NSData!)     class func compositionWithData(_ data: NSData!) -> QCComposition!     func protocols() -> [AnyObject]!     func attributes() -> [NSObject : AnyObject]!     func inputKeys() -> [AnyObject]!     func outputKeys() -> [AnyObject]! } extension QCComposition {     func identifier() -> String! } ``` |

Modified [QCComposition.init(data: NSData!)](https://developer.apple.com/documentation/quartz/qccomposition/1504831-compositionwithdata)

|  | Declaration |
| --- | --- |
| From | ``` init!(data data: NSData!) -> QCComposition ``` |
| To | ``` init!(data data: NSData!) ``` |

Modified [QCComposition.init(file: String!)](https://developer.apple.com/documentation/quartz/qccomposition/1503768-compositionwithfile)

|  | Declaration |
| --- | --- |
| From | ``` init!(file path: String!) -> QCComposition ``` |
| To | ``` init!(file path: String!) ``` |

Modified [QCCompositionLayer](https://developer.apple.com/documentation/quartz/qccompositionlayer)

|  | Declaration |
| --- | --- |
| From | ``` class QCCompositionLayer : CAOpenGLLayer, QCCompositionRenderer {     init!(file path: String!) -> QCCompositionLayer     class func compositionLayerWithFile(_ path: String!) -> QCCompositionLayer!     init!(composition composition: QCComposition!) -> QCCompositionLayer     class func compositionLayerWithComposition(_ composition: QCComposition!) -> QCCompositionLayer!     init!(file path: String!)     init!(composition composition: QCComposition!)     func composition() -> QCComposition! } ``` |
| To | ``` class QCCompositionLayer : CAOpenGLLayer, QCCompositionRenderer {      init!(file path: String!)     class func compositionLayerWithFile(_ path: String!) -> QCCompositionLayer!      init!(composition composition: QCComposition!)     class func compositionLayerWithComposition(_ composition: QCComposition!) -> QCCompositionLayer!     init!(file path: String!)     init!(composition composition: QCComposition!)     func composition() -> QCComposition! } ``` |

Modified [QCCompositionRenderer.attributes() -> [NSObject : AnyObject]!](https://developer.apple.com/documentation/quartz/qccompositionrenderer/1503829-attributes)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified [QCPlugInContext](https://developer.apple.com/documentation/quartz/qcplugincontext)

|  | Declaration |
| --- | --- |
| From | ``` protocol QCPlugInContext {     func compositionURL() -> NSURL!     func userInfo() -> NSMutableDictionary!     func colorSpace() -> Unmanaged<CGColorSpace>!     func bounds() -> NSRect     func CGLContextObj() -> CGLContextObj     func outputImageProviderFromBufferWithPixelFormat(_ format: String!, pixelsWide width: Int, pixelsHigh height: Int, baseAddress baseAddress: UnsafePointer<Void>, bytesPerRow rowBytes: Int, releaseCallback callback: QCPlugInBufferReleaseCallback, releaseContext context: UnsafeMutablePointer<Void>, colorSpace colorSpace: CGColorSpace!, shouldColorMatch colorMatch: Bool) -> AnyObject!     func outputImageProviderFromTextureWithPixelFormat(_ format: String!, pixelsWide width: Int, pixelsHigh height: Int, name name: GLuint, flipped flipped: Bool, releaseCallback callback: QCPlugInTextureReleaseCallback, releaseContext context: UnsafeMutablePointer<Void>, colorSpace colorSpace: CGColorSpace!, shouldColorMatch colorMatch: Bool) -> AnyObject! } ``` |
| To | ``` protocol QCPlugInContext {     func compositionURL() -> NSURL!     func userInfo() -> NSMutableDictionary!     func colorSpace() -> Unmanaged<CGColorSpace>!     func bounds() -> NSRect     func CGLContextObj() -> CGLContextObj     func outputImageProviderFromBufferWithPixelFormat(_ format: String!, pixelsWide width: Int, pixelsHigh height: Int, baseAddress baseAddress: UnsafePointer<Void>, bytesPerRow rowBytes: Int, releaseCallback callback: QCPlugInBufferReleaseCallback!, releaseContext context: UnsafeMutablePointer<Void>, colorSpace colorSpace: CGColorSpace!, shouldColorMatch colorMatch: Bool) -> AnyObject!     func outputImageProviderFromTextureWithPixelFormat(_ format: String!, pixelsWide width: Int, pixelsHigh height: Int, name name: GLuint, flipped flipped: Bool, releaseCallback callback: QCPlugInTextureReleaseCallback!, releaseContext context: UnsafeMutablePointer<Void>, colorSpace colorSpace: CGColorSpace!, shouldColorMatch colorMatch: Bool) -> AnyObject! } ``` |

Modified [QCPlugInContext.outputImageProviderFromBufferWithPixelFormat(_: String!, pixelsWide: Int, pixelsHigh: Int, baseAddress: UnsafePointer<Void>, bytesPerRow: Int, releaseCallback: QCPlugInBufferReleaseCallback!, releaseContext: UnsafeMutablePointer<Void>, colorSpace: CGColorSpace!, shouldColorMatch: Bool) -> AnyObject!](https://developer.apple.com/documentation/quartz/qcplugincontext/1488754-outputimageproviderfrombufferwit)

|  | Declaration |
| --- | --- |
| From | ``` func outputImageProviderFromBufferWithPixelFormat(_ format: String!, pixelsWide width: Int, pixelsHigh height: Int, baseAddress baseAddress: UnsafePointer<Void>, bytesPerRow rowBytes: Int, releaseCallback callback: QCPlugInBufferReleaseCallback, releaseContext context: UnsafeMutablePointer<Void>, colorSpace colorSpace: CGColorSpace!, shouldColorMatch colorMatch: Bool) -> AnyObject! ``` |
| To | ``` func outputImageProviderFromBufferWithPixelFormat(_ format: String!, pixelsWide width: Int, pixelsHigh height: Int, baseAddress baseAddress: UnsafePointer<Void>, bytesPerRow rowBytes: Int, releaseCallback callback: QCPlugInBufferReleaseCallback!, releaseContext context: UnsafeMutablePointer<Void>, colorSpace colorSpace: CGColorSpace!, shouldColorMatch colorMatch: Bool) -> AnyObject! ``` |

Modified [QCPlugInContext.outputImageProviderFromTextureWithPixelFormat(_: String!, pixelsWide: Int, pixelsHigh: Int, name: GLuint, flipped: Bool, releaseCallback: QCPlugInTextureReleaseCallback!, releaseContext: UnsafeMutablePointer<Void>, colorSpace: CGColorSpace!, shouldColorMatch: Bool) -> AnyObject!](https://developer.apple.com/documentation/quartz/qcplugincontext/1488756-outputimageproviderfromtexture)

|  | Declaration |
| --- | --- |
| From | ``` func outputImageProviderFromTextureWithPixelFormat(_ format: String!, pixelsWide width: Int, pixelsHigh height: Int, name name: GLuint, flipped flipped: Bool, releaseCallback callback: QCPlugInTextureReleaseCallback, releaseContext context: UnsafeMutablePointer<Void>, colorSpace colorSpace: CGColorSpace!, shouldColorMatch colorMatch: Bool) -> AnyObject! ``` |
| To | ``` func outputImageProviderFromTextureWithPixelFormat(_ format: String!, pixelsWide width: Int, pixelsHigh height: Int, name name: GLuint, flipped flipped: Bool, releaseCallback callback: QCPlugInTextureReleaseCallback!, releaseContext context: UnsafeMutablePointer<Void>, colorSpace colorSpace: CGColorSpace!, shouldColorMatch colorMatch: Bool) -> AnyObject! ``` |

Modified [QCPlugInExecutionMode [struct]](https://developer.apple.com/documentation/quartz/qcpluginexecutionmode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct QCPlugInExecutionMode {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct QCPlugInExecutionMode : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [QCPlugInTimeMode [struct]](https://developer.apple.com/documentation/quartz/qcplugintimemode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct QCPlugInTimeMode {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct QCPlugInTimeMode : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [QLPreviewPanel](https://developer.apple.com/documentation/quartz/qlpreviewpanel)

|  | Declaration |
| --- | --- |
| From | ``` class QLPreviewPanel : NSPanel {     class func sharedPreviewPanel() -> QLPreviewPanel!     class func sharedPreviewPanelExists() -> Bool     var currentController: AnyObject! { get }     func updateController()     unowned(unsafe) var dataSource: QLPreviewPanelDataSource!     func reloadData()     func refreshCurrentPreviewItem()     var currentPreviewItemIndex: Int     var currentPreviewItem: QLPreviewItem! { get }     var displayState: AnyObject!     unowned(unsafe) var delegate: QLPreviewPanelDelegate!     func enterFullScreenMode(_ screen: NSScreen!, withOptions options: [NSObject : AnyObject]!) -> Bool     func exitFullScreenModeWithOptions(_ options: [NSObject : AnyObject]!)     var inFullScreenMode: Bool { get } } ``` |
| To | ``` class QLPreviewPanel : NSPanel {     class func sharedPreviewPanel() -> QLPreviewPanel!     class func sharedPreviewPanelExists() -> Bool     var currentController: AnyObject! { get }     func updateController()     unowned(unsafe) var dataSource: QLPreviewPanelDataSource!     func reloadData()     func refreshCurrentPreviewItem()     var currentPreviewItemIndex: Int     var currentPreviewItem: QLPreviewItem! { get }     var displayState: AnyObject!     unowned(unsafe) var delegate: AnyObject!     func enterFullScreenMode(_ screen: NSScreen!, withOptions options: [NSObject : AnyObject]!) -> Bool     func exitFullScreenModeWithOptions(_ options: [NSObject : AnyObject]!)     var inFullScreenMode: Bool { get } } ``` |

Modified [QLPreviewPanel.delegate](https://developer.apple.com/documentation/quartz/qlpreviewpanel/1504770-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: QLPreviewPanelDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: AnyObject! ``` |

Modified [QLPreviewPanelDataSource.numberOfPreviewItemsInPreviewPanel(_: QLPreviewPanel!) -> Int](https://developer.apple.com/documentation/quartz/qlpreviewpaneldatasource/1504441-numberofpreviewitemsinpreviewpan)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified [QLPreviewPanelDataSource.previewPanel(_: QLPreviewPanel!, previewItemAtIndex: Int) -> QLPreviewItem!](https://developer.apple.com/documentation/quartz/qlpreviewpaneldatasource/1504383-previewpanel)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified [QLPreviewPanelDelegate.previewPanel(_: QLPreviewPanel!, handleEvent: NSEvent!) -> Bool](https://developer.apple.com/documentation/quartz/qlpreviewpaneldelegate/1503889-previewpanel)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified [QLPreviewPanelDelegate.previewPanel(_: QLPreviewPanel!, sourceFrameOnScreenForPreviewItem: QLPreviewItem!) -> NSRect](https://developer.apple.com/documentation/quartz/qlpreviewpaneldelegate/1503423-previewpanel)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified [QLPreviewPanelDelegate.previewPanel(_: QLPreviewPanel!, transitionImageForPreviewItem: QLPreviewItem!, contentRect: UnsafeMutablePointer<NSRect>) -> AnyObject!](https://developer.apple.com/documentation/quartz/qlpreviewpaneldelegate/1505277-previewpanel)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified [QLPreviewViewStyle [enum]](https://developer.apple.com/documentation/quartz/qlpreviewviewstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [QuartzFilter](https://developer.apple.com/documentation/quartz/quartzfilter)

|  | Declaration |
| --- | --- |
| From | ``` class QuartzFilter : NSObject {     init!(URL aURL: NSURL!) -> QuartzFilter     class func quartzFilterWithURL(_ aURL: NSURL!) -> QuartzFilter!     init!(properties properties: [NSObject : AnyObject]!) -> QuartzFilter     class func quartzFilterWithProperties(_ properties: [NSObject : AnyObject]!) -> QuartzFilter!     init!(outputIntents outputIntents: [AnyObject]!) -> QuartzFilter     class func quartzFilterWithOutputIntents(_ outputIntents: [AnyObject]!) -> QuartzFilter!     func properties() -> [NSObject : AnyObject]!     func url() -> NSURL!     func localizedName() -> String!     func applyToContext(_ aContext: CGContext!) -> Bool     func removeFromContext(_ aContext: CGContext!) } ``` |
| To | ``` class QuartzFilter : NSObject {      init!(URL aURL: NSURL!)     class func quartzFilterWithURL(_ aURL: NSURL!) -> QuartzFilter!      init!(properties properties: [NSObject : AnyObject]!)     class func quartzFilterWithProperties(_ properties: [NSObject : AnyObject]!) -> QuartzFilter!      init!(outputIntents outputIntents: [AnyObject]!)     class func quartzFilterWithOutputIntents(_ outputIntents: [AnyObject]!) -> QuartzFilter!     func properties() -> [NSObject : AnyObject]!     func url() -> NSURL!     func localizedName() -> String!     func applyToContext(_ aContext: CGContext!) -> Bool     func removeFromContext(_ aContext: CGContext!) } ``` |

Modified [QuartzFilter.init(outputIntents: [AnyObject]!)](https://developer.apple.com/documentation/quartz/quartzfilter/1433675-quartzfilterwithoutputintents)

|  | Declaration |
| --- | --- |
| From | ``` init!(outputIntents outputIntents: [AnyObject]!) -> QuartzFilter ``` |
| To | ``` init!(outputIntents outputIntents: [AnyObject]!) ``` |

Modified [QuartzFilter.init(properties: [NSObject : AnyObject]!)](https://developer.apple.com/documentation/quartz/quartzfilter/1433673-quartzfilterwithproperties)

|  | Declaration |
| --- | --- |
| From | ``` init!(properties properties: [NSObject : AnyObject]!) -> QuartzFilter ``` |
| To | ``` init!(properties properties: [NSObject : AnyObject]!) ``` |

Modified [QuartzFilter.init(URL: NSURL!)](https://developer.apple.com/documentation/quartz/quartzfilter/1433671-quartzfilterwithurl)

|  | Declaration |
| --- | --- |
| From | ``` init!(URL aURL: NSURL!) -> QuartzFilter ``` |
| To | ``` init!(URL aURL: NSURL!) ``` |

Modified [QuartzFilterManager](https://developer.apple.com/documentation/quartz/quartzfiltermanager)

|  | Declaration |
| --- | --- |
| From | ``` class QuartzFilterManager : NSObject {     init!() -> QuartzFilterManager     class func filterManager() -> QuartzFilterManager!     class func filtersInDomains(_ domains: [AnyObject]!) -> [AnyObject]!     func filterPanel() -> NSPanel!     func filterView() -> QuartzFilterView!     func selectedFilter() -> QuartzFilter!     func selectFilter(_ filter: QuartzFilter!) -> Bool     func setDelegate(_ aDelegate: AnyObject!)     func delegate() -> AnyObject!     func importFilter(_ filterProperties: [NSObject : AnyObject]!) -> QuartzFilter! } ``` |
| To | ``` class QuartzFilterManager : NSObject {      init!()     class func filterManager() -> QuartzFilterManager!     class func filtersInDomains(_ domains: [AnyObject]!) -> [AnyObject]!     func filterPanel() -> NSPanel!     func filterView() -> QuartzFilterView!     func selectedFilter() -> QuartzFilter!     func selectFilter(_ filter: QuartzFilter!) -> Bool     func setDelegate(_ aDelegate: AnyObject!)     func delegate() -> AnyObject!     func importFilter(_ filterProperties: [NSObject : AnyObject]!) -> QuartzFilter! } ``` |

Modified [globalUpdateOK](https://developer.apple.com/documentation/quartz/globalupdateok)

|  | Declaration |
| --- | --- |
| From | ``` var globalUpdateOK: Boolean ``` |
| To | ``` var globalUpdateOK: DarwinBoolean ``` |

Modified [QCPlugInBufferReleaseCallback](https://developer.apple.com/documentation/quartz/qcpluginbufferreleasecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias QCPlugInBufferReleaseCallback = CFunctionPointer<((UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias QCPlugInBufferReleaseCallback = (UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [QCPlugInTextureReleaseCallback](https://developer.apple.com/documentation/quartz/qcplugintexturereleasecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias QCPlugInTextureReleaseCallback = CFunctionPointer<((CGLContextObj, GLuint, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias QCPlugInTextureReleaseCallback = (CGLContextObj, GLuint, UnsafeMutablePointer<Void>) -> Void ``` |

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
