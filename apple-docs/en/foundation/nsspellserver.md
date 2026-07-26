---
title: NSSpellServer
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsspellserver
source_url: 'https://developer.apple.com/documentation/foundation/nsspellserver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsspellserver.json'
content_hash: 'sha256:f643b9ac339bdbd8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSSpellServer

<sub>Class</sub>

A server that your app uses to provide a spell checker service to other apps running in the system.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSSpellServer
```

## Overview

A **service provider** is an application that declares its availability in a standard way, so that any other applications that wish to use it can do so. If you build a spelling checker that makes use of the [NSSpellServer](nsspellserver.md) class and list it as an available service, then users of any application that makes use of [NSSpellChecker](../appkit/nsspellchecker.md) or includes a Services menu will see your spelling checker as one of the available dictionaries.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring Spelling Servers

- [delegate](nsspellserver/delegate.md) — Returns the receiver’s delegate.

### Providing Spelling Services

- [- registerLanguage:byVendor:](<nsspellserver/registerlanguage(__byvendor_).md>) — Notifies the receiver of a language your spelling checker can check.
- [- run](<nsspellserver/run().md>) — Causes the receiver to start listening for spell-checking requests.

### Managing the Spell-Checking Process

- [- isWordInUserDictionaries:caseSensitive:](<nsspellserver/isword(inuserdictionaries_casesensitive_).md>) — Indicates whether a given word is in the user’s list of learned words or the document’s list of words to ignore.

### Constants

- [Grammatical-Analysis Details](grammatical-analysis-details.md) — These constants are used as the keys in the outDetails dictionaries returned by [NSSpellServer](nsspellserver.md) and [checkGrammar(of:startingAt:language:wrap:inSpellDocumentWithTag:details:)](<../appkit/nsspellchecker/checkgrammar(of_startingat_language_wrap_inspelldocumentwithtag_details_).md>) ([NSSpellChecker](../appkit/nsspellchecker.md)).

## See Also

### Spelling and Grammar

- [NSSpellServerDelegate](nsspellserverdelegate.md) — The optional methods implemented by the delegate of a spell server.
