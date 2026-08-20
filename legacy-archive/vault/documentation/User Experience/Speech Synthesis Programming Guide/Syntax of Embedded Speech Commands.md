---
title: Speech Synthesis Programming Guide
apple_id: TP40004365
resource_type: Guide
platform: macOS
topic: User Experience
technology: ApplicationServices
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/SpeechSynthesisProgrammingGuide/CommandSyntax/CommandSyntax.html
archived_at: '2026-07-18T02:12:49.604663Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Speech Synthesis Programming Guide](Introduction%20to%20Speech%20Synthesis%20Programming%20Guide.md)


[Next](Phonemes.md)[Previous](Techniques%20for%20Customizing%20Synthesized%20Speech.md)

# Syntax of Embedded Speech Commands

This appendix provides a formalization of the embedded command syntax structure, subject to the following conventions:

- Items enclosed in angle brackets (< and >) represent logical units that are listed and defined in another row in the table.
- Items enclosed in brackets ([ and ]) are optional.
- Items followed by an ellipsis (...) may be repeated one or more times.
- When two or more items are separated by a vertical bar (|), any one of the listed items may be used.

Table A-1 defines the identifiers used in embedded commands.

__Table A-1__  Embedded command syntax structure

| Identifier | Syntax |
| _CommandBlock_ | <_BeginDelimiter_> <_CommandList_> <_EndDelimiter_> |
| _BeginDelimiter_ | <_String1_> | <_String2_> |
| _EndDelimiter_ | <_String1_> | <_String2_> |
| _CommandList_ | <_Command_> [; <_Command_>] ... |
| _Command_ | <_CommandSelector_> [_Parameter_] ... |
| _CommandSelector_ | <_OSType_> |
| _Parameter_ | <_OSType_> | <_String1_> | <_String2_> | <_StringN_> | <_RealValue_> | <_32BitValue_> | <_16BitValue_> | <_8BitValue_> |
| _String1_ | <_Character_> |
| _String2_ | <_Character_> <_Character_> |
| _StringN_ | [<_Character_> ...] |
| _OSType_ | <_Character_> <_Character_> <_Character_> <_Character_> |
| _32BitValue_ | <_OSType_> | <_LongInt_> | <_HexLongInt_> |
| _16BitValue_ | <_Integer_> | <_HexInteger_> |
| _8BitValue_ | <_Byte_> | <_HexByte_> |
| _RealValue_ | <Decimal number: 0.0000 ≤ N ≤ 65,535.9999> |
| _LongInt_ | <Decimal number: 0 ≤ N ≤ 4,294,967,295> |
| _HexLongInt_ | <Hex number: 0x00000000 ≤ N ≤ 0xFFFFFFFF> |
| _Integer_ | <Decimal number: 0 ≤ N ≤ 65,535> |
| _HexInteger_ | <Hex number: 0x0000 ≤ N ≤ 0xFFFF> |
| _Character_ | <Any printable character (for example A, b, \*, ~, \)> |
| _Byte_ | <Decimal number: 0 ≤ N ≤ 255> |
| _HexByte_ | <Hex number: 0x00 ≤ N ≤ 0xFF> |

[Next](Phonemes.md)[Previous](Techniques%20for%20Customizing%20Synthesized%20Speech.md)

