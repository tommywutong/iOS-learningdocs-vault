---
title: Spell Checking Programming Topics
apple_id: 10000092i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2004-02-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SpellCheck/Tasks/CreatingSpellServer.html
archived_at: '2026-07-15T07:19:21.173389Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Spell Checking Programming Topics](Introduction%20to%20Spell%20Checking.md)


[Next](Document%20Revision%20History.md)[Previous](Checking%20Text%20Spelling.md)

# Creating a Spell Server

The NSSpellServer class gives you
a way to make your particular spelling checker a service that’s
available to any application. A service is an application that
declares its availability in a standard way, so that any other applications
that wish to use it can do so. If you build a spelling checker that
makes use of the NSSpellServer class and list it as an available service,
then users of any application that makes use of NSSpellChecker or
includes a Services menu will see your spelling checker as one of
the available dictionaries.

To make use of NSSpellServer, you write a small program that
creates an NSSpellServer instance and a delegate of the server that
responds to messages asking it to find a misspelled word and to
suggest guesses to correct the misspelled word. Send the NSSpellServer `registerLanguage:byVendor:` messages
to tell it the languages your delegate can handle.

The program that runs your spelling checker should not be
built as an Application Kit application, but as a simple program.
Suppose you supply spelling checkers under the vendor name “Acme”
and the file containing the code for your delegate is called AcmeEnglishSpellChecker.
Then the following might be your program's main function:

```
void main()
{
    NSSpellServer *aServer = [[NSSpellServer alloc] init];
    if ([aServer registerLanguage:"English" byVendor:"Acme"]) {
        [aServer setDelegate:[[AcmeEnglishSpellChecker alloc] init]];
        [aServer run];
        fprintf(stderr, "Unexpected death of Acme SpellChecker!\n");
    else {
        fprintf(stderr, "Unable to check in Acme SpellChecker.\n");
    }
}
```

Your delegate is an instance of a custom
subclass. (It’s simplest to make it a subclass of NSObject, but
that's not a requirement.) Given an NSString, your delegate must
be able to find a misspelled word by implementing the method `spellServer:findMisspelledWordInString:language:wordCount:countOnly:`.
Usually, this method also reports the number of words it has scanned,
but that isn’t mandatory.

Optionally, the delegate may also suggest corrections for
misspelled words. It does so by implementing the method `spellServerS:suggestGuessesForWord:inLanguage:`.

When there’s more than one spelling checker available,
the user selects the one desired. The application that requests
a spelling check uses an NSSpellChecker object, and it provides
a Spelling panel; in the panel there’s a pop-up list of available
spelling checkers. Your spelling checker appears in that list if
it has a service descriptor.

A service descriptor is an entry in a text
file called services. Usually it’s located within the bundle that
also contains your spelling checker’s executable file. The bundle
(or directory) that contains the services file must have a name
ending in “`.service`”
or “.`app`”. The system looks
for service bundles in a standard set of directories.

A spell checker service availability notice has a
standard format, illustrated in the following example for the Acme
spelling checker:

```
Spell Checker: Acme
Language: French
Language: English
Executable: franglais.daemon
```

The first line identifies the type of service; for a spelling
checker, it must say “Spell Checker:” followed by your vendor
name. The next line contains the English name of a language your
spelling checker is prepared to check. (The language must be one
your system recognizes.) If your program can check more than one
language, use an additional line for each additional language. The
last line of a descriptor gives the name of the service’s executable
file. (It requires a complete path if it's in a different directory.)

If there’s a service descriptor for your Acme spelling checker
and also a service descriptor for the English checker provided by
a vendor named Consolidated, a user looking at the Spelling panel’s
pop-up list would see:

```
English (Acme)
English (Consolidated)
French (Acme)
```


The act of checking
spelling usually involves the interplay of objects in two classes:
the user application’s NSSpellChecker (which responds to interactions
with the user) and your spelling checker’s NSSpellServer (which
provides the application interface for your spelling checker). You
can see the interaction between the two in the following list of
steps involved in finding a misspelled word.

- The user of an application selects a menu item
  to request a spelling check. The application sends a message to
  its NSSpellChecker object. The NSSpellChecker in turn sends a corresponding
  message to the appropriate NSSpellServer.
- The NSSpellServer receives the message asking it to check
  the spelling of an NSString. It forwards the message to its delegate.
- The delegate searches for a misspelled word. If it finds one,
  it returns an NSRange identifying the word’s location in the string.
- The NSSpellServer receives a message asking it to suggest
  guesses for the correct spelling of a misspelled word, and forwards
  the message to its delegate.
- The delegate returns a list of possible corrections, which
  the NSSpellServer in turn returns to the NSSpellChecker that initiated
  the request.
- The NSSpellServer doesn’t know what the user does with the
  errors its delegate has found or with the guesses its delegate has
  proposed. (Perhaps the user corrects the document, perhaps by selecting
  a correction from the NSSpellChecker’s display of guesses; but
  that’s not the NSSpellServer’s responsibility.) However, if
  the user presses the Learn or Forget buttons (thereby causing the
  NSSpellChecker to revise the user’s word list), the NSSpellServer
  receives a notification of the word thus learned or forgotten. It’s
  up to you whether your spell checker acts on this information. If
  the user presses the Ignore button, the delegate is not notified
  (but the next time that word occurs in the text, the method `isWordInUserDictionaries:caseSensitive:` will
  report `YES` rather than `NO`).
- Once the NSSpellServer delegate has reported a misspelled
  word, it has completed its search. Of course, it’s likely that
  the user’s application will then send a new message, this time
  asking the NSSpellServer to check a string containing the part of
  the text it didn’t get to previously.

[Next](Document%20Revision%20History.md)[Previous](Checking%20Text%20Spelling.md)

