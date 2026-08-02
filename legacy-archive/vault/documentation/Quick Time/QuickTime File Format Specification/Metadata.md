---
title: QuickTime File Format Specification
apple_id: TP40000939
resource_type: Guide
platform: macOS
topic: Data Management
technology: QuickTime
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/QTFF/Metadata/Metadata.html
archived_at: '2026-07-27T06:57:06.087153Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [QuickTime File Format Specification](Introduction%20to%20QuickTime%20File%20Format%20Specification.md)


[Next](Media%20Data%20Atom%20Types.md)[Previous](Movie%20Atoms.md)

# Metadata

This chapter describes how to store metadata in QuickTime Movie files. It also defines keys for some common metadata types as examples of how to employ the metadata capabilities in the QuickTime file format.

## Overview

Metadata can be defined as useful information related to media. This section describes a method of associating metadata with media in a QuickTime file that is extensible and allows for language and country tagging. In addition, it provides a means to store the type of the metadata and associate a name with metadata. This method of storing metadata is supported in both QuickTime 7 and QuickTime X.

This metadata format uses a key–value pair for each type of metadata being stored. Standard keys, with specific formats for the values they indicate, have been defined. See [QuickTime Metadata Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknltgny) for details.

__Note:__ The QuickTime file format also defines user data which, in some limited cases, can be used to store metadata. The method of storing metadata defined in this section provides an extensible and flexible design for handling a wide variety of metadata types.

### Data Type

The storage type of metadata items is defined via an enumerated list of data types, defined statically; an example might be “plain Unicode text”. See the [Well-Known Types](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknltgna) table for details of the standard, defined data types.

### Meaning or Purpose

The meaning of a metadata item identifies what it represents: a copyright notice, the performer’s name, and so on. It uses an extensible namespace allowing for meanings or keys to be added, and then referenced, from metadata items. These keys may be four-character codes, names in reverse-address format (such as “com.apple.quicktime.windowlocation”) or any other key format including native formats from external metadata standards. A key is tagged with its namespace allowing for extension in the future. It is recommended that reverse-address format be used in the general case: this provides an extensible syntax for vendor data or for other organizations or standards bodies.

### Data Location

Metadata is stored immediately in the corresponding atom structures, by value.

### Localization

A metadata item can be identified as specific to a country or set of countries, to a language or set of languages, or to some combination of languages and countries. This identification allows for a default value (suitable for any language or country not explicitly called out), a single value, or a list of values.

### Storage Location in a QuickTime File

Within a QuickTime file, metadata can be stored within a movie atom (`‘moov’`), a track atom (`‘trak’`) or a media atom (`‘mdia’`). Only one metadata atom is allowed for each location. If there is user data and metadata stored in the same location, and both declare the same information, for example, declare a copyright notice, the metadata takes precedence.

## Metadata Structure

The container for metadata is an atom of type `‘meta’`. The metadata atom must contain the following subatoms: metadata handler atom (`‘hdlr’`), metadata item keys atom (`‘keys’`), and metadata item list atom (`‘ilst’`). Other optional atoms that may be contained in a metadata atom include the country list atom (`‘ctry’`), language list atom (`‘lang’`) and free space atom (`‘free’`). The country list and language list atoms can be used to store localized data in an efficient manner. The free space atom may be used to reserve space in a metadata atom for later additions to it, or to zero out bytes within a metadata atom after editing and removing elements from it. The free space atom may not occur within any other subatom contained in the metadata atom.

### Metadata Atom

The metadata atom is the container for carrying metadata.

[Figure 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknlts) shows a sample layout for this atom.

__Figure 3-1__  Sample of a metadata atom and subatoms

（原归档配图获取待重试：`metadata_atom.jpg`）

### Metadata Handler Atom

The metadata handler atom is a full atom with an atom type of `‘hdlr’`. It defines the structure used for all types of metadata stored within the metadata atom.

The layout of the metadata handler atom is defined:

**Size**
: A 32-bit unsigned integer that indicates the size in bytes of the atom structure

**Type**
: A 32-bit unsigned integer value set to `'hdlr'`

**Version**
: One byte that is set to 0

**Flags**
: Three bytes that are set to 0

**Predefined**
: A 32-bit integer that is set to 0

**Handler type**
: A 32-bit integer that indicates the structure used in the metadata atom, set to `‘mdta’`

**Reserved**
: An array of 3 const unsigned 32-bit integers set to 0

**Name**
: The name is a NULL-terminated string in UTF-8 characters which gives a human-readable name for a metadata type, for debugging and inspection purposes. The string may be empty or a single byte containing 0.

__Note:__ A reader parsing a metadata atom should confirm the handler type in the metadata handler atom is `‘mdta’` before interpreting any other structures in the metadata atom according to the specification presented here. If the handler type is not `‘mdta’`, the interpretation is defined by another specification.

### Metadata Header Atom

The metadata format optionally assigns unique identifiers to metadata items for such purposes as defining stable identifiers for external references into the set of metadata items. This is accomplished by including an item information atom in added metadata item atoms contained by the metadata item list atom. Such unique identifiers must be guaranteed to be unique.

To make the assignment of unique item identifiers more efficient, the metadata atom may contain a metadata header atom holding the integer value for the next unique item identifier to assign stored in the nextItemID field. In general it holds a value one greater than the largest identifier used so far.

__Important:__ The metadata header atom must exist if there are metadata item atoms containing an item information atom indicating the item’s unique ID.

Upon assigning the identifier to a metadata item, if the value of the nextItemID field is less than 0xFFFFFFFF, it should be incremented to the next unused value. If the value of nextItemID is equal to 0xFFFFFFFF, it should not be changed: in that case, a search for an unused item identifier value in the range from 0 to 0xFFFFFFFF is needed for all additions.

The metadata header atom is a full atom with an atom type of `‘mhdr’`. It contains the following fields:

**Size**
: A 32-bit unsigned integer that indicates the size in bytes of the atom structure

**Type**
: A 32-bit unsigned integer value set to `'mdhr'`

**Version**
: One byte that is set to 0.

**Flags**
: Three bytes that are set to 0.

**nextItemID**
: A 32-bit unsigned integer indicating the value to use for the item ID of the next item created or assigned an item ID. If the value is all ones, it indicates that future additions will require a search for an unused item ID.

__Note:__ If the last metadata item with an item information atom is removed and value of nextItemID is 0xFFFFFFFF, an implementation may reset the metadata header atom’s nextItemID value to 0 so that new assignments are again efficient (that is, they do not require a search for unused identifiers).

## Extensibility

In order to allow metadata to be rewritten easily and without the need to rewrite the entire QuickTime movie file, free space atoms may occur anywhere in the definition of the metadata atom between the positions of other atoms contained by the metadata atom. Free space atoms may not be inserted between items in the metadata item list atom or within atoms in the metadata item list atom. This restriction on free space atom definition avoids the risk of confusing a free space atom with a meaning of a `‘free’` identifier or a value atom of type `‘free’` defined in the context of the metadata atom structure.

Similarly, UUID atoms for specific extensions may be placed in any position where a succession of atoms is permitted. Note that UUID atoms should not be created for atoms already defined using four-character codes.

Unrecognized atoms (that is, those atoms whose types not defined in the context of the metadata atom structure and are contained within the metadata item list atom) are ignored.

## Localization List Sets

When metadata items have individual values associated with more than one country or more than one language, a country list atom and/or language list atom are required. Alternatively, if all values are associated with zero or one country, no country list atom is required, and if all values are associated with zero or one language, no language list atom is required.

## Country List Atom

When one or more items must be identified as being suitable for more than one country, each list of countries is stored in this otherwise optional atom. The country list atom is a full atom with an atom type of `‘ctry’`.

Each list starts with a two-byte count of the number of items in the list, and then each ISO 3166 code representing countries in the list.

The atom consists of a count of the number of lists, expressed as a 32-bit integer, and then these lists, appended end-to-end. The country list atom contains the following fields:

**Size**
: A 32-bit unsigned integer that indicates the size in bytes of the atom structure

**Type**
: A 32-bit unsigned integer value set to `'ctry'`

**Version**
: One byte that is set to 0.

**Flags**
: Three bytes that are set to 0.

**Entry_count**
: A 32-bit integer indicating the number of Country arrays to follow in this atom.

**Country_count**
: A 16-bit integer indicating the number of Countries in the array.

**Country[Country_count]**
: An array of 16-bit integers, defined according to the ISO 3166 definition of country codes.

Note that:

- Indexes into the country list atom are 1-based.
- Zero (0) is reserved and never used as an index.
- Currently, there is a limit of 255 countries that may be recorded in a country list atom.

An example country list atom consisting of two country lists with two and three countries, respectively, is shown in [Table 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknltina).

__Table 3-1__  Example country list atom

| Field Size | Field | Field Contents | Comment |
| 32-bit | atom_size | 26 | Size of this country list atom in bytes. |
| 32-bit | atom_type | 'ctry’ |  |
| 32-bit | entry_count | 2 | Number of country lists. |
| 16-bit | country_count | 2 | Number of countries in country list 1. |
| 16-bit | country | 'US’ |  |
| 16-bit | country | 'UK’ |  |
| 16-bit | country_count | 3 | Number of countries in country list 2. |
| 16-bit | country | 'JP’ |  |
| 16-bit | country | 'US’ |  |
| 16-bit | country | 'FR’ |  |

## Language List Atom

When one or more items must be identified as being suitable for more than one language, each list of languages is stored in this otherwise optional atom. The language list atom is a full atom with an atom type of `‘lang’`.

Each list starts with a 2-byte count of the number of items in the list, and then each ISO 639-2/T code, packed into two bytes, according to the ISO Language Code definition in the MP4 specification.

The atom consists of a count of the number of lists, expressed as a 32-bit integer, and then these lists, appended end-to-end. The language list atom contains the following fields:

**Size**
: A 32-bit unsigned integer that indicates the size in bytes of the atom structure

**Type**
: A 32-bit unsigned integer value set to `'lang'`

**Version**
: One byte that is set to 0.

**Flags**
: Three bytes that are set to 0.

**Entry_count**
: A 32-bit integer indicating the number of language arrays to follow in this atom.

**Language_count**
: A 16-bit integer indicating the number of languages in the array.

**Language[Language_count]**
: An array of 16-bit integers, defined according to the ISO 639-2/T definition of language codes.

Note that:

- Indexes into the Language List atom are 1-based.
- Zero (0) is reserved and never used as an index.
- Currently, there is a limit of 255 languages that may be recorded in a Language List atom.

[Table 3-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknltima) shows an example Language List atom consisting of two language lists with three and two languages, respectively.

__Table 3-2__  Example Language List atom

| Field Size | Field | Field Contents | Comment |
| 32-bit | atom_size | 26 | Size of this Language List atom in bytes. |
| 32-bit | atom_type | 'lang’ |  |
| 32-bit | entry_count | 2 | Number of language lists. |
| 16-bit | language_count | 3 | Number of languages in language list 1. |
| 16-bit | language | 5575 | Packed ISO code for ‘eng’ (English) |
| 16-bit | language | 6721 | Packed ISO code for ‘fra’ (French) |
| 16-bit | language | 4277 | Packed ISO code for ‘deu’ (German) |
| 16-bit | language_count | 2 | Number of languages in language list 2. |
| 16-bit | language | 19969 | Packed ISO code for ‘spa’ (Spanish) |
| 16-bit | language | 16882 | Packed ISO code for ‘por’ (Portuguese) |

## Metadata Item Keys Atom

The metadata item keys atom holds a list of the metadata keys that may be present in the metadata atom. This list is indexed starting with 1; 0 is a reserved index value. The metadata item keys atom is a full atom with an atom type of `‘keys’`.

This atom has the following structure:

**Size**
: A 32-bit unsigned integer that indicates the size in bytes of the atom structure

**Type**
: A 32-bit unsigned integer value set to `'keys'`

**Version**
: One byte that is set to 0

**Flags**
: Three bytes that are set to 0

**Entry_count**
: A 32-bit integer indicating the number of key arrays to follow in this atom

**Key_size**
: A 32-bit integer indicating the size of the entire structure containing a key definition. Therefore the key_size = sizeof(key_size) + sizeof(key_namespace) + sizeof(key_value). Since key_size and key_namespace are both 32 bit integers, together they have a size of 8 bytes. Hence, the key_value structure will be equal to key_size - 8.

**Key_namespace**
: A 32-bit integer defining a naming scheme used for metadata keys. Location metadata keys, for example, use the `‘mdta’` key namespace.

**Key_value[Key_size-8]**
: An array of 8-bit integers, each containing the actual name of the metadata key. Keys with the ‘mdta’ namespace use a reverse DNS naming convention. For example, the location metadata coordinates use a metadata key_value of ‘com.apple.quicktime.location.ISO6709’.

Note that:

- Indexes into the metadata item keys atom are 1-based (1…entry_count).
- Zero (0) is reserved and never used as an index.
- The structure of key_value depends upon the key namespace.

[Figure 3-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknltemy) shows a sample layout for this atom.

__Figure 3-2__  A typical metadata item keys atom

（原归档配图获取待重试：`item_keys_atom.jpg`）

[Figure 3-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknltema) shows an example of a metadata item keys atom consisting of three keys: two from one key namespace and a third from another key namespace.

__Figure 3-3__  An example of a metadata item keys atom

（原归档配图获取待重试：`example_item_keys.jpg`）

## Metadata Item List Atom

The metadata item list atom holds a list of actual metadata values that are present in the metadata atom. The metadata items are formatted as a list of items. The metadata item list atom is of type `‘ilst’` and contains a number of metadata items, each of which is an atom.

[Figure 3-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknlteni) shows the connection between keys.

__Figure 3-4__  The metadata item list atom and the item/key Connection

（原归档配图获取待重试：`item_list_atom.jpg`）

## Metadata Item Atom

Each item in the metadata item list atom is identified by its key. The atom type for each metadata item atom should be set equal to the index of the key for the metadata within the item atom, taking this index from the metadata item keys atom. In addition, each metadata item atom contains a [Value Atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknlteny), to hold the value of the metadata item.

The metadata item atom has the following structure:

**Item_info**
: An optional item information atom, see [Item Information Atom (ID and flags)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknltgma)

**Name**
: An optional name atom, defined below.

**Data value atom[]**
: An array of value atoms, defined below.

## Value Atom

The value of the metadata item is expressed as immediate data in a value atom. The value atom starts with two fields: a type indicator, and a locale indicator. Both the type and locale indicators are four bytes long. There may be multiple ‘value’ entries, using different type, country or language codes (see the Data Ordering section below for the required ordering).

The Value atom structure contains the following fields:

**Type**
: A type indicator, defined in [Type Indicator](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknlteoa).

**Locale**
: A locale indicator, defined in [Locale Indicator](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknlteoi).

## Type Indicator

The type indicator is formed of four bytes split between two fields. The first byte indicates the set of types from which the type is drawn. The second through fourth byte forms the second field and its interpretation depends upon the value in the first field.

The indicator byte must have a value of 0, meaning the type is drawn from the well-known set of types. All other values are reserved.

If the type indicator byte is 0, the following 24 bits hold the well-known type. Please refer to the list of Well-Known Types, in the Well-Known Types section below.

## Locale Indicator

The locale indicator is formatted as a four-byte value. It is formed from two two-byte values: a country indicator, and a language indicator. In each case, the two-byte field has the possible values shown in [Table 3-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknltimi).

__Table 3-3__  Country and language indicators

| Value | Meaning |
| 0 | This atom provides the default value of this datum for any locale not explicitly listed. |
| 1 to 255 | The value is an index into the country or language list (the upper byte is 0). |
| otherwise | The value is an ISO 3166 code (for the country code) or a packed ISO 639-2/T code (for the language). |

Note that both ISO 3166 and ISO 639-2/T codes have a nonzero value in their top byte, and so will have a value > 255.

Software applications that read metadata may be customized for a specific set of countries or languages. If a metadata writer does not want to limit a metadata item to a specific set of countries, it should use the reserved value ZZ from ISO 3166 as its country code. Similarly if the metadata writer does not want to limit the user’s language (this is not recommended) it uses the value ‘und’ (undetermined) from the ISO 639-2/T specification.

A software application matches a country code if either (a) the value to be matched to is 0 (default) or (b) the codes are equal. A software application matches to a list of codes if its value is a member of that list. A software application matches to a locale if both country and language match.

[Table 3-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknltimq) shows some example metadata tags.

__Table 3-4__  Example metadata tags

| Country | Language | Meaning |
| 0 | eng | All speakers of English, regardless of country |
| GB | 0 | All people in the United Kingdom, regardless of language |
| CA | fra | French speakers in Canada |
| DE,GB,FR,IT | 0 | People in Germany, France, United Kingdom, and Italy, regardless of language |
| DE,GB,FR,IT | deu,fra | People in Germany, France, United Kingdom, and Italy, who speak German or French |
| 0 | 0 | Default, all speakers in all countries |

To reiterate, if the country_indicator value is in the range 1 to 255, it is interpreted as the 1-based index for a country list in the Country Language atom in the Metadata atom. If the language_indicator value is in the range 1 to 255, it is interpreted as the 1-based index for a language list in the Language List atom in the Metadata atom. Otherwise, the country_indicator or language_indicator is unspecified (0) or holds the immediate value for a single country or language.

## Item Information Atom (ID and flags)

The optional item information atom contains information about the item: item-specific flags and item optional identifier. This ID must be unique within the metadata atom. To simplify assignment of item identifiers, the metadata header atom’s nextItemInfo field can be used as described in [Metadata Header Atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknltcmy).

The item information atom must be present if the item has an assigned ID or has nonzero flags.

No flags are currently defined; they should be set to 0 in this version of the specification.

The item information atom is a full atom with an atom type of `‘itif’`. This atom has the following structure:

**Size**
: A 32-bit unsigned integer that indicates the size in bytes of the atom structure

**Type**
: A 32-bit unsigned integer value set to `'itif'`

**Version**
: One byte that is set to 0.

**Flags**
: Three bytes that are set to 0.

**Item_ID**
: An unsigned 32-bit integer, unique within the container.

## Name

The Name atom is a full atom with an atom type of ‘name’. This atom contains a metadata name formatted as a string of UTF-8 characters, to fill the atom. It is optional. If it is not present, the item is unnamed, and cannot be referred to by name. Names are not user visible; they provide a way to refer to metadata items. The maximum length of a name may be limited in specific environments.

No two metadata items may have the same name.

This atom has the following structure:

**Version**
: One byte that is set to 0.

**Flags**
: Three bytes that are set to 0.

**Name**
: An array of bytes, constituting a UTF-8 string, containing the name.

## Data Atom Structure

The Data atom has an atom type of ‘data’, and contains four bytes each of type and locale indicators, as specified in [Type Indicator](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknlteoa) and [Locale Indicator](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknlteoi), and then the actual value of the metadata, formatted as required by the type.

This atom has the following structure:

**Type Indicator**
: The type indicator, as defined in [Type Indicator](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknlteoa).

**Locale Indicator**
: The locale indicator, as defined in [Locale Indicator](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknlteoi).

**Value**
: An array of bytes containing the value of the metadata.

## Data Ordering

Multiple values for the same tag represent multiple representations of the same information, differing either by language or storage type or by the size or nature of the data. For example, an artist name may be supplied in three ways:

- as a large JPEG of their signature
- as a smaller ‘thumbnail’ JPEG of their signature
- as text

An application may then choose the variation of the the artist name to display based on the size it needs.

Data must be ordered in each item from the most-specific data to the most general. An application may, if it wishes, stop ‘searching’ for a value once it finds a value that it can display (it has an acceptable locale and type).

## Well-Known Types

The basic data-type list is in [Table 3-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknltgni).

__Table 3-5__  Well-known data types

| Code | Type | Comment |
| 0 | reserved | Reserved for use where no type needs to be indicated |
| 1 | UTF-8 | Without any count or NULL terminator |
| 2 | UTF-16 | Also known as UTF-16BE |
| 3 | S/JIS | Deprecated unless it is needed for special Japanese characters |
| 4 | UTF-8 sort | Variant storage of a string for sorting only |
| 5 | UTF-16 sort | Variant storage of a string for sorting only |
| 13 | JPEG | In a JFIF wrapper |
| 14 | PNG | In a PNG wrapper |
| 21 | BE Signed Integer | A big-endian signed integer in 1,2,3 or 4 bytes  __Note:__ This data type is not supported in [Timed Metadata Media](Media%20Data%20Atom%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzugy). Use one of the fixed-size signed integer data types (that is, type codes 65, 66, or 67) instead. |
| 22 | BE Unsigned Integer | A big-endian unsigned integer in 1,2,3 or 4 bytes; size of value determines integer size  __Note:__ This data type is not supported in [Timed Metadata Media](Media%20Data%20Atom%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzugy). Use one of the fixed-size unsigned integer data types (that is, type codes 75, 76, or 77) instead. |
| 23 | BE Float32 | A big-endian 32-bit floating point value (IEEE754) |
| 24 | BE Float64 | A big-endian 64-bit floating point value (IEEE754) |
| 27 | BMP | Windows bitmap format graphics |
| 28 | QuickTime Metadata atom | A block of data having the structure of the Metadata atom defined in this specification |
| 65 | 8-bit Signed Integer | An 8-bit signed integer |
| 66 | BE 16-bit Signed Integer | A big-endian 16-bit signed integer |
| 67 | BE 32-bit Signed Integer | A big-endian 32-bit signed integer |
| 70 | BE PointF32 | A block of data representing a two dimensional (2D) point with 32-bit big-endian floating point x and y coordinates. It has the structure:  `struct { BEFloat32 x; BEFloat32 y; }` |
| 71 | BE DimensionsF32 | A block of data representing 2D dimensions with 32-bit big-endian floating point width and height. It has the structure:  `struct { BEFloat32 width; BEFloat32 height; }` |
| 72 | BE RectF32 | A block of data representing a 2D rectangle with 32-bit big-endian floating point x and y coordinates and a 32-bit big-endian floating point width and height size. It has the structure:  `struct { BEFloat32 x; BEFloat32 y; BEFloat32 width; BEFloat32 height;}`  or the equivalent structure:  `struct { PointF32 origin; DimensionsF32 size; }` |
| 74 | BE 64-bit Signed Integer | A big-endian 64-bit signed integer |
| 75 | 8-bit Unsigned Integer | An 8-bit unsigned integer |
| 76 | BE 16-bit Unsigned Integer | A big-endian 16-bit unsigned integer |
| 77 | BE 32-bit Unsigned Integer | A big-endian 32-bit unsigned integer |
| 78 | BE 64-bit Unsigned Integer | A big-endian 64-bit unsigned integer |
| 79 | AffineTransformF64 | A block of data representing a 3x3 transformation matrix. It has the structure:  `struct { BEFloat64 matrix[3][3]; }` |

The sorting variant of text is used for languages in which sorting is not evident from the written form (for example, some forms of Asian languages). In these cases, the sorting can only be performed by a human who can identify the actual words by understanding the context. For these languages, an alternative form of the same information can be stored using a different representation of the same text which can be machine sorted. This alternative representation is still sorted according to the sort rules of the language in question, as defined for the text system in use (for example, Unicode). In general, a simple lexical sorting which compares the values of the characters alone is not sufficient.

## Location Metadata

Many systems have the ability to detect or establish their position in a coordinate reference system. The specification “ISO 6709:2008 Standard representation of geographic point location by coordinates” describes one way of storing such information. One of the common systems is the Global Positioning System (GPS) developed by the US Department of Defense. Other systems include the ability of some cellular telephone systems to triangulate the position of cell-phones, and the possibility that IEEE 802.11 Wireless Base Stations are tagged with their position (whereupon mobile units that can ‘see’ their signal can establish that they are probably ‘near’ that location).

This support is increasingly common in still and movie cameras, or composite devices (such as camera-phones) that can function as cameras.

Apple has defined a key for storing the location coordinates as metadata, as well as several auxiliary pieces of information about a location. For all the location metadata keys defined in this specification, the Metadata atom handler-type should be ‘mdta’. See the com.apple.quicktime.location.ISO6709 entry in the following table for a description of the main location metadata key, and the additional table describing auxiliary location metadata keys.

## QuickTime Metadata Keys

QuickTime has defined the keys shown in [Table 3-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknltimy) for holding data in a Metadata atom:

__Table 3-6__  Metadata keys

| Key | Key Type | Value Payload | Definition | Example |
| com.apple.quicktime.album | 'mdta’ | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Album or collection name of which the movie content forms a part. | Technical documents performed to blues tunes Volume 1. |
| com.apple.quicktime.artist | 'mdta’ | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Name of the artist who created the movie file content. | Grandma Doe and the Spec Writers. |
| com.apple.quicktime.artwork | 'mdta’ | An representative image for the movie content in a format such as JPEG (value type 13), PNG (value type 14) or BMP (value type 27). This might be album artwork, a movie poster, etc. | A single image that can represent the movie file content. | (a picture of the cover art) |
| com.apple.quicktime.author | 'mdta’ | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Name of the author of the movie file content. | Technical writer (anonymous) |
| com.apple.quicktime.comment | 'mdta’ | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | User entered comment regarding the movie file content. | Great for a laugh. |
| com.apple.quicktime.copyright | 'mdta’ | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Copyright statement for the movie file content. | Copyright © 2012 Grandma Doe |
| com.apple.quicktime.creationdate | 'mdta’ | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | The date the movie file content was created. | 4/21/2012 |
| com.apple.quicktime.description | 'mdta’ | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Description of the movie file content. | This group of engineers takes popular technical documents and does music videos performing them to novel blues tunes they write. |
| com.apple.quicktime.director | 'mdta’ | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Name of the director of the movie content. | Papa Doe |
| com.apple.quicktime.title | 'mdta’ | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | The title of the movie file content. This is typically a single text line. | Technical Writers Do the Blues |
| com.apple.quicktime.genre | 'mdta’ | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Text describing the genre or genres to which the movie content conforms. There is no prescribed vocabulary for names of genres. | Blues |
| com.apple.quicktime.information | 'mdta’ | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Information about the movie file content. | Recorded live on location. |
| com.apple.quicktime.keywords | 'mdta’ | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Keywords associated with the movie file content. | Blues Specifications Group Video Music |
| com.apple.quicktime.location.ISO6709 | 'mdta’ | Defined in ISO 6709:2008. | Geographic point location by coordinates as defined in ISO 6709:2008. | "+27.5916+086.5640+8850/" |
| com.apple.quicktime.producer | 'mdta’ | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Name of producer of movie file content. | Jimmy Doe Junior |
| com.apple.quicktime.publisher | 'mdta’ | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Name of publisher of movie file content. | The Do-Doe Art House, Inc. |
| com.apple.quicktime.software | 'mdta’ | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Name of software used to create the movie file content. | Do-the-Blues v2.3 |
| com.apple.quicktime.year | 'mdta’ | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Year when the movie file or the original content was created or recorded. | 2012 |
| com.apple.quicktime.collection.user | 'mdta’ | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | A name indicating a user-defined collection that includes this movie. | Blues Specification Group |
| com.apple.quicktime.rating.user | 'mdta’ | A BE Float32 (value type 23). The range of this number is 0.0 to 5.0, inclusive. | A number, assigned by the user, that indicates the rating or relative value of the movie. This number can range from 0.0 to 5.0. A value of 0.0 indicates that the user has not rated the movie. | 4.5 |

In addition, QuickTime recommends the auxiliary keys shown in [Table 3-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknltini) for holding additional metadata to be associated with a location.

__Table 3-7__  Auxiliary keys for metadata

| Key | Key Type | Value Payload | Definition | Example |
| com.apple.quicktime.location.name | 'mdta’ | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Name of the location. | “Sweden” or “Grandmother’s house” |
| com.apple.quicktime.location.body | 'mdta’ | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | The astronomical body, for compatibility with the 3GPP format. 'earth' is assumed if not present. | “earth” |
| com.apple.quicktime.location.note | 'mdta’ | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Descriptive comment. | “following a dog” |
| com.apple.quicktime.location.role | 'mdta’ | An unsigned integer (value type 22). | A single byte, binary value containing a value from the set: 0 indicates “shooting location”, 1 indicates “real location”, 2 indicates “fictional location”. Other values are reserved. | 1, for shooting location |
| com.apple.quicktime.location.date | 'mdta’ | Defined in ISO8601:2004. | A date and time, stored using the extended format defined in ISO 8601:2004- Data elements and interchange format. | "2012-02-24T17:56Z" for a date of February 24, 2012, time of 17:56, UTC. |
| com.apple.quicktime.direction.facing | 'mdta’ | A UTF-8 string (value type 1)holding a machine readable direction value, as described below. This should not be tagged with a country or language code. | An indication of the direction the camera is facing during the shot. | “+20.34M/-5.3” for a heading of 20.34º magnetic, looking or going down at 5.3º below the horizontal. |
| com.apple.quicktime.direction.motion | 'mdta’ | A UTF-8 string (value type 1) holding a machine readable direction value, as described below. This should not be tagged with a country or language code. | An indication of the direction the camera is moving during the shot. | “+20.34M/-5.3” for a heading of 20.34º magnetic, looking or going down at 5.3º below the horizontal. |

## Direction Definition

For the metadata keys which define a direction, com.apple.quicktime.direction.facing and com.apple.quicktime.direction.motion, directions are specified as a string consisting of one or two angles, separated by a slash if two occur.  The first is a compass direction, expressed in degrees and decimal degrees, optionally preceded by the characters “+” or “-”, and optionally followed by the character “M”.  The direction is determined as accurately as possible; the nominal due north (zero degrees) is defined as facing along a line of longitude of the location system, unless the angle is followed by the “M” character indicating a magnetic heading. The second is an elevation direction, expressed in degrees and decimal degrees between +90.0 and -90.0, with 0 being horizontal (level), +90.0 being straight up, and -90.0 being straight down (and for these two cases, the compass direction is irrelevant).

[Next](Media%20Data%20Atom%20Types.md)[Previous](Movie%20Atoms.md)
