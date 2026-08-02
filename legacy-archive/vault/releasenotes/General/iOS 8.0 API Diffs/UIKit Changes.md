---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/UIKit.html
archived_at: '2026-07-18T02:56:01.272576Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# UIKit Changes

## UIKit

NSAttributedString.hModified [-[NSAttributedString initWithData:options:documentAttributes:error:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1524613-initwithdata)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(NSData *)data options:(NSDictionary *)options documentAttributes:(NSDictionary **)dict error:(NSError **)error ``` |
| To | ``` - (instancetype)initWithData:(NSData *)data options:(NSDictionary *)options documentAttributes:(NSDictionary **)dict error:(NSError **)error ``` |

Modified [-[NSAttributedString initWithFileURL:options:documentAttributes:error:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1620492-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFileURL:(NSURL *)url options:(NSDictionary *)options documentAttributes:(NSDictionary **)dict error:(NSError **)error ``` |
| To | ``` - (instancetype)initWithFileURL:(NSURL *)url options:(NSDictionary *)options documentAttributes:(NSDictionary **)dict error:(NSError **)error ``` |

NSFileProviderExtension.h (Added)Added [NSFileProviderExtension](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension)Added [-[NSFileProviderExtension URLForItemWithPersistentIdentifier:]](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/1623481-urlforitemwithpersistentidentifi)Added [-[NSFileProviderExtension documentStorageURL]](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/1623476-documentstorageurl)Added [-[NSFileProviderExtension itemChangedAtURL:]](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/1623474-itemchanged)Added [-[NSFileProviderExtension persistentIdentifierForItemAtURL:]](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/1623479-persistentidentifierforitematurl)Added [+[NSFileProviderExtension placeholderURLForURL:]](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/1623477-placeholderurl)Added [-[NSFileProviderExtension providePlaceholderAtURL:completionHandler:]](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/1623483-provideplaceholderaturl)Added [-[NSFileProviderExtension providerIdentifier]](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/1623473-provideridentifier)Added [-[NSFileProviderExtension startProvidingItemAtURL:completionHandler:]](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/1623482-startprovidingitematurl)Added [-[NSFileProviderExtension stopProvidingItemAtURL:]](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/1623480-stopprovidingitematurl)Added [+[NSFileProviderExtension writePlaceholderAtURL:withMetadata:error:]](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/1623475-writeplaceholderaturl)NSLayoutConstraint.hRemoved UILayoutPriorityDefaultHighRemoved UILayoutPriorityDefaultLowRemoved UILayoutPriorityFittingSizeLevelRemoved UILayoutPriorityRequiredAdded [+[NSLayoutConstraint activateConstraints:]](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526955-activate)Added [NSLayoutConstraint.active](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1527000-isactive)Added [+[NSLayoutConstraint deactivateConstraints:]](https://developer.apple.com/documentation/uikit/nslayoutconstraint/1526066-deactivateconstraints)Added [NSLayoutConstraint.identifier](https://developer.apple.com/documentation/uikit/nslayoutconstraint/1526879-identifier)Added [NSLayoutAttributeBottomMargin](https://developer.apple.com/documentation/uikit/nslayoutattribute/nslayoutattributebottommargin)Added [NSLayoutAttributeCenterXWithinMargins](https://developer.apple.com/documentation/uikit/nslayoutattribute/nslayoutattributecenterxwithinmargins)Added [NSLayoutAttributeCenterYWithinMargins](https://developer.apple.com/documentation/uikit/nslayoutattribute/nslayoutattributecenterywithinmargins)Added [NSLayoutAttributeFirstBaseline](https://developer.apple.com/documentation/appkit/nslayoutattribute/nslayoutattributefirstbaseline)Added [NSLayoutAttributeLastBaseline](https://developer.apple.com/documentation/appkit/nslayoutconstraint/attribute/lastbaseline)Added [NSLayoutAttributeLeadingMargin](https://developer.apple.com/documentation/uikit/nslayoutattribute/nslayoutattributeleadingmargin)Added [NSLayoutAttributeLeftMargin](https://developer.apple.com/documentation/uikit/nslayoutattribute/nslayoutattributeleftmargin)Added [NSLayoutAttributeRightMargin](https://developer.apple.com/documentation/uikit/nslayoutattribute/nslayoutattributerightmargin)Added [NSLayoutAttributeTopMargin](https://developer.apple.com/documentation/uikit/nslayoutattribute/nslayoutattributetopmargin)Added [NSLayoutAttributeTrailingMargin](https://developer.apple.com/documentation/uikit/nslayoutattribute/nslayoutattributetrailingmargin)Added NSLayoutConstraint(NSIdentifier)Added [NSLayoutFormatAlignAllFirstBaseline](https://developer.apple.com/documentation/appkit/nslayoutformatoptions/nslayoutformatalignallfirstbaseline)Added [NSLayoutFormatAlignAllLastBaseline](https://developer.apple.com/documentation/appkit/nslayoutformatoptions/nslayoutformatalignalllastbaseline)Added [UILayoutPriorityDefaultHigh](https://developer.apple.com/documentation/uikit/uilayoutpriority/1622249-defaulthigh)Added [UILayoutPriorityDefaultLow](https://developer.apple.com/documentation/uikit/uilayoutprioritydefaultlow)Added [UILayoutPriorityFittingSizeLevel](https://developer.apple.com/documentation/uikit/uilayoutpriority/1622248-fittingsizelevel)Added [UILayoutPriorityRequired](https://developer.apple.com/documentation/uikit/uilayoutpriorityrequired)Modified [+[NSLayoutConstraint constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:]](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526954-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)constraintWithItem:(id)view1 attribute:(NSLayoutAttribute)attr1 relatedBy:(NSLayoutRelation)relation toItem:(id)view2 attribute:(NSLayoutAttribute)attr2 multiplier:(CGFloat)multiplier constant:(CGFloat)c ``` |
| To | ``` + (instancetype)constraintWithItem:(id)view1 attribute:(NSLayoutAttribute)attr1 relatedBy:(NSLayoutRelation)relation toItem:(id)view2 attribute:(NSLayoutAttribute)attr2 multiplier:(CGFloat)multiplier constant:(CGFloat)c ``` |

NSLayoutManager.hModified [-[NSLayoutManagerDelegate layoutManager:boundingBoxForControlGlyphAtIndex:forTextContainer:proposedLineFragment:glyphPosition:characterIndex:]](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/1402922-layoutmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSLayoutManagerDelegate layoutManager:didCompleteLayoutForTextContainer:atEnd:]](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/1402926-layoutmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSLayoutManagerDelegate layoutManager:lineSpacingAfterGlyphAtIndex:withProposedLineFragmentRect:]](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/1402948-layoutmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSLayoutManagerDelegate layoutManager:paragraphSpacingAfterGlyphAtIndex:withProposedLineFragmentRect:]](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/1403076-layoutmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSLayoutManagerDelegate layoutManager:paragraphSpacingBeforeGlyphAtIndex:withProposedLineFragmentRect:]](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/1403177-layoutmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSLayoutManagerDelegate layoutManager:shouldBreakLineByHyphenatingBeforeCharacterAtIndex:]](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/1403128-layoutmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSLayoutManagerDelegate layoutManager:shouldBreakLineByWordBeforeCharacterAtIndex:]](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/1403051-layoutmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSLayoutManagerDelegate layoutManager:shouldGenerateGlyphs:properties:characterIndexes:font:forGlyphRange:]](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/1403073-layoutmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSLayoutManagerDelegate layoutManager:shouldUseAction:forControlCharacterAtIndex:]](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/1403167-layoutmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSLayoutManagerDelegate layoutManager:textContainer:didChangeGeometryFromSize:]](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/1403049-layoutmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSLayoutManagerDelegate layoutManagerDidInvalidateLayout:]](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/1402993-layoutmanagerdidinvalidatelayout)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSParagraphStyle.hModified [-[NSTextTab initWithTextAlignment:location:options:]](https://developer.apple.com/documentation/uikit/nstexttab/1526080-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTextAlignment:(NSTextAlignment)alignment location:(CGFloat)loc options:(NSDictionary *)options ``` |
| To | ``` - (instancetype)initWithTextAlignment:(NSTextAlignment)alignment location:(CGFloat)loc options:(NSDictionary *)options ``` |

NSTextAttachment.hModified [-[NSTextAttachment initWithData:ofType:]](https://developer.apple.com/documentation/appkit/nstextattachment/1508374-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(NSData *)contentData ofType:(NSString *)uti ``` |
| To | ``` - (instancetype)initWithData:(NSData *)contentData ofType:(NSString *)uti ``` |

NSTextContainer.hModified [-[NSTextContainer initWithSize:]](https://developer.apple.com/documentation/uikit/nstextcontainer/1444529-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithSize:(CGSize)size ``` |
| To | ``` - (instancetype)initWithSize:(CGSize)size ``` |

NSTextStorage.hModified [-[NSTextStorageDelegate textStorage:didProcessEditing:range:changeInLength:]](https://developer.apple.com/documentation/uikit/nstextstoragedelegate/1534375-textstorage)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextStorageDelegate textStorage:willProcessEditing:range:changeInLength:]](https://developer.apple.com/documentation/uikit/nstextstoragedelegate/1534795-textstorage)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UIAccelerometer.hModified [-[UIAccelerometerDelegate accelerometer:didAccelerate:]](https://developer.apple.com/documentation/uikit/uiaccelerometerdelegate/1620653-accelerometer)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UIAccessibility.hAdded [NSObject.accessibilityCustomActions](https://developer.apple.com/documentation/objectivec/nsobject/1615150-accessibilitycustomactions)Added [NSObject.accessibilityElements](https://developer.apple.com/documentation/objectivec/nsobject/1615147-accessibilityelements)Added [NSObject.accessibilityNavigationStyle](https://developer.apple.com/documentation/objectivec/nsobject/1615200-accessibilitynavigationstyle)Added [UIAccessibilityBoldTextStatusDidChangeNotification](https://developer.apple.com/documentation/uikit/uiaccessibility/1615152-boldtextstatusdidchangenotificat)Added [UIAccessibilityDarkerSystemColorsEnabled()](https://developer.apple.com/documentation/uikit/1615087-uiaccessibilitydarkersystemcolor)Added [UIAccessibilityDarkerSystemColorsStatusDidChangeNotification](https://developer.apple.com/documentation/uikit/uiaccessibility/1615177-darkersystemcolorsstatusdidchang)Added [UIAccessibilityGrayscaleStatusDidChangeNotification](https://developer.apple.com/documentation/uikit/uiaccessibilitygrayscalestatusdidchangenotification)Added [UIAccessibilityIsBoldTextEnabled()](https://developer.apple.com/documentation/uikit/uiaccessibility/1615156-isboldtextenabled)Added [UIAccessibilityIsGrayscaleEnabled()](https://developer.apple.com/documentation/uikit/1615189-uiaccessibilityisgrayscaleenable)Added [UIAccessibilityIsReduceMotionEnabled()](https://developer.apple.com/documentation/uikit/uiaccessibility/1615133-isreducemotionenabled)Added [UIAccessibilityIsReduceTransparencyEnabled()](https://developer.apple.com/documentation/uikit/uiaccessibility/1615074-isreducetransparencyenabled)Added [UIAccessibilityIsSpeakScreenEnabled()](https://developer.apple.com/documentation/uikit/1615109-uiaccessibilityisspeakscreenenab)Added [UIAccessibilityIsSpeakSelectionEnabled()](https://developer.apple.com/documentation/uikit/1615154-uiaccessibilityisspeakselectione)Added [UIAccessibilityIsSwitchControlRunning()](https://developer.apple.com/documentation/uikit/1615131-uiaccessibilityisswitchcontrolru)Added [UIAccessibilityReduceMotionStatusDidChangeNotification](https://developer.apple.com/documentation/uikit/uiaccessibility/1615204-reducemotionstatusdidchangenotif)Added [UIAccessibilityReduceTransparencyStatusDidChangeNotification](https://developer.apple.com/documentation/uikit/uiaccessibility/1615125-reducetransparencystatusdidchang)Added [UIAccessibilitySpeakScreenStatusDidChangeNotification](https://developer.apple.com/documentation/uikit/uiaccessibilityspeakscreenstatusdidchangenotification)Added [UIAccessibilitySpeakSelectionStatusDidChangeNotification](https://developer.apple.com/documentation/uikit/uiaccessibility/1615127-speakselectionstatusdidchangenot)Added [UIAccessibilitySwitchControlStatusDidChangeNotification](https://developer.apple.com/documentation/uikit/uiaccessibility/1615099-switchcontrolstatusdidchangenoti)UIAccessibilityAdditions.hModified [-[UIPickerViewAccessibilityDelegate pickerView:accessibilityHintForComponent:]](https://developer.apple.com/documentation/uikit/uipickerviewaccessibilitydelegate/1621056-pickerview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPickerViewAccessibilityDelegate pickerView:accessibilityLabelForComponent:]](https://developer.apple.com/documentation/uikit/uipickerviewaccessibilitydelegate/1621052-pickerview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIScrollViewAccessibilityDelegate accessibilityScrollStatusForScrollView:]](https://developer.apple.com/documentation/uikit/uiscrollviewaccessibilitydelegate/1621055-accessibilityscrollstatus)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UIAccessibilityConstants.hAdded [UIAccessibilityNavigationStyle](https://developer.apple.com/documentation/uikit/uiaccessibilitynavigationstyle)Added [UIAccessibilityNavigationStyleAutomatic](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilitynavigationstyle/automatic)Added [UIAccessibilityNavigationStyleCombined](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilitynavigationstyle/combined)Added [UIAccessibilityNavigationStyleSeparate](https://developer.apple.com/documentation/uikit/uiaccessibilitynavigationstyle/uiaccessibilitynavigationstyleseparate)Added [UIAccessibilityNotificationSwitchControlIdentifier](https://developer.apple.com/documentation/uikit/uiaccessibility/assistivetechnologyidentifier/1620191-notificationswitchcontrol)Added [UIAccessibilityPauseAssistiveTechnologyNotification](https://developer.apple.com/documentation/uikit/uiaccessibility/notification/1620192-pauseassistivetechnology)Added [UIAccessibilityResumeAssistiveTechnologyNotification](https://developer.apple.com/documentation/uikit/uiaccessibilityresumeassistivetechnologynotification)UIAccessibilityCustomAction.h (Added)Added [UIAccessibilityCustomAction](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction)Added [-[UIAccessibilityCustomAction initWithName:target:selector:]](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/1620499-initwithname)Added [UIAccessibilityCustomAction.name](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/1620502-name)Added [UIAccessibilityCustomAction.selector](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/1620498-selector)Added [UIAccessibilityCustomAction.target](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/1620501-target)UIAccessibilityElement.hModified [-[UIAccessibilityElement initWithAccessibilityContainer:]](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/1619582-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithAccessibilityContainer:(id)container ``` |
| To | ``` - (instancetype)initWithAccessibilityContainer:(id)container ``` |

UIAccessibilityIdentification.hAdded UIBarItem(UIAccessibility)UIActionSheet.hModified [-[UIActionSheet initWithTitle:delegate:cancelButtonTitle:destructiveButtonTitle:otherButtonTitles:]](https://developer.apple.com/documentation/uikit/uiactionsheet/1622875-initwithtitle)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTitle:(NSString *)title delegate:(id<UIActionSheetDelegate>)delegate cancelButtonTitle:(NSString *)cancelButtonTitle destructiveButtonTitle:(NSString *)destructiveButtonTitle otherButtonTitles:(NSString *)otherButtonTitles, ... ``` |
| To | ``` - (instancetype)initWithTitle:(NSString *)title delegate:(id<UIActionSheetDelegate>)delegate cancelButtonTitle:(NSString *)cancelButtonTitle destructiveButtonTitle:(NSString *)destructiveButtonTitle otherButtonTitles:(NSString *)otherButtonTitles, ... ``` |

Modified [-[UIActionSheetDelegate actionSheet:clickedButtonAtIndex:]](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/1622876-actionsheet)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIActionSheetDelegate actionSheet:didDismissWithButtonIndex:]](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/1622879-actionsheet)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIActionSheetDelegate actionSheet:willDismissWithButtonIndex:]](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/1622884-actionsheet)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIActionSheetDelegate actionSheetCancel:]](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/1622867-actionsheetcancel)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIActionSheetDelegate didPresentActionSheet:]](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/1622877-didpresent)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIActionSheetDelegate willPresentActionSheet:]](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/1622865-willpresentactionsheet)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UIActivityIndicatorView.hModified [-[UIActivityIndicatorView initWithActivityIndicatorStyle:]](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/1622840-initwithactivityindicatorstyle)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithActivityIndicatorStyle:(UIActivityIndicatorViewStyle)style ``` |
| To | ``` - (instancetype)initWithActivityIndicatorStyle:(UIActivityIndicatorViewStyle)style ``` |

UIActivityItemProvider.hModified [-[UIActivityItemProvider initWithPlaceholderItem:]](https://developer.apple.com/documentation/uikit/uiactivityitemprovider/1620463-initwithplaceholderitem)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithPlaceholderItem:(id)placeholderItem ``` |
| To | ``` - (instancetype)initWithPlaceholderItem:(id)placeholderItem ``` |

Modified [-[UIActivityItemSource activityViewController:dataTypeIdentifierForActivityType:]](https://developer.apple.com/documentation/uikit/uiactivityitemsource/1620456-activityviewcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIActivityItemSource activityViewController:subjectForActivityType:]](https://developer.apple.com/documentation/uikit/uiactivityitemsource/1620455-activityviewcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIActivityItemSource activityViewController:thumbnailImageForActivityType:suggestedSize:]](https://developer.apple.com/documentation/uikit/uiactivityitemsource/1620462-activityviewcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UIActivityViewController.hAdded [UIActivityViewController.completionWithItemsHandler](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/1622022-completionwithitemshandler)Added [UIActivityViewControllerCompletionWithItemsHandler](https://developer.apple.com/documentation/uikit/uiactivityviewcontrollercompletionwithitemshandler)Modified [UIActivityViewController.completionHandler](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/1622010-completionhandler)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [-[UIActivityViewController initWithActivityItems:applicationActivities:]](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/1622019-initwithactivityitems)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithActivityItems:(NSArray *)activityItems applicationActivities:(NSArray *)applicationActivities ``` |
| To | ``` - (instancetype)initWithActivityItems:(NSArray *)activityItems applicationActivities:(NSArray *)applicationActivities ``` |

UIAlertController.h (Added)Added [UIAlertAction](https://developer.apple.com/documentation/uikit/uialertaction)Added [+[UIAlertAction actionWithTitle:style:handler:]](https://developer.apple.com/documentation/uikit/uialertaction/1620097-actionwithtitle)Added [UIAlertAction.enabled](https://developer.apple.com/documentation/uikit/uialertaction/1620109-enabled)Added [UIAlertAction.style](https://developer.apple.com/documentation/uikit/uialertaction/1620107-style)Added [UIAlertAction.title](https://developer.apple.com/documentation/uikit/uialertaction/1620098-title)Added [UIAlertController](https://developer.apple.com/documentation/uikit/uialertcontroller)Added [UIAlertController.actions](https://developer.apple.com/documentation/uikit/uialertcontroller/1620099-actions)Added [-[UIAlertController addAction:]](https://developer.apple.com/documentation/uikit/uialertcontroller/1620094-addaction)Added [-[UIAlertController addTextFieldWithConfigurationHandler:]](https://developer.apple.com/documentation/uikit/uialertcontroller/1620093-addtextfieldwithconfigurationhan)Added [+[UIAlertController alertControllerWithTitle:message:preferredStyle:]](https://developer.apple.com/documentation/uikit/uialertcontroller/1620092-alertcontrollerwithtitle)Added [UIAlertController.message](https://developer.apple.com/documentation/uikit/uialertcontroller/1620106-message)Added [UIAlertController.preferredStyle](https://developer.apple.com/documentation/uikit/uialertcontroller/1620096-preferredstyle)Added [UIAlertController.textFields](https://developer.apple.com/documentation/uikit/uialertcontroller/1620104-textfields)Added [UIAlertController.title](https://developer.apple.com/documentation/uikit/uialertcontroller/1620103-title)Added [UIAlertActionStyle](https://developer.apple.com/documentation/uikit/uialertaction/style)Added [UIAlertActionStyleCancel](https://developer.apple.com/documentation/uikit/uialertactionstyle/uialertactionstylecancel)Added [UIAlertActionStyleDefault](https://developer.apple.com/documentation/uikit/uialertactionstyle/uialertactionstyledefault)Added [UIAlertActionStyleDestructive](https://developer.apple.com/documentation/uikit/uialertactionstyle/uialertactionstyledestructive)Added [UIAlertControllerStyle](https://developer.apple.com/documentation/uikit/uialertcontroller/style)Added [UIAlertControllerStyleActionSheet](https://developer.apple.com/documentation/uikit/uialertcontrollerstyle/uialertcontrollerstyleactionsheet)Added [UIAlertControllerStyleAlert](https://developer.apple.com/documentation/uikit/uialertcontroller/style/alert)UIAlertView.hModified [-[UIAlertView initWithTitle:message:delegate:cancelButtonTitle:otherButtonTitles:]](https://developer.apple.com/documentation/uikit/uialertview/1620765-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTitle:(NSString *)title message:(NSString *)message delegate:(id)delegate cancelButtonTitle:(NSString *)cancelButtonTitle otherButtonTitles:(NSString *)otherButtonTitles, ... ``` |
| To | ``` - (instancetype)initWithTitle:(NSString *)title message:(NSString *)message delegate:(id)delegate cancelButtonTitle:(NSString *)cancelButtonTitle otherButtonTitles:(NSString *)otherButtonTitles, ... ``` |

Modified [-[UIAlertViewDelegate alertView:clickedButtonAtIndex:]](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620752-alertview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIAlertViewDelegate alertView:didDismissWithButtonIndex:]](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620772-alertview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIAlertViewDelegate alertView:willDismissWithButtonIndex:]](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620763-alertview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIAlertViewDelegate alertViewCancel:]](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620778-alertviewcancel)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIAlertViewDelegate alertViewShouldEnableFirstOtherButton:]](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620774-alertviewshouldenablefirstotherb)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIAlertViewDelegate didPresentAlertView:]](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620750-didpresent)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIAlertViewDelegate willPresentAlertView:]](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620767-willpresent)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UIAppearance.hAdded [+[UIAppearance appearanceForTraitCollection:]](https://developer.apple.com/documentation/uikit/uiappearance/1615007-appearancefortraitcollection)Added [+[UIAppearance appearanceForTraitCollection:whenContainedIn:]](https://developer.apple.com/documentation/uikit/uiappearance/1615012-appearancefortraitcollection)Modified [+[UIAppearance appearanceWhenContainedIn:]](https://developer.apple.com/documentation/uikit/uiappearance/1615006-appearancewhencontainedin)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)appearanceWhenContainedIn:(Class<UIAppearanceContainer> *)ContainerClass, ... ``` |
| To | ``` + (instancetype)appearanceWhenContainedIn:(Class<UIAppearanceContainer>)ContainerClass, ... ``` |

UIApplication.hAdded [-[UIApplication currentUserNotificationSettings]](https://developer.apple.com/documentation/uikit/uiapplication/1623092-currentusernotificationsettings)Added [-[UIApplication isRegisteredForRemoteNotifications]](https://developer.apple.com/documentation/uikit/uiapplication/1623069-isregisteredforremotenotificatio)Added [-[UIApplication registerForRemoteNotifications]](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications)Added [-[UIApplication registerUserNotificationSettings:]](https://developer.apple.com/documentation/uikit/uiapplication/1622932-registerusernotificationsettings)Added [-[UIApplicationDelegate application:continueUserActivity:restorationHandler:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623072-application)Added [-[UIApplicationDelegate application:didFailToContinueUserActivityWithType:error:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622927-application)Added [-[UIApplicationDelegate application:didRegisterUserNotificationSettings:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623022-application)Added [-[UIApplicationDelegate application:didUpdateUserActivity:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622963-application)Added [-[UIApplicationDelegate application:handleActionWithIdentifier:forLocalNotification:completionHandler:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623028-application)Added [-[UIApplicationDelegate application:handleActionWithIdentifier:forRemoteNotification:completionHandler:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623068-application)Added [-[UIApplicationDelegate application:shouldAllowExtensionPointIdentifier:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623122-application)Added [-[UIApplicationDelegate application:willContinueUserActivityWithType:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622919-application)Added UIApplication(UIUserNotificationSettings)Added [UIApplicationKeyboardExtensionPointIdentifier](https://developer.apple.com/documentation/uikit/uiapplicationkeyboardextensionpointidentifier)Added [UIApplicationLaunchOptionsUserActivityDictionaryKey](https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey/1623113-useractivitydictionary)Added [UIApplicationLaunchOptionsUserActivityTypeKey](https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey/1622954-useractivitytype)Added [UIApplicationOpenSettingsURLString](https://developer.apple.com/documentation/uikit/uiapplicationopensettingsurlstring)Added [UIInterfaceOrientationUnknown](https://developer.apple.com/documentation/uikit/uiinterfaceorientation/uiinterfaceorientationunknown)Modified [-[UIApplication enabledRemoteNotificationTypes]](https://developer.apple.com/documentation/uikit/uiapplication/1623075-enabledremotenotificationtypes)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [-[UIApplication registerForRemoteNotificationTypes:]](https://developer.apple.com/documentation/uikit/uiapplication/1623010-registerforremotenotificationtyp)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [-[UIApplicationDelegate application:didChangeStatusBarFrame:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622947-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate application:didChangeStatusBarOrientation:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622943-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate application:didDecodeRestorableStateWithCoder:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623006-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate application:didFailToRegisterForRemoteNotificationsWithError:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622962-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate application:didFinishLaunchingWithOptions:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate application:didReceiveLocalNotification:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622930-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate application:didReceiveRemoteNotification:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623117-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate application:didReceiveRemoteNotification:fetchCompletionHandler:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate application:didRegisterForRemoteNotificationsWithDeviceToken:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622958-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate application:handleEventsForBackgroundURLSession:completionHandler:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622941-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate application:handleOpenURL:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622964-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate application:openURL:sourceApplication:annotation:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623073-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate application:performFetchWithCompletionHandler:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623125-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate application:shouldRestoreApplicationState:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622987-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate application:shouldSaveApplicationState:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623089-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate application:supportedInterfaceOrientationsForWindow:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623107-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate application:viewControllerWithRestorationIdentifierPath:coder:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623062-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate application:willChangeStatusBarFrame:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623020-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate application:willChangeStatusBarOrientation:duration:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623054-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate application:willEncodeRestorableStateWithCoder:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623099-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate application:willFinishLaunchingWithOptions:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623032-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate applicationDidBecomeActive:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622956-applicationdidbecomeactive)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate applicationDidEnterBackground:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622997-applicationdidenterbackground)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate applicationDidFinishLaunching:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623053-applicationdidfinishlaunching)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate applicationDidReceiveMemoryWarning:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623063-applicationdidreceivememorywarni)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate applicationProtectedDataDidBecomeAvailable:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623044-applicationprotecteddatadidbecom)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate applicationProtectedDataWillBecomeUnavailable:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623019-applicationprotecteddatawillbeco)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate applicationSignificantTimeChange:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622992-applicationsignificanttimechange)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate applicationWillEnterForeground:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623076-applicationwillenterforeground)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate applicationWillResignActive:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622950-applicationwillresignactive)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIApplicationDelegate applicationWillTerminate:]](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623111-applicationwillterminate)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [UIRemoteNotificationTypeAlert](https://developer.apple.com/documentation/uikit/uiremotenotificationtype/1623004-alert)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [UIRemoteNotificationTypeBadge](https://developer.apple.com/documentation/uikit/uiremotenotificationtype/uiremotenotificationtypebadge)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [UIRemoteNotificationTypeNewsstandContentAvailability](https://developer.apple.com/documentation/uikit/uiremotenotificationtype/1622977-newsstandcontentavailability)

|  | Deprecation | Introduction |
| --- | --- | --- |
| From | -- | iOS 5.0 |
| To | iOS 8.0 | iOS 3.0 |

Modified [UIRemoteNotificationTypeNone](https://developer.apple.com/documentation/uikit/uiremotenotificationtype/uiremotenotificationtypenone)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [UIRemoteNotificationTypeSound](https://developer.apple.com/documentation/uikit/uiremotenotificationtype/1622926-sound)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

UIBarButtonItem.hModified [-[UIBarButtonItem initWithBarButtonSystemItem:target:action:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617153-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithBarButtonSystemItem:(UIBarButtonSystemItem)systemItem target:(id)target action:(SEL)action ``` |
| To | ``` - (instancetype)initWithBarButtonSystemItem:(UIBarButtonSystemItem)systemItem target:(id)target action:(SEL)action ``` |

Modified [-[UIBarButtonItem initWithCustomView:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617151-initwithcustomview)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCustomView:(UIView *)customView ``` |
| To | ``` - (instancetype)initWithCustomView:(UIView *)customView ``` |

Modified [-[UIBarButtonItem initWithImage:landscapeImagePhone:style:target:action:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617118-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithImage:(UIImage *)image landscapeImagePhone:(UIImage *)landscapeImagePhone style:(UIBarButtonItemStyle)style target:(id)target action:(SEL)action ``` |
| To | ``` - (instancetype)initWithImage:(UIImage *)image landscapeImagePhone:(UIImage *)landscapeImagePhone style:(UIBarButtonItemStyle)style target:(id)target action:(SEL)action ``` |

Modified [-[UIBarButtonItem initWithImage:style:target:action:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617163-initwithimage)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithImage:(UIImage *)image style:(UIBarButtonItemStyle)style target:(id)target action:(SEL)action ``` |
| To | ``` - (instancetype)initWithImage:(UIImage *)image style:(UIBarButtonItemStyle)style target:(id)target action:(SEL)action ``` |

Modified [-[UIBarButtonItem initWithTitle:style:target:action:]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617148-initwithtitle)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTitle:(NSString *)title style:(UIBarButtonItemStyle)style target:(id)target action:(SEL)action ``` |
| To | ``` - (instancetype)initWithTitle:(NSString *)title style:(UIBarButtonItemStyle)style target:(id)target action:(SEL)action ``` |

Modified [UIBarButtonItemStyleBordered](https://developer.apple.com/documentation/uikit/uibarbuttonitemstyle/uibarbuttonitemstylebordered)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

UIBarCommon.hAdded [UIBarMetricsCompact](https://developer.apple.com/documentation/uikit/uibarmetrics/compact)Added [UIBarMetricsCompactPrompt](https://developer.apple.com/documentation/uikit/uibarmetrics/compactprompt)Modified [-[UIBarPositioningDelegate positionForBar:]](https://developer.apple.com/documentation/uikit/uibarpositioningdelegate/1624872-positionforbar)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [UIBarMetricsLandscapePhone](https://developer.apple.com/documentation/uikit/uibarmetrics/1624859-landscapephone)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [UIBarMetricsLandscapePhonePrompt](https://developer.apple.com/documentation/uikit/uibarmetrics/uibarmetricslandscapephoneprompt)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

UICollectionView.hAdded [-[UICollectionViewDelegate collectionView:willDisplayCell:forItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618087-collectionview)Added [-[UICollectionViewDelegate collectionView:willDisplaySupplementaryView:forElementKind:atIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618062-collectionview)Modified [-[UICollectionView initWithFrame:collectionViewLayout:]](https://developer.apple.com/documentation/uikit/uicollectionview/1618053-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFrame:(CGRect)frame collectionViewLayout:(UICollectionViewLayout *)layout ``` |
| To | ``` - (instancetype)initWithFrame:(CGRect)frame collectionViewLayout:(UICollectionViewLayout *)layout ``` |

Modified [-[UICollectionViewDataSource collectionView:viewForSupplementaryElementOfKind:atIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/1618037-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollectionViewDataSource numberOfSectionsInCollectionView:]](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/1618023-numberofsections)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollectionViewDelegate collectionView:canPerformAction:forItemAtIndexPath:withSender:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618051-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollectionViewDelegate collectionView:didDeselectItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618035-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollectionViewDelegate collectionView:didEndDisplayingCell:forItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618006-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollectionViewDelegate collectionView:didEndDisplayingSupplementaryView:forElementOfKind:atIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618036-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollectionViewDelegate collectionView:didHighlightItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618049-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollectionViewDelegate collectionView:didSelectItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618032-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollectionViewDelegate collectionView:didUnhighlightItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618027-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollectionViewDelegate collectionView:performAction:forItemAtIndexPath:withSender:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618073-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollectionViewDelegate collectionView:shouldDeselectItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618067-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollectionViewDelegate collectionView:shouldHighlightItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618070-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollectionViewDelegate collectionView:shouldSelectItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618095-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollectionViewDelegate collectionView:shouldShowMenuForItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618010-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollectionViewDelegate collectionView:transitionLayoutForOldLayout:newLayout:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618100-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UICollectionViewCell.hAdded [-[UICollectionReusableView preferredLayoutAttributesFittingAttributes:]](https://developer.apple.com/documentation/uikit/uicollectionreusableview/1620132-preferredlayoutattributesfitting)UICollectionViewController.hModified [-[UICollectionViewController initWithCollectionViewLayout:]](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/1623976-initwithcollectionviewlayout)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCollectionViewLayout:(UICollectionViewLayout *)layout ``` |
| To | ``` - (instancetype)initWithCollectionViewLayout:(UICollectionViewLayout *)layout ``` |

UICollectionViewFlowLayout.hAdded [UICollectionViewFlowLayout.estimatedItemSize](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/1617709-estimateditemsize)Modified [-[UICollectionViewDelegateFlowLayout collectionView:layout:insetForSectionAtIndex:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/1617718-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollectionViewDelegateFlowLayout collectionView:layout:minimumInteritemSpacingForSectionAtIndex:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/1617696-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollectionViewDelegateFlowLayout collectionView:layout:minimumLineSpacingForSectionAtIndex:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/1617705-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollectionViewDelegateFlowLayout collectionView:layout:referenceSizeForFooterInSection:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/1617713-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollectionViewDelegateFlowLayout collectionView:layout:referenceSizeForHeaderInSection:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/1617702-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollectionViewDelegateFlowLayout collectionView:layout:sizeForItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/1617708-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UICollectionViewLayout.hRemoved UICollectionViewLayout(SubclassingHooks)Removed UICollectionViewLayout(UpdateSupportHooks)Added [-[UICollectionViewLayout invalidationContextForPreferredLayoutAttributes:withOriginalAttributes:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617767-invalidationcontextforpreferredl)Added [-[UICollectionViewLayout shouldInvalidateLayoutForPreferredLayoutAttributes:withOriginalAttributes:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617746-shouldinvalidatelayout)Added [UICollectionViewLayoutInvalidationContext.contentOffsetAdjustment](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617731-contentoffsetadjustment)Added [UICollectionViewLayoutInvalidationContext.contentSizeAdjustment](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617763-contentsizeadjustment)Added [-[UICollectionViewLayoutInvalidationContext invalidateDecorationElementsOfKind:atIndexPaths:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617736-invalidatedecorationelements)Added [-[UICollectionViewLayoutInvalidationContext invalidateItemsAtIndexPaths:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617795-invalidateitemsatindexpaths)Added [-[UICollectionViewLayoutInvalidationContext invalidateSupplementaryElementsOfKind:atIndexPaths:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617747-invalidatesupplementaryelements)Added [UICollectionViewLayoutInvalidationContext.invalidatedDecorationIndexPaths](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617805-invalidateddecorationindexpaths)Added [UICollectionViewLayoutInvalidationContext.invalidatedItemIndexPaths](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617723-invalidateditemindexpaths)Added [UICollectionViewLayoutInvalidationContext.invalidatedSupplementaryIndexPaths](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617777-invalidatedsupplementaryindexpat)Added UICollectionViewLayout(UISubclassingHooks)Added UICollectionViewLayout(UIUpdateSupportHooks)Modified [-[UICollectionViewLayout indexPathsToDeleteForDecorationViewOfKind:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617730-indexpathstodeletefordecorationv)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)indexPathsToDeleteForDecorationViewOfKind:(NSString *)kind ``` |
| To | ``` - (NSArray *)indexPathsToDeleteForDecorationViewOfKind:(NSString *)elementKind ``` |

Modified [-[UICollectionViewLayout indexPathsToDeleteForSupplementaryViewOfKind:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617807-indexpathstodeleteforsupplementa)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)indexPathsToDeleteForSupplementaryViewOfKind:(NSString *)kind ``` |
| To | ``` - (NSArray *)indexPathsToDeleteForSupplementaryViewOfKind:(NSString *)elementKind ``` |

Modified [-[UICollectionViewLayout indexPathsToInsertForDecorationViewOfKind:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617750-indexpathstoinsertfordecorationv)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)indexPathsToInsertForDecorationViewOfKind:(NSString *)kind ``` |
| To | ``` - (NSArray *)indexPathsToInsertForDecorationViewOfKind:(NSString *)elementKind ``` |

Modified [-[UICollectionViewLayout indexPathsToInsertForSupplementaryViewOfKind:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617770-indexpathstoinsertforsupplementa)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)indexPathsToInsertForSupplementaryViewOfKind:(NSString *)kind ``` |
| To | ``` - (NSArray *)indexPathsToInsertForSupplementaryViewOfKind:(NSString *)elementKind ``` |

Modified [-[UICollectionViewLayout layoutAttributesForDecorationViewOfKind:atIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617809-layoutattributesfordecorationvie)

|  | Declaration |
| --- | --- |
| From | ``` - (UICollectionViewLayoutAttributes *)layoutAttributesForDecorationViewOfKind:(NSString *)decorationViewKind atIndexPath:(NSIndexPath *)indexPath ``` |
| To | ``` - (UICollectionViewLayoutAttributes *)layoutAttributesForDecorationViewOfKind:(NSString *)elementKind atIndexPath:(NSIndexPath *)indexPath ``` |

Modified [-[UICollectionViewLayout layoutAttributesForSupplementaryViewOfKind:atIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617792-layoutattributesforsupplementary)

|  | Declaration |
| --- | --- |
| From | ``` - (UICollectionViewLayoutAttributes *)layoutAttributesForSupplementaryViewOfKind:(NSString *)kind atIndexPath:(NSIndexPath *)indexPath ``` |
| To | ``` - (UICollectionViewLayoutAttributes *)layoutAttributesForSupplementaryViewOfKind:(NSString *)elementKind atIndexPath:(NSIndexPath *)indexPath ``` |

Modified [-[UICollectionViewLayout registerClass:forDecorationViewOfKind:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617739-registerclass)

|  | Declaration |
| --- | --- |
| From | ``` - (void)registerClass:(Class)viewClass forDecorationViewOfKind:(NSString *)decorationViewKind ``` |
| To | ``` - (void)registerClass:(Class)viewClass forDecorationViewOfKind:(NSString *)elementKind ``` |

Modified [-[UICollectionViewLayout registerNib:forDecorationViewOfKind:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617732-registernib)

|  | Declaration |
| --- | --- |
| From | ``` - (void)registerNib:(UINib *)nib forDecorationViewOfKind:(NSString *)decorationViewKind ``` |
| To | ``` - (void)registerNib:(UINib *)nib forDecorationViewOfKind:(NSString *)elementKind ``` |

UICollectionViewTransitionLayout.hModified [-[UICollectionViewTransitionLayout initWithCurrentLayout:nextLayout:]](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/1622189-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCurrentLayout:(UICollectionViewLayout *)currentLayout nextLayout:(UICollectionViewLayout *)newLayout ``` |
| To | ``` - (instancetype)initWithCurrentLayout:(UICollectionViewLayout *)currentLayout nextLayout:(UICollectionViewLayout *)newLayout ``` |

UICollisionBehavior.hModified [-[UICollisionBehaviorDelegate collisionBehavior:beganContactForItem:withBoundaryIdentifier:atPoint:]](https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate/1624816-collisionbehavior)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollisionBehaviorDelegate collisionBehavior:beganContactForItem:withItem:atPoint:]](https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate/1624835-collisionbehavior)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollisionBehaviorDelegate collisionBehavior:endedContactForItem:withBoundaryIdentifier:]](https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate/1624834-collisionbehavior)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UICollisionBehaviorDelegate collisionBehavior:endedContactForItem:withItem:]](https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate/1624833-collisionbehavior)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UIColor.hModified [-[CIColor initWithColor:]](https://developer.apple.com/documentation/coreimage/cicolor/1528762-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithColor:(UIColor *)color ``` |
| To | ``` - (instancetype)initWithColor:(UIColor *)color ``` |

UIDevice.hAdded [UIUserInterfaceIdiomUnspecified](https://developer.apple.com/documentation/uikit/uiuserinterfaceidiom/uiuserinterfaceidiomunspecified)UIDocument.hAdded [-[UIDocument restoreUserActivityState:]](https://developer.apple.com/documentation/uikit/uidocument/1619973-restoreuseractivitystate)Added [-[UIDocument updateUserActivityState:]](https://developer.apple.com/documentation/uikit/uidocument/1619986-updateuseractivitystate)Added [UIDocument.userActivity](https://developer.apple.com/documentation/uikit/uidocument/1619963-useractivity)Added [NSUserActivityDocumentURLKey](https://developer.apple.com/documentation/appkit/useractivityurlkey)Added UIDocument(ActivityContinuation)Modified [-[UIDocument initWithFileURL:]](https://developer.apple.com/documentation/uikit/uidocument/1619979-initwithfileurl)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFileURL:(NSURL *)url ``` |
| To | ``` - (instancetype)initWithFileURL:(NSURL *)url ``` |

UIDocumentInteractionController.hModified [-[UIDocumentInteractionControllerDelegate documentInteractionController:canPerformAction:]](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616800-documentinteractioncontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIDocumentInteractionControllerDelegate documentInteractionController:didEndSendingToApplication:]](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616824-documentinteractioncontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIDocumentInteractionControllerDelegate documentInteractionController:performAction:]](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616823-documentinteractioncontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIDocumentInteractionControllerDelegate documentInteractionController:willBeginSendingToApplication:]](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616825-documentinteractioncontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIDocumentInteractionControllerDelegate documentInteractionControllerDidDismissOpenInMenu:]](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616826-documentinteractioncontrollerdid)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIDocumentInteractionControllerDelegate documentInteractionControllerDidDismissOptionsMenu:]](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616803-documentinteractioncontrollerdid)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIDocumentInteractionControllerDelegate documentInteractionControllerDidEndPreview:]](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616809-documentinteractioncontrollerdid)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIDocumentInteractionControllerDelegate documentInteractionControllerRectForPreview:]](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616805-documentinteractioncontrollerrec)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIDocumentInteractionControllerDelegate documentInteractionControllerViewControllerForPreview:]](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616799-documentinteractioncontrollervie)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIDocumentInteractionControllerDelegate documentInteractionControllerViewForPreview:]](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616819-documentinteractioncontrollervie)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIDocumentInteractionControllerDelegate documentInteractionControllerWillBeginPreview:]](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616806-documentinteractioncontrollerwil)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIDocumentInteractionControllerDelegate documentInteractionControllerWillPresentOpenInMenu:]](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616818-documentinteractioncontrollerwil)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIDocumentInteractionControllerDelegate documentInteractionControllerWillPresentOptionsMenu:]](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616822-documentinteractioncontrollerwil)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UIDocumentMenuViewController.h (Added)Added [UIDocumentMenuDelegate](https://developer.apple.com/documentation/uikit/uidocumentmenudelegate)Added [-[UIDocumentMenuDelegate documentMenu:didPickDocumentPicker:]](https://developer.apple.com/documentation/uikit/uidocumentmenudelegate/1614188-documentmenu)Added [-[UIDocumentMenuDelegate documentMenuWasCancelled:]](https://developer.apple.com/documentation/uikit/uidocumentmenudelegate/1614190-documentmenuwascancelled)Added [UIDocumentMenuViewController](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller)Added [-[UIDocumentMenuViewController addOptionWithTitle:image:order:handler:]](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/1614193-addoption)Added [UIDocumentMenuViewController.delegate](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/1614192-delegate)Added [-[UIDocumentMenuViewController initWithDocumentTypes:inMode:]](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/1614187-init)Added [-[UIDocumentMenuViewController initWithURL:inMode:]](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/1614191-init)Added [UIDocumentMenuOrder](https://developer.apple.com/documentation/uikit/uidocumentmenuorder)Added [UIDocumentMenuOrderFirst](https://developer.apple.com/documentation/uikit/uidocumentmenuorder/first)Added [UIDocumentMenuOrderLast](https://developer.apple.com/documentation/uikit/uidocumentmenuorder/last)UIDocumentPickerExtensionViewController.h (Added)Added [UIDocumentPickerExtensionViewController](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller)Added [-[UIDocumentPickerExtensionViewController dismissGrantingAccessToURL:]](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/1614391-dismissgrantingaccesstourl)Added [UIDocumentPickerExtensionViewController.documentPickerMode](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/1614393-documentpickermode)Added [UIDocumentPickerExtensionViewController.documentStorageURL](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/1614390-documentstorageurl)Added [UIDocumentPickerExtensionViewController.originalURL](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/1614392-originalurl)Added [-[UIDocumentPickerExtensionViewController prepareForPresentationInMode:]](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/1614395-prepareforpresentationinmode)Added [UIDocumentPickerExtensionViewController.providerIdentifier](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/1614396-provideridentifier)Added [UIDocumentPickerExtensionViewController.validTypes](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/1614394-validtypes)UIDocumentPickerViewController.h (Added)Added [UIDocumentPickerDelegate](https://developer.apple.com/documentation/uikit/uidocumentpickerdelegate)Added [-[UIDocumentPickerDelegate documentPicker:didPickDocumentAtURL:]](https://developer.apple.com/documentation/uikit/uidocumentpickerdelegate/1618680-documentpicker)Added [-[UIDocumentPickerDelegate documentPickerWasCancelled:]](https://developer.apple.com/documentation/uikit/uidocumentpickerdelegate/1618679-documentpickerwascancelled)Added [UIDocumentPickerViewController](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller)Added [UIDocumentPickerViewController.delegate](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/1618690-delegate)Added [UIDocumentPickerViewController.documentPickerMode](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/1618681-documentpickermode)Added [-[UIDocumentPickerViewController initWithDocumentTypes:inMode:]](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/1618678-initwithdocumenttypes)Added [-[UIDocumentPickerViewController initWithURL:inMode:]](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/1618684-init)Added [UIDocumentPickerMode](https://developer.apple.com/documentation/uikit/uidocumentpickermode)Added [UIDocumentPickerModeExportToService](https://developer.apple.com/documentation/uikit/uidocumentpickermode/uidocumentpickermodeexporttoservice)Added [UIDocumentPickerModeImport](https://developer.apple.com/documentation/uikit/uidocumentpickermode/import)Added [UIDocumentPickerModeMoveToService](https://developer.apple.com/documentation/uikit/uidocumentpickermode/movetoservice)Added [UIDocumentPickerModeOpen](https://developer.apple.com/documentation/uikit/uidocumentpickermode/open)UIDynamicAnimator.hModified [-[UIDynamicAnimatorDelegate dynamicAnimatorDidPause:]](https://developer.apple.com/documentation/uikit/uidynamicanimatordelegate/1621193-dynamicanimatordidpause)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIDynamicAnimatorDelegate dynamicAnimatorWillResume:]](https://developer.apple.com/documentation/uikit/uidynamicanimatordelegate/1621188-dynamicanimatorwillresume)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UIGeometry.hAdded [-[NSCoder decodeCGVectorForKey:]](https://developer.apple.com/documentation/foundation/nscoder/1624488-decodecgvectorforkey)Added [-[NSCoder encodeCGVector:forKey:]](https://developer.apple.com/documentation/foundation/nscoder/1624532-encodecgvector)Added [-[NSValue CGVectorValue]](https://developer.apple.com/documentation/foundation/nsvalue/1624486-cgvectorvalue)Added [+[NSValue valueWithCGVector:]](https://developer.apple.com/documentation/foundation/nsvalue/1624493-valuewithcgvector)Added [CGVectorFromString()](https://developer.apple.com/documentation/uikit/1624513-cgvectorfromstring)Added [NSStringFromCGVector()](https://developer.apple.com/documentation/uikit/1624476-nsstringfromcgvector)UIGestureRecognizer.hModified [-[UIGestureRecognizer initWithTarget:action:]](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1624211-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTarget:(id)target action:(SEL)action ``` |
| To | ``` - (instancetype)initWithTarget:(id)target action:(SEL)action ``` |

Modified [-[UIGestureRecognizerDelegate gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:]](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/1624222-gesturerecognizer)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIGestureRecognizerDelegate gestureRecognizer:shouldReceiveTouch:]](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/1624214-gesturerecognizer)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIGestureRecognizerDelegate gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:]](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/1624208-gesturerecognizer)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIGestureRecognizerDelegate gestureRecognizer:shouldRequireFailureOfGestureRecognizer:]](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/1624229-gesturerecognizer)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIGestureRecognizerDelegate gestureRecognizerShouldBegin:]](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/1624213-gesturerecognizershouldbegin)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UIGestureRecognizerSubclass.hRemoved UIGestureRecognizer(ForSubclassEyesOnly)Added UIGestureRecognizer(UIGestureRecognizerProtected)UIGuidedAccessRestrictions.hModified [-[UIGuidedAccessRestrictionDelegate detailTextForGuidedAccessRestrictionWithIdentifier:]](https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictiondelegate/1621158-detailtextforguidedaccessrestric)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UIImage.hAdded [UIImage.imageAsset](https://developer.apple.com/documentation/uikit/uiimage/1624151-imageasset)Added [+[UIImage imageNamed:inBundle:compatibleWithTraitCollection:]](https://developer.apple.com/documentation/uikit/uiimage/1624154-imagenamed)Added [UIImage.traitCollection](https://developer.apple.com/documentation/uikit/uiimage/1624158-traitcollection)Modified [-[CIImage initWithImage:]](https://developer.apple.com/documentation/coreimage/ciimage/1624119-initwithimage)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithImage:(UIImage *)image ``` |
| To | ``` - (instancetype)initWithImage:(UIImage *)image ``` |

Modified [-[CIImage initWithImage:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1624098-initwithimage)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithImage:(UIImage *)image options:(NSDictionary *)options ``` |
| To | ``` - (instancetype)initWithImage:(UIImage *)image options:(NSDictionary *)options ``` |

Modified [UIImage](https://developer.apple.com/documentation/uikit/uiimage)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSSecureCoding |

Modified [-[UIImage initWithCGImage:]](https://developer.apple.com/documentation/uikit/uiimage/1624090-initwithcgimage)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCGImage:(CGImageRef)cgImage ``` |
| To | ``` - (instancetype)initWithCGImage:(CGImageRef)cgImage ``` |

Modified [-[UIImage initWithCGImage:scale:orientation:]](https://developer.apple.com/documentation/uikit/uiimage/1624091-initwithcgimage)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCGImage:(CGImageRef)cgImage scale:(CGFloat)scale orientation:(UIImageOrientation)orientation ``` |
| To | ``` - (instancetype)initWithCGImage:(CGImageRef)cgImage scale:(CGFloat)scale orientation:(UIImageOrientation)orientation ``` |

Modified [-[UIImage initWithCIImage:]](https://developer.apple.com/documentation/uikit/uiimage/1624114-initwithciimage)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCIImage:(CIImage *)ciImage ``` |
| To | ``` - (instancetype)initWithCIImage:(CIImage *)ciImage ``` |

Modified [-[UIImage initWithCIImage:scale:orientation:]](https://developer.apple.com/documentation/uikit/uiimage/1624150-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCIImage:(CIImage *)ciImage scale:(CGFloat)scale orientation:(UIImageOrientation)orientation ``` |
| To | ``` - (instancetype)initWithCIImage:(CIImage *)ciImage scale:(CGFloat)scale orientation:(UIImageOrientation)orientation ``` |

Modified [-[UIImage initWithContentsOfFile:]](https://developer.apple.com/documentation/uikit/uiimage/1624112-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfFile:(NSString *)path ``` |
| To | ``` - (instancetype)initWithContentsOfFile:(NSString *)path ``` |

Modified [-[UIImage initWithData:]](https://developer.apple.com/documentation/uikit/uiimage/1624106-initwithdata)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(NSData *)data ``` |
| To | ``` - (instancetype)initWithData:(NSData *)data ``` |

Modified [-[UIImage initWithData:scale:]](https://developer.apple.com/documentation/uikit/uiimage/1624109-initwithdata)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(NSData *)data scale:(CGFloat)scale ``` |
| To | ``` - (instancetype)initWithData:(NSData *)data scale:(CGFloat)scale ``` |

UIImageAsset.h (Added)Added [UIImageAsset](https://developer.apple.com/documentation/uikit/uiimageasset)Added [-[UIImageAsset imageWithTraitCollection:]](https://developer.apple.com/documentation/uikit/uiimageasset/1624976-image)Added [-[UIImageAsset registerImage:withTraitCollection:]](https://developer.apple.com/documentation/uikit/uiimageasset/1624974-register)Added [-[UIImageAsset unregisterImageWithTraitCollection:]](https://developer.apple.com/documentation/uikit/uiimageasset/1624973-unregister)UIImagePickerController.hModified [-[UIImagePickerControllerDelegate imagePickerController:didFinishPickingImage:editingInfo:]](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate/1619152-imagepickercontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIImagePickerControllerDelegate imagePickerController:didFinishPickingMediaWithInfo:]](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate/1619126-imagepickercontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIImagePickerControllerDelegate imagePickerControllerDidCancel:]](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate/1619133-imagepickercontrollerdidcancel)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UIImageView.hModified [-[UIImageView initWithImage:]](https://developer.apple.com/documentation/uikit/uiimageview/1621062-initwithimage)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithImage:(UIImage *)image ``` |
| To | ``` - (instancetype)initWithImage:(UIImage *)image ``` |

Modified [-[UIImageView initWithImage:highlightedImage:]](https://developer.apple.com/documentation/uikit/uiimageview/1621064-initwithimage)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithImage:(UIImage *)image highlightedImage:(UIImage *)highlightedImage ``` |
| To | ``` - (instancetype)initWithImage:(UIImage *)image highlightedImage:(UIImage *)highlightedImage ``` |

UIInputView.hModified [-[UIInputView initWithFrame:inputViewStyle:]](https://developer.apple.com/documentation/uikit/uiinputview/1619477-initwithframe)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFrame:(CGRect)frame inputViewStyle:(UIInputViewStyle)inputViewStyle ``` |
| To | ``` - (instancetype)initWithFrame:(CGRect)frame inputViewStyle:(UIInputViewStyle)inputViewStyle ``` |

UIInputViewController.h (Added)Added [UIInputViewController](https://developer.apple.com/documentation/uikit/uiinputviewcontroller)Added [-[UIInputViewController advanceToNextInputMode]](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/1618191-advancetonextinputmode)Added [-[UIInputViewController dismissKeyboard]](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/1618196-dismisskeyboard)Added [UIInputViewController.inputView](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/1618192-inputview)Added [UIInputViewController.primaryLanguage](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/1618200-primarylanguage)Added [-[UIInputViewController requestSupplementaryLexiconWithCompletion:]](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/1618195-requestsupplementarylexicon)Added [UIInputViewController.textDocumentProxy](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/1618193-textdocumentproxy)Added [UITextDocumentProxy](https://developer.apple.com/documentation/uikit/uitextdocumentproxy)Added [-[UITextDocumentProxy adjustTextPositionByCharacterOffset:]](https://developer.apple.com/documentation/uikit/uitextdocumentproxy/1618194-adjusttextposition)Added [UITextDocumentProxy.documentContextAfterInput](https://developer.apple.com/documentation/uikit/uitextdocumentproxy/1618199-documentcontextafterinput)Added [UITextDocumentProxy.documentContextBeforeInput](https://developer.apple.com/documentation/uikit/uitextdocumentproxy/1618190-documentcontextbeforeinput)UIInterface.hAdded [UIUserInterfaceSizeClass](https://developer.apple.com/documentation/uikit/uiuserinterfacesizeclass)Added [UIUserInterfaceSizeClassCompact](https://developer.apple.com/documentation/uikit/uiuserinterfacesizeclass/compact)Added [UIUserInterfaceSizeClassRegular](https://developer.apple.com/documentation/uikit/uiuserinterfacesizeclass/uiuserinterfacesizeclassregular)Added [UIUserInterfaceSizeClassUnspecified](https://developer.apple.com/documentation/uikit/uiuserinterfacesizeclass/uiuserinterfacesizeclassunspecified)UILexicon.h (Added)Added [UILexicon](https://developer.apple.com/documentation/uikit/uilexicon)Added [UILexicon.entries](https://developer.apple.com/documentation/uikit/uilexicon/1614133-entries)Added [UILexiconEntry](https://developer.apple.com/documentation/uikit/uilexiconentry)Added [UILexiconEntry.documentText](https://developer.apple.com/documentation/uikit/uilexiconentry/1614130-documenttext)Added [UILexiconEntry.userInput](https://developer.apple.com/documentation/uikit/uilexiconentry/1614132-userinput)UILocalNotification.hAdded [UILocalNotification.category](https://developer.apple.com/documentation/uikit/uilocalnotification/1616655-category)Added [UILocalNotification.region](https://developer.apple.com/documentation/uikit/uilocalnotification/1616644-region)Added [UILocalNotification.regionTriggersOnce](https://developer.apple.com/documentation/uikit/uilocalnotification/1616654-regiontriggersonce)UIMenuController.hModified [-[UIMenuItem initWithTitle:action:]](https://developer.apple.com/documentation/uikit/uimenuitem/1622824-initwithtitle)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTitle:(NSString *)title action:(SEL)action ``` |
| To | ``` - (instancetype)initWithTitle:(NSString *)title action:(SEL)action ``` |

UINavigationBar.hModified [UINavigationBar.delegate](https://developer.apple.com/documentation/uikit/uinavigationbar/1624951-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id delegate ``` |
| To | ``` @property(nonatomic, assign) id<UINavigationBarDelegate> delegate ``` |

Modified [-[UINavigationBarDelegate navigationBar:didPopItem:]](https://developer.apple.com/documentation/uikit/uinavigationbardelegate/1624948-navigationbar)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UINavigationBarDelegate navigationBar:didPushItem:]](https://developer.apple.com/documentation/uikit/uinavigationbardelegate/1624964-navigationbar)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UINavigationBarDelegate navigationBar:shouldPopItem:]](https://developer.apple.com/documentation/uikit/uinavigationbardelegate/1624944-navigationbar)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UINavigationBarDelegate navigationBar:shouldPushItem:]](https://developer.apple.com/documentation/uikit/uinavigationbardelegate/1624941-navigationbar)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UINavigationItem initWithTitle:]](https://developer.apple.com/documentation/uikit/uinavigationitem/1624943-initwithtitle)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTitle:(NSString *)title ``` |
| To | ``` - (instancetype)initWithTitle:(NSString *)title ``` |

UINavigationController.hAdded [UINavigationController.barHideOnSwipeGestureRecognizer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621854-barhideonswipegesturerecognizer)Added [UINavigationController.barHideOnTapGestureRecognizer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621852-barhideontapgesturerecognizer)Added [UINavigationController.hidesBarsOnSwipe](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621883-hidesbarsonswipe)Added [UINavigationController.hidesBarsOnTap](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621879-hidesbarsontap)Added [UINavigationController.hidesBarsWhenKeyboardAppears](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621881-hidesbarswhenkeyboardappears)Added [UINavigationController.hidesBarsWhenVerticallyCompact](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621869-hidesbarswhenverticallycompact)Added [-[UINavigationController showViewController:sender:]](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621872-show)Modified [-[UINavigationController initWithRootViewController:]](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621858-initwithrootviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithRootViewController:(UIViewController *)rootViewController ``` |
| To | ``` - (instancetype)initWithRootViewController:(UIViewController *)rootViewController ``` |

Modified [-[UINavigationControllerDelegate navigationController:animationControllerForOperation:fromViewController:toViewController:]](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/1621846-navigationcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UINavigationControllerDelegate navigationController:didShowViewController:animated:]](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/1621848-navigationcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UINavigationControllerDelegate navigationController:interactionControllerForAnimationController:]](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/1621880-navigationcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UINavigationControllerDelegate navigationController:willShowViewController:animated:]](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/1621878-navigationcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UINavigationControllerDelegate navigationControllerPreferredInterfaceOrientationForPresentation:]](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/1621864-navigationcontrollerpreferredint)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UINavigationControllerDelegate navigationControllerSupportedInterfaceOrientations:]](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/1621884-navigationcontrollersupportedint)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UINibDeclarations.hAdded #def IBInspectableAdded #def IB_DESIGNABLEUINibLoading.hAdded [-[NSObject prepareForInterfaceBuilder]](https://developer.apple.com/documentation/objectivec/nsobject/1402908-prepareforinterfacebuilder)UIPageViewController.hModified [-[UIPageViewController initWithTransitionStyle:navigationOrientation:options:]](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614105-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTransitionStyle:(UIPageViewControllerTransitionStyle)style navigationOrientation:(UIPageViewControllerNavigationOrientation)navigationOrientation options:(NSDictionary *)options ``` |
| To | ``` - (instancetype)initWithTransitionStyle:(UIPageViewControllerTransitionStyle)style navigationOrientation:(UIPageViewControllerNavigationOrientation)navigationOrientation options:(NSDictionary *)options ``` |

Modified [-[UIPageViewControllerDataSource presentationCountForPageViewController:]](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdatasource/1614095-presentationcount)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPageViewControllerDataSource presentationIndexForPageViewController:]](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdatasource/1614116-presentationindex)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPageViewControllerDelegate pageViewController:didFinishAnimating:previousViewControllers:transitionCompleted:]](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/1614090-pageviewcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPageViewControllerDelegate pageViewController:spineLocationForInterfaceOrientation:]](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/1614083-pageviewcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPageViewControllerDelegate pageViewController:willTransitionToViewControllers:]](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/1614091-pageviewcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPageViewControllerDelegate pageViewControllerPreferredInterfaceOrientationForPresentation:]](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/1614119-pageviewcontrollerpreferredinter)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPageViewControllerDelegate pageViewControllerSupportedInterfaceOrientations:]](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/1614100-pageviewcontrollersupportedinter)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UIPickerView.hModified [-[UIPickerViewDelegate pickerView:attributedTitleForRow:forComponent:]](https://developer.apple.com/documentation/uikit/uipickerviewdelegate/1614375-pickerview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPickerViewDelegate pickerView:didSelectRow:inComponent:]](https://developer.apple.com/documentation/uikit/uipickerviewdelegate/1614371-pickerview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPickerViewDelegate pickerView:rowHeightForComponent:]](https://developer.apple.com/documentation/uikit/uipickerviewdelegate/1614386-pickerview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPickerViewDelegate pickerView:titleForRow:forComponent:]](https://developer.apple.com/documentation/uikit/uipickerviewdelegate/1614384-pickerview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPickerViewDelegate pickerView:viewForRow:forComponent:reusingView:]](https://developer.apple.com/documentation/uikit/uipickerviewdelegate/1614389-pickerview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPickerViewDelegate pickerView:widthForComponent:]](https://developer.apple.com/documentation/uikit/uipickerviewdelegate/1614378-pickerview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UIPopoverBackgroundView.hRemoved +[UIPopoverBackgroundView arrowBase]Removed +[UIPopoverBackgroundView arrowHeight]Removed +[UIPopoverBackgroundView contentViewInsets]Added [UIPopoverBackgroundViewMethods](https://developer.apple.com/documentation/uikit/uipopoverbackgroundviewmethods)Added [+[UIPopoverBackgroundViewMethods arrowBase]](https://developer.apple.com/documentation/uikit/uipopoverbackgroundviewmethods/1619351-arrowbase)Added [+[UIPopoverBackgroundViewMethods arrowHeight]](https://developer.apple.com/documentation/uikit/uipopoverbackgroundviewmethods/1619354-arrowheight)Added [+[UIPopoverBackgroundViewMethods contentViewInsets]](https://developer.apple.com/documentation/uikit/uipopoverbackgroundviewmethods/1619349-contentviewinsets)Modified [UIPopoverBackgroundView](https://developer.apple.com/documentation/uikit/uipopoverbackgroundview)

|  | Protocols |
| --- | --- |
| From | -- |
| To | UIPopoverBackgroundViewMethods |

UIPopoverController.hModified [-[UIPopoverController initWithContentViewController:]](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624669-initwithcontentviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentViewController:(UIViewController *)viewController ``` |
| To | ``` - (instancetype)initWithContentViewController:(UIViewController *)viewController ``` |

Modified [-[UIPopoverControllerDelegate popoverController:willRepositionPopoverToRect:inView:]](https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/1624664-popovercontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPopoverControllerDelegate popoverControllerDidDismissPopover:]](https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/1624671-popovercontrollerdiddismisspopov)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPopoverControllerDelegate popoverControllerShouldDismissPopover:]](https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/1624661-popovercontrollershoulddismisspo)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [UIViewController.contentSizeForViewInPopover](https://developer.apple.com/documentation/uikit/uiviewcontroller/1619323-contentsizeforviewinpopover)

|  | Header |
| --- | --- |
| From | UIKit/UIPopoverController.h |
| To | UIKit/UIPopoverSupport.h |

Modified [UIViewController.modalInPopover](https://developer.apple.com/documentation/uikit/uiviewcontroller/1619312-ismodalinpopover)

|  | Header |
| --- | --- |
| From | UIKit/UIPopoverController.h |
| To | UIKit/UIPopoverSupport.h |

Modified [UIPopoverArrowDirection](https://developer.apple.com/documentation/uikit/uipopoverarrowdirection)

|  | Header |
| --- | --- |
| From | UIKit/UIPopoverController.h |
| To | UIKit/UIPopoverSupport.h |

Modified [UIPopoverArrowDirectionAny](https://developer.apple.com/documentation/uikit/uipopoverarrowdirection/uipopoverarrowdirectionany)

|  | Header |
| --- | --- |
| From | UIKit/UIPopoverController.h |
| To | UIKit/UIPopoverSupport.h |

Modified [UIPopoverArrowDirectionDown](https://developer.apple.com/documentation/uikit/uipopoverarrowdirection/1619317-down)

|  | Header |
| --- | --- |
| From | UIKit/UIPopoverController.h |
| To | UIKit/UIPopoverSupport.h |

Modified [UIPopoverArrowDirectionLeft](https://developer.apple.com/documentation/uikit/uipopoverarrowdirection/uipopoverarrowdirectionleft)

|  | Header |
| --- | --- |
| From | UIKit/UIPopoverController.h |
| To | UIKit/UIPopoverSupport.h |

Modified [UIPopoverArrowDirectionRight](https://developer.apple.com/documentation/uikit/uipopoverarrowdirection/1619309-right)

|  | Header |
| --- | --- |
| From | UIKit/UIPopoverController.h |
| To | UIKit/UIPopoverSupport.h |

Modified [UIPopoverArrowDirectionUnknown](https://developer.apple.com/documentation/uikit/uipopoverarrowdirection/1619315-unknown)

|  | Header |
| --- | --- |
| From | UIKit/UIPopoverController.h |
| To | UIKit/UIPopoverSupport.h |

Modified [UIPopoverArrowDirectionUp](https://developer.apple.com/documentation/uikit/uipopoverarrowdirection/1619319-up)

|  | Header |
| --- | --- |
| From | UIKit/UIPopoverController.h |
| To | UIKit/UIPopoverSupport.h |

Modified UIViewController(UIPopoverController)

|  | Header |
| --- | --- |
| From | UIKit/UIPopoverController.h |
| To | UIKit/UIPopoverSupport.h |

UIPopoverPresentationController.h (Added)Added [UIPopoverPresentationController](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller)Added [UIPopoverPresentationController.arrowDirection](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622315-arrowdirection)Added [UIPopoverPresentationController.backgroundColor](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622316-backgroundcolor)Added [UIPopoverPresentationController.barButtonItem](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622314-barbuttonitem)Added [UIPopoverPresentationController.delegate](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622320-delegate)Added [UIPopoverPresentationController.passthroughViews](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622312-passthroughviews)Added [UIPopoverPresentationController.permittedArrowDirections](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622319-permittedarrowdirections)Added [UIPopoverPresentationController.popoverBackgroundViewClass](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622318-popoverbackgroundviewclass)Added [UIPopoverPresentationController.popoverLayoutMargins](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622323-popoverlayoutmargins)Added [UIPopoverPresentationController.sourceRect](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622324-sourcerect)Added [UIPopoverPresentationController.sourceView](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622313-sourceview)Added [UIPopoverPresentationControllerDelegate](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontrollerdelegate)Added [-[UIPopoverPresentationControllerDelegate popoverPresentationController:willRepositionPopoverToRect:inView:]](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontrollerdelegate/1622326-popoverpresentationcontroller)Added [-[UIPopoverPresentationControllerDelegate popoverPresentationControllerDidDismissPopover:]](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontrollerdelegate/1622322-popoverpresentationcontrollerdid)Added [-[UIPopoverPresentationControllerDelegate popoverPresentationControllerShouldDismissPopover:]](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontrollerdelegate/1622321-popoverpresentationcontrollersho)Added [-[UIPopoverPresentationControllerDelegate prepareForPopoverPresentation:]](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontrollerdelegate/1622317-prepareforpopoverpresentation)UIPopoverSupport.h (Added)Modified [UIViewController.contentSizeForViewInPopover](https://developer.apple.com/documentation/uikit/uiviewcontroller/1619323-contentsizeforviewinpopover)

|  | Header |
| --- | --- |
| From | UIKit/UIPopoverController.h |
| To | UIKit/UIPopoverSupport.h |

Modified [UIViewController.modalInPopover](https://developer.apple.com/documentation/uikit/uiviewcontroller/1619312-ismodalinpopover)

|  | Header |
| --- | --- |
| From | UIKit/UIPopoverController.h |
| To | UIKit/UIPopoverSupport.h |

Modified [UIPopoverArrowDirection](https://developer.apple.com/documentation/uikit/uipopoverarrowdirection)

|  | Header |
| --- | --- |
| From | UIKit/UIPopoverController.h |
| To | UIKit/UIPopoverSupport.h |

Modified [UIPopoverArrowDirectionAny](https://developer.apple.com/documentation/uikit/uipopoverarrowdirection/uipopoverarrowdirectionany)

|  | Header |
| --- | --- |
| From | UIKit/UIPopoverController.h |
| To | UIKit/UIPopoverSupport.h |

Modified [UIPopoverArrowDirectionDown](https://developer.apple.com/documentation/uikit/uipopoverarrowdirection/1619317-down)

|  | Header |
| --- | --- |
| From | UIKit/UIPopoverController.h |
| To | UIKit/UIPopoverSupport.h |

Modified [UIPopoverArrowDirectionLeft](https://developer.apple.com/documentation/uikit/uipopoverarrowdirection/uipopoverarrowdirectionleft)

|  | Header |
| --- | --- |
| From | UIKit/UIPopoverController.h |
| To | UIKit/UIPopoverSupport.h |

Modified [UIPopoverArrowDirectionRight](https://developer.apple.com/documentation/uikit/uipopoverarrowdirection/1619309-right)

|  | Header |
| --- | --- |
| From | UIKit/UIPopoverController.h |
| To | UIKit/UIPopoverSupport.h |

Modified [UIPopoverArrowDirectionUnknown](https://developer.apple.com/documentation/uikit/uipopoverarrowdirection/1619315-unknown)

|  | Header |
| --- | --- |
| From | UIKit/UIPopoverController.h |
| To | UIKit/UIPopoverSupport.h |

Modified [UIPopoverArrowDirectionUp](https://developer.apple.com/documentation/uikit/uipopoverarrowdirection/1619319-up)

|  | Header |
| --- | --- |
| From | UIKit/UIPopoverController.h |
| To | UIKit/UIPopoverSupport.h |

Modified UIViewController(UIPopoverController)

|  | Header |
| --- | --- |
| From | UIKit/UIPopoverController.h |
| To | UIKit/UIPopoverSupport.h |

UIPresentationController.h (Added)Added [UIAdaptivePresentationControllerDelegate](https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate)Added [-[UIAdaptivePresentationControllerDelegate adaptivePresentationStyleForPresentationController:]](https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/1618343-adaptivepresentationstyleforpres)Added [-[UIAdaptivePresentationControllerDelegate presentationController:viewControllerForAdaptivePresentationStyle:]](https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/1618326-presentationcontroller)Added [UIPresentationController](https://developer.apple.com/documentation/uikit/uipresentationcontroller)Added [-[UIPresentationController adaptivePresentationStyle]](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618340-adaptivepresentationstyle)Added [UIPresentationController.containerView](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618332-containerview)Added [-[UIPresentationController containerViewDidLayoutSubviews]](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618331-containerviewdidlayoutsubviews)Added [-[UIPresentationController containerViewWillLayoutSubviews]](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618341-containerviewwilllayoutsubviews)Added [UIPresentationController.delegate](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618329-delegate)Added [-[UIPresentationController dismissalTransitionDidEnd:]](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618323-dismissaltransitiondidend)Added [-[UIPresentationController dismissalTransitionWillBegin]](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618342-dismissaltransitionwillbegin)Added [-[UIPresentationController frameOfPresentedViewInContainerView]](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618337-frameofpresentedviewincontainerv)Added [-[UIPresentationController initWithPresentedViewController:presentingViewController:]](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618328-init)Added [UIPresentationController.overrideTraitCollection](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618335-overridetraitcollection)Added [UIPresentationController.presentationStyle](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618320-presentationstyle)Added [-[UIPresentationController presentationTransitionDidEnd:]](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618327-presentationtransitiondidend)Added [-[UIPresentationController presentationTransitionWillBegin]](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618330-presentationtransitionwillbegin)Added [-[UIPresentationController presentedView]](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618321-presentedview)Added [UIPresentationController.presentedViewController](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618322-presentedviewcontroller)Added [UIPresentationController.presentingViewController](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618338-presentingviewcontroller)Added [-[UIPresentationController shouldPresentInFullscreen]](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618336-shouldpresentinfullscreen)Added [-[UIPresentationController shouldRemovePresentersView]](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618319-shouldremovepresentersview)UIPrintFormatter.hAdded [UIPrintFormatter.perPageContentInsets](https://developer.apple.com/documentation/uikit/uiprintformatter/1621831-perpagecontentinsets)Modified [-[UIMarkupTextPrintFormatter initWithMarkupText:]](https://developer.apple.com/documentation/uikit/uimarkuptextprintformatter/1621845-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithMarkupText:(NSString *)markupText ``` |
| To | ``` - (instancetype)initWithMarkupText:(NSString *)markupText ``` |

Modified [-[UISimpleTextPrintFormatter initWithText:]](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/1621822-initwithtext)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithText:(NSString *)text ``` |
| To | ``` - (instancetype)initWithText:(NSString *)text ``` |

UIPrintInteractionController.hAdded [-[UIPrintInteractionController printToPrinter:completionHandler:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618174-print)Added [UIPrintInteractionController.showsPaperSelectionForLoadedPapers](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618164-showspaperselectionforloadedpape)Modified [-[UIPrintInteractionControllerDelegate printInteractionController:choosePaper:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618160-printinteractioncontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPrintInteractionControllerDelegate printInteractionController:cutLengthForPaper:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618179-printinteractioncontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPrintInteractionControllerDelegate printInteractionControllerDidDismissPrinterOptions:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618175-printinteractioncontrollerdiddis)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPrintInteractionControllerDelegate printInteractionControllerDidFinishJob:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618154-printinteractioncontrollerdidfin)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPrintInteractionControllerDelegate printInteractionControllerDidPresentPrinterOptions:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618158-printinteractioncontrollerdidpre)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPrintInteractionControllerDelegate printInteractionControllerParentViewController:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618162-printinteractioncontrollerparent)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPrintInteractionControllerDelegate printInteractionControllerWillDismissPrinterOptions:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618151-printinteractioncontrollerwilldi)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPrintInteractionControllerDelegate printInteractionControllerWillPresentPrinterOptions:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618168-printinteractioncontrollerwillpr)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIPrintInteractionControllerDelegate printInteractionControllerWillStartJob:]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618185-printinteractioncontrollerwillst)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UIPrinter.h (Added)Added [UIPrinter](https://developer.apple.com/documentation/uikit/uiprinter)Added [UIPrinter.URL](https://developer.apple.com/documentation/uikit/uiprinter/1620440-url)Added [-[UIPrinter contactPrinter:]](https://developer.apple.com/documentation/uikit/uiprinter/1620431-contactprinter)Added [UIPrinter.displayLocation](https://developer.apple.com/documentation/uikit/uiprinter/1620426-displaylocation)Added [UIPrinter.displayName](https://developer.apple.com/documentation/uikit/uiprinter/1620427-displayname)Added [UIPrinter.makeAndModel](https://developer.apple.com/documentation/uikit/uiprinter/1620438-makeandmodel)Added [+[UIPrinter printerWithURL:]](https://developer.apple.com/documentation/uikit/uiprinter/1620442-init)Added [UIPrinter.supportedJobTypes](https://developer.apple.com/documentation/uikit/uiprinter/1620436-supportedjobtypes)Added [UIPrinter.supportsColor](https://developer.apple.com/documentation/uikit/uiprinter/1620429-supportscolor)Added [UIPrinter.supportsDuplex](https://developer.apple.com/documentation/uikit/uiprinter/1620434-supportsduplex)Added [UIPrinterJobTypeDocument](https://developer.apple.com/documentation/uikit/uiprinterjobtypes/uiprinterjobtypedocument)Added [UIPrinterJobTypeEnvelope](https://developer.apple.com/documentation/uikit/uiprinter/jobtypes/1620428-envelope)Added [UIPrinterJobTypeLabel](https://developer.apple.com/documentation/uikit/uiprinterjobtypes/uiprinterjobtypelabel)Added [UIPrinterJobTypeLargeFormat](https://developer.apple.com/documentation/uikit/uiprinter/jobtypes/1620443-largeformat)Added [UIPrinterJobTypePhoto](https://developer.apple.com/documentation/uikit/uiprinter/jobtypes/1620433-photo)Added [UIPrinterJobTypePostcard](https://developer.apple.com/documentation/uikit/uiprinter/jobtypes/1620437-postcard)Added [UIPrinterJobTypeReceipt](https://developer.apple.com/documentation/uikit/uiprinter/jobtypes/1620430-receipt)Added [UIPrinterJobTypeRoll](https://developer.apple.com/documentation/uikit/uiprinter/jobtypes/1620439-roll)Added [UIPrinterJobTypeUnknown](https://developer.apple.com/documentation/uikit/uiprinter/jobtypes/1620444-unknown)Added [UIPrinterJobTypes](https://developer.apple.com/documentation/uikit/uiprinter/jobtypes)UIPrinterPickerController.h (Added)Added [UIPrinterPickerController](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller)Added [UIPrinterPickerController.delegate](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/1620511-delegate)Added [-[UIPrinterPickerController dismissAnimated:]](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/1620512-dismissanimated)Added [-[UIPrinterPickerController presentAnimated:completionHandler:]](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/1620514-present)Added [-[UIPrinterPickerController presentFromBarButtonItem:animated:completionHandler:]](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/1620507-present)Added [-[UIPrinterPickerController presentFromRect:inView:animated:completionHandler:]](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/1620515-presentfromrect)Added [+[UIPrinterPickerController printerPickerControllerWithInitiallySelectedPrinter:]](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/1620517-init)Added [UIPrinterPickerController.selectedPrinter](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/1620516-selectedprinter)Added [UIPrinterPickerControllerDelegate](https://developer.apple.com/documentation/uikit/uiprinterpickercontrollerdelegate)Added [-[UIPrinterPickerControllerDelegate printerPickerController:shouldShowPrinter:]](https://developer.apple.com/documentation/uikit/uiprinterpickercontrollerdelegate/1620503-printerpickercontroller)Added [-[UIPrinterPickerControllerDelegate printerPickerControllerDidDismiss:]](https://developer.apple.com/documentation/uikit/uiprinterpickercontrollerdelegate/1620510-printerpickercontrollerdiddismis)Added [-[UIPrinterPickerControllerDelegate printerPickerControllerDidPresent:]](https://developer.apple.com/documentation/uikit/uiprinterpickercontrollerdelegate/1620508-printerpickercontrollerdidpresen)Added [-[UIPrinterPickerControllerDelegate printerPickerControllerDidSelectPrinter:]](https://developer.apple.com/documentation/uikit/uiprinterpickercontrollerdelegate/1620504-printerpickercontrollerdidselect)Added [-[UIPrinterPickerControllerDelegate printerPickerControllerParentViewController:]](https://developer.apple.com/documentation/uikit/uiprinterpickercontrollerdelegate/1620518-printerpickercontrollerparentvie)Added [-[UIPrinterPickerControllerDelegate printerPickerControllerWillDismiss:]](https://developer.apple.com/documentation/uikit/uiprinterpickercontrollerdelegate/1620519-printerpickercontrollerwilldismi)Added [-[UIPrinterPickerControllerDelegate printerPickerControllerWillPresent:]](https://developer.apple.com/documentation/uikit/uiprinterpickercontrollerdelegate/1620513-printerpickercontrollerwillprese)Added [UIPrinterPickerCompletionHandler](https://developer.apple.com/documentation/uikit/uiprinterpickercompletionhandler)UIProgressView.hModified [-[UIProgressView initWithProgressViewStyle:]](https://developer.apple.com/documentation/uikit/uiprogressview/1619833-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithProgressViewStyle:(UIProgressViewStyle)style ``` |
| To | ``` - (instancetype)initWithProgressViewStyle:(UIProgressViewStyle)style ``` |

UIReferenceLibraryViewController.hModified [-[UIReferenceLibraryViewController initWithTerm:]](https://developer.apple.com/documentation/uikit/uireferencelibraryviewcontroller/1624808-initwithterm)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTerm:(NSString *)term ``` |
| To | ``` - (instancetype)initWithTerm:(NSString *)term ``` |

UIRefreshControl.hModified [-[UIRefreshControl init]](https://developer.apple.com/documentation/uikit/uirefreshcontrol/1624846-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

UIResponder.hAdded [UIResponder.inputAccessoryViewController](https://developer.apple.com/documentation/uikit/uiresponder/1621124-inputaccessoryviewcontroller)Added [UIResponder.inputViewController](https://developer.apple.com/documentation/uikit/uiresponder/1621117-inputviewcontroller)Added [-[UIResponder restoreUserActivityState:]](https://developer.apple.com/documentation/uikit/uiresponder/1621111-restoreuseractivitystate)Added [-[UIResponder updateUserActivityState:]](https://developer.apple.com/documentation/uikit/uiresponder/1621095-updateuseractivitystate)Added [UIResponder.userActivity](https://developer.apple.com/documentation/uikit/uiresponder/1621089-useractivity)Added UIResponder(ActivityContinuation)Modified [UIResponder.inputAccessoryView](https://developer.apple.com/documentation/uikit/uiresponder/1621119-inputaccessoryview)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) UIView *inputAccessoryView ``` |
| To | ``` @property(nonatomic, readonly, retain) UIView *inputAccessoryView ``` |

Modified [UIResponder.inputView](https://developer.apple.com/documentation/uikit/uiresponder/1621092-inputview)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) UIView *inputView ``` |
| To | ``` @property(nonatomic, readonly, retain) UIView *inputView ``` |

Modified [UIResponder.textInputContextIdentifier](https://developer.apple.com/documentation/uikit/uiresponder/1621091-textinputcontextidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) NSString *textInputContextIdentifier ``` |
| To | ``` @property(nonatomic, readonly, retain) NSString *textInputContextIdentifier ``` |

Modified [UIResponder.textInputMode](https://developer.apple.com/documentation/uikit/uiresponder/1621133-textinputmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) UITextInputMode *textInputMode ``` |
| To | ``` @property(nonatomic, readonly, retain) UITextInputMode *textInputMode ``` |

UIScreen.hAdded [UIScreen.coordinateSpace](https://developer.apple.com/documentation/uikit/uiscreen/1617833-coordinatespace)Added [UIScreen.fixedCoordinateSpace](https://developer.apple.com/documentation/uikit/uiscreen/1617819-fixedcoordinatespace)Added [UIScreen.nativeBounds](https://developer.apple.com/documentation/uikit/uiscreen/1617810-nativebounds)Added [UIScreen.nativeScale](https://developer.apple.com/documentation/uikit/uiscreen/1617825-nativescale)Modified [UIScreen](https://developer.apple.com/documentation/uikit/uiscreen)

|  | Protocols |
| --- | --- |
| From | -- |
| To | UITraitEnvironment |

UIScrollView.hModified [-[UIScrollViewDelegate scrollViewDidEndDecelerating:]](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619417-scrollviewdidenddecelerating)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIScrollViewDelegate scrollViewDidEndDragging:willDecelerate:]](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619436-scrollviewdidenddragging)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIScrollViewDelegate scrollViewDidEndScrollingAnimation:]](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619379-scrollviewdidendscrollinganimati)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIScrollViewDelegate scrollViewDidEndZooming:withView:atScale:]](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619407-scrollviewdidendzooming)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIScrollViewDelegate scrollViewDidScroll:]](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619392-scrollviewdidscroll)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIScrollViewDelegate scrollViewDidScrollToTop:]](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619382-scrollviewdidscrolltotop)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIScrollViewDelegate scrollViewDidZoom:]](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619409-scrollviewdidzoom)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIScrollViewDelegate scrollViewShouldScrollToTop:]](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619378-scrollviewshouldscrolltotop)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIScrollViewDelegate scrollViewWillBeginDecelerating:]](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619386-scrollviewwillbegindecelerating)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIScrollViewDelegate scrollViewWillBeginDragging:]](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619394-scrollviewwillbegindragging)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIScrollViewDelegate scrollViewWillBeginZooming:withView:]](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619396-scrollviewwillbeginzooming)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIScrollViewDelegate scrollViewWillEndDragging:withVelocity:targetContentOffset:]](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619385-scrollviewwillenddragging)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIScrollViewDelegate viewForZoomingInScrollView:]](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619426-viewforzoominginscrollview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UISearchBar.hRemoved UISearchBar.autocapitalizationTypeRemoved UISearchBar.autocorrectionTypeRemoved UISearchBar.keyboardTypeRemoved UISearchBar.spellCheckingTypeModified [UISearchBar](https://developer.apple.com/documentation/uikit/uisearchbar)

|  | Protocols |
| --- | --- |
| From | UIBarPositioning |
| To | UIBarPositioning, UITextInputTraits |

Modified [-[UISearchBarDelegate searchBar:selectedScopeButtonIndexDidChange:]](https://developer.apple.com/documentation/uikit/uisearchbardelegate/1624280-searchbar)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBarDelegate searchBar:shouldChangeTextInRange:replacementText:]](https://developer.apple.com/documentation/uikit/uisearchbardelegate/1624328-searchbar)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBarDelegate searchBar:textDidChange:]](https://developer.apple.com/documentation/uikit/uisearchbardelegate/1624299-searchbar)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBarDelegate searchBarBookmarkButtonClicked:]](https://developer.apple.com/documentation/uikit/uisearchbardelegate/1624312-searchbarbookmarkbuttonclicked)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBarDelegate searchBarCancelButtonClicked:]](https://developer.apple.com/documentation/uikit/uisearchbardelegate/1624314-searchbarcancelbuttonclicked)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBarDelegate searchBarResultsListButtonClicked:]](https://developer.apple.com/documentation/uikit/uisearchbardelegate/1624305-searchbarresultslistbuttonclicke)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBarDelegate searchBarSearchButtonClicked:]](https://developer.apple.com/documentation/uikit/uisearchbardelegate/1624294-searchbarsearchbuttonclicked)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBarDelegate searchBarShouldBeginEditing:]](https://developer.apple.com/documentation/uikit/uisearchbardelegate/1624306-searchbarshouldbeginediting)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBarDelegate searchBarShouldEndEditing:]](https://developer.apple.com/documentation/uikit/uisearchbardelegate/1624329-searchbarshouldendediting)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBarDelegate searchBarTextDidBeginEditing:]](https://developer.apple.com/documentation/uikit/uisearchbardelegate/1624303-searchbartextdidbeginediting)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISearchBarDelegate searchBarTextDidEndEditing:]](https://developer.apple.com/documentation/uikit/uisearchbardelegate/1624301-searchbartextdidendediting)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UISearchController.h (Added)Added [UISearchController](https://developer.apple.com/documentation/uikit/uisearchcontroller)Added [UISearchController.active](https://developer.apple.com/documentation/uikit/uisearchcontroller/1618659-isactive)Added [UISearchController.delegate](https://developer.apple.com/documentation/uikit/uisearchcontroller/1618654-delegate)Added [UISearchController.dimsBackgroundDuringPresentation](https://developer.apple.com/documentation/uikit/uisearchcontroller/1618660-dimsbackgroundduringpresentation)Added [UISearchController.hidesNavigationBarDuringPresentation](https://developer.apple.com/documentation/uikit/uisearchcontroller/1618650-hidesnavigationbarduringpresenta)Added [-[UISearchController initWithSearchResultsController:]](https://developer.apple.com/documentation/uikit/uisearchcontroller/1618647-initwithsearchresultscontroller)Added [UISearchController.searchBar](https://developer.apple.com/documentation/uikit/uisearchcontroller/1618657-searchbar)Added [UISearchController.searchResultsController](https://developer.apple.com/documentation/uikit/uisearchcontroller/1618649-searchresultscontroller)Added [UISearchController.searchResultsUpdater](https://developer.apple.com/documentation/uikit/uisearchcontroller/1618661-searchresultsupdater)Added [UISearchControllerDelegate](https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate)Added [-[UISearchControllerDelegate didDismissSearchController:]](https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate/1618651-diddismisssearchcontroller)Added [-[UISearchControllerDelegate didPresentSearchController:]](https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate/1618646-didpresentsearchcontroller)Added [-[UISearchControllerDelegate presentSearchController:]](https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate/1618648-presentsearchcontroller)Added [-[UISearchControllerDelegate willDismissSearchController:]](https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate/1618655-willdismisssearchcontroller)Added [-[UISearchControllerDelegate willPresentSearchController:]](https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate/1618652-willpresentsearchcontroller)Added [UISearchResultsUpdating](https://developer.apple.com/documentation/uikit/uisearchresultsupdating)Added [-[UISearchResultsUpdating updateSearchResultsForSearchController:]](https://developer.apple.com/documentation/uikit/uisearchresultsupdating/1618658-updatesearchresults)UISearchDisplayController.hModified [UISearchDisplayController](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [-[UISearchDisplayController initWithSearchBar:contentsController:]](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/1620411-initwithsearchbar)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithSearchBar:(UISearchBar *)searchBar contentsController:(UIViewController *)viewController ``` |
| To | ``` - (instancetype)initWithSearchBar:(UISearchBar *)searchBar contentsController:(UIViewController *)viewController ``` |

Modified [-[UISearchDisplayDelegate searchDisplayController:didHideSearchResultsTableView:]](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/1620395-searchdisplaycontroller)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

Modified [-[UISearchDisplayDelegate searchDisplayController:didLoadSearchResultsTableView:]](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/1620398-searchdisplaycontroller)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

Modified [-[UISearchDisplayDelegate searchDisplayController:didShowSearchResultsTableView:]](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/1620396-searchdisplaycontroller)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

Modified [-[UISearchDisplayDelegate searchDisplayController:shouldReloadTableForSearchScope:]](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/1620409-searchdisplaycontroller)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

Modified [-[UISearchDisplayDelegate searchDisplayController:shouldReloadTableForSearchString:]](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/1620403-searchdisplaycontroller)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

Modified [-[UISearchDisplayDelegate searchDisplayController:willHideSearchResultsTableView:]](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/1620407-searchdisplaycontroller)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

Modified [-[UISearchDisplayDelegate searchDisplayController:willShowSearchResultsTableView:]](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/1620391-searchdisplaycontroller)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

Modified [-[UISearchDisplayDelegate searchDisplayController:willUnloadSearchResultsTableView:]](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/1620401-searchdisplaycontroller)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

Modified [-[UISearchDisplayDelegate searchDisplayControllerDidBeginSearch:]](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/1620410-searchdisplaycontrollerdidbegins)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

Modified [-[UISearchDisplayDelegate searchDisplayControllerDidEndSearch:]](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/1620402-searchdisplaycontrollerdidendsea)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

Modified [-[UISearchDisplayDelegate searchDisplayControllerWillBeginSearch:]](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/1620399-searchdisplaycontrollerwillbegin)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

Modified [-[UISearchDisplayDelegate searchDisplayControllerWillEndSearch:]](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/1620389-searchdisplaycontrollerwillendse)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

UISegmentedControl.hModified [-[UISegmentedControl initWithItems:]](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618569-initwithitems)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithItems:(NSArray *)items ``` |
| To | ``` - (instancetype)initWithItems:(NSArray *)items ``` |

Modified [UISegmentedControlStyleBar](https://developer.apple.com/documentation/uikit/uisegmentedcontrolstyle/uisegmentedcontrolstylebar)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [UISegmentedControlStyleBezeled](https://developer.apple.com/documentation/uikit/uisegmentedcontrolstyle/uisegmentedcontrolstylebezeled)

|  | Deprecation | Introduction |
| --- | --- | --- |
| From | -- | iOS 4.0 |
| To | iOS 7.0 | iOS 2.0 |

Modified [UISegmentedControlStyleBordered](https://developer.apple.com/documentation/uikit/uisegmentedcontrolstyle/uisegmentedcontrolstylebordered)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [UISegmentedControlStylePlain](https://developer.apple.com/documentation/uikit/uisegmentedcontrolstyle/uisegmentedcontrolstyleplain)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

UISplitViewController.hAdded [UISplitViewController.collapsed](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/1623185-iscollapsed)Added [UISplitViewController.displayMode](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/1623194-displaymode)Added [-[UISplitViewController displayModeButtonItem]](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/1623196-displaymodebuttonitem)Added [UISplitViewController.maximumPrimaryColumnWidth](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/1623180-maximumprimarycolumnwidth)Added [UISplitViewController.minimumPrimaryColumnWidth](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/1623198-minimumprimarycolumnwidth)Added [UISplitViewController.preferredDisplayMode](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/1623170-preferreddisplaymode)Added [UISplitViewController.preferredPrimaryColumnWidthFraction](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/1623183-preferredprimarycolumnwidthfract)Added [UISplitViewController.primaryColumnWidth](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/1623200-primarycolumnwidth)Added [-[UISplitViewController showDetailViewController:sender:]](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/1623182-showdetailviewcontroller)Added [-[UISplitViewController showViewController:sender:]](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/1623199-showviewcontroller)Added [-[UISplitViewControllerDelegate primaryViewControllerForCollapsingSplitViewController:]](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623197-primaryviewcontroller)Added [-[UISplitViewControllerDelegate primaryViewControllerForExpandingSplitViewController:]](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623188-primaryviewcontrollerforexpandin)Added [-[UISplitViewControllerDelegate splitViewController:collapseSecondaryViewController:ontoPrimaryViewController:]](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623184-splitviewcontroller)Added [-[UISplitViewControllerDelegate splitViewController:separateSecondaryViewControllerFromPrimaryViewController:]](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623189-splitviewcontroller)Added [-[UISplitViewControllerDelegate splitViewController:showDetailViewController:sender:]](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623204-splitviewcontroller)Added [-[UISplitViewControllerDelegate splitViewController:showViewController:sender:]](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623168-splitviewcontroller)Added [-[UISplitViewControllerDelegate splitViewController:willChangeToDisplayMode:]](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623176-splitviewcontroller)Added [-[UISplitViewControllerDelegate targetDisplayModeForActionInSplitViewController:]](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623192-targetdisplaymodeforactioninspli)Added [-[UIViewController collapseSecondaryViewController:forSplitViewController:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1623193-collapsesecondaryviewcontroller)Added [-[UIViewController separateSecondaryViewControllerForSplitViewController:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1623191-separatesecondaryviewcontroller)Added [UISplitViewControllerAutomaticDimension](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/1623166-automaticdimension)Added [UISplitViewControllerDisplayMode](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode)Added [UISplitViewControllerDisplayModeAllVisible](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode/allvisible)Added [UISplitViewControllerDisplayModeAutomatic](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode/automatic)Added [UISplitViewControllerDisplayModePrimaryHidden](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode/primaryhidden)Added [UISplitViewControllerDisplayModePrimaryOverlay](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdisplaymode/uisplitviewcontrollerdisplaymodeprimaryoverlay)Modified [-[UISplitViewControllerDelegate splitViewController:popoverController:willPresentViewController:]](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623186-splitviewcontroller)

|  | Deprecation | Introduction | Optional |
| --- | --- | --- | --- |
| From | -- | iOS 3.2 | -- |
| To | iOS 8.0 | iOS 2.0 | yes |

Modified [-[UISplitViewControllerDelegate splitViewController:shouldHideViewController:inOrientation:]](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623174-splitviewcontroller)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

Modified [-[UISplitViewControllerDelegate splitViewController:willHideViewController:withBarButtonItem:forPopoverController:]](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623175-splitviewcontroller)

|  | Deprecation | Introduction | Optional |
| --- | --- | --- | --- |
| From | -- | iOS 3.2 | -- |
| To | iOS 8.0 | iOS 2.0 | yes |

Modified [-[UISplitViewControllerDelegate splitViewController:willShowViewController:invalidatingBarButtonItem:]](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623202-splitviewcontroller)

|  | Deprecation | Introduction | Optional |
| --- | --- | --- | --- |
| From | -- | iOS 3.2 | -- |
| To | iOS 8.0 | iOS 2.0 | yes |

Modified [-[UISplitViewControllerDelegate splitViewControllerPreferredInterfaceOrientationForPresentation:]](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623169-splitviewcontrollerpreferredinte)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UISplitViewControllerDelegate splitViewControllerSupportedInterfaceOrientations:]](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623178-splitviewcontrollersupportedinte)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UIStateRestoration.hModified [-[UIStateRestoring applicationFinishedRestoringState]](https://developer.apple.com/documentation/uikit/uistaterestoring/1616864-applicationfinishedrestoringstat)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIStateRestoring decodeRestorableStateWithCoder:]](https://developer.apple.com/documentation/uikit/uistaterestoring/1616854-decoderestorablestate)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIStateRestoring encodeRestorableStateWithCoder:]](https://developer.apple.com/documentation/uikit/uistaterestoring/1616866-encoderestorablestatewithcoder)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [UIStateRestoring.objectRestorationClass](https://developer.apple.com/documentation/uikit/uistaterestoring/1616851-objectrestorationclass)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) Class<UIObjectRestoration> *objectRestorationClass ``` |
| To | ``` @property(nonatomic, readonly) Class<UIObjectRestoration> objectRestorationClass ``` |

UIStoryboardSegue.hModified [-[UIStoryboardSegue initWithIdentifier:source:destination:]](https://developer.apple.com/documentation/uikit/uistoryboardsegue/1621908-initwithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithIdentifier:(NSString *)identifier source:(UIViewController *)source destination:(UIViewController *)destination ``` |
| To | ``` - (instancetype)initWithIdentifier:(NSString *)identifier source:(UIViewController *)source destination:(UIViewController *)destination ``` |

Modified [+[UIStoryboardSegue segueWithIdentifier:source:destination:performHandler:]](https://developer.apple.com/documentation/uikit/uistoryboardsegue/1621910-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)segueWithIdentifier:(NSString *)identifier source:(UIViewController *)source destination:(UIViewController *)destination performHandler:(void (^)(void))performHandler ``` |
| To | ``` + (instancetype)segueWithIdentifier:(NSString *)identifier source:(UIViewController *)source destination:(UIViewController *)destination performHandler:(void (^)(void))performHandler ``` |

UIStringDrawing.hModified [UILineBreakModeCharacterWrap](https://developer.apple.com/documentation/uikit/uilinebreakmode/uilinebreakmodecharacterwrap)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 6.0 |

Modified [UILineBreakModeClip](https://developer.apple.com/documentation/uikit/uilinebreakmode/uilinebreakmodeclip)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 6.0 |

Modified [UILineBreakModeHeadTruncation](https://developer.apple.com/documentation/uikit/uilinebreakmode/uilinebreakmodeheadtruncation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 6.0 |

Modified [UILineBreakModeMiddleTruncation](https://developer.apple.com/documentation/uikit/uilinebreakmode/uilinebreakmodemiddletruncation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 6.0 |

Modified [UILineBreakModeTailTruncation](https://developer.apple.com/documentation/uikit/uilinebreakmode/uilinebreakmodetailtruncation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 6.0 |

Modified [UILineBreakModeWordWrap](https://developer.apple.com/documentation/uikit/uilinebreakmode/uilinebreakmodewordwrap)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 6.0 |

Modified [UITextAlignmentCenter](https://developer.apple.com/documentation/uikit/uitextalignment/uitextalignmentcenter)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 6.0 |

Modified [UITextAlignmentLeft](https://developer.apple.com/documentation/uikit/uitextalignment/uitextalignmentleft)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 6.0 |

Modified [UITextAlignmentRight](https://developer.apple.com/documentation/uikit/uitextalignment/uitextalignmentright)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 6.0 |

UISwitch.hModified [-[UISwitch initWithFrame:]](https://developer.apple.com/documentation/uikit/uiswitch/1623682-initwithframe)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFrame:(CGRect)frame ``` |
| To | ``` - (instancetype)initWithFrame:(CGRect)frame ``` |

UITabBar.hModified [UITabBar.selectedImageTintColor](https://developer.apple.com/documentation/uikit/uitabbar/1623470-selectedimagetintcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [-[UITabBarDelegate tabBar:didBeginCustomizingItems:]](https://developer.apple.com/documentation/uikit/uitabbardelegate/1623471-tabbar)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITabBarDelegate tabBar:didEndCustomizingItems:changed:]](https://developer.apple.com/documentation/uikit/uitabbardelegate/1623447-tabbar)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITabBarDelegate tabBar:didSelectItem:]](https://developer.apple.com/documentation/uikit/uitabbardelegate/1623463-tabbar)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITabBarDelegate tabBar:willBeginCustomizingItems:]](https://developer.apple.com/documentation/uikit/uitabbardelegate/1623451-tabbar)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITabBarDelegate tabBar:willEndCustomizingItems:changed:]](https://developer.apple.com/documentation/uikit/uitabbardelegate/1623464-tabbar)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UITabBarController.hModified [-[UITabBarControllerDelegate tabBarController:animationControllerForTransitionFromViewController:toViewController:]](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621167-tabbarcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITabBarControllerDelegate tabBarController:didEndCustomizingViewControllers:changed:]](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621168-tabbarcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITabBarControllerDelegate tabBarController:didSelectViewController:]](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621173-tabbarcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITabBarControllerDelegate tabBarController:interactionControllerForAnimationController:]](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621170-tabbarcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITabBarControllerDelegate tabBarController:shouldSelectViewController:]](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621166-tabbarcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITabBarControllerDelegate tabBarController:willBeginCustomizingViewControllers:]](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621179-tabbarcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITabBarControllerDelegate tabBarController:willEndCustomizingViewControllers:changed:]](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621178-tabbarcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITabBarControllerDelegate tabBarControllerPreferredInterfaceOrientationForPresentation:]](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621176-tabbarcontrollerpreferredinterfa)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITabBarControllerDelegate tabBarControllerSupportedInterfaceOrientations:]](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621180-tabbarcontrollersupportedinterfa)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UITabBarItem.hModified [-[UITabBarItem initWithTabBarSystemItem:tag:]](https://developer.apple.com/documentation/uikit/uitabbaritem/1617067-initwithtabbarsystemitem)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTabBarSystemItem:(UITabBarSystemItem)systemItem tag:(NSInteger)tag ``` |
| To | ``` - (instancetype)initWithTabBarSystemItem:(UITabBarSystemItem)systemItem tag:(NSInteger)tag ``` |

Modified [-[UITabBarItem initWithTitle:image:tag:]](https://developer.apple.com/documentation/uikit/uitabbaritem/1617056-initwithtitle)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTitle:(NSString *)title image:(UIImage *)image tag:(NSInteger)tag ``` |
| To | ``` - (instancetype)initWithTitle:(NSString *)title image:(UIImage *)image tag:(NSInteger)tag ``` |

UITableView.hAdded [UITableView.separatorEffect](https://developer.apple.com/documentation/uikit/uitableview/1614865-separatoreffect)Added [-[UITableViewDelegate tableView:editActionsForRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614956-tableview)Added [UITableViewRowAction](https://developer.apple.com/documentation/uikit/uitableviewrowaction)Added [UITableViewRowAction.backgroundColor](https://developer.apple.com/documentation/uikit/uitableviewrowaction/1614995-backgroundcolor)Added [UITableViewRowAction.backgroundEffect](https://developer.apple.com/documentation/uikit/uitableviewrowaction/1614990-backgroundeffect)Added [+[UITableViewRowAction rowActionWithStyle:title:handler:]](https://developer.apple.com/documentation/uikit/uitableviewrowaction/1614893-init)Added [UITableViewRowAction.style](https://developer.apple.com/documentation/uikit/uitableviewrowaction/1614887-style)Added [UITableViewRowAction.title](https://developer.apple.com/documentation/uikit/uitableviewrowaction/1614993-title)Added [UITableViewRowActionStyle](https://developer.apple.com/documentation/uikit/uitableviewrowaction/style)Added [UITableViewRowActionStyleDefault](https://developer.apple.com/documentation/uikit/uitableviewrowactionstyle/uitableviewrowactionstyledefault)Added [UITableViewRowActionStyleDestructive](https://developer.apple.com/documentation/uikit/uitableviewrowaction/style/1614917-destructive)Added [UITableViewRowActionStyleNormal](https://developer.apple.com/documentation/uikit/uitableviewrowactionstyle/uitableviewrowactionstylenormal)Modified [-[UITableView initWithFrame:style:]](https://developer.apple.com/documentation/uikit/uitableview/1614886-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFrame:(CGRect)frame style:(UITableViewStyle)style ``` |
| To | ``` - (instancetype)initWithFrame:(CGRect)frame style:(UITableViewStyle)style ``` |

Modified [-[UITableViewDataSource numberOfSectionsInTableView:]](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614860-numberofsectionsintableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDataSource sectionIndexTitlesForTableView:]](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614857-sectionindextitles)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDataSource tableView:canEditRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614900-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDataSource tableView:canMoveRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614927-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDataSource tableView:commitEditingStyle:forRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614871-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDataSource tableView:moveRowAtIndexPath:toIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614867-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDataSource tableView:sectionForSectionIndexTitle:atIndex:]](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614933-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDataSource tableView:titleForFooterInSection:]](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614994-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDataSource tableView:titleForHeaderInSection:]](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614850-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:accessoryButtonTappedForRowWithIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614996-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:accessoryTypeForRowWithIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614948-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:canPerformAction:forRowAtIndexPath:withSender:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614898-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:didDeselectRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614916-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:didEndDisplayingCell:forRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614870-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:didEndDisplayingFooterView:forSection:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614856-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:didEndDisplayingHeaderView:forSection:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614971-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:didEndEditingRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614963-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:didHighlightRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614982-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:didSelectRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614877-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:didUnhighlightRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614868-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:editingStyleForRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614869-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:estimatedHeightForFooterInSection:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614939-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:estimatedHeightForHeaderInSection:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614854-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:estimatedHeightForRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614926-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:heightForFooterInSection:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614967-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:heightForHeaderInSection:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614855-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:heightForRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614998-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:indentationLevelForRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614966-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:performAction:forRowAtIndexPath:withSender:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614980-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:shouldHighlightRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614988-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:shouldIndentWhileEditingRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614873-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:shouldShowMenuForRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614950-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:targetIndexPathForMoveFromRowAtIndexPath:toProposedIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614953-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:titleForDeleteConfirmationButtonForRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614970-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:viewForFooterInSection:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614946-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:viewForHeaderInSection:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614901-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:willBeginEditingRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614907-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:willDeselectRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614977-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:willDisplayCell:forRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614883-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:willDisplayFooterView:forSection:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614941-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:willDisplayHeaderView:forSection:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614905-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITableViewDelegate tableView:willSelectRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614943-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UITableViewCell.hModified [-[UITableViewCell initWithStyle:reuseIdentifier:]](https://developer.apple.com/documentation/uikit/uitableviewcell/1623276-initwithstyle)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier ``` |
| To | ``` - (instancetype)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier ``` |

UITableViewController.hModified [-[UITableViewController initWithStyle:]](https://developer.apple.com/documentation/uikit/uitableviewcontroller/1614754-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithStyle:(UITableViewStyle)style ``` |
| To | ``` - (instancetype)initWithStyle:(UITableViewStyle)style ``` |

UITableViewHeaderFooterView.hModified [-[UITableViewHeaderFooterView initWithReuseIdentifier:]](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/1624918-initwithreuseidentifier)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithReuseIdentifier:(NSString *)reuseIdentifier ``` |
| To | ``` - (instancetype)initWithReuseIdentifier:(NSString *)reuseIdentifier ``` |

UITextField.hModified [-[UITextFieldDelegate textField:shouldChangeCharactersInRange:replacementString:]](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619599-textfield)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextFieldDelegate textFieldDidBeginEditing:]](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619590-textfielddidbeginediting)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextFieldDelegate textFieldDidEndEditing:]](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619591-textfielddidendediting)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextFieldDelegate textFieldShouldBeginEditing:]](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619601-textfieldshouldbeginediting)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextFieldDelegate textFieldShouldClear:]](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619594-textfieldshouldclear)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextFieldDelegate textFieldShouldEndEditing:]](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619592-textfieldshouldendediting)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextFieldDelegate textFieldShouldReturn:]](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619603-textfieldshouldreturn)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UITextInput.hModified [-[UITextInput characterOffsetOfPosition:withinRange:]](https://developer.apple.com/documentation/uikit/uitextinput/1614545-characteroffsetofposition)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextInput dictationRecognitionFailed]](https://developer.apple.com/documentation/uikit/uitextinput/1614519-dictationrecognitionfailed)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextInput dictationRecordingDidEnd]](https://developer.apple.com/documentation/uikit/uitextinput/1614507-dictationrecordingdidend)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextInput frameForDictationResultPlaceholder:]](https://developer.apple.com/documentation/uikit/uitextinput/1614493-framefordictationresultplacehold)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextInput insertDictationResult:]](https://developer.apple.com/documentation/uikit/uitextinput/1614568-insertdictationresult)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextInput insertDictationResultPlaceholder]](https://developer.apple.com/documentation/uikit/uitextinput/1614466-insertdictationresultplaceholder)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextInput positionWithinRange:atCharacterOffset:]](https://developer.apple.com/documentation/uikit/uitextinput/1614542-positionwithinrange)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextInput removeDictationResultPlaceholder:willInsertResult:]](https://developer.apple.com/documentation/uikit/uitextinput/1614546-removedictationresultplaceholder)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextInput shouldChangeTextInRange:replacementText:]](https://developer.apple.com/documentation/uikit/uitextinput/1614495-shouldchangetext)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextInput textStylingAtPosition:inDirection:]](https://developer.apple.com/documentation/uikit/uitextinput/1614566-textstyling)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextInputStringTokenizer initWithTextInput:]](https://developer.apple.com/documentation/uikit/uitextinputstringtokenizer/1614469-initwithtextinput)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTextInput:(UIResponder<UITextInput> *)textInput ``` |
| To | ``` - (instancetype)initWithTextInput:(UIResponder<UITextInput> *)textInput ``` |

Modified [UITextInputTextBackgroundColorKey](https://developer.apple.com/documentation/uikit/uitextinputtextbackgroundcolorkey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [UITextInputTextColorKey](https://developer.apple.com/documentation/uikit/uitextinputtextcolorkey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [UITextInputTextFontKey](https://developer.apple.com/documentation/uikit/uitextinputtextfontkey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

UITextView.hModified [-[UITextViewDelegate textView:shouldChangeTextInRange:replacementText:]](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618630-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextViewDelegate textView:shouldInteractWithTextAttachment:inRange:]](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618621-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextViewDelegate textView:shouldInteractWithURL:inRange:]](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618606-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextViewDelegate textViewDidBeginEditing:]](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618610-textviewdidbeginediting)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextViewDelegate textViewDidChange:]](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618599-textviewdidchange)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextViewDelegate textViewDidChangeSelection:]](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618620-textviewdidchangeselection)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextViewDelegate textViewDidEndEditing:]](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618628-textviewdidendediting)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextViewDelegate textViewShouldBeginEditing:]](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618608-textviewshouldbeginediting)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UITextViewDelegate textViewShouldEndEditing:]](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618603-textviewshouldendediting)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UITouch.hAdded [UITouch.majorRadius](https://developer.apple.com/documentation/uikit/uitouch/1618106-majorradius)Added [UITouch.majorRadiusTolerance](https://developer.apple.com/documentation/uikit/uitouch/1618120-majorradiustolerance)UITraitCollection.h (Added)Added [UITraitCollection](https://developer.apple.com/documentation/uikit/uitraitcollection)Added [-[UITraitCollection containsTraitsInCollection:]](https://developer.apple.com/documentation/uikit/uitraitcollection/1623506-containstraits)Added [UITraitCollection.displayScale](https://developer.apple.com/documentation/uikit/uitraitcollection/1623519-displayscale)Added [UITraitCollection.horizontalSizeClass](https://developer.apple.com/documentation/uikit/uitraitcollection/1623508-horizontalsizeclass)Added [+[UITraitCollection traitCollectionWithDisplayScale:]](https://developer.apple.com/documentation/uikit/uitraitcollection/1623518-traitcollectionwithdisplayscale)Added [+[UITraitCollection traitCollectionWithHorizontalSizeClass:]](https://developer.apple.com/documentation/uikit/uitraitcollection/1623520-init)Added [+[UITraitCollection traitCollectionWithTraitsFromCollections:]](https://developer.apple.com/documentation/uikit/uitraitcollection/1623512-traitcollectionwithtraitsfromcol)Added [+[UITraitCollection traitCollectionWithUserInterfaceIdiom:]](https://developer.apple.com/documentation/uikit/uitraitcollection/1623507-init)Added [+[UITraitCollection traitCollectionWithVerticalSizeClass:]](https://developer.apple.com/documentation/uikit/uitraitcollection/1623505-init)Added [UITraitCollection.userInterfaceIdiom](https://developer.apple.com/documentation/uikit/uitraitcollection/1623521-userinterfaceidiom)Added [UITraitCollection.verticalSizeClass](https://developer.apple.com/documentation/uikit/uitraitcollection/1623513-verticalsizeclass)Added [UITraitEnvironment](https://developer.apple.com/documentation/uikit/uitraitenvironment)Added [UITraitEnvironment.traitCollection](https://developer.apple.com/documentation/uikit/uitraitenvironment/1623514-traitcollection)Added [-[UITraitEnvironment traitCollectionDidChange:]](https://developer.apple.com/documentation/uikit/uitraitenvironment/1623516-traitcollectiondidchange)UIUserNotificationSettings.h (Added)Added [UIMutableUserNotificationAction](https://developer.apple.com/documentation/uikit/uimutableusernotificationaction)Added [UIMutableUserNotificationAction.activationMode](https://developer.apple.com/documentation/uikit/uimutableusernotificationaction/1615372-activationmode)Added [UIMutableUserNotificationAction.authenticationRequired](https://developer.apple.com/documentation/uikit/uimutableusernotificationaction/1615389-authenticationrequired)Added [UIMutableUserNotificationAction.destructive](https://developer.apple.com/documentation/uikit/uimutableusernotificationaction/1615322-destructive)Added [UIMutableUserNotificationAction.identifier](https://developer.apple.com/documentation/uikit/uimutableusernotificationaction/1615379-identifier)Added [UIMutableUserNotificationAction.title](https://developer.apple.com/documentation/uikit/uimutableusernotificationaction/1615370-title)Added [UIMutableUserNotificationCategory](https://developer.apple.com/documentation/uikit/uimutableusernotificationcategory)Added [UIMutableUserNotificationCategory.identifier](https://developer.apple.com/documentation/uikit/uimutableusernotificationcategory/1615376-identifier)Added [-[UIMutableUserNotificationCategory setActions:forContext:]](https://developer.apple.com/documentation/uikit/uimutableusernotificationcategory/1615397-setactions)Added [UIUserNotificationAction](https://developer.apple.com/documentation/uikit/uiusernotificationaction)Added [UIUserNotificationAction.activationMode](https://developer.apple.com/documentation/uikit/uiusernotificationaction/1615329-activationmode)Added [UIUserNotificationAction.authenticationRequired](https://developer.apple.com/documentation/uikit/uiusernotificationaction/1615381-isauthenticationrequired)Added [UIUserNotificationAction.destructive](https://developer.apple.com/documentation/uikit/uiusernotificationaction/1615385-isdestructive)Added [UIUserNotificationAction.identifier](https://developer.apple.com/documentation/uikit/uiusernotificationaction/1615361-identifier)Added [UIUserNotificationAction.title](https://developer.apple.com/documentation/uikit/uiusernotificationaction/1615358-title)Added [UIUserNotificationCategory](https://developer.apple.com/documentation/uikit/uiusernotificationcategory)Added [-[UIUserNotificationCategory actionsForContext:]](https://developer.apple.com/documentation/uikit/uiusernotificationcategory/1615374-actionsforcontext)Added [UIUserNotificationCategory.identifier](https://developer.apple.com/documentation/uikit/uiusernotificationcategory/1615383-identifier)Added [UIUserNotificationSettings](https://developer.apple.com/documentation/uikit/uiusernotificationsettings)Added [UIUserNotificationSettings.categories](https://developer.apple.com/documentation/uikit/uiusernotificationsettings/1615365-categories)Added [+[UIUserNotificationSettings settingsForTypes:categories:]](https://developer.apple.com/documentation/uikit/uiusernotificationsettings/1615401-settingsfortypes)Added [UIUserNotificationSettings.types](https://developer.apple.com/documentation/uikit/uiusernotificationsettings/1615321-types)Added [UIUserNotificationActionContext](https://developer.apple.com/documentation/uikit/uiusernotificationactioncontext)Added [UIUserNotificationActionContextDefault](https://developer.apple.com/documentation/uikit/uiusernotificationactioncontext/default)Added [UIUserNotificationActionContextMinimal](https://developer.apple.com/documentation/uikit/uiusernotificationactioncontext/minimal)Added [UIUserNotificationActivationMode](https://developer.apple.com/documentation/uikit/uiusernotificationactivationmode)Added [UIUserNotificationActivationModeBackground](https://developer.apple.com/documentation/uikit/uiusernotificationactivationmode/background)Added [UIUserNotificationActivationModeForeground](https://developer.apple.com/documentation/uikit/uiusernotificationactivationmode/uiusernotificationactivationmodeforeground)Added [UIUserNotificationType](https://developer.apple.com/documentation/uikit/uiusernotificationtype)Added [UIUserNotificationTypeAlert](https://developer.apple.com/documentation/uikit/uiusernotificationtype/uiusernotificationtypealert)Added [UIUserNotificationTypeBadge](https://developer.apple.com/documentation/uikit/uiusernotificationtype/uiusernotificationtypebadge)Added [UIUserNotificationTypeNone](https://developer.apple.com/documentation/uikit/uiusernotificationtype/uiusernotificationtypenone)Added [UIUserNotificationTypeSound](https://developer.apple.com/documentation/uikit/uiusernotificationtype/uiusernotificationtypesound)UIVideoEditorController.hModified [-[UIVideoEditorControllerDelegate videoEditorController:didFailWithError:]](https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate/1622342-videoeditorcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIVideoEditorControllerDelegate videoEditorController:didSaveEditedVideoToPath:]](https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate/1622336-videoeditorcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIVideoEditorControllerDelegate videoEditorControllerDidCancel:]](https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate/1622335-videoeditorcontrollerdidcancel)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UIView.hAdded [UICoordinateSpace](https://developer.apple.com/documentation/uikit/uicoordinatespace)Added [UICoordinateSpace.bounds](https://developer.apple.com/documentation/uikit/uicoordinatespace/1622443-bounds)Added [-[UICoordinateSpace convertPoint:fromCoordinateSpace:]](https://developer.apple.com/documentation/uikit/uicoordinatespace/1622550-convertpoint)Added [-[UICoordinateSpace convertPoint:toCoordinateSpace:]](https://developer.apple.com/documentation/uikit/uicoordinatespace/1622609-convertpoint)Added [-[UICoordinateSpace convertRect:fromCoordinateSpace:]](https://developer.apple.com/documentation/uikit/uicoordinatespace/1622661-convertrect)Added [-[UICoordinateSpace convertRect:toCoordinateSpace:]](https://developer.apple.com/documentation/uikit/uicoordinatespace/1622564-convert)Added [UIView.layoutMargins](https://developer.apple.com/documentation/uikit/uiview/1622566-layoutmargins)Added [-[UIView layoutMarginsDidChange]](https://developer.apple.com/documentation/uikit/uiview/1622416-layoutmarginsdidchange)Added [UIView.maskView](https://developer.apple.com/documentation/uikit/uiview/1622557-maskview)Added [UIView.preservesSuperviewLayoutMargins](https://developer.apple.com/documentation/uikit/uiview/1622653-preservessuperviewlayoutmargins)Added [-[UIView systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:]](https://developer.apple.com/documentation/uikit/uiview/1622623-systemlayoutsizefittingsize)Modified [UIView](https://developer.apple.com/documentation/uikit/uiview)

|  | Protocols |
| --- | --- |
| From | NSCoding, UIAppearance, UIAppearanceContainer, UIDynamicItem |
| To | NSCoding, UIAppearance, UIAppearanceContainer, UICoordinateSpace, UIDynamicItem, UITraitEnvironment |

Modified [-[UIView initWithFrame:]](https://developer.apple.com/documentation/uikit/uiview/1622488-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFrame:(CGRect)frame ``` |
| To | ``` - (instancetype)initWithFrame:(CGRect)frame ``` |

Modified [UIViewAnimationOptionOverrideInheritedOptions](https://developer.apple.com/documentation/uikit/uiviewanimationoptions/uiviewanimationoptionoverrideinheritedoptions)

|  | Introduction |
| --- | --- |
| From | iOS 7.0 |
| To | iOS 4.0 |

Modified [UIViewAnimationOptionTransitionCrossDissolve](https://developer.apple.com/documentation/uikit/uiview/animationoptions/1622499-transitioncrossdissolve)

|  | Introduction |
| --- | --- |
| From | iOS 5.0 |
| To | iOS 4.0 |

Modified [UIViewAnimationOptionTransitionFlipFromBottom](https://developer.apple.com/documentation/uikit/uiview/animationoptions/1622632-transitionflipfrombottom)

|  | Introduction |
| --- | --- |
| From | iOS 5.0 |
| To | iOS 4.0 |

Modified [UIViewAnimationOptionTransitionFlipFromTop](https://developer.apple.com/documentation/uikit/uiviewanimationoptions/uiviewanimationoptiontransitionflipfromtop)

|  | Introduction |
| --- | --- |
| From | iOS 5.0 |
| To | iOS 4.0 |

UIViewController.hRemoved UIViewController(CustomTransitioning)Added [UIContentContainer](https://developer.apple.com/documentation/uikit/uicontentcontainer)Added [UIContentContainer.preferredContentSize](https://developer.apple.com/documentation/uikit/uicontentcontainer/1621481-preferredcontentsize)Added [-[UIContentContainer preferredContentSizeDidChangeForChildContentContainer:]](https://developer.apple.com/documentation/uikit/uicontentcontainer/1621351-preferredcontentsizedidchangefor)Added [-[UIContentContainer sizeForChildContentContainer:withParentContainerSize:]](https://developer.apple.com/documentation/uikit/uicontentcontainer/1621484-sizeforchildcontentcontainer)Added [-[UIContentContainer systemLayoutFittingSizeDidChangeForChildContentContainer:]](https://developer.apple.com/documentation/uikit/uicontentcontainer/1621424-systemlayoutfittingsizedidchange)Added [-[UIContentContainer viewWillTransitionToSize:withTransitionCoordinator:]](https://developer.apple.com/documentation/uikit/uicontentcontainer/1621466-viewwilltransitiontosize)Added [-[UIContentContainer willTransitionToTraitCollection:withTransitionCoordinator:]](https://developer.apple.com/documentation/uikit/uicontentcontainer/1621511-willtransitiontotraitcollection)Added [UIViewController.extensionContext](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621411-extensioncontext)Added [-[UIViewController overrideTraitCollectionForChildViewController:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621486-overridetraitcollection)Added [UIViewController.popoverPresentationController](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621428-popoverpresentationcontroller)Added [UIViewController.presentationController](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621426-presentationcontroller)Added [-[UIViewController setOverrideTraitCollection:forChildViewController:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621406-setoverridetraitcollection)Added [-[UIViewController showDetailViewController:sender:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621432-showdetailviewcontroller)Added [-[UIViewController showViewController:sender:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621377-showviewcontroller)Added [-[UIViewController targetViewControllerForAction:sender:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621415-targetviewcontroller)Added [UIModalPresentationOverCurrentContext](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/overcurrentcontext)Added [UIModalPresentationOverFullScreen](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/uimodalpresentationoverfullscreen)Added [UIModalPresentationPopover](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/uimodalpresentationpopover)Added UIViewController(NSExtensionAdditions)Added UIViewController(UIAdaptivePresentations)Added UIViewController(UIViewControllerTransitioning)Added [UIViewControllerShowDetailTargetDidChangeNotification](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621368-showdetailtargetdidchangenotific)Modified [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller)

|  | Protocols |
| --- | --- |
| From | NSCoding, UIAppearanceContainer |
| To | NSCoding, UIAppearanceContainer, UIContentContainer, UITraitEnvironment |

Modified [-[UIViewController didRotateFromInterfaceOrientation:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621492-didrotatefrominterfaceorientatio)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [-[UIViewController initWithNibName:bundle:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621359-initwithnibname)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil ``` |
| To | ``` - (instancetype)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil ``` |

Modified [UIViewController.interfaceOrientation](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621373-interfaceorientation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [UIViewController.restorationClass](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621472-restorationclass)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readwrite, assign) Class<UIViewControllerRestoration> *restorationClass ``` |
| To | ``` @property(nonatomic, readwrite, assign) Class<UIViewControllerRestoration> restorationClass ``` |

Modified [-[UIViewController rotatingFooterView]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621402-rotatingfooterview)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [-[UIViewController rotatingHeaderView]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621412-rotatingheaderview)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [UIViewController.searchDisplayController](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621420-searchdisplaycontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [-[UIViewController shouldAutomaticallyForwardRotationMethods]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621480-shouldautomaticallyforwardrotati)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [-[UIViewController willAnimateRotationToInterfaceOrientation:duration:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621458-willanimaterotation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [-[UIViewController willRotateToInterfaceOrientation:duration:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621376-willrotate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

UIViewControllerTransitionCoordinator.hRemoved UIViewController(TransitionCoordinator)Added [-[UIViewControllerTransitionCoordinatorContext targetTransform]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619289-targettransform)Added [-[UIViewControllerTransitionCoordinatorContext viewForKey:]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619302-viewforkey)Added UIViewController(UIViewControllerTransitionCoordinator)UIViewControllerTransitioning.hAdded [-[UIViewControllerContextTransitioning targetTransform]](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622036-targettransform)Added [-[UIViewControllerContextTransitioning viewForKey:]](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622055-view)Added [-[UIViewControllerTransitioningDelegate presentationControllerForPresentedViewController:presentingViewController:sourceViewController:]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate/1622057-presentationcontroller)Added [UITransitionContextFromViewKey](https://developer.apple.com/documentation/uikit/uitransitioncontextfromviewkey)Added [UITransitionContextToViewKey](https://developer.apple.com/documentation/uikit/uitransitioncontextviewkey/1622062-to)Modified [-[UIViewControllerAnimatedTransitioning animationEnded:]](https://developer.apple.com/documentation/uikit/uiviewcontrolleranimatedtransitioning/1622059-animationended)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIViewControllerInteractiveTransitioning completionCurve]](https://developer.apple.com/documentation/uikit/uiviewcontrollerinteractivetransitioning/1622027-completioncurve)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIViewControllerInteractiveTransitioning completionSpeed]](https://developer.apple.com/documentation/uikit/uiviewcontrollerinteractivetransitioning/1622031-completionspeed)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIViewControllerTransitioningDelegate animationControllerForDismissedController:]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate/1622047-animationcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIViewControllerTransitioningDelegate animationControllerForPresentedController:presentingController:sourceController:]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate/1622037-animationcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIViewControllerTransitioningDelegate interactionControllerForDismissal:]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate/1622030-interactioncontrollerfordismissa)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIViewControllerTransitioningDelegate interactionControllerForPresentation:]](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate/1622050-interactioncontrollerforpresenta)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

UIVisualEffectView.h (Added)Added [UIBlurEffect](https://developer.apple.com/documentation/uikit/uiblureffect)Added [+[UIBlurEffect effectWithStyle:]](https://developer.apple.com/documentation/uikit/uiblureffect/1615060-init)Added [UIVibrancyEffect](https://developer.apple.com/documentation/uikit/uivibrancyeffect)Added [+[UIVibrancyEffect effectForBlurEffect:]](https://developer.apple.com/documentation/uikit/uivibrancyeffect/1615064-effectforblureffect)Added [UIVisualEffect](https://developer.apple.com/documentation/uikit/uivisualeffect)Added [UIVisualEffectView](https://developer.apple.com/documentation/uikit/uivisualeffectview)Added [UIVisualEffectView.contentView](https://developer.apple.com/documentation/uikit/uivisualeffectview/1615068-contentview)Added [UIVisualEffectView.effect](https://developer.apple.com/documentation/uikit/uivisualeffectview/1615072-effect)Added [-[UIVisualEffectView initWithEffect:]](https://developer.apple.com/documentation/uikit/uivisualeffectview/1615051-init)Added [UIBlurEffectStyle](https://developer.apple.com/documentation/uikit/uiblureffectstyle)Added [UIBlurEffectStyleDark](https://developer.apple.com/documentation/uikit/uiblureffectstyle/uiblureffectstyledark)Added [UIBlurEffectStyleExtraLight](https://developer.apple.com/documentation/uikit/uiblureffectstyle/uiblureffectstyleextralight)Added [UIBlurEffectStyleLight](https://developer.apple.com/documentation/uikit/uiblureffect/style/light)UIWebView.hModified [-[UIWebViewDelegate webView:didFailLoadWithError:]](https://developer.apple.com/documentation/uikit/uiwebviewdelegate/1617970-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIWebViewDelegate webView:shouldStartLoadWithRequest:navigationType:]](https://developer.apple.com/documentation/uikit/uiwebviewdelegate/1617945-webview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIWebViewDelegate webViewDidFinishLoad:]](https://developer.apple.com/documentation/uikit/uiwebviewdelegate/1617969-webviewdidfinishload)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[UIWebViewDelegate webViewDidStartLoad:]](https://developer.apple.com/documentation/uikit/uiwebviewdelegate/1617947-webviewdidstartload)

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
