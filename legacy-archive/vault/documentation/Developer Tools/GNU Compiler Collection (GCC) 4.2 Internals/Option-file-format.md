---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Option-file-format.html
archived_at: '2026-07-15T07:31:02.451682Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Option properties](Option-properties.md#apple-j5yhi2lpnywxa4tpobsxe5djmvzq),
Up: [Options](Options.md#apple-j5yhi2lpnzzq)

---

### 7.1 Option file format

Option files are a simple list of records in which each field occupies
its own line and in which the records themselves are separated by
blank lines. Comments may appear on their own line anywhere within
the file and are preceded by semicolons. Whitespace is allowed before
the semicolon.

The files can contain the following types of record:

- A language definition record. \xA0These records have two fields: the
  string ``Language`' and the name of the language. \xA0Once a language
  has been declared in this way, it can be used as an option property.
  See [Option properties](Option-properties.md#apple-j5yhi2lpnywxa4tpobsxe5djmvzq).
- An option definition record. \xA0These records have the following fields:
  1. the name of the option, with the leading “-” removed
  2. a space-separated list of option properties (see [Option properties](Option-properties.md#apple-j5yhi2lpnywxa4tpobsxe5djmvzq))
  3. the help text to use for `--help` (omitted if the second field
     contains the `Undocumented` property).

  By default, all options beginning with “f”, “W” or “m” are
  implicitly assumed to take a “no-” form. This form should not be
  listed separately. If an option beginning with one of these letters
  does not have a “no-” form, you can use the `RejectNegative`
  property to reject it.

  The help text is automatically line-wrapped before being displayed.
  Normally the name of the option is printed on the left-hand side of
  the output and the help text is printed on the right. However, if the
  help text contains a tab character, the text to the left of the tab is
  used instead of the option's name and the text to the right of the
  tab forms the help text. This allows you to elaborate on what type
  of argument the option takes.
- A target mask record. \xA0These records have one field of the form
  ``Mask(x)`'. \xA0The options-processing script will automatically
  allocate a bit in `target_flags` (see [Run-time Target](Run_002dtime-Target.md#apple-kj2w4xzqgazgi5djnvss2vdbojtwk5a)) for
  each mask name x and set the macro `MASK_`x to the
  appropriate bitmask. \xA0It will also declare a `TARGET_`x
  macro that has the value 1 when bit `MASK_`x is set and
  0 otherwise.

  They are primarily intended to declare target masks that are not
  associated with user options, either because these masks represent
  internal switches or because the options are not available on all
  configurations and yet the masks always need to be defined.
