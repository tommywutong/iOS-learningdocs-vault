---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/AppKit.html
archived_at: '2026-07-15T07:34:43.680525Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# AppKit Changes

## AppKit

NSATSTypesetter.hRemoved [-[NSATSTypesetter attributedString]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1530598-attributedstring)Removed [-[NSATSTypesetter bidiProcessingEnabled]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1524295-bidiprocessingenabled)Removed [-[NSATSTypesetter currentTextContainer]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1527830-currenttextcontainer)Removed [-[NSATSTypesetter hyphenationFactor]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1526758-hyphenationfactor)Removed [-[NSATSTypesetter layoutManager]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1535366-layoutmanager)Removed [-[NSATSTypesetter lineFragmentPadding]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1532628-linefragmentpadding)Removed [-[NSATSTypesetter paragraphGlyphRange]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1528373-paragraphglyphrange)Removed [-[NSATSTypesetter paragraphSeparatorGlyphRange]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1531108-paragraphseparatorglyphrange)Removed [-[NSATSTypesetter setAttributedString:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1530598-attributedstring)Removed [-[NSATSTypesetter setBidiProcessingEnabled:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1524295-bidiprocessingenabled)Removed [-[NSATSTypesetter setHyphenationFactor:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1526758-hyphenationfactor)Removed [-[NSATSTypesetter setLineFragmentPadding:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1532628-linefragmentpadding)Removed [-[NSATSTypesetter setTypesetterBehavior:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1533819-typesetterbehavior)Removed [-[NSATSTypesetter setUsesFontLeading:]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1533331-usesfontleading)Removed [-[NSATSTypesetter typesetterBehavior]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1533819-typesetterbehavior)Removed [-[NSATSTypesetter usesFontLeading]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1533331-usesfontleading)Added [NSATSTypesetter.attributedString](https://developer.apple.com/documentation/appkit/nsatstypesetter/1530598-attributedstring)Added [NSATSTypesetter.bidiProcessingEnabled](https://developer.apple.com/documentation/appkit/nsatstypesetter/1524295-bidiprocessingenabled)Added [NSATSTypesetter.currentTextContainer](https://developer.apple.com/documentation/appkit/nsatstypesetter/1527830-currenttextcontainer)Added [NSATSTypesetter.hyphenationFactor](https://developer.apple.com/documentation/appkit/nsatstypesetter/1526758-hyphenationfactor)Added [NSATSTypesetter.layoutManager](https://developer.apple.com/documentation/appkit/nsatstypesetter/1535366-layoutmanager)Added [NSATSTypesetter.lineFragmentPadding](https://developer.apple.com/documentation/appkit/nsatstypesetter/1532628-linefragmentpadding)Added [NSATSTypesetter.paragraphGlyphRange](https://developer.apple.com/documentation/appkit/nsatstypesetter/1528373-paragraphglyphrange)Added [NSATSTypesetter.paragraphSeparatorGlyphRange](https://developer.apple.com/documentation/appkit/nsatstypesetter/1531108-paragraphseparatorglyphrange)Added [NSATSTypesetter.typesetterBehavior](https://developer.apple.com/documentation/appkit/nsatstypesetter/1533819-typesetterbehavior)Added [NSATSTypesetter.usesFontLeading](https://developer.apple.com/documentation/appkit/nsatstypesetter/1533331-usesfontleading)Modified [+[NSATSTypesetter sharedTypesetter]](https://developer.apple.com/documentation/appkit/nsatstypesetter/1530993-shared)

|  | Declaration |
| --- | --- |
| From | ``` + (id)sharedTypesetter ``` |
| To | ``` + (NSATSTypesetter *)sharedTypesetter ``` |

NSAccessibility.hRemoved [-[NSObject accessibilityFocusedUIElement]](https://developer.apple.com/documentation/objectivec/nsobject/1526100-accessibilityfocuseduielement)Removed [-[NSObject accessibilityNotifiesWhenDestroyed]](https://developer.apple.com/documentation/objectivec/nsobject/1534050-accessibilitynotifieswhendestroy)Added [NSObject.accessibilityFocusedUIElement](https://developer.apple.com/documentation/objectivec/nsobject/1526100-accessibilityfocuseduielement)Added [NSObject.accessibilityNotifiesWhenDestroyed](https://developer.apple.com/documentation/objectivec/nsobject/1534050-accessibilitynotifieswhendestroy)Added [NSWorkspace.accessibilityDisplayShouldDifferentiateWithoutColor](https://developer.apple.com/documentation/appkit/nsworkspace/1524656-accessibilitydisplayshoulddiffer)Added [NSWorkspace.accessibilityDisplayShouldIncreaseContrast](https://developer.apple.com/documentation/appkit/nsworkspace/1526290-accessibilitydisplayshouldincrea)Added [NSWorkspace.accessibilityDisplayShouldReduceTransparency](https://developer.apple.com/documentation/appkit/nsworkspace/1533006-accessibilitydisplayshouldreduce)Added [NSAccessibilityFrameInView()](https://developer.apple.com/documentation/appkit/1528628-nsaccessibilityframeinview)Added [NSAccessibilityPointInView()](https://developer.apple.com/documentation/appkit/1534336-nsaccessibilitypointinview)Added NSWorkspace(NSWorkspaceAccessibilityDisplay)Added [NSWorkspaceAccessibilityDisplayOptionsDidChangeNotification](https://developer.apple.com/documentation/appkit/nsworkspace/1534227-accessibilitydisplayoptionsdidch)Modified [-[NSObject accessibilityActionDescription:]](https://developer.apple.com/documentation/objectivec/nsobject/1533500-accessibilityactiondescription)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.1 | OS X 10.10 |

Modified [-[NSObject accessibilityActionNames]](https://developer.apple.com/documentation/objectivec/nsobject/1527905-accessibilityactionnames)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.1 | OS X 10.10 |

Modified [-[NSObject accessibilityAttributeNames]](https://developer.apple.com/documentation/objectivec/nsobject/1525181-accessibilityattributenames)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.1 | OS X 10.10 |

Modified [-[NSObject accessibilityAttributeValue:]](https://developer.apple.com/documentation/objectivec/nsobject/1532465-accessibilityattributevalue)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.1 | OS X 10.10 |

Modified [-[NSObject accessibilityAttributeValue:forParameter:]](https://developer.apple.com/documentation/objectivec/nsobject/1524809-accessibilityattributevalue)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.1 | OS X 10.10 |

Modified [-[NSObject accessibilityIsAttributeSettable:]](https://developer.apple.com/documentation/objectivec/nsobject/1529207-accessibilityisattributesettable)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.1 | OS X 10.10 |

Modified [-[NSObject accessibilityIsIgnored]](https://developer.apple.com/documentation/objectivec/nsobject/1526439-accessibilityisignored)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.1 | OS X 10.10 |

Modified [-[NSObject accessibilityParameterizedAttributeNames]](https://developer.apple.com/documentation/objectivec/nsobject/1525455-accessibilityparameterizedattrib)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.1 | OS X 10.10 |

Modified [-[NSObject accessibilityPerformAction:]](https://developer.apple.com/documentation/objectivec/nsobject/1533528-accessibilityperformaction)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.1 | OS X 10.10 |

Modified [-[NSObject accessibilitySetOverrideValue:forAttribute:]](https://developer.apple.com/documentation/objectivec/nsobject/1535843-accessibilitysetoverridevalue)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.4 | -- |
| To | OS X 10.1 | OS X 10.10 |

Modified [-[NSObject accessibilitySetValue:forAttribute:]](https://developer.apple.com/documentation/objectivec/nsobject/1528477-accessibilitysetvalue)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.1 | OS X 10.10 |

NSAccessibilityConstants.h (Added)Added [NSAccessibilityActivationPointAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityactivationpointattribute)Added [NSAccessibilityAlternateUIVisibleAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityalternateuivisibleattribute)Added [NSAccessibilityOrientation](https://developer.apple.com/documentation/appkit/nsaccessibilityorientation)Added [NSAccessibilityOrientationHorizontal](https://developer.apple.com/documentation/appkit/nsaccessibilityorientation/horizontal)Added [NSAccessibilityOrientationUnknown](https://developer.apple.com/documentation/appkit/nsaccessibilityorientation/unknown)Added [NSAccessibilityOrientationVertical](https://developer.apple.com/documentation/appkit/nsaccessibilityorientation/nsaccessibilityorientationvertical)Added [NSAccessibilityRulerMarkerType](https://developer.apple.com/documentation/appkit/nsaccessibilityrulermarkertype)Added [NSAccessibilityRulerMarkerTypeIndentFirstLine](https://developer.apple.com/documentation/appkit/nsaccessibilityrulermarkertype/indentfirstline)Added [NSAccessibilityRulerMarkerTypeIndentHead](https://developer.apple.com/documentation/appkit/nsaccessibilityrulermarkertype/nsaccessibilityrulermarkertypeindenthead)Added [NSAccessibilityRulerMarkerTypeIndentTail](https://developer.apple.com/documentation/appkit/nsaccessibilityrulermarkertype/nsaccessibilityrulermarkertypeindenttail)Added [NSAccessibilityRulerMarkerTypeTabStopCenter](https://developer.apple.com/documentation/appkit/nsaccessibilityrulermarkertype/tabstopcenter)Added [NSAccessibilityRulerMarkerTypeTabStopDecimal](https://developer.apple.com/documentation/appkit/nsaccessibilityrulermarkertype/tabstopdecimal)Added [NSAccessibilityRulerMarkerTypeTabStopLeft](https://developer.apple.com/documentation/appkit/nsaccessibilityrulermarkertype/nsaccessibilityrulermarkertypetabstopleft)Added [NSAccessibilityRulerMarkerTypeTabStopRight](https://developer.apple.com/documentation/appkit/nsaccessibilityrulermarkertype/nsaccessibilityrulermarkertypetabstopright)Added [NSAccessibilityRulerMarkerTypeUnknown](https://developer.apple.com/documentation/appkit/nsaccessibilityrulermarkertype/nsaccessibilityrulermarkertypeunknown)Added [NSAccessibilitySharedFocusElementsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitysharedfocuselementsattribute)Added [NSAccessibilitySortDirection](https://developer.apple.com/documentation/appkit/nsaccessibilitysortdirection)Added [NSAccessibilitySortDirectionAscending](https://developer.apple.com/documentation/appkit/nsaccessibilitysortdirection/ascending)Added [NSAccessibilitySortDirectionDescending](https://developer.apple.com/documentation/appkit/nsaccessibilitysortdirection/descending)Added [NSAccessibilitySortDirectionUnknown](https://developer.apple.com/documentation/appkit/nsaccessibilitysortdirection/nsaccessibilitysortdirectionunknown)Added [NSAccessibilityUnits](https://developer.apple.com/documentation/appkit/nsaccessibilityunits)Added [NSAccessibilityUnitsCentimeters](https://developer.apple.com/documentation/appkit/nsaccessibilityunits/centimeters)Added [NSAccessibilityUnitsInches](https://developer.apple.com/documentation/appkit/nsaccessibilityunits/inches)Added [NSAccessibilityUnitsPicas](https://developer.apple.com/documentation/appkit/nsaccessibilityunits/nsaccessibilityunitspicas)Added [NSAccessibilityUnitsPoints](https://developer.apple.com/documentation/appkit/nsaccessibilityunits/nsaccessibilityunitspoints)Added [NSAccessibilityUnitsUnknown](https://developer.apple.com/documentation/appkit/nsaccessibilityunits/unknown)Modified [NSAccessibilityAllowedValuesAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1535521-allowedvalues)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityAnnouncementKey](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationuserinfokey/1528310-announcement)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityAnnouncementRequestedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1530633-announcementrequested)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityApplicationActivatedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1527225-applicationactivated)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityApplicationDeactivatedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1535292-applicationdeactivated)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityApplicationHiddenNotification](https://developer.apple.com/documentation/appkit/nsaccessibilityapplicationhiddennotification)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityApplicationRole](https://developer.apple.com/documentation/appkit/nsaccessibilityapplicationrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityApplicationShownNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1527720-applicationshown)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityAscendingSortDirectionValue](https://developer.apple.com/documentation/appkit/nsaccessibilitysortdirectionvalue/1529212-ascending)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityAttachmentTextAttribute](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1528504-accessibilityattachment)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityAttributedStringForRangeParameterizedAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityparameterizedattributename/1531181-attributedstringforrange)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityAutocorrectedTextAttribute](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1529894-accessibilityautocorrected)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityBackgroundColorTextAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitybackgroundcolortextattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityBoundsForRangeParameterizedAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityboundsforrangeparameterizedattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityBrowserRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1526035-browser)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityBusyIndicatorRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1525957-busyindicator)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityButtonRole](https://developer.apple.com/documentation/appkit/nsaccessibilitybuttonrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityCancelAction](https://developer.apple.com/documentation/appkit/nsaccessibilitycancelaction)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityCancelButtonAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitycancelbuttonattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityCellForColumnAndRowParameterizedAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityparameterizedattributename/1530333-cellforcolumnandrow)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityCellRole](https://developer.apple.com/documentation/appkit/nsaccessibilitycellrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityCenterTabStopMarkerTypeValue](https://developer.apple.com/documentation/appkit/nsaccessibilityrulermarkertypevalue/1529836-centertabstop)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityCentimetersUnitValue](https://developer.apple.com/documentation/appkit/nsaccessibilitycentimetersunitvalue)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityCheckBoxRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1525866-checkbox)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityChildrenAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1532027-children)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityClearButtonAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1529218-clearbutton)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityCloseButtonAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityclosebuttonattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityCloseButtonSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilityclosebuttonsubrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityColorWellRole](https://developer.apple.com/documentation/appkit/nsaccessibilitycolorwellrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityColumnCountAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1525168-columncount)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityColumnHeaderUIElementsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1529208-columnheaderuielements)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityColumnIndexRangeAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitycolumnindexrangeattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityColumnRole](https://developer.apple.com/documentation/appkit/nsaccessibilitycolumnrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityColumnTitlesAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitycolumntitlesattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityColumnsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitycolumnsattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityComboBoxRole](https://developer.apple.com/documentation/appkit/nsaccessibilitycomboboxrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityConfirmAction](https://developer.apple.com/documentation/appkit/nsaccessibilityactionname/1526234-confirm)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityContainsProtectedContentAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitycontainsprotectedcontentattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityContentListSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysubrole/1525223-contentlist)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityContentsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1526036-contents)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityCreatedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1527609-created)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityCriticalValueAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1535723-criticalvalue)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityDecimalTabStopMarkerTypeValue](https://developer.apple.com/documentation/appkit/nsaccessibilitydecimaltabstopmarkertypevalue)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityDecrementAction](https://developer.apple.com/documentation/appkit/nsaccessibilitydecrementaction)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityDecrementArrowSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitydecrementarrowsubrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityDecrementButtonAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitydecrementbuttonattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityDecrementPageSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysubrole/1533536-decrementpage)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityDefaultButtonAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1527426-defaultbutton)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityDefinitionListSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysubrole/1533657-definitionlist)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityDeleteAction](https://developer.apple.com/documentation/appkit/nsaccessibilityactionname/1532450-delete)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityDescendingSortDirectionValue](https://developer.apple.com/documentation/appkit/nsaccessibilitydescendingsortdirectionvalue)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityDescriptionAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitydescriptionattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityDescriptionListSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysubrole/1532769-descriptionlist)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityDialogSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitydialogsubrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityDisclosedByRowAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitydisclosedbyrowattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityDisclosedRowsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1534310-disclosedrows)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityDisclosingAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1529679-disclosing)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityDisclosureLevelAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitydisclosurelevelattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityDisclosureTriangleRole](https://developer.apple.com/documentation/appkit/nsaccessibilitydisclosuretrianglerole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityDocumentAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1530064-document)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityDrawerCreatedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitydrawercreatednotification)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityDrawerRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1527631-drawer)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityEditedAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityeditedattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityEnabledAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1530006-enabled)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityErrorCodeExceptionInfo](https://developer.apple.com/documentation/appkit/nsaccessibilityerrorcodeexceptioninfo)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityExpandedAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityexpandedattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityExtrasMenuBarAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityextrasmenubarattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityFilenameAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1528010-filename)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityFirstLineIndentMarkerTypeValue](https://developer.apple.com/documentation/appkit/nsaccessibilityrulermarkertypevalue/1535332-firstlineindent)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityFloatingWindowSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilityfloatingwindowsubrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityFocusedAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityfocusedattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityFocusedUIElementAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityfocuseduielementattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityFocusedUIElementChangedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilityfocuseduielementchangednotification)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityFocusedWindowAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1525174-focusedwindow)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityFocusedWindowChangedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilityfocusedwindowchangednotification)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityFontFamilyKey](https://developer.apple.com/documentation/appkit/nsaccessibilityfontfamilykey)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityFontNameKey](https://developer.apple.com/documentation/appkit/nsaccessibilityfontattributekey/1526304-fontname)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityFontSizeKey](https://developer.apple.com/documentation/appkit/nsaccessibilityfontattributekey/1531806-fontsize)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityFontTextAttribute](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1527142-accessibilityfont)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityForegroundColorTextAttribute](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1529308-accessibilityforegroundcolor)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityFrontmostAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityfrontmostattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityFullScreenButtonAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1533541-fullscreenbutton)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityFullScreenButtonSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysubrole/1533410-fullscreenbutton)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityGridRole](https://developer.apple.com/documentation/appkit/nsaccessibilitygridrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityGroupRole](https://developer.apple.com/documentation/appkit/nsaccessibilitygrouprole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityGrowAreaAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1535484-growarea)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityGrowAreaRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1533168-growarea)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityHandleRole](https://developer.apple.com/documentation/appkit/nsaccessibilityhandlerole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityHandlesAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1528324-handles)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityHeadIndentMarkerTypeValue](https://developer.apple.com/documentation/appkit/nsaccessibilityheadindentmarkertypevalue)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityHeaderAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityheaderattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityHelpAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1532280-help)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityHelpTagCreatedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1535267-helptagcreated)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityHelpTagRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1525059-helptag)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityHiddenAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1530103-hidden)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityHorizontalOrientationValue](https://developer.apple.com/documentation/appkit/nsaccessibilityhorizontalorientationvalue)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityHorizontalScrollBarAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityhorizontalscrollbarattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityHorizontalUnitDescriptionAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1535021-horizontalunitdescription)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityHorizontalUnitsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1526134-horizontalunits)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityIdentifierAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1528737-identifier)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityImageRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1531974-image)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityInchesUnitValue](https://developer.apple.com/documentation/appkit/nsaccessibilityinchesunitvalue)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityIncrementAction](https://developer.apple.com/documentation/appkit/nsaccessibilityincrementaction)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityIncrementArrowSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilityincrementarrowsubrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityIncrementButtonAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1528787-incrementbutton)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityIncrementPageSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilityincrementpagesubrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityIncrementorRole](https://developer.apple.com/documentation/appkit/nsaccessibilityincrementorrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityIndexAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1526021-index)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityInsertionPointLineNumberAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1531601-insertionpointlinenumber)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityLabelUIElementsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1526421-labeluielements)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityLabelValueAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1532419-labelvalue)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityLayoutAreaRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1524860-layoutarea)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityLayoutChangedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1524251-layoutchanged)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityLayoutItemRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1527759-layoutitem)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityLayoutPointForScreenPointParameterizedAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityparameterizedattributename/1532391-layoutpointforscreenpoint)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityLayoutSizeForScreenSizeParameterizedAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityparameterizedattributename/1534311-layoutsizeforscreensize)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityLeftTabStopMarkerTypeValue](https://developer.apple.com/documentation/appkit/nsaccessibilityrulermarkertypevalue/1525792-lefttabstop)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityLevelIndicatorRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1527049-levelindicator)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityLineForIndexParameterizedAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitylineforindexparameterizedattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityLinkRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1527747-link)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityLinkTextAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitylinktextattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityLinkedUIElementsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitylinkeduielementsattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityListRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1533621-list)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMainAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitymainattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMainWindowAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1534812-mainwindow)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMainWindowChangedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1535613-mainwindowchanged)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMarkedMisspelledTextAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitymarkedmisspelledtextattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMarkerGroupUIElementAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1527016-markergroupuielement)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMarkerTypeAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitymarkertypeattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMarkerTypeDescriptionAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitymarkertypedescriptionattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMarkerUIElementsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1535811-markeruielements)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMarkerValuesAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1528798-markervalues)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMatteContentUIElementAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitymattecontentuielementattribute)

|  | Introduction | Deprecation | Header |
| --- | --- | --- | --- |
| From | OS X 10.4 | -- | AppKit/NSAccessibility.h |
| To | OS X 10.1 | OS X 10.10 | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMatteHoleAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1529969-mattehole)

|  | Introduction | Deprecation | Header |
| --- | --- | --- | --- |
| From | OS X 10.4 | -- | AppKit/NSAccessibility.h |
| To | OS X 10.1 | OS X 10.10 | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMatteRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1530745-matte)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMaxValueAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1525668-maxvalue)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMenuBarAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1524617-menubar)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMenuBarRole](https://developer.apple.com/documentation/appkit/nsaccessibilitymenubarrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMenuButtonRole](https://developer.apple.com/documentation/appkit/nsaccessibilitymenubuttonrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMenuItemRole](https://developer.apple.com/documentation/appkit/nsaccessibilitymenuitemrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMenuRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1532502-menu)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMinValueAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1531652-minvalue)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMinimizeButtonAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityminimizebuttonattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMinimizeButtonSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilityminimizebuttonsubrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMinimizedAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1530900-minimized)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMisspelledTextAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitymisspelledtextattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityModalAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitymodalattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityMovedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitymovednotification)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityNextContentsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitynextcontentsattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityNumberOfCharactersAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitynumberofcharactersattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityOrderedByRowAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1532435-orderedbyrow)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityOrientationAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1535581-orientation)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityOutlineRole](https://developer.apple.com/documentation/appkit/nsaccessibilityoutlinerole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityOutlineRowSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysubrole/1534918-outlinerow)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityOverflowButtonAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityoverflowbuttonattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityParentAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1532582-parent)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityPicasUnitValue](https://developer.apple.com/documentation/appkit/nsaccessibilityrulerunitvalue/1527365-picas)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityPickAction](https://developer.apple.com/documentation/appkit/nsaccessibilitypickaction)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityPlaceholderValueAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1526634-placeholdervalue)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityPointsUnitValue](https://developer.apple.com/documentation/appkit/nsaccessibilityrulerunitvalue/1530225-points)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityPopUpButtonRole](https://developer.apple.com/documentation/appkit/nsaccessibilitypopupbuttonrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityPopoverRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1531574-popover)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityPositionAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitypositionattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityPostNotificationWithUserInfo()](https://developer.apple.com/documentation/appkit/1534572-nsaccessibilitypostnotificationw)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityPressAction](https://developer.apple.com/documentation/appkit/nsaccessibilitypressaction)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityPreviousContentsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitypreviouscontentsattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityPriorityHigh](https://developer.apple.com/documentation/appkit/nsaccessibilityprioritylevel/nsaccessibilitypriorityhigh)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityPriorityKey](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationuserinfokey/1531038-priority)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityPriorityLevel](https://developer.apple.com/documentation/appkit/nsaccessibilityprioritylevel)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityPriorityLow](https://developer.apple.com/documentation/appkit/nsaccessibilityprioritylevel/low)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityPriorityMedium](https://developer.apple.com/documentation/appkit/nsaccessibilityprioritylevel/nsaccessibilityprioritymedium)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityProgressIndicatorRole](https://developer.apple.com/documentation/appkit/nsaccessibilityprogressindicatorrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityProxyAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityproxyattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRTFForRangeParameterizedAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityparameterizedattributename/1534455-rtfforrange)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRadioButtonRole](https://developer.apple.com/documentation/appkit/nsaccessibilityradiobuttonrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRadioGroupRole](https://developer.apple.com/documentation/appkit/nsaccessibilityradiogrouprole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRaiseAction](https://developer.apple.com/documentation/appkit/nsaccessibilityactionname/1528706-raise)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRangeForIndexParameterizedAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityrangeforindexparameterizedattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRangeForLineParameterizedAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityrangeforlineparameterizedattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRangeForPositionParameterizedAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityrangeforpositionparameterizedattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRatingIndicatorSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilityratingindicatorsubrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRelevanceIndicatorRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrelevanceindicatorrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityResizedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilityresizednotification)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRightTabStopMarkerTypeValue](https://developer.apple.com/documentation/appkit/nsaccessibilityrulermarkertypevalue/1531334-righttabstop)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRoleAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1524581-role)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRoleDescriptionAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1530857-roledescription)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRowCollapsedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilityrowcollapsednotification)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRowCountAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1535915-rowcount)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRowCountChangedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilityrowcountchangednotification)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRowExpandedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1526130-rowexpanded)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRowHeaderUIElementsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityrowheaderuielementsattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRowIndexRangeAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1530121-rowindexrange)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRowRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrowrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRowsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityrowsattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRulerMarkerRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrulermarkerrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityRulerRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrulerrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityScreenPointForLayoutPointParameterizedAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityscreenpointforlayoutpointparameterizedattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityScreenSizeForLayoutSizeParameterizedAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityscreensizeforlayoutsizeparameterizedattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityScrollAreaRole](https://developer.apple.com/documentation/appkit/nsaccessibilityscrollarearole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityScrollBarRole](https://developer.apple.com/documentation/appkit/nsaccessibilityscrollbarrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySearchButtonAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1533975-searchbutton)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySearchFieldSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysubrole/1525735-searchfield)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySearchMenuAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitysearchmenuattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySecureTextFieldSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysecuretextfieldsubrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySelectedAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1529328-selected)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySelectedCellsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityselectedcellsattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySelectedCellsChangedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1531991-selectedcellschanged)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySelectedChildrenAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1529775-selectedchildren)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySelectedChildrenChangedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1531928-selectedchildrenchanged)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySelectedChildrenMovedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1525499-selectedchildrenmoved)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySelectedColumnsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1532921-selectedcolumns)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySelectedColumnsChangedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1535491-selectedcolumnschanged)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySelectedRowsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityselectedrowsattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySelectedRowsChangedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1525430-selectedrowschanged)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySelectedTextAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1528589-selectedtext)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySelectedTextChangedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1535460-selectedtextchanged)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySelectedTextRangeAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityselectedtextrangeattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySelectedTextRangesAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityselectedtextrangesattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityServesAsTitleForUIElementsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1528875-servesastitleforuielements)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityShadowTextAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityshadowtextattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySharedCharacterRangeAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1526642-sharedcharacterrange)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySharedTextUIElementsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitysharedtextuielementsattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySheetCreatedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitysheetcreatednotification)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySheetRole](https://developer.apple.com/documentation/appkit/nsaccessibilitysheetrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityShowAlternateUIAction](https://developer.apple.com/documentation/appkit/nsaccessibilityshowalternateuiaction)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityShowDefaultUIAction](https://developer.apple.com/documentation/appkit/nsaccessibilityactionname/1526573-showdefaultui)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityShowMenuAction](https://developer.apple.com/documentation/appkit/nsaccessibilityshowmenuaction)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityShownMenuAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityshownmenuattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySizeAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitysizeattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySliderRole](https://developer.apple.com/documentation/appkit/nsaccessibilitysliderrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySortButtonRole](https://developer.apple.com/documentation/appkit/nsaccessibilitysortbuttonrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySortButtonSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysortbuttonsubrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySortDirectionAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitysortdirectionattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySplitGroupRole](https://developer.apple.com/documentation/appkit/nsaccessibilitysplitgrouprole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySplitterRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1531028-splitter)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySplittersAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1535312-splitters)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityStandardWindowSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitystandardwindowsubrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityStaticTextRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1534498-statictext)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityStrikethroughColorTextAttribute](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1533801-accessibilitystrikethroughcolor)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityStrikethroughTextAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitystrikethroughtextattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityStringForRangeParameterizedAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitystringforrangeparameterizedattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityStyleRangeForIndexParameterizedAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitystylerangeforindexparameterizedattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySubroleAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitysubroleattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySuperscriptTextAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitysuperscripttextattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySwitchSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilityswitchsubrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySystemDialogSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysubrole/1534169-systemdialog)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySystemFloatingWindowSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysystemfloatingwindowsubrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilitySystemWideRole](https://developer.apple.com/documentation/appkit/nsaccessibilitysystemwiderole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityTabGroupRole](https://developer.apple.com/documentation/appkit/nsaccessibilitytabgrouprole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityTableRole](https://developer.apple.com/documentation/appkit/nsaccessibilitytablerole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityTableRowSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysubrole/1528102-tablerow)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityTabsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1531592-tabs)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityTailIndentMarkerTypeValue](https://developer.apple.com/documentation/appkit/nsaccessibilitytailindentmarkertypevalue)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityTextAreaRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1533503-textarea)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityTextAttachmentSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysubrole/1535563-textattachment)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityTextFieldRole](https://developer.apple.com/documentation/appkit/nsaccessibilitytextfieldrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityTextLinkSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysubrole/1524548-textlink)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityTimelineSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitytimelinesubrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityTitleAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitytitleattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityTitleChangedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1534878-titlechanged)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityTitleUIElementAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitytitleuielementattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityToggleSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysubrole/1525391-toggle)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityToolbarButtonAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1529714-toolbarbutton)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityToolbarButtonSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysubrole/1528164-toolbarbutton)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityToolbarRole](https://developer.apple.com/documentation/appkit/nsaccessibilitytoolbarrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityTopLevelUIElementAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitytopleveluielementattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityUIElementDestroyedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1530862-uielementdestroyed)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityUIElementsKey](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationuserinfokey/1534944-uielements)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityURLAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1526857-url)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityUnderlineColorTextAttribute](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1531758-accessibilityunderlinecolor)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityUnderlineTextAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityunderlinetextattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityUnitDescriptionAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1535556-unitdescription)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityUnitsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityunitsattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityUnitsChangedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1524318-unitschanged)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityUnknownMarkerTypeValue](https://developer.apple.com/documentation/appkit/nsaccessibilityrulermarkertypevalue/1534709-unknown)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityUnknownOrientationValue](https://developer.apple.com/documentation/appkit/nsaccessibilityunknownorientationvalue)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityUnknownRole](https://developer.apple.com/documentation/appkit/nsaccessibilityrole/1529224-unknown)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityUnknownSortDirectionValue](https://developer.apple.com/documentation/appkit/nsaccessibilityunknownsortdirectionvalue)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityUnknownSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysubrole/1529404-unknown)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityUnknownUnitValue](https://developer.apple.com/documentation/appkit/nsaccessibilityrulerunitvalue/1528322-unknown)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityValueAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1525310-value)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityValueChangedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilityvaluechangednotification)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityValueDescriptionAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1529313-valuedescription)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityValueIndicatorRole](https://developer.apple.com/documentation/appkit/nsaccessibilityvalueindicatorrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityVerticalOrientationValue](https://developer.apple.com/documentation/appkit/nsaccessibilityorientationvalue/1534621-vertical)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityVerticalScrollBarAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityverticalscrollbarattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityVerticalUnitDescriptionAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1535062-verticalunitdescription)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityVerticalUnitsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1525427-verticalunits)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityVisibleCellsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1531171-visiblecells)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityVisibleCharacterRangeAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1524527-visiblecharacterrange)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityVisibleChildrenAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1535777-visiblechildren)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityVisibleColumnsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityvisiblecolumnsattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityVisibleNameKey](https://developer.apple.com/documentation/appkit/nsaccessibilityvisiblenamekey)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityVisibleRowsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1524643-visiblerows)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityWarningValueAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitywarningvalueattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityWindowAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitywindowattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityWindowCreatedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitywindowcreatednotification)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityWindowDeminiaturizedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1526464-windowdeminiaturized)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityWindowMiniaturizedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitywindowminiaturizednotification)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityWindowMovedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitywindowmovednotification)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityWindowResizedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilitynotificationname/1535476-windowresized)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityWindowRole](https://developer.apple.com/documentation/appkit/nsaccessibilitywindowrole)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityWindowsAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilitywindowsattribute)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityZoomButtonAttribute](https://developer.apple.com/documentation/appkit/nsaccessibilityattributename/1528873-zoombutton)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

Modified [NSAccessibilityZoomButtonSubrole](https://developer.apple.com/documentation/appkit/nsaccessibilitysubrole/1530400-zoombutton)

|  | Header |
| --- | --- |
| From | AppKit/NSAccessibility.h |
| To | AppKit/NSAccessibilityConstants.h |

NSAccessibilityElement.h (Added)Added [NSAccessibilityElement](https://developer.apple.com/documentation/appkit/nsaccessibilityelement)Added [-[NSAccessibilityElement accessibilityAddChildElement:]](https://developer.apple.com/documentation/appkit/nsaccessibilityelement/1533717-accessibilityaddchildelement)Added [+[NSAccessibilityElement accessibilityElementWithRole:frame:label:parent:]](https://developer.apple.com/documentation/appkit/nsaccessibilityelement/1531178-element)Added [NSAccessibilityElement.accessibilityFrameInParentSpace](https://developer.apple.com/documentation/appkit/nsaccessibilityelement/1569648-accessibilityframeinparentspace)NSAccessibilityProtocols.h (Added)Added [NSAccessibility](https://developer.apple.com/documentation/appkit/nsaccessibility)Added [NSAccessibility.accessibilityActivationPoint](https://developer.apple.com/documentation/appkit/nsaccessibility/1535149-accessibilityactivationpoint)Added [NSAccessibility.accessibilityAllowedValues](https://developer.apple.com/documentation/appkit/nsaccessibility/1534941-accessibilityallowedvalues)Added [NSAccessibility.accessibilityAlternateUIVisible](https://developer.apple.com/documentation/appkit/nsaccessibility/1535035-accessibilityalternateuivisible)Added [NSAccessibility.accessibilityApplicationFocusedUIElement](https://developer.apple.com/documentation/appkit/nsaccessibility/1535139-accessibilityapplicationfocusedu)Added [-[NSAccessibility accessibilityAttributedStringForRange:]](https://developer.apple.com/documentation/appkit/nsaccessibility/1532250-accessibilityattributedstring)Added [NSAccessibility.accessibilityCancelButton](https://developer.apple.com/documentation/appkit/nsaccessibility/1535060-accessibilitycancelbutton)Added [-[NSAccessibility accessibilityCellForColumn:row:]](https://developer.apple.com/documentation/appkit/nsaccessibility/1532709-accessibilitycellforcolumn)Added [NSAccessibility.accessibilityChildren](https://developer.apple.com/documentation/appkit/nsaccessibility/1535018-accessibilitychildren)Added [NSAccessibility.accessibilityClearButton](https://developer.apple.com/documentation/appkit/nsaccessibility/1534949-accessibilityclearbutton)Added [NSAccessibility.accessibilityCloseButton](https://developer.apple.com/documentation/appkit/nsaccessibility/1535022-accessibilityclosebutton)Added [NSAccessibility.accessibilityColumnCount](https://developer.apple.com/documentation/appkit/nsaccessibility/1534966-accessibilitycolumncount)Added [NSAccessibility.accessibilityColumnHeaderUIElements](https://developer.apple.com/documentation/appkit/nsaccessibility/1534988-accessibilitycolumnheaderuieleme)Added [NSAccessibility.accessibilityColumnIndexRange](https://developer.apple.com/documentation/appkit/nsaccessibility/1534979-accessibilitycolumnindexrange)Added [NSAccessibility.accessibilityColumnTitles](https://developer.apple.com/documentation/appkit/nsaccessibility/1535148-accessibilitycolumntitles)Added [NSAccessibility.accessibilityColumns](https://developer.apple.com/documentation/appkit/nsaccessibility/1535115-accessibilitycolumns)Added [NSAccessibility.accessibilityContents](https://developer.apple.com/documentation/appkit/nsaccessibility/1535026-accessibilitycontents)Added [NSAccessibility.accessibilityCriticalValue](https://developer.apple.com/documentation/appkit/nsaccessibility/1534973-accessibilitycriticalvalue)Added [NSAccessibility.accessibilityDecrementButton](https://developer.apple.com/documentation/appkit/nsaccessibility/1535097-accessibilitydecrementbutton)Added [NSAccessibility.accessibilityDefaultButton](https://developer.apple.com/documentation/appkit/nsaccessibility/1534957-accessibilitydefaultbutton)Added [NSAccessibility.accessibilityDisclosed](https://developer.apple.com/documentation/appkit/nsaccessibility/1535124-accessibilitydisclosed)Added [NSAccessibility.accessibilityDisclosedByRow](https://developer.apple.com/documentation/appkit/nsaccessibility/1535146-accessibilitydisclosedbyrow)Added [NSAccessibility.accessibilityDisclosedRows](https://developer.apple.com/documentation/appkit/nsaccessibility/1535008-accessibilitydisclosedrows)Added [NSAccessibility.accessibilityDisclosureLevel](https://developer.apple.com/documentation/appkit/nsaccessibility/1535111-accessibilitydisclosurelevel)Added [NSAccessibility.accessibilityDocument](https://developer.apple.com/documentation/appkit/nsaccessibility/1534993-accessibilitydocument)Added [NSAccessibility.accessibilityEdited](https://developer.apple.com/documentation/appkit/nsaccessibility/1535077-accessibilityedited)Added [NSAccessibility.accessibilityElement](https://developer.apple.com/documentation/appkit/nsaccessibility/1535002-accessibilityelement)Added [NSAccessibility.accessibilityEnabled](https://developer.apple.com/documentation/appkit/nsaccessibility/1535024-accessibilityenabled)Added [NSAccessibility.accessibilityExpanded](https://developer.apple.com/documentation/appkit/nsaccessibility/1535045-accessibilityexpanded)Added [NSAccessibility.accessibilityExtrasMenuBar](https://developer.apple.com/documentation/appkit/nsaccessibility/1534996-accessibilityextrasmenubar)Added [NSAccessibility.accessibilityFilename](https://developer.apple.com/documentation/appkit/nsaccessibility/1535068-accessibilityfilename)Added [NSAccessibility.accessibilityFocused](https://developer.apple.com/documentation/appkit/nsaccessibility/1534994-accessibilityfocused)Added [NSAccessibility.accessibilityFocusedWindow](https://developer.apple.com/documentation/appkit/nsaccessibility/1534986-accessibilityfocusedwindow)Added [NSAccessibility.accessibilityFrame](https://developer.apple.com/documentation/appkit/nsaccessibility/1534939-accessibilityframe)Added [-[NSAccessibility accessibilityFrameForRange:]](https://developer.apple.com/documentation/appkit/nsaccessibility/1526088-accessibilityframeforrange)Added [NSAccessibility.accessibilityFrontmost](https://developer.apple.com/documentation/appkit/nsaccessibility/1535073-accessibilityfrontmost)Added [NSAccessibility.accessibilityFullScreenButton](https://developer.apple.com/documentation/appkit/nsaccessibility/1534999-accessibilityfullscreenbutton)Added [NSAccessibility.accessibilityGrowArea](https://developer.apple.com/documentation/appkit/nsaccessibility/1535074-accessibilitygrowarea)Added [NSAccessibility.accessibilityHandles](https://developer.apple.com/documentation/appkit/nsaccessibility/1535085-accessibilityhandles)Added [NSAccessibility.accessibilityHeader](https://developer.apple.com/documentation/appkit/nsaccessibility/1534938-accessibilityheader)Added [NSAccessibility.accessibilityHelp](https://developer.apple.com/documentation/appkit/nsaccessibility/1534974-accessibilityhelp)Added [NSAccessibility.accessibilityHidden](https://developer.apple.com/documentation/appkit/nsaccessibility/1534961-accessibilityhidden)Added [NSAccessibility.accessibilityHorizontalScrollBar](https://developer.apple.com/documentation/appkit/nsaccessibility/1534942-accessibilityhorizontalscrollbar)Added [NSAccessibility.accessibilityHorizontalUnitDescription](https://developer.apple.com/documentation/appkit/nsaccessibility/1535095-accessibilityhorizontalunitdescr)Added [NSAccessibility.accessibilityHorizontalUnits](https://developer.apple.com/documentation/appkit/nsaccessibility/1535154-accessibilityhorizontalunits)Added [NSAccessibility.accessibilityIdentifier](https://developer.apple.com/documentation/appkit/nsaccessibility/1535023-accessibilityidentifier)Added [NSAccessibility.accessibilityIncrementButton](https://developer.apple.com/documentation/appkit/nsaccessibility/1535007-accessibilityincrementbutton)Added [NSAccessibility.accessibilityIndex](https://developer.apple.com/documentation/appkit/nsaccessibility/1535067-accessibilityindex)Added [NSAccessibility.accessibilityInsertionPointLineNumber](https://developer.apple.com/documentation/appkit/nsaccessibility/1535050-accessibilityinsertionpointlinen)Added [NSAccessibility.accessibilityLabel](https://developer.apple.com/documentation/appkit/nsaccessibility/1534976-accessibilitylabel)Added [NSAccessibility.accessibilityLabelUIElements](https://developer.apple.com/documentation/appkit/nsaccessibility/1534954-accessibilitylabeluielements)Added [NSAccessibility.accessibilityLabelValue](https://developer.apple.com/documentation/appkit/nsaccessibility/1535108-accessibilitylabelvalue)Added [-[NSAccessibility accessibilityLayoutPointForScreenPoint:]](https://developer.apple.com/documentation/appkit/nsaccessibility/1526401-accessibilitylayoutpoint)Added [-[NSAccessibility accessibilityLayoutSizeForScreenSize:]](https://developer.apple.com/documentation/appkit/nsaccessibility/1535016-accessibilitylayoutsizeforscreen)Added [-[NSAccessibility accessibilityLineForIndex:]](https://developer.apple.com/documentation/appkit/nsaccessibility/1525305-accessibilityline)Added [NSAccessibility.accessibilityLinkedUIElements](https://developer.apple.com/documentation/appkit/nsaccessibility/1534972-accessibilitylinkeduielements)Added [NSAccessibility.accessibilityMain](https://developer.apple.com/documentation/appkit/nsaccessibility/1534936-accessibilitymain)Added [NSAccessibility.accessibilityMainWindow](https://developer.apple.com/documentation/appkit/nsaccessibility/1535138-accessibilitymainwindow)Added [NSAccessibility.accessibilityMarkerGroupUIElement](https://developer.apple.com/documentation/appkit/nsaccessibility/1535081-accessibilitymarkergroupuielemen)Added [NSAccessibility.accessibilityMarkerTypeDescription](https://developer.apple.com/documentation/appkit/nsaccessibility/1534968-accessibilitymarkertypedescripti)Added [NSAccessibility.accessibilityMarkerUIElements](https://developer.apple.com/documentation/appkit/nsaccessibility/1535037-accessibilitymarkeruielements)Added [NSAccessibility.accessibilityMarkerValues](https://developer.apple.com/documentation/appkit/nsaccessibility/1535076-accessibilitymarkervalues)Added [NSAccessibility.accessibilityMaxValue](https://developer.apple.com/documentation/appkit/nsaccessibility/1535078-accessibilitymaxvalue)Added [NSAccessibility.accessibilityMenuBar](https://developer.apple.com/documentation/appkit/nsaccessibility/1535055-accessibilitymenubar)Added [NSAccessibility.accessibilityMinValue](https://developer.apple.com/documentation/appkit/nsaccessibility/1534995-accessibilityminvalue)Added [NSAccessibility.accessibilityMinimizeButton](https://developer.apple.com/documentation/appkit/nsaccessibility/1535052-accessibilityminimizebutton)Added [NSAccessibility.accessibilityMinimized](https://developer.apple.com/documentation/appkit/nsaccessibility/1535028-accessibilityminimized)Added [NSAccessibility.accessibilityModal](https://developer.apple.com/documentation/appkit/nsaccessibility/1535140-accessibilitymodal)Added [NSAccessibility.accessibilityNextContents](https://developer.apple.com/documentation/appkit/nsaccessibility/1535034-accessibilitynextcontents)Added [NSAccessibility.accessibilityNumberOfCharacters](https://developer.apple.com/documentation/appkit/nsaccessibility/1534982-accessibilitynumberofcharacters)Added [NSAccessibility.accessibilityOrderedByRow](https://developer.apple.com/documentation/appkit/nsaccessibility/1535061-accessibilityorderedbyrow)Added [NSAccessibility.accessibilityOrientation](https://developer.apple.com/documentation/appkit/nsaccessibility/1535106-accessibilityorientation)Added [NSAccessibility.accessibilityOverflowButton](https://developer.apple.com/documentation/appkit/nsaccessibility/1534943-accessibilityoverflowbutton)Added [NSAccessibility.accessibilityParent](https://developer.apple.com/documentation/appkit/nsaccessibility/1535040-accessibilityparent)Added [-[NSAccessibility accessibilityPerformCancel]](https://developer.apple.com/documentation/appkit/nsaccessibility/1528679-accessibilityperformcancel)Added [-[NSAccessibility accessibilityPerformConfirm]](https://developer.apple.com/documentation/appkit/nsaccessibility/1534952-accessibilityperformconfirm)Added [-[NSAccessibility accessibilityPerformDecrement]](https://developer.apple.com/documentation/appkit/nsaccessibility/1526626-accessibilityperformdecrement)Added [-[NSAccessibility accessibilityPerformDelete]](https://developer.apple.com/documentation/appkit/nsaccessibility/1524609-accessibilityperformdelete)Added [-[NSAccessibility accessibilityPerformIncrement]](https://developer.apple.com/documentation/appkit/nsaccessibility/1525705-accessibilityperformincrement)Added [-[NSAccessibility accessibilityPerformPick]](https://developer.apple.com/documentation/appkit/nsaccessibility/1535130-accessibilityperformpick)Added [-[NSAccessibility accessibilityPerformPress]](https://developer.apple.com/documentation/appkit/nsaccessibility/1526358-accessibilityperformpress)Added [-[NSAccessibility accessibilityPerformRaise]](https://developer.apple.com/documentation/appkit/nsaccessibility/1530545-accessibilityperformraise)Added [-[NSAccessibility accessibilityPerformShowAlternateUI]](https://developer.apple.com/documentation/appkit/nsaccessibility/1533983-accessibilityperformshowalternat)Added [-[NSAccessibility accessibilityPerformShowDefaultUI]](https://developer.apple.com/documentation/appkit/nsaccessibility/1531207-accessibilityperformshowdefaultu)Added [-[NSAccessibility accessibilityPerformShowMenu]](https://developer.apple.com/documentation/appkit/nsaccessibility/1532774-accessibilityperformshowmenu)Added [NSAccessibility.accessibilityPlaceholderValue](https://developer.apple.com/documentation/appkit/nsaccessibility/1535063-accessibilityplaceholdervalue)Added [NSAccessibility.accessibilityPreviousContents](https://developer.apple.com/documentation/appkit/nsaccessibility/1534950-accessibilitypreviouscontents)Added [NSAccessibility.accessibilityProtectedContent](https://developer.apple.com/documentation/appkit/nsaccessibility/1535083-accessibilityprotectedcontent)Added [NSAccessibility.accessibilityProxy](https://developer.apple.com/documentation/appkit/nsaccessibility/1535143-accessibilityproxy)Added [-[NSAccessibility accessibilityRTFForRange:]](https://developer.apple.com/documentation/appkit/nsaccessibility/1529273-accessibilityrtf)Added [-[NSAccessibility accessibilityRangeForIndex:]](https://developer.apple.com/documentation/appkit/nsaccessibility/1525329-accessibilityrange)Added [-[NSAccessibility accessibilityRangeForLine:]](https://developer.apple.com/documentation/appkit/nsaccessibility/1528813-accessibilityrangeforline)Added [-[NSAccessibility accessibilityRangeForPosition:]](https://developer.apple.com/documentation/appkit/nsaccessibility/1531615-accessibilityrangeforposition)Added [NSAccessibility.accessibilityRole](https://developer.apple.com/documentation/appkit/nsaccessibility/1535005-accessibilityrole)Added [NSAccessibility.accessibilityRoleDescription](https://developer.apple.com/documentation/appkit/nsaccessibility/1535144-accessibilityroledescription)Added [NSAccessibility.accessibilityRowCount](https://developer.apple.com/documentation/appkit/nsaccessibility/1535013-accessibilityrowcount)Added [NSAccessibility.accessibilityRowHeaderUIElements](https://developer.apple.com/documentation/appkit/nsaccessibility/1535014-accessibilityrowheaderuielements)Added [NSAccessibility.accessibilityRowIndexRange](https://developer.apple.com/documentation/appkit/nsaccessibility/1535153-accessibilityrowindexrange)Added [NSAccessibility.accessibilityRows](https://developer.apple.com/documentation/appkit/nsaccessibility/1534945-accessibilityrows)Added [NSAccessibility.accessibilityRulerMarkerType](https://developer.apple.com/documentation/appkit/nsaccessibility/1535099-accessibilityrulermarkertype)Added [-[NSAccessibility accessibilityScreenPointForLayoutPoint:]](https://developer.apple.com/documentation/appkit/nsaccessibility/1524668-accessibilityscreenpoint)Added [-[NSAccessibility accessibilityScreenSizeForLayoutSize:]](https://developer.apple.com/documentation/appkit/nsaccessibility/1526114-accessibilityscreensizeforlayout)Added [NSAccessibility.accessibilitySearchButton](https://developer.apple.com/documentation/appkit/nsaccessibility/1535105-accessibilitysearchbutton)Added [NSAccessibility.accessibilitySearchMenu](https://developer.apple.com/documentation/appkit/nsaccessibility/1535015-accessibilitysearchmenu)Added [NSAccessibility.accessibilitySelected](https://developer.apple.com/documentation/appkit/nsaccessibility/1534981-accessibilityselected)Added [NSAccessibility.accessibilitySelectedCells](https://developer.apple.com/documentation/appkit/nsaccessibility/1535101-accessibilityselectedcells)Added [NSAccessibility.accessibilitySelectedChildren](https://developer.apple.com/documentation/appkit/nsaccessibility/1534970-accessibilityselectedchildren)Added [NSAccessibility.accessibilitySelectedColumns](https://developer.apple.com/documentation/appkit/nsaccessibility/1534978-accessibilityselectedcolumns)Added [NSAccessibility.accessibilitySelectedRows](https://developer.apple.com/documentation/appkit/nsaccessibility/1535125-accessibilityselectedrows)Added [NSAccessibility.accessibilitySelectedText](https://developer.apple.com/documentation/appkit/nsaccessibility/1535038-accessibilityselectedtext)Added [NSAccessibility.accessibilitySelectedTextRange](https://developer.apple.com/documentation/appkit/nsaccessibility/1534989-accessibilityselectedtextrange)Added [NSAccessibility.accessibilitySelectedTextRanges](https://developer.apple.com/documentation/appkit/nsaccessibility/1535133-accessibilityselectedtextranges)Added [NSAccessibility.accessibilityServesAsTitleForUIElements](https://developer.apple.com/documentation/appkit/nsaccessibility/1535122-accessibilityservesastitleforuie)Added [NSAccessibility.accessibilitySharedCharacterRange](https://developer.apple.com/documentation/appkit/nsaccessibility/1535069-accessibilitysharedcharacterrang)Added [NSAccessibility.accessibilitySharedFocusElements](https://developer.apple.com/documentation/appkit/nsaccessibility/1534990-accessibilitysharedfocuselements)Added [NSAccessibility.accessibilitySharedTextUIElements](https://developer.apple.com/documentation/appkit/nsaccessibility/1534991-accessibilitysharedtextuielement)Added [NSAccessibility.accessibilityShownMenu](https://developer.apple.com/documentation/appkit/nsaccessibility/1534983-accessibilityshownmenu)Added [NSAccessibility.accessibilitySortDirection](https://developer.apple.com/documentation/appkit/nsaccessibility/1534962-accessibilitysortdirection)Added [NSAccessibility.accessibilitySplitters](https://developer.apple.com/documentation/appkit/nsaccessibility/1535088-accessibilitysplitters)Added [-[NSAccessibility accessibilityStringForRange:]](https://developer.apple.com/documentation/appkit/nsaccessibility/1534940-accessibilitystring)Added [-[NSAccessibility accessibilityStyleRangeForIndex:]](https://developer.apple.com/documentation/appkit/nsaccessibility/1530474-accessibilitystylerangeforindex)Added [NSAccessibility.accessibilitySubrole](https://developer.apple.com/documentation/appkit/nsaccessibility/1535070-accessibilitysubrole)Added [NSAccessibility.accessibilityTabs](https://developer.apple.com/documentation/appkit/nsaccessibility/1535044-accessibilitytabs)Added [NSAccessibility.accessibilityTitle](https://developer.apple.com/documentation/appkit/nsaccessibility/1535033-accessibilitytitle)Added [NSAccessibility.accessibilityTitleUIElement](https://developer.apple.com/documentation/appkit/nsaccessibility/1535155-accessibilitytitleuielement)Added [NSAccessibility.accessibilityToolbarButton](https://developer.apple.com/documentation/appkit/nsaccessibility/1535075-accessibilitytoolbarbutton)Added [NSAccessibility.accessibilityTopLevelUIElement](https://developer.apple.com/documentation/appkit/nsaccessibility/1535092-accessibilitytopleveluielement)Added [NSAccessibility.accessibilityURL](https://developer.apple.com/documentation/appkit/nsaccessibility/1535157-accessibilityurl)Added [NSAccessibility.accessibilityUnitDescription](https://developer.apple.com/documentation/appkit/nsaccessibility/1535094-accessibilityunitdescription)Added [NSAccessibility.accessibilityUnits](https://developer.apple.com/documentation/appkit/nsaccessibility/1535029-accessibilityunits)Added [NSAccessibility.accessibilityValue](https://developer.apple.com/documentation/appkit/nsaccessibility/1535103-accessibilityvalue)Added [NSAccessibility.accessibilityValueDescription](https://developer.apple.com/documentation/appkit/nsaccessibility/1535113-accessibilityvaluedescription)Added [NSAccessibility.accessibilityVerticalScrollBar](https://developer.apple.com/documentation/appkit/nsaccessibility/1535053-accessibilityverticalscrollbar)Added [NSAccessibility.accessibilityVerticalUnitDescription](https://developer.apple.com/documentation/appkit/nsaccessibility/1535065-accessibilityverticalunitdescrip)Added [NSAccessibility.accessibilityVerticalUnits](https://developer.apple.com/documentation/appkit/nsaccessibility/1535011-accessibilityverticalunits)Added [NSAccessibility.accessibilityVisibleCells](https://developer.apple.com/documentation/appkit/nsaccessibility/1535042-accessibilityvisiblecells)Added [NSAccessibility.accessibilityVisibleCharacterRange](https://developer.apple.com/documentation/appkit/nsaccessibility/1535058-accessibilityvisiblecharacterran)Added [NSAccessibility.accessibilityVisibleChildren](https://developer.apple.com/documentation/appkit/nsaccessibility/1534964-accessibilityvisiblechildren)Added [NSAccessibility.accessibilityVisibleColumns](https://developer.apple.com/documentation/appkit/nsaccessibility/1535150-accessibilityvisiblecolumns)Added [NSAccessibility.accessibilityVisibleRows](https://developer.apple.com/documentation/appkit/nsaccessibility/1535004-accessibilityvisiblerows)Added [NSAccessibility.accessibilityWarningValue](https://developer.apple.com/documentation/appkit/nsaccessibility/1535032-accessibilitywarningvalue)Added [NSAccessibility.accessibilityWindow](https://developer.apple.com/documentation/appkit/nsaccessibility/1535030-accessibilitywindow)Added [NSAccessibility.accessibilityWindows](https://developer.apple.com/documentation/appkit/nsaccessibility/1535117-accessibilitywindows)Added [NSAccessibility.accessibilityZoomButton](https://developer.apple.com/documentation/appkit/nsaccessibility/1535090-accessibilityzoombutton)Added [-[NSAccessibility isAccessibilitySelectorAllowed:]](https://developer.apple.com/documentation/appkit/nsaccessibility/1524956-isaccessibilityselectorallowed)Added [NSAccessibilityButton](https://developer.apple.com/documentation/appkit/nsaccessibilitybutton)Added [-[NSAccessibilityButton accessibilityLabel]](https://developer.apple.com/documentation/appkit/nsaccessibilitybutton/1524910-accessibilitylabel)Added [-[NSAccessibilityButton accessibilityPerformPress]](https://developer.apple.com/documentation/appkit/nsaccessibilitybutton/1525542-accessibilityperformpress)Added [NSAccessibilityCheckBox](https://developer.apple.com/documentation/appkit/nsaccessibilitycheckbox)Added [-[NSAccessibilityCheckBox accessibilityValue]](https://developer.apple.com/documentation/appkit/nsaccessibilitycheckbox/1524299-accessibilityvalue)Added [NSAccessibilityContainsTransientUI](https://developer.apple.com/documentation/appkit/nsaccessibilitycontainstransientui)Added [-[NSAccessibilityContainsTransientUI accessibilityPerformShowAlternateUI]](https://developer.apple.com/documentation/appkit/nsaccessibilitycontainstransientui/1535134-accessibilityperformshowalternat)Added [-[NSAccessibilityContainsTransientUI accessibilityPerformShowDefaultUI]](https://developer.apple.com/documentation/appkit/nsaccessibilitycontainstransientui/1529235-accessibilityperformshowdefaultu)Added [-[NSAccessibilityContainsTransientUI isAccessibilityAlternateUIVisible]](https://developer.apple.com/documentation/appkit/nsaccessibilitycontainstransientui/1526272-isaccessibilityalternateuivisibl)Added [NSAccessibilityElement](https://developer.apple.com/documentation/appkit/nsaccessibilityelementprotocol)Added [-[NSAccessibilityElement accessibilityFrame]](https://developer.apple.com/documentation/appkit/nsaccessibilityelementprotocol/1528055-accessibilityframe)Added [-[NSAccessibilityElement accessibilityIdentifier]](https://developer.apple.com/documentation/appkit/nsaccessibilityelementprotocol/1533707-accessibilityidentifier)Added [-[NSAccessibilityElement accessibilityParent]](https://developer.apple.com/documentation/appkit/1534023-nsaccessibilityelement/1529078-accessibilityparent)Added [-[NSAccessibilityElement isAccessibilityFocused]](https://developer.apple.com/documentation/appkit/nsaccessibilityelementprotocol/1525133-isaccessibilityfocused)Added [NSAccessibilityGroup](https://developer.apple.com/documentation/appkit/nsaccessibilitygroup)Added [NSAccessibilityImage](https://developer.apple.com/documentation/appkit/nsaccessibilityimage)Added [-[NSAccessibilityImage accessibilityLabel]](https://developer.apple.com/documentation/appkit/nsaccessibilityimage/1531608-accessibilitylabel)Added [NSAccessibilityLayoutArea](https://developer.apple.com/documentation/appkit/nsaccessibilitylayoutarea)Added [-[NSAccessibilityLayoutArea accessibilityChildren]](https://developer.apple.com/documentation/appkit/nsaccessibilitylayoutarea/1534997-accessibilitychildren)Added [-[NSAccessibilityLayoutArea accessibilityFocusedUIElement]](https://developer.apple.com/documentation/appkit/nsaccessibilitylayoutarea/1533902-accessibilityfocuseduielement)Added [-[NSAccessibilityLayoutArea accessibilityLabel]](https://developer.apple.com/documentation/appkit/nsaccessibilitylayoutarea/1527051-accessibilitylabel)Added [-[NSAccessibilityLayoutArea accessibilitySelectedChildren]](https://developer.apple.com/documentation/appkit/nsaccessibilitylayoutarea/1528883-accessibilityselectedchildren)Added [NSAccessibilityLayoutItem](https://developer.apple.com/documentation/appkit/nsaccessibilitylayoutitem)Added [-[NSAccessibilityLayoutItem setAccessibilityFrame:]](https://developer.apple.com/documentation/appkit/nsaccessibilitylayoutitem/1533160-setaccessibilityframe)Added [NSAccessibilityList](https://developer.apple.com/documentation/appkit/nsaccessibilitylist)Added [NSAccessibilityNavigableStaticText](https://developer.apple.com/documentation/appkit/nsaccessibilitynavigablestatictext)Added [-[NSAccessibilityNavigableStaticText accessibilityFrameForRange:]](https://developer.apple.com/documentation/appkit/nsaccessibilitynavigablestatictext/1524702-accessibilityframeforrange)Added [-[NSAccessibilityNavigableStaticText accessibilityLineForIndex:]](https://developer.apple.com/documentation/appkit/nsaccessibilitynavigablestatictext/1534931-accessibilitylineforindex)Added [-[NSAccessibilityNavigableStaticText accessibilityRangeForLine:]](https://developer.apple.com/documentation/appkit/nsaccessibilitynavigablestatictext/1527015-accessibilityrangeforline)Added [-[NSAccessibilityNavigableStaticText accessibilityStringForRange:]](https://developer.apple.com/documentation/appkit/nsaccessibilitynavigablestatictext/1525402-accessibilitystringforrange)Added [NSAccessibilityOutline](https://developer.apple.com/documentation/appkit/nsaccessibilityoutline)Added [NSAccessibilityProgressIndicator](https://developer.apple.com/documentation/appkit/nsaccessibilityprogressindicator)Added [-[NSAccessibilityProgressIndicator accessibilityValue]](https://developer.apple.com/documentation/appkit/nsaccessibilityprogressindicator/1531500-accessibilityvalue)Added [NSAccessibilityRadioButton](https://developer.apple.com/documentation/appkit/nsaccessibilityradiobutton)Added [-[NSAccessibilityRadioButton accessibilityValue]](https://developer.apple.com/documentation/appkit/nsaccessibilityradiobutton/1526534-accessibilityvalue)Added [NSAccessibilityRow](https://developer.apple.com/documentation/appkit/nsaccessibilityrow)Added [-[NSAccessibilityRow accessibilityDisclosureLevel]](https://developer.apple.com/documentation/appkit/nsaccessibilityrow/1531837-accessibilitydisclosurelevel)Added [-[NSAccessibilityRow accessibilityIndex]](https://developer.apple.com/documentation/appkit/nsaccessibilityrow/1526746-accessibilityindex)Added [NSAccessibilitySlider](https://developer.apple.com/documentation/appkit/nsaccessibilityslider)Added [-[NSAccessibilitySlider accessibilityLabel]](https://developer.apple.com/documentation/appkit/nsaccessibilityslider/1530176-accessibilitylabel)Added [-[NSAccessibilitySlider accessibilityPerformDecrement]](https://developer.apple.com/documentation/appkit/nsaccessibilityslider/1534967-accessibilityperformdecrement)Added [-[NSAccessibilitySlider accessibilityPerformIncrement]](https://developer.apple.com/documentation/appkit/nsaccessibilityslider/1528478-accessibilityperformincrement)Added [-[NSAccessibilitySlider accessibilityValue]](https://developer.apple.com/documentation/appkit/nsaccessibilityslider/1530335-accessibilityvalue)Added [NSAccessibilityStaticText](https://developer.apple.com/documentation/appkit/nsaccessibilitystatictext)Added [-[NSAccessibilityStaticText accessibilityAttributedStringForRange:]](https://developer.apple.com/documentation/appkit/nsaccessibilitystatictext/1535001-accessibilityattributedstringfor)Added [-[NSAccessibilityStaticText accessibilityValue]](https://developer.apple.com/documentation/appkit/nsaccessibilitystatictext/1528730-accessibilityvalue)Added [-[NSAccessibilityStaticText accessibilityVisibleCharacterRange]](https://developer.apple.com/documentation/appkit/nsaccessibilitystatictext/1532230-accessibilityvisiblecharacterran)Added [NSAccessibilityStepper](https://developer.apple.com/documentation/appkit/nsaccessibilitystepper)Added [-[NSAccessibilityStepper accessibilityLabel]](https://developer.apple.com/documentation/appkit/nsaccessibilitystepper/1528702-accessibilitylabel)Added [-[NSAccessibilityStepper accessibilityPerformDecrement]](https://developer.apple.com/documentation/appkit/nsaccessibilitystepper/1525327-accessibilityperformdecrement)Added [-[NSAccessibilityStepper accessibilityPerformIncrement]](https://developer.apple.com/documentation/appkit/nsaccessibilitystepper/1533764-accessibilityperformincrement)Added [-[NSAccessibilityStepper accessibilityValue]](https://developer.apple.com/documentation/appkit/nsaccessibilitystepper/1528167-accessibilityvalue)Added [NSAccessibilitySwitch](https://developer.apple.com/documentation/appkit/nsaccessibilityswitch)Added [-[NSAccessibilitySwitch accessibilityPerformDecrement]](https://developer.apple.com/documentation/appkit/nsaccessibilityswitch/1528290-accessibilityperformdecrement)Added [-[NSAccessibilitySwitch accessibilityPerformIncrement]](https://developer.apple.com/documentation/appkit/nsaccessibilityswitch/1533985-accessibilityperformincrement)Added [-[NSAccessibilitySwitch accessibilityValue]](https://developer.apple.com/documentation/appkit/nsaccessibilityswitch/1533946-accessibilityvalue)Added [NSAccessibilityTable](https://developer.apple.com/documentation/appkit/nsaccessibilitytable)Added [-[NSAccessibilityTable accessibilityColumnHeaderUIElements]](https://developer.apple.com/documentation/appkit/nsaccessibilitytable/1526621-accessibilitycolumnheaderuieleme)Added [-[NSAccessibilityTable accessibilityColumns]](https://developer.apple.com/documentation/appkit/nsaccessibilitytable/1524744-accessibilitycolumns)Added [-[NSAccessibilityTable accessibilityHeaderGroup]](https://developer.apple.com/documentation/appkit/nsaccessibilitytable/1535017-accessibilityheadergroup)Added [-[NSAccessibilityTable accessibilityLabel]](https://developer.apple.com/documentation/appkit/nsaccessibilitytable/1526563-accessibilitylabel)Added [-[NSAccessibilityTable accessibilityRowHeaderUIElements]](https://developer.apple.com/documentation/appkit/nsaccessibilitytable/1524262-accessibilityrowheaderuielements)Added [-[NSAccessibilityTable accessibilityRows]](https://developer.apple.com/documentation/appkit/nsaccessibilitytable/1526672-accessibilityrows)Added [-[NSAccessibilityTable accessibilitySelectedCells]](https://developer.apple.com/documentation/appkit/nsaccessibilitytable/1525577-accessibilityselectedcells)Added [-[NSAccessibilityTable accessibilitySelectedColumns]](https://developer.apple.com/documentation/appkit/nsaccessibilitytable/1528430-accessibilityselectedcolumns)Added [-[NSAccessibilityTable accessibilitySelectedRows]](https://developer.apple.com/documentation/appkit/nsaccessibilitytable/1529241-accessibilityselectedrows)Added [-[NSAccessibilityTable accessibilityVisibleCells]](https://developer.apple.com/documentation/appkit/nsaccessibilitytable/1526711-accessibilityvisiblecells)Added [-[NSAccessibilityTable accessibilityVisibleColumns]](https://developer.apple.com/documentation/appkit/nsaccessibilitytable/1530264-accessibilityvisiblecolumns)Added [-[NSAccessibilityTable accessibilityVisibleRows]](https://developer.apple.com/documentation/appkit/nsaccessibilitytable/1535128-accessibilityvisiblerows)Added [-[NSAccessibilityTable setAccessibilitySelectedRows:]](https://developer.apple.com/documentation/appkit/nsaccessibilitytable/1534612-setaccessibilityselectedrows)NSActionCell.hRemoved [-[NSActionCell action]](https://developer.apple.com/documentation/appkit/nsactioncell/1531427-action)Removed [-[NSActionCell setAction:]](https://developer.apple.com/documentation/appkit/nsactioncell/1531427-action)Removed [-[NSActionCell setTag:]](https://developer.apple.com/documentation/appkit/nsactioncell/1535314-tag)Removed [-[NSActionCell setTarget:]](https://developer.apple.com/documentation/appkit/nsactioncell/1535837-target)Removed [-[NSActionCell tag]](https://developer.apple.com/documentation/appkit/nsactioncell/1535314-tag)Removed [-[NSActionCell target]](https://developer.apple.com/documentation/appkit/nsactioncell/1535837-target)Added [NSActionCell.action](https://developer.apple.com/documentation/appkit/nsactioncell/1531427-action)Added [NSActionCell.tag](https://developer.apple.com/documentation/appkit/nsactioncell/1535314-tag)Added [NSActionCell.target](https://developer.apple.com/documentation/appkit/nsactioncell/1535837-target)NSAlert.hRemoved [-[NSAlert accessoryView]](https://developer.apple.com/documentation/appkit/nsalert/1530575-accessoryview)Removed [-[NSAlert alertStyle]](https://developer.apple.com/documentation/appkit/nsalert/1528506-alertstyle)Removed [-[NSAlert buttons]](https://developer.apple.com/documentation/appkit/nsalert/1532992-buttons)Removed [-[NSAlert delegate]](https://developer.apple.com/documentation/appkit/nsalert/1534327-delegate)Removed [-[NSAlert helpAnchor]](https://developer.apple.com/documentation/appkit/nsalert/1534314-helpanchor)Removed [-[NSAlert icon]](https://developer.apple.com/documentation/appkit/nsalert/1531688-icon)Removed [-[NSAlert informativeText]](https://developer.apple.com/documentation/appkit/nsalert/1529629-informativetext)Removed [-[NSAlert messageText]](https://developer.apple.com/documentation/appkit/nsalert/1532498-messagetext)Removed [-[NSAlert setAccessoryView:]](https://developer.apple.com/documentation/appkit/nsalert/1530575-accessoryview)Removed [-[NSAlert setAlertStyle:]](https://developer.apple.com/documentation/appkit/nsalert/1528506-alertstyle)Removed [-[NSAlert setDelegate:]](https://developer.apple.com/documentation/appkit/nsalert/1534327-delegate)Removed [-[NSAlert setHelpAnchor:]](https://developer.apple.com/documentation/appkit/nsalert/1534314-helpanchor)Removed [-[NSAlert setIcon:]](https://developer.apple.com/documentation/appkit/nsalert/1531688-icon)Removed [-[NSAlert setInformativeText:]](https://developer.apple.com/documentation/appkit/nsalert/1529629-informativetext)Removed [-[NSAlert setMessageText:]](https://developer.apple.com/documentation/appkit/nsalert/1532498-messagetext)Removed [-[NSAlert setShowsHelp:]](https://developer.apple.com/documentation/appkit/nsalert/1535856-showshelp)Removed [-[NSAlert setShowsSuppressionButton:]](https://developer.apple.com/documentation/appkit/nsalert/1535196-showssuppressionbutton)Removed [-[NSAlert showsHelp]](https://developer.apple.com/documentation/appkit/nsalert/1535856-showshelp)Removed [-[NSAlert showsSuppressionButton]](https://developer.apple.com/documentation/appkit/nsalert/1535196-showssuppressionbutton)Removed [-[NSAlert suppressionButton]](https://developer.apple.com/documentation/appkit/nsalert/1532209-suppressionbutton)Removed [-[NSAlert window]](https://developer.apple.com/documentation/appkit/nsalert/1526566-window)Added [NSAlert.accessoryView](https://developer.apple.com/documentation/appkit/nsalert/1530575-accessoryview)Added [NSAlert.alertStyle](https://developer.apple.com/documentation/appkit/nsalert/1528506-alertstyle)Added [NSAlert.buttons](https://developer.apple.com/documentation/appkit/nsalert/1532992-buttons)Added [NSAlert.delegate](https://developer.apple.com/documentation/appkit/nsalert/1534327-delegate)Added [NSAlert.helpAnchor](https://developer.apple.com/documentation/appkit/nsalert/1534314-helpanchor)Added [NSAlert.icon](https://developer.apple.com/documentation/appkit/nsalert/1531688-icon)Added [NSAlert.informativeText](https://developer.apple.com/documentation/appkit/nsalert/1529629-informativetext)Added [NSAlert.messageText](https://developer.apple.com/documentation/appkit/nsalert/1532498-messagetext)Added [NSAlert.showsHelp](https://developer.apple.com/documentation/appkit/nsalert/1535856-showshelp)Added [NSAlert.showsSuppressionButton](https://developer.apple.com/documentation/appkit/nsalert/1535196-showssuppressionbutton)Added [NSAlert.suppressionButton](https://developer.apple.com/documentation/appkit/nsalert/1532209-suppressionbutton)Added [NSAlert.window](https://developer.apple.com/documentation/appkit/nsalert/1526566-window)Modified [+[NSAlert alertWithMessageText:defaultButton:alternateButton:otherButton:informativeTextWithFormat:]](https://developer.apple.com/documentation/appkit/nsalert/1550982-alertwithmessagetext)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSAlert beginSheetModalForWindow:modalDelegate:didEndSelector:contextInfo:]](https://developer.apple.com/documentation/appkit/nsalert/1532128-beginsheetmodalforwindow)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSAlertDelegate alertShowHelp:]](https://developer.apple.com/documentation/appkit/nsalertdelegate/1526980-alertshowhelp)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSAnimation.hRemoved [-[NSAnimation animationBlockingMode]](https://developer.apple.com/documentation/appkit/nsanimation/1533725-animationblockingmode)Removed [-[NSAnimation animationCurve]](https://developer.apple.com/documentation/appkit/nsanimation/1535321-animationcurve)Removed [-[NSAnimation currentProgress]](https://developer.apple.com/documentation/appkit/nsanimation/1530843-currentprogress)Removed [-[NSAnimation currentValue]](https://developer.apple.com/documentation/appkit/nsanimation/1531043-currentvalue)Removed [-[NSAnimation delegate]](https://developer.apple.com/documentation/appkit/nsanimation/1524439-delegate)Removed [-[NSAnimation duration]](https://developer.apple.com/documentation/appkit/nsanimation/1535110-duration)Removed [-[NSAnimation frameRate]](https://developer.apple.com/documentation/appkit/nsanimation/1526694-framerate)Removed [-[NSAnimation isAnimating]](https://developer.apple.com/documentation/appkit/nsanimation/1527492-isanimating)Removed [-[NSAnimation progressMarks]](https://developer.apple.com/documentation/appkit/nsanimation/1533642-progressmarks)Removed [-[NSAnimation runLoopModesForAnimating]](https://developer.apple.com/documentation/appkit/nsanimation/1526965-runloopmodesforanimating)Removed [-[NSAnimation setAnimationBlockingMode:]](https://developer.apple.com/documentation/appkit/nsanimation/1533725-animationblockingmode)Removed [-[NSAnimation setAnimationCurve:]](https://developer.apple.com/documentation/appkit/nsanimation/1535321-animationcurve)Removed [-[NSAnimation setCurrentProgress:]](https://developer.apple.com/documentation/appkit/nsanimation/1530843-currentprogress)Removed [-[NSAnimation setDelegate:]](https://developer.apple.com/documentation/appkit/nsanimation/1524439-delegate)Removed [-[NSAnimation setDuration:]](https://developer.apple.com/documentation/appkit/nsanimation/1535110-duration)Removed [-[NSAnimation setFrameRate:]](https://developer.apple.com/documentation/appkit/nsanimation/1526694-framerate)Removed [-[NSAnimation setProgressMarks:]](https://developer.apple.com/documentation/appkit/nsanimation/1533642-progressmarks)Removed [-[NSViewAnimation setViewAnimations:]](https://developer.apple.com/documentation/appkit/nsviewanimation/1527416-viewanimations)Removed [-[NSViewAnimation viewAnimations]](https://developer.apple.com/documentation/appkit/nsviewanimation/1527416-viewanimations)Added [NSAnimation.animating](https://developer.apple.com/documentation/appkit/nsanimation/1527492-isanimating)Added [NSAnimation.animationBlockingMode](https://developer.apple.com/documentation/appkit/nsanimation/1533725-animationblockingmode)Added [NSAnimation.animationCurve](https://developer.apple.com/documentation/appkit/nsanimation/1535321-animationcurve)Added [NSAnimation.currentProgress](https://developer.apple.com/documentation/appkit/nsanimation/1530843-currentprogress)Added [NSAnimation.currentValue](https://developer.apple.com/documentation/appkit/nsanimation/1531043-currentvalue)Added [NSAnimation.delegate](https://developer.apple.com/documentation/appkit/nsanimation/1524439-delegate)Added [NSAnimation.duration](https://developer.apple.com/documentation/appkit/nsanimation/1535110-duration)Added [NSAnimation.frameRate](https://developer.apple.com/documentation/appkit/nsanimation/1526694-framerate)Added [NSAnimation.progressMarks](https://developer.apple.com/documentation/appkit/nsanimation/1533642-progressmarks)Added [NSAnimation.runLoopModesForAnimating](https://developer.apple.com/documentation/appkit/nsanimation/1526965-runloopmodesforanimating)Added [NSViewAnimation.viewAnimations](https://developer.apple.com/documentation/appkit/nsviewanimation/1527416-viewanimations)Modified [-[NSAnimation initWithDuration:animationCurve:]](https://developer.apple.com/documentation/appkit/nsanimation/1530069-initwithduration)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDuration:(NSTimeInterval)duration animationCurve:(NSAnimationCurve)animationCurve ``` |
| To | ``` - (instancetype)initWithDuration:(NSTimeInterval)duration animationCurve:(NSAnimationCurve)animationCurve ``` |

Modified [-[NSAnimationDelegate animation:didReachProgressMark:]](https://developer.apple.com/documentation/appkit/nsanimationdelegate/1535100-animation)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSAnimationDelegate animation:valueForProgress:]](https://developer.apple.com/documentation/appkit/nsanimationdelegate/1528965-animation)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSAnimationDelegate animationDidEnd:]](https://developer.apple.com/documentation/appkit/nsanimationdelegate/1535871-animationdidend)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSAnimationDelegate animationDidStop:]](https://developer.apple.com/documentation/appkit/nsanimationdelegate/1534155-animationdidstop)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSAnimationDelegate animationShouldStart:]](https://developer.apple.com/documentation/appkit/nsanimationdelegate/1533279-animationshouldstart)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSViewAnimation initWithViewAnimations:]](https://developer.apple.com/documentation/appkit/nsviewanimation/1531141-initwithviewanimations)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithViewAnimations:(NSArray *)viewAnimations ``` |
| To | ``` - (instancetype)initWithViewAnimations:(NSArray *)viewAnimations ``` |

NSAnimationContext.hModified [NSAnimationContext.timingFunction](https://developer.apple.com/documentation/appkit/nsanimationcontext/1524985-timingfunction)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) CAMediaTimingFunction *timingFunction ``` |
| To | ``` @property(strong) CAMediaTimingFunction *timingFunction ``` |

NSAppearance.hAdded [NSAppearance.allowsVibrancy](https://developer.apple.com/documentation/appkit/nsappearance/1524694-allowsvibrancy)Added [NSAppearance.name](https://developer.apple.com/documentation/appkit/nsappearance/1528677-name)Added [NSAppearanceNameVibrantDark](https://developer.apple.com/documentation/appkit/nsappearance/name/1529488-vibrantdark)Added [NSAppearanceNameVibrantLight](https://developer.apple.com/documentation/appkit/nsappearance/name/1535233-vibrantlight)Modified [-[NSAppearance initWithAppearanceNamed:bundle:]](https://developer.apple.com/documentation/appkit/nsappearance/1529131-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithAppearanceNamed:(NSString *)name bundle:(NSBundle *)bundle ``` |
| To | ``` - (instancetype)initWithAppearanceNamed:(NSString *)name bundle:(NSBundle *)bundle ``` |

Modified [NSAppearanceCustomization.appearance](https://developer.apple.com/documentation/appkit/nsappearancecustomization/1533925-appearance)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) NSAppearance *appearance ``` |
| To | ``` @property(strong) NSAppearance *appearance ``` |

Modified [NSAppearanceCustomization.effectiveAppearance](https://developer.apple.com/documentation/appkit/nsappearancecustomization/1535147-effectiveappearance)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSAppearance *effectiveAppearance ``` |
| To | ``` @property(readonly, strong) NSAppearance *effectiveAppearance ``` |

Modified [NSAppearanceNameLightContent](https://developer.apple.com/documentation/appkit/nsappearance/name/1527091-lightcontent)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

NSAppleScriptExtensions.hRemoved [-[NSAppleScript richTextSource]](https://developer.apple.com/documentation/foundation/nsapplescript/1387495-richtextsource)Added [NSAppleScript.richTextSource](https://developer.apple.com/documentation/foundation/nsapplescript/1387495-richtextsource)NSApplication.hRemoved [-[NSApplication applicationIconImage]](https://developer.apple.com/documentation/appkit/nsapplication/1428744-applicationiconimage)Removed [-[NSApplication context]](https://developer.apple.com/documentation/appkit/nsapplication/1428535-context)Removed [-[NSApplication currentEvent]](https://developer.apple.com/documentation/appkit/nsapplication/1428668-currentevent)Removed [-[NSApplication currentSystemPresentationOptions]](https://developer.apple.com/documentation/appkit/nsapplication/1428717-currentsystempresentationoptions)Removed [-[NSApplication delegate]](https://developer.apple.com/documentation/appkit/nsapplication/1428705-delegate)Removed [-[NSApplication dockTile]](https://developer.apple.com/documentation/appkit/nsapplication/1428671-docktile)Removed [-[NSApplication enabledRemoteNotificationTypes]](https://developer.apple.com/documentation/appkit/nsapplication/1428776-enabledremotenotificationtypes)Removed [-[NSApplication helpMenu]](https://developer.apple.com/documentation/appkit/nsapplication/1428644-helpmenu)Removed [-[NSApplication isActive]](https://developer.apple.com/documentation/appkit/nsapplication/1428493-isactive)Removed [-[NSApplication isFullKeyboardAccessEnabled]](https://developer.apple.com/documentation/appkit/nsapplication/1428469-fullkeyboardaccessenabled)Removed [-[NSApplication isHidden]](https://developer.apple.com/documentation/appkit/nsapplication/1428416-ishidden)Removed [-[NSApplication isRunning]](https://developer.apple.com/documentation/appkit/nsapplication/1428759-running)Removed [-[NSApplication keyWindow]](https://developer.apple.com/documentation/appkit/nsapplication/1428406-keywindow)Removed [-[NSApplication mainMenu]](https://developer.apple.com/documentation/appkit/nsapplication/1428634-mainmenu)Removed [-[NSApplication mainWindow]](https://developer.apple.com/documentation/appkit/nsapplication/1428723-mainwindow)Removed [-[NSApplication modalWindow]](https://developer.apple.com/documentation/appkit/nsapplication/1428610-modalwindow)Removed [-[NSApplication occlusionState]](https://developer.apple.com/documentation/appkit/nsapplication/1428656-occlusionstate)Removed [-[NSApplication presentationOptions]](https://developer.apple.com/documentation/appkit/nsapplication/1428664-presentationoptions)Removed [-[NSApplication servicesMenu]](https://developer.apple.com/documentation/appkit/nsapplication/1428608-servicesmenu)Removed [-[NSApplication servicesProvider]](https://developer.apple.com/documentation/appkit/nsapplication/1428467-servicesprovider)Removed [-[NSApplication setApplicationIconImage:]](https://developer.apple.com/documentation/appkit/nsapplication/1428744-applicationiconimage)Removed [-[NSApplication setDelegate:]](https://developer.apple.com/documentation/appkit/nsapplication/1428705-delegate)Removed [-[NSApplication setHelpMenu:]](https://developer.apple.com/documentation/appkit/nsapplication/1428644-helpmenu)Removed [-[NSApplication setMainMenu:]](https://developer.apple.com/documentation/appkit/nsapplication/1428634-mainmenu)Removed [-[NSApplication setPresentationOptions:]](https://developer.apple.com/documentation/appkit/nsapplication/1428664-presentationoptions)Removed [-[NSApplication setServicesMenu:]](https://developer.apple.com/documentation/appkit/nsapplication/1428608-servicesmenu)Removed [-[NSApplication setServicesProvider:]](https://developer.apple.com/documentation/appkit/nsapplication/1428467-servicesprovider)Removed [-[NSApplication setWindowsMenu:]](https://developer.apple.com/documentation/appkit/nsapplication/1428547-windowsmenu)Removed [-[NSApplication userInterfaceLayoutDirection]](https://developer.apple.com/documentation/appkit/nsapplication/1428556-userinterfacelayoutdirection)Removed [-[NSApplication windows]](https://developer.apple.com/documentation/appkit/nsapplication/1428402-windows)Removed [-[NSApplication windowsMenu]](https://developer.apple.com/documentation/appkit/nsapplication/1428547-windowsmenu)Added [NSApplication.active](https://developer.apple.com/documentation/appkit/nsapplication/1428493-active)Added [NSApplication.applicationIconImage](https://developer.apple.com/documentation/appkit/nsapplication/1428744-applicationiconimage)Added [NSApplication.context](https://developer.apple.com/documentation/appkit/nsapplication/1428535-context)Added [NSApplication.currentEvent](https://developer.apple.com/documentation/appkit/nsapplication/1428668-currentevent)Added [NSApplication.currentSystemPresentationOptions](https://developer.apple.com/documentation/appkit/nsapplication/1428717-currentsystempresentationoptions)Added [NSApplication.delegate](https://developer.apple.com/documentation/appkit/nsapplication/1428705-delegate)Added [NSApplication.dockTile](https://developer.apple.com/documentation/appkit/nsapplication/1428671-docktile)Added [NSApplication.enabledRemoteNotificationTypes](https://developer.apple.com/documentation/appkit/nsapplication/1428776-enabledremotenotificationtypes)Added [NSApplication.fullKeyboardAccessEnabled](https://developer.apple.com/documentation/appkit/nsapplication/1428469-isfullkeyboardaccessenabled)Added [NSApplication.helpMenu](https://developer.apple.com/documentation/appkit/nsapplication/1428644-helpmenu)Added [NSApplication.hidden](https://developer.apple.com/documentation/appkit/nsapplication/1428416-ishidden)Added [NSApplication.keyWindow](https://developer.apple.com/documentation/appkit/nsapplication/1428406-keywindow)Added [NSApplication.mainMenu](https://developer.apple.com/documentation/appkit/nsapplication/1428634-mainmenu)Added [NSApplication.mainWindow](https://developer.apple.com/documentation/appkit/nsapplication/1428723-mainwindow)Added [NSApplication.modalWindow](https://developer.apple.com/documentation/appkit/nsapplication/1428610-modalwindow)Added [NSApplication.occlusionState](https://developer.apple.com/documentation/appkit/nsapplication/1428656-occlusionstate)Added [NSApplication.presentationOptions](https://developer.apple.com/documentation/appkit/nsapplication/1428664-presentationoptions)Added [NSApplication.running](https://developer.apple.com/documentation/appkit/nsapplication/1428759-isrunning)Added [NSApplication.servicesMenu](https://developer.apple.com/documentation/appkit/nsapplication/1428608-servicesmenu)Added [NSApplication.servicesProvider](https://developer.apple.com/documentation/appkit/nsapplication/1428467-servicesprovider)Added [NSApplication.userInterfaceLayoutDirection](https://developer.apple.com/documentation/appkit/nsapplication/1428556-userinterfacelayoutdirection)Added [NSApplication.windows](https://developer.apple.com/documentation/appkit/nsapplication/1428402-windows)Added [NSApplication.windowsMenu](https://developer.apple.com/documentation/appkit/nsapplication/1428547-windowsmenu)Added [-[NSApplicationDelegate application:continueUserActivity:restorationHandler:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428471-application)Added [-[NSApplicationDelegate application:didFailToContinueUserActivityWithType:error:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428613-application)Added [-[NSApplicationDelegate application:didUpdateUserActivity:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428457-application)Added [-[NSApplicationDelegate application:willContinueUserActivityWithType:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428364-application)Added [#def NSAppKitVersionNumber10_9](https://developer.apple.com/documentation/appkit/nsappkitversionnumber10_9)Modified [NSApplication](https://developer.apple.com/documentation/appkit/nsapplication)

|  | Protocols |
| --- | --- |
| From | NSUserInterfaceValidations |
| To | NSAccessibility, NSAccessibilityElement, NSUserInterfaceValidations |

Modified [-[NSApplication beginSheet:modalForWindow:modalDelegate:didEndSelector:contextInfo:]](https://developer.apple.com/documentation/appkit/nsapplication/1428505-beginsheet)

|  | Deprecation |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.10 |

Modified [-[NSApplication endSheet:]](https://developer.apple.com/documentation/appkit/nsapplication/1428503-endsheet)

|  | Deprecation |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.10 |

Modified [-[NSApplication endSheet:returnCode:]](https://developer.apple.com/documentation/appkit/nsapplication/1428629-endsheet)

|  | Deprecation |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.10 |

Modified [-[NSApplicationDelegate application:didDecodeRestorableState:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428693-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate application:didFailToRegisterForRemoteNotificationsWithError:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428554-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate application:didReceiveRemoteNotification:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428430-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate application:didRegisterForRemoteNotificationsWithDeviceToken:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428766-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate application:openFile:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428612-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate application:openFileWithoutUI:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428459-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate application:openFiles:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428742-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate application:openTempFile:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428495-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate application:printFile:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428520-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate application:printFiles:withSettings:showPrintPanels:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428713-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate application:willEncodeRestorableState:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428400-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate application:willPresentError:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428721-application)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate applicationDidBecomeActive:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428577-applicationdidbecomeactive)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate applicationDidChangeOcclusionState:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428362-applicationdidchangeocclusionsta)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate applicationDidChangeScreenParameters:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428424-applicationdidchangescreenparame)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate applicationDidFinishLaunching:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428385-applicationdidfinishlaunching)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate applicationDidHide:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428552-applicationdidhide)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate applicationDidResignActive:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428636-applicationdidresignactive)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate applicationDidUnhide:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428755-applicationdidunhide)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate applicationDidUpdate:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428589-applicationdidupdate)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate applicationDockMenu:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428564-applicationdockmenu)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate applicationOpenUntitledFile:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428491-applicationopenuntitledfile)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate applicationShouldHandleReopen:hasVisibleWindows:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428638-applicationshouldhandlereopen)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate applicationShouldOpenUntitledFile:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428444-applicationshouldopenuntitledfil)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate applicationShouldTerminate:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428642-applicationshouldterminate)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate applicationShouldTerminateAfterLastWindowClosed:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428381-applicationshouldterminateafterl)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate applicationWillBecomeActive:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428699-applicationwillbecomeactive)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate applicationWillFinishLaunching:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428623-applicationwillfinishlaunching)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate applicationWillHide:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428478-applicationwillhide)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate applicationWillResignActive:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428539-applicationwillresignactive)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate applicationWillTerminate:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428522-applicationwillterminate)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate applicationWillUnhide:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428585-applicationwillunhide)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSApplicationDelegate applicationWillUpdate:]](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428774-applicationwillupdate)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSServicesMenuRequestor readSelectionFromPasteboard:]](https://developer.apple.com/documentation/appkit/nsservicesmenurequestor/1428481-readselection)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSServicesMenuRequestor writeSelectionToPasteboard:types:]](https://developer.apple.com/documentation/appkit/nsservicesmenurequestor/1428477-writeselection)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [NSRunAbortedResponse](https://developer.apple.com/documentation/appkit/1428372-return_values_for_modal_operatio/nsrunabortedresponse)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSRunContinuesResponse](https://developer.apple.com/documentation/appkit/1428372-return_values_for_modal_operatio/nsruncontinuesresponse)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSRunStoppedResponse](https://developer.apple.com/documentation/appkit/nsrunstoppedresponse)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

NSApplicationScripting.hRemoved [-[NSApplication orderedDocuments]](https://developer.apple.com/documentation/appkit/nsapplication/1494283-ordereddocuments)Removed [-[NSApplication orderedWindows]](https://developer.apple.com/documentation/appkit/nsapplication/1494287-orderedwindows)Added [NSApplication.orderedDocuments](https://developer.apple.com/documentation/appkit/nsapplication/1494283-ordereddocuments)Added [NSApplication.orderedWindows](https://developer.apple.com/documentation/appkit/nsapplication/1494287-orderedwindows)NSArrayController.hRemoved [-[NSArrayController alwaysUsesMultipleValuesMarker]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1527129-alwaysusesmultiplevaluesmarker)Removed [-[NSArrayController arrangedObjects]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1534299-arrangedobjects)Removed [-[NSArrayController automaticRearrangementKeyPaths]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1526714-automaticrearrangementkeypaths)Removed [-[NSArrayController automaticallyRearrangesObjects]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1524747-automaticallyrearrangesobjects)Removed [-[NSArrayController avoidsEmptySelection]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1532785-avoidsemptyselection)Removed [-[NSArrayController canInsert]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1532900-caninsert)Removed [-[NSArrayController canSelectNext]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1534863-canselectnext)Removed [-[NSArrayController canSelectPrevious]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1534274-canselectprevious)Removed [-[NSArrayController clearsFilterPredicateOnInsertion]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1534701-clearsfilterpredicateoninsertion)Removed [-[NSArrayController filterPredicate]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1524815-filterpredicate)Removed [-[NSArrayController preservesSelection]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1530628-preservesselection)Removed [-[NSArrayController selectedObjects]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1526568-selectedobjects)Removed -[NSArrayController selectionIndex]Removed [-[NSArrayController selectionIndexes]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1529908-selectionindexes)Removed [-[NSArrayController selectsInsertedObjects]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1527427-selectsinsertedobjects)Removed [-[NSArrayController setAlwaysUsesMultipleValuesMarker:]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1527129-alwaysusesmultiplevaluesmarker)Removed [-[NSArrayController setAutomaticallyRearrangesObjects:]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1524747-automaticallyrearrangesobjects)Removed [-[NSArrayController setAvoidsEmptySelection:]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1532785-avoidsemptyselection)Removed [-[NSArrayController setClearsFilterPredicateOnInsertion:]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1534701-clearsfilterpredicateoninsertion)Removed [-[NSArrayController setFilterPredicate:]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1524815-filterpredicate)Removed [-[NSArrayController setPreservesSelection:]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1530628-preservesselection)Removed [-[NSArrayController setSelectsInsertedObjects:]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1527427-selectsinsertedobjects)Removed [-[NSArrayController setSortDescriptors:]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1525707-sortdescriptors)Removed [-[NSArrayController sortDescriptors]](https://developer.apple.com/documentation/appkit/nsarraycontroller/1525707-sortdescriptors)Added [NSArrayController.alwaysUsesMultipleValuesMarker](https://developer.apple.com/documentation/appkit/nsarraycontroller/1527129-alwaysusesmultiplevaluesmarker)Added [NSArrayController.arrangedObjects](https://developer.apple.com/documentation/appkit/nsarraycontroller/1534299-arrangedobjects)Added [NSArrayController.automaticRearrangementKeyPaths](https://developer.apple.com/documentation/appkit/nsarraycontroller/1526714-automaticrearrangementkeypaths)Added [NSArrayController.automaticallyRearrangesObjects](https://developer.apple.com/documentation/appkit/nsarraycontroller/1524747-automaticallyrearrangesobjects)Added [NSArrayController.avoidsEmptySelection](https://developer.apple.com/documentation/appkit/nsarraycontroller/1532785-avoidsemptyselection)Added [NSArrayController.canInsert](https://developer.apple.com/documentation/appkit/nsarraycontroller/1532900-caninsert)Added [NSArrayController.canSelectNext](https://developer.apple.com/documentation/appkit/nsarraycontroller/1534863-canselectnext)Added [NSArrayController.canSelectPrevious](https://developer.apple.com/documentation/appkit/nsarraycontroller/1534274-canselectprevious)Added [NSArrayController.clearsFilterPredicateOnInsertion](https://developer.apple.com/documentation/appkit/nsarraycontroller/1534701-clearsfilterpredicateoninsertion)Added [NSArrayController.filterPredicate](https://developer.apple.com/documentation/appkit/nsarraycontroller/1524815-filterpredicate)Added [NSArrayController.preservesSelection](https://developer.apple.com/documentation/appkit/nsarraycontroller/1530628-preservesselection)Added [NSArrayController.selectedObjects](https://developer.apple.com/documentation/appkit/nsarraycontroller/1526568-selectedobjects)Added [NSArrayController.selectionIndex](https://developer.apple.com/documentation/appkit/nsarraycontroller/1535885-selectionindex)Added [NSArrayController.selectionIndexes](https://developer.apple.com/documentation/appkit/nsarraycontroller/1529908-selectionindexes)Added [NSArrayController.selectsInsertedObjects](https://developer.apple.com/documentation/appkit/nsarraycontroller/1527427-selectsinsertedobjects)Added [NSArrayController.sortDescriptors](https://developer.apple.com/documentation/appkit/nsarraycontroller/1525707-sortdescriptors)NSAttributedString.hRemoved [-[NSAttributedString containsAttachments]](https://developer.apple.com/documentation/foundation/nsattributedstring/1533869-containsattachments)Added [NSAttributedString.containsAttachments](https://developer.apple.com/documentation/foundation/nsattributedstring/1533869-containsattachments)Added NSAttributedString(NSAttributedStringPasteboardAdditions)Added [NSTextEffectAttributeName](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1524319-texteffect)Added [NSTextEffectLetterpressStyle](https://developer.apple.com/documentation/foundation/nsattributedstring/texteffectstyle/1532217-letterpressstyle)Modified [-[NSAttributedString initWithData:options:documentAttributes:error:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1524613-initwithdata)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(NSData *)data options:(NSDictionary *)options documentAttributes:(NSDictionary **)dict error:(NSError **)error ``` |
| To | ``` - (instancetype)initWithData:(NSData *)data options:(NSDictionary *)options documentAttributes:(NSDictionary **)dict error:(NSError **)error ``` |

Modified [-[NSAttributedString initWithDocFormat:documentAttributes:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1534329-initwithdocformat)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDocFormat:(NSData *)data documentAttributes:(NSDictionary **)dict ``` |
| To | ``` - (instancetype)initWithDocFormat:(NSData *)data documentAttributes:(NSDictionary **)dict ``` |

Modified [-[NSAttributedString initWithHTML:baseURL:documentAttributes:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1524624-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithHTML:(NSData *)data baseURL:(NSURL *)base documentAttributes:(NSDictionary **)dict ``` |
| To | ``` - (instancetype)initWithHTML:(NSData *)data baseURL:(NSURL *)base documentAttributes:(NSDictionary **)dict ``` |

Modified [-[NSAttributedString initWithHTML:documentAttributes:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1525953-initwithhtml)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithHTML:(NSData *)data documentAttributes:(NSDictionary **)dict ``` |
| To | ``` - (instancetype)initWithHTML:(NSData *)data documentAttributes:(NSDictionary **)dict ``` |

Modified [-[NSAttributedString initWithHTML:options:documentAttributes:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1535412-initwithhtml)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithHTML:(NSData *)data options:(NSDictionary *)options documentAttributes:(NSDictionary **)dict ``` |
| To | ``` - (instancetype)initWithHTML:(NSData *)data options:(NSDictionary *)options documentAttributes:(NSDictionary **)dict ``` |

Modified [-[NSAttributedString initWithPath:documentAttributes:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1525939-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithPath:(NSString *)path documentAttributes:(NSDictionary **)dict ``` |
| To | ``` - (instancetype)initWithPath:(NSString *)path documentAttributes:(NSDictionary **)dict ``` |

Modified [-[NSAttributedString initWithRTF:documentAttributes:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1532912-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithRTF:(NSData *)data documentAttributes:(NSDictionary **)dict ``` |
| To | ``` - (instancetype)initWithRTF:(NSData *)data documentAttributes:(NSDictionary **)dict ``` |

Modified [-[NSAttributedString initWithRTFD:documentAttributes:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1530987-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithRTFD:(NSData *)data documentAttributes:(NSDictionary **)dict ``` |
| To | ``` - (instancetype)initWithRTFD:(NSData *)data documentAttributes:(NSDictionary **)dict ``` |

Modified [-[NSAttributedString initWithRTFDFileWrapper:documentAttributes:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1533594-initwithrtfdfilewrapper)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithRTFDFileWrapper:(NSFileWrapper *)wrapper documentAttributes:(NSDictionary **)dict ``` |
| To | ``` - (instancetype)initWithRTFDFileWrapper:(NSFileWrapper *)wrapper documentAttributes:(NSDictionary **)dict ``` |

Modified [-[NSAttributedString initWithURL:documentAttributes:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1533913-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithURL:(NSURL *)url documentAttributes:(NSDictionary **)dict ``` |
| To | ``` - (instancetype)initWithURL:(NSURL *)url documentAttributes:(NSDictionary **)dict ``` |

Modified [-[NSAttributedString initWithURL:options:documentAttributes:error:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1530490-initwithurl)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithURL:(NSURL *)url options:(NSDictionary *)options documentAttributes:(NSDictionary **)dict error:(NSError **)error ``` |
| To | ``` - (instancetype)initWithURL:(NSURL *)url options:(NSDictionary *)options documentAttributes:(NSDictionary **)dict error:(NSError **)error ``` |

Modified [NSNoUnderlineStyle](https://developer.apple.com/documentation/appkit/1580760-nsunderlinestrikethroughmask/nsnounderlinestyle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.9 |

Modified [NSSingleUnderlineStyle](https://developer.apple.com/documentation/appkit/1580760-nsunderlinestrikethroughmask/nssingleunderlinestyle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.9 |

NSBezierPath.hRemoved [-[NSBezierPath bezierPathByFlatteningPath]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520733-bezierpathbyflatteningpath)Removed [-[NSBezierPath bezierPathByReversingPath]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520656-reversed)Removed [-[NSBezierPath bounds]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520722-bounds)Removed [-[NSBezierPath controlPointBounds]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520654-controlpointbounds)Removed [-[NSBezierPath currentPoint]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520698-currentpoint)Removed [-[NSBezierPath elementCount]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520645-elementcount)Removed [-[NSBezierPath flatness]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520676-flatness)Removed [-[NSBezierPath isEmpty]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520712-empty)Removed [-[NSBezierPath lineCapStyle]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520667-linecapstyle)Removed [-[NSBezierPath lineJoinStyle]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520726-linejoinstyle)Removed [-[NSBezierPath lineWidth]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520655-linewidth)Removed [-[NSBezierPath miterLimit]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520740-miterlimit)Removed [-[NSBezierPath setFlatness:]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520676-flatness)Removed [-[NSBezierPath setLineCapStyle:]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520667-linecapstyle)Removed [-[NSBezierPath setLineJoinStyle:]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520726-linejoinstyle)Removed [-[NSBezierPath setLineWidth:]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520655-linewidth)Removed [-[NSBezierPath setMiterLimit:]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520740-miterlimit)Removed [-[NSBezierPath setWindingRule:]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520657-windingrule)Removed [-[NSBezierPath windingRule]](https://developer.apple.com/documentation/appkit/nsbezierpath/1520657-windingrule)Added [NSBezierPath.bezierPathByFlatteningPath](https://developer.apple.com/documentation/appkit/nsbezierpath/1520733-bezierpathbyflatteningpath)Added [NSBezierPath.bezierPathByReversingPath](https://developer.apple.com/documentation/appkit/nsbezierpath/1520656-bezierpathbyreversingpath)Added [NSBezierPath.bounds](https://developer.apple.com/documentation/appkit/nsbezierpath/1520722-bounds)Added [NSBezierPath.controlPointBounds](https://developer.apple.com/documentation/appkit/nsbezierpath/1520654-controlpointbounds)Added [NSBezierPath.currentPoint](https://developer.apple.com/documentation/appkit/nsbezierpath/1520698-currentpoint)Added [NSBezierPath.elementCount](https://developer.apple.com/documentation/appkit/nsbezierpath/1520645-elementcount)Added [NSBezierPath.empty](https://developer.apple.com/documentation/appkit/nsbezierpath/1520712-isempty)Added [NSBezierPath.flatness](https://developer.apple.com/documentation/appkit/nsbezierpath/1520676-flatness)Added [NSBezierPath.lineCapStyle](https://developer.apple.com/documentation/appkit/nsbezierpath/1520667-linecapstyle)Added [NSBezierPath.lineJoinStyle](https://developer.apple.com/documentation/appkit/nsbezierpath/1520726-linejoinstyle)Added [NSBezierPath.lineWidth](https://developer.apple.com/documentation/appkit/nsbezierpath/1520655-linewidth)Added [NSBezierPath.miterLimit](https://developer.apple.com/documentation/appkit/nsbezierpath/1520740-miterlimit)Added [NSBezierPath.windingRule](https://developer.apple.com/documentation/appkit/nsbezierpath/1520657-windingrule)NSBitmapImageRep.hRemoved [-[NSBitmapImageRep CGImage]](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395506-cgimage)Removed [-[NSBitmapImageRep TIFFRepresentation]](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395557-tiffrepresentation)Removed [-[NSBitmapImageRep bitmapData]](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395421-bitmapdata)Removed [-[NSBitmapImageRep bitmapFormat]](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395508-bitmapformat)Removed [-[NSBitmapImageRep bitsPerPixel]](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395488-bitsperpixel)Removed [-[NSBitmapImageRep bytesPerPlane]](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395559-bytesperplane)Removed [-[NSBitmapImageRep bytesPerRow]](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395454-bytesperrow)Removed [-[NSBitmapImageRep colorSpace]](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395468-colorspace)Removed [-[NSBitmapImageRep isPlanar]](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395482-planar)Removed [-[NSBitmapImageRep numberOfPlanes]](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395474-numberofplanes)Removed [-[NSBitmapImageRep samplesPerPixel]](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395577-samplesperpixel)Added [NSBitmapImageRep.CGImage](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395506-cgimage)Added [NSBitmapImageRep.TIFFRepresentation](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395557-tiffrepresentation)Added [NSBitmapImageRep.bitmapData](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395421-bitmapdata)Added [NSBitmapImageRep.bitmapFormat](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395508-bitmapformat)Added [NSBitmapImageRep.bitsPerPixel](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395488-bitsperpixel)Added [NSBitmapImageRep.bytesPerPlane](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395559-bytesperplane)Added [NSBitmapImageRep.bytesPerRow](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395454-bytesperrow)Added [NSBitmapImageRep.colorSpace](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395468-colorspace)Added [NSBitmapImageRep.numberOfPlanes](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395474-numberofplanes)Added [NSBitmapImageRep.planar](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395482-isplanar)Added [NSBitmapImageRep.samplesPerPixel](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395577-samplesperpixel)Added [NS16BitBigEndianBitmapFormat](https://developer.apple.com/documentation/appkit/ns16bitbigendianbitmapformat)Added [NS16BitLittleEndianBitmapFormat](https://developer.apple.com/documentation/appkit/ns16bitlittleendianbitmapformat)Added [NS32BitBigEndianBitmapFormat](https://developer.apple.com/documentation/appkit/ns32bitbigendianbitmapformat)Added [NS32BitLittleEndianBitmapFormat](https://developer.apple.com/documentation/appkit/ns32bitlittleendianbitmapformat)Modified [NSBitmapImageRep](https://developer.apple.com/documentation/appkit/nsbitmapimagerep)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSSecureCoding |

Modified [+[NSBitmapImageRep imageRepWithData:]](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395502-imagerepwithdata)

|  | Declaration |
| --- | --- |
| From | ``` + (id)imageRepWithData:(NSData *)data ``` |
| To | ``` + (instancetype)imageRepWithData:(NSData *)data ``` |

Modified [-[NSBitmapImageRep initForIncrementalLoad]](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395522-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initForIncrementalLoad ``` |
| To | ``` - (instancetype)initForIncrementalLoad ``` |

Modified [-[NSBitmapImageRep initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bitmapFormat:bytesPerRow:bitsPerPixel:]](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395538-initwithbitmapdataplanes)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithBitmapDataPlanes:(unsigned char **)planes pixelsWide:(NSInteger)width pixelsHigh:(NSInteger)height bitsPerSample:(NSInteger)bps samplesPerPixel:(NSInteger)spp hasAlpha:(BOOL)alpha isPlanar:(BOOL)isPlanar colorSpaceName:(NSString *)colorSpaceName bitmapFormat:(NSBitmapFormat)bitmapFormat bytesPerRow:(NSInteger)rBytes bitsPerPixel:(NSInteger)pBits ``` |
| To | ``` - (instancetype)initWithBitmapDataPlanes:(unsigned char **)planes pixelsWide:(NSInteger)width pixelsHigh:(NSInteger)height bitsPerSample:(NSInteger)bps samplesPerPixel:(NSInteger)spp hasAlpha:(BOOL)alpha isPlanar:(BOOL)isPlanar colorSpaceName:(NSString *)colorSpaceName bitmapFormat:(NSBitmapFormat)bitmapFormat bytesPerRow:(NSInteger)rBytes bitsPerPixel:(NSInteger)pBits ``` |

Modified [-[NSBitmapImageRep initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bytesPerRow:bitsPerPixel:]](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395540-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithBitmapDataPlanes:(unsigned char **)planes pixelsWide:(NSInteger)width pixelsHigh:(NSInteger)height bitsPerSample:(NSInteger)bps samplesPerPixel:(NSInteger)spp hasAlpha:(BOOL)alpha isPlanar:(BOOL)isPlanar colorSpaceName:(NSString *)colorSpaceName bytesPerRow:(NSInteger)rBytes bitsPerPixel:(NSInteger)pBits ``` |
| To | ``` - (instancetype)initWithBitmapDataPlanes:(unsigned char **)planes pixelsWide:(NSInteger)width pixelsHigh:(NSInteger)height bitsPerSample:(NSInteger)bps samplesPerPixel:(NSInteger)spp hasAlpha:(BOOL)alpha isPlanar:(BOOL)isPlanar colorSpaceName:(NSString *)colorSpaceName bytesPerRow:(NSInteger)rBytes bitsPerPixel:(NSInteger)pBits ``` |

Modified [-[NSBitmapImageRep initWithCGImage:]](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395423-initwithcgimage)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCGImage:(CGImageRef)cgImage ``` |
| To | ``` - (instancetype)initWithCGImage:(CGImageRef)cgImage ``` |

Modified [-[NSBitmapImageRep initWithCIImage:]](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395587-initwithciimage)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCIImage:(CIImage *)ciImage ``` |
| To | ``` - (instancetype)initWithCIImage:(CIImage *)ciImage ``` |

Modified [-[NSBitmapImageRep initWithData:]](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395569-initwithdata)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(NSData *)data ``` |
| To | ``` - (instancetype)initWithData:(NSData *)data ``` |

Modified [-[NSBitmapImageRep initWithFocusedViewRect:]](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/1395550-initwithfocusedviewrect)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFocusedViewRect:(NSRect)rect ``` |
| To | ``` - (instancetype)initWithFocusedViewRect:(NSRect)rect ``` |

NSBox.hRemoved [-[NSBox borderColor]](https://developer.apple.com/documentation/appkit/nsbox/1429839-bordercolor)Removed [-[NSBox borderRect]](https://developer.apple.com/documentation/appkit/nsbox/1429787-borderrect)Removed [-[NSBox borderType]](https://developer.apple.com/documentation/appkit/nsbox/1429802-bordertype)Removed [-[NSBox borderWidth]](https://developer.apple.com/documentation/appkit/nsbox/1429831-borderwidth)Removed [-[NSBox boxType]](https://developer.apple.com/documentation/appkit/nsbox/1429822-boxtype)Removed [-[NSBox contentView]](https://developer.apple.com/documentation/appkit/nsbox/1429818-contentview)Removed [-[NSBox contentViewMargins]](https://developer.apple.com/documentation/appkit/nsbox/1429837-contentviewmargins)Removed [-[NSBox cornerRadius]](https://developer.apple.com/documentation/appkit/nsbox/1429812-cornerradius)Removed [-[NSBox fillColor]](https://developer.apple.com/documentation/appkit/nsbox/1429797-fillcolor)Removed [-[NSBox isTransparent]](https://developer.apple.com/documentation/appkit/nsbox/1429821-transparent)Removed [-[NSBox setBorderColor:]](https://developer.apple.com/documentation/appkit/nsbox/1429839-bordercolor)Removed [-[NSBox setBorderType:]](https://developer.apple.com/documentation/appkit/nsbox/1429802-bordertype)Removed [-[NSBox setBorderWidth:]](https://developer.apple.com/documentation/appkit/nsbox/1429831-borderwidth)Removed [-[NSBox setBoxType:]](https://developer.apple.com/documentation/appkit/nsbox/1429822-boxtype)Removed [-[NSBox setContentView:]](https://developer.apple.com/documentation/appkit/nsbox/1429818-contentview)Removed [-[NSBox setContentViewMargins:]](https://developer.apple.com/documentation/appkit/nsbox/1429837-contentviewmargins)Removed [-[NSBox setCornerRadius:]](https://developer.apple.com/documentation/appkit/nsbox/1429812-cornerradius)Removed [-[NSBox setFillColor:]](https://developer.apple.com/documentation/appkit/nsbox/1429797-fillcolor)Removed [-[NSBox setTitle:]](https://developer.apple.com/documentation/appkit/nsbox/1429795-title)Removed [-[NSBox setTitleFont:]](https://developer.apple.com/documentation/appkit/nsbox/1429791-titlefont)Removed [-[NSBox setTitlePosition:]](https://developer.apple.com/documentation/appkit/nsbox/1429844-titleposition)Removed [-[NSBox setTransparent:]](https://developer.apple.com/documentation/appkit/nsbox/1429821-transparent)Removed [-[NSBox title]](https://developer.apple.com/documentation/appkit/nsbox/1429795-title)Removed [-[NSBox titleCell]](https://developer.apple.com/documentation/appkit/nsbox/1429789-titlecell)Removed [-[NSBox titleFont]](https://developer.apple.com/documentation/appkit/nsbox/1429791-titlefont)Removed [-[NSBox titlePosition]](https://developer.apple.com/documentation/appkit/nsbox/1429844-titleposition)Removed [-[NSBox titleRect]](https://developer.apple.com/documentation/appkit/nsbox/1429785-titlerect)Added [NSBox.borderColor](https://developer.apple.com/documentation/appkit/nsbox/1429839-bordercolor)Added [NSBox.borderRect](https://developer.apple.com/documentation/appkit/nsbox/1429787-borderrect)Added [NSBox.borderType](https://developer.apple.com/documentation/appkit/nsbox/1429802-bordertype)Added [NSBox.borderWidth](https://developer.apple.com/documentation/appkit/nsbox/1429831-borderwidth)Added [NSBox.boxType](https://developer.apple.com/documentation/appkit/nsbox/1429822-boxtype)Added [NSBox.contentView](https://developer.apple.com/documentation/appkit/nsbox/1429818-contentview)Added [NSBox.contentViewMargins](https://developer.apple.com/documentation/appkit/nsbox/1429837-contentviewmargins)Added [NSBox.cornerRadius](https://developer.apple.com/documentation/appkit/nsbox/1429812-cornerradius)Added [NSBox.fillColor](https://developer.apple.com/documentation/appkit/nsbox/1429797-fillcolor)Added [NSBox.title](https://developer.apple.com/documentation/appkit/nsbox/1429795-title)Added [NSBox.titleCell](https://developer.apple.com/documentation/appkit/nsbox/1429789-titlecell)Added [NSBox.titleFont](https://developer.apple.com/documentation/appkit/nsbox/1429791-titlefont)Added [NSBox.titlePosition](https://developer.apple.com/documentation/appkit/nsbox/1429844-titleposition)Added [NSBox.titleRect](https://developer.apple.com/documentation/appkit/nsbox/1429785-titlerect)Added [NSBox.transparent](https://developer.apple.com/documentation/appkit/nsbox/1429821-istransparent)NSBrowser.hRemoved [-[NSBrowser allowsBranchSelection]](https://developer.apple.com/documentation/appkit/nsbrowser/1407796-allowsbranchselection)Removed [-[NSBrowser allowsEmptySelection]](https://developer.apple.com/documentation/appkit/nsbrowser/1407585-allowsemptyselection)Removed [-[NSBrowser allowsMultipleSelection]](https://developer.apple.com/documentation/appkit/nsbrowser/1407509-allowsmultipleselection)Removed [-[NSBrowser allowsTypeSelect]](https://developer.apple.com/documentation/appkit/nsbrowser/1407682-allowstypeselect)Removed [-[NSBrowser autohidesScroller]](https://developer.apple.com/documentation/appkit/nsbrowser/1407696-autohidesscroller)Removed [-[NSBrowser backgroundColor]](https://developer.apple.com/documentation/appkit/nsbrowser/1407520-backgroundcolor)Removed [-[NSBrowser cellPrototype]](https://developer.apple.com/documentation/appkit/nsbrowser/1407662-cellprototype)Removed [-[NSBrowser clickedColumn]](https://developer.apple.com/documentation/appkit/nsbrowser/1407590-clickedcolumn)Removed [-[NSBrowser clickedRow]](https://developer.apple.com/documentation/appkit/nsbrowser/1407671-clickedrow)Removed [-[NSBrowser columnResizingType]](https://developer.apple.com/documentation/appkit/nsbrowser/1407694-columnresizingtype)Removed [-[NSBrowser columnsAutosaveName]](https://developer.apple.com/documentation/appkit/nsbrowser/1407650-columnsautosavename)Removed [-[NSBrowser delegate]](https://developer.apple.com/documentation/appkit/nsbrowser/1407686-delegate)Removed [-[NSBrowser doubleAction]](https://developer.apple.com/documentation/appkit/nsbrowser/1407698-doubleaction)Removed [-[NSBrowser firstVisibleColumn]](https://developer.apple.com/documentation/appkit/nsbrowser/1407703-firstvisiblecolumn)Removed [-[NSBrowser hasHorizontalScroller]](https://developer.apple.com/documentation/appkit/nsbrowser/1407551-hashorizontalscroller)Removed [-[NSBrowser isLoaded]](https://developer.apple.com/documentation/appkit/nsbrowser/1407758-loaded)Removed [-[NSBrowser isTitled]](https://developer.apple.com/documentation/appkit/nsbrowser/1407735-titled)Removed [-[NSBrowser lastColumn]](https://developer.apple.com/documentation/appkit/nsbrowser/1407715-lastcolumn)Removed [-[NSBrowser lastVisibleColumn]](https://developer.apple.com/documentation/appkit/nsbrowser/1407610-lastvisiblecolumn)Removed [-[NSBrowser maxVisibleColumns]](https://developer.apple.com/documentation/appkit/nsbrowser/1407749-maxvisiblecolumns)Removed [-[NSBrowser minColumnWidth]](https://developer.apple.com/documentation/appkit/nsbrowser/1407513-mincolumnwidth)Removed [-[NSBrowser numberOfVisibleColumns]](https://developer.apple.com/documentation/appkit/nsbrowser/1407700-numberofvisiblecolumns)Removed [-[NSBrowser pathSeparator]](https://developer.apple.com/documentation/appkit/nsbrowser/1407688-pathseparator)Removed [-[NSBrowser prefersAllColumnUserResizing]](https://developer.apple.com/documentation/appkit/nsbrowser/1407690-prefersallcolumnuserresizing)Removed [-[NSBrowser reusesColumns]](https://developer.apple.com/documentation/appkit/nsbrowser/1407792-reusescolumns)Removed [-[NSBrowser rowHeight]](https://developer.apple.com/documentation/appkit/nsbrowser/1407642-rowheight)Removed [-[NSBrowser selectedCell]](https://developer.apple.com/documentation/appkit/nsbrowser/1407730-selectedcell)Removed [-[NSBrowser selectedCells]](https://developer.apple.com/documentation/appkit/nsbrowser/1407588-selectedcells)Removed [-[NSBrowser selectedColumn]](https://developer.apple.com/documentation/appkit/nsbrowser/1407568-selectedcolumn)Removed [-[NSBrowser selectionIndexPath]](https://developer.apple.com/documentation/appkit/nsbrowser/1407507-selectionindexpath)Removed [-[NSBrowser selectionIndexPaths]](https://developer.apple.com/documentation/appkit/nsbrowser/1407536-selectionindexpaths)Removed [-[NSBrowser sendAction]](https://developer.apple.com/documentation/appkit/nsbrowser/1407675-sendaction)Removed [-[NSBrowser sendsActionOnArrowKeys]](https://developer.apple.com/documentation/appkit/nsbrowser/1407614-sendsactiononarrowkeys)Removed [-[NSBrowser separatesColumns]](https://developer.apple.com/documentation/appkit/nsbrowser/1407653-separatescolumns)Removed [-[NSBrowser setAllowsBranchSelection:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407796-allowsbranchselection)Removed [-[NSBrowser setAllowsEmptySelection:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407585-allowsemptyselection)Removed [-[NSBrowser setAllowsMultipleSelection:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407509-allowsmultipleselection)Removed [-[NSBrowser setAllowsTypeSelect:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407682-allowstypeselect)Removed [-[NSBrowser setAutohidesScroller:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407696-autohidesscroller)Removed [-[NSBrowser setBackgroundColor:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407520-backgroundcolor)Removed [-[NSBrowser setCellPrototype:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407662-cellprototype)Removed [-[NSBrowser setColumnResizingType:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407694-columnresizingtype)Removed [-[NSBrowser setColumnsAutosaveName:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407650-columnsautosavename)Removed [-[NSBrowser setDelegate:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407686-delegate)Removed [-[NSBrowser setDoubleAction:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407698-doubleaction)Removed [-[NSBrowser setHasHorizontalScroller:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407551-hashorizontalscroller)Removed [-[NSBrowser setLastColumn:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407715-lastcolumn)Removed [-[NSBrowser setMaxVisibleColumns:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407749-maxvisiblecolumns)Removed [-[NSBrowser setMinColumnWidth:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407513-mincolumnwidth)Removed [-[NSBrowser setPathSeparator:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407688-pathseparator)Removed [-[NSBrowser setPrefersAllColumnUserResizing:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407690-prefersallcolumnuserresizing)Removed [-[NSBrowser setReusesColumns:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407792-reusescolumns)Removed [-[NSBrowser setRowHeight:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407642-rowheight)Removed [-[NSBrowser setSelectionIndexPath:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407507-selectionindexpath)Removed [-[NSBrowser setSelectionIndexPaths:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407536-selectionindexpaths)Removed [-[NSBrowser setSendsActionOnArrowKeys:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407614-sendsactiononarrowkeys)Removed [-[NSBrowser setSeparatesColumns:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407653-separatescolumns)Removed [-[NSBrowser setTakesTitleFromPreviousColumn:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407564-takestitlefrompreviouscolumn)Removed [-[NSBrowser setTitled:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407735-titled)Removed [-[NSBrowser takesTitleFromPreviousColumn]](https://developer.apple.com/documentation/appkit/nsbrowser/1407564-takestitlefrompreviouscolumn)Removed [-[NSBrowser titleHeight]](https://developer.apple.com/documentation/appkit/nsbrowser/1407709-titleheight)Added [NSBrowser.allowsBranchSelection](https://developer.apple.com/documentation/appkit/nsbrowser/1407796-allowsbranchselection)Added [NSBrowser.allowsEmptySelection](https://developer.apple.com/documentation/appkit/nsbrowser/1407585-allowsemptyselection)Added [NSBrowser.allowsMultipleSelection](https://developer.apple.com/documentation/appkit/nsbrowser/1407509-allowsmultipleselection)Added [NSBrowser.allowsTypeSelect](https://developer.apple.com/documentation/appkit/nsbrowser/1407682-allowstypeselect)Added [NSBrowser.autohidesScroller](https://developer.apple.com/documentation/appkit/nsbrowser/1407696-autohidesscroller)Added [NSBrowser.backgroundColor](https://developer.apple.com/documentation/appkit/nsbrowser/1407520-backgroundcolor)Added [NSBrowser.cellPrototype](https://developer.apple.com/documentation/appkit/nsbrowser/1407662-cellprototype)Added [NSBrowser.clickedColumn](https://developer.apple.com/documentation/appkit/nsbrowser/1407590-clickedcolumn)Added [NSBrowser.clickedRow](https://developer.apple.com/documentation/appkit/nsbrowser/1407671-clickedrow)Added [NSBrowser.columnResizingType](https://developer.apple.com/documentation/appkit/nsbrowser/1407694-columnresizingtype)Added [NSBrowser.columnsAutosaveName](https://developer.apple.com/documentation/appkit/nsbrowser/1407650-columnsautosavename)Added [NSBrowser.delegate](https://developer.apple.com/documentation/appkit/nsbrowser/1407686-delegate)Added [NSBrowser.doubleAction](https://developer.apple.com/documentation/appkit/nsbrowser/1407698-doubleaction)Added [NSBrowser.firstVisibleColumn](https://developer.apple.com/documentation/appkit/nsbrowser/1407703-firstvisiblecolumn)Added [NSBrowser.hasHorizontalScroller](https://developer.apple.com/documentation/appkit/nsbrowser/1407551-hashorizontalscroller)Added [NSBrowser.lastColumn](https://developer.apple.com/documentation/appkit/nsbrowser/1407715-lastcolumn)Added [NSBrowser.lastVisibleColumn](https://developer.apple.com/documentation/appkit/nsbrowser/1407610-lastvisiblecolumn)Added [NSBrowser.loaded](https://developer.apple.com/documentation/appkit/nsbrowser/1407758-loaded)Added [NSBrowser.maxVisibleColumns](https://developer.apple.com/documentation/appkit/nsbrowser/1407749-maxvisiblecolumns)Added [NSBrowser.minColumnWidth](https://developer.apple.com/documentation/appkit/nsbrowser/1407513-mincolumnwidth)Added [NSBrowser.numberOfVisibleColumns](https://developer.apple.com/documentation/appkit/nsbrowser/1407700-numberofvisiblecolumns)Added [NSBrowser.pathSeparator](https://developer.apple.com/documentation/appkit/nsbrowser/1407688-pathseparator)Added [NSBrowser.prefersAllColumnUserResizing](https://developer.apple.com/documentation/appkit/nsbrowser/1407690-prefersallcolumnuserresizing)Added [NSBrowser.reusesColumns](https://developer.apple.com/documentation/appkit/nsbrowser/1407792-reusescolumns)Added [NSBrowser.rowHeight](https://developer.apple.com/documentation/appkit/nsbrowser/1407642-rowheight)Added [NSBrowser.selectedCell](https://developer.apple.com/documentation/appkit/nsbrowser/1407730-selectedcell)Added [NSBrowser.selectedCells](https://developer.apple.com/documentation/appkit/nsbrowser/1407588-selectedcells)Added [NSBrowser.selectedColumn](https://developer.apple.com/documentation/appkit/nsbrowser/1407568-selectedcolumn)Added [NSBrowser.selectionIndexPath](https://developer.apple.com/documentation/appkit/nsbrowser/1407507-selectionindexpath)Added [NSBrowser.selectionIndexPaths](https://developer.apple.com/documentation/appkit/nsbrowser/1407536-selectionindexpaths)Added NSBrowser.sendActionAdded [NSBrowser.sendsActionOnArrowKeys](https://developer.apple.com/documentation/appkit/nsbrowser/1407614-sendsactiononarrowkeys)Added [NSBrowser.separatesColumns](https://developer.apple.com/documentation/appkit/nsbrowser/1407653-separatescolumns)Added [NSBrowser.takesTitleFromPreviousColumn](https://developer.apple.com/documentation/appkit/nsbrowser/1407564-takestitlefrompreviouscolumn)Added [NSBrowser.titleHeight](https://developer.apple.com/documentation/appkit/nsbrowser/1407709-titleheight)Added [NSBrowser.titled](https://developer.apple.com/documentation/appkit/nsbrowser/1407735-titled)Modified [-[NSBrowser columnOfMatrix:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407640-columnofmatrix)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSBrowser matrixClass]](https://developer.apple.com/documentation/appkit/nsbrowser/1407790-matrixclass)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSBrowser matrixInColumn:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407573-matrix)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSBrowser setMatrixClass:]](https://developer.apple.com/documentation/appkit/nsbrowser/1407711-setmatrixclass)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSBrowserDelegate browser:acceptDrop:atRow:column:dropOperation:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407737-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:canDragRowsWithIndexes:inColumn:withEvent:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407768-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:child:ofItem:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407572-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:createRowsForColumn:inMatrix:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407666-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:didChangeLastColumn:toColumn:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407612-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:draggingImageForRowsWithIndexes:inColumn:withEvent:offset:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407598-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:headerViewControllerForItem:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407782-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:heightOfRow:inColumn:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407646-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:isColumnValid:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407540-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:isLeafItem:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407786-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:namesOfPromisedFilesDroppedAtDestination:forDraggedRowsWithIndexes:inColumn:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407624-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:nextTypeSelectMatchFromRow:toRow:inColumn:forString:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407553-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:numberOfChildrenOfItem:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407755-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:numberOfRowsInColumn:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407583-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:objectValueForItem:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407594-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:previewViewControllerForLeafItem:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407772-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:selectCellWithString:inColumn:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407548-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:selectRow:inColumn:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407802-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:selectionIndexesForProposedSelection:inColumn:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407660-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:setObjectValue:forItem:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407756-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:shouldEditItem:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407634-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:shouldShowCellExpansionForRow:column:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407602-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:shouldSizeColumn:forUserResize:toWidth:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407557-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:shouldTypeSelectForEvent:withCurrentSearchString:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407804-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:sizeToFitWidthOfColumn:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407524-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:titleOfColumn:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407677-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:typeSelectStringForRow:inColumn:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407762-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:validateDrop:proposedRow:column:dropOperation:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407766-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:willDisplayCell:atRow:column:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407705-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browser:writeRowsWithIndexes:inColumn:toPasteboard:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407657-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browserColumnConfigurationDidChange:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407542-browsercolumnconfigurationdidcha)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browserDidScroll:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407566-browserdidscroll)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate browserWillScroll:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407721-browserwillscroll)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBrowserDelegate rootItemForBrowser:]](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/1407526-rootitem)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSBrowserCell.hRemoved [-[NSBrowserCell alternateImage]](https://developer.apple.com/documentation/appkit/nsbrowsercell/1435768-alternateimage)Removed [-[NSBrowserCell image]](https://developer.apple.com/documentation/appkit/nsbrowsercell/1435766-image)Removed [-[NSBrowserCell isLeaf]](https://developer.apple.com/documentation/appkit/nsbrowsercell/1435771-isleaf)Removed [-[NSBrowserCell isLoaded]](https://developer.apple.com/documentation/appkit/nsbrowsercell/1435772-isloaded)Removed [-[NSBrowserCell setAlternateImage:]](https://developer.apple.com/documentation/appkit/nsbrowsercell/1435768-alternateimage)Removed [-[NSBrowserCell setImage:]](https://developer.apple.com/documentation/appkit/nsbrowsercell/1435766-image)Removed [-[NSBrowserCell setLeaf:]](https://developer.apple.com/documentation/appkit/nsbrowsercell/1435771-isleaf)Removed [-[NSBrowserCell setLoaded:]](https://developer.apple.com/documentation/appkit/nsbrowsercell/1435772-loaded)Added [NSBrowserCell.alternateImage](https://developer.apple.com/documentation/appkit/nsbrowsercell/1435768-alternateimage)Added [NSBrowserCell.image](https://developer.apple.com/documentation/appkit/nsbrowsercell/1435766-image)Added [NSBrowserCell.leaf](https://developer.apple.com/documentation/appkit/nsbrowsercell/1435771-isleaf)Added [NSBrowserCell.loaded](https://developer.apple.com/documentation/appkit/nsbrowsercell/1435772-loaded)NSButton.hRemoved [-[NSButton allowsMixedState]](https://developer.apple.com/documentation/appkit/nsbutton/1528670-allowsmixedstate)Removed [-[NSButton alternateImage]](https://developer.apple.com/documentation/appkit/nsbutton/1533935-alternateimage)Removed [-[NSButton alternateTitle]](https://developer.apple.com/documentation/appkit/nsbutton/1529588-alternatetitle)Removed [-[NSButton attributedAlternateTitle]](https://developer.apple.com/documentation/appkit/nsbutton/1526723-attributedalternatetitle)Removed [-[NSButton attributedTitle]](https://developer.apple.com/documentation/appkit/nsbutton/1524640-attributedtitle)Removed [-[NSButton bezelStyle]](https://developer.apple.com/documentation/appkit/nsbutton/1527022-bezelstyle)Removed [-[NSButton image]](https://developer.apple.com/documentation/appkit/nsbutton/1534221-image)Removed [-[NSButton imagePosition]](https://developer.apple.com/documentation/appkit/nsbutton/1526778-imageposition)Removed -[NSButton isBordered]Removed -[NSButton isTransparent]Removed [-[NSButton keyEquivalent]](https://developer.apple.com/documentation/appkit/nsbutton/1525368-keyequivalent)Removed [-[NSButton keyEquivalentModifierMask]](https://developer.apple.com/documentation/appkit/nsbutton/1532670-keyequivalentmodifiermask)Removed [-[NSButton setAllowsMixedState:]](https://developer.apple.com/documentation/appkit/nsbutton/1528670-allowsmixedstate)Removed [-[NSButton setAlternateImage:]](https://developer.apple.com/documentation/appkit/nsbutton/1533935-alternateimage)Removed [-[NSButton setAlternateTitle:]](https://developer.apple.com/documentation/appkit/nsbutton/1529588-alternatetitle)Removed [-[NSButton setAttributedAlternateTitle:]](https://developer.apple.com/documentation/appkit/nsbutton/1526723-attributedalternatetitle)Removed [-[NSButton setAttributedTitle:]](https://developer.apple.com/documentation/appkit/nsbutton/1524640-attributedtitle)Removed [-[NSButton setBezelStyle:]](https://developer.apple.com/documentation/appkit/nsbutton/1527022-bezelstyle)Removed [-[NSButton setBordered:]](https://developer.apple.com/documentation/appkit/nsbutton/1525565-bordered)Removed [-[NSButton setImage:]](https://developer.apple.com/documentation/appkit/nsbutton/1534221-image)Removed [-[NSButton setImagePosition:]](https://developer.apple.com/documentation/appkit/nsbutton/1526778-imageposition)Removed [-[NSButton setKeyEquivalent:]](https://developer.apple.com/documentation/appkit/nsbutton/1525368-keyequivalent)Removed [-[NSButton setKeyEquivalentModifierMask:]](https://developer.apple.com/documentation/appkit/nsbutton/1532670-keyequivalentmodifiermask)Removed [-[NSButton setShowsBorderOnlyWhileMouseInside:]](https://developer.apple.com/documentation/appkit/nsbutton/1532248-showsborderonlywhilemouseinside)Removed [-[NSButton setSound:]](https://developer.apple.com/documentation/appkit/nsbutton/1530910-sound)Removed [-[NSButton setState:]](https://developer.apple.com/documentation/appkit/nsbutton/1528907-state)Removed [-[NSButton setTitle:]](https://developer.apple.com/documentation/appkit/nsbutton/1524430-title)Removed [-[NSButton setTransparent:]](https://developer.apple.com/documentation/appkit/nsbutton/1529659-transparent)Removed [-[NSButton showsBorderOnlyWhileMouseInside]](https://developer.apple.com/documentation/appkit/nsbutton/1532248-showsborderonlywhilemouseinside)Removed [-[NSButton sound]](https://developer.apple.com/documentation/appkit/nsbutton/1530910-sound)Removed [-[NSButton state]](https://developer.apple.com/documentation/appkit/nsbutton/1528907-state)Removed [-[NSButton title]](https://developer.apple.com/documentation/appkit/nsbutton/1524430-title)Added [NSButton.allowsMixedState](https://developer.apple.com/documentation/appkit/nsbutton/1528670-allowsmixedstate)Added [NSButton.alternateImage](https://developer.apple.com/documentation/appkit/nsbutton/1533935-alternateimage)Added [NSButton.alternateTitle](https://developer.apple.com/documentation/appkit/nsbutton/1529588-alternatetitle)Added [NSButton.attributedAlternateTitle](https://developer.apple.com/documentation/appkit/nsbutton/1526723-attributedalternatetitle)Added [NSButton.attributedTitle](https://developer.apple.com/documentation/appkit/nsbutton/1524640-attributedtitle)Added [NSButton.bezelStyle](https://developer.apple.com/documentation/appkit/nsbutton/1527022-bezelstyle)Added [NSButton.bordered](https://developer.apple.com/documentation/appkit/nsbutton/1525565-isbordered)Added [NSButton.image](https://developer.apple.com/documentation/appkit/nsbutton/1534221-image)Added [NSButton.imagePosition](https://developer.apple.com/documentation/appkit/nsbutton/1526778-imageposition)Added [NSButton.keyEquivalent](https://developer.apple.com/documentation/appkit/nsbutton/1525368-keyequivalent)Added [NSButton.keyEquivalentModifierMask](https://developer.apple.com/documentation/appkit/nsbutton/1532670-keyequivalentmodifiermask)Added [NSButton.showsBorderOnlyWhileMouseInside](https://developer.apple.com/documentation/appkit/nsbutton/1532248-showsborderonlywhilemouseinside)Added [NSButton.sound](https://developer.apple.com/documentation/appkit/nsbutton/1530910-sound)Added [NSButton.state](https://developer.apple.com/documentation/appkit/nsbutton/1528907-state)Added [NSButton.title](https://developer.apple.com/documentation/appkit/nsbutton/1524430-title)Added [NSButton.transparent](https://developer.apple.com/documentation/appkit/nsbutton/1529659-istransparent)Modified [NSButton](https://developer.apple.com/documentation/appkit/nsbutton)

|  | Protocols |
| --- | --- |
| From | NSUserInterfaceValidations |
| To | NSAccessibilityButton, NSUserInterfaceValidations |

NSButtonCell.hRemoved [-[NSButtonCell alternateImage]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1527064-alternateimage)Removed [-[NSButtonCell alternateTitle]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1535382-alternatetitle)Removed [-[NSButtonCell attributedAlternateTitle]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1526922-attributedalternatetitle)Removed [-[NSButtonCell attributedTitle]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1529303-attributedtitle)Removed [-[NSButtonCell backgroundColor]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1529743-backgroundcolor)Removed [-[NSButtonCell bezelStyle]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1528696-bezelstyle)Removed [-[NSButtonCell gradientType]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1532259-gradienttype)Removed [-[NSButtonCell highlightsBy]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1528459-highlightsby)Removed [-[NSButtonCell imageDimsWhenDisabled]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1534152-imagedimswhendisabled)Removed [-[NSButtonCell imagePosition]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1529593-imageposition)Removed [-[NSButtonCell imageScaling]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1535104-imagescaling)Removed [-[NSButtonCell isOpaque]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1533667-opaque)Removed [-[NSButtonCell isTransparent]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1530887-transparent)Removed [-[NSButtonCell keyEquivalent]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1529476-keyequivalent)Removed [-[NSButtonCell keyEquivalentFont]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1531184-keyequivalentfont)Removed [-[NSButtonCell keyEquivalentModifierMask]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1528315-keyequivalentmodifiermask)Removed [-[NSButtonCell setAlternateImage:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1527064-alternateimage)Removed [-[NSButtonCell setAlternateTitle:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1535382-alternatetitle)Removed [-[NSButtonCell setAttributedAlternateTitle:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1526922-attributedalternatetitle)Removed [-[NSButtonCell setAttributedTitle:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1529303-attributedtitle)Removed [-[NSButtonCell setBackgroundColor:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1529743-backgroundcolor)Removed [-[NSButtonCell setBezelStyle:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1528696-bezelstyle)Removed [-[NSButtonCell setFont:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1806988-setfont)Removed [-[NSButtonCell setGradientType:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1532259-gradienttype)Removed [-[NSButtonCell setHighlightsBy:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1528459-highlightsby)Removed [-[NSButtonCell setImageDimsWhenDisabled:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1534152-imagedimswhendisabled)Removed [-[NSButtonCell setImagePosition:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1529593-imageposition)Removed [-[NSButtonCell setImageScaling:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1535104-imagescaling)Removed [-[NSButtonCell setKeyEquivalent:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1529476-keyequivalent)Removed [-[NSButtonCell setKeyEquivalentFont:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1531184-keyequivalentfont)Removed [-[NSButtonCell setKeyEquivalentModifierMask:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1528315-keyequivalentmodifiermask)Removed [-[NSButtonCell setShowsBorderOnlyWhileMouseInside:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1527903-showsborderonlywhilemouseinside)Removed [-[NSButtonCell setShowsStateBy:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1533225-showsstateby)Removed [-[NSButtonCell setSound:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1525955-sound)Removed [-[NSButtonCell setTitle:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1535916-title)Removed [-[NSButtonCell setTransparent:]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1530887-transparent)Removed [-[NSButtonCell showsBorderOnlyWhileMouseInside]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1527903-showsborderonlywhilemouseinside)Removed [-[NSButtonCell showsStateBy]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1533225-showsstateby)Removed [-[NSButtonCell sound]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1525955-sound)Removed [-[NSButtonCell title]](https://developer.apple.com/documentation/appkit/nsbuttoncell/1535916-title)Added [NSButtonCell.alternateImage](https://developer.apple.com/documentation/appkit/nsbuttoncell/1527064-alternateimage)Added [NSButtonCell.alternateTitle](https://developer.apple.com/documentation/appkit/nsbuttoncell/1535382-alternatetitle)Added [NSButtonCell.attributedAlternateTitle](https://developer.apple.com/documentation/appkit/nsbuttoncell/1526922-attributedalternatetitle)Added [NSButtonCell.attributedTitle](https://developer.apple.com/documentation/appkit/nsbuttoncell/1529303-attributedtitle)Added [NSButtonCell.backgroundColor](https://developer.apple.com/documentation/appkit/nsbuttoncell/1529743-backgroundcolor)Added [NSButtonCell.bezelStyle](https://developer.apple.com/documentation/appkit/nsbuttoncell/1528696-bezelstyle)Added [NSButtonCell.gradientType](https://developer.apple.com/documentation/appkit/nsbuttoncell/1532259-gradienttype)Added [NSButtonCell.highlightsBy](https://developer.apple.com/documentation/appkit/nsbuttoncell/1528459-highlightsby)Added [NSButtonCell.imageDimsWhenDisabled](https://developer.apple.com/documentation/appkit/nsbuttoncell/1534152-imagedimswhendisabled)Added [NSButtonCell.imagePosition](https://developer.apple.com/documentation/appkit/nsbuttoncell/1529593-imageposition)Added [NSButtonCell.imageScaling](https://developer.apple.com/documentation/appkit/nsbuttoncell/1535104-imagescaling)Added [NSButtonCell.keyEquivalent](https://developer.apple.com/documentation/appkit/nsbuttoncell/1529476-keyequivalent)Added [NSButtonCell.keyEquivalentFont](https://developer.apple.com/documentation/appkit/nsbuttoncell/1531184-keyequivalentfont)Added [NSButtonCell.keyEquivalentModifierMask](https://developer.apple.com/documentation/appkit/nsbuttoncell/1528315-keyequivalentmodifiermask)Added [NSButtonCell.opaque](https://developer.apple.com/documentation/appkit/nsbuttoncell/1533667-opaque)Added [NSButtonCell.showsBorderOnlyWhileMouseInside](https://developer.apple.com/documentation/appkit/nsbuttoncell/1527903-showsborderonlywhilemouseinside)Added [NSButtonCell.showsStateBy](https://developer.apple.com/documentation/appkit/nsbuttoncell/1533225-showsstateby)Added [NSButtonCell.sound](https://developer.apple.com/documentation/appkit/nsbuttoncell/1525955-sound)Added [NSButtonCell.title](https://developer.apple.com/documentation/appkit/nsbuttoncell/1535916-title)Added [NSButtonCell.transparent](https://developer.apple.com/documentation/appkit/nsbuttoncell/1530887-transparent)NSCIImageRep.hRemoved [-[NSCIImageRep CIImage]](https://developer.apple.com/documentation/appkit/nsciimagerep/1525696-ciimage)Added [NSCIImageRep.CIImage](https://developer.apple.com/documentation/appkit/nsciimagerep/1525696-ciimage)Modified [-[CIImage initWithBitmapImageRep:]](https://developer.apple.com/documentation/coreimage/ciimage/1535335-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithBitmapImageRep:(NSBitmapImageRep *)bitmapImageRep ``` |
| To | ``` - (instancetype)initWithBitmapImageRep:(NSBitmapImageRep *)bitmapImageRep ``` |

Modified [+[NSCIImageRep imageRepWithCIImage:]](https://developer.apple.com/documentation/appkit/nsciimagerep/1550736-imagerepwithciimage)

|  | Declaration |
| --- | --- |
| From | ``` + (id)imageRepWithCIImage:(CIImage *)image ``` |
| To | ``` + (instancetype)imageRepWithCIImage:(CIImage *)image ``` |

Modified [-[NSCIImageRep initWithCIImage:]](https://developer.apple.com/documentation/appkit/nsciimagerep/1528642-initwithciimage)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCIImage:(CIImage *)image ``` |
| To | ``` - (instancetype)initWithCIImage:(CIImage *)image ``` |

NSCachedImageRep.hModified [NSCachedImageRep](https://developer.apple.com/documentation/appkit/nscachedimagerep)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

NSCell.hRemoved [-[NSCell acceptsFirstResponder]](https://developer.apple.com/documentation/appkit/nscell/1525710-acceptsfirstresponder)Removed [-[NSCell action]](https://developer.apple.com/documentation/appkit/nscell/1524654-action)Removed [-[NSCell alignment]](https://developer.apple.com/documentation/appkit/nscell/1534359-alignment)Removed [-[NSCell allowsEditingTextAttributes]](https://developer.apple.com/documentation/appkit/nscell/1535675-allowseditingtextattributes)Removed [-[NSCell allowsMixedState]](https://developer.apple.com/documentation/appkit/nscell/1531578-allowsmixedstate)Removed [-[NSCell allowsUndo]](https://developer.apple.com/documentation/appkit/nscell/1531576-allowsundo)Removed [-[NSCell attributedStringValue]](https://developer.apple.com/documentation/appkit/nscell/1534119-attributedstringvalue)Removed [-[NSCell backgroundStyle]](https://developer.apple.com/documentation/appkit/nscell/1524686-backgroundstyle)Removed [-[NSCell baseWritingDirection]](https://developer.apple.com/documentation/appkit/nscell/1525503-basewritingdirection)Removed [-[NSCell cellSize]](https://developer.apple.com/documentation/appkit/nscell/1532056-cellsize)Removed [-[NSCell controlSize]](https://developer.apple.com/documentation/appkit/nscell/1530780-controlsize)Removed [-[NSCell controlTint]](https://developer.apple.com/documentation/appkit/nscell/1529397-controltint)Removed [-[NSCell controlView]](https://developer.apple.com/documentation/appkit/nscell/1535913-controlview)Removed [-[NSCell doubleValue]](https://developer.apple.com/documentation/appkit/nscell/1534765-doublevalue)Removed [-[NSCell floatValue]](https://developer.apple.com/documentation/appkit/nscell/1534292-floatvalue)Removed [-[NSCell focusRingType]](https://developer.apple.com/documentation/appkit/nscell/1534132-focusringtype)Removed [-[NSCell font]](https://developer.apple.com/documentation/appkit/nscell/1526710-font)Removed [-[NSCell formatter]](https://developer.apple.com/documentation/appkit/nscell/1531115-formatter)Removed [-[NSCell hasValidObjectValue]](https://developer.apple.com/documentation/appkit/nscell/1534009-hasvalidobjectvalue)Removed [-[NSCell image]](https://developer.apple.com/documentation/appkit/nscell/1526028-image)Removed [-[NSCell importsGraphics]](https://developer.apple.com/documentation/appkit/nscell/1532380-importsgraphics)Removed [-[NSCell intValue]](https://developer.apple.com/documentation/appkit/nscell/1525170-intvalue)Removed [-[NSCell integerValue]](https://developer.apple.com/documentation/appkit/nscell/1527783-integervalue)Removed [-[NSCell interiorBackgroundStyle]](https://developer.apple.com/documentation/appkit/nscell/1526141-interiorbackgroundstyle)Removed [-[NSCell isBezeled]](https://developer.apple.com/documentation/appkit/nscell/1533376-bezeled)Removed [-[NSCell isBordered]](https://developer.apple.com/documentation/appkit/nscell/1525990-isbordered)Removed [-[NSCell isContinuous]](https://developer.apple.com/documentation/appkit/nscell/1529179-continuous)Removed [-[NSCell isEditable]](https://developer.apple.com/documentation/appkit/nscell/1535822-iseditable)Removed [-[NSCell isEnabled]](https://developer.apple.com/documentation/appkit/nscell/1533415-enabled)Removed [-[NSCell isHighlighted]](https://developer.apple.com/documentation/appkit/nscell/1530864-ishighlighted)Removed [-[NSCell isOpaque]](https://developer.apple.com/documentation/appkit/nscell/1531610-isopaque)Removed [-[NSCell isScrollable]](https://developer.apple.com/documentation/appkit/nscell/1534125-scrollable)Removed [-[NSCell isSelectable]](https://developer.apple.com/documentation/appkit/nscell/1529411-isselectable)Removed [-[NSCell keyEquivalent]](https://developer.apple.com/documentation/appkit/nscell/1532218-keyequivalent)Removed [-[NSCell lineBreakMode]](https://developer.apple.com/documentation/appkit/nscell/1531065-linebreakmode)Removed [-[NSCell menu]](https://developer.apple.com/documentation/appkit/nscell/1530019-menu)Removed [-[NSCell mouseDownFlags]](https://developer.apple.com/documentation/appkit/nscell/1527798-mousedownflags)Removed [-[NSCell nextState]](https://developer.apple.com/documentation/appkit/nscell/1531235-nextstate)Removed [-[NSCell objectValue]](https://developer.apple.com/documentation/appkit/nscell/1530936-objectvalue)Removed [-[NSCell refusesFirstResponder]](https://developer.apple.com/documentation/appkit/nscell/1525857-refusesfirstresponder)Removed [-[NSCell representedObject]](https://developer.apple.com/documentation/appkit/nscell/1533116-representedobject)Removed [-[NSCell sendsActionOnEndEditing]](https://developer.apple.com/documentation/appkit/nscell/1526617-sendsactiononendediting)Removed [-[NSCell setAction:]](https://developer.apple.com/documentation/appkit/nscell/1524654-action)Removed [-[NSCell setAlignment:]](https://developer.apple.com/documentation/appkit/nscell/1534359-alignment)Removed [-[NSCell setAllowsEditingTextAttributes:]](https://developer.apple.com/documentation/appkit/nscell/1535675-allowseditingtextattributes)Removed [-[NSCell setAllowsMixedState:]](https://developer.apple.com/documentation/appkit/nscell/1531578-allowsmixedstate)Removed [-[NSCell setAllowsUndo:]](https://developer.apple.com/documentation/appkit/nscell/1531576-allowsundo)Removed [-[NSCell setAttributedStringValue:]](https://developer.apple.com/documentation/appkit/nscell/1534119-attributedstringvalue)Removed [-[NSCell setBackgroundStyle:]](https://developer.apple.com/documentation/appkit/nscell/1524686-backgroundstyle)Removed [-[NSCell setBaseWritingDirection:]](https://developer.apple.com/documentation/appkit/nscell/1525503-basewritingdirection)Removed [-[NSCell setBezeled:]](https://developer.apple.com/documentation/appkit/nscell/1533376-isbezeled)Removed [-[NSCell setBordered:]](https://developer.apple.com/documentation/appkit/nscell/1525990-isbordered)Removed [-[NSCell setContinuous:]](https://developer.apple.com/documentation/appkit/nscell/1529179-iscontinuous)Removed [-[NSCell setControlSize:]](https://developer.apple.com/documentation/appkit/nscell/1530780-controlsize)Removed [-[NSCell setControlTint:]](https://developer.apple.com/documentation/appkit/nscell/1529397-controltint)Removed [-[NSCell setControlView:]](https://developer.apple.com/documentation/appkit/nscell/1535913-controlview)Removed [-[NSCell setDoubleValue:]](https://developer.apple.com/documentation/appkit/nscell/1534765-doublevalue)Removed [-[NSCell setEditable:]](https://developer.apple.com/documentation/appkit/nscell/1535822-editable)Removed [-[NSCell setEnabled:]](https://developer.apple.com/documentation/appkit/nscell/1533415-isenabled)Removed [-[NSCell setFloatValue:]](https://developer.apple.com/documentation/appkit/nscell/1534292-floatvalue)Removed [-[NSCell setFocusRingType:]](https://developer.apple.com/documentation/appkit/nscell/1534132-focusringtype)Removed [-[NSCell setFont:]](https://developer.apple.com/documentation/appkit/nscell/1526710-font)Removed [-[NSCell setFormatter:]](https://developer.apple.com/documentation/appkit/nscell/1531115-formatter)Removed [-[NSCell setHighlighted:]](https://developer.apple.com/documentation/appkit/nscell/1530864-ishighlighted)Removed [-[NSCell setImage:]](https://developer.apple.com/documentation/appkit/nscell/1526028-image)Removed [-[NSCell setImportsGraphics:]](https://developer.apple.com/documentation/appkit/nscell/1532380-importsgraphics)Removed [-[NSCell setIntValue:]](https://developer.apple.com/documentation/appkit/nscell/1525170-intvalue)Removed [-[NSCell setIntegerValue:]](https://developer.apple.com/documentation/appkit/nscell/1527783-integervalue)Removed [-[NSCell setLineBreakMode:]](https://developer.apple.com/documentation/appkit/nscell/1531065-linebreakmode)Removed [-[NSCell setMenu:]](https://developer.apple.com/documentation/appkit/nscell/1530019-menu)Removed [-[NSCell setObjectValue:]](https://developer.apple.com/documentation/appkit/nscell/1530936-objectvalue)Removed [-[NSCell setRefusesFirstResponder:]](https://developer.apple.com/documentation/appkit/nscell/1525857-refusesfirstresponder)Removed [-[NSCell setRepresentedObject:]](https://developer.apple.com/documentation/appkit/nscell/1533116-representedobject)Removed [-[NSCell setScrollable:]](https://developer.apple.com/documentation/appkit/nscell/1534125-scrollable)Removed [-[NSCell setSelectable:]](https://developer.apple.com/documentation/appkit/nscell/1529411-selectable)Removed [-[NSCell setSendsActionOnEndEditing:]](https://developer.apple.com/documentation/appkit/nscell/1526617-sendsactiononendediting)Removed [-[NSCell setShowsFirstResponder:]](https://developer.apple.com/documentation/appkit/nscell/1532415-showsfirstresponder)Removed [-[NSCell setState:]](https://developer.apple.com/documentation/appkit/nscell/1527417-state)Removed [-[NSCell setStringValue:]](https://developer.apple.com/documentation/appkit/nscell/1530915-stringvalue)Removed [-[NSCell setTag:]](https://developer.apple.com/documentation/appkit/nscell/1532348-tag)Removed [-[NSCell setTarget:]](https://developer.apple.com/documentation/appkit/nscell/1535832-target)Removed [-[NSCell setTitle:]](https://developer.apple.com/documentation/appkit/nscell/1525561-title)Removed [-[NSCell setTruncatesLastVisibleLine:]](https://developer.apple.com/documentation/appkit/nscell/1526736-truncateslastvisibleline)Removed [-[NSCell setType:]](https://developer.apple.com/documentation/appkit/nscell/1524871-type)Removed [-[NSCell setUserInterfaceLayoutDirection:]](https://developer.apple.com/documentation/appkit/nscell/1529213-userinterfacelayoutdirection)Removed [-[NSCell setUsesSingleLineMode:]](https://developer.apple.com/documentation/appkit/nscell/1525481-usessinglelinemode)Removed [-[NSCell setWraps:]](https://developer.apple.com/documentation/appkit/nscell/1527479-wraps)Removed [-[NSCell showsFirstResponder]](https://developer.apple.com/documentation/appkit/nscell/1532415-showsfirstresponder)Removed [-[NSCell state]](https://developer.apple.com/documentation/appkit/nscell/1527417-state)Removed [-[NSCell stringValue]](https://developer.apple.com/documentation/appkit/nscell/1530915-stringvalue)Removed [-[NSCell tag]](https://developer.apple.com/documentation/appkit/nscell/1532348-tag)Removed [-[NSCell target]](https://developer.apple.com/documentation/appkit/nscell/1535832-target)Removed [-[NSCell title]](https://developer.apple.com/documentation/appkit/nscell/1525561-title)Removed [-[NSCell truncatesLastVisibleLine]](https://developer.apple.com/documentation/appkit/nscell/1526736-truncateslastvisibleline)Removed [-[NSCell type]](https://developer.apple.com/documentation/appkit/nscell/1524871-type)Removed [-[NSCell userInterfaceLayoutDirection]](https://developer.apple.com/documentation/appkit/nscell/1529213-userinterfacelayoutdirection)Removed [-[NSCell usesSingleLineMode]](https://developer.apple.com/documentation/appkit/nscell/1525481-usessinglelinemode)Removed [-[NSCell wantsNotificationForMarkedText]](https://developer.apple.com/documentation/appkit/nscell/1535894-wantsnotificationformarkedtext)Removed [-[NSCell wraps]](https://developer.apple.com/documentation/appkit/nscell/1527479-wraps)Added [NSCell.acceptsFirstResponder](https://developer.apple.com/documentation/appkit/nscell/1525710-acceptsfirstresponder)Added [NSCell.action](https://developer.apple.com/documentation/appkit/nscell/1524654-action)Added [NSCell.alignment](https://developer.apple.com/documentation/appkit/nscell/1534359-alignment)Added [NSCell.allowsEditingTextAttributes](https://developer.apple.com/documentation/appkit/nscell/1535675-allowseditingtextattributes)Added [NSCell.allowsMixedState](https://developer.apple.com/documentation/appkit/nscell/1531578-allowsmixedstate)Added [NSCell.allowsUndo](https://developer.apple.com/documentation/appkit/nscell/1531576-allowsundo)Added [NSCell.attributedStringValue](https://developer.apple.com/documentation/appkit/nscell/1534119-attributedstringvalue)Added [NSCell.backgroundStyle](https://developer.apple.com/documentation/appkit/nscell/1524686-backgroundstyle)Added [NSCell.baseWritingDirection](https://developer.apple.com/documentation/appkit/nscell/1525503-basewritingdirection)Added [NSCell.bezeled](https://developer.apple.com/documentation/appkit/nscell/1533376-bezeled)Added [NSCell.bordered](https://developer.apple.com/documentation/appkit/nscell/1525990-isbordered)Added [NSCell.cellSize](https://developer.apple.com/documentation/appkit/nscell/1532056-cellsize)Added [NSCell.continuous](https://developer.apple.com/documentation/appkit/nscell/1529179-continuous)Added [NSCell.controlSize](https://developer.apple.com/documentation/appkit/nscell/1530780-controlsize)Added [NSCell.controlTint](https://developer.apple.com/documentation/appkit/nscell/1529397-controltint)Added [NSCell.controlView](https://developer.apple.com/documentation/appkit/nscell/1535913-controlview)Added [NSCell.doubleValue](https://developer.apple.com/documentation/appkit/nscell/1534765-doublevalue)Added [NSCell.editable](https://developer.apple.com/documentation/appkit/nscell/1535822-iseditable)Added [NSCell.enabled](https://developer.apple.com/documentation/appkit/nscell/1533415-enabled)Added [NSCell.floatValue](https://developer.apple.com/documentation/appkit/nscell/1534292-floatvalue)Added [NSCell.focusRingType](https://developer.apple.com/documentation/appkit/nscell/1534132-focusringtype)Added [NSCell.font](https://developer.apple.com/documentation/appkit/nscell/1526710-font)Added [NSCell.formatter](https://developer.apple.com/documentation/appkit/nscell/1531115-formatter)Added [NSCell.hasValidObjectValue](https://developer.apple.com/documentation/appkit/nscell/1534009-hasvalidobjectvalue)Added [NSCell.highlighted](https://developer.apple.com/documentation/appkit/nscell/1530864-highlighted)Added [NSCell.image](https://developer.apple.com/documentation/appkit/nscell/1526028-image)Added [NSCell.importsGraphics](https://developer.apple.com/documentation/appkit/nscell/1532380-importsgraphics)Added [NSCell.intValue](https://developer.apple.com/documentation/appkit/nscell/1525170-intvalue)Added [NSCell.integerValue](https://developer.apple.com/documentation/appkit/nscell/1527783-integervalue)Added [NSCell.interiorBackgroundStyle](https://developer.apple.com/documentation/appkit/nscell/1526141-interiorbackgroundstyle)Added [NSCell.keyEquivalent](https://developer.apple.com/documentation/appkit/nscell/1532218-keyequivalent)Added [NSCell.lineBreakMode](https://developer.apple.com/documentation/appkit/nscell/1531065-linebreakmode)Added [NSCell.menu](https://developer.apple.com/documentation/appkit/nscell/1530019-menu)Added [NSCell.mouseDownFlags](https://developer.apple.com/documentation/appkit/nscell/1527798-mousedownflags)Added [NSCell.nextState](https://developer.apple.com/documentation/appkit/nscell/1531235-nextstate)Added [NSCell.objectValue](https://developer.apple.com/documentation/appkit/nscell/1530936-objectvalue)Added [NSCell.opaque](https://developer.apple.com/documentation/appkit/nscell/1531610-opaque)Added [NSCell.refusesFirstResponder](https://developer.apple.com/documentation/appkit/nscell/1525857-refusesfirstresponder)Added [NSCell.representedObject](https://developer.apple.com/documentation/appkit/nscell/1533116-representedobject)Added [NSCell.scrollable](https://developer.apple.com/documentation/appkit/nscell/1534125-scrollable)Added [NSCell.selectable](https://developer.apple.com/documentation/appkit/nscell/1529411-selectable)Added [NSCell.sendsActionOnEndEditing](https://developer.apple.com/documentation/appkit/nscell/1526617-sendsactiononendediting)Added [NSCell.showsFirstResponder](https://developer.apple.com/documentation/appkit/nscell/1532415-showsfirstresponder)Added [NSCell.state](https://developer.apple.com/documentation/appkit/nscell/1527417-state)Added [NSCell.stringValue](https://developer.apple.com/documentation/appkit/nscell/1530915-stringvalue)Added [NSCell.tag](https://developer.apple.com/documentation/appkit/nscell/1532348-tag)Added [NSCell.target](https://developer.apple.com/documentation/appkit/nscell/1535832-target)Added [NSCell.title](https://developer.apple.com/documentation/appkit/nscell/1525561-title)Added [NSCell.truncatesLastVisibleLine](https://developer.apple.com/documentation/appkit/nscell/1526736-truncateslastvisibleline)Added [NSCell.type](https://developer.apple.com/documentation/appkit/nscell/1524871-type)Added [NSCell.userInterfaceLayoutDirection](https://developer.apple.com/documentation/appkit/nscell/1529213-userinterfacelayoutdirection)Added [NSCell.usesSingleLineMode](https://developer.apple.com/documentation/appkit/nscell/1525481-usessinglelinemode)Added [NSCell.wantsNotificationForMarkedText](https://developer.apple.com/documentation/appkit/nscell/1535894-wantsnotificationformarkedtext)Added [NSCell.wraps](https://developer.apple.com/documentation/appkit/nscell/1527479-wraps)Added [NSCellHitResult](https://developer.apple.com/documentation/appkit/nscell/hitresult)Added [NSCellStyleMask](https://developer.apple.com/documentation/appkit/nscell/stylemask)Modified [NSCell](https://developer.apple.com/documentation/appkit/nscell)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSUserInterfaceItemIdentification |
| To | NSAccessibility, NSAccessibilityElement, NSCoding, NSCopying, NSUserInterfaceItemIdentification |

Modified [-[NSCell hitTestForEvent:inRect:ofView:]](https://developer.apple.com/documentation/appkit/nscell/1529601-hittestforevent)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)hitTestForEvent:(NSEvent *)event inRect:(NSRect)cellFrame ofView:(NSView *)controlView ``` |
| To | ``` - (NSCellHitResult)hitTestForEvent:(NSEvent *)event inRect:(NSRect)cellFrame ofView:(NSView *)controlView ``` |

Modified [-[NSCell initImageCell:]](https://developer.apple.com/documentation/appkit/nscell/1533898-initimagecell)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initImageCell:(NSImage *)image ``` |
| To | ``` - (instancetype)initImageCell:(NSImage *)image ``` |

Modified [-[NSCell initTextCell:]](https://developer.apple.com/documentation/appkit/nscell/1530851-inittextcell)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initTextCell:(NSString *)aString ``` |
| To | ``` - (instancetype)initTextCell:(NSString *)aString ``` |

Modified [NSAnyType](https://developer.apple.com/documentation/appkit/1560866-anonymous/nsanytype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSDoubleType](https://developer.apple.com/documentation/appkit/1560866-anonymous/nsdoubletype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSFloatType](https://developer.apple.com/documentation/appkit/1560866-anonymous/nsfloattype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSIntType](https://developer.apple.com/documentation/appkit/1560866-anonymous/nsinttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSPositiveDoubleType](https://developer.apple.com/documentation/appkit/1560866-anonymous/nspositivedoubletype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSPositiveFloatType](https://developer.apple.com/documentation/appkit/1560866-anonymous/nspositivefloattype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSPositiveIntType](https://developer.apple.com/documentation/appkit/1560866-anonymous/nspositiveinttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSScaleNone](https://developer.apple.com/documentation/appkit/nsimagescaling/nsscalenone)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSScaleProportionally](https://developer.apple.com/documentation/appkit/nsimagescaling/1534465-nsscaleproportionally)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSScaleToFit](https://developer.apple.com/documentation/appkit/nsimagescaling/nsscaletofit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

NSClickGestureRecognizer.h (Added)Added [NSClickGestureRecognizer](https://developer.apple.com/documentation/appkit/nsclickgesturerecognizer)Added [NSClickGestureRecognizer.buttonMask](https://developer.apple.com/documentation/appkit/nsclickgesturerecognizer/1530136-buttonmask)Added [NSClickGestureRecognizer.numberOfClicksRequired](https://developer.apple.com/documentation/appkit/nsclickgesturerecognizer/1534485-numberofclicksrequired)NSClipView.hRemoved [-[NSClipView backgroundColor]](https://developer.apple.com/documentation/appkit/nsclipview/1525469-backgroundcolor)Removed [-[NSClipView copiesOnScroll]](https://developer.apple.com/documentation/appkit/nsclipview/1532142-copiesonscroll)Removed [-[NSClipView documentCursor]](https://developer.apple.com/documentation/appkit/nsclipview/1535377-documentcursor)Removed [-[NSClipView documentRect]](https://developer.apple.com/documentation/appkit/nsclipview/1533338-documentrect)Removed [-[NSClipView documentView]](https://developer.apple.com/documentation/appkit/nsclipview/1524587-documentview)Removed [-[NSClipView documentVisibleRect]](https://developer.apple.com/documentation/appkit/nsclipview/1527958-documentvisiblerect)Removed [-[NSClipView drawsBackground]](https://developer.apple.com/documentation/appkit/nsclipview/1534684-drawsbackground)Removed [-[NSClipView setBackgroundColor:]](https://developer.apple.com/documentation/appkit/nsclipview/1525469-backgroundcolor)Removed [-[NSClipView setCopiesOnScroll:]](https://developer.apple.com/documentation/appkit/nsclipview/1532142-copiesonscroll)Removed [-[NSClipView setDocumentCursor:]](https://developer.apple.com/documentation/appkit/nsclipview/1535377-documentcursor)Removed [-[NSClipView setDocumentView:]](https://developer.apple.com/documentation/appkit/nsclipview/1524587-documentview)Removed [-[NSClipView setDrawsBackground:]](https://developer.apple.com/documentation/appkit/nsclipview/1534684-drawsbackground)Added [NSClipView.automaticallyAdjustsContentInsets](https://developer.apple.com/documentation/appkit/nsclipview/1527540-automaticallyadjustscontentinset)Added [NSClipView.backgroundColor](https://developer.apple.com/documentation/appkit/nsclipview/1525469-backgroundcolor)Added [NSClipView.contentInsets](https://developer.apple.com/documentation/appkit/nsclipview/1524329-contentinsets)Added [NSClipView.copiesOnScroll](https://developer.apple.com/documentation/appkit/nsclipview/1532142-copiesonscroll)Added [NSClipView.documentCursor](https://developer.apple.com/documentation/appkit/nsclipview/1535377-documentcursor)Added [NSClipView.documentRect](https://developer.apple.com/documentation/appkit/nsclipview/1533338-documentrect)Added [NSClipView.documentView](https://developer.apple.com/documentation/appkit/nsclipview/1524587-documentview)Added [NSClipView.documentVisibleRect](https://developer.apple.com/documentation/appkit/nsclipview/1527958-documentvisiblerect)Added [NSClipView.drawsBackground](https://developer.apple.com/documentation/appkit/nsclipview/1534684-drawsbackground)Modified [-[NSClipView constrainScrollPoint:]](https://developer.apple.com/documentation/appkit/nsclipview/1526678-constrainscroll)

|  | Deprecation |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.10 |

NSCollectionView.hRemoved [-[NSCollectionView allowsMultipleSelection]](https://developer.apple.com/documentation/appkit/nscollectionview/1524276-allowsmultipleselection)Removed [-[NSCollectionView backgroundColors]](https://developer.apple.com/documentation/appkit/nscollectionview/1528220-backgroundcolors)Removed [-[NSCollectionView content]](https://developer.apple.com/documentation/appkit/nscollectionview/1528207-content)Removed [-[NSCollectionView delegate]](https://developer.apple.com/documentation/appkit/nscollectionview/1528246-delegate)Removed [-[NSCollectionView isFirstResponder]](https://developer.apple.com/documentation/appkit/nscollectionview/1528199-isfirstresponder)Removed [-[NSCollectionView isSelectable]](https://developer.apple.com/documentation/appkit/nscollectionview/1528300-isselectable)Removed [-[NSCollectionView itemPrototype]](https://developer.apple.com/documentation/appkit/nscollectionview/1528285-itemprototype)Removed [-[NSCollectionView maxItemSize]](https://developer.apple.com/documentation/appkit/nscollectionview/1526761-maxitemsize)Removed [-[NSCollectionView maxNumberOfColumns]](https://developer.apple.com/documentation/appkit/nscollectionview/1528281-maxnumberofcolumns)Removed [-[NSCollectionView maxNumberOfRows]](https://developer.apple.com/documentation/appkit/nscollectionview/1524757-maxnumberofrows)Removed [-[NSCollectionView minItemSize]](https://developer.apple.com/documentation/appkit/nscollectionview/1526293-minitemsize)Removed [-[NSCollectionView selectionIndexes]](https://developer.apple.com/documentation/appkit/nscollectionview/1525505-selectionindexes)Removed [-[NSCollectionView setAllowsMultipleSelection:]](https://developer.apple.com/documentation/appkit/nscollectionview/1524276-allowsmultipleselection)Removed [-[NSCollectionView setBackgroundColors:]](https://developer.apple.com/documentation/appkit/nscollectionview/1528220-backgroundcolors)Removed [-[NSCollectionView setContent:]](https://developer.apple.com/documentation/appkit/nscollectionview/1528207-content)Removed [-[NSCollectionView setDelegate:]](https://developer.apple.com/documentation/appkit/nscollectionview/1528246-delegate)Removed [-[NSCollectionView setItemPrototype:]](https://developer.apple.com/documentation/appkit/nscollectionview/1528285-itemprototype)Removed [-[NSCollectionView setMaxItemSize:]](https://developer.apple.com/documentation/appkit/nscollectionview/1526761-maxitemsize)Removed [-[NSCollectionView setMaxNumberOfColumns:]](https://developer.apple.com/documentation/appkit/nscollectionview/1528281-maxnumberofcolumns)Removed [-[NSCollectionView setMaxNumberOfRows:]](https://developer.apple.com/documentation/appkit/nscollectionview/1524757-maxnumberofrows)Removed [-[NSCollectionView setMinItemSize:]](https://developer.apple.com/documentation/appkit/nscollectionview/1526293-minitemsize)Removed [-[NSCollectionView setSelectable:]](https://developer.apple.com/documentation/appkit/nscollectionview/1528300-isselectable)Removed [-[NSCollectionView setSelectionIndexes:]](https://developer.apple.com/documentation/appkit/nscollectionview/1525505-selectionindexes)Added [NSCollectionView.allowsMultipleSelection](https://developer.apple.com/documentation/appkit/nscollectionview/1524276-allowsmultipleselection)Added [NSCollectionView.backgroundColors](https://developer.apple.com/documentation/appkit/nscollectionview/1528220-backgroundcolors)Added [NSCollectionView.content](https://developer.apple.com/documentation/appkit/nscollectionview/1528207-content)Added [NSCollectionView.delegate](https://developer.apple.com/documentation/appkit/nscollectionview/1528246-delegate)Added [NSCollectionView.firstResponder](https://developer.apple.com/documentation/appkit/nscollectionview/1528199-firstresponder)Added [NSCollectionView.itemPrototype](https://developer.apple.com/documentation/appkit/nscollectionview/1528285-itemprototype)Added [NSCollectionView.maxItemSize](https://developer.apple.com/documentation/appkit/nscollectionview/1526761-maxitemsize)Added [NSCollectionView.maxNumberOfColumns](https://developer.apple.com/documentation/appkit/nscollectionview/1528281-maxnumberofcolumns)Added [NSCollectionView.maxNumberOfRows](https://developer.apple.com/documentation/appkit/nscollectionview/1524757-maxnumberofrows)Added [NSCollectionView.minItemSize](https://developer.apple.com/documentation/appkit/nscollectionview/1526293-minitemsize)Added [NSCollectionView.selectable](https://developer.apple.com/documentation/appkit/nscollectionview/1528300-isselectable)Added [NSCollectionView.selectionIndexes](https://developer.apple.com/documentation/appkit/nscollectionview/1525505-selectionindexes)Modified [-[NSCollectionViewDelegate collectionView:acceptDrop:index:dropOperation:]](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/1528242-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSCollectionViewDelegate collectionView:canDragItemsAtIndexes:withEvent:]](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/1528212-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSCollectionViewDelegate collectionView:draggingImageForItemsAtIndexes:withEvent:offset:]](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/1528138-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSCollectionViewDelegate collectionView:draggingSession:endedAtPoint:dragOperation:]](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/1528224-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSCollectionViewDelegate collectionView:draggingSession:willBeginAtPoint:forItemsAtIndexes:]](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/1524615-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSCollectionViewDelegate collectionView:namesOfPromisedFilesDroppedAtDestination:forDraggedItemsAtIndexes:]](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/1528189-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSCollectionViewDelegate collectionView:pasteboardWriterForItemAtIndex:]](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/1528257-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSCollectionViewDelegate collectionView:updateDraggingItemsForDrag:]](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/1526881-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSCollectionViewDelegate collectionView:validateDrop:proposedIndex:dropOperation:]](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/1528283-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSCollectionViewDelegate collectionView:writeItemsAtIndexes:toPasteboard:]](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/1524770-collectionview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [NSCollectionViewItem.imageView](https://developer.apple.com/documentation/appkit/nscollectionviewitem/1525366-imageview)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) NSImageView *imageView ``` |
| To | ``` @property(assign) IBOutlet NSImageView *imageView ``` |

Modified [NSCollectionViewItem.textField](https://developer.apple.com/documentation/appkit/nscollectionviewitem/1527126-textfield)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) NSTextField *textField ``` |
| To | ``` @property(assign) IBOutlet NSTextField *textField ``` |

NSColor.hRemoved [-[NSColor CGColor]](https://developer.apple.com/documentation/appkit/nscolor/1527738-cgcolor)Removed [-[NSColor alphaComponent]](https://developer.apple.com/documentation/appkit/nscolor/1532504-alphacomponent)Removed [-[NSColor blackComponent]](https://developer.apple.com/documentation/appkit/nscolor/1526883-blackcomponent)Removed [-[NSColor blueComponent]](https://developer.apple.com/documentation/appkit/nscolor/1534229-bluecomponent)Removed [-[NSColor brightnessComponent]](https://developer.apple.com/documentation/appkit/nscolor/1529355-brightnesscomponent)Removed [-[NSColor catalogNameComponent]](https://developer.apple.com/documentation/appkit/nscolor/1535443-catalognamecomponent)Removed [-[NSColor colorNameComponent]](https://developer.apple.com/documentation/appkit/nscolor/1528278-colornamecomponent)Removed [-[NSColor colorSpace]](https://developer.apple.com/documentation/appkit/nscolor/1526733-colorspace)Removed [-[NSColor colorSpaceName]](https://developer.apple.com/documentation/appkit/nscolor/1535228-colorspacename)Removed [-[NSColor cyanComponent]](https://developer.apple.com/documentation/appkit/nscolor/1528234-cyancomponent)Removed [-[NSColor greenComponent]](https://developer.apple.com/documentation/appkit/nscolor/1525935-greencomponent)Removed [-[NSColor hueComponent]](https://developer.apple.com/documentation/appkit/nscolor/1531780-huecomponent)Removed [-[NSColor localizedCatalogNameComponent]](https://developer.apple.com/documentation/appkit/nscolor/1535351-localizedcatalognamecomponent)Removed [-[NSColor localizedColorNameComponent]](https://developer.apple.com/documentation/appkit/nscolor/1527286-localizedcolornamecomponent)Removed [-[NSColor magentaComponent]](https://developer.apple.com/documentation/appkit/nscolor/1535560-magentacomponent)Removed [-[NSColor numberOfComponents]](https://developer.apple.com/documentation/appkit/nscolor/1531308-numberofcomponents)Removed [-[NSColor patternImage]](https://developer.apple.com/documentation/appkit/nscolor/1531572-patternimage)Removed [-[NSColor redComponent]](https://developer.apple.com/documentation/appkit/nscolor/1530483-redcomponent)Removed [-[NSColor saturationComponent]](https://developer.apple.com/documentation/appkit/nscolor/1526326-saturationcomponent)Removed [-[NSColor whiteComponent]](https://developer.apple.com/documentation/appkit/nscolor/1534051-whitecomponent)Removed [-[NSColor yellowComponent]](https://developer.apple.com/documentation/appkit/nscolor/1531965-yellowcomponent)Added [NSColor.CGColor](https://developer.apple.com/documentation/appkit/nscolor/1527738-cgcolor)Added [NSColor.alphaComponent](https://developer.apple.com/documentation/appkit/nscolor/1532504-alphacomponent)Added [NSColor.blackComponent](https://developer.apple.com/documentation/appkit/nscolor/1526883-blackcomponent)Added [NSColor.blueComponent](https://developer.apple.com/documentation/appkit/nscolor/1534229-bluecomponent)Added [NSColor.brightnessComponent](https://developer.apple.com/documentation/appkit/nscolor/1529355-brightnesscomponent)Added [NSColor.catalogNameComponent](https://developer.apple.com/documentation/appkit/nscolor/1535443-catalognamecomponent)Added [NSColor.colorNameComponent](https://developer.apple.com/documentation/appkit/nscolor/1528278-colornamecomponent)Added [NSColor.colorSpace](https://developer.apple.com/documentation/appkit/nscolor/1526733-colorspace)Added [NSColor.colorSpaceName](https://developer.apple.com/documentation/appkit/nscolor/1535228-colorspacename)Added [NSColor.cyanComponent](https://developer.apple.com/documentation/appkit/nscolor/1528234-cyancomponent)Added [NSColor.greenComponent](https://developer.apple.com/documentation/appkit/nscolor/1525935-greencomponent)Added [NSColor.hueComponent](https://developer.apple.com/documentation/appkit/nscolor/1531780-huecomponent)Added [-[NSColor init]](https://developer.apple.com/documentation/appkit/nscolor/1533939-init)Added [-[NSColor initWithCoder:]](https://developer.apple.com/documentation/appkit/nscolor/1527272-init)Added [+[NSColor labelColor]](https://developer.apple.com/documentation/appkit/nscolor/1534657-labelcolor)Added [NSColor.localizedCatalogNameComponent](https://developer.apple.com/documentation/appkit/nscolor/1535351-localizedcatalognamecomponent)Added [NSColor.localizedColorNameComponent](https://developer.apple.com/documentation/appkit/nscolor/1527286-localizedcolornamecomponent)Added [NSColor.magentaComponent](https://developer.apple.com/documentation/appkit/nscolor/1535560-magentacomponent)Added [NSColor.numberOfComponents](https://developer.apple.com/documentation/appkit/nscolor/1531308-numberofcomponents)Added [NSColor.patternImage](https://developer.apple.com/documentation/appkit/nscolor/1531572-patternimage)Added [+[NSColor quaternaryLabelColor]](https://developer.apple.com/documentation/appkit/nscolor/1534635-quaternarylabelcolor)Added [NSColor.redComponent](https://developer.apple.com/documentation/appkit/nscolor/1530483-redcomponent)Added [NSColor.saturationComponent](https://developer.apple.com/documentation/appkit/nscolor/1526326-saturationcomponent)Added [+[NSColor secondaryLabelColor]](https://developer.apple.com/documentation/appkit/nscolor/1533254-secondarylabelcolor)Added [+[NSColor tertiaryLabelColor]](https://developer.apple.com/documentation/appkit/nscolor/1532376-tertiarylabelcolor)Added [NSColor.whiteComponent](https://developer.apple.com/documentation/appkit/nscolor/1534051-whitecomponent)Added [NSColor.yellowComponent](https://developer.apple.com/documentation/appkit/nscolor/1531965-yellowcomponent)Modified [-[CIColor initWithColor:]](https://developer.apple.com/documentation/coreimage/cicolor/1528762-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithColor:(NSColor *)color ``` |
| To | ``` - (instancetype)initWithColor:(NSColor *)color ``` |

Modified [NSColor](https://developer.apple.com/documentation/appkit/nscolor)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSPasteboardReading, NSPasteboardWriting |
| To | NSCopying, NSPasteboardReading, NSPasteboardWriting, NSSecureCoding |

NSColorList.hRemoved [-[NSColorList allKeys]](https://developer.apple.com/documentation/appkit/nscolorlist/1522141-allkeys)Removed [-[NSColorList isEditable]](https://developer.apple.com/documentation/appkit/nscolorlist/1522125-editable)Removed [-[NSColorList name]](https://developer.apple.com/documentation/appkit/nscolorlist/1522138-name)Added [NSColorList.allKeys](https://developer.apple.com/documentation/appkit/nscolorlist/1522141-allkeys)Added [NSColorList.editable](https://developer.apple.com/documentation/appkit/nscolorlist/1522125-editable)Added [NSColorList.name](https://developer.apple.com/documentation/appkit/nscolorlist/1522138-name)Modified [-[NSColorList initWithName:]](https://developer.apple.com/documentation/appkit/nscolorlist/1522140-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithName:(NSString *)name ``` |
| To | ``` - (instancetype)initWithName:(NSString *)name ``` |

Modified [-[NSColorList initWithName:fromFile:]](https://developer.apple.com/documentation/appkit/nscolorlist/1522133-initwithname)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithName:(NSString *)name fromFile:(NSString *)path ``` |
| To | ``` - (instancetype)initWithName:(NSString *)name fromFile:(NSString *)path ``` |

NSColorPanel.hRemoved [-[NSColorPanel accessoryView]](https://developer.apple.com/documentation/appkit/nscolorpanel/1526892-accessoryview)Removed [-[NSColorPanel alpha]](https://developer.apple.com/documentation/appkit/nscolorpanel/1526246-alpha)Removed [-[NSColorPanel color]](https://developer.apple.com/documentation/appkit/nscolorpanel/1530835-color)Removed [-[NSColorPanel isContinuous]](https://developer.apple.com/documentation/appkit/nscolorpanel/1528265-continuous)Removed [-[NSColorPanel mode]](https://developer.apple.com/documentation/appkit/nscolorpanel/1525410-mode)Removed [-[NSColorPanel setAccessoryView:]](https://developer.apple.com/documentation/appkit/nscolorpanel/1526892-accessoryview)Removed [-[NSColorPanel setColor:]](https://developer.apple.com/documentation/appkit/nscolorpanel/1530835-color)Removed [-[NSColorPanel setContinuous:]](https://developer.apple.com/documentation/appkit/nscolorpanel/1528265-continuous)Removed [-[NSColorPanel setMode:]](https://developer.apple.com/documentation/appkit/nscolorpanel/1525410-mode)Removed [-[NSColorPanel setShowsAlpha:]](https://developer.apple.com/documentation/appkit/nscolorpanel/1525279-showsalpha)Removed [-[NSColorPanel showsAlpha]](https://developer.apple.com/documentation/appkit/nscolorpanel/1525279-showsalpha)Added [NSColorPanel.accessoryView](https://developer.apple.com/documentation/appkit/nscolorpanel/1526892-accessoryview)Added [NSColorPanel.alpha](https://developer.apple.com/documentation/appkit/nscolorpanel/1526246-alpha)Added [NSColorPanel.color](https://developer.apple.com/documentation/appkit/nscolorpanel/1530835-color)Added [NSColorPanel.continuous](https://developer.apple.com/documentation/appkit/nscolorpanel/1528265-continuous)Added [NSColorPanel.mode](https://developer.apple.com/documentation/appkit/nscolorpanel/1525410-mode)Added [NSColorPanel.showsAlpha](https://developer.apple.com/documentation/appkit/nscolorpanel/1525279-showsalpha)Added [NSColorPanelOptions](https://developer.apple.com/documentation/appkit/nscolorpaneloptions)Modified [+[NSColorPanel setPickerMask:]](https://developer.apple.com/documentation/appkit/nscolorpanel/1534004-setpickermask)

|  | Declaration |
| --- | --- |
| From | ``` + (void)setPickerMask:(NSUInteger)mask ``` |
| To | ``` + (void)setPickerMask:(NSColorPanelOptions)mask ``` |

NSColorPicker.hRemoved [-[NSColorPicker buttonToolTip]](https://developer.apple.com/documentation/appkit/nscolorpicker/1492404-buttontooltip)Removed [-[NSColorPicker colorPanel]](https://developer.apple.com/documentation/appkit/nscolorpicker/1492396-colorpanel)Removed [-[NSColorPicker minContentSize]](https://developer.apple.com/documentation/appkit/nscolorpicker/1492391-mincontentsize)Removed [-[NSColorPicker provideNewButtonImage]](https://developer.apple.com/documentation/appkit/nscolorpicker/1492393-providenewbuttonimage)Added [NSColorPicker.buttonToolTip](https://developer.apple.com/documentation/appkit/nscolorpicker/1492404-buttontooltip)Added [NSColorPicker.colorPanel](https://developer.apple.com/documentation/appkit/nscolorpicker/1492396-colorpanel)Added [NSColorPicker.minContentSize](https://developer.apple.com/documentation/appkit/nscolorpicker/1492391-mincontentsize)Added [NSColorPicker.provideNewButtonImage](https://developer.apple.com/documentation/appkit/nscolorpicker/1492393-providenewbuttonimage)Modified [-[NSColorPicker initWithPickerMask:colorPanel:]](https://developer.apple.com/documentation/appkit/nscolorpicker/1492397-initwithpickermask)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithPickerMask:(NSUInteger)mask colorPanel:(NSColorPanel *)owningColorPanel ``` |
| To | ``` - (instancetype)initWithPickerMask:(NSUInteger)mask colorPanel:(NSColorPanel *)owningColorPanel ``` |

NSColorPicking.hModified [-[NSColorPickingDefault initWithPickerMask:colorPanel:]](https://developer.apple.com/documentation/appkit/nscolorpickingdefault/1528432-initwithpickermask)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithPickerMask:(NSUInteger)mask colorPanel:(NSColorPanel *)owningColorPanel ``` |
| To | ``` - (instancetype)initWithPickerMask:(NSUInteger)mask colorPanel:(NSColorPanel *)owningColorPanel ``` |

NSColorSpace.hRemoved [-[NSColorSpace CGColorSpace]](https://developer.apple.com/documentation/appkit/nscolorspace/1412073-cgcolorspace)Removed [-[NSColorSpace ICCProfileData]](https://developer.apple.com/documentation/appkit/nscolorspace/1412078-iccprofiledata)Removed [-[NSColorSpace colorSpaceModel]](https://developer.apple.com/documentation/appkit/nscolorspace/1412095-colorspacemodel)Removed [-[NSColorSpace colorSyncProfile]](https://developer.apple.com/documentation/appkit/nscolorspace/1412076-colorsyncprofile)Removed [-[NSColorSpace localizedName]](https://developer.apple.com/documentation/appkit/nscolorspace/1412072-localizedname)Removed [-[NSColorSpace numberOfColorComponents]](https://developer.apple.com/documentation/appkit/nscolorspace/1412099-numberofcolorcomponents)Added [NSColorSpace.CGColorSpace](https://developer.apple.com/documentation/appkit/nscolorspace/1412073-cgcolorspace)Added [NSColorSpace.ICCProfileData](https://developer.apple.com/documentation/appkit/nscolorspace/1412078-iccprofiledata)Added [NSColorSpace.colorSpaceModel](https://developer.apple.com/documentation/appkit/nscolorspace/1412095-colorspacemodel)Added [NSColorSpace.colorSyncProfile](https://developer.apple.com/documentation/appkit/nscolorspace/1412076-colorsyncprofile)Added [NSColorSpace.localizedName](https://developer.apple.com/documentation/appkit/nscolorspace/1412072-localizedname)Added [NSColorSpace.numberOfColorComponents](https://developer.apple.com/documentation/appkit/nscolorspace/1412099-numberofcolorcomponents)Modified [NSColorSpace](https://developer.apple.com/documentation/appkit/nscolorspace)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSSecureCoding |

Modified [-[NSColorSpace initWithCGColorSpace:]](https://developer.apple.com/documentation/appkit/nscolorspace/1412059-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCGColorSpace:(CGColorSpaceRef)cgColorSpace ``` |
| To | ``` - (instancetype)initWithCGColorSpace:(CGColorSpaceRef)cgColorSpace ``` |

Modified [-[NSColorSpace initWithColorSyncProfile:]](https://developer.apple.com/documentation/appkit/nscolorspace/1412062-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithColorSyncProfile:(void *)prof ``` |
| To | ``` - (instancetype)initWithColorSyncProfile:(void *)prof ``` |

Modified [-[NSColorSpace initWithICCProfileData:]](https://developer.apple.com/documentation/appkit/nscolorspace/1412094-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithICCProfileData:(NSData *)iccData ``` |
| To | ``` - (instancetype)initWithICCProfileData:(NSData *)iccData ``` |

NSColorWell.hRemoved [-[NSColorWell color]](https://developer.apple.com/documentation/appkit/nscolorwell/1534546-color)Removed -[NSColorWell isActive]Removed -[NSColorWell isBordered]Removed [-[NSColorWell setBordered:]](https://developer.apple.com/documentation/appkit/nscolorwell/1528015-bordered)Removed [-[NSColorWell setColor:]](https://developer.apple.com/documentation/appkit/nscolorwell/1534546-color)Added [NSColorWell.active](https://developer.apple.com/documentation/appkit/nscolorwell/1528698-isactive)Added [NSColorWell.bordered](https://developer.apple.com/documentation/appkit/nscolorwell/1528015-bordered)Added [NSColorWell.color](https://developer.apple.com/documentation/appkit/nscolorwell/1534546-color)NSComboBox.hRemoved [-[NSComboBox completes]](https://developer.apple.com/documentation/appkit/nscombobox/1436749-completes)Removed [-[NSComboBox dataSource]](https://developer.apple.com/documentation/appkit/nscombobox/1436729-datasource)Removed [-[NSComboBox hasVerticalScroller]](https://developer.apple.com/documentation/appkit/nscombobox/1436705-hasverticalscroller)Removed [-[NSComboBox indexOfSelectedItem]](https://developer.apple.com/documentation/appkit/nscombobox/1436701-indexofselecteditem)Removed [-[NSComboBox intercellSpacing]](https://developer.apple.com/documentation/appkit/nscombobox/1436771-intercellspacing)Removed [-[NSComboBox isButtonBordered]](https://developer.apple.com/documentation/appkit/nscombobox/1436711-buttonbordered)Removed [-[NSComboBox itemHeight]](https://developer.apple.com/documentation/appkit/nscombobox/1436767-itemheight)Removed [-[NSComboBox numberOfItems]](https://developer.apple.com/documentation/appkit/nscombobox/1436747-numberofitems)Removed [-[NSComboBox numberOfVisibleItems]](https://developer.apple.com/documentation/appkit/nscombobox/1436741-numberofvisibleitems)Removed [-[NSComboBox objectValueOfSelectedItem]](https://developer.apple.com/documentation/appkit/nscombobox/1436743-objectvalueofselecteditem)Removed [-[NSComboBox objectValues]](https://developer.apple.com/documentation/appkit/nscombobox/1436709-objectvalues)Removed [-[NSComboBox setButtonBordered:]](https://developer.apple.com/documentation/appkit/nscombobox/1436711-buttonbordered)Removed [-[NSComboBox setCompletes:]](https://developer.apple.com/documentation/appkit/nscombobox/1436749-completes)Removed [-[NSComboBox setDataSource:]](https://developer.apple.com/documentation/appkit/nscombobox/1436729-datasource)Removed [-[NSComboBox setHasVerticalScroller:]](https://developer.apple.com/documentation/appkit/nscombobox/1436705-hasverticalscroller)Removed [-[NSComboBox setIntercellSpacing:]](https://developer.apple.com/documentation/appkit/nscombobox/1436771-intercellspacing)Removed [-[NSComboBox setItemHeight:]](https://developer.apple.com/documentation/appkit/nscombobox/1436767-itemheight)Removed [-[NSComboBox setNumberOfVisibleItems:]](https://developer.apple.com/documentation/appkit/nscombobox/1436741-numberofvisibleitems)Removed [-[NSComboBox setUsesDataSource:]](https://developer.apple.com/documentation/appkit/nscombobox/1436727-usesdatasource)Removed [-[NSComboBox usesDataSource]](https://developer.apple.com/documentation/appkit/nscombobox/1436727-usesdatasource)Added [NSComboBox.buttonBordered](https://developer.apple.com/documentation/appkit/nscombobox/1436711-buttonbordered)Added [NSComboBox.completes](https://developer.apple.com/documentation/appkit/nscombobox/1436749-completes)Added [NSComboBox.dataSource](https://developer.apple.com/documentation/appkit/nscombobox/1436729-datasource)Added [NSComboBox.hasVerticalScroller](https://developer.apple.com/documentation/appkit/nscombobox/1436705-hasverticalscroller)Added [NSComboBox.indexOfSelectedItem](https://developer.apple.com/documentation/appkit/nscombobox/1436701-indexofselecteditem)Added [NSComboBox.intercellSpacing](https://developer.apple.com/documentation/appkit/nscombobox/1436771-intercellspacing)Added [NSComboBox.itemHeight](https://developer.apple.com/documentation/appkit/nscombobox/1436767-itemheight)Added [NSComboBox.numberOfItems](https://developer.apple.com/documentation/appkit/nscombobox/1436747-numberofitems)Added [NSComboBox.numberOfVisibleItems](https://developer.apple.com/documentation/appkit/nscombobox/1436741-numberofvisibleitems)Added [NSComboBox.objectValueOfSelectedItem](https://developer.apple.com/documentation/appkit/nscombobox/1436743-objectvalueofselecteditem)Added [NSComboBox.objectValues](https://developer.apple.com/documentation/appkit/nscombobox/1436709-objectvalues)Added [NSComboBox.usesDataSource](https://developer.apple.com/documentation/appkit/nscombobox/1436727-usesdatasource)Modified [-[NSComboBoxDataSource comboBox:completedString:]](https://developer.apple.com/documentation/appkit/nscomboboxdatasource/1436733-combobox)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSComboBoxDataSource comboBox:indexOfItemWithStringValue:]](https://developer.apple.com/documentation/appkit/nscomboboxdatasource/1436713-combobox)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSComboBoxDataSource comboBox:objectValueForItemAtIndex:]](https://developer.apple.com/documentation/appkit/nscomboboxdatasource/1436753-combobox)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSComboBoxDataSource numberOfItemsInComboBox:]](https://developer.apple.com/documentation/appkit/nscomboboxdatasource/1436780-numberofitems)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSComboBoxDelegate comboBoxSelectionDidChange:]](https://developer.apple.com/documentation/appkit/nscomboboxdelegate/1436769-comboboxselectiondidchange)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSComboBoxDelegate comboBoxSelectionIsChanging:]](https://developer.apple.com/documentation/appkit/nscomboboxdelegate/1436715-comboboxselectionischanging)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSComboBoxDelegate comboBoxWillDismiss:]](https://developer.apple.com/documentation/appkit/nscomboboxdelegate/1436763-comboboxwilldismiss)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSComboBoxDelegate comboBoxWillPopUp:]](https://developer.apple.com/documentation/appkit/nscomboboxdelegate/1436784-comboboxwillpopup)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSComboBoxCell.hRemoved [-[NSComboBoxCell completes]](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410262-completes)Removed [-[NSComboBoxCell dataSource]](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410266-datasource)Removed [-[NSComboBoxCell hasVerticalScroller]](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410252-hasverticalscroller)Removed [-[NSComboBoxCell indexOfSelectedItem]](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410274-indexofselecteditem)Removed [-[NSComboBoxCell intercellSpacing]](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410270-intercellspacing)Removed [-[NSComboBoxCell isButtonBordered]](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410246-buttonbordered)Removed [-[NSComboBoxCell itemHeight]](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410306-itemheight)Removed [-[NSComboBoxCell numberOfItems]](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410260-numberofitems)Removed [-[NSComboBoxCell numberOfVisibleItems]](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410298-numberofvisibleitems)Removed [-[NSComboBoxCell objectValueOfSelectedItem]](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410278-objectvalueofselecteditem)Removed [-[NSComboBoxCell objectValues]](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410304-objectvalues)Removed [-[NSComboBoxCell setButtonBordered:]](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410246-buttonbordered)Removed [-[NSComboBoxCell setCompletes:]](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410262-completes)Removed [-[NSComboBoxCell setDataSource:]](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410266-datasource)Removed [-[NSComboBoxCell setHasVerticalScroller:]](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410252-hasverticalscroller)Removed [-[NSComboBoxCell setIntercellSpacing:]](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410270-intercellspacing)Removed [-[NSComboBoxCell setItemHeight:]](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410306-itemheight)Removed [-[NSComboBoxCell setNumberOfVisibleItems:]](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410298-numberofvisibleitems)Removed [-[NSComboBoxCell setUsesDataSource:]](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410254-usesdatasource)Removed [-[NSComboBoxCell usesDataSource]](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410254-usesdatasource)Added [NSComboBoxCell.buttonBordered](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410246-buttonbordered)Added [NSComboBoxCell.completes](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410262-completes)Added [NSComboBoxCell.dataSource](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410266-datasource)Added [NSComboBoxCell.hasVerticalScroller](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410252-hasverticalscroller)Added [NSComboBoxCell.indexOfSelectedItem](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410274-indexofselecteditem)Added [NSComboBoxCell.intercellSpacing](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410270-intercellspacing)Added [NSComboBoxCell.itemHeight](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410306-itemheight)Added [NSComboBoxCell.numberOfItems](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410260-numberofitems)Added [NSComboBoxCell.numberOfVisibleItems](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410298-numberofvisibleitems)Added [NSComboBoxCell.objectValueOfSelectedItem](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410278-objectvalueofselecteditem)Added [NSComboBoxCell.objectValues](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410304-objectvalues)Added [NSComboBoxCell.usesDataSource](https://developer.apple.com/documentation/appkit/nscomboboxcell/1410254-usesdatasource)Modified [-[NSComboBoxCellDataSource comboBoxCell:completedString:]](https://developer.apple.com/documentation/appkit/nscomboboxcelldatasource/1410250-comboboxcell)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSComboBoxCellDataSource comboBoxCell:indexOfItemWithStringValue:]](https://developer.apple.com/documentation/appkit/nscomboboxcelldatasource/1410285-comboboxcell)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSComboBoxCellDataSource comboBoxCell:objectValueForItemAtIndex:]](https://developer.apple.com/documentation/appkit/nscomboboxcelldatasource/1410258-comboboxcell)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSComboBoxCellDataSource numberOfItemsInComboBoxCell:]](https://developer.apple.com/documentation/appkit/nscomboboxcelldatasource/1410302-numberofitems)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSControl.hRemoved [-[NSControl action]](https://developer.apple.com/documentation/appkit/nscontrol/1428956-action)Removed [-[NSControl alignment]](https://developer.apple.com/documentation/appkit/nscontrol/1428906-alignment)Removed [-[NSControl allowsExpansionToolTips]](https://developer.apple.com/documentation/appkit/nscontrol/1428962-allowsexpansiontooltips)Removed [-[NSControl attributedStringValue]](https://developer.apple.com/documentation/appkit/nscontrol/1428916-attributedstringvalue)Removed [-[NSControl baseWritingDirection]](https://developer.apple.com/documentation/appkit/nscontrol/1428921-basewritingdirection)Removed [-[NSControl doubleValue]](https://developer.apple.com/documentation/appkit/nscontrol/1428942-doublevalue)Removed [-[NSControl floatValue]](https://developer.apple.com/documentation/appkit/nscontrol/1428889-floatvalue)Removed [-[NSControl font]](https://developer.apple.com/documentation/appkit/nscontrol/1428914-font)Removed [-[NSControl formatter]](https://developer.apple.com/documentation/appkit/nscontrol/1428887-formatter)Removed [-[NSControl ignoresMultiClick]](https://developer.apple.com/documentation/appkit/nscontrol/1428863-ignoresmulticlick)Removed [-[NSControl intValue]](https://developer.apple.com/documentation/appkit/nscontrol/1428939-intvalue)Removed [-[NSControl integerValue]](https://developer.apple.com/documentation/appkit/nscontrol/1428969-integervalue)Removed [-[NSControl isContinuous]](https://developer.apple.com/documentation/appkit/nscontrol/1428952-iscontinuous)Removed [-[NSControl isEnabled]](https://developer.apple.com/documentation/appkit/nscontrol/1428970-enabled)Removed [-[NSControl objectValue]](https://developer.apple.com/documentation/appkit/nscontrol/1428849-objectvalue)Removed [-[NSControl setAction:]](https://developer.apple.com/documentation/appkit/nscontrol/1428956-action)Removed [-[NSControl setAlignment:]](https://developer.apple.com/documentation/appkit/nscontrol/1428906-alignment)Removed [-[NSControl setAllowsExpansionToolTips:]](https://developer.apple.com/documentation/appkit/nscontrol/1428962-allowsexpansiontooltips)Removed [-[NSControl setAttributedStringValue:]](https://developer.apple.com/documentation/appkit/nscontrol/1428916-attributedstringvalue)Removed [-[NSControl setBaseWritingDirection:]](https://developer.apple.com/documentation/appkit/nscontrol/1428921-basewritingdirection)Removed [-[NSControl setContinuous:]](https://developer.apple.com/documentation/appkit/nscontrol/1428952-iscontinuous)Removed [-[NSControl setDoubleValue:]](https://developer.apple.com/documentation/appkit/nscontrol/1428942-doublevalue)Removed [-[NSControl setEnabled:]](https://developer.apple.com/documentation/appkit/nscontrol/1428970-enabled)Removed [-[NSControl setFloatValue:]](https://developer.apple.com/documentation/appkit/nscontrol/1428889-floatvalue)Removed [-[NSControl setFont:]](https://developer.apple.com/documentation/appkit/nscontrol/1428914-font)Removed [-[NSControl setFormatter:]](https://developer.apple.com/documentation/appkit/nscontrol/1428887-formatter)Removed [-[NSControl setIgnoresMultiClick:]](https://developer.apple.com/documentation/appkit/nscontrol/1428863-ignoresmulticlick)Removed [-[NSControl setIntValue:]](https://developer.apple.com/documentation/appkit/nscontrol/1428939-intvalue)Removed [-[NSControl setIntegerValue:]](https://developer.apple.com/documentation/appkit/nscontrol/1428969-integervalue)Removed [-[NSControl setObjectValue:]](https://developer.apple.com/documentation/appkit/nscontrol/1428849-objectvalue)Removed [-[NSControl setStringValue:]](https://developer.apple.com/documentation/appkit/nscontrol/1428950-stringvalue)Removed [-[NSControl setTag:]](https://developer.apple.com/documentation/appkit/nscontrol/1428910-tag)Removed [-[NSControl setTarget:]](https://developer.apple.com/documentation/appkit/nscontrol/1428885-target)Removed -[NSControl setUserInterfaceLayoutDirection:]Removed [-[NSControl stringValue]](https://developer.apple.com/documentation/appkit/nscontrol/1428950-stringvalue)Removed [-[NSControl tag]](https://developer.apple.com/documentation/appkit/nscontrol/1428910-tag)Removed [-[NSControl target]](https://developer.apple.com/documentation/appkit/nscontrol/1428885-target)Removed -[NSControl userInterfaceLayoutDirection]Removed NSControl(NSControlAttributedStringMethods)Added [NSControl.action](https://developer.apple.com/documentation/appkit/nscontrol/1428956-action)Added [NSControl.alignment](https://developer.apple.com/documentation/appkit/nscontrol/1428906-alignment)Added [NSControl.allowsExpansionToolTips](https://developer.apple.com/documentation/appkit/nscontrol/1428962-allowsexpansiontooltips)Added [NSControl.attributedStringValue](https://developer.apple.com/documentation/appkit/nscontrol/1428916-attributedstringvalue)Added [NSControl.baseWritingDirection](https://developer.apple.com/documentation/appkit/nscontrol/1428921-basewritingdirection)Added [NSControl.continuous](https://developer.apple.com/documentation/appkit/nscontrol/1428952-iscontinuous)Added [NSControl.controlSize](https://developer.apple.com/documentation/appkit/nscontrol/1428871-controlsize)Added [NSControl.doubleValue](https://developer.apple.com/documentation/appkit/nscontrol/1428942-doublevalue)Added [-[NSControl drawWithExpansionFrame:inView:]](https://developer.apple.com/documentation/appkit/nscontrol/1428895-drawwithexpansionframe)Added [-[NSControl editWithFrame:editor:delegate:event:]](https://developer.apple.com/documentation/appkit/nscontrol/1428919-edit)Added [NSControl.enabled](https://developer.apple.com/documentation/appkit/nscontrol/1428970-isenabled)Added [-[NSControl endEditing:]](https://developer.apple.com/documentation/appkit/nscontrol/1428936-endediting)Added [-[NSControl expansionFrameWithFrame:]](https://developer.apple.com/documentation/appkit/nscontrol/1428932-expansionframewithframe)Added [NSControl.floatValue](https://developer.apple.com/documentation/appkit/nscontrol/1428889-floatvalue)Added [NSControl.font](https://developer.apple.com/documentation/appkit/nscontrol/1428914-font)Added [NSControl.formatter](https://developer.apple.com/documentation/appkit/nscontrol/1428887-formatter)Added [NSControl.highlighted](https://developer.apple.com/documentation/appkit/nscontrol/1428927-ishighlighted)Added [NSControl.ignoresMultiClick](https://developer.apple.com/documentation/appkit/nscontrol/1428863-ignoresmulticlick)Added [-[NSControl initWithCoder:]](https://developer.apple.com/documentation/appkit/nscontrol/1428861-initwithcoder)Added [NSControl.intValue](https://developer.apple.com/documentation/appkit/nscontrol/1428939-intvalue)Added [NSControl.integerValue](https://developer.apple.com/documentation/appkit/nscontrol/1428969-integervalue)Added [NSControl.lineBreakMode](https://developer.apple.com/documentation/appkit/nscontrol/1428978-linebreakmode)Added [NSControl.objectValue](https://developer.apple.com/documentation/appkit/nscontrol/1428849-objectvalue)Added [NSControl.refusesFirstResponder](https://developer.apple.com/documentation/appkit/nscontrol/1428976-refusesfirstresponder)Added [-[NSControl selectWithFrame:editor:delegate:start:length:]](https://developer.apple.com/documentation/appkit/nscontrol/1428968-selectwithframe)Added [-[NSControl sizeThatFits:]](https://developer.apple.com/documentation/appkit/nscontrol/1428902-sizethatfits)Added [NSControl.stringValue](https://developer.apple.com/documentation/appkit/nscontrol/1428950-stringvalue)Added [NSControl.tag](https://developer.apple.com/documentation/appkit/nscontrol/1428910-tag)Added [NSControl.target](https://developer.apple.com/documentation/appkit/nscontrol/1428885-target)Added [NSControl.usesSingleLineMode](https://developer.apple.com/documentation/appkit/nscontrol/1428929-usessinglelinemode)Added NSControl(NSControlEditableTextMethods)Added NSControl(NSControlTextMethods)Modified [-[NSControl calcSize]](https://developer.apple.com/documentation/appkit/nscontrol/1428857-calcsize)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSControl cell]](https://developer.apple.com/documentation/appkit/nscontrol/1428960-cell)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[NSControl cellClass]](https://developer.apple.com/documentation/appkit/nscontrol/1428891-cellclass)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSControl drawCell:]](https://developer.apple.com/documentation/appkit/nscontrol/1428869-drawcell)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSControl drawCellInside:]](https://developer.apple.com/documentation/appkit/nscontrol/1428881-drawcellinside)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSControl initWithFrame:]](https://developer.apple.com/documentation/appkit/nscontrol/1428900-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithFrame:(NSRect)frameRect ``` | -- |
| To | ``` - (instancetype)initWithFrame:(NSRect)frameRect ``` | yes |

Modified [-[NSControl selectCell:]](https://developer.apple.com/documentation/appkit/nscontrol/1428966-selectcell)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSControl selectedCell]](https://developer.apple.com/documentation/appkit/nscontrol/1428964-selectedcell)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSControl selectedTag]](https://developer.apple.com/documentation/appkit/nscontrol/1428845-selectedtag)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSControl setCell:]](https://developer.apple.com/documentation/appkit/nscontrol/1428960-cell)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified +[NSControl setCellClass:]

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSControl setNeedsDisplay]](https://developer.apple.com/documentation/appkit/nscontrol/1428879-setneedsdisplay)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSControl updateCell:]](https://developer.apple.com/documentation/appkit/nscontrol/1428893-updatecell)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSControl updateCellInside:]](https://developer.apple.com/documentation/appkit/nscontrol/1428923-updatecellinside)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSControlTextEditingDelegate control:didFailToFormatString:errorDescription:]](https://developer.apple.com/documentation/appkit/nscontroltexteditingdelegate/1428883-control)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSControlTextEditingDelegate control:didFailToValidatePartialString:errorDescription:]](https://developer.apple.com/documentation/appkit/nscontroltexteditingdelegate/1428941-control)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSControlTextEditingDelegate control:isValidObject:]](https://developer.apple.com/documentation/appkit/nscontroltexteditingdelegate/1428873-control)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSControlTextEditingDelegate control:textShouldBeginEditing:]](https://developer.apple.com/documentation/appkit/nscontroltexteditingdelegate/1428865-control)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSControlTextEditingDelegate control:textShouldEndEditing:]](https://developer.apple.com/documentation/appkit/nscontroltexteditingdelegate/1428984-control)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSControlTextEditingDelegate control:textView:completions:forPartialWordRange:indexOfSelectedItem:]](https://developer.apple.com/documentation/appkit/nscontroltexteditingdelegate/1428925-control)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSControlTextEditingDelegate control:textView:doCommandBySelector:]](https://developer.apple.com/documentation/appkit/nscontroltexteditingdelegate/1428898-control)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSController.hRemoved [-[NSController isEditing]](https://developer.apple.com/documentation/appkit/nscontroller/1527136-editing)Added [NSController.editing](https://developer.apple.com/documentation/appkit/nscontroller/1527136-editing)Added [-[NSController init]](https://developer.apple.com/documentation/appkit/nscontroller/1528092-init)Added [-[NSController initWithCoder:]](https://developer.apple.com/documentation/appkit/nscontroller/1525048-init)NSCursor.hRemoved [-[NSCursor hotSpot]](https://developer.apple.com/documentation/appkit/nscursor/1529096-hotspot)Removed [-[NSCursor image]](https://developer.apple.com/documentation/appkit/nscursor/1527062-image)Removed -[NSCursor isSetOnMouseEntered]Removed -[NSCursor isSetOnMouseExited]Added [NSCursor.hotSpot](https://developer.apple.com/documentation/appkit/nscursor/1529096-hotspot)Added [NSCursor.image](https://developer.apple.com/documentation/appkit/nscursor/1527062-image)Added [NSCursor.setOnMouseEntered](https://developer.apple.com/documentation/appkit/nscursor/1525108-issetonmouseentered)Added [NSCursor.setOnMouseExited](https://developer.apple.com/documentation/appkit/nscursor/1532492-setonmouseexited)Modified [-[NSCursor initWithImage:foregroundColorHint:backgroundColorHint:hotSpot:]](https://developer.apple.com/documentation/appkit/nscursor/1524604-initwithimage)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithImage:(NSImage *)newImage foregroundColorHint:(NSColor *)fg backgroundColorHint:(NSColor *)bg hotSpot:(NSPoint)hotSpot ``` |
| To | ``` - (instancetype)initWithImage:(NSImage *)newImage foregroundColorHint:(NSColor *)fg backgroundColorHint:(NSColor *)bg hotSpot:(NSPoint)hotSpot ``` |

Modified [-[NSCursor initWithImage:hotSpot:]](https://developer.apple.com/documentation/appkit/nscursor/1524612-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithImage:(NSImage *)newImage hotSpot:(NSPoint)aPoint ``` |
| To | ``` - (instancetype)initWithImage:(NSImage *)newImage hotSpot:(NSPoint)aPoint ``` |

NSCustomImageRep.hRemoved [-[NSCustomImageRep delegate]](https://developer.apple.com/documentation/appkit/nscustomimagerep/1534716-delegate)Removed [-[NSCustomImageRep drawSelector]](https://developer.apple.com/documentation/appkit/nscustomimagerep/1529935-drawselector)Removed [-[NSCustomImageRep drawingHandler]](https://developer.apple.com/documentation/appkit/nscustomimagerep/1527316-drawinghandler)Added [NSCustomImageRep.delegate](https://developer.apple.com/documentation/appkit/nscustomimagerep/1534716-delegate)Added [NSCustomImageRep.drawSelector](https://developer.apple.com/documentation/appkit/nscustomimagerep/1529935-drawselector)Added [NSCustomImageRep.drawingHandler](https://developer.apple.com/documentation/appkit/nscustomimagerep/1527316-drawinghandler)Modified [-[NSCustomImageRep initWithDrawSelector:delegate:]](https://developer.apple.com/documentation/appkit/nscustomimagerep/1533328-initwithdrawselector)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDrawSelector:(SEL)aMethod delegate:(id)anObject ``` |
| To | ``` - (instancetype)initWithDrawSelector:(SEL)aMethod delegate:(id)anObject ``` |

Modified [-[NSCustomImageRep initWithSize:flipped:drawingHandler:]](https://developer.apple.com/documentation/appkit/nscustomimagerep/1526521-initwithsize)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithSize:(NSSize)size flipped:(BOOL)drawingHandlerShouldBeCalledWithFlippedContext drawingHandler:(BOOL (^)(NSRect dstRect))drawingHandler ``` |
| To | ``` - (instancetype)initWithSize:(NSSize)size flipped:(BOOL)drawingHandlerShouldBeCalledWithFlippedContext drawingHandler:(BOOL (^)(NSRect dstRect))drawingHandler ``` |

NSDatePicker.hRemoved [-[NSDatePicker backgroundColor]](https://developer.apple.com/documentation/appkit/nsdatepicker/1527710-backgroundcolor)Removed [-[NSDatePicker calendar]](https://developer.apple.com/documentation/appkit/nsdatepicker/1533591-calendar)Removed [-[NSDatePicker datePickerElements]](https://developer.apple.com/documentation/appkit/nsdatepicker/1533480-datepickerelements)Removed [-[NSDatePicker datePickerMode]](https://developer.apple.com/documentation/appkit/nsdatepicker/1527214-datepickermode)Removed [-[NSDatePicker datePickerStyle]](https://developer.apple.com/documentation/appkit/nsdatepicker/1528570-datepickerstyle)Removed [-[NSDatePicker dateValue]](https://developer.apple.com/documentation/appkit/nsdatepicker/1527606-datevalue)Removed [-[NSDatePicker delegate]](https://developer.apple.com/documentation/appkit/nsdatepicker/1533878-delegate)Removed [-[NSDatePicker drawsBackground]](https://developer.apple.com/documentation/appkit/nsdatepicker/1528266-drawsbackground)Removed [-[NSDatePicker isBezeled]](https://developer.apple.com/documentation/appkit/nsdatepicker/1533534-bezeled)Removed [-[NSDatePicker isBordered]](https://developer.apple.com/documentation/appkit/nsdatepicker/1534176-isbordered)Removed [-[NSDatePicker locale]](https://developer.apple.com/documentation/appkit/nsdatepicker/1525940-locale)Removed [-[NSDatePicker maxDate]](https://developer.apple.com/documentation/appkit/nsdatepicker/1535887-maxdate)Removed [-[NSDatePicker minDate]](https://developer.apple.com/documentation/appkit/nsdatepicker/1526893-mindate)Removed [-[NSDatePicker setBackgroundColor:]](https://developer.apple.com/documentation/appkit/nsdatepicker/1527710-backgroundcolor)Removed [-[NSDatePicker setBezeled:]](https://developer.apple.com/documentation/appkit/nsdatepicker/1533534-bezeled)Removed [-[NSDatePicker setBordered:]](https://developer.apple.com/documentation/appkit/nsdatepicker/1534176-bordered)Removed [-[NSDatePicker setCalendar:]](https://developer.apple.com/documentation/appkit/nsdatepicker/1533591-calendar)Removed [-[NSDatePicker setDatePickerElements:]](https://developer.apple.com/documentation/appkit/nsdatepicker/1533480-datepickerelements)Removed [-[NSDatePicker setDatePickerMode:]](https://developer.apple.com/documentation/appkit/nsdatepicker/1527214-datepickermode)Removed [-[NSDatePicker setDatePickerStyle:]](https://developer.apple.com/documentation/appkit/nsdatepicker/1528570-datepickerstyle)Removed [-[NSDatePicker setDateValue:]](https://developer.apple.com/documentation/appkit/nsdatepicker/1527606-datevalue)Removed [-[NSDatePicker setDelegate:]](https://developer.apple.com/documentation/appkit/nsdatepicker/1533878-delegate)Removed [-[NSDatePicker setDrawsBackground:]](https://developer.apple.com/documentation/appkit/nsdatepicker/1528266-drawsbackground)Removed [-[NSDatePicker setLocale:]](https://developer.apple.com/documentation/appkit/nsdatepicker/1525940-locale)Removed [-[NSDatePicker setMaxDate:]](https://developer.apple.com/documentation/appkit/nsdatepicker/1535887-maxdate)Removed [-[NSDatePicker setMinDate:]](https://developer.apple.com/documentation/appkit/nsdatepicker/1526893-mindate)Removed [-[NSDatePicker setTextColor:]](https://developer.apple.com/documentation/appkit/nsdatepicker/1534294-textcolor)Removed [-[NSDatePicker setTimeInterval:]](https://developer.apple.com/documentation/appkit/nsdatepicker/1526681-timeinterval)Removed [-[NSDatePicker setTimeZone:]](https://developer.apple.com/documentation/appkit/nsdatepicker/1535451-timezone)Removed [-[NSDatePicker textColor]](https://developer.apple.com/documentation/appkit/nsdatepicker/1534294-textcolor)Removed [-[NSDatePicker timeInterval]](https://developer.apple.com/documentation/appkit/nsdatepicker/1526681-timeinterval)Removed [-[NSDatePicker timeZone]](https://developer.apple.com/documentation/appkit/nsdatepicker/1535451-timezone)Added [NSDatePicker.backgroundColor](https://developer.apple.com/documentation/appkit/nsdatepicker/1527710-backgroundcolor)Added [NSDatePicker.bezeled](https://developer.apple.com/documentation/appkit/nsdatepicker/1533534-bezeled)Added [NSDatePicker.bordered](https://developer.apple.com/documentation/appkit/nsdatepicker/1534176-isbordered)Added [NSDatePicker.calendar](https://developer.apple.com/documentation/appkit/nsdatepicker/1533591-calendar)Added [NSDatePicker.datePickerElements](https://developer.apple.com/documentation/appkit/nsdatepicker/1533480-datepickerelements)Added [NSDatePicker.datePickerMode](https://developer.apple.com/documentation/appkit/nsdatepicker/1527214-datepickermode)Added [NSDatePicker.datePickerStyle](https://developer.apple.com/documentation/appkit/nsdatepicker/1528570-datepickerstyle)Added [NSDatePicker.dateValue](https://developer.apple.com/documentation/appkit/nsdatepicker/1527606-datevalue)Added [NSDatePicker.delegate](https://developer.apple.com/documentation/appkit/nsdatepicker/1533878-delegate)Added [NSDatePicker.drawsBackground](https://developer.apple.com/documentation/appkit/nsdatepicker/1528266-drawsbackground)Added [NSDatePicker.locale](https://developer.apple.com/documentation/appkit/nsdatepicker/1525940-locale)Added [NSDatePicker.maxDate](https://developer.apple.com/documentation/appkit/nsdatepicker/1535887-maxdate)Added [NSDatePicker.minDate](https://developer.apple.com/documentation/appkit/nsdatepicker/1526893-mindate)Added [NSDatePicker.textColor](https://developer.apple.com/documentation/appkit/nsdatepicker/1534294-textcolor)Added [NSDatePicker.timeInterval](https://developer.apple.com/documentation/appkit/nsdatepicker/1526681-timeinterval)Added [NSDatePicker.timeZone](https://developer.apple.com/documentation/appkit/nsdatepicker/1535451-timezone)NSDatePickerCell.hRemoved [-[NSDatePickerCell backgroundColor]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459629-backgroundcolor)Removed [-[NSDatePickerCell calendar]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459609-calendar)Removed [-[NSDatePickerCell datePickerElements]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459639-datepickerelements)Removed [-[NSDatePickerCell datePickerMode]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459602-datepickermode)Removed [-[NSDatePickerCell datePickerStyle]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459635-datepickerstyle)Removed [-[NSDatePickerCell dateValue]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459594-datevalue)Removed [-[NSDatePickerCell delegate]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459615-delegate)Removed [-[NSDatePickerCell drawsBackground]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459591-drawsbackground)Removed [-[NSDatePickerCell locale]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459625-locale)Removed [-[NSDatePickerCell maxDate]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459640-maxdate)Removed [-[NSDatePickerCell minDate]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459619-mindate)Removed [-[NSDatePickerCell setBackgroundColor:]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459629-backgroundcolor)Removed [-[NSDatePickerCell setCalendar:]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459609-calendar)Removed [-[NSDatePickerCell setDatePickerElements:]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459639-datepickerelements)Removed [-[NSDatePickerCell setDatePickerMode:]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459602-datepickermode)Removed [-[NSDatePickerCell setDatePickerStyle:]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459635-datepickerstyle)Removed [-[NSDatePickerCell setDateValue:]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459594-datevalue)Removed [-[NSDatePickerCell setDelegate:]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459615-delegate)Removed [-[NSDatePickerCell setDrawsBackground:]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459591-drawsbackground)Removed [-[NSDatePickerCell setLocale:]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459625-locale)Removed [-[NSDatePickerCell setMaxDate:]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459640-maxdate)Removed [-[NSDatePickerCell setMinDate:]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459619-mindate)Removed [-[NSDatePickerCell setTextColor:]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459644-textcolor)Removed [-[NSDatePickerCell setTimeInterval:]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459589-timeinterval)Removed [-[NSDatePickerCell setTimeZone:]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459633-timezone)Removed [-[NSDatePickerCell textColor]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459644-textcolor)Removed [-[NSDatePickerCell timeInterval]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459589-timeinterval)Removed [-[NSDatePickerCell timeZone]](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459633-timezone)Added [NSDatePickerCell.backgroundColor](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459629-backgroundcolor)Added [NSDatePickerCell.calendar](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459609-calendar)Added [NSDatePickerCell.datePickerElements](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459639-datepickerelements)Added [NSDatePickerCell.datePickerMode](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459602-datepickermode)Added [NSDatePickerCell.datePickerStyle](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459635-datepickerstyle)Added [NSDatePickerCell.dateValue](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459594-datevalue)Added [NSDatePickerCell.delegate](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459615-delegate)Added [NSDatePickerCell.drawsBackground](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459591-drawsbackground)Added [NSDatePickerCell.locale](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459625-locale)Added [NSDatePickerCell.maxDate](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459640-maxdate)Added [NSDatePickerCell.minDate](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459619-mindate)Added [NSDatePickerCell.textColor](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459644-textcolor)Added [NSDatePickerCell.timeInterval](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459589-timeinterval)Added [NSDatePickerCell.timeZone](https://developer.apple.com/documentation/appkit/nsdatepickercell/1459633-timezone)Modified [-[NSDatePickerCellDelegate datePickerCell:validateProposedDateValue:timeInterval:]](https://developer.apple.com/documentation/appkit/nsdatepickercelldelegate/1459631-datepickercell)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSDictionaryController.hRemoved [-[NSDictionaryController excludedKeys]](https://developer.apple.com/documentation/appkit/nsdictionarycontroller/1535356-excludedkeys)Removed [-[NSDictionaryController includedKeys]](https://developer.apple.com/documentation/appkit/nsdictionarycontroller/1525172-includedkeys)Removed [-[NSDictionaryController initialKey]](https://developer.apple.com/documentation/appkit/nsdictionarycontroller/1530444-initialkey)Removed [-[NSDictionaryController initialValue]](https://developer.apple.com/documentation/appkit/nsdictionarycontroller/1535925-initialvalue)Removed [-[NSDictionaryController localizedKeyDictionary]](https://developer.apple.com/documentation/appkit/nsdictionarycontroller/1532944-localizedkeydictionary)Removed [-[NSDictionaryController localizedKeyTable]](https://developer.apple.com/documentation/appkit/nsdictionarycontroller/1524332-localizedkeytable)Removed [-[NSDictionaryController setExcludedKeys:]](https://developer.apple.com/documentation/appkit/nsdictionarycontroller/1535356-excludedkeys)Removed [-[NSDictionaryController setIncludedKeys:]](https://developer.apple.com/documentation/appkit/nsdictionarycontroller/1525172-includedkeys)Removed [-[NSDictionaryController setInitialKey:]](https://developer.apple.com/documentation/appkit/nsdictionarycontroller/1530444-initialkey)Removed [-[NSDictionaryController setInitialValue:]](https://developer.apple.com/documentation/appkit/nsdictionarycontroller/1535925-initialvalue)Removed [-[NSDictionaryController setLocalizedKeyDictionary:]](https://developer.apple.com/documentation/appkit/nsdictionarycontroller/1532944-localizedkeydictionary)Removed [-[NSDictionaryController setLocalizedKeyTable:]](https://developer.apple.com/documentation/appkit/nsdictionarycontroller/1524332-localizedkeytable)Added [NSDictionaryController.excludedKeys](https://developer.apple.com/documentation/appkit/nsdictionarycontroller/1535356-excludedkeys)Added [NSDictionaryController.includedKeys](https://developer.apple.com/documentation/appkit/nsdictionarycontroller/1525172-includedkeys)Added [NSDictionaryController.initialKey](https://developer.apple.com/documentation/appkit/nsdictionarycontroller/1530444-initialkey)Added [NSDictionaryController.initialValue](https://developer.apple.com/documentation/appkit/nsdictionarycontroller/1535925-initialvalue)Added [NSDictionaryController.localizedKeyDictionary](https://developer.apple.com/documentation/appkit/nsdictionarycontroller/1532944-localizedkeydictionary)Added [NSDictionaryController.localizedKeyTable](https://developer.apple.com/documentation/appkit/nsdictionarycontroller/1524332-localizedkeytable)NSDockTile.hRemoved [-[NSDockTile badgeLabel]](https://developer.apple.com/documentation/appkit/nsdocktile/1524433-badgelabel)Removed [-[NSDockTile contentView]](https://developer.apple.com/documentation/appkit/nsdocktile/1525995-contentview)Removed [-[NSDockTile owner]](https://developer.apple.com/documentation/appkit/nsdocktile/1533723-owner)Removed [-[NSDockTile setBadgeLabel:]](https://developer.apple.com/documentation/appkit/nsdocktile/1524433-badgelabel)Removed [-[NSDockTile setContentView:]](https://developer.apple.com/documentation/appkit/nsdocktile/1525995-contentview)Removed [-[NSDockTile setShowsApplicationBadge:]](https://developer.apple.com/documentation/appkit/nsdocktile/1528057-showsapplicationbadge)Removed [-[NSDockTile showsApplicationBadge]](https://developer.apple.com/documentation/appkit/nsdocktile/1528057-showsapplicationbadge)Removed [-[NSDockTile size]](https://developer.apple.com/documentation/appkit/nsdocktile/1534239-size)Added [NSDockTile.badgeLabel](https://developer.apple.com/documentation/appkit/nsdocktile/1524433-badgelabel)Added [NSDockTile.contentView](https://developer.apple.com/documentation/appkit/nsdocktile/1525995-contentview)Added [NSDockTile.owner](https://developer.apple.com/documentation/appkit/nsdocktile/1533723-owner)Added [NSDockTile.showsApplicationBadge](https://developer.apple.com/documentation/appkit/nsdocktile/1528057-showsapplicationbadge)Added [NSDockTile.size](https://developer.apple.com/documentation/appkit/nsdocktile/1534239-size)Modified [-[NSDockTilePlugIn dockMenu]](https://developer.apple.com/documentation/appkit/nsdocktileplugin/1527547-dockmenu)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSDocument.hRemoved [-[NSDocument PDFPrintOperation]](https://developer.apple.com/documentation/appkit/nsdocument/1515246-pdfprintoperation)Removed [-[NSDocument autosavedContentsFileURL]](https://developer.apple.com/documentation/appkit/nsdocument/1515232-autosavedcontentsfileurl)Removed [-[NSDocument autosavingFileType]](https://developer.apple.com/documentation/appkit/nsdocument/1515136-autosavingfiletype)Removed [-[NSDocument autosavingIsImplicitlyCancellable]](https://developer.apple.com/documentation/appkit/nsdocument/1515149-autosavingisimplicitlycancellabl)Removed [-[NSDocument backupFileURL]](https://developer.apple.com/documentation/appkit/nsdocument/1515200-backupfileurl)Removed [-[NSDocument displayName]](https://developer.apple.com/documentation/appkit/nsdocument/1515077-displayname)Removed [-[NSDocument fileModificationDate]](https://developer.apple.com/documentation/appkit/nsdocument/1515039-filemodificationdate)Removed [-[NSDocument fileNameExtensionWasHiddenInLastRunSavePanel]](https://developer.apple.com/documentation/appkit/nsdocument/1515092-filenameextensionwashiddeninlast)Removed [-[NSDocument fileType]](https://developer.apple.com/documentation/appkit/nsdocument/1515121-filetype)Removed [-[NSDocument fileTypeFromLastRunSavePanel]](https://developer.apple.com/documentation/appkit/nsdocument/1515240-filetypefromlastrunsavepanel)Removed [-[NSDocument fileURL]](https://developer.apple.com/documentation/appkit/nsdocument/1515038-fileurl)Removed [-[NSDocument hasUnautosavedChanges]](https://developer.apple.com/documentation/appkit/nsdocument/1515079-hasunautosavedchanges)Removed [-[NSDocument hasUndoManager]](https://developer.apple.com/documentation/appkit/nsdocument/1515103-hasundomanager)Removed [-[NSDocument isDocumentEdited]](https://developer.apple.com/documentation/appkit/nsdocument/1515091-documentedited)Removed [-[NSDocument isDraft]](https://developer.apple.com/documentation/appkit/nsdocument/1515065-isdraft)Removed [-[NSDocument isEntireFileLoaded]](https://developer.apple.com/documentation/appkit/nsdocument/1515053-isentirefileloaded)Removed [-[NSDocument isInViewingMode]](https://developer.apple.com/documentation/appkit/nsdocument/1515086-inviewingmode)Removed [-[NSDocument isLocked]](https://developer.apple.com/documentation/appkit/nsdocument/1515212-locked)Removed [-[NSDocument keepBackupFile]](https://developer.apple.com/documentation/appkit/nsdocument/1515060-keepbackupfile)Removed [-[NSDocument printInfo]](https://developer.apple.com/documentation/appkit/nsdocument/1515163-printinfo)Removed [-[NSDocument setAutosavedContentsFileURL:]](https://developer.apple.com/documentation/appkit/nsdocument/1515232-autosavedcontentsfileurl)Removed [-[NSDocument setDraft:]](https://developer.apple.com/documentation/appkit/nsdocument/1515065-draft)Removed [-[NSDocument setFileModificationDate:]](https://developer.apple.com/documentation/appkit/nsdocument/1515039-filemodificationdate)Removed [-[NSDocument setFileType:]](https://developer.apple.com/documentation/appkit/nsdocument/1515121-filetype)Removed [-[NSDocument setFileURL:]](https://developer.apple.com/documentation/appkit/nsdocument/1515038-fileurl)Removed [-[NSDocument setHasUndoManager:]](https://developer.apple.com/documentation/appkit/nsdocument/1515103-hasundomanager)Removed [-[NSDocument setPrintInfo:]](https://developer.apple.com/documentation/appkit/nsdocument/1515163-printinfo)Removed [-[NSDocument setUndoManager:]](https://developer.apple.com/documentation/appkit/nsdocument/1515166-undomanager)Removed [-[NSDocument shouldRunSavePanelWithAccessoryView]](https://developer.apple.com/documentation/appkit/nsdocument/1515183-shouldrunsavepanelwithaccessoryv)Removed [-[NSDocument undoManager]](https://developer.apple.com/documentation/appkit/nsdocument/1515166-undomanager)Removed [-[NSDocument windowControllers]](https://developer.apple.com/documentation/appkit/nsdocument/1515156-windowcontrollers)Removed [-[NSDocument windowForSheet]](https://developer.apple.com/documentation/appkit/nsdocument/1515064-windowforsheet)Removed [-[NSDocument windowNibName]](https://developer.apple.com/documentation/appkit/nsdocument/1515174-windownibname)Added [NSDocument.PDFPrintOperation](https://developer.apple.com/documentation/appkit/nsdocument/1515246-pdfprintoperation)Added [NSDocument.autosavedContentsFileURL](https://developer.apple.com/documentation/appkit/nsdocument/1515232-autosavedcontentsfileurl)Added [NSDocument.autosavingFileType](https://developer.apple.com/documentation/appkit/nsdocument/1515136-autosavingfiletype)Added [NSDocument.autosavingIsImplicitlyCancellable](https://developer.apple.com/documentation/appkit/nsdocument/1515149-autosavingisimplicitlycancellabl)Added [NSDocument.backupFileURL](https://developer.apple.com/documentation/appkit/nsdocument/1515200-backupfileurl)Added [NSDocument.displayName](https://developer.apple.com/documentation/appkit/nsdocument/1515077-displayname)Added [NSDocument.documentEdited](https://developer.apple.com/documentation/appkit/nsdocument/1515091-documentedited)Added [NSDocument.draft](https://developer.apple.com/documentation/appkit/nsdocument/1515065-draft)Added [NSDocument.entireFileLoaded](https://developer.apple.com/documentation/appkit/nsdocument/1515053-entirefileloaded)Added [NSDocument.fileModificationDate](https://developer.apple.com/documentation/appkit/nsdocument/1515039-filemodificationdate)Added [NSDocument.fileNameExtensionWasHiddenInLastRunSavePanel](https://developer.apple.com/documentation/appkit/nsdocument/1515092-filenameextensionwashiddeninlast)Added [NSDocument.fileType](https://developer.apple.com/documentation/appkit/nsdocument/1515121-filetype)Added [NSDocument.fileTypeFromLastRunSavePanel](https://developer.apple.com/documentation/appkit/nsdocument/1515240-filetypefromlastrunsavepanel)Added [NSDocument.fileURL](https://developer.apple.com/documentation/appkit/nsdocument/1515038-fileurl)Added [NSDocument.hasUnautosavedChanges](https://developer.apple.com/documentation/appkit/nsdocument/1515079-hasunautosavedchanges)Added [NSDocument.hasUndoManager](https://developer.apple.com/documentation/appkit/nsdocument/1515103-hasundomanager)Added [NSDocument.inViewingMode](https://developer.apple.com/documentation/appkit/nsdocument/1515086-isinviewingmode)Added [NSDocument.keepBackupFile](https://developer.apple.com/documentation/appkit/nsdocument/1515060-keepbackupfile)Added [NSDocument.locked](https://developer.apple.com/documentation/appkit/nsdocument/1515212-islocked)Added [NSDocument.printInfo](https://developer.apple.com/documentation/appkit/nsdocument/1515163-printinfo)Added [NSDocument.shouldRunSavePanelWithAccessoryView](https://developer.apple.com/documentation/appkit/nsdocument/1515183-shouldrunsavepanelwithaccessoryv)Added [NSDocument.undoManager](https://developer.apple.com/documentation/appkit/nsdocument/1515166-undomanager)Added [NSDocument.windowControllers](https://developer.apple.com/documentation/appkit/nsdocument/1515156-windowcontrollers)Added [NSDocument.windowForSheet](https://developer.apple.com/documentation/appkit/nsdocument/1515064-windowforsheet)Added [NSDocument.windowNibName](https://developer.apple.com/documentation/appkit/nsdocument/1515174-windownibname)Modified [-[NSDocument browseDocumentVersions:]](https://developer.apple.com/documentation/appkit/nsdocument/1515193-browsedocumentversions)

|  | Declaration |
| --- | --- |
| From | ``` - (void)browseDocumentVersions:(id)sender ``` |
| To | ``` - (IBAction)browseDocumentVersions:(id)sender ``` |

Modified [-[NSDocument duplicateDocument:]](https://developer.apple.com/documentation/appkit/nsdocument/1515226-duplicatedocument)

|  | Declaration |
| --- | --- |
| From | ``` - (void)duplicateDocument:(id)sender ``` |
| To | ``` - (IBAction)duplicateDocument:(id)sender ``` |

Modified [-[NSDocument init]](https://developer.apple.com/documentation/appkit/nsdocument/1515181-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)init ``` | -- |
| To | ``` - (instancetype)init ``` | yes |

Modified [-[NSDocument initForURL:withContentsOfURL:ofType:error:]](https://developer.apple.com/documentation/appkit/nsdocument/1515041-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initForURL:(NSURL *)urlOrNil withContentsOfURL:(NSURL *)contentsURL ofType:(NSString *)typeName error:(NSError **)outError ``` |
| To | ``` - (instancetype)initForURL:(NSURL *)urlOrNil withContentsOfURL:(NSURL *)contentsURL ofType:(NSString *)typeName error:(NSError **)outError ``` |

Modified [-[NSDocument initWithContentsOfURL:ofType:error:]](https://developer.apple.com/documentation/appkit/nsdocument/1515097-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)url ofType:(NSString *)typeName error:(NSError **)outError ``` |
| To | ``` - (instancetype)initWithContentsOfURL:(NSURL *)url ofType:(NSString *)typeName error:(NSError **)outError ``` |

Modified [-[NSDocument initWithType:error:]](https://developer.apple.com/documentation/appkit/nsdocument/1515159-initwithtype)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithType:(NSString *)typeName error:(NSError **)outError ``` |
| To | ``` - (instancetype)initWithType:(NSString *)typeName error:(NSError **)outError ``` |

Modified [-[NSDocument lockDocument:]](https://developer.apple.com/documentation/appkit/nsdocument/1515218-lock)

|  | Declaration |
| --- | --- |
| From | ``` - (void)lockDocument:(id)sender ``` |
| To | ``` - (IBAction)lockDocument:(id)sender ``` |

Modified [-[NSDocument moveDocument:]](https://developer.apple.com/documentation/appkit/nsdocument/1515118-move)

|  | Declaration |
| --- | --- |
| From | ``` - (void)moveDocument:(id)sender ``` |
| To | ``` - (IBAction)moveDocument:(id)sender ``` |

Modified [-[NSDocument moveDocumentToUbiquityContainer:]](https://developer.apple.com/documentation/appkit/nsdocument/1515210-movedocumenttoubiquitycontainer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)moveDocumentToUbiquityContainer:(id)sender ``` |
| To | ``` - (IBAction)moveDocumentToUbiquityContainer:(id)sender ``` |

Modified [-[NSDocument printDocument:]](https://developer.apple.com/documentation/appkit/nsdocument/1515154-printdocument)

|  | Declaration |
| --- | --- |
| From | ``` - (void)printDocument:(id)sender ``` |
| To | ``` - (IBAction)printDocument:(id)sender ``` |

Modified [-[NSDocument renameDocument:]](https://developer.apple.com/documentation/appkit/nsdocument/1515231-renamedocument)

|  | Declaration |
| --- | --- |
| From | ``` - (void)renameDocument:(id)sender ``` |
| To | ``` - (IBAction)renameDocument:(id)sender ``` |

Modified [-[NSDocument revertDocumentToSaved:]](https://developer.apple.com/documentation/appkit/nsdocument/1515059-reverttosaved)

|  | Declaration |
| --- | --- |
| From | ``` - (void)revertDocumentToSaved:(id)sender ``` |
| To | ``` - (IBAction)revertDocumentToSaved:(id)sender ``` |

Modified [-[NSDocument runPageLayout:]](https://developer.apple.com/documentation/appkit/nsdocument/1515140-runpagelayout)

|  | Declaration |
| --- | --- |
| From | ``` - (void)runPageLayout:(id)sender ``` |
| To | ``` - (IBAction)runPageLayout:(id)sender ``` |

Modified [-[NSDocument saveDocument:]](https://developer.apple.com/documentation/appkit/nsdocument/1515147-savedocument)

|  | Declaration |
| --- | --- |
| From | ``` - (void)saveDocument:(id)sender ``` |
| To | ``` - (IBAction)saveDocument:(id)sender ``` |

Modified [-[NSDocument saveDocumentAs:]](https://developer.apple.com/documentation/appkit/nsdocument/1515171-savedocumentas)

|  | Declaration |
| --- | --- |
| From | ``` - (void)saveDocumentAs:(id)sender ``` |
| To | ``` - (IBAction)saveDocumentAs:(id)sender ``` |

Modified [-[NSDocument saveDocumentTo:]](https://developer.apple.com/documentation/appkit/nsdocument/1515208-savedocumentto)

|  | Declaration |
| --- | --- |
| From | ``` - (void)saveDocumentTo:(id)sender ``` |
| To | ``` - (IBAction)saveDocumentTo:(id)sender ``` |

Modified [-[NSDocument saveDocumentToPDF:]](https://developer.apple.com/documentation/appkit/nsdocument/1515176-savedocumenttopdf)

|  | Declaration |
| --- | --- |
| From | ``` - (void)saveDocumentToPDF:(id)sender ``` |
| To | ``` - (IBAction)saveDocumentToPDF:(id)sender ``` |

Modified [-[NSDocument saveToURL:ofType:forSaveOperation:error:]](https://developer.apple.com/documentation/appkit/nsdocument/1515187-savetourl)

|  | Deprecation |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.6 |

Modified [-[NSDocument unlockDocument:]](https://developer.apple.com/documentation/appkit/nsdocument/1515068-unlock)

|  | Declaration |
| --- | --- |
| From | ``` - (void)unlockDocument:(id)sender ``` |
| To | ``` - (IBAction)unlockDocument:(id)sender ``` |

Modified [NSAutosaveOperation](https://developer.apple.com/documentation/appkit/nssaveoperationtype/nsautosaveoperation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

NSDocumentController.hRemoved [-[NSDocumentController URLsFromRunningOpenPanel]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514972-urlsfromrunningopenpanel)Removed [-[NSDocumentController autosavingDelay]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514953-autosavingdelay)Removed [-[NSDocumentController currentDirectory]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514942-currentdirectory)Removed [-[NSDocumentController currentDocument]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514957-currentdocument)Removed [-[NSDocumentController documentClassNames]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514988-documentclassnames)Removed [-[NSDocumentController documents]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1515003-documents)Removed [-[NSDocumentController hasEditedDocuments]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514964-hasediteddocuments)Removed [-[NSDocumentController maximumRecentDocumentCount]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514991-maximumrecentdocumentcount)Removed [-[NSDocumentController recentDocumentURLs]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514976-recentdocumenturls)Removed [-[NSDocumentController setAutosavingDelay:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514953-autosavingdelay)Added [NSDocumentController.URLsFromRunningOpenPanel](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514972-urlsfromrunningopenpanel)Added [NSDocumentController.autosavingDelay](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514953-autosavingdelay)Added [NSDocumentController.currentDirectory](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514942-currentdirectory)Added [NSDocumentController.currentDocument](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514957-currentdocument)Added [NSDocumentController.documentClassNames](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514988-documentclassnames)Added [NSDocumentController.documents](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1515003-documents)Added [NSDocumentController.hasEditedDocuments](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514964-hasediteddocuments)Added [-[NSDocumentController initWithCoder:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514955-init)Added [NSDocumentController.maximumRecentDocumentCount](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514991-maximumrecentdocumentcount)Added [NSDocumentController.recentDocumentURLs](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514976-recentdocumenturls)Modified [-[NSDocumentController clearRecentDocuments:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514933-clearrecentdocuments)

|  | Declaration |
| --- | --- |
| From | ``` - (void)clearRecentDocuments:(id)sender ``` |
| To | ``` - (IBAction)clearRecentDocuments:(id)sender ``` |

Modified [-[NSDocumentController init]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1515007-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)init ``` | -- |
| To | ``` - (instancetype)init ``` | yes |

Modified [-[NSDocumentController newDocument:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514997-newdocument)

|  | Declaration |
| --- | --- |
| From | ``` - (void)newDocument:(id)sender ``` |
| To | ``` - (IBAction)newDocument:(id)sender ``` |

Modified [-[NSDocumentController openDocument:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1515005-opendocument)

|  | Declaration |
| --- | --- |
| From | ``` - (void)openDocument:(id)sender ``` |
| To | ``` - (IBAction)openDocument:(id)sender ``` |

Modified [-[NSDocumentController saveAllDocuments:]](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1514959-savealldocuments)

|  | Declaration |
| --- | --- |
| From | ``` - (void)saveAllDocuments:(id)sender ``` |
| To | ``` - (IBAction)saveAllDocuments:(id)sender ``` |

NSDocumentScripting.hRemoved [-[NSDocument lastComponentOfFileName]](https://developer.apple.com/documentation/appkit/nsdocument/1500132-lastcomponentoffilename)Removed [-[NSDocument objectSpecifier]](https://developer.apple.com/documentation/appkit/nsdocument/1500134-objectspecifier)Removed [-[NSDocument setLastComponentOfFileName:]](https://developer.apple.com/documentation/appkit/nsdocument/1500132-lastcomponentoffilename)Added [NSDocument.lastComponentOfFileName](https://developer.apple.com/documentation/appkit/nsdocument/1500132-lastcomponentoffilename)Added [NSDocument.objectSpecifier](https://developer.apple.com/documentation/appkit/nsdocument/1500134-objectspecifier)NSDragging.hRemoved [#def NSDragOperationAll](https://developer.apple.com/documentation/appkit/nsdragginginfo/nsdragoperationall_deprecation/nsdragoperationall)Added [NSDragOperationAll](https://developer.apple.com/documentation/appkit/nsdragoperation/1415962-all)Modified [-[NSDraggingDestination concludeDragOperation:]](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1416010-concludedragoperation)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDraggingDestination draggingEnded:]](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1416096-draggingended)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDraggingDestination draggingEntered:]](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1416019-draggingentered)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDraggingDestination draggingExited:]](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1416056-draggingexited)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDraggingDestination draggingUpdated:]](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1415998-draggingupdated)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDraggingDestination performDragOperation:]](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1415970-performdragoperation)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDraggingDestination prepareForDragOperation:]](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1416066-preparefordragoperation)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDraggingDestination updateDraggingItemsForDrag:]](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1416050-updatedraggingitemsfordrag)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDraggingDestination wantsPeriodicDraggingUpdates]](https://developer.apple.com/documentation/appkit/nsdraggingdestination/1416049-wantsperiodicdraggingupdates)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDraggingSource draggingSession:endedAtPoint:operation:]](https://developer.apple.com/documentation/appkit/nsdraggingsource/1416017-draggingsession)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDraggingSource draggingSession:movedToPoint:]](https://developer.apple.com/documentation/appkit/nsdraggingsource/1416079-draggingsession)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDraggingSource draggingSession:willBeginAtPoint:]](https://developer.apple.com/documentation/appkit/nsdraggingsource/1415960-draggingsession)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDraggingSource ignoreModifierKeysForDraggingSession:]](https://developer.apple.com/documentation/appkit/nsdraggingsource/1415974-ignoremodifierkeys)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [NSDragOperationAll_Obsolete](https://developer.apple.com/documentation/appkit/nsdragoperation/nsdragoperationall_obsolete)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

NSDraggingItem.hModified [NSDraggingImageComponent.contents](https://developer.apple.com/documentation/appkit/nsdraggingimagecomponent/1529426-contents)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) id contents ``` |
| To | ``` @property(strong) id contents ``` |

Modified [+[NSDraggingImageComponent draggingImageComponentWithKey:]](https://developer.apple.com/documentation/appkit/nsdraggingimagecomponent/1557913-draggingimagecomponentwithkey)

|  | Declaration |
| --- | --- |
| From | ``` + (id)draggingImageComponentWithKey:(NSString *)key ``` |
| To | ``` + (NSDraggingImageComponent *)draggingImageComponentWithKey:(NSString *)key ``` |

Modified [-[NSDraggingImageComponent initWithKey:]](https://developer.apple.com/documentation/appkit/nsdraggingimagecomponent/1534187-initwithkey)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithKey:(NSString *)key ``` |
| To | ``` - (instancetype)initWithKey:(NSString *)key ``` |

Modified [NSDraggingItem.imageComponents](https://developer.apple.com/documentation/appkit/nsdraggingitem/1524302-imagecomponents)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly) NSArray *imageComponents ``` |
| To | ``` @property(readonly, copy) NSArray *imageComponents ``` |

Modified [-[NSDraggingItem initWithPasteboardWriter:]](https://developer.apple.com/documentation/appkit/nsdraggingitem/1535417-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithPasteboardWriter:(id<NSPasteboardWriting>)pasteboardWriter ``` |
| To | ``` - (instancetype)initWithPasteboardWriter:(id<NSPasteboardWriting>)pasteboardWriter ``` |

Modified [NSDraggingItem.item](https://developer.apple.com/documentation/appkit/nsdraggingitem/1533258-item)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readonly) id item ``` |
| To | ``` @property(readonly, strong) id item ``` |

NSDrawer.hRemoved [-[NSDrawer contentSize]](https://developer.apple.com/documentation/appkit/nsdrawer/1438302-contentsize)Removed [-[NSDrawer contentView]](https://developer.apple.com/documentation/appkit/nsdrawer/1438260-contentview)Removed [-[NSDrawer delegate]](https://developer.apple.com/documentation/appkit/nsdrawer/1438304-delegate)Removed [-[NSDrawer edge]](https://developer.apple.com/documentation/appkit/nsdrawer/1438320-edge)Removed [-[NSDrawer leadingOffset]](https://developer.apple.com/documentation/appkit/nsdrawer/1438306-leadingoffset)Removed [-[NSDrawer maxContentSize]](https://developer.apple.com/documentation/appkit/nsdrawer/1438266-maxcontentsize)Removed [-[NSDrawer minContentSize]](https://developer.apple.com/documentation/appkit/nsdrawer/1438291-mincontentsize)Removed [-[NSDrawer parentWindow]](https://developer.apple.com/documentation/appkit/nsdrawer/1438312-parentwindow)Removed [-[NSDrawer preferredEdge]](https://developer.apple.com/documentation/appkit/nsdrawer/1438272-preferrededge)Removed [-[NSDrawer setContentSize:]](https://developer.apple.com/documentation/appkit/nsdrawer/1438302-contentsize)Removed [-[NSDrawer setContentView:]](https://developer.apple.com/documentation/appkit/nsdrawer/1438260-contentview)Removed [-[NSDrawer setDelegate:]](https://developer.apple.com/documentation/appkit/nsdrawer/1438304-delegate)Removed [-[NSDrawer setLeadingOffset:]](https://developer.apple.com/documentation/appkit/nsdrawer/1438306-leadingoffset)Removed [-[NSDrawer setMaxContentSize:]](https://developer.apple.com/documentation/appkit/nsdrawer/1438266-maxcontentsize)Removed [-[NSDrawer setMinContentSize:]](https://developer.apple.com/documentation/appkit/nsdrawer/1438291-mincontentsize)Removed [-[NSDrawer setParentWindow:]](https://developer.apple.com/documentation/appkit/nsdrawer/1438312-parentwindow)Removed [-[NSDrawer setPreferredEdge:]](https://developer.apple.com/documentation/appkit/nsdrawer/1438272-preferrededge)Removed [-[NSDrawer setTrailingOffset:]](https://developer.apple.com/documentation/appkit/nsdrawer/1438277-trailingoffset)Removed [-[NSDrawer state]](https://developer.apple.com/documentation/appkit/nsdrawer/1438287-state)Removed [-[NSDrawer trailingOffset]](https://developer.apple.com/documentation/appkit/nsdrawer/1438277-trailingoffset)Removed [-[NSWindow drawers]](https://developer.apple.com/documentation/appkit/nswindow/1438323-drawers)Added [NSDrawer.contentSize](https://developer.apple.com/documentation/appkit/nsdrawer/1438302-contentsize)Added [NSDrawer.contentView](https://developer.apple.com/documentation/appkit/nsdrawer/1438260-contentview)Added [NSDrawer.delegate](https://developer.apple.com/documentation/appkit/nsdrawer/1438304-delegate)Added [NSDrawer.edge](https://developer.apple.com/documentation/appkit/nsdrawer/1438320-edge)Added [NSDrawer.leadingOffset](https://developer.apple.com/documentation/appkit/nsdrawer/1438306-leadingoffset)Added [NSDrawer.maxContentSize](https://developer.apple.com/documentation/appkit/nsdrawer/1438266-maxcontentsize)Added [NSDrawer.minContentSize](https://developer.apple.com/documentation/appkit/nsdrawer/1438291-mincontentsize)Added [NSDrawer.parentWindow](https://developer.apple.com/documentation/appkit/nsdrawer/1438312-parentwindow)Added [NSDrawer.preferredEdge](https://developer.apple.com/documentation/appkit/nsdrawer/1438272-preferrededge)Added [NSDrawer.state](https://developer.apple.com/documentation/appkit/nsdrawer/1438287-state)Added [NSDrawer.trailingOffset](https://developer.apple.com/documentation/appkit/nsdrawer/1438277-trailingoffset)Added [NSWindow.drawers](https://developer.apple.com/documentation/appkit/nswindow/1438323-drawers)Modified [NSDrawer](https://developer.apple.com/documentation/appkit/nsdrawer)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSAccessibility, NSAccessibilityElement |

Modified [-[NSDrawer initWithContentSize:preferredEdge:]](https://developer.apple.com/documentation/appkit/nsdrawer/1438262-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentSize:(NSSize)contentSize preferredEdge:(NSRectEdge)edge ``` |
| To | ``` - (instancetype)initWithContentSize:(NSSize)contentSize preferredEdge:(NSRectEdge)edge ``` |

Modified [-[NSDrawerDelegate drawerDidClose:]](https://developer.apple.com/documentation/appkit/nsdrawerdelegate/1438273-drawerdidclose)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDrawerDelegate drawerDidOpen:]](https://developer.apple.com/documentation/appkit/nsdrawerdelegate/1438285-drawerdidopen)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDrawerDelegate drawerShouldClose:]](https://developer.apple.com/documentation/appkit/nsdrawerdelegate/1438289-drawershouldclose)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDrawerDelegate drawerShouldOpen:]](https://developer.apple.com/documentation/appkit/nsdrawerdelegate/1438318-drawershouldopen)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDrawerDelegate drawerWillClose:]](https://developer.apple.com/documentation/appkit/nsdrawerdelegate/1438314-drawerwillclose)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDrawerDelegate drawerWillOpen:]](https://developer.apple.com/documentation/appkit/nsdrawerdelegate/1438325-drawerwillopen)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDrawerDelegate drawerWillResizeContents:toSize:]](https://developer.apple.com/documentation/appkit/nsdrawerdelegate/1438293-drawerwillresizecontents)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSEPSImageRep.hRemoved [-[NSEPSImageRep EPSRepresentation]](https://developer.apple.com/documentation/appkit/nsepsimagerep/1534453-epsrepresentation)Removed [-[NSEPSImageRep boundingBox]](https://developer.apple.com/documentation/appkit/nsepsimagerep/1528455-boundingbox)Added [NSEPSImageRep.EPSRepresentation](https://developer.apple.com/documentation/appkit/nsepsimagerep/1534453-epsrepresentation)Added [NSEPSImageRep.boundingBox](https://developer.apple.com/documentation/appkit/nsepsimagerep/1528455-boundingbox)Modified [+[NSEPSImageRep imageRepWithData:]](https://developer.apple.com/documentation/appkit/nsepsimagerep/1575616-imagerepwithdata)

|  | Declaration |
| --- | --- |
| From | ``` + (id)imageRepWithData:(NSData *)epsData ``` |
| To | ``` + (instancetype)imageRepWithData:(NSData *)epsData ``` |

Modified [-[NSEPSImageRep initWithData:]](https://developer.apple.com/documentation/appkit/nsepsimagerep/1528187-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(NSData *)epsData ``` |
| To | ``` - (instancetype)initWithData:(NSData *)epsData ``` |

Modified [-[NSEPSImageRep prepareGState]](https://developer.apple.com/documentation/appkit/nsepsimagerep/1526292-preparegstate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

NSEvent.hRemoved [-[NSEvent CGEvent]](https://developer.apple.com/documentation/appkit/nsevent/1530429-cgevent)Removed [-[NSEvent absoluteX]](https://developer.apple.com/documentation/appkit/nsevent/1530617-absolutex)Removed [-[NSEvent absoluteY]](https://developer.apple.com/documentation/appkit/nsevent/1528904-absolutey)Removed [-[NSEvent absoluteZ]](https://developer.apple.com/documentation/appkit/nsevent/1532154-absolutez)Removed [-[NSEvent buttonMask]](https://developer.apple.com/documentation/appkit/nsevent/1535428-buttonmask)Removed [-[NSEvent buttonNumber]](https://developer.apple.com/documentation/appkit/nsevent/1527828-buttonnumber)Removed [-[NSEvent capabilityMask]](https://developer.apple.com/documentation/appkit/nsevent/1534648-capabilitymask)Removed [-[NSEvent characters]](https://developer.apple.com/documentation/appkit/nsevent/1534183-characters)Removed [-[NSEvent charactersIgnoringModifiers]](https://developer.apple.com/documentation/appkit/nsevent/1524605-charactersignoringmodifiers)Removed [-[NSEvent clickCount]](https://developer.apple.com/documentation/appkit/nsevent/1528200-clickcount)Removed [-[NSEvent context]](https://developer.apple.com/documentation/appkit/nsevent/1524291-context)Removed [-[NSEvent data1]](https://developer.apple.com/documentation/appkit/nsevent/1528289-data1)Removed [-[NSEvent data2]](https://developer.apple.com/documentation/appkit/nsevent/1528647-data2)Removed [-[NSEvent deltaX]](https://developer.apple.com/documentation/appkit/nsevent/1534871-deltax)Removed [-[NSEvent deltaY]](https://developer.apple.com/documentation/appkit/nsevent/1534158-deltay)Removed [-[NSEvent deltaZ]](https://developer.apple.com/documentation/appkit/nsevent/1531528-deltaz)Removed [-[NSEvent deviceID]](https://developer.apple.com/documentation/appkit/nsevent/1530014-deviceid)Removed [-[NSEvent eventNumber]](https://developer.apple.com/documentation/appkit/nsevent/1535220-eventnumber)Removed [-[NSEvent eventRef]](https://developer.apple.com/documentation/appkit/nsevent/1525143-eventref)Removed [-[NSEvent hasPreciseScrollingDeltas]](https://developer.apple.com/documentation/appkit/nsevent/1525758-hasprecisescrollingdeltas)Removed [-[NSEvent isARepeat]](https://developer.apple.com/documentation/appkit/nsevent/1528049-isarepeat)Removed [-[NSEvent isDirectionInvertedFromDevice]](https://developer.apple.com/documentation/appkit/nsevent/1525151-isdirectioninvertedfromdevice)Removed [-[NSEvent isEnteringProximity]](https://developer.apple.com/documentation/appkit/nsevent/1531702-isenteringproximity)Removed [-[NSEvent keyCode]](https://developer.apple.com/documentation/appkit/nsevent/1534513-keycode)Removed [-[NSEvent locationInWindow]](https://developer.apple.com/documentation/appkit/nsevent/1529068-locationinwindow)Removed [-[NSEvent magnification]](https://developer.apple.com/documentation/appkit/nsevent/1531642-magnification)Removed [-[NSEvent modifierFlags]](https://developer.apple.com/documentation/appkit/nsevent/1534405-modifierflags)Removed [-[NSEvent momentumPhase]](https://developer.apple.com/documentation/appkit/nsevent/1525439-momentumphase)Removed [-[NSEvent phase]](https://developer.apple.com/documentation/appkit/nsevent/1533550-phase)Removed [-[NSEvent pointingDeviceID]](https://developer.apple.com/documentation/appkit/nsevent/1528818-pointingdeviceid)Removed [-[NSEvent pointingDeviceSerialNumber]](https://developer.apple.com/documentation/appkit/nsevent/1533420-pointingdeviceserialnumber)Removed [-[NSEvent pointingDeviceType]](https://developer.apple.com/documentation/appkit/nsevent/1535573-pointingdevicetype)Removed [-[NSEvent pressure]](https://developer.apple.com/documentation/appkit/nsevent/1534543-pressure)Removed [-[NSEvent rotation]](https://developer.apple.com/documentation/appkit/nsevent/1526249-rotation)Removed [-[NSEvent scrollingDeltaX]](https://developer.apple.com/documentation/appkit/nsevent/1524505-scrollingdeltax)Removed [-[NSEvent scrollingDeltaY]](https://developer.apple.com/documentation/appkit/nsevent/1535387-scrollingdeltay)Removed [-[NSEvent subtype]](https://developer.apple.com/documentation/appkit/nsevent/1527726-subtype)Removed [-[NSEvent systemTabletID]](https://developer.apple.com/documentation/appkit/nsevent/1528299-systemtabletid)Removed [-[NSEvent tabletID]](https://developer.apple.com/documentation/appkit/nsevent/1527003-tabletid)Removed [-[NSEvent tangentialPressure]](https://developer.apple.com/documentation/appkit/nsevent/1525959-tangentialpressure)Removed [-[NSEvent tilt]](https://developer.apple.com/documentation/appkit/nsevent/1534226-tilt)Removed [-[NSEvent timestamp]](https://developer.apple.com/documentation/appkit/nsevent/1528239-timestamp)Removed [-[NSEvent trackingArea]](https://developer.apple.com/documentation/appkit/nsevent/1534800-trackingarea)Removed [-[NSEvent trackingNumber]](https://developer.apple.com/documentation/appkit/nsevent/1533974-trackingnumber)Removed [-[NSEvent type]](https://developer.apple.com/documentation/appkit/nsevent/1528439-type)Removed [-[NSEvent uniqueID]](https://developer.apple.com/documentation/appkit/nsevent/1535813-uniqueid)Removed [-[NSEvent userData]](https://developer.apple.com/documentation/appkit/nsevent/1526810-userdata)Removed [-[NSEvent vendorDefined]](https://developer.apple.com/documentation/appkit/nsevent/1530551-vendordefined)Removed [-[NSEvent vendorID]](https://developer.apple.com/documentation/appkit/nsevent/1525177-vendorid)Removed [-[NSEvent vendorPointingDeviceType]](https://developer.apple.com/documentation/appkit/nsevent/1527736-vendorpointingdevicetype)Removed [-[NSEvent window]](https://developer.apple.com/documentation/appkit/nsevent/1530808-window)Removed [-[NSEvent windowNumber]](https://developer.apple.com/documentation/appkit/nsevent/1531361-windownumber)Added [NSEvent.ARepeat](https://developer.apple.com/documentation/appkit/nsevent/1528049-arepeat)Added [NSEvent.CGEvent](https://developer.apple.com/documentation/appkit/nsevent/1530429-cgevent)Added [NSEvent.absoluteX](https://developer.apple.com/documentation/appkit/nsevent/1530617-absolutex)Added [NSEvent.absoluteY](https://developer.apple.com/documentation/appkit/nsevent/1528904-absolutey)Added [NSEvent.absoluteZ](https://developer.apple.com/documentation/appkit/nsevent/1532154-absolutez)Added [NSEvent.buttonMask](https://developer.apple.com/documentation/appkit/nsevent/1535428-buttonmask)Added [NSEvent.buttonNumber](https://developer.apple.com/documentation/appkit/nsevent/1527828-buttonnumber)Added [NSEvent.capabilityMask](https://developer.apple.com/documentation/appkit/nsevent/1534648-capabilitymask)Added [NSEvent.characters](https://developer.apple.com/documentation/appkit/nsevent/1534183-characters)Added [NSEvent.charactersIgnoringModifiers](https://developer.apple.com/documentation/appkit/nsevent/1524605-charactersignoringmodifiers)Added [NSEvent.clickCount](https://developer.apple.com/documentation/appkit/nsevent/1528200-clickcount)Added [NSEvent.context](https://developer.apple.com/documentation/appkit/nsevent/1524291-context)Added [NSEvent.data1](https://developer.apple.com/documentation/appkit/nsevent/1528289-data1)Added [NSEvent.data2](https://developer.apple.com/documentation/appkit/nsevent/1528647-data2)Added [NSEvent.deltaX](https://developer.apple.com/documentation/appkit/nsevent/1534871-deltax)Added [NSEvent.deltaY](https://developer.apple.com/documentation/appkit/nsevent/1534158-deltay)Added [NSEvent.deltaZ](https://developer.apple.com/documentation/appkit/nsevent/1531528-deltaz)Added [NSEvent.deviceID](https://developer.apple.com/documentation/appkit/nsevent/1530014-deviceid)Added [NSEvent.directionInvertedFromDevice](https://developer.apple.com/documentation/appkit/nsevent/1525151-directioninvertedfromdevice)Added [NSEvent.enteringProximity](https://developer.apple.com/documentation/appkit/nsevent/1531702-isenteringproximity)Added [NSEvent.eventNumber](https://developer.apple.com/documentation/appkit/nsevent/1535220-eventnumber)Added [NSEvent.eventRef](https://developer.apple.com/documentation/appkit/nsevent/1525143-eventref)Added [NSEvent.hasPreciseScrollingDeltas](https://developer.apple.com/documentation/appkit/nsevent/1525758-hasprecisescrollingdeltas)Added [NSEvent.keyCode](https://developer.apple.com/documentation/appkit/nsevent/1534513-keycode)Added [NSEvent.locationInWindow](https://developer.apple.com/documentation/appkit/nsevent/1529068-locationinwindow)Added [NSEvent.magnification](https://developer.apple.com/documentation/appkit/nsevent/1531642-magnification)Added [NSEvent.modifierFlags](https://developer.apple.com/documentation/appkit/nsevent/1534405-modifierflags)Added [NSEvent.momentumPhase](https://developer.apple.com/documentation/appkit/nsevent/1525439-momentumphase)Added [NSEvent.phase](https://developer.apple.com/documentation/appkit/nsevent/1533550-phase)Added [NSEvent.pointingDeviceID](https://developer.apple.com/documentation/appkit/nsevent/1528818-pointingdeviceid)Added [NSEvent.pointingDeviceSerialNumber](https://developer.apple.com/documentation/appkit/nsevent/1533420-pointingdeviceserialnumber)Added [NSEvent.pointingDeviceType](https://developer.apple.com/documentation/appkit/nsevent/1535573-pointingdevicetype)Added [NSEvent.pressure](https://developer.apple.com/documentation/appkit/nsevent/1534543-pressure)Added [NSEvent.rotation](https://developer.apple.com/documentation/appkit/nsevent/1526249-rotation)Added [NSEvent.scrollingDeltaX](https://developer.apple.com/documentation/appkit/nsevent/1524505-scrollingdeltax)Added [NSEvent.scrollingDeltaY](https://developer.apple.com/documentation/appkit/nsevent/1535387-scrollingdeltay)Added [NSEvent.subtype](https://developer.apple.com/documentation/appkit/nsevent/1527726-subtype)Added [NSEvent.systemTabletID](https://developer.apple.com/documentation/appkit/nsevent/1528299-systemtabletid)Added [NSEvent.tabletID](https://developer.apple.com/documentation/appkit/nsevent/1527003-tabletid)Added [NSEvent.tangentialPressure](https://developer.apple.com/documentation/appkit/nsevent/1525959-tangentialpressure)Added [NSEvent.tilt](https://developer.apple.com/documentation/appkit/nsevent/1534226-tilt)Added [NSEvent.timestamp](https://developer.apple.com/documentation/appkit/nsevent/1528239-timestamp)Added [NSEvent.trackingArea](https://developer.apple.com/documentation/appkit/nsevent/1534800-trackingarea)Added [NSEvent.trackingNumber](https://developer.apple.com/documentation/appkit/nsevent/1533974-trackingnumber)Added [NSEvent.type](https://developer.apple.com/documentation/appkit/nsevent/1528439-type)Added [NSEvent.uniqueID](https://developer.apple.com/documentation/appkit/nsevent/1535813-uniqueid)Added [NSEvent.userData](https://developer.apple.com/documentation/appkit/nsevent/1526810-userdata)Added [NSEvent.vendorDefined](https://developer.apple.com/documentation/appkit/nsevent/1530551-vendordefined)Added [NSEvent.vendorID](https://developer.apple.com/documentation/appkit/nsevent/1525177-vendorid)Added [NSEvent.vendorPointingDeviceType](https://developer.apple.com/documentation/appkit/nsevent/1527736-vendorpointingdevicetype)Added [NSEvent.window](https://developer.apple.com/documentation/appkit/nsevent/1530808-window)Added [NSEvent.windowNumber](https://developer.apple.com/documentation/appkit/nsevent/1531361-windownumber)Added [NSEventButtonMask](https://developer.apple.com/documentation/appkit/nseventbuttonmask)Added [NSEventModifierFlags](https://developer.apple.com/documentation/appkit/nseventmodifierflags)Added [NSEventSubtype](https://developer.apple.com/documentation/appkit/nsevent/eventsubtype)Modified [+[NSEvent enterExitEventWithType:location:modifierFlags:timestamp:windowNumber:context:eventNumber:trackingNumber:userData:]](https://developer.apple.com/documentation/appkit/nsevent/1535383-enterexiteventwithtype)

|  | Declaration |
| --- | --- |
| From | ``` + (NSEvent *)enterExitEventWithType:(NSEventType)type location:(NSPoint)location modifierFlags:(NSUInteger)flags timestamp:(NSTimeInterval)time windowNumber:(NSInteger)wNum context:(NSGraphicsContext *)context eventNumber:(NSInteger)eNum trackingNumber:(NSInteger)tNum userData:(void *)data ``` |
| To | ``` + (NSEvent *)enterExitEventWithType:(NSEventType)type location:(NSPoint)location modifierFlags:(NSEventModifierFlags)flags timestamp:(NSTimeInterval)time windowNumber:(NSInteger)wNum context:(NSGraphicsContext *)context eventNumber:(NSInteger)eNum trackingNumber:(NSInteger)tNum userData:(void *)data ``` |

Modified [+[NSEvent keyEventWithType:location:modifierFlags:timestamp:windowNumber:context:characters:charactersIgnoringModifiers:isARepeat:keyCode:]](https://developer.apple.com/documentation/appkit/nsevent/1533943-keyeventwithtype)

|  | Declaration |
| --- | --- |
| From | ``` + (NSEvent *)keyEventWithType:(NSEventType)type location:(NSPoint)location modifierFlags:(NSUInteger)flags timestamp:(NSTimeInterval)time windowNumber:(NSInteger)wNum context:(NSGraphicsContext *)context characters:(NSString *)keys charactersIgnoringModifiers:(NSString *)ukeys isARepeat:(BOOL)flag keyCode:(unsigned short)code ``` |
| To | ``` + (NSEvent *)keyEventWithType:(NSEventType)type location:(NSPoint)location modifierFlags:(NSEventModifierFlags)flags timestamp:(NSTimeInterval)time windowNumber:(NSInteger)wNum context:(NSGraphicsContext *)context characters:(NSString *)keys charactersIgnoringModifiers:(NSString *)ukeys isARepeat:(BOOL)flag keyCode:(unsigned short)code ``` |

Modified [+[NSEvent modifierFlags]](https://developer.apple.com/documentation/appkit/nsevent/1535211-modifierflags)

|  | Declaration |
| --- | --- |
| From | ``` + (NSUInteger)modifierFlags ``` |
| To | ``` + (NSEventModifierFlags)modifierFlags ``` |

Modified [+[NSEvent mouseEventWithType:location:modifierFlags:timestamp:windowNumber:context:eventNumber:clickCount:pressure:]](https://developer.apple.com/documentation/appkit/nsevent/1532495-mouseeventwithtype)

|  | Declaration |
| --- | --- |
| From | ``` + (NSEvent *)mouseEventWithType:(NSEventType)type location:(NSPoint)location modifierFlags:(NSUInteger)flags timestamp:(NSTimeInterval)time windowNumber:(NSInteger)wNum context:(NSGraphicsContext *)context eventNumber:(NSInteger)eNum clickCount:(NSInteger)cNum pressure:(float)pressure ``` |
| To | ``` + (NSEvent *)mouseEventWithType:(NSEventType)type location:(NSPoint)location modifierFlags:(NSEventModifierFlags)flags timestamp:(NSTimeInterval)time windowNumber:(NSInteger)wNum context:(NSGraphicsContext *)context eventNumber:(NSInteger)eNum clickCount:(NSInteger)cNum pressure:(float)pressure ``` |

Modified [+[NSEvent otherEventWithType:location:modifierFlags:timestamp:windowNumber:context:subtype:data1:data2:]](https://developer.apple.com/documentation/appkit/nsevent/1530010-othereventwithtype)

|  | Declaration |
| --- | --- |
| From | ``` + (NSEvent *)otherEventWithType:(NSEventType)type location:(NSPoint)location modifierFlags:(NSUInteger)flags timestamp:(NSTimeInterval)time windowNumber:(NSInteger)wNum context:(NSGraphicsContext *)context subtype:(short)subtype data1:(NSInteger)d1 data2:(NSInteger)d2 ``` |
| To | ``` + (NSEvent *)otherEventWithType:(NSEventType)type location:(NSPoint)location modifierFlags:(NSEventModifierFlags)flags timestamp:(NSTimeInterval)time windowNumber:(NSInteger)wNum context:(NSGraphicsContext *)context subtype:(short)subtype data1:(NSInteger)d1 data2:(NSInteger)d2 ``` |

Modified [NSEventMaskBeginGesture](https://developer.apple.com/documentation/appkit/nseventmask/nseventmaskbegingesture)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [NSEventMaskEndGesture](https://developer.apple.com/documentation/appkit/nseventmask/nseventmaskendgesture)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [NSEventMaskFromType()](https://developer.apple.com/documentation/appkit/1525407-nseventmaskfromtype)

|  | Declaration |
| --- | --- |
| From | ``` NSUInteger NSEventMaskFromType (	NSEventType type); ``` |
| To | ``` NSEventMask NSEventMaskFromType (	NSEventType type); ``` |

Modified [NSEventMaskGesture](https://developer.apple.com/documentation/appkit/nseventmask/nseventmaskgesture)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [NSEventMaskMagnify](https://developer.apple.com/documentation/appkit/nsevent/eventtypemask/1528004-magnify)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [NSEventMaskRotate](https://developer.apple.com/documentation/appkit/nsevent/eventtypemask/1535086-rotate)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [NSEventMaskSwipe](https://developer.apple.com/documentation/appkit/nseventmask/nseventmaskswipe)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [NSEventPhaseMayBegin](https://developer.apple.com/documentation/appkit/nsevent/phase/1528100-maybegin)

|  | Introduction |
| --- | --- |
| From | OS X 10.8 |
| To | OS X 10.7 |

NSFileWrapperExtensions.hRemoved [-[NSFileWrapper icon]](https://developer.apple.com/documentation/foundation/filewrapper/1413123-icon)Removed [-[NSFileWrapper setIcon:]](https://developer.apple.com/documentation/foundation/filewrapper/1413123-icon)Added [NSFileWrapper.icon](https://developer.apple.com/documentation/foundation/nsfilewrapper/1413123-icon)NSFont.hRemoved [-[NSFont ascender]](https://developer.apple.com/documentation/appkit/nsfont/1535420-ascender)Removed [-[NSFont boundingRectForFont]](https://developer.apple.com/documentation/appkit/nsfont/1527321-boundingrectforfont)Removed [-[NSFont capHeight]](https://developer.apple.com/documentation/appkit/nsfont/1528292-capheight)Removed [-[NSFont coveredCharacterSet]](https://developer.apple.com/documentation/appkit/nsfont/1535912-coveredcharacterset)Removed [-[NSFont descender]](https://developer.apple.com/documentation/appkit/nsfont/1532270-descender)Removed [-[NSFont displayName]](https://developer.apple.com/documentation/appkit/nsfont/1531660-displayname)Removed [-[NSFont familyName]](https://developer.apple.com/documentation/appkit/nsfont/1529585-familyname)Removed [-[NSFont fontDescriptor]](https://developer.apple.com/documentation/appkit/nsfont/1530476-fontdescriptor)Removed [-[NSFont fontName]](https://developer.apple.com/documentation/appkit/nsfont/1526183-fontname)Removed [-[NSFont isFixedPitch]](https://developer.apple.com/documentation/appkit/nsfont/1529210-fixedpitch)Removed [-[NSFont isVertical]](https://developer.apple.com/documentation/appkit/nsfont/1534644-vertical)Removed [-[NSFont italicAngle]](https://developer.apple.com/documentation/appkit/nsfont/1535194-italicangle)Removed [-[NSFont leading]](https://developer.apple.com/documentation/appkit/nsfont/1534083-leading)Removed [-[NSFont matrix]](https://developer.apple.com/documentation/appkit/nsfont/1531033-matrix)Removed [-[NSFont maximumAdvancement]](https://developer.apple.com/documentation/appkit/nsfont/1526023-maximumadvancement)Removed [-[NSFont mostCompatibleStringEncoding]](https://developer.apple.com/documentation/appkit/nsfont/1527635-mostcompatiblestringencoding)Removed [-[NSFont numberOfGlyphs]](https://developer.apple.com/documentation/appkit/nsfont/1533968-numberofglyphs)Removed [-[NSFont pointSize]](https://developer.apple.com/documentation/appkit/nsfont/1524511-pointsize)Removed [-[NSFont printerFont]](https://developer.apple.com/documentation/appkit/nsfont/1534215-printerfont)Removed [-[NSFont renderingMode]](https://developer.apple.com/documentation/appkit/nsfont/1535064-renderingmode)Removed [-[NSFont screenFont]](https://developer.apple.com/documentation/appkit/nsfont/1534412-screen)Removed [-[NSFont textTransform]](https://developer.apple.com/documentation/appkit/nsfont/1526270-texttransform)Removed [-[NSFont underlinePosition]](https://developer.apple.com/documentation/appkit/nsfont/1533984-underlineposition)Removed [-[NSFont underlineThickness]](https://developer.apple.com/documentation/appkit/nsfont/1531229-underlinethickness)Removed [-[NSFont verticalFont]](https://developer.apple.com/documentation/appkit/nsfont/1535152-verticalfont)Removed [-[NSFont xHeight]](https://developer.apple.com/documentation/appkit/nsfont/1533428-xheight)Added [NSFont.ascender](https://developer.apple.com/documentation/appkit/nsfont/1535420-ascender)Added [NSFont.boundingRectForFont](https://developer.apple.com/documentation/appkit/nsfont/1527321-boundingrectforfont)Added [NSFont.capHeight](https://developer.apple.com/documentation/appkit/nsfont/1528292-capheight)Added [NSFont.coveredCharacterSet](https://developer.apple.com/documentation/appkit/nsfont/1535912-coveredcharacterset)Added [NSFont.descender](https://developer.apple.com/documentation/appkit/nsfont/1532270-descender)Added [NSFont.displayName](https://developer.apple.com/documentation/appkit/nsfont/1531660-displayname)Added [NSFont.familyName](https://developer.apple.com/documentation/appkit/nsfont/1529585-familyname)Added [NSFont.fixedPitch](https://developer.apple.com/documentation/appkit/nsfont/1529210-fixedpitch)Added [NSFont.fontDescriptor](https://developer.apple.com/documentation/appkit/nsfont/1530476-fontdescriptor)Added [NSFont.fontName](https://developer.apple.com/documentation/appkit/nsfont/1526183-fontname)Added [NSFont.italicAngle](https://developer.apple.com/documentation/appkit/nsfont/1535194-italicangle)Added [NSFont.leading](https://developer.apple.com/documentation/appkit/nsfont/1534083-leading)Added [NSFont.matrix](https://developer.apple.com/documentation/appkit/nsfont/1531033-matrix)Added [NSFont.maximumAdvancement](https://developer.apple.com/documentation/appkit/nsfont/1526023-maximumadvancement)Added [NSFont.mostCompatibleStringEncoding](https://developer.apple.com/documentation/appkit/nsfont/1527635-mostcompatiblestringencoding)Added [NSFont.numberOfGlyphs](https://developer.apple.com/documentation/appkit/nsfont/1533968-numberofglyphs)Added [NSFont.pointSize](https://developer.apple.com/documentation/appkit/nsfont/1524511-pointsize)Added [NSFont.printerFont](https://developer.apple.com/documentation/appkit/nsfont/1534215-printerfont)Added [NSFont.renderingMode](https://developer.apple.com/documentation/appkit/nsfont/1535064-renderingmode)Added [NSFont.screenFont](https://developer.apple.com/documentation/appkit/nsfont/1534412-screen)Added [NSFont.textTransform](https://developer.apple.com/documentation/appkit/nsfont/1526270-texttransform)Added [NSFont.underlinePosition](https://developer.apple.com/documentation/appkit/nsfont/1533984-underlineposition)Added [NSFont.underlineThickness](https://developer.apple.com/documentation/appkit/nsfont/1531229-underlinethickness)Added [NSFont.vertical](https://developer.apple.com/documentation/appkit/nsfont/1534644-vertical)Added [NSFont.verticalFont](https://developer.apple.com/documentation/appkit/nsfont/1535152-vertical)Added [NSFont.xHeight](https://developer.apple.com/documentation/appkit/nsfont/1533428-xheight)Modified [NSFont](https://developer.apple.com/documentation/appkit/nsfont)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSFontCollection.hRemoved [-[NSFontCollection exclusionDescriptors]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497456-exclusiondescriptors)Removed [-[NSFontCollection matchingDescriptors]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497523-matchingdescriptors)Removed [-[NSFontCollection queryDescriptors]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497441-querydescriptors)Removed [-[NSMutableFontCollection setExclusionDescriptors:]](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/1497442-exclusiondescriptors)Removed [-[NSMutableFontCollection setQueryDescriptors:]](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/1497457-querydescriptors)Added [NSFontCollection.exclusionDescriptors](https://developer.apple.com/documentation/appkit/nsfontcollection/1497456-exclusiondescriptors)Added [NSFontCollection.matchingDescriptors](https://developer.apple.com/documentation/appkit/nsfontcollection/1497523-matchingdescriptors)Added [NSFontCollection.queryDescriptors](https://developer.apple.com/documentation/appkit/nsfontcollection/1497441-querydescriptors)Added [NSMutableFontCollection.exclusionDescriptors](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/1497442-exclusiondescriptors)Added [+[NSMutableFontCollection fontCollectionWithAllAvailableDescriptors]](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/1497506-withallavailabledescriptors)Added [+[NSMutableFontCollection fontCollectionWithDescriptors:]](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/1497450-init)Added [+[NSMutableFontCollection fontCollectionWithLocale:]](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/1497479-fontcollectionwithlocale)Added [+[NSMutableFontCollection fontCollectionWithName:]](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/1497503-init)Added [+[NSMutableFontCollection fontCollectionWithName:visibility:]](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/1497453-init)Added [NSMutableFontCollection.queryDescriptors](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/1497457-querydescriptors)Modified [+[NSFontCollection fontCollectionWithAllAvailableDescriptors]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497473-fontcollectionwithallavailablede)

|  | Declaration |
| --- | --- |
| From | ``` + (id)fontCollectionWithAllAvailableDescriptors ``` |
| To | ``` + (NSFontCollection *)fontCollectionWithAllAvailableDescriptors ``` |

Modified [+[NSFontCollection fontCollectionWithDescriptors:]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497467-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)fontCollectionWithDescriptors:(NSArray *)queryDescriptors ``` |
| To | ``` + (NSFontCollection *)fontCollectionWithDescriptors:(NSArray *)queryDescriptors ``` |

Modified [+[NSFontCollection fontCollectionWithLocale:]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497481-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)fontCollectionWithLocale:(NSLocale *)locale ``` |
| To | ``` + (NSFontCollection *)fontCollectionWithLocale:(NSLocale *)locale ``` |

Modified [+[NSFontCollection fontCollectionWithName:]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497514-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)fontCollectionWithName:(NSString *)name ``` |
| To | ``` + (NSFontCollection *)fontCollectionWithName:(NSString *)name ``` |

Modified [+[NSFontCollection fontCollectionWithName:visibility:]](https://developer.apple.com/documentation/appkit/nsfontcollection/1497475-fontcollectionwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (id)fontCollectionWithName:(NSString *)name visibility:(NSFontCollectionVisibility)visibility ``` |
| To | ``` + (NSFontCollection *)fontCollectionWithName:(NSString *)name visibility:(NSFontCollectionVisibility)visibility ``` |

NSFontDescriptor.hRemoved [-[NSFontDescriptor fontAttributes]](https://developer.apple.com/documentation/appkit/nsfontdescriptor/1469831-fontattributes)Removed [-[NSFontDescriptor matrix]](https://developer.apple.com/documentation/appkit/nsfontdescriptor/1469950-matrix)Removed [-[NSFontDescriptor pointSize]](https://developer.apple.com/documentation/appkit/nsfontdescriptor/1469829-pointsize)Removed [-[NSFontDescriptor postscriptName]](https://developer.apple.com/documentation/appkit/nsfontdescriptor/1469948-postscriptname)Removed [-[NSFontDescriptor symbolicTraits]](https://developer.apple.com/documentation/appkit/nsfontdescriptor/1469858-symbolictraits)Added [NSFontDescriptor.fontAttributes](https://developer.apple.com/documentation/appkit/nsfontdescriptor/1469831-fontattributes)Added [NSFontDescriptor.matrix](https://developer.apple.com/documentation/appkit/nsfontdescriptor/1469950-matrix)Added [NSFontDescriptor.pointSize](https://developer.apple.com/documentation/appkit/nsfontdescriptor/1469829-pointsize)Added [NSFontDescriptor.postscriptName](https://developer.apple.com/documentation/appkit/nsfontdescriptor/1469948-postscriptname)Added [NSFontDescriptor.symbolicTraits](https://developer.apple.com/documentation/appkit/nsfontdescriptor/1469858-symbolictraits)Modified [NSFontDescriptor](https://developer.apple.com/documentation/appkit/nsfontdescriptor)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

Modified [-[NSFontDescriptor initWithFontAttributes:]](https://developer.apple.com/documentation/appkit/nsfontdescriptor/1469991-initwithfontattributes)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFontAttributes:(NSDictionary *)attributes ``` |
| To | ``` - (instancetype)initWithFontAttributes:(NSDictionary *)attributes ``` |

NSFontManager.hRemoved [-[NSFontManager action]](https://developer.apple.com/documentation/appkit/nsfontmanager/1462349-action)Removed [-[NSFontManager availableFontFamilies]](https://developer.apple.com/documentation/appkit/nsfontmanager/1462323-availablefontfamilies)Removed [-[NSFontManager availableFonts]](https://developer.apple.com/documentation/appkit/nsfontmanager/1462372-availablefonts)Removed [-[NSFontManager collectionNames]](https://developer.apple.com/documentation/appkit/nsfontmanager/1462313-collectionnames)Removed [-[NSFontManager currentFontAction]](https://developer.apple.com/documentation/appkit/nsfontmanager/1462362-currentfontaction)Removed [-[NSFontManager delegate]](https://developer.apple.com/documentation/appkit/nsfontmanager/1462363-delegate)Removed [-[NSFontManager isEnabled]](https://developer.apple.com/documentation/appkit/nsfontmanager/1462341-isenabled)Removed [-[NSFontManager isMultiple]](https://developer.apple.com/documentation/appkit/nsfontmanager/1462376-multiple)Removed [-[NSFontManager selectedFont]](https://developer.apple.com/documentation/appkit/nsfontmanager/1462268-selectedfont)Removed [-[NSFontManager sendAction]](https://developer.apple.com/documentation/appkit/nsfontmanager/1462386-sendaction)Removed [-[NSFontManager setAction:]](https://developer.apple.com/documentation/appkit/nsfontmanager/1462349-action)Removed [-[NSFontManager setDelegate:]](https://developer.apple.com/documentation/appkit/nsfontmanager/1462363-delegate)Removed [-[NSFontManager setEnabled:]](https://developer.apple.com/documentation/appkit/nsfontmanager/1462341-isenabled)Removed [-[NSFontManager setTarget:]](https://developer.apple.com/documentation/appkit/nsfontmanager/1462380-target)Removed [-[NSFontManager target]](https://developer.apple.com/documentation/appkit/nsfontmanager/1462380-target)Added [NSFontManager.action](https://developer.apple.com/documentation/appkit/nsfontmanager/1462349-action)Added [NSFontManager.availableFontFamilies](https://developer.apple.com/documentation/appkit/nsfontmanager/1462323-availablefontfamilies)Added [NSFontManager.availableFonts](https://developer.apple.com/documentation/appkit/nsfontmanager/1462372-availablefonts)Added [NSFontManager.collectionNames](https://developer.apple.com/documentation/appkit/nsfontmanager/1462313-collectionnames)Added [NSFontManager.currentFontAction](https://developer.apple.com/documentation/appkit/nsfontmanager/1462362-currentfontaction)Added [NSFontManager.delegate](https://developer.apple.com/documentation/appkit/nsfontmanager/1462363-delegate)Added [NSFontManager.enabled](https://developer.apple.com/documentation/appkit/nsfontmanager/1462341-isenabled)Added [NSFontManager.multiple](https://developer.apple.com/documentation/appkit/nsfontmanager/1462376-ismultiple)Added [NSFontManager.selectedFont](https://developer.apple.com/documentation/appkit/nsfontmanager/1462268-selectedfont)Added [NSFontManager.sendAction](https://developer.apple.com/documentation/appkit/nsfontmanager/1462386-sendaction)Added [NSFontManager.target](https://developer.apple.com/documentation/appkit/nsfontmanager/1462380-target)Added [NSFontCollectionOptions](https://developer.apple.com/documentation/appkit/nsfontcollectionoptions)Modified [-[NSFontManager addCollection:options:]](https://developer.apple.com/documentation/appkit/nsfontmanager/1462272-addcollection)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)addCollection:(NSString *)collectionName options:(NSInteger)collectionOptions ``` |
| To | ``` - (BOOL)addCollection:(NSString *)collectionName options:(NSFontCollectionOptions)collectionOptions ``` |

NSFontPanel.hRemoved [-[NSFontPanel accessoryView]](https://developer.apple.com/documentation/appkit/nsfontpanel/1535927-accessoryview)Removed [-[NSFontPanel isEnabled]](https://developer.apple.com/documentation/appkit/nsfontpanel/1526041-enabled)Removed [-[NSFontPanel setAccessoryView:]](https://developer.apple.com/documentation/appkit/nsfontpanel/1535927-accessoryview)Removed [-[NSFontPanel setEnabled:]](https://developer.apple.com/documentation/appkit/nsfontpanel/1526041-enabled)Removed [-[NSFontPanel worksWhenModal]](https://developer.apple.com/documentation/appkit/nsfontpanel/1529532-workswhenmodal)Added [NSFontPanel.accessoryView](https://developer.apple.com/documentation/appkit/nsfontpanel/1535927-accessoryview)Added [NSFontPanel.enabled](https://developer.apple.com/documentation/appkit/nsfontpanel/1526041-enabled)Added [NSFontPanel.worksWhenModal](https://developer.apple.com/documentation/appkit/nsfontpanel/1529532-workswhenmodal)Modified [NSFPCurrentField](https://developer.apple.com/documentation/appkit/1579351-tags_of_views_in_the_fontpanel/nsfpcurrentfield)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.0 |

Modified [NSFPPreviewButton](https://developer.apple.com/documentation/appkit/1579351-tags_of_views_in_the_fontpanel/nsfppreviewbutton)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.0 |

Modified [NSFPPreviewField](https://developer.apple.com/documentation/appkit/1579351-tags_of_views_in_the_fontpanel/nsfppreviewfield)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.0 |

Modified [NSFPRevertButton](https://developer.apple.com/documentation/appkit/1579351-tags_of_views_in_the_fontpanel/nsfprevertbutton)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.0 |

Modified [NSFPSetButton](https://developer.apple.com/documentation/appkit/1579351-tags_of_views_in_the_fontpanel/nsfpsetbutton)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.0 |

Modified [NSFPSizeField](https://developer.apple.com/documentation/appkit/1579351-tags_of_views_in_the_fontpanel/nsfpsizefield)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.0 |

Modified [NSFPSizeTitle](https://developer.apple.com/documentation/appkit/1579351-tags_of_views_in_the_fontpanel/nsfpsizetitle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.0 |

NSForm.hModified [NSForm](https://developer.apple.com/documentation/appkit/nsform)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

NSFormCell.hRemoved [-[NSFormCell attributedTitle]](https://developer.apple.com/documentation/appkit/nsformcell/1527410-attributedtitle)Removed [-[NSFormCell isOpaque]](https://developer.apple.com/documentation/appkit/nsformcell/1529440-isopaque)Removed [-[NSFormCell placeholderAttributedString]](https://developer.apple.com/documentation/appkit/nsformcell/1535914-placeholderattributedstring)Removed [-[NSFormCell placeholderString]](https://developer.apple.com/documentation/appkit/nsformcell/1534043-placeholderstring)Removed [-[NSFormCell preferredTextFieldWidth]](https://developer.apple.com/documentation/appkit/nsformcell/1527483-preferredtextfieldwidth)Removed [-[NSFormCell setAttributedTitle:]](https://developer.apple.com/documentation/appkit/nsformcell/1527410-attributedtitle)Removed [-[NSFormCell setPlaceholderAttributedString:]](https://developer.apple.com/documentation/appkit/nsformcell/1535914-placeholderattributedstring)Removed [-[NSFormCell setPlaceholderString:]](https://developer.apple.com/documentation/appkit/nsformcell/1534043-placeholderstring)Removed [-[NSFormCell setPreferredTextFieldWidth:]](https://developer.apple.com/documentation/appkit/nsformcell/1527483-preferredtextfieldwidth)Removed [-[NSFormCell setTitle:]](https://developer.apple.com/documentation/appkit/nsformcell/1526646-title)Removed [-[NSFormCell setTitleAlignment:]](https://developer.apple.com/documentation/appkit/nsformcell/1525716-titlealignment)Removed [-[NSFormCell setTitleBaseWritingDirection:]](https://developer.apple.com/documentation/appkit/nsformcell/1526419-titlebasewritingdirection)Removed [-[NSFormCell setTitleFont:]](https://developer.apple.com/documentation/appkit/nsformcell/1525255-titlefont)Removed [-[NSFormCell setTitleWidth:]](https://developer.apple.com/documentation/appkit/nsformcell/1535464-titlewidth)Removed [-[NSFormCell title]](https://developer.apple.com/documentation/appkit/nsformcell/1526646-title)Removed [-[NSFormCell titleAlignment]](https://developer.apple.com/documentation/appkit/nsformcell/1525716-titlealignment)Removed [-[NSFormCell titleBaseWritingDirection]](https://developer.apple.com/documentation/appkit/nsformcell/1526419-titlebasewritingdirection)Removed [-[NSFormCell titleFont]](https://developer.apple.com/documentation/appkit/nsformcell/1525255-titlefont)Removed [-[NSFormCell titleWidth]](https://developer.apple.com/documentation/appkit/nsformcell/1535464-titlewidth)Added [NSFormCell.attributedTitle](https://developer.apple.com/documentation/appkit/nsformcell/1527410-attributedtitle)Added [NSFormCell.opaque](https://developer.apple.com/documentation/appkit/nsformcell/1529440-isopaque)Added [NSFormCell.placeholderAttributedString](https://developer.apple.com/documentation/appkit/nsformcell/1535914-placeholderattributedstring)Added [NSFormCell.placeholderString](https://developer.apple.com/documentation/appkit/nsformcell/1534043-placeholderstring)Added [NSFormCell.preferredTextFieldWidth](https://developer.apple.com/documentation/appkit/nsformcell/1527483-preferredtextfieldwidth)Added [NSFormCell.title](https://developer.apple.com/documentation/appkit/nsformcell/1526646-title)Added [NSFormCell.titleAlignment](https://developer.apple.com/documentation/appkit/nsformcell/1525716-titlealignment)Added [NSFormCell.titleBaseWritingDirection](https://developer.apple.com/documentation/appkit/nsformcell/1526419-titlebasewritingdirection)Added [NSFormCell.titleFont](https://developer.apple.com/documentation/appkit/nsformcell/1525255-titlefont)Added [NSFormCell.titleWidth](https://developer.apple.com/documentation/appkit/nsformcell/1535464-titlewidth)Modified [-[NSFormCell initTextCell:]](https://developer.apple.com/documentation/appkit/nsformcell/1526669-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initTextCell:(NSString *)aString ``` |
| To | ``` - (instancetype)initTextCell:(NSString *)aString ``` |

NSGestureRecognizer.h (Added)Added [NSGestureRecognizer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer)Added [NSGestureRecognizer.action](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1529280-action)Added [-[NSGestureRecognizer canBePreventedByGestureRecognizer:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1534587-canbeprevented)Added [-[NSGestureRecognizer canPreventGestureRecognizer:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1534503-canprevent)Added [NSGestureRecognizer.delaysKeyEvents](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1529788-delayskeyevents)Added [NSGestureRecognizer.delaysMagnificationEvents](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1529974-delaysmagnificationevents)Added [NSGestureRecognizer.delaysOtherMouseButtonEvents](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1530375-delaysothermousebuttonevents)Added [NSGestureRecognizer.delaysPrimaryMouseButtonEvents](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1533619-delaysprimarymousebuttonevents)Added [NSGestureRecognizer.delaysRotationEvents](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1535384-delaysrotationevents)Added [NSGestureRecognizer.delaysSecondaryMouseButtonEvents](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1535204-delayssecondarymousebuttonevents)Added [NSGestureRecognizer.delegate](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1529879-delegate)Added [NSGestureRecognizer.enabled](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1535263-enabled)Added [-[NSGestureRecognizer flagsChanged:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1532604-flagschanged)Added [-[NSGestureRecognizer initWithCoder:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1534865-init)Added [-[NSGestureRecognizer initWithTarget:action:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1535012-init)Added [-[NSGestureRecognizer keyDown:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1532158-keydown)Added [-[NSGestureRecognizer keyUp:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1526578-keyup)Added [-[NSGestureRecognizer locationInView:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1524261-location)Added [-[NSGestureRecognizer magnifyWithEvent:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1528828-magnify)Added [-[NSGestureRecognizer mouseDown:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1524901-mousedown)Added [-[NSGestureRecognizer mouseDragged:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1534535-mousedragged)Added [-[NSGestureRecognizer mouseUp:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1526116-mouseup)Added [-[NSGestureRecognizer otherMouseDown:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1534433-othermousedown)Added [-[NSGestureRecognizer otherMouseDragged:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1534208-othermousedragged)Added [-[NSGestureRecognizer otherMouseUp:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1527874-othermouseup)Added [-[NSGestureRecognizer reset]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1527219-reset)Added [-[NSGestureRecognizer rightMouseDown:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1527421-rightmousedown)Added [-[NSGestureRecognizer rightMouseDragged:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1529778-rightmousedragged)Added [-[NSGestureRecognizer rightMouseUp:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1525729-rightmouseup)Added [-[NSGestureRecognizer rotateWithEvent:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1531401-rotate)Added [-[NSGestureRecognizer shouldBeRequiredToFailByGestureRecognizer:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1530755-shouldberequiredtofailbygesturer)Added [-[NSGestureRecognizer shouldRequireFailureOfGestureRecognizer:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1532939-shouldrequirefailure)Added [NSGestureRecognizer.state](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1535694-state)Added [-[NSGestureRecognizer tabletPoint:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1529889-tabletpoint)Added [NSGestureRecognizer.target](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1530932-target)Added [NSGestureRecognizer.view](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1527192-view)Added [NSGestureRecognizerDelegate](https://developer.apple.com/documentation/appkit/nsgesturerecognizerdelegate)Added [-[NSGestureRecognizerDelegate gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizerdelegate/1535422-gesturerecognizer)Added [-[NSGestureRecognizerDelegate gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizerdelegate/1529773-gesturerecognizer)Added [-[NSGestureRecognizerDelegate gestureRecognizer:shouldRequireFailureOfGestureRecognizer:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizerdelegate/1527318-gesturerecognizer)Added [-[NSGestureRecognizerDelegate gestureRecognizerShouldBegin:]](https://developer.apple.com/documentation/appkit/nsgesturerecognizerdelegate/1535463-gesturerecognizershouldbegin)Added NSGestureRecognizer(NSSubclassUse)Added [NSGestureRecognizerState](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/state)Added [NSGestureRecognizerStateBegan](https://developer.apple.com/documentation/appkit/nsgesturerecognizerstate/nsgesturerecognizerstatebegan)Added [NSGestureRecognizerStateCancelled](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/state/cancelled)Added [NSGestureRecognizerStateChanged](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/state/changed)Added [NSGestureRecognizerStateEnded](https://developer.apple.com/documentation/appkit/nsgesturerecognizerstate/nsgesturerecognizerstateended)Added [NSGestureRecognizerStateFailed](https://developer.apple.com/documentation/appkit/nsgesturerecognizerstate/nsgesturerecognizerstatefailed)Added [NSGestureRecognizerStatePossible](https://developer.apple.com/documentation/appkit/nsgesturerecognizerstate/nsgesturerecognizerstatepossible)Added [NSGestureRecognizerStateRecognized](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/state/1525604-recognized)NSGlyphGenerator.hModified [+[NSGlyphGenerator sharedGlyphGenerator]](https://developer.apple.com/documentation/appkit/nsglyphgenerator/1425155-shared)

|  | Declaration |
| --- | --- |
| From | ``` + (id)sharedGlyphGenerator ``` |
| To | ``` + (NSGlyphGenerator *)sharedGlyphGenerator ``` |

NSGlyphInfo.hRemoved [-[NSGlyphInfo characterCollection]](https://developer.apple.com/documentation/appkit/nsglyphinfo/1447136-charactercollection)Removed [-[NSGlyphInfo characterIdentifier]](https://developer.apple.com/documentation/appkit/nsglyphinfo/1447120-characteridentifier)Removed [-[NSGlyphInfo glyphName]](https://developer.apple.com/documentation/appkit/nsglyphinfo/1447132-glyphname)Added [NSGlyphInfo.characterCollection](https://developer.apple.com/documentation/appkit/nsglyphinfo/1447136-charactercollection)Added [NSGlyphInfo.characterIdentifier](https://developer.apple.com/documentation/appkit/nsglyphinfo/1447120-characteridentifier)Added [NSGlyphInfo.glyphName](https://developer.apple.com/documentation/appkit/nsglyphinfo/1447132-glyphname)Modified [NSGlyphInfo](https://developer.apple.com/documentation/appkit/nsglyphinfo)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSGradient.hRemoved [-[NSGradient colorSpace]](https://developer.apple.com/documentation/appkit/nsgradient/1531310-colorspace)Removed [-[NSGradient numberOfColorStops]](https://developer.apple.com/documentation/appkit/nsgradient/1535846-numberofcolorstops)Added [NSGradient.colorSpace](https://developer.apple.com/documentation/appkit/nsgradient/1531310-colorspace)Added [NSGradient.numberOfColorStops](https://developer.apple.com/documentation/appkit/nsgradient/1535846-numberofcolorstops)Modified [-[NSGradient initWithColors:]](https://developer.apple.com/documentation/appkit/nsgradient/1535315-initwithcolors)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithColors:(NSArray *)colorArray ``` |
| To | ``` - (instancetype)initWithColors:(NSArray *)colorArray ``` |

Modified [-[NSGradient initWithColors:atLocations:colorSpace:]](https://developer.apple.com/documentation/appkit/nsgradient/1524459-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithColors:(NSArray *)colorArray atLocations:(const CGFloat *)locations colorSpace:(NSColorSpace *)colorSpace ``` |
| To | ``` - (instancetype)initWithColors:(NSArray *)colorArray atLocations:(const CGFloat *)locations colorSpace:(NSColorSpace *)colorSpace ``` |

Modified [-[NSGradient initWithColorsAndLocations:]](https://developer.apple.com/documentation/appkit/nsgradient/1555387-initwithcolorsandlocations)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithColorsAndLocations:(NSColor *)firstColor, ... ``` |
| To | ``` - (instancetype)initWithColorsAndLocations:(NSColor *)firstColor, ... ``` |

Modified [-[NSGradient initWithStartingColor:endingColor:]](https://developer.apple.com/documentation/appkit/nsgradient/1525448-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithStartingColor:(NSColor *)startingColor endingColor:(NSColor *)endingColor ``` |
| To | ``` - (instancetype)initWithStartingColor:(NSColor *)startingColor endingColor:(NSColor *)endingColor ``` |

NSGraphics.hAdded [NSCompositeColor](https://developer.apple.com/documentation/appkit/nscompositecolor)Added [NSCompositeColorBurn](https://developer.apple.com/documentation/appkit/nscompositecolorburn)Added [NSCompositeColorDodge](https://developer.apple.com/documentation/appkit/nscompositecolordodge)Added [NSCompositeDarken](https://developer.apple.com/documentation/appkit/nscompositedarken)Added [NSCompositeDifference](https://developer.apple.com/documentation/appkit/nscompositedifference)Added [NSCompositeExclusion](https://developer.apple.com/documentation/appkit/nscompositeexclusion)Added [NSCompositeHardLight](https://developer.apple.com/documentation/appkit/nscompositehardlight)Added [NSCompositeHue](https://developer.apple.com/documentation/appkit/nscompositehue)Added [NSCompositeLighten](https://developer.apple.com/documentation/appkit/nscompositelighten)Added [NSCompositeLuminosity](https://developer.apple.com/documentation/appkit/nscompositeluminosity)Added [NSCompositeMultiply](https://developer.apple.com/documentation/appkit/nscompositemultiply)Added [NSCompositeOverlay](https://developer.apple.com/documentation/appkit/nscompositeoverlay)Added [NSCompositeSaturation](https://developer.apple.com/documentation/appkit/nscompositesaturation)Added [NSCompositeScreen](https://developer.apple.com/documentation/appkit/nscompositescreen)Added [NSCompositeSoftLight](https://developer.apple.com/documentation/appkit/nscompositesoftlight)Modified [NSCompositeHighlight](https://developer.apple.com/documentation/appkit/nscompositehighlight)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.0 |

Modified [NSCopyBits()](https://developer.apple.com/documentation/appkit/1473630-nscopybits)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSCountWindows()](https://developer.apple.com/documentation/appkit/1473636-nscountwindows)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [NSCountWindowsForContext()](https://developer.apple.com/documentation/appkit/1473767-nscountwindowsforcontext)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [NSHighlightRect()](https://developer.apple.com/documentation/appkit/1473592-nshighlightrect)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.0 |

Modified [NSWindowList()](https://developer.apple.com/documentation/appkit/1473806-nswindowlist)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [NSWindowListForContext()](https://developer.apple.com/documentation/appkit/1473755-nswindowlistforcontext)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

NSGraphicsContext.hRemoved [-[NSGraphicsContext CIContext]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1534326-cicontext)Removed [-[NSGraphicsContext attributes]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1528254-attributes)Removed [-[NSGraphicsContext colorRenderingIntent]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1533527-colorrenderingintent)Removed [-[NSGraphicsContext compositingOperation]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1525984-compositingoperation)Removed [-[NSGraphicsContext graphicsPort]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1524914-graphicsport)Removed [-[NSGraphicsContext imageInterpolation]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1529711-imageinterpolation)Removed [-[NSGraphicsContext isDrawingToScreen]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1524673-isdrawingtoscreen)Removed [-[NSGraphicsContext isFlipped]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1531568-flipped)Removed [-[NSGraphicsContext patternPhase]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1527510-patternphase)Removed [-[NSGraphicsContext setColorRenderingIntent:]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1533527-colorrenderingintent)Removed [-[NSGraphicsContext setCompositingOperation:]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1525984-compositingoperation)Removed [-[NSGraphicsContext setImageInterpolation:]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1529711-imageinterpolation)Removed [-[NSGraphicsContext setPatternPhase:]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1527510-patternphase)Removed [-[NSGraphicsContext setShouldAntialias:]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1529486-shouldantialias)Removed [-[NSGraphicsContext shouldAntialias]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1529486-shouldantialias)Added [NSGraphicsContext.CGContext](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1524878-cgcontext)Added [NSGraphicsContext.CIContext](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1534326-cicontext)Added [NSGraphicsContext.attributes](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1528254-attributes)Added [NSGraphicsContext.colorRenderingIntent](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1533527-colorrenderingintent)Added [NSGraphicsContext.compositingOperation](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1525984-compositingoperation)Added [NSGraphicsContext.drawingToScreen](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1524673-drawingtoscreen)Added [NSGraphicsContext.flipped](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1531568-flipped)Added [-[NSGraphicsContext focusStack]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1564181-focusstack)Added [+[NSGraphicsContext graphicsContextWithCGContext:flipped:]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1535380-graphicscontextwithcgcontext)Added [NSGraphicsContext.graphicsPort](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1524914-graphicsport)Added [NSGraphicsContext.imageInterpolation](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1529711-imageinterpolation)Added [NSGraphicsContext.patternPhase](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1527510-patternphase)Added [-[NSGraphicsContext setFocusStack:]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1564182-setfocusstack)Added [NSGraphicsContext.shouldAntialias](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1529486-shouldantialias)Added NSGraphicsContext(NSGraphicsContextDeprecated)Modified [+[NSGraphicsContext graphicsContextWithGraphicsPort:flipped:]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1529263-graphicscontextwithgraphicsport)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[NSGraphicsContext setGraphicsState:]](https://developer.apple.com/documentation/appkit/nsgraphicscontext/1531891-setgraphicsstate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

NSImage.hRemoved [-[NSImage TIFFRepresentation]](https://developer.apple.com/documentation/appkit/nsimage/1519841-tiffrepresentation)Removed [-[NSImage accessibilityDescription]](https://developer.apple.com/documentation/appkit/nsimage/1519943-accessibilitydescription)Removed [-[NSImage alignmentRect]](https://developer.apple.com/documentation/appkit/nsimage/1519905-alignmentrect)Removed [-[NSImage backgroundColor]](https://developer.apple.com/documentation/appkit/nsimage/1520059-backgroundcolor)Removed [-[NSImage cacheMode]](https://developer.apple.com/documentation/appkit/nsimage/1519850-cachemode)Removed [-[NSImage delegate]](https://developer.apple.com/documentation/appkit/nsimage/1519926-delegate)Removed [-[NSImage isValid]](https://developer.apple.com/documentation/appkit/nsimage/1519991-valid)Removed [-[NSImage matchesOnMultipleResolution]](https://developer.apple.com/documentation/appkit/nsimage/1519963-matchesonmultipleresolution)Removed [-[NSImage matchesOnlyOnBestFittingAxis]](https://developer.apple.com/documentation/appkit/nsimage/1519848-matchesonlyonbestfittingaxis)Removed [-[NSImage prefersColorMatch]](https://developer.apple.com/documentation/appkit/nsimage/1520010-preferscolormatch)Removed [-[NSImage representations]](https://developer.apple.com/documentation/appkit/nsimage/1519858-representations)Removed [-[NSImage setAccessibilityDescription:]](https://developer.apple.com/documentation/appkit/nsimage/1519943-accessibilitydescription)Removed [-[NSImage setAlignmentRect:]](https://developer.apple.com/documentation/appkit/nsimage/1519905-alignmentrect)Removed [-[NSImage setBackgroundColor:]](https://developer.apple.com/documentation/appkit/nsimage/1520059-backgroundcolor)Removed [-[NSImage setCacheMode:]](https://developer.apple.com/documentation/appkit/nsimage/1519850-cachemode)Removed [-[NSImage setDelegate:]](https://developer.apple.com/documentation/appkit/nsimage/1519926-delegate)Removed [-[NSImage setMatchesOnMultipleResolution:]](https://developer.apple.com/documentation/appkit/nsimage/1519963-matchesonmultipleresolution)Removed [-[NSImage setMatchesOnlyOnBestFittingAxis:]](https://developer.apple.com/documentation/appkit/nsimage/1519848-matchesonlyonbestfittingaxis)Removed [-[NSImage setPrefersColorMatch:]](https://developer.apple.com/documentation/appkit/nsimage/1520010-preferscolormatch)Removed [-[NSImage setSize:]](https://developer.apple.com/documentation/appkit/nsimage/1519987-size)Removed [-[NSImage setUsesEPSOnResolutionMismatch:]](https://developer.apple.com/documentation/appkit/nsimage/1519868-usesepsonresolutionmismatch)Removed [-[NSImage size]](https://developer.apple.com/documentation/appkit/nsimage/1519987-size)Removed [-[NSImage usesEPSOnResolutionMismatch]](https://developer.apple.com/documentation/appkit/nsimage/1519868-usesepsonresolutionmismatch)Added [NSImage.TIFFRepresentation](https://developer.apple.com/documentation/appkit/nsimage/1519841-tiffrepresentation)Added [NSImage.accessibilityDescription](https://developer.apple.com/documentation/appkit/nsimage/1519943-accessibilitydescription)Added [NSImage.alignmentRect](https://developer.apple.com/documentation/appkit/nsimage/1519905-alignmentrect)Added [NSImage.backgroundColor](https://developer.apple.com/documentation/appkit/nsimage/1520059-backgroundcolor)Added [NSImage.cacheMode](https://developer.apple.com/documentation/appkit/nsimage/1519850-cachemode)Added [NSImage.capInsets](https://developer.apple.com/documentation/appkit/nsimage/1520012-capinsets)Added [NSImage.delegate](https://developer.apple.com/documentation/appkit/nsimage/1519926-delegate)Added [NSImage.matchesOnMultipleResolution](https://developer.apple.com/documentation/appkit/nsimage/1519963-matchesonmultipleresolution)Added [NSImage.matchesOnlyOnBestFittingAxis](https://developer.apple.com/documentation/appkit/nsimage/1519848-matchesonlyonbestfittingaxis)Added [NSImage.prefersColorMatch](https://developer.apple.com/documentation/appkit/nsimage/1520010-preferscolormatch)Added [NSImage.representations](https://developer.apple.com/documentation/appkit/nsimage/1519858-representations)Added [NSImage.resizingMode](https://developer.apple.com/documentation/appkit/nsimage/1520060-resizingmode)Added [NSImage.size](https://developer.apple.com/documentation/appkit/nsimage/1519987-size)Added [NSImage.usesEPSOnResolutionMismatch](https://developer.apple.com/documentation/appkit/nsimage/1519868-usesepsonresolutionmismatch)Added [NSImage.valid](https://developer.apple.com/documentation/appkit/nsimage/1519991-valid)Added [NSImageResizingMode](https://developer.apple.com/documentation/appkit/nsimageresizingmode)Added [NSImageResizingModeStretch](https://developer.apple.com/documentation/appkit/nsimage/resizingmode/stretch)Added [NSImageResizingModeTile](https://developer.apple.com/documentation/appkit/nsimageresizingmode/nsimageresizingmodetile)Modified [NSImage](https://developer.apple.com/documentation/appkit/nsimage)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSPasteboardReading, NSPasteboardWriting |
| To | NSCoding, NSCopying, NSPasteboardReading, NSPasteboardWriting, NSSecureCoding |

Modified [+[NSImage imageFileTypes]](https://developer.apple.com/documentation/appkit/nsimage/1519989-imagefiletypes)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[NSImage imageNamed:]](https://developer.apple.com/documentation/appkit/nsimage/1520015-imagenamed)

|  | Declaration |
| --- | --- |
| From | ``` + (id)imageNamed:(NSString *)name ``` |
| To | ``` + (NSImage *)imageNamed:(NSString *)name ``` |

Modified [+[NSImage imagePasteboardTypes]](https://developer.apple.com/documentation/appkit/nsimage/1519924-imagepasteboardtypes)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[NSImage imageUnfilteredFileTypes]](https://developer.apple.com/documentation/appkit/nsimage/1519973-imageunfilteredfiletypes)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[NSImage imageUnfilteredPasteboardTypes]](https://developer.apple.com/documentation/appkit/nsimage/1519872-imageunfilteredpasteboardtypes)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[NSImage imageWithSize:flipped:drawingHandler:]](https://developer.apple.com/documentation/appkit/nsimage/1519860-imagewithsize)

|  | Declaration |
| --- | --- |
| From | ``` + (id)imageWithSize:(NSSize)size flipped:(BOOL)drawingHandlerShouldBeCalledWithFlippedContext drawingHandler:(BOOL (^)(NSRect dstRect))drawingHandler ``` |
| To | ``` + (NSImage *)imageWithSize:(NSSize)size flipped:(BOOL)drawingHandlerShouldBeCalledWithFlippedContext drawingHandler:(BOOL (^)(NSRect dstRect))drawingHandler ``` |

Modified [-[NSImage initByReferencingFile:]](https://developer.apple.com/documentation/appkit/nsimage/1519955-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initByReferencingFile:(NSString *)fileName ``` |
| To | ``` - (instancetype)initByReferencingFile:(NSString *)fileName ``` |

Modified [-[NSImage initByReferencingURL:]](https://developer.apple.com/documentation/appkit/nsimage/1519990-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initByReferencingURL:(NSURL *)url ``` |
| To | ``` - (instancetype)initByReferencingURL:(NSURL *)url ``` |

Modified [-[NSImage initWithCGImage:size:]](https://developer.apple.com/documentation/appkit/nsimage/1519939-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCGImage:(CGImageRef)cgImage size:(NSSize)size ``` |
| To | ``` - (instancetype)initWithCGImage:(CGImageRef)cgImage size:(NSSize)size ``` |

Modified [-[NSImage initWithContentsOfFile:]](https://developer.apple.com/documentation/appkit/nsimage/1519918-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfFile:(NSString *)fileName ``` |
| To | ``` - (instancetype)initWithContentsOfFile:(NSString *)fileName ``` |

Modified [-[NSImage initWithContentsOfURL:]](https://developer.apple.com/documentation/appkit/nsimage/1519907-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)url ``` |
| To | ``` - (instancetype)initWithContentsOfURL:(NSURL *)url ``` |

Modified [-[NSImage initWithData:]](https://developer.apple.com/documentation/appkit/nsimage/1519941-initwithdata)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(NSData *)data ``` |
| To | ``` - (instancetype)initWithData:(NSData *)data ``` |

Modified [-[NSImage initWithDataIgnoringOrientation:]](https://developer.apple.com/documentation/appkit/nsimage/1519915-initwithdataignoringorientation)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDataIgnoringOrientation:(NSData *)data ``` |
| To | ``` - (instancetype)initWithDataIgnoringOrientation:(NSData *)data ``` |

Modified [-[NSImage initWithIconRef:]](https://developer.apple.com/documentation/appkit/nsimage/1519930-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithIconRef:(IconRef)iconRef ``` |
| To | ``` - (instancetype)initWithIconRef:(IconRef)iconRef ``` |

Modified [-[NSImage initWithPasteboard:]](https://developer.apple.com/documentation/appkit/nsimage/1519952-initwithpasteboard)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithPasteboard:(NSPasteboard *)pasteboard ``` |
| To | ``` - (instancetype)initWithPasteboard:(NSPasteboard *)pasteboard ``` |

Modified [-[NSImage initWithSize:]](https://developer.apple.com/documentation/appkit/nsimage/1520033-initwithsize)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithSize:(NSSize)aSize ``` |
| To | ``` - (instancetype)initWithSize:(NSSize)aSize ``` |

Modified [-[NSImageDelegate image:didLoadPartOfRepresentation:withValidRows:]](https://developer.apple.com/documentation/appkit/nsimagedelegate/1519916-image)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSImageDelegate image:didLoadRepresentation:withStatus:]](https://developer.apple.com/documentation/appkit/nsimagedelegate/1520028-image)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSImageDelegate image:didLoadRepresentationHeader:]](https://developer.apple.com/documentation/appkit/nsimagedelegate/1519945-image)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSImageDelegate image:willLoadRepresentation:]](https://developer.apple.com/documentation/appkit/nsimagedelegate/1519934-image)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSImageDelegate imageDidNotDraw:inRect:]](https://developer.apple.com/documentation/appkit/nsimagedelegate/1519927-imagedidnotdraw)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [NSImageNameDotMac](https://developer.apple.com/documentation/appkit/nsimagenamedotmac)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

NSImageCell.hRemoved [-[NSImageCell imageAlignment]](https://developer.apple.com/documentation/appkit/nsimagecell/1524421-imagealignment)Removed [-[NSImageCell imageFrameStyle]](https://developer.apple.com/documentation/appkit/nsimagecell/1526164-imageframestyle)Removed [-[NSImageCell imageScaling]](https://developer.apple.com/documentation/appkit/nsimagecell/1532559-imagescaling)Removed [-[NSImageCell setImageAlignment:]](https://developer.apple.com/documentation/appkit/nsimagecell/1524421-imagealignment)Removed [-[NSImageCell setImageFrameStyle:]](https://developer.apple.com/documentation/appkit/nsimagecell/1526164-imageframestyle)Removed [-[NSImageCell setImageScaling:]](https://developer.apple.com/documentation/appkit/nsimagecell/1532559-imagescaling)Added [NSImageCell.imageAlignment](https://developer.apple.com/documentation/appkit/nsimagecell/1524421-imagealignment)Added [NSImageCell.imageFrameStyle](https://developer.apple.com/documentation/appkit/nsimagecell/1526164-imageframestyle)Added [NSImageCell.imageScaling](https://developer.apple.com/documentation/appkit/nsimagecell/1532559-imagescaling)NSImageRep.hRemoved [-[NSImageRep bitsPerSample]](https://developer.apple.com/documentation/appkit/nsimagerep/1533157-bitspersample)Removed [-[NSImageRep colorSpaceName]](https://developer.apple.com/documentation/appkit/nsimagerep/1535395-colorspacename)Removed -[NSImageRep hasAlpha]Removed -[NSImageRep isOpaque]Removed [-[NSImageRep pixelsHigh]](https://developer.apple.com/documentation/appkit/nsimagerep/1533989-pixelshigh)Removed [-[NSImageRep pixelsWide]](https://developer.apple.com/documentation/appkit/nsimagerep/1526995-pixelswide)Removed [-[NSImageRep setAlpha:]](https://developer.apple.com/documentation/appkit/nsimagerep/1534506-hasalpha)Removed [-[NSImageRep setBitsPerSample:]](https://developer.apple.com/documentation/appkit/nsimagerep/1533157-bitspersample)Removed [-[NSImageRep setColorSpaceName:]](https://developer.apple.com/documentation/appkit/nsimagerep/1535395-colorspacename)Removed [-[NSImageRep setOpaque:]](https://developer.apple.com/documentation/appkit/nsimagerep/1528462-opaque)Removed [-[NSImageRep setPixelsHigh:]](https://developer.apple.com/documentation/appkit/nsimagerep/1533989-pixelshigh)Removed [-[NSImageRep setPixelsWide:]](https://developer.apple.com/documentation/appkit/nsimagerep/1526995-pixelswide)Removed [-[NSImageRep setSize:]](https://developer.apple.com/documentation/appkit/nsimagerep/1524374-size)Removed [-[NSImageRep size]](https://developer.apple.com/documentation/appkit/nsimagerep/1524374-size)Added [NSImageRep.alpha](https://developer.apple.com/documentation/appkit/nsimagerep/1534506-alpha)Added [NSImageRep.bitsPerSample](https://developer.apple.com/documentation/appkit/nsimagerep/1533157-bitspersample)Added [NSImageRep.colorSpaceName](https://developer.apple.com/documentation/appkit/nsimagerep/1535395-colorspacename)Added [-[NSImageRep init]](https://developer.apple.com/documentation/appkit/nsimagerep/1530271-init)Added [-[NSImageRep initWithCoder:]](https://developer.apple.com/documentation/appkit/nsimagerep/1535319-init)Added [NSImageRep.opaque](https://developer.apple.com/documentation/appkit/nsimagerep/1528462-isopaque)Added [NSImageRep.pixelsHigh](https://developer.apple.com/documentation/appkit/nsimagerep/1533989-pixelshigh)Added [NSImageRep.pixelsWide](https://developer.apple.com/documentation/appkit/nsimagerep/1526995-pixelswide)Added [NSImageRep.size](https://developer.apple.com/documentation/appkit/nsimagerep/1524374-size)Modified [+[NSImageRep imageFileTypes]](https://developer.apple.com/documentation/appkit/nsimagerep/1532660-imagefiletypes)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[NSImageRep imagePasteboardTypes]](https://developer.apple.com/documentation/appkit/nsimagerep/1527425-imagepasteboardtypes)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[NSImageRep imageRepClassForFileType:]](https://developer.apple.com/documentation/appkit/nsimagerep/1535328-imagerepclassforfiletype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[NSImageRep imageRepClassForPasteboardType:]](https://developer.apple.com/documentation/appkit/nsimagerep/1527017-imagerepclassforpasteboardtype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[NSImageRep imageUnfilteredFileTypes]](https://developer.apple.com/documentation/appkit/nsimagerep/1534890-imageunfilteredfiletypes)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[NSImageRep imageUnfilteredPasteboardTypes]](https://developer.apple.com/documentation/appkit/nsimagerep/1525257-imageunfilteredpasteboardtypes)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

NSImageView.hRemoved [-[NSImageView allowsCutCopyPaste]](https://developer.apple.com/documentation/appkit/nsimageview/1404961-allowscutcopypaste)Removed [-[NSImageView animates]](https://developer.apple.com/documentation/appkit/nsimageview/1404950-animates)Removed [-[NSImageView image]](https://developer.apple.com/documentation/appkit/nsimageview/1404952-image)Removed [-[NSImageView imageAlignment]](https://developer.apple.com/documentation/appkit/nsimageview/1404963-imagealignment)Removed [-[NSImageView imageFrameStyle]](https://developer.apple.com/documentation/appkit/nsimageview/1404948-imageframestyle)Removed [-[NSImageView imageScaling]](https://developer.apple.com/documentation/appkit/nsimageview/1404956-imagescaling)Removed [-[NSImageView isEditable]](https://developer.apple.com/documentation/appkit/nsimageview/1404954-editable)Removed [-[NSImageView setAllowsCutCopyPaste:]](https://developer.apple.com/documentation/appkit/nsimageview/1404961-allowscutcopypaste)Removed [-[NSImageView setAnimates:]](https://developer.apple.com/documentation/appkit/nsimageview/1404950-animates)Removed [-[NSImageView setEditable:]](https://developer.apple.com/documentation/appkit/nsimageview/1404954-editable)Removed [-[NSImageView setImage:]](https://developer.apple.com/documentation/appkit/nsimageview/1404952-image)Removed [-[NSImageView setImageAlignment:]](https://developer.apple.com/documentation/appkit/nsimageview/1404963-imagealignment)Removed [-[NSImageView setImageFrameStyle:]](https://developer.apple.com/documentation/appkit/nsimageview/1404948-imageframestyle)Removed [-[NSImageView setImageScaling:]](https://developer.apple.com/documentation/appkit/nsimageview/1404956-imagescaling)Added [NSImageView.allowsCutCopyPaste](https://developer.apple.com/documentation/appkit/nsimageview/1404961-allowscutcopypaste)Added [NSImageView.animates](https://developer.apple.com/documentation/appkit/nsimageview/1404950-animates)Added [NSImageView.editable](https://developer.apple.com/documentation/appkit/nsimageview/1404954-iseditable)Added [NSImageView.image](https://developer.apple.com/documentation/appkit/nsimageview/1404952-image)Added [NSImageView.imageAlignment](https://developer.apple.com/documentation/appkit/nsimageview/1404963-imagealignment)Added [NSImageView.imageFrameStyle](https://developer.apple.com/documentation/appkit/nsimageview/1404948-imageframestyle)Added [NSImageView.imageScaling](https://developer.apple.com/documentation/appkit/nsimageview/1404956-imagescaling)Modified [NSImageView](https://developer.apple.com/documentation/appkit/nsimageview)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSAccessibilityImage |

NSInputManager.hModified [NSInputManager](https://developer.apple.com/documentation/appkit/nsinputmanager)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [+[NSInputManager currentInputManager]](https://developer.apple.com/documentation/appkit/nsinputmanager/1412820-currentinputmanager)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [+[NSInputManager cycleToNextInputLanguage:]](https://developer.apple.com/documentation/appkit/nsinputmanager/1412827-cycletonextinputlanguage)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [+[NSInputManager cycleToNextInputServerInLanguage:]](https://developer.apple.com/documentation/appkit/nsinputmanager/1412826-cycletonextinputserverinlanguage)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [-[NSInputManager handleMouseEvent:]](https://developer.apple.com/documentation/appkit/nsinputmanager/1412828-handlemouseevent)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [-[NSInputManager markedTextAbandoned:]](https://developer.apple.com/documentation/appkit/nsinputmanager/1412817-markedtextabandoned)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [-[NSInputManager markedTextSelectionChanged:client:]](https://developer.apple.com/documentation/appkit/nsinputmanager/1412846-markedtextselectionchanged)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [-[NSInputManager wantsToHandleMouseEvents]](https://developer.apple.com/documentation/appkit/nsinputmanager/1412815-wantstohandlemouseevents)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [-[NSTextInput attributedSubstringFromRange:]](https://developer.apple.com/documentation/appkit/nstextinput/1412836-attributedsubstringfromrange)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [-[NSTextInput characterIndexForPoint:]](https://developer.apple.com/documentation/appkit/nstextinput/1412847-characterindexforpoint)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [-[NSTextInput conversationIdentifier]](https://developer.apple.com/documentation/appkit/nstextinput/1412823-conversationidentifier)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [-[NSTextInput doCommandBySelector:]](https://developer.apple.com/documentation/appkit/nstextinput/1412853-docommandbyselector)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [-[NSTextInput firstRectForCharacterRange:]](https://developer.apple.com/documentation/appkit/nstextinput/1412838-firstrectforcharacterrange)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [-[NSTextInput hasMarkedText]](https://developer.apple.com/documentation/appkit/nstextinput/1412824-hasmarkedtext)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [-[NSTextInput insertText:]](https://developer.apple.com/documentation/appkit/nstextinput/1412816-inserttext)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [-[NSTextInput markedRange]](https://developer.apple.com/documentation/appkit/nstextinput/1412831-markedrange)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [-[NSTextInput selectedRange]](https://developer.apple.com/documentation/appkit/nstextinput/1412848-selectedrange)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [-[NSTextInput setMarkedText:selectedRange:]](https://developer.apple.com/documentation/appkit/nstextinput/1412851-setmarkedtext)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [-[NSTextInput unmarkText]](https://developer.apple.com/documentation/appkit/nstextinput/1412840-unmarktext)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [-[NSTextInput validAttributesForMarkedText]](https://developer.apple.com/documentation/appkit/nstextinput/1412825-validattributesformarkedtext)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

NSInputServer.hModified [NSInputServer](https://developer.apple.com/documentation/appkit/nsinputserver)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

NSInterfaceStyle.hModified [NSMacintoshInterfaceStyle](https://developer.apple.com/documentation/appkit/1555069-anonymous/nsmacintoshinterfacestyle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.8 |

Modified [NSNextStepInterfaceStyle](https://developer.apple.com/documentation/appkit/1555069-anonymous/nsnextstepinterfacestyle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.8 |

Modified [NSNoInterfaceStyle](https://developer.apple.com/documentation/appkit/1555069-anonymous/nsnointerfacestyle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.8 |

Modified [NSWindows95InterfaceStyle](https://developer.apple.com/documentation/appkit/1555069-anonymous/nswindows95interfacestyle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.8 |

NSItemProvider.h (Added)Added [NSItemProvider.containerFrame](https://developer.apple.com/documentation/foundation/nsitemprovider/1528571-containerframe)Added [NSItemProvider.preferredPresentationSize](https://developer.apple.com/documentation/foundation/nsitemprovider/1528574-preferredpresentationsize)Added [NSItemProvider.sourceFrame](https://developer.apple.com/documentation/foundation/nsitemprovider/1528569-sourceframe)Added NSItemProvider(NSItemSourceInfo)Added [NSTypeIdentifierAddressText](https://developer.apple.com/documentation/appkit/nstypeidentifieraddresstext)Added [NSTypeIdentifierDateText](https://developer.apple.com/documentation/appkit/nstypeidentifierdatetext)Added [NSTypeIdentifierPhoneNumberText](https://developer.apple.com/documentation/appkit/nstypeidentifierphonenumbertext)Added [NSTypeIdentifierTransitInformationText](https://developer.apple.com/documentation/appkit/nstypeidentifiertransitinformationtext)NSKeyValueBinding.hRemoved [-[NSObject exposedBindings]](https://developer.apple.com/documentation/objectivec/nsobject/1458048-exposedbindings)Added [NSObject.exposedBindings](https://developer.apple.com/documentation/objectivec/nsobject/1458048-exposedbindings)NSLayoutConstraint.hRemoved [-[NSView alignmentRectInsets]](https://developer.apple.com/documentation/appkit/nsview/1526870-alignmentrectinsets)Removed [-[NSView baselineOffsetFromBottom]](https://developer.apple.com/documentation/appkit/nsview/1526949-baselineoffsetfrombottom)Removed [-[NSView constraints]](https://developer.apple.com/documentation/appkit/nsview/1526917-constraints)Removed [-[NSView fittingSize]](https://developer.apple.com/documentation/appkit/nsview/1526904-fittingsize)Removed [-[NSView hasAmbiguousLayout]](https://developer.apple.com/documentation/appkit/nsview/1526907-hasambiguouslayout)Removed [-[NSView intrinsicContentSize]](https://developer.apple.com/documentation/appkit/nsview/1526996-intrinsiccontentsize)Removed [-[NSView needsLayout]](https://developer.apple.com/documentation/appkit/nsview/1526912-needslayout)Removed [-[NSView needsUpdateConstraints]](https://developer.apple.com/documentation/appkit/nsview/1526856-needsupdateconstraints)Removed [-[NSView setNeedsLayout:]](https://developer.apple.com/documentation/appkit/nsview/1526912-needslayout)Removed [-[NSView setNeedsUpdateConstraints:]](https://developer.apple.com/documentation/appkit/nsview/1526856-needsupdateconstraints)Removed [-[NSView setTranslatesAutoresizingMaskIntoConstraints:]](https://developer.apple.com/documentation/appkit/nsview/1526961-translatesautoresizingmaskintoco)Removed [-[NSView translatesAutoresizingMaskIntoConstraints]](https://developer.apple.com/documentation/appkit/nsview/1526961-translatesautoresizingmaskintoco)Removed NSLayoutPriorityDefaultHighRemoved NSLayoutPriorityDefaultLowRemoved NSLayoutPriorityDragThatCanResizeWindowRemoved NSLayoutPriorityDragThatCannotResizeWindowRemoved NSLayoutPriorityFittingSizeCompressionRemoved NSLayoutPriorityRequiredRemoved NSLayoutPriorityWindowSizeStayPutAdded [+[NSLayoutConstraint activateConstraints:]](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526955-activate)Added [NSLayoutConstraint.active](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1527000-isactive)Added [+[NSLayoutConstraint deactivateConstraints:]](https://developer.apple.com/documentation/uikit/nslayoutconstraint/1526066-deactivateconstraints)Added [NSView.alignmentRectInsets](https://developer.apple.com/documentation/appkit/nsview/1526870-alignmentrectinsets)Added [NSView.baselineOffsetFromBottom](https://developer.apple.com/documentation/appkit/nsview/1526949-baselineoffsetfrombottom)Added [NSView.constraints](https://developer.apple.com/documentation/appkit/nsview/1526917-constraints)Added [NSView.fittingSize](https://developer.apple.com/documentation/appkit/nsview/1526904-fittingsize)Added [NSView.hasAmbiguousLayout](https://developer.apple.com/documentation/appkit/nsview/1526907-hasambiguouslayout)Added [NSView.intrinsicContentSize](https://developer.apple.com/documentation/appkit/nsview/1526996-intrinsiccontentsize)Added [NSView.needsLayout](https://developer.apple.com/documentation/appkit/nsview/1526912-needslayout)Added [NSView.needsUpdateConstraints](https://developer.apple.com/documentation/appkit/nsview/1526856-needsupdateconstraints)Added [NSView.translatesAutoresizingMaskIntoConstraints](https://developer.apple.com/documentation/appkit/nsview/1526961-translatesautoresizingmaskintoco)Added [NSLayoutPriorityDefaultHigh](https://developer.apple.com/documentation/appkit/nslayoutconstraint/priority/1526966-defaulthigh)Added [NSLayoutPriorityDefaultLow](https://developer.apple.com/documentation/appkit/nslayoutprioritydefaultlow)Added [NSLayoutPriorityDragThatCanResizeWindow](https://developer.apple.com/documentation/appkit/nslayoutconstraint/priority/1526940-dragthatcanresizewindow)Added [NSLayoutPriorityDragThatCannotResizeWindow](https://developer.apple.com/documentation/appkit/nslayoutprioritydragthatcannotresizewindow)Added [NSLayoutPriorityFittingSizeCompression](https://developer.apple.com/documentation/appkit/nslayoutconstraint/priority/1526862-fittingsizecompression)Added [NSLayoutPriorityRequired](https://developer.apple.com/documentation/appkit/nslayoutconstraint/priority/1526880-required)Added [NSLayoutPriorityWindowSizeStayPut](https://developer.apple.com/documentation/appkit/nslayoutconstraint/priority/1526895-windowsizestayput)Modified [+[NSLayoutConstraint constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:]](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526954-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)constraintWithItem:(id)view1 attribute:(NSLayoutAttribute)attr1 relatedBy:(NSLayoutRelation)relation toItem:(id)view2 attribute:(NSLayoutAttribute)attr2 multiplier:(CGFloat)multiplier constant:(CGFloat)c ``` |
| To | ``` + (instancetype)constraintWithItem:(id)view1 attribute:(NSLayoutAttribute)attr1 relatedBy:(NSLayoutRelation)relation toItem:(id)view2 attribute:(NSLayoutAttribute)attr2 multiplier:(CGFloat)multiplier constant:(CGFloat)c ``` |

NSLayoutManager.hRemoved [-[NSLayoutManager allowsNonContiguousLayout]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403197-allowsnoncontiguouslayout)Removed [-[NSLayoutManager attributedString]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1807628-attributedstring)Removed [-[NSLayoutManager backgroundLayoutEnabled]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1402952-backgroundlayoutenabled)Removed [-[NSLayoutManager defaultAttachmentScaling]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403045-defaultattachmentscaling)Removed [-[NSLayoutManager delegate]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402920-delegate)Removed [-[NSLayoutManager extraLineFragmentRect]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403175-extralinefragmentrect)Removed [-[NSLayoutManager extraLineFragmentTextContainer]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403165-extralinefragmenttextcontainer)Removed [-[NSLayoutManager extraLineFragmentUsedRect]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402988-extralinefragmentusedrect)Removed [-[NSLayoutManager firstTextView]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1402995-firsttextview)Removed [-[NSLayoutManager firstUnlaidCharacterIndex]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403067-firstunlaidcharacterindex)Removed [-[NSLayoutManager firstUnlaidGlyphIndex]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403245-firstunlaidglyphindex)Removed [-[NSLayoutManager glyphGenerator]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403069-glyphgenerator)Removed [-[NSLayoutManager hasNonContiguousLayout]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403207-hasnoncontiguouslayout)Removed [-[NSLayoutManager hyphenationFactor]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403134-hyphenationfactor)Removed [-[NSLayoutManager layoutOptions]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1807703-layoutoptions)Removed [-[NSLayoutManager numberOfGlyphs]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402937-numberofglyphs)Removed [-[NSLayoutManager setAllowsNonContiguousLayout:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403197-allowsnoncontiguouslayout)Removed [-[NSLayoutManager setBackgroundLayoutEnabled:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1402952-backgroundlayoutenabled)Removed [-[NSLayoutManager setDefaultAttachmentScaling:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403045-defaultattachmentscaling)Removed [-[NSLayoutManager setDelegate:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402920-delegate)Removed [-[NSLayoutManager setGlyphGenerator:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403069-glyphgenerator)Removed [-[NSLayoutManager setHyphenationFactor:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403134-hyphenationfactor)Removed [-[NSLayoutManager setShowsControlCharacters:]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402912-showscontrolcharacters)Removed [-[NSLayoutManager setShowsInvisibleCharacters:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403254-showsinvisiblecharacters)Removed [-[NSLayoutManager setTextStorage:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403015-textstorage)Removed [-[NSLayoutManager setTypesetter:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403205-typesetter)Removed [-[NSLayoutManager setTypesetterBehavior:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403199-typesetterbehavior)Removed [-[NSLayoutManager setUsesFontLeading:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403156-usesfontleading)Removed [-[NSLayoutManager setUsesScreenFonts:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403075-usesscreenfonts)Removed [-[NSLayoutManager showsControlCharacters]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402912-showscontrolcharacters)Removed [-[NSLayoutManager showsInvisibleCharacters]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403254-showsinvisiblecharacters)Removed [-[NSLayoutManager textContainers]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403144-textcontainers)Removed [-[NSLayoutManager textStorage]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403015-textstorage)Removed [-[NSLayoutManager textViewForBeginningOfSelection]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403089-textviewforbeginningofselection)Removed [-[NSLayoutManager typesetter]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403205-typesetter)Removed [-[NSLayoutManager typesetterBehavior]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403199-typesetterbehavior)Removed [-[NSLayoutManager usesFontLeading]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403156-usesfontleading)Removed [-[NSLayoutManager usesScreenFonts]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403075-usesscreenfonts)Added [NSLayoutManager.allowsNonContiguousLayout](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403197-allowsnoncontiguouslayout)Added [NSLayoutManager.attributedString](https://developer.apple.com/documentation/appkit/nslayoutmanager/1807628-attributedstring)Added [NSLayoutManager.backgroundLayoutEnabled](https://developer.apple.com/documentation/appkit/nslayoutmanager/1402952-backgroundlayoutenabled)Added [NSLayoutManager.defaultAttachmentScaling](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403045-defaultattachmentscaling)Added [NSLayoutManager.delegate](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402920-delegate)Added [NSLayoutManager.extraLineFragmentRect](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403175-extralinefragmentrect)Added [NSLayoutManager.extraLineFragmentTextContainer](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403165-extralinefragmenttextcontainer)Added [NSLayoutManager.extraLineFragmentUsedRect](https://developer.apple.com/documentation/appkit/nslayoutmanager/1402988-extralinefragmentusedrect)Added [NSLayoutManager.firstTextView](https://developer.apple.com/documentation/appkit/nslayoutmanager/1402995-firsttextview)Added [NSLayoutManager.firstUnlaidCharacterIndex](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403067-firstunlaidcharacterindex)Added [NSLayoutManager.firstUnlaidGlyphIndex](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403245-firstunlaidglyphindex)Added [NSLayoutManager.glyphGenerator](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403069-glyphgenerator)Added [NSLayoutManager.hasNonContiguousLayout](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403207-hasnoncontiguouslayout)Added [NSLayoutManager.hyphenationFactor](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403134-hyphenationfactor)Added [NSLayoutManager.layoutOptions](https://developer.apple.com/documentation/uikit/nslayoutmanager/1807703-layoutoptions)Added [NSLayoutManager.numberOfGlyphs](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402937-numberofglyphs)Added [NSLayoutManager.showsControlCharacters](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402912-showscontrolcharacters)Added [NSLayoutManager.showsInvisibleCharacters](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403254-showsinvisiblecharacters)Added [NSLayoutManager.textContainers](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403144-textcontainers)Added [NSLayoutManager.textStorage](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403015-textstorage)Added [NSLayoutManager.textViewForBeginningOfSelection](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403089-textviewforbeginningofselection)Added [NSLayoutManager.typesetter](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403205-typesetter)Added [NSLayoutManager.typesetterBehavior](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403199-typesetterbehavior)Added [NSLayoutManager.usesFontLeading](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403156-usesfontleading)Added [NSLayoutManager.usesScreenFonts](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403075-usesscreenfonts)Modified [-[NSLayoutManager init]](https://developer.apple.com/documentation/uikit/nslayoutmanager/1402975-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)init ``` | -- |
| To | ``` - (instancetype)init ``` | yes |

Modified [-[NSLayoutManager textStorage:edited:range:changeInLength:invalidatedRange:]](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403142-textstorage)

|  | Declaration |
| --- | --- |
| From | ``` - (void)textStorage:(NSTextStorage *)str edited:(NSUInteger)editedMask range:(NSRange)newCharRange changeInLength:(NSInteger)delta invalidatedRange:(NSRange)invalidatedCharRange ``` |
| To | ``` - (void)textStorage:(NSTextStorage *)str edited:(NSTextStorageEditedOptions)editedMask range:(NSRange)newCharRange changeInLength:(NSInteger)delta invalidatedRange:(NSRange)invalidatedCharRange ``` |

Modified [-[NSLayoutManagerDelegate layoutManager:didCompleteLayoutForTextContainer:atEnd:]](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/1402926-layoutmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSLayoutManagerDelegate layoutManager:shouldUseTemporaryAttributes:forDrawingToScreen:atCharacterIndex:effectiveRange:]](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/1403085-layoutmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSLayoutManagerDelegate layoutManagerDidInvalidateLayout:]](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/1402993-layoutmanagerdidinvalidatelayout)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSLevelIndicator.hRemoved [-[NSLevelIndicator criticalValue]](https://developer.apple.com/documentation/appkit/nslevelindicator/1388821-criticalvalue)Removed [-[NSLevelIndicator maxValue]](https://developer.apple.com/documentation/appkit/nslevelindicator/1388839-maxvalue)Removed [-[NSLevelIndicator minValue]](https://developer.apple.com/documentation/appkit/nslevelindicator/1388829-minvalue)Removed [-[NSLevelIndicator numberOfMajorTickMarks]](https://developer.apple.com/documentation/appkit/nslevelindicator/1388819-numberofmajortickmarks)Removed [-[NSLevelIndicator numberOfTickMarks]](https://developer.apple.com/documentation/appkit/nslevelindicator/1388827-numberoftickmarks)Removed [-[NSLevelIndicator setCriticalValue:]](https://developer.apple.com/documentation/appkit/nslevelindicator/1388821-criticalvalue)Removed [-[NSLevelIndicator setMaxValue:]](https://developer.apple.com/documentation/appkit/nslevelindicator/1388839-maxvalue)Removed [-[NSLevelIndicator setMinValue:]](https://developer.apple.com/documentation/appkit/nslevelindicator/1388829-minvalue)Removed [-[NSLevelIndicator setNumberOfMajorTickMarks:]](https://developer.apple.com/documentation/appkit/nslevelindicator/1388819-numberofmajortickmarks)Removed [-[NSLevelIndicator setNumberOfTickMarks:]](https://developer.apple.com/documentation/appkit/nslevelindicator/1388827-numberoftickmarks)Removed [-[NSLevelIndicator setTickMarkPosition:]](https://developer.apple.com/documentation/appkit/nslevelindicator/1388837-tickmarkposition)Removed [-[NSLevelIndicator setWarningValue:]](https://developer.apple.com/documentation/appkit/nslevelindicator/1388835-warningvalue)Removed [-[NSLevelIndicator tickMarkPosition]](https://developer.apple.com/documentation/appkit/nslevelindicator/1388837-tickmarkposition)Removed [-[NSLevelIndicator warningValue]](https://developer.apple.com/documentation/appkit/nslevelindicator/1388835-warningvalue)Added [NSLevelIndicator.criticalValue](https://developer.apple.com/documentation/appkit/nslevelindicator/1388821-criticalvalue)Added [NSLevelIndicator.levelIndicatorStyle](https://developer.apple.com/documentation/appkit/nslevelindicator/1388833-levelindicatorstyle)Added [NSLevelIndicator.maxValue](https://developer.apple.com/documentation/appkit/nslevelindicator/1388839-maxvalue)Added [NSLevelIndicator.minValue](https://developer.apple.com/documentation/appkit/nslevelindicator/1388829-minvalue)Added [NSLevelIndicator.numberOfMajorTickMarks](https://developer.apple.com/documentation/appkit/nslevelindicator/1388819-numberofmajortickmarks)Added [NSLevelIndicator.numberOfTickMarks](https://developer.apple.com/documentation/appkit/nslevelindicator/1388827-numberoftickmarks)Added [NSLevelIndicator.tickMarkPosition](https://developer.apple.com/documentation/appkit/nslevelindicator/1388837-tickmarkposition)Added [NSLevelIndicator.warningValue](https://developer.apple.com/documentation/appkit/nslevelindicator/1388835-warningvalue)NSLevelIndicatorCell.hRemoved [-[NSLevelIndicatorCell criticalValue]](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1525337-criticalvalue)Removed [-[NSLevelIndicatorCell levelIndicatorStyle]](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1531954-levelindicatorstyle)Removed [-[NSLevelIndicatorCell maxValue]](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1528309-maxvalue)Removed [-[NSLevelIndicatorCell minValue]](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1534472-minvalue)Removed [-[NSLevelIndicatorCell numberOfMajorTickMarks]](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1528987-numberofmajortickmarks)Removed [-[NSLevelIndicatorCell numberOfTickMarks]](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1534680-numberoftickmarks)Removed [-[NSLevelIndicatorCell setCriticalValue:]](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1525337-criticalvalue)Removed [-[NSLevelIndicatorCell setLevelIndicatorStyle:]](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1531954-levelindicatorstyle)Removed [-[NSLevelIndicatorCell setMaxValue:]](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1528309-maxvalue)Removed [-[NSLevelIndicatorCell setMinValue:]](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1534472-minvalue)Removed [-[NSLevelIndicatorCell setNumberOfMajorTickMarks:]](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1528987-numberofmajortickmarks)Removed [-[NSLevelIndicatorCell setNumberOfTickMarks:]](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1534680-numberoftickmarks)Removed [-[NSLevelIndicatorCell setTickMarkPosition:]](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1532399-tickmarkposition)Removed [-[NSLevelIndicatorCell setWarningValue:]](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1528974-warningvalue)Removed [-[NSLevelIndicatorCell tickMarkPosition]](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1532399-tickmarkposition)Removed [-[NSLevelIndicatorCell warningValue]](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1528974-warningvalue)Added [NSLevelIndicatorCell.criticalValue](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1525337-criticalvalue)Added [NSLevelIndicatorCell.levelIndicatorStyle](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1531954-levelindicatorstyle)Added [NSLevelIndicatorCell.maxValue](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1528309-maxvalue)Added [NSLevelIndicatorCell.minValue](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1534472-minvalue)Added [NSLevelIndicatorCell.numberOfMajorTickMarks](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1528987-numberofmajortickmarks)Added [NSLevelIndicatorCell.numberOfTickMarks](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1534680-numberoftickmarks)Added [NSLevelIndicatorCell.tickMarkPosition](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1532399-tickmarkposition)Added [NSLevelIndicatorCell.warningValue](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1528974-warningvalue)Modified [-[NSLevelIndicatorCell initWithLevelIndicatorStyle:]](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/1527498-initwithlevelindicatorstyle)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithLevelIndicatorStyle:(NSLevelIndicatorStyle)levelIndicatorStyle ``` |
| To | ``` - (instancetype)initWithLevelIndicatorStyle:(NSLevelIndicatorStyle)levelIndicatorStyle ``` |

NSMagnificationGestureRecognizer.h (Added)Added [NSMagnificationGestureRecognizer](https://developer.apple.com/documentation/appkit/nsmagnificationgesturerecognizer)Added [NSMagnificationGestureRecognizer.magnification](https://developer.apple.com/documentation/appkit/nsmagnificationgesturerecognizer/1510428-magnification)NSMatrix.hRemoved [-[NSMatrix allowsEmptySelection]](https://developer.apple.com/documentation/appkit/nsmatrix/1436394-allowsemptyselection)Removed [-[NSMatrix autorecalculatesCellSize]](https://developer.apple.com/documentation/appkit/nsmatrix/1436501-autorecalculatescellsize)Removed [-[NSMatrix autosizesCells]](https://developer.apple.com/documentation/appkit/nsmatrix/1436375-autosizescells)Removed [-[NSMatrix backgroundColor]](https://developer.apple.com/documentation/appkit/nsmatrix/1436442-backgroundcolor)Removed [-[NSMatrix cellBackgroundColor]](https://developer.apple.com/documentation/appkit/nsmatrix/1436449-cellbackgroundcolor)Removed [-[NSMatrix cellClass]](https://developer.apple.com/documentation/appkit/nsmatrix/1436445-cellclass)Removed [-[NSMatrix cellSize]](https://developer.apple.com/documentation/appkit/nsmatrix/1436497-cellsize)Removed [-[NSMatrix cells]](https://developer.apple.com/documentation/appkit/nsmatrix/1436464-cells)Removed [-[NSMatrix delegate]](https://developer.apple.com/documentation/appkit/nsmatrix/1436404-delegate)Removed [-[NSMatrix doubleAction]](https://developer.apple.com/documentation/appkit/nsmatrix/1436469-doubleaction)Removed [-[NSMatrix drawsBackground]](https://developer.apple.com/documentation/appkit/nsmatrix/1436447-drawsbackground)Removed [-[NSMatrix drawsCellBackground]](https://developer.apple.com/documentation/appkit/nsmatrix/1436379-drawscellbackground)Removed [-[NSMatrix intercellSpacing]](https://developer.apple.com/documentation/appkit/nsmatrix/1436398-intercellspacing)Removed [-[NSMatrix isAutoscroll]](https://developer.apple.com/documentation/appkit/nsmatrix/1436410-autoscroll)Removed [-[NSMatrix isSelectionByRect]](https://developer.apple.com/documentation/appkit/nsmatrix/1436431-isselectionbyrect)Removed [-[NSMatrix keyCell]](https://developer.apple.com/documentation/appkit/nsmatrix/1436411-keycell)Removed [-[NSMatrix mode]](https://developer.apple.com/documentation/appkit/nsmatrix/1436390-mode)Removed [-[NSMatrix mouseDownFlags]](https://developer.apple.com/documentation/appkit/nsmatrix/1436487-mousedownflags)Removed [-[NSMatrix numberOfColumns]](https://developer.apple.com/documentation/appkit/nsmatrix/1436461-numberofcolumns)Removed [-[NSMatrix numberOfRows]](https://developer.apple.com/documentation/appkit/nsmatrix/1436507-numberofrows)Removed [-[NSMatrix prototype]](https://developer.apple.com/documentation/appkit/nsmatrix/1436406-prototype)Removed [-[NSMatrix selectedCell]](https://developer.apple.com/documentation/appkit/nsmatrix/1436472-selectedcell)Removed [-[NSMatrix selectedCells]](https://developer.apple.com/documentation/appkit/nsmatrix/1436434-selectedcells)Removed [-[NSMatrix selectedColumn]](https://developer.apple.com/documentation/appkit/nsmatrix/1436389-selectedcolumn)Removed [-[NSMatrix selectedRow]](https://developer.apple.com/documentation/appkit/nsmatrix/1436377-selectedrow)Removed [-[NSMatrix setAllowsEmptySelection:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436394-allowsemptyselection)Removed [-[NSMatrix setAutorecalculatesCellSize:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436501-autorecalculatescellsize)Removed [-[NSMatrix setAutoscroll:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436410-autoscroll)Removed [-[NSMatrix setAutosizesCells:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436375-autosizescells)Removed [-[NSMatrix setBackgroundColor:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436442-backgroundcolor)Removed [-[NSMatrix setCellBackgroundColor:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436449-cellbackgroundcolor)Removed [-[NSMatrix setCellClass:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436445-cellclass)Removed [-[NSMatrix setCellSize:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436497-cellsize)Removed [-[NSMatrix setDelegate:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436404-delegate)Removed [-[NSMatrix setDoubleAction:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436469-doubleaction)Removed [-[NSMatrix setDrawsBackground:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436447-drawsbackground)Removed [-[NSMatrix setDrawsCellBackground:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436379-drawscellbackground)Removed [-[NSMatrix setIntercellSpacing:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436398-intercellspacing)Removed [-[NSMatrix setKeyCell:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436411-keycell)Removed [-[NSMatrix setMode:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436390-mode)Removed [-[NSMatrix setPrototype:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436406-prototype)Removed [-[NSMatrix setSelectionByRect:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436431-selectionbyrect)Removed [-[NSMatrix setTabKeyTraversesCells:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436491-tabkeytraversescells)Removed [-[NSMatrix tabKeyTraversesCells]](https://developer.apple.com/documentation/appkit/nsmatrix/1436491-tabkeytraversescells)Added [NSMatrix.allowsEmptySelection](https://developer.apple.com/documentation/appkit/nsmatrix/1436394-allowsemptyselection)Added [NSMatrix.autorecalculatesCellSize](https://developer.apple.com/documentation/appkit/nsmatrix/1436501-autorecalculatescellsize)Added [NSMatrix.autoscroll](https://developer.apple.com/documentation/appkit/nsmatrix/1436410-autoscroll)Added [NSMatrix.autosizesCells](https://developer.apple.com/documentation/appkit/nsmatrix/1436375-autosizescells)Added [NSMatrix.backgroundColor](https://developer.apple.com/documentation/appkit/nsmatrix/1436442-backgroundcolor)Added [NSMatrix.cellBackgroundColor](https://developer.apple.com/documentation/appkit/nsmatrix/1436449-cellbackgroundcolor)Added [NSMatrix.cellClass](https://developer.apple.com/documentation/appkit/nsmatrix/1436445-cellclass)Added [NSMatrix.cellSize](https://developer.apple.com/documentation/appkit/nsmatrix/1436497-cellsize)Added [NSMatrix.cells](https://developer.apple.com/documentation/appkit/nsmatrix/1436464-cells)Added [NSMatrix.delegate](https://developer.apple.com/documentation/appkit/nsmatrix/1436404-delegate)Added [NSMatrix.doubleAction](https://developer.apple.com/documentation/appkit/nsmatrix/1436469-doubleaction)Added [NSMatrix.drawsBackground](https://developer.apple.com/documentation/appkit/nsmatrix/1436447-drawsbackground)Added [NSMatrix.drawsCellBackground](https://developer.apple.com/documentation/appkit/nsmatrix/1436379-drawscellbackground)Added [NSMatrix.intercellSpacing](https://developer.apple.com/documentation/appkit/nsmatrix/1436398-intercellspacing)Added [NSMatrix.keyCell](https://developer.apple.com/documentation/appkit/nsmatrix/1436411-keycell)Added [NSMatrix.mode](https://developer.apple.com/documentation/appkit/nsmatrix/1436390-mode)Added [NSMatrix.mouseDownFlags](https://developer.apple.com/documentation/appkit/nsmatrix/1436487-mousedownflags)Added [NSMatrix.numberOfColumns](https://developer.apple.com/documentation/appkit/nsmatrix/1436461-numberofcolumns)Added [NSMatrix.numberOfRows](https://developer.apple.com/documentation/appkit/nsmatrix/1436507-numberofrows)Added [NSMatrix.prototype](https://developer.apple.com/documentation/appkit/nsmatrix/1436406-prototype)Added [NSMatrix.selectedCell](https://developer.apple.com/documentation/appkit/nsmatrix/1436472-selectedcell)Added [NSMatrix.selectedCells](https://developer.apple.com/documentation/appkit/nsmatrix/1436434-selectedcells)Added [NSMatrix.selectedColumn](https://developer.apple.com/documentation/appkit/nsmatrix/1436389-selectedcolumn)Added [NSMatrix.selectedRow](https://developer.apple.com/documentation/appkit/nsmatrix/1436377-selectedrow)Added [NSMatrix.selectionByRect](https://developer.apple.com/documentation/appkit/nsmatrix/1436431-isselectionbyrect)Added [NSMatrix.tabKeyTraversesCells](https://developer.apple.com/documentation/appkit/nsmatrix/1436491-tabkeytraversescells)Modified [-[NSMatrix initWithFrame:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436428-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFrame:(NSRect)frameRect ``` |
| To | ``` - (instancetype)initWithFrame:(NSRect)frameRect ``` |

Modified [-[NSMatrix initWithFrame:mode:cellClass:numberOfRows:numberOfColumns:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436400-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFrame:(NSRect)frameRect mode:(NSMatrixMode)aMode cellClass:(Class)factoryId numberOfRows:(NSInteger)rowsHigh numberOfColumns:(NSInteger)colsWide ``` |
| To | ``` - (instancetype)initWithFrame:(NSRect)frameRect mode:(NSMatrixMode)aMode cellClass:(Class)factoryId numberOfRows:(NSInteger)rowsHigh numberOfColumns:(NSInteger)colsWide ``` |

Modified [-[NSMatrix initWithFrame:mode:prototype:numberOfRows:numberOfColumns:]](https://developer.apple.com/documentation/appkit/nsmatrix/1436386-initwithframe)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFrame:(NSRect)frameRect mode:(NSMatrixMode)aMode prototype:(NSCell *)aCell numberOfRows:(NSInteger)rowsHigh numberOfColumns:(NSInteger)colsWide ``` |
| To | ``` - (instancetype)initWithFrame:(NSRect)frameRect mode:(NSMatrixMode)aMode prototype:(NSCell *)aCell numberOfRows:(NSInteger)rowsHigh numberOfColumns:(NSInteger)colsWide ``` |

NSMediaLibraryBrowserController.hModified [-[NSMediaLibraryBrowserController togglePanel:]](https://developer.apple.com/documentation/appkit/nsmedialibrarybrowsercontroller/1423479-togglepanel)

|  | Declaration |
| --- | --- |
| From | ``` - (void)togglePanel:(id)sender ``` |
| To | ``` - (IBAction)togglePanel:(id)sender ``` |

NSMenu.hRemoved [-[NSMenu allowsContextMenuPlugIns]](https://developer.apple.com/documentation/appkit/nsmenu/1518220-allowscontextmenuplugins)Removed [-[NSMenu autoenablesItems]](https://developer.apple.com/documentation/appkit/nsmenu/1518227-autoenablesitems)Removed [-[NSMenu delegate]](https://developer.apple.com/documentation/appkit/nsmenu/1518169-delegate)Removed [-[NSMenu font]](https://developer.apple.com/documentation/appkit/nsmenu/1518230-font)Removed [-[NSMenu highlightedItem]](https://developer.apple.com/documentation/appkit/nsmenu/1518222-highlighteditem)Removed [-[NSMenu isTornOff]](https://developer.apple.com/documentation/appkit/nsmenu/1518190-istornoff)Removed [-[NSMenu itemArray]](https://developer.apple.com/documentation/appkit/nsmenu/1518186-itemarray)Removed [-[NSMenu menuBarHeight]](https://developer.apple.com/documentation/appkit/nsmenu/1518141-menubarheight)Removed [-[NSMenu menuChangedMessagesEnabled]](https://developer.apple.com/documentation/appkit/nsmenu/1518148-menuchangedmessagesenabled)Removed [-[NSMenu minimumWidth]](https://developer.apple.com/documentation/appkit/nsmenu/1518221-minimumwidth)Removed [-[NSMenu numberOfItems]](https://developer.apple.com/documentation/appkit/nsmenu/1518202-numberofitems)Removed [-[NSMenu propertiesToUpdate]](https://developer.apple.com/documentation/appkit/nsmenu/1518245-propertiestoupdate)Removed [-[NSMenu setAllowsContextMenuPlugIns:]](https://developer.apple.com/documentation/appkit/nsmenu/1518220-allowscontextmenuplugins)Removed [-[NSMenu setAutoenablesItems:]](https://developer.apple.com/documentation/appkit/nsmenu/1518227-autoenablesitems)Removed [-[NSMenu setDelegate:]](https://developer.apple.com/documentation/appkit/nsmenu/1518169-delegate)Removed [-[NSMenu setFont:]](https://developer.apple.com/documentation/appkit/nsmenu/1518230-font)Removed [-[NSMenu setMenuChangedMessagesEnabled:]](https://developer.apple.com/documentation/appkit/nsmenu/1518148-menuchangedmessagesenabled)Removed [-[NSMenu setMinimumWidth:]](https://developer.apple.com/documentation/appkit/nsmenu/1518221-minimumwidth)Removed [-[NSMenu setShowsStateColumn:]](https://developer.apple.com/documentation/appkit/nsmenu/1518253-showsstatecolumn)Removed [-[NSMenu setSupermenu:]](https://developer.apple.com/documentation/appkit/nsmenu/1518204-supermenu)Removed [-[NSMenu setTitle:]](https://developer.apple.com/documentation/appkit/nsmenu/1518192-title)Removed [-[NSMenu showsStateColumn]](https://developer.apple.com/documentation/appkit/nsmenu/1518253-showsstatecolumn)Removed [-[NSMenu size]](https://developer.apple.com/documentation/appkit/nsmenu/1518185-size)Removed [-[NSMenu supermenu]](https://developer.apple.com/documentation/appkit/nsmenu/1518204-supermenu)Removed [-[NSMenu title]](https://developer.apple.com/documentation/appkit/nsmenu/1518192-title)Added [NSMenu.allowsContextMenuPlugIns](https://developer.apple.com/documentation/appkit/nsmenu/1518220-allowscontextmenuplugins)Added [NSMenu.autoenablesItems](https://developer.apple.com/documentation/appkit/nsmenu/1518227-autoenablesitems)Added [NSMenu.delegate](https://developer.apple.com/documentation/appkit/nsmenu/1518169-delegate)Added [NSMenu.font](https://developer.apple.com/documentation/appkit/nsmenu/1518230-font)Added [NSMenu.highlightedItem](https://developer.apple.com/documentation/appkit/nsmenu/1518222-highlighteditem)Added [NSMenu.itemArray](https://developer.apple.com/documentation/appkit/nsmenu/1518186-itemarray)Added [NSMenu.menuBarHeight](https://developer.apple.com/documentation/appkit/nsmenu/1518141-menubarheight)Added [NSMenu.menuChangedMessagesEnabled](https://developer.apple.com/documentation/appkit/nsmenu/1518148-menuchangedmessagesenabled)Added [NSMenu.minimumWidth](https://developer.apple.com/documentation/appkit/nsmenu/1518221-minimumwidth)Added [NSMenu.numberOfItems](https://developer.apple.com/documentation/appkit/nsmenu/1518202-numberofitems)Added [NSMenu.propertiesToUpdate](https://developer.apple.com/documentation/appkit/nsmenu/1518245-propertiestoupdate)Added [NSMenu.showsStateColumn](https://developer.apple.com/documentation/appkit/nsmenu/1518253-showsstatecolumn)Added [NSMenu.size](https://developer.apple.com/documentation/appkit/nsmenu/1518185-size)Added [NSMenu.supermenu](https://developer.apple.com/documentation/appkit/nsmenu/1518204-supermenu)Added [NSMenu.title](https://developer.apple.com/documentation/appkit/nsmenu/1518192-title)Added [NSMenu.tornOff](https://developer.apple.com/documentation/appkit/nsmenu/1518190-tornoff)Modified [-[NSMenu initWithTitle:]](https://developer.apple.com/documentation/appkit/nsmenu/1518144-initwithtitle)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTitle:(NSString *)aTitle ``` |
| To | ``` - (instancetype)initWithTitle:(NSString *)aTitle ``` |

Modified [-[NSMenuDelegate confinementRectForMenu:onScreen:]](https://developer.apple.com/documentation/appkit/nsmenudelegate/1518247-confinementrect)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSMenuDelegate menu:updateItem:atIndex:shouldCancel:]](https://developer.apple.com/documentation/appkit/nsmenudelegate/1518256-menu)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSMenuDelegate menu:willHighlightItem:]](https://developer.apple.com/documentation/appkit/nsmenudelegate/1518260-menu)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSMenuDelegate menuDidClose:]](https://developer.apple.com/documentation/appkit/nsmenudelegate/1518167-menudidclose)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSMenuDelegate menuHasKeyEquivalent:forEvent:target:action:]](https://developer.apple.com/documentation/appkit/nsmenudelegate/1518211-menuhaskeyequivalent)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSMenuDelegate menuNeedsUpdate:]](https://developer.apple.com/documentation/appkit/nsmenudelegate/1518235-menuneedsupdate)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSMenuDelegate menuWillOpen:]](https://developer.apple.com/documentation/appkit/nsmenudelegate/1518156-menuwillopen)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSMenuDelegate numberOfItemsInMenu:]](https://developer.apple.com/documentation/appkit/nsmenudelegate/1518242-numberofitemsinmenu)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSMenuItem.hRemoved [-[NSMenuItem action]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514825-action)Removed [-[NSMenuItem attributedTitle]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514860-attributedtitle)Removed [-[NSMenuItem hasSubmenu]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514817-hassubmenu)Removed [-[NSMenuItem image]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514819-image)Removed [-[NSMenuItem indentationLevel]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514809-indentationlevel)Removed [-[NSMenuItem isAlternate]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514823-alternate)Removed [-[NSMenuItem isEnabled]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514863-enabled)Removed [-[NSMenuItem isHidden]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514846-ishidden)Removed [-[NSMenuItem isHiddenOrHasHiddenAncestor]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514832-hiddenorhashiddenancestor)Removed [-[NSMenuItem isHighlighted]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514856-ishighlighted)Removed [-[NSMenuItem isSeparatorItem]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514837-separatoritem)Removed [-[NSMenuItem keyEquivalent]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514842-keyequivalent)Removed [-[NSMenuItem keyEquivalentModifierMask]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514815-keyequivalentmodifiermask)Removed [-[NSMenuItem menu]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514830-menu)Removed [-[NSMenuItem mixedStateImage]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514827-mixedstateimage)Removed [-[NSMenuItem offStateImage]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514821-offstateimage)Removed [-[NSMenuItem onStateImage]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514861-onstateimage)Removed [-[NSMenuItem parentItem]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514813-parent)Removed [-[NSMenuItem representedObject]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514834-representedobject)Removed [-[NSMenuItem setAction:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514825-action)Removed [-[NSMenuItem setAlternate:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514823-alternate)Removed [-[NSMenuItem setAttributedTitle:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514860-attributedtitle)Removed [-[NSMenuItem setEnabled:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514863-enabled)Removed [-[NSMenuItem setHidden:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514846-ishidden)Removed [-[NSMenuItem setImage:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514819-image)Removed [-[NSMenuItem setIndentationLevel:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514809-indentationlevel)Removed [-[NSMenuItem setKeyEquivalent:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514842-keyequivalent)Removed [-[NSMenuItem setKeyEquivalentModifierMask:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514815-keyequivalentmodifiermask)Removed [-[NSMenuItem setMenu:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514830-menu)Removed [-[NSMenuItem setMixedStateImage:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514827-mixedstateimage)Removed [-[NSMenuItem setOffStateImage:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514821-offstateimage)Removed [-[NSMenuItem setOnStateImage:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514861-onstateimage)Removed [-[NSMenuItem setRepresentedObject:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514834-representedobject)Removed [-[NSMenuItem setState:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514804-state)Removed [-[NSMenuItem setSubmenu:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514845-submenu)Removed [-[NSMenuItem setTag:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514840-tag)Removed [-[NSMenuItem setTarget:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514843-target)Removed [-[NSMenuItem setTitle:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514805-title)Removed [-[NSMenuItem setToolTip:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514848-tooltip)Removed [-[NSMenuItem setView:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514835-view)Removed [-[NSMenuItem state]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514804-state)Removed [-[NSMenuItem submenu]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514845-submenu)Removed [-[NSMenuItem tag]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514840-tag)Removed [-[NSMenuItem target]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514843-target)Removed [-[NSMenuItem title]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514805-title)Removed [-[NSMenuItem toolTip]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514848-tooltip)Removed [-[NSMenuItem userKeyEquivalent]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514850-userkeyequivalent)Removed [-[NSMenuItem view]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514835-view)Removed [-[NSView enclosingMenuItem]](https://developer.apple.com/documentation/appkit/nsview/1514865-enclosingmenuitem)Added [NSMenuItem.action](https://developer.apple.com/documentation/appkit/nsmenuitem/1514825-action)Added [NSMenuItem.alternate](https://developer.apple.com/documentation/appkit/nsmenuitem/1514823-alternate)Added [NSMenuItem.attributedTitle](https://developer.apple.com/documentation/appkit/nsmenuitem/1514860-attributedtitle)Added [NSMenuItem.enabled](https://developer.apple.com/documentation/appkit/nsmenuitem/1514863-enabled)Added [NSMenuItem.hasSubmenu](https://developer.apple.com/documentation/appkit/nsmenuitem/1514817-hassubmenu)Added [NSMenuItem.hidden](https://developer.apple.com/documentation/appkit/nsmenuitem/1514846-hidden)Added [NSMenuItem.hiddenOrHasHiddenAncestor](https://developer.apple.com/documentation/appkit/nsmenuitem/1514832-ishiddenorhashiddenancestor)Added [NSMenuItem.highlighted](https://developer.apple.com/documentation/appkit/nsmenuitem/1514856-ishighlighted)Added [NSMenuItem.image](https://developer.apple.com/documentation/appkit/nsmenuitem/1514819-image)Added [NSMenuItem.indentationLevel](https://developer.apple.com/documentation/appkit/nsmenuitem/1514809-indentationlevel)Added [NSMenuItem.keyEquivalent](https://developer.apple.com/documentation/appkit/nsmenuitem/1514842-keyequivalent)Added [NSMenuItem.keyEquivalentModifierMask](https://developer.apple.com/documentation/appkit/nsmenuitem/1514815-keyequivalentmodifiermask)Added [NSMenuItem.menu](https://developer.apple.com/documentation/appkit/nsmenuitem/1514830-menu)Added [NSMenuItem.mixedStateImage](https://developer.apple.com/documentation/appkit/nsmenuitem/1514827-mixedstateimage)Added [NSMenuItem.offStateImage](https://developer.apple.com/documentation/appkit/nsmenuitem/1514821-offstateimage)Added [NSMenuItem.onStateImage](https://developer.apple.com/documentation/appkit/nsmenuitem/1514861-onstateimage)Added [NSMenuItem.parentItem](https://developer.apple.com/documentation/appkit/nsmenuitem/1514813-parent)Added [NSMenuItem.representedObject](https://developer.apple.com/documentation/appkit/nsmenuitem/1514834-representedobject)Added [NSMenuItem.separatorItem](https://developer.apple.com/documentation/appkit/nsmenuitem/1514837-separatoritem)Added [NSMenuItem.state](https://developer.apple.com/documentation/appkit/nsmenuitem/1514804-state)Added [NSMenuItem.submenu](https://developer.apple.com/documentation/appkit/nsmenuitem/1514845-submenu)Added [NSMenuItem.tag](https://developer.apple.com/documentation/appkit/nsmenuitem/1514840-tag)Added [NSMenuItem.target](https://developer.apple.com/documentation/appkit/nsmenuitem/1514843-target)Added [NSMenuItem.title](https://developer.apple.com/documentation/appkit/nsmenuitem/1514805-title)Added [NSMenuItem.toolTip](https://developer.apple.com/documentation/appkit/nsmenuitem/1514848-tooltip)Added [NSMenuItem.userKeyEquivalent](https://developer.apple.com/documentation/appkit/nsmenuitem/1514850-userkeyequivalent)Added [NSMenuItem.view](https://developer.apple.com/documentation/appkit/nsmenuitem/1514835-view)Added [NSView.enclosingMenuItem](https://developer.apple.com/documentation/appkit/nsview/1514865-enclosingmenuitem)Modified [-[NSMenuItem initWithTitle:action:keyEquivalent:]](https://developer.apple.com/documentation/appkit/nsmenuitem/1514858-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTitle:(NSString *)aString action:(SEL)aSelector keyEquivalent:(NSString *)charCode ``` |
| To | ``` - (instancetype)initWithTitle:(NSString *)aString action:(SEL)aSelector keyEquivalent:(NSString *)charCode ``` |

NSMenuItemCell.hRemoved [-[NSMenuItemCell imageWidth]](https://developer.apple.com/documentation/appkit/nsmenuitemcell/1498877-imagewidth)Removed [-[NSMenuItemCell keyEquivalentWidth]](https://developer.apple.com/documentation/appkit/nsmenuitemcell/1498874-keyequivalentwidth)Removed [-[NSMenuItemCell menuItem]](https://developer.apple.com/documentation/appkit/nsmenuitemcell/1498871-menuitem)Removed [-[NSMenuItemCell needsDisplay]](https://developer.apple.com/documentation/appkit/nsmenuitemcell/1498861-needsdisplay)Removed [-[NSMenuItemCell needsSizing]](https://developer.apple.com/documentation/appkit/nsmenuitemcell/1498869-needssizing)Removed [-[NSMenuItemCell setMenuItem:]](https://developer.apple.com/documentation/appkit/nsmenuitemcell/1498871-menuitem)Removed [-[NSMenuItemCell setNeedsDisplay:]](https://developer.apple.com/documentation/appkit/nsmenuitemcell/1498861-needsdisplay)Removed [-[NSMenuItemCell setNeedsSizing:]](https://developer.apple.com/documentation/appkit/nsmenuitemcell/1498869-needssizing)Removed [-[NSMenuItemCell stateImageWidth]](https://developer.apple.com/documentation/appkit/nsmenuitemcell/1498879-stateimagewidth)Removed [-[NSMenuItemCell tag]](https://developer.apple.com/documentation/appkit/nsmenuitemcell/1498882-tag)Removed [-[NSMenuItemCell titleWidth]](https://developer.apple.com/documentation/appkit/nsmenuitemcell/1498865-titlewidth)Added [NSMenuItemCell.imageWidth](https://developer.apple.com/documentation/appkit/nsmenuitemcell/1498877-imagewidth)Added [NSMenuItemCell.keyEquivalentWidth](https://developer.apple.com/documentation/appkit/nsmenuitemcell/1498874-keyequivalentwidth)Added [NSMenuItemCell.menuItem](https://developer.apple.com/documentation/appkit/nsmenuitemcell/1498871-menuitem)Added [NSMenuItemCell.needsDisplay](https://developer.apple.com/documentation/appkit/nsmenuitemcell/1498861-needsdisplay)Added [NSMenuItemCell.needsSizing](https://developer.apple.com/documentation/appkit/nsmenuitemcell/1498869-needssizing)Added [NSMenuItemCell.stateImageWidth](https://developer.apple.com/documentation/appkit/nsmenuitemcell/1498879-stateimagewidth)Added [NSMenuItemCell.tag](https://developer.apple.com/documentation/appkit/nsmenuitemcell/1498882-tag)Added [NSMenuItemCell.titleWidth](https://developer.apple.com/documentation/appkit/nsmenuitemcell/1498865-titlewidth)NSMovie.hModified NSMovie

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.5 |

NSMovieView.hModified NSMovieView

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.5 |

NSNib.hModified [-[NSNib initWithNibData:bundle:]](https://developer.apple.com/documentation/appkit/nsnib/1535865-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithNibData:(NSData *)nibData bundle:(NSBundle *)bundle ``` |
| To | ``` - (instancetype)initWithNibData:(NSData *)nibData bundle:(NSBundle *)bundle ``` |

Modified [-[NSNib initWithNibNamed:bundle:]](https://developer.apple.com/documentation/appkit/nsnib/1533932-initwithnibnamed)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithNibNamed:(NSString *)nibName bundle:(NSBundle *)bundle ``` |
| To | ``` - (instancetype)initWithNibNamed:(NSString *)nibName bundle:(NSBundle *)bundle ``` |

NSNibConnector.hRemoved -[NSNibConnector destination]Removed -[NSNibConnector label]Removed -[NSNibConnector setDestination:]Removed -[NSNibConnector setLabel:]Removed -[NSNibConnector setSource:]Removed -[NSNibConnector source]Added [NSNibConnector.destination](https://developer.apple.com/documentation/appkit/nsnibconnector/1387482-destination)Added [NSNibConnector.label](https://developer.apple.com/documentation/appkit/nsnibconnector/1387493-label)Added [NSNibConnector.source](https://developer.apple.com/documentation/appkit/nsnibconnector/1387484-source)NSNibLoading.hAdded [-[NSObject prepareForInterfaceBuilder]](https://developer.apple.com/documentation/objectivec/nsobject/1402908-prepareforinterfacebuilder)NSObjectController.hRemoved [-[NSObjectController automaticallyPreparesContent]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1534767-automaticallypreparescontent)Removed [-[NSObjectController canAdd]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1528497-canadd)Removed [-[NSObjectController canRemove]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1532378-canremove)Removed [-[NSObjectController content]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1530826-content)Removed [-[NSObjectController entityName]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1535467-entityname)Removed [-[NSObjectController fetchPredicate]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1533545-fetchpredicate)Removed [-[NSObjectController isEditable]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1534699-editable)Removed [-[NSObjectController managedObjectContext]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1530382-managedobjectcontext)Removed [-[NSObjectController objectClass]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1535459-objectclass)Removed [-[NSObjectController selectedObjects]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1535397-selectedobjects)Removed [-[NSObjectController selection]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1527403-selection)Removed [-[NSObjectController setAutomaticallyPreparesContent:]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1534767-automaticallypreparescontent)Removed [-[NSObjectController setContent:]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1530826-content)Removed [-[NSObjectController setEditable:]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1534699-editable)Removed [-[NSObjectController setEntityName:]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1535467-entityname)Removed [-[NSObjectController setFetchPredicate:]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1533545-fetchpredicate)Removed [-[NSObjectController setManagedObjectContext:]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1530382-managedobjectcontext)Removed [-[NSObjectController setObjectClass:]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1535459-objectclass)Removed [-[NSObjectController setUsesLazyFetching:]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1531411-useslazyfetching)Removed [-[NSObjectController usesLazyFetching]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1531411-useslazyfetching)Added [NSObjectController.automaticallyPreparesContent](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1534767-automaticallypreparescontent)Added [NSObjectController.canAdd](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1528497-canadd)Added [NSObjectController.canRemove](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1532378-canremove)Added [NSObjectController.content](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1530826-content)Added [NSObjectController.editable](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1534699-editable)Added [NSObjectController.entityName](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1535467-entityname)Added [NSObjectController.fetchPredicate](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1533545-fetchpredicate)Added [-[NSObjectController initWithCoder:]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1532995-initwithcoder)Added [NSObjectController.managedObjectContext](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1530382-managedobjectcontext)Added [NSObjectController.objectClass](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1535459-objectclass)Added [NSObjectController.selectedObjects](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1535397-selectedobjects)Added [NSObjectController.selection](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1527403-selection)Added [NSObjectController.usesLazyFetching](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1531411-useslazyfetching)Modified [-[NSObjectController initWithContent:]](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1529422-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithContent:(id)content ``` | -- |
| To | ``` - (instancetype)initWithContent:(id)content ``` | yes |

NSOpenGL.hRemoved [-[NSOpenGLContext CGLContextObj]](https://developer.apple.com/documentation/appkit/nsopenglcontext/1436158-cglcontextobj)Removed [-[NSOpenGLContext currentVirtualScreen]](https://developer.apple.com/documentation/appkit/nsopenglcontext/1436216-currentvirtualscreen)Removed [-[NSOpenGLContext setCurrentVirtualScreen:]](https://developer.apple.com/documentation/appkit/nsopenglcontext/1436216-currentvirtualscreen)Removed [-[NSOpenGLContext setView:]](https://developer.apple.com/documentation/appkit/nsopenglcontext/1436204-view)Removed [-[NSOpenGLContext view]](https://developer.apple.com/documentation/appkit/nsopenglcontext/1436204-view)Removed [-[NSOpenGLPixelFormat CGLPixelFormatObj]](https://developer.apple.com/documentation/appkit/nsopenglpixelformat/1436148-cglpixelformatobj)Removed [-[NSOpenGLPixelFormat numberOfVirtualScreens]](https://developer.apple.com/documentation/appkit/nsopenglpixelformat/1436144-numberofvirtualscreens)Removed [NSOpenGLPixelFormatAuxiliary](https://developer.apple.com/documentation/appkit/data_types/nsopenglpixelformatauxiliary)Added [NSOpenGLContext.CGLContextObj](https://developer.apple.com/documentation/appkit/nsopenglcontext/1436158-cglcontextobj)Added [NSOpenGLContext.currentVirtualScreen](https://developer.apple.com/documentation/appkit/nsopenglcontext/1436216-currentvirtualscreen)Added [NSOpenGLContext.pixelFormat](https://developer.apple.com/documentation/appkit/nsopenglcontext/1436140-pixelformat)Added [NSOpenGLContext.view](https://developer.apple.com/documentation/appkit/nsopenglcontext/1436204-view)Added [NSOpenGLPixelFormat.CGLPixelFormatObj](https://developer.apple.com/documentation/appkit/nsopenglpixelformat/1436148-cglpixelformatobj)Added [NSOpenGLPixelFormat.numberOfVirtualScreens](https://developer.apple.com/documentation/appkit/nsopenglpixelformat/1436144-numberofvirtualscreens)Added NSOpenGLContext(NSOpenGLPixelBufer)Added [NSOpenGLProfileVersion4_1Core](https://developer.apple.com/documentation/appkit/1436146-opengl_profiles/nsopenglprofileversion4_1core)Modified [NSOpenGLContext](https://developer.apple.com/documentation/appkit/nsopenglcontext)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSLocking |

Modified [-[NSOpenGLContext copyAttributesFromContext:withMask:]](https://developer.apple.com/documentation/appkit/nsopenglcontext/1436166-copyattributesfromcontext)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.8 |

Modified [-[NSOpenGLContext createTexture:fromView:internalFormat:]](https://developer.apple.com/documentation/appkit/nsopenglcontext/1436141-createtexture)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.8 |

Modified [-[NSOpenGLContext initWithCGLContextObj:]](https://developer.apple.com/documentation/appkit/nsopenglcontext/1436180-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCGLContextObj:(void *)context ``` |
| To | ``` - (NSOpenGLContext *)initWithCGLContextObj:(struct _CGLContextObject *)context ``` |

Modified [-[NSOpenGLContext initWithFormat:shareContext:]](https://developer.apple.com/documentation/appkit/nsopenglcontext/1436178-initwithformat)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFormat:(NSOpenGLPixelFormat *)format shareContext:(NSOpenGLContext *)share ``` |
| To | ``` - (instancetype)initWithFormat:(NSOpenGLPixelFormat *)format shareContext:(NSOpenGLContext *)share ``` |

Modified [-[NSOpenGLContext pixelBuffer]](https://developer.apple.com/documentation/appkit/nsopenglcontext/1436218-pixelbuffer)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified [-[NSOpenGLContext pixelBufferCubeMapFace]](https://developer.apple.com/documentation/appkit/nsopenglcontext/1436122-pixelbuffercubemapface)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified [-[NSOpenGLContext pixelBufferMipMapLevel]](https://developer.apple.com/documentation/appkit/nsopenglcontext/1436173-pixelbuffermipmaplevel)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified [-[NSOpenGLContext setFullScreen]](https://developer.apple.com/documentation/appkit/nsopenglcontext/1436221-setfullscreen)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified [-[NSOpenGLContext setOffScreen:width:height:rowbytes:]](https://developer.apple.com/documentation/appkit/nsopenglcontext/1436113-setoffscreen)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified [-[NSOpenGLContext setPixelBuffer:cubeMapFace:mipMapLevel:currentVirtualScreen:]](https://developer.apple.com/documentation/appkit/nsopenglcontext/1436105-setpixelbuffer)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified [-[NSOpenGLContext setTextureImageToPixelBuffer:colorBuffer:]](https://developer.apple.com/documentation/appkit/nsopenglcontext/1436164-settextureimagetopixelbuffer)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified [NSOpenGLPixelBuffer](https://developer.apple.com/documentation/appkit/nsopenglpixelbuffer)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.2 | OS X 10.7 |

Modified [-[NSOpenGLPixelBuffer CGLPBufferObj]](https://developer.apple.com/documentation/appkit/nsopenglpixelbuffer/1436155-cglpbufferobj)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (void *)CGLPBufferObj ``` | -- |
| To | ``` - (struct _CGLPBufferObject *)CGLPBufferObj ``` | OS X 10.7 |

Modified [-[NSOpenGLPixelBuffer initWithCGLPBufferObj:]](https://developer.apple.com/documentation/appkit/nsopenglpixelbuffer/1436176-initwithcglpbufferobj)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (id)initWithCGLPBufferObj:(void *)pbuffer ``` | -- |
| To | ``` - (NSOpenGLPixelBuffer *)initWithCGLPBufferObj:(struct _CGLPBufferObject *)pbuffer ``` | OS X 10.7 |

Modified [-[NSOpenGLPixelBuffer initWithTextureTarget:textureInternalFormat:textureMaxMipMapLevel:pixelsWide:pixelsHigh:]](https://developer.apple.com/documentation/appkit/nsopenglpixelbuffer/1436115-initwithtexturetarget)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` - (id)initWithTextureTarget:(GLenum)target textureInternalFormat:(GLenum)format textureMaxMipMapLevel:(GLint)maxLevel pixelsWide:(GLsizei)pixelsWide pixelsHigh:(GLsizei)pixelsHigh ``` | OS X 10.3 | -- |
| To | ``` - (instancetype)initWithTextureTarget:(GLenum)target textureInternalFormat:(GLenum)format textureMaxMipMapLevel:(GLint)maxLevel pixelsWide:(GLsizei)pixelsWide pixelsHigh:(GLsizei)pixelsHigh ``` | OS X 10.2 | OS X 10.7 |

Modified [-[NSOpenGLPixelBuffer pixelsHigh]](https://developer.apple.com/documentation/appkit/nsopenglpixelbuffer/1436220-pixelshigh)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.2 | OS X 10.7 |

Modified [-[NSOpenGLPixelBuffer pixelsWide]](https://developer.apple.com/documentation/appkit/nsopenglpixelbuffer/1436217-pixelswide)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.2 | OS X 10.7 |

Modified [-[NSOpenGLPixelBuffer textureInternalFormat]](https://developer.apple.com/documentation/appkit/nsopenglpixelbuffer/1436215-textureinternalformat)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.2 | OS X 10.7 |

Modified [-[NSOpenGLPixelBuffer textureMaxMipMapLevel]](https://developer.apple.com/documentation/appkit/nsopenglpixelbuffer/1436120-texturemaxmipmaplevel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.2 | OS X 10.7 |

Modified [-[NSOpenGLPixelBuffer textureTarget]](https://developer.apple.com/documentation/appkit/nsopenglpixelbuffer/1436187-texturetarget)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.2 | OS X 10.7 |

Modified [-[NSOpenGLPixelFormat attributes]](https://developer.apple.com/documentation/appkit/nsopenglpixelformat/1436127-attributes)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [-[NSOpenGLPixelFormat initWithAttributes:]](https://developer.apple.com/documentation/appkit/nsopenglpixelformat/1436219-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithAttributes:(const NSOpenGLPixelFormatAttribute *)attribs ``` |
| To | ``` - (instancetype)initWithAttributes:(const NSOpenGLPixelFormatAttribute *)attribs ``` |

Modified [-[NSOpenGLPixelFormat initWithCGLPixelFormatObj:]](https://developer.apple.com/documentation/appkit/nsopenglpixelformat/1436129-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCGLPixelFormatObj:(void *)format ``` |
| To | ``` - (NSOpenGLPixelFormat *)initWithCGLPixelFormatObj:(struct _CGLPixelFormatObject *)format ``` |

Modified [-[NSOpenGLPixelFormat initWithData:]](https://developer.apple.com/documentation/appkit/nsopenglpixelformat/1436207-initwithdata)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [-[NSOpenGLPixelFormat setAttributes:]](https://developer.apple.com/documentation/appkit/nsopenglpixelformat/1436128-setattributes)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [NSOpenGLGOResetLibrary](https://developer.apple.com/documentation/appkit/nsopenglglobaloption/nsopenglgoresetlibrary)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.4 |

Modified [NSOpenGLPFACompliant](https://developer.apple.com/documentation/appkit/1436213-opengl_pixel_format_attributes/nsopenglpfacompliant)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.9 |

Modified [NSOpenGLPFAFullScreen](https://developer.apple.com/documentation/appkit/1436213-opengl_pixel_format_attributes/nsopenglpfafullscreen)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [NSOpenGLPFAMPSafe](https://developer.apple.com/documentation/appkit/1436213-opengl_pixel_format_attributes/nsopenglpfampsafe)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.5 |

Modified [NSOpenGLPFAMultiScreen](https://developer.apple.com/documentation/appkit/1436213-opengl_pixel_format_attributes/nsopenglpfamultiscreen)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.5 |

Modified [NSOpenGLPFAOffScreen](https://developer.apple.com/documentation/appkit/1436213-opengl_pixel_format_attributes/nsopenglpfaoffscreen)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified [NSOpenGLPFAPixelBuffer](https://developer.apple.com/documentation/appkit/1436213-opengl_pixel_format_attributes/nsopenglpfapixelbuffer)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified [NSOpenGLPFARemotePixelBuffer](https://developer.apple.com/documentation/appkit/1436213-opengl_pixel_format_attributes/nsopenglpfaremotepixelbuffer)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.3 | OS X 10.7 |

Modified [NSOpenGLPFARobust](https://developer.apple.com/documentation/appkit/1436213-opengl_pixel_format_attributes/nsopenglpfarobust)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.5 |

Modified [NSOpenGLPFASingleRenderer](https://developer.apple.com/documentation/appkit/1436213-opengl_pixel_format_attributes/nsopenglpfasinglerenderer)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.9 |

Modified [NSOpenGLPFAWindow](https://developer.apple.com/documentation/appkit/1436213-opengl_pixel_format_attributes/nsopenglpfawindow)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.9 |

NSOpenGLLayer.hModified [NSOpenGLLayer.openGLContext](https://developer.apple.com/documentation/appkit/nsopengllayer/1522570-openglcontext)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) NSOpenGLContext *openGLContext ``` |
| To | ``` @property(strong) NSOpenGLContext *openGLContext ``` |

Modified [NSOpenGLLayer.openGLPixelFormat](https://developer.apple.com/documentation/appkit/nsopengllayer/1522568-openglpixelformat)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) NSOpenGLPixelFormat *openGLPixelFormat ``` |
| To | ``` @property(strong) NSOpenGLPixelFormat *openGLPixelFormat ``` |

NSOpenGLView.hRemoved [-[NSOpenGLView openGLContext]](https://developer.apple.com/documentation/appkit/nsopenglview/1414942-openglcontext)Removed [-[NSOpenGLView pixelFormat]](https://developer.apple.com/documentation/appkit/nsopenglview/1414946-pixelformat)Removed [-[NSOpenGLView setOpenGLContext:]](https://developer.apple.com/documentation/appkit/nsopenglview/1414942-openglcontext)Removed [-[NSOpenGLView setPixelFormat:]](https://developer.apple.com/documentation/appkit/nsopenglview/1414946-pixelformat)Removed [-[NSView setWantsBestResolutionOpenGLSurface:]](https://developer.apple.com/documentation/appkit/nsview/1414938-wantsbestresolutionopenglsurface)Removed [-[NSView wantsBestResolutionOpenGLSurface]](https://developer.apple.com/documentation/appkit/nsview/1414938-wantsbestresolutionopenglsurface)Added [NSOpenGLView.openGLContext](https://developer.apple.com/documentation/appkit/nsopenglview/1414942-openglcontext)Added [NSOpenGLView.pixelFormat](https://developer.apple.com/documentation/appkit/nsopenglview/1414946-pixelformat)Added [NSView.wantsBestResolutionOpenGLSurface](https://developer.apple.com/documentation/appkit/nsview/1414938-wantsbestresolutionopenglsurface)Modified [-[NSOpenGLView initWithFrame:pixelFormat:]](https://developer.apple.com/documentation/appkit/nsopenglview/1414931-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFrame:(NSRect)frameRect pixelFormat:(NSOpenGLPixelFormat *)format ``` |
| To | ``` - (instancetype)initWithFrame:(NSRect)frameRect pixelFormat:(NSOpenGLPixelFormat *)format ``` |

NSOpenPanel.hRemoved [-[NSOpenPanel URLs]](https://developer.apple.com/documentation/appkit/nsopenpanel/1529845-urls)Removed [-[NSOpenPanel allowsMultipleSelection]](https://developer.apple.com/documentation/appkit/nsopenpanel/1530786-allowsmultipleselection)Removed [-[NSOpenPanel canChooseDirectories]](https://developer.apple.com/documentation/appkit/nsopenpanel/1532668-canchoosedirectories)Removed [-[NSOpenPanel canChooseFiles]](https://developer.apple.com/documentation/appkit/nsopenpanel/1527060-canchoosefiles)Removed [-[NSOpenPanel resolvesAliases]](https://developer.apple.com/documentation/appkit/nsopenpanel/1533625-resolvesaliases)Removed [-[NSOpenPanel setAllowsMultipleSelection:]](https://developer.apple.com/documentation/appkit/nsopenpanel/1530786-allowsmultipleselection)Removed [-[NSOpenPanel setCanChooseDirectories:]](https://developer.apple.com/documentation/appkit/nsopenpanel/1532668-canchoosedirectories)Removed [-[NSOpenPanel setCanChooseFiles:]](https://developer.apple.com/documentation/appkit/nsopenpanel/1527060-canchoosefiles)Removed [-[NSOpenPanel setResolvesAliases:]](https://developer.apple.com/documentation/appkit/nsopenpanel/1533625-resolvesaliases)Added [NSOpenPanel.URLs](https://developer.apple.com/documentation/appkit/nsopenpanel/1529845-urls)Added [NSOpenPanel.allowsMultipleSelection](https://developer.apple.com/documentation/appkit/nsopenpanel/1530786-allowsmultipleselection)Added [NSOpenPanel.canChooseDirectories](https://developer.apple.com/documentation/appkit/nsopenpanel/1532668-canchoosedirectories)Added [NSOpenPanel.canChooseFiles](https://developer.apple.com/documentation/appkit/nsopenpanel/1527060-canchoosefiles)Added [NSOpenPanel.canDownloadUbiquitousContents](https://developer.apple.com/documentation/appkit/nsopenpanel/1533418-candownloadubiquitouscontents)Added [NSOpenPanel.canResolveUbiquitousConflicts](https://developer.apple.com/documentation/appkit/nsopenpanel/1533261-canresolveubiquitousconflicts)Added [NSOpenPanel.resolvesAliases](https://developer.apple.com/documentation/appkit/nsopenpanel/1533625-resolvesaliases)NSOutlineView.hRemoved [-[NSOutlineView autoresizesOutlineColumn]](https://developer.apple.com/documentation/appkit/nsoutlineview/1532304-autoresizesoutlinecolumn)Removed [-[NSOutlineView autosaveExpandedItems]](https://developer.apple.com/documentation/appkit/nsoutlineview/1530638-autosaveexpandeditems)Removed [-[NSOutlineView indentationMarkerFollowsCell]](https://developer.apple.com/documentation/appkit/nsoutlineview/1531707-indentationmarkerfollowscell)Removed [-[NSOutlineView indentationPerLevel]](https://developer.apple.com/documentation/appkit/nsoutlineview/1535181-indentationperlevel)Removed [-[NSOutlineView outlineTableColumn]](https://developer.apple.com/documentation/appkit/nsoutlineview/1533581-outlinetablecolumn)Removed [-[NSOutlineView setAutoresizesOutlineColumn:]](https://developer.apple.com/documentation/appkit/nsoutlineview/1532304-autoresizesoutlinecolumn)Removed [-[NSOutlineView setAutosaveExpandedItems:]](https://developer.apple.com/documentation/appkit/nsoutlineview/1530638-autosaveexpandeditems)Removed [-[NSOutlineView setIndentationMarkerFollowsCell:]](https://developer.apple.com/documentation/appkit/nsoutlineview/1531707-indentationmarkerfollowscell)Removed [-[NSOutlineView setIndentationPerLevel:]](https://developer.apple.com/documentation/appkit/nsoutlineview/1535181-indentationperlevel)Removed [-[NSOutlineView setOutlineTableColumn:]](https://developer.apple.com/documentation/appkit/nsoutlineview/1533581-outlinetablecolumn)Removed [-[NSOutlineView setUserInterfaceLayoutDirection:]](https://developer.apple.com/documentation/appkit/nsoutlineview/1524564-userinterfacelayoutdirection)Removed [-[NSOutlineView userInterfaceLayoutDirection]](https://developer.apple.com/documentation/appkit/nsoutlineview/1524564-userinterfacelayoutdirection)Added [NSOutlineView.autoresizesOutlineColumn](https://developer.apple.com/documentation/appkit/nsoutlineview/1532304-autoresizesoutlinecolumn)Added [NSOutlineView.autosaveExpandedItems](https://developer.apple.com/documentation/appkit/nsoutlineview/1530638-autosaveexpandeditems)Added [-[NSOutlineView child:ofItem:]](https://developer.apple.com/documentation/appkit/nsoutlineview/1527501-child)Added [NSOutlineView.indentationMarkerFollowsCell](https://developer.apple.com/documentation/appkit/nsoutlineview/1531707-indentationmarkerfollowscell)Added [NSOutlineView.indentationPerLevel](https://developer.apple.com/documentation/appkit/nsoutlineview/1535181-indentationperlevel)Added [-[NSOutlineView numberOfChildrenOfItem:]](https://developer.apple.com/documentation/appkit/nsoutlineview/1534304-numberofchildren)Added [NSOutlineView.outlineTableColumn](https://developer.apple.com/documentation/appkit/nsoutlineview/1533581-outlinetablecolumn)Added [NSOutlineView.userInterfaceLayoutDirection](https://developer.apple.com/documentation/appkit/nsoutlineview/1524564-userinterfacelayoutdirection)Modified [NSOutlineView](https://developer.apple.com/documentation/appkit/nsoutlineview)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSAccessibilityOutline |

Modified [-[NSOutlineViewDataSource outlineView:acceptDrop:item:childIndex:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1529572-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDataSource outlineView:child:ofItem:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1528977-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDataSource outlineView:draggingSession:endedAtPoint:operation:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1532073-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDataSource outlineView:draggingSession:willBeginAtPoint:forItems:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1535142-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDataSource outlineView:isItemExpandable:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1535198-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDataSource outlineView:itemForPersistentObject:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1533602-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDataSource outlineView:namesOfPromisedFilesDroppedAtDestination:forDraggedItems:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1533948-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDataSource outlineView:numberOfChildrenOfItem:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1535549-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDataSource outlineView:objectValueForTableColumn:byItem:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1531606-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDataSource outlineView:pasteboardWriterForItem:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1525837-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDataSource outlineView:persistentObjectForItem:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1532545-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDataSource outlineView:setObjectValue:forTableColumn:byItem:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1534817-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDataSource outlineView:sortDescriptorsDidChange:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1535892-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDataSource outlineView:updateDraggingItemsForDrag:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1534424-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDataSource outlineView:validateDrop:proposedItem:proposedChildIndex:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1533597-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDataSource outlineView:writeItems:toPasteboard:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/1532910-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:dataCellForTableColumn:item:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1525161-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:didAddRowView:forRow:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1528320-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:didClickTableColumn:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1534040-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:didDragTableColumn:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1526632-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:didRemoveRowView:forRow:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1530612-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:heightOfRowByItem:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1531870-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:isGroupItem:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1528482-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:mouseDownInHeaderOfTableColumn:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1531835-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:nextTypeSelectMatchFromItem:toItem:forString:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1533321-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:rowViewForItem:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1532140-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:selectionIndexesForProposedSelection:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1527575-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:shouldCollapseItem:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1529825-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:shouldEditTableColumn:item:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1535450-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:shouldExpandItem:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1531199-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:shouldReorderColumn:toColumn:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1530792-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:shouldSelectItem:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1531075-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:shouldSelectTableColumn:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1535118-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:shouldShowCellExpansionForTableColumn:item:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1534411-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:shouldShowOutlineCellForItem:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1534006-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:shouldTrackCell:forTableColumn:item:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1534295-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:shouldTypeSelectForEvent:withCurrentSearchString:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1532941-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:sizeToFitWidthOfColumn:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1530479-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:toolTipForCell:rect:tableColumn:item:mouseLocation:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1527695-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:typeSelectStringForTableColumn:item:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1526847-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:viewForTableColumn:item:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1535566-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:willDisplayCell:forTableColumn:item:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1529359-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineView:willDisplayOutlineCell:forTableColumn:item:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1535808-outlineview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineViewColumnDidMove:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1525297-outlineviewcolumndidmove)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineViewColumnDidResize:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1533372-outlineviewcolumndidresize)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineViewItemDidCollapse:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1535557-outlineviewitemdidcollapse)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineViewItemDidExpand:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1530869-outlineviewitemdidexpand)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineViewItemWillCollapse:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1526896-outlineviewitemwillcollapse)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineViewItemWillExpand:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1535847-outlineviewitemwillexpand)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineViewSelectionDidChange:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1526913-outlineviewselectiondidchange)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate outlineViewSelectionIsChanging:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1532481-outlineviewselectionischanging)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutlineViewDelegate selectionShouldChangeInOutlineView:]](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/1530734-selectionshouldchangeinoutlinevi)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSPDFImageRep.hRemoved [-[NSPDFImageRep PDFRepresentation]](https://developer.apple.com/documentation/appkit/nspdfimagerep/1530162-pdfrepresentation)Removed [-[NSPDFImageRep bounds]](https://developer.apple.com/documentation/appkit/nspdfimagerep/1533966-bounds)Removed [-[NSPDFImageRep currentPage]](https://developer.apple.com/documentation/appkit/nspdfimagerep/1528846-currentpage)Removed [-[NSPDFImageRep pageCount]](https://developer.apple.com/documentation/appkit/nspdfimagerep/1533063-pagecount)Removed [-[NSPDFImageRep setCurrentPage:]](https://developer.apple.com/documentation/appkit/nspdfimagerep/1528846-currentpage)Added [NSPDFImageRep.PDFRepresentation](https://developer.apple.com/documentation/appkit/nspdfimagerep/1530162-pdfrepresentation)Added [NSPDFImageRep.bounds](https://developer.apple.com/documentation/appkit/nspdfimagerep/1533966-bounds)Added [NSPDFImageRep.currentPage](https://developer.apple.com/documentation/appkit/nspdfimagerep/1528846-currentpage)Added [NSPDFImageRep.pageCount](https://developer.apple.com/documentation/appkit/nspdfimagerep/1533063-pagecount)Modified [+[NSPDFImageRep imageRepWithData:]](https://developer.apple.com/documentation/appkit/nspdfimagerep/1586713-imagerepwithdata)

|  | Declaration |
| --- | --- |
| From | ``` + (id)imageRepWithData:(NSData *)pdfData ``` |
| To | ``` + (instancetype)imageRepWithData:(NSData *)pdfData ``` |

Modified [-[NSPDFImageRep initWithData:]](https://developer.apple.com/documentation/appkit/nspdfimagerep/1535547-initwithdata)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(NSData *)pdfData ``` |
| To | ``` - (instancetype)initWithData:(NSData *)pdfData ``` |

NSPDFPanel.hModified [NSPDFPanel.accessoryController](https://developer.apple.com/documentation/appkit/nspdfpanel/1524637-accessorycontroller)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) NSViewController *accessoryController ``` |
| To | ``` @property(strong) NSViewController *accessoryController ``` |

NSPICTImageRep.hRemoved [-[NSPICTImageRep PICTRepresentation]](https://developer.apple.com/documentation/appkit/nspictimagerep/1524591-pictrepresentation)Removed [-[NSPICTImageRep boundingBox]](https://developer.apple.com/documentation/appkit/nspictimagerep/1524978-boundingbox)Added [NSPICTImageRep.PICTRepresentation](https://developer.apple.com/documentation/appkit/nspictimagerep/1524591-pictrepresentation)Added [NSPICTImageRep.boundingBox](https://developer.apple.com/documentation/appkit/nspictimagerep/1524978-boundingbox)Modified [+[NSPICTImageRep imageRepWithData:]](https://developer.apple.com/documentation/appkit/nspictimagerep/1588725-imagerepwithdata)

|  | Declaration |
| --- | --- |
| From | ``` + (id)imageRepWithData:(NSData *)pictData ``` |
| To | ``` + (instancetype)imageRepWithData:(NSData *)pictData ``` |

Modified [-[NSPICTImageRep initWithData:]](https://developer.apple.com/documentation/appkit/nspictimagerep/1533954-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(NSData *)pictData ``` |
| To | ``` - (instancetype)initWithData:(NSData *)pictData ``` |

NSPageController.hModified [NSPageController.delegate](https://developer.apple.com/documentation/appkit/nspagecontroller/1435019-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<NSPageControllerDelegate> delegate ``` |
| To | ``` @property(assign) IBOutlet id<NSPageControllerDelegate> delegate ``` |

Modified [-[NSPageController navigateBack:]](https://developer.apple.com/documentation/appkit/nspagecontroller/1435017-navigateback)

|  | Declaration |
| --- | --- |
| From | ``` - (void)navigateBack:(id)sender ``` |
| To | ``` - (IBAction)navigateBack:(id)sender ``` |

Modified [-[NSPageController navigateForward:]](https://developer.apple.com/documentation/appkit/nspagecontroller/1435004-navigateforward)

|  | Declaration |
| --- | --- |
| From | ``` - (void)navigateForward:(id)sender ``` |
| To | ``` - (IBAction)navigateForward:(id)sender ``` |

Modified [NSPageController.selectedViewController](https://developer.apple.com/documentation/appkit/nspagecontroller/1435013-selectedviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readonly) NSViewController *selectedViewController ``` |
| To | ``` @property(readonly, strong) NSViewController *selectedViewController ``` |

Modified [-[NSPageController takeSelectedIndexFrom:]](https://developer.apple.com/documentation/appkit/nspagecontroller/1435011-takeselectedindexfrom)

|  | Declaration |
| --- | --- |
| From | ``` - (void)takeSelectedIndexFrom:(id)sender ``` |
| To | ``` - (IBAction)takeSelectedIndexFrom:(id)sender ``` |

Modified [-[NSPageControllerDelegate pageController:didTransitionToObject:]](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/1435021-pagecontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPageControllerDelegate pageController:frameForObject:]](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/1434992-pagecontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPageControllerDelegate pageController:identifierForObject:]](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/1435007-pagecontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPageControllerDelegate pageController:prepareViewController:withObject:]](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/1434983-pagecontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPageControllerDelegate pageController:viewControllerForIdentifier:]](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/1435015-pagecontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPageControllerDelegate pageControllerDidEndLiveTransition:]](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/1434985-pagecontrollerdidendlivetransiti)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPageControllerDelegate pageControllerWillStartLiveTransition:]](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/1435009-pagecontrollerwillstartlivetrans)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSPageLayout.hRemoved [-[NSPageLayout accessoryControllers]](https://developer.apple.com/documentation/appkit/nspagelayout/1397788-accessorycontrollers)Removed [-[NSPageLayout printInfo]](https://developer.apple.com/documentation/appkit/nspagelayout/1397804-printinfo)Added [NSPageLayout.accessoryControllers](https://developer.apple.com/documentation/appkit/nspagelayout/1397788-accessorycontrollers)Added [NSPageLayout.printInfo](https://developer.apple.com/documentation/appkit/nspagelayout/1397804-printinfo)NSPanGestureRecognizer.h (Added)Added [NSPanGestureRecognizer](https://developer.apple.com/documentation/appkit/nspangesturerecognizer)Added [NSPanGestureRecognizer.buttonMask](https://developer.apple.com/documentation/appkit/nspangesturerecognizer/1515529-buttonmask)Added [-[NSPanGestureRecognizer setTranslation:inView:]](https://developer.apple.com/documentation/appkit/nspangesturerecognizer/1515533-settranslation)Added [-[NSPanGestureRecognizer translationInView:]](https://developer.apple.com/documentation/appkit/nspangesturerecognizer/1515531-translationinview)Added [-[NSPanGestureRecognizer velocityInView:]](https://developer.apple.com/documentation/appkit/nspangesturerecognizer/1515532-velocityinview)NSPanel.hRemoved [-[NSPanel becomesKeyOnlyIfNeeded]](https://developer.apple.com/documentation/appkit/nspanel/1528836-becomeskeyonlyifneeded)Removed [-[NSPanel isFloatingPanel]](https://developer.apple.com/documentation/appkit/nspanel/1531901-floatingpanel)Removed [-[NSPanel setBecomesKeyOnlyIfNeeded:]](https://developer.apple.com/documentation/appkit/nspanel/1528836-becomeskeyonlyifneeded)Removed [-[NSPanel setFloatingPanel:]](https://developer.apple.com/documentation/appkit/nspanel/1531901-isfloatingpanel)Removed [-[NSPanel setWorksWhenModal:]](https://developer.apple.com/documentation/appkit/nspanel/1525549-workswhenmodal)Removed [-[NSPanel worksWhenModal]](https://developer.apple.com/documentation/appkit/nspanel/1525549-workswhenmodal)Added [NSPanel.becomesKeyOnlyIfNeeded](https://developer.apple.com/documentation/appkit/nspanel/1528836-becomeskeyonlyifneeded)Added [NSPanel.floatingPanel](https://developer.apple.com/documentation/appkit/nspanel/1531901-floatingpanel)Added [NSPanel.worksWhenModal](https://developer.apple.com/documentation/appkit/nspanel/1525549-workswhenmodal)Modified [NSAlertAlternateReturn](https://developer.apple.com/documentation/appkit/nsalertalternatereturn)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSAlertDefaultReturn](https://developer.apple.com/documentation/appkit/nsalertdefaultreturn)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSAlertErrorReturn](https://developer.apple.com/documentation/appkit/nsalerterrorreturn)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSAlertOtherReturn](https://developer.apple.com/documentation/appkit/nsalertotherreturn)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSBeginAlertSheet()](https://developer.apple.com/documentation/appkit/1540941-nsbeginalertsheet)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSBeginCriticalAlertSheet()](https://developer.apple.com/documentation/appkit/1540925-nsbegincriticalalertsheet)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSBeginInformationalAlertSheet()](https://developer.apple.com/documentation/appkit/1540936-nsbegininformationalalertsheet)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSCancelButton](https://developer.apple.com/documentation/appkit/nscancelbutton)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSGetAlertPanel()](https://developer.apple.com/documentation/appkit/1540947-nsgetalertpanel)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSGetCriticalAlertPanel()](https://developer.apple.com/documentation/appkit/1540932-nsgetcriticalalertpanel)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSGetInformationalAlertPanel()](https://developer.apple.com/documentation/appkit/1540937-nsgetinformationalalertpanel)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSHUDWindowMask](https://developer.apple.com/documentation/appkit/nshudwindowmask)

|  | Introduction |
| --- | --- |
| From | OS X 10.5 |
| To | OS X 10.6 |

Modified [NSOKButton](https://developer.apple.com/documentation/appkit/1540940-anonymous/nsokbutton)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSReleaseAlertPanel()](https://developer.apple.com/documentation/appkit/1533868-nsreleasealertpanel)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSRunAlertPanel()](https://developer.apple.com/documentation/appkit/1540934-nsrunalertpanel)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSRunCriticalAlertPanel()](https://developer.apple.com/documentation/appkit/1540943-nsruncriticalalertpanel)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSRunInformationalAlertPanel()](https://developer.apple.com/documentation/appkit/1540926-nsruninformationalalertpanel)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

NSParagraphStyle.hRemoved [-[NSMutableParagraphStyle setAlignment:]](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1534368-alignment)Removed [-[NSMutableParagraphStyle setBaseWritingDirection:]](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1534601-basewritingdirection)Removed [-[NSMutableParagraphStyle setDefaultTabInterval:]](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1529861-defaulttabinterval)Removed [-[NSMutableParagraphStyle setFirstLineHeadIndent:]](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1528392-firstlineheadindent)Removed [-[NSMutableParagraphStyle setHeadIndent:]](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1525135-headindent)Removed [-[NSMutableParagraphStyle setHeaderLevel:]](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1533962-headerlevel)Removed [-[NSMutableParagraphStyle setHyphenationFactor:]](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1535553-hyphenationfactor)Removed [-[NSMutableParagraphStyle setLineBreakMode:]](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1535126-linebreakmode)Removed [-[NSMutableParagraphStyle setLineHeightMultiple:]](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1524596-lineheightmultiple)Removed [-[NSMutableParagraphStyle setLineSpacing:]](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1528742-linespacing)Removed [-[NSMutableParagraphStyle setMaximumLineHeight:]](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1524351-maximumlineheight)Removed [-[NSMutableParagraphStyle setMinimumLineHeight:]](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1531118-minimumlineheight)Removed [-[NSMutableParagraphStyle setParagraphSpacing:]](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1532528-paragraphspacing)Removed [-[NSMutableParagraphStyle setParagraphSpacingBefore:]](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1527729-paragraphspacingbefore)Removed [-[NSMutableParagraphStyle setTabStops:]](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1531988-tabstops)Removed [-[NSMutableParagraphStyle setTailIndent:]](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1531666-tailindent)Removed [-[NSMutableParagraphStyle setTextBlocks:]](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1535855-textblocks)Removed [-[NSMutableParagraphStyle setTextLists:]](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1524648-textlists)Removed [-[NSMutableParagraphStyle setTighteningFactorForTruncation:]](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1531383-tighteningfactorfortruncation)Removed [-[NSParagraphStyle alignment]](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1532321-alignment)Removed [-[NSParagraphStyle baseWritingDirection]](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1527354-basewritingdirection)Removed [-[NSParagraphStyle defaultTabInterval]](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1535614-defaulttabinterval)Removed [-[NSParagraphStyle firstLineHeadIndent]](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1527764-firstlineheadindent)Removed [-[NSParagraphStyle headIndent]](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1530760-headindent)Removed [-[NSParagraphStyle headerLevel]](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1535869-headerlevel)Removed [-[NSParagraphStyle hyphenationFactor]](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1529275-hyphenationfactor)Removed [-[NSParagraphStyle lineBreakMode]](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1529937-linebreakmode)Removed [-[NSParagraphStyle lineHeightMultiple]](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1528614-lineheightmultiple)Removed [-[NSParagraphStyle lineSpacing]](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1524635-linespacing)Removed [-[NSParagraphStyle maximumLineHeight]](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1533343-maximumlineheight)Removed [-[NSParagraphStyle minimumLineHeight]](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1535639-minimumlineheight)Removed [-[NSParagraphStyle paragraphSpacing]](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1530912-paragraphspacing)Removed [-[NSParagraphStyle paragraphSpacingBefore]](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1533011-paragraphspacingbefore)Removed [-[NSParagraphStyle tabStops]](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1532841-tabstops)Removed [-[NSParagraphStyle tailIndent]](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1525556-tailindent)Removed [-[NSParagraphStyle textBlocks]](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1528053-textblocks)Removed [-[NSParagraphStyle textLists]](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1534193-textlists)Removed [-[NSParagraphStyle tighteningFactorForTruncation]](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1529278-tighteningfactorfortruncation)Removed [-[NSTextTab alignment]](https://developer.apple.com/documentation/appkit/nstexttab/1527212-alignment)Removed [-[NSTextTab location]](https://developer.apple.com/documentation/appkit/nstexttab/1527968-location)Removed [-[NSTextTab options]](https://developer.apple.com/documentation/uikit/nstexttab/1534965-options)Removed [-[NSTextTab tabStopType]](https://developer.apple.com/documentation/appkit/nstexttab/1527842-tabstoptype)Added [NSMutableParagraphStyle.alignment](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1534368-alignment)Added [NSMutableParagraphStyle.baseWritingDirection](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1534601-basewritingdirection)Added [NSMutableParagraphStyle.defaultTabInterval](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1529861-defaulttabinterval)Added [NSMutableParagraphStyle.firstLineHeadIndent](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1528392-firstlineheadindent)Added [NSMutableParagraphStyle.headIndent](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1525135-headindent)Added [NSMutableParagraphStyle.headerLevel](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1533962-headerlevel)Added [NSMutableParagraphStyle.hyphenationFactor](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1535553-hyphenationfactor)Added [NSMutableParagraphStyle.lineBreakMode](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1535126-linebreakmode)Added [NSMutableParagraphStyle.lineHeightMultiple](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1524596-lineheightmultiple)Added [NSMutableParagraphStyle.lineSpacing](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1528742-linespacing)Added [NSMutableParagraphStyle.maximumLineHeight](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1524351-maximumlineheight)Added [NSMutableParagraphStyle.minimumLineHeight](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1531118-minimumlineheight)Added [NSMutableParagraphStyle.paragraphSpacing](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1532528-paragraphspacing)Added [NSMutableParagraphStyle.paragraphSpacingBefore](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1527729-paragraphspacingbefore)Added [NSMutableParagraphStyle.tabStops](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1531988-tabstops)Added [NSMutableParagraphStyle.tailIndent](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1531666-tailindent)Added [NSMutableParagraphStyle.textBlocks](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1535855-textblocks)Added [NSMutableParagraphStyle.textLists](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1524648-textlists)Added [NSMutableParagraphStyle.tighteningFactorForTruncation](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1531383-tighteningfactorfortruncation)Added [NSParagraphStyle.alignment](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1532321-alignment)Added [NSParagraphStyle.baseWritingDirection](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1527354-basewritingdirection)Added [NSParagraphStyle.defaultTabInterval](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1535614-defaulttabinterval)Added [NSParagraphStyle.firstLineHeadIndent](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1527764-firstlineheadindent)Added [NSParagraphStyle.headIndent](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1530760-headindent)Added [NSParagraphStyle.headerLevel](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1535869-headerlevel)Added [NSParagraphStyle.hyphenationFactor](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1529275-hyphenationfactor)Added [NSParagraphStyle.lineBreakMode](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1529937-linebreakmode)Added [NSParagraphStyle.lineHeightMultiple](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1528614-lineheightmultiple)Added [NSParagraphStyle.lineSpacing](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1524635-linespacing)Added [NSParagraphStyle.maximumLineHeight](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1533343-maximumlineheight)Added [NSParagraphStyle.minimumLineHeight](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1535639-minimumlineheight)Added [NSParagraphStyle.paragraphSpacing](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1530912-paragraphspacing)Added [NSParagraphStyle.paragraphSpacingBefore](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1533011-paragraphspacingbefore)Added [NSParagraphStyle.tabStops](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1532841-tabstops)Added [NSParagraphStyle.tailIndent](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1525556-tailindent)Added [NSParagraphStyle.textBlocks](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1528053-textblocks)Added [NSParagraphStyle.textLists](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1534193-textlists)Added [NSParagraphStyle.tighteningFactorForTruncation](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1529278-tighteningfactorfortruncation)Added [NSTextTab.alignment](https://developer.apple.com/documentation/appkit/nstexttab/1527212-alignment)Added [NSTextTab.location](https://developer.apple.com/documentation/appkit/nstexttab/1527968-location)Added [NSTextTab.options](https://developer.apple.com/documentation/appkit/nstexttab/1534965-options)Added [NSTextTab.tabStopType](https://developer.apple.com/documentation/appkit/nstexttab/1527842-tabstoptype)Modified [NSParagraphStyle](https://developer.apple.com/documentation/uikit/nsparagraphstyle)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying, NSSecureCoding |

Modified [-[NSTextTab initWithTextAlignment:location:options:]](https://developer.apple.com/documentation/uikit/nstexttab/1526080-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTextAlignment:(NSTextAlignment)alignment location:(CGFloat)loc options:(NSDictionary *)options ``` |
| To | ``` - (instancetype)initWithTextAlignment:(NSTextAlignment)alignment location:(CGFloat)loc options:(NSDictionary *)options ``` |

Modified [-[NSTextTab initWithType:location:]](https://developer.apple.com/documentation/appkit/nstexttab/1526556-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithType:(NSTextTabType)type location:(CGFloat)loc ``` |
| To | ``` - (instancetype)initWithType:(NSTextTabType)type location:(CGFloat)loc ``` |

NSPasteboard.hRemoved [-[NSPasteboard changeCount]](https://developer.apple.com/documentation/appkit/nspasteboard/1533544-changecount)Removed [-[NSPasteboard name]](https://developer.apple.com/documentation/appkit/nspasteboard/1529388-name)Removed [-[NSPasteboard pasteboardItems]](https://developer.apple.com/documentation/appkit/nspasteboard/1529995-pasteboarditems)Removed [-[NSPasteboard types]](https://developer.apple.com/documentation/appkit/nspasteboard/1529599-types)Added [NSPasteboard.changeCount](https://developer.apple.com/documentation/appkit/nspasteboard/1533544-changecount)Added [NSPasteboard.name](https://developer.apple.com/documentation/appkit/nspasteboard/1529388-name)Added [NSPasteboard.pasteboardItems](https://developer.apple.com/documentation/appkit/nspasteboard/1529995-pasteboarditems)Added [NSPasteboard.types](https://developer.apple.com/documentation/appkit/nspasteboard/1529599-types)Modified [-[NSPasteboardReading initWithPasteboardPropertyList:ofType:]](https://developer.apple.com/documentation/appkit/nspasteboardreading/1528252-initwithpasteboardpropertylist)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPasteboardWriting writingOptionsForType:pasteboard:]](https://developer.apple.com/documentation/appkit/nspasteboardwriting/1525372-writingoptionsfortype)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSPasteboardItem.hRemoved [-[NSPasteboardItem types]](https://developer.apple.com/documentation/appkit/nspasteboarditem/1508499-types)Added [NSPasteboardItem.types](https://developer.apple.com/documentation/appkit/nspasteboarditem/1508499-types)Modified [-[NSPasteboardItemDataProvider pasteboardFinishedWithDataProvider:]](https://developer.apple.com/documentation/appkit/nspasteboarditemdataprovider/1508506-pasteboardfinishedwithdataprovid)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSPathCell.hRemoved [-[NSPathCell URL]](https://developer.apple.com/documentation/appkit/nspathcell/1525034-url)Removed [-[NSPathCell allowedTypes]](https://developer.apple.com/documentation/appkit/nspathcell/1524305-allowedtypes)Removed [-[NSPathCell backgroundColor]](https://developer.apple.com/documentation/appkit/nspathcell/1527481-backgroundcolor)Removed [-[NSPathCell clickedPathComponentCell]](https://developer.apple.com/documentation/appkit/nspathcell/1524894-clickedpathcomponentcell)Removed [-[NSPathCell delegate]](https://developer.apple.com/documentation/appkit/nspathcell/1532834-delegate)Removed [-[NSPathCell doubleAction]](https://developer.apple.com/documentation/appkit/nspathcell/1532554-doubleaction)Removed [-[NSPathCell pathComponentCells]](https://developer.apple.com/documentation/appkit/nspathcell/1529433-pathcomponentcells)Removed [-[NSPathCell pathStyle]](https://developer.apple.com/documentation/appkit/nspathcell/1524249-pathstyle)Removed [-[NSPathCell placeholderAttributedString]](https://developer.apple.com/documentation/appkit/nspathcell/1524552-placeholderattributedstring)Removed [-[NSPathCell placeholderString]](https://developer.apple.com/documentation/appkit/nspathcell/1531136-placeholderstring)Removed [-[NSPathCell setAllowedTypes:]](https://developer.apple.com/documentation/appkit/nspathcell/1524305-allowedtypes)Removed [-[NSPathCell setBackgroundColor:]](https://developer.apple.com/documentation/appkit/nspathcell/1527481-backgroundcolor)Removed [-[NSPathCell setControlSize:]](https://developer.apple.com/documentation/appkit/nspathcell/1808573-setcontrolsize)Removed [-[NSPathCell setDelegate:]](https://developer.apple.com/documentation/appkit/nspathcell/1532834-delegate)Removed [-[NSPathCell setDoubleAction:]](https://developer.apple.com/documentation/appkit/nspathcell/1532554-doubleaction)Removed [-[NSPathCell setPathComponentCells:]](https://developer.apple.com/documentation/appkit/nspathcell/1529433-pathcomponentcells)Removed [-[NSPathCell setPathStyle:]](https://developer.apple.com/documentation/appkit/nspathcell/1524249-pathstyle)Removed [-[NSPathCell setPlaceholderAttributedString:]](https://developer.apple.com/documentation/appkit/nspathcell/1524552-placeholderattributedstring)Removed [-[NSPathCell setPlaceholderString:]](https://developer.apple.com/documentation/appkit/nspathcell/1531136-placeholderstring)Removed [-[NSPathCell setURL:]](https://developer.apple.com/documentation/appkit/nspathcell/1524894-clickedpathcomponentcell)Added [NSPathCell.URL](https://developer.apple.com/documentation/appkit/nspathcell/1525034-url)Added [NSPathCell.allowedTypes](https://developer.apple.com/documentation/appkit/nspathcell/1524305-allowedtypes)Added [NSPathCell.backgroundColor](https://developer.apple.com/documentation/appkit/nspathcell/1527481-backgroundcolor)Added [NSPathCell.clickedPathComponentCell](https://developer.apple.com/documentation/appkit/nspathcell/1524894-clickedpathcomponentcell)Added [NSPathCell.delegate](https://developer.apple.com/documentation/appkit/nspathcell/1532834-delegate)Added [NSPathCell.doubleAction](https://developer.apple.com/documentation/appkit/nspathcell/1532554-doubleaction)Added [NSPathCell.pathComponentCells](https://developer.apple.com/documentation/appkit/nspathcell/1529433-pathcomponentcells)Added [NSPathCell.pathStyle](https://developer.apple.com/documentation/appkit/nspathcell/1524249-pathstyle)Added [NSPathCell.placeholderAttributedString](https://developer.apple.com/documentation/appkit/nspathcell/1524552-placeholderattributedstring)Added [NSPathCell.placeholderString](https://developer.apple.com/documentation/appkit/nspathcell/1531136-placeholderstring)Modified [-[NSPathCellDelegate pathCell:willDisplayOpenPanel:]](https://developer.apple.com/documentation/appkit/nspathcelldelegate/1526099-pathcell)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPathCellDelegate pathCell:willPopUpMenu:]](https://developer.apple.com/documentation/appkit/nspathcelldelegate/1525005-pathcell)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [NSPathStyleNavigationBar](https://developer.apple.com/documentation/appkit/nspathstyle/nspathstylenavigationbar)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

NSPathComponentCell.hRemoved [-[NSPathComponentCell URL]](https://developer.apple.com/documentation/appkit/nspathcomponentcell/1534779-url)Removed [-[NSPathComponentCell image]](https://developer.apple.com/documentation/appkit/nspathcomponentcell/1527550-image)Removed [-[NSPathComponentCell setImage:]](https://developer.apple.com/documentation/appkit/nspathcomponentcell/1527550-image)Removed [-[NSPathComponentCell setURL:]](https://developer.apple.com/documentation/appkit/nspathcomponentcell/1534779-url)Added [NSPathComponentCell.URL](https://developer.apple.com/documentation/appkit/nspathcomponentcell/1534779-url)Added [NSPathComponentCell.image](https://developer.apple.com/documentation/appkit/nspathcomponentcell/1527550-image)NSPathControl.hRemoved [-[NSPathControl URL]](https://developer.apple.com/documentation/appkit/nspathcontrol/1527205-url)Removed [-[NSPathControl backgroundColor]](https://developer.apple.com/documentation/appkit/nspathcontrol/1534164-backgroundcolor)Removed [-[NSPathControl delegate]](https://developer.apple.com/documentation/appkit/nspathcontrol/1526753-delegate)Removed [-[NSPathControl doubleAction]](https://developer.apple.com/documentation/appkit/nspathcontrol/1534088-doubleaction)Removed [-[NSPathControl menu]](https://developer.apple.com/documentation/appkit/nspathcontrol/1535867-menu)Removed [-[NSPathControl pathStyle]](https://developer.apple.com/documentation/appkit/nspathcontrol/1532330-pathstyle)Removed [-[NSPathControl setBackgroundColor:]](https://developer.apple.com/documentation/appkit/nspathcontrol/1534164-backgroundcolor)Removed [-[NSPathControl setDelegate:]](https://developer.apple.com/documentation/appkit/nspathcontrol/1526753-delegate)Removed [-[NSPathControl setDoubleAction:]](https://developer.apple.com/documentation/appkit/nspathcontrol/1534088-doubleaction)Removed [-[NSPathControl setMenu:]](https://developer.apple.com/documentation/appkit/nspathcontrol/1535867-menu)Removed [-[NSPathControl setPathStyle:]](https://developer.apple.com/documentation/appkit/nspathcontrol/1532330-pathstyle)Removed [-[NSPathControl setURL:]](https://developer.apple.com/documentation/appkit/nspathcontrol/1527205-url)Added [NSPathControl.URL](https://developer.apple.com/documentation/appkit/nspathcontrol/1527205-url)Added [NSPathControl.allowedTypes](https://developer.apple.com/documentation/appkit/nspathcontrol/1527415-allowedtypes)Added [NSPathControl.backgroundColor](https://developer.apple.com/documentation/appkit/nspathcontrol/1534164-backgroundcolor)Added [NSPathControl.clickedPathItem](https://developer.apple.com/documentation/appkit/nspathcontrol/1535047-clickedpathitem)Added [NSPathControl.delegate](https://developer.apple.com/documentation/appkit/nspathcontrol/1526753-delegate)Added [NSPathControl.doubleAction](https://developer.apple.com/documentation/appkit/nspathcontrol/1534088-doubleaction)Added [NSPathControl.editable](https://developer.apple.com/documentation/appkit/nspathcontrol/1535833-editable)Added [NSPathControl.menu](https://developer.apple.com/documentation/appkit/nspathcontrol/1535867-menu)Added [NSPathControl.pathItems](https://developer.apple.com/documentation/appkit/nspathcontrol/1528208-pathitems)Added [NSPathControl.pathStyle](https://developer.apple.com/documentation/appkit/nspathcontrol/1532330-pathstyle)Added [NSPathControl.placeholderAttributedString](https://developer.apple.com/documentation/appkit/nspathcontrol/1531486-placeholderattributedstring)Added [NSPathControl.placeholderString](https://developer.apple.com/documentation/appkit/nspathcontrol/1531787-placeholderstring)Added [-[NSPathControlDelegate pathControl:shouldDragItem:withPasteboard:]](https://developer.apple.com/documentation/appkit/nspathcontroldelegate/1526752-pathcontrol)Added NSPathControl(NSDeprecated)Modified [-[NSPathControl clickedPathComponentCell]](https://developer.apple.com/documentation/appkit/nspathcontrol/1533929-clickedpathcomponentcell)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSPathControl pathComponentCells]](https://developer.apple.com/documentation/appkit/nspathcontrol/1526652-pathcomponentcells)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSPathControl setPathComponentCells:]](https://developer.apple.com/documentation/appkit/nspathcontrol/1524663-setpathcomponentcells)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSPathControlDelegate pathControl:acceptDrop:]](https://developer.apple.com/documentation/appkit/nspathcontroldelegate/1528517-pathcontrol)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPathControlDelegate pathControl:shouldDragPathComponentCell:withPasteboard:]](https://developer.apple.com/documentation/appkit/nspathcontroldelegate/1533453-pathcontrol)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPathControlDelegate pathControl:validateDrop:]](https://developer.apple.com/documentation/appkit/nspathcontroldelegate/1528554-pathcontrol)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPathControlDelegate pathControl:willDisplayOpenPanel:]](https://developer.apple.com/documentation/appkit/nspathcontroldelegate/1530012-pathcontrol)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPathControlDelegate pathControl:willPopUpMenu:]](https://developer.apple.com/documentation/appkit/nspathcontroldelegate/1531724-pathcontrol)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSPathControlItem.h (Added)Added [NSPathControlItem](https://developer.apple.com/documentation/appkit/nspathcontrolitem)Added [NSPathControlItem.URL](https://developer.apple.com/documentation/appkit/nspathcontrolitem/1388289-url)Added [NSPathControlItem.attributedTitle](https://developer.apple.com/documentation/appkit/nspathcontrolitem/1388287-attributedtitle)Added [NSPathControlItem.image](https://developer.apple.com/documentation/appkit/nspathcontrolitem/1388295-image)Added [NSPathControlItem.title](https://developer.apple.com/documentation/appkit/nspathcontrolitem/1388293-title)NSPersistentDocument.hRemoved [-[NSPersistentDocument managedObjectContext]](https://developer.apple.com/documentation/appkit/nspersistentdocument/1396162-managedobjectcontext)Removed [-[NSPersistentDocument managedObjectModel]](https://developer.apple.com/documentation/appkit/nspersistentdocument/1396152-managedobjectmodel)Removed [-[NSPersistentDocument setManagedObjectContext:]](https://developer.apple.com/documentation/appkit/nspersistentdocument/1396162-managedobjectcontext)Added [NSPersistentDocument.managedObjectContext](https://developer.apple.com/documentation/appkit/nspersistentdocument/1396162-managedobjectcontext)Added [NSPersistentDocument.managedObjectModel](https://developer.apple.com/documentation/appkit/nspersistentdocument/1396152-managedobjectmodel)NSPopUpButton.hRemoved [-[NSPopUpButton autoenablesItems]](https://developer.apple.com/documentation/appkit/nspopupbutton/1530543-autoenablesitems)Removed [-[NSPopUpButton indexOfSelectedItem]](https://developer.apple.com/documentation/appkit/nspopupbutton/1534134-indexofselecteditem)Removed [-[NSPopUpButton itemArray]](https://developer.apple.com/documentation/appkit/nspopupbutton/1535361-itemarray)Removed [-[NSPopUpButton itemTitles]](https://developer.apple.com/documentation/appkit/nspopupbutton/1529271-itemtitles)Removed [-[NSPopUpButton lastItem]](https://developer.apple.com/documentation/appkit/nspopupbutton/1535371-lastitem)Removed [-[NSPopUpButton menu]](https://developer.apple.com/documentation/appkit/nspopupbutton/1535480-menu)Removed [-[NSPopUpButton numberOfItems]](https://developer.apple.com/documentation/appkit/nspopupbutton/1534959-numberofitems)Removed [-[NSPopUpButton preferredEdge]](https://developer.apple.com/documentation/appkit/nspopupbutton/1535345-preferrededge)Removed [-[NSPopUpButton pullsDown]](https://developer.apple.com/documentation/appkit/nspopupbutton/1532070-pullsdown)Removed [-[NSPopUpButton selectedItem]](https://developer.apple.com/documentation/appkit/nspopupbutton/1526197-selecteditem)Removed [-[NSPopUpButton setAutoenablesItems:]](https://developer.apple.com/documentation/appkit/nspopupbutton/1530543-autoenablesitems)Removed [-[NSPopUpButton setMenu:]](https://developer.apple.com/documentation/appkit/nspopupbutton/1535480-menu)Removed [-[NSPopUpButton setPreferredEdge:]](https://developer.apple.com/documentation/appkit/nspopupbutton/1535345-preferrededge)Removed [-[NSPopUpButton setPullsDown:]](https://developer.apple.com/documentation/appkit/nspopupbutton/1532070-pullsdown)Removed [-[NSPopUpButton titleOfSelectedItem]](https://developer.apple.com/documentation/appkit/nspopupbutton/1534038-titleofselecteditem)Added [NSPopUpButton.autoenablesItems](https://developer.apple.com/documentation/appkit/nspopupbutton/1530543-autoenablesitems)Added [NSPopUpButton.indexOfSelectedItem](https://developer.apple.com/documentation/appkit/nspopupbutton/1534134-indexofselecteditem)Added [NSPopUpButton.itemArray](https://developer.apple.com/documentation/appkit/nspopupbutton/1535361-itemarray)Added [NSPopUpButton.itemTitles](https://developer.apple.com/documentation/appkit/nspopupbutton/1529271-itemtitles)Added [NSPopUpButton.lastItem](https://developer.apple.com/documentation/appkit/nspopupbutton/1535371-lastitem)Added [NSPopUpButton.menu](https://developer.apple.com/documentation/appkit/nspopupbutton/1535480-menu)Added [NSPopUpButton.numberOfItems](https://developer.apple.com/documentation/appkit/nspopupbutton/1534959-numberofitems)Added [NSPopUpButton.preferredEdge](https://developer.apple.com/documentation/appkit/nspopupbutton/1535345-preferrededge)Added [NSPopUpButton.pullsDown](https://developer.apple.com/documentation/appkit/nspopupbutton/1532070-pullsdown)Added [NSPopUpButton.selectedItem](https://developer.apple.com/documentation/appkit/nspopupbutton/1526197-selecteditem)Added [NSPopUpButton.selectedTag](https://developer.apple.com/documentation/appkit/nspopupbutton/1577134-selectedtag)Added [NSPopUpButton.titleOfSelectedItem](https://developer.apple.com/documentation/appkit/nspopupbutton/1534038-titleofselecteditem)Modified [-[NSPopUpButton initWithFrame:pullsDown:]](https://developer.apple.com/documentation/appkit/nspopupbutton/1524562-initwithframe)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFrame:(NSRect)buttonFrame pullsDown:(BOOL)flag ``` |
| To | ``` - (instancetype)initWithFrame:(NSRect)buttonFrame pullsDown:(BOOL)flag ``` |

NSPopUpButtonCell.hRemoved [-[NSPopUpButtonCell altersStateOfSelectedItem]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1528446-altersstateofselecteditem)Removed [-[NSPopUpButtonCell arrowPosition]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1534598-arrowposition)Removed [-[NSPopUpButtonCell autoenablesItems]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1530889-autoenablesitems)Removed [-[NSPopUpButtonCell indexOfSelectedItem]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1534937-indexofselecteditem)Removed [-[NSPopUpButtonCell itemArray]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1533757-itemarray)Removed [-[NSPopUpButtonCell itemTitles]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1532067-itemtitles)Removed [-[NSPopUpButtonCell lastItem]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1535415-lastitem)Removed [-[NSPopUpButtonCell menu]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1529059-menu)Removed [-[NSPopUpButtonCell numberOfItems]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1533633-numberofitems)Removed [-[NSPopUpButtonCell objectValue]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1807211-objectvalue)Removed [-[NSPopUpButtonCell preferredEdge]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1535408-preferrededge)Removed [-[NSPopUpButtonCell pullsDown]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1529949-pullsdown)Removed [-[NSPopUpButtonCell selectedItem]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1533239-selecteditem)Removed [-[NSPopUpButtonCell setAltersStateOfSelectedItem:]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1528446-altersstateofselecteditem)Removed [-[NSPopUpButtonCell setArrowPosition:]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1534598-arrowposition)Removed [-[NSPopUpButtonCell setAutoenablesItems:]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1530889-autoenablesitems)Removed [-[NSPopUpButtonCell setMenu:]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1529059-menu)Removed [-[NSPopUpButtonCell setObjectValue:]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1807208-setobjectvalue)Removed [-[NSPopUpButtonCell setPreferredEdge:]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1535408-preferrededge)Removed [-[NSPopUpButtonCell setPullsDown:]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1529949-pullsdown)Removed [-[NSPopUpButtonCell setUsesItemFromMenu:]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1534951-usesitemfrommenu)Removed [-[NSPopUpButtonCell titleOfSelectedItem]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1529952-titleofselecteditem)Removed [-[NSPopUpButtonCell usesItemFromMenu]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1534951-usesitemfrommenu)Added [NSPopUpButtonCell.altersStateOfSelectedItem](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1528446-altersstateofselecteditem)Added [NSPopUpButtonCell.arrowPosition](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1534598-arrowposition)Added [NSPopUpButtonCell.autoenablesItems](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1530889-autoenablesitems)Added [NSPopUpButtonCell.indexOfSelectedItem](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1534937-indexofselecteditem)Added [NSPopUpButtonCell.itemArray](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1533757-itemarray)Added [NSPopUpButtonCell.itemTitles](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1532067-itemtitles)Added [NSPopUpButtonCell.lastItem](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1535415-lastitem)Added [NSPopUpButtonCell.menu](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1529059-menu)Added [NSPopUpButtonCell.numberOfItems](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1533633-numberofitems)Added [NSPopUpButtonCell.preferredEdge](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1535408-preferrededge)Added [NSPopUpButtonCell.pullsDown](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1529949-pullsdown)Added [NSPopUpButtonCell.selectedItem](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1533239-selecteditem)Added [NSPopUpButtonCell.titleOfSelectedItem](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1529952-titleofselecteditem)Added [NSPopUpButtonCell.usesItemFromMenu](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1534951-usesitemfrommenu)Modified [-[NSPopUpButtonCell initTextCell:pullsDown:]](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1528591-inittextcell)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initTextCell:(NSString *)stringValue pullsDown:(BOOL)pullDown ``` |
| To | ``` - (instancetype)initTextCell:(NSString *)stringValue pullsDown:(BOOL)pullDown ``` |

NSPopover.hAdded [NSPopover.effectiveAppearance](https://developer.apple.com/documentation/appkit/nspopover/1526863-effectiveappearance)Added [-[NSPopover init]](https://developer.apple.com/documentation/appkit/nspopover/1526851-init)Added [-[NSPopover initWithCoder:]](https://developer.apple.com/documentation/appkit/nspopover/1524631-initwithcoder)Added [-[NSPopoverDelegate popoverShouldDetach:]](https://developer.apple.com/documentation/appkit/nspopoverdelegate/1529911-popovershoulddetach)Modified [NSPopover](https://developer.apple.com/documentation/appkit/nspopover)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSAccessibility, NSAccessibilityElement, NSAppearanceCustomization |

Modified [NSPopover.appearance](https://developer.apple.com/documentation/appkit/nspopover/1529859-appearance)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @property NSPopoverAppearance appearance ``` | OS X 10.7 |
| To | ``` @property(strong) NSAppearance *appearance ``` | OS X 10.10 |

Modified [NSPopover.contentViewController](https://developer.apple.com/documentation/appkit/nspopover/1526794-contentviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) NSViewController *contentViewController ``` |
| To | ``` @property(retain) IBOutlet NSViewController *contentViewController ``` |

Modified [NSPopover.delegate](https://developer.apple.com/documentation/appkit/nspopover/1526708-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<NSPopoverDelegate> delegate ``` |
| To | ``` @property(assign) IBOutlet id<NSPopoverDelegate> delegate ``` |

Modified [-[NSPopover performClose:]](https://developer.apple.com/documentation/appkit/nspopover/1534290-performclose)

|  | Declaration |
| --- | --- |
| From | ``` - (void)performClose:(id)sender ``` |
| To | ``` - (IBAction)performClose:(id)sender ``` |

Modified [-[NSPopoverDelegate detachableWindowForPopover:]](https://developer.apple.com/documentation/appkit/nspopoverdelegate/1534822-detachablewindowforpopover)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPopoverDelegate popoverDidClose:]](https://developer.apple.com/documentation/appkit/nspopoverdelegate/1526581-popoverdidclose)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPopoverDelegate popoverDidShow:]](https://developer.apple.com/documentation/appkit/nspopoverdelegate/1533573-popoverdidshow)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPopoverDelegate popoverShouldClose:]](https://developer.apple.com/documentation/appkit/nspopoverdelegate/1532593-popovershouldclose)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPopoverDelegate popoverWillClose:]](https://developer.apple.com/documentation/appkit/nspopoverdelegate/1535119-popoverwillclose)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPopoverDelegate popoverWillShow:]](https://developer.apple.com/documentation/appkit/nspopoverdelegate/1532556-popoverwillshow)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [NSPopoverAppearanceHUD](https://developer.apple.com/documentation/appkit/nspopover/appearance/hud)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSPopoverAppearanceMinimal](https://developer.apple.com/documentation/appkit/nspopoverappearance/nspopoverappearanceminimal)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

NSPredicateEditor.hRemoved [-[NSPredicateEditor rowTemplates]](https://developer.apple.com/documentation/appkit/nspredicateeditor/1474094-rowtemplates)Removed [-[NSPredicateEditor setRowTemplates:]](https://developer.apple.com/documentation/appkit/nspredicateeditor/1474094-rowtemplates)Added [NSPredicateEditor.rowTemplates](https://developer.apple.com/documentation/appkit/nspredicateeditor/1474094-rowtemplates)NSPredicateEditorRowTemplate.hRemoved [-[NSPredicateEditorRowTemplate compoundTypes]](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/1401202-compoundtypes)Removed [-[NSPredicateEditorRowTemplate leftExpressions]](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/1401191-leftexpressions)Removed [-[NSPredicateEditorRowTemplate modifier]](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/1401204-modifier)Removed [-[NSPredicateEditorRowTemplate operators]](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/1401195-operators)Removed [-[NSPredicateEditorRowTemplate options]](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/1401197-options)Removed [-[NSPredicateEditorRowTemplate rightExpressionAttributeType]](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/1401206-rightexpressionattributetype)Removed [-[NSPredicateEditorRowTemplate rightExpressions]](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/1401173-rightexpressions)Removed [-[NSPredicateEditorRowTemplate templateViews]](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/1401193-templateviews)Added [NSPredicateEditorRowTemplate.compoundTypes](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/1401202-compoundtypes)Added [NSPredicateEditorRowTemplate.leftExpressions](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/1401191-leftexpressions)Added [NSPredicateEditorRowTemplate.modifier](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/1401204-modifier)Added [NSPredicateEditorRowTemplate.operators](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/1401195-operators)Added [NSPredicateEditorRowTemplate.options](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/1401197-options)Added [NSPredicateEditorRowTemplate.rightExpressionAttributeType](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/1401206-rightexpressionattributetype)Added [NSPredicateEditorRowTemplate.rightExpressions](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/1401173-rightexpressions)Added [NSPredicateEditorRowTemplate.templateViews](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/1401193-templateviews)Modified [-[NSPredicateEditorRowTemplate initWithCompoundTypes:]](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/1401177-initwithcompoundtypes)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCompoundTypes:(NSArray *)compoundTypes ``` |
| To | ``` - (instancetype)initWithCompoundTypes:(NSArray *)compoundTypes ``` |

Modified [-[NSPredicateEditorRowTemplate initWithLeftExpressions:rightExpressionAttributeType:modifier:operators:options:]](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/1401181-initwithleftexpressions)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithLeftExpressions:(NSArray *)leftExpressions rightExpressionAttributeType:(NSAttributeType)attributeType modifier:(NSComparisonPredicateModifier)modifier operators:(NSArray *)operators options:(NSUInteger)options ``` |
| To | ``` - (instancetype)initWithLeftExpressions:(NSArray *)leftExpressions rightExpressionAttributeType:(NSAttributeType)attributeType modifier:(NSComparisonPredicateModifier)modifier operators:(NSArray *)operators options:(NSUInteger)options ``` |

Modified [-[NSPredicateEditorRowTemplate initWithLeftExpressions:rightExpressions:modifier:operators:options:]](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/1401175-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithLeftExpressions:(NSArray *)leftExpressions rightExpressions:(NSArray *)rightExpressions modifier:(NSComparisonPredicateModifier)modifier operators:(NSArray *)operators options:(NSUInteger)options ``` |
| To | ``` - (instancetype)initWithLeftExpressions:(NSArray *)leftExpressions rightExpressions:(NSArray *)rightExpressions modifier:(NSComparisonPredicateModifier)modifier operators:(NSArray *)operators options:(NSUInteger)options ``` |

NSPressGestureRecognizer.h (Added)Added [NSPressGestureRecognizer](https://developer.apple.com/documentation/appkit/nspressgesturerecognizer)Added [NSPressGestureRecognizer.allowableMovement](https://developer.apple.com/documentation/appkit/nspressgesturerecognizer/1527495-allowablemovement)Added [NSPressGestureRecognizer.buttonMask](https://developer.apple.com/documentation/appkit/nspressgesturerecognizer/1534468-buttonmask)Added [NSPressGestureRecognizer.minimumPressDuration](https://developer.apple.com/documentation/appkit/nspressgesturerecognizer/1531726-minimumpressduration)NSPrintInfo.hRemoved [-[NSPrintInfo bottomMargin]](https://developer.apple.com/documentation/appkit/nsprintinfo/1528397-bottommargin)Removed [-[NSPrintInfo horizontalPagination]](https://developer.apple.com/documentation/appkit/nsprintinfo/1532693-horizontalpagination)Removed [-[NSPrintInfo imageablePageBounds]](https://developer.apple.com/documentation/appkit/nsprintinfo/1526570-imageablepagebounds)Removed [-[NSPrintInfo isHorizontallyCentered]](https://developer.apple.com/documentation/appkit/nsprintinfo/1534703-horizontallycentered)Removed [-[NSPrintInfo isSelectionOnly]](https://developer.apple.com/documentation/appkit/nsprintinfo/1534094-isselectiononly)Removed [-[NSPrintInfo isVerticallyCentered]](https://developer.apple.com/documentation/appkit/nsprintinfo/1530330-isverticallycentered)Removed [-[NSPrintInfo jobDisposition]](https://developer.apple.com/documentation/appkit/nsprintinfo/1528717-jobdisposition)Removed [-[NSPrintInfo leftMargin]](https://developer.apple.com/documentation/appkit/nsprintinfo/1533430-leftmargin)Removed [-[NSPrintInfo localizedPaperName]](https://developer.apple.com/documentation/appkit/nsprintinfo/1524573-localizedpapername)Removed [-[NSPrintInfo orientation]](https://developer.apple.com/documentation/appkit/nsprintinfo/1533755-orientation)Removed [-[NSPrintInfo paperName]](https://developer.apple.com/documentation/appkit/nsprintinfo/1532124-papername)Removed [-[NSPrintInfo paperSize]](https://developer.apple.com/documentation/appkit/nsprintinfo/1534030-papersize)Removed [-[NSPrintInfo printSettings]](https://developer.apple.com/documentation/appkit/nsprintinfo/1529413-printsettings)Removed [-[NSPrintInfo printer]](https://developer.apple.com/documentation/appkit/nsprintinfo/1524495-printer)Removed [-[NSPrintInfo rightMargin]](https://developer.apple.com/documentation/appkit/nsprintinfo/1530882-rightmargin)Removed [-[NSPrintInfo scalingFactor]](https://developer.apple.com/documentation/appkit/nsprintinfo/1529753-scalingfactor)Removed [-[NSPrintInfo setBottomMargin:]](https://developer.apple.com/documentation/appkit/nsprintinfo/1528397-bottommargin)Removed [-[NSPrintInfo setHorizontalPagination:]](https://developer.apple.com/documentation/appkit/nsprintinfo/1532693-horizontalpagination)Removed [-[NSPrintInfo setHorizontallyCentered:]](https://developer.apple.com/documentation/appkit/nsprintinfo/1534703-horizontallycentered)Removed [-[NSPrintInfo setJobDisposition:]](https://developer.apple.com/documentation/appkit/nsprintinfo/1528717-jobdisposition)Removed [-[NSPrintInfo setLeftMargin:]](https://developer.apple.com/documentation/appkit/nsprintinfo/1533430-leftmargin)Removed [-[NSPrintInfo setOrientation:]](https://developer.apple.com/documentation/appkit/nsprintinfo/1533755-orientation)Removed [-[NSPrintInfo setPaperName:]](https://developer.apple.com/documentation/appkit/nsprintinfo/1532124-papername)Removed [-[NSPrintInfo setPaperSize:]](https://developer.apple.com/documentation/appkit/nsprintinfo/1534030-papersize)Removed [-[NSPrintInfo setPrinter:]](https://developer.apple.com/documentation/appkit/nsprintinfo/1524495-printer)Removed [-[NSPrintInfo setRightMargin:]](https://developer.apple.com/documentation/appkit/nsprintinfo/1530882-rightmargin)Removed [-[NSPrintInfo setScalingFactor:]](https://developer.apple.com/documentation/appkit/nsprintinfo/1529753-scalingfactor)Removed [-[NSPrintInfo setSelectionOnly:]](https://developer.apple.com/documentation/appkit/nsprintinfo/1534094-selectiononly)Removed [-[NSPrintInfo setTopMargin:]](https://developer.apple.com/documentation/appkit/nsprintinfo/1529662-topmargin)Removed [-[NSPrintInfo setVerticalPagination:]](https://developer.apple.com/documentation/appkit/nsprintinfo/1526743-verticalpagination)Removed [-[NSPrintInfo setVerticallyCentered:]](https://developer.apple.com/documentation/appkit/nsprintinfo/1530330-verticallycentered)Removed [-[NSPrintInfo topMargin]](https://developer.apple.com/documentation/appkit/nsprintinfo/1529662-topmargin)Removed [-[NSPrintInfo verticalPagination]](https://developer.apple.com/documentation/appkit/nsprintinfo/1526743-verticalpagination)Added [NSPrintInfo.bottomMargin](https://developer.apple.com/documentation/appkit/nsprintinfo/1528397-bottommargin)Added [NSPrintInfo.horizontalPagination](https://developer.apple.com/documentation/appkit/nsprintinfo/1532693-horizontalpagination)Added [NSPrintInfo.horizontallyCentered](https://developer.apple.com/documentation/appkit/nsprintinfo/1534703-horizontallycentered)Added [NSPrintInfo.imageablePageBounds](https://developer.apple.com/documentation/appkit/nsprintinfo/1526570-imageablepagebounds)Added [NSPrintInfo.jobDisposition](https://developer.apple.com/documentation/appkit/nsprintinfo/1528717-jobdisposition)Added [NSPrintInfo.leftMargin](https://developer.apple.com/documentation/appkit/nsprintinfo/1533430-leftmargin)Added [NSPrintInfo.localizedPaperName](https://developer.apple.com/documentation/appkit/nsprintinfo/1524573-localizedpapername)Added [NSPrintInfo.orientation](https://developer.apple.com/documentation/appkit/nsprintinfo/1533755-orientation)Added [NSPrintInfo.paperName](https://developer.apple.com/documentation/appkit/nsprintinfo/1532124-papername)Added [NSPrintInfo.paperSize](https://developer.apple.com/documentation/appkit/nsprintinfo/1534030-papersize)Added [NSPrintInfo.printSettings](https://developer.apple.com/documentation/appkit/nsprintinfo/1529413-printsettings)Added [NSPrintInfo.printer](https://developer.apple.com/documentation/appkit/nsprintinfo/1524495-printer)Added [NSPrintInfo.rightMargin](https://developer.apple.com/documentation/appkit/nsprintinfo/1530882-rightmargin)Added [NSPrintInfo.scalingFactor](https://developer.apple.com/documentation/appkit/nsprintinfo/1529753-scalingfactor)Added [NSPrintInfo.selectionOnly](https://developer.apple.com/documentation/appkit/nsprintinfo/1534094-selectiononly)Added [NSPrintInfo.topMargin](https://developer.apple.com/documentation/appkit/nsprintinfo/1529662-topmargin)Added [NSPrintInfo.verticalPagination](https://developer.apple.com/documentation/appkit/nsprintinfo/1526743-verticalpagination)Added [NSPrintInfo.verticallyCentered](https://developer.apple.com/documentation/appkit/nsprintinfo/1530330-isverticallycentered)Modified [-[NSPrintInfo initWithDictionary:]](https://developer.apple.com/documentation/appkit/nsprintinfo/1526768-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDictionary:(NSDictionary *)attributes ``` |
| To | ``` - (instancetype)initWithDictionary:(NSDictionary *)attributes ``` |

Modified [NSPrintSavePath](https://developer.apple.com/documentation/appkit/nsprintsavepath)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

NSPrintOperation.hRemoved [-[NSPrintOperation PDFPanel]](https://developer.apple.com/documentation/appkit/nsprintoperation/1526838-pdfpanel)Removed [-[NSPrintOperation canSpawnSeparateThread]](https://developer.apple.com/documentation/appkit/nsprintoperation/1532487-canspawnseparatethread)Removed [-[NSPrintOperation context]](https://developer.apple.com/documentation/appkit/nsprintoperation/1534162-context)Removed [-[NSPrintOperation currentPage]](https://developer.apple.com/documentation/appkit/nsprintoperation/1534881-currentpage)Removed [-[NSPrintOperation isCopyingOperation]](https://developer.apple.com/documentation/appkit/nsprintoperation/1534206-iscopyingoperation)Removed [-[NSPrintOperation jobTitle]](https://developer.apple.com/documentation/appkit/nsprintoperation/1535322-jobtitle)Removed [-[NSPrintOperation pageOrder]](https://developer.apple.com/documentation/appkit/nsprintoperation/1532990-pageorder)Removed [-[NSPrintOperation pageRange]](https://developer.apple.com/documentation/appkit/nsprintoperation/1524601-pagerange)Removed [-[NSPrintOperation preferredRenderingQuality]](https://developer.apple.com/documentation/appkit/nsprintoperation/1529716-preferredrenderingquality)Removed [-[NSPrintOperation printInfo]](https://developer.apple.com/documentation/appkit/nsprintoperation/1535187-printinfo)Removed [-[NSPrintOperation printPanel]](https://developer.apple.com/documentation/appkit/nsprintoperation/1529626-printpanel)Removed [-[NSPrintOperation setCanSpawnSeparateThread:]](https://developer.apple.com/documentation/appkit/nsprintoperation/1532487-canspawnseparatethread)Removed [-[NSPrintOperation setJobTitle:]](https://developer.apple.com/documentation/appkit/nsprintoperation/1535322-jobtitle)Removed [-[NSPrintOperation setPDFPanel:]](https://developer.apple.com/documentation/appkit/nsprintoperation/1526838-pdfpanel)Removed [-[NSPrintOperation setPageOrder:]](https://developer.apple.com/documentation/appkit/nsprintoperation/1532990-pageorder)Removed [-[NSPrintOperation setPrintInfo:]](https://developer.apple.com/documentation/appkit/nsprintoperation/1535187-printinfo)Removed [-[NSPrintOperation setPrintPanel:]](https://developer.apple.com/documentation/appkit/nsprintoperation/1529626-printpanel)Removed [-[NSPrintOperation setShowsPrintPanel:]](https://developer.apple.com/documentation/appkit/nsprintoperation/1530666-showsprintpanel)Removed [-[NSPrintOperation setShowsProgressPanel:]](https://developer.apple.com/documentation/appkit/nsprintoperation/1535665-showsprogresspanel)Removed [-[NSPrintOperation showsPrintPanel]](https://developer.apple.com/documentation/appkit/nsprintoperation/1530666-showsprintpanel)Removed [-[NSPrintOperation showsProgressPanel]](https://developer.apple.com/documentation/appkit/nsprintoperation/1535665-showsprogresspanel)Removed [-[NSPrintOperation view]](https://developer.apple.com/documentation/appkit/nsprintoperation/1530311-view)Added [NSPrintOperation.PDFPanel](https://developer.apple.com/documentation/appkit/nsprintoperation/1526838-pdfpanel)Added [NSPrintOperation.canSpawnSeparateThread](https://developer.apple.com/documentation/appkit/nsprintoperation/1532487-canspawnseparatethread)Added [NSPrintOperation.context](https://developer.apple.com/documentation/appkit/nsprintoperation/1534162-context)Added [NSPrintOperation.copyingOperation](https://developer.apple.com/documentation/appkit/nsprintoperation/1534206-copyingoperation)Added [NSPrintOperation.currentPage](https://developer.apple.com/documentation/appkit/nsprintoperation/1534881-currentpage)Added [NSPrintOperation.jobTitle](https://developer.apple.com/documentation/appkit/nsprintoperation/1535322-jobtitle)Added [NSPrintOperation.pageOrder](https://developer.apple.com/documentation/appkit/nsprintoperation/1532990-pageorder)Added [NSPrintOperation.pageRange](https://developer.apple.com/documentation/appkit/nsprintoperation/1524601-pagerange)Added [NSPrintOperation.preferredRenderingQuality](https://developer.apple.com/documentation/appkit/nsprintoperation/1529716-preferredrenderingquality)Added [NSPrintOperation.printInfo](https://developer.apple.com/documentation/appkit/nsprintoperation/1535187-printinfo)Added [NSPrintOperation.printPanel](https://developer.apple.com/documentation/appkit/nsprintoperation/1529626-printpanel)Added [NSPrintOperation.showsPrintPanel](https://developer.apple.com/documentation/appkit/nsprintoperation/1530666-showsprintpanel)Added [NSPrintOperation.showsProgressPanel](https://developer.apple.com/documentation/appkit/nsprintoperation/1535665-showsprogresspanel)Added [NSPrintOperation.view](https://developer.apple.com/documentation/appkit/nsprintoperation/1530311-view)NSPrintPanel.hRemoved [-[NSPrintPanel accessoryControllers]](https://developer.apple.com/documentation/appkit/nsprintpanel/1490543-accessorycontrollers)Removed [-[NSPrintPanel helpAnchor]](https://developer.apple.com/documentation/appkit/nsprintpanel/1490537-helpanchor)Removed [-[NSPrintPanel jobStyleHint]](https://developer.apple.com/documentation/appkit/nsprintpanel/1490529-jobstylehint)Removed [-[NSPrintPanel options]](https://developer.apple.com/documentation/appkit/nsprintpanel/1490542-options)Removed [-[NSPrintPanel printInfo]](https://developer.apple.com/documentation/appkit/nsprintpanel/1490513-printinfo)Removed [-[NSPrintPanel setHelpAnchor:]](https://developer.apple.com/documentation/appkit/nsprintpanel/1490537-helpanchor)Removed [-[NSPrintPanel setJobStyleHint:]](https://developer.apple.com/documentation/appkit/nsprintpanel/1490529-jobstylehint)Removed [-[NSPrintPanel setOptions:]](https://developer.apple.com/documentation/appkit/nsprintpanel/1490542-options)Added [NSPrintPanel.accessoryControllers](https://developer.apple.com/documentation/appkit/nsprintpanel/1490543-accessorycontrollers)Added [NSPrintPanel.helpAnchor](https://developer.apple.com/documentation/appkit/nsprintpanel/1490537-helpanchor)Added [NSPrintPanel.jobStyleHint](https://developer.apple.com/documentation/appkit/nsprintpanel/1490529-jobstylehint)Added [NSPrintPanel.options](https://developer.apple.com/documentation/appkit/nsprintpanel/1490542-options)Added [NSPrintPanel.printInfo](https://developer.apple.com/documentation/appkit/nsprintpanel/1490513-printinfo)Modified [-[NSPrintPanelAccessorizing keyPathsForValuesAffectingPreview]](https://developer.apple.com/documentation/appkit/nsprintpanelaccessorizing/1490516-keypathsforvaluesaffectingprevie)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSPrinter.hRemoved [-[NSPrinter deviceDescription]](https://developer.apple.com/documentation/appkit/nsprinter/1525201-devicedescription)Removed [-[NSPrinter languageLevel]](https://developer.apple.com/documentation/appkit/nsprinter/1525215-languagelevel)Removed [-[NSPrinter name]](https://developer.apple.com/documentation/appkit/nsprinter/1525189-name)Removed [-[NSPrinter type]](https://developer.apple.com/documentation/appkit/nsprinter/1524450-type)Added [NSPrinter.deviceDescription](https://developer.apple.com/documentation/appkit/nsprinter/1525201-devicedescription)Added [NSPrinter.languageLevel](https://developer.apple.com/documentation/appkit/nsprinter/1525215-languagelevel)Added [NSPrinter.name](https://developer.apple.com/documentation/appkit/nsprinter/1525189-name)Added [NSPrinter.type](https://developer.apple.com/documentation/appkit/nsprinter/1524450-type)NSProgressIndicator.hRemoved [-[NSProgressIndicator controlSize]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501157-controlsize)Removed [-[NSProgressIndicator controlTint]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501153-controltint)Removed [-[NSProgressIndicator doubleValue]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501173-doublevalue)Removed [-[NSProgressIndicator isBezeled]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501161-isbezeled)Removed [-[NSProgressIndicator isDisplayedWhenStopped]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501171-displayedwhenstopped)Removed [-[NSProgressIndicator isIndeterminate]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501146-isindeterminate)Removed [-[NSProgressIndicator maxValue]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501165-maxvalue)Removed [-[NSProgressIndicator minValue]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501169-minvalue)Removed [-[NSProgressIndicator setBezeled:]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501161-bezeled)Removed [-[NSProgressIndicator setControlSize:]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501157-controlsize)Removed [-[NSProgressIndicator setControlTint:]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501153-controltint)Removed [-[NSProgressIndicator setDisplayedWhenStopped:]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501171-displayedwhenstopped)Removed [-[NSProgressIndicator setDoubleValue:]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501173-doublevalue)Removed [-[NSProgressIndicator setIndeterminate:]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501146-indeterminate)Removed [-[NSProgressIndicator setMaxValue:]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501165-maxvalue)Removed [-[NSProgressIndicator setMinValue:]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501169-minvalue)Removed [-[NSProgressIndicator setStyle:]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501158-style)Removed [-[NSProgressIndicator setUsesThreadedAnimation:]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501160-usesthreadedanimation)Removed [-[NSProgressIndicator style]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501158-style)Removed [-[NSProgressIndicator usesThreadedAnimation]](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501160-usesthreadedanimation)Added [NSProgressIndicator.bezeled](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501161-isbezeled)Added [NSProgressIndicator.controlSize](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501157-controlsize)Added [NSProgressIndicator.controlTint](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501153-controltint)Added [NSProgressIndicator.displayedWhenStopped](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501171-displayedwhenstopped)Added [NSProgressIndicator.doubleValue](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501173-doublevalue)Added [NSProgressIndicator.indeterminate](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501146-isindeterminate)Added [NSProgressIndicator.maxValue](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501165-maxvalue)Added [NSProgressIndicator.minValue](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501169-minvalue)Added [NSProgressIndicator.style](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501158-style)Added [NSProgressIndicator.usesThreadedAnimation](https://developer.apple.com/documentation/appkit/nsprogressindicator/1501160-usesthreadedanimation)Modified [NSProgressIndicator](https://developer.apple.com/documentation/appkit/nsprogressindicator)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSAccessibilityProgressIndicator |

NSQuickDrawView.hModified NSQuickDrawView

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.4 |

NSResponder.hRemoved [-[NSResponder acceptsFirstResponder]](https://developer.apple.com/documentation/appkit/nsresponder/1528708-acceptsfirstresponder)Removed [-[NSResponder menu]](https://developer.apple.com/documentation/appkit/nsresponder/1533094-menu)Removed [-[NSResponder nextResponder]](https://developer.apple.com/documentation/appkit/nsresponder/1528245-nextresponder)Removed [-[NSResponder setMenu:]](https://developer.apple.com/documentation/appkit/nsresponder/1533094-menu)Removed [-[NSResponder setNextResponder:]](https://developer.apple.com/documentation/appkit/nsresponder/1528245-nextresponder)Removed [-[NSResponder undoManager]](https://developer.apple.com/documentation/appkit/nsresponder/1535376-undomanager)Added [NSResponder.acceptsFirstResponder](https://developer.apple.com/documentation/appkit/nsresponder/1528708-acceptsfirstresponder)Added [-[NSResponder init]](https://developer.apple.com/documentation/appkit/nsresponder/1525437-init)Added [-[NSResponder initWithCoder:]](https://developer.apple.com/documentation/appkit/nsresponder/1535389-initwithcoder)Added [NSResponder.menu](https://developer.apple.com/documentation/appkit/nsresponder/1533094-menu)Added [NSResponder.nextResponder](https://developer.apple.com/documentation/appkit/nsresponder/1528245-nextresponder)Added [NSResponder.undoManager](https://developer.apple.com/documentation/appkit/nsresponder/1535376-undomanager)NSRotationGestureRecognizer.h (Added)Added [NSRotationGestureRecognizer](https://developer.apple.com/documentation/appkit/nsrotationgesturerecognizer)Added [NSRotationGestureRecognizer.rotation](https://developer.apple.com/documentation/appkit/nsrotationgesturerecognizer/1527087-rotation)Added [NSRotationGestureRecognizer.rotationInDegrees](https://developer.apple.com/documentation/appkit/nsrotationgesturerecognizer/1535523-rotationindegrees)NSRuleEditor.hRemoved [-[NSRuleEditor canRemoveAllRows]](https://developer.apple.com/documentation/appkit/nsruleeditor/1535531-canremoveallrows)Removed [-[NSRuleEditor criteriaKeyPath]](https://developer.apple.com/documentation/appkit/nsruleeditor/1524761-criteriakeypath)Removed [-[NSRuleEditor delegate]](https://developer.apple.com/documentation/appkit/nsruleeditor/1528017-delegate)Removed [-[NSRuleEditor displayValuesKeyPath]](https://developer.apple.com/documentation/appkit/nsruleeditor/1535572-displayvalueskeypath)Removed [-[NSRuleEditor formattingDictionary]](https://developer.apple.com/documentation/appkit/nsruleeditor/1526737-formattingdictionary)Removed [-[NSRuleEditor formattingStringsFilename]](https://developer.apple.com/documentation/appkit/nsruleeditor/1533323-formattingstringsfilename)Removed [-[NSRuleEditor isEditable]](https://developer.apple.com/documentation/appkit/nsruleeditor/1530425-iseditable)Removed [-[NSRuleEditor nestingMode]](https://developer.apple.com/documentation/appkit/nsruleeditor/1533955-nestingmode)Removed [-[NSRuleEditor numberOfRows]](https://developer.apple.com/documentation/appkit/nsruleeditor/1529330-numberofrows)Removed [-[NSRuleEditor predicate]](https://developer.apple.com/documentation/appkit/nsruleeditor/1525681-predicate)Removed [-[NSRuleEditor rowClass]](https://developer.apple.com/documentation/appkit/nsruleeditor/1535414-rowclass)Removed [-[NSRuleEditor rowHeight]](https://developer.apple.com/documentation/appkit/nsruleeditor/1531071-rowheight)Removed [-[NSRuleEditor rowTypeKeyPath]](https://developer.apple.com/documentation/appkit/nsruleeditor/1527020-rowtypekeypath)Removed [-[NSRuleEditor selectedRowIndexes]](https://developer.apple.com/documentation/appkit/nsruleeditor/1529841-selectedrowindexes)Removed [-[NSRuleEditor setCanRemoveAllRows:]](https://developer.apple.com/documentation/appkit/nsruleeditor/1535531-canremoveallrows)Removed [-[NSRuleEditor setCriteriaKeyPath:]](https://developer.apple.com/documentation/appkit/nsruleeditor/1524761-criteriakeypath)Removed [-[NSRuleEditor setDelegate:]](https://developer.apple.com/documentation/appkit/nsruleeditor/1528017-delegate)Removed [-[NSRuleEditor setDisplayValuesKeyPath:]](https://developer.apple.com/documentation/appkit/nsruleeditor/1535572-displayvalueskeypath)Removed [-[NSRuleEditor setEditable:]](https://developer.apple.com/documentation/appkit/nsruleeditor/1530425-iseditable)Removed [-[NSRuleEditor setFormattingDictionary:]](https://developer.apple.com/documentation/appkit/nsruleeditor/1526737-formattingdictionary)Removed [-[NSRuleEditor setFormattingStringsFilename:]](https://developer.apple.com/documentation/appkit/nsruleeditor/1533323-formattingstringsfilename)Removed [-[NSRuleEditor setNestingMode:]](https://developer.apple.com/documentation/appkit/nsruleeditor/1533955-nestingmode)Removed [-[NSRuleEditor setRowClass:]](https://developer.apple.com/documentation/appkit/nsruleeditor/1535414-rowclass)Removed [-[NSRuleEditor setRowHeight:]](https://developer.apple.com/documentation/appkit/nsruleeditor/1531071-rowheight)Removed [-[NSRuleEditor setRowTypeKeyPath:]](https://developer.apple.com/documentation/appkit/nsruleeditor/1527020-rowtypekeypath)Removed [-[NSRuleEditor setSubrowsKeyPath:]](https://developer.apple.com/documentation/appkit/nsruleeditor/1535242-subrowskeypath)Removed [-[NSRuleEditor subrowsKeyPath]](https://developer.apple.com/documentation/appkit/nsruleeditor/1535242-subrowskeypath)Added [NSRuleEditor.canRemoveAllRows](https://developer.apple.com/documentation/appkit/nsruleeditor/1535531-canremoveallrows)Added [NSRuleEditor.criteriaKeyPath](https://developer.apple.com/documentation/appkit/nsruleeditor/1524761-criteriakeypath)Added [NSRuleEditor.delegate](https://developer.apple.com/documentation/appkit/nsruleeditor/1528017-delegate)Added [NSRuleEditor.displayValuesKeyPath](https://developer.apple.com/documentation/appkit/nsruleeditor/1535572-displayvalueskeypath)Added [NSRuleEditor.editable](https://developer.apple.com/documentation/appkit/nsruleeditor/1530425-iseditable)Added [NSRuleEditor.formattingDictionary](https://developer.apple.com/documentation/appkit/nsruleeditor/1526737-formattingdictionary)Added [NSRuleEditor.formattingStringsFilename](https://developer.apple.com/documentation/appkit/nsruleeditor/1533323-formattingstringsfilename)Added [NSRuleEditor.nestingMode](https://developer.apple.com/documentation/appkit/nsruleeditor/1533955-nestingmode)Added [NSRuleEditor.numberOfRows](https://developer.apple.com/documentation/appkit/nsruleeditor/1529330-numberofrows)Added [NSRuleEditor.predicate](https://developer.apple.com/documentation/appkit/nsruleeditor/1525681-predicate)Added [NSRuleEditor.rowClass](https://developer.apple.com/documentation/appkit/nsruleeditor/1535414-rowclass)Added [NSRuleEditor.rowHeight](https://developer.apple.com/documentation/appkit/nsruleeditor/1531071-rowheight)Added [NSRuleEditor.rowTypeKeyPath](https://developer.apple.com/documentation/appkit/nsruleeditor/1527020-rowtypekeypath)Added [NSRuleEditor.selectedRowIndexes](https://developer.apple.com/documentation/appkit/nsruleeditor/1529841-selectedrowindexes)Added [NSRuleEditor.subrowsKeyPath](https://developer.apple.com/documentation/appkit/nsruleeditor/1535242-subrowskeypath)Modified [-[NSRuleEditorDelegate ruleEditor:predicatePartsForCriterion:withDisplayValue:inRow:]](https://developer.apple.com/documentation/appkit/nsruleeditordelegate/1526667-ruleeditor)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSRuleEditorDelegate ruleEditorRowsDidChange:]](https://developer.apple.com/documentation/appkit/nsruleeditordelegate/1533292-ruleeditorrowsdidchange)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSRulerMarker.hRemoved [-[NSRulerMarker image]](https://developer.apple.com/documentation/appkit/nsrulermarker/1496251-image)Removed [-[NSRulerMarker imageOrigin]](https://developer.apple.com/documentation/appkit/nsrulermarker/1496236-imageorigin)Removed [-[NSRulerMarker imageRectInRuler]](https://developer.apple.com/documentation/appkit/nsrulermarker/1496249-imagerectinruler)Removed [-[NSRulerMarker isDragging]](https://developer.apple.com/documentation/appkit/nsrulermarker/1496253-dragging)Removed [-[NSRulerMarker isMovable]](https://developer.apple.com/documentation/appkit/nsrulermarker/1496247-movable)Removed [-[NSRulerMarker isRemovable]](https://developer.apple.com/documentation/appkit/nsrulermarker/1496238-isremovable)Removed [-[NSRulerMarker markerLocation]](https://developer.apple.com/documentation/appkit/nsrulermarker/1496255-markerlocation)Removed [-[NSRulerMarker representedObject]](https://developer.apple.com/documentation/appkit/nsrulermarker/1496244-representedobject)Removed [-[NSRulerMarker ruler]](https://developer.apple.com/documentation/appkit/nsrulermarker/1496239-ruler)Removed [-[NSRulerMarker setImage:]](https://developer.apple.com/documentation/appkit/nsrulermarker/1496251-image)Removed [-[NSRulerMarker setImageOrigin:]](https://developer.apple.com/documentation/appkit/nsrulermarker/1496236-imageorigin)Removed [-[NSRulerMarker setMarkerLocation:]](https://developer.apple.com/documentation/appkit/nsrulermarker/1496255-markerlocation)Removed [-[NSRulerMarker setMovable:]](https://developer.apple.com/documentation/appkit/nsrulermarker/1496247-ismovable)Removed [-[NSRulerMarker setRemovable:]](https://developer.apple.com/documentation/appkit/nsrulermarker/1496238-removable)Removed [-[NSRulerMarker setRepresentedObject:]](https://developer.apple.com/documentation/appkit/nsrulermarker/1496244-representedobject)Removed [-[NSRulerMarker thicknessRequiredInRuler]](https://developer.apple.com/documentation/appkit/nsrulermarker/1496245-thicknessrequiredinruler)Added [NSRulerMarker.dragging](https://developer.apple.com/documentation/appkit/nsrulermarker/1496253-isdragging)Added [NSRulerMarker.image](https://developer.apple.com/documentation/appkit/nsrulermarker/1496251-image)Added [NSRulerMarker.imageOrigin](https://developer.apple.com/documentation/appkit/nsrulermarker/1496236-imageorigin)Added [NSRulerMarker.imageRectInRuler](https://developer.apple.com/documentation/appkit/nsrulermarker/1496249-imagerectinruler)Added [NSRulerMarker.markerLocation](https://developer.apple.com/documentation/appkit/nsrulermarker/1496255-markerlocation)Added [NSRulerMarker.movable](https://developer.apple.com/documentation/appkit/nsrulermarker/1496247-movable)Added [NSRulerMarker.removable](https://developer.apple.com/documentation/appkit/nsrulermarker/1496238-isremovable)Added [NSRulerMarker.representedObject](https://developer.apple.com/documentation/appkit/nsrulermarker/1496244-representedobject)Added [NSRulerMarker.ruler](https://developer.apple.com/documentation/appkit/nsrulermarker/1496239-ruler)Added [NSRulerMarker.thicknessRequiredInRuler](https://developer.apple.com/documentation/appkit/nsrulermarker/1496245-thicknessrequiredinruler)Modified [-[NSRulerMarker initWithRulerView:markerLocation:image:imageOrigin:]](https://developer.apple.com/documentation/appkit/nsrulermarker/1496240-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithRulerView:(NSRulerView *)ruler markerLocation:(CGFloat)location image:(NSImage *)image imageOrigin:(NSPoint)imageOrigin ``` |
| To | ``` - (instancetype)initWithRulerView:(NSRulerView *)ruler markerLocation:(CGFloat)location image:(NSImage *)image imageOrigin:(NSPoint)imageOrigin ``` |

NSRulerView.hRemoved [-[NSRulerView accessoryView]](https://developer.apple.com/documentation/appkit/nsrulerview/1532804-accessoryview)Removed [-[NSRulerView baselineLocation]](https://developer.apple.com/documentation/appkit/nsrulerview/1534886-baselinelocation)Removed [-[NSRulerView clientView]](https://developer.apple.com/documentation/appkit/nsrulerview/1533483-clientview)Removed [-[NSRulerView isFlipped]](https://developer.apple.com/documentation/appkit/nsrulerview/1526302-isflipped)Removed [-[NSRulerView markers]](https://developer.apple.com/documentation/appkit/nsrulerview/1535213-markers)Removed [-[NSRulerView measurementUnits]](https://developer.apple.com/documentation/appkit/nsrulerview/1531493-measurementunits)Removed [-[NSRulerView orientation]](https://developer.apple.com/documentation/appkit/nsrulerview/1530596-orientation)Removed [-[NSRulerView originOffset]](https://developer.apple.com/documentation/appkit/nsrulerview/1535432-originoffset)Removed [-[NSRulerView requiredThickness]](https://developer.apple.com/documentation/appkit/nsrulerview/1526479-requiredthickness)Removed [-[NSRulerView reservedThicknessForAccessoryView]](https://developer.apple.com/documentation/appkit/nsrulerview/1530160-reservedthicknessforaccessoryvie)Removed [-[NSRulerView reservedThicknessForMarkers]](https://developer.apple.com/documentation/appkit/nsrulerview/1535112-reservedthicknessformarkers)Removed [-[NSRulerView ruleThickness]](https://developer.apple.com/documentation/appkit/nsrulerview/1527872-rulethickness)Removed [-[NSRulerView scrollView]](https://developer.apple.com/documentation/appkit/nsrulerview/1533741-scrollview)Removed [-[NSRulerView setAccessoryView:]](https://developer.apple.com/documentation/appkit/nsrulerview/1532804-accessoryview)Removed [-[NSRulerView setClientView:]](https://developer.apple.com/documentation/appkit/nsrulerview/1533483-clientview)Removed [-[NSRulerView setMarkers:]](https://developer.apple.com/documentation/appkit/nsrulerview/1535213-markers)Removed [-[NSRulerView setMeasurementUnits:]](https://developer.apple.com/documentation/appkit/nsrulerview/1531493-measurementunits)Removed [-[NSRulerView setOrientation:]](https://developer.apple.com/documentation/appkit/nsrulerview/1530596-orientation)Removed [-[NSRulerView setOriginOffset:]](https://developer.apple.com/documentation/appkit/nsrulerview/1535432-originoffset)Removed [-[NSRulerView setReservedThicknessForAccessoryView:]](https://developer.apple.com/documentation/appkit/nsrulerview/1530160-reservedthicknessforaccessoryvie)Removed [-[NSRulerView setReservedThicknessForMarkers:]](https://developer.apple.com/documentation/appkit/nsrulerview/1535112-reservedthicknessformarkers)Removed [-[NSRulerView setRuleThickness:]](https://developer.apple.com/documentation/appkit/nsrulerview/1527872-rulethickness)Removed [-[NSRulerView setScrollView:]](https://developer.apple.com/documentation/appkit/nsrulerview/1533741-scrollview)Added [NSRulerView.accessoryView](https://developer.apple.com/documentation/appkit/nsrulerview/1532804-accessoryview)Added [NSRulerView.baselineLocation](https://developer.apple.com/documentation/appkit/nsrulerview/1534886-baselinelocation)Added [NSRulerView.clientView](https://developer.apple.com/documentation/appkit/nsrulerview/1533483-clientview)Added [NSRulerView.flipped](https://developer.apple.com/documentation/appkit/nsrulerview/1526302-flipped)Added [NSRulerView.markers](https://developer.apple.com/documentation/appkit/nsrulerview/1535213-markers)Added [NSRulerView.measurementUnits](https://developer.apple.com/documentation/appkit/nsrulerview/1531493-measurementunits)Added [NSRulerView.orientation](https://developer.apple.com/documentation/appkit/nsrulerview/1530596-orientation)Added [NSRulerView.originOffset](https://developer.apple.com/documentation/appkit/nsrulerview/1535432-originoffset)Added [NSRulerView.requiredThickness](https://developer.apple.com/documentation/appkit/nsrulerview/1526479-requiredthickness)Added [NSRulerView.reservedThicknessForAccessoryView](https://developer.apple.com/documentation/appkit/nsrulerview/1530160-reservedthicknessforaccessoryvie)Added [NSRulerView.reservedThicknessForMarkers](https://developer.apple.com/documentation/appkit/nsrulerview/1535112-reservedthicknessformarkers)Added [NSRulerView.ruleThickness](https://developer.apple.com/documentation/appkit/nsrulerview/1527872-rulethickness)Added [NSRulerView.scrollView](https://developer.apple.com/documentation/appkit/nsrulerview/1533741-scrollview)Modified [-[NSRulerView initWithScrollView:orientation:]](https://developer.apple.com/documentation/appkit/nsrulerview/1535316-initwithscrollview)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithScrollView:(NSScrollView *)scrollView orientation:(NSRulerOrientation)orientation ``` |
| To | ``` - (instancetype)initWithScrollView:(NSScrollView *)scrollView orientation:(NSRulerOrientation)orientation ``` |

NSRunningApplication.hRemoved [-[NSWorkspace runningApplications]](https://developer.apple.com/documentation/appkit/nsworkspace/1534059-runningapplications)Added [NSWorkspace.runningApplications](https://developer.apple.com/documentation/appkit/nsworkspace/1534059-runningapplications)Modified [NSRunningApplication.bundleIdentifier](https://developer.apple.com/documentation/appkit/nsrunningapplication/1529140-bundleidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *bundleIdentifier ``` |
| To | ``` @property(readonly, copy) NSString *bundleIdentifier ``` |

Modified [NSRunningApplication.bundleURL](https://developer.apple.com/documentation/appkit/nsrunningapplication/1535500-bundleurl)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSURL *bundleURL ``` |
| To | ``` @property(readonly, copy) NSURL *bundleURL ``` |

Modified [+[NSRunningApplication currentApplication]](https://developer.apple.com/documentation/appkit/nsrunningapplication/1533604-current)

|  | Declaration |
| --- | --- |
| From | ``` + (NSRunningApplication *)currentApplication ``` |
| To | ``` + (instancetype)currentApplication ``` |

Modified [NSRunningApplication.executableURL](https://developer.apple.com/documentation/appkit/nsrunningapplication/1531062-executableurl)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSURL *executableURL ``` |
| To | ``` @property(readonly, copy) NSURL *executableURL ``` |

Modified [NSRunningApplication.icon](https://developer.apple.com/documentation/appkit/nsrunningapplication/1529885-icon)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSImage *icon ``` |
| To | ``` @property(readonly, strong) NSImage *icon ``` |

Modified [NSRunningApplication.launchDate](https://developer.apple.com/documentation/appkit/nsrunningapplication/1532595-launchdate)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSDate *launchDate ``` |
| To | ``` @property(readonly, copy) NSDate *launchDate ``` |

Modified [NSRunningApplication.localizedName](https://developer.apple.com/documentation/appkit/nsrunningapplication/1526751-localizedname)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *localizedName ``` |
| To | ``` @property(readonly, copy) NSString *localizedName ``` |

Modified [+[NSRunningApplication runningApplicationWithProcessIdentifier:]](https://developer.apple.com/documentation/appkit/nsrunningapplication/1530730-init)

|  | Declaration |
| --- | --- |
| From | ``` + (NSRunningApplication *)runningApplicationWithProcessIdentifier:(pid_t)pid ``` |
| To | ``` + (instancetype)runningApplicationWithProcessIdentifier:(pid_t)pid ``` |

NSSavePanel.hRemoved [-[NSSavePanel URL]](https://developer.apple.com/documentation/appkit/nssavepanel/1534384-url)Removed [-[NSSavePanel accessoryView]](https://developer.apple.com/documentation/appkit/nssavepanel/1525544-accessoryview)Removed [-[NSSavePanel allowedFileTypes]](https://developer.apple.com/documentation/appkit/nssavepanel/1534419-allowedfiletypes)Removed [-[NSSavePanel allowsOtherFileTypes]](https://developer.apple.com/documentation/appkit/nssavepanel/1526960-allowsotherfiletypes)Removed [-[NSSavePanel canCreateDirectories]](https://developer.apple.com/documentation/appkit/nssavepanel/1532626-cancreatedirectories)Removed [-[NSSavePanel canSelectHiddenExtension]](https://developer.apple.com/documentation/appkit/nssavepanel/1535360-canselecthiddenextension)Removed [-[NSSavePanel delegate]](https://developer.apple.com/documentation/appkit/nssavepanel/1532570-delegate)Removed [-[NSSavePanel directoryURL]](https://developer.apple.com/documentation/appkit/nssavepanel/1531279-directoryurl)Removed [-[NSSavePanel isExpanded]](https://developer.apple.com/documentation/appkit/nssavepanel/1534515-expanded)Removed [-[NSSavePanel isExtensionHidden]](https://developer.apple.com/documentation/appkit/nssavepanel/1529267-extensionhidden)Removed [-[NSSavePanel message]](https://developer.apple.com/documentation/appkit/nssavepanel/1528581-message)Removed [-[NSSavePanel nameFieldLabel]](https://developer.apple.com/documentation/appkit/nssavepanel/1535411-namefieldlabel)Removed [-[NSSavePanel nameFieldStringValue]](https://developer.apple.com/documentation/appkit/nssavepanel/1529299-namefieldstringvalue)Removed [-[NSSavePanel prompt]](https://developer.apple.com/documentation/appkit/nssavepanel/1525227-prompt)Removed [-[NSSavePanel setAccessoryView:]](https://developer.apple.com/documentation/appkit/nssavepanel/1525544-accessoryview)Removed [-[NSSavePanel setAllowedFileTypes:]](https://developer.apple.com/documentation/appkit/nssavepanel/1534419-allowedfiletypes)Removed [-[NSSavePanel setAllowsOtherFileTypes:]](https://developer.apple.com/documentation/appkit/nssavepanel/1526960-allowsotherfiletypes)Removed [-[NSSavePanel setCanCreateDirectories:]](https://developer.apple.com/documentation/appkit/nssavepanel/1532626-cancreatedirectories)Removed [-[NSSavePanel setCanSelectHiddenExtension:]](https://developer.apple.com/documentation/appkit/nssavepanel/1535360-canselecthiddenextension)Removed [-[NSSavePanel setDelegate:]](https://developer.apple.com/documentation/appkit/nssavepanel/1532570-delegate)Removed [-[NSSavePanel setDirectoryURL:]](https://developer.apple.com/documentation/appkit/nssavepanel/1531279-directoryurl)Removed [-[NSSavePanel setExtensionHidden:]](https://developer.apple.com/documentation/appkit/nssavepanel/1529267-extensionhidden)Removed [-[NSSavePanel setMessage:]](https://developer.apple.com/documentation/appkit/nssavepanel/1528581-message)Removed [-[NSSavePanel setNameFieldLabel:]](https://developer.apple.com/documentation/appkit/nssavepanel/1535411-namefieldlabel)Removed [-[NSSavePanel setNameFieldStringValue:]](https://developer.apple.com/documentation/appkit/nssavepanel/1529299-namefieldstringvalue)Removed [-[NSSavePanel setPrompt:]](https://developer.apple.com/documentation/appkit/nssavepanel/1525227-prompt)Removed [-[NSSavePanel setShowsHiddenFiles:]](https://developer.apple.com/documentation/appkit/nssavepanel/1524285-showshiddenfiles)Removed [-[NSSavePanel setShowsTagField:]](https://developer.apple.com/documentation/appkit/nssavepanel/1525589-showstagfield)Removed [-[NSSavePanel setTagNames:]](https://developer.apple.com/documentation/appkit/nssavepanel/1535928-tagnames)Removed [-[NSSavePanel setTitle:]](https://developer.apple.com/documentation/appkit/nssavepanel/1535071-title)Removed [-[NSSavePanel setTreatsFilePackagesAsDirectories:]](https://developer.apple.com/documentation/appkit/nssavepanel/1529384-treatsfilepackagesasdirectories)Removed [-[NSSavePanel showsHiddenFiles]](https://developer.apple.com/documentation/appkit/nssavepanel/1524285-showshiddenfiles)Removed [-[NSSavePanel showsTagField]](https://developer.apple.com/documentation/appkit/nssavepanel/1525589-showstagfield)Removed [-[NSSavePanel tagNames]](https://developer.apple.com/documentation/appkit/nssavepanel/1535928-tagnames)Removed [-[NSSavePanel title]](https://developer.apple.com/documentation/appkit/nssavepanel/1535071-title)Removed [-[NSSavePanel treatsFilePackagesAsDirectories]](https://developer.apple.com/documentation/appkit/nssavepanel/1529384-treatsfilepackagesasdirectories)Added [NSSavePanel.URL](https://developer.apple.com/documentation/appkit/nssavepanel/1534384-url)Added [NSSavePanel.accessoryView](https://developer.apple.com/documentation/appkit/nssavepanel/1525544-accessoryview)Added [NSSavePanel.allowedFileTypes](https://developer.apple.com/documentation/appkit/nssavepanel/1534419-allowedfiletypes)Added [NSSavePanel.allowsOtherFileTypes](https://developer.apple.com/documentation/appkit/nssavepanel/1526960-allowsotherfiletypes)Added [NSSavePanel.canCreateDirectories](https://developer.apple.com/documentation/appkit/nssavepanel/1532626-cancreatedirectories)Added [NSSavePanel.canSelectHiddenExtension](https://developer.apple.com/documentation/appkit/nssavepanel/1535360-canselecthiddenextension)Added [NSSavePanel.delegate](https://developer.apple.com/documentation/appkit/nssavepanel/1532570-delegate)Added [NSSavePanel.directoryURL](https://developer.apple.com/documentation/appkit/nssavepanel/1531279-directoryurl)Added [NSSavePanel.expanded](https://developer.apple.com/documentation/appkit/nssavepanel/1534515-isexpanded)Added [NSSavePanel.extensionHidden](https://developer.apple.com/documentation/appkit/nssavepanel/1529267-extensionhidden)Added [NSSavePanel.message](https://developer.apple.com/documentation/appkit/nssavepanel/1528581-message)Added [NSSavePanel.nameFieldLabel](https://developer.apple.com/documentation/appkit/nssavepanel/1535411-namefieldlabel)Added [NSSavePanel.nameFieldStringValue](https://developer.apple.com/documentation/appkit/nssavepanel/1529299-namefieldstringvalue)Added [NSSavePanel.prompt](https://developer.apple.com/documentation/appkit/nssavepanel/1525227-prompt)Added [NSSavePanel.showsHiddenFiles](https://developer.apple.com/documentation/appkit/nssavepanel/1524285-showshiddenfiles)Added [NSSavePanel.showsTagField](https://developer.apple.com/documentation/appkit/nssavepanel/1525589-showstagfield)Added [NSSavePanel.tagNames](https://developer.apple.com/documentation/appkit/nssavepanel/1535928-tagnames)Added [NSSavePanel.title](https://developer.apple.com/documentation/appkit/nssavepanel/1535071-title)Added [NSSavePanel.treatsFilePackagesAsDirectories](https://developer.apple.com/documentation/appkit/nssavepanel/1529384-treatsfilepackagesasdirectories)Modified [-[NSOpenSavePanelDelegate panel:didChangeToDirectoryURL:]](https://developer.apple.com/documentation/appkit/nsopensavepaneldelegate/1527117-panel)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOpenSavePanelDelegate panel:shouldEnableURL:]](https://developer.apple.com/documentation/appkit/nsopensavepaneldelegate/1535200-panel)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOpenSavePanelDelegate panel:userEnteredFilename:confirmed:]](https://developer.apple.com/documentation/appkit/nsopensavepaneldelegate/1524630-panel)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOpenSavePanelDelegate panel:validateURL:error:]](https://developer.apple.com/documentation/appkit/nsopensavepaneldelegate/1535141-panel)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOpenSavePanelDelegate panel:willExpand:]](https://developer.apple.com/documentation/appkit/nsopensavepaneldelegate/1532953-panel)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOpenSavePanelDelegate panelSelectionDidChange:]](https://developer.apple.com/documentation/appkit/nsopensavepaneldelegate/1533556-panelselectiondidchange)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSavePanel cancel:]](https://developer.apple.com/documentation/appkit/nssavepanel/1534357-cancel)

|  | Declaration |
| --- | --- |
| From | ``` - (void)cancel:(id)sender ``` |
| To | ``` - (IBAction)cancel:(id)sender ``` |

Modified [-[NSSavePanel ok:]](https://developer.apple.com/documentation/appkit/nssavepanel/1535364-ok)

|  | Declaration |
| --- | --- |
| From | ``` - (void)ok:(id)sender ``` |
| To | ``` - (IBAction)ok:(id)sender ``` |

Modified [-[NSSavePanel selectText:]](https://developer.apple.com/documentation/appkit/nssavepanel/1539012-selecttext)

|  | Declaration |
| --- | --- |
| From | ``` - (void)selectText:(id)sender ``` |
| To | ``` - (IBAction)selectText:(id)sender ``` |

NSScreen.hRemoved [-[NSScreen backingScaleFactor]](https://developer.apple.com/documentation/appkit/nsscreen/1388385-backingscalefactor)Removed [-[NSScreen colorSpace]](https://developer.apple.com/documentation/appkit/nsscreen/1388383-colorspace)Removed [-[NSScreen depth]](https://developer.apple.com/documentation/appkit/nsscreen/1388373-depth)Removed [-[NSScreen deviceDescription]](https://developer.apple.com/documentation/appkit/nsscreen/1388360-devicedescription)Removed [-[NSScreen frame]](https://developer.apple.com/documentation/appkit/nsscreen/1388387-frame)Removed [-[NSScreen supportedWindowDepths]](https://developer.apple.com/documentation/appkit/nsscreen/1388391-supportedwindowdepths)Removed [-[NSScreen visibleFrame]](https://developer.apple.com/documentation/appkit/nsscreen/1388369-visibleframe)Added [NSScreen.backingScaleFactor](https://developer.apple.com/documentation/appkit/nsscreen/1388385-backingscalefactor)Added [NSScreen.colorSpace](https://developer.apple.com/documentation/appkit/nsscreen/1388383-colorspace)Added [NSScreen.depth](https://developer.apple.com/documentation/appkit/nsscreen/1388373-depth)Added [NSScreen.deviceDescription](https://developer.apple.com/documentation/appkit/nsscreen/1388360-devicedescription)Added [NSScreen.frame](https://developer.apple.com/documentation/appkit/nsscreen/1388387-frame)Added [NSScreen.supportedWindowDepths](https://developer.apple.com/documentation/appkit/nsscreen/1388391-supportedwindowdepths)Added [NSScreen.visibleFrame](https://developer.apple.com/documentation/appkit/nsscreen/1388369-visibleframe)NSScrollView.hRemoved [-[NSScrollView autohidesScrollers]](https://developer.apple.com/documentation/appkit/nsscrollview/1403536-autohidesscrollers)Removed [-[NSScrollView backgroundColor]](https://developer.apple.com/documentation/appkit/nsscrollview/1403473-backgroundcolor)Removed [-[NSScrollView borderType]](https://developer.apple.com/documentation/appkit/nsscrollview/1403528-bordertype)Removed [-[NSScrollView contentSize]](https://developer.apple.com/documentation/appkit/nsscrollview/1403458-contentsize)Removed [-[NSScrollView contentView]](https://developer.apple.com/documentation/appkit/nsscrollview/1403547-contentview)Removed [-[NSScrollView documentCursor]](https://developer.apple.com/documentation/appkit/nsscrollview/1403446-documentcursor)Removed [-[NSScrollView documentView]](https://developer.apple.com/documentation/appkit/nsscrollview/1403485-documentview)Removed [-[NSScrollView documentVisibleRect]](https://developer.apple.com/documentation/appkit/nsscrollview/1403466-documentvisiblerect)Removed [-[NSScrollView drawsBackground]](https://developer.apple.com/documentation/appkit/nsscrollview/1403474-drawsbackground)Removed [-[NSScrollView findBarPosition]](https://developer.apple.com/documentation/appkit/nsscrollview/1403501-findbarposition)Removed [-[NSScrollView hasHorizontalRuler]](https://developer.apple.com/documentation/appkit/nsscrollview/1403457-hashorizontalruler)Removed [-[NSScrollView hasHorizontalScroller]](https://developer.apple.com/documentation/appkit/nsscrollview/1403530-hashorizontalscroller)Removed [-[NSScrollView hasVerticalRuler]](https://developer.apple.com/documentation/appkit/nsscrollview/1403496-hasverticalruler)Removed [-[NSScrollView hasVerticalScroller]](https://developer.apple.com/documentation/appkit/nsscrollview/1403491-hasverticalscroller)Removed [-[NSScrollView horizontalLineScroll]](https://developer.apple.com/documentation/appkit/nsscrollview/1403539-horizontallinescroll)Removed [-[NSScrollView horizontalPageScroll]](https://developer.apple.com/documentation/appkit/nsscrollview/1403478-horizontalpagescroll)Removed [-[NSScrollView horizontalRulerView]](https://developer.apple.com/documentation/appkit/nsscrollview/1403498-horizontalrulerview)Removed [-[NSScrollView horizontalScrollElasticity]](https://developer.apple.com/documentation/appkit/nsscrollview/1403540-horizontalscrollelasticity)Removed [-[NSScrollView horizontalScroller]](https://developer.apple.com/documentation/appkit/nsscrollview/1403447-horizontalscroller)Removed [-[NSScrollView lineScroll]](https://developer.apple.com/documentation/appkit/nsscrollview/1403454-linescroll)Removed [-[NSScrollView pageScroll]](https://developer.apple.com/documentation/appkit/nsscrollview/1403449-pagescroll)Removed [-[NSScrollView rulersVisible]](https://developer.apple.com/documentation/appkit/nsscrollview/1403445-rulersvisible)Removed [-[NSScrollView scrollerKnobStyle]](https://developer.apple.com/documentation/appkit/nsscrollview/1403544-scrollerknobstyle)Removed [-[NSScrollView scrollerStyle]](https://developer.apple.com/documentation/appkit/nsscrollview/1403520-scrollerstyle)Removed [-[NSScrollView scrollsDynamically]](https://developer.apple.com/documentation/appkit/nsscrollview/1403519-scrollsdynamically)Removed [-[NSScrollView setAutohidesScrollers:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403536-autohidesscrollers)Removed [-[NSScrollView setBackgroundColor:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403473-backgroundcolor)Removed [-[NSScrollView setBorderType:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403528-bordertype)Removed [-[NSScrollView setContentView:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403547-contentview)Removed [-[NSScrollView setDocumentCursor:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403446-documentcursor)Removed [-[NSScrollView setDocumentView:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403485-documentview)Removed [-[NSScrollView setDrawsBackground:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403474-drawsbackground)Removed [-[NSScrollView setFindBarPosition:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403501-findbarposition)Removed [-[NSScrollView setHasHorizontalRuler:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403457-hashorizontalruler)Removed [-[NSScrollView setHasHorizontalScroller:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403530-hashorizontalscroller)Removed [-[NSScrollView setHasVerticalRuler:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403496-hasverticalruler)Removed [-[NSScrollView setHasVerticalScroller:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403491-hasverticalscroller)Removed [-[NSScrollView setHorizontalLineScroll:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403539-horizontallinescroll)Removed [-[NSScrollView setHorizontalPageScroll:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403478-horizontalpagescroll)Removed [-[NSScrollView setHorizontalRulerView:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403498-horizontalrulerview)Removed [-[NSScrollView setHorizontalScrollElasticity:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403540-horizontalscrollelasticity)Removed [-[NSScrollView setHorizontalScroller:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403447-horizontalscroller)Removed [-[NSScrollView setLineScroll:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403454-linescroll)Removed [-[NSScrollView setPageScroll:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403449-pagescroll)Removed [-[NSScrollView setRulersVisible:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403445-rulersvisible)Removed [-[NSScrollView setScrollerKnobStyle:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403544-scrollerknobstyle)Removed [-[NSScrollView setScrollerStyle:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403520-scrollerstyle)Removed [-[NSScrollView setScrollsDynamically:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403519-scrollsdynamically)Removed [-[NSScrollView setUsesPredominantAxisScrolling:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403489-usespredominantaxisscrolling)Removed [-[NSScrollView setVerticalLineScroll:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403490-verticallinescroll)Removed [-[NSScrollView setVerticalPageScroll:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403512-verticalpagescroll)Removed [-[NSScrollView setVerticalRulerView:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403507-verticalrulerview)Removed [-[NSScrollView setVerticalScrollElasticity:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403475-verticalscrollelasticity)Removed [-[NSScrollView setVerticalScroller:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403526-verticalscroller)Removed [-[NSScrollView usesPredominantAxisScrolling]](https://developer.apple.com/documentation/appkit/nsscrollview/1403489-usespredominantaxisscrolling)Removed [-[NSScrollView verticalLineScroll]](https://developer.apple.com/documentation/appkit/nsscrollview/1403490-verticallinescroll)Removed [-[NSScrollView verticalPageScroll]](https://developer.apple.com/documentation/appkit/nsscrollview/1403512-verticalpagescroll)Removed [-[NSScrollView verticalRulerView]](https://developer.apple.com/documentation/appkit/nsscrollview/1403507-verticalrulerview)Removed [-[NSScrollView verticalScrollElasticity]](https://developer.apple.com/documentation/appkit/nsscrollview/1403475-verticalscrollelasticity)Removed [-[NSScrollView verticalScroller]](https://developer.apple.com/documentation/appkit/nsscrollview/1403526-verticalscroller)Added [NSScrollView.autohidesScrollers](https://developer.apple.com/documentation/appkit/nsscrollview/1403536-autohidesscrollers)Added [NSScrollView.automaticallyAdjustsContentInsets](https://developer.apple.com/documentation/appkit/nsscrollview/1403502-automaticallyadjustscontentinset)Added [NSScrollView.backgroundColor](https://developer.apple.com/documentation/appkit/nsscrollview/1403473-backgroundcolor)Added [NSScrollView.borderType](https://developer.apple.com/documentation/appkit/nsscrollview/1403528-bordertype)Added [NSScrollView.contentInsets](https://developer.apple.com/documentation/appkit/nsscrollview/1403461-contentinsets)Added [NSScrollView.contentSize](https://developer.apple.com/documentation/appkit/nsscrollview/1403458-contentsize)Added [NSScrollView.contentView](https://developer.apple.com/documentation/appkit/nsscrollview/1403547-contentview)Added [NSScrollView.documentCursor](https://developer.apple.com/documentation/appkit/nsscrollview/1403446-documentcursor)Added [NSScrollView.documentView](https://developer.apple.com/documentation/appkit/nsscrollview/1403485-documentview)Added [NSScrollView.documentVisibleRect](https://developer.apple.com/documentation/appkit/nsscrollview/1403466-documentvisiblerect)Added [NSScrollView.drawsBackground](https://developer.apple.com/documentation/appkit/nsscrollview/1403474-drawsbackground)Added [NSScrollView.findBarPosition](https://developer.apple.com/documentation/appkit/nsscrollview/1403501-findbarposition)Added [NSScrollView.hasHorizontalRuler](https://developer.apple.com/documentation/appkit/nsscrollview/1403457-hashorizontalruler)Added [NSScrollView.hasHorizontalScroller](https://developer.apple.com/documentation/appkit/nsscrollview/1403530-hashorizontalscroller)Added [NSScrollView.hasVerticalRuler](https://developer.apple.com/documentation/appkit/nsscrollview/1403496-hasverticalruler)Added [NSScrollView.hasVerticalScroller](https://developer.apple.com/documentation/appkit/nsscrollview/1403491-hasverticalscroller)Added [NSScrollView.horizontalLineScroll](https://developer.apple.com/documentation/appkit/nsscrollview/1403539-horizontallinescroll)Added [NSScrollView.horizontalPageScroll](https://developer.apple.com/documentation/appkit/nsscrollview/1403478-horizontalpagescroll)Added [NSScrollView.horizontalRulerView](https://developer.apple.com/documentation/appkit/nsscrollview/1403498-horizontalrulerview)Added [NSScrollView.horizontalScrollElasticity](https://developer.apple.com/documentation/appkit/nsscrollview/1403540-horizontalscrollelasticity)Added [NSScrollView.horizontalScroller](https://developer.apple.com/documentation/appkit/nsscrollview/1403447-horizontalscroller)Added [-[NSScrollView initWithCoder:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403527-initwithcoder)Added [-[NSScrollView initWithFrame:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403450-init)Added [NSScrollView.lineScroll](https://developer.apple.com/documentation/appkit/nsscrollview/1403454-linescroll)Added [NSScrollView.pageScroll](https://developer.apple.com/documentation/appkit/nsscrollview/1403449-pagescroll)Added [NSScrollView.rulersVisible](https://developer.apple.com/documentation/appkit/nsscrollview/1403445-rulersvisible)Added [NSScrollView.scrollerInsets](https://developer.apple.com/documentation/appkit/nsscrollview/1403529-scrollerinsets)Added [NSScrollView.scrollerKnobStyle](https://developer.apple.com/documentation/appkit/nsscrollview/1403544-scrollerknobstyle)Added [NSScrollView.scrollerStyle](https://developer.apple.com/documentation/appkit/nsscrollview/1403520-scrollerstyle)Added [NSScrollView.scrollsDynamically](https://developer.apple.com/documentation/appkit/nsscrollview/1403519-scrollsdynamically)Added [NSScrollView.usesPredominantAxisScrolling](https://developer.apple.com/documentation/appkit/nsscrollview/1403489-usespredominantaxisscrolling)Added [NSScrollView.verticalLineScroll](https://developer.apple.com/documentation/appkit/nsscrollview/1403490-verticallinescroll)Added [NSScrollView.verticalPageScroll](https://developer.apple.com/documentation/appkit/nsscrollview/1403512-verticalpagescroll)Added [NSScrollView.verticalRulerView](https://developer.apple.com/documentation/appkit/nsscrollview/1403507-verticalrulerview)Added [NSScrollView.verticalScrollElasticity](https://developer.apple.com/documentation/appkit/nsscrollview/1403475-verticalscrollelasticity)Added [NSScrollView.verticalScroller](https://developer.apple.com/documentation/appkit/nsscrollview/1403526-verticalscroller)Modified [+[NSScrollView contentSizeForFrameSize:hasHorizontalScroller:hasVerticalScroller:borderType:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403481-contentsizeforframesize)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified [+[NSScrollView frameSizeForContentSize:hasHorizontalScroller:hasVerticalScroller:borderType:]](https://developer.apple.com/documentation/appkit/nsscrollview/1403469-framesizeforcontentsize)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

NSScroller.hRemoved [-[NSScroller arrowsPosition]](https://developer.apple.com/documentation/appkit/nsscroller/1523676-arrowsposition)Removed [-[NSScroller controlSize]](https://developer.apple.com/documentation/appkit/nsscroller/1523659-controlsize)Removed [-[NSScroller controlTint]](https://developer.apple.com/documentation/appkit/nsscroller/1523672-controltint)Removed [-[NSScroller hitPart]](https://developer.apple.com/documentation/appkit/nsscroller/1523596-hitpart)Removed [-[NSScroller knobProportion]](https://developer.apple.com/documentation/appkit/nsscroller/1523626-setknobproportion)Removed [-[NSScroller knobStyle]](https://developer.apple.com/documentation/appkit/nsscroller/1523666-knobstyle)Removed [-[NSScroller scrollerStyle]](https://developer.apple.com/documentation/appkit/nsscroller/1523591-scrollerstyle)Removed [-[NSScroller setArrowsPosition:]](https://developer.apple.com/documentation/appkit/nsscroller/1523676-arrowsposition)Removed [-[NSScroller setControlSize:]](https://developer.apple.com/documentation/appkit/nsscroller/1523659-controlsize)Removed [-[NSScroller setControlTint:]](https://developer.apple.com/documentation/appkit/nsscroller/1523672-controltint)Removed [-[NSScroller setKnobStyle:]](https://developer.apple.com/documentation/appkit/nsscroller/1523666-knobstyle)Removed [-[NSScroller setScrollerStyle:]](https://developer.apple.com/documentation/appkit/nsscroller/1523591-scrollerstyle)Removed [-[NSScroller usableParts]](https://developer.apple.com/documentation/appkit/nsscroller/1523648-usableparts)Added [NSScroller.arrowsPosition](https://developer.apple.com/documentation/appkit/nsscroller/1523676-arrowsposition)Added [NSScroller.controlSize](https://developer.apple.com/documentation/appkit/nsscroller/1523659-controlsize)Added [NSScroller.controlTint](https://developer.apple.com/documentation/appkit/nsscroller/1523672-controltint)Added [NSScroller.hitPart](https://developer.apple.com/documentation/appkit/nsscroller/1523596-hitpart)Added [NSScroller.knobProportion](https://developer.apple.com/documentation/appkit/nsscroller/1523593-knobproportion)Added [NSScroller.knobStyle](https://developer.apple.com/documentation/appkit/nsscroller/1523666-knobstyle)Added [NSScroller.scrollerStyle](https://developer.apple.com/documentation/appkit/nsscroller/1523591-scrollerstyle)Added [NSScroller.usableParts](https://developer.apple.com/documentation/appkit/nsscroller/1523648-usableparts)Modified [+[NSScroller scrollerWidth]](https://developer.apple.com/documentation/appkit/nsscroller/1523613-scrollerwidth)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified [+[NSScroller scrollerWidthForControlSize:]](https://developer.apple.com/documentation/appkit/nsscroller/1523615-scrollerwidthforcontrolsize)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

NSSearchField.hRemoved [-[NSSearchField recentSearches]](https://developer.apple.com/documentation/appkit/nssearchfield/1531413-recentsearches)Removed [-[NSSearchField recentsAutosaveName]](https://developer.apple.com/documentation/appkit/nssearchfield/1530035-recentsautosavename)Removed [-[NSSearchField setRecentSearches:]](https://developer.apple.com/documentation/appkit/nssearchfield/1531413-recentsearches)Removed [-[NSSearchField setRecentsAutosaveName:]](https://developer.apple.com/documentation/appkit/nssearchfield/1530035-recentsautosavename)Added [NSSearchField.maximumRecents](https://developer.apple.com/documentation/appkit/nssearchfield/1533938-maximumrecents)Added [NSSearchField.recentSearches](https://developer.apple.com/documentation/appkit/nssearchfield/1531413-recentsearches)Added [NSSearchField.recentsAutosaveName](https://developer.apple.com/documentation/appkit/nssearchfield/1530035-recentsautosavename)Added [NSSearchField.searchMenuTemplate](https://developer.apple.com/documentation/appkit/nssearchfield/1529467-searchmenutemplate)Added [NSSearchField.sendsSearchStringImmediately](https://developer.apple.com/documentation/appkit/nssearchfield/1529081-sendssearchstringimmediately)Added [NSSearchField.sendsWholeSearchString](https://developer.apple.com/documentation/appkit/nssearchfield/1533976-sendswholesearchstring)NSSearchFieldCell.hRemoved [-[NSSearchFieldCell cancelButtonCell]](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399440-cancelbuttoncell)Removed [-[NSSearchFieldCell maximumRecents]](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399468-maximumrecents)Removed [-[NSSearchFieldCell recentSearches]](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399446-recentsearches)Removed [-[NSSearchFieldCell recentsAutosaveName]](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399463-recentsautosavename)Removed [-[NSSearchFieldCell searchButtonCell]](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399457-searchbuttoncell)Removed [-[NSSearchFieldCell searchMenuTemplate]](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399452-searchmenutemplate)Removed [-[NSSearchFieldCell sendsSearchStringImmediately]](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399444-sendssearchstringimmediately)Removed [-[NSSearchFieldCell sendsWholeSearchString]](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399453-sendswholesearchstring)Removed [-[NSSearchFieldCell setCancelButtonCell:]](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399440-cancelbuttoncell)Removed [-[NSSearchFieldCell setMaximumRecents:]](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399468-maximumrecents)Removed [-[NSSearchFieldCell setRecentSearches:]](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399446-recentsearches)Removed [-[NSSearchFieldCell setRecentsAutosaveName:]](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399463-recentsautosavename)Removed [-[NSSearchFieldCell setSearchButtonCell:]](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399457-searchbuttoncell)Removed [-[NSSearchFieldCell setSearchMenuTemplate:]](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399452-searchmenutemplate)Removed [-[NSSearchFieldCell setSendsSearchStringImmediately:]](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399444-sendssearchstringimmediately)Removed [-[NSSearchFieldCell setSendsWholeSearchString:]](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399453-sendswholesearchstring)Added [NSSearchFieldCell.cancelButtonCell](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399440-cancelbuttoncell)Added [NSSearchFieldCell.maximumRecents](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399468-maximumrecents)Added [NSSearchFieldCell.recentSearches](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399446-recentsearches)Added [NSSearchFieldCell.recentsAutosaveName](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399463-recentsautosavename)Added [NSSearchFieldCell.searchButtonCell](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399457-searchbuttoncell)Added [NSSearchFieldCell.searchMenuTemplate](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399452-searchmenutemplate)Added [NSSearchFieldCell.sendsSearchStringImmediately](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399444-sendssearchstringimmediately)Added [NSSearchFieldCell.sendsWholeSearchString](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399453-sendswholesearchstring)NSSecureTextField.hRemoved [-[NSSecureTextFieldCell echosBullets]](https://developer.apple.com/documentation/appkit/nssecuretextfieldcell/1395984-echosbullets)Removed [-[NSSecureTextFieldCell setEchosBullets:]](https://developer.apple.com/documentation/appkit/nssecuretextfieldcell/1395984-echosbullets)Added [NSSecureTextFieldCell.echosBullets](https://developer.apple.com/documentation/appkit/nssecuretextfieldcell/1395984-echosbullets)NSSegmentedCell.hRemoved [-[NSSegmentedCell segmentCount]](https://developer.apple.com/documentation/appkit/nssegmentedcell/1500185-segmentcount)Removed [-[NSSegmentedCell segmentStyle]](https://developer.apple.com/documentation/appkit/nssegmentedcell/1500172-segmentstyle)Removed [-[NSSegmentedCell selectedSegment]](https://developer.apple.com/documentation/appkit/nssegmentedcell/1500193-selectedsegment)Removed [-[NSSegmentedCell setSegmentCount:]](https://developer.apple.com/documentation/appkit/nssegmentedcell/1500185-segmentcount)Removed [-[NSSegmentedCell setSegmentStyle:]](https://developer.apple.com/documentation/appkit/nssegmentedcell/1500172-segmentstyle)Removed [-[NSSegmentedCell setSelectedSegment:]](https://developer.apple.com/documentation/appkit/nssegmentedcell/1500193-selectedsegment)Removed [-[NSSegmentedCell setTrackingMode:]](https://developer.apple.com/documentation/appkit/nssegmentedcell/1500200-trackingmode)Removed [-[NSSegmentedCell trackingMode]](https://developer.apple.com/documentation/appkit/nssegmentedcell/1500200-trackingmode)Added [NSSegmentedCell.segmentCount](https://developer.apple.com/documentation/appkit/nssegmentedcell/1500185-segmentcount)Added [NSSegmentedCell.segmentStyle](https://developer.apple.com/documentation/appkit/nssegmentedcell/1500172-segmentstyle)Added [NSSegmentedCell.selectedSegment](https://developer.apple.com/documentation/appkit/nssegmentedcell/1500193-selectedsegment)Added [NSSegmentedCell.trackingMode](https://developer.apple.com/documentation/appkit/nssegmentedcell/1500200-trackingmode)NSSegmentedControl.hRemoved [-[NSSegmentedControl segmentCount]](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/1527451-segmentcount)Removed [-[NSSegmentedControl segmentStyle]](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/1528507-segmentstyle)Removed [-[NSSegmentedControl selectedSegment]](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/1534490-selectedsegment)Removed [-[NSSegmentedControl setSegmentCount:]](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/1527451-segmentcount)Removed [-[NSSegmentedControl setSegmentStyle:]](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/1528507-segmentstyle)Removed [-[NSSegmentedControl setSelectedSegment:]](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/1534490-selectedsegment)Added [NSSegmentedControl.segmentCount](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/1527451-segmentcount)Added [NSSegmentedControl.segmentStyle](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/1528507-segmentstyle)Added [NSSegmentedControl.selectedSegment](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/1534490-selectedsegment)Added [NSSegmentStyleSeparated](https://developer.apple.com/documentation/appkit/nssegmentstyle/nssegmentstyleseparated)NSShadow.hRemoved [-[NSShadow setShadowBlurRadius:]](https://developer.apple.com/documentation/appkit/nsshadow/1429846-shadowblurradius)Removed [-[NSShadow setShadowColor:]](https://developer.apple.com/documentation/appkit/nsshadow/1429855-shadowcolor)Removed [-[NSShadow setShadowOffset:]](https://developer.apple.com/documentation/appkit/nsshadow/1429851-shadowoffset)Removed [-[NSShadow shadowBlurRadius]](https://developer.apple.com/documentation/uikit/nsshadow/1429846-shadowblurradius)Removed [-[NSShadow shadowColor]](https://developer.apple.com/documentation/appkit/nsshadow/1429855-shadowcolor)Removed [-[NSShadow shadowOffset]](https://developer.apple.com/documentation/appkit/nsshadow/1429851-shadowoffset)Added [NSShadow.shadowBlurRadius](https://developer.apple.com/documentation/uikit/nsshadow/1429846-shadowblurradius)Added [NSShadow.shadowColor](https://developer.apple.com/documentation/uikit/nsshadow/1429855-shadowcolor)Added [NSShadow.shadowOffset](https://developer.apple.com/documentation/appkit/nsshadow/1429851-shadowoffset)Modified [-[NSShadow init]](https://developer.apple.com/documentation/appkit/nsshadow/1429853-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

NSSharingService.hModified [NSSharingService.alternateImage](https://developer.apple.com/documentation/appkit/nssharingservice/1402650-alternateimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) NSImage *alternateImage ``` |
| To | ``` @property(readonly, strong) NSImage *alternateImage ``` |

Modified [NSSharingService.image](https://developer.apple.com/documentation/appkit/nssharingservice/1402654-image)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) NSImage *image ``` |
| To | ``` @property(readonly, strong) NSImage *image ``` |

Modified [-[NSSharingService initWithTitle:image:alternateImage:handler:]](https://developer.apple.com/documentation/appkit/nssharingservice/1402614-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTitle:(NSString *)title image:(NSImage *)image alternateImage:(NSImage *)alternateImage handler:(void (^)(void))block ``` |
| To | ``` - (instancetype)initWithTitle:(NSString *)title image:(NSImage *)image alternateImage:(NSImage *)alternateImage handler:(void (^)(void))block ``` |

Modified [-[NSSharingServiceDelegate sharingService:didFailToShareItems:error:]](https://developer.apple.com/documentation/appkit/nssharingservicedelegate/1402710-sharingservice)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSharingServiceDelegate sharingService:didShareItems:]](https://developer.apple.com/documentation/appkit/nssharingservicedelegate/1402638-sharingservice)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSharingServiceDelegate sharingService:sourceFrameOnScreenForShareItem:]](https://developer.apple.com/documentation/appkit/nssharingservicedelegate/1402695-sharingservice)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSharingServiceDelegate sharingService:sourceWindowForShareItems:sharingContentScope:]](https://developer.apple.com/documentation/appkit/nssharingservicedelegate/1402679-sharingservice)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSharingServiceDelegate sharingService:transitionImageForShareItem:contentRect:]](https://developer.apple.com/documentation/appkit/nssharingservicedelegate/1402622-sharingservice)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSharingServiceDelegate sharingService:willShareItems:]](https://developer.apple.com/documentation/appkit/nssharingservicedelegate/1402642-sharingservice)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSharingServicePicker initWithItems:]](https://developer.apple.com/documentation/appkit/nssharingservicepicker/1402691-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithItems:(NSArray *)items ``` |
| To | ``` - (instancetype)initWithItems:(NSArray *)items ``` |

Modified [-[NSSharingServicePickerDelegate sharingServicePicker:delegateForSharingService:]](https://developer.apple.com/documentation/appkit/nssharingservicepickerdelegate/1402608-sharingservicepicker)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSharingServicePickerDelegate sharingServicePicker:didChooseSharingService:]](https://developer.apple.com/documentation/appkit/nssharingservicepickerdelegate/1402610-sharingservicepicker)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSharingServicePickerDelegate sharingServicePicker:sharingServicesForItems:proposedSharingServices:]](https://developer.apple.com/documentation/appkit/nssharingservicepickerdelegate/1402664-sharingservicepicker)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSSlider.hRemoved [-[NSSlider allowsTickMarkValuesOnly]](https://developer.apple.com/documentation/appkit/nsslider/1526898-allowstickmarkvaluesonly)Removed [-[NSSlider altIncrementValue]](https://developer.apple.com/documentation/appkit/nsslider/1532901-altincrementvalue)Removed [-[NSSlider isVertical]](https://developer.apple.com/documentation/appkit/nsslider/1527901-isvertical)Removed [-[NSSlider knobThickness]](https://developer.apple.com/documentation/appkit/nsslider/1532909-knobthickness)Removed [-[NSSlider maxValue]](https://developer.apple.com/documentation/appkit/nsslider/1532919-maxvalue)Removed [-[NSSlider minValue]](https://developer.apple.com/documentation/appkit/nsslider/1524665-minvalue)Removed [-[NSSlider numberOfTickMarks]](https://developer.apple.com/documentation/appkit/nsslider/1524268-numberoftickmarks)Removed [-[NSSlider setAllowsTickMarkValuesOnly:]](https://developer.apple.com/documentation/appkit/nsslider/1526898-allowstickmarkvaluesonly)Removed [-[NSSlider setAltIncrementValue:]](https://developer.apple.com/documentation/appkit/nsslider/1532901-altincrementvalue)Removed [-[NSSlider setMaxValue:]](https://developer.apple.com/documentation/appkit/nsslider/1532919-maxvalue)Removed [-[NSSlider setMinValue:]](https://developer.apple.com/documentation/appkit/nsslider/1524665-minvalue)Removed [-[NSSlider setNumberOfTickMarks:]](https://developer.apple.com/documentation/appkit/nsslider/1524268-numberoftickmarks)Removed [-[NSSlider setTickMarkPosition:]](https://developer.apple.com/documentation/appkit/nsslider/1529657-tickmarkposition)Removed [-[NSSlider tickMarkPosition]](https://developer.apple.com/documentation/appkit/nsslider/1529657-tickmarkposition)Added [NSSlider.allowsTickMarkValuesOnly](https://developer.apple.com/documentation/appkit/nsslider/1526898-allowstickmarkvaluesonly)Added [NSSlider.altIncrementValue](https://developer.apple.com/documentation/appkit/nsslider/1532901-altincrementvalue)Added [NSSlider.knobThickness](https://developer.apple.com/documentation/appkit/nsslider/1532909-knobthickness)Added [NSSlider.maxValue](https://developer.apple.com/documentation/appkit/nsslider/1532919-maxvalue)Added [NSSlider.minValue](https://developer.apple.com/documentation/appkit/nsslider/1524665-minvalue)Added [NSSlider.numberOfTickMarks](https://developer.apple.com/documentation/appkit/nsslider/1524268-numberoftickmarks)Added [NSSlider.sliderType](https://developer.apple.com/documentation/appkit/nsslider/1532924-slidertype)Added [NSSlider.tickMarkPosition](https://developer.apple.com/documentation/appkit/nsslider/1529657-tickmarkposition)Added [NSSlider.vertical](https://developer.apple.com/documentation/appkit/nsslider/1527901-vertical)Modified [NSSlider](https://developer.apple.com/documentation/appkit/nsslider)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSAccessibilitySlider |

NSSliderCell.hRemoved [-[NSSliderCell allowsTickMarkValuesOnly]](https://developer.apple.com/documentation/appkit/nsslidercell/1444604-allowstickmarkvaluesonly)Removed [-[NSSliderCell altIncrementValue]](https://developer.apple.com/documentation/appkit/nsslidercell/1444596-altincrementvalue)Removed -[NSSliderCell isVertical]Removed [-[NSSliderCell knobThickness]](https://developer.apple.com/documentation/appkit/nsslidercell/1444593-knobthickness)Removed [-[NSSliderCell maxValue]](https://developer.apple.com/documentation/appkit/nsslidercell/1444589-maxvalue)Removed [-[NSSliderCell minValue]](https://developer.apple.com/documentation/appkit/nsslidercell/1444641-minvalue)Removed [-[NSSliderCell numberOfTickMarks]](https://developer.apple.com/documentation/appkit/nsslidercell/1444621-numberoftickmarks)Removed [-[NSSliderCell setAllowsTickMarkValuesOnly:]](https://developer.apple.com/documentation/appkit/nsslidercell/1444604-allowstickmarkvaluesonly)Removed [-[NSSliderCell setAltIncrementValue:]](https://developer.apple.com/documentation/appkit/nsslidercell/1444596-altincrementvalue)Removed [-[NSSliderCell setMaxValue:]](https://developer.apple.com/documentation/appkit/nsslidercell/1444589-maxvalue)Removed [-[NSSliderCell setMinValue:]](https://developer.apple.com/documentation/appkit/nsslidercell/1444641-minvalue)Removed [-[NSSliderCell setNumberOfTickMarks:]](https://developer.apple.com/documentation/appkit/nsslidercell/1444621-numberoftickmarks)Removed [-[NSSliderCell setSliderType:]](https://developer.apple.com/documentation/appkit/nsslidercell/1444598-slidertype)Removed [-[NSSliderCell setTickMarkPosition:]](https://developer.apple.com/documentation/appkit/nsslidercell/1444616-tickmarkposition)Removed [-[NSSliderCell sliderType]](https://developer.apple.com/documentation/appkit/nsslidercell/1444598-slidertype)Removed [-[NSSliderCell tickMarkPosition]](https://developer.apple.com/documentation/appkit/nsslidercell/1444616-tickmarkposition)Removed [-[NSSliderCell trackRect]](https://developer.apple.com/documentation/appkit/nsslidercell/1444583-trackrect)Added [NSSliderCell.allowsTickMarkValuesOnly](https://developer.apple.com/documentation/appkit/nsslidercell/1444604-allowstickmarkvaluesonly)Added [NSSliderCell.altIncrementValue](https://developer.apple.com/documentation/appkit/nsslidercell/1444596-altincrementvalue)Added [NSSliderCell.knobThickness](https://developer.apple.com/documentation/appkit/nsslidercell/1444593-knobthickness)Added [NSSliderCell.maxValue](https://developer.apple.com/documentation/appkit/nsslidercell/1444589-maxvalue)Added [NSSliderCell.minValue](https://developer.apple.com/documentation/appkit/nsslidercell/1444641-minvalue)Added [NSSliderCell.numberOfTickMarks](https://developer.apple.com/documentation/appkit/nsslidercell/1444621-numberoftickmarks)Added [NSSliderCell.sliderType](https://developer.apple.com/documentation/appkit/nsslidercell/1444598-slidertype)Added [NSSliderCell.tickMarkPosition](https://developer.apple.com/documentation/appkit/nsslidercell/1444616-tickmarkposition)Added [NSSliderCell.trackRect](https://developer.apple.com/documentation/appkit/nsslidercell/1444583-trackrect)Added [NSSliderCell.vertical](https://developer.apple.com/documentation/appkit/nsslidercell/1444602-isvertical)NSSound.hRemoved [-[NSSound currentTime]](https://developer.apple.com/documentation/appkit/nssound/1477320-currenttime)Removed [-[NSSound delegate]](https://developer.apple.com/documentation/appkit/nssound/1477300-delegate)Removed [-[NSSound duration]](https://developer.apple.com/documentation/appkit/nssound/1477313-duration)Removed [-[NSSound isPlaying]](https://developer.apple.com/documentation/appkit/nssound/1477302-playing)Removed [-[NSSound loops]](https://developer.apple.com/documentation/appkit/nssound/1477311-loops)Removed [-[NSSound name]](https://developer.apple.com/documentation/appkit/nssound/1477296-name)Removed [-[NSSound playbackDeviceIdentifier]](https://developer.apple.com/documentation/appkit/nssound/1477284-playbackdeviceidentifier)Removed [-[NSSound setCurrentTime:]](https://developer.apple.com/documentation/appkit/nssound/1477320-currenttime)Removed [-[NSSound setDelegate:]](https://developer.apple.com/documentation/appkit/nssound/1477300-delegate)Removed [-[NSSound setLoops:]](https://developer.apple.com/documentation/appkit/nssound/1477311-loops)Removed [-[NSSound setPlaybackDeviceIdentifier:]](https://developer.apple.com/documentation/appkit/nssound/1477284-playbackdeviceidentifier)Removed [-[NSSound setVolume:]](https://developer.apple.com/documentation/appkit/nssound/1477315-volume)Removed [-[NSSound volume]](https://developer.apple.com/documentation/appkit/nssound/1477315-volume)Added [NSSound.currentTime](https://developer.apple.com/documentation/appkit/nssound/1477320-currenttime)Added [NSSound.delegate](https://developer.apple.com/documentation/appkit/nssound/1477300-delegate)Added [NSSound.duration](https://developer.apple.com/documentation/appkit/nssound/1477313-duration)Added [NSSound.loops](https://developer.apple.com/documentation/appkit/nssound/1477311-loops)Added [NSSound.name](https://developer.apple.com/documentation/appkit/nssound/1477296-name)Added [NSSound.playbackDeviceIdentifier](https://developer.apple.com/documentation/appkit/nssound/1477284-playbackdeviceidentifier)Added [NSSound.playing](https://developer.apple.com/documentation/appkit/nssound/1477302-playing)Added [NSSound.volume](https://developer.apple.com/documentation/appkit/nssound/1477315-volume)Modified [-[NSSound initWithContentsOfFile:byReference:]](https://developer.apple.com/documentation/appkit/nssound/1477274-initwithcontentsoffile)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfFile:(NSString *)path byReference:(BOOL)byRef ``` |
| To | ``` - (instancetype)initWithContentsOfFile:(NSString *)path byReference:(BOOL)byRef ``` |

Modified [-[NSSound initWithContentsOfURL:byReference:]](https://developer.apple.com/documentation/appkit/nssound/1477288-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)url byReference:(BOOL)byRef ``` |
| To | ``` - (instancetype)initWithContentsOfURL:(NSURL *)url byReference:(BOOL)byRef ``` |

Modified [-[NSSound initWithData:]](https://developer.apple.com/documentation/appkit/nssound/1477292-initwithdata)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(NSData *)data ``` |
| To | ``` - (instancetype)initWithData:(NSData *)data ``` |

Modified [-[NSSound initWithPasteboard:]](https://developer.apple.com/documentation/appkit/nssound/1477294-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithPasteboard:(NSPasteboard *)pasteboard ``` |
| To | ``` - (instancetype)initWithPasteboard:(NSPasteboard *)pasteboard ``` |

Modified [+[NSSound soundNamed:]](https://developer.apple.com/documentation/appkit/nssound/1477318-soundnamed)

|  | Declaration |
| --- | --- |
| From | ``` + (id)soundNamed:(NSString *)name ``` |
| To | ``` + (NSSound *)soundNamed:(NSString *)name ``` |

Modified [-[NSSoundDelegate sound:didFinishPlaying:]](https://developer.apple.com/documentation/appkit/nssounddelegate/1477298-sound)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSSpeechRecognizer.hRemoved [-[NSSpeechRecognizer blocksOtherRecognizers]](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/1533022-blocksotherrecognizers)Removed [-[NSSpeechRecognizer commands]](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/1529757-commands)Removed [-[NSSpeechRecognizer delegate]](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/1528171-delegate)Removed [-[NSSpeechRecognizer displayedCommandsTitle]](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/1530622-displayedcommandstitle)Removed [-[NSSpeechRecognizer listensInForegroundOnly]](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/1533405-listensinforegroundonly)Removed [-[NSSpeechRecognizer setBlocksOtherRecognizers:]](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/1533022-blocksotherrecognizers)Removed [-[NSSpeechRecognizer setCommands:]](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/1529757-commands)Removed [-[NSSpeechRecognizer setDelegate:]](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/1528171-delegate)Removed [-[NSSpeechRecognizer setDisplayedCommandsTitle:]](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/1530622-displayedcommandstitle)Removed [-[NSSpeechRecognizer setListensInForegroundOnly:]](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/1533405-listensinforegroundonly)Added [NSSpeechRecognizer.blocksOtherRecognizers](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/1533022-blocksotherrecognizers)Added [NSSpeechRecognizer.commands](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/1529757-commands)Added [NSSpeechRecognizer.delegate](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/1528171-delegate)Added [NSSpeechRecognizer.displayedCommandsTitle](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/1530622-displayedcommandstitle)Added [NSSpeechRecognizer.listensInForegroundOnly](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/1533405-listensinforegroundonly)Modified [-[NSSpeechRecognizer init]](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/1527990-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

Modified [-[NSSpeechRecognizerDelegate speechRecognizer:didRecognizeCommand:]](https://developer.apple.com/documentation/appkit/nsspeechrecognizerdelegate/1534211-speechrecognizer)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSSpeechSynthesizer.hRemoved [-[NSSpeechSynthesizer delegate]](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/1448460-delegate)Removed -[NSSpeechSynthesizer isSpeaking]Removed [-[NSSpeechSynthesizer rate]](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/1448450-rate)Removed [-[NSSpeechSynthesizer setDelegate:]](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/1448460-delegate)Removed [-[NSSpeechSynthesizer setRate:]](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/1448450-rate)Removed [-[NSSpeechSynthesizer setUsesFeedbackWindow:]](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/1448488-usesfeedbackwindow)Removed [-[NSSpeechSynthesizer setVolume:]](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/1448501-volume)Removed [-[NSSpeechSynthesizer usesFeedbackWindow]](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/1448488-usesfeedbackwindow)Removed [-[NSSpeechSynthesizer volume]](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/1448501-volume)Added [NSSpeechSynthesizer.delegate](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/1448460-delegate)Added [NSSpeechSynthesizer.rate](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/1448450-rate)Added [NSSpeechSynthesizer.speaking](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/1448511-speaking)Added [NSSpeechSynthesizer.usesFeedbackWindow](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/1448488-usesfeedbackwindow)Added [NSSpeechSynthesizer.volume](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/1448501-volume)Modified [-[NSSpeechSynthesizer initWithVoice:]](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/1448381-initwithvoice)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithVoice:(NSString *)voice ``` |
| To | ``` - (instancetype)initWithVoice:(NSString *)voice ``` |

Modified [-[NSSpeechSynthesizerDelegate speechSynthesizer:didEncounterErrorAtIndex:ofString:message:]](https://developer.apple.com/documentation/appkit/nsspeechsynthesizerdelegate/1448407-speechsynthesizer)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSpeechSynthesizerDelegate speechSynthesizer:didEncounterSyncMessage:]](https://developer.apple.com/documentation/appkit/nsspeechsynthesizerdelegate/1448540-speechsynthesizer)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSpeechSynthesizerDelegate speechSynthesizer:didFinishSpeaking:]](https://developer.apple.com/documentation/appkit/nsspeechsynthesizerdelegate/1448538-speechsynthesizer)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSpeechSynthesizerDelegate speechSynthesizer:willSpeakPhoneme:]](https://developer.apple.com/documentation/appkit/nsspeechsynthesizerdelegate/1448442-speechsynthesizer)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSpeechSynthesizerDelegate speechSynthesizer:willSpeakWord:ofString:]](https://developer.apple.com/documentation/appkit/nsspeechsynthesizerdelegate/1448480-speechsynthesizer)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSSpellChecker.hRemoved [-[NSSpellChecker accessoryView]](https://developer.apple.com/documentation/appkit/nsspellchecker/1528160-accessoryview)Removed [-[NSSpellChecker automaticallyIdentifiesLanguages]](https://developer.apple.com/documentation/appkit/nsspellchecker/1534335-automaticallyidentifieslanguages)Removed [-[NSSpellChecker availableLanguages]](https://developer.apple.com/documentation/appkit/nsspellchecker/1530496-availablelanguages)Removed [-[NSSpellChecker setAccessoryView:]](https://developer.apple.com/documentation/appkit/nsspellchecker/1528160-accessoryview)Removed [-[NSSpellChecker setAutomaticallyIdentifiesLanguages:]](https://developer.apple.com/documentation/appkit/nsspellchecker/1534335-automaticallyidentifieslanguages)Removed [-[NSSpellChecker setSubstitutionsPanelAccessoryViewController:]](https://developer.apple.com/documentation/appkit/nsspellchecker/1531645-substitutionspanelaccessoryviewc)Removed [-[NSSpellChecker spellingPanel]](https://developer.apple.com/documentation/appkit/nsspellchecker/1532806-spellingpanel)Removed [-[NSSpellChecker substitutionsPanel]](https://developer.apple.com/documentation/appkit/nsspellchecker/1534172-substitutionspanel)Removed [-[NSSpellChecker substitutionsPanelAccessoryViewController]](https://developer.apple.com/documentation/appkit/nsspellchecker/1531645-substitutionspanelaccessoryviewc)Removed [-[NSSpellChecker userPreferredLanguages]](https://developer.apple.com/documentation/appkit/nsspellchecker/1525173-userpreferredlanguages)Removed [-[NSSpellChecker userReplacementsDictionary]](https://developer.apple.com/documentation/appkit/nsspellchecker/1524925-userreplacementsdictionary)Added [NSSpellChecker.accessoryView](https://developer.apple.com/documentation/appkit/nsspellchecker/1528160-accessoryview)Added [NSSpellChecker.automaticallyIdentifiesLanguages](https://developer.apple.com/documentation/appkit/nsspellchecker/1534335-automaticallyidentifieslanguages)Added [NSSpellChecker.availableLanguages](https://developer.apple.com/documentation/appkit/nsspellchecker/1530496-availablelanguages)Added [NSSpellChecker.spellingPanel](https://developer.apple.com/documentation/appkit/nsspellchecker/1532806-spellingpanel)Added [NSSpellChecker.substitutionsPanel](https://developer.apple.com/documentation/appkit/nsspellchecker/1534172-substitutionspanel)Added [NSSpellChecker.substitutionsPanelAccessoryViewController](https://developer.apple.com/documentation/appkit/nsspellchecker/1531645-substitutionspanelaccessoryviewc)Added [NSSpellChecker.userPreferredLanguages](https://developer.apple.com/documentation/appkit/nsspellchecker/1525173-userpreferredlanguages)Added [NSSpellChecker.userReplacementsDictionary](https://developer.apple.com/documentation/appkit/nsspellchecker/1524925-userreplacementsdictionary)NSSplitView.hRemoved [-[NSSplitView autosaveName]](https://developer.apple.com/documentation/appkit/nssplitview/1455319-autosavename)Removed [-[NSSplitView delegate]](https://developer.apple.com/documentation/appkit/nssplitview/1455306-delegate)Removed [-[NSSplitView dividerColor]](https://developer.apple.com/documentation/appkit/nssplitview/1455267-dividercolor)Removed [-[NSSplitView dividerStyle]](https://developer.apple.com/documentation/appkit/nssplitview/1455291-dividerstyle)Removed [-[NSSplitView dividerThickness]](https://developer.apple.com/documentation/appkit/nssplitview/1455257-dividerthickness)Removed -[NSSplitView isVertical]Removed [-[NSSplitView setAutosaveName:]](https://developer.apple.com/documentation/appkit/nssplitview/1455319-autosavename)Removed [-[NSSplitView setDelegate:]](https://developer.apple.com/documentation/appkit/nssplitview/1455306-delegate)Removed [-[NSSplitView setDividerStyle:]](https://developer.apple.com/documentation/appkit/nssplitview/1455291-dividerstyle)Removed [-[NSSplitView setVertical:]](https://developer.apple.com/documentation/appkit/nssplitview/1455318-isvertical)Added [NSSplitView.autosaveName](https://developer.apple.com/documentation/appkit/nssplitview/1455319-autosavename)Added [NSSplitView.delegate](https://developer.apple.com/documentation/appkit/nssplitview/1455306-delegate)Added [NSSplitView.dividerColor](https://developer.apple.com/documentation/appkit/nssplitview/1455267-dividercolor)Added [NSSplitView.dividerStyle](https://developer.apple.com/documentation/appkit/nssplitview/1455291-dividerstyle)Added [NSSplitView.dividerThickness](https://developer.apple.com/documentation/appkit/nssplitview/1455257-dividerthickness)Added [NSSplitView.vertical](https://developer.apple.com/documentation/appkit/nssplitview/1455318-vertical)Modified [-[NSSplitViewDelegate splitView:additionalEffectiveRectOfDividerAtIndex:]](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/1455292-splitview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSplitViewDelegate splitView:canCollapseSubview:]](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/1455304-splitview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSplitViewDelegate splitView:constrainMaxCoordinate:ofSubviewAt:]](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/1455300-splitview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSplitViewDelegate splitView:constrainMinCoordinate:ofSubviewAt:]](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/1455302-splitview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSplitViewDelegate splitView:constrainSplitPosition:ofSubviewAt:]](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/1455312-splitview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSplitViewDelegate splitView:effectiveRect:forDrawnRect:ofDividerAtIndex:]](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/1455288-splitview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSplitViewDelegate splitView:resizeSubviewsWithOldSize:]](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/1455273-splitview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSplitViewDelegate splitView:shouldAdjustSizeOfSubview:]](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/1455269-splitview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSplitViewDelegate splitView:shouldCollapseSubview:forDoubleClickOnDividerAtIndex:]](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/1455263-splitview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSplitViewDelegate splitView:shouldHideDividerAtIndex:]](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/1455280-splitview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSplitViewDelegate splitViewDidResizeSubviews:]](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/1455314-splitviewdidresizesubviews)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSplitViewDelegate splitViewWillResizeSubviews:]](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/1455289-splitviewwillresizesubviews)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSSplitViewController.h (Added)Added [NSSplitViewController](https://developer.apple.com/documentation/appkit/nssplitviewcontroller)Added [-[NSSplitViewController addSplitViewItem:]](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/1388928-addsplitviewitem)Added [-[NSSplitViewController insertSplitViewItem:atIndex:]](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/1388886-insertsplitviewitem)Added [-[NSSplitViewController removeSplitViewItem:]](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/1388903-removesplitviewitem)Added [NSSplitViewController.splitView](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/1388907-splitview)Added [-[NSSplitViewController splitView:additionalEffectiveRectOfDividerAtIndex:]](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/1388922-splitview)Added [-[NSSplitViewController splitView:canCollapseSubview:]](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/1388861-splitview)Added [-[NSSplitViewController splitView:effectiveRect:forDrawnRect:ofDividerAtIndex:]](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/1388897-splitview)Added [-[NSSplitViewController splitView:shouldCollapseSubview:forDoubleClickOnDividerAtIndex:]](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/1388909-splitview)Added [-[NSSplitViewController splitView:shouldHideDividerAtIndex:]](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/1388882-splitview)Added [-[NSSplitViewController splitViewItemForViewController:]](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/1388857-splitviewitem)Added [NSSplitViewController.splitViewItems](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/1388876-splitviewitems)Added [-[NSSplitViewController viewDidLoad]](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/1388874-viewdidload)Added [NSSplitViewItem](https://developer.apple.com/documentation/appkit/nssplitviewitem)Added [NSSplitViewItem.canCollapse](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388926-cancollapse)Added [NSSplitViewItem.collapsed](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388891-collapsed)Added [NSSplitViewItem.holdingPriority](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388887-holdingpriority)Added [+[NSSplitViewItem splitViewItemWithViewController:]](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388918-splitviewitemwithviewcontroller)Added [NSSplitViewItem.viewController](https://developer.apple.com/documentation/appkit/nssplitviewitem/1388911-viewcontroller)NSStackView.hRemoved [#def NSStackViewSpacingUseDefault](https://developer.apple.com/documentation/appkit/nsstackview/nsstackviewspacingusedefault/nsstackviewspacingusedefault)Removed [NSStackViewVisibilityPriorityDetachOnlyIfNecessary](https://developer.apple.com/documentation/appkit/nsstackviewvisibilitypriority/nsstackviewvisibilityprioritydetachonlyifnecessary)Removed [NSStackViewVisibilityPriorityMustHold](https://developer.apple.com/documentation/appkit/nsstackviewvisibilitypriority/nsstackviewvisibilityprioritymusthold)Removed [NSStackViewVisibilityPriorityNotVisible](https://developer.apple.com/documentation/appkit/nsstackviewvisibilitypriority/nsstackviewvisibilityprioritynotvisible)Added [NSStackViewSpacingUseDefault](https://developer.apple.com/documentation/appkit/nsstackview/1488938-usedefaultspacing)Added [NSStackViewVisibilityPriorityDetachOnlyIfNecessary](https://developer.apple.com/documentation/appkit/nsstackview/visibilitypriority/1488918-detachonlyifnecessary)Added [NSStackViewVisibilityPriorityMustHold](https://developer.apple.com/documentation/appkit/nsstackviewvisibilityprioritymusthold)Added [NSStackViewVisibilityPriorityNotVisible](https://developer.apple.com/documentation/appkit/nsstackviewvisibilityprioritynotvisible)Modified [NSStackView.detachedViews](https://developer.apple.com/documentation/appkit/nsstackview/1488952-detachedviews)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *detachedViews ``` |
| To | ``` @property(readonly, copy) NSArray *detachedViews ``` |

Modified [+[NSStackView stackViewWithViews:]](https://developer.apple.com/documentation/appkit/nsstackview/1488929-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)stackViewWithViews:(NSArray *)views ``` |
| To | ``` + (instancetype)stackViewWithViews:(NSArray *)views ``` |

Modified [NSStackView.views](https://developer.apple.com/documentation/appkit/nsstackview/1488914-views)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *views ``` |
| To | ``` @property(readonly, copy) NSArray *views ``` |

Modified [-[NSStackViewDelegate stackView:didReattachViews:]](https://developer.apple.com/documentation/appkit/nsstackviewdelegate/1488921-stackview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSStackViewDelegate stackView:willDetachViews:]](https://developer.apple.com/documentation/appkit/nsstackviewdelegate/1488953-stackview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSStatusBar.hRemoved [-[NSStatusBar isVertical]](https://developer.apple.com/documentation/appkit/nsstatusbar/1530580-isvertical)Removed [-[NSStatusBar thickness]](https://developer.apple.com/documentation/appkit/nsstatusbar/1534591-thickness)Removed #def NSSquareStatusItemLengthRemoved #def NSVariableStatusItemLengthAdded [NSStatusBar.thickness](https://developer.apple.com/documentation/appkit/nsstatusbar/1534591-thickness)Added [NSStatusBar.vertical](https://developer.apple.com/documentation/appkit/nsstatusbar/1530580-vertical)Added [NSSquareStatusItemLength](https://developer.apple.com/documentation/appkit/nssquarestatusitemlength)Added [NSVariableStatusItemLength](https://developer.apple.com/documentation/appkit/nsvariablestatusitemlength)NSStatusBarButton.h (Added)Added [NSStatusBarButton](https://developer.apple.com/documentation/appkit/nsstatusbarbutton)Added [NSStatusBarButton.appearsDisabled](https://developer.apple.com/documentation/appkit/nsstatusbarbutton/1409292-appearsdisabled)NSStatusItem.hRemoved [-[NSStatusItem action]](https://developer.apple.com/documentation/appkit/nsstatusitem/1531580-action)Removed [-[NSStatusItem alternateImage]](https://developer.apple.com/documentation/appkit/nsstatusitem/1534014-alternateimage)Removed [-[NSStatusItem attributedTitle]](https://developer.apple.com/documentation/appkit/nsstatusitem/1534223-attributedtitle)Removed [-[NSStatusItem doubleAction]](https://developer.apple.com/documentation/appkit/nsstatusitem/1535555-doubleaction)Removed [-[NSStatusItem highlightMode]](https://developer.apple.com/documentation/appkit/nsstatusitem/1528609-highlightmode)Removed [-[NSStatusItem image]](https://developer.apple.com/documentation/appkit/nsstatusitem/1524711-image)Removed [-[NSStatusItem isEnabled]](https://developer.apple.com/documentation/appkit/nsstatusitem/1527352-enabled)Removed [-[NSStatusItem length]](https://developer.apple.com/documentation/appkit/nsstatusitem/1529402-length)Removed [-[NSStatusItem menu]](https://developer.apple.com/documentation/appkit/nsstatusitem/1535918-menu)Removed [-[NSStatusItem setAction:]](https://developer.apple.com/documentation/appkit/nsstatusitem/1531580-action)Removed [-[NSStatusItem setAlternateImage:]](https://developer.apple.com/documentation/appkit/nsstatusitem/1534014-alternateimage)Removed [-[NSStatusItem setAttributedTitle:]](https://developer.apple.com/documentation/appkit/nsstatusitem/1534223-attributedtitle)Removed [-[NSStatusItem setDoubleAction:]](https://developer.apple.com/documentation/appkit/nsstatusitem/1535555-doubleaction)Removed [-[NSStatusItem setEnabled:]](https://developer.apple.com/documentation/appkit/nsstatusitem/1527352-isenabled)Removed [-[NSStatusItem setHighlightMode:]](https://developer.apple.com/documentation/appkit/nsstatusitem/1528609-highlightmode)Removed [-[NSStatusItem setImage:]](https://developer.apple.com/documentation/appkit/nsstatusitem/1524711-image)Removed [-[NSStatusItem setLength:]](https://developer.apple.com/documentation/appkit/nsstatusitem/1529402-length)Removed [-[NSStatusItem setMenu:]](https://developer.apple.com/documentation/appkit/nsstatusitem/1535918-menu)Removed [-[NSStatusItem setTarget:]](https://developer.apple.com/documentation/appkit/nsstatusitem/1532686-target)Removed [-[NSStatusItem setTitle:]](https://developer.apple.com/documentation/appkit/nsstatusitem/1534494-title)Removed [-[NSStatusItem setToolTip:]](https://developer.apple.com/documentation/appkit/nsstatusitem/1534916-tooltip)Removed [-[NSStatusItem setView:]](https://developer.apple.com/documentation/appkit/nsstatusitem/1531522-view)Removed [-[NSStatusItem statusBar]](https://developer.apple.com/documentation/appkit/nsstatusitem/1525951-statusbar)Removed [-[NSStatusItem target]](https://developer.apple.com/documentation/appkit/nsstatusitem/1532686-target)Removed [-[NSStatusItem title]](https://developer.apple.com/documentation/appkit/nsstatusitem/1534494-title)Removed [-[NSStatusItem toolTip]](https://developer.apple.com/documentation/appkit/nsstatusitem/1534916-tooltip)Removed [-[NSStatusItem view]](https://developer.apple.com/documentation/appkit/nsstatusitem/1531522-view)Removed NSStatusItem(NSStatusItemCommon)Removed NSStatusItem(NSStatusItemView)Added [NSStatusItem.action](https://developer.apple.com/documentation/appkit/nsstatusitem/1531580-action)Added [NSStatusItem.alternateImage](https://developer.apple.com/documentation/appkit/nsstatusitem/1534014-alternateimage)Added [NSStatusItem.attributedTitle](https://developer.apple.com/documentation/appkit/nsstatusitem/1534223-attributedtitle)Added [NSStatusItem.button](https://developer.apple.com/documentation/appkit/nsstatusitem/1535056-button)Added [NSStatusItem.doubleAction](https://developer.apple.com/documentation/appkit/nsstatusitem/1535555-doubleaction)Added [NSStatusItem.enabled](https://developer.apple.com/documentation/appkit/nsstatusitem/1527352-enabled)Added [NSStatusItem.highlightMode](https://developer.apple.com/documentation/appkit/nsstatusitem/1528609-highlightmode)Added [NSStatusItem.image](https://developer.apple.com/documentation/appkit/nsstatusitem/1524711-image)Added [NSStatusItem.length](https://developer.apple.com/documentation/appkit/nsstatusitem/1529402-length)Added [NSStatusItem.menu](https://developer.apple.com/documentation/appkit/nsstatusitem/1535918-menu)Added [NSStatusItem.statusBar](https://developer.apple.com/documentation/appkit/nsstatusitem/1525951-statusbar)Added [NSStatusItem.target](https://developer.apple.com/documentation/appkit/nsstatusitem/1532686-target)Added [NSStatusItem.title](https://developer.apple.com/documentation/appkit/nsstatusitem/1534494-title)Added [NSStatusItem.toolTip](https://developer.apple.com/documentation/appkit/nsstatusitem/1534916-tooltip)Added [NSStatusItem.view](https://developer.apple.com/documentation/appkit/nsstatusitem/1531522-view)Added NSStatusItem(NSStatusItemDeprecated)Modified [-[NSStatusItem drawStatusBarBackgroundInRect:withHighlight:]](https://developer.apple.com/documentation/appkit/nsstatusitem/1532509-drawstatusbarbackgroundinrect)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSStatusItem popUpStatusItemMenu:]](https://developer.apple.com/documentation/appkit/nsstatusitem/1524256-popupmenu)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSStatusItem sendActionOn:]](https://developer.apple.com/documentation/appkit/nsstatusitem/1535025-sendaction)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

NSStepper.hRemoved [-[NSStepper autorepeat]](https://developer.apple.com/documentation/appkit/nsstepper/1523571-autorepeat)Removed [-[NSStepper increment]](https://developer.apple.com/documentation/appkit/nsstepper/1523573-increment)Removed [-[NSStepper maxValue]](https://developer.apple.com/documentation/appkit/nsstepper/1523578-maxvalue)Removed [-[NSStepper minValue]](https://developer.apple.com/documentation/appkit/nsstepper/1523569-minvalue)Removed [-[NSStepper setAutorepeat:]](https://developer.apple.com/documentation/appkit/nsstepper/1523571-autorepeat)Removed [-[NSStepper setIncrement:]](https://developer.apple.com/documentation/appkit/nsstepper/1523573-increment)Removed [-[NSStepper setMaxValue:]](https://developer.apple.com/documentation/appkit/nsstepper/1523578-maxvalue)Removed [-[NSStepper setMinValue:]](https://developer.apple.com/documentation/appkit/nsstepper/1523569-minvalue)Removed [-[NSStepper setValueWraps:]](https://developer.apple.com/documentation/appkit/nsstepper/1523580-valuewraps)Removed [-[NSStepper valueWraps]](https://developer.apple.com/documentation/appkit/nsstepper/1523580-valuewraps)Added [NSStepper.autorepeat](https://developer.apple.com/documentation/appkit/nsstepper/1523571-autorepeat)Added [NSStepper.increment](https://developer.apple.com/documentation/appkit/nsstepper/1523573-increment)Added [NSStepper.maxValue](https://developer.apple.com/documentation/appkit/nsstepper/1523578-maxvalue)Added [NSStepper.minValue](https://developer.apple.com/documentation/appkit/nsstepper/1523569-minvalue)Added [NSStepper.valueWraps](https://developer.apple.com/documentation/appkit/nsstepper/1523580-valuewraps)Modified [NSStepper](https://developer.apple.com/documentation/appkit/nsstepper)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSAccessibilityStepper |

NSStepperCell.hRemoved [-[NSStepperCell autorepeat]](https://developer.apple.com/documentation/appkit/nssteppercell/1392323-autorepeat)Removed [-[NSStepperCell increment]](https://developer.apple.com/documentation/appkit/nssteppercell/1392331-increment)Removed [-[NSStepperCell maxValue]](https://developer.apple.com/documentation/appkit/nssteppercell/1392321-maxvalue)Removed [-[NSStepperCell minValue]](https://developer.apple.com/documentation/appkit/nssteppercell/1392327-minvalue)Removed [-[NSStepperCell setAutorepeat:]](https://developer.apple.com/documentation/appkit/nssteppercell/1392323-autorepeat)Removed [-[NSStepperCell setIncrement:]](https://developer.apple.com/documentation/appkit/nssteppercell/1392331-increment)Removed [-[NSStepperCell setMaxValue:]](https://developer.apple.com/documentation/appkit/nssteppercell/1392321-maxvalue)Removed [-[NSStepperCell setMinValue:]](https://developer.apple.com/documentation/appkit/nssteppercell/1392327-minvalue)Removed [-[NSStepperCell setValueWraps:]](https://developer.apple.com/documentation/appkit/nssteppercell/1392325-valuewraps)Removed [-[NSStepperCell valueWraps]](https://developer.apple.com/documentation/appkit/nssteppercell/1392325-valuewraps)Added [NSStepperCell.autorepeat](https://developer.apple.com/documentation/appkit/nssteppercell/1392323-autorepeat)Added [NSStepperCell.increment](https://developer.apple.com/documentation/appkit/nssteppercell/1392331-increment)Added [NSStepperCell.maxValue](https://developer.apple.com/documentation/appkit/nssteppercell/1392321-maxvalue)Added [NSStepperCell.minValue](https://developer.apple.com/documentation/appkit/nssteppercell/1392327-minvalue)Added [NSStepperCell.valueWraps](https://developer.apple.com/documentation/appkit/nssteppercell/1392325-valuewraps)NSStoryboard.h (Added)Added [NSStoryboard](https://developer.apple.com/documentation/appkit/nsstoryboard)Added [-[NSStoryboard instantiateControllerWithIdentifier:]](https://developer.apple.com/documentation/appkit/nsstoryboard/1426549-instantiatecontroller)Added [-[NSStoryboard instantiateInitialController]](https://developer.apple.com/documentation/appkit/nsstoryboard/1426545-instantiateinitialcontroller)Added [+[NSStoryboard storyboardWithName:bundle:]](https://developer.apple.com/documentation/appkit/nsstoryboard/1426547-init)NSStoryboardSegue.h (Added)Added [NSSeguePerforming](https://developer.apple.com/documentation/appkit/nssegueperforming)Added [-[NSSeguePerforming performSegueWithIdentifier:sender:]](https://developer.apple.com/documentation/appkit/nssegueperforming/1409583-performseguewithidentifier)Added [-[NSSeguePerforming prepareForSegue:sender:]](https://developer.apple.com/documentation/appkit/nssegueperforming/1409580-prepare)Added [-[NSSeguePerforming shouldPerformSegueWithIdentifier:sender:]](https://developer.apple.com/documentation/appkit/nssegueperforming/1409574-shouldperformseguewithidentifier)Added [NSStoryboardSegue](https://developer.apple.com/documentation/appkit/nsstoryboardsegue)Added [NSStoryboardSegue.destinationController](https://developer.apple.com/documentation/appkit/nsstoryboardsegue/1409586-destinationcontroller)Added [NSStoryboardSegue.identifier](https://developer.apple.com/documentation/appkit/nsstoryboardsegue/1409578-identifier)Added [-[NSStoryboardSegue initWithIdentifier:source:destination:]](https://developer.apple.com/documentation/appkit/nsstoryboardsegue/1409572-init)Added [-[NSStoryboardSegue perform]](https://developer.apple.com/documentation/appkit/nsstoryboardsegue/1409587-perform)Added [+[NSStoryboardSegue segueWithIdentifier:source:destination:performHandler:]](https://developer.apple.com/documentation/appkit/nsstoryboardsegue/1409576-seguewithidentifier)Added [NSStoryboardSegue.sourceController](https://developer.apple.com/documentation/appkit/nsstoryboardsegue/1409582-sourcecontroller)NSStringDrawing.hRemoved [-[NSAttributedString size]](https://developer.apple.com/documentation/foundation/nsattributedstring/1528362-size)Added NSAttributedString.sizeNSTabView.hRemoved [-[NSTabView allowsTruncatedLabels]](https://developer.apple.com/documentation/appkit/nstabview/1391645-allowstruncatedlabels)Removed [-[NSTabView contentRect]](https://developer.apple.com/documentation/appkit/nstabview/1391659-contentrect)Removed [-[NSTabView controlSize]](https://developer.apple.com/documentation/appkit/nstabview/1391633-controlsize)Removed [-[NSTabView controlTint]](https://developer.apple.com/documentation/appkit/nstabview/1391647-controltint)Removed [-[NSTabView delegate]](https://developer.apple.com/documentation/appkit/nstabview/1391615-delegate)Removed [-[NSTabView drawsBackground]](https://developer.apple.com/documentation/appkit/nstabview/1391588-drawsbackground)Removed [-[NSTabView font]](https://developer.apple.com/documentation/appkit/nstabview/1391617-font)Removed [-[NSTabView minimumSize]](https://developer.apple.com/documentation/appkit/nstabview/1391598-minimumsize)Removed [-[NSTabView numberOfTabViewItems]](https://developer.apple.com/documentation/appkit/nstabview/1391596-numberoftabviewitems)Removed [-[NSTabView selectedTabViewItem]](https://developer.apple.com/documentation/appkit/nstabview/1391625-selectedtabviewitem)Removed [-[NSTabView setAllowsTruncatedLabels:]](https://developer.apple.com/documentation/appkit/nstabview/1391645-allowstruncatedlabels)Removed [-[NSTabView setControlSize:]](https://developer.apple.com/documentation/appkit/nstabview/1391633-controlsize)Removed [-[NSTabView setControlTint:]](https://developer.apple.com/documentation/appkit/nstabview/1391647-controltint)Removed [-[NSTabView setDelegate:]](https://developer.apple.com/documentation/appkit/nstabview/1391615-delegate)Removed [-[NSTabView setDrawsBackground:]](https://developer.apple.com/documentation/appkit/nstabview/1391588-drawsbackground)Removed [-[NSTabView setFont:]](https://developer.apple.com/documentation/appkit/nstabview/1391617-font)Removed [-[NSTabView setTabViewType:]](https://developer.apple.com/documentation/appkit/nstabview/1391602-tabviewtype)Removed [-[NSTabView tabViewItems]](https://developer.apple.com/documentation/appkit/nstabview/1391613-tabviewitems)Removed [-[NSTabView tabViewType]](https://developer.apple.com/documentation/appkit/nstabview/1391602-tabviewtype)Added [NSTabView.allowsTruncatedLabels](https://developer.apple.com/documentation/appkit/nstabview/1391645-allowstruncatedlabels)Added [NSTabView.contentRect](https://developer.apple.com/documentation/appkit/nstabview/1391659-contentrect)Added [NSTabView.controlSize](https://developer.apple.com/documentation/appkit/nstabview/1391633-controlsize)Added [NSTabView.controlTint](https://developer.apple.com/documentation/appkit/nstabview/1391647-controltint)Added [NSTabView.delegate](https://developer.apple.com/documentation/appkit/nstabview/1391615-delegate)Added [NSTabView.drawsBackground](https://developer.apple.com/documentation/appkit/nstabview/1391588-drawsbackground)Added [NSTabView.font](https://developer.apple.com/documentation/appkit/nstabview/1391617-font)Added [NSTabView.minimumSize](https://developer.apple.com/documentation/appkit/nstabview/1391598-minimumsize)Added [NSTabView.numberOfTabViewItems](https://developer.apple.com/documentation/appkit/nstabview/1391596-numberoftabviewitems)Added [NSTabView.selectedTabViewItem](https://developer.apple.com/documentation/appkit/nstabview/1391625-selectedtabviewitem)Added [NSTabView.tabViewItems](https://developer.apple.com/documentation/appkit/nstabview/1391613-tabviewitems)Added [NSTabView.tabViewType](https://developer.apple.com/documentation/appkit/nstabview/1391602-tabviewtype)Modified [-[NSTabViewDelegate tabView:didSelectTabViewItem:]](https://developer.apple.com/documentation/appkit/nstabviewdelegate/1391582-tabview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTabViewDelegate tabView:shouldSelectTabViewItem:]](https://developer.apple.com/documentation/appkit/nstabviewdelegate/1391651-tabview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTabViewDelegate tabView:willSelectTabViewItem:]](https://developer.apple.com/documentation/appkit/nstabviewdelegate/1391611-tabview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTabViewDelegate tabViewDidChangeNumberOfTabViewItems:]](https://developer.apple.com/documentation/appkit/nstabviewdelegate/1391657-tabviewdidchangenumberoftabviewi)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSTabViewController.h (Added)Added [NSTabViewController](https://developer.apple.com/documentation/appkit/nstabviewcontroller)Added [-[NSTabViewController addTabViewItem:]](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428214-addtabviewitem)Added [NSTabViewController.canPropagateSelectedChildViewControllerTitle](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428239-canpropagateselectedchildviewcon)Added [-[NSTabViewController insertTabViewItem:atIndex:]](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428255-inserttabviewitem)Added [-[NSTabViewController removeTabViewItem:]](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428235-removetabviewitem)Added [NSTabViewController.selectedTabViewItemIndex](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428220-selectedtabviewitemindex)Added [NSTabViewController.tabStyle](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428259-tabstyle)Added [NSTabViewController.tabView](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428241-tabview)Added [-[NSTabViewController tabView:didSelectTabViewItem:]](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428243-tabview)Added [-[NSTabViewController tabView:shouldSelectTabViewItem:]](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428237-tabview)Added [-[NSTabViewController tabView:willSelectTabViewItem:]](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428231-tabview)Added [-[NSTabViewController tabViewItemForViewController:]](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428233-tabviewitem)Added [NSTabViewController.tabViewItems](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428222-tabviewitems)Added [-[NSTabViewController toolbar:itemForItemIdentifier:willBeInsertedIntoToolbar:]](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428218-toolbar)Added [-[NSTabViewController toolbarAllowedItemIdentifiers:]](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428229-toolbaralloweditemidentifiers)Added [-[NSTabViewController toolbarDefaultItemIdentifiers:]](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428251-toolbardefaultitemidentifiers)Added [-[NSTabViewController toolbarSelectableItemIdentifiers:]](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428261-toolbarselectableitemidentifiers)Added [NSTabViewController.transitionOptions](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428257-transitionoptions)Added [-[NSTabViewController viewDidLoad]](https://developer.apple.com/documentation/appkit/nstabviewcontroller/1428253-viewdidload)Added [NSTabViewControllerTabStyle](https://developer.apple.com/documentation/appkit/nstabviewcontrollertabstyle)Added [NSTabViewControllerTabStyleSegmentedControlOnBottom](https://developer.apple.com/documentation/appkit/nstabviewcontrollertabstyle/nstabviewcontrollertabstylesegmentedcontrolonbottom)Added [NSTabViewControllerTabStyleSegmentedControlOnTop](https://developer.apple.com/documentation/appkit/nstabviewcontroller/tabstyle/segmentedcontrolontop)Added [NSTabViewControllerTabStyleToolbar](https://developer.apple.com/documentation/appkit/nstabviewcontroller/tabstyle/toolbar)Added [NSTabViewControllerTabStyleUnspecified](https://developer.apple.com/documentation/appkit/nstabviewcontrollertabstyle/nstabviewcontrollertabstyleunspecified)NSTabViewItem.hRemoved [-[NSTabViewItem color]](https://developer.apple.com/documentation/appkit/nstabviewitem/1477525-color)Removed [-[NSTabViewItem identifier]](https://developer.apple.com/documentation/appkit/nstabviewitem/1477529-identifier)Removed [-[NSTabViewItem initialFirstResponder]](https://developer.apple.com/documentation/appkit/nstabviewitem/1477541-initialfirstresponder)Removed [-[NSTabViewItem label]](https://developer.apple.com/documentation/appkit/nstabviewitem/1477542-label)Removed [-[NSTabViewItem setColor:]](https://developer.apple.com/documentation/appkit/nstabviewitem/1477525-color)Removed [-[NSTabViewItem setIdentifier:]](https://developer.apple.com/documentation/appkit/nstabviewitem/1477529-identifier)Removed [-[NSTabViewItem setInitialFirstResponder:]](https://developer.apple.com/documentation/appkit/nstabviewitem/1477541-initialfirstresponder)Removed [-[NSTabViewItem setLabel:]](https://developer.apple.com/documentation/appkit/nstabviewitem/1477542-label)Removed [-[NSTabViewItem setToolTip:]](https://developer.apple.com/documentation/appkit/nstabviewitem/1477515-tooltip)Removed [-[NSTabViewItem setView:]](https://developer.apple.com/documentation/appkit/nstabviewitem/1477537-view)Removed [-[NSTabViewItem tabState]](https://developer.apple.com/documentation/appkit/nstabviewitem/1477539-tabstate)Removed [-[NSTabViewItem tabView]](https://developer.apple.com/documentation/appkit/nstabviewitem/1477535-tabview)Removed [-[NSTabViewItem toolTip]](https://developer.apple.com/documentation/appkit/nstabviewitem/1477515-tooltip)Removed [-[NSTabViewItem view]](https://developer.apple.com/documentation/appkit/nstabviewitem/1477537-view)Added [NSTabViewItem.color](https://developer.apple.com/documentation/appkit/nstabviewitem/1477525-color)Added [NSTabViewItem.identifier](https://developer.apple.com/documentation/appkit/nstabviewitem/1477529-identifier)Added [NSTabViewItem.image](https://developer.apple.com/documentation/appkit/nstabviewitem/1477527-image)Added [NSTabViewItem.initialFirstResponder](https://developer.apple.com/documentation/appkit/nstabviewitem/1477541-initialfirstresponder)Added [NSTabViewItem.label](https://developer.apple.com/documentation/appkit/nstabviewitem/1477542-label)Added [NSTabViewItem.tabState](https://developer.apple.com/documentation/appkit/nstabviewitem/1477539-tabstate)Added [NSTabViewItem.tabView](https://developer.apple.com/documentation/appkit/nstabviewitem/1477535-tabview)Added [+[NSTabViewItem tabViewItemWithViewController:]](https://developer.apple.com/documentation/appkit/nstabviewitem/1477509-tabviewitemwithviewcontroller)Added [NSTabViewItem.toolTip](https://developer.apple.com/documentation/appkit/nstabviewitem/1477515-tooltip)Added [NSTabViewItem.view](https://developer.apple.com/documentation/appkit/nstabviewitem/1477537-view)Added [NSTabViewItem.viewController](https://developer.apple.com/documentation/appkit/nstabviewitem/1477521-viewcontroller)Modified [-[NSTabViewItem initWithIdentifier:]](https://developer.apple.com/documentation/appkit/nstabviewitem/1477533-initwithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithIdentifier:(id)identifier ``` |
| To | ``` - (instancetype)initWithIdentifier:(id)identifier ``` |

NSTableCellView.hModified [NSTableCellView.draggingImageComponents](https://developer.apple.com/documentation/appkit/nstablecellview/1483199-draggingimagecomponents)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readonly) NSArray *draggingImageComponents ``` |
| To | ``` @property(readonly, strong) NSArray *draggingImageComponents ``` |

Modified [NSTableCellView.imageView](https://developer.apple.com/documentation/appkit/nstablecellview/1483213-imageview)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) NSImageView *imageView ``` |
| To | ``` @property(assign) IBOutlet NSImageView *imageView ``` |

Modified [NSTableCellView.objectValue](https://developer.apple.com/documentation/appkit/nstablecellview/1483204-objectvalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) id objectValue ``` |
| To | ``` @property(strong) id objectValue ``` |

Modified [NSTableCellView.textField](https://developer.apple.com/documentation/appkit/nstablecellview/1483202-textfield)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) NSTextField *textField ``` |
| To | ``` @property(assign) IBOutlet NSTextField *textField ``` |

NSTableColumn.hRemoved [-[NSTableColumn dataCell]](https://developer.apple.com/documentation/appkit/nstablecolumn/1534251-datacell)Removed [-[NSTableColumn headerCell]](https://developer.apple.com/documentation/appkit/nstablecolumn/1525137-headercell)Removed [-[NSTableColumn headerToolTip]](https://developer.apple.com/documentation/appkit/nstablecolumn/1524685-headertooltip)Removed [-[NSTableColumn identifier]](https://developer.apple.com/documentation/appkit/nstablecolumn/1531113-identifier)Removed [-[NSTableColumn isEditable]](https://developer.apple.com/documentation/appkit/nstablecolumn/1528412-editable)Removed [-[NSTableColumn isHidden]](https://developer.apple.com/documentation/appkit/nstablecolumn/1524681-ishidden)Removed [-[NSTableColumn maxWidth]](https://developer.apple.com/documentation/appkit/nstablecolumn/1526342-maxwidth)Removed [-[NSTableColumn minWidth]](https://developer.apple.com/documentation/appkit/nstablecolumn/1525126-minwidth)Removed [-[NSTableColumn resizingMask]](https://developer.apple.com/documentation/appkit/nstablecolumn/1529591-resizingmask)Removed [-[NSTableColumn setDataCell:]](https://developer.apple.com/documentation/appkit/nstablecolumn/1534251-datacell)Removed [-[NSTableColumn setEditable:]](https://developer.apple.com/documentation/appkit/nstablecolumn/1528412-editable)Removed [-[NSTableColumn setHeaderCell:]](https://developer.apple.com/documentation/appkit/nstablecolumn/1525137-headercell)Removed [-[NSTableColumn setHeaderToolTip:]](https://developer.apple.com/documentation/appkit/nstablecolumn/1524685-headertooltip)Removed [-[NSTableColumn setHidden:]](https://developer.apple.com/documentation/appkit/nstablecolumn/1524681-hidden)Removed [-[NSTableColumn setIdentifier:]](https://developer.apple.com/documentation/appkit/nstablecolumn/1531113-identifier)Removed [-[NSTableColumn setMaxWidth:]](https://developer.apple.com/documentation/appkit/nstablecolumn/1526342-maxwidth)Removed [-[NSTableColumn setMinWidth:]](https://developer.apple.com/documentation/appkit/nstablecolumn/1525126-minwidth)Removed [-[NSTableColumn setResizingMask:]](https://developer.apple.com/documentation/appkit/nstablecolumn/1529591-resizingmask)Removed [-[NSTableColumn setSortDescriptorPrototype:]](https://developer.apple.com/documentation/appkit/nstablecolumn/1534663-sortdescriptorprototype)Removed [-[NSTableColumn setTableView:]](https://developer.apple.com/documentation/appkit/nstablecolumn/1535908-tableview)Removed [-[NSTableColumn setWidth:]](https://developer.apple.com/documentation/appkit/nstablecolumn/1528774-width)Removed [-[NSTableColumn sortDescriptorPrototype]](https://developer.apple.com/documentation/appkit/nstablecolumn/1534663-sortdescriptorprototype)Removed [-[NSTableColumn tableView]](https://developer.apple.com/documentation/appkit/nstablecolumn/1535908-tableview)Removed [-[NSTableColumn width]](https://developer.apple.com/documentation/appkit/nstablecolumn/1528774-width)Added [NSTableColumn.dataCell](https://developer.apple.com/documentation/appkit/nstablecolumn/1534251-datacell)Added [NSTableColumn.editable](https://developer.apple.com/documentation/appkit/nstablecolumn/1528412-editable)Added [NSTableColumn.headerCell](https://developer.apple.com/documentation/appkit/nstablecolumn/1525137-headercell)Added [NSTableColumn.headerToolTip](https://developer.apple.com/documentation/appkit/nstablecolumn/1524685-headertooltip)Added [NSTableColumn.hidden](https://developer.apple.com/documentation/appkit/nstablecolumn/1524681-ishidden)Added [NSTableColumn.identifier](https://developer.apple.com/documentation/appkit/nstablecolumn/1531113-identifier)Added [NSTableColumn.maxWidth](https://developer.apple.com/documentation/appkit/nstablecolumn/1526342-maxwidth)Added [NSTableColumn.minWidth](https://developer.apple.com/documentation/appkit/nstablecolumn/1525126-minwidth)Added [NSTableColumn.resizingMask](https://developer.apple.com/documentation/appkit/nstablecolumn/1529591-resizingmask)Added [NSTableColumn.sortDescriptorPrototype](https://developer.apple.com/documentation/appkit/nstablecolumn/1534663-sortdescriptorprototype)Added [NSTableColumn.tableView](https://developer.apple.com/documentation/appkit/nstablecolumn/1535908-tableview)Added [NSTableColumn.title](https://developer.apple.com/documentation/appkit/nstablecolumn/1526875-title)Added [NSTableColumn.width](https://developer.apple.com/documentation/appkit/nstablecolumn/1528774-width)Added [NSTableColumnResizingOptions](https://developer.apple.com/documentation/appkit/nstablecolumnresizingoptions)Modified [-[NSTableColumn dataCellForRow:]](https://developer.apple.com/documentation/appkit/nstablecolumn/1532459-datacell)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSTableColumn initWithIdentifier:]](https://developer.apple.com/documentation/appkit/nstablecolumn/1526749-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithIdentifier:(NSString *)identifier ``` |
| To | ``` - (instancetype)initWithIdentifier:(NSString *)identifier ``` |

NSTableHeaderView.hRemoved [-[NSTableHeaderView draggedColumn]](https://developer.apple.com/documentation/appkit/nstableheaderview/1534458-draggedcolumn)Removed [-[NSTableHeaderView draggedDistance]](https://developer.apple.com/documentation/appkit/nstableheaderview/1527836-draggeddistance)Removed [-[NSTableHeaderView resizedColumn]](https://developer.apple.com/documentation/appkit/nstableheaderview/1528247-resizedcolumn)Removed [-[NSTableHeaderView setTableView:]](https://developer.apple.com/documentation/appkit/nstableheaderview/1535730-tableview)Removed [-[NSTableHeaderView tableView]](https://developer.apple.com/documentation/appkit/nstableheaderview/1535730-tableview)Added [NSTableHeaderView.draggedColumn](https://developer.apple.com/documentation/appkit/nstableheaderview/1534458-draggedcolumn)Added [NSTableHeaderView.draggedDistance](https://developer.apple.com/documentation/appkit/nstableheaderview/1527836-draggeddistance)Added [NSTableHeaderView.resizedColumn](https://developer.apple.com/documentation/appkit/nstableheaderview/1528247-resizedcolumn)Added [NSTableHeaderView.tableView](https://developer.apple.com/documentation/appkit/nstableheaderview/1535730-tableview)NSTableRowView.hAdded [NSTableRowView.nextRowSelected](https://developer.apple.com/documentation/appkit/nstablerowview/1529083-nextrowselected)Added [NSTableRowView.previousRowSelected](https://developer.apple.com/documentation/appkit/nstablerowview/1535313-previousrowselected)Modified [NSTableRowView](https://developer.apple.com/documentation/appkit/nstablerowview)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSAccessibilityRow |

NSTableView.hRemoved [-[NSTableView allowsColumnReordering]](https://developer.apple.com/documentation/appkit/nstableview/1530207-allowscolumnreordering)Removed [-[NSTableView allowsColumnResizing]](https://developer.apple.com/documentation/appkit/nstableview/1527826-allowscolumnresizing)Removed [-[NSTableView allowsColumnSelection]](https://developer.apple.com/documentation/appkit/nstableview/1525276-allowscolumnselection)Removed [-[NSTableView allowsEmptySelection]](https://developer.apple.com/documentation/appkit/nstableview/1535902-allowsemptyselection)Removed [-[NSTableView allowsMultipleSelection]](https://developer.apple.com/documentation/appkit/nstableview/1532523-allowsmultipleselection)Removed [-[NSTableView allowsTypeSelect]](https://developer.apple.com/documentation/appkit/nstableview/1526084-allowstypeselect)Removed [-[NSTableView autosaveName]](https://developer.apple.com/documentation/appkit/nstableview/1534409-autosavename)Removed [-[NSTableView autosaveTableColumns]](https://developer.apple.com/documentation/appkit/nstableview/1525596-autosavetablecolumns)Removed [-[NSTableView backgroundColor]](https://developer.apple.com/documentation/appkit/nstableview/1527806-backgroundcolor)Removed [-[NSTableView clickedColumn]](https://developer.apple.com/documentation/appkit/nstableview/1529205-clickedcolumn)Removed [-[NSTableView clickedRow]](https://developer.apple.com/documentation/appkit/nstableview/1527357-clickedrow)Removed [-[NSTableView columnAutoresizingStyle]](https://developer.apple.com/documentation/appkit/nstableview/1530784-columnautoresizingstyle)Removed [-[NSTableView cornerView]](https://developer.apple.com/documentation/appkit/nstableview/1535831-cornerview)Removed [-[NSTableView doubleAction]](https://developer.apple.com/documentation/appkit/nstableview/1526992-doubleaction)Removed [-[NSTableView draggingDestinationFeedbackStyle]](https://developer.apple.com/documentation/appkit/nstableview/1527570-draggingdestinationfeedbackstyle)Removed [-[NSTableView editedColumn]](https://developer.apple.com/documentation/appkit/nstableview/1532307-editedcolumn)Removed [-[NSTableView editedRow]](https://developer.apple.com/documentation/appkit/nstableview/1534282-editedrow)Removed [-[NSTableView effectiveRowSizeStyle]](https://developer.apple.com/documentation/appkit/nstableview/1531825-effectiverowsizestyle)Removed [-[NSTableView floatsGroupRows]](https://developer.apple.com/documentation/appkit/nstableview/1528624-floatsgrouprows)Removed [-[NSTableView gridColor]](https://developer.apple.com/documentation/appkit/nstableview/1524620-gridcolor)Removed [-[NSTableView gridStyleMask]](https://developer.apple.com/documentation/appkit/nstableview/1528689-gridstylemask)Removed [-[NSTableView headerView]](https://developer.apple.com/documentation/appkit/nstableview/1535880-headerview)Removed [-[NSTableView highlightedTableColumn]](https://developer.apple.com/documentation/appkit/nstableview/1524980-highlightedtablecolumn)Removed [-[NSTableView intercellSpacing]](https://developer.apple.com/documentation/appkit/nstableview/1524258-intercellspacing)Removed [-[NSTableView numberOfColumns]](https://developer.apple.com/documentation/appkit/nstableview/1528902-numberofcolumns)Removed [-[NSTableView numberOfRows]](https://developer.apple.com/documentation/appkit/nstableview/1527941-numberofrows)Removed [-[NSTableView numberOfSelectedColumns]](https://developer.apple.com/documentation/appkit/nstableview/1524361-numberofselectedcolumns)Removed [-[NSTableView numberOfSelectedRows]](https://developer.apple.com/documentation/appkit/nstableview/1527463-numberofselectedrows)Removed [-[NSTableView registeredNibsByIdentifier]](https://developer.apple.com/documentation/appkit/nstableview/1530663-registerednibsbyidentifier)Removed [-[NSTableView rowHeight]](https://developer.apple.com/documentation/appkit/nstableview/1529148-rowheight)Removed [-[NSTableView rowSizeStyle]](https://developer.apple.com/documentation/appkit/nstableview/1534438-rowsizestyle)Removed [-[NSTableView selectedColumn]](https://developer.apple.com/documentation/appkit/nstableview/1532974-selectedcolumn)Removed [-[NSTableView selectedColumnIndexes]](https://developer.apple.com/documentation/appkit/nstableview/1524283-selectedcolumnindexes)Removed [-[NSTableView selectedRow]](https://developer.apple.com/documentation/appkit/nstableview/1535010-selectedrow)Removed [-[NSTableView selectedRowIndexes]](https://developer.apple.com/documentation/appkit/nstableview/1533844-selectedrowindexes)Removed [-[NSTableView selectionHighlightStyle]](https://developer.apple.com/documentation/appkit/nstableview/1526311-selectionhighlightstyle)Removed [-[NSTableView setAllowsColumnReordering:]](https://developer.apple.com/documentation/appkit/nstableview/1530207-allowscolumnreordering)Removed [-[NSTableView setAllowsColumnResizing:]](https://developer.apple.com/documentation/appkit/nstableview/1527826-allowscolumnresizing)Removed [-[NSTableView setAllowsColumnSelection:]](https://developer.apple.com/documentation/appkit/nstableview/1525276-allowscolumnselection)Removed [-[NSTableView setAllowsEmptySelection:]](https://developer.apple.com/documentation/appkit/nstableview/1535902-allowsemptyselection)Removed [-[NSTableView setAllowsMultipleSelection:]](https://developer.apple.com/documentation/appkit/nstableview/1532523-allowsmultipleselection)Removed [-[NSTableView setAllowsTypeSelect:]](https://developer.apple.com/documentation/appkit/nstableview/1526084-allowstypeselect)Removed [-[NSTableView setAutosaveName:]](https://developer.apple.com/documentation/appkit/nstableview/1534409-autosavename)Removed [-[NSTableView setAutosaveTableColumns:]](https://developer.apple.com/documentation/appkit/nstableview/1525596-autosavetablecolumns)Removed [-[NSTableView setBackgroundColor:]](https://developer.apple.com/documentation/appkit/nstableview/1527806-backgroundcolor)Removed [-[NSTableView setColumnAutoresizingStyle:]](https://developer.apple.com/documentation/appkit/nstableview/1530784-columnautoresizingstyle)Removed [-[NSTableView setCornerView:]](https://developer.apple.com/documentation/appkit/nstableview/1535831-cornerview)Removed [-[NSTableView setDoubleAction:]](https://developer.apple.com/documentation/appkit/nstableview/1526992-doubleaction)Removed [-[NSTableView setDraggingDestinationFeedbackStyle:]](https://developer.apple.com/documentation/appkit/nstableview/1527570-draggingdestinationfeedbackstyle)Removed [-[NSTableView setFloatsGroupRows:]](https://developer.apple.com/documentation/appkit/nstableview/1528624-floatsgrouprows)Removed [-[NSTableView setGridColor:]](https://developer.apple.com/documentation/appkit/nstableview/1524620-gridcolor)Removed [-[NSTableView setGridStyleMask:]](https://developer.apple.com/documentation/appkit/nstableview/1528689-gridstylemask)Removed [-[NSTableView setHeaderView:]](https://developer.apple.com/documentation/appkit/nstableview/1535880-headerview)Removed [-[NSTableView setHighlightedTableColumn:]](https://developer.apple.com/documentation/appkit/nstableview/1524980-highlightedtablecolumn)Removed [-[NSTableView setIntercellSpacing:]](https://developer.apple.com/documentation/appkit/nstableview/1524258-intercellspacing)Removed [-[NSTableView setRowHeight:]](https://developer.apple.com/documentation/appkit/nstableview/1529148-rowheight)Removed [-[NSTableView setRowSizeStyle:]](https://developer.apple.com/documentation/appkit/nstableview/1534438-rowsizestyle)Removed [-[NSTableView setSelectionHighlightStyle:]](https://developer.apple.com/documentation/appkit/nstableview/1526311-selectionhighlightstyle)Removed [-[NSTableView setSortDescriptors:]](https://developer.apple.com/documentation/appkit/nstableview/1534198-sortdescriptors)Removed [-[NSTableView setUsesAlternatingRowBackgroundColors:]](https://developer.apple.com/documentation/appkit/nstableview/1533967-usesalternatingrowbackgroundcolo)Removed [-[NSTableView setVerticalMotionCanBeginDrag:]](https://developer.apple.com/documentation/appkit/nstableview/1534585-verticalmotioncanbegindrag)Removed [-[NSTableView sortDescriptors]](https://developer.apple.com/documentation/appkit/nstableview/1534198-sortdescriptors)Removed [-[NSTableView tableColumns]](https://developer.apple.com/documentation/appkit/nstableview/1528735-tablecolumns)Removed [-[NSTableView usesAlternatingRowBackgroundColors]](https://developer.apple.com/documentation/appkit/nstableview/1533967-usesalternatingrowbackgroundcolo)Removed [-[NSTableView verticalMotionCanBeginDrag]](https://developer.apple.com/documentation/appkit/nstableview/1534585-verticalmotioncanbegindrag)Added [NSTableView.allowsColumnReordering](https://developer.apple.com/documentation/appkit/nstableview/1530207-allowscolumnreordering)Added [NSTableView.allowsColumnResizing](https://developer.apple.com/documentation/appkit/nstableview/1527826-allowscolumnresizing)Added [NSTableView.allowsColumnSelection](https://developer.apple.com/documentation/appkit/nstableview/1525276-allowscolumnselection)Added [NSTableView.allowsEmptySelection](https://developer.apple.com/documentation/appkit/nstableview/1535902-allowsemptyselection)Added [NSTableView.allowsMultipleSelection](https://developer.apple.com/documentation/appkit/nstableview/1532523-allowsmultipleselection)Added [NSTableView.allowsTypeSelect](https://developer.apple.com/documentation/appkit/nstableview/1526084-allowstypeselect)Added [NSTableView.autosaveName](https://developer.apple.com/documentation/appkit/nstableview/1534409-autosavename)Added [NSTableView.autosaveTableColumns](https://developer.apple.com/documentation/appkit/nstableview/1525596-autosavetablecolumns)Added [NSTableView.backgroundColor](https://developer.apple.com/documentation/appkit/nstableview/1527806-backgroundcolor)Added [NSTableView.clickedColumn](https://developer.apple.com/documentation/appkit/nstableview/1529205-clickedcolumn)Added [NSTableView.clickedRow](https://developer.apple.com/documentation/appkit/nstableview/1527357-clickedrow)Added [NSTableView.columnAutoresizingStyle](https://developer.apple.com/documentation/appkit/nstableview/1530784-columnautoresizingstyle)Added [NSTableView.cornerView](https://developer.apple.com/documentation/appkit/nstableview/1535831-cornerview)Added [NSTableView.doubleAction](https://developer.apple.com/documentation/appkit/nstableview/1526992-doubleaction)Added [NSTableView.draggingDestinationFeedbackStyle](https://developer.apple.com/documentation/appkit/nstableview/1527570-draggingdestinationfeedbackstyle)Added [NSTableView.editedColumn](https://developer.apple.com/documentation/appkit/nstableview/1532307-editedcolumn)Added [NSTableView.editedRow](https://developer.apple.com/documentation/appkit/nstableview/1534282-editedrow)Added [NSTableView.effectiveRowSizeStyle](https://developer.apple.com/documentation/appkit/nstableview/1531825-effectiverowsizestyle)Added [NSTableView.floatsGroupRows](https://developer.apple.com/documentation/appkit/nstableview/1528624-floatsgrouprows)Added [NSTableView.gridColor](https://developer.apple.com/documentation/appkit/nstableview/1524620-gridcolor)Added [NSTableView.gridStyleMask](https://developer.apple.com/documentation/appkit/nstableview/1528689-gridstylemask)Added [NSTableView.headerView](https://developer.apple.com/documentation/appkit/nstableview/1535880-headerview)Added [NSTableView.highlightedTableColumn](https://developer.apple.com/documentation/appkit/nstableview/1524980-highlightedtablecolumn)Added [-[NSTableView initWithCoder:]](https://developer.apple.com/documentation/appkit/nstableview/1528481-initwithcoder)Added [-[NSTableView initWithFrame:]](https://developer.apple.com/documentation/appkit/nstableview/1525511-initwithframe)Added [NSTableView.intercellSpacing](https://developer.apple.com/documentation/appkit/nstableview/1524258-intercellspacing)Added [NSTableView.numberOfColumns](https://developer.apple.com/documentation/appkit/nstableview/1528902-numberofcolumns)Added [NSTableView.numberOfRows](https://developer.apple.com/documentation/appkit/nstableview/1527941-numberofrows)Added [NSTableView.numberOfSelectedColumns](https://developer.apple.com/documentation/appkit/nstableview/1524361-numberofselectedcolumns)Added [NSTableView.numberOfSelectedRows](https://developer.apple.com/documentation/appkit/nstableview/1527463-numberofselectedrows)Added [NSTableView.registeredNibsByIdentifier](https://developer.apple.com/documentation/appkit/nstableview/1530663-registerednibsbyidentifier)Added [NSTableView.rowHeight](https://developer.apple.com/documentation/appkit/nstableview/1529148-rowheight)Added [NSTableView.rowSizeStyle](https://developer.apple.com/documentation/appkit/nstableview/1534438-rowsizestyle)Added [NSTableView.selectedColumn](https://developer.apple.com/documentation/appkit/nstableview/1532974-selectedcolumn)Added [NSTableView.selectedColumnIndexes](https://developer.apple.com/documentation/appkit/nstableview/1524283-selectedcolumnindexes)Added [NSTableView.selectedRow](https://developer.apple.com/documentation/appkit/nstableview/1535010-selectedrow)Added [NSTableView.selectedRowIndexes](https://developer.apple.com/documentation/appkit/nstableview/1533844-selectedrowindexes)Added [NSTableView.selectionHighlightStyle](https://developer.apple.com/documentation/appkit/nstableview/1526311-selectionhighlightstyle)Added [NSTableView.sortDescriptors](https://developer.apple.com/documentation/appkit/nstableview/1534198-sortdescriptors)Added [NSTableView.tableColumns](https://developer.apple.com/documentation/appkit/nstableview/1528735-tablecolumns)Added [NSTableView.usesAlternatingRowBackgroundColors](https://developer.apple.com/documentation/appkit/nstableview/1533967-usesalternatingrowbackgroundcolo)Added [NSTableView.usesStaticContents](https://developer.apple.com/documentation/appkit/nstableview/1533450-usesstaticcontents)Added [NSTableView.verticalMotionCanBeginDrag](https://developer.apple.com/documentation/appkit/nstableview/1534585-verticalmotioncanbegindrag)Modified [NSTableView](https://developer.apple.com/documentation/appkit/nstableview)

|  | Protocols |
| --- | --- |
| From | NSDraggingSource, NSTextViewDelegate, NSUserInterfaceValidations |
| To | NSAccessibilityTable, NSDraggingSource, NSTextViewDelegate, NSUserInterfaceValidations |

Modified [-[NSTableView focusedColumn]](https://developer.apple.com/documentation/appkit/nstableview/1533870-focusedcolumn)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSTableView performClickOnCellAtColumn:row:]](https://developer.apple.com/documentation/appkit/nstableview/1527932-performclickoncellatcolumn)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSTableView preparedCellAtColumn:row:]](https://developer.apple.com/documentation/appkit/nstableview/1534640-preparedcell)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSTableView setFocusedColumn:]](https://developer.apple.com/documentation/appkit/nstableview/1534977-setfocusedcolumn)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSTableView shouldFocusCell:atColumn:row:]](https://developer.apple.com/documentation/appkit/nstableview/1531629-shouldfocuscell)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSTableView textDidBeginEditing:]](https://developer.apple.com/documentation/appkit/nstableview/1535888-textdidbeginediting)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSTableView textDidChange:]](https://developer.apple.com/documentation/appkit/nstableview/1529764-textdidchange)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSTableView textDidEndEditing:]](https://developer.apple.com/documentation/appkit/nstableview/1532159-textdidendediting)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSTableView textShouldBeginEditing:]](https://developer.apple.com/documentation/appkit/nstableview/1529201-textshouldbeginediting)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSTableView textShouldEndEditing:]](https://developer.apple.com/documentation/appkit/nstableview/1531760-textshouldendediting)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSTableViewDataSource numberOfRowsInTableView:]](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1524583-numberofrowsintableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDataSource tableView:acceptDrop:row:dropOperation:]](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1527733-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDataSource tableView:draggingSession:endedAtPoint:operation:]](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1534355-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDataSource tableView:draggingSession:willBeginAtPoint:forRowIndexes:]](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1528890-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDataSource tableView:namesOfPromisedFilesDroppedAtDestination:forDraggedRowsWithIndexes:]](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1530316-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDataSource tableView:objectValueForTableColumn:row:]](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1533674-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDataSource tableView:pasteboardWriterForRow:]](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1535294-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDataSource tableView:setObjectValue:forTableColumn:row:]](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1526317-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDataSource tableView:sortDescriptorsDidChange:]](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1532935-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDataSource tableView:updateDraggingItemsForDrag:]](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1535273-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDataSource tableView:validateDrop:proposedRow:proposedDropOperation:]](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1532052-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDataSource tableView:writeRowsWithIndexes:toPasteboard:]](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1525370-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate selectionShouldChangeInTableView:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1533949-selectionshouldchange)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:dataCellForTableColumn:row:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1529321-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:didAddRowView:forRow:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1527434-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:didClickTableColumn:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1533923-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:didDragTableColumn:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1535732-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:didRemoveRowView:forRow:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1528674-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:heightOfRow:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1529684-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:isGroupRow:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1526676-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:mouseDownInHeaderOfTableColumn:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1531711-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:nextTypeSelectMatchFromRow:toRow:forString:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1534757-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:rowViewForRow:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1532417-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:selectionIndexesForProposedSelection:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1532829-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:shouldEditTableColumn:row:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1527305-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:shouldReorderColumn:toColumn:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1534434-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:shouldSelectRow:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1526916-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:shouldSelectTableColumn:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1527204-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:shouldShowCellExpansionForTableColumn:row:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1535567-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:shouldTrackCell:forTableColumn:row:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1533564-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:shouldTypeSelectForEvent:withCurrentSearchString:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1526347-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:sizeToFitWidthOfColumn:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1526429-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:toolTipForCell:rect:tableColumn:row:mouseLocation:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1526097-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:typeSelectStringForTableColumn:row:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1530001-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:viewForTableColumn:row:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1527449-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableView:willDisplayCell:forTableColumn:row:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1533829-tableview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableViewColumnDidMove:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1534237-tableviewcolumndidmove)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableViewColumnDidResize:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1535901-tableviewcolumndidresize)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableViewSelectionDidChange:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1528567-tableviewselectiondidchange)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTableViewDelegate tableViewSelectionIsChanging:]](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1530812-tableviewselectionischanging)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSText.hRemoved [-[NSText alignment]](https://developer.apple.com/documentation/appkit/nstext/1534102-alignment)Removed [-[NSText backgroundColor]](https://developer.apple.com/documentation/appkit/nstext/1535324-backgroundcolor)Removed [-[NSText baseWritingDirection]](https://developer.apple.com/documentation/appkit/nstext/1526206-basewritingdirection)Removed [-[NSText delegate]](https://developer.apple.com/documentation/appkit/nstext/1529480-delegate)Removed [-[NSText drawsBackground]](https://developer.apple.com/documentation/appkit/nstext/1531772-drawsbackground)Removed [-[NSText font]](https://developer.apple.com/documentation/appkit/nstext/1534646-font)Removed [-[NSText importsGraphics]](https://developer.apple.com/documentation/appkit/nstext/1531887-importsgraphics)Removed [-[NSText isEditable]](https://developer.apple.com/documentation/appkit/nstext/1529876-iseditable)Removed [-[NSText isFieldEditor]](https://developer.apple.com/documentation/appkit/nstext/1533080-isfieldeditor)Removed [-[NSText isHorizontallyResizable]](https://developer.apple.com/documentation/appkit/nstext/1527489-horizontallyresizable)Removed [-[NSText isRichText]](https://developer.apple.com/documentation/appkit/nstext/1531003-richtext)Removed [-[NSText isRulerVisible]](https://developer.apple.com/documentation/appkit/nstext/1533732-rulervisible)Removed [-[NSText isSelectable]](https://developer.apple.com/documentation/appkit/nstext/1535368-selectable)Removed [-[NSText isVerticallyResizable]](https://developer.apple.com/documentation/appkit/nstext/1535082-verticallyresizable)Removed [-[NSText maxSize]](https://developer.apple.com/documentation/appkit/nstext/1535900-maxsize)Removed [-[NSText minSize]](https://developer.apple.com/documentation/appkit/nstext/1526222-minsize)Removed [-[NSText selectedRange]](https://developer.apple.com/documentation/appkit/nstext/1526227-selectedrange)Removed [-[NSText setAlignment:]](https://developer.apple.com/documentation/appkit/nstext/1534102-alignment)Removed [-[NSText setBackgroundColor:]](https://developer.apple.com/documentation/appkit/nstext/1535324-backgroundcolor)Removed [-[NSText setBaseWritingDirection:]](https://developer.apple.com/documentation/appkit/nstext/1526206-basewritingdirection)Removed [-[NSText setDelegate:]](https://developer.apple.com/documentation/appkit/nstext/1529480-delegate)Removed [-[NSText setDrawsBackground:]](https://developer.apple.com/documentation/appkit/nstext/1531772-drawsbackground)Removed [-[NSText setEditable:]](https://developer.apple.com/documentation/appkit/nstext/1529876-iseditable)Removed [-[NSText setFieldEditor:]](https://developer.apple.com/documentation/appkit/nstext/1533080-isfieldeditor)Removed [-[NSText setFont:]](https://developer.apple.com/documentation/appkit/nstext/1534646-font)Removed [-[NSText setHorizontallyResizable:]](https://developer.apple.com/documentation/appkit/nstext/1527489-horizontallyresizable)Removed [-[NSText setImportsGraphics:]](https://developer.apple.com/documentation/appkit/nstext/1531887-importsgraphics)Removed [-[NSText setMaxSize:]](https://developer.apple.com/documentation/appkit/nstext/1535900-maxsize)Removed [-[NSText setMinSize:]](https://developer.apple.com/documentation/appkit/nstext/1526222-minsize)Removed [-[NSText setRichText:]](https://developer.apple.com/documentation/appkit/nstext/1531003-richtext)Removed [-[NSText setSelectable:]](https://developer.apple.com/documentation/appkit/nstext/1535368-selectable)Removed [-[NSText setSelectedRange:]](https://developer.apple.com/documentation/appkit/nstext/1526227-selectedrange)Removed [-[NSText setString:]](https://developer.apple.com/documentation/appkit/nstext/1528601-string)Removed [-[NSText setTextColor:]](https://developer.apple.com/documentation/appkit/nstext/1534875-textcolor)Removed [-[NSText setUsesFontPanel:]](https://developer.apple.com/documentation/appkit/nstext/1527431-usesfontpanel)Removed [-[NSText setVerticallyResizable:]](https://developer.apple.com/documentation/appkit/nstext/1535082-isverticallyresizable)Removed [-[NSText string]](https://developer.apple.com/documentation/appkit/nstext/1528601-string)Removed [-[NSText textColor]](https://developer.apple.com/documentation/appkit/nstext/1534875-textcolor)Removed [-[NSText usesFontPanel]](https://developer.apple.com/documentation/appkit/nstext/1527431-usesfontpanel)Added [NSText.alignment](https://developer.apple.com/documentation/appkit/nstext/1534102-alignment)Added [NSText.backgroundColor](https://developer.apple.com/documentation/appkit/nstext/1535324-backgroundcolor)Added [NSText.baseWritingDirection](https://developer.apple.com/documentation/appkit/nstext/1526206-basewritingdirection)Added [NSText.delegate](https://developer.apple.com/documentation/appkit/nstext/1529480-delegate)Added [NSText.drawsBackground](https://developer.apple.com/documentation/appkit/nstext/1531772-drawsbackground)Added [NSText.editable](https://developer.apple.com/documentation/appkit/nstext/1529876-iseditable)Added [NSText.fieldEditor](https://developer.apple.com/documentation/appkit/nstext/1533080-fieldeditor)Added [NSText.font](https://developer.apple.com/documentation/appkit/nstext/1534646-font)Added [NSText.horizontallyResizable](https://developer.apple.com/documentation/appkit/nstext/1527489-ishorizontallyresizable)Added [NSText.importsGraphics](https://developer.apple.com/documentation/appkit/nstext/1531887-importsgraphics)Added [-[NSText initWithCoder:]](https://developer.apple.com/documentation/appkit/nstext/1535093-initwithcoder)Added [-[NSText initWithFrame:]](https://developer.apple.com/documentation/appkit/nstext/1525191-initwithframe)Added [NSText.maxSize](https://developer.apple.com/documentation/appkit/nstext/1535900-maxsize)Added [NSText.minSize](https://developer.apple.com/documentation/appkit/nstext/1526222-minsize)Added [NSText.richText](https://developer.apple.com/documentation/appkit/nstext/1531003-richtext)Added [NSText.rulerVisible](https://developer.apple.com/documentation/appkit/nstext/1533732-rulervisible)Added [NSText.selectable](https://developer.apple.com/documentation/appkit/nstext/1535368-isselectable)Added [NSText.selectedRange](https://developer.apple.com/documentation/appkit/nstext/1526227-selectedrange)Added [NSText.string](https://developer.apple.com/documentation/appkit/nstext/1528601-string)Added [NSText.textColor](https://developer.apple.com/documentation/appkit/nstext/1534875-textcolor)Added [NSText.usesFontPanel](https://developer.apple.com/documentation/appkit/nstext/1527431-usesfontpanel)Added [NSText.verticallyResizable](https://developer.apple.com/documentation/appkit/nstext/1535082-verticallyresizable)Modified [-[NSTextDelegate textDidBeginEditing:]](https://developer.apple.com/documentation/appkit/nstextdelegate/1535575-textdidbeginediting)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextDelegate textDidChange:]](https://developer.apple.com/documentation/appkit/nstextdelegate/1526982-textdidchange)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextDelegate textDidEndEditing:]](https://developer.apple.com/documentation/appkit/nstextdelegate/1529016-textdidendediting)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextDelegate textShouldBeginEditing:]](https://developer.apple.com/documentation/appkit/nstextdelegate/1533298-textshouldbeginediting)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextDelegate textShouldEndEditing:]](https://developer.apple.com/documentation/appkit/nstextdelegate/1525992-textshouldendediting)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSTextAlternatives.hModified [NSTextAlternatives.alternativeStrings](https://developer.apple.com/documentation/appkit/nstextalternatives/1527585-alternativestrings)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *alternativeStrings ``` |
| To | ``` @property(readonly, copy) NSArray *alternativeStrings ``` |

Modified [-[NSTextAlternatives initWithPrimaryString:alternativeStrings:]](https://developer.apple.com/documentation/appkit/nstextalternatives/1529445-initwithprimarystring)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithPrimaryString:(NSString *)primaryString alternativeStrings:(NSArray *)alternativeStrings ``` |
| To | ``` - (instancetype)initWithPrimaryString:(NSString *)primaryString alternativeStrings:(NSArray *)alternativeStrings ``` |

Modified [NSTextAlternatives.primaryString](https://developer.apple.com/documentation/appkit/nstextalternatives/1526166-primarystring)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *primaryString ``` |
| To | ``` @property(readonly, copy) NSString *primaryString ``` |

NSTextAttachment.hRemoved [-[NSTextAttachment attachmentCell]](https://developer.apple.com/documentation/appkit/nstextattachment/1508413-attachmentcell)Removed [-[NSTextAttachment fileWrapper]](https://developer.apple.com/documentation/appkit/nstextattachment/1508398-filewrapper)Removed [-[NSTextAttachment setAttachmentCell:]](https://developer.apple.com/documentation/appkit/nstextattachment/1508413-attachmentcell)Removed [-[NSTextAttachment setFileWrapper:]](https://developer.apple.com/documentation/uikit/nstextattachment/1508398-filewrapper)Added [NSTextAttachment.attachmentCell](https://developer.apple.com/documentation/appkit/nstextattachment/1508413-attachmentcell)Added [NSTextAttachment.fileWrapper](https://developer.apple.com/documentation/uikit/nstextattachment/1508398-filewrapper)Modified [-[NSTextAttachment initWithFileWrapper:]](https://developer.apple.com/documentation/appkit/nstextattachment/1508373-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFileWrapper:(NSFileWrapper *)fileWrapper ``` |
| To | ``` - (instancetype)initWithFileWrapper:(NSFileWrapper *)fileWrapper ``` |

NSTextContainer.hRemoved [-[NSTextContainer containerSize]](https://developer.apple.com/documentation/appkit/nstextcontainer/1444551-containersize)Removed [-[NSTextContainer heightTracksTextView]](https://developer.apple.com/documentation/appkit/nstextcontainer/1444559-heighttrackstextview)Removed [-[NSTextContainer isSimpleRectangularTextContainer]](https://developer.apple.com/documentation/uikit/nstextcontainer/1444525-issimplerectangulartextcontainer)Removed [-[NSTextContainer layoutManager]](https://developer.apple.com/documentation/appkit/nstextcontainer/1444517-layoutmanager)Removed [-[NSTextContainer lineFragmentPadding]](https://developer.apple.com/documentation/appkit/nstextcontainer/1444527-linefragmentpadding)Removed [-[NSTextContainer setContainerSize:]](https://developer.apple.com/documentation/appkit/nstextcontainer/1444551-containersize)Removed [-[NSTextContainer setHeightTracksTextView:]](https://developer.apple.com/documentation/uikit/nstextcontainer/1444559-heighttrackstextview)Removed [-[NSTextContainer setLayoutManager:]](https://developer.apple.com/documentation/uikit/nstextcontainer/1444517-layoutmanager)Removed [-[NSTextContainer setLineFragmentPadding:]](https://developer.apple.com/documentation/appkit/nstextcontainer/1444527-linefragmentpadding)Removed [-[NSTextContainer setTextView:]](https://developer.apple.com/documentation/appkit/nstextcontainer/1444537-textview)Removed [-[NSTextContainer setWidthTracksTextView:]](https://developer.apple.com/documentation/appkit/nstextcontainer/1444563-widthtrackstextview)Removed [-[NSTextContainer textView]](https://developer.apple.com/documentation/appkit/nstextcontainer/1444537-textview)Removed [-[NSTextContainer widthTracksTextView]](https://developer.apple.com/documentation/appkit/nstextcontainer/1444563-widthtrackstextview)Added [NSTextContainer.containerSize](https://developer.apple.com/documentation/appkit/nstextcontainer/1444551-containersize)Added [NSTextContainer.heightTracksTextView](https://developer.apple.com/documentation/appkit/nstextcontainer/1444559-heighttrackstextview)Added [NSTextContainer.layoutManager](https://developer.apple.com/documentation/uikit/nstextcontainer/1444517-layoutmanager)Added [NSTextContainer.lineFragmentPadding](https://developer.apple.com/documentation/uikit/nstextcontainer/1444527-linefragmentpadding)Added [NSTextContainer.simpleRectangularTextContainer](https://developer.apple.com/documentation/appkit/nstextcontainer/1444525-simplerectangulartextcontainer)Added [NSTextContainer.textView](https://developer.apple.com/documentation/appkit/nstextcontainer/1444537-textview)Added [NSTextContainer.widthTracksTextView](https://developer.apple.com/documentation/uikit/nstextcontainer/1444563-widthtrackstextview)Modified [-[NSTextContainer initWithContainerSize:]](https://developer.apple.com/documentation/appkit/nstextcontainer/1444543-initwithcontainersize)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContainerSize:(NSSize)size ``` |
| To | ``` - (instancetype)initWithContainerSize:(NSSize)size ``` |

NSTextField.hRemoved [-[NSTextField acceptsFirstResponder]](https://developer.apple.com/documentation/appkit/nstextfield/1399393-acceptsfirstresponder)Removed [-[NSTextField allowsEditingTextAttributes]](https://developer.apple.com/documentation/appkit/nstextfield/1399401-allowseditingtextattributes)Removed [-[NSTextField backgroundColor]](https://developer.apple.com/documentation/appkit/nstextfield/1399389-backgroundcolor)Removed [-[NSTextField bezelStyle]](https://developer.apple.com/documentation/appkit/nstextfield/1399418-bezelstyle)Removed [-[NSTextField delegate]](https://developer.apple.com/documentation/appkit/nstextfield/1399437-delegate)Removed [-[NSTextField drawsBackground]](https://developer.apple.com/documentation/appkit/nstextfield/1399416-drawsbackground)Removed [-[NSTextField importsGraphics]](https://developer.apple.com/documentation/appkit/nstextfield/1399428-importsgraphics)Removed [-[NSTextField isBezeled]](https://developer.apple.com/documentation/appkit/nstextfield/1399435-bezeled)Removed [-[NSTextField isBordered]](https://developer.apple.com/documentation/appkit/nstextfield/1399403-bordered)Removed [-[NSTextField isEditable]](https://developer.apple.com/documentation/appkit/nstextfield/1399407-editable)Removed [-[NSTextField isSelectable]](https://developer.apple.com/documentation/appkit/nstextfield/1399422-isselectable)Removed [-[NSTextField preferredMaxLayoutWidth]](https://developer.apple.com/documentation/appkit/nstextfield/1399395-preferredmaxlayoutwidth)Removed [-[NSTextField setAllowsEditingTextAttributes:]](https://developer.apple.com/documentation/appkit/nstextfield/1399401-allowseditingtextattributes)Removed [-[NSTextField setBackgroundColor:]](https://developer.apple.com/documentation/appkit/nstextfield/1399389-backgroundcolor)Removed [-[NSTextField setBezelStyle:]](https://developer.apple.com/documentation/appkit/nstextfield/1399418-bezelstyle)Removed [-[NSTextField setBezeled:]](https://developer.apple.com/documentation/appkit/nstextfield/1399435-isbezeled)Removed [-[NSTextField setBordered:]](https://developer.apple.com/documentation/appkit/nstextfield/1399403-isbordered)Removed [-[NSTextField setDelegate:]](https://developer.apple.com/documentation/appkit/nstextfield/1399437-delegate)Removed [-[NSTextField setDrawsBackground:]](https://developer.apple.com/documentation/appkit/nstextfield/1399416-drawsbackground)Removed [-[NSTextField setEditable:]](https://developer.apple.com/documentation/appkit/nstextfield/1399407-iseditable)Removed [-[NSTextField setImportsGraphics:]](https://developer.apple.com/documentation/appkit/nstextfield/1399428-importsgraphics)Removed [-[NSTextField setPreferredMaxLayoutWidth:]](https://developer.apple.com/documentation/appkit/nstextfield/1399395-preferredmaxlayoutwidth)Removed [-[NSTextField setSelectable:]](https://developer.apple.com/documentation/appkit/nstextfield/1399422-isselectable)Removed [-[NSTextField setTextColor:]](https://developer.apple.com/documentation/appkit/nstextfield/1399409-textcolor)Removed [-[NSTextField textColor]](https://developer.apple.com/documentation/appkit/nstextfield/1399409-textcolor)Added [NSTextField.acceptsFirstResponder](https://developer.apple.com/documentation/appkit/nstextfield/1399393-acceptsfirstresponder)Added [NSTextField.allowsEditingTextAttributes](https://developer.apple.com/documentation/appkit/nstextfield/1399401-allowseditingtextattributes)Added [NSTextField.backgroundColor](https://developer.apple.com/documentation/appkit/nstextfield/1399389-backgroundcolor)Added [NSTextField.bezelStyle](https://developer.apple.com/documentation/appkit/nstextfield/1399418-bezelstyle)Added [NSTextField.bezeled](https://developer.apple.com/documentation/appkit/nstextfield/1399435-bezeled)Added [NSTextField.bordered](https://developer.apple.com/documentation/appkit/nstextfield/1399403-bordered)Added [NSTextField.delegate](https://developer.apple.com/documentation/appkit/nstextfield/1399437-delegate)Added [NSTextField.drawsBackground](https://developer.apple.com/documentation/appkit/nstextfield/1399416-drawsbackground)Added [NSTextField.editable](https://developer.apple.com/documentation/appkit/nstextfield/1399407-iseditable)Added [NSTextField.importsGraphics](https://developer.apple.com/documentation/appkit/nstextfield/1399428-importsgraphics)Added [NSTextField.placeholderAttributedString](https://developer.apple.com/documentation/appkit/nstextfield/1399387-placeholderattributedstring)Added [NSTextField.placeholderString](https://developer.apple.com/documentation/appkit/nstextfield/1399391-placeholderstring)Added [NSTextField.preferredMaxLayoutWidth](https://developer.apple.com/documentation/appkit/nstextfield/1399395-preferredmaxlayoutwidth)Added [NSTextField.selectable](https://developer.apple.com/documentation/appkit/nstextfield/1399422-selectable)Added [NSTextField.textColor](https://developer.apple.com/documentation/appkit/nstextfield/1399409-textcolor)Modified [NSTextField](https://developer.apple.com/documentation/appkit/nstextfield)

|  | Protocols |
| --- | --- |
| From | NSUserInterfaceValidations |
| To | NSAccessibilityNavigableStaticText, NSUserInterfaceValidations |

NSTextFieldCell.hRemoved [-[NSTextFieldCell allowedInputSourceLocales]](https://developer.apple.com/documentation/appkit/nstextfieldcell/1447163-allowedinputsourcelocales)Removed [-[NSTextFieldCell backgroundColor]](https://developer.apple.com/documentation/appkit/nstextfieldcell/1447159-backgroundcolor)Removed [-[NSTextFieldCell bezelStyle]](https://developer.apple.com/documentation/appkit/nstextfieldcell/1447161-bezelstyle)Removed [-[NSTextFieldCell drawsBackground]](https://developer.apple.com/documentation/appkit/nstextfieldcell/1447155-drawsbackground)Removed [-[NSTextFieldCell placeholderAttributedString]](https://developer.apple.com/documentation/appkit/nstextfieldcell/1447153-placeholderattributedstring)Removed [-[NSTextFieldCell placeholderString]](https://developer.apple.com/documentation/appkit/nstextfieldcell/1447165-placeholderstring)Removed [-[NSTextFieldCell setAllowedInputSourceLocales:]](https://developer.apple.com/documentation/appkit/nstextfieldcell/1447163-allowedinputsourcelocales)Removed [-[NSTextFieldCell setBackgroundColor:]](https://developer.apple.com/documentation/appkit/nstextfieldcell/1447159-backgroundcolor)Removed [-[NSTextFieldCell setBezelStyle:]](https://developer.apple.com/documentation/appkit/nstextfieldcell/1447161-bezelstyle)Removed [-[NSTextFieldCell setDrawsBackground:]](https://developer.apple.com/documentation/appkit/nstextfieldcell/1447155-drawsbackground)Removed [-[NSTextFieldCell setPlaceholderAttributedString:]](https://developer.apple.com/documentation/appkit/nstextfieldcell/1447153-placeholderattributedstring)Removed [-[NSTextFieldCell setPlaceholderString:]](https://developer.apple.com/documentation/appkit/nstextfieldcell/1447165-placeholderstring)Removed [-[NSTextFieldCell setTextColor:]](https://developer.apple.com/documentation/appkit/nstextfieldcell/1447151-textcolor)Removed [-[NSTextFieldCell textColor]](https://developer.apple.com/documentation/appkit/nstextfieldcell/1447151-textcolor)Added [NSTextFieldCell.allowedInputSourceLocales](https://developer.apple.com/documentation/appkit/nstextfieldcell/1447163-allowedinputsourcelocales)Added [NSTextFieldCell.backgroundColor](https://developer.apple.com/documentation/appkit/nstextfieldcell/1447159-backgroundcolor)Added [NSTextFieldCell.bezelStyle](https://developer.apple.com/documentation/appkit/nstextfieldcell/1447161-bezelstyle)Added [NSTextFieldCell.drawsBackground](https://developer.apple.com/documentation/appkit/nstextfieldcell/1447155-drawsbackground)Added [NSTextFieldCell.placeholderAttributedString](https://developer.apple.com/documentation/appkit/nstextfieldcell/1447153-placeholderattributedstring)Added [NSTextFieldCell.placeholderString](https://developer.apple.com/documentation/appkit/nstextfieldcell/1447165-placeholderstring)Added [NSTextFieldCell.textColor](https://developer.apple.com/documentation/appkit/nstextfieldcell/1447151-textcolor)NSTextFinder.hModified [NSTextFinder.client](https://developer.apple.com/documentation/appkit/nstextfinder/1533813-client)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<NSTextFinderClient> client ``` |
| To | ``` @property(assign) IBOutlet id<NSTextFinderClient> client ``` |

Modified [NSTextFinder.findBarContainer](https://developer.apple.com/documentation/appkit/nstextfinder/1526748-findbarcontainer)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<NSTextFinderBarContainer> findBarContainer ``` |
| To | ``` @property(assign) IBOutlet id<NSTextFinderBarContainer> findBarContainer ``` |

Modified [NSTextFinder.incrementalMatchRanges](https://developer.apple.com/documentation/appkit/nstextfinder/1528304-incrementalmatchranges)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *incrementalMatchRanges ``` |
| To | ``` @property(readonly, copy) NSArray *incrementalMatchRanges ``` |

Modified [-[NSTextFinder init]](https://developer.apple.com/documentation/appkit/nstextfinder/1535019-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

Modified [-[NSTextFinderBarContainer contentView]](https://developer.apple.com/documentation/appkit/nstextfinderbarcontainer/1532766-contentview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [NSTextFinderBarContainer.findBarView](https://developer.apple.com/documentation/appkit/nstextfinderbarcontainer/1531692-findbarview)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) NSView *findBarView ``` |
| To | ``` @property(strong) NSView *findBarView ``` |

Modified [-[NSTextFinderClient contentViewAtIndex:effectiveCharacterRange:]](https://developer.apple.com/documentation/appkit/nstextfinderclient/1524830-contentview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextFinderClient didReplaceCharacters]](https://developer.apple.com/documentation/appkit/nstextfinderclient/1534301-didreplacecharacters)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextFinderClient drawCharactersInRange:forContentView:]](https://developer.apple.com/documentation/appkit/nstextfinderclient/1533760-drawcharactersinrange)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextFinderClient rectsForCharacterRange:]](https://developer.apple.com/documentation/appkit/nstextfinderclient/1529980-rects)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextFinderClient replaceCharactersInRange:withString:]](https://developer.apple.com/documentation/appkit/nstextfinderclient/1527702-replacecharactersinrange)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextFinderClient scrollRangeToVisible:]](https://developer.apple.com/documentation/appkit/nstextfinderclient/1526989-scrollrangetovisible)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextFinderClient shouldReplaceCharactersInRanges:withStrings:]](https://developer.apple.com/documentation/appkit/nstextfinderclient/1529811-shouldreplacecharacters)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [NSTextFinderClient.string](https://developer.apple.com/documentation/appkit/nstextfinderclient/1529462-string)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *string ``` |
| To | ``` @property(readonly, strong) NSString *string ``` |

Modified [-[NSTextFinderClient stringAtIndex:effectiveRange:endsWithSearchBoundary:]](https://developer.apple.com/documentation/appkit/nstextfinderclient/1529466-string)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextFinderClient stringLength]](https://developer.apple.com/documentation/appkit/nstextfinderclient/1534333-stringlength)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [NSTextFinderClient.visibleCharacterRanges](https://developer.apple.com/documentation/appkit/nstextfinderclient/1524834-visiblecharacterranges)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *visibleCharacterRanges ``` |
| To | ``` @property(readonly, copy) NSArray *visibleCharacterRanges ``` |

NSTextInputClient.hModified [-[NSTextInputClient attributedString]](https://developer.apple.com/documentation/appkit/nstextinputclient/1438232-attributedstring)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextInputClient baselineDeltaForCharacterAtIndex:]](https://developer.apple.com/documentation/appkit/nstextinputclient/1438254-baselinedeltaforcharacteratindex)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextInputClient drawsVerticallyForCharacterAtIndex:]](https://developer.apple.com/documentation/appkit/nstextinputclient/1438252-drawsverticallyforcharacteratind)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextInputClient fractionOfDistanceThroughGlyphForPoint:]](https://developer.apple.com/documentation/appkit/nstextinputclient/1438236-fractionofdistancethroughglyphfo)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextInputClient windowLevel]](https://developer.apple.com/documentation/appkit/nstextinputclient/1438248-windowlevel)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSTextInputContext.hModified [-[NSTextInputContext initWithClient:]](https://developer.apple.com/documentation/appkit/nstextinputcontext/1532777-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithClient:(id<NSTextInputClient>)theClient ``` |
| To | ``` - (instancetype)initWithClient:(id<NSTextInputClient>)theClient ``` |

NSTextList.hRemoved [-[NSTextList listOptions]](https://developer.apple.com/documentation/appkit/nstextlist/1533519-listoptions)Removed [-[NSTextList markerFormat]](https://developer.apple.com/documentation/appkit/nstextlist/1533865-markerformat)Removed [-[NSTextList setStartingItemNumber:]](https://developer.apple.com/documentation/appkit/nstextlist/1528597-startingitemnumber)Removed [-[NSTextList startingItemNumber]](https://developer.apple.com/documentation/appkit/nstextlist/1528597-startingitemnumber)Added [NSTextList.listOptions](https://developer.apple.com/documentation/appkit/nstextlist/1533519-listoptions)Added [NSTextList.markerFormat](https://developer.apple.com/documentation/appkit/nstextlist/1533865-markerformat)Added [NSTextList.startingItemNumber](https://developer.apple.com/documentation/appkit/nstextlist/1528597-startingitemnumber)Added [NSTextListOptions](https://developer.apple.com/documentation/appkit/nstextlistoptions)Modified [-[NSTextList initWithMarkerFormat:options:]](https://developer.apple.com/documentation/appkit/nstextlist/1526123-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithMarkerFormat:(NSString *)format options:(NSUInteger)mask ``` |
| To | ``` - (instancetype)initWithMarkerFormat:(NSString *)format options:(NSUInteger)mask ``` |

NSTextStorage.hRemoved [-[NSTextStorage changeInLength]](https://developer.apple.com/documentation/uikit/nstextstorage/1528400-changeinlength)Removed [-[NSTextStorage delegate]](https://developer.apple.com/documentation/appkit/nstextstorage/1532704-delegate)Removed [-[NSTextStorage editedMask]](https://developer.apple.com/documentation/uikit/nstextstorage/1525323-editedmask)Removed [-[NSTextStorage editedRange]](https://developer.apple.com/documentation/uikit/nstextstorage/1524379-editedrange)Removed [-[NSTextStorage fixesAttributesLazily]](https://developer.apple.com/documentation/appkit/nstextstorage/1532043-fixesattributeslazily)Removed [-[NSTextStorage layoutManagers]](https://developer.apple.com/documentation/uikit/nstextstorage/1527938-layoutmanagers)Removed [-[NSTextStorage setDelegate:]](https://developer.apple.com/documentation/appkit/nstextstorage/1532704-delegate)Added [NSTextStorage.changeInLength](https://developer.apple.com/documentation/uikit/nstextstorage/1528400-changeinlength)Added [NSTextStorage.delegate](https://developer.apple.com/documentation/uikit/nstextstorage/1532704-delegate)Added [NSTextStorage.editedMask](https://developer.apple.com/documentation/appkit/nstextstorage/1525323-editedmask)Added [NSTextStorage.editedRange](https://developer.apple.com/documentation/appkit/nstextstorage/1524379-editedrange)Added [NSTextStorage.fixesAttributesLazily](https://developer.apple.com/documentation/uikit/nstextstorage/1532043-fixesattributeslazily)Added [NSTextStorage.layoutManagers](https://developer.apple.com/documentation/uikit/nstextstorage/1527938-layoutmanagers)Added [NSTextStorageEditedOptions](https://developer.apple.com/documentation/appkit/nstextstorageeditedoptions)Modified [-[NSTextStorageDelegate textStorageDidProcessEditing:]](https://developer.apple.com/documentation/uikit/nstextstoragedelegate/1808521-textstoragedidprocessediting)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextStorageDelegate textStorageWillProcessEditing:]](https://developer.apple.com/documentation/appkit/nstextstoragedelegate/1808519-textstoragewillprocessediting)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSTextStorageScripting.hRemoved [-[NSTextStorage attributeRuns]](https://developer.apple.com/documentation/appkit/nstextstorage/1532095-attributeruns)Removed [-[NSTextStorage characters]](https://developer.apple.com/documentation/appkit/nstextstorage/1535788-characters)Removed [-[NSTextStorage font]](https://developer.apple.com/documentation/appkit/nstextstorage/1535365-font)Removed [-[NSTextStorage foregroundColor]](https://developer.apple.com/documentation/appkit/nstextstorage/1527175-foregroundcolor)Removed [-[NSTextStorage paragraphs]](https://developer.apple.com/documentation/appkit/nstextstorage/1525943-paragraphs)Removed [-[NSTextStorage setAttributeRuns:]](https://developer.apple.com/documentation/appkit/nstextstorage/1532095-attributeruns)Removed [-[NSTextStorage setCharacters:]](https://developer.apple.com/documentation/appkit/nstextstorage/1535788-characters)Removed [-[NSTextStorage setFont:]](https://developer.apple.com/documentation/appkit/nstextstorage/1535365-font)Removed [-[NSTextStorage setForegroundColor:]](https://developer.apple.com/documentation/appkit/nstextstorage/1527175-foregroundcolor)Removed [-[NSTextStorage setParagraphs:]](https://developer.apple.com/documentation/appkit/nstextstorage/1525943-paragraphs)Removed [-[NSTextStorage setWords:]](https://developer.apple.com/documentation/appkit/nstextstorage/1524565-words)Removed [-[NSTextStorage words]](https://developer.apple.com/documentation/appkit/nstextstorage/1524565-words)Added [NSTextStorage.attributeRuns](https://developer.apple.com/documentation/appkit/nstextstorage/1532095-attributeruns)Added [NSTextStorage.characters](https://developer.apple.com/documentation/appkit/nstextstorage/1535788-characters)Added [NSTextStorage.font](https://developer.apple.com/documentation/appkit/nstextstorage/1535365-font)Added [NSTextStorage.foregroundColor](https://developer.apple.com/documentation/appkit/nstextstorage/1527175-foregroundcolor)Added [NSTextStorage.paragraphs](https://developer.apple.com/documentation/appkit/nstextstorage/1525943-paragraphs)Added [NSTextStorage.words](https://developer.apple.com/documentation/appkit/nstextstorage/1524565-words)NSTextTable.hRemoved [-[NSTextBlock backgroundColor]](https://developer.apple.com/documentation/appkit/nstextblock/1527300-backgroundcolor)Removed [-[NSTextBlock contentWidth]](https://developer.apple.com/documentation/appkit/nstextblock/1532506-contentwidth)Removed [-[NSTextBlock contentWidthValueType]](https://developer.apple.com/documentation/appkit/nstextblock/1525975-contentwidthvaluetype)Removed [-[NSTextBlock setBackgroundColor:]](https://developer.apple.com/documentation/appkit/nstextblock/1527300-backgroundcolor)Removed [-[NSTextBlock setVerticalAlignment:]](https://developer.apple.com/documentation/appkit/nstextblock/1533097-verticalalignment)Removed [-[NSTextBlock verticalAlignment]](https://developer.apple.com/documentation/appkit/nstextblock/1533097-verticalalignment)Removed [-[NSTextTable collapsesBorders]](https://developer.apple.com/documentation/appkit/nstexttable/1534170-collapsesborders)Removed [-[NSTextTable hidesEmptyCells]](https://developer.apple.com/documentation/appkit/nstexttable/1526288-hidesemptycells)Removed [-[NSTextTable layoutAlgorithm]](https://developer.apple.com/documentation/appkit/nstexttable/1531734-layoutalgorithm)Removed [-[NSTextTable numberOfColumns]](https://developer.apple.com/documentation/appkit/nstexttable/1532413-numberofcolumns)Removed [-[NSTextTable setCollapsesBorders:]](https://developer.apple.com/documentation/appkit/nstexttable/1534170-collapsesborders)Removed [-[NSTextTable setHidesEmptyCells:]](https://developer.apple.com/documentation/appkit/nstexttable/1526288-hidesemptycells)Removed [-[NSTextTable setLayoutAlgorithm:]](https://developer.apple.com/documentation/appkit/nstexttable/1531734-layoutalgorithm)Removed [-[NSTextTable setNumberOfColumns:]](https://developer.apple.com/documentation/appkit/nstexttable/1532413-numberofcolumns)Removed [-[NSTextTableBlock columnSpan]](https://developer.apple.com/documentation/appkit/nstexttableblock/1528568-columnspan)Removed [-[NSTextTableBlock rowSpan]](https://developer.apple.com/documentation/appkit/nstexttableblock/1528586-rowspan)Removed [-[NSTextTableBlock startingColumn]](https://developer.apple.com/documentation/appkit/nstexttableblock/1525383-startingcolumn)Removed [-[NSTextTableBlock startingRow]](https://developer.apple.com/documentation/appkit/nstexttableblock/1525803-startingrow)Removed [-[NSTextTableBlock table]](https://developer.apple.com/documentation/appkit/nstexttableblock/1525141-table)Added [NSTextBlock.backgroundColor](https://developer.apple.com/documentation/appkit/nstextblock/1527300-backgroundcolor)Added [NSTextBlock.contentWidth](https://developer.apple.com/documentation/appkit/nstextblock/1532506-contentwidth)Added [NSTextBlock.contentWidthValueType](https://developer.apple.com/documentation/appkit/nstextblock/1525975-contentwidthvaluetype)Added [NSTextBlock.verticalAlignment](https://developer.apple.com/documentation/appkit/nstextblock/1533097-verticalalignment)Added [NSTextTable.collapsesBorders](https://developer.apple.com/documentation/appkit/nstexttable/1534170-collapsesborders)Added [NSTextTable.hidesEmptyCells](https://developer.apple.com/documentation/appkit/nstexttable/1526288-hidesemptycells)Added [NSTextTable.layoutAlgorithm](https://developer.apple.com/documentation/appkit/nstexttable/1531734-layoutalgorithm)Added [NSTextTable.numberOfColumns](https://developer.apple.com/documentation/appkit/nstexttable/1532413-numberofcolumns)Added [NSTextTableBlock.columnSpan](https://developer.apple.com/documentation/appkit/nstexttableblock/1528568-columnspan)Added [NSTextTableBlock.rowSpan](https://developer.apple.com/documentation/appkit/nstexttableblock/1528586-rowspan)Added [NSTextTableBlock.startingColumn](https://developer.apple.com/documentation/appkit/nstexttableblock/1525383-startingcolumn)Added [NSTextTableBlock.startingRow](https://developer.apple.com/documentation/appkit/nstexttableblock/1525803-startingrow)Added [NSTextTableBlock.table](https://developer.apple.com/documentation/appkit/nstexttableblock/1525141-table)Modified [-[NSTextBlock init]](https://developer.apple.com/documentation/appkit/nstextblock/1528169-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

Modified [-[NSTextTableBlock initWithTable:startingRow:rowSpan:startingColumn:columnSpan:]](https://developer.apple.com/documentation/appkit/nstexttableblock/1532894-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTable:(NSTextTable *)table startingRow:(NSInteger)row rowSpan:(NSInteger)rowSpan startingColumn:(NSInteger)col columnSpan:(NSInteger)colSpan ``` |
| To | ``` - (instancetype)initWithTable:(NSTextTable *)table startingRow:(NSInteger)row rowSpan:(NSInteger)rowSpan startingColumn:(NSInteger)col columnSpan:(NSInteger)colSpan ``` |

NSTextView.hRemoved [-[NSTextView acceptableDragTypes]](https://developer.apple.com/documentation/appkit/nstextview/1449234-acceptabledragtypes)Removed [-[NSTextView acceptsGlyphInfo]](https://developer.apple.com/documentation/appkit/nstextview/1449163-acceptsglyphinfo)Removed [-[NSTextView allowedInputSourceLocales]](https://developer.apple.com/documentation/appkit/nstextview/1449370-allowedinputsourcelocales)Removed [-[NSTextView allowsDocumentBackgroundColorChange]](https://developer.apple.com/documentation/appkit/nstextview/1449397-allowsdocumentbackgroundcolorcha)Removed [-[NSTextView allowsImageEditing]](https://developer.apple.com/documentation/appkit/nstextview/1449425-allowsimageediting)Removed [-[NSTextView allowsUndo]](https://developer.apple.com/documentation/appkit/nstextview/1449450-allowsundo)Removed [-[NSTextView backgroundColor]](https://developer.apple.com/documentation/appkit/nstextview/1449501-backgroundcolor)Removed [-[NSTextView defaultParagraphStyle]](https://developer.apple.com/documentation/appkit/nstextview/1449271-defaultparagraphstyle)Removed [-[NSTextView delegate]](https://developer.apple.com/documentation/appkit/nstextview/1449521-delegate)Removed [-[NSTextView displaysLinkToolTips]](https://developer.apple.com/documentation/appkit/nstextview/1449204-displayslinktooltips)Removed [-[NSTextView drawsBackground]](https://developer.apple.com/documentation/appkit/nstextview/1449530-drawsbackground)Removed [-[NSTextView enabledTextCheckingTypes]](https://developer.apple.com/documentation/appkit/nstextview/1449529-enabledtextcheckingtypes)Removed [-[NSTextView importsGraphics]](https://developer.apple.com/documentation/appkit/nstextview/1449266-importsgraphics)Removed [-[NSTextView insertionPointColor]](https://developer.apple.com/documentation/appkit/nstextview/1449309-insertionpointcolor)Removed [-[NSTextView isAutomaticDashSubstitutionEnabled]](https://developer.apple.com/documentation/appkit/nstextview/1449403-automaticdashsubstitutionenabled)Removed [-[NSTextView isAutomaticDataDetectionEnabled]](https://developer.apple.com/documentation/appkit/nstextview/1449192-automaticdatadetectionenabled)Removed [-[NSTextView isAutomaticLinkDetectionEnabled]](https://developer.apple.com/documentation/appkit/nstextview/1449170-automaticlinkdetectionenabled)Removed [-[NSTextView isAutomaticQuoteSubstitutionEnabled]](https://developer.apple.com/documentation/appkit/nstextview/1449258-automaticquotesubstitutionenable)Removed [-[NSTextView isAutomaticSpellingCorrectionEnabled]](https://developer.apple.com/documentation/appkit/nstextview/1449254-automaticspellingcorrectionenabl)Removed [-[NSTextView isAutomaticTextReplacementEnabled]](https://developer.apple.com/documentation/appkit/nstextview/1449210-automatictextreplacementenabled)Removed [-[NSTextView isCoalescingUndo]](https://developer.apple.com/documentation/appkit/nstextview/1449368-coalescingundo)Removed [-[NSTextView isContinuousSpellCheckingEnabled]](https://developer.apple.com/documentation/appkit/nstextview/1449430-continuousspellcheckingenabled)Removed [-[NSTextView isEditable]](https://developer.apple.com/documentation/appkit/nstextview/1449345-editable)Removed [-[NSTextView isFieldEditor]](https://developer.apple.com/documentation/appkit/nstextview/1449156-fieldeditor)Removed [-[NSTextView isGrammarCheckingEnabled]](https://developer.apple.com/documentation/appkit/nstextview/1449166-isgrammarcheckingenabled)Removed [-[NSTextView isIncrementalSearchingEnabled]](https://developer.apple.com/documentation/appkit/nstextview/1449458-incrementalsearchingenabled)Removed [-[NSTextView isRichText]](https://developer.apple.com/documentation/appkit/nstextview/1449538-isrichtext)Removed [-[NSTextView isRulerVisible]](https://developer.apple.com/documentation/appkit/nstextview/1449406-rulervisible)Removed [-[NSTextView isSelectable]](https://developer.apple.com/documentation/appkit/nstextview/1449297-isselectable)Removed [-[NSTextView layoutManager]](https://developer.apple.com/documentation/appkit/nstextview/1449148-layoutmanager)Removed [-[NSTextView linkTextAttributes]](https://developer.apple.com/documentation/appkit/nstextview/1449452-linktextattributes)Removed [-[NSTextView markedTextAttributes]](https://developer.apple.com/documentation/appkit/nstextview/1449179-markedtextattributes)Removed [-[NSTextView rangeForUserCharacterAttributeChange]](https://developer.apple.com/documentation/appkit/nstextview/1449392-rangeforusercharacterattributech)Removed [-[NSTextView rangeForUserCompletion]](https://developer.apple.com/documentation/appkit/nstextview/1449329-rangeforusercompletion)Removed [-[NSTextView rangeForUserParagraphAttributeChange]](https://developer.apple.com/documentation/appkit/nstextview/1449252-rangeforuserparagraphattributech)Removed [-[NSTextView rangeForUserTextChange]](https://developer.apple.com/documentation/appkit/nstextview/1449315-rangeforusertextchange)Removed [-[NSTextView rangesForUserCharacterAttributeChange]](https://developer.apple.com/documentation/appkit/nstextview/1449503-rangesforusercharacterattributec)Removed [-[NSTextView rangesForUserParagraphAttributeChange]](https://developer.apple.com/documentation/appkit/nstextview/1449161-rangesforuserparagraphattributec)Removed [-[NSTextView rangesForUserTextChange]](https://developer.apple.com/documentation/appkit/nstextview/1449434-rangesforusertextchange)Removed [-[NSTextView readablePasteboardTypes]](https://developer.apple.com/documentation/appkit/nstextview/1449361-readablepasteboardtypes)Removed [-[NSTextView selectedRanges]](https://developer.apple.com/documentation/appkit/nstextview/1449129-selectedranges)Removed [-[NSTextView selectedTextAttributes]](https://developer.apple.com/documentation/appkit/nstextview/1449270-selectedtextattributes)Removed [-[NSTextView selectionAffinity]](https://developer.apple.com/documentation/appkit/nstextview/1449291-selectionaffinity)Removed [-[NSTextView selectionGranularity]](https://developer.apple.com/documentation/appkit/nstextview/1449165-selectiongranularity)Removed [-[NSTextView setAcceptsGlyphInfo:]](https://developer.apple.com/documentation/appkit/nstextview/1449163-acceptsglyphinfo)Removed [-[NSTextView setAllowedInputSourceLocales:]](https://developer.apple.com/documentation/appkit/nstextview/1449370-allowedinputsourcelocales)Removed [-[NSTextView setAllowsDocumentBackgroundColorChange:]](https://developer.apple.com/documentation/appkit/nstextview/1449397-allowsdocumentbackgroundcolorcha)Removed [-[NSTextView setAllowsImageEditing:]](https://developer.apple.com/documentation/appkit/nstextview/1449425-allowsimageediting)Removed [-[NSTextView setAllowsUndo:]](https://developer.apple.com/documentation/appkit/nstextview/1449450-allowsundo)Removed [-[NSTextView setAutomaticDashSubstitutionEnabled:]](https://developer.apple.com/documentation/appkit/nstextview/1449403-automaticdashsubstitutionenabled)Removed [-[NSTextView setAutomaticDataDetectionEnabled:]](https://developer.apple.com/documentation/appkit/nstextview/1449192-automaticdatadetectionenabled)Removed [-[NSTextView setAutomaticLinkDetectionEnabled:]](https://developer.apple.com/documentation/appkit/nstextview/1449170-automaticlinkdetectionenabled)Removed [-[NSTextView setAutomaticQuoteSubstitutionEnabled:]](https://developer.apple.com/documentation/appkit/nstextview/1449258-automaticquotesubstitutionenable)Removed [-[NSTextView setAutomaticSpellingCorrectionEnabled:]](https://developer.apple.com/documentation/appkit/nstextview/1449254-automaticspellingcorrectionenabl)Removed [-[NSTextView setAutomaticTextReplacementEnabled:]](https://developer.apple.com/documentation/appkit/nstextview/1449210-isautomatictextreplacementenable)Removed [-[NSTextView setBackgroundColor:]](https://developer.apple.com/documentation/appkit/nstextview/1449501-backgroundcolor)Removed [-[NSTextView setContinuousSpellCheckingEnabled:]](https://developer.apple.com/documentation/appkit/nstextview/1449430-continuousspellcheckingenabled)Removed [-[NSTextView setDefaultParagraphStyle:]](https://developer.apple.com/documentation/appkit/nstextview/1449271-defaultparagraphstyle)Removed [-[NSTextView setDelegate:]](https://developer.apple.com/documentation/appkit/nstextview/1449521-delegate)Removed [-[NSTextView setDisplaysLinkToolTips:]](https://developer.apple.com/documentation/appkit/nstextview/1449204-displayslinktooltips)Removed [-[NSTextView setDrawsBackground:]](https://developer.apple.com/documentation/appkit/nstextview/1449530-drawsbackground)Removed [-[NSTextView setEditable:]](https://developer.apple.com/documentation/appkit/nstextview/1449345-iseditable)Removed [-[NSTextView setEnabledTextCheckingTypes:]](https://developer.apple.com/documentation/appkit/nstextview/1449529-enabledtextcheckingtypes)Removed [-[NSTextView setFieldEditor:]](https://developer.apple.com/documentation/appkit/nstextview/1449156-fieldeditor)Removed [-[NSTextView setGrammarCheckingEnabled:]](https://developer.apple.com/documentation/appkit/nstextview/1449166-isgrammarcheckingenabled)Removed [-[NSTextView setImportsGraphics:]](https://developer.apple.com/documentation/appkit/nstextview/1449266-importsgraphics)Removed [-[NSTextView setIncrementalSearchingEnabled:]](https://developer.apple.com/documentation/appkit/nstextview/1449458-incrementalsearchingenabled)Removed [-[NSTextView setInsertionPointColor:]](https://developer.apple.com/documentation/appkit/nstextview/1449309-insertionpointcolor)Removed [-[NSTextView setLinkTextAttributes:]](https://developer.apple.com/documentation/appkit/nstextview/1449452-linktextattributes)Removed [-[NSTextView setMarkedTextAttributes:]](https://developer.apple.com/documentation/appkit/nstextview/1449179-markedtextattributes)Removed [-[NSTextView setRichText:]](https://developer.apple.com/documentation/appkit/nstextview/1449538-richtext)Removed [-[NSTextView setRulerVisible:]](https://developer.apple.com/documentation/appkit/nstextview/1449406-isrulervisible)Removed [-[NSTextView setSelectable:]](https://developer.apple.com/documentation/appkit/nstextview/1449297-isselectable)Removed [-[NSTextView setSelectedRanges:]](https://developer.apple.com/documentation/appkit/nstextview/1449129-selectedranges)Removed [-[NSTextView setSelectedTextAttributes:]](https://developer.apple.com/documentation/appkit/nstextview/1449270-selectedtextattributes)Removed [-[NSTextView setSelectionGranularity:]](https://developer.apple.com/documentation/appkit/nstextview/1449165-selectiongranularity)Removed [-[NSTextView setSmartInsertDeleteEnabled:]](https://developer.apple.com/documentation/appkit/nstextview/1449236-smartinsertdeleteenabled)Removed [-[NSTextView setTextContainer:]](https://developer.apple.com/documentation/appkit/nstextview/1449364-textcontainer)Removed [-[NSTextView setTextContainerInset:]](https://developer.apple.com/documentation/appkit/nstextview/1449168-textcontainerinset)Removed [-[NSTextView setTypingAttributes:]](https://developer.apple.com/documentation/appkit/nstextview/1449487-typingattributes)Removed [-[NSTextView setUsesFindBar:]](https://developer.apple.com/documentation/appkit/nstextview/1449456-usesfindbar)Removed [-[NSTextView setUsesFindPanel:]](https://developer.apple.com/documentation/appkit/nstextview/1449293-usesfindpanel)Removed [-[NSTextView setUsesFontPanel:]](https://developer.apple.com/documentation/appkit/nstextview/1449534-usesfontpanel)Removed [-[NSTextView setUsesInspectorBar:]](https://developer.apple.com/documentation/appkit/nstextview/1449407-usesinspectorbar)Removed [-[NSTextView setUsesRuler:]](https://developer.apple.com/documentation/appkit/nstextview/1449218-usesruler)Removed [-[NSTextView shouldDrawInsertionPoint]](https://developer.apple.com/documentation/appkit/nstextview/1449152-shoulddrawinsertionpoint)Removed [-[NSTextView smartInsertDeleteEnabled]](https://developer.apple.com/documentation/appkit/nstextview/1449236-smartinsertdeleteenabled)Removed [-[NSTextView spellCheckerDocumentTag]](https://developer.apple.com/documentation/appkit/nstextview/1449513-spellcheckerdocumenttag)Removed [-[NSTextView textContainer]](https://developer.apple.com/documentation/appkit/nstextview/1449364-textcontainer)Removed [-[NSTextView textContainerInset]](https://developer.apple.com/documentation/appkit/nstextview/1449168-textcontainerinset)Removed [-[NSTextView textContainerOrigin]](https://developer.apple.com/documentation/appkit/nstextview/1449477-textcontainerorigin)Removed [-[NSTextView textStorage]](https://developer.apple.com/documentation/appkit/nstextview/1449196-textstorage)Removed [-[NSTextView typingAttributes]](https://developer.apple.com/documentation/appkit/nstextview/1449487-typingattributes)Removed [-[NSTextView usesFindBar]](https://developer.apple.com/documentation/appkit/nstextview/1449456-usesfindbar)Removed [-[NSTextView usesFindPanel]](https://developer.apple.com/documentation/appkit/nstextview/1449293-usesfindpanel)Removed [-[NSTextView usesFontPanel]](https://developer.apple.com/documentation/appkit/nstextview/1449534-usesfontpanel)Removed [-[NSTextView usesInspectorBar]](https://developer.apple.com/documentation/appkit/nstextview/1449407-usesinspectorbar)Removed [-[NSTextView usesRuler]](https://developer.apple.com/documentation/appkit/nstextview/1449218-usesruler)Removed [-[NSTextView writablePasteboardTypes]](https://developer.apple.com/documentation/appkit/nstextview/1449222-writablepasteboardtypes)Added [NSTextView.acceptableDragTypes](https://developer.apple.com/documentation/appkit/nstextview/1449234-acceptabledragtypes)Added [NSTextView.acceptsGlyphInfo](https://developer.apple.com/documentation/appkit/nstextview/1449163-acceptsglyphinfo)Added [NSTextView.allowedInputSourceLocales](https://developer.apple.com/documentation/appkit/nstextview/1449370-allowedinputsourcelocales)Added [NSTextView.allowsDocumentBackgroundColorChange](https://developer.apple.com/documentation/appkit/nstextview/1449397-allowsdocumentbackgroundcolorcha)Added [NSTextView.allowsImageEditing](https://developer.apple.com/documentation/appkit/nstextview/1449425-allowsimageediting)Added [NSTextView.allowsUndo](https://developer.apple.com/documentation/appkit/nstextview/1449450-allowsundo)Added [NSTextView.automaticDashSubstitutionEnabled](https://developer.apple.com/documentation/appkit/nstextview/1449403-isautomaticdashsubstitutionenabl)Added [NSTextView.automaticDataDetectionEnabled](https://developer.apple.com/documentation/appkit/nstextview/1449192-isautomaticdatadetectionenabled)Added [NSTextView.automaticLinkDetectionEnabled](https://developer.apple.com/documentation/appkit/nstextview/1449170-isautomaticlinkdetectionenabled)Added [NSTextView.automaticQuoteSubstitutionEnabled](https://developer.apple.com/documentation/appkit/nstextview/1449258-isautomaticquotesubstitutionenab)Added [NSTextView.automaticSpellingCorrectionEnabled](https://developer.apple.com/documentation/appkit/nstextview/1449254-isautomaticspellingcorrectionena)Added [NSTextView.automaticTextReplacementEnabled](https://developer.apple.com/documentation/appkit/nstextview/1449210-isautomatictextreplacementenable)Added [NSTextView.backgroundColor](https://developer.apple.com/documentation/appkit/nstextview/1449501-backgroundcolor)Added [NSTextView.coalescingUndo](https://developer.apple.com/documentation/appkit/nstextview/1449368-coalescingundo)Added [NSTextView.continuousSpellCheckingEnabled](https://developer.apple.com/documentation/appkit/nstextview/1449430-continuousspellcheckingenabled)Added [NSTextView.defaultParagraphStyle](https://developer.apple.com/documentation/appkit/nstextview/1449271-defaultparagraphstyle)Added [NSTextView.delegate](https://developer.apple.com/documentation/appkit/nstextview/1449521-delegate)Added [NSTextView.displaysLinkToolTips](https://developer.apple.com/documentation/appkit/nstextview/1449204-displayslinktooltips)Added [NSTextView.drawsBackground](https://developer.apple.com/documentation/appkit/nstextview/1449530-drawsbackground)Added [NSTextView.editable](https://developer.apple.com/documentation/appkit/nstextview/1449345-editable)Added [NSTextView.enabledTextCheckingTypes](https://developer.apple.com/documentation/appkit/nstextview/1449529-enabledtextcheckingtypes)Added [NSTextView.fieldEditor](https://developer.apple.com/documentation/appkit/nstextview/1449156-isfieldeditor)Added [NSTextView.grammarCheckingEnabled](https://developer.apple.com/documentation/appkit/nstextview/1449166-isgrammarcheckingenabled)Added [NSTextView.importsGraphics](https://developer.apple.com/documentation/appkit/nstextview/1449266-importsgraphics)Added [NSTextView.incrementalSearchingEnabled](https://developer.apple.com/documentation/appkit/nstextview/1449458-incrementalsearchingenabled)Added [-[NSTextView initWithCoder:]](https://developer.apple.com/documentation/appkit/nstextview/1449489-initwithcoder)Added [NSTextView.insertionPointColor](https://developer.apple.com/documentation/appkit/nstextview/1449309-insertionpointcolor)Added [NSTextView.layoutManager](https://developer.apple.com/documentation/appkit/nstextview/1449148-layoutmanager)Added [NSTextView.linkTextAttributes](https://developer.apple.com/documentation/appkit/nstextview/1449452-linktextattributes)Added [NSTextView.markedTextAttributes](https://developer.apple.com/documentation/appkit/nstextview/1449179-markedtextattributes)Added [NSTextView.rangeForUserCharacterAttributeChange](https://developer.apple.com/documentation/appkit/nstextview/1449392-rangeforusercharacterattributech)Added [NSTextView.rangeForUserCompletion](https://developer.apple.com/documentation/appkit/nstextview/1449329-rangeforusercompletion)Added [NSTextView.rangeForUserParagraphAttributeChange](https://developer.apple.com/documentation/appkit/nstextview/1449252-rangeforuserparagraphattributech)Added [NSTextView.rangeForUserTextChange](https://developer.apple.com/documentation/appkit/nstextview/1449315-rangeforusertextchange)Added [NSTextView.rangesForUserCharacterAttributeChange](https://developer.apple.com/documentation/appkit/nstextview/1449503-rangesforusercharacterattributec)Added [NSTextView.rangesForUserParagraphAttributeChange](https://developer.apple.com/documentation/appkit/nstextview/1449161-rangesforuserparagraphattributec)Added [NSTextView.rangesForUserTextChange](https://developer.apple.com/documentation/appkit/nstextview/1449434-rangesforusertextchange)Added [NSTextView.readablePasteboardTypes](https://developer.apple.com/documentation/appkit/nstextview/1449361-readablepasteboardtypes)Added [NSTextView.richText](https://developer.apple.com/documentation/appkit/nstextview/1449538-isrichtext)Added [NSTextView.rulerVisible](https://developer.apple.com/documentation/appkit/nstextview/1449406-rulervisible)Added [NSTextView.selectable](https://developer.apple.com/documentation/appkit/nstextview/1449297-selectable)Added [NSTextView.selectedRanges](https://developer.apple.com/documentation/appkit/nstextview/1449129-selectedranges)Added [NSTextView.selectedTextAttributes](https://developer.apple.com/documentation/appkit/nstextview/1449270-selectedtextattributes)Added [NSTextView.selectionAffinity](https://developer.apple.com/documentation/appkit/nstextview/1449291-selectionaffinity)Added [NSTextView.selectionGranularity](https://developer.apple.com/documentation/appkit/nstextview/1449165-selectiongranularity)Added [NSTextView.shouldDrawInsertionPoint](https://developer.apple.com/documentation/appkit/nstextview/1449152-shoulddrawinsertionpoint)Added [NSTextView.smartInsertDeleteEnabled](https://developer.apple.com/documentation/appkit/nstextview/1449236-smartinsertdeleteenabled)Added [NSTextView.spellCheckerDocumentTag](https://developer.apple.com/documentation/appkit/nstextview/1449513-spellcheckerdocumenttag)Added [NSTextView.textContainer](https://developer.apple.com/documentation/appkit/nstextview/1449364-textcontainer)Added [NSTextView.textContainerInset](https://developer.apple.com/documentation/appkit/nstextview/1449168-textcontainerinset)Added [NSTextView.textContainerOrigin](https://developer.apple.com/documentation/appkit/nstextview/1449477-textcontainerorigin)Added [NSTextView.textStorage](https://developer.apple.com/documentation/appkit/nstextview/1449196-textstorage)Added [NSTextView.typingAttributes](https://developer.apple.com/documentation/appkit/nstextview/1449487-typingattributes)Added [NSTextView.usesFindBar](https://developer.apple.com/documentation/appkit/nstextview/1449456-usesfindbar)Added [NSTextView.usesFindPanel](https://developer.apple.com/documentation/appkit/nstextview/1449293-usesfindpanel)Added [NSTextView.usesFontPanel](https://developer.apple.com/documentation/appkit/nstextview/1449534-usesfontpanel)Added [NSTextView.usesInspectorBar](https://developer.apple.com/documentation/appkit/nstextview/1449407-usesinspectorbar)Added [NSTextView.usesRolloverButtonForSelection](https://developer.apple.com/documentation/appkit/nstextview/1449357-usesrolloverbuttonforselection)Added [NSTextView.usesRuler](https://developer.apple.com/documentation/appkit/nstextview/1449218-usesruler)Added [NSTextView.writablePasteboardTypes](https://developer.apple.com/documentation/appkit/nstextview/1449222-writablepasteboardtypes)Modified [NSTextView](https://developer.apple.com/documentation/appkit/nstextview)

|  | Protocols |
| --- | --- |
| From | NSDraggingSource, NSTextInput, NSTextInputClient, NSTextLayoutOrientationProvider, NSUserInterfaceValidations |
| To | NSAccessibilityNavigableStaticText, NSDraggingSource, NSTextInput, NSTextInputClient, NSTextLayoutOrientationProvider, NSUserInterfaceValidations |

Modified [-[NSTextView initWithFrame:]](https://developer.apple.com/documentation/appkit/nstextview/1449262-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFrame:(NSRect)frameRect ``` |
| To | ``` - (instancetype)initWithFrame:(NSRect)frameRect ``` |

Modified [-[NSTextView initWithFrame:textContainer:]](https://developer.apple.com/documentation/appkit/nstextview/1449347-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithFrame:(NSRect)frameRect textContainer:(NSTextContainer *)container ``` | -- |
| To | ``` - (instancetype)initWithFrame:(NSRect)frameRect textContainer:(NSTextContainer *)container ``` | yes |

Modified [-[NSTextView orderFrontSharingServicePicker:]](https://developer.apple.com/documentation/appkit/nstextview/1449150-orderfrontsharingservicepicker)

|  | Declaration |
| --- | --- |
| From | ``` - (void)orderFrontSharingServicePicker:(id)sender ``` |
| To | ``` - (IBAction)orderFrontSharingServicePicker:(id)sender ``` |

Modified [-[NSTextView toggleQuickLookPreviewPanel:]](https://developer.apple.com/documentation/appkit/nstextview/1449415-togglequicklookpreviewpanel)

|  | Declaration |
| --- | --- |
| From | ``` - (void)toggleQuickLookPreviewPanel:(id)sender ``` |
| To | ``` - (IBAction)toggleQuickLookPreviewPanel:(id)sender ``` |

Modified [-[NSTextViewDelegate textView:URLForContentsOfTextAttachment:atIndex:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449194-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate textView:clickedOnCell:inRect:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449495-textview)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.6 | yes |

Modified [-[NSTextViewDelegate textView:clickedOnCell:inRect:atIndex:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449335-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate textView:clickedOnLink:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449380-textview)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.6 | yes |

Modified [-[NSTextViewDelegate textView:clickedOnLink:atIndex:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449527-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate textView:completions:forPartialWordRange:indexOfSelectedItem:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449260-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate textView:didCheckTextInRange:types:options:results:orthography:wordCount:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449317-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate textView:doCommandBySelector:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449419-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate textView:doubleClickedOnCell:inRect:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449374-textview)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.6 | yes |

Modified [-[NSTextViewDelegate textView:doubleClickedOnCell:inRect:atIndex:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449333-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate textView:draggedCell:inRect:event:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449185-textview)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.6 | yes |

Modified [-[NSTextViewDelegate textView:draggedCell:inRect:event:atIndex:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449154-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate textView:menu:forEvent:atIndex:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449341-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate textView:shouldChangeTextInRange:replacementString:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449325-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate textView:shouldChangeTextInRanges:replacementStrings:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449206-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate textView:shouldChangeTypingAttributes:toAttributes:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449376-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate textView:shouldSetSpellingState:range:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449284-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate textView:willChangeSelectionFromCharacterRange:toCharacterRange:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449227-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate textView:willChangeSelectionFromCharacterRanges:toCharacterRanges:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449264-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate textView:willCheckTextInRange:options:types:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449307-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate textView:willDisplayToolTip:forCharacterAtIndex:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449411-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate textView:willShowSharingServicePicker:forItems:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449339-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate textView:writablePasteboardTypesForCell:atIndex:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449485-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate textView:writeCell:atIndex:toPasteboard:type:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449294-textview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate textViewDidChangeSelection:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449363-textviewdidchangeselection)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate textViewDidChangeTypingAttributes:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449303-textviewdidchangetypingattribute)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTextViewDelegate undoManagerForTextView:]](https://developer.apple.com/documentation/appkit/nstextviewdelegate/1449225-undomanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSTitlebarAccessoryViewController.h (Added)Added [NSTitlebarAccessoryViewController](https://developer.apple.com/documentation/appkit/nstitlebaraccessoryviewcontroller)Added [NSTitlebarAccessoryViewController.fullScreenMinHeight](https://developer.apple.com/documentation/appkit/nstitlebaraccessoryviewcontroller/1397782-fullscreenminheight)Added [NSTitlebarAccessoryViewController.layoutAttribute](https://developer.apple.com/documentation/appkit/nstitlebaraccessoryviewcontroller/1397778-layoutattribute)Added [-[NSTitlebarAccessoryViewController viewDidAppear]](https://developer.apple.com/documentation/appkit/nstitlebaraccessoryviewcontroller/1397780-viewdidappear)Added [-[NSTitlebarAccessoryViewController viewDidDisappear]](https://developer.apple.com/documentation/appkit/nstitlebaraccessoryviewcontroller/1397776-viewdiddisappear)Added [-[NSTitlebarAccessoryViewController viewWillAppear]](https://developer.apple.com/documentation/appkit/nstitlebaraccessoryviewcontroller/1397774-viewwillappear)NSTokenField.hRemoved [-[NSTokenField completionDelay]](https://developer.apple.com/documentation/appkit/nstokenfield/1535823-completiondelay)Removed [-[NSTokenField setCompletionDelay:]](https://developer.apple.com/documentation/appkit/nstokenfield/1535823-completiondelay)Removed [-[NSTokenField setTokenStyle:]](https://developer.apple.com/documentation/appkit/nstokenfield/1534077-tokenstyle)Removed [-[NSTokenField setTokenizingCharacterSet:]](https://developer.apple.com/documentation/appkit/nstokenfield/1534230-tokenizingcharacterset)Removed [-[NSTokenField tokenStyle]](https://developer.apple.com/documentation/appkit/nstokenfield/1534077-tokenstyle)Removed [-[NSTokenField tokenizingCharacterSet]](https://developer.apple.com/documentation/appkit/nstokenfield/1534230-tokenizingcharacterset)Added [NSTokenField.completionDelay](https://developer.apple.com/documentation/appkit/nstokenfield/1535823-completiondelay)Added [NSTokenField.tokenStyle](https://developer.apple.com/documentation/appkit/nstokenfield/1534077-tokenstyle)Added [NSTokenField.tokenizingCharacterSet](https://developer.apple.com/documentation/appkit/nstokenfield/1534230-tokenizingcharacterset)Modified [-[NSTokenFieldDelegate tokenField:completionsForSubstring:indexOfToken:indexOfSelectedItem:]](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/1532474-tokenfield)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTokenFieldDelegate tokenField:displayStringForRepresentedObject:]](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/1526020-tokenfield)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTokenFieldDelegate tokenField:editingStringForRepresentedObject:]](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/1524432-tokenfield)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTokenFieldDelegate tokenField:hasMenuForRepresentedObject:]](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/1533494-tokenfield)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTokenFieldDelegate tokenField:menuForRepresentedObject:]](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/1528750-tokenfield)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTokenFieldDelegate tokenField:readFromPasteboard:]](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/1529534-tokenfield)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTokenFieldDelegate tokenField:representedObjectForEditingString:]](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/1527909-tokenfield)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTokenFieldDelegate tokenField:shouldAddObjects:atIndex:]](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/1524376-tokenfield)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTokenFieldDelegate tokenField:styleForRepresentedObject:]](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/1530203-tokenfield)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTokenFieldDelegate tokenField:writeRepresentedObjects:toPasteboard:]](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/1528190-tokenfield)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSTokenFieldCell.hRemoved [-[NSTokenFieldCell completionDelay]](https://developer.apple.com/documentation/appkit/nstokenfieldcell/1523806-completiondelay)Removed [-[NSTokenFieldCell delegate]](https://developer.apple.com/documentation/appkit/nstokenfieldcell/1523813-delegate)Removed [-[NSTokenFieldCell setCompletionDelay:]](https://developer.apple.com/documentation/appkit/nstokenfieldcell/1523806-completiondelay)Removed [-[NSTokenFieldCell setDelegate:]](https://developer.apple.com/documentation/appkit/nstokenfieldcell/1523813-delegate)Removed [-[NSTokenFieldCell setTokenStyle:]](https://developer.apple.com/documentation/appkit/nstokenfieldcell/1523827-tokenstyle)Removed [-[NSTokenFieldCell setTokenizingCharacterSet:]](https://developer.apple.com/documentation/appkit/nstokenfieldcell/1523822-tokenizingcharacterset)Removed [-[NSTokenFieldCell tokenStyle]](https://developer.apple.com/documentation/appkit/nstokenfieldcell/1523827-tokenstyle)Removed [-[NSTokenFieldCell tokenizingCharacterSet]](https://developer.apple.com/documentation/appkit/nstokenfieldcell/1523822-tokenizingcharacterset)Removed [NSDefaultTokenStyle](https://developer.apple.com/documentation/appkit/nstokenstyle/nsdefaulttokenstyle)Removed [NSPlainTextTokenStyle](https://developer.apple.com/documentation/appkit/nstokenstyle/nsplaintexttokenstyle)Removed [NSRoundedTokenStyle](https://developer.apple.com/documentation/appkit/nstokenstyle/nsroundedtokenstyle)Added [NSTokenFieldCell.completionDelay](https://developer.apple.com/documentation/appkit/nstokenfieldcell/1523806-completiondelay)Added [NSTokenFieldCell.delegate](https://developer.apple.com/documentation/appkit/nstokenfieldcell/1523813-delegate)Added [NSTokenFieldCell.tokenStyle](https://developer.apple.com/documentation/appkit/nstokenfieldcell/1523827-tokenstyle)Added [NSTokenFieldCell.tokenizingCharacterSet](https://developer.apple.com/documentation/appkit/nstokenfieldcell/1523822-tokenizingcharacterset)Added [NSDefaultTokenStyle](https://developer.apple.com/documentation/appkit/nsdefaulttokenstyle)Added [NSPlainTextTokenStyle](https://developer.apple.com/documentation/appkit/nsplaintexttokenstyle)Added [NSRoundedTokenStyle](https://developer.apple.com/documentation/appkit/nsroundedtokenstyle)Added [NSTokenStyleDefault](https://developer.apple.com/documentation/appkit/nstokenfield/tokenstyle/default)Added [NSTokenStyleNone](https://developer.apple.com/documentation/appkit/nstokenfield/tokenstyle/none)Added [NSTokenStylePlainSquared](https://developer.apple.com/documentation/appkit/nstokenstyle/nstokenstyleplainsquared)Added [NSTokenStyleRounded](https://developer.apple.com/documentation/appkit/nstokenfield/tokenstyle/rounded)Added [NSTokenStyleSquared](https://developer.apple.com/documentation/appkit/nstokenstyle/nstokenstylesquared)Modified [-[NSTokenFieldCellDelegate tokenFieldCell:completionsForSubstring:indexOfToken:indexOfSelectedItem:]](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/1523818-tokenfieldcell)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTokenFieldCellDelegate tokenFieldCell:displayStringForRepresentedObject:]](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/1523804-tokenfieldcell)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTokenFieldCellDelegate tokenFieldCell:editingStringForRepresentedObject:]](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/1523824-tokenfieldcell)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTokenFieldCellDelegate tokenFieldCell:hasMenuForRepresentedObject:]](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/1523826-tokenfieldcell)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTokenFieldCellDelegate tokenFieldCell:menuForRepresentedObject:]](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/1523796-tokenfieldcell)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTokenFieldCellDelegate tokenFieldCell:readFromPasteboard:]](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/1523807-tokenfieldcell)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTokenFieldCellDelegate tokenFieldCell:representedObjectForEditingString:]](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/1523795-tokenfieldcell)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTokenFieldCellDelegate tokenFieldCell:shouldAddObjects:atIndex:]](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/1523823-tokenfieldcell)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTokenFieldCellDelegate tokenFieldCell:styleForRepresentedObject:]](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/1523829-tokenfieldcell)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSTokenFieldCellDelegate tokenFieldCell:writeRepresentedObjects:toPasteboard:]](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/1523803-tokenfieldcell)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSToolbar.hRemoved [-[NSToolbar allowsUserCustomization]](https://developer.apple.com/documentation/appkit/nstoolbar/1516962-allowsusercustomization)Removed [-[NSToolbar autosavesConfiguration]](https://developer.apple.com/documentation/appkit/nstoolbar/1516992-autosavesconfiguration)Removed [-[NSToolbar configurationDictionary]](https://developer.apple.com/documentation/appkit/nstoolbar/1516956-configurationdictionary)Removed [-[NSToolbar customizationPaletteIsRunning]](https://developer.apple.com/documentation/appkit/nstoolbar/1516987-customizationpaletteisrunning)Removed [-[NSToolbar delegate]](https://developer.apple.com/documentation/appkit/nstoolbar/1516939-delegate)Removed [-[NSToolbar displayMode]](https://developer.apple.com/documentation/appkit/nstoolbar/1516937-displaymode)Removed [-[NSToolbar fullScreenAccessoryView]](https://developer.apple.com/documentation/appkit/nstoolbar/1516991-fullscreenaccessoryview)Removed [-[NSToolbar fullScreenAccessoryViewMaxHeight]](https://developer.apple.com/documentation/appkit/nstoolbar/1516989-fullscreenaccessoryviewmaxheight)Removed [-[NSToolbar fullScreenAccessoryViewMinHeight]](https://developer.apple.com/documentation/appkit/nstoolbar/1516977-fullscreenaccessoryviewminheight)Removed [-[NSToolbar identifier]](https://developer.apple.com/documentation/appkit/nstoolbar/1516953-identifier)Removed [-[NSToolbar isVisible]](https://developer.apple.com/documentation/appkit/nstoolbar/1516935-isvisible)Removed [-[NSToolbar items]](https://developer.apple.com/documentation/appkit/nstoolbar/1516946-items)Removed [-[NSToolbar selectedItemIdentifier]](https://developer.apple.com/documentation/appkit/nstoolbar/1516999-selecteditemidentifier)Removed [-[NSToolbar setAllowsUserCustomization:]](https://developer.apple.com/documentation/appkit/nstoolbar/1516962-allowsusercustomization)Removed [-[NSToolbar setAutosavesConfiguration:]](https://developer.apple.com/documentation/appkit/nstoolbar/1516992-autosavesconfiguration)Removed [-[NSToolbar setDelegate:]](https://developer.apple.com/documentation/appkit/nstoolbar/1516939-delegate)Removed [-[NSToolbar setDisplayMode:]](https://developer.apple.com/documentation/appkit/nstoolbar/1516937-displaymode)Removed [-[NSToolbar setFullScreenAccessoryView:]](https://developer.apple.com/documentation/appkit/nstoolbar/1516991-fullscreenaccessoryview)Removed [-[NSToolbar setFullScreenAccessoryViewMaxHeight:]](https://developer.apple.com/documentation/appkit/nstoolbar/1516989-fullscreenaccessoryviewmaxheight)Removed [-[NSToolbar setFullScreenAccessoryViewMinHeight:]](https://developer.apple.com/documentation/appkit/nstoolbar/1516977-fullscreenaccessoryviewminheight)Removed -[NSToolbar setSelectedItemIdentifier:]Removed [-[NSToolbar setShowsBaselineSeparator:]](https://developer.apple.com/documentation/appkit/nstoolbar/1516954-showsbaselineseparator)Removed [-[NSToolbar setSizeMode:]](https://developer.apple.com/documentation/appkit/nstoolbar/1516966-sizemode)Removed [-[NSToolbar setVisible:]](https://developer.apple.com/documentation/appkit/nstoolbar/1516935-visible)Removed [-[NSToolbar showsBaselineSeparator]](https://developer.apple.com/documentation/appkit/nstoolbar/1516954-showsbaselineseparator)Removed [-[NSToolbar sizeMode]](https://developer.apple.com/documentation/appkit/nstoolbar/1516966-sizemode)Removed [-[NSToolbar visibleItems]](https://developer.apple.com/documentation/appkit/nstoolbar/1516993-visibleitems)Added [NSToolbar.allowsExtensionItems](https://developer.apple.com/documentation/appkit/nstoolbar/1517005-allowsextensionitems)Added [NSToolbar.allowsUserCustomization](https://developer.apple.com/documentation/appkit/nstoolbar/1516962-allowsusercustomization)Added [NSToolbar.autosavesConfiguration](https://developer.apple.com/documentation/appkit/nstoolbar/1516992-autosavesconfiguration)Added [NSToolbar.configurationDictionary](https://developer.apple.com/documentation/appkit/nstoolbar/1516956-configuration)Added [NSToolbar.customizationPaletteIsRunning](https://developer.apple.com/documentation/appkit/nstoolbar/1516987-customizationpaletteisrunning)Added [NSToolbar.delegate](https://developer.apple.com/documentation/appkit/nstoolbar/1516939-delegate)Added [NSToolbar.displayMode](https://developer.apple.com/documentation/appkit/nstoolbar/1516937-displaymode)Added [NSToolbar.fullScreenAccessoryView](https://developer.apple.com/documentation/appkit/nstoolbar/1516991-fullscreenaccessoryview)Added [NSToolbar.fullScreenAccessoryViewMaxHeight](https://developer.apple.com/documentation/appkit/nstoolbar/1516989-fullscreenaccessoryviewmaxheight)Added [NSToolbar.fullScreenAccessoryViewMinHeight](https://developer.apple.com/documentation/appkit/nstoolbar/1516977-fullscreenaccessoryviewminheight)Added [NSToolbar.identifier](https://developer.apple.com/documentation/appkit/nstoolbar/1516953-identifier)Added [NSToolbar.items](https://developer.apple.com/documentation/appkit/nstoolbar/1516946-items)Added [NSToolbar.selectedItemIdentifier](https://developer.apple.com/documentation/appkit/nstoolbar/1516999-selecteditemidentifier)Added [NSToolbar.showsBaselineSeparator](https://developer.apple.com/documentation/appkit/nstoolbar/1516954-showsbaselineseparator)Added [NSToolbar.sizeMode](https://developer.apple.com/documentation/appkit/nstoolbar/1516966-sizemode)Added [NSToolbar.visible](https://developer.apple.com/documentation/appkit/nstoolbar/1516935-visible)Added [NSToolbar.visibleItems](https://developer.apple.com/documentation/appkit/nstoolbar/1516993-visibleitems)Added NSToolbar(NSDeprecated)Modified [-[NSToolbar initWithIdentifier:]](https://developer.apple.com/documentation/appkit/nstoolbar/1516975-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithIdentifier:(NSString *)identifier ``` | -- |
| To | ``` - (instancetype)initWithIdentifier:(NSString *)identifier ``` | yes |

Modified [-[NSToolbarDelegate toolbar:itemForItemIdentifier:willBeInsertedIntoToolbar:]](https://developer.apple.com/documentation/appkit/nstoolbardelegate/1516985-toolbar)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSToolbarDelegate toolbarAllowedItemIdentifiers:]](https://developer.apple.com/documentation/appkit/nstoolbardelegate/1516995-toolbaralloweditemidentifiers)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSToolbarDelegate toolbarDefaultItemIdentifiers:]](https://developer.apple.com/documentation/appkit/nstoolbardelegate/1516944-toolbardefaultitemidentifiers)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSToolbarDelegate toolbarDidRemoveItem:]](https://developer.apple.com/documentation/appkit/nstoolbardelegate/1516970-toolbardidremoveitem)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSToolbarDelegate toolbarSelectableItemIdentifiers:]](https://developer.apple.com/documentation/appkit/nstoolbardelegate/1516981-toolbarselectableitemidentifiers)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSToolbarDelegate toolbarWillAddItem:]](https://developer.apple.com/documentation/appkit/nstoolbardelegate/1516964-toolbarwilladditem)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSToolbarItem.hRemoved [-[NSToolbarItem action]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1525723-action)Removed [-[NSToolbarItem allowsDuplicatesInToolbar]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1530116-allowsduplicatesintoolbar)Removed [-[NSToolbarItem autovalidates]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1524463-autovalidates)Removed [-[NSToolbarItem image]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1527749-image)Removed [-[NSToolbarItem isEnabled]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1524277-enabled)Removed [-[NSToolbarItem itemIdentifier]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1524394-itemidentifier)Removed [-[NSToolbarItem label]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1535127-label)Removed [-[NSToolbarItem maxSize]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1526451-maxsize)Removed [-[NSToolbarItem menuFormRepresentation]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1532562-menuformrepresentation)Removed [-[NSToolbarItem minSize]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1531777-minsize)Removed [-[NSToolbarItem paletteLabel]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1525421-palettelabel)Removed [-[NSToolbarItem setAction:]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1525723-action)Removed [-[NSToolbarItem setAutovalidates:]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1524463-autovalidates)Removed [-[NSToolbarItem setEnabled:]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1524277-enabled)Removed [-[NSToolbarItem setImage:]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1527749-image)Removed [-[NSToolbarItem setLabel:]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1535127-label)Removed [-[NSToolbarItem setMaxSize:]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1526451-maxsize)Removed [-[NSToolbarItem setMenuFormRepresentation:]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1532562-menuformrepresentation)Removed [-[NSToolbarItem setMinSize:]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1531777-minsize)Removed [-[NSToolbarItem setPaletteLabel:]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1525421-palettelabel)Removed [-[NSToolbarItem setTag:]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1524618-tag)Removed [-[NSToolbarItem setTarget:]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1525982-target)Removed [-[NSToolbarItem setToolTip:]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1524627-tooltip)Removed [-[NSToolbarItem setView:]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1534039-view)Removed [-[NSToolbarItem setVisibilityPriority:]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1527947-visibilitypriority)Removed [-[NSToolbarItem tag]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1524618-tag)Removed [-[NSToolbarItem target]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1525982-target)Removed [-[NSToolbarItem toolTip]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1524627-tooltip)Removed [-[NSToolbarItem toolbar]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1532976-toolbar)Removed [-[NSToolbarItem view]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1534039-view)Removed [-[NSToolbarItem visibilityPriority]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1527947-visibilitypriority)Added [NSToolbarItem.action](https://developer.apple.com/documentation/appkit/nstoolbaritem/1525723-action)Added [NSToolbarItem.allowsDuplicatesInToolbar](https://developer.apple.com/documentation/appkit/nstoolbaritem/1530116-allowsduplicatesintoolbar)Added [NSToolbarItem.autovalidates](https://developer.apple.com/documentation/appkit/nstoolbaritem/1524463-autovalidates)Added [NSToolbarItem.enabled](https://developer.apple.com/documentation/appkit/nstoolbaritem/1524277-enabled)Added [NSToolbarItem.image](https://developer.apple.com/documentation/appkit/nstoolbaritem/1527749-image)Added [NSToolbarItem.itemIdentifier](https://developer.apple.com/documentation/appkit/nstoolbaritem/1524394-itemidentifier)Added [NSToolbarItem.label](https://developer.apple.com/documentation/appkit/nstoolbaritem/1535127-label)Added [NSToolbarItem.maxSize](https://developer.apple.com/documentation/appkit/nstoolbaritem/1526451-maxsize)Added [NSToolbarItem.menuFormRepresentation](https://developer.apple.com/documentation/appkit/nstoolbaritem/1532562-menuformrepresentation)Added [NSToolbarItem.minSize](https://developer.apple.com/documentation/appkit/nstoolbaritem/1531777-minsize)Added [NSToolbarItem.paletteLabel](https://developer.apple.com/documentation/appkit/nstoolbaritem/1525421-palettelabel)Added [NSToolbarItem.tag](https://developer.apple.com/documentation/appkit/nstoolbaritem/1524618-tag)Added [NSToolbarItem.target](https://developer.apple.com/documentation/appkit/nstoolbaritem/1525982-target)Added [NSToolbarItem.toolTip](https://developer.apple.com/documentation/appkit/nstoolbaritem/1524627-tooltip)Added [NSToolbarItem.toolbar](https://developer.apple.com/documentation/appkit/nstoolbaritem/1532976-toolbar)Added [NSToolbarItem.view](https://developer.apple.com/documentation/appkit/nstoolbaritem/1534039-view)Added [NSToolbarItem.visibilityPriority](https://developer.apple.com/documentation/appkit/nstoolbaritem/1527947-visibilitypriority)Modified [-[NSToolbarItem initWithItemIdentifier:]](https://developer.apple.com/documentation/appkit/nstoolbaritem/1534084-initwithitemidentifier)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithItemIdentifier:(NSString *)itemIdentifier ``` | -- |
| To | ``` - (instancetype)initWithItemIdentifier:(NSString *)itemIdentifier ``` | yes |

NSToolbarItemGroup.hRemoved [-[NSToolbarItemGroup setSubitems:]](https://developer.apple.com/documentation/appkit/nstoolbaritemgroup/1529923-subitems)Removed [-[NSToolbarItemGroup subitems]](https://developer.apple.com/documentation/appkit/nstoolbaritemgroup/1529923-subitems)Added [NSToolbarItemGroup.subitems](https://developer.apple.com/documentation/appkit/nstoolbaritemgroup/1529923-subitems)NSTouch.hRemoved [NSTouch.isResting](https://developer.apple.com/documentation/appkit/nstouch/1808479-isresting)Added [NSTouch.resting](https://developer.apple.com/documentation/appkit/nstouch/1525663-resting)Modified [NSTouch.device](https://developer.apple.com/documentation/appkit/nstouch/1533562-device)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) id device ``` |
| To | ``` @property(readonly, strong) id device ``` |

Modified [NSTouch.identity](https://developer.apple.com/documentation/appkit/nstouch/1535399-identity)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) id<NSObject, NSCopying> identity ``` |
| To | ``` @property(readonly, strong) id<NSObject, NSCopying> identity ``` |

Modified [NSTouchPhaseAny](https://developer.apple.com/documentation/appkit/nstouchphase/nstouchphaseany)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.7 |

Modified [NSTouchPhaseBegan](https://developer.apple.com/documentation/appkit/nstouch/phase/1527407-began)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.7 |

Modified [NSTouchPhaseCancelled](https://developer.apple.com/documentation/appkit/nstouch/phase/1535562-cancelled)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.7 |

Modified [NSTouchPhaseEnded](https://developer.apple.com/documentation/appkit/nstouchphase/nstouchphaseended)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.7 |

Modified [NSTouchPhaseMoved](https://developer.apple.com/documentation/appkit/nstouch/phase/1533043-moved)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.7 |

Modified [NSTouchPhaseStationary](https://developer.apple.com/documentation/appkit/nstouchphase/nstouchphasestationary)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.7 |

Modified [NSTouchPhaseTouching](https://developer.apple.com/documentation/appkit/nstouchphase/nstouchphasetouching)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.7 |

NSTrackingArea.hRemoved [-[NSTrackingArea options]](https://developer.apple.com/documentation/appkit/nstrackingarea/1533013-options)Removed [-[NSTrackingArea owner]](https://developer.apple.com/documentation/appkit/nstrackingarea/1525965-owner)Removed [-[NSTrackingArea rect]](https://developer.apple.com/documentation/appkit/nstrackingarea/1525874-rect)Removed [-[NSTrackingArea userInfo]](https://developer.apple.com/documentation/appkit/nstrackingarea/1527949-userinfo)Added [NSTrackingArea.options](https://developer.apple.com/documentation/appkit/nstrackingarea/1533013-options)Added [NSTrackingArea.owner](https://developer.apple.com/documentation/appkit/nstrackingarea/1525965-owner)Added [NSTrackingArea.rect](https://developer.apple.com/documentation/appkit/nstrackingarea/1525874-rect)Added [NSTrackingArea.userInfo](https://developer.apple.com/documentation/appkit/nstrackingarea/1527949-userinfo)Modified [-[NSTrackingArea initWithRect:options:owner:userInfo:]](https://developer.apple.com/documentation/appkit/nstrackingarea/1524488-initwithrect)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithRect:(NSRect)rect options:(NSTrackingAreaOptions)options owner:(id)owner userInfo:(NSDictionary *)userInfo ``` |
| To | ``` - (instancetype)initWithRect:(NSRect)rect options:(NSTrackingAreaOptions)options owner:(id)owner userInfo:(NSDictionary *)userInfo ``` |

NSTreeController.hRemoved [-[NSTreeController alwaysUsesMultipleValuesMarker]](https://developer.apple.com/documentation/appkit/nstreecontroller/1529530-alwaysusesmultiplevaluesmarker)Removed [-[NSTreeController arrangedObjects]](https://developer.apple.com/documentation/appkit/nstreecontroller/1527465-arrangedobjects)Removed [-[NSTreeController avoidsEmptySelection]](https://developer.apple.com/documentation/appkit/nstreecontroller/1526188-avoidsemptyselection)Removed [-[NSTreeController canAddChild]](https://developer.apple.com/documentation/appkit/nstreecontroller/1525790-canaddchild)Removed [-[NSTreeController canInsert]](https://developer.apple.com/documentation/appkit/nstreecontroller/1534180-caninsert)Removed [-[NSTreeController canInsertChild]](https://developer.apple.com/documentation/appkit/nstreecontroller/1524647-caninsertchild)Removed [-[NSTreeController childrenKeyPath]](https://developer.apple.com/documentation/appkit/nstreecontroller/1528721-childrenkeypath)Removed [-[NSTreeController content]](https://developer.apple.com/documentation/appkit/nstreecontroller/1530427-content)Removed [-[NSTreeController countKeyPath]](https://developer.apple.com/documentation/appkit/nstreecontroller/1529127-countkeypath)Removed [-[NSTreeController leafKeyPath]](https://developer.apple.com/documentation/appkit/nstreecontroller/1532164-leafkeypath)Removed [-[NSTreeController preservesSelection]](https://developer.apple.com/documentation/appkit/nstreecontroller/1524473-preservesselection)Removed [-[NSTreeController selectedNodes]](https://developer.apple.com/documentation/appkit/nstreecontroller/1534151-selectednodes)Removed [-[NSTreeController selectedObjects]](https://developer.apple.com/documentation/appkit/nstreecontroller/1529670-selectedobjects)Removed [-[NSTreeController selectionIndexPath]](https://developer.apple.com/documentation/appkit/nstreecontroller/1533951-selectionindexpath)Removed [-[NSTreeController selectionIndexPaths]](https://developer.apple.com/documentation/appkit/nstreecontroller/1534861-selectionindexpaths)Removed [-[NSTreeController selectsInsertedObjects]](https://developer.apple.com/documentation/appkit/nstreecontroller/1534200-selectsinsertedobjects)Removed [-[NSTreeController setAlwaysUsesMultipleValuesMarker:]](https://developer.apple.com/documentation/appkit/nstreecontroller/1529530-alwaysusesmultiplevaluesmarker)Removed [-[NSTreeController setAvoidsEmptySelection:]](https://developer.apple.com/documentation/appkit/nstreecontroller/1526188-avoidsemptyselection)Removed [-[NSTreeController setChildrenKeyPath:]](https://developer.apple.com/documentation/appkit/nstreecontroller/1528721-childrenkeypath)Removed [-[NSTreeController setContent:]](https://developer.apple.com/documentation/appkit/nstreecontroller/1530427-content)Removed [-[NSTreeController setCountKeyPath:]](https://developer.apple.com/documentation/appkit/nstreecontroller/1529127-countkeypath)Removed [-[NSTreeController setLeafKeyPath:]](https://developer.apple.com/documentation/appkit/nstreecontroller/1532164-leafkeypath)Removed [-[NSTreeController setPreservesSelection:]](https://developer.apple.com/documentation/appkit/nstreecontroller/1524473-preservesselection)Removed [-[NSTreeController setSelectsInsertedObjects:]](https://developer.apple.com/documentation/appkit/nstreecontroller/1534200-selectsinsertedobjects)Removed [-[NSTreeController setSortDescriptors:]](https://developer.apple.com/documentation/appkit/nstreecontroller/1526827-sortdescriptors)Removed [-[NSTreeController sortDescriptors]](https://developer.apple.com/documentation/appkit/nstreecontroller/1526827-sortdescriptors)Added [NSTreeController.alwaysUsesMultipleValuesMarker](https://developer.apple.com/documentation/appkit/nstreecontroller/1529530-alwaysusesmultiplevaluesmarker)Added [NSTreeController.arrangedObjects](https://developer.apple.com/documentation/appkit/nstreecontroller/1527465-arrangedobjects)Added [NSTreeController.avoidsEmptySelection](https://developer.apple.com/documentation/appkit/nstreecontroller/1526188-avoidsemptyselection)Added [NSTreeController.canAddChild](https://developer.apple.com/documentation/appkit/nstreecontroller/1525790-canaddchild)Added [NSTreeController.canInsert](https://developer.apple.com/documentation/appkit/nstreecontroller/1534180-caninsert)Added [NSTreeController.canInsertChild](https://developer.apple.com/documentation/appkit/nstreecontroller/1524647-caninsertchild)Added [NSTreeController.childrenKeyPath](https://developer.apple.com/documentation/appkit/nstreecontroller/1528721-childrenkeypath)Added [NSTreeController.content](https://developer.apple.com/documentation/appkit/nstreecontroller/1530427-content)Added [NSTreeController.countKeyPath](https://developer.apple.com/documentation/appkit/nstreecontroller/1529127-countkeypath)Added [NSTreeController.leafKeyPath](https://developer.apple.com/documentation/appkit/nstreecontroller/1532164-leafkeypath)Added [NSTreeController.preservesSelection](https://developer.apple.com/documentation/appkit/nstreecontroller/1524473-preservesselection)Added [NSTreeController.selectedNodes](https://developer.apple.com/documentation/appkit/nstreecontroller/1534151-selectednodes)Added [NSTreeController.selectedObjects](https://developer.apple.com/documentation/appkit/nstreecontroller/1529670-selectedobjects)Added [NSTreeController.selectionIndexPath](https://developer.apple.com/documentation/appkit/nstreecontroller/1533951-selectionindexpath)Added [NSTreeController.selectionIndexPaths](https://developer.apple.com/documentation/appkit/nstreecontroller/1534861-selectionindexpaths)Added [NSTreeController.selectsInsertedObjects](https://developer.apple.com/documentation/appkit/nstreecontroller/1534200-selectsinsertedobjects)Added [NSTreeController.sortDescriptors](https://developer.apple.com/documentation/appkit/nstreecontroller/1526827-sortdescriptors)NSTreeNode.hRemoved [-[NSTreeNode childNodes]](https://developer.apple.com/documentation/appkit/nstreenode/1525285-children)Removed [-[NSTreeNode indexPath]](https://developer.apple.com/documentation/appkit/nstreenode/1532255-indexpath)Removed [-[NSTreeNode isLeaf]](https://developer.apple.com/documentation/appkit/nstreenode/1532729-leaf)Removed [-[NSTreeNode mutableChildNodes]](https://developer.apple.com/documentation/appkit/nstreenode/1527238-mutablechildnodes)Removed [-[NSTreeNode parentNode]](https://developer.apple.com/documentation/appkit/nstreenode/1530728-parentnode)Removed [-[NSTreeNode representedObject]](https://developer.apple.com/documentation/appkit/nstreenode/1531596-representedobject)Added [NSTreeNode.childNodes](https://developer.apple.com/documentation/appkit/nstreenode/1525285-childnodes)Added [NSTreeNode.indexPath](https://developer.apple.com/documentation/appkit/nstreenode/1532255-indexpath)Added [NSTreeNode.leaf](https://developer.apple.com/documentation/appkit/nstreenode/1532729-isleaf)Added [NSTreeNode.mutableChildNodes](https://developer.apple.com/documentation/appkit/nstreenode/1527238-mutablechildnodes)Added [NSTreeNode.parentNode](https://developer.apple.com/documentation/appkit/nstreenode/1530728-parentnode)Added [NSTreeNode.representedObject](https://developer.apple.com/documentation/appkit/nstreenode/1531596-representedobject)Modified [-[NSTreeNode initWithRepresentedObject:]](https://developer.apple.com/documentation/appkit/nstreenode/1533294-initwithrepresentedobject)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithRepresentedObject:(id)modelObject ``` |
| To | ``` - (instancetype)initWithRepresentedObject:(id)modelObject ``` |

Modified [+[NSTreeNode treeNodeWithRepresentedObject:]](https://developer.apple.com/documentation/appkit/nstreenode/1537056-treenodewithrepresentedobject)

|  | Declaration |
| --- | --- |
| From | ``` + (id)treeNodeWithRepresentedObject:(id)modelObject ``` |
| To | ``` + (instancetype)treeNodeWithRepresentedObject:(id)modelObject ``` |

NSTypesetter.hRemoved [-[NSTypesetter attributedString]](https://developer.apple.com/documentation/appkit/nstypesetter/1524704-attributedstring)Removed [-[NSTypesetter attributesForExtraLineFragment]](https://developer.apple.com/documentation/appkit/nstypesetter/1534922-attributesforextralinefragment)Removed [-[NSTypesetter bidiProcessingEnabled]](https://developer.apple.com/documentation/appkit/nstypesetter/1533588-bidiprocessingenabled)Removed [-[NSTypesetter currentParagraphStyle]](https://developer.apple.com/documentation/appkit/nstypesetter/1528893-currentparagraphstyle)Removed [-[NSTypesetter currentTextContainer]](https://developer.apple.com/documentation/appkit/nstypesetter/1534527-currenttextcontainer)Removed [-[NSTypesetter hyphenationFactor]](https://developer.apple.com/documentation/appkit/nstypesetter/1535877-hyphenationfactor)Removed [-[NSTypesetter layoutManager]](https://developer.apple.com/documentation/appkit/nstypesetter/1533958-layoutmanager)Removed [-[NSTypesetter lineFragmentPadding]](https://developer.apple.com/documentation/appkit/nstypesetter/1531129-linefragmentpadding)Removed [-[NSTypesetter paragraphCharacterRange]](https://developer.apple.com/documentation/appkit/nstypesetter/1533422-paragraphcharacterrange)Removed [-[NSTypesetter paragraphGlyphRange]](https://developer.apple.com/documentation/appkit/nstypesetter/1528301-paragraphglyphrange)Removed [-[NSTypesetter paragraphSeparatorCharacterRange]](https://developer.apple.com/documentation/appkit/nstypesetter/1531746-paragraphseparatorcharacterrange)Removed [-[NSTypesetter paragraphSeparatorGlyphRange]](https://developer.apple.com/documentation/appkit/nstypesetter/1534165-paragraphseparatorglyphrange)Removed [-[NSTypesetter setAttributedString:]](https://developer.apple.com/documentation/appkit/nstypesetter/1524704-attributedstring)Removed [-[NSTypesetter setBidiProcessingEnabled:]](https://developer.apple.com/documentation/appkit/nstypesetter/1533588-bidiprocessingenabled)Removed [-[NSTypesetter setHyphenationFactor:]](https://developer.apple.com/documentation/appkit/nstypesetter/1535877-hyphenationfactor)Removed [-[NSTypesetter setLineFragmentPadding:]](https://developer.apple.com/documentation/appkit/nstypesetter/1531129-linefragmentpadding)Removed [-[NSTypesetter setTypesetterBehavior:]](https://developer.apple.com/documentation/appkit/nstypesetter/1528244-typesetterbehavior)Removed [-[NSTypesetter setUsesFontLeading:]](https://developer.apple.com/documentation/appkit/nstypesetter/1526716-usesfontleading)Removed [-[NSTypesetter textContainers]](https://developer.apple.com/documentation/appkit/nstypesetter/1526310-textcontainers)Removed [-[NSTypesetter typesetterBehavior]](https://developer.apple.com/documentation/appkit/nstypesetter/1528244-typesetterbehavior)Removed [-[NSTypesetter usesFontLeading]](https://developer.apple.com/documentation/appkit/nstypesetter/1526716-usesfontleading)Added [NSTypesetter.attributedString](https://developer.apple.com/documentation/appkit/nstypesetter/1524704-attributedstring)Added [NSTypesetter.attributesForExtraLineFragment](https://developer.apple.com/documentation/appkit/nstypesetter/1534922-attributesforextralinefragment)Added [NSTypesetter.bidiProcessingEnabled](https://developer.apple.com/documentation/appkit/nstypesetter/1533588-bidiprocessingenabled)Added [NSTypesetter.currentParagraphStyle](https://developer.apple.com/documentation/appkit/nstypesetter/1528893-currentparagraphstyle)Added [NSTypesetter.currentTextContainer](https://developer.apple.com/documentation/appkit/nstypesetter/1534527-currenttextcontainer)Added [NSTypesetter.hyphenationFactor](https://developer.apple.com/documentation/appkit/nstypesetter/1535877-hyphenationfactor)Added [NSTypesetter.layoutManager](https://developer.apple.com/documentation/appkit/nstypesetter/1533958-layoutmanager)Added [NSTypesetter.lineFragmentPadding](https://developer.apple.com/documentation/appkit/nstypesetter/1531129-linefragmentpadding)Added [NSTypesetter.paragraphCharacterRange](https://developer.apple.com/documentation/appkit/nstypesetter/1533422-paragraphcharacterrange)Added [NSTypesetter.paragraphGlyphRange](https://developer.apple.com/documentation/appkit/nstypesetter/1528301-paragraphglyphrange)Added [NSTypesetter.paragraphSeparatorCharacterRange](https://developer.apple.com/documentation/appkit/nstypesetter/1531746-paragraphseparatorcharacterrange)Added [NSTypesetter.paragraphSeparatorGlyphRange](https://developer.apple.com/documentation/appkit/nstypesetter/1534165-paragraphseparatorglyphrange)Added [NSTypesetter.textContainers](https://developer.apple.com/documentation/appkit/nstypesetter/1526310-textcontainers)Added [NSTypesetter.typesetterBehavior](https://developer.apple.com/documentation/appkit/nstypesetter/1528244-typesetterbehavior)Added [NSTypesetter.usesFontLeading](https://developer.apple.com/documentation/appkit/nstypesetter/1526716-usesfontleading)NSUserActivity.h (Added)Added [-[NSDocument restoreUserActivityState:]](https://developer.apple.com/documentation/appkit/nsdocument/1535442-restoreuseractivitystate)Added [-[NSDocument updateUserActivityState:]](https://developer.apple.com/documentation/appkit/nsdocument/1529014-updateuseractivitystate)Added [NSDocument.userActivity](https://developer.apple.com/documentation/appkit/nsdocument/1526106-useractivity)Added [-[NSResponder restoreUserActivityState:]](https://developer.apple.com/documentation/appkit/nsresponder/1526024-restoreuseractivitystate)Added [-[NSResponder updateUserActivityState:]](https://developer.apple.com/documentation/appkit/nsresponder/1534884-updateuseractivitystate)Added [NSResponder.userActivity](https://developer.apple.com/documentation/appkit/nsresponder/1534108-useractivity)Added NSDocument(NSUserActivity)Added NSResponder(NSUserActivity)Added [NSUserActivityDocumentURLKey](https://developer.apple.com/documentation/appkit/useractivityurlkey)Added [#def NS_USER_ACTIVITY_SUPPORTED](https://developer.apple.com/documentation/appkit/ns_user_activity_supported)NSUserDefaultsController.hRemoved [-[NSUserDefaultsController appliesImmediately]](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/1388191-appliesimmediately)Removed [-[NSUserDefaultsController defaults]](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/1388182-defaults)Removed [-[NSUserDefaultsController hasUnappliedChanges]](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/1388186-hasunappliedchanges)Removed [-[NSUserDefaultsController initialValues]](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/1388188-initialvalues)Removed [-[NSUserDefaultsController setAppliesImmediately:]](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/1388191-appliesimmediately)Removed [-[NSUserDefaultsController setInitialValues:]](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/1388188-initialvalues)Removed [-[NSUserDefaultsController values]](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/1388176-values)Added [NSUserDefaultsController.appliesImmediately](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/1388191-appliesimmediately)Added [NSUserDefaultsController.defaults](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/1388182-defaults)Added [NSUserDefaultsController.hasUnappliedChanges](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/1388186-hasunappliedchanges)Added [-[NSUserDefaultsController initWithCoder:]](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/1388172-init)Added [NSUserDefaultsController.initialValues](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/1388188-initialvalues)Added [NSUserDefaultsController.values](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/1388176-values)Modified [-[NSUserDefaultsController initWithDefaults:initialValues:]](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/1388184-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithDefaults:(NSUserDefaults *)defaults initialValues:(NSDictionary *)initialValues ``` | -- |
| To | ``` - (instancetype)initWithDefaults:(NSUserDefaults *)defaults initialValues:(NSDictionary *)initialValues ``` | yes |

Modified [+[NSUserDefaultsController sharedUserDefaultsController]](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/1388190-shareduserdefaultscontroller)

|  | Declaration |
| --- | --- |
| From | ``` + (id)sharedUserDefaultsController ``` |
| To | ``` + (NSUserDefaultsController *)sharedUserDefaultsController ``` |

NSUserInterfaceItemSearching.hModified [-[NSUserInterfaceItemSearching performActionForItem:]](https://developer.apple.com/documentation/appkit/nsuserinterfaceitemsearching/1420812-performactionforitem)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSUserInterfaceItemSearching showAllHelpTopicsForSearchString:]](https://developer.apple.com/documentation/appkit/nsuserinterfaceitemsearching/1420806-showallhelptopicsforsearchstring)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSView.hRemoved [-[NSView acceptsTouchEvents]](https://developer.apple.com/documentation/appkit/nsview/1483739-acceptstouchevents)Removed [-[NSView alphaValue]](https://developer.apple.com/documentation/appkit/nsview/1483560-alphavalue)Removed [-[NSView autoresizesSubviews]](https://developer.apple.com/documentation/appkit/nsview/1483358-autoresizessubviews)Removed [-[NSView autoresizingMask]](https://developer.apple.com/documentation/appkit/nsview/1483281-autoresizingmask)Removed [-[NSView backgroundFilters]](https://developer.apple.com/documentation/appkit/nsview/1483689-backgroundfilters)Removed [-[NSView bounds]](https://developer.apple.com/documentation/appkit/nsview/1483817-bounds)Removed [-[NSView boundsRotation]](https://developer.apple.com/documentation/appkit/nsview/1483746-boundsrotation)Removed [-[NSView canBecomeKeyView]](https://developer.apple.com/documentation/appkit/nsview/1483759-canbecomekeyview)Removed [-[NSView canDraw]](https://developer.apple.com/documentation/appkit/nsview/1483277-candraw)Removed [-[NSView canDrawConcurrently]](https://developer.apple.com/documentation/appkit/nsview/1483425-candrawconcurrently)Removed [-[NSView canDrawSubviewsIntoLayer]](https://developer.apple.com/documentation/appkit/nsview/1483347-candrawsubviewsintolayer)Removed [-[NSView compositingFilter]](https://developer.apple.com/documentation/appkit/nsview/1483516-compositingfilter)Removed [-[NSView contentFilters]](https://developer.apple.com/documentation/appkit/nsview/1483703-contentfilters)Removed [-[NSView enclosingScrollView]](https://developer.apple.com/documentation/appkit/nsview/1483654-enclosingscrollview)Removed [-[NSView focusRingMaskBounds]](https://developer.apple.com/documentation/appkit/nsview/1483287-focusringmaskbounds)Removed [-[NSView focusRingType]](https://developer.apple.com/documentation/appkit/nsview/1483261-focusringtype)Removed [-[NSView frame]](https://developer.apple.com/documentation/appkit/nsview/1483713-frame)Removed [-[NSView frameCenterRotation]](https://developer.apple.com/documentation/appkit/nsview/1483367-framecenterrotation)Removed [-[NSView frameRotation]](https://developer.apple.com/documentation/appkit/nsview/1483412-framerotation)Removed [-[NSView heightAdjustLimit]](https://developer.apple.com/documentation/appkit/nsview/1483691-heightadjustlimit)Removed [-[NSView inLiveResize]](https://developer.apple.com/documentation/appkit/nsview/1483267-inliveresize)Removed [-[NSView inputContext]](https://developer.apple.com/documentation/appkit/nsview/1483323-inputcontext)Removed [-[NSView isDrawingFindIndicator]](https://developer.apple.com/documentation/appkit/nsview/1483317-drawingfindindicator)Removed [-[NSView isFlipped]](https://developer.apple.com/documentation/appkit/nsview/1483532-isflipped)Removed [-[NSView isHidden]](https://developer.apple.com/documentation/appkit/nsview/1483369-hidden)Removed [-[NSView isHiddenOrHasHiddenAncestor]](https://developer.apple.com/documentation/appkit/nsview/1483473-ishiddenorhashiddenancestor)Removed [-[NSView isInFullScreenMode]](https://developer.apple.com/documentation/appkit/nsview/1483337-isinfullscreenmode)Removed [-[NSView isOpaque]](https://developer.apple.com/documentation/appkit/nsview/1483558-opaque)Removed [-[NSView isRotatedFromBase]](https://developer.apple.com/documentation/appkit/nsview/1483709-isrotatedfrombase)Removed [-[NSView isRotatedOrScaledFromBase]](https://developer.apple.com/documentation/appkit/nsview/1483390-isrotatedorscaledfrombase)Removed [-[NSView layer]](https://developer.apple.com/documentation/appkit/nsview/1483298-layer)Removed [-[NSView layerContentsPlacement]](https://developer.apple.com/documentation/appkit/nsview/1483375-layercontentsplacement)Removed [-[NSView layerContentsRedrawPolicy]](https://developer.apple.com/documentation/appkit/nsview/1483514-layercontentsredrawpolicy)Removed [-[NSView layerUsesCoreImageFilters]](https://developer.apple.com/documentation/appkit/nsview/1483576-layerusescoreimagefilters)Removed [-[NSView mouseDownCanMoveWindow]](https://developer.apple.com/documentation/appkit/nsview/1483666-mousedowncanmovewindow)Removed [-[NSView needsDisplay]](https://developer.apple.com/documentation/appkit/nsview/1483360-needsdisplay)Removed [-[NSView needsPanelToBecomeKey]](https://developer.apple.com/documentation/appkit/nsview/1483512-needspaneltobecomekey)Removed [-[NSView nextKeyView]](https://developer.apple.com/documentation/appkit/nsview/1483465-nextkeyview)Removed [-[NSView nextValidKeyView]](https://developer.apple.com/documentation/appkit/nsview/1483572-nextvalidkeyview)Removed [-[NSView opaqueAncestor]](https://developer.apple.com/documentation/appkit/nsview/1483383-opaqueancestor)Removed [-[NSView pageFooter]](https://developer.apple.com/documentation/appkit/nsview/1483355-pagefooter)Removed [-[NSView pageHeader]](https://developer.apple.com/documentation/appkit/nsview/1483674-pageheader)Removed [-[NSView postsBoundsChangedNotifications]](https://developer.apple.com/documentation/appkit/nsview/1483239-postsboundschangednotifications)Removed [-[NSView postsFrameChangedNotifications]](https://developer.apple.com/documentation/appkit/nsview/1483524-postsframechangednotifications)Removed [-[NSView preservesContentDuringLiveResize]](https://developer.apple.com/documentation/appkit/nsview/1483795-preservescontentduringliveresize)Removed [-[NSView previousKeyView]](https://developer.apple.com/documentation/appkit/nsview/1483646-previouskeyview)Removed [-[NSView previousValidKeyView]](https://developer.apple.com/documentation/appkit/nsview/1483371-previousvalidkeyview)Removed [-[NSView printJobTitle]](https://developer.apple.com/documentation/appkit/nsview/1483753-printjobtitle)Removed [-[NSView rectPreservedDuringLiveResize]](https://developer.apple.com/documentation/appkit/nsview/1483528-rectpreservedduringliveresize)Removed [-[NSView registeredDraggedTypes]](https://developer.apple.com/documentation/appkit/nsview/1483564-registereddraggedtypes)Removed [-[NSView setAcceptsTouchEvents:]](https://developer.apple.com/documentation/appkit/nsview/1483739-acceptstouchevents)Removed [-[NSView setAlphaValue:]](https://developer.apple.com/documentation/appkit/nsview/1483560-alphavalue)Removed [-[NSView setAutoresizesSubviews:]](https://developer.apple.com/documentation/appkit/nsview/1483358-autoresizessubviews)Removed [-[NSView setAutoresizingMask:]](https://developer.apple.com/documentation/appkit/nsview/1483281-autoresizingmask)Removed [-[NSView setBackgroundFilters:]](https://developer.apple.com/documentation/appkit/nsview/1483689-backgroundfilters)Removed [-[NSView setBounds:]](https://developer.apple.com/documentation/appkit/nsview/1483817-bounds)Removed [-[NSView setBoundsRotation:]](https://developer.apple.com/documentation/appkit/nsview/1483746-boundsrotation)Removed [-[NSView setCanDrawConcurrently:]](https://developer.apple.com/documentation/appkit/nsview/1483425-candrawconcurrently)Removed [-[NSView setCanDrawSubviewsIntoLayer:]](https://developer.apple.com/documentation/appkit/nsview/1483347-candrawsubviewsintolayer)Removed [-[NSView setCompositingFilter:]](https://developer.apple.com/documentation/appkit/nsview/1483516-compositingfilter)Removed [-[NSView setContentFilters:]](https://developer.apple.com/documentation/appkit/nsview/1483703-contentfilters)Removed [-[NSView setFocusRingType:]](https://developer.apple.com/documentation/appkit/nsview/1483261-focusringtype)Removed [-[NSView setFrame:]](https://developer.apple.com/documentation/appkit/nsview/1483713-frame)Removed [-[NSView setFrameCenterRotation:]](https://developer.apple.com/documentation/appkit/nsview/1483367-framecenterrotation)Removed [-[NSView setFrameRotation:]](https://developer.apple.com/documentation/appkit/nsview/1483412-framerotation)Removed [-[NSView setHidden:]](https://developer.apple.com/documentation/appkit/nsview/1483369-ishidden)Removed [-[NSView setLayer:]](https://developer.apple.com/documentation/appkit/nsview/1483298-layer)Removed [-[NSView setLayerContentsPlacement:]](https://developer.apple.com/documentation/appkit/nsview/1483375-layercontentsplacement)Removed [-[NSView setLayerContentsRedrawPolicy:]](https://developer.apple.com/documentation/appkit/nsview/1483514-layercontentsredrawpolicy)Removed [-[NSView setLayerUsesCoreImageFilters:]](https://developer.apple.com/documentation/appkit/nsview/1483576-layerusescoreimagefilters)Removed [-[NSView setNeedsDisplay:]](https://developer.apple.com/documentation/appkit/nsview/1483360-needsdisplay)Removed [-[NSView setNextKeyView:]](https://developer.apple.com/documentation/appkit/nsview/1483465-nextkeyview)Removed [-[NSView setPostsBoundsChangedNotifications:]](https://developer.apple.com/documentation/appkit/nsview/1483239-postsboundschangednotifications)Removed [-[NSView setPostsFrameChangedNotifications:]](https://developer.apple.com/documentation/appkit/nsview/1483524-postsframechangednotifications)Removed [-[NSView setShadow:]](https://developer.apple.com/documentation/appkit/nsview/1483263-shadow)Removed [-[NSView setToolTip:]](https://developer.apple.com/documentation/appkit/nsview/1483541-tooltip)Removed [-[NSView setUserInterfaceLayoutDirection:]](https://developer.apple.com/documentation/appkit/nsview/1483254-userinterfacelayoutdirection)Removed [-[NSView setWantsLayer:]](https://developer.apple.com/documentation/appkit/nsview/1483695-wantslayer)Removed [-[NSView setWantsRestingTouches:]](https://developer.apple.com/documentation/appkit/nsview/1483594-wantsrestingtouches)Removed [-[NSView shadow]](https://developer.apple.com/documentation/appkit/nsview/1483263-shadow)Removed [-[NSView subviews]](https://developer.apple.com/documentation/appkit/nsview/1483539-subviews)Removed [-[NSView superview]](https://developer.apple.com/documentation/appkit/nsview/1483737-superview)Removed [-[NSView tag]](https://developer.apple.com/documentation/appkit/nsview/1483248-tag)Removed [-[NSView toolTip]](https://developer.apple.com/documentation/appkit/nsview/1483541-tooltip)Removed [-[NSView trackingAreas]](https://developer.apple.com/documentation/appkit/nsview/1483333-trackingareas)Removed [-[NSView userInterfaceLayoutDirection]](https://developer.apple.com/documentation/appkit/nsview/1483254-userinterfacelayoutdirection)Removed [-[NSView visibleRect]](https://developer.apple.com/documentation/appkit/nsview/1483446-visiblerect)Removed [-[NSView wantsDefaultClipping]](https://developer.apple.com/documentation/appkit/nsview/1483365-wantsdefaultclipping)Removed [-[NSView wantsLayer]](https://developer.apple.com/documentation/appkit/nsview/1483695-wantslayer)Removed [-[NSView wantsRestingTouches]](https://developer.apple.com/documentation/appkit/nsview/1483594-wantsrestingtouches)Removed [-[NSView wantsUpdateLayer]](https://developer.apple.com/documentation/appkit/nsview/1483461-wantsupdatelayer)Removed [-[NSView widthAdjustLimit]](https://developer.apple.com/documentation/appkit/nsview/1483392-widthadjustlimit)Removed [-[NSView window]](https://developer.apple.com/documentation/appkit/nsview/1483301-window)Added [NSView.acceptsTouchEvents](https://developer.apple.com/documentation/appkit/nsview/1483739-acceptstouchevents)Added [-[NSView addGestureRecognizer:]](https://developer.apple.com/documentation/appkit/nsview/1483749-addgesturerecognizer)Added [NSView.allowsVibrancy](https://developer.apple.com/documentation/appkit/nsview/1483793-allowsvibrancy)Added [NSView.alphaValue](https://developer.apple.com/documentation/appkit/nsview/1483560-alphavalue)Added [NSView.autoresizesSubviews](https://developer.apple.com/documentation/appkit/nsview/1483358-autoresizessubviews)Added [NSView.autoresizingMask](https://developer.apple.com/documentation/appkit/nsview/1483281-autoresizingmask)Added [NSView.backgroundFilters](https://developer.apple.com/documentation/appkit/nsview/1483689-backgroundfilters)Added [NSView.bounds](https://developer.apple.com/documentation/appkit/nsview/1483817-bounds)Added [NSView.boundsRotation](https://developer.apple.com/documentation/appkit/nsview/1483746-boundsrotation)Added [NSView.canBecomeKeyView](https://developer.apple.com/documentation/appkit/nsview/1483759-canbecomekeyview)Added [NSView.canDraw](https://developer.apple.com/documentation/appkit/nsview/1483277-candraw)Added [NSView.canDrawConcurrently](https://developer.apple.com/documentation/appkit/nsview/1483425-candrawconcurrently)Added [NSView.canDrawSubviewsIntoLayer](https://developer.apple.com/documentation/appkit/nsview/1483347-candrawsubviewsintolayer)Added [NSView.compositingFilter](https://developer.apple.com/documentation/appkit/nsview/1483516-compositingfilter)Added [NSView.contentFilters](https://developer.apple.com/documentation/appkit/nsview/1483703-contentfilters)Added [NSView.drawingFindIndicator](https://developer.apple.com/documentation/appkit/nsview/1483317-isdrawingfindindicator)Added [NSView.enclosingScrollView](https://developer.apple.com/documentation/appkit/nsview/1483654-enclosingscrollview)Added [NSView.flipped](https://developer.apple.com/documentation/appkit/nsview/1483532-flipped)Added [NSView.focusRingMaskBounds](https://developer.apple.com/documentation/appkit/nsview/1483287-focusringmaskbounds)Added [NSView.focusRingType](https://developer.apple.com/documentation/appkit/nsview/1483261-focusringtype)Added [NSView.frame](https://developer.apple.com/documentation/appkit/nsview/1483713-frame)Added [NSView.frameCenterRotation](https://developer.apple.com/documentation/appkit/nsview/1483367-framecenterrotation)Added [NSView.frameRotation](https://developer.apple.com/documentation/appkit/nsview/1483412-framerotation)Added [NSView.gestureRecognizers](https://developer.apple.com/documentation/appkit/nsview/1483658-gesturerecognizers)Added [NSView.heightAdjustLimit](https://developer.apple.com/documentation/appkit/nsview/1483691-heightadjustlimit)Added [NSView.hidden](https://developer.apple.com/documentation/appkit/nsview/1483369-ishidden)Added [NSView.hiddenOrHasHiddenAncestor](https://developer.apple.com/documentation/appkit/nsview/1483473-ishiddenorhashiddenancestor)Added [NSView.inFullScreenMode](https://developer.apple.com/documentation/appkit/nsview/1483337-isinfullscreenmode)Added [NSView.inLiveResize](https://developer.apple.com/documentation/appkit/nsview/1483267-inliveresize)Added [-[NSView initWithCoder:]](https://developer.apple.com/documentation/appkit/nsview/1483715-init)Added [NSView.inputContext](https://developer.apple.com/documentation/appkit/nsview/1483323-inputcontext)Added [NSView.layer](https://developer.apple.com/documentation/appkit/nsview/1483298-layer)Added [NSView.layerContentsPlacement](https://developer.apple.com/documentation/appkit/nsview/1483375-layercontentsplacement)Added [NSView.layerContentsRedrawPolicy](https://developer.apple.com/documentation/appkit/nsview/1483514-layercontentsredrawpolicy)Added [NSView.layerUsesCoreImageFilters](https://developer.apple.com/documentation/appkit/nsview/1483576-layerusescoreimagefilters)Added [NSView.mouseDownCanMoveWindow](https://developer.apple.com/documentation/appkit/nsview/1483666-mousedowncanmovewindow)Added [NSView.needsDisplay](https://developer.apple.com/documentation/appkit/nsview/1483360-needsdisplay)Added [NSView.needsPanelToBecomeKey](https://developer.apple.com/documentation/appkit/nsview/1483512-needspaneltobecomekey)Added [NSView.nextKeyView](https://developer.apple.com/documentation/appkit/nsview/1483465-nextkeyview)Added [NSView.nextValidKeyView](https://developer.apple.com/documentation/appkit/nsview/1483572-nextvalidkeyview)Added [NSView.opaque](https://developer.apple.com/documentation/appkit/nsview/1483558-isopaque)Added [NSView.opaqueAncestor](https://developer.apple.com/documentation/appkit/nsview/1483383-opaqueancestor)Added [NSView.pageFooter](https://developer.apple.com/documentation/appkit/nsview/1483355-pagefooter)Added [NSView.pageHeader](https://developer.apple.com/documentation/appkit/nsview/1483674-pageheader)Added [NSView.postsBoundsChangedNotifications](https://developer.apple.com/documentation/appkit/nsview/1483239-postsboundschangednotifications)Added [NSView.postsFrameChangedNotifications](https://developer.apple.com/documentation/appkit/nsview/1483524-postsframechangednotifications)Added [NSView.preservesContentDuringLiveResize](https://developer.apple.com/documentation/appkit/nsview/1483795-preservescontentduringliveresize)Added [NSView.previousKeyView](https://developer.apple.com/documentation/appkit/nsview/1483646-previouskeyview)Added [NSView.previousValidKeyView](https://developer.apple.com/documentation/appkit/nsview/1483371-previousvalidkeyview)Added [NSView.printJobTitle](https://developer.apple.com/documentation/appkit/nsview/1483753-printjobtitle)Added [NSView.rectPreservedDuringLiveResize](https://developer.apple.com/documentation/appkit/nsview/1483528-rectpreservedduringliveresize)Added [NSView.registeredDraggedTypes](https://developer.apple.com/documentation/appkit/nsview/1483564-registereddraggedtypes)Added [-[NSView removeGestureRecognizer:]](https://developer.apple.com/documentation/appkit/nsview/1483789-removegesturerecognizer)Added [NSView.rotatedFromBase](https://developer.apple.com/documentation/appkit/nsview/1483709-rotatedfrombase)Added [NSView.rotatedOrScaledFromBase](https://developer.apple.com/documentation/appkit/nsview/1483390-rotatedorscaledfrombase)Added [NSView.shadow](https://developer.apple.com/documentation/appkit/nsview/1483263-shadow)Added [NSView.subviews](https://developer.apple.com/documentation/appkit/nsview/1483539-subviews)Added [NSView.superview](https://developer.apple.com/documentation/appkit/nsview/1483737-superview)Added [NSView.tag](https://developer.apple.com/documentation/appkit/nsview/1483248-tag)Added [NSView.toolTip](https://developer.apple.com/documentation/appkit/nsview/1483541-tooltip)Added [NSView.trackingAreas](https://developer.apple.com/documentation/appkit/nsview/1483333-trackingareas)Added [NSView.userInterfaceLayoutDirection](https://developer.apple.com/documentation/appkit/nsview/1483254-userinterfacelayoutdirection)Added [NSView.visibleRect](https://developer.apple.com/documentation/appkit/nsview/1483446-visiblerect)Added [NSView.wantsDefaultClipping](https://developer.apple.com/documentation/appkit/nsview/1483365-wantsdefaultclipping)Added [NSView.wantsLayer](https://developer.apple.com/documentation/appkit/nsview/1483695-wantslayer)Added [NSView.wantsRestingTouches](https://developer.apple.com/documentation/appkit/nsview/1483594-wantsrestingtouches)Added [NSView.wantsUpdateLayer](https://developer.apple.com/documentation/appkit/nsview/1483461-wantsupdatelayer)Added [NSView.widthAdjustLimit](https://developer.apple.com/documentation/appkit/nsview/1483392-widthadjustlimit)Added [NSView.window](https://developer.apple.com/documentation/appkit/nsview/1483301-window)Added [NSAutoresizingMaskOptions](https://developer.apple.com/documentation/appkit/nsautoresizingmaskoptions)Added NSView(NSGestureRecognizer)Modified [NSView](https://developer.apple.com/documentation/appkit/nsview)

|  | Protocols |
| --- | --- |
| From | NSAnimatablePropertyContainer, NSAppearanceCustomization, NSDraggingDestination, NSUserInterfaceItemIdentification |
| To | NSAccessibility, NSAccessibilityElement, NSAnimatablePropertyContainer, NSAppearanceCustomization, NSDraggingDestination, NSUserInterfaceItemIdentification |

Modified [-[NSView allocateGState]](https://developer.apple.com/documentation/appkit/nsview/1483581-allocategstate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSView convertPointFromBase:]](https://developer.apple.com/documentation/appkit/nsview/1483778-convertpointfrombase)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified [-[NSView convertPointToBase:]](https://developer.apple.com/documentation/appkit/nsview/1483362-convertpointtobase)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified [-[NSView convertRectFromBase:]](https://developer.apple.com/documentation/appkit/nsview/1483591-convertrectfrombase)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified [-[NSView convertRectToBase:]](https://developer.apple.com/documentation/appkit/nsview/1483331-convertrecttobase)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified [-[NSView convertSizeFromBase:]](https://developer.apple.com/documentation/appkit/nsview/1483357-convertsizefrombase)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified [-[NSView convertSizeToBase:]](https://developer.apple.com/documentation/appkit/nsview/1483349-convertsizetobase)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified [-[NSView dragImage:at:offset:event:pasteboard:source:slideBack:]](https://developer.apple.com/documentation/appkit/nsview/1483279-dragimage)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified [-[NSView gState]](https://developer.apple.com/documentation/appkit/nsview/1483313-gstate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSView initWithFrame:]](https://developer.apple.com/documentation/appkit/nsview/1483458-initwithframe)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithFrame:(NSRect)frameRect ``` | -- |
| To | ``` - (instancetype)initWithFrame:(NSRect)frameRect ``` | yes |

Modified [-[NSView releaseGState]](https://developer.apple.com/documentation/appkit/nsview/1483761-releasegstate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSView renewGState]](https://developer.apple.com/documentation/appkit/nsview/1483727-renewgstate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSView setUpGState]](https://developer.apple.com/documentation/appkit/nsview/1483652-setupgstate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSView shouldDrawColor]](https://developer.apple.com/documentation/appkit/nsview/1483250-shoulddrawcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

NSViewController.hRemoved [-[NSViewController nibBundle]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434433-nibbundle)Removed [-[NSViewController nibName]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434472-nibname)Removed [-[NSViewController representedObject]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434453-representedobject)Removed [-[NSViewController setRepresentedObject:]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434453-representedobject)Removed [-[NSViewController setTitle:]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434426-title)Removed [-[NSViewController setView:]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434401-view)Removed [-[NSViewController title]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434426-title)Removed [-[NSViewController view]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434401-view)Added [-[NSViewController addChildViewController:]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434501-addchildviewcontroller)Added [NSViewController.childViewControllers](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434432-childviewcontrollers)Added [-[NSViewController dismissController:]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434447-dismisscontroller)Added [-[NSViewController dismissViewController:]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434413-dismiss)Added [NSViewController.extensionContext](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434457-extensioncontext)Added [-[NSViewController initWithCoder:]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434441-initwithcoder)Added [-[NSViewController insertChildViewController:atIndex:]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434437-insertchildviewcontroller)Added [NSViewController.nibBundle](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434433-nibbundle)Added [NSViewController.nibName](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434472-nibname)Added [NSViewController.parentViewController](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434491-parentviewcontroller)Added [NSViewController.preferredContentSize](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434409-preferredcontentsize)Added [-[NSViewController preferredContentSizeDidChangeForViewController:]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434434-preferredcontentsizedidchangefor)Added [NSViewController.preferredMaximumSize](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434403-preferredmaximumsize)Added [NSViewController.preferredMinimumSize](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434418-preferredminimumsize)Added [NSViewController.preferredScreenOrigin](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434468-preferredscreenorigin)Added [-[NSViewController presentViewController:animator:]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434431-presentviewcontroller)Added [-[NSViewController presentViewController:asPopoverRelativeToRect:ofView:preferredEdge:behavior:]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434422-present)Added [-[NSViewController presentViewControllerAsModalWindow:]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434462-presentviewcontrollerasmodalwind)Added [-[NSViewController presentViewControllerAsSheet:]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434489-presentassheet)Added [NSViewController.presentedViewControllers](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434497-presentedviewcontrollers)Added [NSViewController.presentingViewController](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434439-presentingviewcontroller)Added [-[NSViewController removeChildViewControllerAtIndex:]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434404-removechild)Added [-[NSViewController removeFromParentViewController]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434466-removefromparent)Added [NSViewController.representedObject](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434453-representedobject)Added [NSViewController.sourceItemView](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434479-sourceitemview)Added [NSViewController.storyboard](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434499-storyboard)Added [NSViewController.title](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434426-title)Added [-[NSViewController transitionFromViewController:toViewController:options:completionHandler:]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434407-transitionfromviewcontroller)Added [-[NSViewController updateViewConstraints]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434400-updateviewconstraints)Added [NSViewController.view](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434401-view)Added [-[NSViewController viewDidAppear]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434455-viewdidappear)Added [-[NSViewController viewDidDisappear]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434416-viewdiddisappear)Added [-[NSViewController viewDidLayout]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434451-viewdidlayout)Added [-[NSViewController viewDidLoad]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434476-viewdidload)Added [NSViewController.viewLoaded](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434435-viewloaded)Added [-[NSViewController viewWillAppear]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434415-viewwillappear)Added [-[NSViewController viewWillDisappear]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434483-viewwilldisappear)Added [-[NSViewController viewWillLayout]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434495-viewwilllayout)Added [-[NSViewController viewWillTransitionToSize:]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434443-viewwilltransition)Added [NSViewControllerPresentationAnimator](https://developer.apple.com/documentation/appkit/nsviewcontrollerpresentationanimator)Added [-[NSViewControllerPresentationAnimator animateDismissalOfViewController:fromViewController:]](https://developer.apple.com/documentation/appkit/nsviewcontrollerpresentationanimator/1434458-animatedismissal)Added [-[NSViewControllerPresentationAnimator animatePresentationOfViewController:fromViewController:]](https://developer.apple.com/documentation/appkit/nsviewcontrollerpresentationanimator/1434396-animatepresentationofviewcontrol)Added NSViewController(NSExtensionAdditions)Added NSViewController(NSViewControllerContainer)Added NSViewController(NSViewControllerPresentation)Added NSViewController(NSViewControllerPresentationAndTransitionStyles)Added NSViewController(NSViewControllerStoryboardingMethods)Added [NSViewControllerTransitionAllowUserInteraction](https://developer.apple.com/documentation/appkit/nsviewcontrollertransitionoptions/nsviewcontrollertransitionallowuserinteraction)Added [NSViewControllerTransitionCrossfade](https://developer.apple.com/documentation/appkit/nsviewcontrollertransitionoptions/nsviewcontrollertransitioncrossfade)Added [NSViewControllerTransitionNone](https://developer.apple.com/documentation/appkit/nsviewcontrollertransitionoptions/nsviewcontrollertransitionnone)Added [NSViewControllerTransitionOptions](https://developer.apple.com/documentation/appkit/nsviewcontrollertransitionoptions)Added [NSViewControllerTransitionSlideBackward](https://developer.apple.com/documentation/appkit/nsviewcontroller/transitionoptions/1434460-slidebackward)Added [NSViewControllerTransitionSlideDown](https://developer.apple.com/documentation/appkit/nsviewcontrollertransitionoptions/nsviewcontrollertransitionslidedown)Added [NSViewControllerTransitionSlideForward](https://developer.apple.com/documentation/appkit/nsviewcontrollertransitionoptions/nsviewcontrollertransitionslideforward)Added [NSViewControllerTransitionSlideLeft](https://developer.apple.com/documentation/appkit/nsviewcontroller/transitionoptions/1434478-slideleft)Added [NSViewControllerTransitionSlideRight](https://developer.apple.com/documentation/appkit/nsviewcontroller/transitionoptions/1434474-slideright)Added [NSViewControllerTransitionSlideUp](https://developer.apple.com/documentation/appkit/nsviewcontrollertransitionoptions/nsviewcontrollertransitionslideup)Modified [NSViewController](https://developer.apple.com/documentation/appkit/nsviewcontroller)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSCoding, NSSeguePerforming, NSUserInterfaceItemIdentification |

Modified [-[NSViewController initWithNibName:bundle:]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434481-initwithnibname)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil ``` | -- |
| To | ``` - (instancetype)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil ``` | yes |

NSVisualEffectView.h (Added)Added [NSVisualEffectView](https://developer.apple.com/documentation/appkit/nsvisualeffectview)Added [NSVisualEffectView.blendingMode](https://developer.apple.com/documentation/appkit/nsvisualeffectview/1535468-blendingmode)Added [NSVisualEffectView.interiorBackgroundStyle](https://developer.apple.com/documentation/appkit/nsvisualeffectview/1529998-interiorbackgroundstyle)Added [NSVisualEffectView.maskImage](https://developer.apple.com/documentation/appkit/nsvisualeffectview/1535318-maskimage)Added [NSVisualEffectView.material](https://developer.apple.com/documentation/appkit/nsvisualeffectview/1526623-material)Added [NSVisualEffectView.state](https://developer.apple.com/documentation/appkit/nsvisualeffectview/1532403-state)Added [-[NSVisualEffectView viewDidMoveToWindow]](https://developer.apple.com/documentation/appkit/nsvisualeffectview/1534300-viewdidmovetowindow)Added [-[NSVisualEffectView viewWillMoveToWindow:]](https://developer.apple.com/documentation/appkit/nsvisualeffectview/1534276-viewwillmovetowindow)Added [NSVisualEffectBlendingMode](https://developer.apple.com/documentation/appkit/nsvisualeffectblendingmode)Added [NSVisualEffectBlendingModeBehindWindow](https://developer.apple.com/documentation/appkit/nsvisualeffectview/blendingmode/behindwindow)Added [NSVisualEffectBlendingModeWithinWindow](https://developer.apple.com/documentation/appkit/nsvisualeffectblendingmode/nsvisualeffectblendingmodewithinwindow)Added [NSVisualEffectMaterial](https://developer.apple.com/documentation/appkit/nsvisualeffectview/material)Added [NSVisualEffectMaterialAppearanceBased](https://developer.apple.com/documentation/appkit/nsvisualeffectview/material/appearancebased)Added [NSVisualEffectMaterialDark](https://developer.apple.com/documentation/appkit/nsvisualeffectview/material/dark)Added [NSVisualEffectMaterialLight](https://developer.apple.com/documentation/appkit/nsvisualeffectmaterial/nsvisualeffectmateriallight)Added [NSVisualEffectMaterialTitlebar](https://developer.apple.com/documentation/appkit/nsvisualeffectmaterial/nsvisualeffectmaterialtitlebar)Added [NSVisualEffectState](https://developer.apple.com/documentation/appkit/nsvisualeffectview/state)Added [NSVisualEffectStateActive](https://developer.apple.com/documentation/appkit/nsvisualeffectstate/nsvisualeffectstateactive)Added [NSVisualEffectStateFollowsWindowActiveState](https://developer.apple.com/documentation/appkit/nsvisualeffectstate/nsvisualeffectstatefollowswindowactivestate)Added [NSVisualEffectStateInactive](https://developer.apple.com/documentation/appkit/nsvisualeffectstate/nsvisualeffectstateinactive)NSWindow.hRemoved [-[NSWindow acceptsMouseMovedEvents]](https://developer.apple.com/documentation/appkit/nswindow/1419340-acceptsmousemovedevents)Removed [-[NSWindow allowsConcurrentViewDrawing]](https://developer.apple.com/documentation/appkit/nswindow/1419300-allowsconcurrentviewdrawing)Removed [-[NSWindow allowsToolTipsWhenApplicationIsInactive]](https://developer.apple.com/documentation/appkit/nswindow/1419138-allowstooltipswhenapplicationisi)Removed [-[NSWindow alphaValue]](https://developer.apple.com/documentation/appkit/nswindow/1419186-alphavalue)Removed [-[NSWindow animationBehavior]](https://developer.apple.com/documentation/appkit/nswindow/1419763-animationbehavior)Removed [-[NSWindow areCursorRectsEnabled]](https://developer.apple.com/documentation/appkit/nswindow/1419668-arecursorrectsenabled)Removed [-[NSWindow aspectRatio]](https://developer.apple.com/documentation/appkit/nswindow/1419507-aspectratio)Removed [-[NSWindow attachedSheet]](https://developer.apple.com/documentation/appkit/nswindow/1419467-attachedsheet)Removed [-[NSWindow autorecalculatesKeyViewLoop]](https://developer.apple.com/documentation/appkit/nswindow/1419214-autorecalculateskeyviewloop)Removed [-[NSWindow backgroundColor]](https://developer.apple.com/documentation/appkit/nswindow/1419751-backgroundcolor)Removed [-[NSWindow backingLocation]](https://developer.apple.com/documentation/appkit/nswindow/1419074-backinglocation)Removed [-[NSWindow backingScaleFactor]](https://developer.apple.com/documentation/appkit/nswindow/1419459-backingscalefactor)Removed [-[NSWindow backingType]](https://developer.apple.com/documentation/appkit/nswindow/1419599-backingtype)Removed [-[NSWindow canBecomeKeyWindow]](https://developer.apple.com/documentation/appkit/nswindow/1419543-canbecomekeywindow)Removed [-[NSWindow canBecomeMainWindow]](https://developer.apple.com/documentation/appkit/nswindow/1419162-canbecomemain)Removed [-[NSWindow canBecomeVisibleWithoutLogin]](https://developer.apple.com/documentation/appkit/nswindow/1419179-canbecomevisiblewithoutlogin)Removed [-[NSWindow canHide]](https://developer.apple.com/documentation/appkit/nswindow/1419725-canhide)Removed [-[NSWindow childWindows]](https://developer.apple.com/documentation/appkit/nswindow/1419236-childwindows)Removed [-[NSWindow collectionBehavior]](https://developer.apple.com/documentation/appkit/nswindow/1419471-collectionbehavior)Removed [-[NSWindow colorSpace]](https://developer.apple.com/documentation/appkit/nswindow/1419569-colorspace)Removed [-[NSWindow contentAspectRatio]](https://developer.apple.com/documentation/appkit/nswindow/1419148-contentaspectratio)Removed [-[NSWindow contentMaxSize]](https://developer.apple.com/documentation/appkit/nswindow/1419154-contentmaxsize)Removed [-[NSWindow contentMinSize]](https://developer.apple.com/documentation/appkit/nswindow/1419670-contentminsize)Removed [-[NSWindow contentResizeIncrements]](https://developer.apple.com/documentation/appkit/nswindow/1419649-contentresizeincrements)Removed [-[NSWindow contentView]](https://developer.apple.com/documentation/appkit/nswindow/1419160-contentview)Removed [-[NSWindow currentEvent]](https://developer.apple.com/documentation/appkit/nswindow/1419298-currentevent)Removed [-[NSWindow deepestScreen]](https://developer.apple.com/documentation/appkit/nswindow/1419080-deepestscreen)Removed [-[NSWindow delegate]](https://developer.apple.com/documentation/appkit/nswindow/1419060-delegate)Removed [-[NSWindow depthLimit]](https://developer.apple.com/documentation/appkit/nswindow/1419613-depthlimit)Removed [-[NSWindow deviceDescription]](https://developer.apple.com/documentation/appkit/nswindow/1419741-devicedescription)Removed [-[NSWindow displaysWhenScreenProfileChanges]](https://developer.apple.com/documentation/appkit/nswindow/1419430-displayswhenscreenprofilechanges)Removed [-[NSWindow dockTile]](https://developer.apple.com/documentation/appkit/nswindow/1419088-docktile)Removed [-[NSWindow firstResponder]](https://developer.apple.com/documentation/appkit/nswindow/1419440-firstresponder)Removed [-[NSWindow frame]](https://developer.apple.com/documentation/appkit/nswindow/1419697-frame)Removed [-[NSWindow graphicsContext]](https://developer.apple.com/documentation/appkit/nswindow/1419713-graphicscontext)Removed [-[NSWindow hasDynamicDepthLimit]](https://developer.apple.com/documentation/appkit/nswindow/1419330-hasdynamicdepthlimit)Removed [-[NSWindow hasShadow]](https://developer.apple.com/documentation/appkit/nswindow/1419234-hasshadow)Removed [-[NSWindow hidesOnDeactivate]](https://developer.apple.com/documentation/appkit/nswindow/1419777-hidesondeactivate)Removed [-[NSWindow ignoresMouseEvents]](https://developer.apple.com/documentation/appkit/nswindow/1419354-ignoresmouseevents)Removed [-[NSWindow inLiveResize]](https://developer.apple.com/documentation/appkit/nswindow/1419378-inliveresize)Removed [-[NSWindow initialFirstResponder]](https://developer.apple.com/documentation/appkit/nswindow/1419479-initialfirstresponder)Removed [-[NSWindow isAutodisplay]](https://developer.apple.com/documentation/appkit/nswindow/1419262-isautodisplay)Removed [-[NSWindow isDocumentEdited]](https://developer.apple.com/documentation/appkit/nswindow/1419311-isdocumentedited)Removed [-[NSWindow isExcludedFromWindowsMenu]](https://developer.apple.com/documentation/appkit/nswindow/1419175-excludedfromwindowsmenu)Removed [-[NSWindow isFlushWindowDisabled]](https://developer.apple.com/documentation/appkit/nswindow/1419583-flushwindowdisabled)Removed [-[NSWindow isKeyWindow]](https://developer.apple.com/documentation/appkit/nswindow/1419735-keywindow)Removed [-[NSWindow isMainWindow]](https://developer.apple.com/documentation/appkit/nswindow/1419130-ismainwindow)Removed [-[NSWindow isMiniaturized]](https://developer.apple.com/documentation/appkit/nswindow/1419699-miniaturized)Removed [-[NSWindow isMovable]](https://developer.apple.com/documentation/appkit/nswindow/1419579-movable)Removed [-[NSWindow isMovableByWindowBackground]](https://developer.apple.com/documentation/appkit/nswindow/1419072-movablebywindowbackground)Removed [-[NSWindow isOnActiveSpace]](https://developer.apple.com/documentation/appkit/nswindow/1419707-onactivespace)Removed [-[NSWindow isOneShot]](https://developer.apple.com/documentation/appkit/nswindow/1419222-oneshot)Removed [-[NSWindow isOpaque]](https://developer.apple.com/documentation/appkit/nswindow/1419086-isopaque)Removed [-[NSWindow isReleasedWhenClosed]](https://developer.apple.com/documentation/appkit/nswindow/1419062-isreleasedwhenclosed)Removed [-[NSWindow isSheet]](https://developer.apple.com/documentation/appkit/nswindow/1419364-issheet)Removed [-[NSWindow isVisible]](https://developer.apple.com/documentation/appkit/nswindow/1419132-visible)Removed [-[NSWindow isZoomed]](https://developer.apple.com/documentation/appkit/nswindow/1419398-zoomed)Removed [-[NSWindow keyViewSelectionDirection]](https://developer.apple.com/documentation/appkit/nswindow/1419158-keyviewselectiondirection)Removed [-[NSWindow level]](https://developer.apple.com/documentation/appkit/nswindow/1419511-level)Removed [-[NSWindow maxSize]](https://developer.apple.com/documentation/appkit/nswindow/1419595-maxsize)Removed [-[NSWindow minSize]](https://developer.apple.com/documentation/appkit/nswindow/1419206-minsize)Removed [-[NSWindow miniwindowImage]](https://developer.apple.com/documentation/appkit/nswindow/1419185-miniwindowimage)Removed [-[NSWindow miniwindowTitle]](https://developer.apple.com/documentation/appkit/nswindow/1419571-miniwindowtitle)Removed [-[NSWindow mouseLocationOutsideOfEventStream]](https://developer.apple.com/documentation/appkit/nswindow/1419280-mouselocationoutsideofeventstrea)Removed [-[NSWindow occlusionState]](https://developer.apple.com/documentation/appkit/nswindow/1419321-occlusionstate)Removed [-[NSWindow parentWindow]](https://developer.apple.com/documentation/appkit/nswindow/1419695-parentwindow)Removed [-[NSWindow preferredBackingLocation]](https://developer.apple.com/documentation/appkit/nswindow/1419102-preferredbackinglocation)Removed [-[NSWindow preservesContentDuringLiveResize]](https://developer.apple.com/documentation/appkit/nswindow/1419588-preservescontentduringliveresize)Removed [-[NSWindow preventsApplicationTerminationWhenModal]](https://developer.apple.com/documentation/appkit/nswindow/1419743-preventsapplicationterminationwh)Removed [-[NSWindow representedFilename]](https://developer.apple.com/documentation/appkit/nswindow/1419631-representedfilename)Removed [-[NSWindow representedURL]](https://developer.apple.com/documentation/appkit/nswindow/1419066-representedurl)Removed [-[NSWindow resizeFlags]](https://developer.apple.com/documentation/appkit/nswindow/1419302-resizeflags)Removed [-[NSWindow resizeIncrements]](https://developer.apple.com/documentation/appkit/nswindow/1419390-resizeincrements)Removed [-[NSWindow screen]](https://developer.apple.com/documentation/appkit/nswindow/1419232-screen)Removed [-[NSWindow setAcceptsMouseMovedEvents:]](https://developer.apple.com/documentation/appkit/nswindow/1419340-acceptsmousemovedevents)Removed [-[NSWindow setAllowsConcurrentViewDrawing:]](https://developer.apple.com/documentation/appkit/nswindow/1419300-allowsconcurrentviewdrawing)Removed [-[NSWindow setAllowsToolTipsWhenApplicationIsInactive:]](https://developer.apple.com/documentation/appkit/nswindow/1419138-allowstooltipswhenapplicationisi)Removed [-[NSWindow setAlphaValue:]](https://developer.apple.com/documentation/appkit/nswindow/1419186-alphavalue)Removed [-[NSWindow setAnimationBehavior:]](https://developer.apple.com/documentation/appkit/nswindow/1419763-animationbehavior)Removed [-[NSWindow setAspectRatio:]](https://developer.apple.com/documentation/appkit/nswindow/1419507-aspectratio)Removed [-[NSWindow setAutodisplay:]](https://developer.apple.com/documentation/appkit/nswindow/1419262-autodisplay)Removed [-[NSWindow setAutorecalculatesKeyViewLoop:]](https://developer.apple.com/documentation/appkit/nswindow/1419214-autorecalculateskeyviewloop)Removed [-[NSWindow setBackgroundColor:]](https://developer.apple.com/documentation/appkit/nswindow/1419751-backgroundcolor)Removed [-[NSWindow setBackingType:]](https://developer.apple.com/documentation/appkit/nswindow/1419599-backingtype)Removed [-[NSWindow setCanBecomeVisibleWithoutLogin:]](https://developer.apple.com/documentation/appkit/nswindow/1419179-canbecomevisiblewithoutlogin)Removed [-[NSWindow setCanHide:]](https://developer.apple.com/documentation/appkit/nswindow/1419725-canhide)Removed [-[NSWindow setCollectionBehavior:]](https://developer.apple.com/documentation/appkit/nswindow/1419471-collectionbehavior)Removed [-[NSWindow setColorSpace:]](https://developer.apple.com/documentation/appkit/nswindow/1419569-colorspace)Removed [-[NSWindow setContentAspectRatio:]](https://developer.apple.com/documentation/appkit/nswindow/1419148-contentaspectratio)Removed [-[NSWindow setContentMaxSize:]](https://developer.apple.com/documentation/appkit/nswindow/1419154-contentmaxsize)Removed [-[NSWindow setContentMinSize:]](https://developer.apple.com/documentation/appkit/nswindow/1419670-contentminsize)Removed [-[NSWindow setContentResizeIncrements:]](https://developer.apple.com/documentation/appkit/nswindow/1419649-contentresizeincrements)Removed [-[NSWindow setContentView:]](https://developer.apple.com/documentation/appkit/nswindow/1419160-contentview)Removed [-[NSWindow setDelegate:]](https://developer.apple.com/documentation/appkit/nswindow/1419060-delegate)Removed [-[NSWindow setDepthLimit:]](https://developer.apple.com/documentation/appkit/nswindow/1419613-depthlimit)Removed [-[NSWindow setDisplaysWhenScreenProfileChanges:]](https://developer.apple.com/documentation/appkit/nswindow/1419430-displayswhenscreenprofilechanges)Removed [-[NSWindow setDocumentEdited:]](https://developer.apple.com/documentation/appkit/nswindow/1419311-documentedited)Removed [-[NSWindow setExcludedFromWindowsMenu:]](https://developer.apple.com/documentation/appkit/nswindow/1419175-isexcludedfromwindowsmenu)Removed [-[NSWindow setHasShadow:]](https://developer.apple.com/documentation/appkit/nswindow/1419234-hasshadow)Removed [-[NSWindow setHidesOnDeactivate:]](https://developer.apple.com/documentation/appkit/nswindow/1419777-hidesondeactivate)Removed [-[NSWindow setIgnoresMouseEvents:]](https://developer.apple.com/documentation/appkit/nswindow/1419354-ignoresmouseevents)Removed [-[NSWindow setInitialFirstResponder:]](https://developer.apple.com/documentation/appkit/nswindow/1419479-initialfirstresponder)Removed [-[NSWindow setLevel:]](https://developer.apple.com/documentation/appkit/nswindow/1419511-level)Removed [-[NSWindow setMaxSize:]](https://developer.apple.com/documentation/appkit/nswindow/1419595-maxsize)Removed [-[NSWindow setMinSize:]](https://developer.apple.com/documentation/appkit/nswindow/1419206-minsize)Removed [-[NSWindow setMiniwindowImage:]](https://developer.apple.com/documentation/appkit/nswindow/1419185-miniwindowimage)Removed [-[NSWindow setMiniwindowTitle:]](https://developer.apple.com/documentation/appkit/nswindow/1419571-miniwindowtitle)Removed [-[NSWindow setMovable:]](https://developer.apple.com/documentation/appkit/nswindow/1419579-movable)Removed [-[NSWindow setMovableByWindowBackground:]](https://developer.apple.com/documentation/appkit/nswindow/1419072-movablebywindowbackground)Removed [-[NSWindow setOneShot:]](https://developer.apple.com/documentation/appkit/nswindow/1419222-oneshot)Removed [-[NSWindow setOpaque:]](https://developer.apple.com/documentation/appkit/nswindow/1419086-isopaque)Removed [-[NSWindow setParentWindow:]](https://developer.apple.com/documentation/appkit/nswindow/1419695-parent)Removed [-[NSWindow setPreferredBackingLocation:]](https://developer.apple.com/documentation/appkit/nswindow/1419102-preferredbackinglocation)Removed [-[NSWindow setPreservesContentDuringLiveResize:]](https://developer.apple.com/documentation/appkit/nswindow/1419588-preservescontentduringliveresize)Removed [-[NSWindow setPreventsApplicationTerminationWhenModal:]](https://developer.apple.com/documentation/appkit/nswindow/1419743-preventsapplicationterminationwh)Removed [-[NSWindow setReleasedWhenClosed:]](https://developer.apple.com/documentation/appkit/nswindow/1419062-releasedwhenclosed)Removed [-[NSWindow setRepresentedFilename:]](https://developer.apple.com/documentation/appkit/nswindow/1419631-representedfilename)Removed [-[NSWindow setRepresentedURL:]](https://developer.apple.com/documentation/appkit/nswindow/1419066-representedurl)Removed [-[NSWindow setResizeIncrements:]](https://developer.apple.com/documentation/appkit/nswindow/1419390-resizeincrements)Removed [-[NSWindow setSharingType:]](https://developer.apple.com/documentation/appkit/nswindow/1419729-sharingtype)Removed [-[NSWindow setShowsResizeIndicator:]](https://developer.apple.com/documentation/appkit/nswindow/1419531-showsresizeindicator)Removed [-[NSWindow setShowsToolbarButton:]](https://developer.apple.com/documentation/appkit/nswindow/1419196-showstoolbarbutton)Removed [-[NSWindow setTitle:]](https://developer.apple.com/documentation/appkit/nswindow/1419404-title)Removed [-[NSWindow setToolbar:]](https://developer.apple.com/documentation/appkit/nswindow/1419731-toolbar)Removed [-[NSWindow setViewsNeedDisplay:]](https://developer.apple.com/documentation/appkit/nswindow/1419609-viewsneeddisplay)Removed [-[NSWindow sharingType]](https://developer.apple.com/documentation/appkit/nswindow/1419729-sharingtype)Removed [-[NSWindow sheetParent]](https://developer.apple.com/documentation/appkit/nswindow/1419052-sheetparent)Removed [-[NSWindow sheets]](https://developer.apple.com/documentation/appkit/nswindow/1419765-sheets)Removed [-[NSWindow showsResizeIndicator]](https://developer.apple.com/documentation/appkit/nswindow/1419531-showsresizeindicator)Removed [-[NSWindow showsToolbarButton]](https://developer.apple.com/documentation/appkit/nswindow/1419196-showstoolbarbutton)Removed [-[NSWindow stringWithSavedFrame]](https://developer.apple.com/documentation/appkit/nswindow/1419515-framedescriptor)Removed -[NSWindow styleMask]Removed [-[NSWindow title]](https://developer.apple.com/documentation/appkit/nswindow/1419404-title)Removed [-[NSWindow toolbar]](https://developer.apple.com/documentation/appkit/nswindow/1419731-toolbar)Removed [-[NSWindow viewsNeedDisplay]](https://developer.apple.com/documentation/appkit/nswindow/1419609-viewsneeddisplay)Removed [-[NSWindow windowNumber]](https://developer.apple.com/documentation/appkit/nswindow/1419068-windownumber)Removed [-[NSWindow windowRef]](https://developer.apple.com/documentation/appkit/nswindow/1419485-windowref)Removed [-[NSWindow worksWhenModal]](https://developer.apple.com/documentation/appkit/nswindow/1419220-workswhenmodal)Added [NSWindow.acceptsMouseMovedEvents](https://developer.apple.com/documentation/appkit/nswindow/1419340-acceptsmousemovedevents)Added [-[NSWindow addTitlebarAccessoryViewController:]](https://developer.apple.com/documentation/appkit/nswindow/1419382-addtitlebaraccessoryviewcontroll)Added [NSWindow.allowsConcurrentViewDrawing](https://developer.apple.com/documentation/appkit/nswindow/1419300-allowsconcurrentviewdrawing)Added [NSWindow.allowsToolTipsWhenApplicationIsInactive](https://developer.apple.com/documentation/appkit/nswindow/1419138-allowstooltipswhenapplicationisi)Added [NSWindow.alphaValue](https://developer.apple.com/documentation/appkit/nswindow/1419186-alphavalue)Added [NSWindow.animationBehavior](https://developer.apple.com/documentation/appkit/nswindow/1419763-animationbehavior)Added [NSWindow.areCursorRectsEnabled](https://developer.apple.com/documentation/appkit/nswindow/1419668-arecursorrectsenabled)Added [NSWindow.aspectRatio](https://developer.apple.com/documentation/appkit/nswindow/1419507-aspectratio)Added [NSWindow.attachedSheet](https://developer.apple.com/documentation/appkit/nswindow/1419467-attachedsheet)Added [NSWindow.autodisplay](https://developer.apple.com/documentation/appkit/nswindow/1419262-isautodisplay)Added [NSWindow.autorecalculatesKeyViewLoop](https://developer.apple.com/documentation/appkit/nswindow/1419214-autorecalculateskeyviewloop)Added [NSWindow.backgroundColor](https://developer.apple.com/documentation/appkit/nswindow/1419751-backgroundcolor)Added [NSWindow.backingLocation](https://developer.apple.com/documentation/appkit/nswindow/1419074-backinglocation)Added [NSWindow.backingScaleFactor](https://developer.apple.com/documentation/appkit/nswindow/1419459-backingscalefactor)Added [NSWindow.backingType](https://developer.apple.com/documentation/appkit/nswindow/1419599-backingtype)Added [NSWindow.canBecomeKeyWindow](https://developer.apple.com/documentation/appkit/nswindow/1419543-canbecomekey)Added [NSWindow.canBecomeMainWindow](https://developer.apple.com/documentation/appkit/nswindow/1419162-canbecomemainwindow)Added [NSWindow.canBecomeVisibleWithoutLogin](https://developer.apple.com/documentation/appkit/nswindow/1419179-canbecomevisiblewithoutlogin)Added [NSWindow.canHide](https://developer.apple.com/documentation/appkit/nswindow/1419725-canhide)Added [NSWindow.childWindows](https://developer.apple.com/documentation/appkit/nswindow/1419236-childwindows)Added [NSWindow.collectionBehavior](https://developer.apple.com/documentation/appkit/nswindow/1419471-collectionbehavior)Added [NSWindow.colorSpace](https://developer.apple.com/documentation/appkit/nswindow/1419569-colorspace)Added [NSWindow.contentAspectRatio](https://developer.apple.com/documentation/appkit/nswindow/1419148-contentaspectratio)Added [NSWindow.contentLayoutGuide](https://developer.apple.com/documentation/appkit/nswindow/1419094-contentlayoutguide)Added [NSWindow.contentLayoutRect](https://developer.apple.com/documentation/appkit/nswindow/1419124-contentlayoutrect)Added [NSWindow.contentMaxSize](https://developer.apple.com/documentation/appkit/nswindow/1419154-contentmaxsize)Added [NSWindow.contentMinSize](https://developer.apple.com/documentation/appkit/nswindow/1419670-contentminsize)Added [NSWindow.contentResizeIncrements](https://developer.apple.com/documentation/appkit/nswindow/1419649-contentresizeincrements)Added [NSWindow.contentView](https://developer.apple.com/documentation/appkit/nswindow/1419160-contentview)Added [NSWindow.contentViewController](https://developer.apple.com/documentation/appkit/nswindow/1419615-contentviewcontroller)Added [NSWindow.currentEvent](https://developer.apple.com/documentation/appkit/nswindow/1419298-currentevent)Added [NSWindow.deepestScreen](https://developer.apple.com/documentation/appkit/nswindow/1419080-deepestscreen)Added [NSWindow.delegate](https://developer.apple.com/documentation/appkit/nswindow/1419060-delegate)Added [NSWindow.depthLimit](https://developer.apple.com/documentation/appkit/nswindow/1419613-depthlimit)Added [NSWindow.deviceDescription](https://developer.apple.com/documentation/appkit/nswindow/1419741-devicedescription)Added [NSWindow.displaysWhenScreenProfileChanges](https://developer.apple.com/documentation/appkit/nswindow/1419430-displayswhenscreenprofilechanges)Added [NSWindow.dockTile](https://developer.apple.com/documentation/appkit/nswindow/1419088-docktile)Added [NSWindow.documentEdited](https://developer.apple.com/documentation/appkit/nswindow/1419311-isdocumentedited)Added [NSWindow.excludedFromWindowsMenu](https://developer.apple.com/documentation/appkit/nswindow/1419175-excludedfromwindowsmenu)Added [NSWindow.firstResponder](https://developer.apple.com/documentation/appkit/nswindow/1419440-firstresponder)Added [NSWindow.flushWindowDisabled](https://developer.apple.com/documentation/appkit/nswindow/1419583-isflushwindowdisabled)Added [NSWindow.frame](https://developer.apple.com/documentation/appkit/nswindow/1419697-frame)Added [NSWindow.graphicsContext](https://developer.apple.com/documentation/appkit/nswindow/1419713-graphicscontext)Added [NSWindow.hasDynamicDepthLimit](https://developer.apple.com/documentation/appkit/nswindow/1419330-hasdynamicdepthlimit)Added [NSWindow.hasShadow](https://developer.apple.com/documentation/appkit/nswindow/1419234-hasshadow)Added [NSWindow.hidesOnDeactivate](https://developer.apple.com/documentation/appkit/nswindow/1419777-hidesondeactivate)Added [NSWindow.ignoresMouseEvents](https://developer.apple.com/documentation/appkit/nswindow/1419354-ignoresmouseevents)Added [NSWindow.inLiveResize](https://developer.apple.com/documentation/appkit/nswindow/1419378-inliveresize)Added [NSWindow.initialFirstResponder](https://developer.apple.com/documentation/appkit/nswindow/1419479-initialfirstresponder)Added [-[NSWindow insertTitlebarAccessoryViewController:atIndex:]](https://developer.apple.com/documentation/appkit/nswindow/1419275-inserttitlebaraccessoryviewcontr)Added [NSWindow.keyViewSelectionDirection](https://developer.apple.com/documentation/appkit/nswindow/1419158-keyviewselectiondirection)Added [NSWindow.keyWindow](https://developer.apple.com/documentation/appkit/nswindow/1419735-keywindow)Added [NSWindow.level](https://developer.apple.com/documentation/appkit/nswindow/1419511-level)Added [NSWindow.mainWindow](https://developer.apple.com/documentation/appkit/nswindow/1419130-ismainwindow)Added [NSWindow.maxSize](https://developer.apple.com/documentation/appkit/nswindow/1419595-maxsize)Added [NSWindow.minSize](https://developer.apple.com/documentation/appkit/nswindow/1419206-minsize)Added [NSWindow.miniaturized](https://developer.apple.com/documentation/appkit/nswindow/1419699-miniaturized)Added [NSWindow.miniwindowImage](https://developer.apple.com/documentation/appkit/nswindow/1419185-miniwindowimage)Added [NSWindow.miniwindowTitle](https://developer.apple.com/documentation/appkit/nswindow/1419571-miniwindowtitle)Added [NSWindow.mouseLocationOutsideOfEventStream](https://developer.apple.com/documentation/appkit/nswindow/1419280-mouselocationoutsideofeventstrea)Added [NSWindow.movable](https://developer.apple.com/documentation/appkit/nswindow/1419579-ismovable)Added [NSWindow.movableByWindowBackground](https://developer.apple.com/documentation/appkit/nswindow/1419072-movablebywindowbackground)Added [NSWindow.occlusionState](https://developer.apple.com/documentation/appkit/nswindow/1419321-occlusionstate)Added [NSWindow.onActiveSpace](https://developer.apple.com/documentation/appkit/nswindow/1419707-onactivespace)Added [NSWindow.oneShot](https://developer.apple.com/documentation/appkit/nswindow/1419222-oneshot)Added [NSWindow.opaque](https://developer.apple.com/documentation/appkit/nswindow/1419086-isopaque)Added [NSWindow.parentWindow](https://developer.apple.com/documentation/appkit/nswindow/1419695-parent)Added [NSWindow.preferredBackingLocation](https://developer.apple.com/documentation/appkit/nswindow/1419102-preferredbackinglocation)Added [NSWindow.preservesContentDuringLiveResize](https://developer.apple.com/documentation/appkit/nswindow/1419588-preservescontentduringliveresize)Added [NSWindow.preventsApplicationTerminationWhenModal](https://developer.apple.com/documentation/appkit/nswindow/1419743-preventsapplicationterminationwh)Added [NSWindow.releasedWhenClosed](https://developer.apple.com/documentation/appkit/nswindow/1419062-isreleasedwhenclosed)Added [-[NSWindow removeTitlebarAccessoryViewControllerAtIndex:]](https://developer.apple.com/documentation/appkit/nswindow/1419643-removetitlebaraccessoryviewcontr)Added [NSWindow.representedFilename](https://developer.apple.com/documentation/appkit/nswindow/1419631-representedfilename)Added [NSWindow.representedURL](https://developer.apple.com/documentation/appkit/nswindow/1419066-representedurl)Added [NSWindow.resizeFlags](https://developer.apple.com/documentation/appkit/nswindow/1419302-resizeflags)Added [NSWindow.resizeIncrements](https://developer.apple.com/documentation/appkit/nswindow/1419390-resizeincrements)Added [NSWindow.screen](https://developer.apple.com/documentation/appkit/nswindow/1419232-screen)Added [NSWindow.sharingType](https://developer.apple.com/documentation/appkit/nswindow/1419729-sharingtype)Added [NSWindow.sheet](https://developer.apple.com/documentation/appkit/nswindow/1419364-sheet)Added [NSWindow.sheetParent](https://developer.apple.com/documentation/appkit/nswindow/1419052-sheetparent)Added [NSWindow.sheets](https://developer.apple.com/documentation/appkit/nswindow/1419765-sheets)Added [NSWindow.showsResizeIndicator](https://developer.apple.com/documentation/appkit/nswindow/1419531-showsresizeindicator)Added [NSWindow.showsToolbarButton](https://developer.apple.com/documentation/appkit/nswindow/1419196-showstoolbarbutton)Added [NSWindow.stringWithSavedFrame](https://developer.apple.com/documentation/appkit/nswindow/1419515-framedescriptor)Added [NSWindow.styleMask](https://developer.apple.com/documentation/appkit/nswindow/1419078-stylemask)Added [NSWindow.title](https://developer.apple.com/documentation/appkit/nswindow/1419404-title)Added [NSWindow.titleVisibility](https://developer.apple.com/documentation/appkit/nswindow/1419635-titlevisibility)Added [NSWindow.titlebarAccessoryViewControllers](https://developer.apple.com/documentation/appkit/nswindow/1419547-titlebaraccessoryviewcontrollers)Added [NSWindow.titlebarAppearsTransparent](https://developer.apple.com/documentation/appkit/nswindow/1419167-titlebarappearstransparent)Added [NSWindow.toolbar](https://developer.apple.com/documentation/appkit/nswindow/1419731-toolbar)Added [-[NSWindow trackEventsMatchingMask:timeout:mode:handler:]](https://developer.apple.com/documentation/appkit/nswindow/1419727-trackevents)Added [NSWindow.viewsNeedDisplay](https://developer.apple.com/documentation/appkit/nswindow/1419609-viewsneeddisplay)Added [NSWindow.visible](https://developer.apple.com/documentation/appkit/nswindow/1419132-isvisible)Added [NSWindow.windowNumber](https://developer.apple.com/documentation/appkit/nswindow/1419068-windownumber)Added [NSWindow.windowRef](https://developer.apple.com/documentation/appkit/nswindow/1419485-windowref)Added [+[NSWindow windowWithContentViewController:]](https://developer.apple.com/documentation/appkit/nswindow/1419551-init)Added [NSWindow.worksWhenModal](https://developer.apple.com/documentation/appkit/nswindow/1419220-workswhenmodal)Added [NSWindow.zoomed](https://developer.apple.com/documentation/appkit/nswindow/1419398-zoomed)Added [#def NSEventDurationForever](https://developer.apple.com/documentation/appkit/nsevent/1419434-foreverduration)Added [NSFullSizeContentViewWindowMask](https://developer.apple.com/documentation/appkit/nsfullsizecontentviewwindowmask)Added NSWindow(NSDeprecated)Added [NSWindowTitleHidden](https://developer.apple.com/documentation/appkit/nswindowtitlevisibility/nswindowtitlehidden)Added [NSWindowTitleVisibility](https://developer.apple.com/documentation/appkit/nswindowtitlevisibility)Added [NSWindowTitleVisible](https://developer.apple.com/documentation/appkit/nswindow/titlevisibility/visible)Modified [NSWindow](https://developer.apple.com/documentation/appkit/nswindow)

|  | Protocols |
| --- | --- |
| From | NSAnimatablePropertyContainer, NSAppearanceCustomization, NSUserInterfaceItemIdentification, NSUserInterfaceValidations |
| To | NSAccessibility, NSAccessibilityElement, NSAnimatablePropertyContainer, NSAppearanceCustomization, NSUserInterfaceItemIdentification, NSUserInterfaceValidations |

Modified [-[NSWindow canStoreColor]](https://developer.apple.com/documentation/appkit/nswindow/1419248-canstorecolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSWindow convertBaseToScreen:]](https://developer.apple.com/documentation/appkit/nswindow/1419550-convertbasetoscreen)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified [-[NSWindow convertScreenToBase:]](https://developer.apple.com/documentation/appkit/nswindow/1419414-convertscreentobase)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified [-[NSWindow gState]](https://developer.apple.com/documentation/appkit/nswindow/1419412-gstate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSWindow initWithContentRect:styleMask:backing:defer:]](https://developer.apple.com/documentation/appkit/nswindow/1419477-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentRect:(NSRect)contentRect styleMask:(NSUInteger)aStyle backing:(NSBackingStoreType)bufferingType defer:(BOOL)flag ``` |
| To | ``` - (instancetype)initWithContentRect:(NSRect)contentRect styleMask:(NSUInteger)aStyle backing:(NSBackingStoreType)bufferingType defer:(BOOL)flag ``` |

Modified [-[NSWindow initWithContentRect:styleMask:backing:defer:screen:]](https://developer.apple.com/documentation/appkit/nswindow/1419755-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentRect:(NSRect)contentRect styleMask:(NSUInteger)aStyle backing:(NSBackingStoreType)bufferingType defer:(BOOL)flag screen:(NSScreen *)screen ``` |
| To | ``` - (instancetype)initWithContentRect:(NSRect)contentRect styleMask:(NSUInteger)aStyle backing:(NSBackingStoreType)bufferingType defer:(BOOL)flag screen:(NSScreen *)screen ``` |

Modified [-[NSWindow useOptimizedDrawing:]](https://developer.apple.com/documentation/appkit/nswindow/1419306-useoptimizeddrawing)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSWindow userSpaceScaleFactor]](https://developer.apple.com/documentation/appkit/nswindow/1419616-userspacescalefactor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified [-[NSWindowDelegate customWindowsToEnterFullScreenForWindow:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419521-customwindowstoenterfullscreen)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate customWindowsToEnterFullScreenForWindow:onScreen:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419557-customwindowstoenterfullscreen)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate customWindowsToExitFullScreenForWindow:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419070-customwindowstoexitfullscreenfor)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate window:didDecodeRestorableState:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419475-window)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate window:shouldDragDocumentWithEvent:from:withPasteboard:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419452-window)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate window:shouldPopUpDocumentPathMenu:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419465-window)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate window:startCustomAnimationToEnterFullScreenOnScreen:withDuration:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419709-window)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate window:startCustomAnimationToEnterFullScreenWithDuration:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419406-window)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate window:startCustomAnimationToExitFullScreenWithDuration:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419705-window)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate window:willEncodeRestorableState:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419619-window)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate window:willPositionSheet:usingRect:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419611-window)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate window:willResizeForVersionBrowserWithMaxPreferredSize:maxAllowedSize:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419360-window)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate window:willUseFullScreenContentSize:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419282-window)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate window:willUseFullScreenPresentationOptions:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419144-window)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidBecomeKey:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419737-windowdidbecomekey)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidBecomeMain:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419190-windowdidbecomemain)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidChangeBackingProperties:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419517-windowdidchangebackingproperties)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidChangeOcclusionState:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419424-windowdidchangeocclusionstate)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidChangeScreen:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419267-windowdidchangescreen)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidChangeScreenProfile:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419581-windowdidchangescreenprofile)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidDeminiaturize:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419296-windowdiddeminiaturize)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidEndLiveResize:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419150-windowdidendliveresize)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidEndSheet:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419773-windowdidendsheet)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidEnterFullScreen:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419116-windowdidenterfullscreen)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidEnterVersionBrowser:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419064-windowdidenterversionbrowser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidExitFullScreen:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419146-windowdidexitfullscreen)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidExitVersionBrowser:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419501-windowdidexitversionbrowser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidExpose:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419258-windowdidexpose)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidFailToEnterFullScreen:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419591-windowdidfailtoenterfullscreen)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidFailToExitFullScreen:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419573-windowdidfailtoexitfullscreen)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidMiniaturize:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419621-windowdidminiaturize)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidMove:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419674-windowdidmove)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidResignKey:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419711-windowdidresignkey)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidResignMain:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419584-windowdidresignmain)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidResize:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419567-windowdidresize)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowDidUpdate:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419493-windowdidupdate)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowShouldClose:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419380-windowshouldclose)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowShouldZoom:toFrame:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419533-windowshouldzoom)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowWillBeginSheet:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419408-windowwillbeginsheet)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowWillClose:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419605-windowwillclose)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowWillEnterFullScreen:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419563-windowwillenterfullscreen)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowWillEnterVersionBrowser:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419463-windowwillenterversionbrowser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowWillExitFullScreen:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419332-windowwillexitfullscreen)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowWillExitVersionBrowser:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419252-windowwillexitversionbrowser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowWillMiniaturize:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419461-windowwillminiaturize)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowWillMove:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419336-windowwillmove)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowWillResize:toSize:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419292-windowwillresize)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowWillReturnFieldEditor:toObject:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419416-windowwillreturnfieldeditor)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowWillReturnUndoManager:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419745-windowwillreturnundomanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowWillStartLiveResize:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419555-windowwillstartliveresize)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWindowDelegate windowWillUseStandardFrame:defaultFrame:]](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419684-windowwillusestandardframe)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [NSUnscaledWindowMask](https://developer.apple.com/documentation/appkit/nsunscaledwindowmask)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.4 | -- |
| To | OS X 10.0 | OS X 10.9 |

NSWindowController.hRemoved [-[NSWindowController document]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1534220-document)Removed [-[NSWindowController isWindowLoaded]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1527496-windowloaded)Removed [-[NSWindowController owner]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1532707-owner)Removed [-[NSWindowController setDocument:]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1534220-document)Removed [-[NSWindowController setShouldCascadeWindows:]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1528177-shouldcascadewindows)Removed [-[NSWindowController setShouldCloseDocument:]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1526933-shouldclosedocument)Removed [-[NSWindowController setWindow:]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1535593-window)Removed [-[NSWindowController setWindowFrameAutosaveName:]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1528616-windowframeautosavename)Removed [-[NSWindowController shouldCascadeWindows]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1528177-shouldcascadewindows)Removed [-[NSWindowController shouldCloseDocument]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1526933-shouldclosedocument)Removed [-[NSWindowController window]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1535593-window)Removed [-[NSWindowController windowFrameAutosaveName]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1528616-windowframeautosavename)Removed [-[NSWindowController windowNibName]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1527084-windownibname)Removed [-[NSWindowController windowNibPath]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1524719-windownibpath)Added [NSWindowController.contentViewController](https://developer.apple.com/documentation/appkit/nswindowcontroller/1532552-contentviewcontroller)Added [-[NSWindowController dismissController:]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1531963-dismisscontroller)Added [NSWindowController.document](https://developer.apple.com/documentation/appkit/nswindowcontroller/1534220-document)Added [-[NSWindowController initWithCoder:]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1529004-initwithcoder)Added [NSWindowController.owner](https://developer.apple.com/documentation/appkit/nswindowcontroller/1532707-owner)Added [NSWindowController.shouldCascadeWindows](https://developer.apple.com/documentation/appkit/nswindowcontroller/1528177-shouldcascadewindows)Added [NSWindowController.shouldCloseDocument](https://developer.apple.com/documentation/appkit/nswindowcontroller/1526933-shouldclosedocument)Added [NSWindowController.storyboard](https://developer.apple.com/documentation/appkit/nswindowcontroller/1527268-storyboard)Added [NSWindowController.window](https://developer.apple.com/documentation/appkit/nswindowcontroller/1535593-window)Added [NSWindowController.windowFrameAutosaveName](https://developer.apple.com/documentation/appkit/nswindowcontroller/1528616-windowframeautosavename)Added [NSWindowController.windowLoaded](https://developer.apple.com/documentation/appkit/nswindowcontroller/1527496-windowloaded)Added [NSWindowController.windowNibName](https://developer.apple.com/documentation/appkit/nswindowcontroller/1527084-windownibname)Added [NSWindowController.windowNibPath](https://developer.apple.com/documentation/appkit/nswindowcontroller/1524719-windownibpath)Added NSWindowController(NSWindowControllerDismissing)Added NSWindowController(NSWindowControllerStoryboardingMethods)Modified [NSWindowController](https://developer.apple.com/documentation/appkit/nswindowcontroller)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSCoding, NSSeguePerforming |

Modified [-[NSWindowController initWithWindow:]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1533442-initwithwindow)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithWindow:(NSWindow *)window ``` | -- |
| To | ``` - (instancetype)initWithWindow:(NSWindow *)window ``` | yes |

Modified [-[NSWindowController initWithWindowNibName:]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1527041-initwithwindownibname)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithWindowNibName:(NSString *)windowNibName ``` |
| To | ``` - (instancetype)initWithWindowNibName:(NSString *)windowNibName ``` |

Modified [-[NSWindowController initWithWindowNibName:owner:]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1535239-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithWindowNibName:(NSString *)windowNibName owner:(id)owner ``` |
| To | ``` - (instancetype)initWithWindowNibName:(NSString *)windowNibName owner:(id)owner ``` |

Modified [-[NSWindowController initWithWindowNibPath:owner:]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1532584-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithWindowNibPath:(NSString *)windowNibPath owner:(id)owner ``` |
| To | ``` - (instancetype)initWithWindowNibPath:(NSString *)windowNibPath owner:(id)owner ``` |

Modified [-[NSWindowController showWindow:]](https://developer.apple.com/documentation/appkit/nswindowcontroller/1534037-showwindow)

|  | Declaration |
| --- | --- |
| From | ``` - (void)showWindow:(id)sender ``` |
| To | ``` - (IBAction)showWindow:(id)sender ``` |

NSWindowRestoration.hRemoved [-[NSWindow isRestorable]](https://developer.apple.com/documentation/appkit/nswindow/1526255-isrestorable)Removed [-[NSWindow restorationClass]](https://developer.apple.com/documentation/appkit/nswindow/1526241-restorationclass)Removed [-[NSWindow setRestorable:]](https://developer.apple.com/documentation/appkit/nswindow/1526255-restorable)Removed [-[NSWindow setRestorationClass:]](https://developer.apple.com/documentation/appkit/nswindow/1526241-restorationclass)Added [NSWindow.restorable](https://developer.apple.com/documentation/appkit/nswindow/1526255-isrestorable)Added [NSWindow.restorationClass](https://developer.apple.com/documentation/appkit/nswindow/1526241-restorationclass)NSWindowScripting.hRemoved [-[NSWindow hasCloseBox]](https://developer.apple.com/documentation/appkit/nswindow/1449574-hasclosebox)Removed [-[NSWindow hasTitleBar]](https://developer.apple.com/documentation/appkit/nswindow/1449568-hastitlebar)Removed [-[NSWindow isFloatingPanel]](https://developer.apple.com/documentation/appkit/windows_panels_and_screens/nswindowscripting/1806891-isfloatingpanel)Removed [-[NSWindow isMiniaturizable]](https://developer.apple.com/documentation/appkit/windows_panels_and_screens/nswindowscripting/1806893-isminiaturizable)Removed [-[NSWindow isModalPanel]](https://developer.apple.com/documentation/appkit/windows_panels_and_screens/nswindowscripting/1806894-ismodalpanel)Removed [-[NSWindow isResizable]](https://developer.apple.com/documentation/appkit/windows_panels_and_screens/nswindowscripting/1806897-isresizable)Removed [-[NSWindow isZoomable]](https://developer.apple.com/documentation/appkit/windows_panels_and_screens/nswindowscripting/1806899-iszoomable)Removed [-[NSWindow orderedIndex]](https://developer.apple.com/documentation/appkit/nswindow/1449577-orderedindex)Removed [-[NSWindow setOrderedIndex:]](https://developer.apple.com/documentation/appkit/nswindow/1449577-orderedindex)Added [NSWindow.floatingPanel](https://developer.apple.com/documentation/appkit/nswindow/1449579-floatingpanel)Added [NSWindow.hasCloseBox](https://developer.apple.com/documentation/appkit/nswindow/1449574-hasclosebox)Added [NSWindow.hasTitleBar](https://developer.apple.com/documentation/appkit/nswindow/1449568-hastitlebar)Added [NSWindow.miniaturizable](https://developer.apple.com/documentation/appkit/nswindow/1449583-isminiaturizable)Added [NSWindow.modalPanel](https://developer.apple.com/documentation/appkit/nswindow/1449576-modalpanel)Added [NSWindow.orderedIndex](https://developer.apple.com/documentation/appkit/nswindow/1449577-orderedindex)Added [NSWindow.resizable](https://developer.apple.com/documentation/appkit/nswindow/1449572-isresizable)Added [NSWindow.zoomable](https://developer.apple.com/documentation/appkit/nswindow/1449587-zoomable)NSWorkspace.hRemoved [-[NSWorkspace fileLabelColors]](https://developer.apple.com/documentation/appkit/nsworkspace/1527553-filelabelcolors)Removed [-[NSWorkspace fileLabels]](https://developer.apple.com/documentation/appkit/nsworkspace/1533953-filelabels)Removed [-[NSWorkspace frontmostApplication]](https://developer.apple.com/documentation/appkit/nsworkspace/1532097-frontmostapplication)Removed [-[NSWorkspace menuBarOwningApplication]](https://developer.apple.com/documentation/appkit/nsworkspace/1525848-menubarowningapplication)Removed [-[NSWorkspace notificationCenter]](https://developer.apple.com/documentation/appkit/nsworkspace/1525071-notificationcenter)Added [NSWorkspace.fileLabelColors](https://developer.apple.com/documentation/appkit/nsworkspace/1527553-filelabelcolors)Added [NSWorkspace.fileLabels](https://developer.apple.com/documentation/appkit/nsworkspace/1533953-filelabels)Added [NSWorkspace.frontmostApplication](https://developer.apple.com/documentation/appkit/nsworkspace/1532097-frontmostapplication)Added [NSWorkspace.menuBarOwningApplication](https://developer.apple.com/documentation/appkit/nsworkspace/1525848-menubarowningapplication)Added [NSWorkspace.notificationCenter](https://developer.apple.com/documentation/appkit/nsworkspace/1525071-notificationcenter)Added [-[NSWorkspace openURL:options:configuration:error:]](https://developer.apple.com/documentation/appkit/nsworkspace/1532940-openurl)Added [-[NSWorkspace openURLs:withApplicationAtURL:options:configuration:error:]](https://developer.apple.com/documentation/appkit/nsworkspace/1528548-openurls)

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
