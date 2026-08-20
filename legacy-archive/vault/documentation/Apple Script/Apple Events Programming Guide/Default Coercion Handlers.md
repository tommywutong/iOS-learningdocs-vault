---
title: Apple Events Programming Guide
apple_id: TP40001449
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleEvents/appendix3_aepg/appendix3_aepg.html
archived_at: '2026-07-15T05:19:25.578711Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Apple Events Programming Guide](Introduction%20to%20Apple%20Events%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Selected%20Apple%20Event%20Constants.md)

# Default Coercion Handlers

This appendix lists the type conversions performed by the default coercion handlers provided by the Mac OS. These handlers may be implemented by the Apple Event Manager, the Open Scripting framework, or other frameworks.

Support for the following coercions was added in Mac OS X version 10.4:

- Between these types:

  `typeStyledText`, `typeUnicodeText`, `typeUTF8Text`, and `typeUTF16ExternalRepresentation`

  and these types:

  `typeType`, `typeEnumerated`, and the numeric types `typeSInt16`, `typeSInt32`, `typeUInt32`, `typeSInt64`, `typeIEEE32BitFloatingPoint`, `typeIEEE64BitFloatingPoint`, and `typeExtended`.

  See table Table C-1 for a mapping between the preferred and non-preferred numeric constant names.
- From `typeChar` to `typeStyledText`.

Table C-1 shows some older, non-preferred numeric constant names and their preferred equivalents. To find available coercions for a non-preferred name from Table C-1, look up its equivalent preferred name in Table C-2.

__Table C-1__  Older, non-preferred numeric types and their preferred types

| Non-preferred numeric constant name | Preferred numeric constant name |
| `typeSMInt`, `typeShortInteger` | `typeSInt16` |
| `typeInteger`, `typeLongInteger` | `typeSInt32` |
| `typeMagnitude` | `typeUInt32` |
| `typeComp` | `typeSInt64` |
| `typeSMFloat`, `typeShortFloat` | `typeIEEE32BitFloatingPoint` |
| `typeFloat`, `typeLongFloat` | `typeIEEE64BitFloatingPoint` |

Table C-2 lists the default coercions handled by the Apple Event Manager.

__Table C-2__  Default coercions provided by the Apple Event Manager

| Coerce from descriptor type | To descriptor type | Comment |
| `typeChar`  `typeStyledText`  `typeUnicodeText`  `typeUTF8Text`  `typeUTF16ExternalRepresentation` | `typeSInt16`  `typeSInt32`  `typeSInt64`  `typeIEEE32BitFloatingPoint`  `typeIEEE64BitFloatingPoint`  `typeExtended` | Any string that is a valid representation of a number can be coerced into an equivalent numeric value. |
| `typeSInt16`  `typeSInt32`  `typeSInt64`  `typeIEEE32BitFloatingPoint`  `typeIEEE64BitFloatingPoint`  `typeExtended` | `typeChar`  `typeStyledText`  `typeUnicodeText`  `typeUTF8Text`  `typeUTF16ExternalRepresentation` | Any numeric descriptor type can be coerced into the equivalent text string. |
| `typeSInt16`  `typeSInt32`  `typeSInt64`  `typeIEEE32BitFloatingPoint`  `typeIEEE64BitFloatingPoint`  `typeExtended` | `typeSInt16`  `typeSInt32`  `typeSInt64`  `typeIEEE32BitFloatingPoint`  `typeIEEE64BitFloatingPoint`  `typeExtended` | Any numeric descriptor type can be coerced into any other numeric descriptor type. |
| `typeChar`  `typeIntlText`  `typeStyledText`  `typeUnicodeText`  `typeUTF8Text`  `typeUTF16ExternalRepresentation` | `typeChar`  `typeIntlText`  `typeStyledText`  `typeUnicodeText`  `typeUTF8Text`  `typeUTF16ExternalRepresentation` | If the destination encoding cannot represent a character in the source text, the result is undefined. |
| `typeChar`  `typeStyledText`  `typeUnicodeText`  `typeUTF8Text`  `typeUTF16ExternalRepresentation` | `typeType`  `typeEnumerated`  `typeKeyword`  `typeProperty` | Any four-character string can be coerced to one of these descriptor types. |
| `typeEnumerated`  `typeKeyword`  `typeProperty`  `typeType` | `typeChar`  `typeStyledText`  `typeUnicodeText`  `typeUTF8Text`  `typeUTF16ExternalRepresentation` | Any of these descriptor types can be coerced to the equivalent text string. |
| `typeIntlText` | `typeChar`  `typeStyledText`  `typeUnicodeText`  `typeUTF8Text`  `typeUTF16ExternalRepresentation` | The result contains text only, without the script code or language code from the original descriptor. |
| `typeTrue` | `typeBoolean` | The result is the Boolean value `true`. |
| `typeFalse` | `typeBoolean` | The result is the Boolean value `false`. |
| `typeEnumerated` | `typeBoolean` | The enumerated value `'true'` becomes the Boolean value true. The enumerated value `'fals'` becomes the Boolean value false. |
| `typeBoolean` | `typeEnumerated` | The Boolean value `false` becomes the enumerated value `'fals'`. The Boolean value `true` becomes the enumerated value `'true'`. |
| `typeSInt16` | `typeBoolean` | A value of 1 becomes the Boolean value `true`. A value of 0 becomes the Boolean value `false`. |
| `typeBoolean` | `typeSInt16` | A value of `false` becomes 0. A value of `true` becomes 1. |
| `typeAlias` | `typeFSS` | An alias is coerced into a file system specification. Not recommended—use `typeFSRef` instead. |
| `typeAlias` | `typeFSRef` | An alias is coerced into a file system reference. |
| `typeAppleEvent` | `typeAppParameters` | An Apple event is coerced into a list of application parameters for the `LaunchParamBlockRec` parameter block. |
| any descriptor type | `typeAEList` | A descriptor is coerced into a descriptor list containing a single item. |
| `typeAEList` | type of list item | A descriptor list containing a single descriptor is coerced into a descriptor. |

[Next](Document%20Revision%20History.md)[Previous](Selected%20Apple%20Event%20Constants.md)

