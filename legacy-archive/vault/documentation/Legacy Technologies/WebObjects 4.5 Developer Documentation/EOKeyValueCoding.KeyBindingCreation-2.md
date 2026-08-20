---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOKeyBindingCreation.html
archived_at: '2026-07-15T08:11:43.461188Z'
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
> : (Java Client only) NSKeyValueCoding

> **__Package:__**
> : (Java Client) com.apple.client.eocontrol
> : (Yellow Box) com.apple.yellow.eocontrol

---

## Interface Description

---

The [EOKeyValueCoding.KeyBindingCreation](#apple-ineucq2iizduu) interface defines
the methods that create and cache [EOKeyBinding](EOKeyBinding.md#apple-ineegqshjfeui)s-objects that associate
a class/key pair to a mechanism for accessing the key.

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

If _bindingTypeMask_ is [EOSetKeyBindingMask](EOKeyValueCoding-3.md#apple-ijauirkbirdui), returns the binding
responsible for setting the value for _key_; otherwise
if _bindingTypeMask_ is [EOStoredKeyBindingMask](EOKeyValueCoding-3.md#apple-ijauiq2djjbeu), returns the
binding responsible for retrieving the value for _key_. EOCustomObject
and EOGenericRecord's implementations look for methods and instance
variables fitting the key-value coding naming conventions as described
in the method descriptions for [takeValue:forKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwkvtbnr2wkotgn5zewzlzhi) and [valueForKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3wmfwhkzkgn5zewzlzhi).

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
