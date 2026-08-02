---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/D2WContextKeys.html
archived_at: '2026-07-15T08:11:29.729190Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


# Direct to Web Context Keys

## Introduction

This document describes the keys that can be accessed with the D2WContext `valueForKey` and `takeValueForKey` methods. When you access a Direct to Web context key in a Direct to Web template's bindings (`.wod`) file, for example,

: `size = d2wContext.size;`

WebObjects indirectly invokes `valueForKey("size")` on the `d2wContext` Direct to Web context. When a bindings file has the entry:

: `value = d2wContext.entity.name;`

WebObjects indirectly invokes `valueForKeyPath("entity.name")` on the `d2wContext` Direct to Web context.

Each key has a type, to which you need to cast the result of `valueForKey`.
For example, to get the current entity in a Direct to Web context called `myContext` use:

: `currentEntity = (EOEntity)myContext.valueForKey("entity");`

Likewise, for `valueForKeyPath` you use:

: `currentEntityName = (String)myContext.valueForKeyPath("entity.name");`

In addition to specifying the type, the key descriptions below also indicate where the key appears in a rule. Keys labeled "Rule's key" are resolved using rules. There are two sets of rules: the rules managed by the Web Assistant (in the `user.d2wmodel` file in your project's Resources suitcase) and the default rules in the Direct to Web Framework (in `$(NEXT_ROOT)/Library/Frameworks/DirectToWeb.framework/Resources/d2w.d2wmodel`).

Keys labeled "Rule's condition" only appear in the conditions (left hand side) of rules. These keys and their values are stored in the Direct to Web context's state dictionary. Three of these keys can be modified using the `takeValueForKey` method: `task`, `entity`, and `propertyKey`. The other keys that appear in the rule's condition are computed when `propertyKey` is modified. Refer to the "Direct to Web Architecture" chapter of _Developing WebObjects Applications With Direct to Web_ for more information about how the Direct to Web context resolves its keys.

The following keys are defined by the Direct to Web context:

: [allowCollapsing](#apple-mfwgy33xinxwy3dbobzws3th)
: [alternateRowColor](#apple-mfwhizlsnzqxizksn53ug33mn5za)
: [attribute](#apple-mf2hi4tjmj2xizi)
: [backgroundColorForPage](#apple-mjqwg23hojxxk3teinxwy33sizxxeudbm5sq)
: [backgroundColorForTable](#apple-mjqwg23hojxxk3teinxwy33sizxxevdbmjwgk)
: [bannerFileName](#apple-mjqw43tfojdgs3dfjzqw2zi)
: [batchSize](#apple-mjqxiy3iknuxuzi)
: [bold](#apple-mjxwyza)
: [border](#apple-mjxxezdfoi)
: [color](#apple-mnxwy33s)
: [colorForLine](#apple-mnxwy33sizxxetdjnzsq)
: [columnCount](#apple-mnxwy5lnnzbw65looq)
: [componentAvailable](#apple-mnxw24dpnzsw45cbozqws3dbmjwgk)
: [componentBorder](#apple-mnxw24dpnzsw45ccn5zgizls)
: [componentName](#apple-mnxw24dpnzsw45comfwwk)
: [customComponentName](#apple-mn2xg5dpnvbw63lqn5xgk3tujzqw2zi)
: [disabled](#apple-mruxgylcnrswi)
: [displayNameForProperty](#apple-mruxg4dmmf4u4ylnmvdg64sqojxxazlsor4q)
: [displayPropertyKeys](#apple-mruxg4dmmf4va4tpobsxe5dzjnsxs4y)
: [editIcon](#apple-mvsgs5cjmnxw4)
: [entity](#apple-mvxhi2lupe)
: [formatter](#apple-mzxxe3lbor2gk4q)
: [framesActive](#apple-mzzgc3lfonawg5djozsq)
: [framework](#apple-mzzgc3lfo5xxe2y)
: [inspectComponentName](#apple-nfxhg4dfmn2eg33nobxw4zloorhgc3lf)
: [inspectIcon](#apple-nfxhg4dfmn2esy3pny)
: [isDeep](#apple-nfzuizlfoa)
: [italic](#apple-nf2gc3djmm)
: [justification](#apple-nj2xg5djmzuwgylunfxw4)
: [keyWhenRelationship](#apple-nnsxsv3imvxfezlmmf2gs33oonugs4a)
: [length](#apple-nrsw4z3una)
: [numCols](#apple-nz2w2q3pnrzq)
: [pageAvailable](#apple-obqwozkbozqws3dbmjwgk)
: [pageName](#apple-obqwozkomfwwk)
: [pageWrapperName](#apple-obqwozkxojqxa4dfojhgc3lf)
: [propertyIsKeyPath](#apple-obzg64dfoj2hssltjnsxsudborua)
: [propertyKey](#apple-obzg64dfoj2hss3fpe)
: [propertyType](#apple-obzg64dfoj2hsvdzobsq)
: [readOnly](#apple-ojswczcpnzwhs)
: [readOnlyEntityNames](#apple-ojswczcpnzwhsrlooruxi6komfwwk4y)
: [refreshRefetchedObjects](#apple-ojswm4tfonufezlgmv2gg2dfmrhwe2tfmn2hg)
: [relationship](#apple-ojswyylunfxw443infya)
: [rows](#apple-ojxxo4y)
: [selectButtonFileName](#apple-onswyzldorbhk5dun5xem2lmmvhgc3lf)
: [showBanner](#apple-onug652cmfxg4zls)
: [size](#apple-onuxuzi)
: [startupEntityName](#apple-on2gc4tuovyek3tunf2hsttbnvsq)
: [startupTask](#apple-on2gc4tuovyfiyltnm)
: [subtask](#apple-on2we5dbonvq)
: [tabContents](#apple-orqweq3pnz2gk3tuom)
: [tableWidth](#apple-orqwe3dfk5uwi5di)
: [tabName](#apple-orqwettbnvsq)
: [tabs](#apple-orqwe4y)
: [target](#apple-orqxez3foq)
: [task](#apple-orqxg2y)
: [threshold](#apple-oruhezltnbxwyza)
: [uiStyle](#apple-ovuvg5dznrsq)
: [usesDistinct](#apple-ovzwk42enfzxi2lomn2a)
: [visibleEntityNames](#apple-ozuxg2lcnrsuk3tunf2hsttbnvsxg)
: [webAssistantPageName](#apple-o5sweqltonuxg5dbnz2faylhmvhgc3lf)

---

__allowCollapsing__

: __Type:__ `Integer`

: __Appears:__ Rule's key (right-hand side)

: A flag that has a value of 1 if the current property level components can be collapsed and a value of 0 otherwise. This flag is primarily used by the display and edit components for relationships.

__alternateRowColor__

: __Type:__ `Integer`

: __Appears:__ Rule's key (right-hand side)

: A flag that has a value of 1 if the list page displays its entries with alternating row colors and a value of zero otherwise. This flag is used by some list page Direct to Web templates.

__attribute__

: __Type:__ `EOAttribute`

: __Appears:__ Rule's condition (left-hand side)

: The receiver's current attribute. Resolves to `null` if the current property is not an attribute. The value for this key is derived from `propertyKey`.

__backgroundColorForPage__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: The HTML background color for the page containing the receiver. Used by the D2WCompactInspectComponent.

__backgroundColorForTable__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: The background color for the table on page containing the receiver.

__bannerFileName__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: The name of the file depicting the banner displayed at the top of a Direct to Web page or a Direct to Web reusable component.

__batchSize__

: __Type:__ `Integer`

: __Appears:__ Rule's key (right-hand side)

: The number of objects per batch displayed on a list page. This key is used by the list and plain-list page Direct to Web templates.

__bold__

: __Type:__ `Integer`

: __Appears:__ Rule's key (right-hand side)

: A flag that has a value of 1 if the text is displayed in bold face and a value of 0 otherwise. This key is used by the styled display property-level components: D2WDisplayStyledDate, D2WDisplayedStyledNumber, D2WDisplayStyledString, and D2WKeyPathContainer.

__border__

: __Type:__ `Integer`

: __Appears:__ Rule's key (right-hand side)

: The width of the border around the main table displayed in the page. This key is used by the Basic look Direct to Web templates containing tables: BASInspectPage, BASListPage, BASPlainListPage, BASQueryAllEntitiesPage, and BASQueryPage.

__color__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: The color used to display the attribute. This key is used by the styled display property-level components: D2WDisplayStyledDate, D2WDisplayStyledNumber, and D2WDisplayStyledString. It is also used by the D2WKeyPathContaininer property-level component.

__colorForLine__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: This key is private. You should never need to get or set the value for it.

__columnCount__

: __Type:__ `Integer`

: __Appears:__ Rule's key (right-hand side)

: The maximum number of columns in the table that displays the listed objects. This key is used by the plain-list page Direct to Web templates: BASPlainListPage, NEUPlainListPage, and WOLPlainListPage.

__componentAvailable__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: The name of a property-level component that can be used to display a property. The Web Assistant asks the rule system for all rules that can fire for this key to determine which property-level components can be used to display a property.

__componentBorder__

: __Type:__ `Integer`

: __Appears:__ Rule's key (right-hand side)

: The width of the border around the table displayed in the property-level component. This key is used by the D2WDisplayToManyTable and D2WKeyPathContainer property-level components.

__componentName__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: The name of a property-level component that can be used to display a particular property for a particular task and entity. This key is used by the Direct to Web templates.

__customComponentName__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: The name of a custom WOComponent defined in your project. This key is used by the D2WCustomComponent and D2WCustomQueryComponent property-level components.

__disabled__

: __Type:__ `Integer`

: __Appears:__ Rule's key (right-hand side)

: A flag that has value of 1 when the current property-level component's hyperlink is disabled and a value of 0 otherwise. This key is used by the D2WDisplayToManyTable, D2WDisplayToOne, D2WEditToOneFault, and D2WKeyPathContainer property-level components.

__displayNameForProperty__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: A String containing a representation of the current property's name that is suitable for displaying in a user interface.

__displayPropertyKeys__

: __Type:__ `NSArray`

: __Appears:__ Rule's key (right-hand side)

: An array of keys for the properties that are visible on the page for the receiver's current task and entity. A Direct to Web template that displays the properties of an entity usually iterates through this list. You can change the visible properties on a page using the Web Assistant.

__editIcon__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: The name of the file depicting an icon the user clicks to edit a relationship. The file must be in your project's WebServerResources suitcase. This key is used by the D2WEditToManyFault and the D2WEditToOneFault property-level components.

__entity__

: __Type:__ `EOEntity`

: __Appears:__ Rule's condition (left-hand side)

: The receiver's current entity, stored in the receiver's state dictionary. The value for this key is set by the Direct to Web factory when it creates a new Direct to Web page.

__formatter__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: A string containing a format specification. This key is used by the number and date property-level components. It is also used by the D2WEditString and D2WQueryStringComponent property-level components.

__framesActive__

: __Type:__ `Integer`

: __Appears:__ Rule's key (right-hand side)

: This key is private. You should never need to get or set the value for it.

__framework__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: The name of the framework containing the image displayed by the D2WDisplayImageFromPath property level component. Defaults to "app" for images in your application.

__inspectComponentName__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: This key is private. You should never need to get or set the value for it.

__inspectIcon__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: The name of the file depicting an icon the user clicks to inspect a relationship. The file must be in your project's WebServerResources suitcase. This key is used by the D2WEditToManyFault and the D2WEditToOneFault property-level components.

__isDeep__

: __Type:__ `Integer`

: __Appears:__ Rule's key (right-hand side)

: A flag that has a value of 1 when fetches should include sub-entities of the fetch specification's entity. Defaults to 0. This key is used by the fetch specifications for query pages.

__italic__

: __Type:__ `Integer`

: __Appears:__ Rule's key (right-hand side)

: A flag that has a value of 1 when text is displayed in italics and a value of 0 otherwise. This key is used by the styled display property-level components: D2WDisplayStyledDate, D2WDisplayedStyledNumber, D2WDisplayStyledString, and D2WKeyPathContainer.

__justification__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: A flag indicating whether or not the text is justified. This key is used by the list page Direct to Web templates: BASListPage, NEUListPage, and WOLListPage.

__keyWhenRelationship__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: When the receiver's current property is a relationship, the value for this key is the key for a property of the destination entity that identifies the entity. For example, if the receiver's current entity is `Movie` and the current property is the `toStudio` relationship, the destination entity is `Studio`. An appropriate value for `keyWhenRelationship` is `name` since the `name` property identifies the studio.

__length__

: __Type:__ `Integer`

: __Appears:__ Rule's key (right-hand side)

: The size of the field used to display a property.

__numCols__

: __Type:__ `Integer`

: __Appears:__ Rule's key (right-hand side)

: The number of columns in the table of checkboxes or radio buttons used to display the destination objects of a relationship. This key is used by the D2WDisplayToManyTable, D2WEditToManyRelationship, D2WEditToOneRelationship, D2WKeyPathContainer, D2WQueryToManyRelationship, and D2WQueryToOneRelationship property-level components.

__pageAvailable__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: The name of a Direct to Web template that can be used to display a page. The Web Assistant asks the rule system for all rules that can fire for this key to determine which Direct to Web templates can be used to display a page. See the "Customizing A Direct to Web Application" chapter of _Developing WebObjects Applications With Direct to Web_ for an example of how to create a rule for this key.

__pageName__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: The name of the Direct to Web template used to display a page. Used by the Direct to Web factory when creating new pages.

__pageWrapperName__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: The name of the page wrapper WOComponent in which the Direct to Web page appears. Defaults to "PageWrapper". If you did not use the Direct to Web wizard to create your project, you should create a component called PageWrapper.wo and add it to your project.

__propertyIsKeyPath__

: __Type:__ `Integer`

: __Appears:__ Rule's condition (left-hand side)

: A flag that has a value of 1 when the receiver's current property is a key path and a value of 0 otherwise. The value for this key is derived from `propertyKey`.

__propertyKey__

: __Type:__ `String`

: __Appears:__ Rule's condition (left-hand side)

: A String containing the key for the receiver's current property. When the the value for this key is set, the values for the `attribute`, `propertyIsKeyPath`, `propertyType`, and `relationship` keys are derived from it. The value for this key is stored in the receiver's state dictionary.

__propertyType__

: __Type:__ `String`

: __Appears:__ Rule's condition (left-hand side)

: A String representing the type of the receiver's current property. Resolves to "r" if the property is a relationship, "a" if the property is an attribute, "c" if the property is a custom property, and "k" if the property is a key path. The value for this key is derived from `propertyKey`.

__readOnly__

: __Type:__ `Integer`

: __Appears:__ Rule's key (right-hand side)

: A flag that has a value of 1 when the receiver's current entity cannot be modified and a value of 0 otherwise. You can change which entites are read-only using the Web Assistant.

__readOnlyEntityNames__

: __Type:__ `NSArray`

: __Appears:__ Rule's key (right-hand side)

: An array of entity names that are read-only. You can change which entities are read-only using the Web Assistant.

__refreshRefetchedObjects__

: __Type:__ `Integer`

: __Appears:__ Rule's key (right-hand side)

: A flag that has a value of 1 when existing objects are overwritten with fetched values when they've been updated or changed. If the flag's value is 0 (the default), existing objects aren't touched when their data is refetched (the fetched data is simply discarded). This key is used by the fetch specifications for query pages.

__relationship__

: __Type:__ `EORelationship`

: __Appears:__ Rule's condition (left-hand side)

: The receiver's current relationship. Resolves to `null` if the current property is not a relationship. The value for this key is derived from `propertyKey`.

__rows__

: __Type:__ `Integer`

: __Appears:__ Rule's key (right-hand side)

: The number of rows in the D2WDisplayLargeString and D2WEditLargeString property-level components. The value for this key is passed to the ROWS attribute of the component's TEXTAREA tag.

__selectButtonFileName__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: The name of the file depicting the an icon the user clicks to select a record in a select component. The file must be in your project's WebServerResources suitcase. This key is used by the BASListPage and WOLListPage Direct to Web templates.

__showBanner__

: __Type:__ `Integer`

: __Appears:__ Rule's key (right-hand side)

: A flag that has a value of 1 when the banner should be displayed by a Direct to Web template and a value of 0 otherwise. This key is useful if you embed a Direct to Web reusable component in one of your pages and find that the banner is too big or unattractive in the page.

__size__

: __Type:__ `Integer`

: __Appears:__ Rule's key (right-hand side)

: The number of rows in the browsers displayed by some of the relationship property-level components. Defaults to 8.

__startupEntityName__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: The name of entity used on startup page. Since the startup page is a query-all page by default, this key is not used in a Direct to Web application generated by the wizard. If you change the default startup task (see `startupTask`) to one that requires an entity, use this key.

__startupTask__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: The startup page task. Defaults to "queryAll". If you override this default and specify a task that requires an entity, you need to specify the value for the `startupEntityName` key.

__subtask__

: __Type:__ `String`

: __Appears:__ Rule's condition (left-hand side)

: This key is private. You should never need to get or set the value for it.

__tabContents__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: This key is private. You should never need to get or set the value for it.

__tableWidth__

: __Type:__ `Number`

: __Appears:__ Rule's key (right-hand side)

: The width of the tab panel. This key is used by the NEUTabInspectPage and the WOLTabInspectPage Direct to Web templates.

__tabName__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: The name of the tab (in a tab-inspect page) the receiver's current property is in. To specify which properties appear in tab called `myTab`, you need to write rules that specify the properties for which `tabName=myTab`.

__tabs__

: __Type:__ `NSArray`

: __Appears:__ Rule's key (right-hand side)

: An array containing the tab names.

__target__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: This key is private. You should never need to get or set the value for it.

__task__

: __Type:__ `String`

: __Appears:__ Rule's condition (left-hand side)

: The receiver's current task, stored in the receiver's state dictionary. The value for this key is set by the Direct to Web factory when it creates a new Direct to Web page.

__threshold__

: __Type:__ `Integer`

: __Appears:__ Rule's key (right-hand side)

: This key is private. You should never need to get or set the value for it.

__uiStyle__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: The user interface style used by the certain relationship property-level components. For the D2WEditToOneRelationship and D2WQueryToOneRelationship components, the value can be "browser", "popup", or "radio". For the D2WEditToManyRelationship and D2WQueryToManyRelationship components, the value can be "browser", or "checkbox"

__usesDistinct__

: __Type:__ `Integer`

: __Appears:__ Rule's key (right-hand side)

: A flag that has a value of 1 when duplicate objects or records are removed after fetching. Defaults to 0. This key is used by the fetch specifications for query pages.

__visibleEntityNames__

: __Type:__ `NSArray`

: __Appears:__ Rule's key (right-hand side)

: An array of entities that appear in the application. These entities can be read-only or not. You can set which entities appear in your application using the Web Assistant.

__webAssistantPageName__

: __Type:__ `String`

: __Appears:__ Rule's key (right-hand side)

: This key is private. You should never need to get or set the value for it.
