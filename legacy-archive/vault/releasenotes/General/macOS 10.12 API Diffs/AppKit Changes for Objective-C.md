---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/AppKit.html
archived_at: '2026-07-18T02:50:33.513629Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# AppKit Changes for Objective-C

### AppKit

#### AppKitDefines.h

Added #def APPKIT_SWIFT_SDK_EPOCH_AT_LEAST

#### NSAccessibility.h

Added [NSWorkspace.accessibilityDisplayShouldInvertColors](https://developer.apple.com/documentation/appkit/nsworkspace/1644068-accessibilitydisplayshouldinvert)Added [NSWorkspace.accessibilityDisplayShouldReduceMotion](https://developer.apple.com/documentation/appkit/nsworkspace/1644069-accessibilitydisplayshouldreduce)

#### NSAccessibilityConstants.h

Added [NSAccessibilityMenuBarItemRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1644579-menubaritem)Added [NSAccessibilityRequiredAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1644515-required)Added [NSAccessibilityTextAlignmentAttribute](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1644251-accessibilityalignment)

#### NSAccessibilityProtocols.h

Added [NSAccessibility.accessibilityRequired](https://developer.apple.com/documentation/appkit/nsaccessibility/1646618-accessibilityrequired)Modified [NSAccessibilityLayoutArea.accessibilityFocusedUIElement](https://developer.apple.com/documentation/appkit/nsaccessibilitylayoutarea/1533902-accessibilityfocuseduielement)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (id)accessibilityFocusedUIElement ``` | -- |
| To | ``` @property(readonly, strong) id accessibilityFocusedUIElement ``` | yes |

#### NSAffineTransform.h

Modified [-[NSAffineTransform transformBezierPath:]](https://developer.apple.com/documentation/foundation/nsaffinetransform/1462131-transform)

|  | Declaration |
| --- | --- |
| From | ``` - (NSBezierPath *)transformBezierPath:(NSBezierPath *)aPath ``` |
| To | ``` - (NSBezierPath *)transformBezierPath:(NSBezierPath *)path ``` |

#### NSAlert.h

Removed [NSCriticalAlertStyle](https://developer.apple.com/documentation/appkit/nscriticalalertstyle)Removed [NSInformationalAlertStyle](https://developer.apple.com/documentation/appkit/nsinformationalalertstyle)Removed [NSWarningAlertStyle](https://developer.apple.com/documentation/appkit/nswarningalertstyle)Added NSAlert(NSAlertDeprecated)Added [NSAlertStyleCritical](https://developer.apple.com/documentation/appkit/nsalertstyle/nsalertstylecritical)Added [NSAlertStyleInformational](https://developer.apple.com/documentation/appkit/nsalertstyle/nsalertstyleinformational)Added [NSAlertStyleWarning](https://developer.apple.com/documentation/appkit/nsalert/style/warning)Added [NSCriticalAlertStyle](https://developer.apple.com/documentation/appkit/nscriticalalertstyle)Added [NSInformationalAlertStyle](https://developer.apple.com/documentation/appkit/nsinformationalalertstyle)Added [NSWarningAlertStyle](https://developer.apple.com/documentation/appkit/nswarningalertstyle)Modified [NSAlert.delegate](https://developer.apple.com/documentation/appkit/nsalert/1534327-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<NSAlertDelegate> delegate ``` |
| To | ``` @property(weak) id<NSAlertDelegate> delegate ``` |

#### NSAnimation.h

Added [-[NSAnimation initWithCoder:]](https://developer.apple.com/documentation/appkit/nsanimation/1643460-initwithcoder)Modified [-[NSAnimation initWithDuration:animationCurve:]](https://developer.apple.com/documentation/appkit/nsanimation/1530069-initwithduration)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [NSAnimation.runLoopModesForAnimating](https://developer.apple.com/documentation/appkit/nsanimation/1526965-runloopmodesforanimating)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray<NSString *> *runLoopModesForAnimating ``` |
| To | ``` @property(readonly, copy) NSArray<NSRunLoopMode> *runLoopModesForAnimating ``` |

#### NSAppearance.h

Added [-[NSAppearance initWithCoder:]](https://developer.apple.com/documentation/appkit/nsappearance/2269729-initwithcoder)Added #def NS_APPEARANCE_DECLARES_DESIGNATED_INITIALIZERSModified [-[NSAppearance initWithAppearanceNamed:bundle:]](https://developer.apple.com/documentation/appkit/nsappearance/1529131-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### NSApplication.h

Added [-[NSApplication enumerateWindowsWithOptions:usingBlock:]](https://developer.apple.com/documentation/appkit/nsapplication/1644472-enumeratewindows)Added [-[NSApplicationDelegate application:userDidAcceptCloudKitShareWithMetadata:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/2138329-application)Added [#def NSAppKitVersionNumber10_11](https://developer.apple.com/documentation/appkit/nsappkitversionnumber10_11)Added [#def NSAppKitVersionNumber10_11_1](https://developer.apple.com/documentation/appkit/nsappkitversion/1644695-macos10_11_1)Added [#def NSAppKitVersionNumber10_11_2](https://developer.apple.com/documentation/appkit/nsappkitversionnumber10_11_2)Added [#def NSAppKitVersionNumber10_11_3](https://developer.apple.com/documentation/appkit/nsappkitversion/1644634-macos10_11_3)Added NSApplication(NSEvent)Added NSApplication(NSResponder)Added [NSWindowListOptions](https://developer.apple.com/documentation/appkit/nswindowlistoptions)Added [NSWindowListOrderedFrontToBack](https://developer.apple.com/documentation/appkit/nsapplication/windowlistoptions/1644713-orderedfronttoback)Modified [-[NSApplication addWindowsItem:title:filename:]](https://developer.apple.com/documentation/appkit/nsapplication/1428660-addwindowsitem)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addWindowsItem:(NSWindow *)win title:(NSString *)aString filename:(BOOL)isFilename ``` |
| To | ``` - (void)addWindowsItem:(NSWindow *)win title:(NSString *)string filename:(BOOL)isFilename ``` |

Modified [-[NSApplication beginModalSessionForWindow:]](https://developer.apple.com/documentation/appkit/nsapplication/1428418-beginmodalsession)

|  | Declaration |
| --- | --- |
| From | ``` - (NSModalSession)beginModalSessionForWindow:(NSWindow *)theWindow ``` |
| To | ``` - (NSModalSession)beginModalSessionForWindow:(NSWindow *)window ``` |

Modified [-[NSApplication beginModalSessionForWindow:relativeToWindow:]](https://developer.apple.com/documentation/appkit/nsapplication/1428604-beginmodalsessionforwindow)

|  | Declaration |
| --- | --- |
| From | ``` - (NSModalSession)beginModalSessionForWindow:(NSWindow *)theWindow relativeToWindow:(NSWindow *)docWindow ``` |
| To | ``` - (NSModalSession)beginModalSessionForWindow:(NSWindow *)window relativeToWindow:(NSWindow *)docWindow ``` |

Modified [-[NSApplication changeWindowsItem:title:filename:]](https://developer.apple.com/documentation/appkit/nsapplication/1428689-changewindowsitem)

|  | Declaration |
| --- | --- |
| From | ``` - (void)changeWindowsItem:(NSWindow *)win title:(NSString *)aString filename:(BOOL)isFilename ``` |
| To | ``` - (void)changeWindowsItem:(NSWindow *)win title:(NSString *)string filename:(BOOL)isFilename ``` |

Modified [NSApplication.context](https://developer.apple.com/documentation/appkit/nsapplication/1428535-context)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[NSApplication discardEventsMatchingMask:beforeEvent:]](https://developer.apple.com/documentation/appkit/nsapplication/1428652-discardevents)

|  | Declaration |
| --- | --- |
| From | ``` - (void)discardEventsMatchingMask:(NSUInteger)mask beforeEvent:(NSEvent *)lastEvent ``` |
| To | ``` - (void)discardEventsMatchingMask:(NSEventMask)mask beforeEvent:(NSEvent *)lastEvent ``` |

Modified [-[NSApplication makeWindowsPerform:inOrder:]](https://developer.apple.com/documentation/appkit/nsapplication/1428580-makewindowsperform)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (NSWindow *)makeWindowsPerform:(SEL)aSelector inOrder:(BOOL)flag ``` | -- |
| To | ``` - (NSWindow *)makeWindowsPerform:(SEL)selector inOrder:(BOOL)flag ``` | OS X 10.12 |

Modified [-[NSApplication nextEventMatchingMask:untilDate:inMode:dequeue:]](https://developer.apple.com/documentation/appkit/nsapplication/1428485-nexteventmatchingmask)

|  | Declaration |
| --- | --- |
| From | ``` - (NSEvent *)nextEventMatchingMask:(NSUInteger)mask untilDate:(NSDate *)expiration inMode:(NSString *)mode dequeue:(BOOL)deqFlag ``` |
| To | ``` - (NSEvent *)nextEventMatchingMask:(NSEventMask)mask untilDate:(NSDate *)expiration inMode:(NSRunLoopMode)mode dequeue:(BOOL)deqFlag ``` |

Modified [-[NSApplication reportException:]](https://developer.apple.com/documentation/appkit/nsapplication/1428396-reportexception)

|  | Declaration |
| --- | --- |
| From | ``` - (void)reportException:(NSException *)theException ``` |
| To | ``` - (void)reportException:(NSException *)exception ``` |

Modified [-[NSApplication runModalForWindow:]](https://developer.apple.com/documentation/appkit/nsapplication/1428436-runmodal)

|  | Declaration |
| --- | --- |
| From | ``` - (NSInteger)runModalForWindow:(NSWindow *)theWindow ``` |
| To | ``` - (NSInteger)runModalForWindow:(NSWindow *)window ``` |

Modified [-[NSApplication runModalForWindow:relativeToWindow:]](https://developer.apple.com/documentation/appkit/nsapplication/1428777-runmodalforwindow)

|  | Declaration |
| --- | --- |
| From | ``` - (NSInteger)runModalForWindow:(NSWindow *)theWindow relativeToWindow:(NSWindow *)docWindow ``` |
| To | ``` - (NSInteger)runModalForWindow:(NSWindow *)window relativeToWindow:(NSWindow *)docWindow ``` |

Modified [-[NSApplication sendAction:to:from:]](https://developer.apple.com/documentation/appkit/nsapplication/1428509-sendaction)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)sendAction:(SEL)theAction to:(id)theTarget from:(id)sender ``` |
| To | ``` - (BOOL)sendAction:(SEL)action to:(id)target from:(id)sender ``` |

Modified [-[NSApplication sendEvent:]](https://developer.apple.com/documentation/appkit/nsapplication/1428359-sendevent)

|  | Declaration |
| --- | --- |
| From | ``` - (void)sendEvent:(NSEvent *)theEvent ``` |
| To | ``` - (void)sendEvent:(NSEvent *)event ``` |

Modified [-[NSApplication targetForAction:]](https://developer.apple.com/documentation/appkit/nsapplication/1428449-target)

|  | Declaration |
| --- | --- |
| From | ``` - (id)targetForAction:(SEL)theAction ``` |
| To | ``` - (id)targetForAction:(SEL)action ``` |

Modified [-[NSApplication targetForAction:to:from:]](https://developer.apple.com/documentation/appkit/nsapplication/1428658-targetforaction)

|  | Declaration |
| --- | --- |
| From | ``` - (id)targetForAction:(SEL)theAction to:(id)theTarget from:(id)sender ``` |
| To | ``` - (id)targetForAction:(SEL)action to:(id)target from:(id)sender ``` |

Modified [-[NSApplication tryToPerform:with:]](https://developer.apple.com/documentation/appkit/nsapplication/1428366-trytoperform)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)tryToPerform:(SEL)anAction with:(id)anObject ``` |
| To | ``` - (BOOL)tryToPerform:(SEL)action with:(id)object ``` |

#### NSBitmapImageRep.h

Removed [NS16BitBigEndianBitmapFormat](https://developer.apple.com/documentation/appkit/ns16bitbigendianbitmapformat)Removed [NS16BitLittleEndianBitmapFormat](https://developer.apple.com/documentation/appkit/ns16bitlittleendianbitmapformat)Removed [NS32BitBigEndianBitmapFormat](https://developer.apple.com/documentation/appkit/ns32bitbigendianbitmapformat)Removed [NS32BitLittleEndianBitmapFormat](https://developer.apple.com/documentation/appkit/ns32bitlittleendianbitmapformat)Removed [NSAlphaFirstBitmapFormat](https://developer.apple.com/documentation/appkit/nsalphafirstbitmapformat)Removed [NSAlphaNonpremultipliedBitmapFormat](https://developer.apple.com/documentation/appkit/nsalphanonpremultipliedbitmapformat)Removed [NSBMPFileType](https://developer.apple.com/documentation/appkit/nsbmpfiletype)Removed [NSFloatingPointSamplesBitmapFormat](https://developer.apple.com/documentation/appkit/nsfloatingpointsamplesbitmapformat)Removed [NSGIFFileType](https://developer.apple.com/documentation/appkit/nsgiffiletype)Removed [NSJPEG2000FileType](https://developer.apple.com/documentation/appkit/nsjpeg2000filetype)Removed [NSJPEGFileType](https://developer.apple.com/documentation/appkit/nsjpegfiletype)Removed [NSPNGFileType](https://developer.apple.com/documentation/appkit/nspngfiletype)Removed [NSTIFFFileType](https://developer.apple.com/documentation/appkit/nstifffiletype)Added [NS16BitBigEndianBitmapFormat](https://developer.apple.com/documentation/appkit/ns16bitbigendianbitmapformat)Added [NS16BitLittleEndianBitmapFormat](https://developer.apple.com/documentation/appkit/ns16bitlittleendianbitmapformat)Added [NS32BitBigEndianBitmapFormat](https://developer.apple.com/documentation/appkit/ns32bitbigendianbitmapformat)Added [NS32BitLittleEndianBitmapFormat](https://developer.apple.com/documentation/appkit/ns32bitlittleendianbitmapformat)Added [NSAlphaFirstBitmapFormat](https://developer.apple.com/documentation/appkit/nsalphafirstbitmapformat)Added [NSAlphaNonpremultipliedBitmapFormat](https://developer.apple.com/documentation/appkit/nsalphanonpremultipliedbitmapformat)Added [NSBitmapFormatAlphaFirst](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/format/1644159-alphafirst)Added [NSBitmapFormatAlphaNonpremultiplied](https://developer.apple.com/documentation/appkit/nsbitmapformat/nsbitmapformatalphanonpremultiplied)Added [NSBitmapFormatFloatingPointSamples](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/format/1644168-floatingpointsamples)Added [NSBitmapFormatSixteenBitBigEndian](https://developer.apple.com/documentation/appkit/nsbitmapformat/nsbitmapformatsixteenbitbigendian)Added [NSBitmapFormatSixteenBitLittleEndian](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/format/1644157-sixteenbitlittleendian)Added [NSBitmapFormatThirtyTwoBitBigEndian](https://developer.apple.com/documentation/appkit/nsbitmapformat/nsbitmapformatthirtytwobitbigendian)Added [NSBitmapFormatThirtyTwoBitLittleEndian](https://developer.apple.com/documentation/appkit/nsbitmapformat/nsbitmapformatthirtytwobitlittleendian)Added [NSBitmapImageFileTypeBMP](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/filetype/bmp)Added [NSBitmapImageFileTypeGIF](https://developer.apple.com/documentation/appkit/nsbitmapimagefiletype/nsbitmapimagefiletypegif)Added [NSBitmapImageFileTypeJPEG](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/filetype/jpeg)Added [NSBitmapImageFileTypeJPEG2000](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/filetype/jpeg2000)Added [NSBitmapImageFileTypePNG](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/filetype/png)Added [NSBitmapImageFileTypeTIFF](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/filetype/tiff)Added [NSBMPFileType](https://developer.apple.com/documentation/appkit/nsbmpfiletype)Added [NSFloatingPointSamplesBitmapFormat](https://developer.apple.com/documentation/appkit/nsfloatingpointsamplesbitmapformat)Added [NSGIFFileType](https://developer.apple.com/documentation/appkit/nsgiffiletype)Added [NSJPEG2000FileType](https://developer.apple.com/documentation/appkit/nsjpeg2000filetype)Added [NSJPEGFileType](https://developer.apple.com/documentation/appkit/nsjpegfiletype)Added [NSPNGFileType](https://developer.apple.com/documentation/appkit/nspngfiletype)Added [NSTIFFFileType](https://developer.apple.com/documentation/appkit/nstifffiletype)

#### NSBrowser.h

Modified [-[NSBrowser drawTitleOfColumn:inRect:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407809-drawtitleofcolumn)

|  | Declaration |
| --- | --- |
| From | ``` - (void)drawTitleOfColumn:(NSInteger)column inRect:(NSRect)aRect ``` |
| To | ``` - (void)drawTitleOfColumn:(NSInteger)column inRect:(NSRect)rect ``` |

Modified [-[NSBrowser editItemAtIndexPath:withEvent:select:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407558-edititematindexpath)

|  | Declaration |
| --- | --- |
| From | ``` - (void)editItemAtIndexPath:(NSIndexPath *)indexPath withEvent:(NSEvent *)theEvent select:(BOOL)select ``` |
| To | ``` - (void)editItemAtIndexPath:(NSIndexPath *)indexPath withEvent:(NSEvent *)event select:(BOOL)select ``` |

Modified [-[NSBrowser setTitle:ofColumn:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407575-settitle)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setTitle:(NSString *)aString ofColumn:(NSInteger)column ``` |
| To | ``` - (void)setTitle:(NSString *)string ofColumn:(NSInteger)column ``` |

#### NSBrowserCell.h

Added [-[NSBrowserCell initImageCell:]](https://developer.apple.com/documentation/appkit/nsbrowsercell/1644593-initimagecell)Added [-[NSBrowserCell initTextCell:]](https://developer.apple.com/documentation/appkit/nsbrowsercell/1644701-init)Added [-[NSBrowserCell initWithCoder:]](https://developer.apple.com/documentation/appkit/nsbrowsercell/1644667-initwithcoder)

#### NSButton.h

Added [+[NSButton buttonWithImage:target:action:]](https://developer.apple.com/documentation/appkit/nsbutton/1644659-buttonwithimage)Added [+[NSButton buttonWithTitle:image:target:action:]](https://developer.apple.com/documentation/appkit/nsbutton/1644719-init)Added [+[NSButton buttonWithTitle:target:action:]](https://developer.apple.com/documentation/appkit/nsbutton/1644256-buttonwithtitle)Added [+[NSButton checkboxWithTitle:target:action:]](https://developer.apple.com/documentation/appkit/nsbutton/1644525-init)Added [NSButton.imageHugsTitle](https://developer.apple.com/documentation/appkit/nsbutton/2092414-imagehugstitle)Added [NSButton.imageScaling](https://developer.apple.com/documentation/appkit/nsbutton/2202284-imagescaling)Added [+[NSButton radioButtonWithTitle:target:action:]](https://developer.apple.com/documentation/appkit/nsbutton/1644340-init)Added NSButton(NSButtonConvenience)Modified [NSButton.keyEquivalentModifierMask](https://developer.apple.com/documentation/appkit/nsbutton/1532670-keyequivalentmodifiermask)

|  | Declaration |
| --- | --- |
| From | ``` @property NSUInteger keyEquivalentModifierMask ``` |
| To | ``` @property NSEventModifierFlags keyEquivalentModifierMask ``` |

Modified [-[NSButton setButtonType:]](https://developer.apple.com/documentation/appkit/nsbutton/1524983-setbuttontype)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setButtonType:(NSButtonType)aType ``` |
| To | ``` - (void)setButtonType:(NSButtonType)type ``` |

#### NSButtonCell.h

Removed [NSAcceleratorButton](https://developer.apple.com/documentation/appkit/nsacceleratorbutton)Removed NSButtonCell(NSKeyboardUI)Removed [NSCircularBezelStyle](https://developer.apple.com/documentation/appkit/nscircularbezelstyle)Removed [NSDisclosureBezelStyle](https://developer.apple.com/documentation/appkit/nsdisclosurebezelstyle)Removed [NSHelpButtonBezelStyle](https://developer.apple.com/documentation/appkit/nshelpbuttonbezelstyle)Removed [NSInlineBezelStyle](https://developer.apple.com/documentation/appkit/nsinlinebezelstyle)Removed [NSMomentaryChangeButton](https://developer.apple.com/documentation/appkit/nsmomentarychangebutton)Removed [NSMomentaryLight](https://developer.apple.com/documentation/appkit/nsmomentarylight)Removed [NSMomentaryLightButton](https://developer.apple.com/documentation/appkit/nsmomentarylightbutton)Removed [NSMomentaryPushButton](https://developer.apple.com/documentation/appkit/nsmomentarypushbutton)Removed [NSMomentaryPushInButton](https://developer.apple.com/documentation/appkit/nsmomentarypushinbutton)Removed [NSMultiLevelAcceleratorButton](https://developer.apple.com/documentation/appkit/nsmultilevelacceleratorbutton)Removed [NSOnOffButton](https://developer.apple.com/documentation/appkit/nsonoffbutton)Removed [NSPushOnPushOffButton](https://developer.apple.com/documentation/appkit/nspushonpushoffbutton)Removed [NSRadioButton](https://developer.apple.com/documentation/appkit/nsradiobutton)Removed [NSRecessedBezelStyle](https://developer.apple.com/documentation/appkit/nsrecessedbezelstyle)Removed [NSRegularSquareBezelStyle](https://developer.apple.com/documentation/appkit/nsregularsquarebezelstyle)Removed [NSRoundedBezelStyle](https://developer.apple.com/documentation/appkit/nsroundedbezelstyle)Removed [NSRoundedDisclosureBezelStyle](https://developer.apple.com/documentation/appkit/nsroundeddisclosurebezelstyle)Removed [NSRoundRectBezelStyle](https://developer.apple.com/documentation/appkit/nsroundrectbezelstyle)Removed [NSShadowlessSquareBezelStyle](https://developer.apple.com/documentation/appkit/nsshadowlesssquarebezelstyle)Removed [NSSmallIconButtonBezelStyle](https://developer.apple.com/documentation/appkit/nssmalliconbuttonbezelstyle)Removed [NSSmallSquareBezelStyle](https://developer.apple.com/documentation/appkit/nssmallsquarebezelstyle)Removed [NSSwitchButton](https://developer.apple.com/documentation/appkit/nsswitchbutton)Removed [NSTexturedRoundedBezelStyle](https://developer.apple.com/documentation/appkit/nstexturedroundedbezelstyle)Removed [NSTexturedSquareBezelStyle](https://developer.apple.com/documentation/appkit/nstexturedsquarebezelstyle)Removed [NSThickerSquareBezelStyle](https://developer.apple.com/documentation/appkit/nsthickersquarebezelstyle)Removed [NSThickSquareBezelStyle](https://developer.apple.com/documentation/appkit/nsthicksquarebezelstyle)Removed [NSToggleButton](https://developer.apple.com/documentation/appkit/nstogglebutton)Added [-[NSButtonCell initImageCell:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1639152-initimagecell)Added [-[NSButtonCell initTextCell:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1639134-inittextcell)Added [-[NSButtonCell initWithCoder:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1639159-initwithcoder)Added [NSAcceleratorButton](https://developer.apple.com/documentation/appkit/nsacceleratorbutton)Added [NSBezelStyleCircular](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle/circular)Added [NSBezelStyleDisclosure](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle/disclosure)Added [NSBezelStyleHelpButton](https://developer.apple.com/documentation/appkit/nsbezelstyle/nsbezelstylehelpbutton)Added [NSBezelStyleInline](https://developer.apple.com/documentation/appkit/nsbezelstyle/nsbezelstyleinline)Added [NSBezelStyleRecessed](https://developer.apple.com/documentation/appkit/nsbezelstyle/nsbezelstylerecessed)Added [NSBezelStyleRegularSquare](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle/regularsquare)Added [NSBezelStyleRounded](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle/rounded)Added [NSBezelStyleRoundedDisclosure](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle/roundeddisclosure)Added [NSBezelStyleRoundRect](https://developer.apple.com/documentation/appkit/nsbezelstyle/nsbezelstyleroundrect)Added [NSBezelStyleShadowlessSquare](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle/shadowlesssquare)Added [NSBezelStyleSmallSquare](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle/smallsquare)Added [NSBezelStyleTexturedRounded](https://developer.apple.com/documentation/appkit/nsbezelstyle/nsbezelstyletexturedrounded)Added [NSBezelStyleTexturedSquare](https://developer.apple.com/documentation/appkit/nsbezelstyle/nsbezelstyletexturedsquare)Added NSButtonCell(NSDeprecated)Added [NSButtonTypeAccelerator](https://developer.apple.com/documentation/appkit/nsbutton/buttontype/accelerator)Added [NSButtonTypeMomentaryChange](https://developer.apple.com/documentation/appkit/nsbuttontype/nsbuttontypemomentarychange)Added [NSButtonTypeMomentaryLight](https://developer.apple.com/documentation/appkit/nsbuttontype/nsbuttontypemomentarylight)Added [NSButtonTypeMomentaryPushIn](https://developer.apple.com/documentation/appkit/nsbuttontype/nsbuttontypemomentarypushin)Added [NSButtonTypeMultiLevelAccelerator](https://developer.apple.com/documentation/appkit/nsbuttontype/nsbuttontypemultilevelaccelerator)Added [NSButtonTypeOnOff](https://developer.apple.com/documentation/appkit/nsbutton/buttontype/onoff)Added [NSButtonTypePushOnPushOff](https://developer.apple.com/documentation/appkit/nsbuttontype/nsbuttontypepushonpushoff)Added [NSButtonTypeRadio](https://developer.apple.com/documentation/appkit/nsbuttontype/nsbuttontyperadio)Added [NSButtonTypeSwitch](https://developer.apple.com/documentation/appkit/nsbuttontype/nsbuttontypeswitch)Added [NSButtonTypeToggle](https://developer.apple.com/documentation/appkit/nsbutton/buttontype/toggle)Added [NSCircularBezelStyle](https://developer.apple.com/documentation/appkit/nscircularbezelstyle)Added [NSDisclosureBezelStyle](https://developer.apple.com/documentation/appkit/nsdisclosurebezelstyle)Added [NSHelpButtonBezelStyle](https://developer.apple.com/documentation/appkit/nshelpbuttonbezelstyle)Added [NSInlineBezelStyle](https://developer.apple.com/documentation/appkit/nsinlinebezelstyle)Added [NSMomentaryChangeButton](https://developer.apple.com/documentation/appkit/nsmomentarychangebutton)Added [NSMomentaryLight](https://developer.apple.com/documentation/appkit/nsmomentarylight)Added [NSMomentaryLightButton](https://developer.apple.com/documentation/appkit/nsmomentarylightbutton)Added [NSMomentaryPushButton](https://developer.apple.com/documentation/appkit/nsmomentarypushbutton)Added [NSMomentaryPushInButton](https://developer.apple.com/documentation/appkit/nsmomentarypushinbutton)Added [NSMultiLevelAcceleratorButton](https://developer.apple.com/documentation/appkit/nsmultilevelacceleratorbutton)Added [NSOnOffButton](https://developer.apple.com/documentation/appkit/nsonoffbutton)Added [NSPushOnPushOffButton](https://developer.apple.com/documentation/appkit/nspushonpushoffbutton)Added [NSRadioButton](https://developer.apple.com/documentation/appkit/nsradiobutton)Added [NSRecessedBezelStyle](https://developer.apple.com/documentation/appkit/nsrecessedbezelstyle)Added [NSRegularSquareBezelStyle](https://developer.apple.com/documentation/appkit/nsregularsquarebezelstyle)Added [NSRoundedBezelStyle](https://developer.apple.com/documentation/appkit/nsroundedbezelstyle)Added [NSRoundedDisclosureBezelStyle](https://developer.apple.com/documentation/appkit/nsroundeddisclosurebezelstyle)Added [NSRoundRectBezelStyle](https://developer.apple.com/documentation/appkit/nsroundrectbezelstyle)Added [NSShadowlessSquareBezelStyle](https://developer.apple.com/documentation/appkit/nsshadowlesssquarebezelstyle)Added [NSSmallIconButtonBezelStyle](https://developer.apple.com/documentation/appkit/nssmalliconbuttonbezelstyle)Added [NSSmallSquareBezelStyle](https://developer.apple.com/documentation/appkit/nssmallsquarebezelstyle)Added [NSSwitchButton](https://developer.apple.com/documentation/appkit/nsswitchbutton)Added [NSTexturedRoundedBezelStyle](https://developer.apple.com/documentation/appkit/nstexturedroundedbezelstyle)Added [NSTexturedSquareBezelStyle](https://developer.apple.com/documentation/appkit/nstexturedsquarebezelstyle)Added [NSThickerSquareBezelStyle](https://developer.apple.com/documentation/appkit/nsthickersquarebezelstyle)Added [NSThickSquareBezelStyle](https://developer.apple.com/documentation/appkit/nsthicksquarebezelstyle)Added [NSToggleButton](https://developer.apple.com/documentation/appkit/nstogglebutton)Modified [NSButtonCell.gradientType](https://developer.apple.com/documentation/appkit/nsbuttoncell/1532259-gradienttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NSButtonCell.keyEquivalentModifierMask](https://developer.apple.com/documentation/appkit/nsbuttoncell/1528315-keyequivalentmodifiermask)

|  | Declaration |
| --- | --- |
| From | ``` @property NSUInteger keyEquivalentModifierMask ``` |
| To | ``` @property NSEventModifierFlags keyEquivalentModifierMask ``` |

Modified [-[NSButtonCell setButtonType:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1527474-setbuttontype)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setButtonType:(NSButtonType)aType ``` |
| To | ``` - (void)setButtonType:(NSButtonType)type ``` |

Modified [NSGradientConcaveStrong](https://developer.apple.com/documentation/appkit/nsbutton/gradienttype/concavestrong)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NSGradientConcaveWeak](https://developer.apple.com/documentation/appkit/nsbutton/gradienttype/concaveweak)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NSGradientConvexStrong](https://developer.apple.com/documentation/appkit/nsgradienttype/nsgradientconvexstrong)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NSGradientConvexWeak](https://developer.apple.com/documentation/appkit/nsbutton/gradienttype/convexweak)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NSGradientNone](https://developer.apple.com/documentation/appkit/nsgradienttype/nsgradientnone)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### NSCell.h

Removed [NSMiniControlSize](https://developer.apple.com/documentation/appkit/nsminicontrolsize)Removed [NSRegularControlSize](https://developer.apple.com/documentation/appkit/nsregularcontrolsize)Removed [NSSmallControlSize](https://developer.apple.com/documentation/appkit/nssmallcontrolsize)Added [-[NSCell init]](https://developer.apple.com/documentation/appkit/nscell/1642242-init)Added [-[NSCell initWithCoder:]](https://developer.apple.com/documentation/appkit/nscell/1642237-init)Added [NSControlSizeMini](https://developer.apple.com/documentation/appkit/nscontrolsize/nscontrolsizemini)Added [NSControlSizeRegular](https://developer.apple.com/documentation/appkit/nscontrolsize/nscontrolsizeregular)Added [NSControlSizeSmall](https://developer.apple.com/documentation/appkit/nscontrolsize/nscontrolsizesmall)Added [NSImageLeading](https://developer.apple.com/documentation/appkit/nscellimageposition/nsimageleading)Added [NSImageTrailing](https://developer.apple.com/documentation/appkit/nscontrol/imageposition/imagetrailing)Added [NSMiniControlSize](https://developer.apple.com/documentation/appkit/nsminicontrolsize)Added [NSRegularControlSize](https://developer.apple.com/documentation/appkit/nsregularcontrolsize)Added [NSSmallControlSize](https://developer.apple.com/documentation/appkit/nssmallcontrolsize)Modified [-[NSCell calcDrawInfo:]](https://developer.apple.com/documentation/appkit/nscell/1533752-calcdrawinfo)

|  | Declaration |
| --- | --- |
| From | ``` - (void)calcDrawInfo:(NSRect)aRect ``` |
| To | ``` - (void)calcDrawInfo:(NSRect)rect ``` |

Modified [-[NSCell cellAttribute:]](https://developer.apple.com/documentation/appkit/nscell/1530877-cellattribute)

|  | Declaration |
| --- | --- |
| From | ``` - (NSInteger)cellAttribute:(NSCellAttribute)aParameter ``` |
| To | ``` - (NSInteger)cellAttribute:(NSCellAttribute)parameter ``` |

Modified [-[NSCell cellSizeForBounds:]](https://developer.apple.com/documentation/appkit/nscell/1524792-cellsize)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSize)cellSizeForBounds:(NSRect)aRect ``` |
| To | ``` - (NSSize)cellSizeForBounds:(NSRect)rect ``` |

Modified [-[NSCell drawingRectForBounds:]](https://developer.apple.com/documentation/appkit/nscell/1526266-drawingrect)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)drawingRectForBounds:(NSRect)theRect ``` |
| To | ``` - (NSRect)drawingRectForBounds:(NSRect)rect ``` |

Modified [-[NSCell editWithFrame:inView:editor:delegate:event:]](https://developer.apple.com/documentation/appkit/nscell/1533600-editwithframe)

|  | Declaration |
| --- | --- |
| From | ``` - (void)editWithFrame:(NSRect)aRect inView:(NSView *)controlView editor:(NSText *)textObj delegate:(id)anObject event:(NSEvent *)theEvent ``` |
| To | ``` - (void)editWithFrame:(NSRect)rect inView:(NSView *)controlView editor:(NSText *)textObj delegate:(id)delegate event:(NSEvent *)event ``` |

Modified [-[NSCell fieldEditorForView:]](https://developer.apple.com/documentation/appkit/nscell/1532763-fieldeditor)

|  | Declaration |
| --- | --- |
| From | ``` - (NSTextView *)fieldEditorForView:(NSView *)aControlView ``` |
| To | ``` - (NSTextView *)fieldEditorForView:(NSView *)controlView ``` |

Modified [-[NSCell imageRectForBounds:]](https://developer.apple.com/documentation/appkit/nscell/1533408-imagerectforbounds)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)imageRectForBounds:(NSRect)theRect ``` |
| To | ``` - (NSRect)imageRectForBounds:(NSRect)rect ``` |

Modified [-[NSCell initImageCell:]](https://developer.apple.com/documentation/appkit/nscell/1533898-initimagecell)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSCell initTextCell:]](https://developer.apple.com/documentation/appkit/nscell/1530851-inittextcell)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initTextCell:(NSString *)aString ``` | -- |
| To | ``` - (instancetype)initTextCell:(NSString *)string ``` | yes |

Modified [-[NSCell isEntryAcceptable:]](https://developer.apple.com/documentation/appkit/nscell/1560879-isentryacceptable)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isEntryAcceptable:(NSString *)aString ``` |
| To | ``` - (BOOL)isEntryAcceptable:(NSString *)string ``` |

Modified [-[NSCell selectWithFrame:inView:editor:delegate:start:length:]](https://developer.apple.com/documentation/appkit/nscell/1527438-selectwithframe)

|  | Declaration |
| --- | --- |
| From | ``` - (void)selectWithFrame:(NSRect)aRect inView:(NSView *)controlView editor:(NSText *)textObj delegate:(id)anObject start:(NSInteger)selStart length:(NSInteger)selLength ``` |
| To | ``` - (void)selectWithFrame:(NSRect)rect inView:(NSView *)controlView editor:(NSText *)textObj delegate:(id)delegate start:(NSInteger)selStart length:(NSInteger)selLength ``` |

Modified [-[NSCell sendActionOn:]](https://developer.apple.com/documentation/appkit/nscell/1528114-sendaction)

|  | Declaration |
| --- | --- |
| From | ``` - (NSInteger)sendActionOn:(NSInteger)mask ``` |
| To | ``` - (NSInteger)sendActionOn:(NSEventMask)mask ``` |

Modified [-[NSCell setCellAttribute:to:]](https://developer.apple.com/documentation/appkit/nscell/1531257-setcellattribute)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setCellAttribute:(NSCellAttribute)aParameter to:(NSInteger)value ``` |
| To | ``` - (void)setCellAttribute:(NSCellAttribute)parameter to:(NSInteger)value ``` |

Modified [-[NSCell setEntryType:]](https://developer.apple.com/documentation/appkit/nscell/1560876-setentrytype)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setEntryType:(NSInteger)aType ``` |
| To | ``` - (void)setEntryType:(NSInteger)type ``` |

Modified [-[NSCell titleRectForBounds:]](https://developer.apple.com/documentation/appkit/nscell/1531281-titlerect)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)titleRectForBounds:(NSRect)theRect ``` |
| To | ``` - (NSRect)titleRectForBounds:(NSRect)rect ``` |

Modified [-[NSCell trackMouse:inRect:ofView:untilMouseUp:]](https://developer.apple.com/documentation/appkit/nscell/1533606-trackmouse)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)trackMouse:(NSEvent *)theEvent inRect:(NSRect)cellFrame ofView:(NSView *)controlView untilMouseUp:(BOOL)flag ``` |
| To | ``` - (BOOL)trackMouse:(NSEvent *)event inRect:(NSRect)cellFrame ofView:(NSView *)controlView untilMouseUp:(BOOL)flag ``` |

#### NSClipView.h

Modified [-[NSClipView autoscroll:]](https://developer.apple.com/documentation/appkit/nsclipview/1528953-autoscroll)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)autoscroll:(NSEvent *)theEvent ``` |
| To | ``` - (BOOL)autoscroll:(NSEvent *)event ``` |

Modified [NSClipView.documentView](https://developer.apple.com/documentation/appkit/nsclipview/1524587-documentview)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id documentView ``` |
| To | ``` @property(assign) __kindof NSView *documentView ``` |

Modified [-[NSView reflectScrolledClipView:]](https://developer.apple.com/documentation/appkit/nsview/1534216-reflectscrolledclipview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)reflectScrolledClipView:(NSClipView *)aClipView ``` |
| To | ``` - (void)reflectScrolledClipView:(NSClipView *)clipView ``` |

Modified [-[NSView scrollClipView:toPoint:]](https://developer.apple.com/documentation/appkit/nsview/1531337-scrollclipview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)scrollClipView:(NSClipView *)aClipView toPoint:(NSPoint)aPoint ``` |
| To | ``` - (void)scrollClipView:(NSClipView *)clipView toPoint:(NSPoint)point ``` |

#### NSCollectionView.h

Added [NSCollectionView.backgroundViewScrollsWithContent](https://developer.apple.com/documentation/appkit/nscollectionview/1644533-backgroundviewscrollswithcontent)Added [-[NSCollectionView toggleSectionCollapse:]](https://developer.apple.com/documentation/appkit/nscollectionview/1644691-togglesectioncollapse)Added [NSCollectionViewSectionHeaderView](https://developer.apple.com/documentation/appkit/nscollectionviewsectionheaderview)Added [NSCollectionViewSectionHeaderView.sectionCollapseButton](https://developer.apple.com/documentation/appkit/nscollectionviewsectionheaderview/1644266-sectioncollapsebutton)Modified [NSCollectionView.collectionViewLayout](https://developer.apple.com/documentation/appkit/nscollectionview/1528271-collectionviewlayout)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSCollectionViewLayout *collectionViewLayout ``` |
| To | ``` @property(strong) __kindof NSCollectionViewLayout *collectionViewLayout ``` |

Modified [NSCollectionView.delegate](https://developer.apple.com/documentation/appkit/nscollectionview/1528246-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<NSCollectionViewDelegate> delegate ``` |
| To | ``` @property(weak) id<NSCollectionViewDelegate> delegate ``` |

#### NSCollectionViewFlowLayout.h

Added [-[NSCollectionViewFlowLayout collapseSectionAtIndex:]](https://developer.apple.com/documentation/appkit/nscollectionviewflowlayout/1644723-collapsesection)Added [-[NSCollectionViewFlowLayout expandSectionAtIndex:]](https://developer.apple.com/documentation/appkit/nscollectionviewflowlayout/1644651-expandsectionatindex)Added [-[NSCollectionViewFlowLayout sectionAtIndexIsCollapsed:]](https://developer.apple.com/documentation/appkit/nscollectionviewflowlayout/1644596-section)Added [NSCollectionViewFlowLayout.sectionFootersPinToVisibleBounds](https://developer.apple.com/documentation/appkit/nscollectionviewflowlayout/1644671-sectionfooterspintovisiblebounds)Added [NSCollectionViewFlowLayout.sectionHeadersPinToVisibleBounds](https://developer.apple.com/documentation/appkit/nscollectionviewflowlayout/1644640-sectionheaderspintovisiblebounds)

#### NSColor.h

Added NSColor.alternateSelectedControlColorAdded NSColor.alternateSelectedControlTextColorAdded NSColor.blackColorAdded NSColor.blueColorAdded NSColor.brownColorAdded NSColor.clearColorAdded [+[NSColor colorWithColorSpace:hue:saturation:brightness:alpha:]](https://developer.apple.com/documentation/appkit/nscolor/1644595-colorwithcolorspace)Added [+[NSColor colorWithDisplayP3Red:green:blue:alpha:]](https://developer.apple.com/documentation/appkit/nscolor/1644633-init)Added NSColor.controlAlternatingRowBackgroundColorsAdded NSColor.controlBackgroundColorAdded NSColor.controlColorAdded NSColor.controlDarkShadowColorAdded NSColor.controlHighlightColorAdded NSColor.controlLightHighlightColorAdded NSColor.controlShadowColorAdded NSColor.controlTextColorAdded NSColor.currentControlTintAdded NSColor.cyanColorAdded NSColor.darkGrayColorAdded NSColor.disabledControlTextColorAdded NSColor.grayColorAdded NSColor.greenColorAdded NSColor.gridColorAdded NSColor.headerColorAdded NSColor.headerTextColorAdded NSColor.highlightColorAdded NSColor.ignoresAlphaAdded NSColor.keyboardFocusIndicatorColorAdded NSColor.knobColorAdded NSColor.labelColorAdded NSColor.lightGrayColorAdded NSColor.magentaColorAdded NSColor.orangeColorAdded NSColor.purpleColorAdded NSColor.quaternaryLabelColorAdded NSColor.redColorAdded NSColor.scrollBarColorAdded NSColor.secondaryLabelColorAdded NSColor.secondarySelectedControlColorAdded NSColor.selectedControlColorAdded NSColor.selectedControlTextColorAdded NSColor.selectedKnobColorAdded NSColor.selectedMenuItemColorAdded NSColor.selectedMenuItemTextColorAdded NSColor.selectedTextBackgroundColorAdded NSColor.selectedTextColorAdded NSColor.shadowColorAdded NSColor.tertiaryLabelColorAdded NSColor.textBackgroundColorAdded NSColor.textColorAdded NSColor.underPageBackgroundColorAdded NSColor.whiteColorAdded NSColor.windowBackgroundColorAdded NSColor.windowFrameColorAdded NSColor.windowFrameTextColorAdded NSColor.yellowColorAdded #def NSCOLOR_USE_CLASS_PROPERTIESModified +[NSColor setIgnoresAlpha:]

|  | Declaration |
| --- | --- |
| From | ``` + (void)setIgnoresAlpha:(BOOL)flag ``` |
| To | ``` + (void)setIgnoresAlpha:(BOOL)ignoresAlpha ``` |

#### NSColorList.h

Added [-[NSColorList writeToURL:error:]](https://developer.apple.com/documentation/appkit/nscolorlist/2269695-writetourl)

#### NSColorPanel.h

Removed [NSCMYKModeColorPanel](https://developer.apple.com/documentation/appkit/nscmykmodecolorpanel)Removed [NSColorListModeColorPanel](https://developer.apple.com/documentation/appkit/nscolorlistmodecolorpanel)Removed [NSCrayonModeColorPanel](https://developer.apple.com/documentation/appkit/nscrayonmodecolorpanel)Removed [NSCustomPaletteModeColorPanel](https://developer.apple.com/documentation/appkit/nscustompalettemodecolorpanel)Removed [NSGrayModeColorPanel](https://developer.apple.com/documentation/appkit/nsgraymodecolorpanel)Removed [NSHSBModeColorPanel](https://developer.apple.com/documentation/appkit/nshsbmodecolorpanel)Removed [NSNoModeColorPanel](https://developer.apple.com/documentation/appkit/nsnomodecolorpanel)Removed [NSRGBModeColorPanel](https://developer.apple.com/documentation/appkit/nsrgbmodecolorpanel)Removed [NSWheelModeColorPanel](https://developer.apple.com/documentation/appkit/nswheelmodecolorpanel)Added [NSCMYKModeColorPanel](https://developer.apple.com/documentation/appkit/nscmykmodecolorpanel)Added [NSColorListModeColorPanel](https://developer.apple.com/documentation/appkit/nscolorlistmodecolorpanel)Added [NSColorPanelModeCMYK](https://developer.apple.com/documentation/appkit/nscolorpanel/mode/cmyk)Added [NSColorPanelModeColorList](https://developer.apple.com/documentation/appkit/nscolorpanelmode/nscolorpanelmodecolorlist)Added [NSColorPanelModeCrayon](https://developer.apple.com/documentation/appkit/nscolorpanelmode/nscolorpanelmodecrayon)Added [NSColorPanelModeCustomPalette](https://developer.apple.com/documentation/appkit/nscolorpanelmode/nscolorpanelmodecustompalette)Added [NSColorPanelModeGray](https://developer.apple.com/documentation/appkit/nscolorpanel/mode/gray)Added [NSColorPanelModeHSB](https://developer.apple.com/documentation/appkit/nscolorpanelmode/nscolorpanelmodehsb)Added [NSColorPanelModeNone](https://developer.apple.com/documentation/appkit/nscolorpanel/mode/none)Added [NSColorPanelModeRGB](https://developer.apple.com/documentation/appkit/nscolorpanel/mode/rgb)Added [NSColorPanelModeWheel](https://developer.apple.com/documentation/appkit/nscolorpanel/mode/wheel)Added [NSCrayonModeColorPanel](https://developer.apple.com/documentation/appkit/nscrayonmodecolorpanel)Added [NSCustomPaletteModeColorPanel](https://developer.apple.com/documentation/appkit/nscustompalettemodecolorpanel)Added [NSGrayModeColorPanel](https://developer.apple.com/documentation/appkit/nsgraymodecolorpanel)Added [NSHSBModeColorPanel](https://developer.apple.com/documentation/appkit/nshsbmodecolorpanel)Added [NSNoModeColorPanel](https://developer.apple.com/documentation/appkit/nsnomodecolorpanel)Added [NSRGBModeColorPanel](https://developer.apple.com/documentation/appkit/nsrgbmodecolorpanel)Added [NSWheelModeColorPanel](https://developer.apple.com/documentation/appkit/nswheelmodecolorpanel)Modified [+[NSColorPanel dragColor:withEvent:fromView:]](https://developer.apple.com/documentation/appkit/nscolorpanel/1529152-dragcolor)

|  | Declaration |
| --- | --- |
| From | ``` + (BOOL)dragColor:(NSColor *)color withEvent:(NSEvent *)theEvent fromView:(NSView *)sourceView ``` |
| To | ``` + (BOOL)dragColor:(NSColor *)color withEvent:(NSEvent *)event fromView:(NSView *)sourceView ``` |

Modified [-[NSColorPanel setAction:]](https://developer.apple.com/documentation/appkit/nscolorpanel/1531244-setaction)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setAction:(SEL)aSelector ``` |
| To | ``` - (void)setAction:(SEL)selector ``` |

Modified [-[NSColorPanel setTarget:]](https://developer.apple.com/documentation/appkit/nscolorpanel/1524753-settarget)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setTarget:(id)anObject ``` |
| To | ``` - (void)setTarget:(id)target ``` |

#### NSColorSpace.h

Removed [NSCMYKColorSpaceModel](https://developer.apple.com/documentation/appkit/nscmykcolorspacemodel)Removed [NSDeviceNColorSpaceModel](https://developer.apple.com/documentation/appkit/nsdevicencolorspacemodel)Removed [NSGrayColorSpaceModel](https://developer.apple.com/documentation/appkit/nsgraycolorspacemodel)Removed [NSIndexedColorSpaceModel](https://developer.apple.com/documentation/appkit/nsindexedcolorspacemodel)Removed [NSLABColorSpaceModel](https://developer.apple.com/documentation/appkit/nslabcolorspacemodel)Removed [NSPatternColorSpaceModel](https://developer.apple.com/documentation/appkit/nspatterncolorspacemodel)Removed [NSRGBColorSpaceModel](https://developer.apple.com/documentation/appkit/nsrgbcolorspacemodel)Removed [NSUnknownColorSpaceModel](https://developer.apple.com/documentation/appkit/nsunknowncolorspacemodel)Added NSColorSpace.adobeRGB1998ColorSpaceAdded NSColorSpace.deviceCMYKColorSpaceAdded NSColorSpace.deviceGrayColorSpaceAdded NSColorSpace.deviceRGBColorSpaceAdded [+[NSColorSpace displayP3ColorSpace]](https://developer.apple.com/documentation/appkit/nscolorspace/1644170-displayp3colorspace)Added NSColorSpace.displayP3ColorSpaceAdded [+[NSColorSpace extendedGenericGamma22GrayColorSpace]](https://developer.apple.com/documentation/appkit/nscolorspace/1644177-extendedgenericgamma22graycolors)Added NSColorSpace.extendedGenericGamma22GrayColorSpaceAdded [+[NSColorSpace extendedSRGBColorSpace]](https://developer.apple.com/documentation/appkit/nscolorspace/1644175-extendedsrgb)Added NSColorSpace.extendedSRGBColorSpaceAdded NSColorSpace.genericCMYKColorSpaceAdded NSColorSpace.genericGamma22GrayColorSpaceAdded NSColorSpace.genericGrayColorSpaceAdded NSColorSpace.genericRGBColorSpaceAdded NSColorSpace.sRGBColorSpaceAdded [NSCMYKColorSpaceModel](https://developer.apple.com/documentation/appkit/nscmykcolorspacemodel)Added #def NSCOLORSPACE_USE_CLASS_PROPERTIESAdded [NSColorSpaceModelCMYK](https://developer.apple.com/documentation/appkit/nscolorspacemodel/nscolorspacemodelcmyk)Added [NSColorSpaceModelDeviceN](https://developer.apple.com/documentation/appkit/nscolorspacemodel/nscolorspacemodeldevicen)Added [NSColorSpaceModelGray](https://developer.apple.com/documentation/appkit/nscolorspacemodel/nscolorspacemodelgray)Added [NSColorSpaceModelIndexed](https://developer.apple.com/documentation/appkit/nscolorspace/model/indexed)Added [NSColorSpaceModelLAB](https://developer.apple.com/documentation/appkit/nscolorspace/model/lab)Added [NSColorSpaceModelPatterned](https://developer.apple.com/documentation/appkit/nscolorspace/model/patterned)Added [NSColorSpaceModelRGB](https://developer.apple.com/documentation/appkit/nscolorspacemodel/nscolorspacemodelrgb)Added [NSColorSpaceModelUnknown](https://developer.apple.com/documentation/appkit/nscolorspace/model/unknown)Added [NSDeviceNColorSpaceModel](https://developer.apple.com/documentation/appkit/nsdevicencolorspacemodel)Added [NSGrayColorSpaceModel](https://developer.apple.com/documentation/appkit/nsgraycolorspacemodel)Added [NSIndexedColorSpaceModel](https://developer.apple.com/documentation/appkit/nsindexedcolorspacemodel)Added [NSLABColorSpaceModel](https://developer.apple.com/documentation/appkit/nslabcolorspacemodel)Added [NSPatternColorSpaceModel](https://developer.apple.com/documentation/appkit/nspatterncolorspacemodel)Added [NSRGBColorSpaceModel](https://developer.apple.com/documentation/appkit/nsrgbcolorspacemodel)Added [NSUnknownColorSpaceModel](https://developer.apple.com/documentation/appkit/nsunknowncolorspacemodel)

#### NSComboBox.h

Removed -[NSComboBox setDelegate:]Modified [NSComboBox.delegate](https://developer.apple.com/documentation/appkit/nscombobox/1436697-delegate)

|  | Declaration |
| --- | --- |
| From | ``` - (id<NSComboBoxDelegate>)delegate ``` |
| To | ``` @property(assign) id<NSComboBoxDelegate> delegate ``` |

Modified [-[NSComboBoxDataSource comboBox:completedString:]](https://developer.apple.com/documentation/appkit/nscomboboxdatasource/1436733-combobox)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)comboBox:(NSComboBox *)aComboBox completedString:(NSString *)string ``` |
| To | ``` - (NSString *)comboBox:(NSComboBox *)comboBox completedString:(NSString *)string ``` |

Modified [-[NSComboBoxDataSource comboBox:indexOfItemWithStringValue:]](https://developer.apple.com/documentation/appkit/nscomboboxdatasource/1436713-combobox)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)comboBox:(NSComboBox *)aComboBox indexOfItemWithStringValue:(NSString *)string ``` |
| To | ``` - (NSUInteger)comboBox:(NSComboBox *)comboBox indexOfItemWithStringValue:(NSString *)string ``` |

Modified [-[NSComboBoxDataSource comboBox:objectValueForItemAtIndex:]](https://developer.apple.com/documentation/appkit/nscomboboxdatasource/1436753-combobox)

|  | Declaration |
| --- | --- |
| From | ``` - (id)comboBox:(NSComboBox *)aComboBox objectValueForItemAtIndex:(NSInteger)index ``` |
| To | ``` - (id)comboBox:(NSComboBox *)comboBox objectValueForItemAtIndex:(NSInteger)index ``` |

Modified [-[NSComboBoxDataSource numberOfItemsInComboBox:]](https://developer.apple.com/documentation/appkit/nscomboboxdatasource/1436780-numberofitems)

|  | Declaration |
| --- | --- |
| From | ``` - (NSInteger)numberOfItemsInComboBox:(NSComboBox *)aComboBox ``` |
| To | ``` - (NSInteger)numberOfItemsInComboBox:(NSComboBox *)comboBox ``` |

#### NSComboBoxCell.h

Modified [-[NSComboBoxCellDataSource comboBoxCell:completedString:]](https://developer.apple.com/documentation/appkit/nscomboboxcelldatasource/1410250-comboboxcell)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)comboBoxCell:(NSComboBoxCell *)aComboBoxCell completedString:(NSString *)uncompletedString ``` |
| To | ``` - (NSString *)comboBoxCell:(NSComboBoxCell *)comboBoxCell completedString:(NSString *)uncompletedString ``` |

Modified [-[NSComboBoxCellDataSource comboBoxCell:indexOfItemWithStringValue:]](https://developer.apple.com/documentation/appkit/nscomboboxcelldatasource/1410285-comboboxcell)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)comboBoxCell:(NSComboBoxCell *)aComboBoxCell indexOfItemWithStringValue:(NSString *)string ``` |
| To | ``` - (NSUInteger)comboBoxCell:(NSComboBoxCell *)comboBoxCell indexOfItemWithStringValue:(NSString *)string ``` |

Modified [-[NSComboBoxCellDataSource comboBoxCell:objectValueForItemAtIndex:]](https://developer.apple.com/documentation/appkit/nscomboboxcelldatasource/1410258-comboboxcell)

|  | Declaration |
| --- | --- |
| From | ``` - (id)comboBoxCell:(NSComboBoxCell *)aComboBoxCell objectValueForItemAtIndex:(NSInteger)index ``` |
| To | ``` - (id)comboBoxCell:(NSComboBoxCell *)comboBoxCell objectValueForItemAtIndex:(NSInteger)index ``` |

#### NSControl.h

Modified [-[NSControl drawCell:]](https://developer.apple.com/documentation/appkit/nscontrol/1428869-drawcell)

|  | Declaration |
| --- | --- |
| From | ``` - (void)drawCell:(NSCell *)aCell ``` |
| To | ``` - (void)drawCell:(NSCell *)cell ``` |

Modified [-[NSControl drawCellInside:]](https://developer.apple.com/documentation/appkit/nscontrol/1428881-drawcellinside)

|  | Declaration |
| --- | --- |
| From | ``` - (void)drawCellInside:(NSCell *)aCell ``` |
| To | ``` - (void)drawCellInside:(NSCell *)cell ``` |

Modified [-[NSControl editWithFrame:editor:delegate:event:]](https://developer.apple.com/documentation/appkit/nscontrol/1428919-edit)

|  | Declaration |
| --- | --- |
| From | ``` - (void)editWithFrame:(NSRect)aRect editor:(NSText *)textObj delegate:(id)anObject event:(NSEvent *)theEvent ``` |
| To | ``` - (void)editWithFrame:(NSRect)rect editor:(NSText *)textObj delegate:(id)delegate event:(NSEvent *)event ``` |

Modified [-[NSControl mouseDown:]](https://developer.apple.com/documentation/appkit/nscontrol/1428918-mousedown)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mouseDown:(NSEvent *)theEvent ``` |
| To | ``` - (void)mouseDown:(NSEvent *)event ``` |

Modified [-[NSControl selectCell:]](https://developer.apple.com/documentation/appkit/nscontrol/1428966-selectcell)

|  | Declaration |
| --- | --- |
| From | ``` - (void)selectCell:(NSCell *)aCell ``` |
| To | ``` - (void)selectCell:(NSCell *)cell ``` |

Modified [-[NSControl selectWithFrame:editor:delegate:start:length:]](https://developer.apple.com/documentation/appkit/nscontrol/1428968-selectwithframe)

|  | Declaration |
| --- | --- |
| From | ``` - (void)selectWithFrame:(NSRect)aRect editor:(NSText *)textObj delegate:(id)anObject start:(NSInteger)selStart length:(NSInteger)selLength ``` |
| To | ``` - (void)selectWithFrame:(NSRect)rect editor:(NSText *)textObj delegate:(id)delegate start:(NSInteger)selStart length:(NSInteger)selLength ``` |

Modified [-[NSControl sendAction:to:]](https://developer.apple.com/documentation/appkit/nscontrol/1428851-sendaction)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)sendAction:(SEL)theAction to:(id)theTarget ``` |
| To | ``` - (BOOL)sendAction:(SEL)action to:(id)target ``` |

Modified [-[NSControl sendActionOn:]](https://developer.apple.com/documentation/appkit/nscontrol/1428972-sendaction)

|  | Declaration |
| --- | --- |
| From | ``` - (NSInteger)sendActionOn:(NSInteger)mask ``` |
| To | ``` - (NSInteger)sendActionOn:(NSEventMask)mask ``` |

Modified [-[NSControl updateCell:]](https://developer.apple.com/documentation/appkit/nscontrol/1428893-updatecell)

|  | Declaration |
| --- | --- |
| From | ``` - (void)updateCell:(NSCell *)aCell ``` |
| To | ``` - (void)updateCell:(NSCell *)cell ``` |

Modified [-[NSControl updateCellInside:]](https://developer.apple.com/documentation/appkit/nscontrol/1428923-updatecellinside)

|  | Declaration |
| --- | --- |
| From | ``` - (void)updateCellInside:(NSCell *)aCell ``` |
| To | ``` - (void)updateCellInside:(NSCell *)cell ``` |

#### NSCursor.h

Added [-[NSCursor initWithCoder:]](https://developer.apple.com/documentation/appkit/nscursor/1640963-initwithcoder)Modified [-[NSCursor initWithImage:foregroundColorHint:backgroundColorHint:hotSpot:]](https://developer.apple.com/documentation/appkit/nscursor/1524604-initwithimage)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[NSCursor initWithImage:hotSpot:]](https://developer.apple.com/documentation/appkit/nscursor/1524612-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithImage:(NSImage *)newImage hotSpot:(NSPoint)aPoint ``` | -- |
| To | ``` - (instancetype)initWithImage:(NSImage *)newImage hotSpot:(NSPoint)point ``` | yes |

Modified [-[NSCursor mouseEntered:]](https://developer.apple.com/documentation/appkit/nscursor/1524582-mouseentered)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mouseEntered:(NSEvent *)theEvent ``` |
| To | ``` - (void)mouseEntered:(NSEvent *)event ``` |

Modified [-[NSCursor mouseExited:]](https://developer.apple.com/documentation/appkit/nscursor/1535790-mouseexited)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mouseExited:(NSEvent *)theEvent ``` |
| To | ``` - (void)mouseExited:(NSEvent *)event ``` |

#### NSCustomImageRep.h

Modified [-[NSCustomImageRep initWithDrawSelector:delegate:]](https://developer.apple.com/documentation/appkit/nscustomimagerep/1533328-initwithdrawselector)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithDrawSelector:(SEL)aMethod delegate:(id)anObject ``` |
| To | ``` - (instancetype)initWithDrawSelector:(SEL)selector delegate:(id)delegate ``` |

#### NSDatePickerCell.h

Added [-[NSDatePickerCell initTextCell:]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1643566-init)Added [-[NSDatePickerCell initWithCoder:]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1643567-init)Modified [-[NSDatePickerCellDelegate datePickerCell:validateProposedDateValue:timeInterval:]](https://developer.apple.com/documentation/appkit/nsdatepickercelldelegate/1459631-datepickercell)

|  | Declaration |
| --- | --- |
| From | ``` - (void)datePickerCell:(NSDatePickerCell *)aDatePickerCell validateProposedDateValue:(NSDate * _Nonnull *)proposedDateValue timeInterval:(NSTimeInterval *)proposedTimeInterval ``` |
| To | ``` - (void)datePickerCell:(NSDatePickerCell *)datePickerCell validateProposedDateValue:(NSDate * _Nonnull *)proposedDateValue timeInterval:(NSTimeInterval *)proposedTimeInterval ``` |

#### NSDocument.h

Added [NSDocument.browsingVersions](https://developer.apple.com/documentation/appkit/nsdocument/2177310-browsingversions)Added [-[NSDocument stopBrowsingVersionsWithCompletionHandler:]](https://developer.apple.com/documentation/appkit/nsdocument/2177312-stopbrowsingversions)Modified [NSDocument.displayName](https://developer.apple.com/documentation/appkit/nsdocument/1515077-displayname)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` @property(readonly, copy) NSString *displayName ``` | yes |
| To | ``` @property(copy) NSString *displayName ``` | -- |

Modified [-[NSDocument validateUserInterfaceItem:]](https://developer.apple.com/documentation/appkit/nsdocument/1515190-validateuserinterfaceitem)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)validateUserInterfaceItem:(id<NSValidatedUserInterfaceItem>)anItem ``` |
| To | ``` - (BOOL)validateUserInterfaceItem:(id<NSValidatedUserInterfaceItem>)item ``` |

#### NSDocumentController.h

Modified [-[NSDocumentController validateUserInterfaceItem:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514943-validateuserinterfaceitem)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)validateUserInterfaceItem:(id<NSValidatedUserInterfaceItem>)anItem ``` |
| To | ``` - (BOOL)validateUserInterfaceItem:(id<NSValidatedUserInterfaceItem>)item ``` |

#### NSDraggingItem.h

Modified [-[NSDraggingImageComponent initWithKey:]](https://developer.apple.com/documentation/appkit/nsdraggingimagecomponent/1534187-initwithkey)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDraggingItem initWithPasteboardWriter:]](https://developer.apple.com/documentation/appkit/nsdraggingitem/1535417-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### NSEvent.h

Removed [NSAlphaShiftKeyMask](https://developer.apple.com/documentation/appkit/nsalphashiftkeymask)Removed [NSAlternateKeyMask](https://developer.apple.com/documentation/appkit/nsalternatekeymask)Removed [NSAnyEventMask](https://developer.apple.com/documentation/appkit/nsanyeventmask)Removed [NSAppKitDefined](https://developer.apple.com/documentation/appkit/nsappkitdefined)Removed [NSAppKitDefinedMask](https://developer.apple.com/documentation/appkit/nsappkitdefinedmask)Removed [NSApplicationActivatedEventType](https://developer.apple.com/documentation/appkit/nsapplicationactivatedeventtype)Removed [NSApplicationDeactivatedEventType](https://developer.apple.com/documentation/appkit/nsapplicationdeactivatedeventtype)Removed [NSApplicationDefined](https://developer.apple.com/documentation/appkit/nsapplicationdefined)Removed [NSApplicationDefinedMask](https://developer.apple.com/documentation/appkit/nsapplicationdefinedmask)Removed [NSAWTEventType](https://developer.apple.com/documentation/appkit/nsawteventtype)Removed [NSCommandKeyMask](https://developer.apple.com/documentation/appkit/nscommandkeymask)Removed [NSControlKeyMask](https://developer.apple.com/documentation/appkit/nscontrolkeymask)Removed [NSCursorPointingDevice](https://developer.apple.com/documentation/appkit/nscursorpointingdevice)Removed [NSCursorUpdate](https://developer.apple.com/documentation/appkit/nscursorupdate)Removed [NSCursorUpdateMask](https://developer.apple.com/documentation/appkit/nscursorupdatemask)Removed [NSDeviceIndependentModifierFlagsMask](https://developer.apple.com/documentation/appkit/nsdeviceindependentmodifierflagsmask)Removed [NSEraserPointingDevice](https://developer.apple.com/documentation/appkit/nseraserpointingdevice)Removed [NSFlagsChanged](https://developer.apple.com/documentation/appkit/nsflagschanged)Removed [NSFlagsChangedMask](https://developer.apple.com/documentation/appkit/nsflagschangedmask)Removed [NSFunctionKeyMask](https://developer.apple.com/documentation/appkit/nsfunctionkeymask)Removed [NSHelpKeyMask](https://developer.apple.com/documentation/appkit/nshelpkeymask)Removed [NSKeyDown](https://developer.apple.com/documentation/appkit/nskeydown)Removed [NSKeyDownMask](https://developer.apple.com/documentation/appkit/nskeydownmask)Removed [NSKeyUp](https://developer.apple.com/documentation/appkit/nskeyup)Removed [NSKeyUpMask](https://developer.apple.com/documentation/appkit/nskeyupmask)Removed [NSLeftMouseDown](https://developer.apple.com/documentation/appkit/nsleftmousedown)Removed [NSLeftMouseDownMask](https://developer.apple.com/documentation/appkit/nsleftmousedownmask)Removed [NSLeftMouseDragged](https://developer.apple.com/documentation/appkit/nsleftmousedragged)Removed [NSLeftMouseDraggedMask](https://developer.apple.com/documentation/appkit/nsleftmousedraggedmask)Removed [NSLeftMouseUp](https://developer.apple.com/documentation/appkit/nsleftmouseup)Removed [NSLeftMouseUpMask](https://developer.apple.com/documentation/appkit/nsleftmouseupmask)Removed [NSMouseEntered](https://developer.apple.com/documentation/appkit/nsmouseentered)Removed [NSMouseEnteredMask](https://developer.apple.com/documentation/appkit/nsmouseenteredmask)Removed [NSMouseEventSubtype](https://developer.apple.com/documentation/appkit/nsmouseeventsubtype)Removed [NSMouseExited](https://developer.apple.com/documentation/appkit/nsmouseexited)Removed [NSMouseExitedMask](https://developer.apple.com/documentation/appkit/nsmouseexitedmask)Removed [NSMouseMoved](https://developer.apple.com/documentation/appkit/nsmousemoved)Removed [NSMouseMovedMask](https://developer.apple.com/documentation/appkit/nsmousemovedmask)Removed [NSNumericPadKeyMask](https://developer.apple.com/documentation/appkit/nsnumericpadkeymask)Removed [NSOtherMouseDown](https://developer.apple.com/documentation/appkit/nsothermousedown)Removed [NSOtherMouseDownMask](https://developer.apple.com/documentation/appkit/nsothermousedownmask)Removed [NSOtherMouseDragged](https://developer.apple.com/documentation/appkit/nsothermousedragged)Removed [NSOtherMouseDraggedMask](https://developer.apple.com/documentation/appkit/nsothermousedraggedmask)Removed [NSOtherMouseUp](https://developer.apple.com/documentation/appkit/nsothermouseup)Removed [NSOtherMouseUpMask](https://developer.apple.com/documentation/appkit/nsothermouseupmask)Removed [NSPenLowerSideMask](https://developer.apple.com/documentation/appkit/nspenlowersidemask)Removed [NSPenPointingDevice](https://developer.apple.com/documentation/appkit/nspenpointingdevice)Removed [NSPenTipMask](https://developer.apple.com/documentation/appkit/nspentipmask)Removed [NSPenUpperSideMask](https://developer.apple.com/documentation/appkit/nspenuppersidemask)Removed [NSPeriodic](https://developer.apple.com/documentation/appkit/nsperiodic)Removed [NSPeriodicMask](https://developer.apple.com/documentation/appkit/nsperiodicmask)Removed [NSPowerOffEventType](https://developer.apple.com/documentation/appkit/nspoweroffeventtype)Removed [NSRightMouseDown](https://developer.apple.com/documentation/appkit/nsrightmousedown)Removed [NSRightMouseDownMask](https://developer.apple.com/documentation/appkit/nsrightmousedownmask)Removed [NSRightMouseDragged](https://developer.apple.com/documentation/appkit/nsrightmousedragged)Removed [NSRightMouseDraggedMask](https://developer.apple.com/documentation/appkit/nsrightmousedraggedmask)Removed [NSRightMouseUp](https://developer.apple.com/documentation/appkit/nsrightmouseup)Removed [NSRightMouseUpMask](https://developer.apple.com/documentation/appkit/nsrightmouseupmask)Removed [NSScreenChangedEventType](https://developer.apple.com/documentation/appkit/nsscreenchangedeventtype)Removed [NSScrollWheel](https://developer.apple.com/documentation/appkit/nsscrollwheel)Removed [NSScrollWheelMask](https://developer.apple.com/documentation/appkit/nsscrollwheelmask)Removed [NSShiftKeyMask](https://developer.apple.com/documentation/appkit/nsshiftkeymask)Removed [NSSystemDefined](https://developer.apple.com/documentation/appkit/nssystemdefined)Removed [NSSystemDefinedMask](https://developer.apple.com/documentation/appkit/nssystemdefinedmask)Removed [NSTabletPoint](https://developer.apple.com/documentation/appkit/nstabletpoint)Removed [NSTabletPointEventSubtype](https://developer.apple.com/documentation/appkit/nstabletpointeventsubtype)Removed [NSTabletPointMask](https://developer.apple.com/documentation/appkit/nstabletpointmask)Removed [NSTabletProximity](https://developer.apple.com/documentation/appkit/nstabletproximity)Removed [NSTabletProximityEventSubtype](https://developer.apple.com/documentation/appkit/nstabletproximityeventsubtype)Removed [NSTabletProximityMask](https://developer.apple.com/documentation/appkit/nstabletproximitymask)Removed [NSTouchEventSubtype](https://developer.apple.com/documentation/appkit/nstoucheventsubtype)Removed [NSUnknownPointingDevice](https://developer.apple.com/documentation/appkit/nsunknownpointingdevice)Removed [NSWindowExposedEventType](https://developer.apple.com/documentation/appkit/nswindowexposedeventtype)Removed [NSWindowMovedEventType](https://developer.apple.com/documentation/appkit/nswindowmovedeventtype)Added [NSAlphaShiftKeyMask](https://developer.apple.com/documentation/appkit/nsalphashiftkeymask)Added [NSAlternateKeyMask](https://developer.apple.com/documentation/appkit/nsalternatekeymask)Added [NSAnyEventMask](https://developer.apple.com/documentation/appkit/nsanyeventmask)Added [NSAppKitDefined](https://developer.apple.com/documentation/appkit/nsappkitdefined)Added [NSAppKitDefinedMask](https://developer.apple.com/documentation/appkit/nsappkitdefinedmask)Added [NSApplicationActivatedEventType](https://developer.apple.com/documentation/appkit/nsapplicationactivatedeventtype)Added [NSApplicationDeactivatedEventType](https://developer.apple.com/documentation/appkit/nsapplicationdeactivatedeventtype)Added [NSApplicationDefined](https://developer.apple.com/documentation/appkit/nsapplicationdefined)Added [NSApplicationDefinedMask](https://developer.apple.com/documentation/appkit/nsapplicationdefinedmask)Added [NSAWTEventType](https://developer.apple.com/documentation/appkit/nsawteventtype)Added [NSCommandKeyMask](https://developer.apple.com/documentation/appkit/nscommandkeymask)Added [NSControlKeyMask](https://developer.apple.com/documentation/appkit/nscontrolkeymask)Added [NSCursorPointingDevice](https://developer.apple.com/documentation/appkit/nscursorpointingdevice)Added [NSCursorUpdate](https://developer.apple.com/documentation/appkit/nscursorupdate)Added [NSCursorUpdateMask](https://developer.apple.com/documentation/appkit/nscursorupdatemask)Added [NSDeviceIndependentModifierFlagsMask](https://developer.apple.com/documentation/appkit/nsdeviceindependentmodifierflagsmask)Added [NSEraserPointingDevice](https://developer.apple.com/documentation/appkit/nseraserpointingdevice)Added [NSEventButtonMaskPenLowerSide](https://developer.apple.com/documentation/appkit/nsevent/buttonmask/1642488-penlowerside)Added [NSEventButtonMaskPenTip](https://developer.apple.com/documentation/appkit/nsevent/buttonmask/1642457-pentip)Added [NSEventButtonMaskPenUpperSide](https://developer.apple.com/documentation/appkit/nseventbuttonmask/nseventbuttonmaskpenupperside)Added [NSEventMaskAny](https://developer.apple.com/documentation/appkit/nseventmask/nseventmaskany)Added [NSEventMaskAppKitDefined](https://developer.apple.com/documentation/appkit/nsevent/eventtypemask/1642410-appkitdefined)Added [NSEventMaskApplicationDefined](https://developer.apple.com/documentation/appkit/nseventmask/nseventmaskapplicationdefined)Added [NSEventMaskCursorUpdate](https://developer.apple.com/documentation/appkit/nseventmask/nseventmaskcursorupdate)Added [NSEventMaskFlagsChanged](https://developer.apple.com/documentation/appkit/nseventmask/nseventmaskflagschanged)Added [NSEventMaskKeyDown](https://developer.apple.com/documentation/appkit/nseventmask/nseventmaskkeydown)Added [NSEventMaskKeyUp](https://developer.apple.com/documentation/appkit/nseventmask/nseventmaskkeyup)Added [NSEventMaskLeftMouseDown](https://developer.apple.com/documentation/appkit/nsevent/eventtypemask/1642496-leftmousedown)Added [NSEventMaskLeftMouseDragged](https://developer.apple.com/documentation/appkit/nseventmask/nseventmaskleftmousedragged)Added [NSEventMaskLeftMouseUp](https://developer.apple.com/documentation/appkit/nsevent/eventtypemask/1642432-leftmouseup)Added [NSEventMaskMouseEntered](https://developer.apple.com/documentation/appkit/nseventmask/nseventmaskmouseentered)Added [NSEventMaskMouseExited](https://developer.apple.com/documentation/appkit/nsevent/eventtypemask/1642420-mouseexited)Added [NSEventMaskMouseMoved](https://developer.apple.com/documentation/appkit/nsevent/eventtypemask/1642429-mousemoved)Added [NSEventMaskOtherMouseDown](https://developer.apple.com/documentation/appkit/nsevent/eventtypemask/1642455-othermousedown)Added [NSEventMaskOtherMouseDragged](https://developer.apple.com/documentation/appkit/nseventmask/nseventmaskothermousedragged)Added [NSEventMaskOtherMouseUp](https://developer.apple.com/documentation/appkit/nsevent/eventtypemask/1642451-othermouseup)Added [NSEventMaskPeriodic](https://developer.apple.com/documentation/appkit/nsevent/eventtypemask/1642445-periodic)Added [NSEventMaskRightMouseDown](https://developer.apple.com/documentation/appkit/nseventmask/nseventmaskrightmousedown)Added [NSEventMaskRightMouseDragged](https://developer.apple.com/documentation/appkit/nseventmask/nseventmaskrightmousedragged)Added [NSEventMaskRightMouseUp](https://developer.apple.com/documentation/appkit/nsevent/eventtypemask/1642401-rightmouseup)Added [NSEventMaskScrollWheel](https://developer.apple.com/documentation/appkit/nsevent/eventtypemask/1642414-scrollwheel)Added [NSEventMaskSystemDefined](https://developer.apple.com/documentation/appkit/nseventmask/nseventmasksystemdefined)Added [NSEventMaskTabletPoint](https://developer.apple.com/documentation/appkit/nseventmask/nseventmasktabletpoint)Added [NSEventMaskTabletProximity](https://developer.apple.com/documentation/appkit/nsevent/eventtypemask/1642454-tabletproximity)Added [NSEventModifierFlagCapsLock](https://developer.apple.com/documentation/appkit/nseventmodifierflags/nseventmodifierflagcapslock)Added [NSEventModifierFlagCommand](https://developer.apple.com/documentation/appkit/nseventmodifierflags/nseventmodifierflagcommand)Added [NSEventModifierFlagControl](https://developer.apple.com/documentation/appkit/nsevent/modifierflags/1642396-control)Added [NSEventModifierFlagDeviceIndependentFlagsMask](https://developer.apple.com/documentation/appkit/nseventmodifierflags/nseventmodifierflagdeviceindependentflagsmask)Added [NSEventModifierFlagFunction](https://developer.apple.com/documentation/appkit/nseventmodifierflags/nseventmodifierflagfunction)Added [NSEventModifierFlagHelp](https://developer.apple.com/documentation/appkit/nseventmodifierflags/nseventmodifierflaghelp)Added [NSEventModifierFlagNumericPad](https://developer.apple.com/documentation/appkit/nseventmodifierflags/nseventmodifierflagnumericpad)Added [NSEventModifierFlagOption](https://developer.apple.com/documentation/appkit/nsevent/modifierflags/1642431-option)Added [NSEventModifierFlagShift](https://developer.apple.com/documentation/appkit/nseventmodifierflags/nseventmodifierflagshift)Added [NSEventSubtypeApplicationActivated](https://developer.apple.com/documentation/appkit/nseventsubtype/nseventsubtypeapplicationactivated)Added [NSEventSubtypeApplicationDeactivated](https://developer.apple.com/documentation/appkit/nseventsubtype/nseventsubtypeapplicationdeactivated)Added [NSEventSubtypeMouseEvent](https://developer.apple.com/documentation/appkit/nsevent/eventsubtype/1642395-mouseevent)Added [NSEventSubtypePowerOff](https://developer.apple.com/documentation/appkit/nsevent/eventsubtype/1642495-poweroff)Added [NSEventSubtypeScreenChanged](https://developer.apple.com/documentation/appkit/nseventsubtype/nseventsubtypescreenchanged)Added [NSEventSubtypeTabletPoint](https://developer.apple.com/documentation/appkit/nsevent/eventsubtype/1642479-tabletpoint)Added [NSEventSubtypeTabletProximity](https://developer.apple.com/documentation/appkit/nseventsubtype/nseventsubtypetabletproximity)Added [NSEventSubtypeTouch](https://developer.apple.com/documentation/appkit/nsevent/eventsubtype/touch)Added [NSEventSubtypeWindowExposed](https://developer.apple.com/documentation/appkit/nsevent/eventsubtype/windowexposed)Added [NSEventSubtypeWindowMoved](https://developer.apple.com/documentation/appkit/nsevent/eventsubtype/windowmoved)Added [NSEventTypeAppKitDefined](https://developer.apple.com/documentation/appkit/nsevent/eventtype/appkitdefined)Added [NSEventTypeApplicationDefined](https://developer.apple.com/documentation/appkit/nseventtype/nseventtypeapplicationdefined)Added [NSEventTypeCursorUpdate](https://developer.apple.com/documentation/appkit/nsevent/eventtype/cursorupdate)Added [NSEventTypeFlagsChanged](https://developer.apple.com/documentation/appkit/nsevent/eventtype/flagschanged)Added [NSEventTypeKeyDown](https://developer.apple.com/documentation/appkit/nsevent/eventtype/keydown)Added [NSEventTypeKeyUp](https://developer.apple.com/documentation/appkit/nsevent/eventtype/keyup)Added [NSEventTypeLeftMouseDown](https://developer.apple.com/documentation/appkit/nsevent/eventtype/leftmousedown)Added [NSEventTypeLeftMouseDragged](https://developer.apple.com/documentation/appkit/nsevent/eventtype/leftmousedragged)Added [NSEventTypeLeftMouseUp](https://developer.apple.com/documentation/appkit/nseventtype/nseventtypeleftmouseup)Added [NSEventTypeMouseEntered](https://developer.apple.com/documentation/appkit/nsevent/eventtype/mouseentered)Added [NSEventTypeMouseExited](https://developer.apple.com/documentation/appkit/nsevent/eventtype/mouseexited)Added [NSEventTypeMouseMoved](https://developer.apple.com/documentation/appkit/nsevent/eventtype/mousemoved)Added [NSEventTypeOtherMouseDown](https://developer.apple.com/documentation/appkit/nsevent/eventtype/othermousedown)Added [NSEventTypeOtherMouseDragged](https://developer.apple.com/documentation/appkit/nseventtype/nseventtypeothermousedragged)Added [NSEventTypeOtherMouseUp](https://developer.apple.com/documentation/appkit/nseventtype/nseventtypeothermouseup)Added [NSEventTypePeriodic](https://developer.apple.com/documentation/appkit/nsevent/eventtype/periodic)Added [NSEventTypeRightMouseDown](https://developer.apple.com/documentation/appkit/nsevent/eventtype/rightmousedown)Added [NSEventTypeRightMouseDragged](https://developer.apple.com/documentation/appkit/nseventtype/nseventtyperightmousedragged)Added [NSEventTypeRightMouseUp](https://developer.apple.com/documentation/appkit/nseventtype/nseventtyperightmouseup)Added [NSEventTypeScrollWheel](https://developer.apple.com/documentation/appkit/nsevent/eventtype/scrollwheel)Added [NSEventTypeSystemDefined](https://developer.apple.com/documentation/appkit/nsevent/eventtype/systemdefined)Added [NSEventTypeTabletPoint](https://developer.apple.com/documentation/appkit/nseventtype/nseventtypetabletpoint)Added [NSEventTypeTabletProximity](https://developer.apple.com/documentation/appkit/nseventtype/nseventtypetabletproximity)Added [NSFlagsChanged](https://developer.apple.com/documentation/appkit/nsflagschanged)Added [NSFlagsChangedMask](https://developer.apple.com/documentation/appkit/nsflagschangedmask)Added [NSFunctionKeyMask](https://developer.apple.com/documentation/appkit/nsfunctionkeymask)Added [NSHelpKeyMask](https://developer.apple.com/documentation/appkit/nshelpkeymask)Added [NSKeyDown](https://developer.apple.com/documentation/appkit/nskeydown)Added [NSKeyDownMask](https://developer.apple.com/documentation/appkit/nskeydownmask)Added [NSKeyUp](https://developer.apple.com/documentation/appkit/nskeyup)Added [NSKeyUpMask](https://developer.apple.com/documentation/appkit/nskeyupmask)Added [NSLeftMouseDown](https://developer.apple.com/documentation/appkit/nsleftmousedown)Added [NSLeftMouseDownMask](https://developer.apple.com/documentation/appkit/nsleftmousedownmask)Added [NSLeftMouseDragged](https://developer.apple.com/documentation/appkit/nsleftmousedragged)Added [NSLeftMouseDraggedMask](https://developer.apple.com/documentation/appkit/nsleftmousedraggedmask)Added [NSLeftMouseUp](https://developer.apple.com/documentation/appkit/nsleftmouseup)Added [NSLeftMouseUpMask](https://developer.apple.com/documentation/appkit/nsleftmouseupmask)Added [NSMouseEntered](https://developer.apple.com/documentation/appkit/nsmouseentered)Added [NSMouseEnteredMask](https://developer.apple.com/documentation/appkit/nsmouseenteredmask)Added [NSMouseEventSubtype](https://developer.apple.com/documentation/appkit/nsmouseeventsubtype)Added [NSMouseExited](https://developer.apple.com/documentation/appkit/nsmouseexited)Added [NSMouseExitedMask](https://developer.apple.com/documentation/appkit/nsmouseexitedmask)Added [NSMouseMoved](https://developer.apple.com/documentation/appkit/nsmousemoved)Added [NSMouseMovedMask](https://developer.apple.com/documentation/appkit/nsmousemovedmask)Added [NSNumericPadKeyMask](https://developer.apple.com/documentation/appkit/nsnumericpadkeymask)Added [NSOtherMouseDown](https://developer.apple.com/documentation/appkit/nsothermousedown)Added [NSOtherMouseDownMask](https://developer.apple.com/documentation/appkit/nsothermousedownmask)Added [NSOtherMouseDragged](https://developer.apple.com/documentation/appkit/nsothermousedragged)Added [NSOtherMouseDraggedMask](https://developer.apple.com/documentation/appkit/nsothermousedraggedmask)Added [NSOtherMouseUp](https://developer.apple.com/documentation/appkit/nsothermouseup)Added [NSOtherMouseUpMask](https://developer.apple.com/documentation/appkit/nsothermouseupmask)Added [NSPenLowerSideMask](https://developer.apple.com/documentation/appkit/nspenlowersidemask)Added [NSPenPointingDevice](https://developer.apple.com/documentation/appkit/nspenpointingdevice)Added [NSPenTipMask](https://developer.apple.com/documentation/appkit/nspentipmask)Added [NSPenUpperSideMask](https://developer.apple.com/documentation/appkit/nspenuppersidemask)Added [NSPeriodic](https://developer.apple.com/documentation/appkit/nsperiodic)Added [NSPeriodicMask](https://developer.apple.com/documentation/appkit/nsperiodicmask)Added [NSPointingDeviceTypeCursor](https://developer.apple.com/documentation/appkit/nsevent/pointingdevicetype/cursor)Added [NSPointingDeviceTypeEraser](https://developer.apple.com/documentation/appkit/nsevent/pointingdevicetype/eraser)Added [NSPointingDeviceTypePen](https://developer.apple.com/documentation/appkit/nspointingdevicetype/nspointingdevicetypepen)Added [NSPointingDeviceTypeUnknown](https://developer.apple.com/documentation/appkit/nsevent/pointingdevicetype/unknown)Added [NSPowerOffEventType](https://developer.apple.com/documentation/appkit/nspoweroffeventtype)Added [NSRightMouseDown](https://developer.apple.com/documentation/appkit/nsrightmousedown)Added [NSRightMouseDownMask](https://developer.apple.com/documentation/appkit/nsrightmousedownmask)Added [NSRightMouseDragged](https://developer.apple.com/documentation/appkit/nsrightmousedragged)Added [NSRightMouseDraggedMask](https://developer.apple.com/documentation/appkit/nsrightmousedraggedmask)Added [NSRightMouseUp](https://developer.apple.com/documentation/appkit/nsrightmouseup)Added [NSRightMouseUpMask](https://developer.apple.com/documentation/appkit/nsrightmouseupmask)Added [NSScreenChangedEventType](https://developer.apple.com/documentation/appkit/nsscreenchangedeventtype)Added [NSScrollWheel](https://developer.apple.com/documentation/appkit/nsscrollwheel)Added [NSScrollWheelMask](https://developer.apple.com/documentation/appkit/nsscrollwheelmask)Added [NSShiftKeyMask](https://developer.apple.com/documentation/appkit/nsshiftkeymask)Added [NSSystemDefined](https://developer.apple.com/documentation/appkit/nssystemdefined)Added [NSSystemDefinedMask](https://developer.apple.com/documentation/appkit/nssystemdefinedmask)Added [NSTabletPoint](https://developer.apple.com/documentation/appkit/nstabletpoint)Added [NSTabletPointEventSubtype](https://developer.apple.com/documentation/appkit/nstabletpointeventsubtype)Added [NSTabletPointMask](https://developer.apple.com/documentation/appkit/nstabletpointmask)Added [NSTabletProximity](https://developer.apple.com/documentation/appkit/nstabletproximity)Added [NSTabletProximityEventSubtype](https://developer.apple.com/documentation/appkit/nstabletproximityeventsubtype)Added [NSTabletProximityMask](https://developer.apple.com/documentation/appkit/nstabletproximitymask)Added [NSTouchEventSubtype](https://developer.apple.com/documentation/appkit/nstoucheventsubtype)Added [NSUnknownPointingDevice](https://developer.apple.com/documentation/appkit/nsunknownpointingdevice)Added [NSWindowExposedEventType](https://developer.apple.com/documentation/appkit/nswindowexposedeventtype)Added [NSWindowMovedEventType](https://developer.apple.com/documentation/appkit/nswindowmovedeventtype)Modified [NSEvent.context](https://developer.apple.com/documentation/appkit/nsevent/1524291-context)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [+[NSEvent enterExitEventWithType:location:modifierFlags:timestamp:windowNumber:context:eventNumber:trackingNumber:userData:]](https://developer.apple.com/documentation/appkit/nsevent/1535383-enterexiteventwithtype)

|  | Declaration |
| --- | --- |
| From | ``` + (NSEvent *)enterExitEventWithType:(NSEventType)type location:(NSPoint)location modifierFlags:(NSEventModifierFlags)flags timestamp:(NSTimeInterval)time windowNumber:(NSInteger)wNum context:(NSGraphicsContext *)context eventNumber:(NSInteger)eNum trackingNumber:(NSInteger)tNum userData:(void *)data ``` |
| To | ``` + (NSEvent *)enterExitEventWithType:(NSEventType)type location:(NSPoint)location modifierFlags:(NSEventModifierFlags)flags timestamp:(NSTimeInterval)time windowNumber:(NSInteger)wNum context:(NSGraphicsContext *)unusedPassNil eventNumber:(NSInteger)eNum trackingNumber:(NSInteger)tNum userData:(void *)data ``` |

Modified [+[NSEvent keyEventWithType:location:modifierFlags:timestamp:windowNumber:context:characters:charactersIgnoringModifiers:isARepeat:keyCode:]](https://developer.apple.com/documentation/appkit/nsevent/1533943-keyeventwithtype)

|  | Declaration |
| --- | --- |
| From | ``` + (NSEvent *)keyEventWithType:(NSEventType)type location:(NSPoint)location modifierFlags:(NSEventModifierFlags)flags timestamp:(NSTimeInterval)time windowNumber:(NSInteger)wNum context:(NSGraphicsContext *)context characters:(NSString *)keys charactersIgnoringModifiers:(NSString *)ukeys isARepeat:(BOOL)flag keyCode:(unsigned short)code ``` |
| To | ``` + (NSEvent *)keyEventWithType:(NSEventType)type location:(NSPoint)location modifierFlags:(NSEventModifierFlags)flags timestamp:(NSTimeInterval)time windowNumber:(NSInteger)wNum context:(NSGraphicsContext *)unusedPassNil characters:(NSString *)keys charactersIgnoringModifiers:(NSString *)ukeys isARepeat:(BOOL)flag keyCode:(unsigned short)code ``` |

Modified [+[NSEvent mouseEventWithType:location:modifierFlags:timestamp:windowNumber:context:eventNumber:clickCount:pressure:]](https://developer.apple.com/documentation/appkit/nsevent/1532495-mouseeventwithtype)

|  | Declaration |
| --- | --- |
| From | ``` + (NSEvent *)mouseEventWithType:(NSEventType)type location:(NSPoint)location modifierFlags:(NSEventModifierFlags)flags timestamp:(NSTimeInterval)time windowNumber:(NSInteger)wNum context:(NSGraphicsContext *)context eventNumber:(NSInteger)eNum clickCount:(NSInteger)cNum pressure:(float)pressure ``` |
| To | ``` + (NSEvent *)mouseEventWithType:(NSEventType)type location:(NSPoint)location modifierFlags:(NSEventModifierFlags)flags timestamp:(NSTimeInterval)time windowNumber:(NSInteger)wNum context:(NSGraphicsContext *)unusedPassNil eventNumber:(NSInteger)eNum clickCount:(NSInteger)cNum pressure:(float)pressure ``` |

Modified [+[NSEvent otherEventWithType:location:modifierFlags:timestamp:windowNumber:context:subtype:data1:data2:]](https://developer.apple.com/documentation/appkit/nsevent/1530010-othereventwithtype)

|  | Declaration |
| --- | --- |
| From | ``` + (NSEvent *)otherEventWithType:(NSEventType)type location:(NSPoint)location modifierFlags:(NSEventModifierFlags)flags timestamp:(NSTimeInterval)time windowNumber:(NSInteger)wNum context:(NSGraphicsContext *)context subtype:(short)subtype data1:(NSInteger)d1 data2:(NSInteger)d2 ``` |
| To | ``` + (NSEvent *)otherEventWithType:(NSEventType)type location:(NSPoint)location modifierFlags:(NSEventModifierFlags)flags timestamp:(NSTimeInterval)time windowNumber:(NSInteger)wNum context:(NSGraphicsContext *)unusedPassNil subtype:(short)subtype data1:(NSInteger)d1 data2:(NSInteger)d2 ``` |

#### NSFilePromiseProvider.h (Added)

Added [NSFilePromiseProvider](https://developer.apple.com/documentation/appkit/nsfilepromiseprovider)Added [NSFilePromiseProvider.delegate](https://developer.apple.com/documentation/appkit/nsfilepromiseprovider/1644726-delegate)Added [NSFilePromiseProvider.fileType](https://developer.apple.com/documentation/appkit/nsfilepromiseprovider/1644738-filetype)Added [-[NSFilePromiseProvider init]](https://developer.apple.com/documentation/appkit/nsfilepromiseprovider/1644655-init)Added [-[NSFilePromiseProvider initWithFileType:delegate:]](https://developer.apple.com/documentation/appkit/nsfilepromiseprovider/1644594-initwithfiletype)Added [NSFilePromiseProvider.userInfo](https://developer.apple.com/documentation/appkit/nsfilepromiseprovider/1644255-userinfo)Added [NSFilePromiseProviderDelegate](https://developer.apple.com/documentation/appkit/nsfilepromiseproviderdelegate)Added [-[NSFilePromiseProviderDelegate filePromiseProvider:fileNameForType:]](https://developer.apple.com/documentation/appkit/nsfilepromiseproviderdelegate/2369278-filepromiseprovider)Added [-[NSFilePromiseProviderDelegate filePromiseProvider:writePromiseToURL:completionHandler:]](https://developer.apple.com/documentation/appkit/nsfilepromiseproviderdelegate/1644244-filepromiseprovider)Added [-[NSFilePromiseProviderDelegate operationQueueForFilePromiseProvider:]](https://developer.apple.com/documentation/appkit/nsfilepromiseproviderdelegate/2369279-operationqueue)

#### NSFilePromiseReceiver.h (Added)

Added [NSFilePromiseReceiver](https://developer.apple.com/documentation/appkit/nsfilepromisereceiver)Added [NSFilePromiseReceiver.fileNames](https://developer.apple.com/documentation/appkit/nsfilepromisereceiver/1642142-filenames)Added [NSFilePromiseReceiver.fileTypes](https://developer.apple.com/documentation/appkit/nsfilepromisereceiver/1642141-filetypes)Added [+[NSFilePromiseReceiver readableDraggedTypes]](https://developer.apple.com/documentation/appkit/nsfilepromisereceiver/1642140-readabledraggedtypes)Added [-[NSFilePromiseReceiver receivePromisedFilesAtDestination:options:operationQueue:reader:]](https://developer.apple.com/documentation/appkit/nsfilepromisereceiver/1642138-receivepromisedfiles)

#### NSFont.h

Modified [-[NSFont advancementForGlyph:]](https://developer.apple.com/documentation/appkit/nsfont/1531555-advancement)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSize)advancementForGlyph:(NSGlyph)ag ``` |
| To | ``` - (NSSize)advancementForGlyph:(NSGlyph)glyph ``` |

Modified [-[NSFont boundingRectForGlyph:]](https://developer.apple.com/documentation/appkit/nsfont/1533748-boundingrectforglyph)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)boundingRectForGlyph:(NSGlyph)aGlyph ``` |
| To | ``` - (NSRect)boundingRectForGlyph:(NSGlyph)glyph ``` |

Modified -[NSFont glyphIsEncoded:]

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)glyphIsEncoded:(NSGlyph)aGlyph ``` |
| To | ``` - (BOOL)glyphIsEncoded:(NSGlyph)glyph ``` |

Modified [-[NSFont glyphWithName:]](https://developer.apple.com/documentation/appkit/nsfont/1530847-glyphwithname)

|  | Declaration |
| --- | --- |
| From | ``` - (NSGlyph)glyphWithName:(NSString *)aName ``` |
| To | ``` - (NSGlyph)glyphWithName:(NSString *)name ``` |

Modified -[NSFont positionOfGlyph:forCharacter:struckOverRect:]

|  | Declaration |
| --- | --- |
| From | ``` - (NSPoint)positionOfGlyph:(NSGlyph)aGlyph forCharacter:(unichar)aChar struckOverRect:(NSRect)aRect ``` |
| To | ``` - (NSPoint)positionOfGlyph:(NSGlyph)glyph forCharacter:(unichar)character struckOverRect:(NSRect)rect ``` |

Modified -[NSFont positionOfGlyph:precededByGlyph:isNominal:]

|  | Declaration |
| --- | --- |
| From | ``` - (NSPoint)positionOfGlyph:(NSGlyph)curGlyph precededByGlyph:(NSGlyph)prevGlyph isNominal:(BOOL *)nominal ``` |
| To | ``` - (NSPoint)positionOfGlyph:(NSGlyph)glyph precededByGlyph:(NSGlyph)prevGlyph isNominal:(BOOL *)nominal ``` |

Modified -[NSFont positionOfGlyph:struckOverGlyph:metricsExist:]

|  | Declaration |
| --- | --- |
| From | ``` - (NSPoint)positionOfGlyph:(NSGlyph)curGlyph struckOverGlyph:(NSGlyph)prevGlyph metricsExist:(BOOL *)exist ``` |
| To | ``` - (NSPoint)positionOfGlyph:(NSGlyph)glyph struckOverGlyph:(NSGlyph)prevGlyph metricsExist:(BOOL *)exist ``` |

Modified -[NSFont positionOfGlyph:struckOverRect:metricsExist:]

|  | Declaration |
| --- | --- |
| From | ``` - (NSPoint)positionOfGlyph:(NSGlyph)aGlyph struckOverRect:(NSRect)aRect metricsExist:(BOOL *)exist ``` |
| To | ``` - (NSPoint)positionOfGlyph:(NSGlyph)glyph struckOverRect:(NSRect)rect metricsExist:(BOOL *)exist ``` |

Modified [+[NSFont setUserFixedPitchFont:]](https://developer.apple.com/documentation/appkit/nsfont/1529050-setuserfixedpitch)

|  | Declaration |
| --- | --- |
| From | ``` + (void)setUserFixedPitchFont:(NSFont *)aFont ``` |
| To | ``` + (void)setUserFixedPitchFont:(NSFont *)font ``` |

Modified [+[NSFont setUserFont:]](https://developer.apple.com/documentation/appkit/nsfont/1526068-setuserfont)

|  | Declaration |
| --- | --- |
| From | ``` + (void)setUserFont:(NSFont *)aFont ``` |
| To | ``` + (void)setUserFont:(NSFont *)font ``` |

#### NSFontDescriptor.h

Modified [-[NSFontDescriptor objectForKey:]](https://developer.apple.com/documentation/appkit/nsfontdescriptor/1469837-objectforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (id)objectForKey:(NSString *)anAttribute ``` |
| To | ``` - (id)objectForKey:(NSString *)attribute ``` |

#### NSForm.h

Modified [-[NSForm indexOfCellWithTag:]](https://developer.apple.com/documentation/appkit/nsform/1524629-indexofcell)

|  | Declaration |
| --- | --- |
| From | ``` - (NSInteger)indexOfCellWithTag:(NSInteger)aTag ``` |
| To | ``` - (NSInteger)indexOfCellWithTag:(NSInteger)tag ``` |

#### NSFormCell.h

Added [-[NSFormCell initWithCoder:]](https://developer.apple.com/documentation/appkit/nsformcell/1643347-initwithcoder)Modified [-[NSFormCell initTextCell:]](https://developer.apple.com/documentation/appkit/nsformcell/1526669-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initTextCell:(NSString *)aString ``` | -- |
| To | ``` - (instancetype)initTextCell:(NSString *)string ``` | yes |

Modified [-[NSFormCell titleWidth:]](https://developer.apple.com/documentation/appkit/nsformcell/1526921-titlewidth)

|  | Declaration |
| --- | --- |
| From | ``` - (CGFloat)titleWidth:(NSSize)aSize ``` |
| To | ``` - (CGFloat)titleWidth:(NSSize)size ``` |

#### NSGlyphInfo.h

Modified [+[NSGlyphInfo glyphInfoWithCharacterIdentifier:collection:baseString:]](https://developer.apple.com/documentation/appkit/nsglyphinfo/1447116-glyphinfowithcharacteridentifier)

|  | Declaration |
| --- | --- |
| From | ``` + (NSGlyphInfo *)glyphInfoWithCharacterIdentifier:(NSUInteger)cid collection:(NSCharacterCollection)characterCollection baseString:(NSString *)theString ``` |
| To | ``` + (NSGlyphInfo *)glyphInfoWithCharacterIdentifier:(NSUInteger)cid collection:(NSCharacterCollection)characterCollection baseString:(NSString *)string ``` |

Modified [+[NSGlyphInfo glyphInfoWithGlyph:forFont:baseString:]](https://developer.apple.com/documentation/appkit/nsglyphinfo/1447124-init)

|  | Declaration |
| --- | --- |
| From | ``` + (NSGlyphInfo *)glyphInfoWithGlyph:(NSGlyph)glyph forFont:(NSFont *)font baseString:(NSString *)theString ``` |
| To | ``` + (NSGlyphInfo *)glyphInfoWithGlyph:(NSGlyph)glyph forFont:(NSFont *)font baseString:(NSString *)string ``` |

Modified [+[NSGlyphInfo glyphInfoWithGlyphName:forFont:baseString:]](https://developer.apple.com/documentation/appkit/nsglyphinfo/1447118-glyphinfowithglyphname)

|  | Declaration |
| --- | --- |
| From | ``` + (NSGlyphInfo *)glyphInfoWithGlyphName:(NSString *)glyphName forFont:(NSFont *)font baseString:(NSString *)theString ``` |
| To | ``` + (NSGlyphInfo *)glyphInfoWithGlyphName:(NSString *)glyphName forFont:(NSFont *)font baseString:(NSString *)string ``` |

#### NSGradient.h

Added [-[NSGradient initWithCoder:]](https://developer.apple.com/documentation/appkit/nsgradient/1644700-init)Modified [-[NSGradient initWithColors:atLocations:colorSpace:]](https://developer.apple.com/documentation/appkit/nsgradient/1524459-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### NSGraphics.h

Removed [NSCompositeClear](https://developer.apple.com/documentation/appkit/nscompositeclear)Removed [NSCompositeColor](https://developer.apple.com/documentation/appkit/nscompositecolor)Removed [NSCompositeColorBurn](https://developer.apple.com/documentation/appkit/nscompositecolorburn)Removed [NSCompositeColorDodge](https://developer.apple.com/documentation/appkit/nscompositecolordodge)Removed [NSCompositeCopy](https://developer.apple.com/documentation/appkit/nscompositecopy)Removed [NSCompositeDarken](https://developer.apple.com/documentation/appkit/nscompositedarken)Removed [NSCompositeDestinationAtop](https://developer.apple.com/documentation/appkit/nscompositedestinationatop)Removed [NSCompositeDestinationIn](https://developer.apple.com/documentation/appkit/nscompositedestinationin)Removed [NSCompositeDestinationOut](https://developer.apple.com/documentation/appkit/nscompositedestinationout)Removed [NSCompositeDestinationOver](https://developer.apple.com/documentation/appkit/nscompositedestinationover)Removed [NSCompositeDifference](https://developer.apple.com/documentation/appkit/nscompositedifference)Removed [NSCompositeExclusion](https://developer.apple.com/documentation/appkit/nscompositeexclusion)Removed [NSCompositeHardLight](https://developer.apple.com/documentation/appkit/nscompositehardlight)Removed [NSCompositeHighlight](https://developer.apple.com/documentation/appkit/nscompositehighlight)Removed [NSCompositeHue](https://developer.apple.com/documentation/appkit/nscompositehue)Removed [NSCompositeLighten](https://developer.apple.com/documentation/appkit/nscompositelighten)Removed [NSCompositeLuminosity](https://developer.apple.com/documentation/appkit/nscompositeluminosity)Removed [NSCompositeMultiply](https://developer.apple.com/documentation/appkit/nscompositemultiply)Removed [NSCompositeOverlay](https://developer.apple.com/documentation/appkit/nscompositeoverlay)Removed [NSCompositePlusDarker](https://developer.apple.com/documentation/appkit/nscompositeplusdarker)Removed [NSCompositePlusLighter](https://developer.apple.com/documentation/appkit/nscompositepluslighter)Removed [NSCompositeSaturation](https://developer.apple.com/documentation/appkit/nscompositesaturation)Removed [NSCompositeScreen](https://developer.apple.com/documentation/appkit/nscompositescreen)Removed [NSCompositeSoftLight](https://developer.apple.com/documentation/appkit/nscompositesoftlight)Removed [NSCompositeSourceAtop](https://developer.apple.com/documentation/appkit/nscompositesourceatop)Removed [NSCompositeSourceIn](https://developer.apple.com/documentation/appkit/nscompositesourcein)Removed [NSCompositeSourceOut](https://developer.apple.com/documentation/appkit/nscompositesourceout)Removed [NSCompositeSourceOver](https://developer.apple.com/documentation/appkit/nscompositesourceover)Removed [NSCompositeXOR](https://developer.apple.com/documentation/appkit/nscompositexor)Added [NSCompositeClear](https://developer.apple.com/documentation/appkit/nscompositeclear)Added [NSCompositeColor](https://developer.apple.com/documentation/appkit/nscompositecolor)Added [NSCompositeColorBurn](https://developer.apple.com/documentation/appkit/nscompositecolorburn)Added [NSCompositeColorDodge](https://developer.apple.com/documentation/appkit/nscompositecolordodge)Added [NSCompositeCopy](https://developer.apple.com/documentation/appkit/nscompositecopy)Added [NSCompositeDarken](https://developer.apple.com/documentation/appkit/nscompositedarken)Added [NSCompositeDestinationAtop](https://developer.apple.com/documentation/appkit/nscompositedestinationatop)Added [NSCompositeDestinationIn](https://developer.apple.com/documentation/appkit/nscompositedestinationin)Added [NSCompositeDestinationOut](https://developer.apple.com/documentation/appkit/nscompositedestinationout)Added [NSCompositeDestinationOver](https://developer.apple.com/documentation/appkit/nscompositedestinationover)Added [NSCompositeDifference](https://developer.apple.com/documentation/appkit/nscompositedifference)Added [NSCompositeExclusion](https://developer.apple.com/documentation/appkit/nscompositeexclusion)Added [NSCompositeHardLight](https://developer.apple.com/documentation/appkit/nscompositehardlight)Added [NSCompositeHighlight](https://developer.apple.com/documentation/appkit/nscompositehighlight)Added [NSCompositeHue](https://developer.apple.com/documentation/appkit/nscompositehue)Added [NSCompositeLighten](https://developer.apple.com/documentation/appkit/nscompositelighten)Added [NSCompositeLuminosity](https://developer.apple.com/documentation/appkit/nscompositeluminosity)Added [NSCompositeMultiply](https://developer.apple.com/documentation/appkit/nscompositemultiply)Added [NSCompositeOverlay](https://developer.apple.com/documentation/appkit/nscompositeoverlay)Added [NSCompositePlusDarker](https://developer.apple.com/documentation/appkit/nscompositeplusdarker)Added [NSCompositePlusLighter](https://developer.apple.com/documentation/appkit/nscompositepluslighter)Added [NSCompositeSaturation](https://developer.apple.com/documentation/appkit/nscompositesaturation)Added [NSCompositeScreen](https://developer.apple.com/documentation/appkit/nscompositescreen)Added [NSCompositeSoftLight](https://developer.apple.com/documentation/appkit/nscompositesoftlight)Added [NSCompositeSourceAtop](https://developer.apple.com/documentation/appkit/nscompositesourceatop)Added [NSCompositeSourceIn](https://developer.apple.com/documentation/appkit/nscompositesourcein)Added [NSCompositeSourceOut](https://developer.apple.com/documentation/appkit/nscompositesourceout)Added [NSCompositeSourceOver](https://developer.apple.com/documentation/appkit/nscompositesourceover)Added [NSCompositeXOR](https://developer.apple.com/documentation/appkit/nscompositexor)Added [NSCompositingOperationClear](https://developer.apple.com/documentation/appkit/nscompositingoperation/clear)Added [NSCompositingOperationColor](https://developer.apple.com/documentation/appkit/nscompositingoperation/nscompositingoperationcolor)Added [NSCompositingOperationColorBurn](https://developer.apple.com/documentation/appkit/nscompositingoperation/colorburn)Added [NSCompositingOperationColorDodge](https://developer.apple.com/documentation/appkit/nscompositingoperation/nscompositingoperationcolordodge)Added [NSCompositingOperationCopy](https://developer.apple.com/documentation/appkit/nscompositingoperation/copy)Added [NSCompositingOperationDarken](https://developer.apple.com/documentation/appkit/nscompositingoperation/darken)Added [NSCompositingOperationDestinationAtop](https://developer.apple.com/documentation/appkit/nscompositingoperation/destinationatop)Added [NSCompositingOperationDestinationIn](https://developer.apple.com/documentation/appkit/nscompositingoperation/destinationin)Added [NSCompositingOperationDestinationOut](https://developer.apple.com/documentation/appkit/nscompositingoperation/destinationout)Added [NSCompositingOperationDestinationOver](https://developer.apple.com/documentation/appkit/nscompositingoperation/destinationover)Added [NSCompositingOperationDifference](https://developer.apple.com/documentation/appkit/nscompositingoperation/difference)Added [NSCompositingOperationExclusion](https://developer.apple.com/documentation/appkit/nscompositingoperation/nscompositingoperationexclusion)Added [NSCompositingOperationHardLight](https://developer.apple.com/documentation/appkit/nscompositingoperation/nscompositingoperationhardlight)Added [NSCompositingOperationHighlight](https://developer.apple.com/documentation/appkit/nscompositingoperation/nscompositingoperationhighlight)Added [NSCompositingOperationHue](https://developer.apple.com/documentation/appkit/nscompositingoperation/nscompositingoperationhue)Added [NSCompositingOperationLighten](https://developer.apple.com/documentation/appkit/nscompositingoperation/nscompositingoperationlighten)Added [NSCompositingOperationLuminosity](https://developer.apple.com/documentation/appkit/nscompositingoperation/luminosity)Added [NSCompositingOperationMultiply](https://developer.apple.com/documentation/appkit/nscompositingoperation/multiply)Added [NSCompositingOperationOverlay](https://developer.apple.com/documentation/appkit/nscompositingoperation/overlay)Added [NSCompositingOperationPlusDarker](https://developer.apple.com/documentation/appkit/nscompositingoperation/nscompositingoperationplusdarker)Added [NSCompositingOperationPlusLighter](https://developer.apple.com/documentation/appkit/nscompositingoperation/pluslighter)Added [NSCompositingOperationSaturation](https://developer.apple.com/documentation/appkit/nscompositingoperation/saturation)Added [NSCompositingOperationScreen](https://developer.apple.com/documentation/appkit/nscompositingoperation/nscompositingoperationscreen)Added [NSCompositingOperationSoftLight](https://developer.apple.com/documentation/appkit/nscompositingoperation/softlight)Added [NSCompositingOperationSourceAtop](https://developer.apple.com/documentation/appkit/nscompositingoperation/nscompositingoperationsourceatop)Added [NSCompositingOperationSourceIn](https://developer.apple.com/documentation/appkit/nscompositingoperation/sourcein)Added [NSCompositingOperationSourceOut](https://developer.apple.com/documentation/appkit/nscompositingoperation/sourceout)Added [NSCompositingOperationSourceOver](https://developer.apple.com/documentation/appkit/nscompositingoperation/sourceover)Added [NSCompositingOperationXOR](https://developer.apple.com/documentation/appkit/nscompositingoperation/nscompositingoperationxor)Added [NSDisplayGamut](https://developer.apple.com/documentation/appkit/nsdisplaygamut)Added [NSDisplayGamutP3](https://developer.apple.com/documentation/appkit/nsdisplaygamut/p3)Added [NSDisplayGamutSRGB](https://developer.apple.com/documentation/appkit/nsdisplaygamut/nsdisplaygamutsrgb)Modified [NSDottedFrameRect()](https://developer.apple.com/documentation/appkit/1473658-nsdottedframerect)

|  | Declaration |
| --- | --- |
| From | ``` void NSDottedFrameRect (     NSRect aRect ); ``` |
| To | ``` void NSDottedFrameRect (     NSRect rect ); ``` |

Modified [NSDrawButton()](https://developer.apple.com/documentation/appkit/1473763-nsdrawbutton)

|  | Declaration |
| --- | --- |
| From | ``` void NSDrawButton (     NSRect aRect,     NSRect clipRect ); ``` |
| To | ``` void NSDrawButton (     NSRect rect,     NSRect clipRect ); ``` |

Modified [NSDrawDarkBezel()](https://developer.apple.com/documentation/appkit/1473771-nsdrawdarkbezel)

|  | Declaration |
| --- | --- |
| From | ``` void NSDrawDarkBezel (     NSRect aRect,     NSRect clipRect ); ``` |
| To | ``` void NSDrawDarkBezel (     NSRect rect,     NSRect clipRect ); ``` |

Modified [NSDrawGrayBezel()](https://developer.apple.com/documentation/appkit/1473712-nsdrawgraybezel)

|  | Declaration |
| --- | --- |
| From | ``` void NSDrawGrayBezel (     NSRect aRect,     NSRect clipRect ); ``` |
| To | ``` void NSDrawGrayBezel (     NSRect rect,     NSRect clipRect ); ``` |

Modified [NSDrawGroove()](https://developer.apple.com/documentation/appkit/1473644-nsdrawgroove)

|  | Declaration |
| --- | --- |
| From | ``` void NSDrawGroove (     NSRect aRect,     NSRect clipRect ); ``` |
| To | ``` void NSDrawGroove (     NSRect rect,     NSRect clipRect ); ``` |

Modified [NSDrawLightBezel()](https://developer.apple.com/documentation/appkit/1473680-nsdrawlightbezel)

|  | Declaration |
| --- | --- |
| From | ``` void NSDrawLightBezel (     NSRect aRect,     NSRect clipRect ); ``` |
| To | ``` void NSDrawLightBezel (     NSRect rect,     NSRect clipRect ); ``` |

Modified [NSDrawWhiteBezel()](https://developer.apple.com/documentation/appkit/1473783-nsdrawwhitebezel)

|  | Declaration |
| --- | --- |
| From | ``` void NSDrawWhiteBezel (     NSRect aRect,     NSRect clipRect ); ``` |
| To | ``` void NSDrawWhiteBezel (     NSRect rect,     NSRect clipRect ); ``` |

Modified [NSDrawWindowBackground()](https://developer.apple.com/documentation/appkit/1473664-nsdrawwindowbackground)

|  | Declaration |
| --- | --- |
| From | ``` void NSDrawWindowBackground (     NSRect aRect ); ``` |
| To | ``` void NSDrawWindowBackground (     NSRect rect ); ``` |

Modified [NSEraseRect()](https://developer.apple.com/documentation/appkit/1473745-nseraserect)

|  | Declaration |
| --- | --- |
| From | ``` void NSEraseRect (     NSRect aRect ); ``` |
| To | ``` void NSEraseRect (     NSRect rect ); ``` |

Modified [NSFrameRect()](https://developer.apple.com/documentation/appkit/1473582-nsframerect)

|  | Declaration |
| --- | --- |
| From | ``` void NSFrameRect (     NSRect aRect ); ``` |
| To | ``` void NSFrameRect (     NSRect rect ); ``` |

Modified [NSFrameRectWithWidth()](https://developer.apple.com/documentation/appkit/1473822-nsframerectwithwidth)

|  | Declaration |
| --- | --- |
| From | ``` void NSFrameRectWithWidth (     NSRect aRect,     CGFloat frameWidth ); ``` |
| To | ``` void NSFrameRectWithWidth (     NSRect rect,     CGFloat frameWidth ); ``` |

Modified [NSFrameRectWithWidthUsingOperation()](https://developer.apple.com/documentation/appkit/1473662-nsframerectwithwidthusingoperati)

|  | Declaration |
| --- | --- |
| From | ``` void NSFrameRectWithWidthUsingOperation (     NSRect aRect,     CGFloat frameWidth,     NSCompositingOperation op ); ``` |
| To | ``` void NSFrameRectWithWidthUsingOperation (     NSRect rect,     CGFloat frameWidth,     NSCompositingOperation op ); ``` |

Modified [NSHighlightRect()](https://developer.apple.com/documentation/appkit/1473592-nshighlightrect)

|  | Declaration |
| --- | --- |
| From | ``` void NSHighlightRect (     NSRect aRect ); ``` |
| To | ``` void NSHighlightRect (     NSRect rect ); ``` |

Modified [NSRectClip()](https://developer.apple.com/documentation/appkit/1473759-nsrectclip)

|  | Declaration |
| --- | --- |
| From | ``` void NSRectClip (     NSRect aRect ); ``` |
| To | ``` void NSRectClip (     NSRect rect ); ``` |

Modified [NSRectFill()](https://developer.apple.com/documentation/appkit/1473652-nsrectfill)

|  | Declaration |
| --- | --- |
| From | ``` void NSRectFill (     NSRect aRect ); ``` |
| To | ``` void NSRectFill (     NSRect rect ); ``` |

Modified [NSRectFillUsingOperation()](https://developer.apple.com/documentation/appkit/1473588-nsrectfillusingoperation)

|  | Declaration |
| --- | --- |
| From | ``` void NSRectFillUsingOperation (     NSRect aRect,     NSCompositingOperation op ); ``` |
| To | ``` void NSRectFillUsingOperation (     NSRect rect,     NSCompositingOperation op ); ``` |

#### NSGridView.h (Added)

Added [NSGridCell](https://developer.apple.com/documentation/appkit/nsgridcell)Added [NSGridCell.column](https://developer.apple.com/documentation/appkit/nsgridcell/1639747-column)Added [NSGridCell.contentView](https://developer.apple.com/documentation/appkit/nsgridcell/1639721-contentview)Added [NSGridCell.customPlacementConstraints](https://developer.apple.com/documentation/appkit/nsgridcell/1639717-customplacementconstraints)Added [+[NSGridCell emptyContentView]](https://developer.apple.com/documentation/appkit/nsgridcell/1639681-emptycontentview)Added [NSGridCell.emptyContentView](https://developer.apple.com/documentation/appkit/nsgridcell/1639681-emptycontentview)Added [NSGridCell.row](https://developer.apple.com/documentation/appkit/nsgridcell/1639763-row)Added [NSGridCell.rowAlignment](https://developer.apple.com/documentation/appkit/nsgridcell/1823686-rowalignment)Added [NSGridCell.xPlacement](https://developer.apple.com/documentation/appkit/nsgridcell/1639710-xplacement)Added [NSGridCell.yPlacement](https://developer.apple.com/documentation/appkit/nsgridcell/1639737-yplacement)Added [NSGridColumn](https://developer.apple.com/documentation/appkit/nsgridcolumn)Added [-[NSGridColumn cellAtIndex:]](https://developer.apple.com/documentation/appkit/nsgridcolumn/1639683-cell)Added [NSGridColumn.gridView](https://developer.apple.com/documentation/appkit/nsgridcolumn/1639675-gridview)Added [NSGridColumn.hidden](https://developer.apple.com/documentation/appkit/nsgridcolumn/1639742-hidden)Added [NSGridColumn.leadingPadding](https://developer.apple.com/documentation/appkit/nsgridcolumn/1639769-leadingpadding)Added [-[NSGridColumn mergeCellsInRange:]](https://developer.apple.com/documentation/appkit/nsgridcolumn/1639752-mergecellsinrange)Added [NSGridColumn.numberOfCells](https://developer.apple.com/documentation/appkit/nsgridcolumn/1639719-numberofcells)Added [NSGridColumn.trailingPadding](https://developer.apple.com/documentation/appkit/nsgridcolumn/1639670-trailingpadding)Added [NSGridColumn.width](https://developer.apple.com/documentation/appkit/nsgridcolumn/1639679-width)Added [NSGridColumn.xPlacement](https://developer.apple.com/documentation/appkit/nsgridcolumn/1639663-xplacement)Added [NSGridRow](https://developer.apple.com/documentation/appkit/nsgridrow)Added [NSGridRow.bottomPadding](https://developer.apple.com/documentation/appkit/nsgridrow/1639739-bottompadding)Added [-[NSGridRow cellAtIndex:]](https://developer.apple.com/documentation/appkit/nsgridrow/1639712-cell)Added [NSGridRow.gridView](https://developer.apple.com/documentation/appkit/nsgridrow/1639773-gridview)Added [NSGridRow.height](https://developer.apple.com/documentation/appkit/nsgridrow/1639728-height)Added [NSGridRow.hidden](https://developer.apple.com/documentation/appkit/nsgridrow/1639723-hidden)Added [-[NSGridRow mergeCellsInRange:]](https://developer.apple.com/documentation/appkit/nsgridrow/1639726-mergecellsinrange)Added [NSGridRow.numberOfCells](https://developer.apple.com/documentation/appkit/nsgridrow/1639685-numberofcells)Added [NSGridRow.rowAlignment](https://developer.apple.com/documentation/appkit/nsgridrow/1823690-rowalignment)Added [NSGridRow.topPadding](https://developer.apple.com/documentation/appkit/nsgridrow/1639785-toppadding)Added [NSGridRow.yPlacement](https://developer.apple.com/documentation/appkit/nsgridrow/1639665-yplacement)Added [NSGridView](https://developer.apple.com/documentation/appkit/nsgridview)Added [-[NSGridView addColumnWithViews:]](https://developer.apple.com/documentation/appkit/nsgridview/1639783-addcolumn)Added [-[NSGridView addRowWithViews:]](https://developer.apple.com/documentation/appkit/nsgridview/1639690-addrowwithviews)Added [-[NSGridView cellAtColumnIndex:rowIndex:]](https://developer.apple.com/documentation/appkit/nsgridview/1639778-cellatcolumnindex)Added [-[NSGridView cellForView:]](https://developer.apple.com/documentation/appkit/nsgridview/1639703-cellforview)Added [-[NSGridView columnAtIndex:]](https://developer.apple.com/documentation/appkit/nsgridview/1639674-columnatindex)Added [NSGridView.columnSpacing](https://developer.apple.com/documentation/appkit/nsgridview/1639776-columnspacing)Added [+[NSGridView gridViewWithNumberOfColumns:rows:]](https://developer.apple.com/documentation/appkit/nsgridview/1639714-init)Added [+[NSGridView gridViewWithViews:]](https://developer.apple.com/documentation/appkit/nsgridview/1639782-init)Added [-[NSGridView indexOfColumn:]](https://developer.apple.com/documentation/appkit/nsgridview/1639667-indexofcolumn)Added [-[NSGridView indexOfRow:]](https://developer.apple.com/documentation/appkit/nsgridview/1639661-indexofrow)Added [-[NSGridView initWithCoder:]](https://developer.apple.com/documentation/appkit/nsgridview/1639780-initwithcoder)Added [-[NSGridView initWithFrame:]](https://developer.apple.com/documentation/appkit/nsgridview/1639692-init)Added [-[NSGridView insertColumnAtIndex:withViews:]](https://developer.apple.com/documentation/appkit/nsgridview/1639700-insertcolumnatindex)Added [-[NSGridView insertRowAtIndex:withViews:]](https://developer.apple.com/documentation/appkit/nsgridview/1639787-insertrowatindex)Added [-[NSGridView mergeCellsInHorizontalRange:verticalRange:]](https://developer.apple.com/documentation/appkit/nsgridview/1639749-mergecells)Added [-[NSGridView moveColumnAtIndex:toIndex:]](https://developer.apple.com/documentation/appkit/nsgridview/1639659-movecolumn)Added [-[NSGridView moveRowAtIndex:toIndex:]](https://developer.apple.com/documentation/appkit/nsgridview/1639687-moverow)Added [NSGridView.numberOfColumns](https://developer.apple.com/documentation/appkit/nsgridview/1639698-numberofcolumns)Added [NSGridView.numberOfRows](https://developer.apple.com/documentation/appkit/nsgridview/1639705-numberofrows)Added [-[NSGridView removeColumnAtIndex:]](https://developer.apple.com/documentation/appkit/nsgridview/1639759-removecolumnatindex)Added [-[NSGridView removeRowAtIndex:]](https://developer.apple.com/documentation/appkit/nsgridview/1639771-removerowatindex)Added [NSGridView.rowAlignment](https://developer.apple.com/documentation/appkit/nsgridview/1823691-rowalignment)Added [-[NSGridView rowAtIndex:]](https://developer.apple.com/documentation/appkit/nsgridview/1639761-rowatindex)Added [NSGridView.rowSpacing](https://developer.apple.com/documentation/appkit/nsgridview/1639730-rowspacing)Added [NSGridView.xPlacement](https://developer.apple.com/documentation/appkit/nsgridview/1639732-xplacement)Added [NSGridView.yPlacement](https://developer.apple.com/documentation/appkit/nsgridview/1639767-yplacement)Added [NSGridCellPlacement](https://developer.apple.com/documentation/appkit/nsgridcellplacement)Added [NSGridCellPlacementBottom](https://developer.apple.com/documentation/appkit/nsgridcellplacement/nsgridcellplacementbottom)Added [NSGridCellPlacementCenter](https://developer.apple.com/documentation/appkit/nsgridcellplacement/nsgridcellplacementcenter)Added [NSGridCellPlacementFill](https://developer.apple.com/documentation/appkit/nsgridcell/placement/fill)Added [NSGridCellPlacementInherited](https://developer.apple.com/documentation/appkit/nsgridcell/placement/inherited)Added [NSGridCellPlacementLeading](https://developer.apple.com/documentation/appkit/nsgridcellplacement/nsgridcellplacementleading)Added [NSGridCellPlacementNone](https://developer.apple.com/documentation/appkit/nsgridcell/placement/none)Added [NSGridCellPlacementTop](https://developer.apple.com/documentation/appkit/nsgridcellplacement/nsgridcellplacementtop)Added [NSGridCellPlacementTrailing](https://developer.apple.com/documentation/appkit/nsgridcellplacement/nsgridcellplacementtrailing)Added [NSGridRowAlignment](https://developer.apple.com/documentation/appkit/nsgridrowalignment)Added [NSGridRowAlignmentFirstBaseline](https://developer.apple.com/documentation/appkit/nsgridrow/alignment/firstbaseline)Added [NSGridRowAlignmentInherited](https://developer.apple.com/documentation/appkit/nsgridrow/alignment/inherited)Added [NSGridRowAlignmentLastBaseline](https://developer.apple.com/documentation/appkit/nsgridrow/alignment/lastbaseline)Added [NSGridRowAlignmentNone](https://developer.apple.com/documentation/appkit/nsgridrowalignment/nsgridrowalignmentnone)Added [NSGridViewSizeForContent](https://developer.apple.com/documentation/appkit/nsgridview/1639715-sizedforcontent)

#### NSImage.h

Added [-[NSImage initWithCoder:]](https://developer.apple.com/documentation/appkit/nsimage/2177315-initwithcoder)Added #def NS_IMAGE_DECLARES_DESIGNATED_INITIALIZERSAdded [NSImageHintUserInterfaceLayoutDirection](https://developer.apple.com/documentation/appkit/nsimagehintuserinterfacelayoutdirection)Added [NSImageNameGoBackTemplate](https://developer.apple.com/documentation/appkit/nsimagenamegobacktemplate)Added [NSImageNameGoForwardTemplate](https://developer.apple.com/documentation/appkit/nsimagenamegoforwardtemplate)Modified [-[NSImage dissolveToPoint:fraction:]](https://developer.apple.com/documentation/appkit/nsimage/1519887-dissolvetopoint)

|  | Declaration |
| --- | --- |
| From | ``` - (void)dissolveToPoint:(NSPoint)point fraction:(CGFloat)aFloat ``` |
| To | ``` - (void)dissolveToPoint:(NSPoint)point fraction:(CGFloat)fraction ``` |

Modified [-[NSImage dissolveToPoint:fromRect:fraction:]](https://developer.apple.com/documentation/appkit/nsimage/1519968-dissolvetopoint)

|  | Declaration |
| --- | --- |
| From | ``` - (void)dissolveToPoint:(NSPoint)point fromRect:(NSRect)rect fraction:(CGFloat)aFloat ``` |
| To | ``` - (void)dissolveToPoint:(NSPoint)point fromRect:(NSRect)rect fraction:(CGFloat)fraction ``` |

Modified [-[NSImage initWithSize:]](https://developer.apple.com/documentation/appkit/nsimage/1520033-initwithsize)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithSize:(NSSize)aSize ``` | -- |
| To | ``` - (instancetype)initWithSize:(NSSize)size ``` | yes |

Modified [-[NSImage TIFFRepresentationUsingCompression:factor:]](https://developer.apple.com/documentation/appkit/nsimage/1519949-tiffrepresentationusingcompressi)

|  | Declaration |
| --- | --- |
| From | ``` - (NSData *)TIFFRepresentationUsingCompression:(NSTIFFCompression)comp factor:(float)aFloat ``` |
| To | ``` - (NSData *)TIFFRepresentationUsingCompression:(NSTIFFCompression)comp factor:(float)factor ``` |

Modified [-[NSImageDelegate imageDidNotDraw:inRect:]](https://developer.apple.com/documentation/appkit/nsimagedelegate/1519927-imagedidnotdraw)

|  | Declaration |
| --- | --- |
| From | ``` - (NSImage *)imageDidNotDraw:(NSImage *)sender inRect:(NSRect)aRect ``` |
| To | ``` - (NSImage *)imageDidNotDraw:(NSImage *)sender inRect:(NSRect)rect ``` |

#### NSImageRep.h

Added [NSImageRep.layoutDirection](https://developer.apple.com/documentation/appkit/nsimagerep/1690237-layoutdirection)Added [NSImageLayoutDirection](https://developer.apple.com/documentation/appkit/nsimage/layoutdirection)Added [NSImageLayoutDirectionLeftToRight](https://developer.apple.com/documentation/appkit/nsimagelayoutdirection/nsimagelayoutdirectionlefttoright)Added [NSImageLayoutDirectionRightToLeft](https://developer.apple.com/documentation/appkit/nsimage/layoutdirection/righttoleft)Added [NSImageLayoutDirectionUnspecified](https://developer.apple.com/documentation/appkit/nsimage/layoutdirection/unspecified)

#### NSImageView.h

Added [+[NSImageView imageViewWithImage:]](https://developer.apple.com/documentation/appkit/nsimageview/1644708-init)Added NSImageView(NSImageViewConvenience)

#### NSInputManager.h

Modified [-[NSInputManager handleMouseEvent:]](https://developer.apple.com/documentation/appkit/nsinputmanager/1412828-handlemouseevent)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)handleMouseEvent:(NSEvent *)theMouseEvent ``` |
| To | ``` - (BOOL)handleMouseEvent:(NSEvent *)mouseEvent ``` |

Modified [-[NSTextInput attributedSubstringFromRange:]](https://developer.apple.com/documentation/appkit/nstextinput/1412836-attributedsubstringfromrange)

|  | Declaration |
| --- | --- |
| From | ``` - (NSAttributedString *)attributedSubstringFromRange:(NSRange)theRange ``` |
| To | ``` - (NSAttributedString *)attributedSubstringFromRange:(NSRange)range ``` |

Modified [-[NSTextInput characterIndexForPoint:]](https://developer.apple.com/documentation/appkit/nstextinput/1412847-characterindexforpoint)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)characterIndexForPoint:(NSPoint)thePoint ``` |
| To | ``` - (NSUInteger)characterIndexForPoint:(NSPoint)point ``` |

Modified [-[NSTextInput doCommandBySelector:]](https://developer.apple.com/documentation/appkit/nstextinput/1412853-docommandbyselector)

|  | Declaration |
| --- | --- |
| From | ``` - (void)doCommandBySelector:(SEL)aSelector ``` |
| To | ``` - (void)doCommandBySelector:(SEL)selector ``` |

Modified [-[NSTextInput firstRectForCharacterRange:]](https://developer.apple.com/documentation/appkit/nstextinput/1412838-firstrectforcharacterrange)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)firstRectForCharacterRange:(NSRange)theRange ``` |
| To | ``` - (NSRect)firstRectForCharacterRange:(NSRange)range ``` |

Modified [-[NSTextInput insertText:]](https://developer.apple.com/documentation/appkit/nstextinput/1412816-inserttext)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertText:(id)aString ``` |
| To | ``` - (void)insertText:(id)string ``` |

Modified [-[NSTextInput setMarkedText:selectedRange:]](https://developer.apple.com/documentation/appkit/nstextinput/1412851-setmarkedtext)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setMarkedText:(id)aString selectedRange:(NSRange)selRange ``` |
| To | ``` - (void)setMarkedText:(id)string selectedRange:(NSRange)selRange ``` |

#### NSInputServer.h

Modified [-[NSInputServer initWithDelegate:name:]](https://developer.apple.com/documentation/appkit/nsinputserver/1538553-initwithdelegate)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDelegate:(id)aDelegate name:(NSString *)name ``` |
| To | ``` - (id)initWithDelegate:(id)delegate name:(NSString *)name ``` |

Modified [-[NSInputServerMouseTracker mouseDownOnCharacterIndex:atCoordinate:withModifier:client:]](https://developer.apple.com/documentation/appkit/nsinputservermousetracker/1538528-mousedownoncharacterindex)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)mouseDownOnCharacterIndex:(NSUInteger)theIndex atCoordinate:(NSPoint)thePoint withModifier:(NSUInteger)theFlags client:(id)sender ``` |
| To | ``` - (BOOL)mouseDownOnCharacterIndex:(NSUInteger)index atCoordinate:(NSPoint)point withModifier:(NSUInteger)flags client:(id)sender ``` |

Modified [-[NSInputServerMouseTracker mouseDraggedOnCharacterIndex:atCoordinate:withModifier:client:]](https://developer.apple.com/documentation/appkit/nsinputservermousetracker/1538554-mousedraggedoncharacterindex)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)mouseDraggedOnCharacterIndex:(NSUInteger)theIndex atCoordinate:(NSPoint)thePoint withModifier:(NSUInteger)theFlags client:(id)sender ``` |
| To | ``` - (BOOL)mouseDraggedOnCharacterIndex:(NSUInteger)index atCoordinate:(NSPoint)point withModifier:(NSUInteger)flags client:(id)sender ``` |

Modified [-[NSInputServerMouseTracker mouseUpOnCharacterIndex:atCoordinate:withModifier:client:]](https://developer.apple.com/documentation/appkit/nsinputservermousetracker/1538539-mouseuponcharacterindex)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mouseUpOnCharacterIndex:(NSUInteger)theIndex atCoordinate:(NSPoint)thePoint withModifier:(NSUInteger)theFlags client:(id)sender ``` |
| To | ``` - (void)mouseUpOnCharacterIndex:(NSUInteger)index atCoordinate:(NSPoint)point withModifier:(NSUInteger)flags client:(id)sender ``` |

Modified [-[NSInputServiceProvider doCommandBySelector:client:]](https://developer.apple.com/documentation/appkit/nsinputserviceprovider/1538533-docommandbyselector)

|  | Declaration |
| --- | --- |
| From | ``` - (void)doCommandBySelector:(SEL)aSelector client:(id)sender ``` |
| To | ``` - (void)doCommandBySelector:(SEL)selector client:(id)sender ``` |

Modified [-[NSInputServiceProvider insertText:client:]](https://developer.apple.com/documentation/appkit/nsinputserviceprovider/1538536-inserttext)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertText:(id)aString client:(id)sender ``` |
| To | ``` - (void)insertText:(id)string client:(id)sender ``` |

#### NSKeyValueBinding.h

Modified [-[NSObject optionDescriptionsForBinding:]](https://developer.apple.com/documentation/objectivec/nsobject/1458174-optiondescriptionsforbinding)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray<NSAttributeDescription *> *)optionDescriptionsForBinding:(NSString *)aBinding ``` |
| To | ``` - (NSArray<NSAttributeDescription *> *)optionDescriptionsForBinding:(NSString *)binding ``` |

#### NSLayoutAnchor.h

Modified [NSLayoutAnchor](https://developer.apple.com/documentation/appkit/nslayoutanchor)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSCoding, NSCopying |

#### NSLayoutConstraint.h

Added [NSLayoutConstraint.firstAnchor](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1644261-firstanchor)Added [NSLayoutConstraint.secondAnchor](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1644260-secondanchor)Modified [-[NSView updateConstraints]](https://developer.apple.com/documentation/appkit/nsview/1526891-updateconstraints)

|  | Override Requires Super |
| --- | --- |
| From | -- |
| To | yes |

#### NSLayoutGuide.h

Added [-[NSLayoutGuide constraintsAffectingLayoutForOrientation:]](https://developer.apple.com/documentation/appkit/nslayoutguide/1641956-constraintsaffectinglayoutforori)Added [NSLayoutGuide.hasAmbiguousLayout](https://developer.apple.com/documentation/appkit/nslayoutguide/1641955-hasambiguouslayout)

#### NSMatrix.h

Modified [-[NSMatrix acceptsFirstMouse:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436454-acceptsfirstmouse)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)acceptsFirstMouse:(NSEvent *)theEvent ``` |
| To | ``` - (BOOL)acceptsFirstMouse:(NSEvent *)event ``` |

Modified [-[NSMatrix cellWithTag:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436481-cellwithtag)

|  | Declaration |
| --- | --- |
| From | ``` - (__kindof NSCell *)cellWithTag:(NSInteger)anInt ``` |
| To | ``` - (__kindof NSCell *)cellWithTag:(NSInteger)tag ``` |

Modified [-[NSMatrix getRow:column:forPoint:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436441-getrow)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)getRow:(NSInteger *)row column:(NSInteger *)col forPoint:(NSPoint)aPoint ``` |
| To | ``` - (BOOL)getRow:(NSInteger *)row column:(NSInteger *)col forPoint:(NSPoint)point ``` |

Modified [-[NSMatrix getRow:column:ofCell:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436421-getrow)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)getRow:(NSInteger *)row column:(NSInteger *)col ofCell:(NSCell *)aCell ``` |
| To | ``` - (BOOL)getRow:(NSInteger *)row column:(NSInteger *)col ofCell:(NSCell *)cell ``` |

Modified [-[NSMatrix initWithFrame:mode:cellClass:numberOfRows:numberOfColumns:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436400-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithFrame:(NSRect)frameRect mode:(NSMatrixMode)aMode cellClass:(Class)factoryId numberOfRows:(NSInteger)rowsHigh numberOfColumns:(NSInteger)colsWide ``` |
| To | ``` - (instancetype)initWithFrame:(NSRect)frameRect mode:(NSMatrixMode)mode cellClass:(Class)factoryId numberOfRows:(NSInteger)rowsHigh numberOfColumns:(NSInteger)colsWide ``` |

Modified [-[NSMatrix initWithFrame:mode:prototype:numberOfRows:numberOfColumns:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436386-initwithframe)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithFrame:(NSRect)frameRect mode:(NSMatrixMode)aMode prototype:(NSCell *)aCell numberOfRows:(NSInteger)rowsHigh numberOfColumns:(NSInteger)colsWide ``` |
| To | ``` - (instancetype)initWithFrame:(NSRect)frameRect mode:(NSMatrixMode)mode prototype:(NSCell *)cell numberOfRows:(NSInteger)rowsHigh numberOfColumns:(NSInteger)colsWide ``` |

Modified [-[NSMatrix mouseDown:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436460-mousedown)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mouseDown:(NSEvent *)theEvent ``` |
| To | ``` - (void)mouseDown:(NSEvent *)event ``` |

Modified [-[NSMatrix performKeyEquivalent:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436418-performkeyequivalent)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)performKeyEquivalent:(NSEvent *)theEvent ``` |
| To | ``` - (BOOL)performKeyEquivalent:(NSEvent *)event ``` |

Modified [-[NSMatrix selectCellWithTag:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436446-selectcell)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)selectCellWithTag:(NSInteger)anInt ``` |
| To | ``` - (BOOL)selectCellWithTag:(NSInteger)tag ``` |

Modified [-[NSMatrix sendAction:to:forAllCells:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436370-sendaction)

|  | Declaration |
| --- | --- |
| From | ``` - (void)sendAction:(SEL)aSelector to:(id)anObject forAllCells:(BOOL)flag ``` |
| To | ``` - (void)sendAction:(SEL)selector to:(id)object forAllCells:(BOOL)flag ``` |

#### NSMenu.h

Added [-[NSMenu initWithCoder:]](https://developer.apple.com/documentation/appkit/nsmenu/1644714-initwithcoder)Modified [NSMenu](https://developer.apple.com/documentation/appkit/nsmenu)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSAccessibility, NSAccessibilityElement, NSCoding, NSCopying, NSUserInterfaceItemIdentification |

Modified [-[NSMenu addItemWithTitle:action:keyEquivalent:]](https://developer.apple.com/documentation/appkit/nsmenu/1518181-additem)

|  | Declaration |
| --- | --- |
| From | ``` - (NSMenuItem *)addItemWithTitle:(NSString *)aString action:(SEL)aSelector keyEquivalent:(NSString *)charCode ``` |
| To | ``` - (NSMenuItem *)addItemWithTitle:(NSString *)string action:(SEL)selector keyEquivalent:(NSString *)charCode ``` |

Modified [NSMenu.delegate](https://developer.apple.com/documentation/appkit/nsmenu/1518169-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<NSMenuDelegate> delegate ``` |
| To | ``` @property(weak) id<NSMenuDelegate> delegate ``` |

Modified [-[NSMenu indexOfItemWithTag:]](https://developer.apple.com/documentation/appkit/nsmenu/1518164-indexofitem)

|  | Declaration |
| --- | --- |
| From | ``` - (NSInteger)indexOfItemWithTag:(NSInteger)aTag ``` |
| To | ``` - (NSInteger)indexOfItemWithTag:(NSInteger)tag ``` |

Modified [-[NSMenu indexOfItemWithTitle:]](https://developer.apple.com/documentation/appkit/nsmenu/1518237-indexofitem)

|  | Declaration |
| --- | --- |
| From | ``` - (NSInteger)indexOfItemWithTitle:(NSString *)aTitle ``` |
| To | ``` - (NSInteger)indexOfItemWithTitle:(NSString *)title ``` |

Modified [-[NSMenu initWithTitle:]](https://developer.apple.com/documentation/appkit/nsmenu/1518144-initwithtitle)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithTitle:(NSString *)aTitle ``` | -- |
| To | ``` - (instancetype)initWithTitle:(NSString *)title ``` | yes |

Modified [-[NSMenu insertItemWithTitle:action:keyEquivalent:atIndex:]](https://developer.apple.com/documentation/appkit/nsmenu/1518146-insertitem)

|  | Declaration |
| --- | --- |
| From | ``` - (NSMenuItem *)insertItemWithTitle:(NSString *)aString action:(SEL)aSelector keyEquivalent:(NSString *)charCode atIndex:(NSInteger)index ``` |
| To | ``` - (NSMenuItem *)insertItemWithTitle:(NSString *)string action:(SEL)selector keyEquivalent:(NSString *)charCode atIndex:(NSInteger)index ``` |

Modified [-[NSMenu itemWithTitle:]](https://developer.apple.com/documentation/appkit/nsmenu/1518248-itemwithtitle)

|  | Declaration |
| --- | --- |
| From | ``` - (NSMenuItem *)itemWithTitle:(NSString *)aTitle ``` |
| To | ``` - (NSMenuItem *)itemWithTitle:(NSString *)title ``` |

Modified [-[NSMenu locationForSubmenu:]](https://developer.apple.com/documentation/appkit/nsmenu/1518158-locationforsubmenu)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPoint)locationForSubmenu:(NSMenu *)aSubmenu ``` |
| To | ``` - (NSPoint)locationForSubmenu:(NSMenu *)submenu ``` |

Modified [-[NSMenu performKeyEquivalent:]](https://developer.apple.com/documentation/appkit/nsmenu/1518198-performkeyequivalent)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)performKeyEquivalent:(NSEvent *)theEvent ``` |
| To | ``` - (BOOL)performKeyEquivalent:(NSEvent *)event ``` |

Modified [+[NSMenu setMenuZone:]](https://developer.apple.com/documentation/appkit/nsmenu/1518263-setmenuzone)

|  | Declaration |
| --- | --- |
| From | ``` + (void)setMenuZone:(NSZone *)aZone ``` |
| To | ``` + (void)setMenuZone:(NSZone *)zone ``` |

Modified [-[NSMenu setSubmenu:forItem:]](https://developer.apple.com/documentation/appkit/nsmenu/1518194-setsubmenu)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setSubmenu:(NSMenu *)aMenu forItem:(NSMenuItem *)anItem ``` |
| To | ``` - (void)setSubmenu:(NSMenu *)menu forItem:(NSMenuItem *)item ``` |

#### NSMenuItem.h

Added [-[NSMenuItem initWithCoder:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1644728-init)Modified [NSMenuItem](https://developer.apple.com/documentation/appkit/nsmenuitem)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSValidatedUserInterfaceItem |
| To | NSAccessibility, NSAccessibilityElement, NSCoding, NSCopying, NSUserInterfaceItemIdentification, NSValidatedUserInterfaceItem |

Modified [-[NSMenuItem initWithTitle:action:keyEquivalent:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514858-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithTitle:(NSString *)aString action:(SEL)aSelector keyEquivalent:(NSString *)charCode ``` | -- |
| To | ``` - (instancetype)initWithTitle:(NSString *)string action:(SEL)selector keyEquivalent:(NSString *)charCode ``` | yes |

Modified [NSMenuItem.keyEquivalentModifierMask](https://developer.apple.com/documentation/appkit/nsmenuitem/1514815-keyequivalentmodifiermask)

|  | Declaration |
| --- | --- |
| From | ``` @property NSUInteger keyEquivalentModifierMask ``` |
| To | ``` @property NSEventModifierFlags keyEquivalentModifierMask ``` |

#### NSMenuItemCell.h

Added [-[NSMenuItemCell initTextCell:]](https://developer.apple.com/documentation/appkit/nsmenuitemcell/1641970-inittextcell)Added [-[NSMenuItemCell initWithCoder:]](https://developer.apple.com/documentation/appkit/nsmenuitemcell/1641971-initwithcoder)

#### NSMenuView.h

Modified -[NSMenuView locationForSubmenu:]

|  | Declaration |
| --- | --- |
| From | ``` - (NSPoint)locationForSubmenu:(NSMenu *)aSubmenu ``` |
| To | ``` - (NSPoint)locationForSubmenu:(NSMenu *)submenu ``` |

#### NSOpenGL.h

Removed [NSOpenGLCPCurrentRendererID](https://developer.apple.com/documentation/appkit/nsopenglcpcurrentrendererid)Removed [NSOpenGLCPGPUFragmentProcessing](https://developer.apple.com/documentation/appkit/nsopenglcpgpufragmentprocessing)Removed [NSOpenGLCPGPUVertexProcessing](https://developer.apple.com/documentation/appkit/nsopenglcpgpuvertexprocessing)Removed [NSOpenGLCPHasDrawable](https://developer.apple.com/documentation/appkit/nsopenglcphasdrawable)Removed [NSOpenGLCPMPSwapsInFlight](https://developer.apple.com/documentation/appkit/nsopenglcpmpswapsinflight)Removed [NSOpenGLCPRasterizationEnable](https://developer.apple.com/documentation/appkit/nsopenglcprasterizationenable)Removed [NSOpenGLCPReclaimResources](https://developer.apple.com/documentation/appkit/nsopenglcpreclaimresources)Removed [NSOpenGLCPStateValidation](https://developer.apple.com/documentation/appkit/nsopenglcpstatevalidation)Removed [NSOpenGLCPSurfaceBackingSize](https://developer.apple.com/documentation/appkit/nsopenglcpsurfacebackingsize)Removed [NSOpenGLCPSurfaceOpacity](https://developer.apple.com/documentation/appkit/nsopenglcpsurfaceopacity)Removed [NSOpenGLCPSurfaceOrder](https://developer.apple.com/documentation/appkit/nsopenglcpsurfaceorder)Removed [NSOpenGLCPSurfaceSurfaceVolatile](https://developer.apple.com/documentation/appkit/nsopenglcpsurfacesurfacevolatile)Removed [NSOpenGLCPSwapInterval](https://developer.apple.com/documentation/appkit/nsopenglcpswapinterval)Removed [NSOpenGLCPSwapRectangle](https://developer.apple.com/documentation/appkit/nsopenglcpswaprectangle)Removed [NSOpenGLCPSwapRectangleEnable](https://developer.apple.com/documentation/appkit/nsopenglcpswaprectangleenable)Added #def NS_OPENGL_PIXEL_FORMAT_DECLARES_DESIGNATED_INITIALIZERSAdded [NSOpenGLContextParameterCurrentRendererID](https://developer.apple.com/documentation/appkit/nsopenglcontext/parameter/currentrendererid)Added [NSOpenGLContextParameterGPUFragmentProcessing](https://developer.apple.com/documentation/appkit/nsopenglcontextparameter/nsopenglcontextparametergpufragmentprocessing)Added [NSOpenGLContextParameterGPUVertexProcessing](https://developer.apple.com/documentation/appkit/nsopenglcontextparameter/nsopenglcontextparametergpuvertexprocessing)Added [NSOpenGLContextParameterHasDrawable](https://developer.apple.com/documentation/appkit/nsopenglcontextparameter/nsopenglcontextparameterhasdrawable)Added [NSOpenGLContextParameterMPSwapsInFlight](https://developer.apple.com/documentation/appkit/nsopenglcontext/parameter/mpswapsinflight)Added [NSOpenGLContextParameterRasterizationEnable](https://developer.apple.com/documentation/appkit/nsopenglcontextparameter/nsopenglcontextparameterrasterizationenable)Added [NSOpenGLContextParameterReclaimResources](https://developer.apple.com/documentation/appkit/nsopenglcontext/parameter/reclaimresources)Added [NSOpenGLContextParameterStateValidation](https://developer.apple.com/documentation/appkit/nsopenglcontext/parameter/statevalidation)Added [NSOpenGLContextParameterSurfaceBackingSize](https://developer.apple.com/documentation/appkit/nsopenglcontext/parameter/surfacebackingsize)Added [NSOpenGLContextParameterSurfaceOpacity](https://developer.apple.com/documentation/appkit/nsopenglcontextparameter/nsopenglcontextparametersurfaceopacity)Added [NSOpenGLContextParameterSurfaceOrder](https://developer.apple.com/documentation/appkit/nsopenglcontextparameter/nsopenglcontextparametersurfaceorder)Added [NSOpenGLContextParameterSurfaceSurfaceVolatile](https://developer.apple.com/documentation/appkit/nsopenglcontextparameter/nsopenglcontextparametersurfacesurfacevolatile)Added [NSOpenGLContextParameterSwapInterval](https://developer.apple.com/documentation/appkit/nsopenglcontext/parameter/swapinterval)Added [NSOpenGLContextParameterSwapRectangle](https://developer.apple.com/documentation/appkit/nsopenglcontext/parameter/swaprectangle)Added [NSOpenGLContextParameterSwapRectangleEnable](https://developer.apple.com/documentation/appkit/nsopenglcontext/parameter/swaprectangleenable)Added [NSOpenGLCPCurrentRendererID](https://developer.apple.com/documentation/appkit/nsopenglcpcurrentrendererid)Added [NSOpenGLCPGPUFragmentProcessing](https://developer.apple.com/documentation/appkit/nsopenglcpgpufragmentprocessing)Added [NSOpenGLCPGPUVertexProcessing](https://developer.apple.com/documentation/appkit/nsopenglcpgpuvertexprocessing)Added [NSOpenGLCPHasDrawable](https://developer.apple.com/documentation/appkit/nsopenglcphasdrawable)Added [NSOpenGLCPMPSwapsInFlight](https://developer.apple.com/documentation/appkit/nsopenglcpmpswapsinflight)Added [NSOpenGLCPRasterizationEnable](https://developer.apple.com/documentation/appkit/nsopenglcprasterizationenable)Added [NSOpenGLCPReclaimResources](https://developer.apple.com/documentation/appkit/nsopenglcpreclaimresources)Added [NSOpenGLCPStateValidation](https://developer.apple.com/documentation/appkit/nsopenglcpstatevalidation)Added [NSOpenGLCPSurfaceBackingSize](https://developer.apple.com/documentation/appkit/nsopenglcpsurfacebackingsize)Added [NSOpenGLCPSurfaceOpacity](https://developer.apple.com/documentation/appkit/nsopenglcpsurfaceopacity)Added [NSOpenGLCPSurfaceOrder](https://developer.apple.com/documentation/appkit/nsopenglcpsurfaceorder)Added [NSOpenGLCPSurfaceSurfaceVolatile](https://developer.apple.com/documentation/appkit/nsopenglcpsurfacesurfacevolatile)Added [NSOpenGLCPSwapInterval](https://developer.apple.com/documentation/appkit/nsopenglcpswapinterval)Added [NSOpenGLCPSwapRectangle](https://developer.apple.com/documentation/appkit/nsopenglcpswaprectangle)Added [NSOpenGLCPSwapRectangleEnable](https://developer.apple.com/documentation/appkit/nsopenglcpswaprectangleenable)Modified [-[NSOpenGLPixelFormat initWithCGLPixelFormatObj:]](https://developer.apple.com/documentation/appkit/nsopenglpixelformat/1436129-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [NSOpenGLPFAStereo](https://developer.apple.com/documentation/appkit/1436213-opengl_pixel_format_attributes/nsopenglpfastereo)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### NSOutlineView.h

Removed -[NSOutlineView setDataSource:]Removed -[NSOutlineView setDelegate:]Added [NSOutlineView.stronglyReferencesItems](https://developer.apple.com/documentation/appkit/nsoutlineview/1644626-stronglyreferencesitems)Modified [NSOutlineView.dataSource](https://developer.apple.com/documentation/appkit/nsoutlineview/1531054-datasource)

|  | Declaration |
| --- | --- |
| From | ``` - (id<NSOutlineViewDataSource>)dataSource ``` |
| To | ``` @property(weak) id<NSOutlineViewDataSource> dataSource ``` |

Modified [NSOutlineView.delegate](https://developer.apple.com/documentation/appkit/nsoutlineview/1534011-delegate)

|  | Declaration |
| --- | --- |
| From | ``` - (id<NSOutlineViewDelegate>)delegate ``` |
| To | ``` @property(weak) id<NSOutlineViewDelegate> delegate ``` |

#### NSPanel.h

Removed [NSDocModalWindowMask](https://developer.apple.com/documentation/appkit/nsdocmodalwindowmask)Removed [NSHUDWindowMask](https://developer.apple.com/documentation/appkit/nshudwindowmask)Removed [NSNonactivatingPanelMask](https://developer.apple.com/documentation/appkit/nsnonactivatingpanelmask)Removed [NSUtilityWindowMask](https://developer.apple.com/documentation/appkit/nsutilitywindowmask)

#### NSParagraphStyle.h

Modified [NSTextTab](https://developer.apple.com/documentation/uikit/nstexttab)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCoding, NSCopying, NSSecureCoding |

#### NSPasteboard.h

Added [-[NSPasteboard prepareForNewContentsWithOptions:]](https://developer.apple.com/documentation/appkit/nspasteboard/2344960-preparefornewcontents)Added [NSPasteboardContentsCurrentHostOnly](https://developer.apple.com/documentation/appkit/nspasteboard/contentsoptions/2344963-currenthostonly)Added [NSPasteboardContentsOptions](https://developer.apple.com/documentation/appkit/nspasteboard/contentsoptions)

#### NSPopover.h

Modified [NSPopover.delegate](https://developer.apple.com/documentation/appkit/nspopover/1526708-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) IBOutlet id<NSPopoverDelegate> delegate ``` |
| To | ``` @property(weak) IBOutlet id<NSPopoverDelegate> delegate ``` |

#### NSPopUpButton.h

Modified [-[NSPopUpButton setTitle:]](https://developer.apple.com/documentation/appkit/nspopupbutton/1535132-settitle)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setTitle:(NSString *)aString ``` |
| To | ``` - (void)setTitle:(NSString *)string ``` |

#### NSPopUpButtonCell.h

Added [-[NSPopUpButtonCell initWithCoder:]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1644676-init)Modified [-[NSPopUpButtonCell initTextCell:pullsDown:]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1528591-inittextcell)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPopUpButtonCell setTitle:]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1528475-settitle)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setTitle:(NSString *)aString ``` |
| To | ``` - (void)setTitle:(NSString *)string ``` |

#### NSPrintInfo.h

Added [-[NSPrintInfo init]](https://developer.apple.com/documentation/appkit/nsprintinfo/1644252-init)Added [-[NSPrintInfo initWithCoder:]](https://developer.apple.com/documentation/appkit/nsprintinfo/1644406-initwithcoder)Modified [-[NSPrintInfo initWithDictionary:]](https://developer.apple.com/documentation/appkit/nsprintinfo/1526768-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### NSResponder.h

Added [-[NSResponder newWindowForTab:]](https://developer.apple.com/documentation/appkit/nsresponder/1644675-newwindowfortab)Added NSResponder(NSWindowTabbing)Modified -[NSResponder doCommandBySelector:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)doCommandBySelector:(SEL)aSelector ``` |
| To | ``` - (void)doCommandBySelector:(SEL)selector ``` |

Modified [-[NSResponder flagsChanged:]](https://developer.apple.com/documentation/appkit/nsresponder/1527647-flagschanged)

|  | Declaration |
| --- | --- |
| From | ``` - (void)flagsChanged:(NSEvent *)theEvent ``` |
| To | ``` - (void)flagsChanged:(NSEvent *)event ``` |

Modified [-[NSResponder keyDown:]](https://developer.apple.com/documentation/appkit/nsresponder/1525805-keydown)

|  | Declaration |
| --- | --- |
| From | ``` - (void)keyDown:(NSEvent *)theEvent ``` |
| To | ``` - (void)keyDown:(NSEvent *)event ``` |

Modified [-[NSResponder keyUp:]](https://developer.apple.com/documentation/appkit/nsresponder/1527436-keyup)

|  | Declaration |
| --- | --- |
| From | ``` - (void)keyUp:(NSEvent *)theEvent ``` |
| To | ``` - (void)keyUp:(NSEvent *)event ``` |

Modified [-[NSResponder mouseDown:]](https://developer.apple.com/documentation/appkit/nsresponder/1524634-mousedown)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mouseDown:(NSEvent *)theEvent ``` |
| To | ``` - (void)mouseDown:(NSEvent *)event ``` |

Modified [-[NSResponder mouseDragged:]](https://developer.apple.com/documentation/appkit/nsresponder/1527420-mousedragged)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mouseDragged:(NSEvent *)theEvent ``` |
| To | ``` - (void)mouseDragged:(NSEvent *)event ``` |

Modified [-[NSResponder mouseEntered:]](https://developer.apple.com/documentation/appkit/nsresponder/1529306-mouseentered)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mouseEntered:(NSEvent *)theEvent ``` |
| To | ``` - (void)mouseEntered:(NSEvent *)event ``` |

Modified [-[NSResponder mouseExited:]](https://developer.apple.com/documentation/appkit/nsresponder/1527561-mouseexited)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mouseExited:(NSEvent *)theEvent ``` |
| To | ``` - (void)mouseExited:(NSEvent *)event ``` |

Modified [-[NSResponder mouseMoved:]](https://developer.apple.com/documentation/appkit/nsresponder/1525114-mousemoved)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mouseMoved:(NSEvent *)theEvent ``` |
| To | ``` - (void)mouseMoved:(NSEvent *)event ``` |

Modified [-[NSResponder mouseUp:]](https://developer.apple.com/documentation/appkit/nsresponder/1535349-mouseup)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mouseUp:(NSEvent *)theEvent ``` |
| To | ``` - (void)mouseUp:(NSEvent *)event ``` |

Modified [-[NSResponder otherMouseDown:]](https://developer.apple.com/documentation/appkit/nsresponder/1525719-othermousedown)

|  | Declaration |
| --- | --- |
| From | ``` - (void)otherMouseDown:(NSEvent *)theEvent ``` |
| To | ``` - (void)otherMouseDown:(NSEvent *)event ``` |

Modified [-[NSResponder otherMouseDragged:]](https://developer.apple.com/documentation/appkit/nsresponder/1529804-othermousedragged)

|  | Declaration |
| --- | --- |
| From | ``` - (void)otherMouseDragged:(NSEvent *)theEvent ``` |
| To | ``` - (void)otherMouseDragged:(NSEvent *)event ``` |

Modified [-[NSResponder otherMouseUp:]](https://developer.apple.com/documentation/appkit/nsresponder/1531343-othermouseup)

|  | Declaration |
| --- | --- |
| From | ``` - (void)otherMouseUp:(NSEvent *)theEvent ``` |
| To | ``` - (void)otherMouseUp:(NSEvent *)event ``` |

Modified [-[NSResponder performKeyEquivalent:]](https://developer.apple.com/documentation/appkit/nsresponder/1524690-performkeyequivalent)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)performKeyEquivalent:(NSEvent *)theEvent ``` |
| To | ``` - (BOOL)performKeyEquivalent:(NSEvent *)event ``` |

Modified [-[NSResponder performMnemonic:]](https://developer.apple.com/documentation/appkit/nsresponder/1584388-performmnemonic)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)performMnemonic:(NSString *)theString ``` |
| To | ``` - (BOOL)performMnemonic:(NSString *)string ``` |

Modified [-[NSResponder rightMouseDown:]](https://developer.apple.com/documentation/appkit/nsresponder/1524727-rightmousedown)

|  | Declaration |
| --- | --- |
| From | ``` - (void)rightMouseDown:(NSEvent *)theEvent ``` |
| To | ``` - (void)rightMouseDown:(NSEvent *)event ``` |

Modified [-[NSResponder rightMouseDragged:]](https://developer.apple.com/documentation/appkit/nsresponder/1529135-rightmousedragged)

|  | Declaration |
| --- | --- |
| From | ``` - (void)rightMouseDragged:(NSEvent *)theEvent ``` |
| To | ``` - (void)rightMouseDragged:(NSEvent *)event ``` |

Modified [-[NSResponder rightMouseUp:]](https://developer.apple.com/documentation/appkit/nsresponder/1526309-rightmouseup)

|  | Declaration |
| --- | --- |
| From | ``` - (void)rightMouseUp:(NSEvent *)theEvent ``` |
| To | ``` - (void)rightMouseUp:(NSEvent *)event ``` |

Modified [-[NSResponder scrollWheel:]](https://developer.apple.com/documentation/appkit/nsresponder/1534192-scrollwheel)

|  | Declaration |
| --- | --- |
| From | ``` - (void)scrollWheel:(NSEvent *)theEvent ``` |
| To | ``` - (void)scrollWheel:(NSEvent *)event ``` |

Modified [-[NSResponder shouldBeTreatedAsInkEvent:]](https://developer.apple.com/documentation/appkit/nsresponder/1534105-shouldbetreatedasinkevent)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)shouldBeTreatedAsInkEvent:(NSEvent *)theEvent ``` |
| To | ``` - (BOOL)shouldBeTreatedAsInkEvent:(NSEvent *)event ``` |

Modified [-[NSResponder tabletPoint:]](https://developer.apple.com/documentation/appkit/nsresponder/1530905-tabletpoint)

|  | Declaration |
| --- | --- |
| From | ``` - (void)tabletPoint:(NSEvent *)theEvent ``` |
| To | ``` - (void)tabletPoint:(NSEvent *)event ``` |

Modified [-[NSResponder tabletProximity:]](https://developer.apple.com/documentation/appkit/nsresponder/1527018-tabletproximity)

|  | Declaration |
| --- | --- |
| From | ``` - (void)tabletProximity:(NSEvent *)theEvent ``` |
| To | ``` - (void)tabletProximity:(NSEvent *)event ``` |

Modified [-[NSResponder tryToPerform:with:]](https://developer.apple.com/documentation/appkit/nsresponder/1524516-trytoperform)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)tryToPerform:(SEL)anAction with:(id)anObject ``` |
| To | ``` - (BOOL)tryToPerform:(SEL)action with:(id)object ``` |

#### NSRulerMarker.h

Added [-[NSRulerMarker initWithCoder:]](https://developer.apple.com/documentation/appkit/nsrulermarker/1642136-initwithcoder)Modified [-[NSRulerMarker initWithRulerView:markerLocation:image:imageOrigin:]](https://developer.apple.com/documentation/appkit/nsrulermarker/1496240-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### NSRulerView.h

Added [-[NSRulerView initWithCoder:]](https://developer.apple.com/documentation/appkit/nsrulerview/1644122-initwithcoder)Modified [-[NSRulerView initWithScrollView:orientation:]](https://developer.apple.com/documentation/appkit/nsrulerview/1535316-initwithscrollview)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSView rulerView:locationForPoint:]](https://developer.apple.com/documentation/appkit/nsview/1535261-rulerview)

|  | Declaration |
| --- | --- |
| From | ``` - (CGFloat)rulerView:(NSRulerView *)ruler locationForPoint:(NSPoint)aPoint ``` |
| To | ``` - (CGFloat)rulerView:(NSRulerView *)ruler locationForPoint:(NSPoint)point ``` |

Modified [-[NSView rulerView:pointForLocation:]](https://developer.apple.com/documentation/appkit/nsview/1524292-rulerview)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPoint)rulerView:(NSRulerView *)ruler pointForLocation:(CGFloat)aPoint ``` |
| To | ``` - (NSPoint)rulerView:(NSRulerView *)ruler pointForLocation:(CGFloat)point ``` |

#### NSScreen.h

Added [-[NSScreen canRepresentDisplayGamut:]](https://developer.apple.com/documentation/appkit/nsscreen/2138325-canrepresent)Modified [-[NSScreen backingAlignedRect:options:]](https://developer.apple.com/documentation/appkit/nsscreen/1388381-backingalignedrect)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)backingAlignedRect:(NSRect)aRect options:(NSAlignmentOptions)options ``` |
| To | ``` - (NSRect)backingAlignedRect:(NSRect)rect options:(NSAlignmentOptions)options ``` |

Modified [-[NSScreen convertRectFromBacking:]](https://developer.apple.com/documentation/appkit/nsscreen/1388364-convertrectfrombacking)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)convertRectFromBacking:(NSRect)aRect ``` |
| To | ``` - (NSRect)convertRectFromBacking:(NSRect)rect ``` |

Modified [-[NSScreen convertRectToBacking:]](https://developer.apple.com/documentation/appkit/nsscreen/1388389-convertrecttobacking)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)convertRectToBacking:(NSRect)aRect ``` |
| To | ``` - (NSRect)convertRectToBacking:(NSRect)rect ``` |

#### NSScroller.h

Modified [-[NSScroller setFloatValue:knobProportion:]](https://developer.apple.com/documentation/appkit/nsscroller/1523664-setfloatvalue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setFloatValue:(float)aFloat knobProportion:(CGFloat)proportion ``` |
| To | ``` - (void)setFloatValue:(float)value knobProportion:(CGFloat)proportion ``` |

Modified [-[NSScroller testPart:]](https://developer.apple.com/documentation/appkit/nsscroller/1523645-testpart)

|  | Declaration |
| --- | --- |
| From | ``` - (NSScrollerPart)testPart:(NSPoint)thePoint ``` |
| To | ``` - (NSScrollerPart)testPart:(NSPoint)point ``` |

Modified [-[NSScroller trackKnob:]](https://developer.apple.com/documentation/appkit/nsscroller/1523594-trackknob)

|  | Declaration |
| --- | --- |
| From | ``` - (void)trackKnob:(NSEvent *)theEvent ``` |
| To | ``` - (void)trackKnob:(NSEvent *)event ``` |

Modified [-[NSScroller trackScrollButtons:]](https://developer.apple.com/documentation/appkit/nsscroller/1523643-trackscrollbuttons)

|  | Declaration |
| --- | --- |
| From | ``` - (void)trackScrollButtons:(NSEvent *)theEvent ``` |
| To | ``` - (void)trackScrollButtons:(NSEvent *)event ``` |

#### NSScrollView.h

Modified [+[NSScrollView contentSizeForFrameSize:hasHorizontalScroller:hasVerticalScroller:borderType:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403481-contentsizeforframesize)

|  | Declaration |
| --- | --- |
| From | ``` + (NSSize)contentSizeForFrameSize:(NSSize)fSize hasHorizontalScroller:(BOOL)hFlag hasVerticalScroller:(BOOL)vFlag borderType:(NSBorderType)aType ``` |
| To | ``` + (NSSize)contentSizeForFrameSize:(NSSize)fSize hasHorizontalScroller:(BOOL)hFlag hasVerticalScroller:(BOOL)vFlag borderType:(NSBorderType)type ``` |

Modified [+[NSScrollView contentSizeForFrameSize:horizontalScrollerClass:verticalScrollerClass:borderType:controlSize:scrollerStyle:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403471-contentsizeforframesize)

|  | Declaration |
| --- | --- |
| From | ``` + (NSSize)contentSizeForFrameSize:(NSSize)fSize horizontalScrollerClass:(Class)horizontalScrollerClass verticalScrollerClass:(Class)verticalScrollerClass borderType:(NSBorderType)aType controlSize:(NSControlSize)controlSize scrollerStyle:(NSScrollerStyle)scrollerStyle ``` |
| To | ``` + (NSSize)contentSizeForFrameSize:(NSSize)fSize horizontalScrollerClass:(Class)horizontalScrollerClass verticalScrollerClass:(Class)verticalScrollerClass borderType:(NSBorderType)type controlSize:(NSControlSize)controlSize scrollerStyle:(NSScrollerStyle)scrollerStyle ``` |

Modified [NSScrollView.documentView](https://developer.apple.com/documentation/appkit/nsscrollview/1403485-documentview)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id documentView ``` |
| To | ``` @property(assign) __kindof NSView *documentView ``` |

Modified [+[NSScrollView frameSizeForContentSize:hasHorizontalScroller:hasVerticalScroller:borderType:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403469-framesizeforcontentsize)

|  | Declaration |
| --- | --- |
| From | ``` + (NSSize)frameSizeForContentSize:(NSSize)cSize hasHorizontalScroller:(BOOL)hFlag hasVerticalScroller:(BOOL)vFlag borderType:(NSBorderType)aType ``` |
| To | ``` + (NSSize)frameSizeForContentSize:(NSSize)cSize hasHorizontalScroller:(BOOL)hFlag hasVerticalScroller:(BOOL)vFlag borderType:(NSBorderType)type ``` |

Modified [+[NSScrollView frameSizeForContentSize:horizontalScrollerClass:verticalScrollerClass:borderType:controlSize:scrollerStyle:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403545-framesizeforcontentsize)

|  | Declaration |
| --- | --- |
| From | ``` + (NSSize)frameSizeForContentSize:(NSSize)cSize horizontalScrollerClass:(Class)horizontalScrollerClass verticalScrollerClass:(Class)verticalScrollerClass borderType:(NSBorderType)aType controlSize:(NSControlSize)controlSize scrollerStyle:(NSScrollerStyle)scrollerStyle ``` |
| To | ``` + (NSSize)frameSizeForContentSize:(NSSize)cSize horizontalScrollerClass:(Class)horizontalScrollerClass verticalScrollerClass:(Class)verticalScrollerClass borderType:(NSBorderType)type controlSize:(NSControlSize)controlSize scrollerStyle:(NSScrollerStyle)scrollerStyle ``` |

Modified [-[NSScrollView scrollWheel:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403494-scrollwheel)

|  | Declaration |
| --- | --- |
| From | ``` - (void)scrollWheel:(NSEvent *)theEvent ``` |
| To | ``` - (void)scrollWheel:(NSEvent *)event ``` |

#### NSSearchFieldCell.h

Added [-[NSSearchFieldCell initTextCell:]](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1643722-init)Added [-[NSSearchFieldCell initWithCoder:]](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1643723-initwithcoder)

#### NSSegmentedControl.h

Added [+[NSSegmentedControl segmentedControlWithImages:trackingMode:target:action:]](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/1644010-segmentedcontrolwithimages)Added [+[NSSegmentedControl segmentedControlWithLabels:trackingMode:target:action:]](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/1644011-segmentedcontrolwithlabels)Added NSSegmentedControl(NSSegmentedControlConvenience)

#### NSSharingService.h

Added [NSCloudSharingServiceDelegate](https://developer.apple.com/documentation/appkit/nscloudsharingservicedelegate)Added [-[NSCloudSharingServiceDelegate optionsForSharingService:shareProvider:]](https://developer.apple.com/documentation/appkit/nscloudsharingservicedelegate/1644694-options)Added [-[NSCloudSharingServiceDelegate sharingService:didCompleteForItems:error:]](https://developer.apple.com/documentation/appkit/nscloudsharingservicedelegate/1644666-sharingservice)Added [-[NSCloudSharingServiceDelegate sharingService:didSaveShare:]](https://developer.apple.com/documentation/appkit/nscloudsharingservicedelegate/1644712-sharingservice)Added [-[NSCloudSharingServiceDelegate sharingService:didStopSharing:]](https://developer.apple.com/documentation/appkit/nscloudsharingservicedelegate/1644709-sharingservice)Added [-[NSItemProvider registerCloudKitShare:container:]](https://developer.apple.com/documentation/foundation/nsitemprovider/1644692-registercloudkitshare)Added [-[NSItemProvider registerCloudKitShareWithPreparationHandler:]](https://developer.apple.com/documentation/foundation/nsitemprovider/1644475-registercloudkitsharewithprepara)Added [-[NSSharingServiceDelegate anchoringViewForSharingService:showRelativeToRect:preferredEdge:]](https://developer.apple.com/documentation/appkit/nssharingservicedelegate/1644711-anchoringview)Added #def NS_SHARING_SERVICE_DELEGATE_TRANSITION_IMAGE_FOR_SHARE_ITEM_DECLARES_NULLABILITYAdded [NSCloudKitSharingServiceAllowPrivate](https://developer.apple.com/documentation/appkit/nssharingservice/cloudkitoptions/1644710-allowprivate)Added [NSCloudKitSharingServiceAllowPublic](https://developer.apple.com/documentation/appkit/nssharingservice/cloudkitoptions/1644257-allowpublic)Added [NSCloudKitSharingServiceAllowReadOnly](https://developer.apple.com/documentation/appkit/nscloudkitsharingserviceoptions/nscloudkitsharingserviceallowreadonly)Added [NSCloudKitSharingServiceAllowReadWrite](https://developer.apple.com/documentation/appkit/nscloudkitsharingserviceoptions/nscloudkitsharingserviceallowreadwrite)Added [NSCloudKitSharingServiceOptions](https://developer.apple.com/documentation/appkit/nscloudkitsharingserviceoptions)Added [NSCloudKitSharingServiceStandard](https://developer.apple.com/documentation/appkit/nssharingservice/cloudkitoptions/1644263-standard)Added NSItemProvider(NSCloudKitSharing)Added [NSSharingServiceNameCloudSharing](https://developer.apple.com/documentation/appkit/nssharingservice/name/1644670-cloudsharing)

#### NSSlider.h

Added [+[NSSlider sliderWithTarget:action:]](https://developer.apple.com/documentation/appkit/nsslider/1644494-sliderwithtarget)Added [+[NSSlider sliderWithValue:minValue:maxValue:target:action:]](https://developer.apple.com/documentation/appkit/nsslider/1644495-init)Added NSSlider(NSSliderConvenience)Added NSSlider(NSSliderDeprecated)Added NSSlider(NSSliderVerticalGetter)Modified [-[NSSlider acceptsFirstMouse:]](https://developer.apple.com/documentation/appkit/nsslider/1530290-acceptsfirstmouse)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)acceptsFirstMouse:(NSEvent *)theEvent ``` |
| To | ``` - (BOOL)acceptsFirstMouse:(NSEvent *)event ``` |

Modified [-[NSSlider setKnobThickness:]](https://developer.apple.com/documentation/appkit/nsslider/1532899-setknobthickness)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setKnobThickness:(CGFloat)aFloat ``` |
| To | ``` - (void)setKnobThickness:(CGFloat)thickness ``` |

Modified [-[NSSlider setTitle:]](https://developer.apple.com/documentation/appkit/nsslider/1532915-settitle)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setTitle:(NSString *)aString ``` |
| To | ``` - (void)setTitle:(NSString *)string ``` |

Modified [-[NSSlider setTitleCell:]](https://developer.apple.com/documentation/appkit/nsslider/1532904-settitlecell)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setTitleCell:(NSCell *)aCell ``` |
| To | ``` - (void)setTitleCell:(NSCell *)cell ``` |

Modified [NSSlider.vertical](https://developer.apple.com/documentation/appkit/nsslider/1527901-vertical)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` @property(getter=isVertical, readonly) NSInteger vertical ``` | yes |
| To | ``` @property(readwrite, getter=isVertical) BOOL vertical ``` | -- |

#### NSSliderCell.h

Removed [NSCircularSlider](https://developer.apple.com/documentation/appkit/nscircularslider)Removed [NSLinearSlider](https://developer.apple.com/documentation/appkit/nslinearslider)Removed [NSTickMarkAbove](https://developer.apple.com/documentation/appkit/nstickmarkabove)Removed [NSTickMarkBelow](https://developer.apple.com/documentation/appkit/nstickmarkbelow)Removed [NSTickMarkLeft](https://developer.apple.com/documentation/appkit/nstickmarkleft)Removed [NSTickMarkRight](https://developer.apple.com/documentation/appkit/nstickmarkright)Added [NSCircularSlider](https://developer.apple.com/documentation/appkit/nscircularslider)Added [NSLinearSlider](https://developer.apple.com/documentation/appkit/nslinearslider)Added NSSliderCell(NSDeprecated)Added NSSliderCell(NSSliderCellVerticalGetter)Added [NSSliderTypeCircular](https://developer.apple.com/documentation/appkit/nsslider/slidertype/circular)Added [NSSliderTypeLinear](https://developer.apple.com/documentation/appkit/nsslidertype/nsslidertypelinear)Added [NSTickMarkAbove](https://developer.apple.com/documentation/appkit/nstickmarkabove)Added [NSTickMarkBelow](https://developer.apple.com/documentation/appkit/nstickmarkbelow)Added [NSTickMarkLeft](https://developer.apple.com/documentation/appkit/nstickmarkleft)Added [NSTickMarkPositionAbove](https://developer.apple.com/documentation/appkit/nsslider/tickmarkposition/above)Added [NSTickMarkPositionBelow](https://developer.apple.com/documentation/appkit/nsslider/tickmarkposition/below)Added [NSTickMarkPositionLeading](https://developer.apple.com/documentation/appkit/nsslider/tickmarkposition/1642260-leading)Added [NSTickMarkPositionTrailing](https://developer.apple.com/documentation/appkit/nstickmarkposition/nstickmarkpositiontrailing)Added [NSTickMarkRight](https://developer.apple.com/documentation/appkit/nstickmarkright)Modified [-[NSSliderCell drawBarInside:flipped:]](https://developer.apple.com/documentation/appkit/nsslidercell/1444587-drawbar)

|  | Declaration |
| --- | --- |
| From | ``` - (void)drawBarInside:(NSRect)aRect flipped:(BOOL)flipped ``` |
| To | ``` - (void)drawBarInside:(NSRect)rect flipped:(BOOL)flipped ``` |

Modified [-[NSSliderCell setKnobThickness:]](https://developer.apple.com/documentation/appkit/nsslidercell/1444612-setknobthickness)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setKnobThickness:(CGFloat)aFloat ``` |
| To | ``` - (void)setKnobThickness:(CGFloat)thickness ``` |

Modified [-[NSSliderCell setTitle:]](https://developer.apple.com/documentation/appkit/nsslidercell/1444631-settitle)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setTitle:(NSString *)aString ``` |
| To | ``` - (void)setTitle:(NSString *)string ``` |

Modified [-[NSSliderCell setTitleCell:]](https://developer.apple.com/documentation/appkit/nsslidercell/1444619-settitlecell)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setTitleCell:(NSCell *)aCell ``` |
| To | ``` - (void)setTitleCell:(NSCell *)cell ``` |

Modified [NSSliderCell.vertical](https://developer.apple.com/documentation/appkit/nsslidercell/1444602-isvertical)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` @property(getter=isVertical, readonly) NSInteger vertical ``` | yes |
| To | ``` @property(readwrite, getter=isVertical) BOOL vertical ``` | -- |

#### NSSound.h

Modified [-[NSSoundDelegate sound:didFinishPlaying:]](https://developer.apple.com/documentation/appkit/nssounddelegate/1477298-sound)

|  | Declaration |
| --- | --- |
| From | ``` - (void)sound:(NSSound *)sound didFinishPlaying:(BOOL)aBool ``` |
| To | ``` - (void)sound:(NSSound *)sound didFinishPlaying:(BOOL)flag ``` |

#### NSSpellChecker.h

Added +[NSSpellChecker isAutomaticCapitalizationEnabled]Added +[NSSpellChecker isAutomaticPeriodSubstitutionEnabled]Added [-[NSSpellChecker preventsAutocorrectionBeforeString:language:]](https://developer.apple.com/documentation/appkit/nsspellchecker/1792008-preventsautocorrectionbeforestri)Added [NSSpellCheckerDidChangeAutomaticCapitalizationNotification](https://developer.apple.com/documentation/appkit/nsspellcheckerdidchangeautomaticcapitalizationnotification)Added [NSSpellCheckerDidChangeAutomaticPeriodSubstitutionNotification](https://developer.apple.com/documentation/appkit/nsspellchecker/1792004-didchangeautomaticperiodsubstitu)Added [NSTextCheckingSelectedRangeKey](https://developer.apple.com/documentation/appkit/nsspellchecker/optionkey/1792005-selectedrange)Modified [-[NSSpellChecker setWordFieldStringValue:]](https://developer.apple.com/documentation/appkit/nsspellchecker/1526688-setwordfieldstringvalue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setWordFieldStringValue:(NSString *)aString ``` |
| To | ``` - (void)setWordFieldStringValue:(NSString *)string ``` |

#### NSSplitView.h

Modified [NSSplitView.delegate](https://developer.apple.com/documentation/appkit/nssplitview/1455306-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<NSSplitViewDelegate> delegate ``` |
| To | ``` @property(weak) id<NSSplitViewDelegate> delegate ``` |

#### NSSplitViewController.h

Modified [NSSplitViewItem](https://developer.apple.com/documentation/appkit/nssplitviewitem)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.automaticMaximumThickness](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388889-automaticmaximumthickness)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.behavior](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388899-behavior)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.canCollapse](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388926-cancollapse)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.collapseBehavior](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388851-collapsebehavior)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.collapsed](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388891-collapsed)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [+[NSSplitViewItem contentListWithViewController:]](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388878-contentlistwithviewcontroller)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.holdingPriority](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388887-holdingpriority)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.maximumThickness](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388930-maximumthickness)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.minimumThickness](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388853-minimumthickness)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.preferredThicknessFraction](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388885-preferredthicknessfraction)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [+[NSSplitViewItem sidebarWithViewController:]](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388920-init)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [+[NSSplitViewItem splitViewItemWithViewController:]](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388918-splitviewitemwithviewcontroller)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.springLoaded](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388895-springloaded)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.viewController](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388911-viewcontroller)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItemBehavior](https://developer.apple.com/documentation/appkit/nssplitviewitembehavior)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItemBehaviorContentList](https://developer.apple.com/documentation/appkit/nssplitviewitem/behavior/contentlist)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItemBehaviorDefault](https://developer.apple.com/documentation/appkit/nssplitviewitembehavior/nssplitviewitembehaviordefault)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItemBehaviorSidebar](https://developer.apple.com/documentation/appkit/nssplitviewitembehavior/nssplitviewitembehaviorsidebar)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItemCollapseBehavior](https://developer.apple.com/documentation/appkit/nssplitviewitemcollapsebehavior)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItemCollapseBehaviorDefault](https://developer.apple.com/documentation/appkit/nssplitviewitem/collapsebehavior/default)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItemCollapseBehaviorPreferResizingSiblingsWithFixedSplitView](https://developer.apple.com/documentation/appkit/nssplitviewitem/collapsebehavior/preferresizingsiblingswithfixedsplitview)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItemCollapseBehaviorPreferResizingSplitViewWithFixedSiblings](https://developer.apple.com/documentation/appkit/nssplitviewitem/collapsebehavior/preferresizingsplitviewwithfixedsiblings)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItemCollapseBehaviorUseConstraints](https://developer.apple.com/documentation/appkit/nssplitviewitem/collapsebehavior/useconstraints)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItemUnspecifiedDimension](https://developer.apple.com/documentation/appkit/nssplitviewitemunspecifieddimension)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

#### NSSplitViewItem.h (Added)

Modified [NSSplitViewItem](https://developer.apple.com/documentation/appkit/nssplitviewitem)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.automaticMaximumThickness](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388889-automaticmaximumthickness)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.behavior](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388899-behavior)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.canCollapse](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388926-cancollapse)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.collapseBehavior](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388851-collapsebehavior)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.collapsed](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388891-collapsed)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [+[NSSplitViewItem contentListWithViewController:]](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388878-contentlistwithviewcontroller)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.holdingPriority](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388887-holdingpriority)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.maximumThickness](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388930-maximumthickness)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.minimumThickness](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388853-minimumthickness)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.preferredThicknessFraction](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388885-preferredthicknessfraction)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [+[NSSplitViewItem sidebarWithViewController:]](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388920-init)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [+[NSSplitViewItem splitViewItemWithViewController:]](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388918-splitviewitemwithviewcontroller)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.springLoaded](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388895-springloaded)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItem.viewController](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388911-viewcontroller)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItemBehavior](https://developer.apple.com/documentation/appkit/nssplitviewitembehavior)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItemBehaviorContentList](https://developer.apple.com/documentation/appkit/nssplitviewitem/behavior/contentlist)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItemBehaviorDefault](https://developer.apple.com/documentation/appkit/nssplitviewitembehavior/nssplitviewitembehaviordefault)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItemBehaviorSidebar](https://developer.apple.com/documentation/appkit/nssplitviewitembehavior/nssplitviewitembehaviorsidebar)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItemCollapseBehavior](https://developer.apple.com/documentation/appkit/nssplitviewitemcollapsebehavior)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItemCollapseBehaviorDefault](https://developer.apple.com/documentation/appkit/nssplitviewitem/collapsebehavior/default)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItemCollapseBehaviorPreferResizingSiblingsWithFixedSplitView](https://developer.apple.com/documentation/appkit/nssplitviewitem/collapsebehavior/preferresizingsiblingswithfixedsplitview)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItemCollapseBehaviorPreferResizingSplitViewWithFixedSiblings](https://developer.apple.com/documentation/appkit/nssplitviewitem/collapsebehavior/preferresizingsplitviewwithfixedsiblings)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItemCollapseBehaviorUseConstraints](https://developer.apple.com/documentation/appkit/nssplitviewitem/collapsebehavior/useconstraints)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

Modified [NSSplitViewItemUnspecifiedDimension](https://developer.apple.com/documentation/appkit/nssplitviewitemunspecifieddimension)

|  | Header |
| --- | --- |
| From | AppKit/NSSplitViewController.h |
| To | AppKit/NSSplitViewItem.h |

#### NSStackView.h

Removed NSStackView(NSStackViewArrangedSubviews)Added NSStackView(NSStackViewGravityAreas)Modified [-[NSStackView addView:inGravity:]](https://developer.apple.com/documentation/appkit/nsstackview/1488897-addview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addView:(NSView *)aView inGravity:(NSStackViewGravity)gravity ``` |
| To | ``` - (void)addView:(NSView *)view inGravity:(NSStackViewGravity)gravity ``` |

Modified [-[NSStackView customSpacingAfterView:]](https://developer.apple.com/documentation/appkit/nsstackview/1488888-customspacing)

|  | Declaration |
| --- | --- |
| From | ``` - (CGFloat)customSpacingAfterView:(NSView *)aView ``` |
| To | ``` - (CGFloat)customSpacingAfterView:(NSView *)view ``` |

Modified [NSStackView.delegate](https://developer.apple.com/documentation/appkit/nsstackview/1488946-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<NSStackViewDelegate> delegate ``` |
| To | ``` @property(weak) id<NSStackViewDelegate> delegate ``` |

Modified [-[NSStackView insertView:atIndex:inGravity:]](https://developer.apple.com/documentation/appkit/nsstackview/1488933-insertview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertView:(NSView *)aView atIndex:(NSUInteger)index inGravity:(NSStackViewGravity)gravity ``` |
| To | ``` - (void)insertView:(NSView *)view atIndex:(NSUInteger)index inGravity:(NSStackViewGravity)gravity ``` |

Modified [-[NSStackView removeView:]](https://developer.apple.com/documentation/appkit/nsstackview/1488916-removeview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeView:(NSView *)aView ``` |
| To | ``` - (void)removeView:(NSView *)view ``` |

Modified [-[NSStackView setCustomSpacing:afterView:]](https://developer.apple.com/documentation/appkit/nsstackview/1488874-setcustomspacing)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setCustomSpacing:(CGFloat)spacing afterView:(NSView *)aView ``` |
| To | ``` - (void)setCustomSpacing:(CGFloat)spacing afterView:(NSView *)view ``` |

Modified [-[NSStackView setVisibilityPriority:forView:]](https://developer.apple.com/documentation/appkit/nsstackview/1488890-setvisibilitypriority)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setVisibilityPriority:(NSStackViewVisibilityPriority)priority forView:(NSView *)aView ``` |
| To | ``` - (void)setVisibilityPriority:(NSStackViewVisibilityPriority)priority forView:(NSView *)view ``` |

Modified [-[NSStackView visibilityPriorityForView:]](https://developer.apple.com/documentation/appkit/nsstackview/1488934-visibilitypriorityforview)

|  | Declaration |
| --- | --- |
| From | ``` - (NSStackViewVisibilityPriority)visibilityPriorityForView:(NSView *)aView ``` |
| To | ``` - (NSStackViewVisibilityPriority)visibilityPriorityForView:(NSView *)view ``` |

#### NSStatusItem.h

Added [NSStatusItem.autosaveName](https://developer.apple.com/documentation/appkit/nsstatusitem/1644022-autosavename)Added [NSStatusItem.behavior](https://developer.apple.com/documentation/appkit/nsstatusitem/1644024-behavior)Added [NSStatusItem.visible](https://developer.apple.com/documentation/appkit/nsstatusitem/1644025-visible)Added [NSStatusItemBehavior](https://developer.apple.com/documentation/appkit/nsstatusitembehavior)Added [NSStatusItemBehaviorRemovalAllowed](https://developer.apple.com/documentation/appkit/nsstatusitembehavior/nsstatusitembehaviorremovalallowed)Added [NSStatusItemBehaviorTerminationOnRemoval](https://developer.apple.com/documentation/appkit/nsstatusitembehavior/nsstatusitembehaviorterminationonremoval)Modified [-[NSStatusItem sendActionOn:]](https://developer.apple.com/documentation/appkit/nsstatusitem/1535025-sendaction)

|  | Declaration |
| --- | --- |
| From | ``` - (NSInteger)sendActionOn:(NSInteger)mask ``` |
| To | ``` - (NSInteger)sendActionOn:(NSEventMask)mask ``` |

#### NSTableColumn.h

Added [-[NSTableColumn initWithCoder:]](https://developer.apple.com/documentation/appkit/nstablecolumn/1644121-initwithcoder)Modified [-[NSTableColumn initWithIdentifier:]](https://developer.apple.com/documentation/appkit/nstablecolumn/1526749-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### NSTableHeaderCell.h

Modified [-[NSTableHeaderCell sortIndicatorRectForBounds:]](https://developer.apple.com/documentation/appkit/nstableheadercell/1525964-sortindicatorrect)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)sortIndicatorRectForBounds:(NSRect)theRect ``` |
| To | ``` - (NSRect)sortIndicatorRectForBounds:(NSRect)rect ``` |

#### NSTableView.h

Removed -[NSTableView setDataSource:]Removed -[NSTableView setDelegate:]Added [NSTableView.userInterfaceLayoutDirection](https://developer.apple.com/documentation/appkit/nstableview/1644591-userinterfacelayoutdirection)Modified [NSTableView.dataSource](https://developer.apple.com/documentation/appkit/nstableview/1531866-datasource)

|  | Declaration |
| --- | --- |
| From | ``` - (id<NSTableViewDataSource>)dataSource ``` |
| To | ``` @property(weak) id<NSTableViewDataSource> dataSource ``` |

Modified [NSTableView.delegate](https://developer.apple.com/documentation/appkit/nstableview/1534325-delegate)

|  | Declaration |
| --- | --- |
| From | ``` - (id<NSTableViewDelegate>)delegate ``` |
| To | ``` @property(weak) id<NSTableViewDelegate> delegate ``` |

Modified [-[NSTableView editColumn:row:withEvent:select:]](https://developer.apple.com/documentation/appkit/nstableview/1526295-editcolumn)

|  | Declaration |
| --- | --- |
| From | ``` - (void)editColumn:(NSInteger)column row:(NSInteger)row withEvent:(NSEvent *)theEvent select:(BOOL)select ``` |
| To | ``` - (void)editColumn:(NSInteger)column row:(NSInteger)row withEvent:(NSEvent *)event select:(BOOL)select ``` |

Modified [-[NSTableView setIndicatorImage:inTableColumn:]](https://developer.apple.com/documentation/appkit/nstableview/1534381-setindicatorimage)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setIndicatorImage:(NSImage *)anImage inTableColumn:(NSTableColumn *)tableColumn ``` |
| To | ``` - (void)setIndicatorImage:(NSImage *)image inTableColumn:(NSTableColumn *)tableColumn ``` |

#### NSTableViewRowAction.h

Added [NSTableViewRowAction.image](https://developer.apple.com/documentation/appkit/nstableviewrowaction/2177311-image)

#### NSTabView.h

Added [NSTabView.tabPosition](https://developer.apple.com/documentation/appkit/nstabview/2097105-tabposition)Added [NSTabView.tabViewBorderType](https://developer.apple.com/documentation/appkit/nstabview/2097112-tabviewbordertype)Added [NSTabPosition](https://developer.apple.com/documentation/appkit/nstabview/tabposition)Added [NSTabPositionBottom](https://developer.apple.com/documentation/appkit/nstabview/tabposition/bottom)Added [NSTabPositionLeft](https://developer.apple.com/documentation/appkit/nstabview/tabposition/left)Added [NSTabPositionNone](https://developer.apple.com/documentation/appkit/nstabposition/nstabpositionnone)Added [NSTabPositionRight](https://developer.apple.com/documentation/appkit/nstabposition/nstabpositionright)Added [NSTabPositionTop](https://developer.apple.com/documentation/appkit/nstabview/tabposition/top)Added [NSTabViewBorderType](https://developer.apple.com/documentation/appkit/nstabviewbordertype)Added [NSTabViewBorderTypeBezel](https://developer.apple.com/documentation/appkit/nstabview/tabviewbordertype/bezel)Added [NSTabViewBorderTypeLine](https://developer.apple.com/documentation/appkit/nstabviewbordertype/nstabviewbordertypeline)Added [NSTabViewBorderTypeNone](https://developer.apple.com/documentation/appkit/nstabview/tabviewbordertype/none)

#### NSText.h

Modified [-[NSText replaceCharactersInRange:withString:]](https://developer.apple.com/documentation/appkit/nstext/1530589-replacecharactersinrange)

|  | Declaration |
| --- | --- |
| From | ``` - (void)replaceCharactersInRange:(NSRange)range withString:(NSString *)aString ``` |
| To | ``` - (void)replaceCharactersInRange:(NSRange)range withString:(NSString *)string ``` |

Modified [NSCenterTextAlignment](https://developer.apple.com/documentation/appkit/nscentertextalignment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NSJustifiedTextAlignment](https://developer.apple.com/documentation/appkit/nsjustifiedtextalignment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NSLeftTextAlignment](https://developer.apple.com/documentation/appkit/nslefttextalignment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NSNaturalTextAlignment](https://developer.apple.com/documentation/appkit/nsnaturaltextalignment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NSRightTextAlignment](https://developer.apple.com/documentation/appkit/nsrighttextalignment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### NSTextContainer.h

Modified [NSTextContainer.textView](https://developer.apple.com/documentation/appkit/nstextcontainer/1444537-textview)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSTextView *textView ``` |
| To | ``` @property(weak) NSTextView *textView ``` |

#### NSTextField.h

Added [+[NSTextField labelWithAttributedString:]](https://developer.apple.com/documentation/appkit/nstextfield/1644658-labelwithattributedstring)Added [+[NSTextField labelWithString:]](https://developer.apple.com/documentation/appkit/nstextfield/1644377-init)Added [+[NSTextField textFieldWithString:]](https://developer.apple.com/documentation/appkit/nstextfield/1644706-init)Added [+[NSTextField wrappingLabelWithString:]](https://developer.apple.com/documentation/appkit/nstextfield/1644543-init)Added NSTextField(NSTextFieldConvenience)

#### NSTextFieldCell.h

Added [-[NSTextFieldCell initTextCell:]](https://developer.apple.com/documentation/appkit/nstextfieldcell/1642278-init)Added [-[NSTextFieldCell initWithCoder:]](https://developer.apple.com/documentation/appkit/nstextfieldcell/1642277-initwithcoder)

#### NSTextFinder.h

Added [-[NSTextFinder initWithCoder:]](https://developer.apple.com/documentation/appkit/nstextfinder/1644638-initwithcoder)Modified [-[NSTextFinder init]](https://developer.apple.com/documentation/appkit/nstextfinder/1535019-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### NSTextInputClient.h

Modified [-[NSTextInputClient attributedSubstringForProposedRange:actualRange:]](https://developer.apple.com/documentation/appkit/nstextinputclient/1438238-attributedsubstringforproposedra)

|  | Declaration |
| --- | --- |
| From | ``` - (NSAttributedString *)attributedSubstringForProposedRange:(NSRange)aRange actualRange:(NSRangePointer)actualRange ``` |
| To | ``` - (NSAttributedString *)attributedSubstringForProposedRange:(NSRange)range actualRange:(NSRangePointer)actualRange ``` |

Modified [-[NSTextInputClient characterIndexForPoint:]](https://developer.apple.com/documentation/appkit/nstextinputclient/1438244-characterindexforpoint)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)characterIndexForPoint:(NSPoint)aPoint ``` |
| To | ``` - (NSUInteger)characterIndexForPoint:(NSPoint)point ``` |

Modified [-[NSTextInputClient doCommandBySelector:]](https://developer.apple.com/documentation/appkit/nstextinputclient/1438256-docommand)

|  | Declaration |
| --- | --- |
| From | ``` - (void)doCommandBySelector:(SEL)aSelector ``` |
| To | ``` - (void)doCommandBySelector:(SEL)selector ``` |

Modified [-[NSTextInputClient firstRectForCharacterRange:actualRange:]](https://developer.apple.com/documentation/appkit/nstextinputclient/1438240-firstrect)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)firstRectForCharacterRange:(NSRange)aRange actualRange:(NSRangePointer)actualRange ``` |
| To | ``` - (NSRect)firstRectForCharacterRange:(NSRange)range actualRange:(NSRangePointer)actualRange ``` |

Modified [-[NSTextInputClient fractionOfDistanceThroughGlyphForPoint:]](https://developer.apple.com/documentation/appkit/nstextinputclient/1438236-fractionofdistancethroughglyphfo)

|  | Declaration |
| --- | --- |
| From | ``` - (CGFloat)fractionOfDistanceThroughGlyphForPoint:(NSPoint)aPoint ``` |
| To | ``` - (CGFloat)fractionOfDistanceThroughGlyphForPoint:(NSPoint)point ``` |

Modified [-[NSTextInputClient insertText:replacementRange:]](https://developer.apple.com/documentation/appkit/nstextinputclient/1438258-inserttext)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertText:(id)aString replacementRange:(NSRange)replacementRange ``` |
| To | ``` - (void)insertText:(id)string replacementRange:(NSRange)replacementRange ``` |

Modified [-[NSTextInputClient setMarkedText:selectedRange:replacementRange:]](https://developer.apple.com/documentation/appkit/nstextinputclient/1438246-setmarkedtext)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setMarkedText:(id)aString selectedRange:(NSRange)selectedRange replacementRange:(NSRange)replacementRange ``` |
| To | ``` - (void)setMarkedText:(id)string selectedRange:(NSRange)selectedRange replacementRange:(NSRange)replacementRange ``` |

#### NSTextInputContext.h

Modified [-[NSTextInputContext handleEvent:]](https://developer.apple.com/documentation/appkit/nstextinputcontext/1528602-handleevent)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)handleEvent:(NSEvent *)theEvent ``` |
| To | ``` - (BOOL)handleEvent:(NSEvent *)event ``` |

Modified [-[NSTextInputContext initWithClient:]](https://developer.apple.com/documentation/appkit/nstextinputcontext/1532777-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithClient:(id<NSTextInputClient>)theClient ``` | -- |
| To | ``` - (instancetype)initWithClient:(id<NSTextInputClient>)client ``` | yes |

#### NSTextTable.h

Modified [-[NSTextBlock init]](https://developer.apple.com/documentation/appkit/nstextblock/1528169-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextTableBlock initWithTable:startingRow:rowSpan:startingColumn:columnSpan:]](https://developer.apple.com/documentation/appkit/nstexttableblock/1532894-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### NSTextView.h

Added +[NSTextView stronglyReferencesTextStorage]Added NSTextView.stronglyReferencesTextStorageModified [-[NSTextView setLayoutOrientation:]](https://developer.apple.com/documentation/appkit/nstextview/1449483-setlayoutorientation)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setLayoutOrientation:(NSTextLayoutOrientation)theOrientation ``` |
| To | ``` - (void)setLayoutOrientation:(NSTextLayoutOrientation)orientation ``` |

#### NSTitlebarAccessoryViewController.h

Added [NSTitlebarAccessoryViewController.hidden](https://developer.apple.com/documentation/appkit/nstitlebaraccessoryviewcontroller/2097084-ishidden)Modified [NSTitlebarAccessoryViewController](https://developer.apple.com/documentation/appkit/nstitlebaraccessoryviewcontroller)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSAnimatablePropertyContainer, NSAnimationDelegate |

#### NSTokenField.h

Removed -[NSTokenField setDelegate:]Modified [NSTokenField.delegate](https://developer.apple.com/documentation/appkit/nstokenfield/1528157-delegate)

|  | Declaration |
| --- | --- |
| From | ``` - (id<NSTokenFieldDelegate>)delegate ``` |
| To | ``` @property(assign) id<NSTokenFieldDelegate> delegate ``` |

#### NSToolbarItem.h

Added [NSCloudSharingValidation](https://developer.apple.com/documentation/appkit/nscloudsharingvalidation)Added [-[NSCloudSharingValidation cloudShareForUserInterfaceItem:]](https://developer.apple.com/documentation/appkit/nscloudsharingvalidation/2315049-cloudshare)Added [NSToolbarCloudSharingItemIdentifier](https://developer.apple.com/documentation/appkit/nstoolbarcloudsharingitemidentifier)Modified [-[NSObject validateToolbarItem:]](https://developer.apple.com/documentation/objectivec/nsobject/1524282-validatetoolbaritem)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)validateToolbarItem:(NSToolbarItem *)theItem ``` |
| To | ``` - (BOOL)validateToolbarItem:(NSToolbarItem *)item ``` |

#### NSTypesetter.h

Modified [+[NSTypesetter sharedSystemTypesetterForBehavior:]](https://developer.apple.com/documentation/appkit/nstypesetter/1530659-sharedsystemtypesetter)

|  | Declaration |
| --- | --- |
| From | ``` + (id)sharedSystemTypesetterForBehavior:(NSTypesetterBehavior)theBehavior ``` |
| To | ``` + (id)sharedSystemTypesetterForBehavior:(NSTypesetterBehavior)behavior ``` |

#### NSUserInterfaceValidation.h

Modified [-[NSUserInterfaceValidations validateUserInterfaceItem:]](https://developer.apple.com/documentation/appkit/nsuserinterfacevalidations/1528162-validateuserinterfaceitem)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)validateUserInterfaceItem:(id<NSValidatedUserInterfaceItem>)anItem ``` |
| To | ``` - (BOOL)validateUserInterfaceItem:(id<NSValidatedUserInterfaceItem>)item ``` |

Modified [NSValidatedUserInterfaceItem.action](https://developer.apple.com/documentation/appkit/nsvalidateduserinterfaceitem/1527339-action)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (SEL)action ``` | -- |
| To | ``` @property(readonly) SEL action ``` | yes |

Modified [NSValidatedUserInterfaceItem.tag](https://developer.apple.com/documentation/appkit/nsvalidateduserinterfaceitem/1531030-tag)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` - (NSInteger)tag ``` | -- |
| To | ``` @property(readonly) NSInteger tag ``` | yes |

#### NSView.h

Modified [-[NSView acceptsFirstMouse:]](https://developer.apple.com/documentation/appkit/nsview/1483410-acceptsfirstmouse)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)acceptsFirstMouse:(NSEvent *)theEvent ``` |
| To | ``` - (BOOL)acceptsFirstMouse:(NSEvent *)event ``` |

Modified [-[NSView addCursorRect:cursor:]](https://developer.apple.com/documentation/appkit/nsview/1483540-addcursorrect)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addCursorRect:(NSRect)aRect cursor:(NSCursor *)anObj ``` |
| To | ``` - (void)addCursorRect:(NSRect)rect cursor:(NSCursor *)object ``` |

Modified [-[NSView addSubview:]](https://developer.apple.com/documentation/appkit/nsview/1483783-addsubview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addSubview:(NSView *)aView ``` |
| To | ``` - (void)addSubview:(NSView *)view ``` |

Modified [-[NSView addSubview:positioned:relativeTo:]](https://developer.apple.com/documentation/appkit/nsview/1483640-addsubview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addSubview:(NSView *)aView positioned:(NSWindowOrderingMode)place relativeTo:(NSView *)otherView ``` |
| To | ``` - (void)addSubview:(NSView *)view positioned:(NSWindowOrderingMode)place relativeTo:(NSView *)otherView ``` |

Modified [-[NSView addToolTipRect:owner:userData:]](https://developer.apple.com/documentation/appkit/nsview/1483229-addtooltip)

|  | Declaration |
| --- | --- |
| From | ``` - (NSToolTipTag)addToolTipRect:(NSRect)aRect owner:(id)anObject userData:(void *)data ``` |
| To | ``` - (NSToolTipTag)addToolTipRect:(NSRect)rect owner:(id)owner userData:(void *)data ``` |

Modified [-[NSView addTrackingRect:owner:userData:assumeInside:]](https://developer.apple.com/documentation/appkit/nsview/1483668-addtrackingrect)

|  | Declaration |
| --- | --- |
| From | ``` - (NSTrackingRectTag)addTrackingRect:(NSRect)aRect owner:(id)anObject userData:(void *)data assumeInside:(BOOL)flag ``` |
| To | ``` - (NSTrackingRectTag)addTrackingRect:(NSRect)rect owner:(id)owner userData:(void *)data assumeInside:(BOOL)flag ``` |

Modified [-[NSView ancestorSharedWithView:]](https://developer.apple.com/documentation/appkit/nsview/1483353-ancestorshared)

|  | Declaration |
| --- | --- |
| From | ``` - (NSView *)ancestorSharedWithView:(NSView *)aView ``` |
| To | ``` - (NSView *)ancestorSharedWithView:(NSView *)view ``` |

Modified [-[NSView autoscroll:]](https://developer.apple.com/documentation/appkit/nsview/1483471-autoscroll)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)autoscroll:(NSEvent *)theEvent ``` |
| To | ``` - (BOOL)autoscroll:(NSEvent *)event ``` |

Modified [-[NSView backingAlignedRect:options:]](https://developer.apple.com/documentation/appkit/nsview/1483321-backingalignedrect)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)backingAlignedRect:(NSRect)aRect options:(NSAlignmentOptions)options ``` |
| To | ``` - (NSRect)backingAlignedRect:(NSRect)rect options:(NSAlignmentOptions)options ``` |

Modified [-[NSView beginPageInRect:atPlacement:]](https://developer.apple.com/documentation/appkit/nsview/1483438-beginpage)

|  | Declaration |
| --- | --- |
| From | ``` - (void)beginPageInRect:(NSRect)aRect atPlacement:(NSPoint)location ``` |
| To | ``` - (void)beginPageInRect:(NSRect)rect atPlacement:(NSPoint)location ``` |

Modified [-[NSView centerScanRect:]](https://developer.apple.com/documentation/appkit/nsview/1483725-centerscanrect)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)centerScanRect:(NSRect)aRect ``` |
| To | ``` - (NSRect)centerScanRect:(NSRect)rect ``` |

Modified [-[NSView convertPoint:fromView:]](https://developer.apple.com/documentation/appkit/nsview/1483269-convertpoint)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPoint)convertPoint:(NSPoint)aPoint fromView:(NSView *)aView ``` |
| To | ``` - (NSPoint)convertPoint:(NSPoint)point fromView:(NSView *)view ``` |

Modified [-[NSView convertPoint:toView:]](https://developer.apple.com/documentation/appkit/nsview/1483406-convertpoint)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPoint)convertPoint:(NSPoint)aPoint toView:(NSView *)aView ``` |
| To | ``` - (NSPoint)convertPoint:(NSPoint)point toView:(NSView *)view ``` |

Modified [-[NSView convertPointFromBacking:]](https://developer.apple.com/documentation/appkit/nsview/1483456-convertpointfrombacking)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPoint)convertPointFromBacking:(NSPoint)aPoint ``` |
| To | ``` - (NSPoint)convertPointFromBacking:(NSPoint)point ``` |

Modified [-[NSView convertPointFromBase:]](https://developer.apple.com/documentation/appkit/nsview/1483778-convertpointfrombase)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPoint)convertPointFromBase:(NSPoint)aPoint ``` |
| To | ``` - (NSPoint)convertPointFromBase:(NSPoint)point ``` |

Modified [-[NSView convertPointFromLayer:]](https://developer.apple.com/documentation/appkit/nsview/1483554-convertpointfromlayer)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPoint)convertPointFromLayer:(NSPoint)aPoint ``` |
| To | ``` - (NSPoint)convertPointFromLayer:(NSPoint)point ``` |

Modified [-[NSView convertPointToBacking:]](https://developer.apple.com/documentation/appkit/nsview/1483803-converttobacking)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPoint)convertPointToBacking:(NSPoint)aPoint ``` |
| To | ``` - (NSPoint)convertPointToBacking:(NSPoint)point ``` |

Modified [-[NSView convertPointToBase:]](https://developer.apple.com/documentation/appkit/nsview/1483362-convertpointtobase)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPoint)convertPointToBase:(NSPoint)aPoint ``` |
| To | ``` - (NSPoint)convertPointToBase:(NSPoint)point ``` |

Modified [-[NSView convertPointToLayer:]](https://developer.apple.com/documentation/appkit/nsview/1483315-convertpointtolayer)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPoint)convertPointToLayer:(NSPoint)aPoint ``` |
| To | ``` - (NSPoint)convertPointToLayer:(NSPoint)point ``` |

Modified [-[NSView convertRect:fromView:]](https://developer.apple.com/documentation/appkit/nsview/1483785-convert)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)convertRect:(NSRect)aRect fromView:(NSView *)aView ``` |
| To | ``` - (NSRect)convertRect:(NSRect)rect fromView:(NSView *)view ``` |

Modified [-[NSView convertRect:toView:]](https://developer.apple.com/documentation/appkit/nsview/1483217-convert)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)convertRect:(NSRect)aRect toView:(NSView *)aView ``` |
| To | ``` - (NSRect)convertRect:(NSRect)rect toView:(NSView *)view ``` |

Modified [-[NSView convertRectFromBacking:]](https://developer.apple.com/documentation/appkit/nsview/1483819-convertrectfrombacking)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)convertRectFromBacking:(NSRect)aRect ``` |
| To | ``` - (NSRect)convertRectFromBacking:(NSRect)rect ``` |

Modified [-[NSView convertRectFromBase:]](https://developer.apple.com/documentation/appkit/nsview/1483591-convertrectfrombase)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)convertRectFromBase:(NSRect)aRect ``` |
| To | ``` - (NSRect)convertRectFromBase:(NSRect)rect ``` |

Modified [-[NSView convertRectFromLayer:]](https://developer.apple.com/documentation/appkit/nsview/1483404-convertrectfromlayer)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)convertRectFromLayer:(NSRect)aRect ``` |
| To | ``` - (NSRect)convertRectFromLayer:(NSRect)rect ``` |

Modified [-[NSView convertRectToBacking:]](https://developer.apple.com/documentation/appkit/nsview/1483648-convertrecttobacking)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)convertRectToBacking:(NSRect)aRect ``` |
| To | ``` - (NSRect)convertRectToBacking:(NSRect)rect ``` |

Modified [-[NSView convertRectToBase:]](https://developer.apple.com/documentation/appkit/nsview/1483331-convertrecttobase)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)convertRectToBase:(NSRect)aRect ``` |
| To | ``` - (NSRect)convertRectToBase:(NSRect)rect ``` |

Modified [-[NSView convertRectToLayer:]](https://developer.apple.com/documentation/appkit/nsview/1483776-converttolayer)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)convertRectToLayer:(NSRect)aRect ``` |
| To | ``` - (NSRect)convertRectToLayer:(NSRect)rect ``` |

Modified [-[NSView convertSize:fromView:]](https://developer.apple.com/documentation/appkit/nsview/1483307-convert)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSize)convertSize:(NSSize)aSize fromView:(NSView *)aView ``` |
| To | ``` - (NSSize)convertSize:(NSSize)size fromView:(NSView *)view ``` |

Modified [-[NSView convertSize:toView:]](https://developer.apple.com/documentation/appkit/nsview/1483744-convertsize)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSize)convertSize:(NSSize)aSize toView:(NSView *)aView ``` |
| To | ``` - (NSSize)convertSize:(NSSize)size toView:(NSView *)view ``` |

Modified [-[NSView convertSizeFromBacking:]](https://developer.apple.com/documentation/appkit/nsview/1483319-convertfrombacking)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSize)convertSizeFromBacking:(NSSize)aSize ``` |
| To | ``` - (NSSize)convertSizeFromBacking:(NSSize)size ``` |

Modified [-[NSView convertSizeFromBase:]](https://developer.apple.com/documentation/appkit/nsview/1483357-convertsizefrombase)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSize)convertSizeFromBase:(NSSize)aSize ``` |
| To | ``` - (NSSize)convertSizeFromBase:(NSSize)size ``` |

Modified [-[NSView convertSizeFromLayer:]](https://developer.apple.com/documentation/appkit/nsview/1483479-convertsizefromlayer)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSize)convertSizeFromLayer:(NSSize)aSize ``` |
| To | ``` - (NSSize)convertSizeFromLayer:(NSSize)size ``` |

Modified [-[NSView convertSizeToBacking:]](https://developer.apple.com/documentation/appkit/nsview/1483227-convertsizetobacking)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSize)convertSizeToBacking:(NSSize)aSize ``` |
| To | ``` - (NSSize)convertSizeToBacking:(NSSize)size ``` |

Modified [-[NSView convertSizeToBase:]](https://developer.apple.com/documentation/appkit/nsview/1483349-convertsizetobase)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSize)convertSizeToBase:(NSSize)aSize ``` |
| To | ``` - (NSSize)convertSizeToBase:(NSSize)size ``` |

Modified [-[NSView convertSizeToLayer:]](https://developer.apple.com/documentation/appkit/nsview/1483701-convertsizetolayer)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSize)convertSizeToLayer:(NSSize)aSize ``` |
| To | ``` - (NSSize)convertSizeToLayer:(NSSize)size ``` |

Modified [-[NSView displayRectIgnoringOpacity:inContext:]](https://developer.apple.com/documentation/appkit/nsview/1483436-displayignoringopacity)

|  | Declaration |
| --- | --- |
| From | ``` - (void)displayRectIgnoringOpacity:(NSRect)aRect inContext:(NSGraphicsContext *)context ``` |
| To | ``` - (void)displayRectIgnoringOpacity:(NSRect)rect inContext:(NSGraphicsContext *)context ``` |

Modified [-[NSView dragFile:fromRect:slideBack:event:]](https://developer.apple.com/documentation/appkit/nsview/1483600-dragfile)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)dragFile:(NSString *)filename fromRect:(NSRect)rect slideBack:(BOOL)aFlag event:(NSEvent *)event ``` |
| To | ``` - (BOOL)dragFile:(NSString *)filename fromRect:(NSRect)rect slideBack:(BOOL)flag event:(NSEvent *)event ``` |

Modified [-[NSView dragImage:at:offset:event:pasteboard:source:slideBack:]](https://developer.apple.com/documentation/appkit/nsview/1483279-dragimage)

|  | Declaration |
| --- | --- |
| From | ``` - (void)dragImage:(NSImage *)anImage at:(NSPoint)viewLocation offset:(NSSize)initialOffset event:(NSEvent *)event pasteboard:(NSPasteboard *)pboard source:(id)sourceObj slideBack:(BOOL)slideFlag ``` |
| To | ``` - (void)dragImage:(NSImage *)image at:(NSPoint)viewLocation offset:(NSSize)initialOffset event:(NSEvent *)event pasteboard:(NSPasteboard *)pboard source:(id)sourceObj slideBack:(BOOL)slideFlag ``` |

Modified [-[NSView dragPromisedFilesOfTypes:fromRect:source:slideBack:event:]](https://developer.apple.com/documentation/appkit/nsview/1483598-dragpromisedfilesoftypes)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)dragPromisedFilesOfTypes:(NSArray<NSString *> *)typeArray fromRect:(NSRect)rect source:(id)sourceObject slideBack:(BOOL)aFlag event:(NSEvent *)event ``` |
| To | ``` - (BOOL)dragPromisedFilesOfTypes:(NSArray<NSString *> *)typeArray fromRect:(NSRect)rect source:(id)sourceObject slideBack:(BOOL)flag event:(NSEvent *)event ``` |

Modified [-[NSView hitTest:]](https://developer.apple.com/documentation/appkit/nsview/1483364-hittest)

|  | Declaration |
| --- | --- |
| From | ``` - (NSView *)hitTest:(NSPoint)aPoint ``` |
| To | ``` - (NSView *)hitTest:(NSPoint)point ``` |

Modified [-[NSView isDescendantOf:]](https://developer.apple.com/documentation/appkit/nsview/1483219-isdescendantof)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isDescendantOf:(NSView *)aView ``` |
| To | ``` - (BOOL)isDescendantOf:(NSView *)view ``` |

Modified [-[NSView locationOfPrintRect:]](https://developer.apple.com/documentation/appkit/nsview/1483223-locationofprintrect)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPoint)locationOfPrintRect:(NSRect)aRect ``` |
| To | ``` - (NSPoint)locationOfPrintRect:(NSRect)rect ``` |

Modified [-[NSView mouse:inRect:]](https://developer.apple.com/documentation/appkit/nsview/1483237-ismousepoint)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)mouse:(NSPoint)aPoint inRect:(NSRect)aRect ``` |
| To | ``` - (BOOL)mouse:(NSPoint)point inRect:(NSRect)rect ``` |

Modified [-[NSView needsToDrawRect:]](https://developer.apple.com/documentation/appkit/nsview/1483570-needstodrawrect)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)needsToDrawRect:(NSRect)aRect ``` |
| To | ``` - (BOOL)needsToDrawRect:(NSRect)rect ``` |

Modified [-[NSView performKeyEquivalent:]](https://developer.apple.com/documentation/appkit/nsview/1483664-performkeyequivalent)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)performKeyEquivalent:(NSEvent *)theEvent ``` |
| To | ``` - (BOOL)performKeyEquivalent:(NSEvent *)event ``` |

Modified [-[NSView performMnemonic:]](https://developer.apple.com/documentation/appkit/nsview/1483585-performmnemonic)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)performMnemonic:(NSString *)theString ``` |
| To | ``` - (BOOL)performMnemonic:(NSString *)string ``` |

Modified [-[NSView removeCursorRect:cursor:]](https://developer.apple.com/documentation/appkit/nsview/1483676-removecursorrect)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeCursorRect:(NSRect)aRect cursor:(NSCursor *)anObj ``` |
| To | ``` - (void)removeCursorRect:(NSRect)rect cursor:(NSCursor *)object ``` |

Modified [-[NSView scrollPoint:]](https://developer.apple.com/documentation/appkit/nsview/1483394-scroll)

|  | Declaration |
| --- | --- |
| From | ``` - (void)scrollPoint:(NSPoint)aPoint ``` |
| To | ``` - (void)scrollPoint:(NSPoint)point ``` |

Modified [-[NSView scrollRect:by:]](https://developer.apple.com/documentation/appkit/nsview/1483497-scroll)

|  | Declaration |
| --- | --- |
| From | ``` - (void)scrollRect:(NSRect)aRect by:(NSSize)delta ``` |
| To | ``` - (void)scrollRect:(NSRect)rect by:(NSSize)delta ``` |

Modified [-[NSView scrollRectToVisible:]](https://developer.apple.com/documentation/appkit/nsview/1483811-scrollrecttovisible)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)scrollRectToVisible:(NSRect)aRect ``` |
| To | ``` - (BOOL)scrollRectToVisible:(NSRect)rect ``` |

Modified [-[NSView shouldDelayWindowOrderingForEvent:]](https://developer.apple.com/documentation/appkit/nsview/1483244-shoulddelaywindowordering)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)shouldDelayWindowOrderingForEvent:(NSEvent *)theEvent ``` |
| To | ``` - (BOOL)shouldDelayWindowOrderingForEvent:(NSEvent *)event ``` |

Modified [-[NSView viewWithTag:]](https://developer.apple.com/documentation/appkit/nsview/1483294-viewwithtag)

|  | Declaration |
| --- | --- |
| From | ``` - (__kindof NSView *)viewWithTag:(NSInteger)aTag ``` |
| To | ``` - (__kindof NSView *)viewWithTag:(NSInteger)tag ``` |

#### NSViewController.h

Modified [NSViewController.presentedViewControllers](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434497-presentedviewcontrollers)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) NSArray<__kindof NSViewController *> *presentedViewControllers ``` |
| To | ``` @property(readonly) NSArray<__kindof NSViewController *> *presentedViewControllers ``` |

#### NSVisualEffectView.h

Added [NSVisualEffectView.emphasized](https://developer.apple.com/documentation/appkit/nsvisualeffectview/1644721-emphasized)Added [NSVisualEffectMaterialSelection](https://developer.apple.com/documentation/appkit/nsvisualeffectmaterial/nsvisualeffectmaterialselection)

#### NSWindow.h

Removed -[NSWindow setStyleMask:]Removed [NSBorderlessWindowMask](https://developer.apple.com/documentation/appkit/nsborderlesswindowmask)Removed [NSClosableWindowMask](https://developer.apple.com/documentation/appkit/nsclosablewindowmask)Removed [NSFullScreenWindowMask](https://developer.apple.com/documentation/appkit/nsfullscreenwindowmask)Removed [NSFullSizeContentViewWindowMask](https://developer.apple.com/documentation/appkit/nsfullsizecontentviewwindowmask)Removed [NSMiniaturizableWindowMask](https://developer.apple.com/documentation/appkit/nsminiaturizablewindowmask)Removed [NSResizableWindowMask](https://developer.apple.com/documentation/appkit/nsresizablewindowmask)Removed [NSTexturedBackgroundWindowMask](https://developer.apple.com/documentation/appkit/nstexturedbackgroundwindowmask)Removed [NSTitledWindowMask](https://developer.apple.com/documentation/appkit/nstitledwindowmask)Removed [NSUnifiedTitleAndToolbarWindowMask](https://developer.apple.com/documentation/appkit/nsunifiedtitleandtoolbarwindowmask)Removed NSWindow(NSKeyboardUI)Removed NSWindow(NSToolbarSupport)Added [-[NSWindow addTabbedWindow:ordered:]](https://developer.apple.com/documentation/appkit/nswindow/1855947-addtabbedwindow)Added [+[NSWindow allowsAutomaticWindowTabbing]](https://developer.apple.com/documentation/appkit/nswindow/1646657-allowsautomaticwindowtabbing)Added [NSWindow.allowsAutomaticWindowTabbing](https://developer.apple.com/documentation/appkit/nswindow/1646657-allowsautomaticwindowtabbing)Added [-[NSWindow canRepresentDisplayGamut:]](https://developer.apple.com/documentation/appkit/nswindow/2138278-canrepresentdisplaygamut)Added [-[NSWindow mergeAllWindows:]](https://developer.apple.com/documentation/appkit/nswindow/1644639-mergeallwindows)Added [-[NSWindow moveTabToNewWindow:]](https://developer.apple.com/documentation/appkit/nswindow/1644410-movetabtonewwindow)Added [-[NSWindow selectNextTab:]](https://developer.apple.com/documentation/appkit/nswindow/1644693-selectnexttab)Added [-[NSWindow selectPreviousTab:]](https://developer.apple.com/documentation/appkit/nswindow/1644555-selectprevioustab)Added +[NSWindow setAllowsAutomaticWindowTabbing:]Added [NSWindow.tabbedWindows](https://developer.apple.com/documentation/appkit/nswindow/1792044-tabbedwindows)Added [NSWindow.tabbingIdentifier](https://developer.apple.com/documentation/appkit/nswindow/1644704-tabbingidentifier)Added [NSWindow.tabbingMode](https://developer.apple.com/documentation/appkit/nswindow/1644729-tabbingmode)Added [-[NSWindow toggleTabBar:]](https://developer.apple.com/documentation/appkit/nswindow/1644517-toggletabbar)Added [+[NSWindow userTabbingPreference]](https://developer.apple.com/documentation/appkit/nswindow/1646658-usertabbingpreference)Added [NSWindow.userTabbingPreference](https://developer.apple.com/documentation/appkit/nswindow/1646658-usertabbingpreference)Added [NSWindow.windowTitlebarLayoutDirection](https://developer.apple.com/documentation/appkit/nswindow/1644535-windowtitlebarlayoutdirection)Added [NSBorderlessWindowMask](https://developer.apple.com/documentation/appkit/nsborderlesswindowmask)Added [NSClosableWindowMask](https://developer.apple.com/documentation/appkit/nsclosablewindowmask)Added [NSDocModalWindowMask](https://developer.apple.com/documentation/appkit/nsdocmodalwindowmask)Added [NSFullScreenWindowMask](https://developer.apple.com/documentation/appkit/nsfullscreenwindowmask)Added [NSFullSizeContentViewWindowMask](https://developer.apple.com/documentation/appkit/nsfullsizecontentviewwindowmask)Added [NSHUDWindowMask](https://developer.apple.com/documentation/appkit/nshudwindowmask)Added [NSMiniaturizableWindowMask](https://developer.apple.com/documentation/appkit/nsminiaturizablewindowmask)Added [NSNonactivatingPanelMask](https://developer.apple.com/documentation/appkit/nsnonactivatingpanelmask)Added [NSResizableWindowMask](https://developer.apple.com/documentation/appkit/nsresizablewindowmask)Added [NSTexturedBackgroundWindowMask](https://developer.apple.com/documentation/appkit/nstexturedbackgroundwindowmask)Added [NSTitledWindowMask](https://developer.apple.com/documentation/appkit/nstitledwindowmask)Added [NSUnifiedTitleAndToolbarWindowMask](https://developer.apple.com/documentation/appkit/nsunifiedtitleandtoolbarwindowmask)Added [NSUtilityWindowMask](https://developer.apple.com/documentation/appkit/nsutilitywindowmask)Added NSWindow(NSCursorRect)Added NSWindow(NSEvent)Added #def NSWINDOW_TRACK_EVENTS_DECLARES_NULLABILITYAdded [NSWindowCollectionBehaviorFullScreenNone](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior/1644248-fullscreennone)Added [NSWindowStyleMask](https://developer.apple.com/documentation/appkit/nswindow/stylemask)Added [NSWindowStyleMaskBorderless](https://developer.apple.com/documentation/appkit/nswindowstylemask/nswindowstylemaskborderless)Added [NSWindowStyleMaskClosable](https://developer.apple.com/documentation/appkit/nswindow/stylemask/1644610-closable)Added [NSWindowStyleMaskDocModalWindow](https://developer.apple.com/documentation/appkit/nswindow/stylemask/1644253-docmodalwindow)Added [NSWindowStyleMaskFullScreen](https://developer.apple.com/documentation/appkit/nswindow/stylemask/1644530-fullscreen)Added [NSWindowStyleMaskFullSizeContentView](https://developer.apple.com/documentation/appkit/nswindow/stylemask/1644646-fullsizecontentview)Added [NSWindowStyleMaskHUDWindow](https://developer.apple.com/documentation/appkit/nswindowstylemask/nswindowstylemaskhudwindow)Added [NSWindowStyleMaskMiniaturizable](https://developer.apple.com/documentation/appkit/nswindow/stylemask/1644650-miniaturizable)Added [NSWindowStyleMaskNonactivatingPanel](https://developer.apple.com/documentation/appkit/nswindow/stylemask/1644696-nonactivatingpanel)Added [NSWindowStyleMaskResizable](https://developer.apple.com/documentation/appkit/nswindow/stylemask/1644717-resizable)Added [NSWindowStyleMaskTexturedBackground](https://developer.apple.com/documentation/appkit/nswindow/stylemask/1644673-texturedbackground)Added [NSWindowStyleMaskTitled](https://developer.apple.com/documentation/appkit/nswindowstylemask/nswindowstylemasktitled)Added [NSWindowStyleMaskUnifiedTitleAndToolbar](https://developer.apple.com/documentation/appkit/nswindow/stylemask/1644619-unifiedtitleandtoolbar)Added [NSWindowStyleMaskUtilityWindow](https://developer.apple.com/documentation/appkit/nswindowstylemask/nswindowstylemaskutilitywindow)Added [NSWindowTabbingMode](https://developer.apple.com/documentation/appkit/nswindow/tabbingmode)Added [NSWindowTabbingModeAutomatic](https://developer.apple.com/documentation/appkit/nswindow/tabbingmode/automatic)Added [NSWindowTabbingModeDisallowed](https://developer.apple.com/documentation/appkit/nswindow/tabbingmode/disallowed)Added [NSWindowTabbingModePreferred](https://developer.apple.com/documentation/appkit/nswindow/tabbingmode/preferred)Added [NSWindowUserTabbingPreference](https://developer.apple.com/documentation/appkit/nswindow/usertabbingpreference)Added [NSWindowUserTabbingPreferenceAlways](https://developer.apple.com/documentation/appkit/nswindowusertabbingpreference/nswindowusertabbingpreferencealways)Added [NSWindowUserTabbingPreferenceInFullScreen](https://developer.apple.com/documentation/appkit/nswindowusertabbingpreference/nswindowusertabbingpreferenceinfullscreen)Added [NSWindowUserTabbingPreferenceManual](https://developer.apple.com/documentation/appkit/nswindow/usertabbingpreference/manual)Modified [-[NSWindow backingAlignedRect:options:]](https://developer.apple.com/documentation/appkit/nswindow/1419319-backingalignedrect)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)backingAlignedRect:(NSRect)aRect options:(NSAlignmentOptions)options ``` |
| To | ``` - (NSRect)backingAlignedRect:(NSRect)rect options:(NSAlignmentOptions)options ``` |

Modified [-[NSWindow cacheImageInRect:]](https://developer.apple.com/documentation/appkit/nswindow/1419410-cacheimageinrect)

|  | Declaration |
| --- | --- |
| From | ``` - (void)cacheImageInRect:(NSRect)aRect ``` |
| To | ``` - (void)cacheImageInRect:(NSRect)rect ``` |

Modified [+[NSWindow contentRectForFrameRect:styleMask:]](https://developer.apple.com/documentation/appkit/nswindow/1419586-contentrect)

|  | Declaration |
| --- | --- |
| From | ``` + (NSRect)contentRectForFrameRect:(NSRect)fRect styleMask:(NSUInteger)aStyle ``` |
| To | ``` + (NSRect)contentRectForFrameRect:(NSRect)fRect styleMask:(NSWindowStyleMask)style ``` |

Modified [-[NSWindow convertBaseToScreen:]](https://developer.apple.com/documentation/appkit/nswindow/1419550-convertbasetoscreen)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPoint)convertBaseToScreen:(NSPoint)aPoint ``` |
| To | ``` - (NSPoint)convertBaseToScreen:(NSPoint)point ``` |

Modified [-[NSWindow convertRectFromBacking:]](https://developer.apple.com/documentation/appkit/nswindow/1419273-convertfrombacking)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)convertRectFromBacking:(NSRect)aRect ``` |
| To | ``` - (NSRect)convertRectFromBacking:(NSRect)rect ``` |

Modified [-[NSWindow convertRectFromScreen:]](https://developer.apple.com/documentation/appkit/nswindow/1419603-convertfromscreen)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)convertRectFromScreen:(NSRect)aRect ``` |
| To | ``` - (NSRect)convertRectFromScreen:(NSRect)rect ``` |

Modified [-[NSWindow convertRectToBacking:]](https://developer.apple.com/documentation/appkit/nswindow/1419260-converttobacking)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)convertRectToBacking:(NSRect)aRect ``` |
| To | ``` - (NSRect)convertRectToBacking:(NSRect)rect ``` |

Modified [-[NSWindow convertRectToScreen:]](https://developer.apple.com/documentation/appkit/nswindow/1419286-convertrecttoscreen)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRect)convertRectToScreen:(NSRect)aRect ``` |
| To | ``` - (NSRect)convertRectToScreen:(NSRect)rect ``` |

Modified [-[NSWindow convertScreenToBase:]](https://developer.apple.com/documentation/appkit/nswindow/1419414-convertscreentobase)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPoint)convertScreenToBase:(NSPoint)aPoint ``` |
| To | ``` - (NSPoint)convertScreenToBase:(NSPoint)point ``` |

Modified [-[NSWindow discardEventsMatchingMask:beforeEvent:]](https://developer.apple.com/documentation/appkit/nswindow/1419676-discardeventsmatchingmask)

|  | Declaration |
| --- | --- |
| From | ``` - (void)discardEventsMatchingMask:(NSUInteger)mask beforeEvent:(NSEvent *)lastEvent ``` |
| To | ``` - (void)discardEventsMatchingMask:(NSEventMask)mask beforeEvent:(NSEvent *)lastEvent ``` |

Modified [-[NSWindow dragImage:at:offset:event:pasteboard:source:slideBack:]](https://developer.apple.com/documentation/appkit/nswindow/1419224-drag)

|  | Declaration |
| --- | --- |
| From | ``` - (void)dragImage:(NSImage *)anImage at:(NSPoint)baseLocation offset:(NSSize)initialOffset event:(NSEvent *)event pasteboard:(NSPasteboard *)pboard source:(id)sourceObj slideBack:(BOOL)slideFlag ``` |
| To | ``` - (void)dragImage:(NSImage *)image at:(NSPoint)baseLocation offset:(NSSize)initialOffset event:(NSEvent *)event pasteboard:(NSPasteboard *)pboard source:(id)sourceObj slideBack:(BOOL)slideFlag ``` |

Modified [-[NSWindow endEditingFor:]](https://developer.apple.com/documentation/appkit/nswindow/1419469-endediting)

|  | Declaration |
| --- | --- |
| From | ``` - (void)endEditingFor:(id)anObject ``` |
| To | ``` - (void)endEditingFor:(id)object ``` |

Modified [-[NSWindow fieldEditor:forObject:]](https://developer.apple.com/documentation/appkit/nswindow/1419647-fieldeditor)

|  | Declaration |
| --- | --- |
| From | ``` - (NSText *)fieldEditor:(BOOL)createFlag forObject:(id)anObject ``` |
| To | ``` - (NSText *)fieldEditor:(BOOL)createFlag forObject:(id)object ``` |

Modified [+[NSWindow frameRectForContentRect:styleMask:]](https://developer.apple.com/documentation/appkit/nswindow/1419372-framerectforcontentrect)

|  | Declaration |
| --- | --- |
| From | ``` + (NSRect)frameRectForContentRect:(NSRect)cRect styleMask:(NSUInteger)aStyle ``` |
| To | ``` + (NSRect)frameRectForContentRect:(NSRect)cRect styleMask:(NSWindowStyleMask)style ``` |

Modified [-[NSWindow initWithContentRect:styleMask:backing:defer:]](https://developer.apple.com/documentation/appkit/nswindow/1419477-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithContentRect:(NSRect)contentRect styleMask:(NSUInteger)aStyle backing:(NSBackingStoreType)bufferingType defer:(BOOL)flag ``` | -- |
| To | ``` - (instancetype)initWithContentRect:(NSRect)contentRect styleMask:(NSWindowStyleMask)style backing:(NSBackingStoreType)bufferingType defer:(BOOL)flag ``` | yes |

Modified [-[NSWindow initWithContentRect:styleMask:backing:defer:screen:]](https://developer.apple.com/documentation/appkit/nswindow/1419755-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithContentRect:(NSRect)contentRect styleMask:(NSUInteger)aStyle backing:(NSBackingStoreType)bufferingType defer:(BOOL)flag screen:(NSScreen *)screen ``` |
| To | ``` - (instancetype)initWithContentRect:(NSRect)contentRect styleMask:(NSWindowStyleMask)style backing:(NSBackingStoreType)bufferingType defer:(BOOL)flag screen:(NSScreen *)screen ``` |

Modified [-[NSWindow invalidateCursorRectsForView:]](https://developer.apple.com/documentation/appkit/nswindow/1419601-invalidatecursorrects)

|  | Declaration |
| --- | --- |
| From | ``` - (void)invalidateCursorRectsForView:(NSView *)aView ``` |
| To | ``` - (void)invalidateCursorRectsForView:(NSView *)view ``` |

Modified [-[NSWindow keyDown:]](https://developer.apple.com/documentation/appkit/nswindow/1419200-keydown)

|  | Declaration |
| --- | --- |
| From | ``` - (void)keyDown:(NSEvent *)theEvent ``` |
| To | ``` - (void)keyDown:(NSEvent *)event ``` |

Modified [-[NSWindow makeFirstResponder:]](https://developer.apple.com/documentation/appkit/nswindow/1419366-makefirstresponder)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)makeFirstResponder:(NSResponder *)aResponder ``` |
| To | ``` - (BOOL)makeFirstResponder:(NSResponder *)responder ``` |

Modified [+[NSWindow minFrameWidthWithTitle:styleMask:]](https://developer.apple.com/documentation/appkit/nswindow/1419294-minframewidth)

|  | Declaration |
| --- | --- |
| From | ``` + (CGFloat)minFrameWidthWithTitle:(NSString *)aTitle styleMask:(NSUInteger)aStyle ``` |
| To | ``` + (CGFloat)minFrameWidthWithTitle:(NSString *)title styleMask:(NSWindowStyleMask)style ``` |

Modified [-[NSWindow nextEventMatchingMask:]](https://developer.apple.com/documentation/appkit/nswindow/1419304-nextevent)

|  | Declaration |
| --- | --- |
| From | ``` - (NSEvent *)nextEventMatchingMask:(NSUInteger)mask ``` |
| To | ``` - (NSEvent *)nextEventMatchingMask:(NSEventMask)mask ``` |

Modified [-[NSWindow nextEventMatchingMask:untilDate:inMode:dequeue:]](https://developer.apple.com/documentation/appkit/nswindow/1419721-nextevent)

|  | Declaration |
| --- | --- |
| From | ``` - (NSEvent *)nextEventMatchingMask:(NSUInteger)mask untilDate:(NSDate *)expiration inMode:(NSString *)mode dequeue:(BOOL)deqFlag ``` |
| To | ``` - (NSEvent *)nextEventMatchingMask:(NSEventMask)mask untilDate:(NSDate *)expiration inMode:(NSRunLoopMode)mode dequeue:(BOOL)deqFlag ``` |

Modified [-[NSWindow selectKeyViewFollowingView:]](https://developer.apple.com/documentation/appkit/nswindow/1419633-selectkeyview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)selectKeyViewFollowingView:(NSView *)aView ``` |
| To | ``` - (void)selectKeyViewFollowingView:(NSView *)view ``` |

Modified [-[NSWindow selectKeyViewPrecedingView:]](https://developer.apple.com/documentation/appkit/nswindow/1419757-selectkeyviewprecedingview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)selectKeyViewPrecedingView:(NSView *)aView ``` |
| To | ``` - (void)selectKeyViewPrecedingView:(NSView *)view ``` |

Modified [-[NSWindow sendEvent:]](https://developer.apple.com/documentation/appkit/nswindow/1419228-sendevent)

|  | Declaration |
| --- | --- |
| From | ``` - (void)sendEvent:(NSEvent *)theEvent ``` |
| To | ``` - (void)sendEvent:(NSEvent *)event ``` |

Modified [-[NSWindow setContentSize:]](https://developer.apple.com/documentation/appkit/nswindow/1419100-setcontentsize)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setContentSize:(NSSize)aSize ``` |
| To | ``` - (void)setContentSize:(NSSize)size ``` |

Modified [-[NSWindow setFrameOrigin:]](https://developer.apple.com/documentation/appkit/nswindow/1419690-setframeorigin)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setFrameOrigin:(NSPoint)aPoint ``` |
| To | ``` - (void)setFrameOrigin:(NSPoint)point ``` |

Modified [-[NSWindow setFrameTopLeftPoint:]](https://developer.apple.com/documentation/appkit/nswindow/1419658-setframetopleftpoint)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setFrameTopLeftPoint:(NSPoint)aPoint ``` |
| To | ``` - (void)setFrameTopLeftPoint:(NSPoint)point ``` |

Modified [+[NSWindow standardWindowButton:forStyleMask:]](https://developer.apple.com/documentation/appkit/nswindow/1419173-standardwindowbutton)

|  | Declaration |
| --- | --- |
| From | ``` + (NSButton *)standardWindowButton:(NSWindowButton)b forStyleMask:(NSUInteger)styleMask ``` |
| To | ``` + (NSButton *)standardWindowButton:(NSWindowButton)b forStyleMask:(NSWindowStyleMask)styleMask ``` |

Modified [NSWindow.styleMask](https://developer.apple.com/documentation/appkit/nswindow/1419078-stylemask)

|  | Declaration |
| --- | --- |
| From | ``` @property NSUInteger styleMask ``` |
| To | ``` @property NSWindowStyleMask styleMask ``` |

Modified [-[NSWindow tryToPerform:with:]](https://developer.apple.com/documentation/appkit/nswindow/1419428-trytoperform)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)tryToPerform:(SEL)anAction with:(id)anObject ``` |
| To | ``` - (BOOL)tryToPerform:(SEL)action with:(id)object ``` |

Modified [NSWindowFullScreenButton](https://developer.apple.com/documentation/appkit/nswindowfullscreenbutton)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### NSWorkspace.h

Modified [-[NSWorkspace openFile:fromImage:at:inView:]](https://developer.apple.com/documentation/appkit/nsworkspace/1533605-openfile)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)openFile:(NSString *)fullPath fromImage:(NSImage *)anImage at:(NSPoint)point inView:(NSView *)aView ``` |
| To | ``` - (BOOL)openFile:(NSString *)fullPath fromImage:(NSImage *)image at:(NSPoint)point inView:(NSView *)view ``` |

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
