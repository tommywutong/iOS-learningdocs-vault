---
title: File Metadata Search Programming Guide
apple_id: TP40001841
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreServices
published: '2011-09-28'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/SpotlightQuery/Concepts/QueryFormat.html
archived_at: '2026-07-15T05:24:41.698152Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File Metadata Search Programming Guide](About%20File%20Metadata%20Queries.md)


[Next](Displaying%20the%20Finder%E2%80%99s%20Spotlight%20Search%20Window.md)[Previous](Searching%20File%20Metadata%20with%20NSMetadataQuery.md)

# File Metadata Query Expression Syntax

File metadata queries are constructed using a query language that is a subset of the predicate string format. The metadata search expression syntax allows an application to construct searches ‘on the fly’, allow advanced users to construct their own queries, or your application to store often used queries for easy use. The syntax is relatively straightforward, including comparisons, language agnostic options, and time and date variables.

The file metadata query expression syntax is a simplified form of filename globbing familiar to shell users. Queries have the following format:

```
attribute == value
```

where `attribute` is a standard metadata attribute (see “_[File Metadata Attributes Reference](../../File%20Metadata%20Attributes%20Reference/About%20the%20File%20Metadata%20Attributes%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmobz)_”) or a custom metadata attribute defined by an importer.

For example, to query Spotlight for all the files authored by “Steve” the query would look like the following:

```
kMDItemAuthors ==[c] "Steve"
```

The available comparison operators are listed in Table 3-1.

__Table 3-1__  Comparison operators

| Operator | Description |
| `==` | equal |
| `!=` | not equal |
| `<` | less than (available for numeric values and dates only) |
| `>` | greater than (available for numeric values and dates only) |
| `<=` | less than or equal (available for numeric values and dates only) |
| `>=` | greater than or equal (available for numeric values and dates only) |
| `InRange(attributeName,minValue,maxValue)` | numeric values within the range of minValue through maxValue in the specified attributeName |

Characters such as `“` and `‘` in the value string should be escaped using the `\` character.

The search value in the example has the modifier “`c`”. These are modifiers specify how the comparison is made. Table 3-2 describes the available comparison modifiers.

Search modifiers should immediately follow the comparison operator and be surrounded by square brackets `[…]`.

__Table 3-2__  Value Comparison modifiers

| Modifier | Description |
| `c` | The comparison is case insensitive. |
| `d` | The comparison is insensitive to diacritical marks. |

Table 3-3 shows several examples that use the comparison modifiers.

__Table 3-3__  Value Comparison modifier examples

| Query string | Results |
| `kMDItemTextContent == "Paris"` | Matches “Paris” but not “paris”. |
| `kMDItemTextContent ==[c] "Paris"` | Matches “Paris” and “paris”. |
| `kMDItemTextContent ==[c] "*Paris*"` | Matches “Paris”, “paris”, “I love Paris”, and “paris-france.jpg””. |
| `kMDItemTextContent == "Frédéric"` | Matches “Frédéric” but not “Frederic”. |
| `kMDItemTextContent ==[d] "Frédéric"` | Matches “Frédéric” and “Frederic” regardless of the word case. |

Using the wildcard characters (`*` and `?` ) you can match substrings at the beginning of a string, end of a string, or anywhere within the string. Table 3-4 shows several common usages.

The `*` character matches multiple characters whereas the `?` wildcard character matches a single character.

__Table 3-4__  Using wildcards

| Query string | Result |
| `kMDItemTextContent == "paris*"` | Matches attribute values that begin with “paris”. For example, matches “paris”, but not “comparison”. |
| `kMDItemTextContent == "*paris"` | Matches attribute values that end with “paris”. |
| `kMDItemTextContent == "*paris*"` | Matches attributes that contain "paris" anywhere within the value. For example, matches “paris” and “comparison”. |
| `kMDItemTextContent == "paris"` | Matches attribute values that are exactly equal to “paris”. |

Queries can be combined using a C-like syntax for `AND` (`&&`) and `OR` (`||`). For example, to restrict a query to audio files authored by “Steve” the query would be:

```
kMDItemAuthors ==[c] "Steve" && kMDItemContentType == "public.audio"
```

Parenthesis can be used to further group query matching. For example, to search for audio files authored by “Steve” or “Daniel” the query would be:

```
(kMDItemAuthors ==[c] "Daniel" || kMDItemAuthors[c] == "Steve") &&
 kMDItemContentType == "public.audio"
```

You can expand this search to include video files using the following query:

```
(kMDItemAuthors ==[c] "Daniel" || kMDItemAuthors ==[c] "Steve" ) &&
 (kMDItemContentType == "public.audio" || kMDItemContentType == "public.video")
```


You can also create queries that use the date and time as the search value. The date and time value is formatted as a floating-point value that is compatible with CFDate, seconds relative to January 1, 2001.

Additionally, the `$time` variable is provided that can be used to specify values relative to the current time, as shown in Table 3-5.

__Table 3-5__  $time variable expressions

| Time variable | Description |
| `$time.now` | The current date and time. |
| `$time.today` | The current date. |
| `$time.yesterday` | Yesterday’s date. |
| `$time.this_week(-1)` | Dates in the previous week. |
| `$time.this_week` | Dates in the current week. |
| `$time.this_month` | Dates in the current month. |
| `$time.this_year` | Dates in the current year. |
| `$time.now(NUMBER)` | The date and time by adding a positive or negative value, in seconds, to the current time. |
| `$time.today(NUMBER)` | The date by adding a positive or negative value, in days, to the current day |
| `$time.this_week(NUMBER)` | Dates by adding a positive or negative value, in weeks, to the current week. |
| `$time.this_month(NUMBER)` | Dates by adding a positive or negative value, in months, to the current month. |
| `$time.this_year(NUMBER)` | Dates by adding a positive or negative value, in years, to the current year. |
| `$time.iso(ISO-8601-STR)` | The date by parsing the specified ISO-8601-STR compliant string. |

Using the `$time` variable you can restrict a search to find only files that have been changed in the last week using the following query:

```
((kMDItemAuthors ==[c] "Daniel" || kMDItemAuthors[c] == "Steve") &&
 (kMDItemContentType == "public.audio" || kMDItemContentType == "public.video")) &&
 (kMDItemFSContentChangeDate == $time.this_week(-1))
```

[Next](Displaying%20the%20Finder%E2%80%99s%20Spotlight%20Search%20Window.md)[Previous](Searching%20File%20Metadata%20with%20NSMetadataQuery.md)

