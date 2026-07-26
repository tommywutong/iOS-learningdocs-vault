---
title: NSBindingOption
framework: AppKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsbindingoption
source_url: 'https://developer.apple.com/documentation/appkit/nsbindingoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsbindingoption.json'
content_hash: 'sha256:1a8881977760f4a7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AppKit](../appkit.md)

# NSBindingOption

<sub>Structure</sub>

<sub>macOS</sub>

```swift
struct NSBindingOption
```

## Discussion

Values that are used as keys in the options dictionary passed to the [bind(_:to:withKeyPath:options:)](<../objectivec/nsobject-swift.class/bind(__to_withkeypath_options_).md>) method.

These keys are also used in the dictionary returned as the [NSOptionsKey](nsbindinginfokey/options.md) value of [infoForBinding(_:)](<../objectivec/nsobject-swift.class/infoforbinding(__).md>). For more information, see [Cocoa Bindings](cocoa-bindings.md).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Binding Options

- [NSAllowsEditingMultipleValuesSelectionBindingOption](nsbindingoption/allowseditingmultiplevaluesselection.md) — An `NSNumber` object containing a Boolean value that determines if the binding allows editing when the value represents a multiple selection.
- [NSAllowsNullArgumentBindingOption](nsbindingoption/allowsnullargument.md) — An `NSNumber` object containing a Boolean value that determines if the argument bindings allows passing argument values of `nil`.
- [NSAlwaysPresentsApplicationModalAlertsBindingOption](nsbindingoption/alwayspresentsapplicationmodalalerts.md) — A number containing a Boolean value that determines if validation and error alert panels displayed as a result of this binding are displayed as application modal alerts.
- [NSConditionallySetsEditableBindingOption](nsbindingoption/conditionallysetseditable.md) — An `NSNumber` object containing a Boolean value that determines if the editable state of the user interface item is automatically configured based on the controller’s selection.
- [NSConditionallySetsEnabledBindingOption](nsbindingoption/conditionallysetsenabled.md) — An `NSNumber` object containing a Boolean value that determines if the enabled state of the user interface item is automatically configured based on the controller’s selection.
- [NSConditionallySetsHiddenBindingOption](nsbindingoption/conditionallysetshidden.md) — An `NSNumber` object containing a Boolean value that determines if the hidden state of the user interface item is automatically configured based on the controller’s selection.
- [NSContentPlacementTagBindingOption](nsbindingoption/contentplacementtag.md) — A number that specifies the tag id of the popup menu item to replace with the content of the array.
- [NSContinuouslyUpdatesValueBindingOption](nsbindingoption/continuouslyupdatesvalue.md) — An `NSNumber` object containing a Boolean value that determines whether the value of the binding is updated as edits are made to the user interface item or is updated only when the user interface item resigns as the responder.
- [NSCreatesSortDescriptorBindingOption](nsbindingoption/createssortdescriptor.md) — An `NSNumber` object containing a Boolean value that determines if a sort descriptor is created for a table column.
- [NSDeletesObjectsOnRemoveBindingsOption](nsbindingoption/deletesobjectsonremove.md) — An `NSNumber` object containing a Boolean value that determines if an object is deleted from the managed context immediately upon being removed from a relationship.
- [NSDisplayNameBindingOption](nsbindingoption/displayname.md) — An `NSString` object containing a human readable string to be displayed for a predicate.
- [NSDisplayPatternBindingOption](nsbindingoption/displaypattern.md) — An `NSString` object that specifies a format string used to construct the final value of a string.
- [NSHandlesContentAsCompoundValueBindingOption](nsbindingoption/handlescontentascompoundvalue.md) — An `NSNumber` object containing a Boolean value that determines if the content is treated as a compound value.
- [NSInsertsNullPlaceholderBindingOption](nsbindingoption/insertsnullplaceholder.md) — An `NSNumber` object containing a Boolean value that determines if an additional item which represents `nil` is inserted into a matrix or pop-up menu before the items in the content array.
- [NSInvokesSeparatelyWithArrayObjectsBindingOption](nsbindingoption/invokesseparatelywitharrayobjects.md) — An `NSNumber` object containing a Boolean value that determines whether the specified selector is invoked with the array as the argument or is invoked repeatedly with each array item as an argument.
- [NSMultipleValuesPlaceholderBindingOption](nsbindingoption/multiplevaluesplaceholder.md) — An object that is used as a placeholder when the key path of the bound controller returns the `NSMultipleValuesMarker` marker for a binding.
- [NSNoSelectionPlaceholderBindingOption](nsbindingoption/noselectionplaceholder.md) — An object that is used as a placeholder when the key path of the bound controller returns the `NSNoSelectionMarker` marker for a binding.
- [NSNotApplicablePlaceholderBindingOption](nsbindingoption/notapplicableplaceholder.md) — An object that is used as a placeholder when the key path of the bound controller returns the `NSNotApplicableMarker` marker for a binding.
- [NSNullPlaceholderBindingOption](nsbindingoption/nullplaceholder.md) — An object that is used as a placeholder when the key path of the bound controller returns `nil` for a binding.
- [NSPredicateFormatBindingOption](nsbindingoption/predicateformat.md) — An `NSString` object containing the predicate pattern string for the predicate bindings. Use `$value` to refer to the value in the search field.
- [NSRaisesForNotApplicableKeysBindingOption](nsbindingoption/raisesfornotapplicablekeys.md) — An `NSNumber` object containing a Boolean value that specifies if an exception is raised when the binding is bound to a key that is not applicable—for example when an object is not key-value coding compliant for a key.
- [NSSelectorNameBindingOption](nsbindingoption/selectorname.md) — An `NSString` object that specifies the method selector invoked by the target binding when the user interface item is clicked.
- [NSSelectsAllWhenSettingContentBindingOption](nsbindingoption/selectsallwhensettingcontent.md) — An `NSNumber` object containing a Boolean value that specifies if all the items in the array controller are selected when the content is set.
- [NSValidatesImmediatelyBindingOption](nsbindingoption/validatesimmediately.md) — An `NSNumber` object containing a Boolean value that determines if the contents of the binding are validated immediately.
- [NSValueTransformerBindingOption](nsbindingoption/valuetransformer.md) — An `NSValueTransformer` instance that is applied to the bound value.
- [NSValueTransformerNameBindingOption](nsbindingoption/valuetransformername.md) — The value for this key is an identifier of a registered `NSValueTransformer` instance that is applied to the bound value.

### Initializers

- [init(rawValue:)](<nsbindingoption/init(rawvalue_).md>)

## See Also

### Key-Value Data

- [NSDictionaryController](nsdictionarycontroller.md) — A bindings-compatible controller that manages the display and editing of a dictionary of key-value pairs.
- [NSDictionaryControllerKeyValuePair](nsdictionarycontrollerkeyvaluepair.md) — A set of methods implemented by arranged objects to give access to information about those objects.
- [NSBindingName](nsbindingname.md) — Values that specify a binding for certain methods.
- [NSBindingInfoKey](nsbindinginfokey.md)
- [NSIsControllerMarker](<nsiscontrollermarker(__).md>) — Tests whether a given object is special marker object used for indicating the state of a selection in relation to a key.
- [NSKeyValueBindingCreation](../objectivec/nskeyvaluebindingcreation.md) — A set of methods that you can use to create and remove bindings between view objects and controllers, or between controllers and model objects.
- [Binding dictionary keys](binding-dictionary-keys.md) — These constants define keys in the binding information dictionary.
