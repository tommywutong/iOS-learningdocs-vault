---
title: 'Writing a parser using NSScanner (a CSV parsing example) | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/11/writing-parser-using-nsscanner-csv.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:dbab23d38c3d8c32'
translated: false
---

> 原文：[Writing a parser using NSScanner (a CSV parsing example) | Cocoa with Love](https://www.cocoawithlove.com/2009/11/writing-parser-using-nsscanner-csv.html)　·　Cocoa with Love (Matt Gallagher)

Comma-separated value (CSV) files are one of the most commonly used data formats for exchanging rows of simple data. There are many implementations of CSV parsing for Cocoa strings but the purpose of this post is to use the example of an RFC4180 compliant CSV parser implementation to show you the basics of writing a recursive descent parser for importing data into your Cocoa applications.

## Introduction

CSV parsers for Cocoa already exist: Drew McCormack at [MacResearch](http://www.macresearch.org) has [a good article covering his implementation of a CSV parser](http://www.macresearch.org/cocoa-scientists-part-xxvi-parsing-csv-data) and [cCSVParse](http://michael.stapelberg.de/cCSVParse) will also do the job. Instead of CSV and the implementation itself, I'm going to try and focus on reading a parser grammar and adapting that into a program of your own.

Most common solutions for parsing CSV files involve quick parsers which don't consider the full format and instead just split strings into lines using `-[NSString componentsSeparatedByString:@"\n"]` and then split lines into columns with `-[NSString componentsSeparatedByString:@","]`. This will work for some cases but it does not handle all aspects of RFC4180 and is limited to simple CSV files.

## The technical description of a CSV file

Adapting slightly from [RFC 4180 - Common Format and MIME Type for Comma-Separated Values (CSV) files](http://tools.ietf.org/html/rfc4180), the Extended Backus-Naur Format (EBNF) grammar for a CSV file is as follows:

If you're not accustomed to reading EBNFs, the very first line here (the "file" line) states that a CSV "file":

- optionally has a "header", which if used must be followed by a "lineSeparator"
- must have a "record"
- the first record may be followed by any number of "lineSeparator" plus "record" entries.

The grammar shown here is slightly less restrictive than RFC4180 in that it allows any data (not just the CSV subset of US-ASCII) in the "textData". I'll also implement the parser so that different separators (including any string that contains no new line or double quote characters) can be used instead of commas. The implementation will also support Unix newlines or classic Mac carriage returns can be used instead of DOS "\\r\\n" line separators.

## Design of the parser

The parser will be a form of [recursive descent parser](http://en.wikipedia.org/wiki/Recursive_descent_parser), which is the easiest way to implement most simple grammars like the one above. The idea is that we write a method for each line of the grammar. If any line contains a reference to another line, the implementation method will attempt to descend into the method for the referenced line.

If you're accustomed to the lex/yacc school of thought and are curious to know if the approach will similarly split tokenizing and parsing into separate stages: yes, it will. Most of the tokenizing is done by `NSScanner` (although it presents each token as requested, not as a pre-prepared stream). The code we actually implement will predominantly deal with the parser/generator side.

Initialization of the parser will be handled by the following method:

```objc
- (id)initWithString:(NSString *)csvString
    separator:(NSString *)separatorString
    hasHeader:(BOOL)hasHeader
    fieldNames:(NSArray *)fieldNames;
```

The structure of CSV files means that it is difficult to guess if the header line is actually present — so we need to tell the parser whether to look for it. An array of names for fields can be provided if there is no header (if no names are provided, they'll be given names with the format "FIELD_X").

The parsing will be initiated by invoking either:

```objc
- (NSArray *)arrayOfParsedRows;
```

where the result is an `NSArray` of `NSDictionary` objects or with:

```objc
- (void)parseRowsForReceiver:(id)receiver selector:(SEL)receiverSelector;
```

where the method `receiverSelector` must take a single `NSDictionary` parameter. This second method does not return the entire result but instead sends each row as it is parsed to the receiver. It is more efficient since it does not need to keep copies of all row data.

## Parser methods

There are two types of parsing methods that we need to implement:

- Structural methods which don't directly access the string (`parseFile`, `parseHeader`, `parseRecord`, `parseName`, `parseField`, `parseEscaped`, `parseNonEscaped`)
- Tokenizing methods which use `NSScanner` to access the string (`parseDoubleQuote`, `parseTwoDoubleQuotes`, `parseSeparator`, `parseLineSeparator`, `parseTextData`)

I'm not going to show all of them here (you can download the full code to see them) but I will show one of each type.

The tokenizing methods are the easiest. All they do is invoke `NSScanner` methods.

```objc
- (NSString *)parseLineSeparator
{
    NSString *matchedNewlines = nil;
    [scanner
        scanCharactersFromSet:[NSCharacterSet newlineCharacterSet]
        intoString:&matchedNewlines];
    return matchedNewlines;
}
```

The structural elements have a bit more to do but are still fairly simple. The "escaped" element in the grammar has the following structure:

This structure is directly reflected in its implementation — it starts and ends with a check for "doubleQuote" and loops over checks for "textData", "separator", "lineSeparator" or "twoDoubleQuotes" in the middle.

```objc
- (NSString *)parseEscaped
{
    if (![self parseDoubleQuote])
    {
        return nil;
    }
    
    NSString *accumulatedData = [NSString string];
    while (YES)
    {
        NSString *fragment = [self parseTextData];
        if (!fragment)
        {
            fragment = [self parseSeparator];
            if (!fragment)
            {
                fragment = [self parseLineSeparator];
                if (!fragment)
                {
                    if ([self parseTwoDoubleQuotes])
                    {
                        fragment = @"\"";
                    }
                    else
                    {
                        break;
                    }
                }
            }
        }
        
        accumulatedData = [accumulatedData stringByAppendingString:fragment];
    }
    
    if (![self parseDoubleQuote])
    {
        return nil;
    }
    
    return accumulatedData;
}
```

An interesting point to note is that most parsing stages return the text that they parse. However, when `parseTwoDoubleQuotes` is used, we instead append just one double quote character, since the two double quotes is actually an escape sequence representing one.

## Lookaheads

The most annoying feature to implement in a recursive descent parser is a lookahead — this happens in the `parseTextData` method.

Lookahead is required because of my choice to accept separator strings longer than a single character. This means that the "textData" element will end with any of:

- \\r
- \\n
- U+0085
- "
- the separator string

Unfortunately, `NSScanner` can't scan until it reaches one of these 5 elements. The best we can do is create a character set from the first four and the first character in the separator string and use `scanUpToCharactersFromSet:intoString:`

When scanning through text data, if we reach the first character of the separator string, we need to scan ahead and see if it is actually the whole separator string. The whole separator string will terminate the "textData" without being added, otherwise we backtrack and add the character to the existing "textData" and continue scanning.

If `NSScanner` had a `scanUpToStringFromArray:intoString:` method, this lookahead could be avoided (or at least shifted out of our code and into `NSScanner`). But this method does not exist and it looked like too much work to efficiently implement as part of this post.

## The sample program

The sample program that I've provided uses this parser to parse a 1.7 MB CSV file containing 16,081 Australian postcode entries, names and longitude/latitudes (data from [SixFive.co.uk](http://www.sixfive.co.uk/index.cfm/2007/3/25/Geocoding-Australian-Postcodes)). As results are parsed, they are entered into a Core Data SQLite file.

The whole process takes about 0.47 seconds on my Mac Pro with parsing taking 0.28 seconds of this time and Core Data object creation taking 0.19 seconds. I'm sure a more carefully coded parser could halve this time or better but it represents good performance for minimal effort.

## Conclusion

> You can [download the CSVParser class and CSVImporter sample project](https://www.cocoawithlove.com/assets/objc-era/CSVImporter.zip) (315kB).

The aim in this post was to present a complete, flexible CSV parser while making the code as easy to read as possible. I hope that it has shown how you can import data from unconventional formats into Cocoa-friendly formats easily while obeying the more minor quirks that many formats have.

The type of parser presented here is a recursive descent parser. This is the easiest parser to implement for simple grammars. However, this is not how commercial parsers are written — larger parsers use generated action and goto tables to handle their branches instead of manually written methods and code. Have a look at the [Wikipedia entry on LR parsers](http://en.wikipedia.org/wiki/LR_parser) for more on how this is done.
