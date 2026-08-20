---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Architecture/The_Direct_to_Web_Context.html
archived_at: '2026-07-15T08:12:23.126628Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Direct_to_W_rganization.md)[![Next](attachments/DirectToWeb/Images/next.gif)](The_Direct_to_Web_Factory.md)

## The Direct to Web Context

As mentioned earlier, a Direct to Web template is rendered
using runtime information about the entities it displays. To translate
that information into something you can bind to the template's
dynamic elements, Direct to Web uses an instance of the D2WContext
class called the Direct to Web context. This object has two functions:
it maintains a _state dictionary_ that holds
the state of a Direct to Web template as it renders, and it provides
values that you can bind directly to attributes of dynamic elements.
Each instance of a Direct to Web template has an associated Direct
to Web context.

### Maintaining State

As the Direct to Web template changes state as it is rendered,
the Direct to Web context changes state with it. Specifically, the
Direct to Web context uses an NSDictionary containing

- the current
  task
- the current entity
- the current property (attribute or relationship)

The task and the entity remain constant while the template
renders (with the exception of the query all template, for which
only the task remains constant). The property does not stay constant,
however. Consider an edit page. It displays the entity name and
the entity's visible properties. To display the properties, the
Direct to Web template iterates through them using a WORepetition.
As it iterates, the Direct to Web context updates the information
about the current property in its dictionary.

### Providing Binding Values

Each Direct to Web template has a Direct to Web context called `d2wContext`,
which implements the EOKeyValueCoding interface. Thus you can bind
directly to keys that the context responds to. For example, [Listing 3-1](#apple-ijauussjirdug) shows
the bindings file for a Direct to Web template that displays the
name of the entity.

__Listing
3-1 Bindings file for a Direct to Web template__

```
String1 : WOString {
    value = d2wContext.entity.name;
};
```

The Direct to Web context determines the values for the keys
(`d2wContext.entity.name` for example)
in one of three ways:

- it looks
  it up in its state dictionary
- it accesses application configuration information. (The Web
  Assistant is the primary way to modify the application configuration.)
- it derives values from the state and configuration information

#### Resolving Keys With the State Dictionary

The state dictionary contains the following entries:

__|  |  |
| --- | --- |
| Key | Description of Value |__| `task` | A string representing the current task. |
| `entity` | An EOEntity representing the current entity. |
| `propertyKey` | A string representing the key of the current property. |
| `attribute` | An EOAttribute representing the current attribute (`null` if the current property is a relationship.) |
| `relationship` | An EORelationship representing the current relationship (`null` if the current property is an attribute.) |

If the dictionary contains the key the template needs, the
Direct to Web context resolves the key by returning the value in
the dictionary. Otherwise the Direct to Web context resolves the
key using one of the other ways.

#### Resolving Keys With the Application Configuration

Some keys can only be resolved using the application configuration
information, which is stored as a database of rules. For example
a rule to determine the property-level component for the `dateReleased` attribute
might be "If the task is 'edit', the entity name is 'Movie',
and the property key is 'dateReleased' then the value for the `componentName` key
is 'D2WQueryDateOperator'."

The Direct to Web context uses the _rule engine_ to
resolve keys that aren't in its dictionary. [Figure 3-3](#apple-ijauursgivdee) shows how the rule engine
relates to the Direct to Web context. ["The Rule System"](The_Rule_System.md#apple-ijauurcbifbeu) contains detailed
information on how the rule engine works.

__Figure
3-3 Direct to Web Architecture__

![[image: ../Art/Architecture.gif]](../Art/Architecture.gif)

#### Resolving Derived Values

The rule engine also provides objects that have methods that
derive values from the Direct to Web context's state dictionary.
An example of a derived value is the name displayed for a property:
a method converts a property name like `dateReleased` to
a display string "Date Released". Using derived values is discussed
in more detail in ["The Rule System"](The_Rule_System.md#apple-ijauurcbifbeu).

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Direct_to_W_rganization.md)[![Next](attachments/DirectToWeb/Images/next.gif)](The_Direct_to_Web_Factory.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
