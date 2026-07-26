---
title: CFStringTokenizer
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstringtokenizer
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringtokenizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringtokenizer.json'
content_hash: 'sha256:7b119bfdb7e4b19e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringTokenizer

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFStringTokenizer
```

## Overview

CFStringTokenizer allows you to tokenize strings into words, sentences or paragraphs in a language-neutral way. It supports languages such as Japanese and Chinese that do not delimit words by spaces, as well as de-compounding German compounds. You can obtain Latin transcription for tokens. It also provides language identification API.

You can use a CFStringTokenizer to break a string into tokens (sub-strings) on the basis of words, sentences, or paragraphs. When you create a tokenizer, you can supply options to further modify the tokenization—see [Tokenization Modifiers](1588024-tokenization-modifiers.md).

In addition, with CFStringTokenizer:

- You can de-compound German compounds
- You can identify the language used in a string (using [CFStringTokenizerCopyBestStringLanguage](<cfstringtokenizercopybeststringlanguage(____).md>))
- You can obtain Latin transcription for tokens

To find a token that includes the character specified by character index and set it as the current token, you call [CFStringTokenizerGoToTokenAtIndex](<cfstringtokenizergototokenatindex(____).md>). To advance to the next token and set it as the current token, you call [CFStringTokenizerAdvanceToNextToken](<cfstringtokenizeradvancetonexttoken(__).md>). To get the range of current token, you call [CFStringTokenizerGetCurrentTokenRange](<cfstringtokenizergetcurrenttokenrange(__).md>). You can use         [CFStringTokenizerCopyCurrentTokenAttribute](<cfstringtokenizercopycurrenttokenattribute(____).md>) to get the attribute of the current token. If the current token is a compound, you can call [CFStringTokenizerGetCurrentSubTokens](<cfstringtokenizergetcurrentsubtokens(________).md>) to retrieve the subtokens or derived subtokens contained in the compound token. To guess the language of a string, you call [CFStringTokenizerCopyBestStringLanguage](<cfstringtokenizercopybeststringlanguage(____).md>).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Tokenizer

- [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) — Returns a tokenizer for a given string.

### Setting the String

- [CFStringTokenizerSetString](<cfstringtokenizersetstring(______).md>) — Sets the string for a tokenizer.

### Changing the Location

- [CFStringTokenizerAdvanceToNextToken](<cfstringtokenizeradvancetonexttoken(__).md>) — Advances the tokenizer to the next token and sets that as the current token.
- [CFStringTokenizerGoToTokenAtIndex](<cfstringtokenizergototokenatindex(____).md>) — Finds a token that includes the character at a given index, and set it as the current token.

### Getting Information About the Current Token

- [CFStringTokenizerCopyCurrentTokenAttribute](<cfstringtokenizercopycurrenttokenattribute(____).md>) — Returns a given attribute of the current token.
- [CFStringTokenizerGetCurrentTokenRange](<cfstringtokenizergetcurrenttokenrange(__).md>) — Returns the range of the current token.
- [CFStringTokenizerGetCurrentSubTokens](<cfstringtokenizergetcurrentsubtokens(________).md>) — Retrieves the subtokens or derived subtokens contained in the compound token.

### Identifying a Language

- [CFStringTokenizerCopyBestStringLanguage](<cfstringtokenizercopybeststringlanguage(____).md>) — Guesses a language of a given string and returns the guess as a BCP 47 string.

### Getting the CFStringTokenizer Type ID

- [CFStringTokenizerGetTypeID](<cfstringtokenizergettypeid().md>) — Returns the type ID for CFStringTokenizer.

### Constants

- [Tokenization Modifiers](1588024-tokenization-modifiers.md) — Tokenization options are used with [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) to specify how the string should be tokenized
- [CFStringTokenizerTokenType](cfstringtokenizertokentype.md) — Token types returned by [CFStringTokenizerGoToTokenAtIndex](<cfstringtokenizergototokenatindex(____).md>) and [CFStringTokenizerAdvanceToNextToken](<cfstringtokenizeradvancetonexttoken(__).md>).

## See Also

### Related Documentation

- [String Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/introCFStrings.html#//apple_ref/doc/uid/10000131i)

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
