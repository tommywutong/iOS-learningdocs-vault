---
title: UITextChecker
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/uitextchecker/'
original_language: en
published: 2016-04-25
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:73df6a1aad830fd9'
translated: false
---

> 原文：[UITextChecker](https://nshipster.com/uitextchecker/)　·　NSHipster (Mattt)

# [UIText​Checker](https://nshipster.com/uitextchecker/)

Written by  [Croath Liu](https://nshipster.com/authors/croath-liu/)  April 25^th, 2016

Make no mistake, a tiny keyboard on a slab of glass doesn’t always lend itself to perfect typing. Whether for accuracy or hilarity, anyone typing on an iOS device notices when autocorrect steps in to help out. You might not know, however, that UIKit includes a class to help you with your user’s typing inside your app.

First introduced in iOS 3.2 (or should we call it iPhone OS 3.2, given the early date?), `UITextChecker` does exactly what it says: it checks text. Read on to learn how you can use this class for spell checking and text completion.

---

## Spell Checking

What happens if you mistype a word in iOS? Type “hipstar” into a text field and iOS will offer to autocorrect to “hipster” most of the time.

![Autocorrecting 'hipstar'](https://nshipster.com/assets/uitextchecker-hipstar-f8ef0b8b885609fdb7a68e50de286f6e9c12e224e9c64e92db0e094fbdba0b68d1e8d48985906952775b08055ded3e4760e9a94cf156f9409b8533acf33ee9fa.png)

We can find the same suggested substitution using `UITextChecker`:

```
import UIKit

let str = "hipstar"
let textChecker = UITextChecker()
let misspelledRange =
    textChecker.rangeOfMisspelledWord(in: str,
                                      range: NSRange(0..<str.utf16.count),
                                      startingAt: 0,
                                      wrap: false,
                                      language: "en_US")

if misspelledRange.location != NSNotFound,
    let firstGuess = textChecker.guesses(forWordRange: misspelledRange,
                                         in: str,
                                         language: "en_US")?.first
{
    print("First guess: \(firstGuess)") // First guess: hipster
} else {
    print("Not found")
}
```

```
NSString *str = @"hipstar";
UITextChecker *textChecker = [[UITextChecker alloc] init];
NSRange misspelledRange = [textChecker
                           rangeOfMisspelledWordInString:str
                           range:NSMakeRange(0, [str length])
                           startingAt:0
                           wrap:NO
                           language:@"en_US"];

NSArray *guesses = [NSArray array];
if (misspelledRange.location != NSNotFound) {
    guesses = [textChecker guessesForWordRange:misspelledRange
                                      inString:str
                                      language:@"en_US"];
    NSLog(@"First guess: %@", [guesses firstObject]);
    // First guess: hipster
} else {
    NSLog(@"Not found");
}
```

The returned array of strings _might_ look like this one:

```
["hipster", "hip star", "hip-star", "hips tar", "hips-tar"]
```

Or it might not—`UITextChecker` produces context- and device-specific guesses. According to the documentation, `guessesForWordRange(_:inString:language:)` “returns an array of strings, in the order in which they should be presented, representing guesses for words that might have been intended in place of the misspelled word at the given range in the given string.”

So no guarantee of idempotence or correctness, which makes sense for a method with `guesses...` in the name. How can NSHipsters trust a method that changes its return value? We’ll find the answer if we dig further.

## Learning New Words

Let’s assume that you want your users to be able to type `"hipstar"` exactly. Let your app know that by telling it to learn the word, using the `UITextChecker.learnWord(_:)` class method:

```
UITextChecker.learnWord(str)
```

```
[UITextChecker learnWord:str];
```

`"hipstar"` is now a recognized word for the whole device and won’t show up as misspelled in further checks.

```
let misspelledRange =
    textChecker.rangeOfMisspelledWord(in: str,
                                      range: NSRange(0..<str.utf16.count),
                                      startingAt: 0,
                                      wrap: false,
                                      language: "en_US")
misspelledRange.location == NSNotFound // true
```

```
NSRange misspelledRange = [textChecker
                           rangeOfMisspelledWordInString:str
                           range:NSMakeRange(0, [str length])
                           startingAt:0
                           wrap:NO
                           language:@"en_US"];
// misspelledRange.location == NSNotFound
```

As expected, the search above returns `NSNotFound`, for `UITextChecker` has learned the word we created. `UITextChecker` also provides class methods for checking and unlearning words: `UITextChecker.hasLearnedWord(_:)` and `UITextChecker.unlearnWord(_:)`.

## Suggesting Completions

There’s one more `UITextChecker` API, this time for finding possible completions for a partial word:

```
let partial = "hipst"
let completions = textChecker.completions(
                    forPartialWordRange: NSRange(0..<partial.utf16.count),
                    in: partial,
                    language: "en_US"
                  )
completions == ["hipster", "hipsters", "hipster's"] // true
```

```
NSString *partial = @"hipst";
NSArray *completions = [textChecker
                        completionsForPartialWordRange:NSMakeRange(0, [partial length])
                        inString:partial
                        language:@"en_US"];
// completions == ["hipster", "hipsters"]
```

`completionsForPartialWordRange` gives you an array of possible words from a group of initial characters. Although the documentation states that the returned array of strings will be sorted by probability, `UITextChecker` only sorts the completions alphabetically. `UITextChecker`’s OS X-based sibling, `NSSpellChecker`, does behave as it describes.

> You won’t see any of the custom words you’ve taught `UITextChecker` show up as possible completions. Why not? Since vocabulary added via `UITextChecker.learnWord(_:)` is global to the device, this prevents your app’s words from showing up in another app’s autocorrections.

---

Building an app that leans heavily on a textual interface? Use `UITextChecker` to make sure the system isn’t flagging your own vocabulary. Writing a keyboard extension? With `UITextChecker` and `UILexicon`, which provides common and user-defined words from the system-wide dictionary and first and last names from the user’s address book, you can support nearly any language without creating your own dictionaries!
