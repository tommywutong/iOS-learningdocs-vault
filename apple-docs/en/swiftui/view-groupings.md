---
title: View groupings
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-groupings
source_url: 'https://developer.apple.com/documentation/swiftui/view-groupings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-groupings.json'
content_hash: 'sha256:a42654bc40880870'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# View groupings

<sub>API Collection</sub>

Present views in different kinds of purpose-driven containers, like forms or control groups.

## Overview

You can create groups of views that serve different purposes.

![](../../../attachments/53961e3c03e161d637bf0a08c342c9a4/view-groupings-hero@2x.png)

For example, a [Group](group.md) construct treats the specified views as a unit without imposing any additional layout or appearance characteristics. A [Form](form.md) presents a group of elements with a platform-specific appearance that’s suitable for gathering input from people.

For design guidance, see [Layout](../design/human-interface-guidelines/layout.md) in the Human Interface Guidelines.

## Topics

### Grouping views into a container

- [Creating custom container views](creating-custom-container-views.md) — Access individual subviews to compose flexible container views.
- [Group](group.md) — A type that collects multiple instances of a content type — like views, scenes, or commands — into a single unit.
- [GroupElementsOfContent](groupelementsofcontent.md) — Transforms the subviews of a given view into a resulting content view.
- [GroupSectionsOfContent](groupsectionsofcontent.md) — Transforms the sections of a given view into a resulting content view.

### Organizing views into sections

- [Section](section.md) — A container view that you can use to add hierarchy within certain views.
- [SectionCollection](sectioncollection.md) — An opaque collection representing the sections of view.
- [SectionConfiguration](sectionconfiguration.md) — Specifies the contents of a section.

### Iterating over dynamic data

- [ForEach](foreach.md) — A structure that computes views on demand from an underlying collection of identified data.
- [ForEachSectionCollection](foreachsectioncollection.md) — A collection which allows a view to be treated as a collection of its sections in a for each loop.
- [ForEachSubviewCollection](foreachsubviewcollection.md) — A collection which allows a view to be treated as a collection of its subviews in a for each loop.
- [DynamicViewContent](dynamicviewcontent.md) — A type of view that generates views from an underlying collection of data.

### Accessing a container’s subviews

- [Subview](subview.md) — An opaque value representing a subview of another view.
- [SubviewsCollection](subviewscollection.md) — An opaque collection representing the subviews of view.
- [SubviewsCollectionSlice](subviewscollectionslice.md) — A slice of a SubviewsCollection.
- [containerValue(_:_:)](<view/containervalue(____).md>) — Sets a particular container value of a view.
- [ContainerValues](containervalues.md) — A collection of container values associated with a given view.
- [ContainerValueKey](containervaluekey.md) — A key for accessing container values.

### Grouping views into a box

- [GroupBox](groupbox.md) — A stylized view, with an optional label, that visually collects a logical grouping of content.
- [groupBoxStyle(_:)](<view/groupboxstyle(__).md>) — Sets the style for group boxes within this view.

### Grouping inputs

- [Form](form.md) — A container for grouping controls used for data entry, such as in settings or inspectors.
- [formStyle(_:)](<view/formstyle(__).md>) — Sets the style for forms in a view hierarchy.
- [LabeledContent](labeledcontent.md) — A container for attaching a label to a value-bearing view.
- [labeledContentStyle(_:)](<view/labeledcontentstyle(__).md>) — Sets a style for labeled content.

### Presenting a group of controls

- [ControlGroup](controlgroup.md) — A container view that displays semantically-related controls in a visually-appropriate manner for the context
- [controlGroupStyle(_:)](<view/controlgroupstyle(__).md>) — Sets the style for control groups within this view.

## See Also

### View layout

- [Layout fundamentals](layout-fundamentals.md) — Arrange views inside built-in layout containers like stacks and grids.
- [Layout adjustments](layout-adjustments.md) — Make fine adjustments to alignment, spacing, padding, and other layout parameters.
- [Custom layout](custom-layout.md) — Place views in custom arrangements and create animated transitions between layout types.
- [Lists](lists.md) — Display a structured, scrollable column of information.
- [Tables](tables.md) — Display selectable, sortable data arranged in rows and columns.
- [Scroll views](scroll-views.md) — Enable people to scroll to content that doesn’t fit in the current display.
