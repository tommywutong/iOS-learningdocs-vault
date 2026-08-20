---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EOKeyBindingCreation.html
archived_at: '2026-07-15T08:11:38.927970Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOKeyValueCoding.KeyBindingCreation

> __Implemented by:__ : EOEnterpriseObject
> : EOCustomObject
> : EOGenericRecord

> **__Implements:__**
> : (com.apple.client.eocontrol only) NSKeyValueCoding

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Interface Description

---

The [EOKeyValueCoding.KeyBindingCreation](#apple-ineucq2iizduu) interface defines
the methods that create and cache [EOKeyValueCoding.KeyBinding](EOKeyValueCoding.KeyBinding.md#apple-ineegqshjfeui)s-objects
that associate a class/key pair to a mechanism for accessing the
key.

EOCustomObject and EOGenericRecord provide default implementations
of this interface. Apple doesn't anticipate the need for you to
invoke or implement the methods in [EOKeyValueCoding.KeyBindingCreation](#apple-ineucq2iizduu).
It is used internally by Enterprise Objects Framework. You should
never need to interact with it at all.

## Instance Methods

---

### createKeyValueBindingForKey

`public abstract EOKeyValueCoding.KeyBinding createKeyValueBindingForKey(
String key,
int bindingTypeMask)`

If _bindingTypeMask_ is [SetKeyBindingMask](EOKeyValueCoding.md#apple-ijauirkbirdui), returns the binding
responsible for setting the value for _key_ ; otherwise
if _bindingTypeMask_ is [StoredKeyBindingMask](EOKeyValueCoding.md#apple-ijauiq2djjbeu), returns the binding
responsible for retrieving the value for _key._ EOCustomObject
and EOGenericRecord's implementations look for methods and instance
variables fitting the key-value coding naming conventions as described
in the method descriptions for [takeValueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz) and [valueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe).

---

### keyValueBindingForKey

`public abstract EOKeyValueCoding.KeyBinding keyValueBindingForKey(
String key,
int bindingTypeMask)`

Returns the binding responsible for setting
or retrieving the value for key, creating and caching the binding
if it isn't cached already. When a binding cannot be found for
the specified key, or if the receiver has overridden the default
implementation of an EOKeyValueCoding accessor method, a binding
that simply invokes that accessor is returned.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
