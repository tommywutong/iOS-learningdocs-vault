---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/schemasInternals/CompositePage.html
archived_at: '2026-07-15T07:23:27.784417Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| schemasInternals.h | schemasInternals.h | schemasInternals.h | schemasInternals.h | schemasInternals.h |

|  |  |
| --- | --- |
| __Includes:__ | [<libxml/xmlversion.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlversion/index.html#//apple_ref/doc/header/xmlversion.h)  [<libxml/xmlregexp.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/xmlregexp/index.html#//apple_ref/doc/header/xmlregexp.h)  [<libxml/hash.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/hash/index.html#//apple_ref/doc/header/hash.h)  <libxml/dict.h> |

## Introduction

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlSchemaAnnot | xmlSchemaAnnot | xmlSchemaAnnot | xmlSchemaAnnot | xmlSchemaAnnot |

---

```
typedef struct _xmlSchemaAnnot xmlSchemaAnnot;
```

##### Discussion

Annotation

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlSchemaAttribute | xmlSchemaAttribute | xmlSchemaAttribute | xmlSchemaAttribute | xmlSchemaAttribute |

---

```
typedef struct _xmlSchemaAttribute xmlSchemaAttribute;
```

##### Discussion

xmlSchemaAttribute:
An attribute definition.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlSchemaAttributeGroup | xmlSchemaAttributeGroup | xmlSchemaAttributeGroup | xmlSchemaAttributeGroup | xmlSchemaAttributeGroup |

---

```
typedef struct _xmlSchemaAttributeGroup xmlSchemaAttributeGroup;
```

##### Discussion

An attribute group definition.

xmlSchemaAttribute and xmlSchemaAttributeGroup start of structures
must be kept similar

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlSchemaAttributeLink | xmlSchemaAttributeLink | xmlSchemaAttributeLink | xmlSchemaAttributeLink | xmlSchemaAttributeLink |

---

```
typedef struct _xmlSchemaAttributeLink xmlSchemaAttributeLink;
```

##### Discussion

xmlSchemaAttributeLink:
Used to build a list of attribute uses on complexType definitions.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlSchemaFacetLink | xmlSchemaFacetLink | xmlSchemaFacetLink | xmlSchemaFacetLink | xmlSchemaFacetLink |

---

```
typedef struct _xmlSchemaFacetLink xmlSchemaFacetLink;
```

##### Discussion

xmlSchemaFacetLink:
Used to build a list of facets.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlSchemaNotation | xmlSchemaNotation | xmlSchemaNotation | xmlSchemaNotation | xmlSchemaNotation |

---

```
typedef struct _xmlSchemaNotation xmlSchemaNotation;
```

##### Discussion

A notation definition.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlSchemaTypeLink | xmlSchemaTypeLink | xmlSchemaTypeLink | xmlSchemaTypeLink | xmlSchemaTypeLink |

---

```
typedef struct _xmlSchemaTypeLink xmlSchemaTypeLink;
```

##### Discussion

xmlSchemaTypeLink:
Used to build a list of types (e.g. member types of
simpleType with variety "union").

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlSchemaWildcard | xmlSchemaWildcard | xmlSchemaWildcard | xmlSchemaWildcard | xmlSchemaWildcard |

---

```
typedef struct _xmlSchemaWildcard xmlSchemaWildcard;
```

##### Discussion

xmlSchemaWildcard.
A wildcard.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| xmlSchemaWildcardNs | xmlSchemaWildcardNs | xmlSchemaWildcardNs | xmlSchemaWildcardNs | xmlSchemaWildcardNs |

---

```
typedef struct _xmlSchemaWildcardNs xmlSchemaWildcardNs;
```

##### Discussion

xmlSchemaCharValueLink:
Used to build a list of namespaces on wildcards.

## Structs and Unions

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _xmlSchema | _xmlSchema | _xmlSchema | _xmlSchema | _xmlSchema |

---

```
struct _xmlSchema {
    const xmlChar *name; /* schema name */
    const xmlChar *targetNamespace; /* the target namespace */
    const xmlChar *version;
    const xmlChar *id;
    xmlDocPtr doc;
    xmlSchemaAnnotPtr annot;
    int flags;
    xmlHashTablePtr typeDecl;
    xmlHashTablePtr attrDecl;
    xmlHashTablePtr attrgrpDecl;
    xmlHashTablePtr elemDecl;
    xmlHashTablePtr notaDecl;
    xmlHashTablePtr schemasImports;
    void *_private; /* unused by the library for users or bindings */
    xmlHashTablePtr groupDecl;
    xmlDictPtr dict;
    void *includes; /* the includes, this is opaque for now */
    int preserve; /* whether to free the document */
    int counter; /* used to give ononymous components unique names */
};
```

##### Discussion

_xmlSchema:

A Schemas definition

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _xmlSchemaFacet | _xmlSchemaFacet | _xmlSchemaFacet | _xmlSchemaFacet | _xmlSchemaFacet |

---

```
struct _xmlSchemaFacet {
    xmlSchemaTypeType type; /* The kind of type */
    struct _xmlSchemaFacet *next;/* the next type if in a sequence ... */
    const xmlChar *value;
    const xmlChar *id;
    xmlSchemaAnnotPtr annot;
    xmlNodePtr node;
    int fixed;
    int whitespace;
    xmlSchemaValPtr val;
    xmlRegexpPtr regexp;
};
```

##### Discussion

A facet definition.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| _xmlSchemaType | _xmlSchemaType | _xmlSchemaType | _xmlSchemaType | _xmlSchemaType |

---

```
struct _xmlSchemaType {
    xmlSchemaTypeType type; /* The kind of type */
    struct _xmlSchemaType *next;/* the next type if in a sequence ... */
    const xmlChar *name;
    const xmlChar *id;
    const xmlChar *ref;
    const xmlChar *refNs;
    xmlSchemaAnnotPtr annot;
    xmlSchemaTypePtr subtypes;
    xmlSchemaAttributePtr attributes;
    xmlNodePtr node;
    int minOccurs;
    int maxOccurs;
    int flags;
    xmlSchemaContentType contentType;
    const xmlChar *base;
    const xmlChar *baseNs;
    xmlSchemaTypePtr baseType;
    xmlSchemaFacetPtr facets;
    struct _xmlSchemaType *redef;/* possible redefinitions for the type */
    int recurse;
    xmlSchemaAttributeLinkPtr attributeUses;
    xmlSchemaWildcardPtr attributeWildcard;
    int builtInType;
    xmlSchemaTypeLinkPtr memberTypes;
    xmlSchemaFacetLinkPtr facetSet;
    const xmlChar *refPrefix;
    xmlSchemaTypePtr contentTypeDef;
    xmlRegexpPtr contModel;
};
```

##### Discussion

_xmlSchemaType:

Schemas type definition.

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ANY_LAX | XML_SCHEMAS_ANY_LAX | XML_SCHEMAS_ANY_LAX | XML_SCHEMAS_ANY_LAX | XML_SCHEMAS_ANY_LAX |

---

```
#define XML_SCHEMAS_ANY_LAX 2
```

##### Discussion

XML_SCHEMAS_ANY_LAX:

Used by wildcards.
Validate if type found, don't worry if not found

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ANY_SKIP | XML_SCHEMAS_ANY_SKIP | XML_SCHEMAS_ANY_SKIP | XML_SCHEMAS_ANY_SKIP | XML_SCHEMAS_ANY_SKIP |

---

```
#define XML_SCHEMAS_ANY_SKIP 1
```

##### Discussion

XML_SCHEMAS_ANY_SKIP:

Skip unknown attribute from validation

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ANY_STRICT | XML_SCHEMAS_ANY_STRICT | XML_SCHEMAS_ANY_STRICT | XML_SCHEMAS_ANY_STRICT | XML_SCHEMAS_ANY_STRICT |

---

```
#define XML_SCHEMAS_ANY_STRICT 3
```

##### Discussion

XML_SCHEMAS_ANY_STRICT:

Used by wildcards.
Apply strict validation rules

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ANYATTR_LAX | XML_SCHEMAS_ANYATTR_LAX | XML_SCHEMAS_ANYATTR_LAX | XML_SCHEMAS_ANYATTR_LAX | XML_SCHEMAS_ANYATTR_LAX |

---

```
#define XML_SCHEMAS_ANYATTR_LAX 2
```

##### Discussion

XML_SCHEMAS_ANYATTR_LAX:

Ignore validation non definition on attributes
Obsolete, not used anymore.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ANYATTR_SKIP | XML_SCHEMAS_ANYATTR_SKIP | XML_SCHEMAS_ANYATTR_SKIP | XML_SCHEMAS_ANYATTR_SKIP | XML_SCHEMAS_ANYATTR_SKIP |

---

```
#define XML_SCHEMAS_ANYATTR_SKIP 1
```

##### Discussion

XML_SCHEMAS_ANYATTR_SKIP:

Skip unknown attribute from validation
Obsolete, not used anymore.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ANYATTR_STRICT | XML_SCHEMAS_ANYATTR_STRICT | XML_SCHEMAS_ANYATTR_STRICT | XML_SCHEMAS_ANYATTR_STRICT | XML_SCHEMAS_ANYATTR_STRICT |

---

```
#define XML_SCHEMAS_ANYATTR_STRICT 3
```

##### Discussion

XML_SCHEMAS_ANYATTR_STRICT:

Apply strict validation rules on attributes
Obsolete, not used anymore.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ATTR_FIXED | XML_SCHEMAS_ATTR_FIXED | XML_SCHEMAS_ATTR_FIXED | XML_SCHEMAS_ATTR_FIXED | XML_SCHEMAS_ATTR_FIXED |

---

```
#define XML_SCHEMAS_ATTR_FIXED 1 << 9
```

##### Discussion

XML_SCHEMAS_ATTR_FIXED:

the attribute has a fixed value

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ATTR_GLOBAL | XML_SCHEMAS_ATTR_GLOBAL | XML_SCHEMAS_ATTR_GLOBAL | XML_SCHEMAS_ATTR_GLOBAL | XML_SCHEMAS_ATTR_GLOBAL |

---

```
#define XML_SCHEMAS_ATTR_GLOBAL 1 << 0
```

##### Discussion

XML_SCHEMAS_ATTR_GLOABAL:

allow elements in no namespace

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ATTR_INTERNAL_RESOLVED | XML_SCHEMAS_ATTR_INTERNAL_RESOLVED | XML_SCHEMAS_ATTR_INTERNAL_RESOLVED | XML_SCHEMAS_ATTR_INTERNAL_RESOLVED | XML_SCHEMAS_ATTR_INTERNAL_RESOLVED |

---

```
#define XML_SCHEMAS_ATTR_INTERNAL_RESOLVED 1 << 8
```

##### Discussion

XML_SCHEMAS_ATTR_INTERNAL_RESOLVED:

this is set when the "type" and "ref" references
have been resolved.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ATTR_NSDEFAULT | XML_SCHEMAS_ATTR_NSDEFAULT | XML_SCHEMAS_ATTR_NSDEFAULT | XML_SCHEMAS_ATTR_NSDEFAULT | XML_SCHEMAS_ATTR_NSDEFAULT |

---

```
#define XML_SCHEMAS_ATTR_NSDEFAULT 1 << 7
```

##### Discussion

XML_SCHEMAS_ATTR_NSDEFAULT:

allow elements in no namespace

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ATTR_USE_OPTIONAL | XML_SCHEMAS_ATTR_USE_OPTIONAL | XML_SCHEMAS_ATTR_USE_OPTIONAL | XML_SCHEMAS_ATTR_USE_OPTIONAL | XML_SCHEMAS_ATTR_USE_OPTIONAL |

---

```
#define XML_SCHEMAS_ATTR_USE_OPTIONAL 2
```

##### Discussion

XML_SCHEMAS_ATTR_USE_OPTIONAL:

The attribute is optional.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ATTR_USE_PROHIBITED | XML_SCHEMAS_ATTR_USE_PROHIBITED | XML_SCHEMAS_ATTR_USE_PROHIBITED | XML_SCHEMAS_ATTR_USE_PROHIBITED | XML_SCHEMAS_ATTR_USE_PROHIBITED |

---

```
#define XML_SCHEMAS_ATTR_USE_PROHIBITED 0
```

##### Discussion

XML_SCHEMAS_ATTR_USE_PROHIBITED:

Used by wildcards.
The attribute is prohibited.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ATTR_USE_REQUIRED | XML_SCHEMAS_ATTR_USE_REQUIRED | XML_SCHEMAS_ATTR_USE_REQUIRED | XML_SCHEMAS_ATTR_USE_REQUIRED | XML_SCHEMAS_ATTR_USE_REQUIRED |

---

```
#define XML_SCHEMAS_ATTR_USE_REQUIRED 1
```

##### Discussion

XML_SCHEMAS_ATTR_USE_REQUIRED:

The attribute is required.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ATTRGROUP_GLOBAL | XML_SCHEMAS_ATTRGROUP_GLOBAL | XML_SCHEMAS_ATTRGROUP_GLOBAL | XML_SCHEMAS_ATTRGROUP_GLOBAL | XML_SCHEMAS_ATTRGROUP_GLOBAL |

---

```
#define XML_SCHEMAS_ATTRGROUP_GLOBAL 1 << 1
```

##### Discussion

XML_SCHEMAS_ATTRGROUP_GLOBAL:

The attribute wildcard has been already builded.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ATTRGROUP_MARKED | XML_SCHEMAS_ATTRGROUP_MARKED | XML_SCHEMAS_ATTRGROUP_MARKED | XML_SCHEMAS_ATTRGROUP_MARKED | XML_SCHEMAS_ATTRGROUP_MARKED |

---

```
#define XML_SCHEMAS_ATTRGROUP_MARKED 1 << 2
```

##### Discussion

XML_SCHEMAS_ATTRGROUP_MARKED:

Marks the attr group as marked; used for circular checks.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ATTRGROUP_WILDCARD_BUILDED | XML_SCHEMAS_ATTRGROUP_WILDCARD_BUILDED | XML_SCHEMAS_ATTRGROUP_WILDCARD_BUILDED | XML_SCHEMAS_ATTRGROUP_WILDCARD_BUILDED | XML_SCHEMAS_ATTRGROUP_WILDCARD_BUILDED |

---

```
#define XML_SCHEMAS_ATTRGROUP_WILDCARD_BUILDED 1 << 0
```

##### Discussion

XML_SCHEMAS_ATTRGROUP_WILDCARD_BUILDED:

The attribute wildcard has been already builded.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_BLOCK_DEFAULT_EXTENSION | XML_SCHEMAS_BLOCK_DEFAULT_EXTENSION | XML_SCHEMAS_BLOCK_DEFAULT_EXTENSION | XML_SCHEMAS_BLOCK_DEFAULT_EXTENSION | XML_SCHEMAS_BLOCK_DEFAULT_EXTENSION |

---

```
#define XML_SCHEMAS_BLOCK_DEFAULT_EXTENSION 1 << 6
```

##### Discussion

XML_SCHEMAS_BLOCK_DEFAULT_EXTENSION:

the schema has "extension" in the set of blockDefault.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_BLOCK_DEFAULT_RESTRICTION | XML_SCHEMAS_BLOCK_DEFAULT_RESTRICTION | XML_SCHEMAS_BLOCK_DEFAULT_RESTRICTION | XML_SCHEMAS_BLOCK_DEFAULT_RESTRICTION | XML_SCHEMAS_BLOCK_DEFAULT_RESTRICTION |

---

```
#define XML_SCHEMAS_BLOCK_DEFAULT_RESTRICTION 1 << 7
```

##### Discussion

XML_SCHEMAS_BLOCK_DEFAULT_RESTRICTION:

the schema has "restriction" in the set of blockDefault.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_BLOCK_DEFAULT_SUBSTITUTION | XML_SCHEMAS_BLOCK_DEFAULT_SUBSTITUTION | XML_SCHEMAS_BLOCK_DEFAULT_SUBSTITUTION | XML_SCHEMAS_BLOCK_DEFAULT_SUBSTITUTION | XML_SCHEMAS_BLOCK_DEFAULT_SUBSTITUTION |

---

```
#define XML_SCHEMAS_BLOCK_DEFAULT_SUBSTITUTION 1 << 8
```

##### Discussion

XML_SCHEMAS_BLOCK_DEFAULT_SUBSTITUTION:

the schema has "substitution" in the set of blockDefault.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ELEM_ABSTRACT | XML_SCHEMAS_ELEM_ABSTRACT | XML_SCHEMAS_ELEM_ABSTRACT | XML_SCHEMAS_ELEM_ABSTRACT | XML_SCHEMAS_ELEM_ABSTRACT |

---

```
#define XML_SCHEMAS_ELEM_ABSTRACT 1 << 4
```

##### Discussion

XML_SCHEMAS_ELEM_ABSTRACT:

the element is abstract

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ELEM_BLOCK_ABSENT | XML_SCHEMAS_ELEM_BLOCK_ABSENT | XML_SCHEMAS_ELEM_BLOCK_ABSENT | XML_SCHEMAS_ELEM_BLOCK_ABSENT | XML_SCHEMAS_ELEM_BLOCK_ABSENT |

---

```
#define XML_SCHEMAS_ELEM_BLOCK_ABSENT 1 << 10
```

##### Discussion

XML_SCHEMAS_ELEM_BLOCK_ABSENT:

the "block" attribute is absent

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ELEM_BLOCK_EXTENSION | XML_SCHEMAS_ELEM_BLOCK_EXTENSION | XML_SCHEMAS_ELEM_BLOCK_EXTENSION | XML_SCHEMAS_ELEM_BLOCK_EXTENSION | XML_SCHEMAS_ELEM_BLOCK_EXTENSION |

---

```
#define XML_SCHEMAS_ELEM_BLOCK_EXTENSION 1 << 11
```

##### Discussion

XML_SCHEMAS_ELEM_BLOCK_EXTENSION:

disallowed substitutions are absent

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ELEM_BLOCK_RESTRICTION | XML_SCHEMAS_ELEM_BLOCK_RESTRICTION | XML_SCHEMAS_ELEM_BLOCK_RESTRICTION | XML_SCHEMAS_ELEM_BLOCK_RESTRICTION | XML_SCHEMAS_ELEM_BLOCK_RESTRICTION |

---

```
#define XML_SCHEMAS_ELEM_BLOCK_RESTRICTION 1 << 12
```

##### Discussion

XML_SCHEMAS_ELEM_BLOCK_RESTRICTION:

disallowed substitutions: "restriction"

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ELEM_BLOCK_SUBSTITUTION | XML_SCHEMAS_ELEM_BLOCK_SUBSTITUTION | XML_SCHEMAS_ELEM_BLOCK_SUBSTITUTION | XML_SCHEMAS_ELEM_BLOCK_SUBSTITUTION | XML_SCHEMAS_ELEM_BLOCK_SUBSTITUTION |

---

```
#define XML_SCHEMAS_ELEM_BLOCK_SUBSTITUTION 1 << 13
```

##### Discussion

XML_SCHEMAS_ELEM_BLOCK_SUBSTITUTION:

disallowed substitutions: "substituion"

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ELEM_CIRCULAR | XML_SCHEMAS_ELEM_CIRCULAR | XML_SCHEMAS_ELEM_CIRCULAR | XML_SCHEMAS_ELEM_CIRCULAR | XML_SCHEMAS_ELEM_CIRCULAR |

---

```
#define XML_SCHEMAS_ELEM_CIRCULAR 1 << 9
```

##### Discussion

XML_SCHEMAS_ELEM_CIRCULAR

a helper flag for the search of circular references.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ELEM_DEFAULT | XML_SCHEMAS_ELEM_DEFAULT | XML_SCHEMAS_ELEM_DEFAULT | XML_SCHEMAS_ELEM_DEFAULT | XML_SCHEMAS_ELEM_DEFAULT |

---

```
#define XML_SCHEMAS_ELEM_DEFAULT 1 << 2
```

##### Discussion

XML_SCHEMAS_ELEM_DEFAULT:

the element has a default value

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ELEM_FINAL_ABSENT | XML_SCHEMAS_ELEM_FINAL_ABSENT | XML_SCHEMAS_ELEM_FINAL_ABSENT | XML_SCHEMAS_ELEM_FINAL_ABSENT | XML_SCHEMAS_ELEM_FINAL_ABSENT |

---

```
#define XML_SCHEMAS_ELEM_FINAL_ABSENT 1 << 14
```

##### Discussion

XML_SCHEMAS_ELEM_FINAL_ABSENT:

substitution group exclusions are absent

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ELEM_FINAL_EXTENSION | XML_SCHEMAS_ELEM_FINAL_EXTENSION | XML_SCHEMAS_ELEM_FINAL_EXTENSION | XML_SCHEMAS_ELEM_FINAL_EXTENSION | XML_SCHEMAS_ELEM_FINAL_EXTENSION |

---

```
#define XML_SCHEMAS_ELEM_FINAL_EXTENSION 1 << 15
```

##### Discussion

XML_SCHEMAS_ELEM_BLOCK_EXTENSION:

substitution group exclusions: "extension"

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ELEM_FINAL_RESTRICTION | XML_SCHEMAS_ELEM_FINAL_RESTRICTION | XML_SCHEMAS_ELEM_FINAL_RESTRICTION | XML_SCHEMAS_ELEM_FINAL_RESTRICTION | XML_SCHEMAS_ELEM_FINAL_RESTRICTION |

---

```
#define XML_SCHEMAS_ELEM_FINAL_RESTRICTION 1 << 16
```

##### Discussion

XML_SCHEMAS_ELEM_BLOCK_RESTRICTION:

substitution group exclusions: "restriction"

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ELEM_FIXED | XML_SCHEMAS_ELEM_FIXED | XML_SCHEMAS_ELEM_FIXED | XML_SCHEMAS_ELEM_FIXED | XML_SCHEMAS_ELEM_FIXED |

---

```
#define XML_SCHEMAS_ELEM_FIXED 1 << 3
```

##### Discussion

XML_SCHEMAS_ELEM_FIXED:

the element has a fixed value

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ELEM_GLOBAL | XML_SCHEMAS_ELEM_GLOBAL | XML_SCHEMAS_ELEM_GLOBAL | XML_SCHEMAS_ELEM_GLOBAL | XML_SCHEMAS_ELEM_GLOBAL |

---

```
#define XML_SCHEMAS_ELEM_GLOBAL 1 << 1
```

##### Discussion

XML_SCHEMAS_ELEM_GLOBAL:

the element is global

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ELEM_INTERNAL_RESOLVED | XML_SCHEMAS_ELEM_INTERNAL_RESOLVED | XML_SCHEMAS_ELEM_INTERNAL_RESOLVED | XML_SCHEMAS_ELEM_INTERNAL_RESOLVED | XML_SCHEMAS_ELEM_INTERNAL_RESOLVED |

---

```
#define XML_SCHEMAS_ELEM_INTERNAL_RESOLVED 1 << 8
```

##### Discussion

XML_SCHEMAS_ELEM_INTERNAL_RESOLVED

this is set when "type", "ref", "substitutionGroup"
references have been resolved.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ELEM_NILLABLE | XML_SCHEMAS_ELEM_NILLABLE | XML_SCHEMAS_ELEM_NILLABLE | XML_SCHEMAS_ELEM_NILLABLE | XML_SCHEMAS_ELEM_NILLABLE |

---

```
#define XML_SCHEMAS_ELEM_NILLABLE 1 << 0
```

##### Discussion

XML_SCHEMAS_ELEM_NILLABLE:

the element is nillable

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ELEM_NSDEFAULT | XML_SCHEMAS_ELEM_NSDEFAULT | XML_SCHEMAS_ELEM_NSDEFAULT | XML_SCHEMAS_ELEM_NSDEFAULT | XML_SCHEMAS_ELEM_NSDEFAULT |

---

```
#define XML_SCHEMAS_ELEM_NSDEFAULT 1 << 7
```

##### Discussion

XML_SCHEMAS_ELEM_NSDEFAULT:

allow elements in no namespace
Obsolete, not used anymore.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ELEM_REF | XML_SCHEMAS_ELEM_REF | XML_SCHEMAS_ELEM_REF | XML_SCHEMAS_ELEM_REF | XML_SCHEMAS_ELEM_REF |

---

```
#define XML_SCHEMAS_ELEM_REF 1 << 6
```

##### Discussion

XML_SCHEMAS_ELEM_REF:

the element is a reference to a type

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_ELEM_TOPLEVEL | XML_SCHEMAS_ELEM_TOPLEVEL | XML_SCHEMAS_ELEM_TOPLEVEL | XML_SCHEMAS_ELEM_TOPLEVEL | XML_SCHEMAS_ELEM_TOPLEVEL |

---

```
#define XML_SCHEMAS_ELEM_TOPLEVEL 1 << 5
```

##### Discussion

XML_SCHEMAS_ELEM_TOPLEVEL:

the element is top level
obsolete: use XML_SCHEMAS_ELEM_GLOBAL instead

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_FINAL_DEFAULT_EXTENSION | XML_SCHEMAS_FINAL_DEFAULT_EXTENSION | XML_SCHEMAS_FINAL_DEFAULT_EXTENSION | XML_SCHEMAS_FINAL_DEFAULT_EXTENSION | XML_SCHEMAS_FINAL_DEFAULT_EXTENSION |

---

```
#define XML_SCHEMAS_FINAL_DEFAULT_EXTENSION 1 << 2
```

##### Discussion

XML_SCHEMAS_FINAL_DEFAULT_EXTENSION:

the schema has "extension" in the set of finalDefault.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_FINAL_DEFAULT_LIST | XML_SCHEMAS_FINAL_DEFAULT_LIST | XML_SCHEMAS_FINAL_DEFAULT_LIST | XML_SCHEMAS_FINAL_DEFAULT_LIST | XML_SCHEMAS_FINAL_DEFAULT_LIST |

---

```
#define XML_SCHEMAS_FINAL_DEFAULT_LIST 1 << 4
```

##### Discussion

XML_SCHEMAS_FINAL_DEFAULT_LIST:

the cshema has "list" in the set of finalDefault.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_FINAL_DEFAULT_RESTRICTION | XML_SCHEMAS_FINAL_DEFAULT_RESTRICTION | XML_SCHEMAS_FINAL_DEFAULT_RESTRICTION | XML_SCHEMAS_FINAL_DEFAULT_RESTRICTION | XML_SCHEMAS_FINAL_DEFAULT_RESTRICTION |

---

```
#define XML_SCHEMAS_FINAL_DEFAULT_RESTRICTION 1 << 3
```

##### Discussion

XML_SCHEMAS_FINAL_DEFAULT_RESTRICTION:

the schema has "restriction" in the set of finalDefault.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_FINAL_DEFAULT_UNION | XML_SCHEMAS_FINAL_DEFAULT_UNION | XML_SCHEMAS_FINAL_DEFAULT_UNION | XML_SCHEMAS_FINAL_DEFAULT_UNION | XML_SCHEMAS_FINAL_DEFAULT_UNION |

---

```
#define XML_SCHEMAS_FINAL_DEFAULT_UNION 1 << 5
```

##### Discussion

XML_SCHEMAS_FINAL_DEFAULT_UNION:

the schema has "union" in the set of finalDefault.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_INCLUDING_CONVERT_NS | XML_SCHEMAS_INCLUDING_CONVERT_NS | XML_SCHEMAS_INCLUDING_CONVERT_NS | XML_SCHEMAS_INCLUDING_CONVERT_NS | XML_SCHEMAS_INCLUDING_CONVERT_NS |

---

```
#define XML_SCHEMAS_INCLUDING_CONVERT_NS 1 << 9
```

##### Discussion

XML_SCHEMAS_INCLUDING_CONVERT_NS:

the schema is currently including an other schema with
no target namespace.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_QUALIF_ATTR | XML_SCHEMAS_QUALIF_ATTR | XML_SCHEMAS_QUALIF_ATTR | XML_SCHEMAS_QUALIF_ATTR | XML_SCHEMAS_QUALIF_ATTR |

---

```
#define XML_SCHEMAS_QUALIF_ATTR 1 << 1
```

##### Discussion

XML_SCHEMAS_QUALIF_ATTR:

the schema requires qualified attributes

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_QUALIF_ELEM | XML_SCHEMAS_QUALIF_ELEM | XML_SCHEMAS_QUALIF_ELEM | XML_SCHEMAS_QUALIF_ELEM | XML_SCHEMAS_QUALIF_ELEM |

---

```
#define XML_SCHEMAS_QUALIF_ELEM 1 << 0
```

##### Discussion

XML_SCHEMAS_QUALIF_ELEM:

the schema requires qualified elements

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_TYPE_ABSTRACT | XML_SCHEMAS_TYPE_ABSTRACT | XML_SCHEMAS_TYPE_ABSTRACT | XML_SCHEMAS_TYPE_ABSTRACT | XML_SCHEMAS_TYPE_ABSTRACT |

---

```
#define XML_SCHEMAS_TYPE_ABSTRACT 1 << 20
```

##### Discussion

XML_SCHEMAS_TYPE_ABSTRACT:

the simple/complexType is abstract.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_TYPE_BLOCK_DEFAULT | XML_SCHEMAS_TYPE_BLOCK_DEFAULT | XML_SCHEMAS_TYPE_BLOCK_DEFAULT | XML_SCHEMAS_TYPE_BLOCK_DEFAULT | XML_SCHEMAS_TYPE_BLOCK_DEFAULT |

---

```
#define XML_SCHEMAS_TYPE_BLOCK_DEFAULT 1 << 17
```

##### Discussion

XML_SCHEMAS_TYPE_BLOCK_DEFAULT:

the complexType did not specify 'block' so use the default of the
 item.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_TYPE_BLOCK_EXTENSION | XML_SCHEMAS_TYPE_BLOCK_EXTENSION | XML_SCHEMAS_TYPE_BLOCK_EXTENSION | XML_SCHEMAS_TYPE_BLOCK_EXTENSION | XML_SCHEMAS_TYPE_BLOCK_EXTENSION |

---

```
#define XML_SCHEMAS_TYPE_BLOCK_EXTENSION 1 << 18
```

##### Discussion

XML_SCHEMAS_TYPE_BLOCK_EXTENSION:

the complexType has a 'block' of "extension".

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_TYPE_BLOCK_RESTRICTION | XML_SCHEMAS_TYPE_BLOCK_RESTRICTION | XML_SCHEMAS_TYPE_BLOCK_RESTRICTION | XML_SCHEMAS_TYPE_BLOCK_RESTRICTION | XML_SCHEMAS_TYPE_BLOCK_RESTRICTION |

---

```
#define XML_SCHEMAS_TYPE_BLOCK_RESTRICTION 1 << 19
```

##### Discussion

XML_SCHEMAS_TYPE_FINAL_RESTRICTION:

the complexType has a 'block' of "restriction".

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_TYPE_BUILTIN_PRIMITIVE | XML_SCHEMAS_TYPE_BUILTIN_PRIMITIVE | XML_SCHEMAS_TYPE_BUILTIN_PRIMITIVE | XML_SCHEMAS_TYPE_BUILTIN_PRIMITIVE | XML_SCHEMAS_TYPE_BUILTIN_PRIMITIVE |

---

```
#define XML_SCHEMAS_TYPE_BUILTIN_PRIMITIVE 1 << 14
```

##### Discussion

XML_SCHEMAS_TYPE_FINAL_UNION:

the simpleType has a final of "union".

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_TYPE_DERIVATION_METHOD_EXTENSION | XML_SCHEMAS_TYPE_DERIVATION_METHOD_EXTENSION | XML_SCHEMAS_TYPE_DERIVATION_METHOD_EXTENSION | XML_SCHEMAS_TYPE_DERIVATION_METHOD_EXTENSION | XML_SCHEMAS_TYPE_DERIVATION_METHOD_EXTENSION |

---

```
#define XML_SCHEMAS_TYPE_DERIVATION_METHOD_EXTENSION 1 << 1
```

##### Discussion

XML_SCHEMAS_TYPE_DERIVATION_METHOD_EXTENSION:

the simple or complex type has a derivation method of "extension".

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_TYPE_DERIVATION_METHOD_RESTRICTION | XML_SCHEMAS_TYPE_DERIVATION_METHOD_RESTRICTION | XML_SCHEMAS_TYPE_DERIVATION_METHOD_RESTRICTION | XML_SCHEMAS_TYPE_DERIVATION_METHOD_RESTRICTION | XML_SCHEMAS_TYPE_DERIVATION_METHOD_RESTRICTION |

---

```
#define XML_SCHEMAS_TYPE_DERIVATION_METHOD_RESTRICTION 1 << 2
```

##### Discussion

XML_SCHEMAS_TYPE_DERIVATION_METHOD_RESTRICTION:

the simple or complex type has a derivation method of "restriction".

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_TYPE_FINAL_DEFAULT | XML_SCHEMAS_TYPE_FINAL_DEFAULT | XML_SCHEMAS_TYPE_FINAL_DEFAULT | XML_SCHEMAS_TYPE_FINAL_DEFAULT | XML_SCHEMAS_TYPE_FINAL_DEFAULT |

---

```
#define XML_SCHEMAS_TYPE_FINAL_DEFAULT 1 << 13
```

##### Discussion

XML_SCHEMAS_TYPE_FINAL_UNION:

the simpleType has a final of "union".

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_TYPE_FINAL_EXTENSION | XML_SCHEMAS_TYPE_FINAL_EXTENSION | XML_SCHEMAS_TYPE_FINAL_EXTENSION | XML_SCHEMAS_TYPE_FINAL_EXTENSION | XML_SCHEMAS_TYPE_FINAL_EXTENSION |

---

```
#define XML_SCHEMAS_TYPE_FINAL_EXTENSION 1 << 9
```

##### Discussion

XML_SCHEMAS_TYPE_FINAL_EXTENSION:

the complexType has a final of "extension".

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_TYPE_FINAL_LIST | XML_SCHEMAS_TYPE_FINAL_LIST | XML_SCHEMAS_TYPE_FINAL_LIST | XML_SCHEMAS_TYPE_FINAL_LIST | XML_SCHEMAS_TYPE_FINAL_LIST |

---

```
#define XML_SCHEMAS_TYPE_FINAL_LIST 1 << 11
```

##### Discussion

XML_SCHEMAS_TYPE_FINAL_LIST:

the simpleType has a final of "list".

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_TYPE_FINAL_RESTRICTION | XML_SCHEMAS_TYPE_FINAL_RESTRICTION | XML_SCHEMAS_TYPE_FINAL_RESTRICTION | XML_SCHEMAS_TYPE_FINAL_RESTRICTION | XML_SCHEMAS_TYPE_FINAL_RESTRICTION |

---

```
#define XML_SCHEMAS_TYPE_FINAL_RESTRICTION 1 << 10
```

##### Discussion

XML_SCHEMAS_TYPE_FINAL_RESTRICTION:

the simpleType/complexType has a final of "restriction".

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_TYPE_FINAL_UNION | XML_SCHEMAS_TYPE_FINAL_UNION | XML_SCHEMAS_TYPE_FINAL_UNION | XML_SCHEMAS_TYPE_FINAL_UNION | XML_SCHEMAS_TYPE_FINAL_UNION |

---

```
#define XML_SCHEMAS_TYPE_FINAL_UNION 1 << 12
```

##### Discussion

XML_SCHEMAS_TYPE_FINAL_UNION:

the simpleType has a final of "union".

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_TYPE_GLOBAL | XML_SCHEMAS_TYPE_GLOBAL | XML_SCHEMAS_TYPE_GLOBAL | XML_SCHEMAS_TYPE_GLOBAL | XML_SCHEMAS_TYPE_GLOBAL |

---

```
#define XML_SCHEMAS_TYPE_GLOBAL 1 << 3
```

##### Discussion

XML_SCHEMAS_TYPE_GLOBAL:

the type is global

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_TYPE_MARKED | XML_SCHEMAS_TYPE_MARKED | XML_SCHEMAS_TYPE_MARKED | XML_SCHEMAS_TYPE_MARKED | XML_SCHEMAS_TYPE_MARKED |

---

```
#define XML_SCHEMAS_TYPE_MARKED 1 << 16
```

##### Discussion

XML_SCHEMAS_TYPE_MARKED

Marks the item as marked; used for circular checks.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_TYPE_MIXED | XML_SCHEMAS_TYPE_MIXED | XML_SCHEMAS_TYPE_MIXED | XML_SCHEMAS_TYPE_MIXED | XML_SCHEMAS_TYPE_MIXED |

---

```
#define XML_SCHEMAS_TYPE_MIXED 1 << 0
```

##### Discussion

XML_SCHEMAS_TYPE_MIXED:

the element content type is mixed

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_TYPE_OWNED_ATTR_WILDCARD | XML_SCHEMAS_TYPE_OWNED_ATTR_WILDCARD | XML_SCHEMAS_TYPE_OWNED_ATTR_WILDCARD | XML_SCHEMAS_TYPE_OWNED_ATTR_WILDCARD | XML_SCHEMAS_TYPE_OWNED_ATTR_WILDCARD |

---

```
#define XML_SCHEMAS_TYPE_OWNED_ATTR_WILDCARD 1 << 4
```

##### Discussion

XML_SCHEMAS_TYPE_OWNED_ATTR_WILDCARD:

the complexType owns an attribute wildcard, i.e.
it can be freed by the complexType

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_TYPE_VARIETY_ABSENT | XML_SCHEMAS_TYPE_VARIETY_ABSENT | XML_SCHEMAS_TYPE_VARIETY_ABSENT | XML_SCHEMAS_TYPE_VARIETY_ABSENT | XML_SCHEMAS_TYPE_VARIETY_ABSENT |

---

```
#define XML_SCHEMAS_TYPE_VARIETY_ABSENT 1 << 5
```

##### Discussion

XML_SCHEMAS_TYPE_VARIETY_ABSENT:

the simpleType has a variety of "absent".

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_TYPE_VARIETY_ATOMIC | XML_SCHEMAS_TYPE_VARIETY_ATOMIC | XML_SCHEMAS_TYPE_VARIETY_ATOMIC | XML_SCHEMAS_TYPE_VARIETY_ATOMIC | XML_SCHEMAS_TYPE_VARIETY_ATOMIC |

---

```
#define XML_SCHEMAS_TYPE_VARIETY_ATOMIC 1 << 8
```

##### Discussion

XML_SCHEMAS_TYPE_VARIETY_ATOMIC:

the simpleType has a variety of "union".

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_TYPE_VARIETY_LIST | XML_SCHEMAS_TYPE_VARIETY_LIST | XML_SCHEMAS_TYPE_VARIETY_LIST | XML_SCHEMAS_TYPE_VARIETY_LIST | XML_SCHEMAS_TYPE_VARIETY_LIST |

---

```
#define XML_SCHEMAS_TYPE_VARIETY_LIST 1 << 6
```

##### Discussion

XML_SCHEMAS_TYPE_VARIETY_LIST:

the simpleType has a variety of "list".

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_TYPE_VARIETY_UNION | XML_SCHEMAS_TYPE_VARIETY_UNION | XML_SCHEMAS_TYPE_VARIETY_UNION | XML_SCHEMAS_TYPE_VARIETY_UNION | XML_SCHEMAS_TYPE_VARIETY_UNION |

---

```
#define XML_SCHEMAS_TYPE_VARIETY_UNION 1 << 7
```

##### Discussion

XML_SCHEMAS_TYPE_VARIETY_UNION:

the simpleType has a variety of "union".

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| XML_SCHEMAS_WILDCARD_COMPLETE | XML_SCHEMAS_WILDCARD_COMPLETE | XML_SCHEMAS_WILDCARD_COMPLETE | XML_SCHEMAS_WILDCARD_COMPLETE | XML_SCHEMAS_WILDCARD_COMPLETE |

---

```
#define XML_SCHEMAS_WILDCARD_COMPLETE 1 << 0
```

##### Discussion

XML_SCHEMAS_WILDCARD_COMPLETE:

If the wildcard is complete.

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

Last Updated: 2006-06-20
