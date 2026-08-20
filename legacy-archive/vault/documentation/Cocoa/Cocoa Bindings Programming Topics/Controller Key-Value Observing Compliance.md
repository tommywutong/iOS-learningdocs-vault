---
title: Cocoa Bindings Programming Topics
apple_id: 10000167i
resource_type: Guide
platform: macOS
topic: General
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/Articles/ControllerKey-ValueObservingCompliance.html
archived_at: '2026-07-15T07:11:59.488689Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Bindings Programming Topics](Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md)


[Next](Troubleshooting%20Cocoa%20Bindings.md)[Previous](Filtering%20Using%20a%20Custom%20Array%20Controller.md)

# Controller Key-Value Observing Compliance

The Cocoa bindings controller classes only provide key-value observing notifications for selected properties. This article enumerates the key-value-observing compliant properties for each class.

NSUserDefaultsController is key-value-observing compliant for the following properties:

- appliesImmediately
- defaults
- hasUnappliedChanges
- initialValues
- values

NSObjectController is key-value-observing compliant for the following properties:

- canAdd
- canRemove
- content
- isEditable
- objectClass
- selectedObjects
- selection

NSArrayController is key-value-observing compliant for the following properties:

- alwaysUsesMultipleValuesMarker
- arrangedObjects
- avoidsEmptySelection
- canAdd
- canInsert
- canRemove
- canSelectNext
- canSelectPrevious
- clearsFilterPredicateOnInsertion
- content
- filterPredicate
- isEditable
- preservesSelection
- selectedObjects
- selection
- selectionIndex
- selectionIndexes
- selectsInsertedObjects
- sortDescriptors

NSTreeController is key-value-observing compliant for the following properties:

- alwaysUsesMultipleValuesMarker
- arrangedObjects
- avoidsEmptySelection
- canAdd
- canAddChild
- canInsert
- canInsertChild
- canRemove
- canSelectNext
- canSelectPrevious
- content
- isEditable
- preservesSelection
- selectedObjects
- selection
- selectionIndexPath
- selectionIndexPaths
- selectsInsertedObjects
- sortDescriptors

[Next](Troubleshooting%20Cocoa%20Bindings.md)[Previous](Filtering%20Using%20a%20Custom%20Array%20Controller.md)

