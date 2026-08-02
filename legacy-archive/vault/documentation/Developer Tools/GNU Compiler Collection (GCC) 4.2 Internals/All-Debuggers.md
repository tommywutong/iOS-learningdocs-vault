---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/All-Debuggers.html
archived_at: '2026-07-15T07:31:01.184412Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [DBX Options](DBX-Options.md#apple-irbfqlkpob2gs33oom),
Up: [Debugging Info](Debugging-Info.md#apple-irswe5lhm5uw4zznjfxgm3y)

---

#### 15.22.1 Macros Affecting All Debugging Formats

These macros affect all debugging formats.

— Macro: __DBX_REGISTER_NUMBER__ (regno)
> A C expression that returns the DBX register number for the compiler
> register number regno. In the default macro provided, the value
> of this expression will be regno itself. But sometimes there are
> some registers that the compiler knows about and DBX does not, or vice
> versa. In such cases, some register may need to have one number in the
> compiler and another for DBX.
>
> If two registers have consecutive numbers inside GCC, and they can be
> used as a pair to hold a multiword value, then they _must_ have
> consecutive numbers after renumbering with `DBX_REGISTER_NUMBER`.
> Otherwise, debuggers will be unable to access such a pair, because they
> expect register pairs to be consecutive in their own numbering scheme.
>
> If you find yourself defining `DBX_REGISTER_NUMBER` in way that
> does not preserve register pairs, then what you must do instead is
> redefine the actual register numbering scheme.

— Macro: __DEBUGGER_AUTO_OFFSET__ (x)
> A C expression that returns the integer offset value for an automatic
> variable having address x (an RTL expression). The default
> computation assumes that x is based on the frame-pointer and
> gives the offset from the frame-pointer. This is required for targets
> that produce debugging output for DBX or COFF-style debugging output
> for SDB and allow the frame-pointer to be eliminated when the
> `-g` options is used.

— Macro: __DEBUGGER_ARG_OFFSET__ (offset, x)
> A C expression that returns the integer offset value for an argument
> having address x (an RTL expression). The nominal offset is
> offset.

— Macro: __PREFERRED_DEBUGGING_TYPE__
> A C expression that returns the type of debugging output GCC should
> produce when the user specifies just `-g`. Define
> this if you have arranged for GCC to support more than one format of
> debugging output. Currently, the allowable values are `DBX_DEBUG`,
> `SDB_DEBUG`, `DWARF_DEBUG`, `DWARF2_DEBUG`,
> `XCOFF_DEBUG`, `VMS_DEBUG`, and `VMS_AND_DWARF2_DEBUG`.
>
> When the user specifies `-ggdb`, GCC normally also uses the
> value of this macro to select the debugging output format, but with two
> exceptions. If `DWARF2_DEBUGGING_INFO` is defined, GCC uses the
> value `DWARF2_DEBUG`. Otherwise, if `DBX_DEBUGGING_INFO` is
> defined, GCC uses `DBX_DEBUG`.
>
> The value of this macro only affects the default debugging output; the
> user can always get a specific type of output by using `-gstabs`,
> `-gcoff`, `-gdwarf-2`, `-gxcoff`, or `-gvms`.
