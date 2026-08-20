---
title: Speech Synthesis Programming Guide
apple_id: TP40004365
resource_type: Guide
platform: macOS
topic: User Experience
technology: ApplicationServices
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/SpeechSynthesisProgrammingGuide/FineTuning/FineTuning.html
archived_at: '2026-07-18T02:12:49.645587Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Speech Synthesis Programming Guide](Introduction%20to%20Speech%20Synthesis%20Programming%20Guide.md)


[Next](Syntax%20of%20Embedded%20Speech%20Commands.md)[Previous](Designing%20and%20Implementing%20an%20Application%20That%20Speaks.md)

# Techniques for Customizing Synthesized Speech

This chapter describes how to fine-tune the speech your application generates. It provides guidelines for using speech synthesis APIs and embedded speech commands and it includes a number of examples of specific tasks. This chapter also describes several ways you can improve your application’s spoken output. If you need fine-grained control over the generated speech in your application, you should read this chapter to learn how to take advantage of the advanced features of the Speech Synthesis framework.

Some of the advanced techniques described in this chapter are supported only by the Carbon speech synthesis API, although any application that has access to the Application Services framework can use them. If you haven’t decided which API to use, you should read [Carbon and Cocoa Speech Synthesis APIs Compared](Designing%20and%20Implementing%20an%20Application%20That%20Speaks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnbnknltc) to find out which API supports the level of customization you want to implement. Other techniques described in this chapter involve the use of embedded speech commands and other text modifiers, which are available to all applications.

The Carbon speech synthesis API allows you to get and set speech attributes, such as rate and volume, and specify other settings on speech channels, such as input mode. In addition to a couple of functions that focus on specific attributes, the Carbon speech synthesis API defines the [GetSpeechInfo](https://developer.apple.com/documentation/applicationservices/1552220-getspeechinfo) and [SetSpeechInfo](https://developer.apple.com/documentation/applicationservices/1552223-setspeechinfo) functions, which act upon a speech channel using an attribute, setting, or other value specified in a selector parameter. This section describes how you can use the attribute-specific functions and the `SetSpeechInfo` function to adjust the speech attributes and other settings on speech channels.

The Carbon speech synthesis API defines the following functions to get and set the rate and pitch attributes on a speech channel:

- [GetSpeechRate](https://developer.apple.com/documentation/applicationservices/1460797-getspeechrate)
- [SetSpeechRate](https://developer.apple.com/documentation/applicationservices/1459896-setspeechrate)
- [GetSpeechPitch](https://developer.apple.com/documentation/applicationservices/1464774-getspeechpitch)
- [SetSpeechPitch](https://developer.apple.com/documentation/applicationservices/1462674-setspeechpitch)

For example, an application might get a new speech rate value from the user and use it to change the speech rate used by the speech channel, as shown below:

```
/* fRateField is associated with a button in the UI and fCurSpeechChannel is a pointer to a speech channel structure created earlier in the application. */
Fixed theNewValue   = [fRateField doubleValue] * 65536.0;
theErr = SetSpeechRate(fCurSpeechChannel, theNewValue);
```

In a similar way, an application can use the `SetSpeechPitch` function to set a speech channel’s pitch attribute to a new value. To get or set other speech attributes and settings on a speech channel, however, you use the `GetSpeechInfo` and `SetSpeechInfo` functions with the appropriate selectors. The one exception to this is the rate attribute, which can be retrieved and set using either the `GetSpeechRate` and `SetSpeechRate` functions mentioned above or the `SetSpeechInfo` function with the `soRate` selector, as shown below:

```
/* As above, fRateField is associated with a button in the UI and fCurSpeechChannel is a pointer to a speech channel structure created earlier in the application. */
Fixed theNewValue   = [fRateField doubleValue] * 65536.0;
theErr = SetSpeechInfo(fCurSpeechChannel, soRate, &theNewValue);
```

The selectors defined in the Carbon speech synthesis API act upon a wide range of properties associated with speech channels. The selectors divide into the following categories:

- Attribute selectors, which specify a speech attribute, such as volume or rate, that the speech channel should use when generating speech.

  All attribute selectors work with both the `GetSpeechInfo` and `SetSpeechInfo` functions. As an alternative to using an attribute selector with the `SetSpeechInfo` function, you can use an equivalent embedded speech command to set a speech attribute (see [Table 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnjnknltm) for more about these commands). The currently available selectors in this category are:

  - `soRate`
  - `soPitchBase`
  - `soPitchMod`
  - `soVolume`
- Input-mode selectors, which specify the mode, such as phoneme or character, that the speech channel should use when processing text.

  All input-mode selectors work with both the `GetSpeechInfo` and `SetSpeechInfo` functions. As an alternative to using a mode selector with the `SetSpeechInfo` function, you can use an equivalent embedded speech command to specify an input-processing mode (see [Table 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnjnknltm) for more about these commands). The currently available selectors in this category are:

  - `soInputMode`
  - `soCharacterMode`
  - `soNumberMode`
- Callback selectors, which associate with a speech channel an application-defined callback function to be called when a particular speech event occurs, such as the conclusion of speech.

  All callback selectors work with only the `SetSpeechInfo` function. One callback selector, `soSyncCallBack`, has a related embedded speech command you can use to trigger a callback to your synchronization callback procedure (see [Table 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnjnknltm) for more about this command). The currently available selectors in this category are:

  - `soTextDoneCallBack`
  - `soSpeechDoneCallBack`
  - `soSyncCallBack`
  - `soErrorCallBack`
  - `soPhonemeCallBack`
  - `soWordCallBack`
- Information selectors, which provide information about the current speech channel and the synthesizer associated with it, such as the set of phoneme symbols recognized by the synthesizer.

  All information selectors work only with the `GetSpeechInfo` function. There are no embedded speech commands equivalent to the information selectors. The currently available selectors in this category are:

  - `soStatus`
  - `soErrors`
  - `soSynthType`
  - `soRecentSync`
  - `soPhonemeSymbols`
- Setting selectors, which specify a speech channel setting, such as the current voice.

  Some setting selectors work with both the `GetSpeechInfo` and `SetSpeechInfo` functions, others with only the `SetSpeechInfo` function. One setting selector, `soCommandDelimiter`, has an equivalent embedded speech command you can use to change the default command delimiter strings (see [Table 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnjnknltm) for more about this command). The currently available selectors in this category are:

  - `soCurrentVoice`
  - `soCommandDelimiter`
  - `soReset`
  - `soRefCon`
  - `soSynthExtension`
  - `soOutputToFileWithCFURL`

As described in [Control Speech Quality Using Embedded Speech Commands](Speech%20Synthesis%20in%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqmznknltk), you use embedded commands to fine-tune the pronunciation of individual words in the text your application passes to a synthesizer. Even if you use only a few of the embedded speech commands described in this section, you may significantly increase the understandability of your application’s spoken output. This section provides an overview of embedded speech command syntax, lists the available commands, and illustrates how to use them to achieve different effects.

Note that some embedded speech commands have functional equivalents provided by the Carbon selector mechanism (for a complete list of available selectors, see _[Speech Synthesis Manager Reference](https://developer.apple.com/documentation/applicationservices/speech_synthesis_manager)_.) This means that to achieve some effects, you can either insert the embedded command in the text, or you can pass the equivalent selector to the Carbon `SetSpeechInfo` function. If you use the `SetSpeechInfo` function (described in [Adjust Speech Channel Settings Using the Carbon Speech Synthesis API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnjnknltcmy)), the effect applies to all speech passing through the current speech channel, subject to synthesizer capabilities. If you use the embedded command to achieve the same effect, however, it applies only to the word immediately preceded by the embedded command.

When processing an input string or buffer, speech synthesizers look for special strings of characters called command delimiters. These character strings are usually defined to be pairings of printable characters that do not typically appear in the text. One character string is defined as the begin command delimiter and another character string is defined as the end command delimiter. When the synthesizer encounters the begin command delimiter string, it interprets the characters following it as one or more embedded commands until it reaches the end command delimiter string.

The default begin and end command delimiter strings recognized by the MacinTalk synthesizer are “[[“ and “]],“ respectively. You can change these strings if necessary, but you should take care to use printable characters that you do not expect to see in the text your application processes. Also, if you change the default delimiters, be sure to change them back to the default characters when you have finished with the text, because the change is persistent for the current speech channel. For example, if you expect square brackets to appear in the text you’ll be sending to the synthesizer, you can change the default command delimiters to strings containing other printable characters that do not naturally occur in your text.

You can disable the processing of all embedded commands by setting both the begin and end command delimiters to two NUL bytes. You might want to do this if your application speaks text over which you have no control and you’re absolutely sure the text contains no embedded commands. To disable processing of embedded commands programmatically, use the `soCommandDelimiter` selector with the `SetSpeechInfo` function, as shown below:

```
// Create a structure to hold the new delimiter values
DelimiterInfo MyNewDelimiters;
MyNewDelimiters.startDelimiter[0] = 0;
MyNewDelimiters.startDelimiter[1] = 0;
MyNewDelimiters.endDelimiter[0] = 0;
MyNewDelimiters.endDelimiter[1] = 0;
SetSpeechInfo(CurrentSpeechChannel, soCommandDelimiter, &MyNewDelimiters);
```


All embedded commands consist of a 4-character command code and a parameter, enclosed by the begin and end command delimiter strings. For example, the `emph` command requires a parameter that tells the synthesizer to increase or decrease the emphasis with which to speak the next word, as shown below:

`[[emph +]]` The + parameter tells the synthesizer to increase emphasis for the following word.

More than one command may occur within a single pair of delimiter strings if they are separated by semicolons, as shown below:

`[[emph +; rate 165]]` Together, these commands tell the synthesizer to speak the following word or phrase with increased emphasis and at a rate of 165 words per minute.

A parameter may consist of a string, a numeric type, or an operating-system type, and may be accompanied by the + or - characters (the exact format of a parameter depends on the command with which it’s associated). Some commands allow you to use the parameter to specify either an absolute value or a relative value. For example, the `volm` command allows you to specify a particular volume or an amount by which to increase or decrease the current volume, as shown below:

`[[volm 0.3]]` This command sets the volume with which the following word is spoken to 0.3.

`[[volm +0.1]]` This command increases the volume with which the following word is spoken by 0.1.

The speech synthesizer ignores all whitespace within an embedded command, so you may insert as many spaces as you need to make your command text more readable.

In addition, this document uses the following characters to express the syntax of embedded speech commands (these characters do not appear in actual embedded speech commands):

- The < and > characters enclose items that represent logical units, such as string, character, integer, or real value. When you insert an embedded command in your text, you replace the logical unit with an actual value. For example, you might replace "`<RealValue>`“ with `3.0`. For precise definitions of each logical unit, see the formal description of the syntax in [Syntax of Embedded Speech Commands](Syntax%20of%20Embedded%20Speech%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnznknltc).
- The | character means “or" and appears between members in a list of possible items, any single one of which may be used. For example, the `emph` command accepts either the + character or the - character for its parameter. Therefore, the syntax of the `emph` command is expressed as `emph + | -`.
- The [ and ] characters enclose an optional item or list of items. For example, the `rate` command accepts the optional addition of the + or - character to its numerical parameter to indicate a change relative to the current value. Therefore, the syntax of the `rate` command is expressed as `rate [+ | -] <RealValue>`.
- Items followed by an ellipsis character (...) may be repeated one or more times.

Table 3-1 describes the embedded speech commands, their parameters, equivalent speech information selectors (if they exist), and in which versions of OS X the commands are available. The syntax of each command in Table 3-1 is expressed using the conventions described in [Overview of Embedded Speech Command Syntax](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnjnknltcmq).

__Table 3-1__  Embedded speech commands

| Command | Syntax and description | Selector |
| `char` | `char NORM | LTRL`  The character mode command sets the word-speaking mode of the speech channel. When the `NORM` parameter is used, the synthesizer attempts to automatically convert words into speech. This is the most basic function of the synthesizer. When the `LTRL` parameter is used, the synthesizer speaks the individual characters of every word, number, and symbol following the command (all other embedded commands are processed normally). For example, to cause the synthesizer to speak the word “cat” as “C-A-T,” you would include the following in a text buffer or string:  `[[char LTRL]] cat [[char NORM]]` | `SoCharacterMode` |
| `cmnt` | `cmnt [<Character>...]`  The comment command is ignored by speech synthesizers. It enables you to add arbitrary content to the text buffer that will never be included in the spoken output. Note that the comment text itself must be included within the begin and end command delimiters of the `cmnt` command.  `[[cmnt This is a comment that will be ignored by the synthesizer.]]` | None |
| `ctxt` | `ctxt [WSKP | WORD | NORM | TSKP | TEXT]`  The context command allows you to identify the context of a word to help the synthesizer generate the correct pronunciation of that word, even if no other words in the surrounding phrase or sentence are spoken. Because the pronunciation of words can be different depending on the context in which they appear, you can use the context command to specify the pronunciation used in a particular context.  The context command recognizes two modes: word-by-word and text fragment. In both modes, you use the appropriate “skip” parameter (`WSKP` or `TSKP`) to identify the text that provides context and the `WORD` or `TEXT` parameter to identify the word or phrase whose pronunciation is affected by the context. The synthesizer parses the entire phrase or sentence to determine the correct pronunciation of the word or phrase, but does not speak the portions of the text marked as “skipped.“ Use the `[[ctxt NORM]]` command to signal a return to the default input-processing mode.  In word-by-word mode, the synthesizer parses the complete text selection to determine the part of speech (such as noun or verb) of the specified word. The synthesizer pronounces the word according to its part of speech, but it does not make any intonation or duration adjustments to the pronunciation. For example, the word “coordinates” is pronounced differently depending on whether it is used as a noun or a verb. The two sentences below illustrate how to use the context command to tell the synthesizer which pronunciation of the word to use:  `[[ctxt WSKP]] GPS provides [[ctxt WORD]] coordinates. [[ctxt NORM]]`  `[[ctxt WSKP]] The post office [[ctxt WORD]] coordinates [[ctxt WSKP]] its deliveries. [[ctxt NORM]]`  In text fragment mode, the synthesizer parses the complete text selection to determine the part of speech and the intonation and duration of the specified word or phrase. For example, the different pronunciations of the phrase “first step” are informed by the context provided by the surrounding words in the following two sentences:  `[[ctxt TSKP]] Your [[ctxt TEXT]] first step [[ctxt TSKP]] should be to relax. [[ctxt NORM]]`  `[[ctxt TSKP]] To relax should be your [[ctxt TEXT]] first step. [[ctxt NORM]]` | None |
| `dlim` | `dlim <BeginDelimiter> <EndDelimiter>`  The delimiter command changes the character sequences that indicate the beginning and end of all subsequent embedded speech commands. The new delimiters take effect after the command list containing the `dlim` command has been completely processed. If the delimiter strings are empty, an error is generated. If you want to disable embedded command processing for the remainder of the text buffer, you can pass two NUL bytes in the `BeginDelimiter` and `EndDelimiter` parameters.  [`[dlim $$ $$]` | `soCommandDelimiter` |
| `emph` | `emph + | -`  The emphasis command causes the synthesizer to speak the next word with greater or less emphasis than it is currently using. The + parameter increases emphasis and the - parameter decreases emphasis.  For example, to emphasize the word “not” in the following phrase, use the `emph` command as follows:  `Do [[emph +]] not [[emph -]] over tighten the screw.` | None |
| `inpt` | `inpt TEXT | PHON | TUNE`  The input mode command switches the input-processing mode to textual mode, phoneme mode, or TUNE format mode. Note that some synthesizers may define additional speech input modes you can use. The default input-processing mode is textual, and you should always use the `[[inpt TEXT]]` command to revert to textual mode after you’re finished providing content in one of the other modes. In phoneme mode, the synthesizer interprets characters as representing phonemes (listed in [Phonemes](Phonemes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqojnknltc)). In the TUNE format mode, the synthesizer recognizes the same set of phonemes but also interprets additional information that specifies a precise spoken contour, or tune, for the words. For more information about the TUNE format, see [Use the TUNE Format to Supply Complex Pitch Contours](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnjnknlto).  For example, to supply the phonemic representation of a name that synthesizers frequently mispronounce, you can use the `inpt` command as follows:  `My name is [[inpt PHON]] AY1yIY2SAX [[inpt TEXT]].` | `soInputMode` |
| `nmbr` | `nmbr NORM | LTRL`  The number mode command sets the number-speaking mode of the synthesizer. The `NORM` parameter causes the synthesizer to speak the number 46 as “forty-six,” whereas the `LTRL` parameter causes the synthesizer to speak the same number as “four six.“  For example, to make it clear that the following 7-digit number is a phone number, you can use the `nmbr` command to tell the synthesizer to say each digit separately, as follows:  `Please call me at [[nmbr LTRL]] 5551990 [[nmbr NORM]].` | `soNumberMode` |
| `pbas` | `pbas [+ | -] <RealValue>`  The baseline pitch command changes the current speech pitch for the speech channel to the specified real value. If the pitch value is preceded by the + or - character, the speech pitch is adjusted relative to its current value. Baseline pitch values are always positive numbers in the range of 1.000 to 127.000. | `soPitchBase` |
| `pmod` | `pmod [+ | -] <RealValue>`  The pitch modulation command changes the modulation range for the speech channel, based on the specified modulation-depth real value. | `soPitchMode` |
| `rate` | `rate [+ | -] <RealValue>`  The speech rate command sets the speech rate on the speech channel to the specified real value. Speech rates fall in the range 0.000 to 65535.999, which translates into a range of 50 to 500 words per minute. If the rate is preceded by a + or - character, the speech rate is increased or decreased relative to its current value. | `soRate` |
| `rset` | `rset <32BitValue>`  The reset command resets the speech channel’s voice and attributes to default values. The parameter has no effect; it should be set to `0`. | `soReset` |
| `slnc` | `slnc <32BitValue>`  The silence command causes the synthesizer to generate silence for the specified number of milliseconds. You might want to insert extra silence between two sentences to allow listeners to fully absorb the meaning of the first one. Note that the precise timing of the silence will vary among synthesizers. | none |
| `sync` | `sync <32BitValue>`  The synchronization command causes an application’s synchronization callback procedure to be executed. The callback is made as the audio corresponding to the next word begins to sound. The 32-bit value is set by the application and is passed to the callback procedure.  You can use the `sync` command to trigger a callback at times other than those defined by the built-in callbacks (such as the phoneme and speech-done callbacks). For example, you might want to perform some custom processing each time a date is spoken to highlight its place on a graphical timeline. To do this, you would define a synchronization callback procedure and refcon values, and insert a `sync` command after each date in the text, as follows:  `In 1066 [[sync 0x000000A1]], William the Conqueror invaded England and by 1072 [[sync 0x000000A2]], the whole of England was conquered and united.` | `soSyncCallback` |
| `vers` | `vers <32BitValue>`  The format version command tells the speech synthesizer which embedded command format version will be used by all subsequent embedded speech commands. | none |
| `volm` | `volm [+ | -] <RealValue>`  The speech volume command sets the speech volume on the current speech channel to the specified real value. If the volume value is preceded by a + or - character, the speech volume is increased or decreased relative to its current value. | `soVolume` |
| `xtnd` | `xtnd <OSType> [<Parameter> ...]`  The synthesizer-specific `xtnd` command enables other synthesizer-specific commands to be embedded in the text. The first parameter (`OSType`) must be the creator ID of the synthesizer. The remaining optional parameters are synthesizer-specific. | `soSynthExtension` |

While embedded speech commands are being processed, errors might be detected and reported to your application. If you enable error callbacks using the `SetSpeechInfo` function with the `soErrorCallBack` selector, your error callback procedure will be executed once for every error that is detected (for more information on the error callback, see [SpeechErrorProcPtr](https://developer.apple.com/documentation/applicationservices/speecherrorprocptr)). If you don’t enable error callbacks, you can still get information about these errors by calling the `GetSpeechInfo` function with the `soErrors` selector.

During processing of embedded speech commands, the following errors can be detected:

| Result code | Value | Description |
| --- | --- | --- |
| `badParmVal` | `-245` | Parameter value is invalid |
| `badCmdText` | `-246` | Embedded command syntax or parameter problem |
| `unimplCmd` | `-247` | Embedded command is not implemented on synthesizer |
| `unimplMsg` | `-248` | Unimplemented message |
| `badVoiceID` | `-250` | Specified voice has not been preloaded |
| `badParmCount` | `-252` | Incorrect number of embedded command arguments |

As described in [Representations of Speech](Speech%20Synthesis%20in%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqmznknltc), the Speech Synthesis framework allows you to represent some or all of the words in a string or buffer as phonemes. When you supply the phonemic representation of a word, you specify the precise combination of sounds you want the synthesizer to pronounce. In addition, you can add phoneme modifiers to increase or decrease the stress with which phonemes and words are pronounced.

Recall that phonemes are represented by combinations of uppercase or lowercase characters, such as OW for the long “o” sound in the English word “boat.“ (Other languages use different phonemes and phoneme symbols; this document focuses on the set of North American English phonemes the MacinTalk synthesizer recognizes.) The complete set of phonemes is listed in [Phonemes](Phonemes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqojnknltc).

Because a synthesizer has no reliable way to detect the difference between characters that represent phonemes and characters that represent words, you must state the appropriate mode. There are two ways you can do this:

- In your application, use the `soPhonemeMode` selector with the `SetSpeechInfo` function to tell the current speech channel to process subsequent text as phonemes. This is a mode change for the speech channel, which means that it will interpret _all_ text as phonemes until you call the `SetSpeechInfo` function with the `soTextMode` selector, to return to the default, text-processing mode (or until the speech channel closes). For examples of how to use this function, see [Adjust Speech Channel Settings Using the Carbon Speech Synthesis API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnjnknltcmy).
- In your text buffer or string, precede the phonemic representation of a word or phrase with the `[[inpt PHON]]` embedded speech command and follow it with the `[[inpt TEXT]]` command. This causes the synthesizer to switch to the phoneme input-processing mode for the content after the `[[inpt PHON]]` command and switch back again when it encounters the `[[inpt TEXT]]` command.

Within the phonemic representation of a word or phrase, you can insert modifiers that allow you to adjust the stress the synthesizer places on words and syllables. These modifiers are called prosodic controls.

Unlike embedded speech commands, prosodic controls do not require command delimiter strings and they do not allow parameters. Because prosodic controls are valid only within the phonemic representation of text, the symbols that represent them consist of characters that are not used to represent phonemes. To use prosodic control symbols in the phonemic representation of your text, place the appropriate symbol before the phoneme you want to modify. The effect of the prosodic control symbol is limited to the phoneme that immediately follows it; it has no effect on any subsequent phonemes.

Table 3-2 lists the available prosodic control symbols and describes how they modify individual phonemes. If you’d like to listen to the spoken version of any of the examples in Table 3-2, you can copy it to a Text Edit document, precede it with the `[[inpt PHON]]` command, and select Speech > Start Speaking Text from the Services menu item.

__Table 3-2__  Prosodic control symbols and descriptions

| Category | Action | Symbol | Description and example |
| Lexical stress | Primary stress | 1 | Marks the primary stress within a word  For example, the word “developer” is pronounced with the primary stress on the second syllable, as shown below:  `dIHv1EHlAXpAXr` |
|  | Secondary stress | 2 | Marks the secondary stress within a word  For example, the word “application” is pronounced with the primary stress on the third syllable and a secondary stress on the first syllable, as shown below:  `2AEplIHk1EYSIXn` |
| Syllable breaks | Syllable mark | = (equal) | Marks syllable breaks within a word  For example, the word “cheaply” is pronounced with a subtle syllable break between “cheap” and “ly.” To ensure that a synthesizer pronounces this word correctly (and not with a syllable break between “chea” and “ply”), you can insert a syllable mark, as shown below:  `C1IYp=lIY` |
| Word prominence | Destressed | ~ (tilde) | Marks words that should be destressed in a sentence  Words that carry minimal information can be destressed to lessen their prominence in a sentence. For example, in the sentence “What is in the bag?,“ the words “in” and “the” are unimportant, relative to “What,” “is,” and “bag.” Therefore, “in” and “the” can be marked as not needing stress, as shown below:  `_w1UXt _1IHz ~2IHn ~nAX _b1AEg?` |
|  | Normal stress | _ (underscore) | Marks words that should receive normal stress  Words that bear information should be spoken with normal stress to differentiate them from less important words. For example, in the sentence “What is in the bag?,“ the words “What,“ “is,“ and “bag” should be spoken with normal stress because they convey more information to the listener than the words “in” and “the.“ Therefore, these information-bearing words can be marked as needing normal stress, as shown below:  `_w1UXt _1IHz ~2IHn ~nAX _b1AEg?` |
|  | Emphatic stress | + (plus) | Marks words that require special emphasis  The most important words in a sentence should receive emphatic stress to make them stand out from the rest of the sentence. For example, in the sentence “Don’t ever do that again!,“ the word “that” can be given extra emphasis to draw attention to it, as shown below:  `~dOWnt ~1EHvAXr ~d1UW +DAEt _AXg1EHn!` |

Punctuation marks are not embedded commands, but they appear in text and can affect the prosody of synthesized speech in some similar ways. This section describes how English-language synthesizers are likely to interpret punctuation marks.

For the most part, punctuation marks affect the pitch of synthesized speech and the duration of pauses. For example, the period at the end of a sentence generally causes a synthesizer to lower the pitch and insert a pause. Most speech synthesizers strive to mimic the pauses and changes in pitch of human speakers in response to punctuation marks, so you’ll obtain the best results by punctuating your text according to standard grammatical rules.

Table 3-3 lists the standard English punctuation marks and how they affect sentence prosody. Be aware that some languages do not use some of these punctuation marks, so synthesizers for other languages might not interpret them as described in Table 3-3, if at all.

__Table 3-3__  Effects of punctuation marks on synthesized speech

| Symbol | Effect on pitch | Effect on timing |
| , | Rise in pitch | Short pause follows |
| ( | Start range of reduced pitch | Short pause follows |
| ) | End range of reduced pitch | Short pause follows |
| . | Fall in pitch | Pause follows |
| " | Expand pitch range | A short pause precedes an opening quote and follows a closing quote |

Even among English-language synthesizers, the specific pitch contours associated with the punctuation marks listed in Table 3-3 might vary according to other considerations arising from analysis of the text. For example, if a synthesizer determines that a question is rhetorical, the pitch might fall at the question mark, instead of rise. Also, the timing effects associated with the punctuation marks can vary according to current speech rate settings. Consequently, you should view the information in Table 3-3 as guidance only; test your application’s spoken output with a particular synthesizer to find out how the punctuation is actually interpreted.

In addition to supporting the phoneme input-processing mode, the MacinTalk synthesizer available in OS X v10.2 and later supports the TUNE input-processing mode. This mode accepts directives in the TUNE format, which allows you to supply a complex pitch contour, or tune, with which a word or phrase should be spoken. Such a tune can represent the pitch and speech-rate changes you hear when a person speaks in an expressive way. For example, adults speaking to small children often vary the pitch of their speech much more than they do when speaking to other adults. As described in [Use Phoneme Modifiers to Adjust Pronunciation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnjnknlti), phoneme modifiers can be used to adjust the stress placed on particular phonemes, but you cannot use them to cause multiple variations in pitch during the pronunciation of a single phoneme. To do this, you must use the TUNE format.

Apple provides the Repeat After Me developer tool to help you create the set of symbols that describe a tune. Using the Repeat After Me application (located in `/Developer/Applications/Utilities/Speech`), you can record an utterance that exhibits your desired pitch contour and use that to shape any other utterance in your application.

Similar to the way you enter and exit the phoneme input-processing mode, you use the `inpt` embedded command to turn on and off the TUNE input-processing mode. Specifically, you insert `[[inpt TUNE]]` before the content in the TUNE format and insert `[[inpt TEXT]]` after it. The TUNE format recognizes the same set of phoneme symbols used in the phoneme input-processing mode (see [Phonemes](Phonemes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqojnknltc) for a description of these symbols).

The TUNE format defines a command syntax you use to specify pitch and duration attributes for each phoneme. Each phoneme may be followed by a pair of braces, enclosing a single duration attribute, preceded by the symbol “D,” and an arbitrary number of pitch attributes, preceded by the symbol “P.“ The duration attribute indicates the total duration of the phoneme in milliseconds. Each pitch attribute consists of a pair of numbers separated by a colon. The first number is decimal value that specifies a pitch in hertz (Hz) and the second number is an integer that specifies the location of that pitch within the phoneme, expressed as an integer percentage of the total duration of the phoneme.

To illustrate the syntax of the TUNE format, consider the sentence “Are you sure you brushed your teeth?“ The default pronunciation of this sentence is perfectly understandable, but the intonation is uninteresting. (If you’re reading this document in Safari, Preview, or Xcode, select “Are you sure you brushed your teeth?“ and choose Speech > Start Speaking Text from the Services menu item to hear the default pronunciation.) Imagine that you want this sentence to be spoken as a parent might speak it to a child, with emphasis on “sure” and an exaggerated rise in pitch through the end of the sentence. Using the Repeat After Me application, you can record a person speaking the sentence in this way, apply the resulting pitch and duration information to the text, and get the representation in the TUNE format. Following this process, you might end up with something similar to the following:

```
[[inpt TUNE]] ~ AA {D 120; P 176.9:0 171.4:22 161.7:61} r {D 60; P 166.7:0} ~ y {D 210; P 161.0:0} UW {D 70; P 178.5:0} _ S {D 290; P 173.3:0 178.2:8 184.9:19 222.9:81} 1AX {D 280; P 234.5:0 246.1:39} r {D 170; P 264.2:0} ~ y {D 200; P 276.9:0 274.9:17 271.0:50} UW {D 40; P 265.0:0 264.3:50} _ b {D 140; P 263.6:0 263.5:13 263.3:60} r {D 110; P 263.1:0 260.4:43} 1UX {D 30; P 256.8:0 256.8:6} S {D 190; P 256.1:0} t {D 20; P 252.0:0 253.6:47} ~ y {D 30; P 255.5:0 257.8:45} AO {D 40; P 260.6:0 260.0:56} r {D 40; P 259.5:0} _ t {D 190; P 251.3:0 250.0:16 245.9:68} 1IY {D 260; P 243.4:0 248.1:8 286.1:72 288.5:84} T {D 220; P 291.6:0 262.8:27 220.0:67 184.8:100} ? {D 300} [[inpt TEXT]]
```

To listen to this version of the sentence, select the lines above (be sure to include the “`[[inpt TUNE]]`‘‘ at the beginning and the “`[[inpt TEXT]]`“ at the end), copy them, and paste them into a Text Edit document. Make sure all the lines are still selected and then select Speech > Start Speaking Text from the Services menu item in the Text Edit menu.

The TUNE format also includes optional settings that describe the beginning value and range of the pitch, expressed in hertz, and the speech rate, expressed in words per minute. You can use these settings to state the pitch and rate conditions that were in effect when you created the tune. If either of these settings have nonzero values, the synthesizer will scale the pitch and duration attribute values you supply for the phonemes according to voice conditions in effect during synthesis. This is analogous to transposing a song to a different key and playing it at a different tempo. If both of these settings are missing, the synthesizer interprets the pitch and duration attribute values as literal values that should be reproduced exactly, which is analogous to playing a song in the key and time signature in which it was composed.

As mentioned in [Notifications, Callbacks, and Speech Synchronization](Speech%20Synthesis%20in%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqmznknltcmy), you can synchronize your application’s spoken output with other tasks in your application. Both the Cocoa and the Carbon speech synthesis APIs provide mechanisms you can use to get notifications when, for example, a word or phoneme is about to be spoken or has just been spoken. This section describes how you can receive these notifications and some of the ways you might use them.

The `NSSpeechSynthesizer` class defines a few delegate methods you can use to synchronize tasks with speech-related actions. For example, you can implement the `speechSynthesizer:willSpeakWord:ofString` delegate method to highlight a word as it’s being spoken. For an example of an implementation that does this, see [Listing 2-2](Designing%20and%20Implementing%20an%20Application%20That%20Speaks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnbnknlto). The `NSSpeechSynthesizer` class also defines the `speechSynthesizer:willSpeakPhoneme` and `speechSynthesizer:didFinishSpeaking` delegate methods you can use to find out when a phoneme is about to be spoken and when an `NSSpeechSynthesizer` object has finished speaking, respectively. [Listing 2-2](Designing%20and%20Implementing%20an%20Application%20That%20Speaks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnbnknlto) includes an implementation of the `speechSynthesizer:didFinishSpeaking` delegate method that resets the cursor to the beginning of the line of text and re-enables buttons in the application window.

The Carbon speech synthesis API defines several callback function types you can use to create and install callback functions in a speech channel. For each event to which you want to respond, you create a callback function that adheres to the prototype defined by the callback pointer (see _[Speech Synthesis Manager Reference](https://developer.apple.com/documentation/applicationservices/speech_synthesis_manager)_ for these prototypes). Then, you install each callback function in a speech channel by passing the appropriate selector to the `SetSpeechInfo` function, as shown below:

```
// Install MyWordCallback callback function in the current speech channel
error = SetSpeechInfo(currentSpeechChannel, soWordCallBack, MyWordCallback);
```

When the Speech Synthesis Manager encounters one of the events handled by these callbacks, it calls the callback function you’ve installed, allowing you to synchronize custom processing with that speech event. The six callback function types defined in the Carbon speech synthesis API are listed below, each accompanied by the selector you use to install the callback function:

| Callback | Selector |
| --- | --- |
| `SpeechWordProcPtr` | `soWordCallBack` |
| `SpeechPhonemeProcPtr` | `soPhonemeCallBack` |
| `SpeechDoneProcPtr` | `soSpeechDoneCallBack` |
| `SpeechErrorProcPtr` | `soErrorCallBack` |
| `SpeechSyncProcPtr` | `soSyncCallBack` |
| `SpeechTextDoneProcPtr` | `soTextDoneCallBack` |

The `SpeechWordProcPtr`, `SpeechPhonemeProcPtr`, and `SpeechDoneProcPtr` callbacks are triggered by the same events as the `NSSpeechSynthesizer` delegate methods. Therefore, you can use these to perform custom processing when a word or phoneme is about to be spoken and when speaking has stopped. See [Listing 2-4](Designing%20and%20Implementing%20an%20Application%20That%20Speaks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnbnknlti) for an example usage of the `SpeechWordProcPtr` callback.

The Carbon speech synthesis API uses the `SpeechErrorProcPtr` pointer to call a speech channel’s error callback function when it encounters syntax errors in a text buffer’s embedded commands (see [Embedded Speech Command Errors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnjnknltcna) for a list of possible errors). In addition to helping you find such errors during application development, this callback allows you to display an alert or perform some other action if there are errors in the embedded commands users supply.

The `SpeechSyncProcPtr` defines a callback function you can implement to synchronize application-specific actions with the presence of the `sync` embedded speech command. When the Speech Synthesis Manager encounters a `sync` command in a string or buffer of text, it calls the callback function you’ve installed in the speech channel. You can use the parameter of the `sync` command to provide an arbitrary value that gets passed to your callback function, allowing you to distinguish among different usages of the command. Although you can use the `sync` command to trigger a callback when a word or phoneme is about to be spoken, it’s best to use the provided callback mechanisms for these events, reserving the `sync` command for application-defined events.

The `SpeechTextDoneProcPtr` defines a callback function that gets called when the Speech Synthesis Manager finishes processing a buffer of text. This can happen before the synthesizer finishes speaking the text or before the synthesizer even starts speaking the text. You might supply a callback function for this event if you want to be able to dispose of the original text buffer as soon as the Speech Synthesis Manager finishes copying it.

Just as it’s confusing to listen to more than one person talking at the same time, it’s confusing for users to hear more than one application speaking at the same time. With the popularity of VoiceOver and an increasing number of applications capable of producing speech, the potential for overlapping or interrupted speech is significant. This section explains how VoiceOver implements speech arbitration and describes ways you can avoid interrupting the spoken output of other applications and processes.

While VoiceOver is running, there is an automatic arbitration mechanism in place that causes all other spoken output to stop when VoiceOver starts to speak. Because VoiceOver provides the accessibility interface to OS X and visually impaired users rely on it to navigate and control the system, it is appropriate to give it priority over other types of spoken output.

While VoiceOver is not running, however, there is no arbitration mechanism in place. For this reason, it’s a good idea for your application to ascertain if another application or process is currently speaking before beginning to speak. Both the Carbon and Cocoa speech synthesis APIs provide a way to do this.

If you’re using the Cocoa `NSSpeechSynthesizer` class to produce spoken output, you can invoke the `isAnyApplicationSpeaking` class method to find out if another application or a system component (such as VoiceOver) is currently producing speech. This method returns a Boolean value your application can use to decide when it’s appropriate to speak. Depending on the needs of your application, you might use this method in the following way:

```
if ([NSSpeechSynthesizer isAnyApplicationSpeaking]) {
    // Wait.
} else {
    [_mySpeechSynthesizer startSpeakingString:myTextToSpeak];
}
```

If you’re using the Carbon speech synthesis API, you use a combination of two functions to determine whether any other application or system component is currently speaking. First, use the [SpeechBusySystemWide](https://developer.apple.com/documentation/applicationservices/1460113-speechbusysystemwide) function to get the total number of speech channels (including paused speech channels) that are currently synthesizing speech on the computer. This includes the speech channels the Speech Synthesis Manager automatically creates in response to the [SpeakString](https://developer.apple.com/documentation/applicationservices/1552250-speakstring) function and all speech channels your application is using. To find out if there are other applications or processes currently producing speech, therefore, you must subtract the speech channels your application is using from the number of speech channels you get from `SpeechBusySystemWide`. To get the total number of speech channels associated with your application, use the [SpeechBusy](https://developer.apple.com/documentation/applicationservices/1464581-speechbusy) function, as shown below:

```
short totalChannels, myTotalChannels;
totalChannels = SpeechBusySystemWide();
myTotalChannels = SpeechBusy();
if ((totalChannels - myTotalChannels) > 0) {
    // Wait.
} else {
    SpeakText(mySpeechChannel, myTextToSpeak, strlen(myTextToSpeak));
}
```


A synthesizer follows a predetermined set of rules about language production when it converts text to spoken output. But no matter how sophisticated and extensive those rules are, there will always be situations they don’t cover. As the developer, you know a lot more about how your application’s speech should sound than any synthesizer does, so you should take advantage of the available customization opportunities to produce the best possible spoken output.

If you’re viewing this document in Safari, Preview, or Xcode, you can listen to any example in this section by selecting it and then choosing Speech > Start Speaking Text from the Services menu item in the Application menu. If you’d like to experiment with the samples, one way to do this is to type or copy and paste them into a Text Edit window. After you’ve made adjustments and you want to listen to the result, select it and choose Speech > Start Speaking Text from the Services menu item in the Text Edit menu.

As described in [Opportunities for the Customization of Synthesized Speech](Speech%20Synthesis%20in%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqmznknltg), you can use embedded commands to adjust the pronunciation of words a synthesizer is likely to mispronounce, such as proper nouns. Another category of words a synthesizer may have difficulty with is words that are spelled the same but pronounced differently depending on semantic context. A common developer reaction to either of these situations is to deliberately misspell the word in an attempt to trick the synthesizer into pronouncing it correctly. Although this approach might work with a particular version of a synthesizer, it is ultimately unreliable. This is because future enhancements to a synthesizer can result in a more accurate pronunciation of the original word and an even worse pronunciation of the misspelled version. A much better approach is to represent the word phonemically and apply the appropriate prosodic controls.

Although you can select individual phonemes and create the phonemic representation of a word “by hand,” it’s usually more efficient to start with a synthesizer’s default phonemic representation and adjust it as necessary. This is because a synthesizer often mispronounces only one or two phonemes in a word, which means the remaining phonemes are accurate.

For example, the default pronunciation of the name “Matthias” places the stress on the first syllable and pronounces the first “a” the same as the “a” in the English word “father.“ (The phonemic representation of this pronunciation is `m1AAtIYIXs`.) To hear the default pronunciation, listen to the spoken version of the following sentence:

`My name is Matthias.`

If you wanted to change the pronunciation so that the stress is on the second syllable and the first “a“ sounds like the “a” in “about,” you would change the phonemic representation of the name to `mAXt1IYIXs`. To hear how this changes the synthesizer’s pronunciation, listen to the spoken version of the following sentence:

`My name is [[inpt PHON]]mAXt1IYIXs[[inpt TEXT]].`

Listening to speech is a mentally intensive process, whether the speech is produced by another person or generated by a synthesizer. For this reason, most human speakers naturally insert pauses into their speech to allow listeners enough time to absorb the content. Including pauses in the spoken output of an application is especially important, because the computer can’t adjust its delivery in response to verbal or nonverbal feedback from the listener.

Adding pauses to synthesized speech is primarily a matter of inserting units of silence at specific places in the text. You can do this in any of the following ways:

- Use appropriate punctuation within sentences. The correct use of commas, colons, and semicolons is as important for listeners as it is for readers.

  Listen to both versions of the sentence below:

  `Today I feel well yesterday I felt terrible.`

  `Today I feel well; yesterday I felt terrible.`

  The second version conveys the juxtaposition of the two states of the speaker’s condition much more clearly than the first version.
- Use short, declarative sentences when possible. Although complex sentences can be acceptable in text, they can be difficult to understand when spoken. The synthesizer automatically adds a noticeable pause between sentences, which helps users assimilate the information in one sentence before turning their attention to the next sentence. For this reason, an idea expressed in a couple of short sentences will include more silence than the same idea expressed in a single, long sentence.

  Listen to the following long sentence:

  `After you insert a section break, you can use the layout tool (located in the Tools menu) to format the new section, which can have different margins and numbers of columns than other sections in the document.`

  Although the synthesizer pauses briefly at the commas and the parentheses, the pauses that accompany the periods in the 3-sentence version of this information make it easier to absorb:

  `After you insert a section break, you can use the layout tool to format the new section. The layout tool is located in the Tools menu. Each section can have different margins and numbers of columns than other sections in the document.`
- Use the `slnc` (silence) embedded speech command. You can add an arbitrary amount of silence anywhere in the text by inserting the `[[slnc x]]` command (where `x` is a number of milliseconds).

  For example, inserting extra silence between the items in a list makes it easier for people to take note of each item. Listen to the following sentence, which lists four items, separated by commas:

  `Don't forget to bring your hat, sunglasses, sandals, and towel.`

  Now listen to the same sentence, with 400 milliseconds of silence inserted between the listed items, and notice that you hear each item more distinctly:

  `Don't forget to bring your hat, [[slnc 400]] sunglasses, [[slnc 400]] sandals, [[slnc 400]] and towel.`

Listen closely to people speaking and you’ll notice that they tend to emphasize the words in a sentence that carry new and important information and deemphasize less important and repetitive words. These differences in emphasis make it easier for listeners to recognize the important ideas in a sentence. Adding appropriate emphasis (or deemphasis) to words in your application’s speech can make the spoken output much easier for listeners to understand.

The following three sentences all follow the same pattern, but each provides different information. Without adjustments in emphasis, the sentences are very similar and it’s hard to focus on the differences in the times and the names.

`On May tenth, you have a meeting in Cupertino. On June tenth, you have a meeting in Tokyo. On July tenth, you have a meeting in Paris.`

Now listen to these three sentences with embedded commands that emphasize the important words and deemphasize the less-important, repetitive words:

`On May tenth, you have a meeting in Cupertino. On [[emph +]] June [[emph -]] tenth, you [[emph -]] have a [[emph -]] meeting in [[emph +]] Tokyo. On [[emph +]] July [[emph -]] tenth, you [[emph -]] have a [[emph -]] meeting in [[emph +]] Paris.`

People naturally express emotion in their speech to add other layers of meaning and to keep listeners engaged. Adding the illusion of emotion to synthesized speech is not as easy as inserting pauses and fine-tuning pronunciations, but you can achieve satisfactory results by carefully adjusting the pitch and timing of your spoken output.

For example, when people are sad or depressed, their speech is usually slower, more monotone, and often quieter than normal. Conversely, when people are happy or excited, their speech generally exhibits greater range in pitch and is often faster and louder than normal. You can use the TUNE format to approximate these qualities to give the impression of emotion to the speech your application generates.

For example, the default pronunciation of the sentence “Sorry, Dave, I can’t do that right now.“ is emotionally bland. To give listeners the impression that the speaker is perhaps a bit regretful, but nonetheless implacable, you might use the TUNE format to create the following utterance:

```
[[inpt TUNE]] ~ s {D 250; P 212.0:0 212.0:35 212.0:54 212.0:85 212.0:96} 1AA {D 190; P 232.0:0 218.0:35 222.0:80} r {D 80; P 216.0:0} IY {D 150; P 177.0:0 162.0:29 162.0:68 162.0:77 162.0:90 162.0:100} , {D 20} ~ d {D 60; P 162.0:0 162.0:36 162.0:57 160.0:93} 1EY {D 350; P 162.0:0 150.0:27 150.0:41 150.0:70} v {D 30; P 150.0:0 150.0:29 150.0:52 150.0:67 150.0:90 150.0:100} , {D 510} ~ 2AY {D 140; P 173.0:0 196.0:45} ~ k {D 100; P 196.0:0 196.0:95} AE {D 180; P 198.0:0 232.0:56} n {D 80; P 232.0:0} t {D 20; P 232.0:0 232.0:38} ~ d {D 40; P 232.0:0 232.0:85 208.0:92} 1UW {D 180; P 210.0:0 232.0:32 253.0:60 245.0:76} ~ D {D 60; P 245.0:0 186.0:92} AE {D 240; P 186.0:0 168.0:37} t {D 30; P 155.0:0 155.0:60 155.0:93} ~ r {D 70; P 155.0:0 149.0:53} 1AY {D 180; P 157.0:0 137.0:61} t {D 40; P 128.0:0 132.2:56 135.0:94} ~ n {D 80; P 129.0:0 153.0:31 147.0:94} 1AW {D 340; P 147.0:0 140.8:22 169.2:88 148.0:100} . {D 780} [[inpt TEXT]]
```

[Next](Syntax%20of%20Embedded%20Speech%20Commands.md)[Previous](Designing%20and%20Implementing%20an%20Application%20That%20Speaks.md)

