---
title: WebObjects Java Client Programming Guide
apple_id: TP30001017
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-08-11'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/DesktopApplications/Appendix_A/XMLDescriptions.html
archived_at: '2026-07-18T02:17:02.801893Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects Java Client Programming Guide](Introduction%20to%20WebObjects%20Java%20Client%20Programming%20Guide.md)


[Next](Glossary.md)[Previous](Document%20Revision%20History.md)

# Controllers and Actions Reference

This appendix provides an overview of the classes used in Java Client applications, including the XML descriptions, tags, and attributes they use. Refer to [XML Value Types](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzsgmwugqkdjfbuqrse) for complete information on the proprietary value types such as `editability` and `alignment`.

The XML attributes for Java Client classes include standard Java value types and these other value types:

- __position__
- `Center`
- `Top`
- `Bottom`
- `Left`
- `Right`
- `TopLeft`
- `TopRight`
- `BottomLeft`
- `BottomRight`

- __border__
- `None`
- `Etched`
- `RaisedBezel`
- `LoweredBezel`
- `LineBorder`

- __editability__
- `Never`
- `Always`
- `IfSuperController`

- __alignment__
- `Center`
- `Left`
- `Right`

- __insets__
- The format for this value type is " _top_, _left_, _bottom_, _right_", with each coordinate specified by an integer.

- __resizing__
- `NoResizing`
- `AspectResizing`
- `FreeResizing`
- `IntegralResizing`
- `PerformanceResizing`
- `HorizontalResizing`
- `VerticalResizing`

- __scaling__
- `ScaleNone`
- `ScaleProportionally`
- `ScaleToFit`
- `ScaleProportionallyIfTooLarge`

- __scaling hint__
- `ScaleDefault`
- `ScaleFast`
- `ScaleSmooth`

- __color__
- Specify by three integers each in the range 0 to 255: “_integerRed_, _integerGreen_, _integerBlue_”, or specify by hex: “#FFFFFF”.

- __font__
- `Size`
- `Style`
- `Font`
- The format for this value type is “_size_, _style_:_fontName_”. Specify `Size` as “+ _integer_” or “-_integer_”. Specify `Style` as `Plain`, `Bold`, `Italic`, or `BoldItalic`.
- Example: `<CONTROLLER className="com.myapp.TextFieldController" font="+2, Bold: Arial"/>`

- __provider method__
- `ClassName`
- `MethodName`
- The format for this value type is “_className_: _methodName_”.

Direct to Java Client user interfaces are defined in XML descriptions. The XML descriptions identify controllers, which in turn represent Enterprise Objects objects and Swing user interface objects. This section lists all the controllers in the Java Client frameworks that have at least one XML tag or one XML attribute. Controllers inherit XML attributes, but inherited XML attributes may not always be appropriate for the inheriting controller.

The following list is alphabetical by controller name, without regard to a controller’s package.

##### com.webobjects.eoapplication.EOActionButtonsController

**Superclass:**
: `com.webobjects.eoapplication.EOActionWidgetController`

**Description:**
: Handles toolbars with multiple action buttons.

**XML Tag:**
: `ACTIONBUTTONSCONTROLLER`

**XML Attributes:**
: `usesLargeButtonRepresentation` (`boolean`)

##### com.webobjects.eogeneration.EOActionController

**Superclass:**
: `com.webobjects.eogeneration.EOTitlesController`

**Description:**
: Handles invoking actions and action keys.

**XML Tag:**
: `ACTIONCONTROLLER`

**XML Attributes:**
: `actionKey` (`String` representing the key path for the action aspect of the association)
: `buttonPosition` (position)
: `usesAction` (`boolean`)
: `usesButton` (`boolean`)

##### com.webobjects.eoapplication.EOActionMenuController

**Superclass:**
: `com.webobjects.eoapplication.EOActionWidgetController`

**Description:**
: Handles pop-up menus with multiple action items.

**XML Tag:**
: `ACTIONMENUCONTROLLER`

##### com.webobjects.eoapplication.EOActionTrigger

**Superclass:**
: `com.webobjects.eoapplication.EOComponentController`

**Description:**
: A lightweight control for actions.

**XML Tag:**
: `ACTIONTRIGGER`

**XML Attributes:**
: `usesLargeButtonRepresentation` (`boolean`)
:

##### com.webobjects.eoapplication.EOActionWidgetController

**Superclass:**
: `com.webobjects.eoapplication.EOComponentController`

**Description:**
: Handles toolbars and other action controls.

**XML Tag:**
: None (abstract class)

**XML Attributes:**
: `widgetPosition` (position)

##### com.webobjects.eoapplication.EOArchiveController

**Superclass:**
: `com.webobjects.eoapplication.EOComponentController`

**Description:**
: Used for loading interface files.

**XML Tag:**
: None (abstract class)

**XML Attributes:**
: `archive` (`String` representing the name of the interface file to be used by a controller rather than the dynamic user-interface generation)

##### com.webobjects.eogeneration.EOAssociationController

**Superclass:**
: `com.webobjects.eogeneration.EOWidgetController`

**Description:**
: Handles associations for widgets, including the editable state and enabled key.

**XML Tag:**
: None (abstract class)

**XML Attributes:**
: `displayGroupProviderMethodName` (provider method name)
: `editability` (editability)
: `enabledDisplayGroupProviderMethodName` (provider method name)
: `enabledKey` (`String` representing the key path for the enabled aspect of the association)
: `prefersContinuousChangeNotification` (`boolean`)
: `suppressesAssociation` (`boolean`)

##### com.webobjects.eoapplication.EOBoxController

**Superclass:**
: `com.webobjects.eoapplication.EOComponentController`

**Description:**
: Displays bordered and titled boxes.

**XML Tag:**
: `BOXCONTROLLER`

**XML Attributes:**
: `borderType` (border)
: `color` (color)
: `font` (font)
: `highlight` (`boolean`)
: `titlePosition` (position)
: `usesTitledBorder` (`boolean`)

##### com.webobjects.eogeneration.EOCheckBoxController

**Superclass:**
: `com.webobjects.eogeneration.EOValueController`

**Description:**
: Handles checkboxes.

**XML Tag:**
: `CHECKBOXCONTROLLER`

**XML Attributes:**
: `displaysLabelInWidget` (`boolean`)

##### com.webobjects.eogeneration.EOComboBoxController

**Superclass:**
: `com.webobjects.eogeneration.EOTitlesController`

**Description:**
: Handles combo boxes with fixed values.

**XML Tag:**
: `COMBOBOXCONTROLLER`

**XML Attributes:**
: `isQueryWidget` (`boolean`)
: `valueKey` (`String` representing the key path for the value aspect of the association)

##### com.webobjects.eoapplication.EOComponentController

**Superclass:**
: `com.webobjects.eoapplication.EOController`

**Description:**
: Handles user interface issues such as visibility state, labels, icons, size information, subcontroller layout; default component controller is an empty box.

**XML Tag:**
: `COMPONENTCONTROLLER`

**XML Attributes:**
: `alignsComponents` (`boolean`)
: `horizontallyResizable` (`boolean`)
: `iconName` (`String`)
: `iconURL` (`String`)
: `insets` (`insets`)
: `label` (`String`)
: `minimumHeight` (`int`)
: `minimumWidth` (`int`)
: `prefersIconOnly` (`boolean`)
: `toolTip` (`String`)
: `usesHorizontalLayout` (`boolean`)
: `verticallyResizable` (`boolean`)

##### com.webobjects.eoapplication.EOController

**Superclass:**
: `java.lang.Object`

**Description:**
: An abstract definition of controllers; handles supercontrollers, subcontrollers, key-value coding for the controller hierarchy, messages in the controller hierarchy, establishing and breaking connections to other controllers.

**XML Tag:**
: None (abstract class)

**XML Attributes:**
: `actions` (array of EOAction objects)
: `className` (`String`)
: `disabledActionNames` (array of strings with names of actions to be disabled)
: `keyValuePairs` (additional values that can be looked up with key-value coding)
: `transient` (`boolean`)
: `typeName` (`String`)

##### com.webobjects.eogeneration.EODefaultActionTrigger

**Superclass:**
: `com.webobjects.eogeneration.EOAssociationController`

**Description:**
: None (abstract class)

**XML Tag:**
: `invokesDefaultAction` (`boolean`)

##### com.webobjects.eogeneration.EODetailSelectionController

**Superclass:**
: `com.webobjects.eogeneration.EOEnumerationController`

**Description:**
: Handles detail selection tables.

**XML Tag:**
: `DETAILSELECTIONCONTROLLER`

**XML Attributes:**
: None

##### com.webobjects.eoapplication.EODialogController

**Superclass:**
: `com.webobjects.eoapplication.EOSimpleWindowController`

**Description:**
: Handles dialogs (such as error messages).

**XML Tag:**
: `DIALOGCONTROLLER`

##### com.webobjects.eogeneration.EODisplayStatisticsController

**Superclass:**
: `com.webobjects.eogeneration.EOStaticLabelController`

**Description:**
: Displays the number of selected objects and the number of displayed objects in list controllers.

**XML Tag:**
: `DISPLAYSTATISTICSCONTROLLER`

**XML Attributes:**
: `displayGroupProviderMethodName` (provider method)
: `displayPattern` (`String`)

##### com.webobjects.eoapplication.EODocumentController

**Superclass:**
: `com.webobjects.eoapplication.EOEntityController`

**Description:**
: Handles editable documents.

**XML Tag:**
: `DOCUMENTCONTROLLER`

**XML Attributes:**
: `editability` (editability)

##### com.webobjects.eogeneration.EOEditingController

**Superclass:**
: `com.webobjects.eoapplication.EODocumentController`

**Description:**
: Handles master-detail associations.

**XML Tag:**
: None

**XML Attributes:**
: `path` (`String`, representing a relationship key path)
: `mandatoryRelationshipPaths` (array of `String` values, representing the relationships to be filled on insert)

##### com.webobjects.eoapplication.EOEntityController

**Superclass:**
: `com.webobjects.eoapplication.EOComponentController`

**Description:**
: Handles business data on the level of entities: entity names, editing context, display group, controller display group, loading archives (Interface Builder files).

**XML Tag:**
: `ENTITYCONTROLLER`

**XML Attributes:**
: `entity` (`String` representing the entity)
: `displayGroupProviderMethodName` (provider method)
: `editingContextProviderMethodName` (provider method)
: `fetchesOnConnectEnabled` (`boolean`)

##### com.webobjects.eogeneration.EOEnumerationController

**Superclass:**
: `com.webobjects.eogeneration.EOTitlesController`

**Description:**
: Handles enumeration widgets.

**XML Tag:**
: None (abstract class)

**XML Attributes:**
: `path` (`String` representing the detail relationship path to title objects)

##### com.webobjects.eogeneration.EOFormatValueController

**Superclass:**
: `com.webobjects.eogeneration.EOValueController`

**Description:**
: Handles the formatting and value aspect of widgets with associations.

**XML Tag:**
: None (abstract class)

**XML Attributes:**
: `formatAllowed` (`boolean`)
: `formatClass` (`String` of the class name of the formatter object)
: `formatPattern` (`String` representing the pattern string of the formatter object)

##### com.webobjects.eogeneration.EOFormController

**Superclass:**
: `com.webobjects.eogeneration.EOEditingController`

**Description:**
: Handles editable forms.

**XML Tag:**
: `FORMCONTROLLER`

##### com.webobjects.eoapplication.EOFrameController

**Superclass:**
: `com.webobjects.eoapplication.EOSimpleWindowController`

**Description:**
: Handles frames.

**XML Tag:**
: `FRAMECONTROLLER`

##### com.webobjects.eogeneration.EOImageViewController

**Superclass:**
: `com.webobjects.eogeneration. EOValueAndURLController`

**Description:**
: Handles image views.

**XML Tag:**
: `IMAGEVIEWCONTROLLER`

**XML Attributes:**
: `imageScaling` (scaling)
: `scalingHints` (scaling hint)

##### com.webobjects.eoapplication.EOInspectorController

**Superclass:**
: `com.webobjects.eoapplication.EOWindowController`

**Description:**
: Handles inspector windows.

**XML Tag:**
: `INSPECTORCONTROLLER`

**XML Attributes:**
: `sharedIdentifier` (`String`)

##### com.webobjects.eoapplication.EOInterfaceController

**Superclass:**
: `com.webobjects.eoapplication.EODocumentController`

**Description:**
: Handles documents that always use an interface file.

**XML Tag:**
: `INTERFACECONTROLLER`

##### com.webobjects.eogeneration.EOListController

**Superclass:**
: `com.webobjects.eogeneration.EOEditingController`

**Description:**
: Handles editable lists.

**XML Tag:**
: `LISTCONTROLLER`

##### com.webobjects.eoapplication.EOMenuSwitchController

**Superclass:**
: `com.webobjects.eoapplication.EOSwitchController`

**Description:**
: Handles switch panes that have a pop-up menu.

**XML Tag:**
: `MENUSWITCHCONTROLLER`

##### com.webobjects.eoapplication.EOModalDialogController

**Superclass:**
: `com.webobjects.eoapplication.EODialogController`

**Description:**
: Handles modal dialog controllers.

**XML Tag:**
: `MODALDIALOGCONTROLLER`

##### com.webobjects.eogeneration.EOMultipleValuesEnumerationController

**Superclass:**
: `com.webobjects.eogeneration.EOEnumerationController`

**Description:**
: Handles to-many relationships to enumeration entities.

**XML Tag:**
: `MULTIPLEVALUESENUMERATIONCONTROLLER`

**XML Attributes:**
: `allowsDuplicates` (`boolean`)
: `allowsRemoveAll` (`boolean`)
: `detailKeys` (an array of `String` values, representing the key paths to be displayed for selected objects)
: `detailRelationshipPath` (`String`)
: `indexKey` (`String`, representing the key to sort on)
: `usesTableLabels` (`boolean`)

##### com.webobjects.eogeneration.EOOneValueEnumerationController

**Superclass:**
: `com.webobjects.eogeneration.EOEnumerationController`

**Description:**
: Handles to-one relationships to enumeration entities.

**XML Tag:**
: `ONEVALUEENUMERATIONCONTROLLER`

**XML Attributes:**
: `isQueryWidget` (`boolean`)

##### com.webobjects.eoapplication.EOProgrammaticSwitchController

**Superclass:**
: `com.webobjects.eoapplication.EOSwitchController`

**Description:**
: Handles switch views that can only be changed programmatically.

**XML Tag:**
: `PROGRAMMATICSWITCHCONTROLLER`

##### com.webobjects.eogeneration.EOQueryController

**Superclass:**
: `com.webobjects.eoapplication.EOEntityController`

**Description:**
: Handles query interfaces.

**XML Tag:**
: `QUERYCONTROLLER`

**XML Attributes:**
: `editability` (editability)
: `runsConfirmDialogForEmptyQualifiers` (`boolean`)

##### com.webobjects.eogeneration.EOQuickTimeViewController

**Superclass:**
: `com.webobjects.eogeneration. EOAssociationController`

**Description:**
: Handles QuickTime views.

**XML Tag:**
: `QUICKTIMEVIEWCONTROLLER`

**XML Attributes:**
: `quickTimeCanvasResizing` (resizing)
: `URLKey` (`String` representing the key path for the URL aspect of the association)

##### com.webobjects.eogeneration.EORangeTextFieldController

**Superclass:**
: `com.webobjects.eogeneration.EORangeValueController`

**Description:**
: Handles range text fields with optional formatters.

**XML Tag:**
: `RANGETEXTFIELDCONTROLLER`

**XML Attributes:**
: `formatAllowed` (`boolean`)
: `formatClass` (`String` of the class name of the format object)
: `formatPattern` (`String` representing the pattern of the format object)
: `isQueryWidget` (`boolean`)

##### com.webobjects.eogeneration.EORangeValueController

**Superclass:**
: `com.webobjects.eogeneration.EORangeWidgetController`

**Description:**
: Handles the value aspect, enabled key aspect, and editable state of range widgets.

**XML Tag:**
: None (abstract class)

**XML Attributes:**
: `displayGroupProviderMethodName` (method name)
: `editability` (editability)
: `enabledDisplayGroupProviderMethodName` (method name)
: `enabledKey` (`String` representing the key path for the enabled aspect of the association)
: `maximumValueKey` (`String` representing the key path for the value aspect of the maximum association)
: `minimumValueKey`(`String` representing the key path for the value aspect of the minimum association)
: `valueKey` (`String` representing the key path for the value aspect of both the minimum and maximum associations)
: `suppressesAssociation` (`boolean`)

##### com.webobjects.eogeneration.EORangeWidgetController

**Superclass:**
: `com.webobjects.eogeneration.EOWidgetController`

**Description:**
: Handles range widgets—two widgets for the minimum and maximum value of the same value.

**XML Tag:**
: None (abstract class)

##### com.webobjects.eoapplication.EOSimpleWindowController

**Superclass:**
: `com.webobjects.eoapplication.EOWindowController`

**Description:**
: Handles standalone windows.

**XML Tag:**
: None (abstract class)

**XML Attributes:**
: `disposeIfDeactivated` (`boolean`)

##### com.webobjects.eoapplication.EOSplitController

**Superclass:**
: `com.webobjects.eoapplication.EOComponentController`

**Description:**
: Handles split views (split & snap) which display exactly two subcontroller views.

**XML Tag:**
: `SPLITCONTROLLER`

**XML Attributes:**
: `allowsOneTouchExpandable` (`boolean`)
: `allowsSnapToZero` (`boolean`)
: `resizeWeight` (`double` from 0.0 to 1.0)
: `usesContinuousLayout` (`boolean`)

##### com.webobjects.eogeneration.EOStaticIconController

**Superclass:**
: `com.webobjects.eoapplication.EOComponentController`

**Description:**
: Handles the display of static icons.

**XML Tag:**
: `STATICICONCONTROLLER`

##### com.webobjects.eogeneration.EOStaticLabelController

**Superclass:**
: `com.webobjects.eoapplication.EOComponentController`

**Description:**
: Handles the display of static messages.

**XML Tag:**
: `STATICLABELCONTROLLER`

**XML Attributes:**
: `alignment` (alignment)
: `color` (color)
: `font` (font)

##### com.webobjects.eogeneration.EOStaticTextFieldController

**Superclass:**
: `com.webobjects.eogeneration.EOTextFieldController`

**Description:**
: Handles uneditable table columns.

**XML Tag:**
: `STATICTEXTFIELDCONTROLLER`

**XML Attributes:**
: `color` (color)
: `font` (font)

##### com.webobjects.eoapplication.EOSwitchController

**Superclass:**
: `com.webobjects.eoapplication.EOComponentController`

**Description:**
: Handles switch views, which only display one view out of many at one time.

**XML Tag:**
: None (abstract class)

##### com.webobjects.eogeneration.EOTableColumnController

**Superclass:**
: `com.webobjects.eogeneration. EOFormatValueController`

**Description:**
: Handles table columns.

**XML Tag:**
: `TABLECOLUMNCONTROLLER`

##### com.webobjects.eogeneration.EOTableController

**Superclass:**
: `com.webobjects.eogeneration.EODefaultActionTrigger`

**Description:**
: Handles table views.

**XML Tag:**
: `TABLECONTROLLER`

**XML Attributes:**
: `allowsMultipleSelection` (`boolean`)
: `sortsByColumnOrder` (`boolean`)

##### com.webobjects.eoapplication.EOTabSwitchController

**Superclass:**
: `com.webobjects.eoapplication.EOSwitchController`

**Description:**
: Handles tabbed panes.

**XML Tag:**
: `TABSWITCHCONTROLLER`

##### com.webobjects.eogeneration.EOTextAreaController

**Superclass:**
: `com.webobjects.eogeneration.EOValueAndURLController`

**Description:**
: Handles scrollable text areas.

**XML Tag:**
: `TEXTAREACONTROLLER`

##### com.webobjects.eogeneration.EOTextFieldController

**Superclass:**
: `com.webobjects.eogeneration.EOFormatValueController`

**Description:**
: Handles editable text fields.

**XML Tag:**
: `TEXTFIELDCONTROLLER`

**XML Attributes:**
: `isQueryWidget` (`boolean`)
: `usesPasswordField` (`boolean`)

##### com.webobjects.eogeneration.EOTitlesController

**Superclass:**
: `com.webobjects.eogeneration.EOAssociationController`

**Description:**
: Handles the attributes of enumeration widgets such as titles, title keys, title display groups, and editable state.

**XML Tag:**
: None (abstract class)

**XML Attributes:**
: `availableTitlesKey` (`String`, representing a key path specifying an array of available title objects)
: `resetTitlesObjectsOnEveryConnect` (`boolean`)
: `searchesTitlesObjectsInEditingContext` (`boolean`)
: `titleKeys` (array of `String` values, representing the key paths to be displayed for title objects)
: `titlesDisplayGroupProviderMethodName` (method name)
: `titlesEntity` (`String`, representing the name of the titles entity; an optional attribute for some subclasses that can derive a name)

##### com.webobjects.eogeneration.EOTreeController

**Superclass:**
: `com.webobjects.eogeneration.EODefaultActionTrigger`

**Description:**
: Handles tree views.

**XML Tag:**
: `TREECONTROLLER`

**XML Attributes:**
: `allowsDiscontiguousSelection` (`boolean`)
: `allowsMultipleSelection` (`boolean`)
: `childrenKey` (`String`, representing a key path for the `children` aspect of the association)
: `expandedIconKey` (`String`, representing a key path for the `expandedIcon` aspect of the association)
: `iconKey` (`String`, representing a key path for the `icon` aspect of the association)
: `isLeafKey` (`String`, representing a key path for the `isLeaf` aspect of the association)
: `isRootVisible` (`boolean`)
: `parentKey` (`String`, representing the inverse key path for the `children` key; not used as an aspect)
: `rootKey` (`String`, representing the key path for the root aspect of the association)
: `valueKey` (`String`, representing the key path for the `value` aspect of the association)

##### com.webobjects.eogeneration.EOValueAndURLController

**Superclass:**
: `com.webobjects.eogeneration.EOValueController`

**Description:**
: Handles the value or URL aspects of widgets with associations.

**XML Tag:**
: None (abstract class)

**XML Attributes:**
: `URLKey` (`String` representing the key path for the URL aspect of the association)

##### com.webobjects.eogeneration.EOValueController

**Superclass:**
: `com.webobjects.eogeneration. EOAssociationController`

**Description:**
: Handles the value aspect of widgets with associations.

**XML Tag:**
: None (abstract class)

**XML Attributes:**
: `valueKey` (`String` representing key path for value aspect of association)

##### com.webobjects.eogeneration.EOWidgetController

**Superclass:**
: `com.webobjects.eoapplication.EOComponentController`

**Description:**
: Handles individual widgets, including their label and alignment.

**XML Tag:**
: None (abstract class)

**XML Attributes:**
: `alignment` (alignment)
: `highlight` (`boolean`)
: `labelAlignment` (alignment)
: `labelComponentPosition` (position)
: `labelComponentWidth` (integer)
: `minimumWidgetHeight` (integer, which specifies the minimum height just for the widget, not the complete component, which includes the label)
: `minimumWidgetWidth` (integer, which specifies the minimum width just for the widget, not the complete component, which includes the label)
: `usesLabelComponent` (`boolean`)

##### com.webobjects.eoapplication.EOWindowController

**Superclass:**
: `com.webobjects.eoapplication.EOComponentController`

**Description:**
: Handles windows and user defaults for window size and position.

**XML Tag:**
: None (abstract class)

**XML Attributes:**
: `windowPosition` (position)
: `usesAction` (`boolean`)
: `usesButton` (`boolean`)
: `usesUserDefaultsWindowLocation` (`boolean`)
: `usesUserDefaultsWindowSize` (`boolean`)

##### APPLICATIONACTION

**Description:**
: Actions sent to the application object.

**XML Attributes:**
: `actionName` (`String`)
: `actionPriority` (`int`)
: `categoryPriority` (`int`)
: `descriptionPath` (`String`)
: `iconName` (`String`)
: `iconURL` (`String`)
: `menuAccelerator` (`String`—example “shift P”)
: `shortDescription` (`String`)
: `smallIconName` (n)
: `smallIconURL` (`String`)
: `standardAction` (`String`; if specified, all other arguments are ignored)
: `toolTip` (`String`)

##### XMLClassValues

**Superclass:**
: `Superclass`

**Description:**
: Para

**XML Tag:**
: XMLTagInfo

##### XMLClassValues

**Superclass:**
: `Superclass`

**Description:**
: Para

**XML Tag:**
: XMLTagInfo

##### CONTROLLERHIERARCHYACTION

**Description:**
: Actions dispatched throughout the controller hierarchy.

**XML Attributes:**
: `actionName` (`String`)
: `actionPriority` (`int`)
: `categoryPriority` (`int`)
: `descriptionPath` (`String`)
: `iconName` (`String`)
: `iconURL` (`String`)
: `menuAccelerator` (`String`—example “shift P”)
: `shortDescription` (`String`)
: `smallIconName` (`String`)
: `smallIconURL` (`String`)
: `standardAction` (`String`; if specified, all other arguments are ignored)
: `toolTip` (`String`)

##### HELPWINDOWACTION

**Description:**
: Action in the Help menu to activate a window for a task.

**XML Attributes:**
: `shortDescription` (`String`)
: `menuAccelerator` (`String`—example “shift P”)
: `multipleWindowsAvailable` (`boolean`)
: `task` (`String`)
: `toolTip` (`String`)

##### INSERTACTION

**Description:**
: Action in the Document menu to insert an object of an entity.

**XML Attributes:**
: `entity` (`String`)
: `toolTip` (`String`)

##### OPENACTION

**Description:**
: Action in the Document menu to open an object of an entity.

**XML Attributes:**
: `entity` (`String`)
: `toolTip` (`String`)

##### QUERYACTION

**Description:**
: Action in the Document menu to start the search for an object of an entity.

**XML Attributes:**
: `entity` (`String`)
: `toolTip` (`String`)

##### SUPERCONTROLLERSACTION

**Description:**
: Action to activate a window for a task.

**XML Attributes:**
: `actionName` (`String`)
: `actionPriority` (`int`)
: `categoryPriority` (`int`)
: `descriptionPath` (`String`)
: `iconName` (`String`)
: `iconURL` (`String`)
: `menuAccelerator` (`String`—example “shift P”)
: `shortDescription` (`String`)
: `smallIconName` (`String`)
: `smallIconURL` (`String`)
: `standardAction` (`String`; if specified, all other arguments are ignored)
: `toolTip` (`String`)

##### STANDARDACTION

**XML Attributes:**
: `entity` (`String`)

##### TOOLWINDOWACTION

**Description:**
: Action in the Tools menu to activate a windoe for a task.

**XML Attributes:**
: `shortDescription` (`String`)
: `menuAccelerator` (`String`—example “shift P”)
: `multipleWindowsAvailable` (`boolean`)
: `task` (`String`)
: `toolTip` (`String`)

##### WINDOWACTION

**Description:**
: Action to activate a window for a task.

**XML Attributes:**
: `actionPriority` (`int`)
: `categoryPriority` (`int`)
: `categoryName` (`String`)
: `descriptionPath` (`String`)
: `iconName` (`String`)
: `iconURL` (`String`)
: `menuAccelerator` (`String`—example “shift P”)
: `multipleWindowsAvailable` (`boolean`)
: `shortDescription` (`String`)
: `smallIconName` (`String`)
: `smallIconURL` (`String`)
: `task` (`String`)
: `toolTip` (`String`)

##### WINDOWOBSERVERACTION

**Description:**
: Action sent to a window observer object (EOApplication.sharedApplication().windowObserver()).

**XML Attributes:**
: `actionName` (`String`)
: `actionPriority` (`int`)
: `categoryPriority` (`int`)
: `descriptionPath` (`String`)
: `iconName` (`String`)
: `iconURL` (`String`)
: `menuAccelerator` (`String`—example “shift P”)
: `multipleWindowsAvailable` (`boolean`)
: `shortDescription` (`String`)
: `smallIconName` (`String`)
: `smallIconURL` (`String`)
: `standardAction` (`String`; if specified, all other arguments are ignored)
: `toolTip` (`String`)

[Next](Glossary.md)[Previous](Document%20Revision%20History.md)

