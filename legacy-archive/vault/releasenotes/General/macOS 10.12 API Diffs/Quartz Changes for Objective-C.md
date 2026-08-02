---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/Quartz.html
archived_at: '2026-07-18T02:50:42.116275Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# Quartz Changes for Objective-C

### Quartz

#### IKCameraDeviceView.h

Modified [IKCameraDeviceView.delegate](https://developer.apple.com/documentation/quartz/ikcameradeviceview/1504315-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<IKCameraDeviceViewDelegate> delegate ``` |
| To | ``` @property(assign) IBOutlet id<IKCameraDeviceViewDelegate> delegate ``` |

#### IKDeviceBrowserView.h

Modified [IKDeviceBrowserView.delegate](https://developer.apple.com/documentation/quartz/ikdevicebrowserview/1443054-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<IKDeviceBrowserViewDelegate> delegate ``` |
| To | ``` @property(assign) IBOutlet id<IKDeviceBrowserViewDelegate> delegate ``` |

#### IKImageBrowserView.h

Removed -[IKImageBrowserView setDataSource:]Removed -[IKImageBrowserView setDelegate:]Removed -[NSObject isSelectable]Added [NSObject.selectable](https://developer.apple.com/documentation/objectivec/nsobject/2369549-isselectable)Modified [IKImageBrowserView.dataSource](https://developer.apple.com/documentation/quartz/ikimagebrowserview/1503824-datasource)

|  | Declaration |
| --- | --- |
| From | ``` - (id)dataSource ``` |
| To | ``` @property(assign) IBOutlet id dataSource ``` |

Modified [IKImageBrowserView.delegate](https://developer.apple.com/documentation/quartz/ikimagebrowserview/1503780-delegate)

|  | Declaration |
| --- | --- |
| From | ``` - (id)delegate ``` |
| To | ``` @property(assign) IBOutlet id delegate ``` |

#### IKImageView.h

Modified [IKImageView.delegate](https://developer.apple.com/documentation/quartz/ikimageview/1504032-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id delegate ``` |
| To | ``` @property(assign) IBOutlet id delegate ``` |

#### IKScannerDeviceView.h

Modified [IKScannerDeviceView.delegate](https://developer.apple.com/documentation/quartz/ikscannerdeviceview/1504170-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<IKScannerDeviceViewDelegate> delegate ``` |
| To | ``` @property(assign) IBOutlet id<IKScannerDeviceViewDelegate> delegate ``` |

#### PDFActionGoTo.h

Removed -[PDFActionGoTo setDestination:]Modified [PDFActionGoTo.destination](https://developer.apple.com/documentation/quartz/pdfactiongoto/1503411-destination)

|  | Declaration |
| --- | --- |
| From | ``` - (PDFDestination *)destination ``` |
| To | ``` @property(nonatomic, retain) PDFDestination *destination ``` |

Modified [-[PDFActionGoTo initWithDestination:]](https://developer.apple.com/documentation/pdfkit/pdfactiongoto/1504070-initwithdestination)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDestination:(PDFDestination *)destination ``` |
| To | ``` - (instancetype)initWithDestination:(PDFDestination *)destination ``` |

#### PDFActionNamed.h

Removed -[PDFActionNamed setName:]Modified [-[PDFActionNamed initWithName:]](https://developer.apple.com/documentation/quartz/pdfactionnamed/1503529-initwithname)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithName:(PDFActionNamedName)name ``` |
| To | ``` - (instancetype)initWithName:(PDFActionNamedName)name ``` |

Modified [PDFActionNamed.name](https://developer.apple.com/documentation/quartz/pdfactionnamed/1503998-name)

|  | Declaration |
| --- | --- |
| From | ``` - (PDFActionNamedName)name ``` |
| To | ``` @property(nonatomic, assign) PDFActionNamedName name ``` |

#### PDFActionRemoteGoTo.h

Removed -[PDFActionRemoteGoTo setPageIndex:]Removed -[PDFActionRemoteGoTo setPoint:]Removed -[PDFActionRemoteGoTo setURL:]Modified [-[PDFActionRemoteGoTo initWithPageIndex:atPoint:fileURL:]](https://developer.apple.com/documentation/pdfkit/pdfactionremotegoto/1504119-initwithpageindex)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithPageIndex:(NSUInteger)pageIndex atPoint:(NSPoint)point fileURL:(NSURL *)url ``` |
| To | ``` - (instancetype)initWithPageIndex:(NSUInteger)pageIndex atPoint:(NSPoint)point fileURL:(NSURL *)url ``` |

Modified [PDFActionRemoteGoTo.pageIndex](https://developer.apple.com/documentation/pdfkit/pdfactionremotegoto/1505132-pageindex)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)pageIndex ``` |
| To | ``` @property(nonatomic, assign) NSUInteger pageIndex ``` |

Modified [PDFActionRemoteGoTo.point](https://developer.apple.com/documentation/pdfkit/pdfactionremotegoto/1505324-point)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPoint)point ``` |
| To | ``` @property(nonatomic, assign) NSPoint point ``` |

Modified [PDFActionRemoteGoTo.URL](https://developer.apple.com/documentation/pdfkit/pdfactionremotegoto/1504008-url)

|  | Declaration |
| --- | --- |
| From | ``` - (NSURL *)URL ``` |
| To | ``` @property(nonatomic, retain) NSURL *URL ``` |

#### PDFActionResetForm.h

Removed -[PDFActionResetForm setFields:]Removed -[PDFActionResetForm setFieldsIncludedAreCleared:]Modified [PDFActionResetForm.fields](https://developer.apple.com/documentation/pdfkit/pdfactionresetform/1503851-fields)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)fields ``` |
| To | ``` @property(nonatomic, assign) NSArray<NSString *> *fields ``` |

Modified [PDFActionResetForm.fieldsIncludedAreCleared](https://developer.apple.com/documentation/quartz/pdfactionresetform/1504038-fieldsincludedarecleared)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)fieldsIncludedAreCleared ``` |
| To | ``` @property(nonatomic, assign) BOOL fieldsIncludedAreCleared ``` |

Modified [-[PDFActionResetForm init]](https://developer.apple.com/documentation/quartz/pdfactionresetform/1503655-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

#### PDFActionURL.h

Removed -[PDFActionURL setURL:]Modified [-[PDFActionURL initWithURL:]](https://developer.apple.com/documentation/quartz/pdfactionurl/1503840-initwithurl)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithURL:(NSURL *)url ``` |
| To | ``` - (instancetype)initWithURL:(NSURL *)url ``` |

Modified [PDFActionURL.URL](https://developer.apple.com/documentation/pdfkit/pdfactionurl/1503683-url)

|  | Declaration |
| --- | --- |
| From | ``` - (NSURL *)URL ``` |
| To | ``` @property(nonatomic, retain) NSURL *URL ``` |

#### PDFAnnotation.h

Removed -[PDFAnnotation setBorder:]Removed -[PDFAnnotation setBounds:]Removed -[PDFAnnotation setColor:]Removed -[PDFAnnotation setContents:]Removed -[PDFAnnotation setModificationDate:]Removed -[PDFAnnotation setMouseUpAction:]Removed -[PDFAnnotation setPopup:]Removed -[PDFAnnotation setShouldDisplay:]Removed -[PDFAnnotation setShouldPrint:]Removed -[PDFAnnotation setUserName:]Added [-[PDFAnnotation initWithDictionary:forPage:]](https://developer.apple.com/documentation/quartz/pdfannotation/1642241-init)Added [-[PDFAnnotation removeValueForAnnotationKey:]](https://developer.apple.com/documentation/pdfkit/pdfannotation/1642266-removevalueforannotationkey)Added [-[PDFAnnotation setBoolean:forAnnotationKey:]](https://developer.apple.com/documentation/quartz/pdfannotation/1642245-setboolean)Added [-[PDFAnnotation setRect:forAnnotationKey:]](https://developer.apple.com/documentation/pdfkit/pdfannotation/1642281-setrect)Added [-[PDFAnnotation setValue:forAnnotationKey:]](https://developer.apple.com/documentation/pdfkit/pdfannotation/1642210-setvalue)Added [-[PDFAnnotation valueForAnnotationKey:]](https://developer.apple.com/documentation/pdfkit/pdfannotation/1642234-value)Added [kPDFAnnotationKey_Action](https://developer.apple.com/documentation/quartz/kpdfannotationkey_action)Added [kPDFAnnotationKey_AdditionalActions](https://developer.apple.com/documentation/quartz/kpdfannotationkey_additionalactions)Added [kPDFAnnotationKey_AppearanceDictionary](https://developer.apple.com/documentation/quartz/kpdfannotationkey_appearancedictionary)Added [kPDFAnnotationKey_AppearanceState](https://developer.apple.com/documentation/quartz/kpdfannotationkey_appearancestate)Added kPDFAnnotationKey_AppleExtrasAdded [kPDFAnnotationKey_Border](https://developer.apple.com/documentation/quartz/kpdfannotationkey_border)Added [kPDFAnnotationKey_BorderStyle](https://developer.apple.com/documentation/quartz/kpdfannotationkey_borderstyle)Added [kPDFAnnotationKey_Color](https://developer.apple.com/documentation/quartz/kpdfannotationkey_color)Added [kPDFAnnotationKey_Contents](https://developer.apple.com/documentation/quartz/kpdfannotationkey_contents)Added [kPDFAnnotationKey_Date](https://developer.apple.com/documentation/quartz/kpdfannotationkey_date)Added [kPDFAnnotationKey_DefaultAppearance](https://developer.apple.com/documentation/quartz/kpdfannotationkey_defaultappearance)Added [kPDFAnnotationKey_Destination](https://developer.apple.com/documentation/quartz/kpdfannotationkey_destination)Added [kPDFAnnotationKey_Flags](https://developer.apple.com/documentation/quartz/kpdfannotationkey_flags)Added [kPDFAnnotationKey_HighlightingMode](https://developer.apple.com/documentation/quartz/kpdfannotationkey_highlightingmode)Added [kPDFAnnotationKey_IconName](https://developer.apple.com/documentation/quartz/kpdfannotationkey_iconname)Added [kPDFAnnotationKey_Inklist](https://developer.apple.com/documentation/quartz/kpdfannotationkey_inklist)Added [kPDFAnnotationKey_InteriorColor](https://developer.apple.com/documentation/quartz/kpdfannotationkey_interiorcolor)Added [kPDFAnnotationKey_LineEndingStyles](https://developer.apple.com/documentation/quartz/kpdfannotationkey_lineendingstyles)Added [kPDFAnnotationKey_LinePoints](https://developer.apple.com/documentation/quartz/kpdfannotationkey_linepoints)Added [kPDFAnnotationKey_Name](https://developer.apple.com/documentation/quartz/kpdfannotationkey_name)Added [kPDFAnnotationKey_Open](https://developer.apple.com/documentation/quartz/kpdfannotationkey_open)Added [kPDFAnnotationKey_Page](https://developer.apple.com/documentation/quartz/kpdfannotationkey_page)Added [kPDFAnnotationKey_Parent](https://developer.apple.com/documentation/quartz/kpdfannotationkey_parent)Added [kPDFAnnotationKey_Popup](https://developer.apple.com/documentation/quartz/kpdfannotationkey_popup)Added [kPDFAnnotationKey_Quadding](https://developer.apple.com/documentation/quartz/kpdfannotationkey_quadding)Added [kPDFAnnotationKey_QuadPoints](https://developer.apple.com/documentation/quartz/kpdfannotationkey_quadpoints)Added [kPDFAnnotationKey_Rect](https://developer.apple.com/documentation/quartz/kpdfannotationkey_rect)Added [kPDFAnnotationKey_Subtype](https://developer.apple.com/documentation/quartz/kpdfannotationkey_subtype)Added [kPDFAnnotationKey_TextLabel](https://developer.apple.com/documentation/quartz/kpdfannotationkey_textlabel)Added [kPDFAnnotationKey_WidgetAppearanceDictionary](https://developer.apple.com/documentation/quartz/kpdfannotationkey_widgetappearancedictionary)Added [kPDFAnnotationKey_WidgetDefaultValue](https://developer.apple.com/documentation/quartz/kpdfannotationkey_widgetdefaultvalue)Added [kPDFAnnotationKey_WidgetFieldFlags](https://developer.apple.com/documentation/quartz/kpdfannotationkey_widgetfieldflags)Added [kPDFAnnotationKey_WidgetFieldType](https://developer.apple.com/documentation/quartz/kpdfannotationkey_widgetfieldtype)Added [kPDFAnnotationKey_WidgetMaxLen](https://developer.apple.com/documentation/quartz/kpdfannotationkey_widgetmaxlen)Added [kPDFAnnotationKey_WidgetOptions](https://developer.apple.com/documentation/quartz/kpdfannotationkey_widgetoptions)Added [kPDFAnnotationKey_WidgetTextLabelUI](https://developer.apple.com/documentation/quartz/kpdfannotationkey_widgettextlabelui)Added [kPDFAnnotationKey_WidgetValue](https://developer.apple.com/documentation/quartz/kpdfannotationkey_widgetvalue)Modified [PDFAnnotation.border](https://developer.apple.com/documentation/pdfkit/pdfannotation/1503713-border)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (PDFBorder *)border ``` | -- |
| To | ``` @property(nonatomic, retain) PDFBorder *border ``` | OS X 10.12 |

Modified [PDFAnnotation.bounds](https://developer.apple.com/documentation/quartz/pdfannotation/1503819-bounds)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)bounds ``` |
| To | ``` @property(nonatomic, readwrite) NSRect bounds ``` |

Modified [PDFAnnotation.color](https://developer.apple.com/documentation/quartz/pdfannotation/1504152-color)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (NSColor *)color ``` | -- |
| To | ``` @property(nonatomic, retain) NSColor *color ``` | OS X 10.12 |

Modified [PDFAnnotation.contents](https://developer.apple.com/documentation/pdfkit/pdfannotation/1503720-contents)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (NSString *)contents ``` | -- |
| To | ``` @property(nonatomic, retain) NSString *contents ``` | OS X 10.12 |

Modified [-[PDFAnnotation drawWithBox:]](https://developer.apple.com/documentation/quartz/pdfannotation/1505208-drawwithbox)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [PDFAnnotation.hasAppearanceStream](https://developer.apple.com/documentation/quartz/pdfannotation/1504890-hasappearancestream)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (BOOL)hasAppearanceStream ``` | -- |
| To | ``` @property(nonatomic, readonly) BOOL hasAppearanceStream ``` | yes |

Modified [-[PDFAnnotation initWithBounds:]](https://developer.apple.com/documentation/quartz/pdfannotation/1505330-initwithbounds)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (id)initWithBounds:(NSRect)bounds ``` | -- |
| To | ``` - (instancetype)initWithBounds:(NSRect)bounds ``` | OS X 10.12 |

Modified [PDFAnnotation.modificationDate](https://developer.apple.com/documentation/pdfkit/pdfannotation/1504438-modificationdate)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (NSDate *)modificationDate ``` | -- |
| To | ``` @property(nonatomic, retain) NSDate *modificationDate ``` | OS X 10.12 |

Modified [PDFAnnotation.mouseUpAction](https://developer.apple.com/documentation/quartz/pdfannotation/1503518-mouseupaction)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (PDFAction *)mouseUpAction ``` | -- |
| To | ``` @property(nonatomic, retain) PDFAction *mouseUpAction ``` | OS X 10.12 |

Modified [PDFAnnotation.page](https://developer.apple.com/documentation/pdfkit/pdfannotation/1504512-page)

|  | Declaration |
| --- | --- |
| From | ``` - (PDFPage *)page ``` |
| To | ``` @property(nonatomic, readwrite, weak) PDFPage *page ``` |

Modified [PDFAnnotation.popup](https://developer.apple.com/documentation/pdfkit/pdfannotation/1503503-popup)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (PDFAnnotationPopup *)popup ``` | -- |
| To | ``` @property(nonatomic, retain) PDFAnnotationPopup *popup ``` | OS X 10.12 |

Modified [-[PDFAnnotation removeAllAppearanceStreams]](https://developer.apple.com/documentation/quartz/pdfannotation/1504919-removeallappearancestreams)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [PDFAnnotation.shouldDisplay](https://developer.apple.com/documentation/quartz/pdfannotation/1504561-shoulddisplay)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)shouldDisplay ``` |
| To | ``` @property(nonatomic, assign) BOOL shouldDisplay ``` |

Modified [PDFAnnotation.shouldPrint](https://developer.apple.com/documentation/quartz/pdfannotation/1504210-shouldprint)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)shouldPrint ``` |
| To | ``` @property(nonatomic, assign) BOOL shouldPrint ``` |

Modified [PDFAnnotation.toolTip](https://developer.apple.com/documentation/quartz/pdfannotation/1503660-tooltip)

|  | Declaration | Deprecation | Readonly |
| --- | --- | --- | --- |
| From | ``` - (NSString *)toolTip ``` | -- | -- |
| To | ``` @property(nonatomic, readonly) NSString *toolTip ``` | OS X 10.12 | yes |

Modified [PDFAnnotation.type](https://developer.apple.com/documentation/pdfkit/pdfannotation/1504795-type)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSString *)type ``` | -- |
| To | ``` @property(nonatomic, readonly) NSString *type ``` | yes |

Modified [PDFAnnotation.userName](https://developer.apple.com/documentation/quartz/pdfannotation/1504174-username)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (NSString *)userName ``` | -- |
| To | ``` @property(nonatomic, retain) NSString *userName ``` | OS X 10.12 |

#### PDFAnnotationButtonWidget.h

Added [kPDFWidgetMixedState](https://developer.apple.com/documentation/pdfkit/pdfwidgetcellstate/mixedstate)Added [kPDFWidgetOffState](https://developer.apple.com/documentation/pdfkit/pdfwidgetcellstate/offstate)Added [kPDFWidgetOnState](https://developer.apple.com/documentation/quartz/pdfwidgetcellstate/kpdfwidgetonstate)Added [PDFWidgetCellState](https://developer.apple.com/documentation/pdfkit/pdfwidgetcellstate)Modified [PDFAnnotationButtonWidget](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationButtonWidget allowsToggleToOff]](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget/1412974-allowstoggletooff)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationButtonWidget backgroundColor]](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget/1412935-backgroundcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationButtonWidget caption]](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget/1412942-caption)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationButtonWidget controlType]](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget/1412968-controltype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationButtonWidget fieldName]](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget/1412933-fieldname)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationButtonWidget font]](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget/1412948-font)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationButtonWidget fontColor]](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget/1412960-fontcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified -[PDFAnnotationButtonWidget isHighlighted]

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationButtonWidget onStateValue]](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget/1412956-onstatevalue)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationButtonWidget setAllowsToggleToOff:]](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget/1412944-setallowstoggletooff)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationButtonWidget setBackgroundColor:]](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget/1412972-setbackgroundcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationButtonWidget setCaption:]](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget/1412962-setcaption)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationButtonWidget setControlType:]](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget/1412943-setcontroltype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationButtonWidget setFieldName:]](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget/1412979-setfieldname)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationButtonWidget setFont:]](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget/1412950-setfont)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationButtonWidget setFontColor:]](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget/1412958-setfontcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified -[PDFAnnotationButtonWidget setHighlighted:]

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationButtonWidget setOnStateValue:]](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget/1412946-setonstatevalue)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationButtonWidget setState:]](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget/1412952-setstate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationButtonWidget state]](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget/1412954-state)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [PDFWidgetControlType](https://developer.apple.com/documentation/quartz/pdfwidgetcontroltype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### PDFAnnotationChoiceWidget.h

Modified [PDFAnnotationChoiceWidget](https://developer.apple.com/documentation/quartz/pdfannotationchoicewidget)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationChoiceWidget backgroundColor]](https://developer.apple.com/documentation/quartz/pdfannotationchoicewidget/1504369-backgroundcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationChoiceWidget choices]](https://developer.apple.com/documentation/quartz/pdfannotationchoicewidget/1504386-choices)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationChoiceWidget fieldName]](https://developer.apple.com/documentation/quartz/pdfannotationchoicewidget/1505079-fieldname)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationChoiceWidget font]](https://developer.apple.com/documentation/quartz/pdfannotationchoicewidget/1503420-font)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationChoiceWidget fontColor]](https://developer.apple.com/documentation/quartz/pdfannotationchoicewidget/1503442-fontcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationChoiceWidget isListChoice]](https://developer.apple.com/documentation/quartz/pdfannotationchoicewidget/1503588-islistchoice)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationChoiceWidget setBackgroundColor:]](https://developer.apple.com/documentation/quartz/pdfannotationchoicewidget/1504820-setbackgroundcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationChoiceWidget setChoices:]](https://developer.apple.com/documentation/quartz/pdfannotationchoicewidget/1503581-setchoices)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationChoiceWidget setFieldName:]](https://developer.apple.com/documentation/quartz/pdfannotationchoicewidget/1503844-setfieldname)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationChoiceWidget setFont:]](https://developer.apple.com/documentation/quartz/pdfannotationchoicewidget/1504806-setfont)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationChoiceWidget setFontColor:]](https://developer.apple.com/documentation/quartz/pdfannotationchoicewidget/1503731-setfontcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationChoiceWidget setIsListChoice:]](https://developer.apple.com/documentation/quartz/pdfannotationchoicewidget/1504597-setislistchoice)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationChoiceWidget setStringValue:]](https://developer.apple.com/documentation/quartz/pdfannotationchoicewidget/1504599-setstringvalue)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationChoiceWidget stringValue]](https://developer.apple.com/documentation/quartz/pdfannotationchoicewidget/1503456-stringvalue)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### PDFAnnotationCircle.h

Modified [PDFAnnotationCircle](https://developer.apple.com/documentation/quartz/pdfannotationcircle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationCircle interiorColor]](https://developer.apple.com/documentation/quartz/pdfannotationcircle/1503424-interiorcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationCircle setInteriorColor:]](https://developer.apple.com/documentation/quartz/pdfannotationcircle/1503739-setinteriorcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### PDFAnnotationFreeText.h

Modified [PDFAnnotationFreeText](https://developer.apple.com/documentation/quartz/pdfannotationfreetext)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationFreeText alignment]](https://developer.apple.com/documentation/quartz/pdfannotationfreetext/1418505-alignment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationFreeText font]](https://developer.apple.com/documentation/quartz/pdfannotationfreetext/1418507-font)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationFreeText fontColor]](https://developer.apple.com/documentation/quartz/pdfannotationfreetext/1418501-fontcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationFreeText setAlignment:]](https://developer.apple.com/documentation/quartz/pdfannotationfreetext/1418499-setalignment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationFreeText setFont:]](https://developer.apple.com/documentation/quartz/pdfannotationfreetext/1418497-setfont)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationFreeText setFontColor:]](https://developer.apple.com/documentation/quartz/pdfannotationfreetext/1418503-setfontcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### PDFAnnotationInk.h

Modified [PDFAnnotationInk](https://developer.apple.com/documentation/quartz/pdfannotationink)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationInk addBezierPath:]](https://developer.apple.com/documentation/quartz/pdfannotationink/1458496-addbezierpath)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationInk paths]](https://developer.apple.com/documentation/quartz/pdfannotationink/1458503-paths)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationInk removeBezierPath:]](https://developer.apple.com/documentation/quartz/pdfannotationink/1458498-removebezierpath)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### PDFAnnotationLine.h

Modified [PDFAnnotationLine](https://developer.apple.com/documentation/quartz/pdfannotationline)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationLine endLineStyle]](https://developer.apple.com/documentation/quartz/pdfannotationline/1462889-endlinestyle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationLine endPoint]](https://developer.apple.com/documentation/quartz/pdfannotationline/1462896-endpoint)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationLine interiorColor]](https://developer.apple.com/documentation/quartz/pdfannotationline/1462880-interiorcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationLine setEndLineStyle:]](https://developer.apple.com/documentation/quartz/pdfannotationline/1462884-setendlinestyle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationLine setEndPoint:]](https://developer.apple.com/documentation/quartz/pdfannotationline/1462892-setend)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationLine setInteriorColor:]](https://developer.apple.com/documentation/quartz/pdfannotationline/1462900-setinteriorcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationLine setStartLineStyle:]](https://developer.apple.com/documentation/quartz/pdfannotationline/1462911-setstartlinestyle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationLine setStartPoint:]](https://developer.apple.com/documentation/quartz/pdfannotationline/1462882-setstart)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationLine startLineStyle]](https://developer.apple.com/documentation/quartz/pdfannotationline/1462907-startlinestyle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationLine startPoint]](https://developer.apple.com/documentation/quartz/pdfannotationline/1462898-startpoint)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [PDFLineStyle](https://developer.apple.com/documentation/pdfkit/pdflinestyle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### PDFAnnotationLink.h

Modified [PDFAnnotationLink](https://developer.apple.com/documentation/quartz/pdfannotationlink)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationLink destination]](https://developer.apple.com/documentation/quartz/pdfannotationlink/1505091-destination)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationLink setDestination:]](https://developer.apple.com/documentation/quartz/pdfannotationlink/1503499-setdestination)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified -[PDFAnnotationLink setHighlighted:]

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationLink setURL:]](https://developer.apple.com/documentation/quartz/pdfannotationlink/1505306-seturl)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationLink URL]](https://developer.apple.com/documentation/quartz/pdfannotationlink/1505288-url)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### PDFAnnotationMarkup.h

Modified [PDFAnnotationMarkup](https://developer.apple.com/documentation/quartz/pdfannotationmarkup)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationMarkup markupType]](https://developer.apple.com/documentation/quartz/pdfannotationmarkup/1504625-markuptype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationMarkup quadrilateralPoints]](https://developer.apple.com/documentation/quartz/pdfannotationmarkup/1503614-quadrilateralpoints)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationMarkup setMarkupType:]](https://developer.apple.com/documentation/quartz/pdfannotationmarkup/1504129-setmarkuptype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationMarkup setQuadrilateralPoints:]](https://developer.apple.com/documentation/quartz/pdfannotationmarkup/1503752-setquadrilateralpoints)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [PDFMarkupType](https://developer.apple.com/documentation/quartz/pdfmarkuptype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### PDFAnnotationPopup.h

Modified [PDFAnnotationPopup](https://developer.apple.com/documentation/quartz/pdfannotationpopup)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationPopup isOpen]](https://developer.apple.com/documentation/quartz/pdfannotationpopup/1505181-isopen)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationPopup setIsOpen:]](https://developer.apple.com/documentation/quartz/pdfannotationpopup/1503539-setisopen)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### PDFAnnotationSquare.h

Modified [PDFAnnotationSquare](https://developer.apple.com/documentation/quartz/pdfannotationsquare)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationSquare interiorColor]](https://developer.apple.com/documentation/quartz/pdfannotationsquare/1478183-interiorcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationSquare setInteriorColor:]](https://developer.apple.com/documentation/quartz/pdfannotationsquare/1478180-setinteriorcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### PDFAnnotationStamp.h

Added -[PDFAnnotationStamp isSignature]Modified [PDFAnnotationStamp](https://developer.apple.com/documentation/quartz/pdfannotationstamp)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationStamp name]](https://developer.apple.com/documentation/quartz/pdfannotationstamp/1490606-name)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationStamp setName:]](https://developer.apple.com/documentation/quartz/pdfannotationstamp/1490604-setname)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### PDFAnnotationText.h

Modified [PDFAnnotationText](https://developer.apple.com/documentation/quartz/pdfannotationtext)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationText iconType]](https://developer.apple.com/documentation/quartz/pdfannotationtext/1504112-icontype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationText setIconType:]](https://developer.apple.com/documentation/quartz/pdfannotationtext/1505275-seticontype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [PDFTextAnnotationIconType](https://developer.apple.com/documentation/quartz/pdftextannotationicontype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### PDFAnnotationTextWidget.h

Modified [PDFAnnotationTextWidget](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationTextWidget alignment]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1504430-alignment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationTextWidget attributedStringValue]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1504145-attributedstringvalue)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationTextWidget backgroundColor]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1504799-backgroundcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationTextWidget fieldName]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1503749-fieldname)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationTextWidget font]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1503438-font)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationTextWidget fontColor]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1503508-fontcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationTextWidget isMultiline]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1505165-ismultiline)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationTextWidget maximumLength]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1504285-maximumlength)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationTextWidget rotation]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1504358-rotation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationTextWidget setAlignment:]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1503750-setalignment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationTextWidget setAttributedStringValue:]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1504779-setattributedstringvalue)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationTextWidget setBackgroundColor:]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1505322-setbackgroundcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationTextWidget setFieldName:]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1503658-setfieldname)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationTextWidget setFont:]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1503642-setfont)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationTextWidget setFontColor:]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1504354-setfontcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationTextWidget setIsMultiline:]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1503773-setismultiline)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationTextWidget setMaximumLength:]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1504488-setmaximumlength)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationTextWidget setRotation:]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1505202-setrotation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationTextWidget setStringValue:]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1503759-setstringvalue)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFAnnotationTextWidget stringValue]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1503429-stringvalue)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### PDFBorder.h

Removed -[PDFBorder setDashPattern:]Removed -[PDFBorder setLineWidth:]Removed -[PDFBorder setStyle:]Modified [PDFBorder.dashPattern](https://developer.apple.com/documentation/pdfkit/pdfborder/1504774-dashpattern)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)dashPattern ``` |
| To | ``` @property(nonatomic, retain) NSArray *dashPattern ``` |

Modified [PDFBorder.lineWidth](https://developer.apple.com/documentation/quartz/pdfborder/1503466-linewidth)

|  | Declaration |
| --- | --- |
| From | ``` - (CGFloat)lineWidth ``` |
| To | ``` @property(nonatomic, assign) CGFloat lineWidth ``` |

Modified [PDFBorder.style](https://developer.apple.com/documentation/quartz/pdfborder/1503719-style)

|  | Declaration |
| --- | --- |
| From | ``` - (PDFBorderStyle)style ``` |
| To | ``` @property(nonatomic, assign) PDFBorderStyle style ``` |

#### PDFDestination.h

Removed -[PDFDestination setZoom:]Modified [-[PDFDestination initWithPage:atPoint:]](https://developer.apple.com/documentation/quartz/pdfdestination/1503785-initwithpage)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithPage:(PDFPage *)page atPoint:(NSPoint)point ``` |
| To | ``` - (instancetype)initWithPage:(PDFPage *)page atPoint:(NSPoint)point ``` |

Modified [PDFDestination.page](https://developer.apple.com/documentation/quartz/pdfdestination/1503433-page)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (PDFPage *)page ``` | -- |
| To | ``` @property(nonatomic, weak, readonly) PDFPage *page ``` | yes |

Modified [PDFDestination.point](https://developer.apple.com/documentation/quartz/pdfdestination/1504218-point)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSPoint)point ``` | -- |
| To | ``` @property(nonatomic, readonly) NSPoint point ``` | yes |

Modified [PDFDestination.zoom](https://developer.apple.com/documentation/pdfkit/pdfdestination/1504094-zoom)

|  | Declaration |
| --- | --- |
| From | ``` - (CGFloat)zoom ``` |
| To | ``` @property(nonatomic, assign) CGFloat zoom ``` |

#### PDFDocument.h

Removed -[PDFDocument setDelegate:]Removed -[PDFDocument setDocumentAttributes:]Removed -[PDFDocument setOutlineRoot:]Modified -[NSObject classForAnnotationClass:]

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified -[NSObject classForPage]

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [PDFDocument.allowsCopying](https://developer.apple.com/documentation/quartz/pdfdocument/1436065-allowscopying)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (BOOL)allowsCopying ``` | -- |
| To | ``` @property(nonatomic, readonly) BOOL allowsCopying ``` | yes |

Modified [PDFDocument.allowsPrinting](https://developer.apple.com/documentation/pdfkit/pdfdocument/1436028-allowsprinting)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (BOOL)allowsPrinting ``` | -- |
| To | ``` @property(nonatomic, readonly) BOOL allowsPrinting ``` | yes |

Modified [-[PDFDocument beginFindStrings:withOptions:]](https://developer.apple.com/documentation/quartz/pdfdocument/1436096-beginfindstrings)

|  | Declaration |
| --- | --- |
| From | ``` - (void)beginFindStrings:(NSArray *)strings withOptions:(NSUInteger)options ``` |
| To | ``` - (void)beginFindStrings:(NSArray<NSString *> *)strings withOptions:(NSUInteger)options ``` |

Modified [PDFDocument.delegate](https://developer.apple.com/documentation/pdfkit/pdfdocument/1436082-delegate)

|  | Declaration |
| --- | --- |
| From | ``` - (id)delegate ``` |
| To | ``` @property(nonatomic, weak) id delegate ``` |

Modified [PDFDocument.documentAttributes](https://developer.apple.com/documentation/quartz/pdfdocument/1436054-documentattributes)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)documentAttributes ``` |
| To | ``` @property(nonatomic, retain) NSDictionary *documentAttributes ``` |

Modified [PDFDocument.documentRef](https://developer.apple.com/documentation/pdfkit/pdfdocument/1436063-documentref)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (CGPDFDocumentRef)documentRef ``` | -- |
| To | ``` @property(nonatomic, readonly) CGPDFDocumentRef documentRef ``` | yes |

Modified [PDFDocument.documentURL](https://developer.apple.com/documentation/quartz/pdfdocument/1436061-documenturl)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSURL *)documentURL ``` | -- |
| To | ``` @property(nonatomic, readonly) NSURL *documentURL ``` | yes |

Modified [-[PDFDocument findString:withOptions:]](https://developer.apple.com/documentation/pdfkit/pdfdocument/1436060-findstring)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)findString:(NSString *)string withOptions:(NSUInteger)options ``` |
| To | ``` - (NSArray<PDFSelection *> *)findString:(NSString *)string withOptions:(NSUInteger)options ``` |

Modified [-[PDFDocument initWithData:]](https://developer.apple.com/documentation/quartz/pdfdocument/1436084-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(NSData *)data ``` |
| To | ``` - (instancetype)initWithData:(NSData *)data ``` |

Modified [-[PDFDocument initWithURL:]](https://developer.apple.com/documentation/quartz/pdfdocument/1436091-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithURL:(NSURL *)url ``` |
| To | ``` - (instancetype)initWithURL:(NSURL *)url ``` |

Modified [PDFDocument.isEncrypted](https://developer.apple.com/documentation/pdfkit/pdfdocument/1436019-isencrypted)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (BOOL)isEncrypted ``` | -- |
| To | ``` @property(nonatomic, readonly) BOOL isEncrypted ``` | yes |

Modified [PDFDocument.isFinding](https://developer.apple.com/documentation/pdfkit/pdfdocument/1436066-isfinding)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (BOOL)isFinding ``` | -- |
| To | ``` @property(nonatomic, readonly) BOOL isFinding ``` | yes |

Modified [PDFDocument.isLocked](https://developer.apple.com/documentation/pdfkit/pdfdocument/1436081-islocked)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (BOOL)isLocked ``` | -- |
| To | ``` @property(nonatomic, readonly) BOOL isLocked ``` | yes |

Modified [PDFDocument.majorVersion](https://developer.apple.com/documentation/pdfkit/pdfdocument/1436034-majorversion)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (int)majorVersion ``` | -- |
| To | ``` @property(nonatomic, readonly) int majorVersion ``` | yes |

Modified [PDFDocument.minorVersion](https://developer.apple.com/documentation/pdfkit/pdfdocument/1436079-minorversion)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (int)minorVersion ``` | -- |
| To | ``` @property(nonatomic, readonly) int minorVersion ``` | yes |

Modified [PDFDocument.outlineRoot](https://developer.apple.com/documentation/quartz/pdfdocument/1436073-outlineroot)

|  | Declaration |
| --- | --- |
| From | ``` - (PDFOutline *)outlineRoot ``` |
| To | ``` @property(nonatomic, retain) PDFOutline *outlineRoot ``` |

Modified [PDFDocument.pageClass](https://developer.apple.com/documentation/pdfkit/pdfdocument/1436016-pageclass)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (Class)pageClass ``` | -- |
| To | ``` @property(nonatomic, readonly) Class pageClass ``` | yes |

Modified [PDFDocument.pageCount](https://developer.apple.com/documentation/pdfkit/pdfdocument/1436035-pagecount)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSUInteger)pageCount ``` | -- |
| To | ``` @property(nonatomic, readonly) NSUInteger pageCount ``` | yes |

Modified [PDFDocument.permissionsStatus](https://developer.apple.com/documentation/quartz/pdfdocument/1436069-permissionsstatus)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (PDFDocumentPermissions)permissionsStatus ``` | -- |
| To | ``` @property(nonatomic, readonly) PDFDocumentPermissions permissionsStatus ``` | yes |

Modified [PDFDocument.selectionForEntireDocument](https://developer.apple.com/documentation/quartz/pdfdocument/1436017-selectionforentiredocument)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (PDFSelection *)selectionForEntireDocument ``` | -- |
| To | ``` @property(nonatomic, readonly) PDFSelection *selectionForEntireDocument ``` | yes |

Modified [PDFDocument.string](https://developer.apple.com/documentation/pdfkit/pdfdocument/1436036-string)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSString *)string ``` | -- |
| To | ``` @property(nonatomic, readonly) NSString *string ``` | yes |

#### PDFKitPlatform.h (Added)

Added #def PDFEdgeInsetsAdded #def PDFKIT_AVAILABLEAdded #def PDFKIT_DEPRECATEDAdded #def PDFKIT_PLATFORM_OSXAdded #def PDFKitPlatformBezierPathAdded #def PDFKitPlatformBezierPathElementAdded #def PDFKitPlatformButtonAdded #def PDFKitPlatformButtonCellAdded #def PDFKitPlatformChoiceWidgetViewAdded #def PDFKitPlatformColorAdded #def PDFKitPlatformControlAdded #def PDFKitPlatformEventAdded #def PDFKitPlatformFontAdded #def PDFKitPlatformImageAdded #def PDFKitPlatformImageViewAdded #def PDFKitPlatformScrollViewAdded #def PDFKitPlatformTextFieldAdded #def PDFKitPlatformTextFieldDidBeginEditingAdded #def PDFKitPlatformTextFieldDidChangeTextAdded #def PDFKitPlatformTextFieldDidEndEditingAdded #def PDFKitPlatformTextViewAdded #def PDFKitPlatformTextViewDidChangeSelectionAdded #def PDFKitPlatformViewAdded #def PDFKitPlatformViewControllerAdded #def PDFPointAdded #def PDFRectAdded #def PDFRectZeroAdded #def PDFSizeAdded #def PDFSizeZero

#### PDFOutline.h

Removed -[PDFOutline setAction:]Removed -[PDFOutline setDestination:]Removed -[PDFOutline setIsOpen:]Removed -[PDFOutline setLabel:]Modified [PDFOutline.action](https://developer.apple.com/documentation/quartz/pdfoutline/1469328-action)

|  | Declaration |
| --- | --- |
| From | ``` - (PDFAction *)action ``` |
| To | ``` @property(nonatomic, retain) PDFAction *action ``` |

Modified [PDFOutline.destination](https://developer.apple.com/documentation/pdfkit/pdfoutline/1469330-destination)

|  | Declaration |
| --- | --- |
| From | ``` - (PDFDestination *)destination ``` |
| To | ``` @property(nonatomic, retain) PDFDestination *destination ``` |

Modified [PDFOutline.document](https://developer.apple.com/documentation/pdfkit/pdfoutline/1469349-document)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (PDFDocument *)document ``` | -- |
| To | ``` @property(nonatomic, readonly) PDFDocument *document ``` | yes |

Modified [PDFOutline.index](https://developer.apple.com/documentation/pdfkit/pdfoutline/1469358-index)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSUInteger)index ``` | -- |
| To | ``` @property(nonatomic, readonly) NSUInteger index ``` | yes |

Modified [-[PDFOutline init]](https://developer.apple.com/documentation/quartz/pdfoutline/1469326-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

Modified [PDFOutline.isOpen](https://developer.apple.com/documentation/quartz/pdfoutline/1469354-isopen)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isOpen ``` |
| To | ``` @property(nonatomic, assign) BOOL isOpen ``` |

Modified [PDFOutline.label](https://developer.apple.com/documentation/pdfkit/pdfoutline/1469343-label)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)label ``` |
| To | ``` @property(nonatomic, retain) NSString *label ``` |

Modified [PDFOutline.numberOfChildren](https://developer.apple.com/documentation/pdfkit/pdfoutline/1469345-numberofchildren)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSUInteger)numberOfChildren ``` | -- |
| To | ``` @property(nonatomic, readonly) NSUInteger numberOfChildren ``` | yes |

Modified [PDFOutline.parent](https://developer.apple.com/documentation/quartz/pdfoutline/1469356-parent)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (PDFOutline *)parent ``` | -- |
| To | ``` @property(nonatomic, readonly) PDFOutline *parent ``` | yes |

#### PDFPage.h

Removed -[PDFPage setDisplaysAnnotations:]Removed -[PDFPage setRotation:]Added [-[PDFPage drawWithBox:toContext:]](https://developer.apple.com/documentation/quartz/pdfpage/1642232-draw)Added [-[PDFPage transformContext:forBox:]](https://developer.apple.com/documentation/pdfkit/pdfpage/1642229-transformcontext)Added [-[PDFPage transformForBox:]](https://developer.apple.com/documentation/pdfkit/pdfpage/2138291-transform)Modified [PDFPage.annotations](https://developer.apple.com/documentation/pdfkit/pdfpage/1503450-annotations)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSArray *)annotations ``` | -- |
| To | ``` @property(nonatomic, readonly) NSArray<PDFAnnotation *> *annotations ``` | yes |

Modified [PDFPage.attributedString](https://developer.apple.com/documentation/quartz/pdfpage/1503883-attributedstring)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSAttributedString *)attributedString ``` | -- |
| To | ``` @property(nonatomic, readonly) NSAttributedString *attributedString ``` | yes |

Modified [PDFPage.dataRepresentation](https://developer.apple.com/documentation/pdfkit/pdfpage/1504381-datarepresentation)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSData *)dataRepresentation ``` | -- |
| To | ``` @property(nonatomic, readonly) NSData *dataRepresentation ``` | yes |

Modified [PDFPage.displaysAnnotations](https://developer.apple.com/documentation/quartz/pdfpage/1504477-displaysannotations)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)displaysAnnotations ``` |
| To | ``` @property(nonatomic, assign) BOOL displaysAnnotations ``` |

Modified [PDFPage.document](https://developer.apple.com/documentation/pdfkit/pdfpage/1503540-document)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (PDFDocument *)document ``` | -- |
| To | ``` @property(nonatomic, readonly, weak) PDFDocument *document ``` | yes |

Modified [-[PDFPage drawWithBox:]](https://developer.apple.com/documentation/quartz/pdfpage/1505015-drawwithbox)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFPage initWithImage:]](https://developer.apple.com/documentation/quartz/pdfpage/1504307-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithImage:(NSImage *)image ``` |
| To | ``` - (instancetype)initWithImage:(NSImage *)image ``` |

Modified [PDFPage.label](https://developer.apple.com/documentation/pdfkit/pdfpage/1504088-label)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSString *)label ``` | -- |
| To | ``` @property(nonatomic, readonly) NSString *label ``` | yes |

Modified [PDFPage.numberOfCharacters](https://developer.apple.com/documentation/quartz/pdfpage/1504395-numberofcharacters)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSUInteger)numberOfCharacters ``` | -- |
| To | ``` @property(nonatomic, readonly) NSUInteger numberOfCharacters ``` | yes |

Modified [PDFPage.pageRef](https://developer.apple.com/documentation/pdfkit/pdfpage/1504419-pageref)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (CGPDFPageRef)pageRef ``` | -- |
| To | ``` @property(nonatomic, readonly) CGPDFPageRef pageRef ``` | yes |

Modified [PDFPage.rotation](https://developer.apple.com/documentation/quartz/pdfpage/1503443-rotation)

|  | Declaration |
| --- | --- |
| From | ``` - (NSInteger)rotation ``` |
| To | ``` @property(nonatomic, assign) NSInteger rotation ``` |

Modified [PDFPage.string](https://developer.apple.com/documentation/quartz/pdfpage/1503949-string)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSString *)string ``` | -- |
| To | ``` @property(nonatomic, readonly) NSString *string ``` | yes |

Modified [-[PDFPage transformContextForBox:]](https://developer.apple.com/documentation/quartz/pdfpage/1503842-transformcontextforbox)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### PDFSelection.h

Removed -[PDFSelection setColor:]Modified [-[PDFSelection addSelections:]](https://developer.apple.com/documentation/quartz/pdfselection/1389573-add)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addSelections:(NSArray *)selections ``` |
| To | ``` - (void)addSelections:(NSArray<PDFSelection *> *)selections ``` |

Modified [PDFSelection.attributedString](https://developer.apple.com/documentation/pdfkit/pdfselection/1389583-attributedstring)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSAttributedString *)attributedString ``` | -- |
| To | ``` @property(nonatomic, readonly) NSAttributedString *attributedString ``` | yes |

Modified [PDFSelection.color](https://developer.apple.com/documentation/quartz/pdfselection/1389577-color)

|  | Declaration |
| --- | --- |
| From | ``` - (NSColor *)color ``` |
| To | ``` @property(nonatomic, retain) NSColor *color ``` |

Modified [-[PDFSelection initWithDocument:]](https://developer.apple.com/documentation/pdfkit/pdfselection/1389585-initwithdocument)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDocument:(PDFDocument *)document ``` |
| To | ``` - (instancetype)initWithDocument:(PDFDocument *)document ``` |

Modified [PDFSelection.pages](https://developer.apple.com/documentation/quartz/pdfselection/1389569-pages)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSArray *)pages ``` | -- |
| To | ``` @property(nonatomic, readonly) NSArray<PDFPage *> *pages ``` | yes |

Modified [-[PDFSelection selectionsByLine]](https://developer.apple.com/documentation/quartz/pdfselection/1389575-selectionsbyline)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)selectionsByLine ``` |
| To | ``` - (NSArray<PDFSelection *> *)selectionsByLine ``` |

Modified [PDFSelection.string](https://developer.apple.com/documentation/pdfkit/pdfselection/1389563-string)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSString *)string ``` | -- |
| To | ``` @property(nonatomic, readonly) NSString *string ``` | yes |

#### PDFThumbnailView.h

Removed -[PDFThumbnailView setAllowsDragging:]Removed -[PDFThumbnailView setAllowsMultipleSelection:]Removed -[PDFThumbnailView setBackgroundColor:]Removed -[PDFThumbnailView setLabelFont:]Removed -[PDFThumbnailView setMaximumNumberOfColumns:]Removed -[PDFThumbnailView setPDFView:]Removed -[PDFThumbnailView setThumbnailSize:]Modified [PDFThumbnailView.allowsDragging](https://developer.apple.com/documentation/quartz/pdfthumbnailview/1504978-allowsdragging)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)allowsDragging ``` |
| To | ``` @property(nonatomic, assign) BOOL allowsDragging ``` |

Modified [PDFThumbnailView.allowsMultipleSelection](https://developer.apple.com/documentation/quartz/pdfthumbnailview/1503781-allowsmultipleselection)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)allowsMultipleSelection ``` |
| To | ``` @property(nonatomic, assign) BOOL allowsMultipleSelection ``` |

Modified [PDFThumbnailView.backgroundColor](https://developer.apple.com/documentation/pdfkit/pdfthumbnailview/1503648-backgroundcolor)

|  | Declaration |
| --- | --- |
| From | ``` - (NSColor *)backgroundColor ``` |
| To | ``` @property(nonatomic, copy) NSColor *backgroundColor ``` |

Modified [PDFThumbnailView.labelFont](https://developer.apple.com/documentation/quartz/pdfthumbnailview/1503482-labelfont)

|  | Declaration |
| --- | --- |
| From | ``` - (NSFont *)labelFont ``` |
| To | ``` @property(nonatomic, copy) NSFont *labelFont ``` |

Modified [PDFThumbnailView.maximumNumberOfColumns](https://developer.apple.com/documentation/quartz/pdfthumbnailview/1504277-maximumnumberofcolumns)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)maximumNumberOfColumns ``` |
| To | ``` @property(nonatomic, assign) NSUInteger maximumNumberOfColumns ``` |

Modified [PDFThumbnailView.PDFView](https://developer.apple.com/documentation/pdfkit/pdfthumbnailview/1503803-pdfview)

|  | Declaration |
| --- | --- |
| From | ``` - (PDFView *)PDFView ``` |
| To | ``` @property(nonatomic, strong) PDFView *PDFView ``` |

Modified [-[PDFThumbnailView selectedPages]](https://developer.apple.com/documentation/pdfkit/pdfthumbnailview/1504275-selectedpages)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)selectedPages ``` |
| To | ``` - (NSArray<PDFPage *> *)selectedPages ``` |

Modified [PDFThumbnailView.thumbnailSize](https://developer.apple.com/documentation/quartz/pdfthumbnailview/1504642-thumbnailsize)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSize)thumbnailSize ``` |
| To | ``` @property(nonatomic, assign) NSSize thumbnailSize ``` |

#### PDFView.h

Removed -[PDFView setAllowsDragging:]Removed -[PDFView setAutoScales:]Removed -[PDFView setBackgroundColor:]Removed -[PDFView setCurrentSelection:]Removed -[PDFView setDelegate:]Removed -[PDFView setDisplayBox:]Removed -[PDFView setDisplayMode:]Removed -[PDFView setDisplaysAsBook:]Removed -[PDFView setDisplaysPageBreaks:]Removed -[PDFView setDocument:]Removed -[PDFView setEnableDataDetectors:]Removed -[PDFView setGreekingThreshold:]Removed -[PDFView setHighlightedSelections:]Removed -[PDFView setInterpolationQuality:]Removed -[PDFView setScaleFactor:]Removed -[PDFView setShouldAntiAlias:]Removed NSObject(PDFViewDelegate)Added [-[PDFView drawPage:toContext:]](https://developer.apple.com/documentation/pdfkit/pdfview/1642250-draw)Added [-[PDFView drawPagePost:toContext:]](https://developer.apple.com/documentation/pdfkit/pdfview/1642236-drawpagepost)Added [PDFViewDelegate](https://developer.apple.com/documentation/quartz/pdfviewdelegate)Modified [PDFView.allowsDragging](https://developer.apple.com/documentation/quartz/pdfview/1503646-allowsdragging)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)allowsDragging ``` |
| To | ``` @property(nonatomic, assign) BOOL allowsDragging ``` |

Modified [PDFView.autoScales](https://developer.apple.com/documentation/quartz/pdfview/1503809-autoscales)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)autoScales ``` |
| To | ``` @property(nonatomic, assign) BOOL autoScales ``` |

Modified [PDFView.backgroundColor](https://developer.apple.com/documentation/quartz/pdfview/1504612-backgroundcolor)

|  | Declaration |
| --- | --- |
| From | ``` - (NSColor *)backgroundColor ``` |
| To | ``` @property(nonatomic, retain) NSColor *backgroundColor ``` |

Modified [PDFView.currentDestination](https://developer.apple.com/documentation/quartz/pdfview/1504602-currentdestination)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (PDFDestination *)currentDestination ``` | -- |
| To | ``` @property(nonatomic, readonly) PDFDestination *currentDestination ``` | yes |

Modified [PDFView.currentPage](https://developer.apple.com/documentation/pdfkit/pdfview/1504963-currentpage)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (PDFPage *)currentPage ``` | -- |
| To | ``` @property(nonatomic, readonly) PDFPage *currentPage ``` | yes |

Modified [PDFView.currentSelection](https://developer.apple.com/documentation/quartz/pdfview/1504716-currentselection)

|  | Declaration |
| --- | --- |
| From | ``` - (PDFSelection *)currentSelection ``` |
| To | ``` @property(nonatomic, retain) PDFSelection *currentSelection ``` |

Modified [PDFView.delegate](https://developer.apple.com/documentation/quartz/pdfview/1504803-delegate)

|  | Declaration |
| --- | --- |
| From | ``` - (id)delegate ``` |
| To | ``` @property(nonatomic, weak) id<PDFViewDelegate> delegate ``` |

Modified [PDFView.displayBox](https://developer.apple.com/documentation/pdfkit/pdfview/1504811-displaybox)

|  | Declaration |
| --- | --- |
| From | ``` - (PDFDisplayBox)displayBox ``` |
| To | ``` @property(nonatomic, assign) PDFDisplayBox displayBox ``` |

Modified [PDFView.displayMode](https://developer.apple.com/documentation/quartz/pdfview/1504490-displaymode)

|  | Declaration |
| --- | --- |
| From | ``` - (PDFDisplayMode)displayMode ``` |
| To | ``` @property(nonatomic, assign) PDFDisplayMode displayMode ``` |

Modified [PDFView.displaysAsBook](https://developer.apple.com/documentation/pdfkit/pdfview/1503723-displaysasbook)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)displaysAsBook ``` |
| To | ``` @property(nonatomic, assign) BOOL displaysAsBook ``` |

Modified [PDFView.displaysPageBreaks](https://developer.apple.com/documentation/pdfkit/pdfview/1504711-displayspagebreaks)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)displaysPageBreaks ``` |
| To | ``` @property(nonatomic, assign) BOOL displaysPageBreaks ``` |

Modified [PDFView.document](https://developer.apple.com/documentation/pdfkit/pdfview/1503521-document)

|  | Declaration |
| --- | --- |
| From | ``` - (PDFDocument *)document ``` |
| To | ``` @property(nonatomic, retain) PDFDocument *document ``` |

Modified [PDFView.documentView](https://developer.apple.com/documentation/pdfkit/pdfview/1505061-documentview)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSView *)documentView ``` | -- |
| To | ``` @property(nonatomic, readonly) NSView *documentView ``` | yes |

Modified [-[PDFView drawPage:]](https://developer.apple.com/documentation/quartz/pdfview/1503783-drawpage)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFView drawPagePost:]](https://developer.apple.com/documentation/quartz/pdfview/1504565-drawpagepost)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [PDFView.enableDataDetectors](https://developer.apple.com/documentation/quartz/pdfview/1505127-enabledatadetectors)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)enableDataDetectors ``` |
| To | ``` @property(nonatomic, assign) BOOL enableDataDetectors ``` |

Modified [PDFView.greekingThreshold](https://developer.apple.com/documentation/quartz/pdfview/1503563-greekingthreshold)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (CGFloat)greekingThreshold ``` | -- |
| To | ``` @property(nonatomic, assign) CGFloat greekingThreshold ``` | OS X 10.12 |

Modified [PDFView.highlightedSelections](https://developer.apple.com/documentation/quartz/pdfview/1505292-highlightedselections)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)highlightedSelections ``` |
| To | ``` @property(nonatomic, retain) NSArray<PDFSelection *> *highlightedSelections ``` |

Modified [PDFView.interpolationQuality](https://developer.apple.com/documentation/quartz/pdfview/1503789-interpolationquality)

|  | Declaration |
| --- | --- |
| From | ``` - (PDFInterpolationQuality)interpolationQuality ``` |
| To | ``` @property(nonatomic, assign) PDFInterpolationQuality interpolationQuality ``` |

Modified [PDFView.scaleFactor](https://developer.apple.com/documentation/quartz/pdfview/1505096-scalefactor)

|  | Declaration |
| --- | --- |
| From | ``` - (CGFloat)scaleFactor ``` |
| To | ``` @property(nonatomic, assign) CGFloat scaleFactor ``` |

Modified [PDFView.shouldAntiAlias](https://developer.apple.com/documentation/quartz/pdfview/1503798-shouldantialias)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (BOOL)shouldAntiAlias ``` | -- |
| To | ``` @property(nonatomic, assign) BOOL shouldAntiAlias ``` | OS X 10.12 |

Modified [-[PDFView takeBackgroundColorFrom:]](https://developer.apple.com/documentation/quartz/pdfview/1503462-takebackgroundcolorfrom)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFView takePasswordFrom:]](https://developer.apple.com/documentation/quartz/pdfview/1504296-takepasswordfrom)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[PDFView visiblePages]](https://developer.apple.com/documentation/quartz/pdfview/1504176-visiblepages)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)visiblePages ``` |
| To | ``` - (NSArray<PDFPage *> *)visiblePages ``` |

Modified [-[PDFViewDelegate PDFViewOpenPDF:forRemoteGoToAction:]](https://developer.apple.com/documentation/pdfkit/pdfviewdelegate/1690920-pdfviewopenpdf)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[PDFViewDelegate PDFViewPerformFind:]](https://developer.apple.com/documentation/quartz/pdfviewdelegate/1690916-pdfviewperformfind)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[PDFViewDelegate PDFViewPerformGoToPage:]](https://developer.apple.com/documentation/pdfkit/pdfviewdelegate/1690924-pdfviewperformgo)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[PDFViewDelegate PDFViewPerformPrint:]](https://developer.apple.com/documentation/quartz/pdfviewdelegate/1690922-pdfviewperformprint)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[PDFViewDelegate PDFViewPrintJobTitle:]](https://developer.apple.com/documentation/quartz/pdfviewdelegate/1690910-pdfviewprintjobtitle)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[PDFViewDelegate PDFViewWillChangeScaleFactor:toScale:]](https://developer.apple.com/documentation/quartz/pdfviewdelegate/1690909-pdfviewwillchangescalefactor)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[PDFViewDelegate PDFViewWillClickOnLink:withURL:]](https://developer.apple.com/documentation/quartz/pdfviewdelegate/1690923-pdfviewwillclick)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

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
