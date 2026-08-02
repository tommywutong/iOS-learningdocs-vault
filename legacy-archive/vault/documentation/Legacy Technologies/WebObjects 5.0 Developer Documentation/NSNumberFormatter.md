---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSNumberFormatter.html
archived_at: '2026-07-15T08:13:56.361419Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

# NSNumberFormatter

> **__Inherits from:__**
> : java.text.Format : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

Instances of NSNumberFormatter convert between BigDecimal numbers and textual representations of numeric values. The representation encompasses integers and floating-point numbers; floating-point numbers can be formatted to a specified decimal position. NSNumberFormatters can also impose ranges on the numeric values that can be formatted.

You can associate a number pattern with a WOString or WOTextField dynamic element. WebObjects uses an NSNumberFormatter object to perform the appropriate conversions.

Instances of NSNumberFormatter are mutable.

## Creating an Instance of NSNumberFormatter

The most common technique for creating a NSNumberFormatter is to use the one-argument constructor, which takes as its argument a string whose contents can be one of the following:

- "positivePattern" For example, `"$###,##0.00"` (the syntax of format strings is discussed in the following section).
- "positivePattern;negativePattern" For example, `"###,##0.00;(###,##0.00)"`.
- "positivePattern;zeroPattern;negativePattern"For example, `"$###,###.00;0.00;($###,##0.00)"`. Note that zero patterns are treated as string constants.

As implied in the above list, you're only required to specify a pattern for positive values. If you don't specify a pattern for negative and zero values, a default pattern based on the positive value pattern is used. For example, if your positive value pattern is `"#,##0.00"`, an input value of `"0"` will be displayed as `"0.00"`.

If you don't specify a pattern for negative values, the pattern specified for positive values is used, preceded by a minus sign (`-`).

If you specify a separate pattern for negative values, its separators should be parallel to those specified in the positive pattern string. In NSNumberFormatter, separators are either enabled or disabled for all patterns-both your negative and positive patterns should therefore use the same approach.

As an alternative to using the one-argument constructor is to use the no-argument constructor and invoking [setPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cqmf2hizlsny) with the pattern. You can also use the [setPositivePattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cqn5zws5djozsvayluorsxe3q) and [setNegativePattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5comvtwc5djozsvayluorsxe3q) methods.

### Pattern String Syntax

Pattern strings can include the following types of characters:

- NumbersPattern strings can include numeric characters. Wherever you include a number in a pattern string, the number is displayed unless an input character in the same relative position overwrites it. For example, suppose you have the positive pattern string `"9,990.00"`, and the value 53.88 is entered into a cell to which the pattern has been applied. The cell would display the value as 9,953.88.
- SeparatorsPattern strings can include the period character (`.`) as a decimal separator, and comma character (`,`) as a thousand separator. If you want to use different characters as separators, you can set them using the [setDecimalSeparator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cemvrws3lbnrjwk4dbojqxi33s) and [setThousandSeparator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cunbxxk43bnzsfgzlqmfzgc5dpoi) methods.
- PlaceholdersYou use the pound sign character (`#`) to represent numeric characters that will be input by the user. For example, suppose you have the positive pattern `"$#,##0.00"`. If the characters 76329 were entered into a cell to which the pattern has been applied, they would be displayed as $76,329.00. Strictly speaking, however, you don't need to use placeholders. The format strings `",0.00"`, `"#,#0.00"`, and `"#,##0.00"` are functionally equivalent. In other words, including separator characters in a pattern string signals NSNumberFormatter to use the separators, regardless of whether you use (or where you put) placeholders. The placeholder character's chief virtue lies in its ability to make pattern strings more human-readable, which is especially useful if you're displaying patterns in the user interface.
- SpacesTo include a space in a pattern string, use the underscore character (`_`). This character inserts a space if no numeric character has been input to occupy that position.
- CurrencyThe dollar sign character (`$`) is normally treated just like any other character that doesn't play a special role in NSNumberFormatter.

All other characters specified in a pattern string are displayed as typed. The following table shows examples of the how the value 1019.55 is displayed for different positive patterns:

|  |  |
| --- | --- |
| __Pattern String__ | __Display__ |
| `"#,##0.00"` | 1,019.55 |
| `"$#,##0.00"` | $1,019.55 |
| `"___,__0.00"` | 1,019.55 |

## Using Separators

NSNumberFormatter supports two different kinds of separators: thousand and decimal. By default these separators are represented by the comma (`,`) and period (`.`) characters respectively. The default pattern ("`#,##0.##`") enables them.

All of the following statements have the effect of enabling thousand separators:

> ```
> // use setPattern:
> numberFormatter.setPattern("#,###");
>
> // use setHasThousandSeparators:
> numberFormatter.setHasThousandSeparators(true);
>
> // use setThousandSeparator:
> numberFormatter.setThousandSeparator("_");
> ```

If you use the statement `numberFormatter.setHasThousandSeparators(false)`, it disables thousand separators, even if you've set them through another means.

Both of the following statements have the effect of enabling decimal separators:

> ```
> // use setFormat: numberFormatter.setFormat("0.00");
>  // use setDecimalSeparator: numberFormatter.setDecimalSeparator("-");
> ```

When you enable or disable separators, it affects both positive and negative patterns. Consequently, both patterns must use the same separator scheme.

You can use the [thousandSeparator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf52gq33vonqw4zctmvygc4tborxxe) and [decimalSeparator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5sgky3jnvqwyu3fobqxeylun5za) methods to return a string containing the character the receiver uses to represent each separator. However, this shouldn't be taken as an indication of whether separators are enabled-even when separators are disabled, an NSNumberFormatter still knows the characters it uses to represent separators.

Separators must be single characters. If you specify multiple characters in the arguments to [setThousandSeparator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cunbxxk43bnzsfgzlqmfzgc5dpoi) and [setDecimalSeparator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cemvrws3lbnrjwk4dbojqxi33s), only the first character is used.

You can't use the same character to represent thousand and decimal separators.

## Localization

NSNumberFormatter provides methods to localize pattern strings. You can change the currency symbol, the decimal separator, and the thousands separator manually, or you can trust NSNumberFormatter to do it for you, based on locales. If you enable localization for an instance of NSNumberFormatter, it will check the current locale and localize pattern strings appropriately for that locale. By default, instances of NSNumberFormatter are not localized. You can enable localization for all new instances of NSNumberFormatter using [setDefaultLocalizesPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgttvnvrgk4sgn5zg2yluorsxel3tmv2eizlgmf2wy5cmn5rwc3djpjsxgudbor2gk4to) or for a specific instance of NSNumberFormatter using [setLocalizesPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cmn5rwc3djpjsxgudbor2gk4to). See the method descriptions for [setDefaultLocalizesPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgttvnvrgk4sgn5zg2yluorsxel3tmv2eizlgmf2wy5cmn5rwc3djpjsxgudbor2gk4to) and [setLocalizesPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cmn5rwc3djpjsxgudbor2gk4to) for more information.

## Constants

---

NSNumberFormatter provides the following constants for specifying rounding modes and special numbers.The rounding mode specifiers are used with [roundingBehavior](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zg65lomruw4z2cmvugc5tjn5za) and [setRoundingBehavior](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5csn52w4zdjnztuezlimf3gs33s).

|  |  |  |
| --- | --- | --- |
| __Constant__ | __Type__ | __Description__ |
| RoundDown | `int` | Rounding mode specifier: round towards negative infinity |
| RoundUp | `int` | Rounding mode specifier: round towards positive infinity |
| RoundPlain | `int` | Rounding mode specifier: round to nearest up |
| RoundBankers | `int` | Rounding mode specifier: round to nearest even |
| NSDecimalNotANumber | `java.math.BigDecimal` | Definition of Not A Number (NaN) |
| DefaultPattern | `String` | Default format for pattern strings: "#,##0.##". |

## Method Types

---

> **Constructors**
>
> : [NSNumberFormatter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5hfgttvnvrgk4sgn5zg2yluorsxe)
>
> **Performing formatted conversions**
>
> : [objectValueForString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5xwe2tfmn2fmylmovsum33skn2he2lom4): [stringForObjectValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zxi4tjnztum33sj5rguzldorlgc3dvmu)
>
> **Methods inherited from java.text.Format**
>
> : [format](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5tg64tnmf2a): [parseObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5ygc4ttmvhwe2tfmn2a)
>
> **Accessing patterns**
>
> : [negativePattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5xgkz3boruxmzkqmf2hizlsny): [pattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5ygc5dumvzg4): [positivePattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5yg643joruxmzkqmf2hizlsny): [setNegativePattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5comvtwc5djozsvayluorsxe3q): [setPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cqmf2hizlsny): [setPositivePattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cqn5zws5djozsvayluorsxe3q)
>
> **Accessing floating point settings**
>
> : [allowsFloats](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5qwy3dpo5zum3dpmf2hg): [roundingBehavior](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zg65lomruw4z2cmvugc5tjn5za): [setAllowsFloats](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cbnrwg653tizwg6yluom): [setRoundingBehavior](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5csn52w4zdjnztuezlimf3gs33s)
>
> **Accessing decimal separator settings**
>
> : [decimalSeparator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5sgky3jnvqwyu3fobqxeylun5za): [setDecimalSeparator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cemvrws3lbnrjwk4dbojqxi33s)
>
> **Accessing thousand separator settings**
>
> : [hasThousandSeparators](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5ugc42unbxxk43bnzsfgzlqmfzgc5dpojzq): [setHasThousandSeparators](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cimfzvi2dpovzwc3teknsxaylsmf2g64tt): [setThousandSeparator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cunbxxk43bnzsfgzlqmfzgc5dpoi): [thousandSeparator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf52gq33vonqw4zctmvygc4tborxxe)
>
> **Accessing strings for special numbers**
>
> : [setStringForNotANumber](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5ctorzgs3thizxxettporau45lnmjsxe): [setStringForNull](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5ctorzgs3thizxxettvnrwa): [setStringForZero](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5ctorzgs3thizxxewtfojxq): [stringForNotANumber](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zxi4tjnztum33sjzxxiqkoovwwezls): [stringForNull](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zxi4tjnztum33sjz2wy3a): [stringForZero](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zxi4tjnztum33sljsxe3y)
>
> **Limiting the input number**
>
> : [maximum](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5wwc6djnv2w2): [minimum](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5wws3tjnv2w2): [setMaximum](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cnmf4gs3lvnu): [setMinimum](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cnnfxgs3lvnu)
>
> **Localization Methods**
>
> : [availableLocales](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgttvnvrgk4sgn5zg2yluorsxel3bozqws3dbmjwgktdpmnqwyzlt): [currencySymbol](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5rxk4tsmvxgg6ktpfwwe33m): [defaultLocale](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgttvnvrgk4sgn5zg2yluorsxel3emvtgc5lmorgg6y3bnrsq): [defaultLocalizesPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgttvnvrgk4sgn5zg2yluorsxel3emvtgc5lmorgg6y3bnruxuzltkbqxi5dfojxa): [locale](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5wg6y3bnrsq): [localizesPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5wg6y3bnruxuzltkbqxi5dfojxa): [setCurrencySymbol](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cdovzhezlomn4vg6lnmjxwy): [setDefaultLocale](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgttvnvrgk4sgn5zg2yluorsxel3tmv2eizlgmf2wy5cmn5rwc3df): [setDefaultLocalizesPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgttvnvrgk4sgn5zg2yluorsxel3tmv2eizlgmf2wy5cmn5rwc3djpjsxgudbor2gk4to): [setLocale](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cmn5rwc3df): [setLocalizesPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cmn5rwc3djpjsxgudbor2gk4to)
>
> **Deprecated Methods**
>
> : [attributedStringForNil](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5qxi5dsnfrhk5dfmrjxi4tjnztum33sjzuwy): [attributedStringForNotANumber](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5qxi5dsnfrhk5dfmrjxi4tjnztum33sjzxxiqkoovwwezls): [attributedStringForZero](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5qxi5dsnfrhk5dfmrjxi4tjnztum33sljsxe3y): [format](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5tg64tnmf2a): [localizesFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5wg6y3bnruxuzltizxxe3lboq): [negativeFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5xgkz3boruxmzkgn5zg2ylu): [positiveFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5yg643joruxmzkgn5zg2ylu): [setAttributedStringForNil](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cbor2he2lcov2gkzctorzgs3thizxxettjnq): [setAttributedStringForNotANumber](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cbor2he2lcov2gkzctorzgs3thizxxettporau45lnmjsxe): [setAttributedStringForZero](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cbor2he2lcov2gkzctorzgs3thizxxewtfojxq): [setFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cgn5zg2ylu): [setLocalizesFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cmn5rwc3djpjsxgrtpojwwc5a): [setNegativeFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5comvtwc5djozsum33snvqxi): [setPositiveFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cqn5zws5djozsum33snvqxi)

## Constructors

---

### NSNumberFormatter

`public NSNumberFormatter()`

Creates an NSNumberFormatter and sets its pattern to the default pattern: "`#,##0.##`".

`public NSNumberFormatter(String pattern)`

Creates an NSFormatter and sets its pattern to _pattern_. If _pattern_ is illegal, the constructor throws an IllegalArgumentException. See ["Pattern String Syntax" (page 208)](#apple-ijduircgijeem) for an explanation of what makes a pattern legal.

__See Also:__ [setPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cqmf2hizlsny)

---

## Static Methods

---

### availableLocales

`public static java.util.Locale[] availableLocales()`

Returns a list of all installed locales.

---

### defaultLocale

`public static java.util.Locale defaultLocale()`

Returns the default locale for all instances of NSNumberFormatter.

---

### defaultLocalizesPattern

`public static boolean defaultLocalizesPattern()`

Returns `true` to indicate that the receiver's format will be localized for all new instances of NSNumberFormatter in your application. By default, patterns are not localized.

__See Also:__ [setDefaultLocalizesPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgttvnvrgk4sgn5zg2yluorsxel3tmv2eizlgmf2wy5cmn5rwc3djpjsxgudbor2gk4to)

---

### setDefaultLocale

`public static void setDefaultLocale(Locale newLocale)`

Sets according to _newLocale_ the default locale of the receiver. Throws an IllegalArgumentException if _newLocale_ is null.

---

### setDefaultLocalizesPattern

`public static void setDefaultLocalizesPattern(boolean newDefault)`

Sets according to _newDefault_ whether all new NSNumberFormatter objects in your application created after this method is invoked are set to be localized by NSNumberFormatter based on the locale. NSNumberFormatter will choose the appropriate currency symbol, decimal separator, thousands separator, string for zero, and string for not a number based on locale if _newDefault_ is `true`. By default, NSNumberFormatters are not localized.

__See Also:__ [defaultLocalizesPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgttvnvrgk4sgn5zg2yluorsxel3emvtgc5lmorgg6y3bnruxuzltkbqxi5dfojxa)

---

## Instance Methods

---

### allowsFloats

`public boolean allowsFloats()`

Returns `true` if the receiver allows as input floating point values (that is, values that include the period character (`.`)), `false` otherwise. When this is set to `false`, only integer values can be provided as input. The default is `true`.

---

### attributedStringForNil

`public String attributedStringForNil()`

Deprecated in the Java Foundation framework. Don't use this method. Use [stringForNull](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zxi4tjnztum33sjz2wy3a) instead.

---

### attributedStringForNotANumber

`public String attributedStringForNotANumber()`

Deprecated in the Java Foundation framework. Don't use this method. Use [stringForNotANumber](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zxi4tjnztum33sjzxxiqkoovwwezls) instead.

---

### attributedStringForZero

`public String attributedStringForZero()`

Deprecated in the Java Foundation framework. Don't use this method. Use [stringForZero](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zxi4tjnztum33sljsxe3y) instead.

---

### currencySymbol

`public String currencySymbol()`

Returns a string representing the symbol the receiver uses to represent currency.

__See Also:__ [setCurrencySymbol](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cdovzhezlomn4vg6lnmjxwy)

---

### decimalSeparator

`public String decimalSeparator()`

Returns a string containing the character the receiver uses to represent decimal separators. By default this is the period character (`.`).

---

### format

`public StringBuffer format( Object object, StringBuffer toAppendTo, java.text.FieldPosition position)`

Formats _object_ to produce a string, appends the string to _toAppendTo_, and returns the resulting StringBuffer. The _position_ parameter specifies an alignment field to place the formatted object. When the method returns, this parameter contains the position of the alignment field. See Sun's java.text.Format documentation for more information.

__See Also:__ [stringForObjectValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zxi4tjnztum33sj5rguzldorlgc3dvmu)

---

### format

`public String format()`

Deprecated in the Java Foundation framework. Don't use this method. Use [pattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5ygc5dumvzg4) instead.

---

### hasThousandSeparators

`public boolean hasThousandSeparators()`

Returns `true` to indicate that the receiver's format includes thousand separators, `false` otherwise. The default is `false`.

---

### locale

`public java.util.Locale locale()`

Returns the current locale.

---

### localizesFormat

`public boolean localizesFormat()`

Deprecated in the Java Foundation framework. Don't use this method. Use [localizesPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5wg6y3bnruxuzltkbqxi5dfojxa) instead.

---

### localizesPattern

`public boolean localizesPattern()`

Returns `true` to indicate that the receiver's format will be localized for a specific instance of NSNumberFormatter. By default, instances of NSNumberFormatter are not localized.

---

### maximum

`public java.math.BigDecimal maximum()`

Returns the highest number allowed as input by the receiver.

---

### minimum

`public java.math.BigDecimal minimum()`

Returns the lowest number allowed as input by the receiver.

---

### negativeFormat

`public String negativeFormat()`

Deprecated in the Java Foundation framework. Don't use this method. Use [negativePattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5xgkz3boruxmzkqmf2hizlsny) instead.

---

### negativePattern

`public String negativePattern()`

Returns a string containing the pattern the receiver uses to display negative numbers.

__See Also:__ [positivePattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5yg643joruxmzkqmf2hizlsny), [setPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cqmf2hizlsny)

---

### objectValueForString

`public Object objectValueForString(String inString) throws java.text.ParseException`

Returns a number (a java.math.BigDecimal object) by parsing _inString_ according to the receiver's pattern. Throws a ParseException if the conversion fails for any reason.

__See Also:__ [setPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cqmf2hizlsny)

---

### parseObject

`public Object parseObject( String source, java.text.ParsePosition status)`

`public Object parseObject(String source) throws java.text.ParseException`

Parses a string to produce an object. See Sun's java.text.Format documentation for more information.

__See Also:__ [objectValueForString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5xwe2tfmn2fmylmovsum33skn2he2lom4)

---

### pattern

`public String pattern()`

Returns a string containing the pattern the receiver uses to format numbers.

__See Also:__ [setPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cqmf2hizlsny)

---

### positiveFormat

`public String positiveFormat()`

Deprecated in the Java Foundation framework. Don't use this method. Use [positivePattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5yg643joruxmzkqmf2hizlsny) instead.

---

### positivePattern

`public String positivePattern()`

Returns a string containing the pattern the receiver uses to format positive numbers.

__See Also:__ [setPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cqmf2hizlsny), [setNegativePattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5comvtwc5djozsvayluorsxe3q)

---

### roundingBehavior

`public int roundingBehavior()`

Returns an integer indicating the rounding behavior used by the receiver.

---

### setAllowsFloats

`public void setAllowsFloats(boolean flag)`

Sets according to _flag_ whether the receiver allows as input floating point values (that is, values that include the period character (`.`)). By default, floating point values are allowed as input.

---

### setAttributedStringForNil

`public void setAttributedStringForNil(String string)`

Deprecated in the Java Foundation framework. Don't use this method. Use [setStringForNull](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5ctorzgs3thizxxettvnrwa) instead.

---

### setAttributedStringForNotANumber

`public void setAttributedStringForNotANumber(String string)`

Deprecated in the Java Foundation framework. Don't use this method. Use [setStringForNotANumber](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5ctorzgs3thizxxettporau45lnmjsxe) instead.

---

### setAttributedStringForZero

`public void setAttributedStringForZero(String string)`

Deprecated in the Java Foundation framework. Don't use this method. Use [setStringForZero](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5ctorzgs3thizxxewtfojxq) instead.

---

### setCurrencySymbol

`public void setCurrencySymbol(String newSymbol)`

Sets the string the receiver uses to represent currency.

__See Also:__ [currencySymbol](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5rxk4tsmvxgg6ktpfwwe33m)

---

### setDecimalSeparator

`public void setDecimalSeparator(String aString)`

Sets the character the receiver uses as a decimal separator to _newSeparator_. If _newSeparator_ contains multiple characters, only the first one is used. Throws an IllegalArgumentException if _aString_ is null or has length other than one character.

---

### setFormat

`public void setFormat(String format)`

Deprecated in the Java Foundation framework. Don't use this method. Use [setPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cqmf2hizlsny) instead.

---

### setHasThousandSeparators

`public void setHasThousandSeparators(boolean flag)`

Sets according to _flag_ whether the receiver uses thousand separators. When _flag_ is `false`, thousand separators are disabled for both positive and negative formats (even if you've set them through another means, such as [setPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cqmf2hizlsny)). When _flag_ is `true`, thousand separators are used. In addition to using this method to add thousand separators to your format, you can also use it to disable thousand separators if you've set them using another method. The default is `false` (though you in effect change this setting to `true` when you set thousand separators through any means, such as [setPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cqmf2hizlsny))

---

### setLocale

`public void setLocale(java.util.Locale newLocale)`

Sets according to _newLocale_ the current locale of the receiver. Throws an IllegalArgumentException if _newLocale_ is null.

---

### setLocalizesFormat

`public void setLocalizesFormat(boolean newDefault)`

Deprecated for the Foundation framework. Don't use this method. Use [setLocalizesPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cmn5rwc3djpjsxgudbor2gk4to)instead.

---

### setLocalizesPattern

`public void setLocalizesPattern(boolean newDefault)`

Sets according to _newDefault_ whether the receiver's pattern is set to be localized by NSNumberFormatter based on the locale. NSNumberFormatter will choose the appropriate currency symbol, decimal separator, thousands separator, string for zero, and string for not a number based on locale if _newDefault_ is `true`. By default, NSNumberFormatters are not localized.

---

### setMaximum

`public void setMaximum(java.math.BigDecimal aMaximum)`

Sets the highest number the receiver allows as input to _aMaximum_. Throws an IllegalArgumentException if _aMaximum_ is not of type BigDecimal.

---

### setMinimum

`public void setMinimum(java.math.BigDecimal aMinimum)`

Sets the lowest number the receiver allows as input to _aMinimum_. Throws an IllegalArgumentException if _aMinimum_ is not of type BigDecimal.

---

### setNegativeFormat

`public void setNegativeFormat(String format)`

Deprecated in the Java Foundation framework. Don't use this method. Use [setNegativePattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5comvtwc5djozsvayluorsxe3q) instead.

---

### setNegativePattern

`public void setNegativePattern(String aString)`

Sets the pattern the receiver uses to display positive numbers to _pattern_. If _pattern_ is illegal, the method throws an IllegalArgumentException. See ["Pattern String Syntax" (page 208)](#apple-ijduircgijeem) for an explanation of what makes a pattern legal. Invokes the private method `validatePattern()` which throws an IllegalArgumentException if the pattern is null, the pattern string is empty, or the string does not contain one of the characters in ",._#0123456789".

__See Also:__ [setPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cqmf2hizlsny)

---

### setPattern

`public void setPattern(String aPattern)`

Sets the receiver's format to the string _aPattern_. This pattern can consist of one, two, or three parts separated by `";"`. The first part of the string represents the positive pattern, the second part of the string represents the zero value, and the last part of the string represents the negative pattern. If the string just has two parts, the first one becomes the positive pattern, and the second one becomes the negative pattern. If the string just has one part, it becomes the positive pattern, and default formats are provided for zero and negative values based on the positive format. For more discussion of this subject, see the section ["Creating an Instance of NSNumberFormatter" (page 207)](#apple-ineeiqscjbduu) in the Class Description. If the positive, negative, or zero pattern is illegal, the method throws an IllegalArgumentException. See ["Pattern String Syntax" (page 208)](#apple-ijduircgijeem) for an explanation of what makes a pattern legal.

The following code excerpt shows the three different approaches for setting an NSNumberFormatter object's format using __setPattern__:

> ```
> NSNumberFormatter numberFormatter = new NSNumberFormatter();
>
> // specify just positive format
> numberFormatter.setPattern("$#,##0.00");
>
> // specify positive and negative formats
> numberFormatter.setPattern("$#,##0.00;($#,##0.00)");
>
> // specify positive, zero, and negative formats
> numberFormatter.setFormat("$#,###.00;0.00;($#,##0.00)");
> ```

__See Also:__ [pattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5ygc5dumvzg4)

---

### setPositiveFormat

`public void setPositiveFormat(String format)`

Deprecated in the Java Foundation framework. Don't use this method. Use [setPositivePattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cqn5zws5djozsvayluorsxe3q) instead.

---

### setPositivePattern

`public void setPositivePattern(String pattern)`

Sets the pattern the receiver uses to display positive numbers to _pattern_. If _pattern_ is illegal, the method throws an IllegalArgumentException. See ["Pattern String Syntax" (page 208)](#apple-ijduircgijeem) for an explanation of what makes a pattern legal. Invokes the private method `validatePattern()` which throws an IllegalArgumentException if the pattern is null, the pattern string is empty, or the string does not contain one of the characters in ",._#0123456789".

__See Also:__ [setPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cqmf2hizlsny)

---

### setRoundingBehavior

`public void setRoundingBehavior(int newRoundingBehavior)`

Sets the receiver's rounding behavior to _newRoundingBehavior_. Throws an IllegalArgumentException if _newRoundingBehavior_ is not one of the standard rounding modes: NSRoundDown, NSRoundUp, NSRoundPlain, NSRoundBankers. Consult the Foundation functions and constants documentation for complete information on rounding modes.

---

### setStringForNotANumber

`public void setStringForNotANumber(String newString)`

Sets the string the receiver uses to display "not a number" to _newString_. Throws an IllegalArgumentException if _newString_ is null.

---

### setStringForNull

`public void setStringForNull(String newString)`

Sets the string the receiver uses to display null values to _newString_. Throws an IllegalArgumentException if _newString_ is null.

---

### setStringForZero

`public void setStringForZero(String aString)`

Sets the string the receiver uses to display zero values to _newString_.

---

### setThousandSeparator

`public void setThousandSeparator(String newSeparator)`

Sets the character the receiver uses as a thousand separator to _newSeparator_. If _newSeparator_ contains multiple characters, only the first one is used. If you don't have thousand separators enabled through any other means (such as [setPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cqmf2hizlsny)), using this method enables them. Throws an IllegalArgumentException if _newSeparator_ is null or has length other than one character.

---

### stringForNotANumber

`public String stringForNotANumber()`

Returns the string the receiver uses to display "not a number" values. By default "not a number" values are displayed as the string "NaN".

---

### stringForNull

`public String stringForNull()`

Returns the string the receiver uses to display null values. By default, null values are displayed as an empty string.

---

### stringForObjectValue

`public String stringForObjectValue(Object object) throws IllegalArgumentException`

Returns a string representing _object_ formatted according to the receiver's pattern. Throws an IllegalArgumentException if _object_ is not an instance of Number.

__See Also:__ [setPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjz2w2ytfojdg64tnmf2hizlsf5zwk5cqmf2hizlsny)

---

### stringForZero

`public String stringForZero()`

Returns the string the receiver uses to display zero values. By default zero values are displayed according to the format specified for positive values; for more discussion of this subject see the section ["Creating an Instance of NSNumberFormatter" (page 207)](#apple-ineeiqscjbduu) in the Class Description.

---

### thousandSeparator

`public String thousandSeparator()`

Returns a string containing the character the receiver uses to represent thousand separators. By default this is the comma character (`,`). Note that the return value doesn't indicate whether thousand separators are enabled.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
