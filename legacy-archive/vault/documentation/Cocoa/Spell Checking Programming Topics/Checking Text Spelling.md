---
title: Spell Checking Programming Topics
apple_id: 10000092i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2004-02-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SpellCheck/Tasks/CheckingTextSpelling.html
archived_at: '2026-07-15T07:19:20.661428Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Spell Checking Programming Topics](Introduction%20to%20Spell%20Checking.md)


[Next](Creating%20a%20Spell%20Server.md)[Previous](Spell%20Checker.md)

# Checking Text Spelling

To check the spelling of some text, an application performs
the following actions:

- Includes in its user interface a menu item (or
  a button or command) by which the user will request spell checking.
- Makes the text to be checked available as an NSString object.
- Creates an instance of the NSSpellChecker class and sends
  it a `checkSpellingOfString:startingAt:` message.

For example, you might use the following statement to create
a spell checker:

```
range = [[NSSpellChecker sharedSpellChecker] checkSpellingOfString:aString startingAt:0];
```

The `checkSpellingOfString:startingAt:` method
checks the spelling of the words in the specified string beginning
at the specified offset (this example uses 0 to start at the beginning
of the string) until it finds a word that is misspelled. Then it
returns an NSRange to indicate the location of the misspelled word.

In a graphical application, whenever a misspelled word is
found, you’ll probably want to highlight the word in the document,
using the NSRange that `checkSpellingOfString:startingAt:` returns
to determine the text to highlight. Then you should show the misspelled
word in the Spelling panel’s misspelled-word field by calling `updateSpellingPanelWithMisspelledWord:`.
If `checkSpellingOfString:startingAt:` does
not find a misspelled word, you should call `updateSpellingPanelWithMisspelledWord:` with
the empty string. This causes the system to beep, letting the user
know that the spell check is complete and no misspelled words were
found. None of these steps is required, but if you do one, you should
do them all.

The object that provides the string being checked should adopt
the following protocols:

| Protocol | Description |
| --- | --- |
| NSChangeSpelling | A message in this protocol (`changeSpelling:`) is sent down the responder chain when the user presses the Correct button. |
| NSIgnoreMisspelledWords | When the object being checked responds to this protocol, the spell server keeps a list of words that are acceptable in the document and enables the Ignore button in the Spelling panel. |

The application may choose to split a document’s text into
segments and check them separately. This is necessary when the text
has segments in different languages. Spell checking is invoked for
one language at a time, so a document that contains portions in three
languages requires at least three checks.

The
process of checking spelling makes use of three references:

- A dictionary registered with the system’s spell-checking
  service. When the Spelling panel first appears, by default it shows
  the dictionary for the user’s preferred language. The user may
  select a different dictionary from the list in the Spelling panel.
- The user’s “learn” list of correctly-spelled words in
  the current language. The NSSpellChecker updates the list when the
  user presses the Learn or Forget buttons in the Spelling panel.
- The document’s list of words to be ignored while checking
  it (if the first responder conforms to the NSIgnoreMisspelledWords
  protocol). The NSSpellChecker updates its copy of this list when
  the user presses the Ignore button in the Spelling panel.

A word is considered to be misspelled if none of these three
accepts it.

The NSString being checked isn’t the same as the document.
In the course of processing a document, an application might run
several checks based on different parts or different versions of
the text, but they all belong to the same document. The NSSpellChecker
keeps a separate “ignored words”
list for each document that it checks. To help match “ignored words”
lists to documents, you should call `uniqueSpellDocumentTag` once
for each document. This method returns a unique arbitrary integer
that will serve to distinguish one document from the others being
checked and to match each “ignored words” list to a document.
When searching for misspelled words, pass the tag as the fourth
argument of `checkSpellingOfString:startingAt:language:wrap:inSpellDocumentWithTag:wordCount:`. (The
convenience method `checkSpellingOfString:startingAt:` takes
no tag. This method is suitable when the first responder does
not conform to the NSIgnoreMisspelledWords protocol.)

When the application saves a document, it may choose to retrieve
the “ignored words” list and save it along with the document.
To get back the right list, it must send the NSSpellChecker an `ignoredWordsInSpellDocumentWithTag:` message.
When the application has closed a document, it should notify the
NSSpellChecker that the document’s “ignored words” list can
now be discarded, by sending it a `closeSpellDocumentWithTag:` message. When
the application reopens the document, it should restore the “ignored
words” list with the message `setIgnoredWords:inSpellDocumentWithTag:`.

[Next](Creating%20a%20Spell%20Server.md)[Previous](Spell%20Checker.md)

