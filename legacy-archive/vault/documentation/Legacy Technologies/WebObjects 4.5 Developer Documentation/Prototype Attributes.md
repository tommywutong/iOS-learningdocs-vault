---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/EOTools/Attributes2.html
archived_at: '2026-07-15T08:03:36.407966Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Tools and Techniques

[!Table of Contents](Changing%20an%20Attribute%27s%20Characteristics.md) [!Previous Section](Changing%20an%20Attribute%27s%20Characteristics.md)

# Prototype Attributes

To allow easier model creation from scratch, EOModeler supports the concept of prototype attributes. Prototype attributes are just what they sound like - special attributes from which other attributes derive their settings. A prototype can specify any of the characteristics you normally define for an attribute. When you create an attribute, you can associate it with one of these prototypes, and the attribute's characteristics are then set from the prototype definition.
For example, suppose your adaptor contains a date prototype that defines the value class to be NSGregorianDate (NSCalendarDate in Objective-C) and the external type to be DATE. When you create an attribute and associate it with this date prototype, the attribute's value class is dynamically resolved to NSGregorianDate and its external type is dynamically resolved to DATE.

## Assigning a Prototype to an Attribute

To associate an attribute with a prototype, use the table mode of the Model Editor. Simply choose a prototype from the combo box in the Prototype column as shown in [Figure 22](#apple-ge2tqmrz). If EOModeler isn't displaying the Prototype column, activate it from the Add Column menu.

!

Figure 22. Assigning a Prototype to an Attribute

If any of the prototype information is incorrect for your attribute, you can override it. Just set the property of the attribute to the value you want (see [Figure 23](#apple-ge2tqnbw)). The remaining attribute properties will still dynamically resolve to the values set in the prototype.

!

Figure 23. Overriding Prototype Settings

## Creating Prototype Attributes

The prototypes you can assign to an attribute come from three places:

- An entity named __EO<AdaptorName>Prototypes__, where __<AdaptorName>__ is the name of the adaptor for your model (EOOraclePrototypes, for example)
- An entity named __EOPrototypes__
- The adaptor for your model

So to create your own prototype, create a prototype entity-an entity named either __EO<AdaptorName>Prototypes__ or __EOPrototypes__-and add an attribute to it. Note that the __EO<AdaptorName>Prototypes__ and __EOPrototypes__ entities can be defined in the current model or in another model in the model group (all the models in your project are typically a part of the same model group).
When resolving a prototype name, Enterprise Objects Framework looks for prototypes in __EO<AdaptorName>Prototypes__, then in __EOPrototypes__, and finally in the adaptor for your model. This search path allows you to override the prototypes provided by each adaptor. Furthermore, if you don't want to use the adaptor-defined prototypes at all, you can hide them. Create an entity named __EOPrototypesToHide__. For each prototype you want to hide, create an attribute with that name; you don't need to specify other attribute properties.
[!Table of Contents](Changing%20an%20Attribute%27s%20Characteristics.md) [!Next Section](Working%20with%20Relationships.md)
